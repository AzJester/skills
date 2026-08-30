---
name: ai-cost-modeling
description: Model what an AI solution costs to run at volume. Use when pricing an AI capability, estimating inference cost per transaction, projecting cost as usage scales, comparing architectures on cost, finding where margin goes, or answering what this costs at contract volume rather than in a demo. Covers unit economics and its drivers, not procurement of the underlying service. `edge-ai-deployment` covers the on-premise and air-gapped case, which is a different model rather than a different rate.
---

# AI cost modeling

AI solutions price badly because the demo is cheap and production is not, and the gap is not proportional. A system costing pennies in a pilot can cost six figures a month at contract volume, and the difference is usually in places nobody modelled.

The question this answers: **what does one unit of work cost, and what happens to that number at scale?**

## Step 1: Define the unit

Cost per token is an input, not an answer. Model cost per **unit of work the customer recognises** — per document processed, per query answered, per report generated, per case triaged.

That is the number that supports a price, survives a review, and can be compared across architectures.

## Step 2: Count what a unit actually consumes

The count that surprises people. One user-visible unit of work is rarely one model call.

| Consumer | Often missed |
| --- | --- |
| Input tokens | System prompt, few-shot examples, and retrieved context — usually the largest input component, and it scales with retrieval depth |
| Output tokens | Reasoning or thinking tokens where the model produces them; typically priced higher than input |
| Retries | Failed parses, refusals, timeouts, validation failures |
| Multi-step | An agentic task is many calls; the count varies per task and has a tail |
| Judge / validation calls | Evaluating or checking output costs model calls too |
| Embedding | Query embedding per request, corpus embedding on ingest and re-index |
| Vector store | Storage and query cost, which scales with corpus rather than usage |
| Surrounding compute | Preprocessing, orchestration, storage, egress |

**Conversation and context growth** is the single most common modelling error. A multi-turn interaction resends accumulated context on every turn, so cost grows with the square of turn count rather than linearly. A ten-turn conversation is not ten times a one-turn cost.

**Agentic step count has a tail.** Model the distribution, not the mean — the p95 task consuming five times the median is what determines whether a busy day is affordable.

## Step 3: Build the model

```
Cost per unit = Σ (tokens_in × rate_in) + (tokens_out × rate_out)
              + (retry_rate × retry_cost)
              + embedding + vector + surrounding compute
              ÷ (1 − cache_hit_rate)ish, where caching applies
```

Then scale it:

| | Value | Assumption |
| --- | --- | --- |
| Units per day, steady state | | |
| Peak-to-average ratio | | |
| Cost per unit | | |
| Daily / monthly / annual | | |
| Growth over the period of performance | | |

State every assumption inline. A cost model whose assumptions are visible survives challenge; one presenting a single number does not, and on a fixed-price bid that matters.

## Step 4: Find the levers, in order of effect

Usually in this order:

1. **Route by difficulty.** Send easy cases to a cheaper model, hard ones to a stronger one. Typically the largest single lever, and it requires a classifier you can evaluate.
2. **Cache.** Prompt caching on stable prefixes — system prompts, few-shot blocks, retrieved context reused across turns — often cuts input cost substantially. Its effect depends entirely on hit rate, so model that rather than assuming it.
3. **Cut retrieved context.** Retrieval depth is usually set generously and rarely tuned. Reducing k from 20 to 8 with no measurable quality loss is a common finding — but it must be measured, via `ai-evaluation`, not assumed.
4. **Trim the prompt.** System prompts accumulate. They are paid for on every call.
5. **Constrain output.** Structured output and length limits reduce the more expensive token class.
6. **Batch** where latency permits.

Every one of these is a quality trade. Re-run the regression suite after each; a cost reduction that quietly degrades output is a defect, not a saving.

## Step 5: Model the commercial shape

For a defense contract, cost per unit is not the whole answer.

- **Contract type changes who carries the risk.** On firm-fixed-price, a usage surprise is your loss; on cost-plus it is visible to the customer. See `contract-vehicles-and-clauses`.
- **Price stability.** Provider pricing changes, models are deprecated, and a bid priced on a rate that later moves is exposed. Model a rate-change scenario and treat it as a risk in `risk-management`.
- **Volume uncertainty.** The customer's estimate is an estimate. Model low, expected and high, and know which one the price survives.
- **Deployment constraints change everything.** On-premise or air-gapped inference replaces per-token pricing with hardware, power and sustainment. That is a different model entirely, not a rate substitution.

## Step 6: Present it so it can be challenged

Show the unit, the per-unit build-up, the volume assumptions, the sensitivity to the two or three drivers that dominate, and the scenario range. `business-case` frames the investment case around it; `trade-study-analysis` uses it where cost is a criterion.

A cost model that cannot be challenged cannot be trusted. Making the assumptions visible is what makes the number defensible when someone asks why it is not half as much.
