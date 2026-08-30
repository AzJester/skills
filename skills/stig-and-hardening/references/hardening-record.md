# Hardening and tailoring record

One row per item not applied as written. This document is read by an assessor who was not in any of the conversations.

| Item ID | Benchmark & version | Severity | Setting as written | Disposition | Reason | Compensating control | Approved by | Date | Review by |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | STIG / SRG / CIS, release | CAT I/II/III | | Applied / Tailored / Exception / Open | | | | | |

## Disposition

**Applied** — the setting is in place as written. Not recorded here; it appears in the scan.

**Tailored** — the item does not apply, with a factual reason. The feature is absent, the interface does not exist, the component is not present.

**Exception** — the item applies and is deliberately not applied, because it breaks a named mission function. Requires a compensating control and a named approver. Time-bounded with a review date.

**Open** — the item applies, is not applied, and there is no accepted reason. This goes on the POA&M in `rmf-ato`, not here.

The distinction between *tailored* and *exception* is the one assessors probe. Tailored means it does not apply. Exception means it applies and you chose otherwise. Recording an exception as a tailoring is the most common way a hardening record loses credibility.

## What makes a reason defensible

A reason has to name something checkable:

- **Good** — "The system has no wireless interface. Verified: no wireless hardware present, driver stack not installed."
- **Good** — "Setting breaks the flight-planning service, which requires the legacy cipher for the GCCS interface until it is upgraded in FY27. Compensating: the interface is confined to a dedicated segment with traffic inspection and per-session logging."
- **Weak** — "Not applicable to our architecture."
- **Weak** — "Causes operational impact."
- **Weak** — "Risk accepted by the programme." Which person, on what date, for how long?

## Health measures

Report with the scan results, not separately:

| Measure | What a bad value means |
| --- | --- |
| Open CAT I count | An authorization problem now, not a backlog |
| Exceptions with expired review dates | Nobody is revisiting; exceptions have become permanent |
| Exception count trend | Rising means the baseline no longer matches operational reality |
| Time since last scan | Evidence currency; a stale scan is not evidence |
| Drift findings since last scan | Changes are bypassing configuration control |

Drift findings are the most diagnostic. A recurring drift on the same setting is a process problem, and correcting the setting each time without asking how it moved guarantees it moves again.
