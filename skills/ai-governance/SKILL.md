---
name: ai-governance
description: Govern an AI system so its risk is managed and demonstrable. Use when applying the NIST AI Risk Management Framework, meeting federal AI use policy, building an AI use case inventory, determining whether a use is high-impact or rights-impacting, writing a model card or system card, designing human oversight, or answering a customer's questions about AI assurance and responsible AI.
---

# AI governance

AI governance answers a question security governance does not: **this system produces outputs nobody can fully predict — so what makes it acceptable to field anyway?**

That framing matters. Security governance asks whether the system resists attack. AI governance asks whether a system whose behaviour is statistical rather than specified can be trusted with a decision, and what oversight makes that trust reasonable.

`threat-modeling` and `rmf-ato` cover the security half. Neither says anything about whether the model is fit for its purpose, which is what a customer buying AI actually asks.

## NIST AI RMF, and what each function is for

Four functions. Govern runs continuously; the other three cycle.

| Function | Question | Output |
| --- | --- | --- |
| **Govern** | Who is accountable, under what policy, with what culture? | Roles, policy, risk tolerance, escalation path |
| **Map** | What is this system, in what context, for whom, with what could go wrong? | Use case description, stakeholders, impact assessment |
| **Measure** | How do we know it works, and keep knowing? | Evaluation results, monitoring, documented limitations |
| **Manage** | What do we do about what we found? | Treatment decisions, oversight design, incident response |

The function programmes skip is **Govern**, because it produces no artifact a customer asked for. Skipping it means the other three have no accountable owner, and the first difficult decision has nowhere to go.

`ai-evaluation` does the Measure work. This skill covers the rest and consumes its results.

## Step 1: Map — say precisely what the system does

Most AI governance failures are scope failures. The system was assessed for one use and deployed for a neighbouring one.

Record, per use case:

- **The decision or output**, specifically. Not "supports analysts" — *ranks incoming reports by likely relevance so an analyst triages the top N*.
- **Who is affected**, including people who are not users. The subject of a decision often has no interaction with the system.
- **Where the human is.** In the loop (approves each), on the loop (monitors and can intervene), out of the loop (fully automated). This single choice drives most of the oversight design.
- **What happens when it is wrong**, separately for false positives and false negatives. These are rarely symmetric, and the asymmetry should drive the threshold.
- **The operating envelope** — data, populations, conditions the system was built and evaluated for. Everything outside it is an untested claim.

The envelope is what stops the neighbouring-use failure. A system evaluated on one population and deployed on another has left its envelope, whatever the accuracy number says.

## Step 2: Determine impact level

Federal AI policy distinguishes uses that affect rights or safety from ones that do not, with heavier obligations attached — impact assessment, testing in the operational context, human oversight, appeal, monitoring, and public inventory.

Determine and record the level with reasoning, early. A determination made late tends to be made in whichever direction is convenient.

For defense programmes, DoD Responsible AI principles apply alongside: **responsible, equitable, traceable, reliable, governable**. Governable is the one with the sharpest engineering consequence — the system must be able to be disengaged or deactivated if it behaves unintendedly, and that has to be designed in rather than asserted.

## Step 3: Design oversight that can actually work

Human oversight is the most-claimed and least-designed control in AI systems. "A human reviews the output" is not oversight if the human cannot realistically disagree.

Oversight is real when:

- The reviewer has **information sufficient to disagree** — not just the output, but why, and what the system was uncertain about.
- The reviewer has **time**. Oversight sized so a human has four seconds per item is a rubber stamp with a person attached.
- **Disagreement is possible and tracked.** If override is technically possible but socially discouraged, or nobody measures how often it happens, oversight is theatre. Override rate is a health measure: near zero usually means rubber-stamping, not accuracy.
- **Automation bias is countered.** People defer to confident-looking output. Presenting uncertainty, showing the alternatives considered, and withholding a recommendation until the reviewer has formed a view all help.

## Step 4: Document — model and system cards

A model card describes the model; a system card describes the deployed system around it. Customers increasingly ask for both, and the second is the one that carries the governance content.

Cover: intended use and out-of-scope uses, training and evaluation data provenance, evaluation results **disaggregated across the populations that matter**, known limitations and failure modes, the human oversight design, monitoring, and the version and date.

Two disciplines: **state out-of-scope uses explicitly**, because the neighbouring-use failure is prevented by writing it down; and **disaggregate the results**, because aggregate accuracy hides subgroup failure and a customer who discovers that themselves will not accept the aggregate again.

## Step 5: Monitor and respond

Models decay. The world shifts away from the training distribution, upstream data pipelines change, and behaviour changes with them.

Monitor input distribution drift, output distribution shift, performance against ground truth where obtainable, override rate, and user-reported failures. Define in advance what triggers re-evaluation, retraining, or withdrawal — a threshold agreed under pressure is a threshold that moves.

An AI incident is not only a security incident. A model producing systematically wrong outputs is an incident with no attacker, and `incident-response` handles it once someone recognises it as one. Say in advance who can pull the system, on what evidence.

## What a customer asks

Ordered by how often it comes up:

1. How do you know it works? → `ai-evaluation`
2. What happens when it is wrong, and who is accountable?
3. What was it trained on, and what are its limits?
4. Where is the human, and can they actually disagree?
5. How would you know it had degraded?
6. Can it be turned off, by whom, on what signal?

Governance that cannot answer six is not ready, however good the model is.

## Reference

- `references/use-case-record.md` — the per-use-case record, impact determination, and oversight design.
- `references/model-card.md` — model and system card structure.
