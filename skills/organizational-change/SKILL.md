---
name: organizational-change
description: Get a delivered system actually used. Use when planning adoption of a new system or process, analyzing stakeholders and their incentives, handling resistance, planning training and support for a rollout, measuring adoption rather than deployment, or diagnosing why something technically successful is being worked around.
---

# Organizational change

The gap between deployed and used. A system can meet every requirement, pass every test, and be quietly worked around by the people it was built for — at which point the program has delivered nothing, whatever the acceptance documentation says.

The failure this exists to prevent is treating adoption as something that happens after delivery, by someone else, with whatever budget remains.

**Resistance is information, not an obstacle.** People generally do not resist a change that makes their work better. When they resist, the usual reasons are that it does not make their work better, that it makes it better for someone else at their cost, or that they have been through this before and it did not go well. All three are worth knowing and none is solved by more communication.

## Step 1: Map who is affected, and what it costs each of them

Not a stakeholder list. For each affected group:

- **What changes for them, concretely** — in their day, in their tools, in what they are measured on.
- **What they gain**, in their own terms rather than the program's.
- **What they lose.** Status, autonomy, expertise that no longer matters, a workaround they were proud of, a relationship with a system they knew well. This column is the one that gets left blank and it is the one that predicts resistance.
- **What they are measured on**, and whether the change helps or hurts that. People behave according to how they are evaluated, and a change that makes someone's numbers worse will be resisted regardless of its merit.
- **Who they listen to.** Rarely the program, usually a respected peer.

**Where a group bears cost so another can benefit, name it.** This is the same interest-based disagreement that derails cross-unit workshops — see `technical-workshop-facilitation`. It cannot be resolved by explaining the benefits more clearly, because they have understood; the benefit is going elsewhere. Either compensate the cost, adjust the design, or make the trade explicitly with someone who has the authority to impose it.

## Step 2: Involve people while the design can still change

Involvement after the design is fixed is consultation theater and is recognized as such immediately.

- **Bring real users in early**, and let their input visibly change something. One visible change from user feedback buys more credibility than a year of communication.
- **Use the people who know the work.** The person who has done the job for a decade knows the exceptions your design has not accounted for. `human-systems-integration` covers designing around real operators; this covers bringing them in.
- **Identify and support the local advocates.** Adoption spreads through respected peers, not through announcements. Find them, involve them early, give them information first, and let them be seen to shape it.
- **Do not confuse a steering committee with the affected population.** They are frequently the least affected people in the organization.

## Step 3: Sequence the rollout to learn

- **Pilot with a group that will tell you the truth**, not the friendliest group and not the hardest. You want findings you can still act on.
- **Fix what the pilot finds before expanding.** A rollout that proceeds on schedule with known unresolved problems teaches everyone that feedback is ignored, and the next group will not bother.
- **Expect a productivity dip and say so in advance.** There is always one. A team told to expect a temporary dip experiences it as expected; a team told the new system will be immediately better experiences it as failure and as evidence they were misled.
- **Support intensively at first, then taper.** Support demand is front-loaded and the first week disproportionately sets attitudes.
- **Retire the old path deliberately.** Where the old way remains available indefinitely, a meaningful fraction of people will keep using it — and you will run both indefinitely. Where it is switched off before the new one works, you will get workarounds that are worse than either. Set the date on evidence from the pilot.

## Step 4: Train for the job, not for the software

- **Train on the task**, in the user's language and workflow, not by touring the interface feature by feature.
- **Train close to when it will be used.** Training delivered weeks early is forgotten and is a common waste in rollouts.
- **Provide reference material people can use in the moment** — short, task-shaped, findable. See `procedural-documentation`.
- **Train the exceptions**, not just the happy path. The happy path is discoverable; the quarterly edge case is where people get stuck and lose faith.

## Step 5: Measure adoption, not deployment

Deployment is a program milestone. Adoption is the outcome, and they are routinely confused in status reporting.

Measures that mean something:

- **Actual usage** — by group, over time, against what the workflow implies it should be
- **Continued use of the old path or of workarounds**, which is the clearest signal something is unresolved
- **Support volume and its shape** — what people are stuck on, and whether it is falling
- **The outcome the change was for.** If the point was cycle time, measure cycle time. Adoption of a system that does not improve the thing it was built for is not success either.

**Investigate low adoption rather than escalating it.** A group not using the system usually has a reason, and it is usually a real one — a case the design does not handle, a step that is slower than before, an integration that does not work in their context. Mandating usage without finding the reason produces compliance behavior: the system is used minimally and the real work happens elsewhere.

## Step 6: Sustain it

- **Somebody owns it after the program ends.** A system with no owner degrades until it is replaced by the next program.
- **Feedback needs a route that visibly produces changes**, or it stops arriving and you lose your early warning.
- **Plan for staff turnover.** In a year, a substantial share of users will be people who never saw the rollout, the training or the reasoning. Onboarding material is part of the deliverable.
- **Watch for silent reversion.** Six months on, check whether the workarounds have come back. They often have, and the reasons are the same ones that were dismissed during rollout.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Adoption planned after delivery | Deployed, unused | Plan and fund it as part of the work |
| Losses not acknowledged | Resistance treated as irrationality | Name what each group gives up |
| Consultation after design freeze | Recognized as theater | Involve users while it can still change |
| Pilot findings not acted on | Feedback stops arriving | Fix before expanding |
| Immediate benefit promised | Normal dip read as failure | Say the dip is coming |
| Old path never retired | Both systems run indefinitely | Set a date on pilot evidence |
| Training on features | Users stuck on their actual task | Train the task, near the time of use |
| Deployment reported as adoption | Success on paper, workarounds in practice | Measure usage and the intended outcome |

The honest one: when people work around a system, they are usually right about something. The question worth asking is what they know that the design did not account for.
