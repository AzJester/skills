# Postmortem: [one-line symptom]

| | |
| --- | --- |
| **Date** | YYYY-MM-DD |
| **Severity** | 1 / 2 / 3 |
| **Duration** | HH:MM detection → HH:MM mitigated (total HH:MM) |
| **Authors** | |
| **Status** | Draft / In review / Final |

## Summary

Three sentences. What broke, for whom, how long. No jargon a new joiner would not have.

## Impact

- Users affected: (number, or estimate with its basis)
- Requests failed: 
- Data affected: (lost, delayed, inconsistent, none)
- Revenue or contractual impact: 

State unknowns as unknown. An honest gap is more useful than a confident guess.

## Timeline

Built from timestamped artifacts, not recollection. Cite the source of each entry.

| Time | Event | Source |
| --- | --- | --- |
| | | |

- **Detection delay**: first symptom → first alert
- **Time to mitigate**: first alert → user impact ended

## Root cause

What actually caused it, traced past the first plausible answer. Use `five-whys-analysis` for a linear chain, `fault-tree-analysis` when several conditions had to coincide, `kepner-tregoe-analysis` when several candidate changes compete.

Every time a person appears here, restate it as the condition that allowed or encouraged the action.

## Contributing factors

Things that made it worse, slower to detect, or harder to fix. Not causes, but each one is an action item candidate.

## What went well

Which defenses worked. Name them so nobody removes them later.

## What was luck

Anything that limited impact by chance rather than design — low traffic, someone happening to be watching. Luck is not a control, and next time it may not hold.

## Action items

| Action | Owner | Due | Class |
| --- | --- | --- | --- |
| | | | prevent / detect / mitigate |

Classify each one honestly. Actions that only shorten mitigation do not stop recurrence, and a postmortem full of them has not fixed the problem.
