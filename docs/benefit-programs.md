# Benefit Programs

Comprehensive documentation of Australian social security and family assistance programs.

## Age Pension

### Eligibility
- **Age**: 67 years (born on or after 1 January 1957)
- **Residence**: 10 years Australian residence, including 5 continuous years. Assumed met; not yet modelled.

### Payment Rates (from 20 September 2026)

| Category | Basic Rate | Pension Supplement | Energy Supplement | Total (fortnight) |
|----------|------------|-------------------|-------------------|-------------------|
| Single | $1,135.40 | $88.20 | $14.10 | $1,237.70 |
| Couple (each) | $855.90 | $66.50 | $10.60 | $933.00 |
| Couple apart, ill health (each) | $1,135.40 | $88.20 | $14.10 | $1,237.70 |

Rates index every 20 March and 20 September; parameters carry each step back to
March 2022. Yearly amounts are 26 fortnights.

### Means Testing

The pension is the maximum rate less the larger of the two reductions.

#### Income Test (from 20 September 2026)
- **Free Area**: $226/fortnight (single), $396/fortnight (couple combined)
- **Taper Rate**: 50c per dollar for a single person; 25c per dollar of combined
  income for each member of a couple
- **Deeming**: 1.75% up to $66,800 (single) or $110,600 (couple combined), then
  3.75%. Rates were frozen at 0.25%/2.25% until 19 September 2025 and are
  returning to market levels in steps.
- **Work Bonus**: first $300/fortnight of employment income disregarded. The
  balance that accrues across fortnights (up to $11,800) is not modelled.

#### Assets Test (from 1 July 2026)

| Category | Homeowner | Non-homeowner |
|----------|-----------|---------------|
| Single - Free area | $333,000 | $600,000 |
| Couple - Free area (combined) | $499,000 | $766,000 |

Assets above the free area reduce the pension by $3 per fortnight per $1,000,
halved for each member of a couple, after rounding the excess down to a
multiple of $250. Cut-off points are derived rather than stored.

### Not modelled

Transitional rates, Rent Assistance, remote area allowance, blind pensioners,
couples where only one partner is eligible, and the residence rules.

## JobSeeker Payment

### Payment Rates (September 2024)

| Category | Rate (fortnight) |
|----------|------------------|
| Single, no children | $762.70 |
| Single, with dependent children | $824.60 |
| Single, principal carer | $1,015.70 |
| Partnered (each) | $695.00 |

### Income Test
- **Free Area**: $150/fortnight
- **Taper Rates**: 
  - 40 cents per dollar between $150-$256
  - 60 cents per dollar above $256
- **Working Credit**: Can accrue up to $11,800

**Reference**: [JobSeeker Payment](https://www.servicesaustralia.gov.au/jobseeker-payment)

## Family Tax Benefit

### Part A - Per Child Rates

| Age | Maximum Rate | Base Rate |
|-----|--------------|-----------|
| 0-12 years | $225.12/fortnight | $70.46/fortnight |
| 13-15 years | $292.18/fortnight | $70.46/fortnight |
| 16-19 years (studying) | $292.18/fortnight | $86.70/fortnight |

**Income Test**:
- Maximum rate: Family income up to $63,166/year
- Reduces by 20 cents per dollar to base rate
- Base rate: Cuts out at $111,038/year + $11,657 per additional child

### Part B - Family Payment

| Youngest Child Age | Maximum Rate (fortnight) |
|-------------------|-------------------------|
| Under 5 years | $189.78 |
| 5-18 years | $132.48 |

**Income Test**:
- Primary earner limit: $103,000/year (couples)
- Secondary earner free area: $6,716/year
- Taper: 20 cents per dollar

**Reference**: [Family Tax Benefit](https://www.servicesaustralia.gov.au/family-tax-benefit)

## Child Care Subsidy

### Subsidy Rates by Income (2024-25)

| Family Income | Subsidy Rate |
|---------------|--------------|
| Up to $79,163 | 90% |
| $79,163 - $89,163 | 90% tapering to 80% |
| $89,163 - $189,390 | 80% tapering to 50% |
| $189,390 - $204,390 | 50% tapering to 20% |
| $204,390 - $264,390 | 20% |
| $264,390 - $374,390 | 20% tapering to 0% |
| Above $374,390 | 0% |

### Hourly Rate Caps
- Centre-based day care: $14.32
- Family day care: $13.29
- Outside school hours care: $12.54

**Activity Test**: Hours of subsidised care based on activity level

**Reference**: [Child Care Subsidy](https://www.servicesaustralia.gov.au/child-care-subsidy)

## Disability Support Pension

### Payment Rates (March 2024)

| Category | Basic Rate | Supplement | Total (fortnight) |
|----------|------------|------------|-------------------|
| Single, 21+ | $1,173.90 | $89.90 | $1,277.90 |
| Single, under 21 (independent) | $841.80 | $89.90 | $945.80 |
| Couple (each) | $884.20 | $67.70 | $962.50 |

**Youth Disability Supplement**: $159.70/fortnight (under 21)

### Eligibility
- Permanent physical, intellectual or psychiatric impairment
- Unable to work 15+ hours per week
- Condition fully diagnosed, treated and stabilised

**Reference**: [Disability Support Pension](https://www.servicesaustralia.gov.au/disability-support-pension)

## Other Major Programs

### Parenting Payment
- **Single**: $1,015.70/fortnight
- **Partnered**: $713.00/fortnight
- Eligibility: Primary carer of child under 6 (partnered) or 8 (single)

### Youth Allowance
- Students and job seekers aged 16-24
- Rates vary by age, living situation, and study/work status
- Parental income test may apply

### Carer Payment
- For those providing full-time care
- Same rate as Age Pension
- Income and assets tested

### Rent Assistance
- Maximum rates vary by family situation
- Singles: Up to $184.80/fortnight
- Couples: Up to $173.86/fortnight
- Additional amounts for children

## Implementation Status

### Currently Implemented
✅ Age Pension (rates, income test, assets test)
✅ JobSeeker Payment (rates, income test)
✅ Family Tax Benefit Part A & B
✅ Child Care Subsidy
✅ Disability Support Pension

### Planned Implementation
⏳ Parenting Payment
⏳ Youth Allowance
⏳ Austudy/ABSTUDY
⏳ Carer Payment and Allowance
⏳ Rent Assistance
⏳ Various supplements and concession cards

## Testing Approach

All benefit calculations validated against:
- Services Australia payment calculators
- Published rate tables
- Real household scenarios
- Income test boundary conditions

See `tests/policy/baseline/` for comprehensive test coverage.