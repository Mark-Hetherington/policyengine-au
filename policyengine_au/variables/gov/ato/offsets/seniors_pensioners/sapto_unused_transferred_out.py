"""Unused SAPTO transferred out to a spouse."""

from policyengine_au.model_api import *


class sapto_unused_transferred_out(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Unused SAPTO transferred out to a spouse"
    documentation = (
        "Amount removed from this person's base rebate amount because it "
        "transfers to their spouse (Income Tax Assessment (1936 Act) "
        "Regulations 2025 reg 12(3)(a)). Read literally, reg 12(3)(a) "
        "removes the whole excess of the base amount over tax payable, even "
        "where reg 12(3)(b)(ii) passes a smaller amount (or nil) to the "
        "spouse. This subtracts the amount the spouse actually receives, "
        "which is what the ATO's SAPTO calculator reports. Either reading "
        "leaves tax payable unchanged, because the amount removed is one "
        "the person's own tax could not absorb."
    )
    reference = "https://www.legislation.gov.au/F2025L01060/2025-09-09/2025-09-09/text/original/pdf"
    unit = AUD

    def formula(person, period, parameters):
        in_couple = person.has_role(TaxUnit.PRIMARY) | person.has_role(TaxUnit.SPOUSE)
        received = person("sapto_unused_transferred_in", period) * in_couple
        return person.tax_unit.sum(received) - received
