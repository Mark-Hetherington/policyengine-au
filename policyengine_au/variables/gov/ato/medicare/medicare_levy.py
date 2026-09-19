"""Medicare levy calculation."""

from policyengine_au.model_api import *


class medicare_levy(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Medicare levy"
    documentation = (
        "Medicare levy on taxable income, with the low income reduction for "
        "individuals (Medicare Levy Act 1986 s 7), using the higher "
        "thresholds for a person entitled to the seniors and pensioners tax "
        "offset (s 3(1)). The ATO requires at least $1 of that offset. The "
        "family income reduction (s 8) is not yet modelled."
    )
    reference = "https://www.legislation.gov.au/C2004A03351/latest"
    unit = AUD

    def formula(person, period, parameters):
        taxable_income = person("taxable_income", period)
        p = parameters(period).gov.ato.medicare
        thresholds = p.low_income_thresholds
        gets_sapto = person("seniors_and_pensioners_tax_offset", period) > 0
        lower = where(
            gets_sapto,
            thresholds.seniors_pensioners.no_levy_threshold,
            thresholds.singles.no_levy_threshold,
        )
        upper = where(
            gets_sapto,
            thresholds.seniors_pensioners.full_levy_threshold,
            thresholds.singles.full_levy_threshold,
        )
        full_levy = taxable_income * p.levy_rate
        excess = max_(taxable_income - lower, 0)
        phase_in_levy = min_(full_levy, excess * p.phase_in_rate)
        return where(taxable_income <= upper, phase_in_levy, full_levy)
