"""Unused SAPTO transferred in from a spouse."""

from policyengine_au.model_api import *


class sapto_unused_transferred_in(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Unused SAPTO transferred in from a spouse"
    documentation = (
        "Amount added to this person's base rebate amount because their "
        "spouse cannot use all of theirs (Income Tax Assessment (1936 Act) "
        "Regulations 2025 reg 12). The spouse's base rebate amount must "
        "exceed their tax payable before offsets, both must be entitled to "
        "SAPTO, and this person's own offset must be below their base "
        "amount. Where the spouse's income exceeds $6,000, reg 12(3)(b)(ii) "
        "gives the amount; exempt pension income counts as income here "
        "(reg 12(5)). Assumes resident tax rates, as reg 12(4)(b) requires."
    )
    reference = "https://www.legislation.gov.au/F2025L01060/2025-09-09/2025-09-09/text/original/pdf"
    unit = AUD

    def formula(person, period, parameters):
        p = parameters(period).gov.ato
        scale = p.income_tax.rates
        transfer = p.offsets.seniors_pensioners.transfer

        in_couple = person.has_role(TaxUnit.PRIMARY) | person.has_role(TaxUnit.SPOUSE)

        def spouse_value(values):
            own = values * in_couple
            return person.tax_unit.sum(own) - own

        base = person("sapto_base_amount", period)
        eligible = person("sapto_eligible", period)
        # Regulation 12(5): exempt pensions count as income in this section.
        income = person("taxable_income", period) + person(
            "exempt_pension_income", period
        )
        # Regulation 12(1)(b): base amount above tax payable before offsets.
        unused = max_(base - scale.calc(income), 0)

        spouse_base = spouse_value(base)
        spouse_unused = spouse_value(unused)
        spouse_income = spouse_value(income)
        spouse_eligible = spouse_value(eligible) > 0

        # Regulation 12(3)(b)(ii), where reg 12(4) applies.
        formula_amount = max_(
            spouse_base - (spouse_income - transfer.income_floor) * transfer.rate,
            0,
        )
        amount = where(
            spouse_income > transfer.income_floor,
            formula_amount,
            spouse_unused,
        )
        transfers = (
            eligible
            & spouse_eligible
            & (spouse_unused > 0)
            # Regulation 12(1)(e).
            & (person("sapto_offset_before_transfer", period) < base)
        )
        return where(transfers, amount, 0)
