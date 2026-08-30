---
name: configuration-management
description: Control what the system is, so changes are deliberate rather than accidental. Use when establishing a baseline, identifying configuration items, running change control or a change board, writing an engineering change request or proposal, tracking deviations and waivers, auditing as-built against as-documented, or answering what configuration was delivered, tested, or deployed.
---

# Configuration management

Configuration management answers one question at any moment: **what, exactly, is the system?** Not what was designed, not what was intended — what it currently is, what it was when tested, and what was delivered.

Programmes without it do not notice they lack it until a verification result cannot be tied to a configuration, and nobody can say whether the tested article resembles the delivered one. At that point the verification evidence is worth much less than it appears, which is the expensive version of this failure.

## Where this sits

`system-dev` journals changes to its Design Registry — that is version history for the model. This skill is the *control* layer: which items are under control, what a baseline means, who may change one, and how a change is approved. Version history records what happened; configuration management decides what is allowed to happen.

## Step 1: Identify configuration items

A configuration item is something controlled as a unit — it has an identifier, a version, an owner, and changes to it are governed.

Choose the granularity deliberately. Too coarse and every trivial change re-baselines a large item; too fine and the overhead exceeds the benefit. The usual test: **something is a CI if it is separately specified, separately verified, or separately delivered.**

Include the non-obvious ones, because these are where uncontrolled change actually enters: interface control documents, requirements baselines, test procedures, build and deployment configuration, third-party dependency versions, and the tooling that produces the build.

## Step 2: Establish baselines

A baseline is an agreed reference point. Its purpose is not the snapshot — it is that after it, change requires agreement.

| Baseline | Established at | Fixes |
| --- | --- | --- |
| **Functional** | SFR | What the system must do — the requirements |
| **Allocated** | PDR | How requirements are allocated to items, and the interfaces between them |
| **Product** | CDR | The detailed design, as built and as documented |

Baselines are established at gates, so `technical-reviews` and this skill are two views of the same event. **A gate that establishes no baseline has not established anything** — the package was reviewed and the programme carried on able to change everything it just agreed.

Record for each baseline: what it contains by CI and version, when it was established, and which gate established it.

## Step 3: Control change

Once baselined, change goes through a request, an assessment, and a decision.

**Request.** What changes, why, which CIs and baselines are affected. `references/change-request-template.md`.

**Impact assessment** — the step most often skipped, and the reason most change control fails. Assess against: requirements, interfaces (both sides — see `interface-control`), verification already completed, cost, schedule, and risk. *Verification impact is the one that surprises people.* A change to a CI whose requirements were already verified invalidates that evidence, and rows in the VCRM go back to open. If the assessment does not say which, it is not an assessment.

**Decision.** A change board, sized to the programme — one person for a small one, a standing board for a large one. What matters is that the deciders are not only the people who want the change. Record: approved, rejected, or deferred, with reasons.

Classify changes so the process is proportionate. A **Class I** change affects form, fit, function, interfaces, cost, or schedule and needs full board approval, often the customer's. A **Class II** change is editorial or internal with no external effect and can be delegated. Classifying by who is inconvenienced rather than by effect is how Class I changes get processed as Class II.

## Step 4: Deviations and waivers

Two words used interchangeably and meaning different things.

- **Deviation** — permission granted *before* the fact to depart from the baseline for a defined period or quantity.
- **Waiver** — acceptance *after* the fact of an item that already departs from the baseline.

Both are decisions, both need a named approver, a scope, and an expiry or a quantity. Neither changes the baseline — that is the point. An accumulation of waivers against a baseline nobody has updated means the baseline has quietly stopped describing the system, and the honest response is a baseline change rather than another waiver.

Track them together and report the count at every gate. A rising waiver count is one of the better early indicators that a programme is drifting from its own design.

## Step 5: Audit

Configuration audits check that the records are true, and are worth running whether or not a customer requires them.

- **FCA** — functional configuration audit. Does the item meet its requirements? Every requirement has accepted evidence or an approved waiver. Depends on `verification-validation`.
- **PCA** — physical configuration audit. Does the as-built item match the as-documented product baseline? Drawings, parts, versions, build manifests.

The most valuable output of an audit is usually not a discrepancy in the item, but a discrepancy in the records — a change made without a request, a version delivered that no baseline names. That finding is about the process and matters more than the individual mismatch.

## Step 6: Status accounting

Be able to answer, at any time and without archaeology:

- What is the current configuration of every CI?
- What was the configuration at any past baseline, test, or delivery?
- What changes are in flight, and what have they been assessed to affect?
- What deviations and waivers are open, and when do they expire?

If answering these takes a person a day, configuration management exists on paper only.

## Reference

- `references/change-request-template.md` — the ECR, with the impact assessment sections that make it useful.
- `references/baseline-record.md` — baseline contents and status accounting.
