"""Age Pension reduction under the income test."""

from policyengine_au.model_api import *

FORTNIGHTS_PER_YEAR = 26


class age_pension_income_test_reduction(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Age Pension income test reduction"
    documentation = (
        "Yearly reduction in this person's Age Pension under the income "
        "test: 50 cents per dollar above the free area for a single "
        "person, or 25 cents per dollar of the couple's combined income "
        "above the couple free area for each partner."
    )
    reference = "https://www.servicesaustralia.gov.au/income-test-for-age-pension"
    unit = AUD

    def formula(person, period, parameters):
        p = parameters(period).gov.dss.age_pension.income_test
        income = person.benefit_unit("age_pension_assessable_income", period)
        fortnightly_income = income / FORTNIGHTS_PER_YEAR
        partnered = person("is_pension_partnered", period)
        free_area = where(partnered, p.free_area.couple_combined, p.free_area.single)
        taper = where(partnered, p.taper_rate.partnered, p.taper_rate.single)
        excess = max_(fortnightly_income - free_area, 0)
        return excess * taper * FORTNIGHTS_PER_YEAR
