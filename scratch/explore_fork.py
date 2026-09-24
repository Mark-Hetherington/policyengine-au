"""
M1 reconnaissance: what does policyengine-au actually implement?

Run this inside the fork, before writing any tests:

    uv run python scratch/explore_fork.py

It answers three questions:
  1. Does the package import and simulate at all?
  2. Which variables exist, and which of the ones we need are missing?
  3. For a household like ours, what numbers does it produce?

Nothing here is a test. It is a survey. The numbers it prints are only
meaningful once checked against the ATO and Services Australia calculators,
which is the actual M1 work.

NOTE: the API surface below is taken from the project's README. If imports
fail, the README is stale — read policyengine_au/__init__.py and fix these
calls, then update SPEC.md §4.3 with what is really there.
"""

from __future__ import annotations

YEAR = "2026"

WANTED = [
    # the ones the projection engine depends on
    "income_tax",
    "medicare_levy",
    "medicare_levy_surcharge",
    "taxable_income",
    "employment_income",
    "superannuation_guarantee",
    "concessional_contributions",
    "concessional_contributions_cap",
    "superannuation_contributions_tax",
    "division_293_tax",
    "age_pension",
    "age_pension_assets_test",
    "age_pension_income_test",
    "hecs_help_repayment",
    "capital_gains_tax",  # expected missing — roadmap says "coming soon"
    "franking_credits",  # expected missing
    "low_income_tax_offset",
]


def main() -> None:
    from policyengine_au import AustralianTaxBenefitSystem
    from policyengine_core.simulations import Simulation

    system = AustralianTaxBenefitSystem()

    # ---- 1. what exists -------------------------------------------------
    available = set(system.variables)
    print(f"{len(available)} variables in the system\n")

    print("wanted variables:")
    for name in WANTED:
        mark = "ok     " if name in available else "MISSING"
        print(f"  {mark}  {name}")

    print("\nanything with 'super' or 'pension' in the name:")
    for name in sorted(available):
        if "super" in name or "pension" in name:
            print(f"  {name}")

    # ---- 2. does it compute --------------------------------------------
    situation = {
        "people": {
            "adult_1": {"age": {YEAR: 44}, "employment_income": {YEAR: 110_000}},
            "adult_2": {"age": {YEAR: 42}, "employment_income": {YEAR: 63_000}},
        },
        "households": {
            "household": {"members": ["adult_1", "adult_2"]},
        },
    }

    sim = Simulation(tax_benefit_system=system, situation=situation)

    print(f"\nresults for {YEAR}:")
    for name in WANTED:
        if name not in available:
            continue
        try:
            value = sim.calculate(name, YEAR)
        except Exception as exc:  # noqa: BLE001 - surveying, not handling
            print(f"  {name}: raised {type(exc).__name__}: {exc}")
            continue
        print(f"  {name}: {value}")

    # ---- 3. how slow is it ---------------------------------------------
    import time

    start = time.perf_counter()
    for _ in range(10):
        Simulation(tax_benefit_system=system, situation=situation).calculate(
            "income_tax", YEAR
        )
    elapsed = (time.perf_counter() - start) / 10
    print(f"\n~{elapsed * 1000:.0f} ms per simulation")
    print(
        f"a 46-year projection would cost ~{elapsed * 46:.1f}s uncached "
        "— see SPEC.md §4.3 on memoisation"
    )

    # ---- 4. parameter horizon ------------------------------------------
    # SPEC.md §10: how far forward do parameters actually go?
    print("\nparameter horizon — check a few key ones by hand, e.g.:")
    print("  system.parameters.tax.income_tax.rates")
    print("  (look at the latest date in the YAML under policyengine_au/parameters/)")


if __name__ == "__main__":
    main()
