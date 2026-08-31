---
name: nasa-sti
description: Prepare a report for the NASA STI Program. Use when writing a NASA technical report, technical memorandum, contractor report or conference publication, completing the report documentation page for a NASA deliverable, applying availability and distribution categories, or preparing a document for the NASA Technical Reports Server. Closely related to DoD technical reports, with a different series and review path.
---

# NASA STI reports

The NASA Scientific and Technical Information Program publishes and catalogs NASA-funded work. The mechanics resemble a DoD technical report — a documentation page, a distribution determination, a catalog — with a different series structure and a different review path.

If you already work in the DoD report format, `dod-technical-report` covers most of the shared discipline. This covers what differs.

## The series

Which type you are writing changes the expected content and the review it receives.

| Type | Is |
| --- | --- |
| **TP** — Technical Publication | Completed research with lasting reference value, including extensive data compilations of continuing reference value; the most substantial type, peer reviewed |
| **TM** — Technical Memorandum | Preliminary or specialized findings, working papers, quick-release reports — not extensive analysis |
| **CR** — Contractor Report | Work performed under a NASA contract or grant — the type most contractors produce |
| **CP** — Conference Publication | Proceedings of NASA-sponsored meetings |
| **SP** — Special Publication | Reference works, handbooks, historical and mission accounts |
| **TT** — Technical Translation | Foreign-language material of NASA interest |

Contractors most often produce **CR**. Get the type confirmed early — it determines the number, the cover, and the review.

## Structure

Broadly as in `dod-technical-report`: cover, report documentation page, notice, contents, summary or abstract, introduction, methods, results, discussion, conclusions, recommendations, references, appendices, symbols and abbreviations.

Two NASA-specific points:

**The Summary.** NASA reports typically open with a Summary that functions like an executive summary but is expected to be genuinely self-contained — a reader should be able to take away the findings without the report. Written last.

**Symbols and units.** NASA work uses SI, and reports routinely carry a formal symbols list with units for every quantity. Where non-SI units are used for engineering reasons, give the SI equivalent.

## The report documentation page

Same standard form family as DoD, and the same two fields decide whether the report is ever found: **abstract** and **subject terms**.

NASA adds a **subject category** from its own scheme, which classifies the report within the NASA taxonomy. Choose it deliberately; it drives where the report surfaces in NTRS.

## Availability and distribution

NASA uses availability categories and distribution limitations rather than the DoD's lettered statements. Determine before writing:

- **Publicly available** — the default for most NASA work, and the reason NTRS is the resource it is.
- **Limited distribution** — where export control, ITAR, proprietary content, or an early-release restriction applies.

Where the work is export controlled, the same regime applies as anywhere else — `export-control-and-markings` covers it, and a NASA report is not exempt because the sponsor is a civil agency. ITAR-controlled content in a NASA report is still ITAR-controlled.

Contractor reports may contain the contractor's proprietary information, and asserting that requires marking it correctly at delivery. See `contract-vehicles-and-clauses` on data rights; the failure mode is identical — unmarked material risks being treated as unrestricted.

## Review

NASA STI documents go through a technical review and, where applicable, an export control and public release review before publication. Build the time in. A report finished on the delivery date with no review margin will be late, and the review is not the place to discover a distribution problem.

## Submission to NTRS

The NASA Technical Reports Server is the catalog and the public face. Practical points:

- The documentation page must be complete; an incomplete one delays acceptance.
- Report numbers come from the assigning authority, not from you.
- Format requirements are set by current STI guidance — check it rather than assuming, since it changes.
- Publicly available reports become genuinely public and indexed. Confirm the release determination is real before relying on it.

**This skill orients you; the authoritative sources are the contract, current NASA STI guidance, and your NASA technical monitor.**

## Where this connects

`dod-technical-report` for the shared report discipline and SF 298 practice. `export-control-and-markings` for the control determination, which is not softened by the sponsor being civil. `ieee-publishing` or `acm-paper` where the same work is also going to a conference or journal, which is common and requires the release review to cover both.
