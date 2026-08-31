# Technology maturation plan

One plan per critical technology element below its target. The plan, not the number, is the deliverable.

## Element and gap

| | |
| --- | --- |
| **Element** | |
| **Current TRL** (evidence-backed) | |
| **Target TRL** | |
| **Needed by** | Gate / date |
| **Levels to advance** | |

## Step plan

One row per level. Levels advance one at a time — a row that spans two levels is usually hiding the environment change, which is the expensive part.

| From → To | Demonstration required | Environment and stressors | Facility / resource | Cost | Duration | Finish by | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4 → 5 | | Relevant: name the stressors | | | | | |
| 5 → 6 | | | | | | | |

Two rows deserve extra scrutiny whenever they appear:

**4 → 5** — the first exposure to real stressors, and where promising technology most often stops. Budget for the possibility that it fails.

**6 → 7** — moving a prototype into the operational environment. The remaining work is integration and environment rather than technology, and it is routinely underestimated because the technology already "works".

## Fallback

Not optional. An element with no alternative is a single point of program failure.

| | |
| --- | --- |
| **If maturation fails, we** | Alternative technology / reduced capability / descope / buy rather than build |
| **Decision point** | The date by which the fallback must be chosen for it to still be viable |
| **Fallback lead time** | |
| **Who decides** | |

The decision point matters more than the fallback. A viable alternative chosen too late is not an alternative.

## Risk linkage

Every element below its required level at the gate it is needed is a risk. Record it in `risk-management` as:

> **If** \<element\> does not reach TRL \<target\> by \<gate\>, **then** \<consequence to schedule, cost, or capability\>, **because** \<what makes maturation uncertain\>.

Handling is this maturation plan; contingency is the fallback above; the trigger is the decision point.

## Reporting

At every gate report, per element: current level, evidence, target, whether on plan, and what has changed since the last gate. `technical-reviews` should see the trajectory rather than a snapshot — an element static at TRL 5 across two gates is a problem the single number does not convey.
