#!/usr/bin/env python3
"""
check_graphics.py - Check figure files against IEEE Xplore graphics requirements.

Thresholds come from IEEE's PDF specification and graphics FAQ:
  - 600 dpi minimum for monochrome (bitonal) art
  - 300 dpi minimum for grayscale and color
  - maximum physical size 7.16 x 8.8 inches
  - vector art is preferred, but every font must be embedded
  - text inside graphics should not fall below ~6 pt (4 pt is the hard floor)

Usage:
  check_graphics.py figures/
  check_graphics.py figures/fig1.pdf figures/fig2.png --json
"""

import argparse
import glob
import json
import os
import re
import shutil
import subprocess
import sys

MAX_W_IN = 7.16
MAX_H_IN = 8.8
RASTER_EXT = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp", ".gif"}
VECTOR_EXT = {".pdf", ".eps", ".ps", ".svg"}


def check_raster(path, findings):
    try:
        from PIL import Image
    except ImportError:
        findings.append((path, "WARN", "Pillow not installed; raster checks skipped."))
        return

    try:
        with Image.open(path) as im:
            w, h = im.size
            mode = im.mode
            dpi = im.info.get("dpi")
            fmt = im.format
    except Exception as e:
        findings.append((path, "ERROR", f"Could not open image: {e}"))
        return

    if os.path.splitext(path)[1].lower() == ".gif":
        findings.append(
            (path, "ERROR", "GIF is not an accepted IEEE figure format. Use PDF, EPS, TIFF, or PNG.")
        )

    bitonal = mode in ("1",)
    grayscale = mode in ("L", "LA")
    required = 600 if bitonal else 300
    kind = "monochrome" if bitonal else ("grayscale" if grayscale else "color")

    if not dpi or dpi[0] in (0, 1):
        findings.append(
            (
                path,
                "WARN",
                f"No DPI metadata ({w}x{h} px, {kind}). Resolution depends on the placed size: "
                f"at {required} dpi this image may be placed at most "
                f"{w/required:.2f} x {h/required:.2f} in. Set DPI on export.",
            )
        )
        return

    dx, dy = float(dpi[0]), float(dpi[1])
    # PNG stores resolution as integer pixels-per-metre, so a true 300 dpi file
    # reads back as 299.9994. Round before comparing or every correct file fails.
    eff = round(min(dx, dy))
    if eff < required:
        findings.append(
            (
                path,
                "ERROR",
                f"{eff} dpi {kind} image. IEEE requires at least {required} dpi for "
                f"{kind}. Re-export from source; upsampling does not add real resolution.",
            )
        )
    else:
        findings.append((path, "OK", f"{eff} dpi {kind}, {w}x{h} px, {fmt}."))

    win, hin = w / dx, h / dy
    if win > MAX_W_IN or hin > MAX_H_IN:
        findings.append(
            (
                path,
                "INFO",
                f"Native size {win:.2f} x {hin:.2f} in is above the {MAX_W_IN} x {MAX_H_IN} in "
                "cap for separately submitted figure files. Harmless when the graphic is placed "
                "smaller in the manuscript (scaling down raises effective dpi), but crop or "
                "resize before uploading loose figures to a journal.",
            )
        )

    if mode in ("RGBA", "LA", "PA"):
        findings.append(
            (path, "WARN", "Image carries an alpha channel. Flatten layers before submission; "
                           "IEEE requires flattened graphics.")
        )


def check_vector(path, findings):
    ext = os.path.splitext(path)[1].lower()

    if ext == ".svg":
        findings.append(
            (
                path,
                "ERROR",
                "SVG is not an accepted IEEE submission format. Convert to PDF or EPS with "
                "fonts embedded or converted to outlines.",
            )
        )
        return

    if not shutil.which("pdffonts"):
        findings.append((path, "WARN", "pdffonts unavailable; font embedding not verified."))
        return

    if ext in (".eps", ".ps"):
        findings.append(
            (
                path,
                "WARN",
                "PostScript art: confirm fonts are embedded. Distilling to PDF makes this "
                "checkable and is generally safer for submission.",
            )
        )
        return

    try:
        out = subprocess.run(["pdffonts", path], capture_output=True, text=True, timeout=60).stdout
    except Exception as e:
        findings.append((path, "WARN", f"pdffonts failed: {e}"))
        return

    lines = [l for l in out.strip().split("\n")[2:] if l.strip()]
    if not lines:
        findings.append((path, "OK", "Vector art with no embedded text (outlines or no fonts)."))
    else:
        bad = []
        for line in lines:
            cols = line.split()
            if len(cols) < 6:
                continue
            emb, sub = cols[-5], cols[-4]
            if emb != "yes":
                bad.append(f"{cols[0]} (emb={emb}, sub={sub})")
        if bad:
            findings.append(
                (
                    path,
                    "ERROR",
                    f"Fonts not embedded: {bad}. Vector graphics require every font embedded, "
                    "or convert text to outlines.",
                )
            )
        else:
            findings.append((path, "OK", f"Vector art, {len(lines)} font(s) embedded."))

    if shutil.which("pdfinfo"):
        try:
            info = subprocess.run(["pdfinfo", path], capture_output=True, text=True, timeout=60).stdout
            m = re.search(r"Page size:\s*([\d.]+) x ([\d.]+)", info)
            if m:
                win, hin = float(m.group(1)) / 72, float(m.group(2)) / 72
                if win > MAX_W_IN or hin > MAX_H_IN:
                    findings.append(
                        (
                            path,
                            "WARN",
                            f"Artboard is {win:.2f} x {hin:.2f} in, above the "
                            f"{MAX_W_IN} x {MAX_H_IN} in cap. Crop the bounding box.",
                        )
                    )
        except Exception:
            pass


def collect(paths):
    files = []
    for p in paths:
        if os.path.isdir(p):
            for ext in list(RASTER_EXT) + list(VECTOR_EXT):
                files.extend(glob.glob(os.path.join(p, "**", "*" + ext), recursive=True))
        else:
            files.append(p)
    return sorted(set(files))


def main():
    ap = argparse.ArgumentParser(description="Check figures against IEEE graphics requirements.")
    ap.add_argument("paths", nargs="+", help="Figure files or directories")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    files = collect(args.paths)
    if not files:
        print("No graphics found.", file=sys.stderr)
        return 2

    findings = []
    for path in files:
        ext = os.path.splitext(path)[1].lower()
        if ext in RASTER_EXT:
            check_raster(path, findings)
        elif ext in VECTOR_EXT:
            check_vector(path, findings)

    if args.json:
        print(json.dumps(
            [{"file": p, "severity": s, "message": m} for p, s, m in findings], indent=2
        ))
    else:
        print(f"IEEE graphics check: {len(files)} file(s)")
        print("=" * 72)
        for p, s, m in findings:
            print(f"{s:<5} {os.path.basename(p)}")
            print(f"      {m}")
        n_err = sum(1 for _, s, _ in findings if s == "ERROR")
        n_warn = sum(1 for _, s, _ in findings if s == "WARN")
        print("=" * 72)
        print(f"{'PASS' if n_err == 0 else 'FAIL'}: {n_err} error(s), {n_warn} warning(s)")

    return 1 if any(s == "ERROR" for _, s, _ in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
