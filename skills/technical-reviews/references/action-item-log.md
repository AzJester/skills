# Review item and action log

RIDs are raised before and during the review; actions are what survives it. Track both in one place so nothing is dispositioned by being forgotten.

| ID | Gate | Raised by | Date | Type | Item | Severity | Disposition | Owner | Due | Closure criterion | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RID-001 | PDR | | | RID / Action | | Major / Minor / Editorial | Accept / Accept-defer / Reject | | | | Open / Closed |

## Column notes

**Type** — a RID is a discrepancy raised against the package; an action is work agreed as a result. A RID can be dispositioned without generating an action, if rejected with reason.

**Severity** — `Major` means the gate's exit criteria are affected and the decision depends on it. `Minor` means it should be fixed but does not gate. `Editorial` means it does not change meaning. Severity is assigned by the reviewer and may be argued, but not silently downgraded by the reviewed party.

**Disposition** — one of three, each requiring something:
- *Accept* → an action, an owner, a date.
- *Accept-defer* → the same, plus the gate at which it will be revisited.
- *Reject* → a written reason. Rejecting without one is how reviewers learn not to bother.

**Closure criterion** — what will be true when this is done, written when the action is raised. "Addressed" is not a criterion; "ICD-004 signed by both parties" is.

**Status** — closed means the closure criterion was met and someone other than the owner confirmed it.

## Reporting at the next gate

Open the next gate with this log, not with the new package. Report:

- Actions closed, with evidence
- Actions overdue, with the reason and a new date
- Actions deferred again — a second deferral is a signal, and a third means the item is not going to be done and should be dispositioned honestly instead

A program that carries the same action through three gates has a decision to make about it, not a date to reset.
