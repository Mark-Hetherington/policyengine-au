"""Non-financial assessable assets."""

from policyengine_au.model_api import *


class non_financial_assets(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Non-financial assessable assets"
    documentation = (
        "Assets counted in the Age Pension assets test that are not "
        "deemed: home contents, vehicles, investment property and similar. "
        "Excludes the principal home for a homeowner."
    )
    reference = "https://www.servicesaustralia.gov.au/asset-types?context=22526"
    unit = AUD
    default_value = 0
