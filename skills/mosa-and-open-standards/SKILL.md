---
name: mosa-and-open-standards
description: Design and defend a modular open systems approach. Use when a solicitation requires MOSA, designating key interfaces, choosing between an open standard and a proprietary interface, aligning a design to SOSA, CMOSS, OpenVPX or FACE, writing or evaluating a MOSA claim, or deciding what a module boundary should actually be. Covers the architecture decision and its evidence; interface-control covers the agreement about a specific interface.
---

# MOSA and open standards

A modular open systems approach is a statutory expectation on major defense acquisition programmes, not a design preference. For tactical edge compute and sensor processing it is also the framing customers now specify directly — a solicitation is as likely to name SOSA alignment as it is to name a performance requirement.

The failure this exists to prevent is a MOSA claim that does not survive examination: a system described as open, built around one proprietary interface that everything has to pass through. That interface is what an evaluator looks for, and finding it discredits the whole claim.

## Step 1: Understand what MOSA actually asks for

The approach rests on a few principles, and the useful thing is that they are testable:

| Principle | The question an evaluator asks |
| --- | --- |
| **Modular design** | Can a module be replaced without redesigning its neighbours? |
| **Key interfaces designated** | Which interfaces are declared key, and are they the ones that matter? |
| **Open standards at those interfaces** | Are they widely available standards, or a specification you published? |
| **Conformance demonstrated** | Is there evidence, or an assertion? |
| **An enabling environment** | Do the contract, the data rights and the business case actually permit it? |

**The last one is where most MOSA efforts fail, and it is not technical.** An architecture can be perfectly modular and still be closed in practice if the government does not hold the data rights to procure a replacement module from someone else. Openness is a data rights and contracting outcome as much as an architectural one — see `contract-vehicles-and-clauses`.

**MOSA is not the same as "uses commercial parts", "uses Linux", or "has an API".** All three are commonly offered as MOSA evidence and none of them answers the question, which is whether a third party could build a module that works in your system.

## Step 2: Decide where the module boundaries actually go

This is the real engineering decision, and it is a judgement about the future, not about the present design.

**Put boundaries where change is expected.** The parts of a tactical edge system that turn over fastest — processing, radios and waveforms, sensors, mission software — are where modularity pays. Boundaries drawn where nothing changes cost interface overhead and buy nothing.

**Put boundaries where a competitor could plausibly supply.** The point of an open interface is a real second source. A module boundary around something only you can build is a boundary that will never be exercised.

**Do not modularise everything.** Every interface has a cost in performance, complexity, power and test. A system decomposed into forty modules to demonstrate openness performs worse and costs more than one with five well-chosen boundaries, and it does not score better.

**The trade is real and should be recorded.** Open standard interfaces frequently cost latency, bandwidth or power against a purpose-built one. Where that trade matters, make it explicitly — `trade-study-analysis` — rather than either sacrificing performance silently or quietly closing the interface.

## Step 3: Know the ecosystem you will be asked about

For tactical edge compute, sensor processing and vehicle-mounted systems, these are the names that appear in requirements. Which apply depends entirely on the customer and the platform, so confirm against the solicitation rather than assuming.

| Standard family | Covers |
| --- | --- |
| **OpenVPX / VITA** | The backplane ecosystem: VPX form factors and profiles, mechanical and cooling conventions, and the connector standards for RF and optical |
| **SOSA aligned** | A sensor open systems architecture built on OpenVPX with defined slot and module profiles, plus software and management conventions |
| **CMOSS** | The Army's suite bringing together modular C5ISR standards for ground platforms, including vehicle integration and modular RF |
| **FACE** | Airborne software: a reference architecture and segment model with a conformance programme |
| **VICTORY** | Ground vehicle integration — shared data bus and services across vehicle systems |

Two practical notes:

**"Aligned" is doing work in "SOSA aligned".** These ecosystems have defined conformance mechanisms, and the difference between a conformant product, an aligned one, and one that merely uses the same connector is exactly what an evaluator probes. Be precise about which you are claiming, and be able to show what backs it.

**Standards conformance is verifiable, so it belongs in the VCRM** with a method and an event like any other requirement — see `verification-validation`.

## Step 4: Designate key interfaces, and mean it

A key interface is one the government intends to be able to procure across. Designating them is a deliberate act with consequences.

For each key interface, establish:

- **The standard it uses**, at a specific version.
- **What crosses it** — mechanical, electrical, thermal, data, timing, power, control, and the state each side assumes about the other. `interface-control` is the discipline for writing this down, and a key interface deserves a real ICD rather than a reference to a standard.
- **The data rights position**, so the interface definition can actually be given to a competing supplier.
- **The conformance evidence** — test, inspection, or a conformance programme result.
- **Who controls change to it**, and how. An interface one party can change unilaterally is not open in any useful sense.

**Where an interface must be proprietary, say so and justify it.** An honest architecture with two declared proprietary interfaces and a stated reason is more credible than one claiming to be entirely open. Evaluators find the proprietary interface either way; the difference is whether you told them.

## Step 5: Write the MOSA claim so it can be checked

Where a proposal or a design review has to argue MOSA — see `proposal-writing` — the argument is specific, not adjectival:

- **The module decomposition**, with a diagram, and why the boundaries are where they are. `architecture-diagrams` renders it.
- **The key interfaces table**: interface, standard and version, what crosses it, conformance evidence, data rights.
- **A replaceability case**: name a module and describe what a third party would need to build a replacement. If the answer requires information you would not release, the module is not open.
- **The trades made**, including where an open standard cost performance and why that was accepted.
- **What is not open**, and why.

**The strongest evidence is a module you did not build.** A system that already integrates someone else's conformant card has demonstrated openness rather than asserted it.

## Step 6: Sustain it, because openness decays

An architecture that was open at delivery closes gradually and without anyone deciding to.

- **Every change that touches a key interface goes through change control**, with the interface owner involved — see `configuration-management` and `interface-control`.
- **Watch for the private extension.** Adding a vendor-specific field or an out-of-band side channel to solve a schedule problem is how a standard interface becomes proprietary in practice while remaining standard on paper.
- **Re-check conformance after significant change**, and after the standard itself revises. These ecosystems publish new revisions, and a product conformant to a superseded version needs a deliberate decision rather than silence.
- **Track the standards roadmap** alongside the product roadmap — see `technology-roadmapping`.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| One proprietary interface in the critical path | Evaluator finds it; the whole claim discredited | Declare it and justify it, or open it |
| Data rights not aligned | Modular architecture, closed in practice | Settle rights alongside the architecture |
| Commercial parts offered as MOSA evidence | Does not answer the question | Show a third party could build a module |
| Everything modularised | Performance and cost penalty, no better score | Boundaries where change and second sources are real |
| "Aligned" claimed loosely | Cannot show what backs it | Be precise; hold the conformance evidence |
| Interfaces designated but not documented | A standard name in place of an ICD | Real ICD per key interface |
| Private extensions after delivery | Standard on paper, proprietary in practice | Change control on key interfaces |
| Conformance never re-checked | Product drifts from a revised standard | Re-check on change and on standard revision |

The honest one: modularity is a claim about what someone else could do without your help, and the only real test is whether they have.
