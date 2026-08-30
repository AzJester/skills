---
name: rmf-ato
description: Run the Risk Management Framework and assemble an authorization package. Use when categorizing a system, selecting or tailoring controls, writing an SSP, preparing for a security control assessment, building or working a POA&M, pursuing an ATO or continuous ATO, or answering what an assessor will ask for. Covers the RMF process and its artifacts, not the design-time threat analysis that feeds it.
---

# RMF and authorization

RMF exists to produce one decision: an authorizing official accepting residual risk in writing. Every artifact in the package is evidence for that decision, and a package that does not help the AO decide is paperwork.

The failure mode is treating RMF as a documentation exercise run at the end. Controls selected after the design is fixed become either expensive retrofits or waivers, and a POA&M opened at assessment time is a design problem discovered too late to fix cheaply.

## Where this sits

`threat-modeling` finds design weaknesses and maps them to control families. This skill runs the process those controls belong to and produces the package. Use them in that order: threat model during design, RMF from categorization onward, with the threat model's findings entering as control selection rationale rather than as a separate document.

## Step 1: Categorize

Categorization drives everything downstream, and getting it wrong is expensive in both directions.

Determine the impact level — low, moderate, high — for **confidentiality, integrity and availability separately**, based on the worst-case adverse effect of a loss. FIPS 199 defines the levels; CNSSI 1253 governs national security systems and does not apply the high-water mark the same way FIPS 200 does for federal systems.

Two disciplines:

**Categorize the information, then the system.** Identify every information type the system handles and its impact levels, then derive the system's. A system inherits the highest impact of anything it holds, and the type nobody remembered is the one that raises it.

**Availability is not automatically the same as the others.** Many systems hold sensitive data with modest availability needs, or the reverse. Setting all three to the same level because it is simpler produces either over-control or an indefensible position.

Record the rationale per objective. An assessor will ask why, and "the previous system was moderate" is not an answer.

## Step 2: Select and tailor

Start from the baseline the categorization implies, then tailor deliberately. Tailoring is a documented engineering judgement, not a deletion.

For each control the baseline gives you, one of:

- **Implemented** — the system satisfies it, and you can say how.
- **Inherited** — a common control provider satisfies it. Name the provider and the agreement. Inheritance claimed without a provider who accepts it is the most common assessment finding.
- **Tailored out** — not applicable, with the reason. "The system has no wireless interfaces" is a reason; "not applicable to our architecture" is not.
- **Compensating** — a different control achieves the intent. State the intent, the compensating control, and why the risk is equivalent.
- **Not implemented** — goes to the POA&M with a date and an owner, before assessment rather than after.

Overlays apply on top of the baseline — privacy, classified, space, cross-domain. Determine which apply early; discovering an overlay after control implementation is a rework cycle.

## Step 3: Implement, and write the SSP as you go

The system security plan describes how each control is satisfied **in this system**, not what the control says. A control description copied from the catalogue tells the assessor nothing and reads as a system nobody has examined.

Each control implementation statement answers: what mechanism satisfies this, where is it configured, who operates it, and what evidence would show it working. Write these while implementing. An SSP written retroactively describes what people remember, and the gaps between memory and configuration are what assessments find.

Hardening evidence comes from `stig-and-hardening`; architecture and boundary from `system-dev` and `network-architecture`; supply chain evidence from `supply-chain-security`.

## Step 4: Assess

The security control assessor tests a sample against the assessment procedures and writes the SAR. Prepare by assessing yourself first, honestly, against the same procedures.

What determines how the assessment goes:

- **Evidence is retrievable and current.** A screenshot from eight months ago against a configuration since changed is worse than no evidence.
- **The boundary is unambiguous.** Most assessment disputes are boundary disputes discovered late — what is in, what is inherited, what is out of scope.
- **Inherited controls have real agreements.** The provider must acknowledge providing them.
- **Self-identified findings are already on the POA&M.** A finding you brought forward costs credibility once; one the assessor finds costs it repeatedly.

## Step 5: Authorize

The package goes to the AO: SSP, SAR, POA&M, and a risk assessment summarising residual risk in terms the AO can decide on.

Outcomes are ATO, ATO with conditions, IATT (test only, time-boxed, not operational), or denial. Write the risk summary for a decision-maker, not for an engineer: what could happen, how likely, what it would cost, and what is being done about it.

**Continuous ATO** replaces a periodic re-authorization with ongoing evidence — automated control monitoring, a pipeline with security gates, and an agreed set of signals the AO accepts as continuous. It is not a lighter path; it front-loads the work into automation and requires the AO to agree the evidence stream in advance. Pursue it where deployment tempo justifies the build, not to avoid a package.

## Step 6: Monitor

Authorization is a state that decays. Configuration drifts, threats change, dependencies age, and the POA&M ages with them.

Continuous monitoring means: control effectiveness re-checked on an agreed frequency, changes assessed for security impact before implementation (see `configuration-management` — a change that touches a control invalidates its evidence), POA&M items worked to closure rather than re-dated, and the AO informed when residual risk materially changes.

A POA&M whose items are repeatedly re-dated is not being worked, and an assessor reads it exactly that way.

## Reference

- `references/package-contents.md` — what goes in the package, and what each artifact must actually contain.
- `references/poam-template.md` — POA&M structure and the discipline that keeps it honest.
