"""Taxable income calculation."""

from policyengine_au.model_api import *


class taxable_income(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Taxable income"
    documentation = "Total taxable income for income tax purposes"
    reference = "https://www.ato.gov.au/individuals-and-families/income-and-deductions/income-you-must-declare"
    unit = AUD

    def formula(person, period, parameters):
        employment = person("employment_income", period)
        self_employment = person("self_employment_income", period)
        investment = person("investment_income", period)
        rental = person("rental_income", period)

        # Age Pension is a taxable payment.
        age_pension = person("age_pension", period)
        # A franked distribution is assessed with the company tax already
        # paid on it added back (Income Tax Assessment Act 1997
        # s 207-20(1)). The cash itself arrives in investment income.
        franking_credits = person("franking_credits", period)
        # A net capital gain is assessable income (ITAA 1997 s 102-5),
        # after the discount on assets held twelve months or more.
        net_capital_gain = person("net_capital_gain", period)

        # Sum all income sources
        total_income = (
            employment
            + self_employment
            + investment
            + rental
            + age_pension
            + franking_credits
            + net_capital_gain
        )

        # Apply deductions (simplified for now)
        deductions = person("total_deductions", period)

        return max_(0, total_income - deductions)
