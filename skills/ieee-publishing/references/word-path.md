# The Word path

Use this when the deliverable must be `.docx`: a co-author who will not use LaTeX, a venue that requires Word, or an internal review cycle that runs on tracked changes.

LaTeX remains the default because IEEEtran removes an entire category of defects. Word can be made compliant, but the discipline has to be supplied by the operator instead of by a class file.

## Contents
- The one rule
- Getting the template
- Producing content
- Editing an existing DOCX
- Validating
- Converting between paths
- Word-specific defects

## The one rule

**Apply named styles. Never apply direct formatting.**

Every heading, caption, body paragraph, and reference entry in the IEEE Word template has a named style. Selecting text and setting the font to 8 pt Times produces something that looks like a caption and behaves like nothing. It will not renumber, will not stay consistent across a document, and will drift the moment anyone edits near it.

`validate_ieee.py` reports runs carrying direct font overrides for exactly this reason.

If a needed style does not exist in the template, stop and say so. Do not approximate it.

## Getting the template

Download the current Word template from the IEEE Author Center or the conference's author kit. Do not reuse a template from an old paper: they get revised, and conference kits sometimes carry event-specific variants.

Choose the correct paper size. US Letter is standard for events in the United States and Canada, A4 for most international events.

Store the template in `assets/` as a `.dotx` once acquired, and note in the project which venue and revision it came from.

## Producing content

Drive `python-docx` against the template, opening it as the base document so its styles are inherited:

```python
import docx
doc = docx.Document("assets/ieee-conference-template.docx")

# Body text
p = doc.add_paragraph("Body text goes here.", style="Body Text")

# Table: caption FIRST, then the table
doc.add_paragraph("TABLE I", style="tablehead")
doc.add_paragraph("Detection Performance by Waveform Class", style="tablecaption")
t = doc.add_table(rows=4, cols=4, style="Table Grid")

# Figure: image FIRST, then the caption
p = doc.add_paragraph()
p.add_run().add_picture("figures/roc.png", width=Inches(3.5))
doc.add_paragraph("Fig. 1. Receiver operating characteristic across signal-to-noise ratio.",
                  style="figurecaption")
```

Style names differ between template revisions. Enumerate what is actually available before writing content:

```python
for s in doc.styles:
    print(s.type, repr(s.name))
```

Match the template's real style names. Do not assume the ones above exist.

## Ordering constraints Word does not enforce

Everything in `references/tables-figures.md` still applies, and none of it is automatic here:

- Table caption above, figure caption below.
- Tables numbered in uppercase Roman, figures in Arabic.
- Table captions take no terminal period; figure captions do.
- First mentions in numerical order.
- `Fig.` in text, always, always singular.

Word's built-in cross-reference fields (`Insert > Cross-reference`) do renumber automatically and are worth using. Typed-in numbers do not renumber, and a single inserted figure silently invalidates every number after it.

## Editing an existing DOCX

When the user hands over a draft, do not rebuild it. Validate first, show the defect list, then fix in place:

```bash
python3 scripts/validate_ieee.py draft.docx --venue conference
```

The DOCX checks cover caption placement relative to its table or image, caption punctuation and capitalization, `Figure` versus `Fig.`, the prohibited `Fig. X of [n]` construction, first-mention ordering for both figures and tables, and direct-formatting overrides.

Preserve the author's content. They came for compliance, not a rewrite.

## Converting between paths

**LaTeX to Word** is lossy and generally not worth it. Pandoc will produce a `.docx` but drops IEEE layout entirely, so the result needs full restyling against the template. Consider it only when a co-author needs to redline prose, and then treat the LaTeX as canonical and hand-merge the edits back.

**Word to LaTeX** works better. Pandoc extracts the prose and structure cleanly; rebuild floats and references by hand:

```bash
pandoc draft.docx -o body.tex --extract-media=figures
```

Then scaffold with `new_paper.py` and move the body content in. Rebuild every float using the patterns in `tables-figures.md` rather than accepting what Pandoc emits, since it produces `table` and `figure` environments that do not follow IEEE caption placement.

## Word-specific defects to check

| Defect | Symptom |
|---|---|
| Fonts not embedded in the exported PDF | The most common Xplore rejection from Word. Force embedding on export. |
| Linked rather than inserted graphics | Images vanish or degrade. Insert, never link. |
| Images pasted from PowerPoint or Excel | Resolution loss. Export from the source application. |
| Typed figure numbers | Do not renumber. Use cross-reference fields. |
| Direct formatting layered over styles | Drift across the document (checked) |
| Section breaks fighting the two-column layout | Floats jump columns unpredictably |
| Equation Editor versus the legacy object | Mixing them produces inconsistent math typography |
| Tracked changes left in the submitted file | Accept or reject all before export, and check the document inspector for residual metadata |

That last one matters doubly under double-blind review: tracked changes and document properties both carry author names.
