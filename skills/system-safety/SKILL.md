---
name: system-safety
description: Run a system safety program and manage hazards to an accepted risk. Use when identifying and tracking hazards, assessing safety risk on a severity and probability matrix, applying the mitigation order of precedence, determining who must accept a residual risk, writing a system safety program plan or safety assessment report, or assessing software contribution to safety. Uses fault-tree-analysis and fmea-analysis as techniques inside a program discipline.
---

# System safety

`fault-tree-analysis` and `fmea-analysis` are analysis techniques. This is the program that decides which hazards to analyze, what to do about them, and — the part most often mishandled — **who is allowed to accept the risk that remains**.

On DoD programs a system safety process is normally a contractual requirement, and MIL-STD-882 is the usual reference. Read the version and tailoring the contract invokes; what follows is the substance and the judgment, not a substitute for the standard.

The failure this exists to prevent is a hazard analysis performed, documented, and then not connected to any decision — hazards identified, residual risk never formally accepted by anyone with the authority to accept it.

## Step 1: Identify hazards, from more than one direction

A hazard is a condition that could result in harm — to people, equipment, or the environment. Finding them is the part that most determines whether the program is worth anything, and single-method searches miss consistently.

Use several lenses:

- **Energy sources.** Electrical, mechanical, thermal, chemical, radiation, stored pressure, gravity. Anything that can do work can do harm.
- **Functional failure.** What if this function fails, operates when it should not, or operates at the wrong time or magnitude? `fmea-analysis` systematises this from the bottom up.
- **Top-down from the mishap.** Start from the outcome you must prevent and work backwards — `fault-tree-analysis` is exactly this.
- **Lessons learned.** Mishaps and near-misses on similar systems. The most productive source and the most often skipped.
- **Interfaces and transitions.** Between subsystems, between operating modes, between human and machine. Hazards concentrate at boundaries — see `interface-control`.
- **The human in the loop.** Not "operator error" as a cause, but the design conditions that make the error likely. See `human-systems-integration`.

**Record every hazard in a tracking system from the moment it is identified**, with a unique identifier, and keep it open until it is formally closed. The hazard tracking log is the program's memory and the artifact an authority will ask to see.

## Step 2: Assess severity and probability

Hazards are assessed on two axes, combined into a risk level. The categories below follow the usual defense convention; use the exact definitions and matrix the contract invokes.

| Severity | Roughly |
| --- | --- |
| **Catastrophic** | Death, permanent total disability, irreversible major environmental damage, loss of the system |
| **Critical** | Permanent partial disability, serious injury, reversible major environmental damage, major system damage |
| **Marginal** | Injury or occupational illness resulting in lost work days, moderate damage |
| **Negligible** | Minor injury or damage not requiring lost work days |

| Probability | Roughly |
| --- | --- |
| **Frequent** | Likely to occur often in the life of an item |
| **Probable** | Will occur several times |
| **Occasional** | Likely to occur sometime |
| **Remote** | Unlikely but possible |
| **Improbable** | So unlikely it can be assumed it will not occur |
| **Eliminated** | Incapable of occurrence — reserved for hazards genuinely designed out |

The matrix combines them into risk levels — commonly high, serious, medium and low.

**Severity is a property of the hazard; probability is a property of the design.** Mitigation usually moves probability. A catastrophic hazard mitigated to improbable is still catastrophic in severity, and that matters for who accepts it.

**Assess before and after mitigation.** Initial risk justifies the effort; residual risk is what gets accepted. Recording only one of them hides either the work done or the exposure remaining.

## Step 3: Mitigate in the order of precedence

The order is not advisory. Mitigations lower down the list are weaker, and a safety case resting on them is weaker.

1. **Eliminate the hazard by design.** Remove the energy source, delete the function, change the architecture. The only mitigation that cannot fail or be ignored.
2. **Reduce risk through design alteration.** Lower the energy, add margin, fail safe, remove single points of failure.
3. **Incorporate engineered features or devices.** Interlocks, guards, relief valves, redundancy that operates without human action.
4. **Provide warning devices.** Alarms and indicators — which require a human to notice and act correctly.
5. **Procedures, training and protective equipment.** The weakest, because it depends entirely on a person doing the right thing under conditions you cannot control.

