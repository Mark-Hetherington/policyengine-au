"""Capital gains eligible for the CGT discount."""

from policyengine_au.model_api import *


class discount_capital_gains(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Discount capital gains"
    documentation = (
        "Gross capital gains on assets held long enough to qualify for "
        "the CGT discount, before the discount is applied. An input: "
        "which parcels were sold, and when they were acquired, is the "
        "caller's business."
    )
    reference = "https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/cgt-discount"
    unit = AUD
    default_value = 0
