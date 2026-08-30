---
name: applied-statistics
description: Use statistics correctly on real decisions. Use when running or interpreting a hypothesis test, computing confidence intervals, determining sample size, designing an experiment, comparing two conditions, judging whether a difference is real, or checking whether a statistical claim in a report or paper is supported. Covers doing the analysis and reading someone else's critically.
---

# Applied statistics

Statistics answers one question: **could this result reasonably have happened by chance?** Everything else — tests, intervals, sample sizes — is machinery for answering it in a specific situation.

Most misuse comes from skipping the question and reaching for a test.

## Step 1: State the question before touching data

Write down, before analysis:

- **The comparison.** What against what.
- **The outcome measure**, and why that one.
- **The effect size that matters.** Not the effect you expect — the smallest difference that would change a decision. A 0.3% improvement may be statistically detectable and practically irrelevant.
- **The direction**, if you have one.

Choosing the analysis after seeing the data is how a random pattern becomes a finding. This is why the pre-registration idea exists, and it applies to engineering decisions as much as to research.

## Step 2: Size the sample

The question that decides whether the study is worth running. An underpowered study cannot detect the effect it was run to find, so its null result means nothing, and running it anyway wastes the effort.

Sample size is driven by four things: the effect size you want to detect, the variability of the measure, the significance level, and the power you want — conventionally 80%, meaning a 20% chance of missing a real effect.

Two practical consequences:

**Small effects need large samples, steeply.** Halving the detectable effect roughly quadruples the sample needed. If the sample is fixed, work backwards and state what effect it can actually detect — that is a more honest framing than reporting a null result as "no difference".

**Compute it before collecting**, and record the calculation. A sample size chosen by convenience and justified afterward is not a justification.

## Step 3: Choose the test by the question and the data

| Comparing | Data | Test |
| --- | --- | --- |
| Two independent groups, continuous | Roughly normal, similar variance | Two-sample t-test |
| Two independent groups, continuous | Skewed, small n, or ordinal | Mann-Whitney U |
| Paired measurements | Roughly normal differences | Paired t-test |
| Paired, non-normal | | Wilcoxon signed-rank |
| Three or more groups | | ANOVA, then post-hoc with correction |
| Proportions, two groups | | Two-proportion z-test, or Fisher's exact for small counts |
| Categorical association | | Chi-square, Fisher's exact when expected counts are small |
| Relationship between continuous variables | | Regression, with residuals checked |

Check the assumptions rather than assuming them. Normality matters most at small n; equal variance has corrections; independence is the assumption most often violated and least often checked — repeated measures on the same units are not independent observations, and treating them as such inflates significance.

## Step 4: Report the interval, not just the p-value

A p-value says whether an effect is distinguishable from zero. It says nothing about how large the effect is or whether it matters.

**Report the effect size with a confidence interval, always.** "The new method reduced processing time by 14% (95% CI: 3% to 25%, p = 0.02)" tells a decision-maker what they need. "p = 0.02" does not.

What p-values are not:
- Not the probability the hypothesis is true.
- Not the probability the result was chance.
- Not a measure of effect size — a tiny effect reaches significance with a large enough sample.
- **Not a threshold that makes 0.049 real and 0.051 not.** Report the value and the interval; let the reader weigh it.

**A non-significant result is not evidence of no difference.** It is a failure to detect one, which may mean there is none or may mean the study was too small. The confidence interval distinguishes these: an interval from −1% to +2% supports "no meaningful difference"; one from −30% to +45% supports nothing at all.

## Step 5: Design experiments to isolate what you are testing

When comparing more than one factor, one-at-a-time testing misses interactions and wastes runs. Factorial designs test several factors simultaneously and reveal whether factors interact — which is often the interesting finding.

The design principles that matter more than the design choice:

- **Randomise assignment.** Non-random assignment lets an unmeasured difference explain your result.
- **Block what you cannot randomise.** Batch, day, operator, machine — remove known nuisance variation rather than letting it become noise.
- **Replicate.** Repeated measurements on one unit estimate measurement error; independent units estimate the variation you care about. Confusing them is a common and consequential error.
- **Control what you can, record what you cannot.**

`test-and-evaluation` needs this for trial counts; `measures-of-effectiveness` needs it wherever a measurement claim carries confidence; `ai-evaluation` needs it for evaluation set sizing.

## Step 6: Read other people's statistics critically

The questions that find most problems, in order:

1. **What was the sample size, and was it justified?**
2. **Was the analysis chosen before or after seeing the data?**
3. **How many comparisons were made?** Twenty tests at p < 0.05 produce one significant result by chance. Correction should be applied, and its absence is a red flag.
4. **Is the effect size reported, with an interval?** A paper reporting only p-values is hiding the magnitude.
5. **Are the observations actually independent?**
6. **Does the sample resemble the population the conclusion is about?**
7. **What is not reported?** Missing subgroups, dropped outliers with no rule stated, an outcome measure that changed.

Point 3 is the most common defect in practice, and the easiest to spot: count the comparisons and look for a correction.

## Reference

- `references/reporting-checklist.md` — what a statistical claim must include to be evaluable.
