---
name: quality-management-system
description: Build and run a quality management system people actually use. Use when establishing or improving a QMS, preparing for an ISO 9001, AS9100 or CMMI appraisal, writing or tailoring process assets, running internal audits and management review, handling nonconformances and corrective action, or diagnosing why a certified organization keeps producing the same defects.
---

# Quality management system

A QMS is a claim: that the organization produces good outcomes because of how it works, not because of who happened to be on the job. Certification is evidence for the claim; it is not the claim.

The failure this exists to prevent is a certified organization whose people work around the documented process because following it is slower than the deadline allows. That organization has the audit finding it deserves waiting for it, and in the meantime it has all the cost of the system and none of the benefit.

## Step 1: Know which standard, and why

| Standard | Is | Assesses |
| --- | --- | --- |
| **ISO 9001** | General quality management | Whether you have a working management system |
| **AS9100** | Aerospace, built on ISO 9001 | The above plus aviation, space and defense additions — risk, configuration, counterfeit parts, product safety |
| **CMMI** | Process capability and maturity model | How consistently and how well processes are performed, on a maturity scale |
| **Customer-specific** | Contractually imposed quality requirements | Whatever the contract says, which flows down — see `teaming-and-subcontracts` |

**Certification is often a market entry requirement rather than a choice**, and where that is true the decision is which scope to certify, not whether. Scope matters: certifying an entire enterprise where one business unit needs it is a large and recurring cost.

**CMMI and ISO answer different questions** and are frequently both required. ISO asks whether you have a management system that works; CMMI asks how capably specific process areas are performed. An organization can hold one and be weak at the other.

**Maturity levels are not a scoreboard.** A level achieved and not sustained is worse than one not pursued, because it has taught the organization that the appraisal is the goal.

## Step 2: Write processes people will follow

The central tension: a process detailed enough to guarantee consistency is usually too heavy to be followed under pressure.

- **Document what actually happens**, then improve it. Documenting an idealized process creates an immediate gap between the QMS and reality, and the QMS is what loses.
- **Write for the practitioner, not the auditor.** A process nobody can follow without a training course will not be followed. `procedural-documentation` applies: one action per step, clear entry and exit criteria, and a stated purpose.
- **Tailoring is a feature, not a loophole** — but it must be governed. Different business units and different contract types genuinely need different processes. Define what may be tailored, by whom, with what approval, and record each tailoring decision. Ungoverned tailoring becomes "we don't do that here", which is a finding.
- **Make the process assets easy to find and use.** Templates, checklists and examples get used; a policy document in a portal does not. The best evidence of a healthy QMS is that people reach for its templates because they are the fastest way to do the work.
- **Keep the process library pruned.** Procedures that no longer describe how work is done are liabilities — they generate findings and they teach people to ignore the library.

## Step 3: Nonconformance and corrective action

Where a QMS either earns its keep or becomes paperwork.

**Nonconformance is a fact, recorded without blame.** An organization where raising one is uncomfortable has fewer records and the same number of problems.

**Corrective action addresses cause, not symptom.** This is where the RCCA family belongs — `rcca-master` runs 8D and routes the analysis methods, and a corrective action that does not name a cause is a repair with a form attached.

Three tests for a corrective action worth the effort:

1. **Does it name a cause?** "Operator error" and "insufficient attention" are not causes. What in the system made the error likely?
2. **Would it prevent recurrence**, rather than catching it next time? Adding an inspection detects; changing the process prevents.
3. **Was effectiveness verified afterwards?** The step most often skipped. An action closed without checking whether it worked is a record, not a correction.

**Track recurrence explicitly.** The same nonconformance appearing repeatedly across different corrective actions is the single most useful signal a QMS produces, and it says the causes are not being found.

**Distinguish correction from corrective action.** Fixing the defective unit is correction. Preventing the next one is corrective action. Both are needed; only one changes anything.

## Step 4: Audit to find problems, not to pass

**Internal audits exist to find things before an external auditor does.** An internal audit program that consistently finds nothing while external audits find issues is not auditing.

- **Audit against what the process says**, and separately ask whether the process is what the organization should be doing. Conformance and effectiveness are different questions and both matter.
- **Auditors independent of the work.** Someone auditing their own area finds less, however honest they are.
- **Findings need owners and dates**, and closure needs verification — the same discipline as corrective action.
- **Sample where risk is**, not uniformly. Uniform sampling spends audit effort where nothing was going to be found.

**Management review is a decision meeting, not a report-out.** Its purpose is that leadership acts on quality data: resources allocated, processes changed, priorities reset. A review that receives a presentation and adjourns has satisfied a clause and changed nothing.

## Step 5: Measure whether it is working

Certification status is not a measure of quality. Useful measures point at outcomes:

- **Escaped defects** — found by the customer rather than internally. The clearest single measure of whether the system works.
- **Recurrence rate** of previously corrected nonconformances.
- **Corrective action cycle time**, and how many are closed without verified effectiveness.
- **Process adherence where it matters**, sampled honestly rather than self-reported.
- **Rework and scrap cost**, which is the price of quality expressed in the only unit leadership reliably acts on.

**If none of these improve after certification, the QMS is documentation.** That is worth stating plainly to leadership, because the alternative is discovering it after a customer does.

## Step 6: Across business units

The cross-unit question is where to standardize and where not to.

- **Standardize what is genuinely common** — nonconformance handling, corrective action, audit, document control, records. These benefit from being identical everywhere and cost little to share.
- **Let engineering and delivery processes differ** where the work genuinely differs. Forcing a hardware program and a software program through one process produces something that fits neither and is followed by neither.
- **Share the process assets, not the mandate.** Templates and examples spread by being useful. A mandated process that does not fit gets tailored into meaninglessness or ignored.
- **One nonconformance and corrective action system across units**, because recurrence across unit boundaries is invisible otherwise, and it is exactly the pattern a portfolio view exists to find.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Certification as the goal | Passes audits, same defects | Measure outcomes, not certification status |
| Idealized documented process | Everyone works around it | Document reality, then improve it |
| Ungoverned tailoring | "We don't do that here" | Define what may be tailored, by whom |
| Corrective action without cause | Same issue recurs under new numbers | Use the RCCA methods; track recurrence |
| Effectiveness never verified | Closed actions, unchanged outcomes | Verify after, before closing |
| Internal audits find nothing | External auditors find plenty | Independent auditors, risk-based sampling |
| Management review as a report-out | No decisions, no resources | Treat it as a decision meeting |
| One process for every unit | Fits nobody, followed by nobody | Standardize the common, vary the delivery |

The honest one: the fastest way to tell whether a QMS is real is to ask a working engineer where they find the template they use. If they do not know, the system exists for the auditor.
