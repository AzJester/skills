---
name: latex-authoring
description: Author and debug documents in LaTeX. Use when writing a paper or report in LaTeX, working with a publisher's document class, managing bibliographies with BibTeX or BibLaTeX, placing figures and tables, building a document that will not compile, or diagnosing why output does not match the template. Multiplies the format skills rather than replacing any of them.
---

# LaTeX authoring

LaTeX rewards understanding one thing: **you describe structure, and the class decides appearance.** Most fights with LaTeX are attempts to control appearance directly, against a class that has already decided.

For a publisher's template, that is not a limitation. The class encodes the venue's requirements, and overriding it produces a document that fails the format check.

## The rule for publisher templates

**Write into the class. Do not fight it.**

- Do not redefine margins, spacing, or font sizes to fit more in. It is detectable, and it is a standard rejection reason.
- Do not load packages that override the class's typography — `geometry`, `setspace`, `titlesec` and friends will break `acmart` and IEEE's classes in ways the venue checks for.
- If the paper does not fit, cut content. Every experienced reviewer recognises a squeezed paper.
- Load the class options the venue specifies, not the ones you prefer.

Read the class documentation before the first compile. `acmart`'s in particular is thorough, and most of the errors people hit are documented behaviours.

## Structure

```latex
\documentclass[options]{class}     % venue-specified

\usepackage{...}                   % as few as possible

\begin{document}
\title{...}
\author{...}
\maketitle
\begin{abstract} ... \end{abstract}

\section{Introduction}
\label{sec:intro}

...

\bibliographystyle{...}
\bibliography{refs}
\end{document}
```

**Label everything you reference, and reference by label.** `\ref{}` and `\cite{}` rather than typed numbers. Hard-coded numbers are wrong the moment a section moves, and they will move.

Use a consistent label convention — `sec:`, `fig:`, `tab:`, `eq:` — so a label's type is visible at the point of use.

## Bibliography: BibTeX or BibLaTeX

**BibTeX** is older, universally supported, and what most publisher templates expect. Style is set by `\bibliographystyle{}`.

**BibLaTeX** with `biber` is more capable — better Unicode, more flexible styles, richer entry types. Use it when you control the document; use BibTeX when the venue's class expects it. Many publisher classes assume BibTeX, and substituting BibLaTeX quietly produces the wrong reference format.

**Keeping the `.bib` file clean** matters more than the choice:

- **Fix the capitalisation problem.** BibTeX lowercases title words per the style. Protect what must stay capitalised with braces: `title = {A Study of {Bayesian} Methods for {DoD} Applications}`. Unprotected proper nouns are the most common reference defect, and it appears in the output rather than in an error.
- Include DOIs.
- Use consistent, meaningful keys — `lastname2024topic`.
- Take entries from the publisher, not from an aggregator that mangles fields. Import once, check once, then trust it.
- Watch for duplicates from different sources with different keys.

## Figures and tables

**Placement is negotiated, not commanded.** `[htbp]` gives LaTeX options; `[h!]` forces a placement and produces bad pages. Let floats float; readers follow references, not adjacency.

```latex
\begin{figure}[tb]
  \centering
  \includegraphics[width=\columnwidth]{filename}
  \caption{Caption below the figure.}
  \label{fig:name}
\end{figure}
```

- **Size relative to the text**, using `\columnwidth` or `\textwidth`, not absolute units. Absolute sizes break when the class changes.
- **Vector formats** — PDF or EPS — for line art. Raster only for photographs, at sufficient resolution.
- **`figure*` and `table*`** span both columns in a two-column class, and place at the top or bottom of a page.
- **`\label` goes after `\caption`.** Before it, the reference resolves to the wrong number, silently.
- Caption placement is a venue rule: IEEE puts figure captions below and table captions above; APA puts both above. The class usually handles it — check the output.

## Errors worth recognising

| Message | Usually means |
| --- | --- |
| `Undefined control sequence` | A missing package, or a typo in a command name |
| `Missing $ inserted` | A math character outside math mode — often an underscore in text |
| `Undefined references` | Compile again; references need two passes |
| `LaTeX Warning: Citation undefined` | Run BibTeX/biber, then LaTeX twice more |
| `Overfull \hbox` | Content wider than the column — usually a long URL, a wide table, or unbreakable code |
| `Float(s) lost` | A float inside a minipage, parbox, footnote or marginpar was discarded — move it into the main text flow |
| `Too many unprocessed floats` | Too many unplaced floats; place some earlier, relax the placement, or `\clearpage` |
| Output does not match the template | A package is overriding the class. Remove packages until it does |

**The compile sequence** for a document with citations: LaTeX, then BibTeX or biber, then LaTeX twice. Skipping it leaves undefined references, and the first run's warnings mislead. Most editors automate this; when debugging, do it by hand.

That last row in the table is the one to internalise. When output disagrees with the template, suspect your own packages before suspecting the class.

## Practical setup

- **Version control the source.** `.tex` and `.bib` are text; diffs are meaningful. Add build artifacts to `.gitignore`.
- **One sentence per line.** Diffs become readable, and rewrapping stops producing spurious changes. LaTeX ignores single line breaks.
- **Comment out rather than delete** while drafting; recover with `%`.
- **Compile often.** An error introduced twenty edits ago is far harder to locate than one introduced now.
- **Overleaf** is where most publisher templates are available directly, and it removes toolchain problems from collaboration. For controlled work, check whether the content may go there at all — see `export-control-and-markings`; pasting controlled technical data into a hosted service is a transmission.

## Where this connects

`ieee-publishing`, `acm-paper`, `apa-7`, `chicago-turabian`, `dod-technical-report` and `nasa-sti` decide what the document must look like. This is how to build it without fighting the class that already knows.
