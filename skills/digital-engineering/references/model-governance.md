# Model governance

An ungoverned model loses trust in about a year. Recovery costs more than governance would have.

## Ownership

| Scope | Owner | May change | Reviews changes |
| --- | --- | --- | --- |

Every part of the model has one owner. Unowned regions are where quality decays first, because nobody is accountable for noticing.

## Quality rules, automated

Rules checked by eye are not checked. Automate these and fail the check rather than filing a comment:

- **Naming** — conventions applied consistently. Inconsistent naming is the first sign of an ungoverned model and makes every search unreliable.
- **Required properties** — each element type carries the properties the programme needs. An element missing its ID or owner is incomplete.
- **No orphans** — no element unconnected to anything. An orphan is either unfinished work or something deleted halfway.
- **No dangling allocations** — every allocation points at something that exists.
- **Requirement coverage** — every requirement allocated; every design element traceable up.
- **Interface completeness** — both ends defined, both owners named. Cross-check against `interface-control`.

## Baselines and change

The model is a configuration item. It is baselined at gates alongside everything else, and changes crossing a baseline go through `configuration-management` change control with a real impact assessment.

The advantage digital engineering buys here is that the impact assessment can be *derived* — which verification a change invalidates is a query against the thread rather than a meeting. That benefit only exists if the thread is trustworthy, which is why the links come before the ceremony.

## Health measures

Track these and report at gates. A model whose health is not measured is one whose decay is discovered by someone relying on it.

| Measure | Signals |
| --- | --- |
| Orphan element count | Unfinished or abandoned work |
| Requirement coverage | Requirements with no allocation |
| Verification coverage | Requirements with no verification link |
| Rule violations | Governance not being enforced |
| Time since last curation pass | Model rot |
| Derived-artifact divergence | Someone is hand-editing outputs |

That last one is the leading indicator. When people start hand-editing generated documents, the model has stopped being authoritative and the programme has not noticed yet.

## Curation as a role

Model curation is a job. Someone owns model health, runs the quality checks, works the orphan list, and has standing to refuse a change that would degrade the model.

Programmes that treat curation as a residual duty spread across a team get a model that nobody owns and everybody works around. The cost of the role is small next to the cost of losing trust in the model, which is paid in reverting to documents while still paying for the tooling.
