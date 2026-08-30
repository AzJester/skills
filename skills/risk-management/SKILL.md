---
name: risk-management
description: Run a programmatic risk register. Use when identifying, scoring, or tracking programme risks, building or reviewing a risk matrix, writing risk statements, deciding a handling strategy, tracking mitigation burn-down, or preparing the risk section of a review or proposal. Covers technical, schedule, cost, supplier and staffing risk. Distinct from FMEA, which analyses design failure modes rather than programme exposure.
---

# Risk management

A risk is a future event that has not happened, might not happen, and would hurt if it did. Two consequences follow, and most bad risk registers violate one of them.

**A risk that has occurred is not a risk, it is an issue.** Issues get worked, not scored. A register full of issues is a status report wearing a risk register's clothes, and it hides the risks that still have time to be cheaply mitigated.

**A risk with no uncertainty is not a risk, it is a plan.** "The integration will be difficult" is a fact about the work. "If the vendor SDK does not support batch enrolment, then integration slips by six weeks" is a risk.

## Not FMEA

This repo has `fmea-analysis`, and the two get confused because both multiply two numbers.

| | FMEA | Risk register |
| --- | --- | --- |
| Object | A design's failure modes | The programme's exposure |
| Question | How can this part fail, and what happens downstream? | What could stop us delivering? |
| Scope | Technical, within the artefact | Technical, schedule, cost, supplier, staffing, external |
| Owner | Design engineer | Programme, with a named risk owner per item |
| Horizon | Life of the design | Life of the programme |

Use FMEA to find design weaknesses. Use this to track that the sole-source part has an eleven-month lead time and one supplier.

## Step 1: Write the risk properly

Use the **if–then** form, with a cause. Anything else scores badly because nobody can agree what is being scored.

> **If** \<condition or event\>, **then** \<consequence to cost, schedule, or performance\>, **because** \<the cause that makes it plausible\>.

Bad: "Schedule risk." Bad: "The API might change."

Good: "**If** the vendor deprecates the v2 authentication API before our migration completes, **then** the enrolment service loses production access and the launch slips by an estimated eight weeks, **because** their published sunset date falls inside our integration window."

The `because` clause is what makes the risk arguable, and arguable risks are the ones that get managed. A risk nobody can dispute is usually a risk nobody has examined.

## Step 2: Score likelihood and consequence

Score both on 1–5 against a published scale, not against intuition. `references/scoring-scales.md` carries scales for likelihood and for consequence across cost, schedule and performance — adapt the thresholds to the programme, but write them down first, because a scale invented per-risk produces a register that cannot be sorted.

Two disciplines:

**Score the consequence assuming the risk occurs and nothing is done.** Scoring the residual by reflex hides how much the mitigation is buying, and makes it impossible to tell whether dropping the mitigation would matter.

**Record both inherent and residual.** Inherent is before handling, residual is after the planned handling works. The gap between them is the value of the mitigation, and it is the number a review board should be asking about.

## Step 3: Choose a handling strategy

Four, and the choice is a decision with an owner, not a label.

- **Avoid** — change the plan so the risk cannot occur. Usually the cheapest and most often overlooked.
- **Mitigate** — reduce likelihood, consequence, or both. State which; a mitigation that reduces neither is an activity.
- **Transfer** — move it to a party better placed to carry it, contractually or by insurance. They must know.
- **Accept** — carry it knowingly, with a named accepter and a trigger that says when to revisit.

Every handling action needs an owner, a date, and a stated effect on the score. "Monitor" is not a handling strategy; it is what you do while you decide on one.

## Step 4: Track burn-down, not headcount

A register that only grows is not being managed. Track, per reporting period:

- Risks opened, closed, and realised (became issues)
- Total exposure, inherent and residual
- Mitigation actions due, completed, and overdue
- Risks whose score moved, and why

**Watch for the two failure patterns.** A register where nothing ever closes means risks are not being retired, only accumulated. A register where scores only ever fall means the scoring is following the schedule rather than the evidence — real risks sometimes get worse, and a register that never shows one rising is not being scored honestly.

## Step 5: Escalate on the trigger, not on the feeling

Every risk above the agreed threshold carries a **trigger**: the observable condition that means it is materialising and the fallback must start. "Vendor has not confirmed the extension by 15 March" is a trigger. "It feels like it is going badly" is not.

When a trigger fires, the risk becomes an issue. Move it, record the date, and stop scoring it.

## Where this connects

- `trade-study-analysis` — a trade study that ignores risk picks the option with the best nominal score and the worst exposure. Feed risk into the criteria.
- `technical-reviews` — every gate should examine the register, and the interesting question at a gate is what moved since last time, not the count.
- `engineering-to-proposal` — a proposal with no risks reads as one that has not thought about the work. The register is where honest, mitigated risk language comes from.
- `incident-response` — a realised risk that caused an incident should already appear here, and if it does not, the postmortem should ask why it was never on the register.

## Reference

- `references/risk-register-template.md` — the register, column by column.
- `references/scoring-scales.md` — 1–5 likelihood and consequence scales, and the 5×5 matrix with its thresholds.
