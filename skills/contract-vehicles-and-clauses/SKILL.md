---
name: contract-vehicles-and-clauses
description: Understand what a contract type and its clauses commit you to. Use when assessing which party carries risk under a contract type, structuring or reading CLINs, identifying the FAR and DFARS clauses that change engineering obligations, understanding data rights and IP consequences, or judging how a contract vehicle shapes a solution and its price. Covers the engineering and delivery consequences, not contract negotiation or legal advice. `sow-and-pws` covers writing the work description itself. `negotiation` covers negotiating them.
---

# Contract vehicles and clauses

Engineering decisions are made inside a contract, and the contract decides who pays when the estimate is wrong. A technically excellent solution priced under the wrong contract type is a loss-making solution.

This skill covers what a contract type and its clauses mean **for the work**. It is not legal advice, and the contracts organisation owns the actual terms — the point here is that engineering choices have contractual consequences and should be made knowing them.

## Contract types, and who carries the risk

| Type | Contractor is paid | Risk sits with | Fits |
| --- | --- | --- | --- |
| **FFP** — firm fixed price | A fixed amount, regardless of cost | **Contractor** | Well-defined scope, understood technology, stable requirements |
| **FPIF** — fixed price incentive | Target cost and fee, with a share line | Shared, per the share ratio | Scope mostly understood, some cost uncertainty |
| **CPFF** — cost plus fixed fee | Allowable cost, plus a fixed fee | **Government** | Genuine uncertainty; research and development |
| **CPIF** — cost plus incentive fee | Cost, plus fee varying with performance | Shared | Uncertain, with measurable outcomes to incentivise |
| **CPAF** — cost plus award fee | Cost, plus fee assessed subjectively | Government, with performance pressure | Where quality is judged rather than measured |
| **T&M / LH** | Fixed labour rates against hours | Mostly government; contractor carries rate risk | Scope that cannot be estimated in advance |

Three consequences engineering actually feels:

**Under FFP, every hour of rework is your money.** An estimate that was optimistic, a requirement that was ambiguous, or a technology less mature than assumed comes directly out of margin. This is why `trl-assessment` and `risk-management` matter commercially and not only technically — bidding FFP on a TRL 4 critical element is a decision to absorb the maturation cost.

**Under cost-plus, the government sees your performance.** EVM reporting is usually required, variances are visible, and CPI is a customer-facing number. See `earned-value-management`.

**T&M has a ceiling.** Work beyond it is unfunded, and continuing past a ceiling without a modification is a problem for both parties.

## CLIN structure shapes delivery

Contract line items are how the work is divided for pricing and payment, and they are not merely administrative.

- **Different CLINs can carry different types.** Fixed-price production alongside cost-plus development is common, and the boundary between them is a real engineering boundary.
- **Funding is per CLIN.** Work performed against an unfunded or exhausted CLIN is work performed at risk.
- **Options are not commitments.** A solution architecture depending on an option that is never exercised has a gap where its funding was.
- **Deliverables attach to CLINs.** Which brings in CDRLs.

**CDRLs and DIDs** define what you must deliver as data — reports, drawings, models, test results, software — in what format, on what schedule, to what standard. A DID specifies the content and format of each item. Read the CDRL list early: it is a substantial and frequently underestimated part of the technical work, and the format requirements often dictate tooling. `dod-technical-report` covers the format most of them take.

## Clauses that change engineering obligations

Not exhaustive, and not a substitute for reading the contract. These are the ones whose engineering consequences are most often discovered late.

**Data rights** — the clause family that determines who may use, modify and disclose what you deliver. The distinctions carry real money:

| Rights | Government may |
| --- | --- |
| Unlimited | Use, modify, disclose to anyone, for any purpose |
| Government purpose | Use and disclose within government purposes, including to your competitors for government work |
| Limited (technical data) / Restricted (software) | Use within government, tightly bounded |
| Specially negotiated | Whatever was agreed |

The rights asserted depend substantially on **who funded the development**. Privately funded IP can generally be delivered with limited or restricted rights; work developed under the contract generally cannot. Assertions must be made at the right time and marked correctly — the practical failure is delivering unmarked material, which risks it being treated as unlimited rights. That is an engineering process problem, not only a legal one, because engineers produce the deliverables.

**Cybersecurity** — DFARS 252.204-7012 and its companions impose safeguarding, incident reporting, and flow-down obligations on your own systems. See `cmmc-readiness`.

**Specifications and standards** — a contract may invoke military or industry standards that carry substantial process obligations. Establish which are compliance documents and which are guidance, because the difference is a large cost.

**Changes** — the clause that lets the government direct changes within scope. Work performed on direction that turns out to be outside scope, without a modification, may be unrecoverable. Constructive change — being directed informally by someone without authority — is a common and expensive trap. The contracting officer is the only person who can change the contract.

**Flow-down** — obligations that must pass to subcontractors. Their non-compliance is your non-compliance. See `supply-chain-security`.

## What this means for a solution

- **Contract type is a risk input.** It determines who absorbs an overrun and belongs in `risk-management` as such.
- **Immature technology on fixed price is a priced decision.** Either mature it first, price the maturation, or propose a contract type that fits the uncertainty.
- **CDRLs are scope.** Estimate them; they are commonly 5–15% of technical effort and are frequently omitted from the estimate entirely.
- **Data rights shape architecture.** Which components you build, buy, or reuse from internal investment determines what you can protect. That decision belongs at design time, not at delivery.

## Reference

Read the contract. This skill orients you toward what to look for; it does not substitute for the document or for your contracts organisation.
