"""Net capital gain for the year."""

from policyengine_au.model_api import *


class net_capital_gain(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Net capital gain"
    documentation = (
        "The amount included in assessable income: gains on assets held "
        "twelve months or more, reduced by the discount, plus gains on "
        "assets held for less, in full. Capital losses, which are applied "
        "against gains before the discount and carried forward, are not "
        "modelled: a negative input is simply treated as nil."
    )
    reference = "https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/cgt-discount"
    unit = AUD

    def formula(person, period, parameters):
        p = parameters(period).gov.ato.capital_gains.discount
        discountable = max_(person("discount_capital_gains", period), 0)
        other = max_(person("other_capital_gains", period), 0)
        return discountable * (1 - p.individual) + other
