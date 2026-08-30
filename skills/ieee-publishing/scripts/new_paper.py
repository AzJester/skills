#!/usr/bin/env python3
"""
new_paper.py - Scaffold an IEEE manuscript project with the correct class options.

Copies IEEEtran.cls and IEEEtran.bst next to the source so builds are reproducible
on machines whose TeX distribution lacks the IEEE package.

Usage:
  new_paper.py --venue conference --title "Adaptive EW Threat Classification" --out ./paper
  new_paper.py --venue journal --title "..." --author "S. Turner" --out ./paper
  new_paper.py --venue peerreview --title "..." --out ./paper     # double-blind
"""

import argparse
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(os.path.dirname(HERE), "assets")

CLASS_OPTIONS = {
    "conference": "conference",
    "journal": "journal",
    "access": "journal",
    "letters": "journal",
    "magazine": "journal",
    "peerreview": "journal,peerreview",
}

NOTES = {
    "conference": "Confirm the page limit and over-length fee in the event's author kit.",
    "journal": "Transactions submissions have no fixed page limit but do have overlength charges.",
    "access": "IEEE Access uses its own template for final files; use this for drafting, then port.",
    "letters": "Letters are strictly length-limited. Confirm the limit before drafting.",
    "magazine": "Magazine articles favor prose over equations. Check the section editor's guidance.",
    "peerreview": "Double-blind: strip author names, affiliations, funding, and self-identifying citations.",
}


TEMPLATE = r"""%% IEEE manuscript scaffolded by the ieee-publishing skill.
%% Venue: {venue}
%% {note}
%%
%% Build:    bash build.sh main.tex
%% Validate: python3 validate_ieee.py main.tex --venue {venue}
%%
%% Do not add \usepackage{{geometry}} or change margins, column widths, or line
%% spacing. IEEEtran sets the required layout and any override is a compliance defect.

\documentclass[{opts}]{{IEEEtran}}

\usepackage{{graphicx}}      % figures
\usepackage{{booktabs}}      % horizontal rules only; IEEE tables use no vertical rules
\usepackage{{threeparttable}}% table notes keyed with superscript lowercase letters
\usepackage{{amsmath,amssymb}}
\usepackage{{subcaption}}    % sub-figure parts (a), (b)
\usepackage{{url}}
\usepackage[hidelinks]{{hyperref}}
\usepackage{{cite}}          % compresses [1], [2], [3] into [1]-[3]

\begin{{document}}

\title{{{title}}}

{authorblock}

\maketitle

\begin{{abstract}}
Replace with the abstract. Keep it self-contained: no citations, no undefined
acronyms, no references to figures or tables. Most venues expect 150 to 250 words.
\end{{abstract}}

\begin{{IEEEkeywords}}
first term, second term, third term, fourth term
\end{{IEEEkeywords}}

\section{{Introduction}}
Body text. Cite sources in square brackets before the punctuation \cite{{example2024}}.
Reference figures as Fig.~\ref{{fig:example}} and tables as Table~\ref{{tab:example}},
always in numerical order of first mention.

\section{{Method}}

%% ---------------------------------------------------------------------------
%% TABLE PATTERN
%% Caption goes ABOVE the tabular. Title Case in the source: IEEEtran renders it
%% in small caps, so an ALL-CAPS source string prints as full-size capitals.
%% No terminal period. Use table* to span both columns.
%% ---------------------------------------------------------------------------
\begin{{table}}[t]
\caption{{Comparison of Candidate Approaches}}
\label{{tab:example}}
\centering
\begin{{threeparttable}}
\begin{{tabular}}{{lrr}}
\toprule
Approach & Accuracy (\%) & Latency (ms)\tnote{{a}} \\
\midrule
Baseline  & 82.4 & 14.1 \\
Proposed  & 91.7 &  9.6 \\
\bottomrule
\end{{tabular}}
\begin{{tablenotes}}[flushleft]\footnotesize
\item[a] Measured end to end over 1000 trials on the reference hardware.
\end{{tablenotes}}
\end{{threeparttable}}
\end{{table}}

\section{{Results}}

%% ---------------------------------------------------------------------------
%% FIGURE PATTERN
%% Caption goes BELOW the graphic. Sentence case, first word capitalized, ends
%% with a period. Do not open with A, An, or The. Do not restate "Fig. N":
%% IEEEtran emits the label itself. Use figure* to span both columns.
%% ---------------------------------------------------------------------------
\begin{{figure}}[t]
\centering
\includegraphics[width=\columnwidth]{{figures/example}}
\caption{{Detection performance across signal-to-noise ratio.}}
\label{{fig:example}}
\end{{figure}}

\section{{Conclusion}}

\section*{{Acknowledgment}}
%% IEEE requires disclosure of AI-generated content (text, figures, images, code)
%% in this section: name the system, name the specific sections it produced, and
%% describe the level of involvement. Delete this block only if no AI content is
%% present. Some conferences prohibit AI-generated body text outright; check the
%% event policy before relying on disclosure alone.

\bibliographystyle{{IEEEtran}}
\bibliography{{refs}}

\end{{document}}
"""

