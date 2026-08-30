# Verification cross-reference matrix

One row per requirement. No requirement without a row, no verification event without a requirement behind it.

| Req ID | Requirement text | Method | Level | Verification event | Success criteria | Evidence artefact | Status | Closed by |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | | I / A / D / T | comp / subsys / system | | | | Open / In work / Passed / Failed / Waived | |

## Column notes

**Method** — Inspection, Analysis, Demonstration, Test. One primary method per row. Where two are genuinely needed (analysis for the extremes, test for the nominal), split into two rows rather than writing "A/T", so each has its own evidence and status.

**Level** — where verification happens. A system-level requirement verified at component level proves the component only; if that is nonetheless sufficient, state the argument in the analysis, not in this cell.

**Success criteria** — the numeric or observable threshold that decides pass or fail, written before the event runs. Criteria written after seeing the data are not criteria.

**Evidence artefact** — a retrievable pointer: report number, data file, procedure run record, photograph. "Team observed" is not evidence.

**Status** — `Waived` and `Failed` are legitimate end states. A matrix with no reds usually means reds were relabelled, not that none occurred.

**Closed by** — the person accountable for the judgement that the evidence supports the claim. Not the person who ran the test.

## Completeness checks

Run these before the matrix is baselined, and again before any review that depends on it.

1. **Coverage** — every requirement in the baseline appears exactly once. Duplicates get closed twice and fixed nowhere.
2. **Traceability upward** — every verification event maps to at least one requirement. An orphan event is invented scope or a missing requirement.
3. **Testability** — every row with method `Test` has a measurable criterion in the requirement text. If it does not, the requirement is the defect; send it back rather than inventing a criterion here.
4. **Level sufficiency** — every row where the verification level is below the requirement level carries a stated argument for why that is enough.
5. **Similarity claims** — every `Analysis` row resting on similarity names the qualified item and the differences dismissed.

## Status roll-up

Report these four numbers, not a percentage:

- Requirements with evidence accepted
- Requirements in work
- Requirements not started
- Requirements failed, waived, or carrying a deviation

A single percentage hides the fourth number, which is the one anyone reviewing the programme actually needs.
