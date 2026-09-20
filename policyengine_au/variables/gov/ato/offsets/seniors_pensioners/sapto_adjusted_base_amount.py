"""SAPTO base rebate amount after any spouse transfer."""

from policyengine_au.model_api import *


class sapto_adjusted_base_amount(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "SAPTO base rebate amount after transfer"
    documentation = (
        "Base rebate amount adjusted for a transfer of a spouse's unused "
        "amount (Income Tax Assessment (1936 Act) Regulations 2025 "
        "reg 12(3)). Used for the amount of the offset under reg 11(2) and "
        "the rebate threshold, but not for entitlement under reg 10."
    )
    reference = "https://www.legislation.gov.au/F2025L01060/2025-09-09/2025-09-09/text/original/pdf"
    unit = AUD

    def formula(person, period, parameters):
        return (
            person("sapto_base_amount", period)
            + person("sapto_unused_transferred_in", period)
            - person("sapto_unused_transferred_out", period)
        )
