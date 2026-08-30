---
name: cmmc-readiness
description: Prepare for CMMC assessment and manage NIST 800-171 compliance as a defense contractor. Use when scoping a CMMC environment, assessing against 800-171 practices, computing or improving an SPRS score, writing a system security plan or POA&M for CUI, preparing for a C3PAO assessment, or understanding what DFARS 7012, 7019, 7020 and 7021 require. This is your own company's compliance, not a customer system's.
---

# CMMC readiness

The distinction that governs everything here: **`rmf-ato` is about a system you deliver to a customer. This is about your own company handling the customer's information.**

Different obligations, different assessor, different consequence. Failing here does not delay a delivery; it makes you ineligible to hold the contract.

## What actually applies

Four DFARS clauses, and knowing which does what prevents most confusion:

| Clause | Requires |
| --- | --- |
| **252.204-7012** | Safeguard covered defense information to NIST SP 800-171, report cyber incidents within 72 hours, preserve media, support damage assessment |
| **252.204-7019** | Have a current 800-171 self-assessment score posted in SPRS as a condition of award |
| **252.204-7020** | Provide the government access to verify, and flow requirements down to subcontractors |
| **252.204-7021** | CMMC certification at the level the contract specifies |

Flow-down under 7020 is the obligation primes underestimate. Your subcontractors handling CUI carry the same requirements, and their failure is your problem.

## Step 1: Scope, which is most of the work

Scoping is where CMMC costs are decided. An enclave that touches everything is expensive to assess and expensive to maintain; one drawn too tightly excludes something that actually handles CUI, which is worse.

Categorise every asset:

| Category | Definition | Assessment treatment |
| --- | --- | --- |
| **CUI assets** | Process, store, or transmit CUI | Assessed against all practices |
| **Security protection assets** | Provide security capability to the environment | Assessed |
| **Contractor risk managed assets** | Could but are not intended to handle CUI | Documented, policy-governed, spot-checked |
| **Specialized assets** | Test equipment, IoT, OT, GFE, restricted systems | Documented, not fully assessed |
| **Out of scope** | Cannot handle CUI, logically or physically separated | Not assessed — separation must be real |

Two rules that decide whether scoping holds up:

**Find the CUI first.** You cannot scope without knowing where CUI actually is — email, file shares, engineering tools, laptops, the contract folder someone keeps locally, the subcontractor's portal. Data discovery precedes scoping, and the informal copies are the ones that break a scope boundary.

**Separation has to be enforced, not asserted.** An asset declared out of scope because "we don't put CUI there" is in scope. Out of scope means something prevents it.

A tight, well-separated enclave with strong boundary control is usually cheaper to certify and to sustain than a flat network declared entirely in scope.

## Step 2: Assess against the practices

800-171 practices across the familiar families — access control, awareness and training, audit and accountability, configuration management, identification and authentication, incident response, maintenance, media protection, personnel security, physical protection, risk assessment, security assessment, system and communications protection, system and information integrity.

For each: implemented, partially implemented, or not implemented, with evidence. The assessment objectives in 800-171A are what an assessor actually tests against — assess yourself against those rather than against the practice statement, because the objectives are more specific and are where partial implementations get found.

**Every practice needs a written policy and evidence of practice.** A control implemented in the technology with no policy behind it fails; a policy with no evidence anyone follows it fails. Assessors ask for both.

## Step 3: SPRS score

The self-assessment score starts at 110 and subtracts weighted points for each practice not fully implemented — some worth 1, some 3, some 5. A negative score is possible and common on a first honest assessment.

Two disciplines:

**Score honestly.** The score is a representation to the government under 7019. An inflated score is a false statement, with consequences well beyond the contract.

**Partial is not implemented.** A practice implemented in three of five locations is not implemented. Scoring it as such is the single most common inflation.

Improving the score means implementing practices, in weight order — the 5-point items move the number fastest, and they are usually the structural ones worth doing anyway.

## Step 4: SSP and POA&M

Same artifacts as `rmf-ato`, different scope. The SSP describes how each practice is met in your environment. The POA&M lists what is not met, with owners and dates.

CMMC constrains POA&Ms more tightly than RMF: certain practices cannot be on a POA&M at all, POA&M items must close within a defined window, and a score floor applies. Check the current rule before assuming an item can be deferred — this is an area where the rules have changed and are worth verifying rather than remembering.

## Step 5: The assessment

Depending on level and contract, self-assessment, a C3PAO third-party assessment, or government-led. What determines how it goes:

- **Evidence is organised by practice** before the assessor arrives, not gathered during.
- **The scope boundary is documented and defensible**, and the network diagram matches reality.
- **Staff can describe what they do.** Assessors interview. A policy nobody in the organisation can describe is a policy that exists only on paper, and interviews find that quickly.
- **Flow-down is evidenced** — subcontractor agreements carry the clauses, and you know their status.

## Where this connects

- `rmf-ato` — the same disciplines, applied to your enterprise rather than a delivered system. Evidence rarely transfers; the habits do.
- `stig-and-hardening` — configuration evidence for the practices about baseline configuration.
- `supply-chain-security` — flow-down and supplier assurance.
- `export-control-and-markings` — CUI marking is a prerequisite. You cannot protect what nobody has marked.

## Reference

- `references/scoping-worksheet.md` — asset categorisation, CUI discovery, and boundary defensibility.
