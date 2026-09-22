"""Division 293 tax."""

from policyengine_au.model_api import *


class division_293_tax(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Division 293 tax"
    documentation = (
        "Extra 15% on concessional contributions for high income earners, "
        "charged on the lesser of the contributions and the amount by "
        "which income plus those contributions exceeds the threshold. "
        "Income here is taxable income; the other components of income for "
        "surcharge purposes are not modelled."
    )
    reference = "https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/division-293-tax"
    unit = AUD

    def formula(person, period, parameters):
        p = parameters(period).gov.ato.superannuation.contribution_rates
        contributions = person("concessional_contributions", period)
        income = person("taxable_income", period) + contributions
        excess = max_(income - p.division_293.threshold, 0)
        return min_(excess, contributions) * p.division_293.rate
