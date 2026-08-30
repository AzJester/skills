# Tables, figures, and captions

The rules in this file are drawn from the IEEE Editorial Style Manual for Authors and IEEE's graphics specification. Every rule marked (checked) is enforced by `validate_ieee.py`.

## Contents
- Why this is the hard part
- Table rules
- Table patterns
- Figure rules
- Figure patterns
- Sub-figures
- Numbering and mention order
- Cross-references in body text
- Graphics file requirements
- Float placement
- Reused figures and permissions

## Why this is the hard part

Tables and figures are where long manuscripts drift, because each float is authored in isolation and the rules differ between the two. Table captions go above, figure captions go below. Tables number in Roman, figures in Arabic. Table captions take no terminal period, figure captions do. Getting one float right does not make the next one right, which is why validation is mechanical rather than a matter of care.

## Table rules

- The caption goes **above** the table, centered, with the label TABLE in caps and the number in **uppercase Roman numerals**. (checked)
- Write the caption in **Title Case** in the source. IEEEtran renders table captions in small caps, so an all-caps source string prints as full-size capitals and looks wrong. (checked)
- The descriptive text is centered directly below the TABLE number line. IEEEtran does this; do not hand-place it.
- **No terminal period** on a table caption. Punctuation inside the caption is fine. (checked)
- Do not restate "TABLE II" inside the caption text. The class emits it. (checked)
- Do not open a caption with A, An, or The. (checked)
- When a caption wraps, it should read as an inverted pyramid, with the longest line first.
- **No vertical rules.** Horizontal rules only, via booktabs. (checked)
- Table notes go below the table, keyed with **superscript lowercase letters**, not numbers or symbols, so they never collide with reference numbers.
- Units belong in the column head in parentheses, not repeated in every cell.
- Use `table*` to span both columns, `table` for one.

## Table patterns

Single column with notes:

```latex
\begin{table}[t]
\caption{Detection Performance by Waveform Class}
\label{tab:detect}
\centering
\begin{threeparttable}
\begin{tabular}{lrrr}
\toprule
Waveform & $P_d$ (\%) & $P_{fa}$ (\%) & Latency (ms)\tnote{a} \\
\midrule
Pulsed        & 97.2 & 0.8 &  6.1 \\
Frequency hop & 91.4 & 1.3 &  9.8 \\
Continuous    & 88.0 & 2.1 & 11.4 \\
\bottomrule
\end{tabular}
\begin{tablenotes}[flushleft]\footnotesize
\item[a] Median over 1000 trials on the reference processor.
\end{tablenotes}
\end{threeparttable}
\end{table}
```

Spanning both columns, placed at the top of a page:

```latex
\begin{table*}[t]
\caption{Comparison Against Published Baselines}
\label{tab:baselines}
\centering
\begin{tabular}{llrrrr}
\toprule
Method & Source & Year & Accuracy (\%) & Params (M) & Notes \\
\midrule
...
\bottomrule
\end{tabular}
\end{table*}
```

Wide tables that still overflow: reduce content, rotate with `\begin{sidewaystable*}` (rotcaption), or split into two tables. Do not shrink the font below `\footnotesize` or scale with `\resizebox`, which produces inconsistent type sizes across the paper.

## Figure rules

- The caption goes **below** the figure. (checked)
- The class emits `Fig. N.` followed by a period and an em space. Supply only the caption text. (checked)
- Sentence case, **first word capitalized**, **ends with a period**. (checked)
- Do not open with A, An, or The. (checked)
- Do not restate "Fig. 3" inside the caption text. (checked)
- Figure footnotes are folded into the caption rather than set separately.
- Axis labels need words, not bare symbols, with units in parentheses.
- Check every color figure in grayscale. If two series become indistinguishable, the figure fails for print and for colorblind readers. Use marker shape or line style in addition to color.
- Use `figure*` to span both columns.

## Figure patterns

```latex
\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{figures/roc}
\caption{Receiver operating characteristic across signal-to-noise ratio.}
\label{fig:roc}
\end{figure}
```

Spanning both columns:

```latex
\begin{figure*}[t]
\centering
\includegraphics[width=\textwidth]{figures/architecture}
\caption{End-to-end processing chain from receiver front end to classifier output.}
\label{fig:arch}
\end{figure*}
```

## Sub-figures

