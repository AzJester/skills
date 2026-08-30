---
name: section-508-conformance
description: Meet and document accessibility obligations on federal deliverables. Use when a solicitation or contract requires Section 508 conformance, when producing an accessibility conformance report or VPAT, when testing software or documents against WCAG success criteria, when claiming an exception, or when deciding what accessibility work a federal deliverable actually requires. Covers the federal obligation and its documentation; ui-ux-pro-max covers designing accessible interfaces.
---

# Section 508 conformance

`ui-ux-pro-max` covers building accessible interfaces. This covers the federal obligation attached to them: what a contract requires, how it is tested, and the report an agency will ask for — frequently at proposal time rather than at delivery.

The failure this exists to prevent is discovering the obligation at delivery. Accessibility retrofitted into a finished system is expensive and produces a worse result than designing for it, and the conformance report cannot be written honestly for a product that was never tested.

## Step 1: Know what actually applies

Section 508 of the Rehabilitation Act requires federal agencies to ensure that the information and communication technology they develop, procure, maintain or use is accessible to people with disabilities. It reaches contractors through the contract: agencies impose it on what they buy.

The current standards incorporate the **WCAG success criteria at Level A and AA** as the technical requirement for web content, software and electronic documents. Which WCAG version applies is set by the standards as adopted and sometimes by agency-specific direction, so confirm the version from the solicitation rather than assuming the newest.

**It applies more broadly than to web applications.** Software interfaces, electronic documents delivered under the contract, training material, video content and hardware with a user interface can all be in scope. A programme that makes its application accessible and delivers inaccessible PDF manuals has not met the requirement — see `procedural-documentation` and `dod-technical-report` for the deliverables this reaches.

**Read the solicitation's own accessibility language.** Agencies vary in what they require, when they require evidence, and how heavily they weight it. Some require a conformance report with the proposal.

## Step 2: Design for it, because retrofit is the expensive path

Nothing here is separable from ordinary design quality, which is why it belongs at the start:

- Semantic structure — real headings, lists, tables, landmarks, and form labels tied to their controls
- Keyboard operability for everything, with a visible focus indicator and no traps
- Contrast that meets the ratio requirements
- Text alternatives for meaningful images, and none for decorative ones
- Errors identified in text, with instructions for correcting them
- No reliance on colour alone to convey meaning
- Captions and audio description for media
- Content that reflows and remains usable when zoomed or resized

`ui-ux-pro-max` covers this material in depth for interface work. Treat accessibility as an acceptance criterion from the first sprint rather than as a testing phase.

## Step 3: Test properly, which means three ways

**Automated tools find roughly a third of what matters** and cannot judge whether an alternative text is meaningful, whether a reading order makes sense, or whether a workflow can actually be completed. Reporting automated results alone is the most common defect in a conformance claim.

| Method | Finds |
| --- | --- |
| **Automated scanning** | Missing labels, contrast failures, structural errors — quickly, at scale |
| **Manual inspection** | Reading order, focus order, meaningful alternatives, correct semantics |
| **Assistive technology testing** | Whether a real task can actually be completed with a screen reader, magnification or keyboard only |

**Test the whole task, not the page.** Conformance is claimed per criterion, but usability is per workflow. A form where every field is labelled and the submit button is unreachable by keyboard passes several criteria and fails the user.

**Test the documents too**, with the same seriousness. Tagged structure, reading order, table headers, and alternative text in PDFs and office documents.

## Step 4: Write the conformance report honestly

An accessibility conformance report — commonly produced using the VPAT template — states, criterion by criterion, how the product conforms. Its value is entirely in its honesty, and agencies have seen enough optimistic ones to read them sceptically.

The conformance levels, and what each actually means:

| Level | Means |
| --- | --- |
| **Supports** | Fully meets the criterion, without exception |
| **Partially supports** | Meets it for some functionality, with defined exceptions |
| **Does not support** | Does not meet it |
| **Not applicable** | The criterion does not apply to this product |

Four disciplines:

**"Supports" means fully.** A criterion met everywhere except one screen is *partially supports*, with the exception described. Overstating here is the finding that damages credibility on everything else in the report.

**Explain every remark.** For anything less than full support, say specifically what does not conform, where, and what the effect on a user is. A bare "partially supports" with no explanation is not a usable answer.

**Report against the version and scope you actually tested**, naming the product version, the date, and the methods used. A report with no methodology behind it is an assertion.

**Keep it current.** A conformance report describes a version. Shipping changes make it stale, and delivering a stale report is a misrepresentation rather than an oversight.

## Step 5: Exceptions, claimed properly

The standards allow limited exceptions — including for certain national security systems, where conformance would impose an undue burden, or where it would require a fundamental alteration of the product.

Two things to understand about them:

- **The agency determines whether an exception applies, not the contractor.** You propose and document; they decide.
- **Undue burden means significant difficulty or expense assessed against the agency's overall resources**, not against your programme's budget. It is a high bar, it must be documented in writing, and where it is claimed the agency still has an obligation to provide alternative access.

**Do not use exceptions as a plan.** A programme intending to claim undue burden rather than build accessibly is making a bet on someone else's determination, usually late.

## Step 6: Put it in the contract mechanics

- **Accessibility requirements belong in the work statement** with a stated standard and a verification method — see `sow-and-pws`.
- **Conformance is verifiable**, so it belongs in the VCRM with a method and an event like any other requirement — see `verification-validation`.
- **The conformance report is a deliverable.** Make it a CDRL with a stated format and update points, rather than a document someone assembles the week before delivery.
- **Flow it down to suppliers** whose components appear in the delivered interface. Their inaccessible component is your non-conformance — see `teaming-and-subcontracts`.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Discovered at delivery | Expensive retrofit, poor result | Acceptance criterion from the first sprint |
| Automated results only | Passes scans, unusable with a screen reader | Automated, manual, and assistive technology |
| Criteria tested, tasks not | Every field labelled, workflow impossible | Test whole workflows |
| Documents excluded | Accessible app, inaccessible manuals | Include every delivered artifact |
| "Supports" overstated | Report loses credibility entirely | Full support means everywhere |
| Remarks left bare | Agency cannot evaluate the claim | Say what fails, where, and the user effect |
| Report goes stale | Misrepresents the shipped version | Version it; update on release |
| Exceptions as a strategy | Betting on someone else's determination | Build accessibly; claim exceptions rarely |

The honest one: the conformance report is read by people who know what an optimistic one looks like, and an honest report with known gaps is worth more than a perfect one that does not survive testing.
