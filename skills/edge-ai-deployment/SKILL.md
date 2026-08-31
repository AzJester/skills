---
name: edge-ai-deployment
description: Run AI inference on constrained, disconnected or classified hardware. Use when deciding between on-device inference and reachback, selecting a model against a power and thermal budget rather than a cloud bill, compressing a model by quantization, pruning or distillation, updating models on equipment without reliable connectivity, or evaluating a model you cannot collect telemetry from. The case ai-solution-architecture and ai-cost-modeling both name as different and neither covers.
---

# Edge AI deployment

Two skills in this repository stop precisely here. `ai-solution-architecture` says a constrained deployment "eliminates most options and changes the cost model entirely." `ai-cost-modeling` says on-premise or air-gapped inference "is a different model entirely, not a rate substitution." Both are right, and this is that different model.

**Cloud inference is a rate; edge inference is a capital, thermal and logistics problem.** The cost is a box you had to design, power you had to find, heat you had to remove, and a model you cannot update on a whim. Almost every habit from cloud AI transfers badly.

## Step 1: Decide where inference actually belongs

The first decision, and the one that constrains everything else.

| Driver | Pushes inference to the device | Pushes it to reachback |
| --- | --- | --- |
| **Latency** | A decision loop faster than a round trip allows | Latency budget is generous |
| **Connectivity** | Disconnected, intermittent or contested — the normal tactical case | Reliable link |
| **Data volume** | Sensor data too large to ship; you move the answer, not the input | Small inputs |
| **Classification** | Data cannot leave the enclave | No constraint |
| **Model size** | Fits the available compute | Model exceeds anything installable |
| **Update cadence** | Rarely, deliberately | Frequently, centrally |

**Hybrid is usually the honest answer**, and it needs designing rather than assuming: a small model on the device handling the common case and the time-critical path, with reachback for the hard cases when a link exists. Say explicitly what happens when the link is not there — see `network-architecture` on designing for the disconnected case first.

**Data gravity decides more of this than latency does.** A sensor producing continuous high-rate data cannot ship it; the compute goes to the data. This is frequently the whole argument and it is often not stated.

## Step 2: Select the model against the box, not the benchmark

The binding constraint is rarely raw compute.

- **Memory and memory bandwidth usually bind first.** A model that fits in memory but streams weights faster than the bus allows runs at a fraction of its theoretical rate. Check the bandwidth, not just the capacity.
- **Sustained throughput is the number, not peak.** A sealed enclosure throttles — see `swap-and-thermal-budgeting`. Specify inference rate at maximum ambient, sealed, in the mounting orientation, at altitude where it applies. Bench numbers in open air at room temperature are not a specification.
- **Power is a budget you are spending from a platform allocation**, and every watt of inference is a watt of heat with a thermal path to design.
- **The accelerator choice is a SWaP-C trade**, not a performance one. A GPU, an NPU and an FPGA differ in throughput, power, thermal behavior, toolchain maturity and obsolescence horizon — and that last one matters, because `component-selection-and-obsolescence` applies to accelerators as much as to any part, and AI silicon turns over fast.
- **Smaller models frequently win the system trade.** A model at 70% of the accuracy at 25% of the power can be the better system once cooling mass, volume and sustained throughput are counted. `trade-study-analysis` is where that belongs, with SWaP as weighted criteria.

## Step 3: Compress deliberately, and measure what it costs

Compression is how a model reaches a constrained device. Each technique trades accuracy for resources differently.

| Technique | Does | Watch for |
| --- | --- | --- |
| **Quantization** | Lower-precision weights and activations | Accuracy loss is task-dependent and uneven — some classes degrade far more than the average |
| **Pruning** | Removes weights or structures | Unstructured pruning rarely yields real speedup without hardware support; structured pruning does |
| **Distillation** | Trains a smaller model from a larger one | Needs the training pipeline and representative data |
| **Architecture choice** | Selecting a model designed for constrained inference | Usually the cheapest win, and the most often skipped |

