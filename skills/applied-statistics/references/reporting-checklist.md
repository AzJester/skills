# Reporting checklist

A statistical claim is evaluable when a reader can judge it without asking you questions. That takes about six elements.

## Every claim carries

- [ ] **The comparison** — what against what
- [ ] **Sample size** per group, and any exclusions with the rule that produced them
- [ ] **The effect size**, in units a reader understands
- [ ] **A confidence interval** on that effect
- [ ] **The test used**, and why it suits the data
- [ ] **The p-value**, as a number rather than a threshold

Missing the interval is the most common omission and the most consequential, because it is what converts a yes/no into a magnitude a decision can use.

## Before the study

- [ ] Question and outcome measure stated
- [ ] Minimum effect worth detecting stated — the decision-relevant one, not the expected one
- [ ] Sample size computed from that effect, with the calculation recorded
- [ ] Analysis plan fixed before data collection
- [ ] Randomisation and blocking decided

## After, before reporting

- [ ] Assumptions checked, not assumed — normality where it matters, variance, and independence
- [ ] Number of comparisons counted, and correction applied where needed
- [ ] Outliers handled by a rule set in advance, not by inspection
- [ ] Missing data described, with how it was handled
- [ ] Any deviation from the analysis plan disclosed

## Phrasing that misleads

| Avoid | Because | Instead |
| --- | --- | --- |
| "No significant difference" | Reads as "no difference" | "No difference detected; the CI spans −4% to +7%, so a meaningful effect is not ruled out" |
| "Highly significant" | Conflates p with importance | Report the effect size |
| "Trending toward significance" | Not a thing | Report the interval and let the reader judge |
| "Proves" | Statistics does not prove | "Is consistent with", "supports" |
| "X% improvement" alone | No uncertainty conveyed | "14% (95% CI: 3–25%)" |

## Sample size, worked backwards

When the sample is fixed by circumstance rather than chosen, do not report a null result as an absence of effect. Instead:

> *With n = 40 per group, this study had 80% power to detect a difference of 12 percentage points or larger. The observed difference was 4 points (95% CI: −5 to +13), so a difference smaller than 12 points cannot be ruled out.*

That is an honest and useful statement. "No significant difference was found" from the same data is neither.
