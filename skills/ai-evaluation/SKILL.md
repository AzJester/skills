---
name: ai-evaluation
description: Prove an AI system is good enough to field. Use when designing an evaluation harness, choosing metrics for a model or agent, building a task-specific benchmark, setting acceptance criteria under uncertainty, running regression evals against a model or prompt change, designing human review protocols, or doing AI TEVV for a defense program. Evaluation sets depend on `data-strategy-and-governance` for provenance and quality.
---

# AI evaluation

Deterministic verification asks whether output equals expected. That question does not apply here: the same input can produce different output, "correct" is often a judgment, and the system will be wrong sometimes by construction.

So the closure argument changes. `verification-validation` closes a requirement when evidence shows the criterion met. AI evaluation closes one when **performance on a representative sample is good enough, with stated confidence, and the failures are understood and acceptable.**

That last clause carries the weight. A system at 94% with unexamined failures is less trustworthy than one at 89% whose failures are characterized, bounded, and caught by something downstream.

## Step 1: Define good enough before measuring

Set the bar first. A threshold chosen after seeing results is not a threshold.

Derive it from consequence, not from what the model happens to achieve:

- What does a false positive cost? A false negative? They are rarely symmetric.
- What does the current process achieve? A model worse than the humans it assists is a different conversation from one that is better but imperfect.
- What downstream catches errors? A system feeding a reviewer needs a different bar from one acting autonomously.
- What is the acceptable **worst-case subgroup** performance? Aggregate thresholds hide the failure that matters.

Write acceptance criteria as `measures-of-effectiveness` does: threshold and objective, with provenance for both.

## Step 2: Build the evaluation set properly

The evaluation set determines what your numbers mean, and most weak evaluations are weak here rather than in the metric.

- **Representative of deployment**, not of training. Drawn from the same collection as training data, it overstates performance — often dramatically.
- **Held out and kept out.** Once an eval set influences development, it measures fit to itself. Keep a genuinely untouched set for final claims.
- **Large enough to distinguish signal from noise.** `applied-statistics` covers sample size; an eval on 40 examples cannot support a claim about a 3-point difference.
- **Stratified across the subgroups and conditions you care about**, with enough in each stratum to say something about it. Twelve examples from a subgroup supports no claim about that subgroup.
- **Includes the hard cases.** Adversarial inputs, edge cases, ambiguous items, out-of-envelope inputs that should be refused. An eval set of typical cases measures typical performance and nothing about the tail, which is where harm lives.

## Step 3: Choose metrics that match the decision

| System does | Useful metrics | Common mistake |
| --- | --- | --- |
| Classification | Precision, recall, F, PR-AUC; per-class | Accuracy on imbalanced data |
| Ranking / retrieval | Precision@k, recall@k, MRR, nDCG | Measuring retrieval quality by end-to-end answers |
| Extraction | Field-level precision/recall, exact vs partial | Document-level accuracy hiding field failures |
| Generation | Task-specific rubric scoring, human preference, factual consistency | Similarity to a reference answer |
| Agentic / multi-step | Task completion, step accuracy, recovery rate, cost per task | Judging only the final answer |

Two notes that matter more than the table:

**Generation has no single correct answer, so a reference-similarity metric measures the wrong thing.** Score against a rubric that encodes what actually matters for the task, and validate the rubric against human judgment before trusting it.

**Agentic systems need step-level measurement.** A trajectory that reaches the right answer through three wrong turns and a lucky recovery scores identically to a clean one on outcome alone, and behaves very differently under distribution shift.

**On LLM-as-judge**: usable and requires its own validation. Establish agreement with human raters on a sample before relying on it, watch for known biases — position, verbosity, self-preference — and re-validate when the judge model changes. An unvalidated judge is a confident number with unknown meaning.

## Step 4: Human review, designed as measurement

Where humans are the ground truth, they are an instrument and need the same rigor as one.

- **Written guidelines**, developed on examples before the real annotation starts.
- **Inter-rater agreement measured** and reported. Where humans agree 70% of the time, no model can be meaningfully scored above that ceiling, and knowing the ceiling reframes the whole evaluation.
- **Blind to condition.** Raters who know which system produced an output score it differently.
- **Disagreements adjudicated by a documented process**, not by whoever is senior.

## Step 5: Regression evals, run on every change

An AI system changes when the model changes, the prompt changes, a parameter changes, a tool changes, or the retrieval corpus changes. Any of these can move behavior in ways nobody predicts.

Run the suite on every change and diff against the previous run. Track **per-case** movement, not just the aggregate: an unchanged average can hide twenty regressions offset by twenty improvements, and the regressions may be in the cases that matter.

Treat a prompt change with the seriousness of a code change — it goes through `configuration-management`, and the prompt is a configuration item.

## Step 6: Report honestly

- **Confidence intervals, not point estimates.** "87%" from 200 examples has a wide interval, and stating it prevents a decision the evidence does not support.
- **Disaggregated results.** Aggregate plus per-subgroup.
- **The failure taxonomy.** Categorize what went wrong and how often, and say which categories are caught downstream and which reach the user. This is usually the most valuable page of an evaluation report.
- **What was not tested.** Every eval has an envelope. Naming it is credibility; having it discovered is not.

## AI TEVV

For defense programs this is AI test, evaluation, verification and validation, and it sits inside `test-and-evaluation` rather than beside it: evaluation results are DT&E evidence, operational evaluation with real users is OT&E, and adversarial testing of the AI is part of cybersecurity T&E. Results feed `ai-governance` as the Measure function, and limitations flow into the model card.

## Reference

- `references/eval-plan.md` — the evaluation plan, acceptance criteria, and the failure taxonomy.