**The default failure is jumping to step 5.** A procedure is cheap, fast and satisfies the paperwork, and it is why "the manual says not to do that" appears in mishap reports. Where a hazard is mitigated by procedure alone, say so explicitly in the risk acceptance — the accepting authority is entitled to know the mitigation is a warning label.

**Verify each mitigation.** A control credited in the analysis but never tested is an assumption. Every mitigation needs a verification method and an event, feeding `verification-validation` like any other requirement.

## Step 4: Risk acceptance is an authority decision, not an engineering one

This is the step that distinguishes a safety program from a safety analysis.

**Residual risk is accepted by a named authority, at a level set by the risk.** Higher risk requires higher authority — on defense programs this is defined, escalating to senior acquisition executives for the most serious risks. The engineering team's job is to characterize the risk honestly and present it; it is not to decide that the residual risk is acceptable.

Three things that go wrong here:

**Risk is understated to keep the acceptance at a convenient level.** Adjusting a probability from occasional to remote without a design change to justify it moves the decision to a lower authority. This is the most serious failure mode in the discipline, and it is usually done gradually and with good intentions.

**Acceptance is never actually obtained.** The analysis is complete, the report is delivered, and no authority ever signed. The program then operates with unaccepted risk, which is a finding and, after a mishap, considerably worse.

**Acceptance is treated as permanent.** It is valid for the configuration and usage assessed. A design change, a new operating environment or a new user population reopens it — which is why safety hazards belong in the impact assessment of `configuration-management` change control.

## Step 5: Software, and the honest limits of probability

Software does not fail randomly, so probability categories built for hardware do not transfer.

The usual approach is to assess software by **the degree of control it exerts over a hazard** and by the severity of what happens if it behaves incorrectly, and to assign a level of rigor — how much analysis, review, test and independence the software requires — rather than a failure rate.

- **Autonomous control of a catastrophic hazard demands the highest rigor.** Software that can command the hazardous outcome without a human or hardware interlock in the path is the case that drives everything.
- **Independence matters more than volume.** Analysis done by the team that wrote the code finds less.
- **Prefer hardware or human interlocks for catastrophic hazards** where the architecture allows it. A mitigation that does not depend on software correctness is stronger than one that does.

The same reasoning applies to AI components, and more sharply — an AI system's behavior on inputs outside its evaluated envelope is not characterized by its test results. Where an AI component sits in a safety path, define the operating envelope explicitly and design the behavior outside it. See `ai-governance` and `ai-evaluation`.

## Step 6: The artifacts, and keeping them alive

- **System safety program plan** — how the program will be run, by whom, with what analyses and what schedule.
- **Hazard tracking log** — every hazard, its status, its mitigations, its verification, its acceptance. Living, not a snapshot.
- **Safety assessment report** — the case that residual risk is understood and accepted, at the point of a decision.
- **Inputs to the technical reviews** — see `technical-reviews`. Safety status is gate criteria, not a parallel activity.

**Integrate with program risk rather than running a separate universe.** `risk-management` carries program exposure; safety carries mishap risk. They use different scales for good reasons, but a safety hazard with program consequences belongs visible in both.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Analysis disconnected from decisions | Documents delivered, no acceptance obtained | Every residual risk formally accepted by the right authority |
| Procedure as first-line mitigation | "The manual says not to" in the mishap report | Work the order of precedence from the top |
| Probability adjusted to lower the authority | Risk quietly reclassified without design change | Justify every probability with a design basis |
| Single-method hazard identification | Whole classes of hazard missed | Several lenses, including lessons learned |
| Mitigations unverified | Credited controls never tested | Verification method and event per mitigation |
| Acceptance treated as permanent | Change invalidates it silently | Safety in the change impact assessment |
| Software assessed by failure rate | A number with no meaning | Assess by control authority and assign rigor |
| Hazard log as a snapshot | Stale within a month | Living tracking system, reviewed at gates |

The honest one is the third. Understating a probability is the easiest thing in this discipline to do quietly, it moves the decision to someone with less authority, and it is exactly what an investigation reconstructs afterwards.
