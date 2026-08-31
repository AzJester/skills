---
name: measures-of-effectiveness
description: Define and track the measures that say whether a system is meeting its objectives. Use when writing MOEs, MOPs, KPPs or technical performance measures, deciding what to measure and at what threshold, building a TPM tracking profile against planned values, choosing evaluation criteria for a trade study, or preparing the performance evidence a review gate expects.
---

# Measures of effectiveness

Requirements say what the system must do. Measures say how well, and whether it is on track to get there. A program with requirements and no measures discovers at verification that it met every shall and satisfied nobody.

## Four things, often confused

The distinctions matter because they answer different questions for different audiences, and collapsing them produces a metric nobody can act on.

| | Question | Whose view | Example |
| --- | --- | --- | --- |
| **MOE** — measure of effectiveness | Does it achieve the mission? | Stakeholder, operational | Time to restore service after a regional outage |
| **MOP** — measure of performance | Does the system perform as designed? | Engineering, technical | Failover completes in under 90 seconds |
| **KPP** — key performance parameter | Is it acceptable at all? | Contractual, gating | Availability ≥ 99.9% — below this, the system is not accepted |
| **TPM** — technical performance measure | Are we on track, right now? | Program management, tracked over time | Current measured failover time versus the planned profile at this date |

The relationship: **MOEs are operational and stakeholder-facing; MOPs are the technical parameters that drive them; KPPs are the subset with a threshold that must not be breached; TPMs are whichever of these you track over time to see trouble early.**

An MOE is not a requirement. It does not say "shall". It says how good is good, and that is why it survives the negotiation that trims requirements.

## Step 1: Start from the mission, not the design

Write MOEs before the design exists, and phrase them in the stakeholder's language rather than the engineer's. If an MOE mentions a component, it is a MOP wearing an MOE's clothes.

Test each candidate MOE against three questions:

- **Would the stakeholder recognize this as what they care about?** If it needs translating, it is not an MOE.
- **Is it independent of the solution?** A good MOE survives a complete redesign. "Requests per second on the enrollment API" dies if enrollment moves off HTTP; "enrollments completed per hour at peak" does not.
- **Can it be observed?** Not necessarily measured cheaply, but observed in principle. An MOE nobody can ever evaluate is an aspiration.

## Step 2: Set threshold and objective, and say which

Every measure gets two values, and stating only one is the most common mistake here.

- **Threshold** — the minimum acceptable. Below this, the capability is not useful and, for a KPP, not acceptable.
- **Objective** — the value worth paying for. Above this, more is not worth the cost.

The gap between them is the trade space. A measure with only a threshold gives engineering no reason to do better than the minimum; one with only an objective gives no basis for accepting anything less. `trade-study-analysis` scores alternatives across exactly this band — measures defined here become its evaluation criteria, which is the cleanest way to stop trade study criteria being invented to fit a preferred answer.

Record where each value came from. A threshold with no provenance gets negotiated away at the first schedule pressure; one traceable to an operational need does not.

## Step 3: Choose TPMs sparingly

Not every measure is tracked over time. Track a TPM when the parameter is uncertain, matters, and can move — and when learning it late would be expensive.

Six to ten TPMs is a working program. Thirty is a spreadsheet nobody reads. Choose the ones where being wrong is expensive.

For each TPM define:

- **The planned profile** — expected value at each milestone, not just the endpoint. Most parameters do not meet their target until late, and a profile makes the difference between on-track-but-not-there-yet and off-track visible.
- **The tolerance band** — how far off the profile is acceptable before it is a problem.
- **The measurement method** — how the current value is obtained, and how much it costs to obtain. A TPM too expensive to measure gets estimated, and estimates drift toward the plan.
- **The trigger** — what happens on breaching the band. Usually: raise a risk in `risk-management`, and report at the next gate.

## Step 4: Track honestly

Report current value against planned profile at every reporting period, with the trend.

Three failure patterns to watch, all of which make a tracking chart worse than none:

**The measure that only ever improves.** Real parameters oscillate. A perfectly monotone curve usually means the value is being estimated from the plan rather than measured from the system.

**The measure that meets its target exactly at the gate.** Convergence timed to a review is a reporting artifact, not engineering.

**The measure quietly redefined.** When a parameter is hard to meet, the definition tends to soften — a percentile changes, a condition is excluded, a unit shifts. Version the definition alongside the value, so a change in definition cannot look like a change in performance.

## Step 5: Feed the gates

Measures are what turns a review from a presentation into an assessment. At PDR, TPMs should have planned profiles and initial estimates; by CDR, measured or credibly analyzed values; at verification, the evidence closing them.

`technical-reviews` expects this, and `verification-validation` is where a measure's final value is proven rather than reported.

## Reference

- `references/tpm-tracking.md` — the tracking sheet, planned profile and trigger conventions.
