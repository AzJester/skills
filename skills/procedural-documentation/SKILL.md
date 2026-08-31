---
name: procedural-documentation
description: Write instructions someone has to follow while doing something. Use when producing a procedure, operator or maintenance instruction, work instruction, standard operating procedure, runbook or installation guide, when placing warnings and cautions, when doing task analysis before writing steps, or when a procedure keeps being performed incorrectly. Covers the conventions of procedural writing, which differ from explanatory documentation.
---

# Procedural documentation

A procedure is not read. It is *used*, by someone whose hands are busy, who is looking away from the page, and who may be tired, under time pressure, or working in bad light. Every convention here exists because a procedure that reads well can still be performed wrongly.

`documentation-architect` covers the Diátaxis quadrants and where procedures sit among the other document types. This covers what a procedure has to do to be safe and repeatable once written.

## Step 1: Task analysis before any writing

The most common defect is a procedure that describes what the author knows rather than what the performer does. Task analysis is the cheap correction.

Establish, in order:

1. **Who performs this** — training, qualification, certification. A step that assumes unstated knowledge is a step that fails intermittently, which is the worst way to fail.
2. **What conditions must hold before starting** — system state, permissions, environmental conditions, whether anything must be de-energised, safed, or backed up.
3. **What is needed** — tools, parts, consumables, credentials, software versions. Discovered mid-procedure, a missing item means an abandoned task in a partially disassembled state.
4. **The actual sequence** — observed or walked through, not recalled. Experts skip steps they no longer notice performing.
5. **What "done" looks like** — the observable end state, and how the performer confirms it.
6. **What can go wrong**, and at which step. This drives warning placement and the off-nominal branches.

**Walk the procedure with someone who has not done it.** This finds more defects than any review. Where they hesitate is where a step is missing.

## Step 2: Structure

Every procedure carries the same frame, whatever the local template calls it:

| Element | Contains |
| --- | --- |
| Purpose and scope | What this accomplishes and when it applies |
| Performer | Who is qualified to do this |
| Safety summary | Hazards present anywhere in the procedure, before any step |
| Prerequisites | Conditions that must hold before starting |
| Tools and materials | Everything needed, with identifiers |
| Steps | The numbered sequence |
| Verification | How to confirm the end state is correct |
| Recovery | What to do if a step fails, or where to go |

**The safety summary goes before the steps and repeats at the point of hazard.** A performer who reads the summary at the start and meets the hazard fifteen steps later needs it again there.

## Step 3: Writing the steps

**One action per step.** The single most important rule. "Remove the four bolts and lift the cover clear" is two actions; under interruption the second is what gets lost. If a step contains "and", check whether it is two steps.

**Imperative mood, active voice, second person implied.** "Set the switch to OFF." Not "The switch should be set to OFF", which does not say to do it now, and not "The technician sets the switch", which is a description of someone else.

**Sequential numbering, and the numbers mean order.** Substeps only where a step genuinely decomposes. Three levels of nesting means the task should be split into two procedures.

**Location before action.** "On the rear panel, set the MODE switch to STANDBY." The performer must find the thing before being told what to do to it; the reverse order makes them re-read.

**Name controls and indicators exactly as they are labeled**, including case and abbreviation. A procedure saying "power switch" for a control labeled `PWR` creates a moment of doubt at the exact wrong time.

**State the observable result** for any step whose success is not obvious. "Set the breaker to ON. The green READY lamp illuminates." Without it, the performer cannot tell a completed step from a failed one, and carries the failure forward.

**Conditional steps state the condition first.** "If the READY lamp does not illuminate, go to step 14." Condition first lets the performer skip the step in one read when it does not apply.

**No forward references to unexplained things.** A step that depends on something described later is a step performed on a guess.

## Step 4: Warnings, cautions and notes

A hierarchy, and using the wrong level dilutes all of them.

| Signal | Means | Consequence of ignoring |
| --- | --- | --- |
| **WARNING** | Hazard to people | Injury or death |
| **CAUTION** | Hazard to equipment, data or mission | Damage or loss |
| **NOTE** | Information that aids performance | Inconvenience or inefficiency |

Four rules that decide whether they work:

**Placement is before the step, never after.** A warning below the step it protects is read after the hazard has been met. This is the most common and most serious defect in procedural writing.

**State the hazard, the consequence, and the avoidance.** "WARNING: Capacitors retain charge for up to five minutes after power removal. Contact can be fatal. Verify discharge with a meter before touching terminals." A warning that only says "high voltage" leaves the performer to infer what to do about it.

**Never put an instruction only in a NOTE.** Notes get skipped. Anything that must be done is a step.

**Do not inflate.** A CAUTION on a step where nothing is damaged trains the performer to skim them, and the one that mattered goes with the rest.

Where a project follows a formal standard for technical manuals — MIL-STD-40051 for DoD technical manuals, or S1000D for structured data-module authoring — that standard governs signal-word wording, placement and format. Read it before writing; the conventions above are consistent with the intent but the standard's specifics are binding.

## Step 5: Verification and recovery

**Verification is a step, not a hope.** End every procedure with an observable confirmation of the intended end state — and where the procedure changes something that can be checked, verify it there rather than only at the end.

**Recovery paths belong in the procedure, not in the performer's head.** For every step that can fail in a foreseeable way, say what to do: retry, branch to another step, stop and escalate, or restore and abort. A procedure with no failure path assumes success, and gets abandoned mid-task the first time reality disagrees.

**Say when to stop.** "If the value is outside the range in Table 3, stop and contact the responsible engineer" is a real instruction. Without an explicit stop condition, a performer under schedule pressure will improvise, and the improvisation will not be recorded.

## Step 6: Test it by having someone follow it

The only real validation. Give the procedure to a qualified performer who has not done this task and watch without helping.

- Every question they ask is a defect.
- Every place they hesitate is an ambiguity.
- Every step they perform differently from the intent is a wording problem, not a performer problem.
- If they finish and the end state is wrong, the verification step is missing or too weak.

Resist explaining. The moment you answer a question aloud, you have lost the finding.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Multiple actions per step | Steps get partially completed | One action per step |
| Warning after the step | Read too late to help | Warnings precede the hazard |
| Instruction hidden in a NOTE | Skipped consistently | Anything mandatory is a step |
| Signal-word inflation | Cautions everywhere, ignored | Reserve levels for real consequence |
| Unstated prerequisites | Task abandoned mid-way | Prerequisites and materials up front |
| No observable result | Failures carried forward silently | State what the performer should see |
| No recovery path | Improvisation, unrecorded | Name the failure branch and the stop condition |
| Written from memory | Expert's steps, not the performer's | Task analysis, then walk it with a novice |

The honest one: a procedure nobody has performed from the page is a draft, however carefully it was written.
