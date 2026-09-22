"""Concessional superannuation contributions."""

from policyengine_au.model_api import *


class concessional_contributions(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Concessional superannuation contributions"
    documentation = (
        "Before-tax contributions for the year: employer super guarantee, "
        "salary sacrifice and personal contributions claimed as a "
        "deduction. An input, so a caller that works out contributions "
        "itself can pass the total. Excess contributions above the cap are "
        "not modelled."
    )
    reference = "https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/contributions-caps"
    unit = AUD
    default_value = 0
