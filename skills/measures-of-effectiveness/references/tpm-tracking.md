# TPM tracking

One sheet per program. Six to ten measures. Adding an eleventh should require removing one.

## Definition table

| TPM | Type | Definition (versioned) | Units | Threshold | Objective | Measurement method | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | MOE / MOP / KPP | v1.0 — | | | | | |

**Definition** carries a version. When a definition changes — a percentile, an excluded condition, a measurement point — increment it and keep the old one visible. Without this, a redefinition looks identical to an improvement on the chart, and that is the most common way a tracking sheet stops being true.

**Measurement method** includes what it costs to obtain. A measure too expensive to take gets estimated instead, and estimates converge on the plan rather than on reality.

## Profile and actuals

| TPM | Milestone | Planned | Tolerance band | Actual | Source | Variance | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | SRR / PDR / CDR / TRR / Delivery | | ± | | measured / analyzed / estimated | | On profile / In band / Breached |

**Source** matters as much as the value. `measured` came from the system; `analyzed` came from a model; `estimated` came from judgment. A sheet of estimates reported alongside measurements, undistinguished, tells the reader nothing.

**Status** is against the profile at this date, not against the endpoint. A parameter at 60% of target halfway through may be exactly on plan. Judging every measure against its final value makes early tracking useless and encourages the late convergence it is meant to catch.

## On breach

A measure outside its band is not a status, it is a trigger. Do all three:

1. Raise or update a risk in `risk-management`, with the breach as evidence.
2. State the recovery plan, its owner, and the milestone by which the measure returns to band.
3. Report it at the next gate whether or not it has recovered — `technical-reviews` should see the breach and the response, not a chart that has been rebaselined to hide it.

**Rebaselining a profile is legitimate and must be recorded as a decision**, with who approved it and why. A profile quietly redrawn to pass through the actuals is the same failure as a redefined measure, and both are visible only if the history is kept.

## What to report

Per period, per measure: current value, source, planned value at this date, variance, trend against the previous two periods, and status.

The trend column is what makes the sheet predictive rather than historical. A measure in band but moving the wrong way for three periods is a problem now, and reporting only current-versus-plan hides it until the breach.
