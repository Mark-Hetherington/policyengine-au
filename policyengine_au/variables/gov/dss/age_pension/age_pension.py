"""Age Pension."""

from policyengine_au.model_api import *


class age_pension(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Age Pension"
    documentation = (
        "Yearly Age Pension: the maximum rate less the larger of the "
        "income test and assets test reductions, not below zero. Paid only "
        "to a person who qualifies on age and residence."
    )
    reference = "https://www.servicesaustralia.gov.au/how-much-age-pension-you-can-get"
    unit = AUD

    def formula(person, period, parameters):
        maximum = person("age_pension_maximum_rate", period)
        income_test = person("age_pension_income_test_reduction", period)
        assets_test = person("age_pension_assets_test_reduction", period)
        entitlement = max_(maximum - max_(income_test, assets_test), 0)
        return entitlement * person("age_pension_eligible", period)
