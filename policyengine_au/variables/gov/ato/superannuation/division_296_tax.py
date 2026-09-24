"""Division 296 tax."""

from policyengine_au.model_api import *


class division_296_tax(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Division 296 tax"
    documentation = (
        "Additional tax on the share of superannuation earnings "
        "attributable to a total super balance above the large super "
        "balance threshold, and a further amount above the very large "
        "balance threshold. Applies from 2026-27. The share is the "
        "proportion of the balance that sits above each threshold, so a "
        "balance just over a threshold bears the rate on almost none of "
        "its earnings."
    )
    reference = "https://www.ato.gov.au/about-ato/new-legislation/in-detail/superannuation/better-targeted-superannuation-concessions"
    unit = AUD

    # No formula before commencement, so earlier years are nil
    # rather than an error about a parameter that did not exist.
    def formula_2026_07_01(person, period, parameters):
        p = parameters(period).gov.ato.superannuation.division_296
        balance = person("total_super_balance", period)
        earnings = person("superannuation_earnings", period)

        # A nil balance has no share above any threshold, and dividing by
        # it would be a nan rather than a zero.
        safe = where(balance > 0, balance, 1)
        above_large = max_(balance - p.large_balance_threshold, 0) / safe
        above_very_large = max_(balance - p.very_large_balance_threshold, 0) / safe

        # Only earnings are taxed, so a loss produces nothing rather than
        # a refund; the law carries it forward, which is not modelled.
        taxable = max_(earnings, 0)
        rate = p.rate * above_large + p.very_large_balance_rate * above_very_large
        return where(balance > 0, taxable * rate, 0)
