---
name: ieee-publishing
description: Write, format, validate, and prepare IEEE papers for submission and publication, with enforced consistency for tables, figures, captions, cross-references, and reference lists. Use this skill whenever the user mentions IEEE, IEEEtran, an IEEE conference paper, an IEEE journal or Transactions article, IEEE Access, IEEE Letters or Magazine, a camera-ready manuscript, PDF eXpress, IEEE Xplore, IEEE citation or reference style, or a two-column technical paper. Also use it when the user asks to fix figure or table formatting, caption placement, table numbering, float ordering, or cross-reference style in a technical paper; when they hand over a draft that must satisfy a conference or journal author kit; or when they ask about IEEE figure resolution, font embedding, page limits, or AI-disclosure requirements. Trigger even when the user only says "format this paper properly" or "make this submission-ready" in an engineering, defense, or applied-research context, since IEEE style is the default target there.
---

# IEEE Publishing

Produce IEEE manuscripts where formatting is enforced by a document class and verified by a script, not remembered by the model. The deliverable is never "a paper that looks IEEE." It is a paper that passes `validate_ieee.py` with zero errors.

## Core rule

**Never hand back a manuscript that has not passed validation.** Formatting drift in long papers is the failure mode this skill exists to prevent. Draft, build, validate, fix, repeat. If validation cannot run (missing dependency, no LaTeX), say so explicitly and list what went unchecked rather than implying the document is clean.

Do not hand-format. Do not set margins, font sizes, column widths, or caption styles by hand. IEEEtran already does it, and any manual override is a defect.

## Step 0. Establish the venue before generating anything

The class option, page limit, reference style, and review mode all depend on the venue. Ask if it is not already known:

1. Which venue? (conference name, Transactions title, IEEE Access, a Letters or Magazine title)
2. Which stage? (initial submission, revision, camera-ready)
3. Single-blind or double-blind review?
4. US Letter or A4?
5. Did the user draft the prose, or is this skill drafting it? (drives the AI disclosure requirement)

Read `references/variants.md` for the class options, page limits, and per-venue quirks. If the user names a specific conference, ask for its author kit URL or fetch it: page limits and over-length fees are set per event, not by IEEE globally, and guessing them wastes a submission.

If the user says "all venues" or is building a template rather than one paper, scaffold the conference variant as the default and note that `new_paper.py --venue` switches it.

## Step 1. Scaffold

```bash
python3 scripts/new_paper.py --venue conference --title "Paper Title" --out ./paper
```

Venues: `conference`, `journal`, `access`, `letters`, `magazine`, `peerreview` (double-blind anonymized).

This writes `main.tex`, `refs.bib`, `figures/`, and copies `IEEEtran.cls` and `IEEEtran.bst` locally so builds are reproducible without a TeX Live IEEE package.

For a Word deliverable, read `references/word-path.md` instead. Word is supported but LaTeX is the default because the class file removes an entire category of defects.

## Step 2. Draft

Write body content only. The class emits every piece of IEEE furniture automatically: the `Abstract` and `Index Terms` run-in heads with their em dashes, section numbering in Roman numerals, `Fig. N.` labels, `TABLE N` labels in Roman numerals, and the two-column layout. Typing any of these by hand is an error.

These rules apply on every job and are checked automatically. Full detail with edge cases is in `references/tables-figures.md`; read it before producing any paper containing more than two floats.

**Tables**
- `\caption` goes *above* the tabular content, inside the float, before `\begin{tabular}`.
- Write the caption in Title Case. IEEEtran renders it in small caps, so an all-caps source string renders as full-size capitals and looks wrong.
- No terminal period on a table caption.
- No vertical rules. Horizontal rules only, via `booktabs`.
- Use `table*` for a float spanning both columns, `table` for one column.
- Table notes go below the table keyed with superscript lowercase letters, via `threeparttable`.

**Figures**
- `\caption` goes *below* the graphic.
- Sentence case, first word capitalized, ends with a period.
- Do not begin a caption with "A", "An", or "The".
- Sub-figure parts are labeled `(a)`, `(b)` in lowercase roman letters, listed in the caption in order.
- For a reused figure, put the source reference number in brackets at the end of the caption.

