# Tax Programs

This document provides comprehensive coverage of Australian tax programs modeled in PolicyEngine Australia.

## Personal Income Tax

### Tax Brackets and Rates

Australia uses a progressive income tax system. Resident rates:

| Taxable Income | 2024-25 and 2025-26 | 2026-27 |
|----------------|---------------------|---------|
| $0 - $18,200 | 0% | 0% |
| $18,201 - $45,000 | 16% | 15% |
| $45,001 - $135,000 | 30% | 30% |
| $135,001 - $190,000 | 37% | 37% |
| $190,001+ | 45% | 45% |

**Reference**: [ATO Tax rates – Australian residents](https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents)

### Implementation

The rates are a marginal rate scale, applied to taxable income with
`parameters(period).gov.ato.income_tax.rates.calc(taxable_income)`.

```yaml
# parameters/gov/ato/income_tax/rates.yaml
brackets:
  - threshold:
      values:
        2022-07-01: 18_200
    rate:
      values:
        2022-07-01: 0.19
        2024-07-01: 0.16
        2026-07-01: 0.15
  # ...
metadata:
  type: marginal_rate
  threshold_unit: currency-AUD
  rate_unit: /1
```

## Low Income Tax Offset

A non-refundable offset for residents, reducing income tax (not the Medicare
levy) to no lower than zero:

| Taxable Income | Offset |
|----------------|--------|
| $0 - $37,500 | $700 |
| $37,501 - $45,000 | $700 less 5% of the excess over $37,500 |
| $45,001 - $66,667 | $325 less 1.5% of the excess over $45,000 |

`income_tax_payable` is `income_tax` less `income_tax_offsets`, floored at
zero.

**Reference**: [ATO Low income tax offset](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/low-income-tax-offset)

## Medicare Levy

### Standard Levy
- **Rate**: 2% of taxable income
- **Purpose**: Funds Australia's public health system

### Low Income Thresholds (2024-25)
- **Singles**: No levy below $26,000; shade-in to $32,500
- **Families**: No levy below $43,846; additional $4,027 per child
- **Seniors/Pensioners**: Higher thresholds at $42,000/$52,500

### Medicare Levy Surcharge
Additional levy for high-income earners without private health insurance:

| Income (Singles) | Income (Families) | Surcharge Rate |
|-----------------|-------------------|----------------|
| < $97,000 | < $194,000 | 0% |
| $97,000 - $113,000 | $194,000 - $226,000 | 1.0% |
| $113,001 - $151,000 | $226,001 - $302,000 | 1.25% |
| > $151,000 | > $302,000 | 1.5% |

**Reference**: [Medicare Levy](https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/medicare-levy)

## HECS-HELP Student Loan Repayments

### Repayment Thresholds and Rates (2024-25)

HECS-HELP uses an income-contingent repayment system:

| Repayment Income | Repayment Rate |
|------------------|----------------|
| Below $54,435 | 0% |
| $54,435 - $62,850 | 1.0% |
| $62,851 - $66,620 | 2.0% |
| $66,621 - $70,618 | 2.5% |
| ... | ... |
| Above $159,663 | 10.0% |

**Features**:
- 18 income bands with progressive rates
- Repayments calculated on "repayment income" (taxable income + reportable fringe benefits + other amounts)
- Automatic withholding through PAYG system

**Reference**: [Study and Training Loan Repayment](https://www.ato.gov.au/individuals-and-families/study-and-training-support-loans)

## Superannuation

### Superannuation Guarantee
- **Current Rate**: 11.5% (2024-25)
- **Scheduled Increase**: 12% from July 2025
- **Minimum Income**: $450 per month threshold

### Contribution Caps (2024-25)
- **Concessional Cap**: $30,000 per year
- **Non-concessional Cap**: $120,000 per year
- **Contributions Tax**: 15% on concessional contributions

### Division 293 Tax
- **Threshold**: $250,000 combined income
- **Additional Tax**: 15% (total 30%) on super contributions for high earners

**Reference**: [Super Guarantee](https://www.ato.gov.au/employers/super-for-employers/super-guarantee-compliance-and-obligations)

## Goods and Services Tax (GST)

- **Standard Rate**: 10%
- **Exemptions**: Basic food, education, health, childcare
- **Input Tax Credits**: Available for businesses

*Note: GST modeling requires consumption data and is planned for future releases*

## State and Territory Taxes

### Payroll Tax
Varies by state, typically:
- **Rate**: 4.85% - 6.85%
- **Threshold**: $600,000 - $2,000,000 annual payroll

### Land Tax
Progressive rates based on land value:
- Exemptions for principal residence
- Varies significantly by state

### Stamp Duty
Transfer duty on property purchases:
- Progressive rates from 1.25% to 7%
- First home buyer concessions available

*Note: State taxes planned for implementation by jurisdiction*

## Implementation Status

### Currently Implemented
✅ Personal income tax (all brackets and rates)
✅ Medicare levy and surcharge
✅ HECS-HELP repayments
✅ Superannuation guarantee contributions

### Planned Implementation
⏳ Capital gains tax
⏳ Fringe benefits tax
⏳ GST with consumption modeling
⏳ State and territory taxes
⏳ Local government rates

## Testing

All tax calculations are validated against:
- ATO tax calculators
- Published tax tables
- Real-world scenarios
- Edge cases and boundary conditions

See `tests/policy/baseline/test_income_tax.yaml` for comprehensive test cases.