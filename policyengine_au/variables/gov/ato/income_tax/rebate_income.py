"""Rebate income."""

from policyengine_au.model_api import *


class rebate_income(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Rebate income"
    documentation = (
        "Taxable income plus reportable superannuation contributions, total "
        "net investment loss and adjusted fringe benefits total (Income Tax "
        "Assessment Act 1936 s 6(1)). Only taxable income is modelled so "
        "far; the other components are treated as nil."
    )
    reference = "https://www.legislation.gov.au/C1936A00027/2026-07-01/2026-07-01/text/original/pdf/1"
    unit = AUD

    def formula(person, period, parameters):
        return person("taxable_income", period)