**Cross-references in body text**
- Always `Fig.`, never `Figure`, including at the start of a sentence, and always singular even when citing `Fig. 1(a) and 1(b)`.
- `Table` is written out in full, with the Roman numeral: `Table II`.
- Never write "in Fig. 2 of [1]". Reproduce the figure or cite the source normally.
- Use a non-breaking tilde: `Fig.~\ref{fig:x}`, `Table~\ref{tab:y}`.

**Ordering**
- The first text mention of each figure and each table must occur in numerical order. This is the single most common defect in real drafts and the validator flags it precisely.

**References**
- BibTeX with `\bibliographystyle{IEEEtran}`. Never `plain`, `alpha`, or `apalike`: they alphabetize, and IEEE numbers by order of first citation.
- Citation numbers sit in square brackets on the line, before punctuation: `results improve [3].`
- Read `references/reference-style.md` for entry formats, author-count rules, DOI placement, and terminal punctuation.

**Prose**
- Apply the user's writing preferences (the `ai-fingerprint` skill if present) to body prose. IEEE style constrains structure and mechanics, not voice.
- Define every acronym at first use in the body. Avoid acronyms in the title.
- Equations are referenced as `(1)`, not `Eq. (1)` mid-sentence.

## Step 3. Build

```bash
bash scripts/build.sh ./paper/main.tex
```

Runs latexmk with local `TEXINPUTS`/`BSTINPUTS`, resolves BibTeX, and produces `main.pdf`. It reruns to settle cross-references and reports unresolved ones.

## Step 4. Validate (hard gate)

```bash
python3 scripts/validate_ieee.py ./paper/main.tex --venue conference --pdf ./paper/main.pdf --page-limit 6
```

Add `--ai-drafted` whenever this skill generated any body text, figures, or code. That switches the AI disclosure check from advisory to blocking.

Add `--json` for machine-readable output when looping.

Every `ERROR` must be fixed. Do not rationalize one away. `WARN` items need a judgment call: report them to the user with a recommendation rather than silently accepting or silently changing them.

Graphics are checked separately, since they usually arrive as loose files:

```bash
python3 scripts/check_graphics.py ./paper/figures/
```

This reports raster resolution against the 300 dpi color and grayscale floor and the 600 dpi monochrome floor, physical dimensions against the 7.16 x 8.8 inch cap, and font embedding in vector files.

Loop: validate, fix, rebuild, re-validate. Report the final clean run to the user.

## Step 5. Prepare for submission

Read `references/submission.md`. The short version:

- Camera-ready PDFs must clear IEEE PDF eXpress before upload. Failure to embed and subset fonts is the most common rejection cause, and `validate_ieee.py --pdf` checks it.
- Every submitting author needs an ORCID.
- AI-generated content (text, figures, images, code) must be disclosed in the acknowledgments, naming the system, the specific sections, and the level of involvement. Editing and grammar assistance falls outside the requirement, though disclosure is still recommended. Some conferences go further and prohibit LLM-generated body text outright, so check the event's policy rather than assuming the general IEEE rule applies.
- Do not paste a generic disclosure sentence. Track which sections were actually drafted and name them.

## Handling an existing draft

When the user hands over a `.docx` or `.tex` that already exists, do not rewrite it into a new file silently. Run the validator first, show the defect list, then fix in place. Users bring papers with real content and cosmetic problems. Preserve the content.

For `.docx` input, `validate_ieee.py` accepts it directly and checks caption placement, caption text style, `Figure` vs `Fig.`, mention ordering, and direct-formatting overrides of template styles.

## Reference files

Read these when the situation calls for them, not upfront:

| File | Read when |
|---|---|
| `references/variants.md` | Always, at Step 0. Class options, page limits, per-venue differences. |
| `references/tables-figures.md` | Any paper with floats. Full caption, numbering, sub-figure, and graphics rules. |
| `references/reference-style.md` | Building or fixing a reference list. Entry formats by source type. |
| `references/submission.md` | Camera-ready, PDF eXpress, disclosure, ORCID, checklists. |
| `references/word-path.md` | The deliverable must be `.docx`. |

## Failure modes to watch for

The model reformatting instead of fixing. When validation flags a caption, fix that caption. Do not regenerate the document.

Silent float renumbering. Reordering floats to satisfy the mention-order check changes every cross-reference. Fix the *text* order when the narrative allows it; renumber only when it does not.

Over-length papers. Cutting to a page limit by shrinking figures or margins is a compliance failure. Cut content.

Claiming a clean build without running the validator. If it did not run, say it did not run.
