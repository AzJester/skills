---
name: ai-solution-architecture
description: Choose and justify the architecture of an AI solution. Use when deciding between prompting, retrieval, fine-tuning and agentic approaches, making a build-buy-partner call, selecting a model against cost, latency and accuracy constraints, designing guardrails and fallbacks, or writing the technical approach for an AI capability. Covers the architectural decision and its consequences, not the API mechanics of any one provider. `agentic-system-design` designs the agentic case; `edge-ai-deployment` covers constrained or disconnected deployment.
---

# AI solution architecture

Most AI solutions are over-architected in one direction and under-architected in another: elaborate model strategy, no failure design. The architecture questions that decide whether a system survives contact are usually not about the model.

## Step 1: Establish what the system must actually do

Before any approach is chosen:

- **The task**, stated as an input and a desired output.
- **Correctness** — what makes an output right, and who decides. If nobody can say, that is the first problem, not the model choice.
- **Consequence of error**, separately for each error type.
- **Volume and latency** — requests per period, acceptable response time, peak behavior.
- **The data** — what exists, where, how sensitive, how current it must be.
- **The human position** — in, on, or out of the loop, from `ai-governance`.

A task whose correctness nobody can define cannot be evaluated, and a system that cannot be evaluated cannot be fielded responsibly regardless of how good it looks in a demo.

## Step 2: Choose the approach, cheapest first

Ascending order of cost and commitment. Escalate only when the simpler option demonstrably fails, and say what failed.

| Approach | Fits | Costs | Escalate when |
| --- | --- | --- | --- |
| **Prompting** | Task expressible in instructions; base model has the knowledge | Lowest. Fast to change | Output quality insufficient on evaluation |
| **Retrieval (RAG)** | Answers depend on your corpus, or must be current or cited | Retrieval quality becomes the bottleneck; corpus must be maintained | Model cannot use retrieved context well, or format is the problem |
| **Fine-tuning** | Consistent format, tone, or a narrow specialized task; enough labeled examples | Data curation, training, re-training on model change; freezes behavior | Behavior must be reliably shaped, and prompting cannot |
| **Agentic** | Task needs multi-step tool use, planning, or iteration | Failure modes multiply; cost and latency scale with steps; hardest to evaluate | The task genuinely requires acting, not answering |

Two things worth stating plainly:

**Most retrieval problems are retrieval problems, not model problems.** When RAG underperforms, the cause is usually chunking, embedding choice, or corpus quality rather than the generation model. Evaluate retrieval separately — precision@k on the retrieval step — before concluding the model is at fault, or you will pay for a larger model to compensate for a chunking bug.

**Fine-tuning is a commitment.** It ties you to a model version, adds a re-training cycle to every model upgrade, and is expensive to reverse. Reach for it for form and consistency, rarely for knowledge — retrieval handles knowledge better and stays current.

## Step 3: Select the model deliberately

Model choice is a trade across accuracy, latency, cost and control — `trade-study-analysis` applies, and the criteria come from step 1.

Practical points:

- **Evaluate on your task**, not on public benchmarks. Benchmark ranking predicts your task's performance loosely at best.
- **Different steps can use different models.** Routing simple cases to a cheaper model and hard ones to a stronger one is usually the largest single cost lever available.
- **Assume the model changes.** Providers deprecate and update. Build so a swap is an evaluation exercise rather than a rewrite, and keep the regression suite from `ai-evaluation` ready to run against a candidate.
- **Where deployment is constrained** — classified, disconnected, on-premise — that constrains the model set before anything else does. Establish it first; it eliminates most options and changes the cost model entirely.

## Step 4: Design the failure behavior

The part that separates a demo from a system.

- **What happens when the model is unavailable?** Queue, degrade, fail closed, fall back to a rule-based path. Decide it rather than discovering it.
- **What happens when the output is malformed?** Validate structure before use. Never parse model output into a consequential action without checking it.
- **What happens when the model is confident and wrong?** This is the dangerous case, because nothing looks unusual. Downstream validation, cross-checks against a source of truth, and human review positioned where it can catch it.
- **What is refused?** Out-of-envelope inputs should be declined rather than answered badly. A system that answers everything is a system that answers some things wrongly with no signal.
- **What is logged?** Enough to reconstruct why an output happened — inputs, retrieved context, model version, parameters, output. Without it, no incident can be investigated, and `incident-response` has nothing to work with.

## Step 5: Build, buy, or partner

| | Fits | Watch |
| --- | --- | --- |
| **Build** | Differentiating capability; unusual constraints; data cannot leave | Sustainment cost, and the scarcity of the people needed |
| **Buy** | Commodity capability; speed matters more than differentiation | Lock-in, roadmap dependency, data handling terms |
| **Partner** | Capability gap on a specific pursuit | Their obligations must flow down — see `supply-chain-security` |

For federal work, ask three questions early because they eliminate options: where does the data go, what are the deployment constraints (classified, air-gapped, on-premise), and is there an authorization path for the service in that environment. A capable service with no path to operate in the target environment is not a candidate.

## Step 6: Write it down as an architecture

The technical approach a reviewer finds credible states: the task and its correctness definition, the approach chosen with what was rejected and why, the model selection with its criteria, the failure design, the evaluation approach, the human oversight position, and the cost model.

An approach that names only the model and the framework reads as a product selection rather than an architecture. `engineering-to-proposal` turns this into volume text once the substance exists.

## Where this connects

`ai-evaluation` proves it works. `ai-governance` governs it. `ai-cost-modeling` prices it. `threat-modeling` covers the security boundary, which for AI includes prompt injection, data exfiltration through outputs, and the tool surface an agentic system can reach.
