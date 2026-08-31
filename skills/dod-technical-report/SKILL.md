---
name: dod-technical-report
description: Write a DoD technical report for DTIC submission or contract delivery. Use when producing a technical report, study, or CDRL deliverable for a defense customer, completing an SF 298 report documentation page, applying a distribution statement, preparing a report for DTIC, or structuring a study so it survives contract review. Covers report structure, front matter and submission mechanics rather than the technical content itself.
---

# DoD technical report

A DoD technical report differs from a journal paper in what it is for. A paper argues a contribution to a field. A report delivers findings to a customer who paid for them, gets cataloged, and is retrieved years later by someone who was not there.

That third property drives most of the format. The front matter exists so a stranger can find the report, know whether they may read it, and know what is in it without reading it.

## Before writing: three determinations

Make these first. Each changes the document, and discovering one late means reworking front matter and possibly the whole release path.

**1. Distribution statement.** Who may receive this — A through F. Statement A requires an actual public release review; it is a determination, not a default. See `export-control-and-markings`.

**2. Export control and CUI status.** Whether the content is controlled, and what markings that requires on every page.

**3. The CDRL and its DID.** If this is a contract deliverable, a Data Item Description almost certainly specifies its content, format, and sometimes its section order. **The DID overrides everything in this skill.** Read it before writing, not before submitting — DIDs routinely mandate structure that is expensive to retrofit.

## Structure

Conventional order. A DID may modify it, and where it does, the DID wins.

**Front matter**

1. **Cover** — title, authors, performing organization, report number, date, distribution statement, and any export control warning.
2. **SF 298 — Report Documentation Page.** Standard form, and the thing catalogs index on. Detailed below.
3. **Notices** — disclaimers, sponsorship acknowledgment, and the standard statement that views are the author's and not necessarily the sponsor's, where required.
4. **Table of contents**, plus lists of figures and tables.
5. **Preface or acknowledgments**, where used.

**Body**

6. **Executive summary** — findings and recommendations, self-contained, readable by someone who reads nothing else. Many readers read only this. Write it last and write it for a decision-maker, not a specialist.
7. **Introduction** — background, problem, objective, scope, and what the report covers and does not.
8. **Approach or methodology** — what was done, in enough detail to be assessed and, where relevant, repeated.
9. **Results** — what was found. Findings separated from interpretation.
10. **Discussion** — what the results mean, their limitations, and how they compare to prior work.
11. **Conclusions** — what is now known. Traceable to results; a conclusion the results do not support is the flaw reviewers find first.
12. **Recommendations** — what should be done, by whom. Distinguish these from conclusions; they are different claims and are often best in separate sections.

**Back matter**

13. **References**
14. **Appendices** — data, derivations, code, test procedures, supporting detail.
15. **List of symbols, abbreviations and acronyms**
16. **Distribution list**, where required.

## The SF 298

The Report Documentation Page is how the report is cataloged and found. Filling it carelessly means a report nobody retrieves.

Key blocks and what they need:

| Block | Content | Common error |
| --- | --- | --- |
| Report date | Publication date | Draft date left in |
| Report type | Final, interim, annual, technical | Omitted |
| Dates covered | Period of the work | Left blank |
| Title | Descriptive, no unexpanded abbreviations | Marketing-style title nobody searches |
| Contract / grant / program element / project / task / work unit numbers | From the contract | Wrong or partial; these are how funding is traced |
| Author(s) | Full names | Initials only |
| Performing organization and report number | Yours | |
| Sponsoring agency and acronym | Who funded it | |
| Distribution statement | The full statement | Abbreviated to a letter |
| Supplementary notes | Prior versions, related reports | |
| **Abstract** | ~200 words, unclassified, self-contained | Written for specialists; assumes the report |
| **Subject terms** | Keywords for retrieval | Left blank — this is what makes the report findable |
| Security classification of report, abstract, and page | Each separately | One value applied to all three |
| Limitation of abstract | Usually UU or SAR | |
| Number of pages | | |
| Responsible person and phone | | |

Two blocks decide whether the report is ever found again: **abstract** and **subject terms**. Write the abstract to stand alone, without acronyms the reader has not met, and choose subject terms someone searching would actually use rather than the ones you prefer.

## Writing conventions

- **Findings and interpretation stay separate.** Results say what happened; discussion says what it means. Blending them is the most common structural weakness.
- **Every recommendation traces to a finding.** A recommendation with no result behind it will be challenged, correctly.
- **State limitations explicitly.** What the study did not cover, what the data could not support, where uncertainty remains. `applied-statistics` for claims resting on data.
- **Define every acronym at first use**, and list them all. Reports are read by people outside the program.
- **Figures and tables are numbered and referenced**, each with a caption that stands alone. A reader skimming figures should still learn something.
- **Classification and control markings on every page**, applied when written rather than before delivery.

## Submission to DTIC

Reports are submitted for cataloging and are then discoverable according to their distribution statement. Practical points:

- Submission requires the completed SF 298; an incomplete one delays or blocks acceptance.
- The distribution statement determines who can retrieve it. Statement A becomes publicly available — confirm the release review actually happened.
- Format requirements are specified by the current submission guidance; check it rather than assuming, since it changes.
- Reports frequently need a report number from your organization's assigning authority. Get it before finalizing the cover.

**This skill orients you; the authoritative sources are the DID, the contract, and DTIC's current submission guidance.** Where any of them conflicts with what is written here, they win.

## Reference

- `references/sf298-and-front-matter.md` — the SF 298 block by block, and front matter patterns.
