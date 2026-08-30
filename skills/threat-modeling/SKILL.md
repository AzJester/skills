---
name: threat-modeling
description: Find security weaknesses in a design before they are built, using STRIDE over a data-flow model, and trace each mitigation to a requirement or a NIST 800-53 control. Use when designing or reviewing a system's security, when asked what could go wrong or how this could be attacked, when preparing an ATO or RMF package, when a design review needs a security section, or when mapping findings to a control family. Applies to architecture, not to code review of a specific function.
---

# Threat modeling

Threat modeling asks four questions, in order: what are we building, what can go wrong, what are we doing about it, and did we do a good job. Most of the value is in the second, and most of the failure is in skipping the first.

This is a design-time activity. It finds classes of weakness in a structure. It does not replace reading code for a specific vulnerability, and it does not replace scanning dependencies.

## Step 1: Model what is actually there

You cannot threat model a system you cannot draw. Build or obtain a data-flow view with four element types:

| Element | Meaning |
| --- | --- |
| **External entity** | Something outside your control: a user, a third-party API, another team's service |
| **Process** | Something that acts: a service, a function, a job |
| **Data store** | Something that holds state: a database, a cache, a bucket, a queue |
| **Data flow** | Something crossing between them, with its protocol and payload |

Then draw the **trust boundaries**: every line where the level of trust changes. Internet to DMZ, DMZ to internal, tenant to tenant, unprivileged to privileged, your code to a vendor's. Threats concentrate on boundaries, and a model without them will produce a shallow analysis.

`architecture-diagrams` renders this well — use a `data flow` spec and mark boundaries as tier containers. If a component's data flows cannot be named, that is the first finding: undocumented flows cannot be secured.

## Step 2: STRIDE, per element

Apply STRIDE to each element rather than to the system as a whole. System-level threat modeling produces generic findings nobody can act on.

| Threat | Violates | Ask |
| --- | --- | --- |
| **S**poofing | Authenticity | Can something claim to be this and be believed? |
| **T**ampering | Integrity | Can data or code be modified in transit or at rest? |
| **R**epudiation | Non-repudiation | Can an actor deny having done it, and would we be able to prove otherwise? |
| **I**nformation disclosure | Confidentiality | Can someone read what they should not? |
| **D**enial of service | Availability | Can someone exhaust or block this? |
| **E**levation of privilege | Authorisation | Can someone gain rights they were not granted? |

Not every threat applies to every element type. External entities can spoof and repudiate but you cannot tamper with them. Data stores rarely spoof. Use `references/stride-by-element.md` for the applicable matrix rather than forcing all six everywhere.

Write each finding as a **scenario**, not a category: not "tampering", but "an authenticated tenant modifies the `tenant_id` in the request body and reads another tenant's records". A finding nobody can picture is a finding nobody will fix.

## Step 3: Rate honestly

For each finding, record likelihood and impact, and the reasoning for both. A rating with no reasoning cannot be challenged, and unchallengeable ratings drift toward whatever the author already believed.

Prefer stating the attacker the threat assumes — unauthenticated internet, authenticated user, malicious insider, compromised dependency, adjacent tenant. Half of all threat-model disagreements are actually disagreements about which attacker is in scope, surfaced late.

## Step 4: Mitigate, and trace it

Each accepted finding gets one of four responses, stated explicitly:

- **Mitigate** — a control that reduces it, named specifically.
- **Transfer** — someone else carries it, and they know.
- **Accept** — with a named person accepting and a reason.
- **Eliminate** — remove the feature or flow.

"We'll be careful" is not a response. Neither is a mitigation with no owner.

Then trace it. A mitigation that exists only in the threat model gets built by nobody:

- Turn each mitigation into a requirement via `requirements-dev`, so it inherits verification and traceability rather than living in a separate document.
- Where the system carries an authorisation boundary, map to the **NIST SP 800-53** control family it satisfies — AC (access control), AU (audit and accountability), IA (identification and authentication), SC (system and communications protection), SI (system and information integrity). `references/control-mapping.md` maps each STRIDE category to its usual families and to the questions an assessor will ask.
- Record the mapping both ways. An assessor asks "which control covers this?"; an engineer asks "why does this control exist?". One table answering both is worth more than two documents.

## Step 5: Did we do a good job?

Check before closing:

- Every element and every trust-boundary crossing was considered, not just the interesting ones.
- Every finding names an attacker and a scenario.
- Every mitigation has an owner and a home outside this document.
- Every acceptance has a named accepter.
- Findings that were considered and dismissed are recorded with the reason. The next reviewer will otherwise raise them again.

Re-run the model when the architecture changes across a trust boundary — new integration, new tenant model, new privilege level. Threat models rot exactly where the system grows.

## Scope

This skill covers design. It does not scan dependencies for known CVEs, review a function for injection, or test a running system. When the question is "is this code safe" rather than "is this design safe", say so and move to code review.

## Reference

- `references/stride-by-element.md` — which threats apply to which element type, with prompting questions.
- `references/control-mapping.md` — STRIDE to NIST 800-53 families, with assessor questions.
