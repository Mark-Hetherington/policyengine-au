"""Membership of a couple for Age Pension purposes."""

from policyengine_au.model_api import *


class is_pension_partnered(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Member of a couple for Age Pension"
    documentation = (
        "Whether the person is a member of a couple, which sets the "
        "payment rate and the means test free areas. Read from the benefit "
        "unit, which must be given explicitly with two adults: by default "
        "policyengine-core places every person in one benefit unit as an "
        "adult, so a household of three would read as partnered."
    )
    reference = "https://www.servicesaustralia.gov.au/how-much-age-pension-you-can-get"

    def formula(person, period, parameters):
        adults = person.benefit_unit.sum(person.has_role(BenefitUnit.ADULT))
        return person.has_role(BenefitUnit.ADULT) & (adults > 1)
