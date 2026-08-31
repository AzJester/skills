---
name: test-report
description: Write the report that delivers test results. Use when documenting the outcome of a test event, writing a test report or CDRL test deliverable, presenting results traced to a test plan or VCRM, categorizing deficiencies by operational impact, writing the limitations section, or turning raw test data into conclusions a customer can act on. Sits after test-and-evaluation plans the event and verification-validation judges the evidence.
---

# Test report

Two skills bracket this one. `test-and-evaluation` plans the event and covers reporting *posture* — negative results are results, deficiencies reported by operational impact. `verification-validation` judges whether evidence closes a requirement. Neither writes the document that delivers the results, which is usually the contract deliverable and often the only artifact that outlives the event.

The failure this exists to prevent is a report that presents data instead of findings. A customer receiving 200 pages of plots and no stated conclusion has received the test team's raw material, not its work.

## Step 1: Establish what makes the report credible before writing it

Three things determine whether a reader can trust any number in the report. Get them recorded, or the rest is unverifiable:

**What was tested.** The exact configuration of the article — hardware serial numbers, software versions and build identifiers, configuration baseline reference. Results are only as good as the match between what was tested and what will be fielded; see `configuration-management`. A report whose article configuration is vague cannot support a fielding decision, no matter how good the data is.

**Under what conditions.** Environment, instrumentation and its calibration, operators and their qualification, and any deviation from the plan. Deviations are recorded whether or not they seem to matter — the reader decides that, not the author.

**Against what plan.** The test plan or procedure identifier and revision, and the requirements or objectives each event was intended to address. A result that traces to nothing is data without a question.

## Step 2: Structure

Whatever the governing template or DID calls the sections, a usable test report carries these, in this order:

| Section | Holds | Common defect |
| --- | --- | --- |
| Summary | Objectives, what was found, what it means, in under a page | Written last and shows it; restates scope instead of findings |
| Objectives and scope | What this event set out to determine, and what it did not | Scope inflated to match what was actually run |
| Article configuration | The exact as-tested configuration | Vague, so results cannot be tied to a baseline |
| Method | Procedure, instrumentation, environment, deviations | Deviations omitted because they "did not matter" |
| Results | The data, organized by objective | Organized by test event rather than by question |
| Analysis | What the data means, with uncertainty | Skipped; the reader is left to infer |
| Deficiencies | Findings, categorized, with impact | Categorized by component instead of by consequence |
| Limitations | What this report does not establish | Missing — the defect that most damages credibility |
| Conclusions | Answers to the objectives, and only those | Recommendations creeping past the evidence |
| Recommendations | What should happen next, separated from conclusions | Merged with conclusions so the reader cannot tell them apart |

**Write the summary last and treat it as the deliverable.** For most readers it is the whole report. It states what was tested, what was found, and what it means for the decision in front of them — not what the document contains.

## Step 3: Present results so they answer questions

**Organize by objective, not by chronology.** The reader wants to know whether the system meets its requirement, not what happened on Tuesday. Test-by-test narration forces them to assemble the answer themselves.

**Every result traces to its objective and its requirement.** A results table with a traceability column feeds straight into the VCRM — see `verification-validation`.

**Give numbers their uncertainty.** A measured value with no tolerance, no sample size, and no measurement uncertainty invites a precision the data does not support. Where a statistical claim is made, state the method and the confidence — see `applied-statistics`.

**Distinguish measured from derived from estimated.** The same discipline `measures-of-effectiveness` applies to tracking charts applies here. A reader who cannot tell which numbers were observed cannot weight them.

**Graphs answer a question in their caption.** "Figure 5-3. Latency exceeds the 200 ms threshold above 40 concurrent users." Not "Figure 5-3. Latency vs. Load." See `technical-editing` on captions and `data-storytelling` on presenting results to non-specialists.

**Include the failures at the same fidelity as the successes.** A report where passing tests get tables and failing tests get a sentence has told the reader what the author wanted to be true.

## Step 4: Deficiencies, categorized by consequence

The single most useful thing a test report does is tell the program which findings matter.

**Categorize by operational impact, not by the component involved.** A finding that stops the mission and one that annoys the operator are different findings even if both are in the same subsystem. Where the program has a defined deficiency classification, use it; where it does not, state the scheme you used in the report.

Each deficiency carries: what was observed, the conditions that produce it, how often it occurred out of how many attempts, the operational consequence, and any workaround. Reproducibility is part of the finding — a defect seen once in forty runs and one seen every time are different problems, and "intermittent" without the ratio is not a description.

**Do not diagnose in the deficiency.** What was observed is a test finding; why it happened is engineering analysis and may be wrong. Keeping them separate lets the design team investigate without inheriting a hypothesis. Where a cause is known, say so and label it as such — see the RCCA skills for doing that properly.

## Step 5: Limitations, written honestly

The section that decides whether the report survives scrutiny. State what this event does **not** establish:

- Conditions not tested — environments, loads, configurations, threat conditions
- Objectives not met, and why
- Instrumentation or fidelity constraints that bound the result
- Sample sizes too small to generalize from
- Deviations from the plan and what they cost
- Anything tested in a surrogate, simulated or laboratory environment that has not been shown to represent the operational one

A reader who finds a limitation the report did not disclose discounts the whole document, and is right to. A report that names its own limits is more useful *and* more trusted than one that quietly hopes nobody asks.

**Negative and null results are reported at full strength.** A test that found nothing usually means the test was not stressing; reporting it as success is how problems reach the field.

## Step 6: Conclusions that stay inside the evidence

**Conclusions answer the objectives. Nothing else.** One conclusion per objective, each traceable to results in the report. A conclusion that requires information not in the report is an opinion.

**Recommendations are separate and labeled.** They are judgment, they may be outside the test team's authority, and mixing them into conclusions lets a reader treat an opinion as a measured finding.

**Do not soften a finding to protect a schedule.** The decision about what to do with a bad result belongs to the program, and it can only be made with the result stated plainly. A hedged conclusion moves that decision to the author, silently.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Data instead of findings | Plots with no stated conclusion | One conclusion per objective, in the summary |
| Chronological organization | Reader assembles the answer themselves | Organize by objective |
| Vague article configuration | Results cannot support a fielding decision | Exact versions and baseline reference |
| Missing limitations | Credibility collapses when one is found | Write the limitations section deliberately |
| Deficiencies by component | Program cannot triage | Categorize by operational impact |
| Intermittent without a ratio | Nobody can size the problem | Occurrences out of attempts, with conditions |
| Success and failure at different fidelity | Reads as advocacy | Same detail for both |
| Recommendations as conclusions | Opinion read as measurement | Separate sections, labeled |

The honest one: a test report's value is set by whether a reader can tell what it does not prove. Everything else is presentation.
