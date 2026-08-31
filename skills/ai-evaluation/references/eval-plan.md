# Evaluation plan

Written before results exist. A plan produced after the numbers is a rationalisation.

## Acceptance criteria

| Measure | Threshold | Objective | Derived from | Worst-case subgroup floor |
| --- | --- | --- | --- | --- |

**Derived from** — consequence of error, current process performance, or a customer requirement. A threshold with no provenance gets renegotiated the first time it is missed.

**Worst-case subgroup floor** — the minimum acceptable performance for any subgroup, separate from the aggregate. Without it, a system can pass while failing a population entirely.

## Evaluation set

| | |
| --- | --- |
| Source | |
| Relationship to training data | |
| Size, total | |
| Stratification | subgroup / condition, with n per stratum |
| Hard-case coverage | adversarial, edge, ambiguous, out-of-envelope |
| Held out from development? | |
| Ground truth established how | |
| Inter-rater agreement (if human) | |

**n per stratum** is where subgroup claims live or die. A stratum with twelve examples supports no claim about that stratum, and reporting one anyway is how disaggregated results mislead.

**Inter-rater agreement** sets the ceiling. Where humans agree 78% of the time, a model scored at 85% against that ground truth is measuring something other than correctness.

## Metrics

| Metric | Why this one | Reported with |
| --- | --- | --- |
| | | CI, n, and per-subgroup breakdown |

For generation tasks, attach the rubric and its validation against human judgment. For LLM-as-judge, attach the agreement study and the date of the judge model version.

## Failure taxonomy

Completed after the run, and usually the most useful part of the report.

| Category | Description | Count | Rate | Caught downstream? | Severity |
| --- | --- | --- | --- | --- | --- |

**Caught downstream** is the column that changes decisions. A failure a reviewer reliably catches is a different risk from one that reaches the user silently, even at identical rates. It is also what justifies fielding a system below the accuracy someone hoped for.

## Regression suite

| | |
| --- | --- |
| Cases in suite | |
| Triggered by | model / prompt / parameter / tool / corpus change |
| Comparison | per-case diff against previous run, not aggregate only |
| Blocking threshold | what stops a release |

Per-case diffing is the point. An unchanged aggregate can conceal offsetting regressions and improvements, and the regressions are not necessarily in cases you can afford to lose.

## Limitations

What this evaluation does not establish. Populations not represented, conditions not tested, time period of the data, and anything the ground truth cannot adjudicate.

Every evaluation has an envelope. Stating it is what makes the results usable by someone who was not involved.
