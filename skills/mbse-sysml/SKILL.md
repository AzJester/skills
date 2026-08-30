---
name: mbse-sysml
description: Build a systems model in SysML. Use when creating or reviewing a SysML model, choosing which diagrams a system actually needs, decomposing a system into blocks, modelling behaviour with activities or state machines, allocating requirements to structure, building parametric constraints for budgets, or deciding between SysML v1 and v2. Covers the modelling practice itself, where digital-engineering covers the strategy around it.
---

# MBSE and SysML

Model-based systems engineering replaces documents with a model as the primary engineering artifact. The gain is that the model can be *queried and checked* in ways a document cannot — what satisfies this requirement, what breaks if this changes, does the power budget close.

That gain only arrives if the model is built to answer questions. Most failed MBSE efforts produce a large, beautiful, structurally complete model that answers none, because completeness was the goal instead of a means.

## Scope, against the neighbours

Three skills touch this, and mixing them wastes effort:

| Skill | Covers |
| --- | --- |
| `digital-engineering` | The strategy — authoritative source of truth, the digital thread, model governance, digital twins |
| **`mbse-sysml`** (this) | **The modelling practice — what to model, in which diagram, to what depth** |
| `system-dev` | This repo's own Design Registry implementation, with typed slots and its commands |

Use `digital-engineering` to decide the model is authoritative. Use this to build it well.

## Step 1: Decide what the model is for

Before opening a tool, write down the questions the model must answer. Three to six of them, specific:

- Which components satisfy this requirement, and which requirements has nothing been allocated to?
- If this interface changes, what is affected on each side?
- Does the power budget close across all operating modes?
- What state is the system in when this event arrives, and what does it do?
- Which verification event covers this requirement, at what level?

**Everything you model should serve one of those questions.** A model element that serves none is maintenance cost with no return. This single discipline separates models that survive from models that get abandoned in year two.

## Step 2: The four pillars, and where effort actually belongs

SysML's four pillars, with the honest note about how effort is usually misallocated.

### Structure — what the parts are

**Block Definition Diagram (BDD)** — the taxonomy. Blocks, their properties, and their composition relationships. This answers "what things exist and what are they made of".

**Internal Block Diagram (IBD)** — the assembly. Parts inside a block, connected through ports. This answers "how are they wired together".

The distinction is the one newcomers stumble over: **BDD defines types, IBD shows a specific assembly of them.** A BDD says a satellite has a power subsystem; an IBD shows which port on the power subsystem connects to which port on the payload.

Ports carry the interface. Model them properly — a connection between two blocks with no ports and no item flows is a line, not an interface, and cannot be checked against anything. See `interface-control` for what the interface agreement then needs.

### Behaviour — what it does

**Activity diagram** — flow of actions and the items passing between them. Best for processing chains and functional flows.

**Sequence diagram** — interaction between parts over time. Best for protocols and message exchanges, and for showing where a timeout lives.

**State machine** — the states a block occupies and the events that move it between them. Best for modes, and for anything whose response depends on what it is currently doing.

**Use case** — actors and the goals they pursue. Useful early, at the boundary, and easy to overuse.

**Behaviour is where models are usually thinnest.** Structure is easy and visible, so it gets built. Behaviour is where the design actually lives, and a model with fifty blocks and two state machines has documented an inventory rather than a system.

### Requirements — what it must do

Requirement elements, with `satisfy`, `verify`, `derive` and `refine` relationships to structure and behaviour.

Two disciplines that decide whether this pillar earns its keep:

**Requirements live in one place.** If requirements are authoritative in a requirements tool and mirrored into the model, the mirror must be one-way and automated. Two authoritative copies diverge, and the model becomes the one nobody trusts.

**The value is the query, not the diagram.** Requirement diagrams are rarely worth drawing. The value is being able to ask which requirements have no `satisfy` relationship, and which model elements satisfy nothing — the orphans in both directions. That query is the reason to model requirements at all.

### Parametrics — what must hold

Constraint blocks binding properties together: mass roll-up, power budget, link budget, timing budget, thermal margin.

**This is the pillar most often skipped and the one that most distinguishes a model from a drawing.** A model carrying budgets as constraints tells you when an allocation breaks. A model carrying only structure cannot, and the budgets live in a spreadsheet that diverges from it.

If you build only one thing beyond structure, build the parametrics for whichever budget is tightest.

## Step 3: Allocate, and keep it honest

Allocation is the connective tissue: requirements to structure, function to component, logical to physical.

- **Every requirement allocated** to at least one structural or behavioural element.
- **Every element traceable up** to something that needs it.
- **Functional and physical decomposition kept distinct** where they differ. Collapsing them early looks tidy and forecloses design alternatives before they have been examined.
- **Allocation checked automatically**, not by eye. Orphans in either direction are the highest-value model query and the reason to have a model at all.

## Step 4: Model to a depth, and stop

Depth is a decision, not an outcome. Set it explicitly:

- Decompose to the level where **responsibility changes hands** — a supplier boundary, a team boundary, a CI boundary.
- Below that, model the interface and treat the internals as a black box unless a question from Step 1 requires otherwise.
- Add depth when a question demands it, not because a branch looks unfinished.

A model that is uniformly deep everywhere has spent most of its effort where nothing depended on it. Depth should be uneven, and the unevenness should map to where the risk is.

## Step 5: SysML v1 or v2

A real decision with tooling and training consequences, best made early.

| | v1 | v2 |
| --- | --- | --- |
| Notation | Graphical, UML profile | Graphical **and textual**, purpose-built metamodel |
| Interchange | XMI, with well-known fidelity problems | Standard API, substantially better interoperability |
| Tooling | Mature, wide vendor support | Growing; check your vendor's actual support level |
| Skills | Widely held | Fewer people, and the textual notation is a genuine shift |
| Version control | Awkward — models are large binary or XML blobs | Textual notation makes diffing and merging tractable |

That last row matters more than it appears. Text-based models can live in git, be reviewed in pull requests, and be diffed — which changes model governance from a manual discipline into the same workflow as code.

**Choosing:** existing v1 models, mature tool investment and trained staff argue for staying. A new programme, an interoperability requirement, or a desire to version models like code argues for v2. Do not straddle — a programme running both without a defined boundary pays for both and gets the interchange problems of neither.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Modelling for completeness | Large model, no queries run against it | Return to the Step 1 questions; delete what serves none |
| Structure only | Many blocks, almost no behaviour or parametrics | Build the state machines and the tightest budget |
| Diagram thinking | People draw diagrams rather than build a model; the same block appears as three unrelated elements | One model, many views. A diagram is a view of it |
| Duplicate requirements | Model and requirements tool disagree | One authoritative home, one-way automated sync |
| Uniform depth | Effort spread evenly regardless of risk | Depth follows responsibility boundaries and risk |
| No automated checks | Orphans and inconsistencies found by review | Automate the queries — see `digital-engineering` |
| Model nobody queries | It is documentation with extra steps | If no decision uses it, stop maintaining it |

The last row is the honest one. A model that informs no decision is not an asset, and the correct response is either to connect it to a decision or to stop paying for it.

## Reference

- `references/diagram-selection.md` — which diagram answers which question, and the modelling patterns worth knowing.
