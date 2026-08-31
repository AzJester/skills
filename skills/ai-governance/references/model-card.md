# Model and system card

Two documents. The model card describes the model; the system card describes the deployed system around it, and is usually the one that answers a customer's questions.

## Model card

**Model details** — name, version, date, type and architecture, owner, license, and what it was derived from if fine-tuned or adapted.

**Intended use** — the uses it was built and evaluated for.

**Out-of-scope uses** — explicit. Uses that look adjacent and are not supported. This section prevents more failures than any other.

**Training data** — sources, provenance, time period, size, known composition and gaps, and how it was collected. Where the base model's training data is not disclosed, say so rather than leaving the section implying knowledge you do not have.

**Evaluation data** — sources, and how it relates to the deployment distribution. An evaluation set drawn from the same collection as training overstates performance.

**Results** — headline metrics, and **disaggregated across the populations and conditions that matter**. Aggregate performance hides subgroup failure, and a customer who finds that themselves stops believing the aggregate.

**Limitations** — where it performs poorly, what it cannot do, and known failure modes. Written plainly; a limitations section that reads as marketing is read as an absence of testing.

**Ethical and fairness considerations** — what was assessed, how, and what was found.

## System card

Everything above sits inside a deployed system, and the system is what gets fielded.

**System description** — the model in context: inputs, preprocessing, the model, postprocessing, thresholds, downstream consumers.

**Deployment context** — who uses it, for what, in what environment, at what volume.

**Human oversight** — the design from the use case record: what the reviewer sees, how they disagree, whether override is tracked.

**Guardrails** — input validation, output filtering, refusal behavior, rate limits, and what happens when the model is unavailable.

**Monitoring** — signals, thresholds, and who watches them.

**Incident history** — what has gone wrong and what changed as a result. A card with an empty incident history on a long-deployed system reads as unmonitored rather than flawless.

**Version and date** — of the card. A card that does not track the system it describes is worse than none, because it is believed.

## Currency

Both cards are configuration items — see `configuration-management`. A model change, a threshold change, or a change to the oversight design updates the card, and the change is what triggers the update rather than a review cycle.
