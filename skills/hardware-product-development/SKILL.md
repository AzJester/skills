---
name: hardware-product-development
description: Develop a physical product through to production. Use when planning a hardware development programme, sequencing build stages from breadboard through EVT, DVT and PVT, deciding what each prototype build must prove, planning board spins and long-lead procurement, running hardware design reviews, or working out why a hardware schedule keeps slipping a spin at a time. Covers the hardware realisation lifecycle; manufacturing-and-npi covers the transition to production.
---

# Hardware product development

Everything else in this repository about running a programme — `wbs-and-scheduling`, `program-startup`, `earned-value-management` — assumes work that can be replanned weekly. Hardware cannot. A board spin costs weeks and money, tooling costs more, and a mistake found at the wrong stage costs a quarter.

**The whole discipline follows from one fact: you get very few iterations.** Software teams learn by shipping and correcting. Hardware teams get three or four real builds before production, and each one has a fixed cost measured in weeks. Everything below is a way of front-loading learning into the cheap part of the programme.

The failure this exists to prevent is discovering a fundamental problem at the design validation build, where the design is frozen, the tooling is cut, and the only options are expensive.

## Step 1: Know what each build stage is for

Each build answers one question. Building without knowing which question wastes the build.

| Stage | Answers | Typical form |
| --- | --- | --- |
| **Breadboard** | Does the concept work at all? | Evaluation boards wired together, nothing like the product |
| **Brassboard** | Does it work in something like the real architecture? | Custom boards, wrong enclosure, right function |
| **Engineering unit** | Does the actual design work? | Real boards, real mechanicals, hand-built |
| **EVT** — engineering validation | Does the intended design meet its functional requirements? | First representative units, small quantity |
| **DVT** — design validation | Does it meet *all* requirements, including environmental and EMC? | Near-final design, production-intent parts |
| **PVT** — production validation | Can it be built repeatably, at rate, on production tooling? | Production line, production tooling, real operators |

Three rules that decide whether the sequence works:

**Do not skip stages to save schedule.** It is the most common compression under pressure and it reliably costs more than it saves, because the problem that would have been found cheaply gets found expensively.

**Each stage has entry and exit criteria written before it starts.** "EVT is done" must mean something specific — see `technical-reviews` for the gate discipline, applied here to build maturity rather than document delivery.

**Qualification testing happens at DVT, not after.** Environmental and EMC qualification are the two disciplines that most often fail late — see `ruggedization-and-environmental-qual` and `emi-emc-and-tempest`. Both need design margin, and design margin cannot be added after the design is frozen.

## Step 2: Front-load the risk, deliberately

The purpose of the early stages is to be wrong cheaply. That only works if you attack the right things first.

- **Identify the three things most likely to sink the design** and test those before anything else. Usually thermal, a new component nobody has used, a radio coexistence problem, or a mechanical constraint that turns out to be immovable.
- **Build test vehicles for single questions.** A thermal mule that is a heater block in the real enclosure answers the thermal question months before the real board exists — and it costs almost nothing. So does a mechanical mock-up for fit and a power board on the bench for the platform interface.
- **Get an EMC pre-scan on the first real board**, on a bench, with near-field probes. Not to pass, but to find out where you are. Cheap, fast, and it is the difference between fixing a radiated emissions problem in layout and fixing it with a shield can and a schedule slip.
- **Measure the environment rather than assuming it.** Where instrumented platform data exists, it beats a specification derived from a category — see `ruggedization-and-environmental-qual` on tailoring.

## Step 3: Plan around long lead and board spins

**Long lead items drive the schedule and are usually identified late.** Connectors, custom mechanicals, castings, displays, anything with an allocation problem, and increasingly anything semiconductor. Identify them at concept, order them before you are confident, and accept scrapping some — it is cheaper than the schedule.

**Budget board spins explicitly, and expect them.** A complex board rarely works fully on the first article. A plan with one spin is a plan with a hidden slip; two to three between first article and DVT is normal. Say so in the schedule rather than discovering it — this is exactly the schedule realism `wbs-and-scheduling` and `cost-estimating-and-boe` are for.

**Design the board so it can be debugged.** Test points, a debug header, the ability to isolate power domains, provision to depopulate or cut a trace. Every one of these is nearly free in layout and each saves a spin.

**Plan bring-up as real work**, with time, people and instruments assigned. First-article bring-up on a complex board takes weeks, not days, and it is where the schedule is either recovered or lost.

## Step 4: Freeze deliberately, and manage what changes after

The design freeze is a decision, not an event that happens when everyone stops changing things.

- **Freeze in stages.** Mechanical interfaces freeze earliest, because tooling and enclosures have the longest lead. Electrical follows. Firmware freezes last and can keep improving — which is exactly why anything that might need changing should be in firmware rather than hardware.
- **After freeze, every change is classified.** Does it affect form, fit, or function? A change that does invalidates qualification testing and may invalidate the baseline — see `configuration-management`, whose change control and physical configuration audit apply directly.
- **Know what a change costs you in re-test.** A component substitution can require re-running environmental or EMC qualification. Understanding that before agreeing to the change is the difference between a decision and a surprise.

## Step 5: Requirements that a hardware team can actually build to

`requirements-dev` covers writing verifiable requirements. Hardware adds specifics that get missed:

- **Every environmental and interface requirement traces to the platform**, not to a category. "Operates in a military vehicle" is not a requirement; the input power characteristics, the temperature range, the vibration profile and the mounting are.
- **Margin is stated, not assumed.** Design margin against a limit is a decision to record, because it is the first thing sacrificed when something else needs room.
- **The verification method matters more than usual** — analysis, similarity, inspection or test, and for hardware the choice determines whether you need a test article and a chamber booking. See `verification-validation`, and book chambers early: qualification lab capacity is a real constraint with lead time.

## Step 6: Where this connects

Hardware development pulls in a wider set of disciplines than software, and most of the schedule risk is at the seams.

| Concern | Skill |
| --- | --- |
| Fitting the envelope — size, weight, power, cooling | `swap-and-thermal-budgeting` |
| Surviving the environment | `ruggedization-and-environmental-qual` |
| Passing EMC and emanations requirements | `emi-emc-and-tempest` |
| Architecture and interface openness | `mosa-and-open-standards` |
| Parts availability across the product's life | `component-selection-and-obsolescence` |
| Building it repeatably | `manufacturing-and-npi` |
| The software on the box | `embedded-firmware-and-secure-boot` |
| Reliability, maintainability, support | `reliability-and-sustainment` |
| Failure analysis during design | `fmea-analysis`, `fault-tree-analysis` |
| Electrical, battery and thermal hazards | `system-safety` |
| Baselines and change after freeze | `configuration-management` |

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Stage skipped to save schedule | Problem found where it is expensive | Keep the sequence; compress within stages |
| Qualification deferred past DVT | No margin left to fix it | Environmental and EMC at DVT, pre-scan far earlier |
| One board spin in the plan | Hidden slip surfaces at first article | Budget two to three; say so |
| Long lead found late | Schedule set by a connector | Identify at concept; order before certainty |
| Undebuggable board | Every problem costs a spin | Test points, debug header, isolation, cut provisions |
| Bring-up unplanned | Weeks of unassigned work | Plan it with people and instruments |
| Freeze as an event | Changes continue informally | Freeze in stages; classify every change after |
| Requirements by category | Design to the wrong environment | Trace every environmental requirement to the platform |

The honest one is the second. Environmental and EMC qualification are where hardware programmes actually fail, they fail at the end, and they fail because the margin needed to pass had to be designed in months earlier.
