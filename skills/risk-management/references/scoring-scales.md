# Scoring scales

Publish the scale before scoring anything. A scale invented per risk produces a register that cannot be sorted, and sorting is the whole point.

Adjust the thresholds to the programme's size — the shape matters more than the numbers.

## Likelihood

| Score | Label | Meaning |
| --- | --- | --- |
| 1 | Very low | Would be surprising. No precedent on this programme or comparable ones. |
| 2 | Low | Possible. Has happened on comparable programmes, conditions here are unfavourable to it. |
| 3 | Moderate | As likely as not. Genuine uncertainty either way. |
| 4 | High | Expected unless something changes. Precedent exists and conditions favour it. |
| 5 | Very high | Near certain absent intervention. Effectively a planning assumption. |

A 5 is usually not a risk. If it is near certain, plan for it and move the consequence into the baseline.

## Consequence

Score against whichever dimension is worst, and record which one drove the score.

| Score | Cost | Schedule | Performance |
| --- | --- | --- | --- |
| 1 | < 1% of budget | < 1 week, absorbed in float | Barely noticeable; no requirement affected |
| 2 | 1–3% | 1–4 weeks, float consumed | A requirement degraded within tolerance |
| 3 | 3–7% | Slips a minor milestone | A requirement missed; workaround exists |
| 4 | 7–15% | Slips a major milestone or gate | A key requirement missed; no workaround |
| 5 | > 15% | Slips delivery or a contractual date | A KPP missed; the system does not meet its purpose |

## The 5×5 matrix

| L \ C | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| **5** | Med | Med | High | High | High |
| **4** | Low | Med | Med | High | High |
| **3** | Low | Med | Med | Med | High |
| **2** | Low | Low | Med | Med | High |
| **1** | Low | Low | Low | Med | Med |

**Thresholds.** High requires an active handling plan with dated actions and reports at every gate. Medium requires a named owner and a trigger. Low is recorded and reviewed periodically, not worked.

Note the asymmetry: consequence 5 is never Low regardless of likelihood. A low-probability event that ends the programme still needs a plan, and a symmetric matrix hides exactly that case.

## Calibration

Compare realised risks against their original scores each period. If risks that materialised were consistently scored 2, the scale is optimistic and the register is decorative. This is the only way scoring improves, and it depends on `Realised` being tracked separately from `Closed`.
