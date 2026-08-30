---
name: engineering-to-proposal
description: Turn delivered engineering work into proposal evidence. Use when harvesting past-performance material from a finished project, writing a technical volume or technical approach section from a real architecture, converting delivered requirements into compliance-matrix rows, or answering "what have we actually done that proves this" during a capture or proposal. Bridges engineering artefacts to capture and proposal work rather than writing either from scratch.
---

# Engineering to proposal

Two bodies of work that rarely meet: the engineering record of what was built, and the proposal that claims you can build it again. This skill moves material from the first into the second without inventing anything.

The failure this exists to prevent is a technical volume written from memory. Memory produces adjectives — robust, scalable, proven — where an evaluator wants nouns and numbers. The engineering record has the nouns and numbers; they are just in the wrong format.

## The rule that governs everything here

**Every claim traces to an artefact.** A commit, a diagram, a test result, a postmortem, a delivered requirement, a CDRL, a signed acceptance. If a sentence in a proposal cannot be traced to something that exists, it is either removed or explicitly marked as a forward-looking commitment rather than past performance.

This matters beyond good practice. Past-performance claims are representations. An unsupported one is a problem long after the proposal is submitted.

## Three jobs

Ask which one is wanted before starting. They draw on different artefacts and produce different outputs.

### Job 1: Harvest past-performance evidence

From a finished or in-flight project, extract what a past-performance volume can use.

Go looking for, in the repository and its records:

| Source | Yields |
| --- | --- |
| Delivered requirements, acceptance records | Scope actually met, verification method |
| Architecture docs, `.omm/` output, diagrams | System scale, integrations, technologies |
| Incident record and postmortems | Availability achieved, response discipline |
| Test results, coverage, CI history | Quality evidence that is measured rather than asserted |
| Git history, release cadence | Delivery tempo, team size, duration |
| Threat model, control mappings | Security posture, compliance footing |

Produce for each relevant item: what was done, the measurable outcome, the technologies, the period, and the artefact it traces to. Where a number is unavailable, record it as unavailable — a gap you can go and fill beats a number you invented.

Relevance is judged against the pursuit, not against how interesting the work was. Say plainly which harvested items do not fit the opportunity.

### Job 2: Technical volume from a real architecture

Turn an architecture into the technical approach an evaluator scores.

The move is from **structure** to **rationale**. The architecture says what the system is; the volume must say why that shape serves this customer's problem. Every component that appears should earn its place by answering a requirement.

1. Start from the actual architecture. `architecture-diagrams` renders it — the `corporate` style is the one that survives a review board; avoid the loud styles here.
2. For each major component, state the decision, the alternatives considered, and why this one. `trade-study-analysis` output is exactly this and can be cited directly. Where a real trade study exists, say so; evaluators can tell the difference between a documented trade and a retrofitted justification.
3. Tie components to the solicitation's requirements. A component with no requirement behind it is either scope you are giving away free or a paragraph to cut.
4. Name the risks honestly and their mitigations. A volume with no risks reads as a volume that has not thought about the work.

Hand the drafted narrative to your account's `executive-summary-builder` for the front matter and `mck-pyramid-checker` for structural review, where those account skills are installed. This skill supplies substance; those shape it.

### Job 3: Delivered requirements to compliance matrix

Where `requirements-dev` or `system-dev` hold a real requirements baseline, the crosswalk to a compliance matrix is mostly mechanical, and doing it by hand is where errors enter.

For each solicitation requirement, produce: the requirement text and its section, whether you have delivered something that meets it, the artefact proving it, and the gap if there is one.

Three outputs matter, and the third is the one usually skipped:

- **Met, with evidence** — the strong rows.
- **Partially met** — what exists, what is missing, and whether the gap is closable before submission.
- **Not met** — including requirements nobody has claimed. An orphan requirement found at proposal time is a finding; found at evaluation time it is a deficiency.

Where a threat model produced control mappings, they slot in here directly: the requirement is what you did, the control is where it files, the threat is why it exists.

## What this skill does not do

It does not write the proposal. It does not decide bid or no-bid. It does not judge whether the past performance is strong enough to lead with. Those belong to `capture-management`, `solution-shaping` and `proposal-writing`, and they work better fed real material than asked to imagine it.

It also does not manufacture evidence. When the honest answer is that a claim has no artefact behind it, say so and let a human decide whether to make the claim anyway. That decision is theirs and it should be made knowingly.

## Reference

- `references/evidence-inventory.md` — the harvest worksheet, one row per claim, with its artefact and gap.
