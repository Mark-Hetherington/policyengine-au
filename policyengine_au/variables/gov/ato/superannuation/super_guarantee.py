"""Superannuation guarantee."""

from policyengine_au.model_api import *


class super_guarantee(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Superannuation guarantee"
    documentation = (
        "Minimum employer contribution: the super guarantee rate applied "
        "to employment income, capped at the maximum contribution base. "
        "Before 1 July 2026 that base was quarterly, so this is the annual "
        "equivalent for even earnings."
    )
    reference = "https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/super-guarantee"
    unit = AUD

    def formula(person, period, parameters):
        p = parameters(period).gov.ato.superannuation.contribution_rates
        earnings = person("employment_income", period)
        capped = min_(earnings, p.maximum_contribution_base)
        return capped * p.super_guarantee_rate
