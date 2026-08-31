---
name: digital-engineering
description: Practice digital engineering as DoD means it. Use when establishing an authoritative source of truth, building or governing a SysML or MBSE model, wiring a digital thread across lifecycle phases, deciding whether a digital twin is worth its cost, or answering how models replace documents as the basis of engineering decisions. Covers model governance and the thread, not the individual design decisions the model records.
---

# Digital engineering

The shift digital engineering asks for is small to state and hard to do: **the model becomes the authoritative artifact, and documents become views generated from it.**

Everything else follows. If documents remain authoritative and the model is a picture of them, you have modeling, not digital engineering, and you pay the cost of both.

## Where this sits

`system-dev` maintains a Design Registry of typed, versioned slots with traceability — that is already model-based engineering in its own idiom. This skill covers what sits around any such model: what makes it authoritative, how the thread reaches other lifecycle phases, and how the model is governed so it stays true.

Use `system-dev` (or a SysML tool) to hold the model. Use this to decide what the model is *for* and who may change it. Use `mbse-sysml` for the modeling practice itself — which diagram answers which question, how deep to decompose, and how to build the parametrics.

## Step 1: Establish the authoritative source of truth

An ASoT is not a repository. It is an agreement that for a defined scope, **one artifact is the truth and everything else is derived**.

For each element of the system, name where truth lives: requirements, architecture, interfaces, verification evidence, configuration. One home each.

Three properties make it real, and the third is the one programs skip:

1. **Single home** — no element's truth exists in two places. Where two tools both hold it, one is authoritative and the other syncs one-way.
2. **Derived, not duplicated** — documents, briefings and reviews are generated from it. A slide deck hand-typed from the model diverges by the second revision.
3. **Enforced** — changing the derived artifact does not change anything. If someone can edit the specification document and have that stick, the document is authoritative and the model is decoration.

The honest test: when the model and a document disagree, which does the program believe? If the answer is "it depends who you ask", there is no ASoT yet.

## Step 2: Build the model at the right fidelity

Model to answer questions, not to be complete. A model built for completeness grows until nobody maintains it, then rots, then gets bypassed.

Decide first what decisions the model must support — requirements allocation, interface definition, behavior analysis, verification traceability, cost or performance trades. Model to that depth and no further.

**SysML in practice.** The four pillars, and what each is actually for:

| Pillar | Diagrams | Answers |
| --- | --- | --- |
| Structure | Block definition, internal block | What are the parts and how are they connected? |
| Behavior | Activity, sequence, state machine, use case | What does it do, in what order, in what states? |
| Requirements | Requirement diagram, tables | What must it do, and what satisfies each? |
| Parametrics | Parametric diagram, constraint blocks | What are the physical and performance relationships? |

Parametrics is the pillar most often skipped and the one that most distinguishes a model from a drawing. A model that carries mass, power or timing budgets as constraints can tell you when an allocation breaks; one that carries only structure cannot.

SysML v2 changes the language substantially — textual notation, a proper API, better interoperability. Whether a program is on v1 or v2 changes tooling and training assumptions, so establish it early rather than discovering it at integration.

The pillars in depth, with the v1/v2 decision laid out, are in `mbse-sysml`.

## Step 3: Wire the thread

The digital thread is the connectivity that lets a change in one phase be traced into every other. Its value is answering questions that otherwise take weeks of archaeology:

- Which requirements does this component satisfy, and which stakeholder need is behind them?
- If I change this interface, what verification becomes invalid? (This is the `configuration-management` impact assessment, answered from the model rather than by memory.)
- Which test evidence closes this requirement, and against which configuration?
- What did this element look like at PDR, and what changed since?

Build the thread by connecting what exists rather than by buying a platform that promises it. The links that carry the most weight are requirement-to-design, design-to-verification, and both to configuration. Get those three trustworthy before extending further.

## Step 4: Govern the model

An ungoverned model becomes untrustworthy in about a year, and an untrusted model gets worked around.

- **Ownership** — every part of the model has a named owner who may change it.
- **Baselines** — the model is baselined at gates like any other configuration item. `configuration-management` covers this; the model is a CI.
- **Change control** — model changes crossing a baseline go through the same process as any other change, with the same impact assessment.
- **Quality rules** — naming conventions, required properties, no orphan elements, no dangling allocations. Automate the checks; a model reviewed only by eye drifts.
- **Curation** — someone owns model health as a job, not as a residual duty. This is the role programs underfund and then wonder why the model rotted.

## Step 5: Digital twin, only where it pays

A digital twin is a model connected to a real instance by live data, kept in correspondence with it over its life. That connection is the expensive part and the part that makes it a twin rather than a model.

It earns its cost when there is a decision to make repeatedly against a specific instance: predicting maintenance for this airframe, tuning this deployed configuration, diagnosing this unit's behavior. It does not earn its cost as a visualization, or as a model somebody called a twin because the term appeared in a solicitation.

Before committing: what decision does it inform, how often, what does being wrong cost, and what keeps the data connection alive for the system's life? A twin whose feed dies is a model that is now quietly wrong.

## What to tell a customer

DoD asks about digital engineering in solicitations, and the weak answer describes tools. The strong answer describes:

- Where truth lives, and what enforces it
- Which decisions the model supports, and at what fidelity
- Which thread links are live, and what question each answers
- Who governs the model and how its health is measured
- What is generated from the model versus authored by hand

`engineering-to-proposal` turns that into volume text; the substance has to exist first.

## Reference

- `references/asot-and-thread.md` — establishing authoritative sources and the links worth building first.
- `references/model-governance.md` — ownership, quality rules, and health measures.
