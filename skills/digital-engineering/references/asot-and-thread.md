# Authoritative source of truth, and the thread

## Truth map

One row per element. The exercise is short and uncomfortable, which is why it is worth doing early.

| Element | Authoritative home | Derived artifacts | Enforced how? | Owner |
| --- | --- | --- | --- | --- |
| Stakeholder needs | | | | |
| System requirements | | | | |
| Architecture and decomposition | | | | |
| Interfaces | | | | |
| Behavior | | | | |
| Verification methods and evidence | | | | |
| Configuration and baselines | | | | |
| Risk | | | | |

**Enforced how** is the column that separates aspiration from practice. Acceptable answers name a mechanism: the document is generated on build and cannot be hand-edited; the tool is the only write path; a check fails the pipeline when the derived artifact diverges. "By policy" is not enforcement.

Where two tools both hold an element, declare one authoritative and make the sync one-way. Bidirectional sync between two authoritative stores produces conflicts nobody resolves, and the resolution rule tends to be whoever saved last.

## Thread links, in the order worth building

Build these three and make them trustworthy before extending. A thread with many weak links is less useful than one with three strong ones, because nobody believes any of it.

**1. Requirement → design element.** Answers what satisfies each requirement, and which requirements a component carries. Also surfaces orphans in both directions: a requirement nothing satisfies, a component nothing needs.

**2. Design element → verification.** Answers what proves this works, and — read backwards — which verification a design change invalidates. This is the link that makes `configuration-management` impact assessment tractable instead of archaeological.

**3. Both → configuration baseline.** Answers what this looked like at any past gate, test or delivery. Without it, evidence cannot be tied to the thing it was produced against.

Extensions worth adding once those hold: requirement → stakeholder need; design → manufacturing and sustainment data; verification evidence → the accreditation package in `rmf-ato`.

## Questions the thread should answer without archaeology

Use these as acceptance tests for the thread. If any takes more than minutes, that link is not real yet.

- Which stakeholder need is behind this requirement?
- Which components would a change to this interface affect, and on whose side?
- Which verification evidence becomes invalid if I change this element?
- What was the configuration when this test result was produced?
- Which requirements are currently unverified, and which are unallocated?
