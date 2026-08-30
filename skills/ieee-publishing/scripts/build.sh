#!/usr/bin/env bash
# build.sh - Compile an IEEE manuscript with the bundled IEEEtran class.
#
# Usage: bash build.sh path/to/main.tex
#
# Puts the skill's assets/ directory on TEXINPUTS and BSTINPUTS so the build
# works even when the local TeX distribution has no IEEE package installed.
# Runs enough passes to settle cross-references and the bibliography, then
# reports anything still unresolved.

set -uo pipefail

TEX_SRC="${1:-main.tex}"
if [[ ! -f "$TEX_SRC" ]]; then
  echo "build.sh: no such file: $TEX_SRC" >&2
  exit 2
fi

SRC_DIR="$(cd "$(dirname "$TEX_SRC")" && pwd)"
BASE="$(basename "${TEX_SRC%.*}")"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ASSETS="$(dirname "$SCRIPT_DIR")/assets"

export TEXINPUTS=".:${SRC_DIR}:${ASSETS}:${TEXINPUTS:-}"
export BSTINPUTS=".:${SRC_DIR}:${ASSETS}:${BSTINPUTS:-}"
export BIBINPUTS=".:${SRC_DIR}:${BIBINPUTS:-}"

cd "$SRC_DIR" || exit 2

if ! command -v pdflatex >/dev/null 2>&1; then
  echo "build.sh: pdflatex not found. Install TeX Live, or use the Word path" >&2
  echo "          (see references/word-path.md)." >&2
  exit 3
fi

echo "Building $BASE.tex"
run_pass() {
  pdflatex -interaction=nonstopmode -halt-on-error -file-line-error "$BASE.tex" \
    > ".build-pass-$1.log" 2>&1
}

if ! run_pass 1; then
  echo
  echo "LaTeX failed. First errors:"
  grep -E "^[^:]+:[0-9]+:|^! " ".build-pass-1.log" | head -20
  exit 1
fi

if grep -q "\\\\citation" "$BASE.aux" 2>/dev/null; then
  if command -v bibtex >/dev/null 2>&1; then
    bibtex "$BASE" > .build-bibtex.log 2>&1 || {
      echo "BibTeX reported problems:"
      grep -E "^(Warning|I couldn't|Repeated|Illegal)" .build-bibtex.log | head -15
    }
  else
    echo "bibtex not found; references will not resolve." >&2
  fi
fi

run_pass 2
run_pass 3

if [[ ! -f "$BASE.pdf" ]]; then
  echo "Build produced no PDF. See .build-pass-3.log" >&2
  exit 1
fi

echo
UNDEF=$(grep -ci "undefined" ".build-pass-3.log" 2>/dev/null) || UNDEF=0
if [[ "$UNDEF" -gt 0 ]]; then
  echo "Unresolved references or citations:"
  grep -i "undefined" ".build-pass-3.log" | sed 's/^/  /' | sort -u | head -20
  echo
fi

OVERFULL=$(grep -c "Overfull .hbox" ".build-pass-3.log" 2>/dev/null) || OVERFULL=0
if [[ "$OVERFULL" -gt 0 ]]; then
  echo "$OVERFULL overfull hbox warning(s): content is spilling past the column."
  echo "  Fix the content, never the column width."
  echo
fi

if command -v pdfinfo >/dev/null 2>&1; then
  PAGES=$(pdfinfo "$BASE.pdf" 2>/dev/null | awk '/^Pages:/{print $2}')
  echo "Built $SRC_DIR/$BASE.pdf (${PAGES:-?} pages)"
else
  echo "Built $SRC_DIR/$BASE.pdf"
fi

rm -f .build-pass-1.log .build-pass-2.log

echo
echo "Now validate before presenting it:"
echo "  python3 $SCRIPT_DIR/validate_ieee.py $SRC_DIR/$BASE.tex --pdf $SRC_DIR/$BASE.pdf --venue <venue>"
