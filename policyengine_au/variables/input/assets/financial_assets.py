"""Financial assets."""

from policyengine_au.model_api import *


class financial_assets(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Financial assets"
    documentation = (
        "Financial investments subject to deeming: bank accounts, shares, "
        "managed funds and account based superannuation pensions. Counted "
        "in the Age Pension assets test as well as deemed for the income "
        "test."
    )
    reference = "https://www.servicesaustralia.gov.au/deeming?context=22526"
    unit = AUD
    default_value = 0
