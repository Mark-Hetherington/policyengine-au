"""Income tax payable after offsets."""

from policyengine_au.model_api import *


class income_tax_payable(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Income tax payable"
    documentation = (
        "Basic income tax liability less non-refundable tax offsets, not "
        "below zero (Income Tax Assessment Act 1997 s 4-10(3)). Excludes "
        "the Medicare levy."
    )
    reference = "https://www.legislation.gov.au/C2004A05138/2026-07-01/2026-07-01/text/original/pdf/1"
    unit = AUD

    def formula(person, period, parameters):
        income_tax = person("income_tax", period)
        offsets = person("income_tax_offsets", period)
        return max_(income_tax - offsets, 0)
