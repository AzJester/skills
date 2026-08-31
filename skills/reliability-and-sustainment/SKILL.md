---
name: reliability-and-sustainment
description: Design for and prove reliability, maintainability and supportability. Use when setting or allocating RAM requirements, predicting or growing reliability, planning maintenance and levels of repair, sizing spares, working the integrated product support elements, estimating operating and support cost, or answering whether a system will actually be available when it is needed. Covers the discipline; fmea-analysis and fault-tree-analysis are techniques used inside it. For hardware products, `hardware-product-development` covers the realization lifecycle this feeds.
---

# Reliability and sustainment

Most of a system's life-cycle cost is incurred after delivery, and most of that is decided before it. Design choices made in the first year set the sustainment bill for the next thirty, and by the time the bill arrives the design is fixed.

`fmea-analysis` and `fault-tree-analysis` are the analysis techniques. This is the discipline that decides what to analyze, what to require, and what to do about the answer.

## Step 1: Get the requirements right, because everything follows from them

Three measures, routinely confused, and only one of them is what the user actually cares about.

| Measure | Asks | Typical expression |
| --- | --- | --- |
| **Reliability** | How long until it fails? | MTBF, MTBCF, mission reliability over a stated duration |
| **Maintainability** | How long to fix it? | MTTR, maintenance hours per operating hour |
| **Availability** | Is it working when needed? | Ao, combining both plus the delays around them |

**Availability is the requirement that matters, and it is the one most often stated loosely.** Operational availability includes not just repair time but the time spent waiting — for a spare, for a technician, for the part to arrive. A system with excellent MTTR and a twelve-week spares pipeline is not available.

Three disciplines:

**State the conditions.** A reliability figure without an operating environment, duty cycle and definition of failure is not a requirement. What counts as a failure — mission-affecting, any fault, anything requiring maintenance — changes the number by multiples and is the single most common source of disagreement at demonstration.

**Allocate down the architecture.** A system-level figure is met, or missed, by the sum of its parts. Allocate to subsystems early so designers know their budget, exactly as `mbse-sysml` treats a mass or power budget — this is a parametric constraint, and modeling it as one lets the model say when an allocation breaks.

**Make it verifiable.** Every RAM requirement needs a method and an event in the VCRM — see `verification-validation`. A reliability requirement that can only be verified by fielding the system for two years has been written without thinking about how it will be proven.

## Step 2: Predict, then grow

**Prediction is for comparison, not for promises.** Reliability predictions — parts-count methods, similar-item comparison, physics-of-failure — are useful for comparing design options and finding the dominant contributors. They are poor absolute forecasts, and the older handbook methods in particular are widely criticized for producing numbers with unwarranted authority. Use them to rank, not to commit.

**Reliability is grown, not predicted into existence.** A new design does not meet its reliability requirement at first build. It gets there through test, failure, root cause and correction, repeated. Plan that explicitly:

- A reliability growth plan with a starting point, a target, and the test time between them.
- A closed-loop failure reporting and corrective action system, so every failure is recorded, root-caused and either fixed or accepted deliberately. The RCCA skills — `rcca-master` routes them — are the analysis half of this.
- **The growth only happens if the corrective actions are actually implemented.** A failure reporting system that records and does not fix produces excellent data about a system that is not improving.

**Find the dominant contributors and work those.** Reliability effort spread evenly is effort mostly spent where it did not matter — a small number of items usually drive most of the failures. `pareto-analysis` applies directly.

## Step 3: Design for maintenance, before it is designed in

Maintainability is designed, and it is designed early or not at all.

- **Access.** The item most likely to fail should not require removing six others to reach. This is an architecture decision, not a packaging detail.
- **Fault isolation.** Built-in test that isolates to the replaceable item is what makes MTTR achievable. Its false alarm rate is a requirement too — a BIT that cries wolf produces unnecessary removals, which is a sustainment cost and a reliability problem in its own right.
- **Standardization.** Common fasteners, common tools, common parts across the system. Every unique tool is a logistics footprint.
- **Modularity at the right level.** What is replaced, by whom, at which maintenance level — decided in design, because it determines the spares and the training.
- **Human factors.** Can it be done by the actual maintainer, in the actual conditions, wearing what they will be wearing? See `human-systems-integration`.

## Step 4: The support system is part of the design

Delivering the hardware and leaving the support to be worked out later is how a system becomes unaffordable to operate.

The integrated product support elements — the exact list varies by service, but the substance is consistent:

| Element | The question it answers |
| --- | --- |
| Product support management | Who owns supportability overall |
| Design interface | How supportability influences the design, while it can |
| Sustaining engineering | Who fixes it when it turns out to be wrong in the field |
| Supply support | Spares: what, how many, where |
| Maintenance planning | Which tasks, at which level, by whom |
| Packaging, handling, storage, transportation | How it moves and survives moving |
| Technical data | The manuals and data — see `procedural-documentation` |
| Support equipment | What is needed to maintain it, and who maintains that |
| Training and training support | How maintainers become qualified |
| Manpower and personnel | How many, of what skill, and are they available |
| Facilities and infrastructure | Where the work happens |
| Computer resources | The software and systems that support all of it |

**The level of repair analysis decides the shape of the whole support system.** What is repaired forward, what goes to a depot, what is discarded on failure — that decision drives spares, training, support equipment and cost together. Made deliberately it is an optimization; made by default it is usually the most expensive option.

**Technical data rights determine whether you have options later.** A system you cannot maintain without the original manufacturer is a sustainment position, not just a technical one — see `contract-vehicles-and-clauses`.

## Step 5: Cost the life, not the delivery

Operating and support cost typically dominates total ownership cost, and it is driven by decisions made during design.

- **Model it early, roughly.** A rough O&S model during design influences the design. A precise one after delivery only informs the budget.
- **The drivers are consistent**: maintenance manpower, spares consumption, and the cost of unavailability. Reliability improvements pay back through all three.
- **Compare alternatives on life-cycle cost, not acquisition cost.** A cheaper unit with half the MTBF is usually more expensive within a few years — and `trade-study-analysis` is where that comparison belongs, with O&S cost as a weighted criterion rather than a footnote.
- **State the assumptions**, especially operating tempo and service life. They dominate the answer and they are frequently inherited unexamined.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Failure undefined | Demonstration disputes what counts | Define failure, environment and duty cycle up front |
| Availability treated as reliability | Meets MTBF, unavailable in the field | Requirement on Ao, including logistics delay |
| Prediction treated as a promise | Commitment to a number nobody can hold | Predict to compare; grow to achieve |
| FRACAS records without corrective action | Excellent data, no improvement | Close the loop, and track closure |
| Maintainability retrofitted | Access designed out; MTTR unachievable | Design interface participates in design |
| Support planned after delivery | Sustainment cost arrives as a surprise | Plan the support elements alongside the design |
| LORA by default | The most expensive support posture, unchosen | Decide the repair levels deliberately |
| Acquisition cost optimized alone | Cheaper to buy, dearer to own | Compare on life-cycle cost |

The honest one: reliability is not a property you can add at the end, and sustainment is not a phase that starts at delivery. Both are consequences of decisions taken while the design was still cheap to change.
