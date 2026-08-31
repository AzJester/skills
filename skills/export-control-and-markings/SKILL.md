---
name: export-control-and-markings
description: Handle export-controlled and controlled unclassified information correctly. Use when marking a document or deliverable, applying a distribution statement, determining whether something is ITAR or EAR controlled, deciding whether a disclosure to a foreign person or a cloud service is an export, preparing material for release, or answering what marking a technical report needs. A guardrail on how information is handled, not legal advice. `industrial-security` covers facility clearances, personnel clearances and classified handling.
---

# Export control and markings

Two separate regimes get conflated, and the practical consequence of getting either wrong is serious enough that the conservative path is nearly always right.

**Export control** governs who may receive certain technical information, regardless of classification. **CUI** governs how sensitive-but-unclassified information is marked, stored and shared. A document can be subject to both, one, or neither, and the determinations are made by different people on different criteria.

This skill covers recognizing when a determination is needed and applying markings correctly. **It is not legal advice, and it does not make determinations.** Your export control officer, security officer and contracting officer own those. What it prevents is the common engineering failure: handling something incorrectly because nobody thought to ask.

## The rule that governs everything here

**When unsure, stop and ask before disclosing, uploading, emailing or publishing.** Unmarked material sent to the wrong recipient cannot be recalled, and the harm is done at the moment of transmission. The cost of asking is an hour; the cost of being wrong ranges from an incident report to criminal liability.

That asymmetry is the whole reason this skill exists.

## Export control: the two regimes

| | ITAR | EAR |
| --- | --- | --- |
| Governs | Defense articles, services, and technical data | Dual-use and less-sensitive items |
| List | USML — United States Munitions List | CCL — Commerce Control List, with ECCNs |
| Administered by | State Department (DDTC) | Commerce Department (BIS) |
| Character | Strict; presumption of control for USML items | Graduated; control depends on item, destination, end use and end user |

**"Export" is broader than shipping.** The concept that catches people:

- **Deemed export** — disclosing controlled technical data to a foreign person **inside the United States** is an export to their country of nationality. A conversation, a screen share, a repository grant, a colleague reading over a shoulder.
- **Electronic transmission** — email, file share, cloud storage. Where the data physically resides matters, and so does who administers the system.
- **Cloud services** — storing controlled technical data in a service without appropriate controls, or one administered by foreign persons, can constitute an export. This is why FedRAMP authorization status and personnel screening for a service are engineering-relevant facts rather than procurement trivia.
- **Publication and conferences** — presenting, publishing, or posting to a public repository.

Fundamental research and information already in the public domain are treated differently, but **the exclusion is narrower than people assume** and does not survive contractual publication restrictions. Do not self-determine that something qualifies.

## CUI

CUI replaced a sprawl of legacy markings — FOUO, SBU, and others — with a single system built on an official registry of categories.

- Every CUI item belongs to a **category** in the registry, each traceable to a law, regulation or government-wide policy. There is no general-purpose "sensitive" category.
- **Basic** CUI follows standard handling; **Specified** carries additional handling required by its authority.
- Marking requires a **banner** at top and bottom of each page, with the category and any limited dissemination controls, plus a **designation indicator** showing who determined it and under what authority.
- Portion marking may be required.
- The **government designates** CUI. As a contractor you mark what the contract tells you to mark, and when it is unclear you ask rather than deciding.

Legacy markings on old documents do not make them correctly marked today. Re-marking is a decision with an owner, not a find-and-replace.

## Distribution statements

Technical documents carry a distribution statement, and it is separate from both classification and CUI. It states who may receive the document.

| | Available to |
| --- | --- |
| **A** | Public release, unlimited |
| **B** | US Government agencies only |
| **C** | US Government agencies and their contractors |
| **D** | DoD and DoD contractors only |
| **E** | DoD components only |
| **F** | As directed by the controlling office |

Each statement carries a reason and a date, and names the controlling DoD office. **Statement A requires an actual public release review** — it is a determination someone makes, not a default for documents nobody wanted to restrict. Marking something A without that review is the most common distribution error, and it is effectively an unreviewed public release.

Export control warnings appear alongside the distribution statement where applicable, not instead of it.

## Applying this in engineering work

The failure is rarely a deliberate decision. It is a default action taken without thinking.

**Before a document leaves your hands**, ask: what is in it, who is receiving it, and what does it need on it? Deliverables inherit their marking requirements from the contract and its CDRLs — see `contract-vehicles-and-clauses`.

**Before granting repository or drive access**, ask whether the recipient is authorized, including nationality where export control applies. Access grants are disclosures.

**Before using a tool or service** with controlled data — a cloud IDE, an AI service, a diagramming tool, a translation service — ask whether the data may go there. Pasting controlled technical data into an external service is a transmission, and this is now among the most common ways it happens.

**Before publishing or presenting**, obtain the release review. `ieee-publishing`, `dod-technical-report` and `manuscript-submission` all produce material that leaves the organization, and the review precedes submission, not publication.

**Before a meeting with foreign nationals**, know what may be discussed. This includes colleagues and partners, and it includes the whiteboard.

## What good practice looks like

- Marking applied **when the document is created**, not before it is sent. Retrofitted markings miss drafts, and drafts circulate.
- Templates carrying the marking blocks, so the default is marked rather than unmarked.
- A named person to ask, and a culture where asking is routine rather than an admission.
- Access reviewed when people join, change role, or leave — see `rmf-ato` and `cmmc-readiness`.
- Tool and service approval done before use rather than after an incident.

## Reference

- `references/marking-checklist.md` — pre-release checklist and marking block patterns.
