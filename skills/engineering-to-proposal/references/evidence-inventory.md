# Evidence inventory

One row per claim you intend to make. A claim with an empty artefact column does not go in the proposal as past performance.

| # | Claim | Measurable outcome | Artefact (path, commit, doc, record) | Period | Relevance to pursuit | Gap |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | | | | | | |

## Column notes

**Claim** — what you did, stated as a fact about the past. If it needs "we would" or "we can", it is not past performance; move it to the forward-looking section where it belongs.

**Measurable outcome** — the number. Uptime, throughput, defect rate, schedule variance, users served, time to deliver. "Improved performance" is not an outcome; "p95 latency 840ms → 190ms" is. Where no number exists, write `no metric captured` rather than a qualitative substitute — that is a gap worth knowing about before the next project, not something to paper over.

**Artefact** — where the proof lives, specifically enough that someone else could find it. A repository path and commit, a document with a date, a test report, an acceptance record, a customer sign-off. "Team knowledge" is not an artefact.

**Period** — when. Evaluators weight recency, and stale relevance is a common reason strong work scores badly.

**Relevance** — which requirement or evaluation factor of *this* pursuit the claim speaks to. If none, the row is interesting but not useful; mark it and leave it out rather than padding.

**Gap** — what is missing to make the claim fully supportable, and whether it can be closed before submission. This column is the point of the worksheet. A gap found now is a task; found during evaluation it is a deficiency.

## Before handing this on

- Every row has an artefact, or is explicitly marked as an unsupported claim for a human to rule on.
- Every number has a source, and estimates are labelled as estimates.
- Claims about a team's capability are separated from claims about this specific delivery. They are evaluated differently.
- Anything covered by a non-disclosure obligation or a customer's release restriction is flagged before it leaves engineering.
