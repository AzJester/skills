---
name: ieee-paper
description: Write or format a paper to IEEE requirements. Use when drafting a conference paper or journal article for IEEE, converting a manuscript into IEEE format, formatting figures, tables, equations or references to IEEE style, checking a paper against IEEE submission requirements, or answering how IEEE wants something presented. Covers both the conference proceedings template and the Transactions journal template, which differ.
---

# IEEE paper

Two things decide everything else, and getting either wrong means reformatting the whole paper late.

## First: which template

IEEE conference and journal formats are **not the same**, and secondary summaries of "IEEE format" routinely conflate them. Establish this before writing a line.

| | Conference proceedings | Journal / Transactions |
| --- | --- | --- |
| Purpose | Papers in a conference proceedings | Articles in an IEEE journal or Transactions |
| Title | Larger, centred | Set by the journal template |
| Figure caption size | Smaller (typically 8 pt) | Larger (typically 10 pt) |
| Submission form | Usually camera-ready, formatted by the author | Often submitted in a review format, typeset by IEEE |

If the target is a journal, the journal's own author instructions override the generic template. Ask which venue before formatting anything.

## Second: the official template is the authority

**Download the current template from IEEE for the specific venue and follow it. This skill is not a substitute for it.**

The reasons are practical. IEEE revises templates; venues add their own constraints (page limits, blind review, extra sections); and journal-specific instructions supersede the generic ones. A paper formatted from a remembered specification and a paper formatted from the venue's current template are not the same paper, and the difference shows up at submission.

Sources, in order of authority:
1. The venue's own author kit or call for papers.
2. The IEEE template for that venue — Word or LaTeX, from IEEE's author center. IEEE also publishes templates through Overleaf for LaTeX authors.
3. The IEEE Editorial Style Manual, for questions the template does not answer.

Use `references/format-spec.md` for the conventional values, and **verify each against the downloaded template** rather than trusting the table. Where this skill and the template disagree, the template wins without argument.

## Structure

Standard order. Not every paper needs every part.

1. **Title** — specific, no unexpanded abbreviations, no formulae. Avoid "Novel", "Improved", "A Study of".
2. **Authors and affiliations**
3. **Abstract** — 150–250 words typical. One paragraph, no citations, no abbreviations that are not expanded, no equations, no figure references. States what was done and what was found, not what will be discussed.
4. **Index Terms / Keywords** — alphabetical, from the IEEE taxonomy where the venue requires it.
5. **Introduction** — problem, why it matters, what exists, the gap, the contribution. State contributions explicitly; reviewers look for them.
6. **Body** — related work, method, experimental setup, results, discussion. Numbering is described below.
7. **Conclusion** — what was shown, its limits, and what follows. Not a restated abstract. Conclusions are not numbered in some templates; check.
8. **Acknowledgment** — unnumbered. IEEE spells it without the middle "e".
9. **References**
10. **Appendices**, if any, before the references or after, per the template.
11. **Author biographies** — journals only, where required.

## Section numbering

Roman numerals, and the hierarchy is fixed:

```
I.  INTRODUCTION                 Roman numeral, centred, small caps
  A. Subsection Heading          Letter, italic, flush left, title case
    1) Sub-subsection:           Number with parenthesis, italic, indented, run into the text
```

**Acknowledgment and References are not numbered.** Neither, in most templates, is the Conclusion — check the one you have.

Do not skip a level, and do not create a subsection that has no sibling. A section with a single `A.` and nothing else should be prose.

## Figures

**Caption goes below the figure.** This is the single most common formatting error, because tables are the opposite.

- Labelled `Fig. 1.`, `Fig. 2.` — abbreviated, with a period after the number.
- Numbered consecutively in order of first mention in the text.
- Every figure is referred to in the text before it appears. A figure nobody references does not belong in the paper.
- **In text, abbreviate to "Fig. 1"** — except when starting a sentence, where it is "Figure 1 shows…".
- Axis labels carry the quantity **and its units**, written out rather than abbreviated where space allows: "Magnetization (A/m)", not "M, A/m".
- Text inside a figure must be legible at print size. This is the second most common problem, and it is why screenshots of plots usually fail.
- Line art as vector where possible; photographs at sufficient resolution. IEEE publishes minimum DPI requirements — check the venue's.
- A figure spanning both columns is placed at the top or bottom of a page, not mid-column.
- Colour: verify whether the venue prints in colour, and whether colour costs. A figure that must survive greyscale needs distinguishable line styles or markers, not just hues.

## Tables

**Caption goes above the table.** The opposite of figures.

- Labelled `TABLE I`, `TABLE II` — **Roman numerals**, unlike figures.
- The caption line is typically small caps or upper case, centred above the table.
- Numbered consecutively in order of first mention.
- Referred to in the text as "Table I" — **not abbreviated**, unlike figures.
- Rules: horizontal rules above and below the header row and at the foot of the table. **Vertical rules are avoided** in IEEE style, as are most interior horizontal rules.
- Units go in the column heading, not repeated in every cell.
- Table notes go beneath the table, keyed with superscript letters rather than numbers, so they are not confused with citations.

Figures and tables are numbered in **separate sequences**. Fig. 1 and Table I can both exist.

## Equations

- Numbered consecutively, in parentheses, **flush right**: (1), (2).
- Referred to as "(1)" — not "Eq. (1)" or "Equation (1)", except at the start of a sentence.
- Punctuated as part of the sentence containing them. An equation ending a sentence takes a full stop.
- Symbols defined at first use, and italicised in text as they are in the equation.
- Use the equation editor consistently; do not mix an editor and inline text for the same symbol.

## References

IEEE uses **numbered citations in square brackets, in order of first appearance.** Full patterns and worked examples for every source type are in `references/citation-style.md`.

Rules that catch people:

- Cited as "[1]" in running text, not "Ref. [1]" or "reference [1]" — except at the start of a sentence: "Reference [1] shows…".
- The bracket is part of the sentence, placed before punctuation: "…as shown in [1]."
- Multiple: "[1], [3], [5]" for a list; "[1]–[5]" for a range.
- Numbered by **first appearance**, not alphabetically.
- Every reference is cited in the text, and every citation appears in the list.
- Author names as initials then surname: "J. K. Author".
- Article titles in quotation marks and sentence case; journal and conference names in italics and title case, abbreviated per IEEE's standard abbreviations.

## Language and style

- **Past tense for what you did and found**; present tense for established facts and for what the paper does ("Section III presents…").
- IEEE accepts first person; "we" is standard and clearer than sustained passive.
- Expand every abbreviation at first use in the body — and again at first use in the abstract, which is read independently. Do not expand in the title.
- SI units. Where a non-SI unit is unavoidable, give the SI equivalent in parentheses.
- A decimal point takes a leading zero: 0.25, not .25.
- Cross-references are capitalised: "Section III", "Fig. 4", "Table II".
- Avoid "etc.", contractions, and stacked nouns three deep.

## Before submitting

- Page limit met **including** references, if the venue counts them.
- Anonymised if the venue is double-blind: no author names, no self-citations in first person, no acknowledgment, no identifying repository links.
- Every figure and table referenced in the text, in order.
- Every reference cited; every citation listed.
- Abbreviations expanded at first use in both abstract and body.
- Figures legible at print size and in greyscale if the venue prints greyscale.
- Run the venue's validation tool if one exists — IEEE PDF eXpress or equivalent is commonly mandatory for conferences, and it rejects on embedded fonts and page size more often than on anything else.

## Reference

- `references/format-spec.md` — conventional layout and type sizes, to be checked against the venue's template.
- `references/citation-style.md` — reference patterns and worked examples by source type.
