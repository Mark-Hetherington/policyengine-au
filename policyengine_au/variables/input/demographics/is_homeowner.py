"""Home ownership."""

from policyengine_au.model_api import *


class is_homeowner(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Homeowner"
    documentation = (
        "Whether the person owns the home they live in, which sets the "
        "assets test free area. A couple counts as homeowners if either "
        "partner owns the home (Social Security Act 1991 s 1064 point "
        "1064-G3, Table G-1 column 3A)."
    )
    reference = "https://www.servicesaustralia.gov.au/assets-test-for-age-pension"
    default_value = False
