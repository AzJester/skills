# AI use case record

One per use case, not per model. The same model in two uses is two records — the impact, oversight and envelope differ.

## Identification

| | |
| --- | --- |
| Use case | |
| Owner (accountable person) | |
| Model(s) and version | |
| Status | Proposed / In development / Deployed / Retired |
| Date and reviewer | |

## What it does

**Decision or output** — specifically, in one sentence a non-specialist understands.

**Who is affected** — users, and people affected without interacting with it.

**Human position** — in the loop / on the loop / out of the loop.

**Consequence of error**

| | Consequence | Who bears it | Detectable? |
| --- | --- | --- | --- |
| False positive | | | |
| False negative | | | |

Asymmetry here drives threshold selection. A system tuned to a balanced metric when the errors are unbalanced is tuned to the wrong thing.

**Operating envelope** — populations, data types, conditions, volumes it was built and evaluated for. Everything outside is untested.

**Out-of-scope uses** — explicit. This field prevents the neighbouring-use failure.

## Impact determination

| | |
| --- | --- |
| High-impact AI? | Yes / No — reasoning (does the output serve as a principal basis for decisions with legal, material, binding or significant effect? Note any rights or safety dimensions in the reasoning) |
| Determination made by / date | |
| Obligations triggered | |

Determine early. A determination made under deadline goes whichever way is convenient.

## Oversight design

| Question | Answer |
| --- | --- |
| What does the reviewer see beyond the output? | |
| How much time per item, realistically? | |
| How does the reviewer disagree, mechanically? | |
| Is override tracked, and by whom? | |
| What is the expected override rate? | |
| What counters automation bias? | |

**Expected override rate** deserves a number. Measuring against it is how you find out whether oversight is real: an override rate near zero usually means rubber-stamping rather than accuracy, and finding that early is much cheaper than finding it after a bad decision.

## Monitoring and triggers

| Signal | Baseline | Threshold | On breach |
| --- | --- | --- | --- |
| Input distribution drift | | | |
| Output distribution shift | | | |
| Performance vs ground truth | | | |
| Override rate | | | |
| User-reported failures | | | |

**On breach** names an action and an owner: re-evaluate, retrain, restrict scope, withdraw. Agreed in advance, because a threshold negotiated during an incident is not a threshold.

## Disengagement

| | |
| --- | --- |
| Who can disable it | |
| On what evidence | |
| How long that takes | |
| What the mission does without it | |

Required by the governable principle. A system nobody can turn off quickly is not governable regardless of the documentation.
