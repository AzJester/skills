#!/usr/bin/env python3
"""
validate_ieee.py - Enforce IEEE manuscript formatting rules.

Accepts a LaTeX source (.tex) or a Word manuscript (.docx), optionally plus a
built PDF, and reports every violation of IEEE Editorial Style Manual and
Xplore submission rules that can be checked mechanically.

Exit code 0 when there are no ERRORs, 1 otherwise. WARNs never fail the build;
they need a human judgment call.

Usage:
  validate_ieee.py main.tex --venue conference --pdf main.pdf --page-limit 6
  validate_ieee.py draft.docx --venue journal
  validate_ieee.py main.tex --ai-drafted --json
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys

ERROR = "ERROR"
WARN = "WARN"
INFO = "INFO"

# Venue -> allowed \documentclass options and a default page limit.
# Page limits are per-event for conferences; always confirm against the author kit.
VENUES = {
    "conference": {"options": ["conference"], "pages": 6},
    "journal": {"options": ["journal"], "pages": None},
    "access": {"options": ["journal"], "pages": None},
    "letters": {"options": ["journal"], "pages": 4},
    "magazine": {"options": ["journal"], "pages": None},
    "peerreview": {"options": ["peerreview"], "pages": None},
}


class Findings:
    def __init__(self):
        self.items = []

    def add(self, severity, check, message, location=None):
        self.items.append(
            {
                "severity": severity,
                "check": check,
                "message": message,
                "location": location,
            }
        )

    def error(self, *a, **k):
        self.add(ERROR, *a, **k)

    def warn(self, *a, **k):
        self.add(WARN, *a, **k)

    def info(self, *a, **k):
        self.add(INFO, *a, **k)

    @property
    def n_errors(self):
        return sum(1 for i in self.items if i["severity"] == ERROR)

    @property
    def n_warns(self):
        return sum(1 for i in self.items if i["severity"] == WARN)


# --------------------------------------------------------------------------
# LaTeX helpers
# --------------------------------------------------------------------------

def strip_comments(text):
    """Remove LaTeX comments but keep line count stable."""
    out = []
    for line in text.split("\n"):
        result = []
        i = 0
        while i < len(line):
            ch = line[i]
            if ch == "\\" and i + 1 < len(line):
                result.append(line[i : i + 2])
                i += 2
                continue
            if ch == "%":
                break
            result.append(ch)
            i += 1
        out.append("".join(result))
    return "\n".join(out)


def extract_braced(text, open_idx):
    """Given index of an opening brace, return (content, index_after_close)."""
    if open_idx >= len(text) or text[open_idx] != "{":
        return None, open_idx
    depth = 0
    i = open_idx
    while i < len(text):
        ch = text[i]
        if ch == "\\":
            i += 2
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return text[open_idx + 1 : i], i + 1
        i += 1
    return None, len(text)


def find_command_arg(text, command, search_from=0):
    """Find \\command{...} and return (content, start, end) or None."""
    pattern = re.compile(r"\\" + command + r"\s*(\[[^\]]*\])?\s*\{")
    m = pattern.search(text, search_from)
    if not m:
        return None
    content, end = extract_braced(text, m.end() - 1)
    if content is None:
        return None
    return content, m.start(), end


def line_of(text, index):
    return text.count("\n", 0, index) + 1


def find_environments(text, names):
    """Return list of dicts for each environment block, in source order."""
    envs = []
    pattern = re.compile(r"\\begin\{(" + "|".join(re.escape(n) for n in names) + r")\}")
    for m in pattern.finditer(text):
        name = m.group(1)
        end_pat = re.compile(r"\\end\{" + re.escape(name) + r"\}")
        depth = 1
        pos = m.end()
        begin_again = re.compile(r"\\begin\{" + re.escape(name) + r"\}")
        end_idx = None
        while pos < len(text):
            nb = begin_again.search(text, pos)
            ne = end_pat.search(text, pos)
            if ne is None:
                break
            if nb and nb.start() < ne.start():
                depth += 1
                pos = nb.end()
                continue
            depth -= 1
            pos = ne.end()
            if depth == 0:
                end_idx = ne.start()
                break
        if end_idx is None:
            end_idx = len(text)
            pos = len(text)
        envs.append(
            {
                "name": name,
                "kind": "table" if name.startswith("table") else "figure",
                "spanning": name.endswith("*"),
                "start": m.start(),
                "body_start": m.end(),
                "body_end": end_idx,
                "end": pos,
                "body": text[m.end() : end_idx],
                "line": line_of(text, m.start()),
            }
        )
    return envs


def normalize_caption(raw):
    """Strip LaTeX markup from a caption to get readable text."""
    s = raw
    s = re.sub(r"\\(?:label|cite|ref|cref|footnote)\s*\{[^}]*\}", "", s)
    s = re.sub(r"\\[a-zA-Z]+\s*\*?\s*(\[[^\]]*\])?", " ", s)
    s = s.replace("{", " ").replace("}", " ")
    s = re.sub(r"\s+", " ", s).strip()
    return s


# --------------------------------------------------------------------------
# LaTeX checks
# --------------------------------------------------------------------------

LEADING_ARTICLES = ("A ", "An ", "The ")


def check_tex(path, args, f):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        raw = fh.read()
    text = strip_comments(raw)
    base = os.path.dirname(os.path.abspath(path))

    # Expand \input / \include one level so multi-file papers validate fully.
    for m in list(re.finditer(r"\\(?:input|include)\s*\{([^}]+)\}", text)):
        sub = m.group(1).strip()
        cand = sub if sub.endswith(".tex") else sub + ".tex"
        cand_path = os.path.join(base, cand)
        if os.path.exists(cand_path):
            with open(cand_path, "r", encoding="utf-8", errors="replace") as sfh:
                text = text.replace(m.group(0), strip_comments(sfh.read()))

    check_documentclass(text, args, f)
    floats = find_environments(text, ["figure", "figure*", "table", "table*"])
    check_floats(text, floats, base, f)
    check_mention_order(text, floats, f)
    check_body_text(text, floats, f)
    check_structure(text, args, f)
    check_bibliography(text, base, f)
    check_ai_disclosure(text, args, f)
    return text


def check_documentclass(text, args, f):
    got = find_command_arg(text, "documentclass")
    m = re.search(r"\\documentclass\s*(\[([^\]]*)\])?\s*\{([^}]*)\}", text)
    if not m:
        f.error("class.missing", "No \\documentclass found.")
        return
    opts = [o.strip() for o in (m.group(2) or "").split(",") if o.strip()]
    cls = m.group(3).strip()
    if cls != "IEEEtran":
        f.error(
            "class.wrong",
            f"Document class is '{cls}'. IEEE manuscripts must use IEEEtran.",
            f"line {line_of(text, m.start())}",
        )
        return
    expected = VENUES.get(args.venue, {}).get("options")
    if expected and not any(e in opts for e in expected):
        f.error(
            "class.option",
            f"Venue '{args.venue}' expects a documentclass option from {expected}; found {opts or 'none'}.",
            f"line {line_of(text, m.start())}",
        )
    if "10pt" not in opts and "11pt" not in opts and "12pt" not in opts:
        pass  # IEEEtran defaults correctly
    if args.venue == "peerreview" and "peerreview" not in opts:
        f.warn(
            "class.peerreview",
            "Double-blind submission but 'peerreview' option not set; author identities may render.",
        )


def check_floats(text, floats, base, f):
    seen_labels = {}
    for fl in floats:
        body = fl["body"]
        loc = f"line {fl['line']} ({fl['name']})"

        cap = find_command_arg(body, "caption")
        if not cap:
            f.error("float.caption.missing", f"{fl['name']} has no \\caption.", loc)
            continue
        cap_text, cap_start, cap_end = cap

        lab = find_command_arg(body, "label")
        if not lab:
            f.error(
                "float.label.missing",
                f"{fl['name']} has no \\label, so it cannot be cross-referenced.",
                loc,
            )
        else:
            lname = lab[0].strip()
            if lname in seen_labels:
                f.error("float.label.duplicate", f"Label '{lname}' is used twice.", loc)
            seen_labels[lname] = fl
            fl["label"] = lname
            expected_prefix = "tab:" if fl["kind"] == "table" else "fig:"
            if not lname.startswith(expected_prefix):
                f.warn(
                    "float.label.prefix",
                    f"Label '{lname}' does not use the '{expected_prefix}' prefix; "
                    "consistent prefixes make ordering errors easier to spot.",
                    loc,
                )

        # --- caption placement -------------------------------------------
        if fl["kind"] == "table":
            tab = re.search(r"\\begin\{(tabular|tabularx|threeparttable|array)", body)
            if tab and cap_start > tab.start():
                f.error(
                    "caption.placement.table",
                    "Table caption appears below the table. IEEE requires the caption "
                    "centered above the table.",
                    loc,
                )
        else:
            gfx = re.search(r"\\(includegraphics|input|resizebox|begin\{tikzpicture\})", body)
            if gfx and cap_start < gfx.start():
                f.error(
                    "caption.placement.figure",
                    "Figure caption appears above the graphic. IEEE requires the caption "
                    "below the figure.",
                    loc,
                )

        # --- caption text -------------------------------------------------
        clean = normalize_caption(cap_text)
        check_caption_text(clean, fl, loc, f)

        # --- table specifics ------------------------------------------------
        if fl["kind"] == "table":
            for spec_m in re.finditer(r"\\begin\{tabular\}\s*(\[[^\]]*\])?\s*\{([^}]*)\}", body):
                if "|" in spec_m.group(2):
                    f.warn(
                        "table.vertical.rules",
                        "Tabular column spec contains vertical rules. IEEE tables use "
                        "horizontal rules only (booktabs \\toprule/\\midrule/\\bottomrule).",
                        loc,
                    )
            if re.search(r"\\hline", body) and not re.search(r"\\toprule", body):
                f.info(
                    "table.rules.style",
                    "Table uses \\hline. booktabs rules render closer to IEEE typesetting.",
                    loc,
                )

        # --- figure specifics -----------------------------------------------
        if fl["kind"] == "figure":
            for gm in re.finditer(r"\\includegraphics\s*(\[[^\]]*\])?\s*\{([^}]*)\}", body):
                target = gm.group(2).strip()
                if not resolve_graphic(base, target):
                    f.error(
                        "graphics.missing",
                        f"Included graphic '{target}' was not found on disk.",
                        loc,
                    )
            check_subfigure_order(clean, loc, f)


def resolve_graphic(base, target):
    cands = [target] + [target + e for e in (".pdf", ".png", ".jpg", ".jpeg", ".eps", ".PDF", ".PNG")]
    for c in cands:
        p = c if os.path.isabs(c) else os.path.join(base, c)
        if os.path.exists(p):
            return p
    return None


def check_caption_text(clean, fl, loc, f):
    if not clean:
        f.error("caption.empty", f"{fl['name']} caption is empty.", loc)
        return

    kind = fl["kind"]

    # Trailing source citation like "[5]" is permitted at the very end.
    stripped = re.sub(r"\s*\[\s*\d+(\s*[,-]\s*\d+)*\s*\]\s*$", "", clean).strip()

    if kind == "table":
        if stripped.endswith("."):
            f.error(
                "caption.table.period",
                "Table caption ends with a period. IEEE table captions take no terminal "
                "period (punctuation inside the caption is fine).",
                loc,
            )
        letters = [c for c in stripped if c.isalpha()]
        if letters and all(c.isupper() for c in letters) and len(letters) > 3:
            f.error(
                "caption.table.allcaps",
                "Table caption is typed in ALL CAPS. IEEEtran renders table captions in "
                "small caps, so an all-caps source string prints as full-size capitals. "
                "Write the caption in Title Case.",
                loc,
            )
    else:
        if not stripped.endswith("."):
            f.error(
                "caption.figure.period",
                "Figure caption does not end with a period. IEEE figure captions are "
                "closed with a period.",
                loc,
            )

    first = stripped.split(" ")[0] if stripped else ""
    if first and first[0].isalpha() and not first[0].isupper():
        f.error(
            "caption.capital",
            f"Caption begins with a lowercase word ('{first}'). The first word of a "
            "caption is always capitalized.",
            loc,
        )

    if any(stripped.startswith(a) for a in LEADING_ARTICLES):
        f.warn(
            "caption.leading.article",
            "Caption begins with A/An/The. The IEEE style manual advises against leading "
            "articles in captions.",
            loc,
        )

    if re.match(r"^(Fig\.?|Figure|Table|TABLE)\s*[IVXLCDM0-9]", stripped, re.I):
        f.error(
            "caption.selflabel",
            "Caption repeats its own label. IEEEtran emits 'Fig. N.' and 'TABLE N' "
            "automatically; the caption text must not restate it.",
            loc,
        )


def check_subfigure_order(clean, loc, f):
    parts = re.findall(r"\(([a-z])\)", clean)
    if len(parts) < 2:
        return
    expected = [chr(ord("a") + i) for i in range(len(parts))]
    if parts != expected:
        f.error(
            "caption.subfig.order",
            f"Sub-figure parts are listed as {parts} but must run in order {expected}.",
            loc,
        )


def body_outside_floats(text, floats):
    """Return body text with float environments blanked out (indices preserved)."""
    chars = list(text)
    for fl in floats:
        for i in range(fl["start"], min(fl["end"], len(chars))):
            chars[i] = " "
    return "".join(chars)


def check_mention_order(text, floats, f):
    body = body_outside_floats(text, floats)

    first_mention = {}
    for m in re.finditer(r"\\(?:ref|cref|Cref|autoref)\s*\{([^}]*)\}", body):
        for label in [l.strip() for l in m.group(1).split(",")]:
            if label and label not in first_mention:
                first_mention[label] = m.start()

    defined = {fl.get("label"): fl for fl in floats if fl.get("label")}

    for label, fl in defined.items():
        if label not in first_mention:
            f.error(
                "float.unreferenced",
                f"{fl['name']} '{label}' is never cited in the body text. Every figure and "
                "table must be mentioned, and mentioned in numerical order.",
                f"line {fl['line']}",
            )

    for m in re.finditer(r"\\(?:ref|cref|Cref|autoref)\s*\{([^}]*)\}", body):
        for label in [l.strip() for l in m.group(1).split(",")]:
            if label and label not in defined and not label.startswith(("eq:", "sec:", "alg:", "app:")):
                f.warn(
                    "ref.undefined",
                    f"Reference to '{label}' has no matching \\label in a float.",
                    f"line {line_of(text, m.start())}",
                )

    for kind in ("figure", "table"):
        seq = [
            (fl["label"], first_mention[fl["label"]], fl)
            for fl in floats
            if fl["kind"] == kind and fl.get("label") in first_mention
        ]
        for i in range(1, len(seq)):
            prev_label, prev_pos, prev_fl = seq[i - 1]
            label, pos, fl = seq[i]
            if pos < prev_pos:
                noun = "Figure" if kind == "figure" else "Table"
                f.error(
                    "float.mention.order",
                    f"{noun} order defect: '{label}' (defined after '{prev_label}', so it "
                    f"gets the higher number) is first mentioned in the text before "
                    f"'{prev_label}'. IEEE requires first citations to appear in numerical "
                    "order. Fix the narrative order or swap the float definitions.",
                    f"line {fl['line']}",
                )


def check_body_text(text, floats, f):
    body = body_outside_floats(text, floats)

    for m in re.finditer(r"\bFigures?\b\s*(~|\\ref|\s+\d)", body):
        f.error(
            "text.figure.word",
            "Body text uses 'Figure'. IEEE always abbreviates to 'Fig.' in text, including "
            "at the start of a sentence.",
            f"line {line_of(text, m.start())}",
        )

    for m in re.finditer(r"\bFigs\.", body):
        f.error(
            "text.figs.plural",
            "Body text uses 'Figs.'. IEEE keeps 'Fig.' singular even when citing several "
            "figures or several parts.",
            f"line {line_of(text, m.start())}",
        )

    for m in re.finditer(r"\bTab\.\s*(~|\\ref|\d)", body):
        f.error(
            "text.table.abbrev",
            "Body text uses 'Tab.'. IEEE writes 'Table' in full, with a Roman numeral.",
            f"line {line_of(text, m.start())}",
        )

    for m in re.finditer(
        r"(Fig\.|Table)[^.\n]{0,40}?\bof\b\s*(reference\s*)?(\\cite\s*\{|\[\s*\d)", body
    ):
        f.error(
            "text.fig.of.ref",
            "Body text uses the 'Fig. X of [n]' construction, which IEEE prohibits. "
            "Reproduce the figure with a source citation in its caption instead.",
            f"line {line_of(text, m.start())}",
        )

    for m in re.finditer(r"(?<![~\\{])\b(Fig\.|Table)\s+\\ref", body):
        f.warn(
            "text.nonbreaking",
            f"'{m.group(1)} \\ref' uses a plain space. Use a non-breaking tilde "
            f"({m.group(1)}~\\ref{{...}}) so the label never wraps to the next line.",
            f"line {line_of(text, m.start())}",
        )

    for m in re.finditer(r"\bEq(?:uation)?\.?\s*~?\s*\(?\\ref\{eq", body):
        f.info(
            "text.equation.style",
            "Equations are normally cited as '(1)' rather than 'Eq. (1)' except at the "
            "start of a sentence.",
            f"line {line_of(text, m.start())}",
        )


def check_structure(text, args, f):
    if not re.search(r"\\begin\{abstract\}", text):
        f.error("struct.abstract", "No abstract environment found.")
    else:
        m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", text, re.S)
        if m:
            words = len(normalize_caption(m.group(1)).split())
            if words > 250:
                f.warn(
                    "struct.abstract.length",
                    f"Abstract runs {words} words. IEEE venues typically cap it at 150 to 250; "
                    "check the author kit.",
                )
            if words < 40:
                f.warn("struct.abstract.length", f"Abstract runs only {words} words.")

    if not re.search(r"\\begin\{IEEEkeywords\}", text):
        f.error(
            "struct.keywords",
            "No IEEEkeywords environment found. IEEE requires Index Terms.",
        )

    title = find_command_arg(text, "title")
    if title:
        t = normalize_caption(title[0])
        acronyms = [w for w in re.findall(r"\b[A-Z]{3,}\b", t) if w not in ("IEEE",)]
        if acronyms:
            f.warn(
                "title.acronym",
                f"Title contains acronyms {acronyms}. IEEE advises against abbreviations in "
                "titles unless unavoidable.",
            )

    if re.search(r"\\(?:geometry|setlength\s*\{\s*\\(?:textwidth|columnsep|topmargin|oddsidemargin))", text):
        f.error(
            "layout.override",
            "Source overrides page geometry. IEEEtran sets the required layout; manual "
            "geometry changes are a compliance failure and are visible to reviewers.",
        )

    if re.search(r"\\usepackage\s*(\[[^\]]*\])?\s*\{[^}]*\bgeometry\b", text):
        f.error(
            "layout.geometry.package",
            "The geometry package is loaded. Remove it: IEEEtran controls the page layout.",
        )

    for cmd in ("baselinestretch", "linespread"):
        if re.search(r"\\" + cmd, text):
            f.error(
                "layout.spacing",
                f"\\{cmd} changes line spacing. IEEE fixes leading; remove it.",
            )


def check_bibliography(text, base, f):
    m = re.search(r"\\bibliographystyle\s*\{([^}]*)\}", text)
    manual = re.search(r"\\begin\{thebibliography\}", text)
    if m:
        style = m.group(1).strip()
        if not style.startswith("IEEEtran"):
            f.error(
                "refs.style",
                f"Bibliography style is '{style}'. IEEE numbers references by order of first "
                "citation; use IEEEtran (plain/alpha/apalike alphabetize and are wrong).",
            )
    elif not manual:
        f.warn("refs.style", "No \\bibliographystyle and no thebibliography environment found.")

    if manual:
        block = re.search(r"\\begin\{thebibliography\}(.*?)\\end\{thebibliography\}", text, re.S)
        if block:
            for bm in re.finditer(r"\\bibitem\s*(\[[^\]]*\])?\s*\{([^}]*)\}(.*?)(?=\\bibitem|\Z)", block.group(1), re.S):
                key = bm.group(2)
                entry = normalize_caption(bm.group(3))
                if not entry:
                    continue
                n_authors = entry.count(" and ") + entry.count(", ")
                if re.search(r"\d\s*-\s*\d", entry) and "--" not in bm.group(3):
                    f.warn(
                        "refs.pagerange",
                        f"Reference '{key}' appears to use a hyphen in a page range. IEEE uses "
                        "an en dash (-- in LaTeX).",
                    )
                if not entry.rstrip().endswith(".") and not re.search(r"https?://\S+$", entry.rstrip()):
                    f.warn(
                        "refs.terminal.period",
                        f"Reference '{key}' does not end with a period. IEEE entries end with a "
                        "period unless they end with a URL.",
                    )

    bibs = re.search(r"\\bibliography\s*\{([^}]*)\}", text)
    if bibs:
        for name in [b.strip() for b in bibs.group(1).split(",")]:
            path = os.path.join(base, name if name.endswith(".bib") else name + ".bib")
            if not os.path.exists(path):
                f.error("refs.bib.missing", f"Bibliography file '{name}' not found.")
                continue
            check_bibfile(path, f)


def check_bibfile(path, f):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        content = fh.read()
    for m in re.finditer(r"@(\w+)\s*\{\s*([^,]+),(.*?)\n\}", content, re.S):
        etype, key, fields = m.group(1).lower(), m.group(2).strip(), m.group(3)
        pages = re.search(r"pages\s*=\s*[{\"]([^}\"]*)", fields, re.I)
        if pages and re.search(r"\d\s*-\s*\d", pages.group(1)) and "--" not in pages.group(1):
            f.warn(
                "refs.pagerange",
                f"Entry '{key}' uses a hyphen in the page range. IEEE uses an en dash: "
                "write 123--145 in BibTeX.",
                path,
            )
        author = re.search(r"author\s*=\s*[{\"](.*?)[}\"]\s*,", fields, re.S | re.I)
        if author:
            names = [a for a in re.split(r"\s+and\s+", author.group(1)) if a.strip()]
            if len(names) > 6 and "et al" not in author.group(1).lower():
                f.warn(
                    "refs.etal",
                    f"Entry '{key}' lists {len(names)} authors. IEEE lists up to six names, "
                    "then the primary author followed by et al.",
                    path,
                )
        if etype in ("article", "inproceedings") and not re.search(r"doi\s*=", fields, re.I):
            f.info(
                "refs.doi",
                f"Entry '{key}' has no DOI field. IEEE requires a DOI for every reference that "
                "has one.",
                path,
            )


AI_TOKENS = (
    "artificial intelligence",
    "large language model",
    "llm",
    "generative ai",
    "claude",
    "gpt",
    "chatgpt",
    "copilot",
    "gemini",
)


def check_ai_disclosure(text, args, f):
    m = re.search(
        r"\\section\*?\s*\{\s*Acknowledg(?:e)?ment[s]?\s*\}(.*?)(?=\\section|\\bibliography|\\begin\{thebibliography\}|\Z)",
        text,
        re.S | re.I,
    )
    ack = m.group(1).lower() if m else ""
    has_disclosure = any(tok in ack for tok in AI_TOKENS)

    if args.ai_drafted and not has_disclosure:
        f.error(
            "ai.disclosure.missing",
            "This manuscript contains AI-generated content but the acknowledgments do not "
            "disclose it. IEEE requires disclosure naming the AI system, the specific "
            "sections it produced, and the level of involvement. Add it, and name the real "
            "sections rather than pasting a generic sentence.",
        )
    elif args.ai_drafted and has_disclosure:
        generic = len(ack.split()) < 20
        if generic:
            f.warn(
                "ai.disclosure.generic",
                "AI disclosure is present but very short. It must identify the system, the "
                "specific sections, and the level of involvement.",
            )
    elif has_disclosure:
        f.info("ai.disclosure.present", "AI disclosure detected in acknowledgments.")


# --------------------------------------------------------------------------
# DOCX checks
# --------------------------------------------------------------------------

def check_docx(path, args, f):
    try:
        import docx
        from docx.table import Table
        from docx.text.paragraph import Paragraph
    except ImportError:
        f.warn("docx.dependency", "python-docx is not installed; DOCX checks were skipped.")
        return ""

    doc = docx.Document(path)
    body = doc.element.body

    blocks = []
    for child in body.iterchildren():
        tag = child.tag.split("}")[-1]
        if tag == "p":
            p = Paragraph(child, doc)
            has_img = bool(child.findall(".//{http://schemas.openxmlformats.org/drawingml/2006/main}blip"))
            blocks.append({"type": "p", "text": p.text.strip(), "img": has_img, "obj": p})
        elif tag == "tbl":
            blocks.append({"type": "tbl", "text": "", "img": False, "obj": Table(child, doc)})

    tbl_cap = re.compile(r"^\s*TABLE\s+([IVXLCDM]+)\b", re.I)
    fig_cap = re.compile(r"^\s*(Fig\.|Figure)\s*(\d+)\b", re.I)

    fig_defs, tab_defs = [], []

    for i, b in enumerate(blocks):
        if b["type"] == "tbl":
            before = blocks[i - 1] if i > 0 else None
            after = blocks[i + 1] if i + 1 < len(blocks) else None
            cap_before = before and tbl_cap.match(before["text"])
            cap_after = after and tbl_cap.match(after["text"])
            if cap_after and not cap_before:
                f.error(
                    "caption.placement.table",
                    f"Table caption '{after['text'][:50]}' sits below its table. IEEE places "
                    "table captions above.",
                    f"block {i}",
                )
            elif not cap_before and not cap_after:
                f.error(
                    "float.caption.missing",
                    f"Table at block {i} has no caption paragraph adjacent to it.",
                    f"block {i}",
                )
            # Record the number from whichever side the caption sits on, so a
            # placement defect does not also suppress the ordering check.
            cap = cap_before or cap_after
            if cap:
                tab_defs.append(cap.group(1).upper())
                cap_block = i - 1 if cap_before else i + 1
                cap_text = before["text"] if cap_before else after["text"]
                check_docx_caption(cap_text, "table", f, f"block {cap_block}")

        if b["type"] == "p" and b["img"]:
            after = blocks[i + 1] if i + 1 < len(blocks) else None
            before = blocks[i - 1] if i > 0 else None
            cap_after = after and fig_cap.match(after["text"])
            cap_before = before and fig_cap.match(before["text"])
            if cap_before and not cap_after:
                f.error(
                    "caption.placement.figure",
                    f"Figure caption '{before['text'][:50]}' sits above its graphic. IEEE "
                    "places figure captions below.",
                    f"block {i}",
                )
            elif not cap_after and not cap_before:
                f.error(
                    "float.caption.missing",
                    f"Image at block {i} has no caption paragraph adjacent to it.",
                    f"block {i}",
                )
            cap = cap_after or cap_before
            if cap:
                fig_defs.append(int(cap.group(2)))
                cap_block = i + 1 if cap_after else i - 1
                cap_text = after["text"] if cap_after else before["text"]
                check_docx_caption(cap_text, "figure", f, f"block {cap_block}")
                if cap.group(1).lower() == "figure":
                    f.error(
                        "caption.figure.label",
                        "Figure caption uses 'Figure'. IEEE captions and text both use 'Fig.'",
                        f"block {cap_block}",
                    )

    prose = "\n".join(
        b["text"] for b in blocks
        if b["type"] == "p" and not tbl_cap.match(b["text"]) and not fig_cap.match(b["text"])
    )

    for m in re.finditer(r"\bFigures?\s+\d", prose):
        f.error(
            "text.figure.word",
            f"Body text uses '{m.group(0)}'. IEEE abbreviates to 'Fig.' in text, including at "
            "the start of a sentence.",
        )
    for m in re.finditer(r"\bFigs\.\s*\d", prose):
        f.error("text.figs.plural", "Body text uses 'Figs.'. IEEE keeps 'Fig.' singular.")
    for m in re.finditer(r"(Fig\.|Table)[^.\n]{0,40}?\bof\b\s*(reference\s*)?\[\s*\d", prose):
        f.error(
            "text.fig.of.ref",
            "Body text uses the 'Fig. X of [n]' construction, which IEEE prohibits.",
        )

    mentioned_figs = [int(m.group(1)) for m in re.finditer(r"\bFig(?:\.|ure)\s*(\d+)", prose)]
    check_docx_order(mentioned_figs, fig_defs, "Figure", f)
    roman = re.findall(r"\bTable\s+([IVXLCDM]+)\b", prose)
    check_docx_order([roman_to_int(r) for r in roman],
                     [roman_to_int(r) for r in tab_defs], "Table", f)

    check_docx_direct_formatting(doc, f)
    return prose


def check_docx_caption(text, kind, f, loc):
    body = re.sub(r"^\s*(TABLE\s+[IVXLCDM]+|Fig\.|Figure\s*\d+)\.?\s*", "", text, flags=re.I).strip()
    if not body:
        return
    if kind == "table":
        if body.endswith("."):
            f.error(
                "caption.table.period",
                "Table caption ends with a period; IEEE table captions take none.",
                loc,
            )
    else:
        if not body.endswith("."):
            f.error(
                "caption.figure.period",
                "Figure caption does not end with a period.",
                loc,
            )
    if any(body.startswith(a) for a in LEADING_ARTICLES):
        f.warn("caption.leading.article", "Caption begins with A/An/The.", loc)
    if body[0].isalpha() and not body[0].isupper():
        f.error("caption.capital", "Caption's first word is not capitalized.", loc)


def check_docx_order(mentions, definitions, noun, f):
    first_seen = []
    for n in mentions:
        if n not in first_seen:
            first_seen.append(n)
    ordered = [n for n in first_seen if n in definitions]
    if ordered != sorted(ordered):
        f.error(
            "float.mention.order",
            f"{noun} first mentions appear in the order {ordered}. IEEE requires first "
            f"citations in numerical order.",
        )
    missing = [d for d in definitions if d not in first_seen]
    if missing:
        f.error(
            "float.unreferenced",
            f"{noun}(s) {missing} are never cited in the body text.",
        )


def roman_to_int(s):
    vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total, prev = 0, 0
    for ch in reversed(s.upper()):
        v = vals.get(ch, 0)
        total = total - v if v < prev else total + v
        prev = max(prev, v)
    return total


def check_docx_direct_formatting(doc, f):
    offenders = 0
    for p in doc.paragraphs:
        for run in p.runs:
            if run.font.size is not None or (run.font.name and run.font.name not in ("Times New Roman",)):
                offenders += 1
    if offenders:
        f.warn(
            "docx.direct.formatting",
            f"{offenders} run(s) carry direct font overrides instead of inheriting template "
            "styles. Direct formatting is how Word manuscripts drift; restyle using the "
            "IEEE template's named styles.",
        )


# --------------------------------------------------------------------------
# PDF checks
# --------------------------------------------------------------------------

def check_pdf(pdf_path, args, f):
    if not os.path.exists(pdf_path):
        f.error("pdf.missing", f"PDF '{pdf_path}' not found; build it before validating.")
        return

    if shutil.which("pdffonts"):
        try:
            out = subprocess.run(
                ["pdffonts", pdf_path], capture_output=True, text=True, timeout=60
            ).stdout
            lines = [l for l in out.strip().split("\n")[2:] if l.strip()]
            bad = []
            for line in lines:
                cols = line.split()
                # columns end with: emb sub uni object ID
                if len(cols) < 6:
                    continue
                emb, sub = cols[-5], cols[-4]
                if emb != "yes" or sub != "yes":
                    bad.append(f"{cols[0]} (emb={emb}, sub={sub})")
            if bad:
                f.error(
                    "pdf.fonts.embedded",
                    f"Fonts not embedded or not subset: {sorted(set(bad))[:6]}. Failure to embed "
                    "and subset fonts is the most common cause of IEEE Xplore PDF rejection.",
                )
            elif lines:
                f.info("pdf.fonts.embedded", f"All {len(lines)} fonts embedded and subset.")
        except Exception as e:
            f.warn("pdf.fonts.embedded", f"pdffonts check failed: {e}")
    else:
        f.warn("pdf.fonts.embedded", "pdffonts unavailable; font embedding was not verified.")

    if shutil.which("pdfinfo"):
        try:
            out = subprocess.run(
                ["pdfinfo", pdf_path], capture_output=True, text=True, timeout=60
            ).stdout
            pages = re.search(r"Pages:\s*(\d+)", out)
            size = re.search(r"Page size:\s*([\d.]+) x ([\d.]+)", out)
            if pages and args.page_limit:
                n = int(pages.group(1))
                if n > args.page_limit:
                    f.error(
                        "pdf.pagecount",
                        f"Manuscript is {n} pages against a limit of {args.page_limit}. Cut "
                        "content: shrinking figures or altering margins is a compliance failure.",
                    )
                else:
                    f.info("pdf.pagecount", f"{n} of {args.page_limit} pages used.")
            if size:
                w, h = float(size.group(1)), float(size.group(2))
                letter = abs(w - 612) < 3 and abs(h - 792) < 3
                a4 = abs(w - 595) < 3 and abs(h - 842) < 3
                if not (letter or a4):
                    f.error(
                        "pdf.pagesize",
                        f"Page size is {w} x {h} pt, which is neither US Letter nor A4.",
                    )
                elif args.paper == "letter" and not letter:
                    f.error("pdf.pagesize", "A4 output but US Letter was requested.")
                elif args.paper == "a4" and not a4:
                    f.error("pdf.pagesize", "US Letter output but A4 was requested.")
        except Exception as e:
            f.warn("pdf.info", f"pdfinfo check failed: {e}")


# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------

SEV_ORDER = {ERROR: 0, WARN: 1, INFO: 2}


def report(f, args, target):
    if args.json:
        print(json.dumps({
            "target": target,
            "venue": args.venue,
            "errors": f.n_errors,
            "warnings": f.n_warns,
            "findings": f.items,
        }, indent=2))
        return

    print(f"IEEE validation: {target}  (venue: {args.venue})")
    print("=" * 72)
    items = sorted(f.items, key=lambda i: (SEV_ORDER[i["severity"]], i["check"]))
    if not items:
        print("No findings.")
    for it in items:
        loc = f"  [{it['location']}]" if it.get("location") else ""
        print(f"{it['severity']:<5} {it['check']}{loc}")
        for line in wrap(it["message"], 68):
            print(f"      {line}")
    print("=" * 72)
    verdict = "PASS" if f.n_errors == 0 else "FAIL"
    print(f"{verdict}: {f.n_errors} error(s), {f.n_warns} warning(s)")
    if f.n_errors:
        print("Fix every ERROR before presenting this manuscript.")


def wrap(text, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > width:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(cur)
    return lines


def main():
    ap = argparse.ArgumentParser(description="Validate an IEEE manuscript.")
    ap.add_argument("source", help="Path to .tex or .docx manuscript")
    ap.add_argument("--venue", default="conference", choices=sorted(VENUES.keys()))
    ap.add_argument("--pdf", help="Built PDF to check for fonts, page count, page size")
    ap.add_argument("--page-limit", type=int, default=None)
    ap.add_argument("--paper", choices=["letter", "a4"], default=None)
    ap.add_argument("--ai-drafted", action="store_true",
                    help="This skill generated body content; makes AI disclosure blocking")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if not os.path.exists(args.source):
        print(f"No such file: {args.source}", file=sys.stderr)
        return 2

    if args.page_limit is None:
        args.page_limit = VENUES.get(args.venue, {}).get("pages")

    f = Findings()
    ext = os.path.splitext(args.source)[1].lower()
    if ext == ".tex":
        check_tex(args.source, args, f)
    elif ext == ".docx":
        check_docx(args.source, args, f)
    else:
        print(f"Unsupported input type '{ext}'. Use .tex or .docx.", file=sys.stderr)
        return 2

    if args.pdf:
        check_pdf(args.pdf, args, f)

    report(f, args, args.source)
    return 1 if f.n_errors else 0


if __name__ == "__main__":
    sys.exit(main())
