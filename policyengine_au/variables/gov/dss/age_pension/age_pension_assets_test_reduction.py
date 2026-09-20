"""Age Pension reduction under the assets test."""

from policyengine_au.model_api import *

FORTNIGHTS_PER_YEAR = 26


class age_pension_assets_test_reduction(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Age Pension assets test reduction"
    documentation = (
        "Yearly reduction in this person's Age Pension under the assets "
        "test. Assets above the free area are rounded down to a multiple "
        "of $250 (Social Security Act 1991 s 1064 point 1064-G7) and "
        "reduce the pension by $3 per fortnight per $1,000, halved for "
        "each member of a couple."
    )
    reference = "https://www.servicesaustralia.gov.au/assets-test-for-age-pension"
    unit = AUD

    def formula(person, period, parameters):
        p = parameters(period).gov.dss.age_pension.assets_test
        benefit_unit = person.benefit_unit
        is_adult = benefit_unit.members.has_role(BenefitUnit.ADULT)
        assets = benefit_unit.sum(
            (
                benefit_unit.members("financial_assets", period)
                + benefit_unit.members("non_financial_assets", period)
            )
            * is_adult
        )
        partnered = person("is_pension_partnered", period)
        homeowner = benefit_unit.any(
            benefit_unit.members("is_homeowner", period) * is_adult
        )
        free_area = where(
            partnered,
            where(
                homeowner,
                p.free_area.couple_combined.homeowner,
                p.free_area.couple_combined.non_homeowner,
            ),
            where(
                homeowner,
                p.free_area.single.homeowner,
                p.free_area.single.non_homeowner,
            ),
        )
        excess = max_(assets - free_area, 0)
        increments = np.floor(excess / p.taper_increment)
        reduction = increments * p.taper_increment / 1_000 * p.taper_rate
        # Each member of a couple bears half the reduction.
        reduction = where(partnered, reduction / 2, reduction)
        return reduction * FORTNIGHTS_PER_YEAR
