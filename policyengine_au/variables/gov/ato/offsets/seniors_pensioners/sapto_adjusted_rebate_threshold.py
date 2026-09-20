"""SAPTO rebate threshold after any spouse transfer."""

from policyengine_au.model_api import *

from policyengine_au.variables.gov.ato.offsets.seniors_pensioners.sapto_rebate_threshold import (
    rebate_threshold,
)


class sapto_adjusted_rebate_threshold(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "SAPTO rebate threshold after transfer"
    documentation = (
        "Rebate threshold worked out from the base rebate amount after any "
        "spouse transfer: transferring an amount also moves the threshold "
        "(note to Income Tax Assessment (1936 Act) Regulations 2025 "
        "reg 12(3))."
    )
    reference = "https://www.legislation.gov.au/F2025L01060/2025-09-09/2025-09-09/text/original/pdf"
    unit = AUD

    def formula(person, period, parameters):
        base = person("sapto_adjusted_base_amount", period)
        return rebate_threshold(base, parameters(period))
