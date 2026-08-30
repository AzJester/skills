---
name: wbs-and-scheduling
description: Build the work breakdown structure and the schedule a programme is managed against. Use when decomposing scope into a WBS, writing a WBS dictionary, setting up control accounts and work packages, building or reviewing an integrated master schedule, assessing schedule health and critical path, running a schedule risk analysis, or diagnosing why a schedule keeps slipping without anyone predicting it. Builds the artefacts earned-value-management reads.
---

# WBS and scheduling

`earned-value-management` requires "scope decomposed to work packages via a WBS" and tells you to read "the critical path from the IMS". This builds both. Without them EVM has nothing to measure and a programme has no way to know it is late until it is.

The failure this exists to prevent is a schedule that is a list of dates rather than a model of the work. A list of dates cannot tell you what happens when something slips, which is the only question a schedule exists to answer.

## Step 1: Decompose the product, not the organisation

**The WBS is product-oriented.** Its elements are deliverables and the work to produce them — hardware, software, data, services — not departments, not phases, not the org chart.

This is the rule most often broken and it is broken for an understandable reason: organising by team is easier and matches how work is assigned. But an org-shaped WBS cannot answer "what did this deliverable cost", cannot survive a reorganisation, and produces control accounts that no single person can be accountable for.

For defense materiel, MIL-STD-881 defines the upper-level structure by commodity type — aircraft, space, ground vehicle, and so on — and using it is normally a contractual requirement rather than a preference. Read the applicable appendix before inventing structure.

**The 100% rule.** The children of any element sum to exactly that element — all of it, and nothing beyond it. Work that appears nowhere in the WBS is work nobody planned, budgeted or scheduled, and it is the standard mechanism by which programmes discover scope late.

**Decompose to where a work package makes sense**, not uniformly. Depth follows risk and manageability, as with modelling depth in `mbse-sysml`. A uniformly deep WBS has spent planning effort where nothing depended on it.

**Write the WBS dictionary.** One entry per element: what it includes, what it explicitly excludes, and its deliverable. The exclusions matter more than the inclusions, because that is where the argument happens later. A WBS without a dictionary is a set of labels that different people read differently.

## Step 2: Control accounts and work packages

| Level | Is | Owned by |
| --- | --- | --- |
| **Control account** | Where a WBS element meets an organisational element — the point where cost, schedule and technical scope are managed together | One control account manager |
| **Work package** | Discrete, schedulable work within a control account, with a measurable output | The CAM, executed by the team |
| **Planning package** | Far-term work not yet decomposed, budgeted but not detailed | The CAM, converted before it starts |

Three disciplines:

**One owner per control account.** Not a committee. If two people are accountable, nobody is.

**Work packages have discrete, measurable output.** "Design the subsystem" cannot be objectively assessed at 40% complete. "Deliver the reviewed interface specification" can. This choice determines whether earned value is honest or invented — see `earned-value-management` on measurement methods.

**Rolling wave is normal and should be deliberate.** Near-term detailed, far-term in planning packages, converted on a stated cadence. What is not acceptable is planning packages that are still planning packages the month the work starts.

## Step 3: Build a schedule that models the work

A schedule is a network of activities connected by logic. Everything useful comes from the logic; dates are an output, not an input.

**Every activity has a predecessor and a successor**, except the true start and finish. An activity floating free of the network is invisible to the critical path and will slip without anyone noticing.

**Use real logic, sparingly typed.** Finish-to-start is the default and should dominate. Start-to-start and finish-to-finish are legitimate but each one is a claim about how the work actually overlaps; finish-to-start with a lag is often a modelling shortcut hiding an activity nobody wanted to name.

**Hard constraints destroy a schedule's predictive value.** "Must finish on" dates override logic — the schedule then shows the date you typed rather than the date the work implies, and it stops warning you. Deadlines belong as milestones with float measured against them, not as constraints on the work.

**Durations come from the estimate**, and the estimate comes from `cost-estimating-and-boe`. A duration invented independently of the hours produces a schedule and a budget that disagree, and the disagreement surfaces at the first performance report.

**Resource-load it, at least at the control account level.** A schedule that is logically perfect and requires forty cleared engineers in a month when twelve exist is fiction. This is where clearance lead times and hiring capacity enter the plan rather than surprising it later.

## Step 4: Read the critical path, and check the schedule is honest

**The critical path is the longest logic path**, and it determines the finish date. Everything else has float. Managing anything other than the critical path does not move the end date.

**Total float versus free float.** Total float is how much an activity can slip before the programme finishes late; free float is how much before its own successor is affected. Confusing them produces surprised project managers.

**Near-critical paths matter.** A path with five days of float is one bad week from being the critical path. Track the top several paths, not just the first.

Health checks worth running before trusting any schedule — the DCMA 14-point assessment formalises these and is commonly required on defense programmes:

- [ ] **Missing logic** — activities without predecessors or successors
- [ ] **Leads** (negative lags) — almost always a modelling error
- [ ] **Excessive lags** — usually an unnamed activity in disguise
- [ ] **Relationship types** — finish-to-start should dominate
- [ ] **Hard constraints** — minimal, justified, and never on work activities
- [ ] **High float** — activities with implausibly large float usually indicate missing logic
- [ ] **Negative float** — the schedule is already late and is telling you
- [ ] **Long durations** — activities longer than a reporting period cannot be assessed
- [ ] **Invalid dates** — work forecast in the past, or actuals in the future
- [ ] **Resources** — assigned where the schedule is resource-driven
- [ ] **Missed tasks** — slipping against baseline
- [ ] **Critical path test** — insert a large delay on a critical activity; the finish date must move by the same amount. If it does not, the network is broken
- [ ] **Baseline execution and completion indices** — whether work is being finished as planned

The critical path test is the one to run first. A schedule that fails it is not a model of anything, and every number derived from it is decoration.

## Step 5: Schedule risk analysis

A deterministic schedule gives one date, with a confidence level nobody has calculated and everybody assumes is high.

- Assign duration ranges — optimistic, most likely, pessimistic — to the activities that drive the outcome, not to all of them.
- Model correlation where it exists. Independent sampling of activities that share a common cause understates risk badly.
- Run the simulation and report a confidence level: the date you would commit to at 50% versus 80% are usually far apart, and the gap is the honest measure of schedule risk.
- **Report the drivers, not just the distribution.** Which activities most influence the finish date is the actionable output.

Feed the result into `risk-management` and, where reserve is priced, into `cost-estimating-and-boe`.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Org-shaped WBS | Cannot cost a deliverable; breaks on reorg | Decompose the product |
| No WBS dictionary | Scope arguments with no arbiter | Write inclusions and exclusions per element |
| Effort-based work packages | Earned value invented, not measured | Discrete, measurable output per package |
| Dates as inputs | Schedule stops predicting | Logic drives dates; deadlines are milestones |
| Hard constraints everywhere | Slip invisible until it is late | Remove them; measure float against milestones |
| Open-ended activities | Invisible to the critical path | Every activity has a predecessor and successor |
| Unresourced schedule | Physically impossible plan | Resource-load and check against capacity |
| Single-point commitment | Confidence level unknown | Schedule risk analysis; commit at a stated confidence |
| Planning packages never converted | Detail arrives after the work starts | Rolling wave on a fixed cadence |

The honest one: most schedules are built to be approved rather than to be true, and the difference is invisible on the day it is approved and obvious eighteen months later.
