"""Non-refundable income tax offsets."""

from policyengine_au.model_api import *


class income_tax_offsets(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Income tax offsets"
    documentation = (
        "Non-refundable tax offsets, which reduce basic income tax "
        "liability but not below zero and not the Medicare levy."
    )
    reference = "https://www.legislation.gov.au/C2004A05138/2026-07-01/2026-07-01/text/original/pdf/1"
    unit = AUD
    adds = [
        "low_income_tax_offset",
        "seniors_and_pensioners_tax_offset",
    ]
