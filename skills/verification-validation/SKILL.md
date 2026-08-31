---
name: verification-validation
description: Plan and run verification and validation for a system. Use when deciding how each requirement will be proven, building a verification cross-reference matrix (VCRM or RVTM), choosing between inspection, analysis, demonstration and test, planning a test campaign, judging whether evidence actually closes a requirement, or answering whether the system was built right and whether it is the right system.
---

# Verification and validation

Two different questions that get conflated, and conflating them is how programs deliver a system that meets every requirement and satisfies nobody.

- **Verification** — did we build the system right? Compares the system to its *requirements*. Objective, and the answer is pass or fail.
- **Validation** — did we build the right system? Compares the system to the *stakeholder need it was meant to serve*. Judgemental, and the answer can be "yes, and it still does not solve the problem".

A requirement can verify clean and validate badly. That is not a paradox; it means the requirement was wrong, and finding that late is the expensive failure this discipline exists to prevent.

## Where this sits

`requirements-dev` produces the requirements and tags each with a nominal method. This skill turns those tags into a verification program: what evidence, produced how, judged against what, closed by whom. Feed its output into `technical-reviews` — a TRR with no verification plan behind it is theater.

## Step 1: Choose the method, per requirement

Four methods, in ascending cost. Choose the cheapest one that actually produces belief.

| Method | What it is | Fits | Evidence produced |
| --- | --- | --- | --- |
| **Inspection** | Look at it. Examine the item, drawing, or code without operating it. | Physical characteristics, markings, workmanship, presence of a feature | Inspection record, photograph, checklist |
| **Analysis** | Reason about it. Modeling, simulation, calculation, or similarity to a qualified item. | Conditions you cannot practically create — lifetime, extremes, statistical margins | Analysis report with assumptions stated |
| **Demonstration** | Operate it and observe. No instrumentation, qualitative. | Operability, human interaction, does-the-thing-happen | Demonstration procedure and observed result |
| **Test** | Operate it under controlled conditions and measure. | Anything with a number in the requirement | Test procedure, instrumented data, pass/fail against criteria |

Two rules that prevent most argument later:

**A requirement whose method is "test" but whose text has no measurable criterion cannot be tested.** Send it back to `requirements-dev`. "The system shall be responsive" has no test; "shall respond within 200 ms at the 95th percentile under 500 concurrent users" does.

**Analysis by similarity needs the similarity argued, not asserted.** Name the qualified item, state how the new application differs, and say why the differences do not matter. An unstated similarity claim is the most common way a verification program quietly develops a hole.

## Step 2: Build the VCRM

The verification cross-reference matrix is the spine. One row per requirement, and no requirement without a row.

Columns: requirement ID, requirement text, method, the level it is verified at (component, subsystem, system), the verification event or procedure, success criteria, evidence artifact, status, and who closes it.

Use `references/vcrm-template.md`. Three checks on it, run before anyone agrees to it:

1. **Every requirement appears exactly once.** A requirement verified in two places gets closed twice and fixed nowhere.
2. **Every verification event traces up to at least one requirement.** An event with no requirement behind it is either scope you invented or a requirement you forgot to write.
3. **The level makes sense.** Verifying a system-level performance requirement at component level proves the component, not the system. Say which level, and say why it is sufficient.

## Step 3: Plan the campaign

Sequence matters. Verification events have prerequisites, and discovering that late costs schedule you do not have.

- Group requirements that share a setup into one event. Test setup cost usually dominates test execution cost.
- Order by what is most likely to fail and most expensive to fix late. Discovering a fundamental problem in the last test is the worst possible ordering.
- Identify what must be verified before the next build, and what can wait. Not everything gates.
- For each event, state what happens on failure: retest, redesign, waive, or accept with deviation. Deciding this in advance stops it being decided under pressure.

## Step 4: Judge evidence honestly

The question is not "did we run the test" but "does this evidence support the claim".

Evidence closes a requirement when: it was produced against the stated success criteria, on the configuration under verification, by a procedure that was followed, and it is retrievable by someone who was not there.

Evidence does **not** close a requirement when it was produced on a different configuration, under conditions more favourable than specified, by a procedure that was modified mid-run without record, or when the result is "it looked fine". Say so and mark it open. A VCRM full of green that nobody believes is worse than one with honest reds, because it removes the signal.

Where a requirement will not be met, the options are redesign, waiver, or deviation — and each is a decision with a named owner, not a status.

The document that delivers these results to a customer is `test-report`.

## Step 5: Validate

Verification finishes and validation begins, and the second one is easy to skip because the first produced a matrix full of green.

Validation asks the stakeholders whose need started this whether the delivered system serves it. Methods are operational demonstration, user trial, scenario walkthrough, or pilot deployment in the real environment.

Three things to look for specifically, because requirements rarely capture them:

- **Emergent behavior.** Properties of the assembled system that no component requirement mentions.
- **The unstated need.** What stakeholders assumed so deeply they never said it. `grilling` is useful here.
- **Fitness in the real environment**, as opposed to the specified one. The specified environment is always cleaner than the real one.

Findings from validation go back to requirements, not to the defect log. A validation failure usually means a requirement was wrong or missing, and filing it as a bug hides that.

## Reference

- `references/vcrm-template.md` — the matrix, its columns, and the completeness checks.
- `references/method-selection.md` — choosing between the four methods, with the arguments that decide borderline cases.
