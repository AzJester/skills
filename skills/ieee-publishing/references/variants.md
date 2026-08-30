# IEEE venue variants

Read this at Step 0, before generating anything. The class option, page limit, reference handling, and anonymization all follow from the venue.

## Contents
- Selecting the variant
- Class options by venue
- Page limits and overlength
- Double-blind submissions
- Stage differences (submission, revision, camera-ready)
- Things that vary by event and must be confirmed

## Selecting the variant

Ask which venue. Do not infer it from the topic. A defense-sensing paper could go to a conference, a Transactions, or IEEE Access, and the three produce different files.

| User says | Variant | `--venue` |
|---|---|---|
| A named conference, symposium, workshop, "proceedings" | Conference | `conference` |
| "IEEE Transactions on ...", "journal paper", "TPAMI", "TAES" | Journal | `journal` |
| "IEEE Access" | Access | `access` |
| "Letters", "IEEE Control Systems Letters", "Sensors Letters" | Letters | `letters` |
| "IEEE Spectrum", "Computer", "Security & Privacy", "AESS Magazine" | Magazine | `magazine` |
| "double-blind", "anonymized", "blind review" | Peer review | `peerreview` |

## Class options by venue

All variants use `IEEEtran.cls` v1.8b. One class file covers every mode through options.

```latex
\documentclass[conference]{IEEEtran}          % conference proceedings
\documentclass[journal]{IEEEtran}             % Transactions, Journals, Letters
\documentclass[journal,peerreview]{IEEEtran}  % double-blind, cover page, single column
\documentclass[technote]{IEEEtran}            % brief technical notes
\documentclass[conference,a4paper]{IEEEtran}  % A4 rather than US Letter
```

Add `draftcls` while writing to get double spacing and visible margins; remove it before building anything you show the user or submit.

`a4paper` matters. US Letter is standard for conferences held in the United States and Canada; A4 is standard for most international events. The call for papers states which. Getting it wrong is a rejection at upload.

## Page limits and overlength

Page limits are set per event and per journal, not by IEEE globally. Never assume.

| Variant | Typical | Note |
|---|---|---|
| Conference | 6 to 8 pages | Many events allow 1 to 2 extra pages for a fee. Confirm in the author kit. |
| Transactions | No hard limit | Overlength page charges apply above a threshold that differs by title. |
| Letters | 4 to 6 pages | Strictly enforced. Cut content early. |
| Access | No hard limit | Article processing charge is flat; length affects review expectations, not price. |
| Magazine | Set by the section editor | Usually far shorter and far less equation-dense. |

When the user names a specific conference, ask for the author kit URL or fetch it. Page limit, over-length fee, anonymization policy, and the AI policy are all set at the event level.

Cutting to a limit means cutting content. Shrinking figures below legibility, reducing margins, changing line spacing, or dropping font size are compliance failures, and `validate_ieee.py` flags the geometry and spacing overrides directly.

## Double-blind submissions

With `peerreview`, IEEEtran produces a single-column double-spaced manuscript with a separate cover page. Beyond the class option:

- Remove author names, affiliations, emails, and ORCID from the author block.
- Remove acknowledgments entirely, including funding. Restore at camera-ready.
- Convert self-citations to third person: "the approach in [7]" rather than "our earlier approach [7]".
- Strip identifying metadata from the PDF and from figure files (Illustrator and Visio both embed author names).
- Remove contract numbers, program names, and facility names that identify the organization. This matters on defense work, where a program name is often more identifying than the author list.

## Stage differences

**Initial submission.** Content correctness dominates. Page limits and font embedding still apply, but PDF eXpress is not usually required yet.

**Revision.** Most venues want a response-to-reviewers document alongside the manuscript. Some want changes highlighted; check the decision letter. Keep the reference numbering consistent with the revised text, since inserting one citation renumbers everything after it.

**Camera-ready.** This is where compliance gets enforced. Run PDF eXpress, add the copyright notice if the event requires one, confirm the page count, and confirm every font is embedded and subset. See `submission.md`.

## Things that must be confirmed, never assumed

- Page limit and over-length fee
- US Letter versus A4
- Whether review is single-blind or double-blind
- Whether the event requires a copyright notice line on page 1
- The event's own AI policy, which may be stricter than the general IEEE rule
- Whether figures are submitted separately (journals often) or embedded only (conferences usually)