NAMED_AUTHOR = r"""\author{{\IEEEauthorblockN{{{author}}}
\IEEEauthorblockA{{\textit{{Department}} \\
\textit{{Organization}}\\
City, Country \\
email@example.org}}
}}"""

ANON_AUTHOR = r"""%% Double-blind: author block intentionally anonymized.
\author{\IEEEauthorblockN{Anonymous Authors}
\IEEEauthorblockA{Affiliation withheld for review}
}"""

BIB = r"""@article{example2024,
  author  = {A. B. Author and C. D. Author},
  title   = {Title of the referenced work},
  journal = {IEEE Trans. Signal Process.},
  volume  = {72},
  number  = {4},
  pages   = {1123--1135},
  month   = apr,
  year    = {2024},
  doi     = {10.1109/TSP.2024.0000000}
}

%% IEEE reference rules enforced by validate_ieee.py:
%%   - page ranges use an en dash: 1123--1135, never a hyphen
%%   - list up to six authors, then the primary author followed by et al.
%%   - include a DOI whenever one exists
%%   - entries end with a period unless they end with a URL
"""

BUILD_STUB = """#!/usr/bin/env bash
# Convenience wrapper. The canonical build script lives in the skill's scripts/ dir.
exec bash "$(dirname "$0")/build.sh" "$(dirname "$0")/main.tex"
"""


def main():
    ap = argparse.ArgumentParser(description="Scaffold an IEEE manuscript project.")
    ap.add_argument("--venue", default="conference", choices=sorted(CLASS_OPTIONS.keys()))
    ap.add_argument("--title", default="Paper Title")
    ap.add_argument("--author", default="First A. Author")
    ap.add_argument("--out", default="./paper")
    args = ap.parse_args()

    out = os.path.abspath(args.out)
    os.makedirs(os.path.join(out, "figures"), exist_ok=True)

    authorblock = ANON_AUTHOR if args.venue == "peerreview" else NAMED_AUTHOR.format(author=args.author)

    main_tex = TEMPLATE.format(
        venue=args.venue,
        note=NOTES[args.venue],
        opts=CLASS_OPTIONS[args.venue],
        title=args.title,
        authorblock=authorblock,
    )

    with open(os.path.join(out, "main.tex"), "w", encoding="utf-8") as fh:
        fh.write(main_tex)
    with open(os.path.join(out, "refs.bib"), "w", encoding="utf-8") as fh:
        fh.write(BIB)

    copied = []
    for asset in ("IEEEtran.cls", "IEEEtran.bst"):
        src = os.path.join(ASSETS, asset)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(out, asset))
            copied.append(asset)

    for script in ("build.sh", "validate_ieee.py", "check_graphics.py"):
        src = os.path.join(HERE, script)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(out, script))

    print(f"Scaffolded {args.venue} manuscript at {out}")
    print(f"  main.tex, refs.bib, figures/, {', '.join(copied)}")
    print(f"  note: {NOTES[args.venue]}")
    print()
    print("Next:")
    print(f"  bash {os.path.join(out, 'build.sh')} {os.path.join(out, 'main.tex')}")
    print(f"  python3 {os.path.join(out, 'validate_ieee.py')} {os.path.join(out, 'main.tex')} "
          f"--venue {args.venue} --pdf {os.path.join(out, 'main.pdf')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
