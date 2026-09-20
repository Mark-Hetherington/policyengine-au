"""Deemed income from financial assets."""

from policyengine_au.model_api import *


class age_pension_deemed_income(Variable):
    value_type = float
    entity = BenefitUnit
    definition_period = YEAR
    label = "Deemed income from financial assets"
    documentation = (
        "Income the Age Pension income test attributes to financial "
        "assets, at the lower rate up to the deeming threshold and the "
        "upper rate above it. Assessed on the couple's combined financial "
        "assets where the person is partnered."
    )
    reference = "https://www.servicesaustralia.gov.au/deeming?context=22526"
    unit = AUD

    def formula(benefit_unit, period, parameters):
        p = parameters(period).gov.dss.age_pension.income_test.deeming
        adults = benefit_unit.members("financial_assets", period) * (
            benefit_unit.members.has_role(BenefitUnit.ADULT)
        )
        assets = benefit_unit.sum(adults)
        partnered = benefit_unit.any(
            benefit_unit.members("is_pension_partnered", period)
        )
        threshold = where(partnered, p.threshold.couple_combined, p.threshold.single)
        lower = min_(assets, threshold)
        upper = max_(assets - threshold, 0)
        return lower * p.lower_rate + upper * p.upper_rate
