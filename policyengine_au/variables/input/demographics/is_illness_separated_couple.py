"""Illness separated couple status."""

from policyengine_au.model_api import *


class is_illness_separated_couple(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Member of an illness separated couple"
    documentation = (
        "Whether the person is a member of an illness separated couple, "
        "within the meaning of the Social Security Act 1991: partners "
        "living apart because of an indefinitely continuing illness or "
        "infirmity, such as one partner being in a nursing home."
    )
    reference = "https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/seniors-and-pensioners-tax-offset"
    default_value = False
