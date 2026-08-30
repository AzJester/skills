---
name: technical-reviews
description: Plan, run, and close a systems engineering technical review gate. Use when preparing for or conducting an SRR, SFR, PDR, CDR, TRR, or FCA/PCA, when setting entry and exit criteria, when assembling the artefact package a gate requires, when writing or dispositioning review action items and RIDs, or when judging whether a programme is genuinely ready to pass a gate. `lessons-learned` captures what each gate taught.
---

# Technical reviews

A gate exists to answer one question: is this programme ready to spend the next phase's money? Everything else about a review is machinery for answering it honestly.

The failure mode is universal and worth naming up front. A review becomes a presentation, the presentation goes well, the gate passes, and the problems arrive two phases later at ten times the cost. A review that cannot fail is not a review. If the outcome is known before the package is read, the gate has already been skipped.

## The gates

| Gate | Question it answers | Baseline established |
| --- | --- | --- |
| **SRR** — System Requirements Review | Are the requirements the right ones, and are they achievable? | Functional |
| **SFR** — System Functional Review | Does the functional decomposition satisfy those requirements? | Functional (refined) |
| **PDR** — Preliminary Design Review | Is the design approach sound enough to detail? | Allocated |
| **CDR** — Critical Design Review | Is the detailed design complete enough to build? | Product |
| **TRR** — Test Readiness Review | Are we ready to run the verification programme? | — |
| **FCA / PCA** — Functional / Physical Configuration Audit | Does the built item match its requirements, and its documentation? | Product (verified) |

Programmes rename and merge these constantly. What matters is not the acronym but that each gate has a question, criteria that could fail it, and a baseline it establishes.

## Step 1: Entry criteria, agreed in advance

Entry criteria decide whether the review happens at all. Agree them a phase early, not the week before, or they become whatever was ready.

The pattern for every gate: the artefacts exist, they are at the maturity the gate needs, they were distributed with enough lead time to be read, and the open items from the previous gate are closed or explicitly carried with agreement.

`references/gate-criteria.md` carries entry and exit criteria per gate, and the artefact each one depends on. Most of those artefacts come from skills already here — `requirements-dev` for the requirements baseline, `system-dev` for the architecture and interfaces, `trade-study-analysis` for the decisions and their rationale, `verification-validation` for the VCRM, `risk-management` for the register, `threat-modeling` where there is a security posture to show.

**If entry criteria are not met, the review moves.** Holding it anyway converts a gate into a status meeting, and every subsequent gate inherits the fiction.

## Step 2: Distribute early, read before

The package goes out far enough ahead to be read — a fortnight is typical, less than a week is theatre. Reviewers submit comments **in writing before** the meeting, as RIDs (review item discrepancies) or equivalent.

This inverts the usual shape, and the inversion is the point. The meeting is not for presenting the material; it is for working the disagreements the written comments already surfaced. A review where the first substantive comment arrives during the meeting wasted everyone's preparation, and usually ends in a pass because there was no time to do anything else.

## Step 3: Run it against the criteria

Work the RIDs, not the slides. For each one: accept and act, accept and defer with a date, or reject with a reason recorded. Rejecting a reviewer's finding is legitimate; rejecting it without a written reason is how reviewers stop bothering.

Keep two things visible throughout: the exit criteria, and the list of open items. The gate's decision follows from those two, and nothing else.

## Step 4: Decide, honestly

Four outcomes. Programmes that only ever use the first two are not reviewing.

- **Pass** — exit criteria met, open items minor and dated.
- **Pass with actions** — criteria substantially met; specific actions with owners and dates, and a named person who confirms closure. Not a euphemism for pass.
- **Conditional** — a specific, material gap. The gate reconvenes on that gap alone once closed, rather than re-reviewing everything.
- **Fail** — the programme is not ready. Rare, and legitimate. A programme that has never failed a gate either is exceptional or is not testing.

Record the decision, the criteria that drove it, and the dissent. A reviewer who disagreed and was overruled should be findable in the record when the issue resurfaces.

## Step 5: Close the loop

An action item without an owner, a date, and a closure criterion is not an action item. Track them to closure and report status at the next gate — the most useful five minutes of any review is the previous gate's actions and what happened to them.

Baseline what the gate established. After PDR the allocated baseline is under configuration control, and changes go through change control rather than through editing. Without that, the gate established nothing.

## For a review you are being reviewed at

Three things reviewers notice and most packages get wrong:

**Show the risks.** A package with no risks reads as one that has not looked. `risk-management` output belongs in the package, with what moved since last gate.

**Show the trade-offs, with the alternatives you rejected and why.** A design presented as inevitable invites the question of what else was considered, and having no answer is worse than having a rejected option.

**Show what is not ready, before someone finds it.** Naming your own gaps buys credibility that carries the rest of the package. Having a gap found for you spends credibility you then need for everything else.

## Reference

- `references/gate-criteria.md` — entry and exit criteria per gate, with the artefacts each depends on.
- `references/action-item-log.md` — RID and action item log, with disposition states.
