---
name: trl-assessment
description: Assess technology readiness on the TRL 1-9 scale and plan the maturation to a target level. Use when asked for a TRL, when a solicitation or gate requires a technology readiness assessment, when judging whether a technology is mature enough to enter a phase, when identifying critical technology elements, or when building a technology maturation plan. Covers TRL, and the related MRL and IRL where those are required. `technology-roadmapping` sequences maturation across a portfolio. `technical-pilot` runs the pilots that produce maturity evidence.
---

# TRL assessment

A technology readiness level answers one question: **how much evidence exists that this technology works, and in what environment was that evidence produced?**

It is a measure of *demonstrated evidence*, not of confidence, effort, or how well the team understands the problem. That distinction is the whole discipline. A team that has thought hard about a technology for two years and never run it outside a laboratory is at TRL 4, however confident they are.

## The two words that decide every level

Nearly every TRL judgement comes down to two questions, and disagreement almost always traces to one of them.

**What was demonstrated?** A component, a breadboard, a prototype, or the actual system? Analysis and simulation cap out at TRL 3 — modelling something is not demonstrating it.

**In what environment?** Laboratory, relevant, or operational?

- *Laboratory* — controlled, benign, convenient. Stressors excluded.
- *Relevant* — the stressors that matter are present, but not all of them, and not necessarily simultaneously.
- *Operational* — the real environment, or one indistinguishable from it in the ways that count.

**"Relevant environment" is where TRL assessments inflate.** A relevant environment must include the stressors that actually threaten the technology. Running a component at room temperature when the mission is thermal-cycled, or at ten users when the deployment is ten thousand, is a laboratory demonstration with an optimistic label. Name the stressors and say which were present; a TRL claim without that list is not assessable.

## The scale

| TRL | Demonstrated | Environment |
| --- | --- | --- |
| **1** | Basic principles observed and reported | — |
| **2** | Technology concept or application formulated | — |
| **3** | Analytical or experimental proof of concept for critical function | Laboratory |
| **4** | Component or breadboard validated | Laboratory |
| **5** | Component or breadboard validated | **Relevant** |
| **6** | System or subsystem model or prototype demonstrated | **Relevant** |
| **7** | System prototype demonstrated | **Operational** |
| **8** | Actual system completed and qualified through test and demonstration | Operational |
| **9** | Actual system proven through successful mission operations | Operational |

Two transitions carry most of the programme risk, and both are environment changes rather than technical ones:

**4 → 5** is where laboratory success meets real stressors, and where a surprising amount of promising technology stops.

**6 → 7** is the integration step: from a prototype in a representative setting to a system prototype in the real one. Schedule estimates routinely underestimate this, because the remaining work is integration and environment rather than the technology itself.

## Step 1: Identify what you are assessing

TRL applies to a **technology element**, not to a system. "The platform is TRL 6" is meaningless — a system is a composition of elements at different levels.

Identify the **critical technology elements**: the parts that are new or novel, *and* whose failure would prevent the system meeting a requirement. Both conditions. A novel component nothing depends on is not critical; a mature component everything depends on is not a technology risk.

For each CTE, assess separately. Where an overall figure is required, **the system's TRL is that of its least mature critical element**, not an average. Averaging is how a programme reports TRL 7 while resting on a TRL 4 dependency.

## Step 2: Assess against evidence

For each CTE, state the level and the evidence that supports it. The evidence is the assessment; the number is shorthand.

Record: what was demonstrated, in what environment with the stressors named, when, by whom, and where the report lives. `references/trl-evidence-sheet.md`.

Three disciplines that keep an assessment honest:

**Assess what has been demonstrated, not what is planned.** Work in progress does not count until it produces evidence. "We will complete environmental testing next month" is TRL 4 today.

**Assess this application, not the technology in general.** A technology proven at TRL 9 elsewhere is not TRL 9 in your system if your environment, scale, or integration differs. The relevant question is readiness *for this use*.

**Where evidence is thin, say so and score low.** A conservative assessment costs credibility once; an inflated one costs it at every subsequent gate, and TRL claims are checked.

## Step 3: Plan the maturation

The assessment's output is not the number, it is the plan to move.

For each CTE below its target, state: current level with evidence, target level and the date it is needed, what must be demonstrated to advance each level, the environment that demonstration requires, cost and schedule, and the fallback if maturation fails.

**Levels advance one at a time.** A plan that jumps 4 → 7 is usually hiding the environment step, and the environment step is the expensive one. If a plan genuinely skips a level, say which demonstration covers both and why.

The fallback is not optional. A CTE whose maturation plan has no alternative is a single point of programme failure, and belongs in `risk-management` as a High risk with that framing.

## Step 4: Feed the rest of the programme

- **`risk-management`** — every CTE below its required level at the gate it is needed is a risk, with the maturation plan as the handling strategy and the fallback as the contingency.
- **`technical-reviews`** — gates check technology maturity. SRR should not accept a requirement resting on a TRL 2 element without a funded maturation plan; PDR expects the critical elements at TRL 6 for most programmes.
- **`trade-study-analysis`** — TRL belongs in the criteria. An alternative that scores best on performance and worst on maturity is a different proposition from one that scores well on both, and trade studies that omit maturity systematically favour the least proven option.
- **`engineering-to-proposal`** — solicitations frequently require a technology readiness assessment, and evaluators check TRL claims against the evidence offered. An assessment built on real evidence is directly reusable; one built on optimism is a liability in a document you sign.

## MRL and IRL

Two companions, used where the programme requires them.

**MRL — manufacturing readiness level**, 1–10. Asks whether it can be *produced* at rate, at cost, at quality. A technology can be TRL 9 and MRL 4: it works, and you cannot make more than one. Where production is in scope, TRL alone understates the risk.

**IRL — integration readiness level**, 1–9. Asks how mature the *interfaces between* elements are. Two TRL 8 components with an unproven interface between them constitute an immature system, and TRL has no way to say so. Where a programme's risk is integration rather than technology, IRL is the more informative measure — and it pairs directly with `interface-control`.

## Reference

- `references/trl-evidence-sheet.md` — per-element assessment and evidence record.
- `references/maturation-plan.md` — the plan template, level by level, with fallbacks.
