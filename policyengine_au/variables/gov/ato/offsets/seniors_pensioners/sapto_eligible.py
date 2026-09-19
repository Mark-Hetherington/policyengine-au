"""Seniors and pensioners tax offset eligibility."""

from policyengine_au.model_api import *


class sapto_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eligible for the seniors and pensioners tax offset"
    documentation = (
        "Qualified for the Age Pension (Income Tax Assessment Act 1936 "
        "s 160AAAA(2)(b)), and rebate income below the cut-out amount in "
        "regulation 10 (s 160AAAA(3)). For a person with a spouse, the "
        "income tested is half the couple's combined rebate income "
        "(s 160AAAA(4)). Qualification through other pensions, allowances "
        "or veterans' entitlements is not modelled."
    )
    reference = "https://www.legislation.gov.au/C1936A00027/2026-07-01/2026-07-01/text/original/pdf/3"

    def formula(person, period, parameters):
        p = parameters(period).gov.ato.offsets.seniors_pensioners
        base = person("sapto_base_amount", period)
        threshold = person("sapto_rebate_threshold", period)
        # Regulation 10: rounded up to the nearest whole dollar.
        cut_out = round_up_to_dollar(base / p.reduction_rate + threshold)
        own_income = person("rebate_income", period)
        is_partnered = person("is_partnered", period)
        is_head_or_spouse = person.has_role(TaxUnit.PRIMARY) | person.has_role(
            TaxUnit.SPOUSE
        )
        couple_income = person.tax_unit.sum(own_income * is_head_or_spouse)
        tested_income = where(is_partnered, couple_income / 2, own_income)
        qualified = person("age_pension_eligible", period)
        return qualified & (tested_income < cut_out)
