---
name: agile-on-a-government-contract
description: Run iterative delivery inside a contract that was written for waterfall. Use when structuring an agile program under EVM, mapping sprints to control accounts and work packages, writing a contract or CDRL set that permits iteration, aligning sprint cadence with reporting and review cadence, establishing a government product owner, or diagnosing why an "agile" program is delivering like a waterfall one. Covers the contract layer; the software workflow skills cover a single team's practice.
---

# Agile on a government contract

The software workflow skills in this repository — `to-spec`, `to-tickets`, `implement`, `speckit-generator` — cover how one team works. None of them touch the layer that actually decides whether iteration is possible: the contract, the baseline and the reporting obligations wrapped around the team.

**The core tension is simple and structural.** Agile fixes cost and time and lets scope flex. Most contracts fix scope and hold you to cost and schedule. Run one inside the other without resolving it and you get the common failure: sprints that cannot change scope, a backlog nobody is permitted to reprioritise, and a baseline that was set eighteen months ago — waterfall with stand-ups.

The failure this exists to prevent is a program that adopts agile ceremony and keeps waterfall commitments, paying the cost of both.

## Step 1: Make the contract permit iteration

If this is not resolved, nothing downstream works. The question is what flexes.

| Structure | Flexes | Works when |
| --- | --- | --- |
| **Fixed scope, fixed price** | Nothing | The requirement is genuinely known and stable — rare for software |
| **Fixed capacity** | Scope, within a funded team over a period | The customer will prioritize a backlog and accept what fits |
| **Capability-based** | The features inside a capability | Capabilities are contracted; stories are worked underneath |
| **Cost-reimbursable with a prioritized backlog** | Scope, continuously | The customer is engaged enough to prioritize |

**Contract capabilities, not stories.** Put the outcome in the work statement at the level of a capability or a mission thread; leave the decomposition to the backlog where it can change. A contract that enumerates two hundred requirements has fixed scope regardless of what the delivery method is called — see `sow-and-pws`.

**Say explicitly how scope changes without a modification.** Reprioritising within a fixed capacity is not a contract change; substituting one capability for another may be. Agreeing that boundary in the contract prevents the argument that otherwise happens in month four.

**The software acquisition pathway exists for this.** DoD has an acquisition pathway designed around iterative software delivery, with value assessments and user agreements in place of traditional milestone structures. Where it applies, it removes much of this friction — check whether the program is on it, because it changes what is possible.

## Step 2: Make EVM and agile coexist

They can. The mapping is mechanical once decided, and the mistake is leaving it undecided until the first report.

| EVM construct | Agile equivalent |
| --- | --- |
| Control account | A team, or a capability, with one accountable owner |
| Work package | An epic or feature, sized to a few sprints |
| Planning package | Far-term epics not yet decomposed |
| Measurement method | Completed and **accepted** stories, or milestone on feature acceptance |
| Rolling wave | Near-term sprints detailed, later epics coarse |

Four disciplines that decide whether the numbers mean anything:

**Earn value on accepted work, not on effort.** A story counts when it meets the definition of done and the customer's representative has accepted it. Earning on hours expended reproduces exactly the problem EVM exists to prevent — see `earned-value-management` on measurement methods deciding whether earned value is honest or invented.

**Story points are for the team; the baseline is in dollars and hours.** Do not try to make points a contractual unit. Convert at the work-package level — points completed against points planned gives percent complete for that package, and that percent applies to its budget.

**The IMS is milestone-level with rolling wave.** Do not put sprints in the integrated master schedule as tasks; you will re-baseline every two weeks. Capabilities, releases and integration events go in the schedule; sprints live in the team's tooling underneath — see `wbs-and-scheduling`.

**Re-planning within a control account is normal, not a variance.** Moving stories between sprints inside an epic is execution. Moving scope between control accounts is a baseline change. Write that distinction down before the first monthly report.

