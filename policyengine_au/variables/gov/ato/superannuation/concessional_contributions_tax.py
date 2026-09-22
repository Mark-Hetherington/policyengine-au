"""Tax on concessional contributions."""

from policyengine_au.model_api import *


class concessional_contributions_tax(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Contributions tax"
    documentation = (
        "Tax the fund pays on concessional contributions, at 15%. Excess "
        "contributions above the cap, which are instead taxed at marginal "
        "rates with an offset, are not modelled."
    )
    reference = "https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/super/growing-your-super/tax-on-contributions"
    unit = AUD

    def formula(person, period, parameters):
        p = parameters(period).gov.ato.superannuation.contribution_rates
        contributions = person("concessional_contributions", period)
        return contributions * p.contributions_tax_rate
