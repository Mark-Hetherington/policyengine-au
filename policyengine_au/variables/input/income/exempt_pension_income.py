"""Exempt pension income."""

from policyengine_au.model_api import *


class exempt_pension_income(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Exempt pension income"
    documentation = (
        "Pension payments exempt from income tax under Subdivision 52-A or "
        "52-B of the Income Tax Assessment Act 1997: disability support "
        "pension, carer payment, and invalidity or partner service pension. "
        "Counted as income when working out the transfer of unused SAPTO "
        "(Income Tax Assessment (1936 Act) Regulations 2025 reg 12(5))."
    )
    reference = "https://www.legislation.gov.au/F2025L01060/2025-09-09/2025-09-09/text/original/pdf"
    unit = AUD
    default_value = 0