Parts are labeled `(a)`, `(b)` in lowercase roman letters in parentheses, and the caption lists them **in order**. (checked)

```latex
\begin{figure}[t]
\centering
\begin{subfigure}{0.48\columnwidth}
  \includegraphics[width=\linewidth]{figures/before}
  \caption{}\label{fig:pair-a}
\end{subfigure}
\hfill
\begin{subfigure}{0.48\columnwidth}
  \includegraphics[width=\linewidth]{figures/after}
  \caption{}\label{fig:pair-b}
\end{subfigure}
\caption{Spectrogram before and after suppression. (a) Raw capture. (b) After adaptive
suppression.}
\label{fig:pair}
\end{figure}
```

Two acceptable caption styles exist. Either lead with a descriptive sentence then list the parts, as above, or open directly with the parts: `Fig. 4. (a) Electrode transmission. (b) Interelectrode crosstalk.` Pick one style and hold it across the whole paper. When citing parts in text, `Fig.` stays singular: "Fig. 4(a) and 4(b)".

## Numbering and mention order

The first text mention of every figure and every table must occur in **numerical order**. (checked)

This is the most common defect in real drafts, because sections get reordered during revision while float definitions stay put. The validator reports which label is out of position and against which.

Two ways to fix it, and the choice matters:

1. **Reorder the narrative.** Preferred when the text can carry the change. Nothing else moves.
2. **Swap the float definitions.** Renumbers the floats, which changes every cross-reference in the paper and in any response-to-reviewers document. Do this only when the narrative order is fixed by the argument.

Never renumber silently. Tell the user which approach was taken.

Every float must be cited at least once. An uncited figure is a defect, not a stylistic choice. (checked)

## Cross-references in body text

| Correct | Wrong |
|---|---|
| `Fig.~\ref{fig:roc}` | `Figure~\ref{fig:roc}` (checked) |
| `Fig. 4(a) and 4(b)` | `Figs. 4(a) and 4(b)` (checked) |
| `Table~\ref{tab:detect}` | `Tab.~\ref{tab:detect}` (checked) |
| `Fig.` at the start of a sentence | `Figure` at the start of a sentence (checked) |
| Reproduce the figure, cite the source in its caption | `Fig. 2 of [1]` (checked) |
| `(3)` for an equation mid-sentence | `Eq. (3)` mid-sentence |

Always use a non-breaking tilde before `\ref` so the number never wraps away from its label. (checked as a warning)

## Graphics file requirements

| Content | Minimum resolution |
|---|---|
| Monochrome (bitonal line art) | 600 dpi |
| Grayscale | 300 dpi |
| Color | 300 dpi |

- Vector formats (PDF, EPS) are preferred and are resolution-independent, but **every font must be embedded**, or convert text to outlines. (checked)
- Accepted formats include PDF, EPS, PS, TIFF, and PNG. SVG is not accepted for submission. (checked)
- Maximum physical size is 7.16 x 8.8 inches for separately submitted figure files.
- Text inside graphics should not fall below about 6 pt at final size. 4 pt is the hard floor for conference graphics.
- Flatten all layers and remove alpha channels. (checked)
- Insert graphics into the manuscript rather than linking to them.
- Upsampling does not create resolution. A 150 dpi image resaved at 600 dpi is still a 150 dpi image. Re-export from the source. (checked)

Run `check_graphics.py` on the figures directory before every build.

## Float placement

Use `[t]` or `[b]`. IEEE typesetting places floats at the top or bottom of a column, not mid-column. `[h]` and `[H]` fight the class and produce placement that will be reset in production anyway.

For a two-column paper, `figure*` and `table*` can only float to the top of a page, never the bottom, and never the page they are defined on. Define spanning floats one section earlier than where they should appear.

Overfull hbox warnings mean content is spilling past the column edge. Fix the content. Never fix the column.

## Reused figures and permissions

When a figure is taken from another source, put the source reference number in brackets at the end of the caption:

```latex
\caption{Hierarchical assessment of sustainability [3].}
```

Reusing a published figure requires permission from the copyright holder, and the caption may need specific wording that the holder or the Creative Commons license dictates. Reproducing your own previously published figure also requires attribution. Flag this to the user rather than deciding it for them.

If a figure is AI-generated, the caption carries a note that the graphic was created using AI generation, and the acknowledgments carry the full disclosure. See `submission.md`.
