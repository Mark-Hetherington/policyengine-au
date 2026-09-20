"""Seniors and pensioners tax offset rebate threshold."""

from policyengine_au.model_api import *


def rebate_threshold(base, parameters_at_period):
    """Rebate threshold for a base rebate amount (regulation 9(4)-(8))."""
    gov = parameters_at_period.gov.ato
    p = gov.offsets.seniors_pensioners.rebate_threshold
    scale = gov.income_tax.rates
    # The tax-free threshold is where the first positive rate starts.
    tax_free_threshold = scale.thresholds[1]
    lowest_rate = scale.rates[1]
    second_lowest_rate = scale.rates[2]
    # Regulation 9(5).
    threshold = (base + p.rebate_maximum_amount) / lowest_rate + tax_free_threshold
    # Regulation 9(6)-(7), when the 9(5) amount exceeds the rebate reduction
    # threshold.
    adjustment = p.rebate_reduction_threshold * (
        p.rebate_reduction_rate + second_lowest_rate - lowest_rate
    )
    high_threshold = (
        lowest_rate * tax_free_threshold + p.rebate_maximum_amount + base + adjustment
    ) / (p.rebate_reduction_rate + second_lowest_rate)
    threshold = where(
        threshold > p.rebate_reduction_threshold, high_threshold, threshold
    )
    # Regulation 9(8): round up to the nearest whole dollar.
    return round_up_to_dollar(threshold)


class sapto_rebate_threshold(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "SAPTO rebate threshold"
    documentation = (
        "Rebate income above which the seniors and pensioners tax offset "
        "shades out (regulation 9(4)-(8)). Derived from the base rebate "
        "amount and the income tax scale, so it moves when the lowest "
        "marginal rate or tax-free threshold changes."
    )
    reference = "https://www.legislation.gov.au/F2025L01060/2025-09-09/2025-09-09/text/original/pdf"
    unit = AUD

    def formula(person, period, parameters):
        base = person("sapto_base_amount", period)
        return rebate_threshold(base, parameters(period))
