---
name: program-recovery
description: Turn around a program that is in trouble. Use when cost or schedule performance is deteriorating, when an EAC is no longer credible, when deciding between re-planning, re-baselining and an over-target baseline, when building a get-well plan, when deciding what to tell the customer and when, or when assessing whether a program can be recovered at all. Acts on what earned-value-management measures.
---

# Program recovery

`earned-value-management` tells you how to read a program in trouble — the indices, the estimate at completion, the reality check on whether the remaining work is achievable. This is what to do about it.

**Recovery is mostly a diagnosis problem.** The single most consequential question is whether the baseline was ever achievable, because the answer determines everything that follows and the two cases need opposite responses. Teams routinely apply the execution remedy to a baseline problem, work harder against an impossible plan, and lose another six months.

The failure this exists to prevent is the recovery plan that is really a hope: same scope, same team, same date, more effort.

## Step 1: Diagnose which problem you have

| | Baseline problem | Execution problem |
| --- | --- | --- |
| **What happened** | The plan was never achievable | The plan was achievable; performance is not meeting it |
| **Signals** | Variance from the very first reports; the estimate was compressed to a target; scope grew without re-planning; staffing profile was never physically possible | Performance started acceptable and deteriorated; a specific cause is identifiable — turnover, a technical surprise, a supplier |
| **Response** | Re-baseline, descope or restructure. Effort will not fix arithmetic | Fix the cause. Re-baselining hides it and it recurs |
| **The trap** | Working harder against an impossible plan | Re-baselining around a problem that will simply reappear |

**Diagnostic questions, answered with evidence:**

- **Was the baseline ever achievable?** Look at the original estimate against the price-to-win. An estimate compressed to fit a target is the most common root cause and the least often named — see `cost-estimating-and-boe`.
- **Is the trend or the level worse?** A poor but stable index is different from one deteriorating monthly. The trend tells you whether you have found the bottom.
- **Is the EAC credible?** Compare the performance required to finish on the current EAC against the performance achieved so far. Where finishing requires efficiency substantially above anything demonstrated, the EAC is a wish and the real number is worse.
- **Is the schedule position real?** SPI drifts toward 1.0 late in a program regardless of lateness. Use the critical path from the IMS — see `wbs-and-scheduling`.
- **Has scope grown without the baseline moving?** Accepted direction without a modification, constructive change, or requirements creep — see `contract-vehicles-and-clauses`.
- **Was the staffing profile ever achievable?** Peak staffing exceeding hiring capacity or cleared-personnel availability is a baseline problem that presents as an execution one — see `industrial-security` and `resource-and-capacity-management`.

**Get an independent look.** The team that built the baseline usually cannot see that it was wrong; they have been explaining the variance monthly and the explanations are internally consistent. Someone from outside the program, reading the same data cold, is the cheapest intervention available.

## Step 2: Know the options and what each actually costs

| Option | Means | Right when | Cost |
| --- | --- | --- | --- |
| **Re-plan within the baseline** | Re-sequence remaining work; move budget between packages | The total is still achievable | Low; no customer approval usually needed |
| **Descope** | Remove or defer scope, with the customer | Priorities can be re-ordered and something is genuinely less needed | Contract modification; a conversation you must have early |
| **Re-baseline** | Establish a new performance measurement baseline | The original is no longer a useful measurement tool | Customer agreement; loses variance history |
| **Over-target baseline** | Formally baseline above the contract budget base — negotiated cost plus authorized unpriced work, excluding fee | Recovery within the contract budget base is not possible and the work must continue | Formal, customer-approved, highly visible |
| **Restructure** | Change the technical approach, team, or supplier | The current approach cannot get there | Disruption, ramp cost, lost work |
| **Terminate** | Stop | The program cannot deliver value for what remains | Real, and sometimes the right answer |

Three things worth stating plainly:

**Re-baselining is not a recovery.** It changes the measuring stick. Done without addressing cause, the new baseline deteriorates the same way and you have spent your credibility for nothing.

