"""Capital gains not eligible for the CGT discount."""

from policyengine_au.model_api import *


class other_capital_gains(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Other capital gains"
    documentation = (
        "Gross capital gains on assets held too briefly to qualify for "
        "the CGT discount. An input, like discount_capital_gains."
    )
    reference = "https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/cgt-discount"
    unit = AUD
    default_value = 0
