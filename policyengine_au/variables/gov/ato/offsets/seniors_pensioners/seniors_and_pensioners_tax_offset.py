"""Seniors and pensioners tax offset."""

from policyengine_au.model_api import *


class seniors_and_pensioners_tax_offset(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Seniors and pensioners tax offset"
    documentation = (
        "The base rebate amount, reduced by 12.5 cents for each dollar of "
        "rebate income above the rebate threshold (regulation 11), rounded "
        "up to the whole dollar as the ATO does. Non-refundable."
    )
    reference = "https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/seniors-and-pensioners-tax-offset"
    unit = AUD
    defined_for = "sapto_eligible"

    def formula(person, period, parameters):
        p = parameters(period).gov.ato.offsets.seniors_pensioners
        base = person("sapto_base_amount", period)
        threshold = person("sapto_rebate_threshold", period)
        excess = max_(person("rebate_income", period) - threshold, 0)
        offset = max_(base - excess * p.reduction_rate, 0)
        return round_up_to_dollar(offset)
