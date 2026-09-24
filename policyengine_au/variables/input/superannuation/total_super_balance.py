"""Total superannuation balance."""

from policyengine_au.model_api import *


class total_super_balance(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Total superannuation balance"
    documentation = (
        "The sum of a person's superannuation interests, used by the "
        "contribution caps and by Division 296. An input, so a caller "
        "holding the balances passes the total. Limited recourse "
        "borrowing amounts, which are disregarded for Division 296, are "
        "not modelled."
    )
    reference = "https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/super/growing-your-super/caps-limits-and-tax-on-super-contributions/total-superannuation-balance"
    unit = AUD
    default_value = 0
