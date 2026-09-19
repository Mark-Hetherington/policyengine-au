"""Whether a person has a spouse."""

from policyengine_au.model_api import *


class is_partnered(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Has a spouse"
    documentation = (
        "Whether the person is the primary taxpayer or spouse in a tax unit "
        "that has a member in the spouse role. Couples must be given a tax "
        "unit with explicit roles: by default every person is placed in one "
        "tax unit as a primary taxpayer, which reads as nobody partnered."
    )
    reference = "https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/seniors-and-pensioners-tax-offset"

    def formula(person, period, parameters):
        is_head_or_spouse = person.has_role(TaxUnit.PRIMARY) | person.has_role(
            TaxUnit.SPOUSE
        )
        tax_unit_has_spouse = person.tax_unit.any(person.has_role(TaxUnit.SPOUSE))
        return is_head_or_spouse & tax_unit_has_spouse
