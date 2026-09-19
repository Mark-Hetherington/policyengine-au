"""Seniors and pensioners tax offset base rebate amount."""

from policyengine_au.model_api import *


class sapto_base_amount(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "SAPTO base rebate amount"
    documentation = (
        "Maximum seniors and pensioners tax offset for the person's class: "
        "single, partnered or illness separated (regulation 9(2)). The "
        "transfer of a spouse's unused amount (regulation 12) is not yet "
        "modelled."
    )
    reference = "https://www.legislation.gov.au/F2025L01060/2025-09-09/2025-09-09/text/original/pdf"
    unit = AUD

    def formula(person, period, parameters):
        p = parameters(period).gov.ato.offsets.seniors_pensioners.base_amount
        return select(
            [
                person("is_illness_separated_couple", period),
                person("is_partnered", period),
            ],
            [p.illness_separated, p.partnered],
            default=p.single,
        )
