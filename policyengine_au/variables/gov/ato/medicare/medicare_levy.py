"""Medicare levy calculation."""

from policyengine_au.model_api import *


class medicare_levy(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Medicare levy"
    documentation = (
        "Medicare levy on taxable income, with the low income reduction for "
        "individuals (Medicare Levy Act 1986 s 7). The family income "
        "reduction (s 8) and the thresholds for people entitled to the "
        "seniors and pensioners tax offset are not yet modelled."
    )
    reference = "https://www.legislation.gov.au/C2004A03351/latest"
    unit = AUD

    def formula(person, period, parameters):
        taxable_income = person("taxable_income", period)
        p = parameters(period).gov.ato.medicare
        thresholds = p.low_income_thresholds.singles
        full_levy = taxable_income * p.levy_rate
        excess = max_(taxable_income - thresholds.no_levy_threshold, 0)
        phase_in_levy = min_(full_levy, excess * p.phase_in_rate)
        return where(
            taxable_income <= thresholds.full_levy_threshold,
            phase_in_levy,
            full_levy,
        )