**An over-target baseline is a formal, visible act**, not a quiet adjustment. Its purpose is to restore a usable measurement baseline when the contract budget base is unachievable and the work must still be managed. Using it to make variances disappear is both ineffective and noticed.

**Descope is the most underused option and usually the most effective.** Customers frequently prefer the important 80% on time to everything late — but only if asked early enough that it is still a choice. Asked late, it reads as a failure announcement. `solution-shaping` covers the descope ladder that should already exist from the pursuit.

## Step 3: Build a get-well plan that is actually a plan

A recovery plan is credible only if it names what changes. "The team will focus" is not a change.

Every recovery plan states:

- **The root cause**, specifically, with the evidence. The RCCA family applies — `rcca-master` routes them.
- **What changes**: scope, sequence, staffing, approach, supplier, or the baseline. At least one must actually change.
- **The new forecast**, built bottom-up rather than by adjusting the old one. A recovery EAC derived by scaling the previous EAC inherits its optimism.
- **What is being given up.** Every recovery trades something — scope, margin, capability, other work. Naming it is what makes the plan honest.
- **Leading indicators with dates**, so that within four to six weeks you know whether it is working. A plan whose first checkpoint is the end is not a plan.
- **What happens if it does not work**, decided now, while people are calm.

**Beware adding people.** Staffing up a late program costs productivity before it adds any — ramp time, onboarding, and the experienced people who now train instead of deliver. On classified work add clearance lead time on top. Sometimes correct; never fast.

**Fix the cause before optimizing the symptom.** Requirements churn, an unachievable baseline and staffing shortfalls account for most recoveries, and none of them is fixed by better tracking.

## Step 4: Tell the customer early, because the arithmetic of credibility is brutal

**Bad news does not improve with age, and the cost of delay is not linear.** A program reporting green until it cannot has spent exactly the credibility it needs at the moment it needs it — `program-startup` makes this point about the first report, and it compounds from there.

- **Bring the diagnosis, options and a recommendation**, not just the problem. `executive-decision-memo` is the right instrument; `briefing-deck` if a briefing is what has been scheduled.
- **Say what you need from them.** Most recoveries require a customer decision — descope, more time, more money, a requirements freeze. A recovery presented with no ask is a status update.
- **Do not present a recovery plan you do not believe.** The second failed recovery costs far more than the first, because after it nothing you say about the program is credited.
- **Expect scrutiny to increase and plan for its cost.** Reviews, reporting and oversight all rise during recovery, and that time comes out of the same team doing the recovering. Budget it.

## Step 5: Know when it cannot be recovered

Sometimes the honest answer is that the program cannot deliver what it promised for what remains.

Signals that it is structural rather than fixable: several recovery attempts with the same result; the cause is a technical approach that cannot work rather than a performance shortfall; the customer's need has changed and the program is delivering to a superseded requirement; or the remaining cost exceeds the remaining value to anyone.

**Raise it.** A program continued past that point consumes people and money and produces an outcome nobody wants — and continuing is usually a decision nobody made. Terminating or restructuring is a customer and leadership decision, and they can only make it if someone puts it in front of them with the evidence.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Wrong diagnosis | Working harder against an impossible plan | Determine baseline versus execution first |
| Re-baseline without cause | New baseline deteriorates identically | Fix the cause; re-baseline only to restore measurement |
| Recovery plan with no change | Same scope, team and date, more effort | Name what actually changes |
| EAC scaled from the old one | Inherits the original optimism | Rebuild bottom-up |
| Adding people to go faster | Productivity drops first | Only with ramp time counted, and rarely |
| Bad news held | Credibility gone when it is needed | Early, with options and a recommendation |
| No leading indicators | Failure discovered at the end | Checkpoints inside six weeks |
| Descope raised late | Reads as failure, not choice | Ask while it is still a choice |
| Oversight cost unbudgeted | Recovery time consumed by reporting | Budget the scrutiny |

The honest one is the first. Most failed recoveries were correctly executed responses to the wrong diagnosis.
