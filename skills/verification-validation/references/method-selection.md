# Choosing a verification method

Pick the cheapest method that produces genuine belief. Escalating without reason wastes schedule; under-picking produces a matrix nobody trusts.

## The decision

Ask in this order and stop at the first yes.

1. **Can you settle it by looking at the item, a drawing, or the source?** → Inspection.
2. **Is the condition impractical or unsafe to create — service life, extreme environment, statistical margin, catastrophic failure?** → Analysis.
3. **Is the requirement qualitative — the function occurs, the operator can complete the task?** → Demonstration.
4. **Does the requirement contain a number that must be met?** → Test.

## Borderline cases, and the argument that settles them

**Demonstration or test?** If the acceptance sentence contains a number, it is a test. "The operator can complete enrollment" is a demonstration; "within four minutes" makes it a test. Watch for numbers hiding in adverbs — "quickly", "reliably", "without noticeable delay" are numbers that have not been written down yet, and they belong back with `requirements-dev`.

**Analysis or test?** Analysis is legitimate when the condition cannot practically be created, not when testing is merely inconvenient. Twenty-year corrosion life is analysis. Peak concurrent load you could generate on a Tuesday is a test. If the reason for choosing analysis is schedule pressure, say that in the plan rather than dressing it as physics.

**Analysis by similarity.** Acceptable, and frequently abused. It requires three things stated explicitly: the qualified item named, how the new application differs, and why each difference does not invalidate the earlier qualification. Missing any of the three, it is an assertion. This is the single most common hole in an otherwise complete verification program.

**Inspection or demonstration?** Inspection examines a static property; demonstration operates the thing. If the item has to be powered or run, it is not inspection.

## Cost and confidence

| Method | Relative cost | Confidence | Fails badly when |
| --- | --- | --- | --- |
| Inspection | Lowest | High for static properties | Used for behavior |
| Analysis | Low to moderate | Only as good as the model and its assumptions | Assumptions unstated or unvalidated |
| Demonstration | Moderate | Good for presence of function | Used where a threshold matters |
| Test | Highest | Highest, on the configuration tested | The tested configuration is not the delivered one |

That last row is the failure worth watching. Test evidence is only as good as the match between the article tested and the article delivered — record the configuration on every result, and re-examine every closed row when the configuration changes.
