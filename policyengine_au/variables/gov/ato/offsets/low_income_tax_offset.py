"""Low income tax offset."""

from policyengine_au.model_api import *


class low_income_tax_offset(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Low income tax offset"
    documentation = (
        "Non-refundable offset for residents with taxable income up to "
        "$66,667 (Income Tax Assessment Act 1997 ss 61-110, 61-115). "
        "Assumes Australian residence; the cap for people under 18 with "
        "excluded income is not modelled."
    )
    reference = "https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/low-income-tax-offset"
    unit = AUD

    def formula(person, period, parameters):
        taxable_income = person("taxable_income", period)
        p = parameters(period).gov.ato.offsets.low_income
        return max_(p.maximum - p.reduction.calc(taxable_income), 0)
