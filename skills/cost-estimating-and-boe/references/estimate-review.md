# Estimate review

## The cost element checklist

Run this against every estimate. The omissions are consistent enough to be predictable.

**Direct labour**
- [ ] Every labour category mapped to the solicitation's, with qualifications met
- [ ] Hours by WBS element, traceable to a scope statement
- [ ] Rates from the approved structure, escalated across the period of performance
- [ ] Staffing profile realistic — ramp-up, clearance lead time, attrition backfill
- [ ] Key personnel named where the solicitation requires it

**Indirect**
- [ ] Fringe, overhead and G&A applied per the disclosed structure
- [ ] Correct pools applied to the correct bases
- [ ] Cost of money where applicable

**Non-labour**
- [ ] Materials with quotes or a documented basis, plus lead times
- [ ] Equipment, including spares and the test articles nobody counted
- [ ] Subcontracts with their own basis — see `teaming-and-subcontracts`
- [ ] Travel: trips, travellers, duration, destination, at realistic frequency
- [ ] Licences and cloud consumption at production volume — see `ai-cost-modeling` for AI workloads
- [ ] Test facility, range or lab time, including queue and rework runs
- [ ] Certification, accreditation and independent assessment costs
- [ ] Shipping, packaging, storage

**Programme costs that get omitted**
- [ ] Programme and project management
- [ ] Systems engineering and integration
- [ ] Documentation and every CDRL, at its stated frequency
- [ ] Security: clearances, facility, RMF or accreditation effort
- [ ] Quality assurance and audits
- [ ] Transition-in and transition-out
- [ ] Customer-required meetings, reviews and reporting
- [ ] Training, both delivered and internal
- [ ] Warranty and sustainment where in scope

## Reviewing someone else's estimate

Seven questions that find most defects:

1. **What is the method, per element, and is it right for the maturity of the scope?** A build-up on undefined scope is false precision; an analogy on well-defined scope wastes available information.
2. **Can I reproduce the arithmetic from what is written?** If not, the BOE is incomplete regardless of whether the number is right.
3. **Which three assumptions drive the number most, and what happens if each is wrong?** If nobody has done this, the estimate has no sensitivity analysis and its risk is unknown.
4. **What is the staffing profile, and is it physically achievable?** Peak staffing that exceeds hiring capacity or available cleared personnel is a schedule risk disguised as a cost estimate.
5. **Where is the integration and test effort?** Consistently the most under-estimated element, and the one that absorbs every upstream slip.
6. **Is the estimate consistent with the technical volume?** Cost realism is exactly this comparison. A technical approach describing continuous delivery and an estimate with no automation effort is a finding.
7. **What is not in here?** Ask the estimator directly. They usually know, and it is usually not written down.

## Sensitivity and ranges

A single-point estimate hides what it depends on. Even a rough range is more useful than a precise number:

- Identify the three to five drivers with the widest uncertainty.
- Vary each across its plausible range, holding others fixed, and record the effect.
- Report the drivers, not just the spread. "The estimate moves ±14% on integration test duration" tells a decision-maker where to look; "$4.2M ± 14%" does not.
- Where the decision warrants it, run a proper probabilistic analysis and report a confidence level rather than a point. See `applied-statistics`.

## What auditors and evaluators look for

- **Traceability** from every number to a source that exists independently of the estimator.
- **Consistency** between the estimate, the technical approach, the schedule and the staffing plan. Inconsistency between volumes is found reliably and read as either carelessness or optimism.
- **Adequate support** for judgemental elements — who, why them, and what they based it on.
- **Rate compliance** with the disclosed and agreed structure.
- **No unsupported factors.** A blanket uplift with no basis is removed in evaluation, and the estimate is then short by that amount.
- **Currency.** Quotes, rates and actuals that have aged past their validity get discounted.

## Where this connects

`wbs-and-scheduling` supplies the structure the estimate hangs on and the schedule that sets duration-driven costs. `earned-value-management` turns the accepted estimate into a performance measurement baseline. `risk-management` sizes management reserve. `solution-shaping` sets the price-to-win the estimate is tested against. `business-case` uses the same discipline for internal investment rather than a bid.
