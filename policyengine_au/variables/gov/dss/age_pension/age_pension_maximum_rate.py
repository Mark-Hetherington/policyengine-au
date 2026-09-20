"""Maximum Age Pension rate."""

from policyengine_au.model_api import *

FORTNIGHTS_PER_YEAR = 26


class age_pension_maximum_rate(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Age Pension maximum rate"
    documentation = (
        "Maximum yearly Age Pension before the income and assets tests: "
        "the basic rate, pension supplement and energy supplement for the "
        "person's situation, over 26 fortnights. Rent Assistance, remote "
        "area allowance and transitional rates are not modelled."
    )
    reference = "https://www.servicesaustralia.gov.au/how-much-age-pension-you-can-get"
    unit = AUD

    def formula(person, period, parameters):
        p = parameters(period).gov.dss.age_pension.payment_rates
        illness_separated = person("is_illness_separated_couple", period)
        partnered = person("is_pension_partnered", period)

        def total(rates):
            return rates.basic_rate + rates.pension_supplement + rates.energy_supplement

        fortnightly = select(
            [illness_separated, partnered],
            [total(p.illness_separated), total(p.partnered)],
            default=total(p.single),
        )
        return fortnightly * FORTNIGHTS_PER_YEAR
