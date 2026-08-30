# Baseline record and status accounting

## Baseline register

| Baseline | Established | Gate | Approved by | Contents (CI list reference) | Superseded by |
| --- | --- | --- | --- | --- | --- |
| Functional | | SRR | | | |
| Allocated | | PDR | | | |
| Product | | CDR | | | |

A baseline is defined by its content list, not by a date. "The PDR baseline" means nothing unless the CIs and versions it contained are recoverable.

## Configuration item index

| CI ID | Name | Type | Owner | Current version | In baselines | Under control since |
| --- | --- | --- | --- | --- | --- | --- |

**Type** — requirement set, design document, ICD, source component, test procedure, build configuration, third-party dependency, tool.

Include the last three. Uncontrolled build configuration and unpinned dependencies are the most common route by which a delivered system differs from a tested one, and they are the items most often left off the index.

## Change log

| ECR | Date | Class | CIs affected | Decision | New baseline | Verification re-run |
| --- | --- | --- | --- | --- | --- | --- |

The last column is the audit trail that connects a change to the evidence it invalidated. Without it, a VCRM can show green for a configuration that no longer exists.

## Deviations and waivers

| ID | Type | CI | Departure from baseline | Approver | Scope / quantity | Expiry | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | Deviation / Waiver | | | | | | Open / Expired / Closed |

Report the open count at every gate. A count that rises across consecutive gates means the baseline no longer describes the system, and the correct response is a baseline change rather than another waiver.

## The four questions

Status accounting exists to answer these without investigation. If any takes more than a few minutes, the records are not being kept:

1. What is the current configuration of every CI?
2. What was the configuration at a given baseline, test, or delivery?
3. What changes are in flight, and what have they been assessed to affect?
4. What deviations and waivers are open, and when do they expire?
