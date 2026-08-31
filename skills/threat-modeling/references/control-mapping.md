# STRIDE to NIST SP 800-53 control families

A mitigation that lives only in a threat model gets built by nobody, and a control with no stated threat gets implemented as paperwork. This table is the join.

Use it in both directions: an engineer asks why a control exists, an assessor asks which control covers a finding.

| STRIDE | Primary families | Typical controls | What an assessor asks |
| --- | --- | --- | --- |
| **Spoofing** | IA, AC | IA-2 identification and authentication, IA-5 authenticator management, AC-3 access enforcement | How is identity established, and how are authenticators issued, rotated, and revoked? |
| **Tampering** | SI, SC, CM | SI-7 software and information integrity, SC-8 transmission confidentiality and integrity, CM-5 access restrictions for change | What detects unauthorised modification, and who is permitted to change what? |
| **Repudiation** | AU | AU-2 event logging, AU-3 content of audit records, AU-9 protection of audit information | What is logged, does it contain enough to attribute an action, and can the actor alter it? |
| **Information disclosure** | SC, AC, MP | SC-28 protection at rest, SC-8 in transit, AC-4 information flow enforcement | Where is the data, who can reach it, and what protects it in each state? |
| **Denial of service** | SC, CP | SC-5 denial-of-service protection, SC-6 resource availability, CP-10 system recovery | What limits consumption, and what is the recovery path when it is exceeded? |
| **Elevation of privilege** | AC | AC-2 account management, AC-3 access enforcement, AC-6 least privilege | Where is authorization decided, and is least privilege demonstrable rather than asserted? |

## Using this without overclaiming

A control family is a starting point for the conversation with your assessor, not a compliance determination. Two cautions worth stating plainly in any document that uses this table:

**A mapping is not an implementation.** Naming AC-6 next to a finding does not mean least privilege exists. The mapping tells you which control the evidence will be filed under; the evidence still has to be produced.

**Baselines differ.** Which controls are in scope depends on the categorization of the system (FIPS 199 low, moderate, high) and on the overlays that apply to it. Do not assert that a control is in scope without the system's actual baseline in front of you. When the baseline is unknown, say the mapping is provisional and name that as an open question rather than guessing.

## Feeding this into the requirements chain

Each mitigation should exit the threat model as a requirement, not as a row in a document nobody reads again:

1. Write the mitigation as a verifiable requirement via `requirements-dev` — it inherits traceability and a verification method.
2. Record the control family alongside it, so the same statement serves the engineer and the assessor.
3. Where a compliance matrix is being built for a proposal or an ATO package, this pairing is the raw material: the requirement is what you did, the control is where it is filed, the threat is why it exists.
