"""Superannuation earnings for Division 296."""

from policyengine_au.model_api import *


class superannuation_earnings(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Superannuation earnings for Division 296"
    documentation = (
        "The relevant super earnings a fund reports for the member. An "
        "input: an APRA regulated fund calculates and reports this, so "
        "there is nothing here to derive it from. Negative earnings are "
        "allowed and produce no tax; carrying a loss forward to a later "
        "year is not modelled."
    )
    reference = "https://www.ato.gov.au/tax-and-super-professionals/for-superannuation-professionals/apra-regulated-funds/managing-member-benefits/taxation-of-member-super-benefits/about-division-296-tax-for-apra-funds"
    unit = AUD
    default_value = 0
