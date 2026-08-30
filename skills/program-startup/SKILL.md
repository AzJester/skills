---
name: program-startup
description: Stand up a programme after award. Use when planning transition-in or phase-in, working the first ninety days of a new contract, extracting requirements and deliverables from the awarded contract, staffing against clearance lead times, receiving government-furnished property or information, establishing the performance measurement baseline, preparing for an integrated baseline review, or taking over from an incumbent.
---

# Programme startup

Winning is not standing up. The transition period is short, mostly unfunded relative to the work in it, and the decisions made in it constrain everything that follows — yet it is routinely treated as an administrative gap between award and real work.

The failure this exists to prevent is a programme that spends its first quarter discovering what it agreed to. Every hour of that comes out of the schedule, and it comes out at the point where there is least margin to give.

## Step 1: Read the contract you actually won

Not the proposal. The awarded contract, including everything incorporated by reference, and including every negotiated change from what was proposed.

Extract, systematically:

- **Every deliverable**, with its due date, format and whether it requires government approval. Build the CDRL calendar now — see `sow-and-pws`. The first deliverables are usually due within thirty days and are usually missed.
- **Every requirement** in the SOW or PWS, shredded into single obligations with an owner. Same discipline as the compliance matrix in `proposal-writing`, and frequently the same matrix, updated.
- **Every performance standard** and how it will be surveilled. What gets measured, from when, and against what.
- **The clauses that change how you work** — data rights, security, cybersecurity, reporting, flow-downs. See `contract-vehicles-and-clauses`.
- **Government-furnished property, information and facilities**, with the dates each is promised.
- **Key personnel commitments**, and what substitution requires.

**Reconcile the contract against the proposal and record every difference.** Where the negotiated scope differs from what was priced, that gap is either a change request or an unfunded commitment, and it should be identified in week one rather than at the first variance report.

## Step 2: Staff it, against real lead times

**Clearance lead time is usually the critical path, and it is usually discovered late.** Investigation and adjudication run on timescales that do not compress for programme urgency. Start every clearance action immediately, including for people whose start date is months away — see `industrial-security`.

- **Key personnel first.** They were named in the proposal, and the customer expects them. Substitution normally requires approval and is a poor first impression.
- **Confirm proposed staff are still available.** Between proposal and award, people leave and get committed elsewhere. Verify rather than assume.
- **Sequence hiring against the schedule**, not evenly. The staffing profile in `wbs-and-scheduling` says who is needed when.
- **Name the accountable people early** — control account managers, technical leads, the person who owns each CDRL. Ambiguity here persists for the life of the programme.

## Step 3: Establish the baselines

Three baselines get set now, and each is much harder to establish later.

**Performance measurement baseline.** Scope decomposed to work packages, budgeted, scheduled, with control account owners — `wbs-and-scheduling` builds it and `earned-value-management` measures against it. Where an integrated baseline review is required, it typically happens within a defined window after award, and it examines whether the baseline is realistic and understood by the people who own it. Preparing for it properly is preparing to execute; treating it as an inspection to survive produces a baseline that passes and then fails.

**Technical baseline.** What the system is, as agreed at award. `configuration-management` establishes it and controls what happens to it. Without it, requirement interpretations drift and there is no record of what changed.

**Risk register, populated on day one.** The pursuit risks from `capture-management` and `risk-management` carry straight into delivery. A register started fresh at award discards everything the capture team learned.

## Step 4: Receive what you were promised

**Verify government-furnished property and information on receipt, against the list.** Not later. GFP that arrives late, incomplete or non-functional is one of the most common sources of legitimate schedule claims — and the claim depends on having documented what arrived, when, and in what condition.

**Chase what has not arrived, in writing.** An informal reminder does not establish a record. This feels adversarial in the first month and is the single most valuable habit when the schedule is questioned in month nine.

**The same applies to access**: networks, facilities, systems, badges. Access delays are schedule delays and they should be tracked as such.

## Step 5: Set the customer relationship deliberately

The working pattern established in the first month is the one you keep.

- **Hold a kickoff that establishes how you will work**, not one that re-presents the proposal. Who talks to whom, what the reporting rhythm is, how issues escalate, what the customer will see and when.
- **Agree the communication protocol**, including who may direct work. Informal direction from someone without authority is how unfunded scope enters a programme, and it is far easier to prevent in week one than to unwind in month six.
- **Deliver something early and well.** The first deliverable sets expectations disproportionately. It is usually small and it is always noticed.
- **Report honestly from the first report.** A programme that reports green until it cannot has spent the credibility it needs when it has a real problem.

## Step 6: Transition from an incumbent

Where you are replacing someone, the transition is a distinct problem with a distinct risk: the knowledge you need is held by people whose jobs you took.

- **Assume documentation is incomplete.** It always is. Plan knowledge capture around people and systems rather than around a handover pack.
- **Identify the undocumented dependencies** — the manual step someone does monthly, the credential in one person's head, the informal arrangement with another team. These are what break after the incumbent leaves.
- **Consider hiring incumbent staff** where it is permitted and appropriate. It is frequently the fastest and lowest-risk knowledge transfer available.
- **Plan for the capability dip.** There will be one. Say so in the transition plan rather than promising continuity you cannot deliver, and put the mitigation where it is visible.

## Step 7: The first ninety days, in order

| When | What must be true |
| --- | --- |
| **Week 1** | Contract read and shredded; CDRL calendar built; clearance actions started; key personnel confirmed; kickoff scheduled |
| **Weeks 2–4** | Accountable owners named; risk register populated; GFP and access status tracked in writing; first deliverables in progress |
| **Weeks 4–8** | Baselines established — performance measurement, technical, risk; tools and environments stood up; reporting rhythm running |
| **Weeks 8–12** | Baseline review passed where required; first performance reports issued; transition complete or its remaining gaps named |

**By the end of it, the programme should be boring.** Startup is finished when nobody is discovering obligations any more.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Working from the proposal | Scope differences found at the first variance | Reconcile contract against proposal in week one |
| CDRL calendar built late | First deliverables missed | Build it in week one |
| Clearances started at need date | Staffing is the critical path | Start immediately, for everyone |
| Baseline as an inspection to survive | Passes review, fails in execution | Build a baseline the owners believe |
| GFP receipt undocumented | No basis for a schedule claim | Verify against the list; chase in writing |
| Informal direction accepted | Unfunded scope accumulates | Agree who may direct work, at kickoff |
| Fresh risk register | Capture knowledge discarded | Carry the pursuit register forward |
| Continuity promised on transition | Dip happens anyway, unmanaged | Plan for it and say so |

The honest one: nearly every problem a programme has in its second year is traceable to something nobody had time to do properly in its first month.
