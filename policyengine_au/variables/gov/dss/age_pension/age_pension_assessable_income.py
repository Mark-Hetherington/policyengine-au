"""Income assessed for the Age Pension income test."""

from policyengine_au.model_api import *

FORTNIGHTS_PER_YEAR = 26


class age_pension_assessable_income(Variable):
    value_type = float
    entity = BenefitUnit
    definition_period = YEAR
    label = "Age Pension assessable income"
    documentation = (
        "Deemed income from financial assets, plus employment income after "
        "the Work Bonus, plus self-employment and rental income, for the "
        "person and their partner. The Work Bonus is applied at its "
        "fortnightly amount only: the balance that accrues across "
        "fortnights is not modelled, so employment income that varies "
        "within a year is overstated."
    )
    reference = "https://www.servicesaustralia.gov.au/income-test-for-age-pension"
    unit = AUD

    def formula(benefit_unit, period, parameters):
        p = parameters(period).gov.dss.age_pension.income_test
        is_adult = benefit_unit.members.has_role(BenefitUnit.ADULT)
        work_bonus = p.work_bonus.fortnightly_amount * FORTNIGHTS_PER_YEAR
        employment = benefit_unit.members("employment_income", period)
        after_work_bonus = max_(employment - work_bonus, 0)
        other = benefit_unit.members(
            "self_employment_income", period
        ) + benefit_unit.members("rental_income", period)
        counted = (after_work_bonus + other) * is_adult
        return benefit_unit.sum(counted) + benefit_unit(
            "age_pension_deemed_income", period
        )
