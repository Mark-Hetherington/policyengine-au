"""Franked dividends received."""

from policyengine_au.model_api import *


class franked_dividend_income(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Franked dividend income"
    documentation = (
        "The cash amount of franked distributions received, directly or "
        "through a trust. This is a component of investment income rather "
        "than an addition to it: include it there as well, because the "
        "cash is assessable either way. Only the franking credit is added "
        "on top."
    )
    reference = "https://www.legislation.gov.au/C2004A05138/2026-07-01/2026-07-01/text/original/pdf/5"
    unit = AUD
    default_value = 0
