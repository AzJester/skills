# Interface control document

**ICD number** · **Revision** · **Date** · **Baseline status**

## 1. Parties and signatures

| Side | Owning party | Technical POC | Approver | Date signed |
| --- | --- | --- | --- | --- |
| A | | | | |
| B | | | | |

Unsigned by both sides, this document is a proposal. Say so on its face rather than letting it circulate as an agreement.

## 2. Scope

What this interface covers, and explicitly what it does not. Name the adjacent interfaces so a reader can tell which document governs what.

## 3. Interface description

What crosses, in which direction, and why it exists. A diagram helps here — `architecture-diagrams` renders the data-flow view.

## 4. Physical and transport

Connector, medium, protocol and version, endpoint and addressing, network path and any intermediaries that terminate or inspect traffic.

## 5. Data

Schema or message definitions. For every field: name, type, **units**, precision, range, mandatory or optional, and default when absent.

Units and precision are stated for every quantity without exception. This section is where most integration defects are prevented.

## 6. Behavior

Which side initiates. Request/response or event. Sequencing and ordering guarantees. Idempotency, and what a duplicate means. State held on either side, and by whom.

## 7. Timing and volume

Rate, latency budget, timeout, retry policy including backoff and maximum attempts, message size limits, throughput and burst tolerance, quotas and what happens at the quota.

## 8. Error handling

The error taxonomy: every condition, its code, and its meaning. Which side retries and which side gives up. Behavior on partial failure. How each side degrades when the other is unavailable.

Specified at the same level of detail as the happy path. If this section is shorter than section 5, it is not finished.

## 9. Security

Authentication and authorization mechanism, credential issuance and rotation, transport protection, audit expectations on each side. Cross-check against `threat-modeling` — an interface is a trust boundary, and its threats belong in the model.

## 10. Lifecycle and versioning

Startup and shutdown ordering. How the interface is versioned. Deprecation policy, including notice period and parallel-running expectations. What each side does on encountering an unknown version.

## 11. Assumptions

Each side records what it assumes about the other that this document does not require.

| Side | Assumption | If untrue |
| --- | --- | --- |

Every row is a missing requirement or a latent defect. Resolve them before signature where the consequence column is serious.

## 12. Verification

How the interface is verified: each side independently, the pair at integration, and the error cases. Cross-reference the VCRM rows in `verification-validation`.

## 13. Open items

Anything unresolved at this revision, with an owner and a date. An ICD signed with open items is honest; one signed with the open items removed is not.

## 14. Change log

| Rev | Date | Change | Backward compatible | Approved by (both sides) |
| --- | --- | --- | --- | --- |
