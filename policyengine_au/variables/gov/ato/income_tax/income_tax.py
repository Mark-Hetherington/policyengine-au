"""Income tax calculation for Australian residents."""

from policyengine_au.model_api import *


class income_tax(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Income tax"
    documentation = "Total income tax liability before offsets and credits"
    reference = (
        "https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents"
    )
    unit = AUD

    def formula(person, period, parameters):
        taxable_income = person("taxable_income", period)
        p = parameters(period).gov.ato.income_tax
        return p.rates.calc(taxable_income)
