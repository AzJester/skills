# Gate entry and exit criteria

Adapt to the program. What must not be adapted away is that every gate has criteria capable of failing it.

The **Source** column names where the artifact comes from in this collection.

---

## SRR — System Requirements Review

*Are the requirements the right ones, and are they achievable?*

**Entry**
- Stakeholder needs captured and traceable to a source — `concept-dev`
- Draft system requirements written and reviewable — `requirements-dev`
- Concept of operations described
- Initial risk register populated — `risk-management`
- Package distributed with reading time

**Exit**
- Every requirement is necessary, verifiable, unambiguous and traceable to a need
- A nominal verification method is assigned to every requirement — `verification-validation`
- No requirement depends on technology at an unacceptable maturity, or the dependency is a scored risk
- Requirements achievable within cost and schedule, with the argument recorded
- Requirements agreed and held stable, ready to baseline at SFR

---

## SFR — System Functional Review

*Does the functional decomposition satisfy the requirements?*

**Entry**
- Functional decomposition complete to the next level — `system-dev`
- Requirements allocated to functions, with no orphans in either direction
- Major interfaces identified — `interface-control`

**Exit**
- Every requirement allocated to at least one function
- Every function traces up to at least one requirement
- Interface boundaries identified and owners named
- **Functional baseline established and placed under configuration control** — `configuration-management`

---

## PDR — Preliminary Design Review

*Is the design approach sound enough to detail?*

**Entry**
- Preliminary design documented, architecture defined — `system-dev`
- Trade studies complete for the major decisions, alternatives recorded — `trade-study-analysis`
- Interface control documents drafted — `interface-control`
- Verification approach defined, VCRM populated — `verification-validation`
- Risk register current, with handling plans for all High risks — `risk-management`
- TPMs defined with planned profiles — `measures-of-effectiveness`
- Security posture assessed where applicable — `threat-modeling`

**Exit**
- Design satisfies the allocated requirements, demonstrably rather than assertedly
- Major trade-offs made, rationale recorded, rejected alternatives named
- Interfaces defined well enough for both sides to proceed independently
- No High risk without a funded handling plan
- Margins identified and adequate — mass, power, timing, whatever the domain measures
- **Allocated baseline established and placed under configuration control** — `configuration-management`

---

## CDR — Critical Design Review

*Is the detailed design complete enough to build?*

**Entry**
- Detailed design complete, drawings and specifications releasable
- Interfaces controlled and agreed by both parties, not merely drafted
- VCRM complete: method, level and event assigned for every requirement
- Test procedures drafted for the major verification events
- Long-lead procurement identified and risk-assessed

**Exit**
- Design is buildable as documented, with no open design decisions
- All interfaces signed by both sides
- Verification program executable within schedule
- Remaining risks acceptable with named accepters
- **Product baseline established**

---

## TRR — Test Readiness Review

*Are we ready to run verification?*

**Entry**
- Test procedures written, reviewed, and dry-run where practical
- Test article configuration known and recorded, matching what will be delivered
- Facilities, instrumentation and staff available
- Success criteria agreed **in writing before** any test runs
- Failure handling agreed: what constitutes a stop, who decides, what happens next

**Exit**
- Procedures adequate to produce the evidence the VCRM expects
- Configuration under test documented and matched against the product baseline
- Data collection sufficient to judge pass or fail without re-running
- Anomaly and stop-test process agreed

---

## FCA / PCA — Functional and Physical Configuration Audit

*Does the built item meet its requirements, and match its documentation?*

**Entry**
- Verification complete, evidence assembled — `verification-validation`
- As-built configuration documented — `configuration-management`
- Deviations and waivers listed with approvals

**Exit**
- **FCA**: every requirement has accepted evidence, or an approved waiver
- **PCA**: the as-built item matches the as-documented product baseline
- Discrepancies dispositioned, not merely listed
