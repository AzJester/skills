---
name: test-and-evaluation
description: Plan and run DoD test and evaluation. Use when writing or reviewing a TEMP, planning developmental or operational test, scoping cybersecurity T&E, accrediting a model or simulation for a purpose, defining measures of suitability and effectiveness, or preparing for a test readiness review or DOT&E engagement. Distinct from contractor-side requirements verification.
---

# Test and evaluation

T&E answers a question verification does not: **will this work for the people who have to use it, in the conditions they will use it in?**

That is why DoD separates it from contractor verification. `verification-validation` in this repo proves the system meets its requirements — necessary, and not sufficient. A system can satisfy every requirement and still fail operationally, because the requirements were written by people who were not there.

## The two halves

| | Developmental (DT&E) | Operational (OT&E) |
| --- | --- | --- |
| Question | Does it meet the specification? | Is it operationally effective, suitable, and survivable? |
| Conditions | Controlled, instrumented, often contractor facility | Realistic, operational environment, threat representative |
| Operators | Engineers and test staff | **Typical users**, trained to the fielded standard |
| Judged against | Requirements | Mission outcomes — MOEs and MOSs |
| Run by | Programme, often with contractor | Independent operational test agency |

The independence of OT&E is the point, not bureaucracy. A test run by the people who built the system, with the people who built it operating it, measures something other than fieldability.

**Effective, suitable, survivable** are three separate verdicts. Effective means it accomplishes the mission. Suitable means it can be operated, maintained, supported, and sustained by real units — reliability, maintainability, logistics, training, human factors. Survivable means it continues in the threat environment, including the cyber threat. Systems fail OT&E on suitability far more often than on effectiveness, and suitability is the half programmes under-plan.

## Step 1: The TEMP

The Test and Evaluation Master Plan is the programme's T&E contract with itself and its oversight. It exists to be agreed early and referred to constantly, not written for a milestone.

Sections that carry the weight:

- **System introduction and mission** — what it does and for whom. Everything downstream is judged against this.
- **T&E strategy** — how DT and OT relate, what is tested where, and what each event is meant to resolve.
- **Evaluation framework** — the critical operational issues, the MOEs and MOSs beneath them, and the data needed to decide each. `measures-of-effectiveness` in this repo defines these; the TEMP commits to measuring them.
- **DT&E and OT&E plans** — events, entrance criteria, resources, schedule.
- **Cybersecurity T&E** — phased, not a single event. See below.
- **Modelling and simulation** — what M&S substitutes for live test, and its accreditation.
- **Resource summary** — ranges, threat systems, instrumentation, articles, people. The section that most often makes a plan infeasible.

Two failure patterns worth naming. A TEMP whose evaluation framework cannot be measured with the resources in the resource summary is a plan that will be renegotiated under pressure. And a TEMP written to pass a milestone review rather than to run a programme gets filed and ignored, after which the programme tests whatever is convenient.

## Step 2: Cybersecurity T&E, in phases

Not one event at the end. The phases run alongside development, and the early ones are the cheap ones:

1. **Understand the requirements** — what the system must protect and against whom.
2. **Characterize the attack surface** — what an adversary can reach. `threat-modeling` produces this.
3. **Cooperative vulnerability identification** — testers work with the programme, full knowledge, finding what is there.
4. **Adversarial cybersecurity DT&E** — a red team with limited knowledge, working against defences.
5. **Cooperative vulnerability and penetration assessment** — operational context, cooperative.
6. **Adversarial assessment** — operational context, realistic threat, including the defenders as part of the system under test.

Phases 5 and 6 test whether the *operators and defenders* detect and respond, not only whether the software resists. That distinction is the reason a system with a clean scan can fail an adversarial assessment.

Findings feed `rmf-ato` as assessment evidence rather than as a parallel activity.

## Step 3: VV&A for models and simulation

When M&S substitutes for live test — because live is impossible, unsafe, or unaffordable — the model becomes evidence, and evidence needs its own argument.

- **Verification** — is the model implemented correctly against its specification?
- **Validation** — does it represent the real world adequately **for the intended use**?
- **Accreditation** — an official decision that it is acceptable for that specific purpose.

The intended-use qualifier is the whole discipline. A model validated for one purpose is not accredited for another, and reusing an accredited model for a new question without re-examining the validation is the standard M&S failure. Record the accreditation decision, its scope, and its limitations alongside every result the model produces.

## Step 4: Run and report honestly

- **Entrance criteria are met before the event starts.** `technical-reviews` covers the TRR; a test run on an article that does not meet entrance criteria produces data about something other than the system.
- **The test article configuration is recorded** against the product baseline. Results are only as good as the match between what was tested and what will be fielded — see `configuration-management`.
- **Deficiencies are reported by operational impact**, not by component. A category that stops the mission and one that annoys the operator are different findings.
- **Negative results are results.** A test that finds nothing usually means the test was not stressing, and reporting it as success is how problems reach the field.

## Reference

- `references/temp-outline.md` — TEMP structure with what each section must actually contain.
- `references/evaluation-framework.md` — COIs, MOEs, MOSs and MOPs, and how they connect to data.