**Measure the loss on your own evaluation set, not on a published benchmark.** A quantization result reported on a general benchmark says nothing about your task, and the degradation is frequently concentrated in exactly the cases you care about — rare classes, edge conditions, degraded inputs. `ai-evaluation` covers building the evaluation set; run the compressed model against it, not the original.

**Report accuracy per class and per condition, not as an average.** An average that holds while the rare-but-critical class collapses is the standard compression failure and an average will not show it.

**Re-run the safety and refusal behavior too.** Compression can change more than accuracy.

## Step 4: Evaluate for a device you cannot watch

The hardest structural difference. Cloud AI is evaluated continuously against production traffic; a disconnected device returns nothing.

- **The pre-deployment evaluation has to carry the whole load.** It must cover the operational envelope, including the degraded inputs the device will actually see — sensor noise, weather, damage, adversarial conditions.
- **Define the operating envelope explicitly and design the behavior outside it.** `ai-governance` makes this point; on the edge it is sharper, because nothing will notice the model is out of its envelope and correct it. The device must know its own limits and say so.
- **Design a data return path if one can exist at all.** Even opportunistic — a sample of inputs and outputs collected when a link appears, or physically retrieved during maintenance. Without it you have no drift detection, no failure analysis, and nothing to improve the next model with.
- **Where no return path exists, say so and plan a refresh cadence** instead of pretending drift will be detected. That is a legitimate position; assuming it will be caught is not.
- **Log inputs and outputs locally where storage and classification permit**, with the model version. After an incident, that record is the entire investigation.

## Step 5: Update models like firmware, because that is what they are

A model on a fielded device is a signed artifact delivered through the same constrained path as everything else. `embedded-firmware-and-secure-boot` covers the mechanism; the model-specific parts:

- **Sign and verify model artifacts**, with anti-rollback. An unverified model is arbitrary behavior with a trusted label.
- **Version the model and bind outputs to it.** Which model produced which output is an accreditation question and an after-action question, and it cannot be reconstructed later.
- **Atomic swap with rollback**, exactly as for firmware. A half-written model is a device that behaves unpredictably rather than one that fails cleanly.
- **Validate on-device after update**, against a small held-out set shipped with the model. Confirms the artifact arrived intact and runs correctly on that hardware before it is trusted.
- **Expect long version skew across a fleet.** Devices will run different models for months. Anything consuming their output must tolerate that — see `interface-control`.

## Step 6: Guardrails have to live on the device

There is no cloud safety layer, no moderation service, and no operator watching.

- **Confidence and abstention are part of the design.** A model that must answer will answer wrongly rather than declining. On the edge, "I do not know" is frequently the most valuable output it can produce.
- **The human oversight has to be genuinely exercisable**, by an operator with the information to disagree and the time to do it — see `human-systems-integration` and `ai-governance`. Oversight that requires context the operator does not have is accountability, not oversight.
- **Where the AI sits in a safety path, `system-safety` applies**, and its point holds: an AI component's behavior outside its evaluated envelope is not characterized by its test results, so prefer a hardware or human interlock over trusting the model.
- **The tool and action surface is a security boundary.** `threat-modeling` covers it; on a device that may be captured, so does `embedded-firmware-and-secure-boot` on zeroization.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Cloud economics assumed | Cost model wrong by an order of magnitude | Capital, power, thermal, sustainment — a different model |
| Bench throughput specified | Throttles in the sealed box | Sustained rate at max ambient, sealed, at altitude |
| Compression measured on a benchmark | Rare critical classes collapse silently | Measure on your own eval set, per class |
| No return path, no plan | Drift undetectable and unplanned | Opportunistic return, or an explicit refresh cadence |
| Model version not bound to output | Incident cannot be investigated | Version every output |
| Model updated like a config file | Unverified behavior on a fielded device | Sign, verify, anti-rollback, atomic swap |
| No abstention behavior | Confidently wrong with nobody watching | Design confidence and refusal |
| Accelerator obsolescence ignored | Part gone before the platform is fielded | Apply `component-selection-and-obsolescence` |

The honest one is the fourth. On a connected system, drift is a monitoring problem; on a disconnected one it is a design decision you make before shipping and live with for years.