## Step 3: Get a real government product owner

**The hardest part is organizational, not technical.** Iterative delivery needs someone on the customer side who can prioritize, accept, and decide — available at the cadence the team works at, not at the cadence of a monthly review.

- **Named, empowered, available.** A product owner who must escalate every decision is a queue, and the team's cycle time becomes the customer's decision latency.
- **Where no single person can decide**, agree a decision forum and its turnaround explicitly. Slow is workable; unpredictable is not.
- **Acceptance criteria agreed before the sprint**, not argued after. This is `requirements-dev` discipline applied at story scale.
- **When the customer cannot supply this**, say so early and structure around it — longer increments, a proxy product owner with written delegation, or a different contract shape. Pretending it will resolve itself is how a program discovers in month six that nothing has been accepted.

## Step 4: Deal with the CDRLs, because they do not go away

Working software is not a deliverable under most contracts; the data item is.

- **Read the CDRL list and its data item descriptions early**, and map each to how it will actually be produced — see `sow-and-pws` and `dod-technical-report`.
- **Generate documentation from the work rather than as a phase.** Architecture decisions recorded as they are made, interface documents maintained alongside the interface, test evidence produced by the pipeline. `devsecops-pipeline` covers producing evidence as an artifact of running rather than assembling it before a review.
- **Put contract obligations in the definition of done.** If a story is not done until its test evidence, documentation and accreditation artifacts exist, they get produced continuously. If they are not in the definition of done, they accumulate into a documentation phase at the end, which is the waterfall you were avoiding.
- **Negotiate delivery cadence for documents.** A document delivered once at 90% design is a waterfall artifact; the same document delivered incrementally with updates is compatible with iteration. This is worth asking for.

## Step 5: Align the cadences

A program runs several clocks at once and they need deliberate alignment.

| Clock | Typical | Feeds |
| --- | --- | --- |
| Sprint | 1–3 weeks | Team execution, story acceptance |
| Release or increment | 1–3 months | Capability delivery, customer value assessment |
| EVM reporting | Monthly | Cost and schedule performance |
| Program review | Quarterly | `technical-reviews`, customer governance |

**Make the reporting boundary land on a sprint boundary.** Otherwise every monthly report contains partially complete stories, and percent complete becomes an estimate — which is exactly what EVM is supposed to eliminate.

**Demonstrate working software at the increment**, to the actual users. It is the most useful thing a government program review can contain and it is frequently replaced with slides.

## Step 6: Continuous delivery needs continuous authorization

The pipeline and the authorization are what make iteration reach the user rather than stopping at a staging environment.

- **A release cadence faster than the authorization cadence delivers nothing.** Where every release requires a fresh authorization, the ATO process is the real delivery cadence.
- **Continuous authorization is the resolution**, and it rests on a pipeline that demonstrably enforces the controls — `rmf-ato` and `devsecops-pipeline` together.
- **Agree what falls inside the authorized envelope** and what requires re-authorization, with the authorizing official, in advance.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Agile ceremony, waterfall commitments | Sprints that cannot change scope | Resolve what flexes, in the contract |
| Requirements enumerated in the contract | Scope fixed whatever the method | Contract capabilities; decompose in the backlog |
| Sprints in the IMS as tasks | Re-baselining every two weeks | Milestone-level IMS, rolling wave |
| Earning value on effort | Percent complete invented | Earn on accepted, done work |
| Story points as a contract unit | Meaningless conversion arguments | Points inside the package; dollars in the baseline |
| No empowered product owner | Nothing gets accepted | Named and available, or restructure |
| CDRLs deferred | Documentation phase at the end | Contract obligations in the definition of done |
| Release faster than authorization | Working software that never ships | Continuous authorization with the pipeline behind it |

The honest one is the first, and the test is a single question: what happened the last time the team wanted to drop something from the backlog? If the answer is that they could not, the program is not agile regardless of its cadence.
