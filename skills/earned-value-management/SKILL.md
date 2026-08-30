---
name: earned-value-management
description: Read and run earned value management on a program. Use when interpreting CPI, SPI, CV, SV or EAC, building or reviewing a performance measurement baseline, writing or reading a variance analysis, working an IPMR or CPR, judging whether a program is where its schedule claims, or explaining cost and schedule performance to someone who will act on it.
---

# Earned value management

EVM exists to answer one question a schedule cannot: **is the work actually done, or does it just look done?**

A schedule shows time spent. A budget shows money spent. Neither shows whether the work those bought was accomplished. EVM adds the third number — the budgeted value of what was actually completed — and every insight comes from comparing the three.

## The three numbers

| | Is | Answers |
| --- | --- | --- |
| **PV** — planned value | Budgeted cost of work scheduled | What should be done by now |
| **EV** — earned value | Budgeted cost of work performed | What is actually done, valued at plan |
| **AC** — actual cost | Cost of work performed | What it cost to get there |

Everything else is arithmetic on these:

- **CV = EV − AC** · Cost variance. Negative means overrunning.
- **SV = EV − PV** · Schedule variance, expressed in dollars.
- **CPI = EV ÷ AC** · Cost efficiency. Below 1.0 means each dollar buys less than a dollar of planned work.
- **SPI = EV ÷ PV** · Schedule efficiency. Below 1.0 means behind.

**SPI's limitation matters and is routinely missed.** Because SV is measured in dollars, SPI drifts toward 1.0 as a program approaches completion regardless of lateness — a program finishing a year late shows SPI = 1.0 at the end, because all the value eventually gets earned. SPI is useful early and misleading late. For real schedule position, use the critical path from the IMS, not SPI.

## Estimate at completion

The forecast, and the number leadership actually acts on.

| Method | Formula | Assumes |
| --- | --- | --- |
| Performance continues | `EAC = BAC ÷ CPI` | Efficiency to date persists. The default, and usually the most honest |
| Remaining work as planned | `EAC = AC + (BAC − EV)` | Past overrun was one-off. Requires a reason |
| Cost and schedule pressure | `EAC = AC + (BAC − EV) ÷ (CPI × SPI)` | Schedule recovery costs money |

**TCPI** — the efficiency required on remaining work to still hit the target — is the reality check: `TCPI = (BAC − EV) ÷ (BAC − AC)`. When TCPI substantially exceeds the CPI achieved so far, the plan requires performance the program has never demonstrated. A TCPI of 1.3 against a running CPI of 0.85 is not a stretch goal; it is a forecast nobody should sign.

Research on completed programs is consistent: **CPI stabilises early and rarely recovers.** By roughly 20% complete, the CPI is a good predictor of the final outcome. A program planning to recover a poor early CPI is planning against the evidence, and saying so early is more useful than saying it later.

## The baseline

EVM measures against a performance measurement baseline, and a bad baseline makes every number meaningless.

- **Scope decomposed to work packages** via a WBS, each with a discrete deliverable, a budget, a schedule, and one owner. `wbs-and-scheduling` builds this and the IMS the critical path comes from.
- **Measurement method chosen per package**, before work starts. This choice drives everything:

| Method | Fits | Fails when |
| --- | --- | --- |
| Milestone | Discrete deliverables | Milestones are large; progress is invisible between them |
| Percent complete | Continuous work | Subjective, and the standard route to inflated EV |
| 0/100 | Short packages | Long packages show nothing until done |
| 50/50 | Medium packages | Overstates early |
| Apportioned | Work that tracks another package | The reference package is itself misreported |
| Level of effort | Support functions with no discrete output | Applied to real work, guaranteeing SPI = 1.0 and hiding the problem |

**Level of effort applied to discrete work is the most common way EVM is made useless.** LOE earns value with time regardless of accomplishment. A baseline with a large LOE fraction reports healthy performance by construction, and a program that keeps reclassifying troubled packages as LOE is manufacturing good news.

- **Control accounts** where budget, schedule and responsibility meet, each with a control account manager who can actually explain the variance.
- **Baseline changes go through change control** — see `configuration-management`. Rebaselining to erase an unfavourable variance is how EVM stops being an early-warning system, which is its only real purpose.

## Variance analysis

The narrative, and where value is either created or wasted.

A useful variance analysis states: what the variance is, **why** — the actual cause, not a restatement of the number — the impact on completion, the corrective action with an owner and a date, and whether previous corrective actions worked.

Weak: *"CPI is 0.87 due to higher than planned costs."* That is the definition of CPI, not a cause.

Strong: *"CPI 0.87. Integration testing required 340 hours against 180 planned, because the vendor SDK's batch interface was undocumented and had to be characterised by experiment. Remaining integration re-estimated at +160 hours; EAC increases $84K. Two engineers redirected from the reporting module, which moves its milestone three weeks — inside float. Prior action to add a vendor support contract has not yet reduced the rate."*

The second one gives a decision-maker something to act on.

## Reading a program you did not build

Order of examination, and the questions each answer raises:

1. **CPI and SPI trend, not the point value.** Direction matters more than the number.
2. **The LOE fraction.** High LOE means the metrics measure less than they appear to.
3. **TCPI against the CPI to date.** How much better than ever must the program now perform?
4. **Rebaseline history.** Frequent rebaselines erase the signal EVM exists to give.
5. **Variance narratives.** Do they name causes, or restate arithmetic?
6. **Critical path from the IMS**, since SPI will not tell you about schedule late in the program.

## Where this connects

`risk-management` — a variance is often a realised risk, and if it was never on the register that is worth asking about. `technical-reviews` — gates should see cost and schedule performance, not only technical maturity. `engineering-to-proposal` — demonstrated CPI and SPI are past-performance evidence, and among the few quantitative kinds available.

## Reference

- `references/variance-analysis.md` — the variance report format and what makes a cause statement real.
