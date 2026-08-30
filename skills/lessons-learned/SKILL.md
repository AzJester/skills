---
name: lessons-learned
description: Capture what a programme learned so the next one benefits. Use when running a lessons learned session at a gate or at close-out, writing a lesson that is specific enough to act on, deciding where a lesson should live so it is found at the moment of use, or diagnosing why an organisation keeps repeating the same mistakes despite having a lessons learned repository. Distinct from incident postmortems and root cause analysis, which are event-scoped.
---

# Lessons learned

**This is the discipline everyone agrees is valuable and almost nobody does.** That is the design constraint, and any approach that ignores it produces another repository nobody opens.

The failure mode is specific and consistent: lessons are captured at close-out when the people have moved on, written as blameless generalities that could apply to any programme, filed in a repository with no retrieval trigger, and never read by the programme that would have benefited. Every step of that is fixable, and fixing the last one matters most.

## Step 1: Understand why it fails, and design against each cause

| Cause | What actually happens | The fix |
| --- | --- | --- |
| **Captured too late** | Close-out, after the team has dispersed and the details are gone | Capture at gates and after events, continuously |
| **Written as generalities** | "Communication could have been better" | A lesson names what happened, why, and what to do differently |
| **Blameless taken too far** | So depersonalised it carries no information | Blameless about people; specific about decisions and conditions |
| **Filed, not applied** | A repository with no retrieval trigger | Put the lesson in the artifact where the work happens |
| **No owner** | Everyone's job, nobody's task | Named owner per lesson, with a change to make |
| **Never measured** | Nobody knows if a lesson was ever used | Track whether lessons changed anything |

**The last row is the one to fix first.** If no lesson has ever changed a template, a checklist, an estimate factor or a process, the programme is theatre and should either be redesigned or stopped honestly.

## Step 2: Capture continuously, not at close-out

The best moments are when something has just happened and the people are still present:

- **At each gate review** — see `technical-reviews`. What did we learn getting here?
- **After a significant event** — a qualification failure, a proposal loss, a supplier problem, a successful delivery. Successes are under-captured and are often more transferable, because the reasons are less obvious.
- **At phase transitions**, when a team hands to another.
- **When someone leaves the programme.** An exit conversation with a departing engineer captures more than a close-out workshop with people who arrived last year.
- **At close-out**, for the whole-programme view — but by then it is the summary, not the source.

**Keep a running log during the programme.** A short entry written the week something happened beats a reconstruction six months later, and it costs minutes.

## Step 3: Write a lesson that is actually a lesson

An observation is not a lesson. "The schedule slipped" is an observation. A lesson carries four parts:

1. **What happened**, concretely and with enough context to recognise the situation again.
2. **Why it happened** — the cause, not the symptom. Where it matters, run it properly; `rcca-master` routes the methods.
3. **What to do differently**, stated as an action someone could take.
4. **Who should do it and where it applies** — which role, at which point, on which kind of programme.

Compare:

> *Observation:* "Environmental qualification took longer than planned."
>
> *Lesson:* "We booked chamber time eight weeks before the need date and the lab's queue was fourteen weeks, costing six weeks on the critical path. Qualification lab capacity should be treated as a long-lead procurement: book at the start of DVT planning and carry the booking as a schedule risk until confirmed. Applies to any programme with formal environmental or EMC qualification — see `ruggedization-and-environmental-qual`."

The second is longer and it is the only one anyone can act on.

**Be specific about decisions and conditions while staying blameless about people.** Blameless means we do not assign fault to an individual; it does not mean we remove the specifics of what was decided and what the conditions were. A lesson stripped of specifics to protect feelings has been stripped of its content.

**Capture what worked.** Practices that saved a programme are as transferable as the ones that hurt it, and are recorded far less often.

## Step 4: Put the lesson where the work happens

**This is the step that determines whether any of it matters.** A repository requires someone to remember to search it, which requires knowing the lesson exists — the exact thing they lack.

Push the lesson into the artifact instead:

| Lesson about | Goes into |
| --- | --- |
| An estimating assumption that was wrong | The estimating factors and the BOE checklist — `cost-estimating-and-boe` |
| A schedule item nobody allowed for | The schedule template and health checks — `wbs-and-scheduling` |
| A risk that materialised | The standard risk register starting set — `risk-management` |
| A review that missed something | The gate's entry and exit criteria — `technical-reviews` |
| A design mistake | The design checklist, or a requirement |
| A process gap | The process asset, via corrective action — `quality-management-system` |
| A proposal weakness | The proposal review checklist — `proposal-writing` |
| A supplier problem | Supplier qualification criteria — `teaming-and-subcontracts` |

**The best lessons learned system is one where the lesson changes the template**, and nobody has to remember it — the next programme inherits it by using the standard artifact. `quality-management-system` provides the mechanism: a lesson becomes a corrective action against a process asset, with effectiveness verified.

**Where a lesson cannot be pushed into an artifact**, it needs a retrieval trigger: attached to a phase, a checklist item that says "review lessons for this gate", or a person whose role is to bring them. Without a trigger it will not be found.

## Step 5: Run the session so it produces something

- **Prepare from data**, not from memory — variance reports, the risk register, change history, test results. Memory reconstructs a narrative; the data shows what happened.
- **Get the range of roles.** Engineering, programme, contracts, quality, and where possible the customer. The most valuable lessons sit at the seams between them.
- **Separate observation from cause from action**, explicitly. Groups conflate all three and produce a list of complaints.
- **Timebox and prioritise.** Five lessons that change something beat forty that are filed.
- **Assign each lesson an owner and a specific change**, before anyone leaves the room. `technical-workshop-facilitation` covers running the session; the decisions-and-actions discipline is the same.
- **Say the uncomfortable ones.** A session that produces only safe lessons has captured the ones nobody needed.

## Step 6: Close the loop

- **Track each lesson to the change it produced.** Not to "captured" — to a modified template, checklist, process or requirement.
- **Report how many lessons changed something**, periodically. It is the only honest measure of the programme.
- **Retire lessons that have been absorbed.** Once the change is in the standard artifact, the lesson has done its job and does not need to sit in a list forever.
- **Feed the estimating and risk data back.** Actual durations, actual costs and risks that materialised are the most valuable output a completed programme produces, and they belong in the next estimate rather than in a document.

## Where this sits

`incident-response` runs postmortems on live operational incidents. The RCCA family, routed by `rcca-master`, finds root cause on a specific failure. This covers what a programme learned across its life — different scope, different timing, different audience.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Captured at close-out only | Details gone, people dispersed | Capture at gates and after events |
| Observations recorded as lessons | Nothing actionable | Four parts: what, why, what to do, who |
| Over-generalised for comfort | Could apply to any programme | Blameless about people, specific about decisions |
| Filed in a repository | Never retrieved | Push into templates and checklists |
| No owner, no change | Captured and forgotten | Owner and a specific artifact change per lesson |
| Only failures captured | What worked is lost | Record successful practices too |
| Never measured | Nobody knows if it works | Count lessons that changed something |
| Actuals not fed back | Next estimate repeats the error | Durations, costs and realised risks into the estimating base |

The honest one: if you cannot name a template, checklist or estimating factor that changed because of a lesson in the last year, this programme is not working — and saying so plainly is more useful than running another session.
