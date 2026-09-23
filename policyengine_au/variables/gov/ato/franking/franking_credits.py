"""Franking credits on franked distributions."""

from policyengine_au.model_api import *


class franking_credits(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Franking credits"
    documentation = (
        "Tax the company already paid on the profits behind a franked "
        "distribution, worked out from the cash amount and the company "
        "tax rate. Assumes distributions are fully franked at the general "
        "rate; partly franked dividends are modelled by scaling the cash "
        "amount passed in."
    )
    reference = "https://www.legislation.gov.au/C2004A05138/2026-07-01/2026-07-01/text/original/pdf/5"
    unit = AUD

    def formula(person, period, parameters):
        franked = person("franked_dividend_income", period)
        rate = parameters(period).gov.ato.company_tax.rate
        return franked * rate / (1 - rate)
