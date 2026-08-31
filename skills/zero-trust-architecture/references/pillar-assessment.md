# Pillar maturity assessment

One row per pillar. This table is usually the most useful artifact in a ZT engagement, because it converts a philosophy into a funded plan.

| Pillar | Current state (evidence) | Current level | Required level | Gap | Closing activity | Owner | Dependency |
| --- | --- | --- | --- | --- | --- | --- | --- |
| User | | Baseline / Target / Advanced | | | | | |
| Device | | | | | | | |
| Application & workload | | | | | | | |
| Data | | | | | | | |
| Network & environment | | | | | | | |
| Automation & orchestration | | | | | | | |
| Visibility & analytics | | | | | | | |

## Column notes

**Current state (evidence)** — what is actually deployed, with something that shows it. A maturity claim with no evidence is an aspiration, and aspirations are what ZT assessments are full of.

**Required level** — from the requirement, per pillar. Not a single level applied across all seven. Requirements differentiate, and pricing should too.

**Dependency** — what must exist first. Most ZT dependencies run in one direction: identity and device posture underpin nearly everything, and data tagging underpins data-pillar policy. Sequencing that ignores dependencies produces a plan that stalls at the second activity.

## The two pillars to check hardest

**Data.** Attribute-based access to data is where zero trust delivers its actual value, and tagging is the work everyone defers. A program claiming Target on Data with no classification scheme, no tagging mechanism, and no attribute-based policy has claimed a level it does not hold.

**Visibility & analytics.** Without it there is no evidence any other pillar works. A ZT design with strong enforcement and weak visibility cannot pass an assessment, because nothing demonstrates enforcement happening.

## Sequencing

Identity and device posture first — most other pillars make access decisions using their outputs. Visibility early, because it is how you prove the rest. Data tagging started early because it is slow, even if its policy comes later. Automation last, because automating an immature policy set scales the mistakes.

## Failure modes worth naming in a plan

- **VPN relabelled.** Network position granted, then trusted. The most common false claim.
- **Enforcement at the perimeter only.** One decision made far from the resource, trusted thereafter.
- **Policy nobody can read.** Expressed as rules rather than in terms the data owner can review.
- **Exceptions accumulating.** Each reasonable, collectively meaning policy no longer describes reality. Track the exception count as a health measure.
- **No answer for the policy point being down.** Fail closed stops the mission; fail open stops being zero trust. Undecided means it will be decided during an incident.
