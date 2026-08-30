#!/usr/bin/env python3
"""Render an architecture spec to .drawio, .svg, .png and .html.

Usage
-----
    python render.py spec.json --outdir out
    python render.py spec.json --outdir out --styles blueprint,tron,ghibli
    python render.py --list-styles

The spec is JSON. See references/spec-schema.md for the full contract.
"""

import argparse
import html
import json
import math
import os
import random
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import glyphs  # noqa: E402
from styles import STYLES, GROUPS, resolve  # noqa: E402

NODE_W, NODE_H = 210, 92
GAP_X, GAP_Y = 36, 30
TIER_PAD, TIER_PAD_TOP = 28, 54
TIER_GAP, MARGIN = 64, 56
MAX_PER_ROW = 4

AWS_RES = {
    "lambda": "lambda", "s3": "s3", "ec2": "ec2", "rds": "rds", "dynamodb": "dynamodb",
    "sqs": "sqs", "sns": "sns", "cloudfront": "cloudfront", "route53": "route_53",
    "apigateway": "api_gateway", "elb": "elastic_load_balancing", "alb": "elastic_load_balancing",
    "ecs": "elastic_container_service", "eks": "elastic_kubernetes_service",
    "waf": "waf", "cloudwatch": "cloudwatch", "kms": "key_management_service",
    "elasticache": "elasticache", "aurora": "aurora", "sagemaker": "sagemaker",
    "cognito": "cognito", "eventbridge": "eventbridge", "step": "step_functions",
}


# --------------------------------------------------------------------- layout
def layout(spec):
    """Assign absolute geometry to tiers and nodes. Explicit x/y/w/h wins."""
    title = spec.get("title")
    subtitle = spec.get("subtitle")
    per_row = int(spec.get("max_per_row", MAX_PER_ROW))
    tiers = spec.get("tiers") or []
    tier_of = {}
    for ti, t in enumerate(tiers):
        for nd in t.get("nodes", []):
            tier_of[nd.get("id")] = ti
    lateral = any(tier_of.get(e.get("from")) == tier_of.get(e.get("to"))
                  and e.get("label") for e in spec.get("edges") or [])
    gap_x = 96 if lateral else GAP_X
    top = MARGIN + (96 if title else 0)

    widest = 0
    for t in tiers:
        n = max(1, len(t.get("nodes", [])))
        cols = min(per_row, n)
        w = cols * NODE_W + (cols - 1) * gap_x + 2 * TIER_PAD
        widest = max(widest, w, int(t.get("w", 0)))
    content_w = max(widest, 900)

    y = top
    index = {}
    for ti, t in enumerate(tiers):
        nodes = t.get("nodes", [])
        n = max(1, len(nodes))
        cols = min(per_row, n)
        rows = math.ceil(n / cols) if n else 1
        t_w = int(t.get("w", cols * NODE_W + (cols - 1) * gap_x + 2 * TIER_PAD))
        t_h = int(t.get("h", TIER_PAD_TOP + rows * NODE_H + (rows - 1) * GAP_Y + TIER_PAD))
        t_x = int(t.get("x", MARGIN + (content_w - t_w) / 2))
        t_y = int(t.get("y", y))
        t.update(_x=t_x, _y=t_y, _w=t_w, _h=t_h, _i=ti)

        for i, nd in enumerate(nodes):
            r, c = divmod(i, cols)
            in_row = min(cols, n - r * cols)
            row_w = in_row * NODE_W + (in_row - 1) * gap_x
            nx = int(nd.get("x", t_x + (t_w - row_w) / 2 + c * (NODE_W + gap_x)))
            ny = int(nd.get("y", t_y + TIER_PAD_TOP + r * (NODE_H + GAP_Y)))
            nd.update(_x=nx, _y=ny, _w=int(nd.get("w", NODE_W)),
                      _h=int(nd.get("h", NODE_H)), _tier=ti)
            index[nd["id"]] = nd
        y = t_y + t_h + TIER_GAP

    legend = spec.get("legend") or []
    height = y - TIER_GAP + MARGIN + (78 if legend else 0)
    spec["_w"] = content_w + 2 * MARGIN
    spec["_h"] = max(height, 400)
    spec["_index"] = index
    spec["_title_y"] = MARGIN + 34 if title else None
    spec["_subtitle"] = subtitle
    return spec


# ------------------------------------------------------------------ svg parts
def esc(s):
    return html.escape(str(s), quote=True)


def _rand(seed):
    r = random.Random(seed)
    return r


def defs(st, W, H):
    """Filters, gradients and patterns used by the effects."""
    fx = st["fx"]
    d = ['<defs>']
    d.append('<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
             'markerHeight="7" orient="auto-start-reverse">'
             '<path d="M0 0L10 5L0 10z" fill="%s"/></marker>' % st["edge"])
    d.append('<filter id="shadow" x="-30%%" y="-30%%" width="180%%" height="200%%">'
             '<feDropShadow dx="0" dy="3" stdDeviation="4" flood-opacity="0.28"/></filter>')
    d.append('<filter id="glow" x="-60%%" y="-60%%" width="240%%" height="240%%">'
             '<feGaussianBlur stdDeviation="5" result="b"/><feMerge>'
             '<feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/>'
             '</feMerge></filter>')
    d.append('<filter id="sketch"><feTurbulence type="fractalNoise" baseFrequency="0.035" '
             'numOctaves="3" seed="7" result="n"/><feDisplacementMap in="SourceGraphic" '
             'in2="n" scale="3.2" xChannelSelector="R" yChannelSelector="G"/></filter>')
    d.append('<filter id="soft"><feGaussianBlur stdDeviation="1.6"/></filter>')
    d.append('<filter id="grain"><feTurbulence type="fractalNoise" baseFrequency="0.9" '
             'numOctaves="4" result="n"/><feColorMatrix in="n" type="saturate" values="0"/>'
             '<feBlend in="SourceGraphic" mode="multiply"/></filter>')
    if st["node2"]:
        d.append('<linearGradient id="ngrad" x1="0" y1="0" x2="0" y2="1">'
                 '<stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/>'
                 '</linearGradient>' % (st["node"], st["node2"]))
    if "grid" in fx or "rule_grid" in fx:
        step = 40 if "grid" in fx else 80
        op = 0.22 if "grid" in fx else 0.10
        d.append('<pattern id="grid" width="%d" height="%d" patternUnits="userSpaceOnUse">'
                 '<path d="M%d 0V%d M0 %d H%d" stroke="%s" stroke-width="0.7" '
                 'opacity="%s" fill="none"/></pattern>'
                 % (step, step, step, step, step, step, st["panel_str"], op))
    if "halftone" in fx or "benday" in fx or "dabs" in fx:
        c = st["accent"] if "benday" in fx else st["muted"]
        r = 2.6 if "benday" in fx else 1.5
        d.append('<pattern id="dots" width="10" height="10" patternUnits="userSpaceOnUse">'
                 '<circle cx="3" cy="3" r="%s" fill="%s" opacity="0.35"/></pattern>'
                 % (r, c))
    if "scanlines" in fx or "blinds" in fx:
        h = 4 if "scanlines" in fx else 14
        d.append('<pattern id="lines" width="%d" height="%d" patternUnits="userSpaceOnUse">'
                 '<rect width="%d" height="%d" fill="%s" opacity="0.18"/></pattern>'
                 % (h, h, h, max(1, h // 3), st["panel_str"]))
    if "weave" in fx:
        d.append('<pattern id="weave" width="24" height="24" patternUnits="userSpaceOnUse">'
                 '<rect width="24" height="12" fill="%s" opacity="0.30"/>'
                 '<rect y="12" width="12" height="12" fill="%s" opacity="0.30"/></pattern>'
                 % (st["accent"], st["accent2"]))
    if "checker_floor" in fx:
        d.append('<pattern id="check" width="60" height="60" patternUnits="userSpaceOnUse">'
                 '<rect width="30" height="30" fill="%s" opacity="0.25"/>'
                 '<rect x="30" y="30" width="30" height="30" fill="%s" opacity="0.25"/>'
                 '</pattern>' % (st["muted"], st["muted"]))
    if "vignette" in fx:
        d.append('<radialGradient id="vig" cx="0.5" cy="0.45" r="0.78">'
                 '<stop offset="0.55" stop-color="#000" stop-opacity="0"/>'
                 '<stop offset="1" stop-color="#000" stop-opacity="0.55"/>'
                 '</radialGradient>')
    if "horizon" in fx:
        d.append('<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">'
                 '<stop offset="0" stop-color="%s"/><stop offset="0.6" stop-color="%s"/>'
                 '<stop offset="1" stop-color="%s"/></linearGradient>'
                 % (st["bg"], st["accent"], st["accent2"]))
    d.append('</defs>')
    return "".join(d)


def background(st, W, H):
    fx, out = st["fx"], []
    out.append('<rect width="%d" height="%d" fill="%s"/>' % (W, H, st["bg"]))
    if "horizon" in fx:
        out.append('<rect width="%d" height="%d" fill="url(#sky)" opacity="0.28"/>' % (W, H))
        cy = H - 40
        for i in range(1, 14):
            y = cy - (H * 0.5) * (1 - i / 14.0) ** 2
            out.append('<path d="M0 %.1f H%d" stroke="%s" stroke-width="0.8" opacity="0.35"/>'
                       % (y, W, st["accent2"]))
        for i in range(-10, 11):
            out.append('<path d="M%.1f %d L%.1f %d" stroke="%s" stroke-width="0.7" '
                       'opacity="0.28"/>' % (W / 2 + i * 34, H * 0.55, W / 2 + i * 260, H,
                                             st["accent2"]))
        out.append('<circle cx="%d" cy="%d" r="120" fill="%s" opacity="0.18"/>'
                   % (W / 2, H * 0.5, st["accent"]))
    if "grid" in fx or "rule_grid" in fx:
        out.append('<rect width="%d" height="%d" fill="url(#grid)"/>' % (W, H))
    if "checker_floor" in fx:
        out.append('<rect y="%d" width="%d" height="%d" fill="url(#check)"/>'
                   % (H * 0.72, W, H * 0.28))
    if "weave" in fx:
        out.append('<rect width="%d" height="%d" fill="url(#weave)" opacity="0.35"/>' % (W, H))
    if "halftone" in fx or "benday" in fx:
        out.append('<rect width="%d" height="%d" fill="url(#dots)"/>' % (W, H))
    if "scanlines" in fx or "blinds" in fx:
        out.append('<rect width="%d" height="%d" fill="url(#lines)"/>' % (W, H))
    if "sunburst" in fx:
        for i in range(36):
            a = math.radians(i * 10)
            out.append('<path d="M%d %d L%.1f %.1f" stroke="%s" stroke-width="1" '
                       'opacity="0.16"/>' % (W / 2, 0, W / 2 + math.cos(a) * H * 1.4,
                                             math.sin(a) * H * 1.4, st["accent"]))
    if "diagonal" in fx:
        for i in range(-2, 14):
            out.append('<path d="M%d 0 L%d %d" stroke="%s" stroke-width="26" '
                       'opacity="0.07"/>' % (i * 140, i * 140 + H, H, st["accent2"]))
    if "waves" in fx:
        for i in range(9):
            y = 60 + i * (H / 9.0)
            seg = " ".join(["t 240 0"] * 6)
            out.append('<path d="M0 %.0f q 120 -26 240 0 %s" stroke="%s" fill="none" '
                       'stroke-width="1.2" opacity="0.16"/>' % (y, seg, st["panel_str"]))
    if "steps" in fx:
        for i in range(6):
            out.append('<path d="M%d %d h60 v-22 h60 v-22 h60" stroke="%s" fill="none" '
                       'stroke-width="2" opacity="0.14"/>'
                       % (40 + i * 220, H - 40, st["accent"]))
    if "confetti" in fx or "sparkle" in fx:
        r = _rand(11)
        pal = [st["accent"], st["accent2"], st["node_str"], st["muted"]]
        for _ in range(46):
            x, y = r.uniform(0, W), r.uniform(0, H)
            c = r.choice(pal)
            k = r.random()
            if k < 0.33:
                out.append('<circle cx="%.0f" cy="%.0f" r="%.0f" fill="%s" opacity="0.5"/>'
                           % (x, y, r.uniform(3, 8), c))
            elif k < 0.66:
                out.append('<path d="M%.0f %.0f l6 -8 l6 8 l-6 8z" fill="%s" opacity="0.45"/>'
                           % (x, y, c))
            else:
                out.append('<path d="M%.0f %.0f q12 -14 24 0 t24 0" stroke="%s" fill="none" '
                           'stroke-width="3" opacity="0.45"/>' % (x, y, c))
    if "clouds" in fx:
        r = _rand(5)
        for _ in range(7):
            x, y = r.uniform(40, W - 40), r.uniform(30, H * 0.35)
            out.append('<g opacity="0.35" fill="#FFFFFF"><ellipse cx="%.0f" cy="%.0f" rx="46" '
                       'ry="20"/><ellipse cx="%.0f" cy="%.0f" rx="30" ry="24"/></g>'
                       % (x, y, x + 26, y - 8))
    if "eyes" in fx:
        r = _rand(9)
        for _ in range(5):
            x, y = r.uniform(60, W - 60), r.uniform(40, H - 40)
            out.append('<g opacity="0.30"><ellipse cx="%.0f" cy="%.0f" rx="26" ry="14" '
                       'fill="none" stroke="%s" stroke-width="2"/><circle cx="%.0f" cy="%.0f" '
                       'r="7" fill="%s"/></g>' % (x, y, st["node_str"], x, y, st["accent"]))
    if "vines" in fx or "filigree" in fx:
        r = _rand(13)
        for _ in range(10):
            x, y = r.uniform(0, W), r.uniform(0, H)
            out.append('<path d="M%.0f %.0f c 30 -40 70 -40 100 0 c -30 40 -70 40 -100 0" '
                       'stroke="%s" fill="none" stroke-width="1.4" opacity="0.30"/>'
                       % (x, y, st["accent"]))
    if "concrete" in fx or "noise" in fx or "smudge" in fx:
        out.append('<rect width="%d" height="%d" filter="url(#grain)" fill="%s" '
                   'opacity="0.10"/>' % (W, H, st["muted"]))
    return "".join(out)


def foreground(st, W, H):
    out = []
    if "vignette" in st["fx"]:
        out.append('<rect width="%d" height="%d" fill="url(#vig)"/>' % (W, H))
    return "".join(out)


def node_shape(st, nd):
    """One node: frame, decorations, icon, labels."""
    x, y, w, h = nd["_x"], nd["_y"], nd["_w"], nd["_h"]
    fx = st["fx"]
    fill = "url(#ngrad)" if st["node2"] else st["node"]
    r = st["radius"]
    filt = ""
    if "glow" in fx:
        filt = ' filter="url(#glow)"'
    elif "shadow" in fx:
        filt = ' filter="url(#shadow)"'
    elif "sketch" in fx:
        filt = ' filter="url(#sketch)"'
    elif "blur" in fx:
        filt = ' filter="url(#soft)"'
    o = ['<g%s>' % (' transform="rotate(-1.2 %d %d)"' % (x + w / 2, y + h / 2)
                    if "skew" in fx else "")]
    o.append('<rect x="%d" y="%d" width="%d" height="%d" rx="%s" fill="%s" stroke="%s" '
             'stroke-width="%s"%s/>' % (x, y, w, h, r, fill, st["node_str"], st["stroke_w"], filt))
    if "double_rule" in fx:
        o.append('<rect x="%d" y="%d" width="%d" height="%d" rx="%s" fill="none" stroke="%s" '
                 'stroke-width="1" opacity="0.75"/>' % (x + 6, y + 6, w - 12, h - 12, max(0, r - 3),
                                                        st["accent"]))
    if "accent_bar" in fx:
        o.append('<rect x="%d" y="%d" width="5" height="%d" fill="%s"/>'
                 % (x, y, h, st["accent"]))
    if "titlebar" in fx:
        o.append('<rect x="%d" y="%d" width="%d" height="18" fill="%s"/>'
                 % (x + 2, y + 2, w - 4, st["accent"]))
    if "bevel" in fx:
        o.append('<path d="M%d %dH%dV%d" stroke="#FFFFFF" opacity="0.7" fill="none" '
                 'stroke-width="2"/>' % (x + 2, y + h - 2, x + 2, y + 2))
        o.append('<path d="M%d %dH%dV%d" stroke="#000000" opacity="0.45" fill="none" '
                 'stroke-width="2"/>' % (x + w - 2, y + 2, x + w - 2, y + h - 2))
    if "gloss" in fx:
        o.append('<path d="M%d %d h%d a%s %s 0 0 1 %s %s v%d q%d 14 -%d 14 h-%d q-%d 0 -%d -14z" '
                 'fill="#FFFFFF" opacity="0.28"/>'
                 % (x + 4, y + 6, w - 8 - r, r, r, 0, 0, h * 0.28, 0, 0, w - 8, 0, 0))
    if "studs" in fx:
        for i in range(3):
            o.append('<circle cx="%d" cy="%d" r="7" fill="%s" opacity="0.55" stroke="%s"/>'
                     % (x + 34 + i * 40, y + 12, st["node"], st["node_str"]))
    if "traffic" in fx:
        for i, c in enumerate(["#FF5F57", "#FEBC2E", "#28C840"]):
            o.append('<circle cx="%d" cy="%d" r="4" fill="%s"/>' % (x + 14 + i * 13, y + 14, c))
    if "blush" in fx:
        o.append('<ellipse cx="%d" cy="%d" rx="9" ry="5" fill="%s" opacity="0.45"/>'
                 % (x + 22, y + h - 20, st["accent"]))
        o.append('<ellipse cx="%d" cy="%d" rx="9" ry="5" fill="%s" opacity="0.45"/>'
                 % (x + w - 22, y + h - 20, st["accent"]))
    if "melt" in fx:
        o.append('<path d="M%d %d q10 34 20 0" stroke="%s" fill="none" stroke-width="%s" '
                 'opacity="0.8"/>' % (x + w * 0.3, y + h, st["node_str"], st["stroke_w"]))
    if "facets" in fx:
        o.append('<path d="M%d %d L%d %d L%d %d Z" fill="%s" opacity="0.22"/>'
                 % (x, y, x + w * 0.55, y, x, y + h, st["accent"]))
    if "leading" in fx:
        o.append('<path d="M%d %d L%d %d M%d %d L%d %d" stroke="%s" stroke-width="4" '
                 'opacity="0.9"/>' % (x + w * 0.5, y, x + w * 0.5, y + h, x, y + h * 0.5,
                                      x + w, y + h * 0.5, st["node_str"]))

    g = glyphs.get(nd.get("icon"))
    tx = x + 18
    label_x = x + 18
    if g:
        o.append('<g transform="translate(%d,%d) scale(1.15)">%s</g>'
                 % (tx, y + h / 2 - 14, g(st["accent"])))
        label_x = x + 52
    lab = str(nd["label"])
    fs = 14 if len(lab) <= 24 else (12.5 if len(lab) <= 30 else 11.5)
    o.append('<text x="%d" y="%d" font-family="%s" font-size="%s" font-weight="600" '
             'fill="%s">%s</text>'
             % (label_x, y + h / 2 - 2, st["font"], fs, st["text"], esc(_clip(lab, 34))))
    if nd.get("sub"):
        o.append('<text x="%d" y="%d" font-family="%s" font-size="11" fill="%s">%s</text>'
                 % (label_x, y + h / 2 + 16, st["font"], st["muted"], esc(_clip(nd["sub"], 32))))
    if nd.get("badge"):
        o.append('<rect x="%d" y="%d" width="%d" height="18" rx="9" fill="%s" opacity="0.85"/>'
                 % (x + w - 16 - 9 * len(str(nd["badge"])), y + 10,
                    9 * len(str(nd["badge"])) + 8, st["accent"]))
        o.append('<text x="%d" y="%d" font-family="%s" font-size="10" fill="%s" '
                 'text-anchor="end">%s</text>' % (x + w - 12, y + 23, st["font"], st["bg"],
                                                  esc(nd["badge"])))
    o.append('</g>')
    return "".join(o)


def _clip(s, n):
    s = str(s)
    return s if len(s) <= n else s[: n - 1] + "\u2026"


def tier_shape(st, t):
    x, y, w, h = t["_x"], t["_y"], t["_w"], t["_h"]
    o = ['<rect x="%d" y="%d" width="%d" height="%d" rx="%s" fill="%s" stroke="%s" '
         'stroke-width="%s" opacity="0.92" stroke-dasharray="%s"/>'
         % (x, y, w, h, max(0, st["radius"]), st["panel"], st["panel_str"],
            max(1, st["stroke_w"] - 0.5), "8 6" if st["radius"] == 0 else "")]
    if t.get("label"):
        o.append('<text x="%d" y="%d" font-family="%s" font-size="15" font-weight="700" '
                 'letter-spacing="1.4" fill="%s">%s</text>'
                 % (x + 20, y + 32, st["font"], st["accent"], esc(t["label"].upper())))
    if t.get("note"):
        o.append('<text x="%d" y="%d" font-family="%s" font-size="11" fill="%s" '
                 'text-anchor="end">%s</text>'
                 % (x + w - 18, y + 30, st["font"], st["muted"], esc(t["note"])))
    return "".join(o)


def edge_path(st, a, b, kind="solid", off=0):
    ax, ay = a["_x"] + a["_w"] / 2, a["_y"] + a["_h"]
    bx, by = b["_x"] + b["_w"] / 2, b["_y"]
    if a["_tier"] == b["_tier"]:
        if a["_x"] < b["_x"]:
            ax, ay = a["_x"] + a["_w"], a["_y"] + a["_h"] / 2
            bx, by = b["_x"], b["_y"] + b["_h"] / 2
        else:
            ax, ay = a["_x"], a["_y"] + a["_h"] / 2
            bx, by = b["_x"] + b["_w"], b["_y"] + b["_h"] / 2
        d = "M%.0f %.0f H%.0f" % (ax, ay, bx)
        lateral = True
    elif a["_tier"] > b["_tier"]:
        ax, ay = a["_x"] + a["_w"] / 2, a["_y"]
        bx, by = b["_x"] + b["_w"] / 2, b["_y"] + b["_h"]
        my = (ay + by) / 2 + off
        d = "M%.0f %.0f V%.0f H%.0f V%.0f" % (ax, ay, my, bx, by)
        lateral = False
    else:
        my = (ay + by) / 2 + off
        d = "M%.0f %.0f V%.0f H%.0f V%.0f" % (ax, ay, my, bx, by)
        lateral = False
    dash = ' stroke-dasharray="7 5"' if kind == "dashed" else (
        ' stroke-dasharray="10 6"' if kind == "flow" else (
            ' stroke-dasharray="%s"' % st["dash"] if st["dash"] else ""))
    anim = ('<animate attributeName="stroke-dashoffset" from="32" to="0" dur="1.1s" '
            'repeatCount="indefinite"/>') if kind == "flow" else ""
    glow = ' filter="url(#glow)"' if "glow" in st["fx"] else ""
    return ('<path d="%s" fill="none" stroke="%s" stroke-width="%s"%s marker-end="url(#arrow)"%s>'
            '%s</path>' % (d, st["edge"], max(1.4, st["stroke_w"]), dash, glow, anim),
            (ax + bx) / 2, (ay + by) / 2 if lateral else (ay + by) / 2 + off, lateral)


def render_svg(spec, style_key):
    st = STYLES[style_key]
    W, H = spec["_w"], spec["_h"]
    idx = spec["_index"]
    o = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
         'font-family="%s">' % (W, H, W, H, st["font"])]
    o.append(defs(st, W, H))
    o.append(background(st, W, H))

    if spec.get("title"):
        ty = spec["_title_y"]
        if st["title_fx"] == "banner":
            o.append('<rect x="%d" y="%d" width="%d" height="4" fill="%s"/>'
                     % (MARGIN, ty + 14, W - 2 * MARGIN, st["accent"]))
        o.append('<text x="%d" y="%d" font-size="30" font-weight="700" fill="%s">%s</text>'
                 % (MARGIN, ty, st["text"], esc(spec["title"])))
        if spec.get("subtitle"):
            o.append('<text x="%d" y="%d" font-size="13" fill="%s">%s</text>'
                     % (MARGIN, ty + 38, st["muted"], esc(spec["subtitle"])))

    for t in spec.get("tiers", []):
        o.append(tier_shape(st, t))
    seen = {}
    for e in spec.get("edges", []):
        a, b = idx.get(e.get("from")), idx.get(e.get("to"))
        if not a or not b:
            continue
        band = (min(a["_tier"], b["_tier"]), max(a["_tier"], b["_tier"]))
        off = (seen.get(band, 0) % 3 - 1) * 13
        seen[band] = seen.get(band, 0) + 1
        path, mx, my, lateral = edge_path(st, a, b, e.get("kind", "solid"), off)
        o.append(path)
        if e.get("label"):
            lab = esc(_clip(e["label"], 20))
            fs = 10 if lateral else 11
            ly = my - 8 if lateral else my
            if not lateral:
                o.append('<rect x="%.0f" y="%.0f" width="%d" height="18" rx="4" fill="%s" '
                         'opacity="0.88"/>' % (mx - 4.6 * len(lab), ly - 13,
                                               int(9.2 * len(lab)), st["bg"]))
            o.append('<text x="%.0f" y="%.0f" font-size="%d" fill="%s" text-anchor="middle">'
                     '%s</text>' % (mx, ly, fs, st["muted"], lab))
    for t in spec.get("tiers", []):
        for nd in t.get("nodes", []):
            o.append(node_shape(st, nd))

    legend = spec.get("legend") or []
    if legend:
        ly = H - MARGIN - 26
        o.append('<text x="%d" y="%d" font-size="11" font-weight="700" fill="%s" '
                 'letter-spacing="1.2">LEGEND</text>' % (MARGIN, ly - 18, st["muted"]))
        for i, item in enumerate(legend):
            lx = MARGIN + i * 190
            o.append('<rect x="%d" y="%d" width="14" height="14" rx="3" fill="%s"/>'
                     % (lx, ly - 11, item.get("color", st["accent"])))
            o.append('<text x="%d" y="%d" font-size="12" fill="%s">%s</text>'
                     % (lx + 22, ly, st["text"], esc(_clip(item.get("label", ""), 20))))
    o.append(foreground(st, W, H))
    o.append('</svg>')
    return "".join(o)


# ------------------------------------------------------------------- draw.io
def aws_res(icon):
    if isinstance(icon, str) and icon.startswith("aws:"):
        return AWS_RES.get(icon.split(":", 1)[1].lower().replace("-", "").replace("_", ""))
    return None


def dio_style(st, kind, nd=None):
    common = "html=1;whiteSpace=wrap;fontFamily=%s;fontColor=%s;" % (
        st["font"].split(",")[0], st["text"])
    if kind == "tier":
        return (common + "rounded=%d;arcSize=8;fillColor=%s;strokeColor=%s;strokeWidth=1;"
                "dashed=%d;verticalAlign=top;align=left;spacingLeft=12;spacingTop=6;"
                "fontStyle=1;fontSize=13;fontColor=%s;opacity=90;"
                % (1 if st["radius"] else 0, st["panel"], st["panel_str"],
                   1 if st["radius"] == 0 else 0, st["accent"]))
    if kind == "edge":
        return ("edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;strokeColor=%s;strokeWidth=2;"
                "fontColor=%s;fontSize=10;endArrow=blockThin;endFill=1;" % (st["edge"], st["muted"]))
    grad = ("gradientColor=%s;gradientDirection=north;" % st["node2"]) if st["node2"] else ""
    shadow = "shadow=1;" if ("shadow" in st["fx"] or "glow" in st["fx"]) else ""
    sketch = "sketch=1;curveFitting=1;jiggle=2;" if "sketch" in st["fx"] else ""
    return (common + "rounded=%d;arcSize=%d;fillColor=%s;%sstrokeColor=%s;strokeWidth=%s;"
            "%s%sfontSize=12;fontStyle=1;verticalAlign=middle;"
            % (1 if st["radius"] else 0, min(50, st["radius"] * 2), st["node"], grad,
               st["node_str"], st["stroke_w"], shadow, sketch))


def render_drawio(spec, style_key):
    st = STYLES[style_key]
    mxfile = ET.Element("mxfile", host="app.diagrams.net", agent="claude-architecture-diagrams",
                        version="24.0.0")
    dia = ET.SubElement(mxfile, "diagram", name=spec.get("title", "Architecture")[:40] or "Diagram")
    model = ET.SubElement(dia, "mxGraphModel", dx="1400", dy="900", grid="0", gridSize="10",
                          guides="1", tooltips="1", connect="1", arrows="1", fold="1",
                          page="1", pageScale="1", pageWidth=str(spec["_w"]),
                          pageHeight=str(spec["_h"]), math="0", shadow="0",
                          background=st["bg"])
    root = ET.SubElement(model, "root")
    ET.SubElement(root, "mxCell", id="0")
    ET.SubElement(root, "mxCell", id="1", parent="0")

    def cell(cid, value, style, x, y, w, h, vertex=True):
        c = ET.SubElement(root, "mxCell", id=cid, value=value, style=style, vertex="1",
                          parent="1")
        ET.SubElement(c, "mxGeometry", x=str(int(x)), y=str(int(y)), width=str(int(w)),
                      height=str(int(h)), attrib={"as": "geometry"})
        return c

    if spec.get("title"):
        cell("title", spec["title"], "text;html=1;fontSize=26;fontStyle=1;fontColor=%s;"
             "align=left;verticalAlign=middle;fontFamily=%s;"
             % (st["text"], st["font"].split(",")[0]), MARGIN, MARGIN - 4, spec["_w"] - 2 * MARGIN,
             40)
        if spec.get("subtitle"):
            cell("subtitle", spec["subtitle"], "text;html=1;fontSize=12;fontColor=%s;align=left;"
                 % st["muted"], MARGIN, MARGIN + 34, spec["_w"] - 2 * MARGIN, 20)

    for t in spec.get("tiers", []):
        cell("tier_%d" % t["_i"], t.get("label", ""), dio_style(st, "tier"),
             t["_x"], t["_y"], t["_w"], t["_h"])
    for t in spec.get("tiers", []):
        for nd in t.get("nodes", []):
            label = nd["label"]
            if nd.get("sub"):
                label = "%s<br><font style='font-size:10px;color:%s'>%s</font>" % (
                    label, st["muted"], nd["sub"])
            res = aws_res(nd.get("icon"))
            style = dio_style(st, "node", nd)
            if res:
                style += "align=left;spacingLeft=72;"
            cell("n_%s" % nd["id"], label, style,
                 nd["_x"], nd["_y"], nd["_w"], nd["_h"])
            if res:
                cell("ic_%s" % nd["id"], "",
                     "sketch=0;outlineConnect=0;fontColor=%s;gradientColor=none;"
                     "fillColor=%s;strokeColor=none;dashed=0;verticalLabelPosition=bottom;"
                     "verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;"
                     "aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.%s;"
                     % (st["text"], st["accent"], res),
                     nd["_x"] + 12, nd["_y"] + (nd["_h"] - 52) / 2, 52, 52)
    for i, e in enumerate(spec.get("edges", [])):
        if e.get("from") not in spec["_index"] or e.get("to") not in spec["_index"]:
            continue
        style = dio_style(st, "edge")
        if e.get("kind") == "dashed":
            style += "dashed=1;"
        if e.get("kind") == "flow":
            style += "dashed=1;flowAnimation=1;"
        c = ET.SubElement(root, "mxCell", id="e_%d" % i, value=e.get("label", ""), style=style,
                          edge="1", parent="1", source="n_%s" % e["from"], target="n_%s" % e["to"])
        ET.SubElement(c, "mxGeometry", relative="1", attrib={"as": "geometry"})

    return '<?xml version="1.0" encoding="UTF-8"?>\n' + \
        ET.tostring(mxfile, encoding="unicode")


# ---------------------------------------------------------------------- html
PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport"
content="width=device-width,initial-scale=1"><title>{title}</title>
<style>
:root{{color-scheme:dark light}}
body{{margin:0;background:{bg};color:{text};font-family:{font};
display:flex;flex-direction:column;align-items:center;padding:32px 16px}}
header{{width:100%;max-width:1400px;margin-bottom:18px}}
h1{{font-size:20px;margin:0 0 4px}}
p.meta{{margin:0;font-size:12px;color:{muted}}}
figure{{margin:0;width:100%;max-width:1400px}}
svg{{width:100%;height:auto;display:block;border-radius:10px}}
footer{{margin-top:22px;font-size:11px;color:{muted}}}
</style></head><body>
<header><h1>{title}</h1><p class="meta">{sub}</p></header>
<figure>{svg}</figure>
<footer>{style} style &middot; generated from spec, rendered offline</footer>
</body></html>"""

GALLERY = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport"
content="width=device-width,initial-scale=1"><title>{title} &mdash; style gallery</title>
<style>
body{{margin:0;background:#12141a;color:#e8eaf0;font-family:Helvetica,Arial,sans-serif;
padding:36px 20px}}
h1{{font-size:24px;margin:0 0 6px}}
p.meta{{color:#98a0b3;font-size:13px;margin:0 0 28px}}
.grid{{display:grid;gap:26px;grid-template-columns:repeat(auto-fit,minmax(460px,1fr));
max-width:1600px;margin:0 auto}}
.card{{background:#1a1d26;border:1px solid #2a2f3d;border-radius:12px;overflow:hidden}}
.card h2{{font-size:13px;letter-spacing:1.4px;text-transform:uppercase;margin:0;
padding:12px 16px;color:#98a0b3;border-bottom:1px solid #2a2f3d}}
.card svg{{width:100%;height:auto;display:block}}
</style></head><body>
<h1>{title}</h1><p class="meta">{n} styles &middot; same architecture spec</p>
<div class="grid">{cards}</div></body></html>"""


def render_html(spec, style_key, svg):
    st = STYLES[style_key]
    return PAGE.format(title=esc(spec.get("title", "Architecture diagram")),
                       sub=esc(spec.get("subtitle", "")), bg=st["bg"], text=st["text"],
                       muted=st["muted"], font=st["font"], svg=svg, style=style_key)


def render_gallery(spec, pairs):
    cards = "".join('<div class="card"><h2>%s</h2>%s</div>' % (k, s) for k, s in pairs)
    return GALLERY.format(title=esc(spec.get("title", "Architecture diagram")),
                          n=len(pairs), cards=cards)


# ---------------------------------------------------------------------- main
def write_outputs(spec, style_key, outdir, stem, png=True):
    svg = render_svg(spec, style_key)
    paths = {}
    base = os.path.join(outdir, "%s-%s" % (stem, style_key))
    with open(base + ".drawio", "w") as f:
        f.write(render_drawio(spec, style_key))
    paths["drawio"] = base + ".drawio"
    with open(base + ".svg", "w") as f:
        f.write(svg)
    paths["svg"] = base + ".svg"
    with open(base + ".html", "w") as f:
        f.write(render_html(spec, style_key, svg))
    paths["html"] = base + ".html"
    if png:
        try:
            import cairosvg
            cairosvg.svg2png(bytestring=svg.encode(), write_to=base + ".png",
                             output_width=spec["_w"] * 2)
            paths["png"] = base + ".png"
        except Exception as exc:  # noqa: BLE001
            print("PNG export skipped (%s)" % exc, file=sys.stderr)
    return paths, svg


def validate(spec):
    """Catch the failures that produce a broken or misleading diagram."""
    out, ids = [], set()
    for t in spec.get("tiers", []):
        if not t.get("nodes"):
            out.append("tier '%s' has no nodes" % t.get("label", "?"))
        for nd in t.get("nodes", []):
            if nd.get("id") in ids:
                out.append("duplicate node id '%s'" % nd.get("id"))
            ids.add(nd.get("id"))
            if not nd.get("label"):
                out.append("node '%s' has no label" % nd.get("id"))
    for e in spec.get("edges", []):
        for end in ("from", "to"):
            if e.get(end) not in ids:
                out.append("edge references unknown node '%s'" % e.get(end))
    connected = {x for e in spec.get("edges", []) for x in (e.get("from"), e.get("to"))}
    for orphan in sorted(ids - connected):
        out.append("node '%s' has no connections" % orphan)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec", nargs="?", help="path to spec JSON")
    ap.add_argument("--outdir", default="out")
    ap.add_argument("--styles", help="comma separated style keys (overrides spec.style)")
    ap.add_argument("--stem", default=None)
    ap.add_argument("--no-png", action="store_true")
    ap.add_argument("--list-styles", action="store_true")
    a = ap.parse_args()

    if a.list_styles:
        for group, keys in GROUPS.items():
            print("\n%s" % group)
            for k in keys:
                print("  %-16s %s" % (k, ", ".join(STYLES[k]["fx"]) or "flat"))
        return
    if not a.spec:
        ap.error("spec is required")

    with open(a.spec) as f:
        spec = json.load(f)
    problems = validate(spec)
    if problems:
        print("\n".join("spec problem: " + p for p in problems), file=sys.stderr)
        if any(p.startswith("duplicate") for p in problems):
            sys.exit(1)
    keys = [resolve(s)[0] for s in (a.styles.split(",") if a.styles
                                    else [spec.get("style", "corporate")])]
    os.makedirs(a.outdir, exist_ok=True)
    stem = a.stem or os.path.splitext(os.path.basename(a.spec))[0]

    pairs, allpaths = [], []
    for k in keys:
        layout(spec)
        paths, svg = write_outputs(spec, k, a.outdir, stem, png=not a.no_png)
        pairs.append((k, svg))
        allpaths.extend(paths.values())
        print("%-14s -> %s" % (k, ", ".join(os.path.basename(p) for p in paths.values())))
    if len(pairs) > 1:
        g = os.path.join(a.outdir, "%s-gallery.html" % stem)
        with open(g, "w") as f:
            f.write(render_gallery(spec, pairs))
        print("gallery       -> %s" % os.path.basename(g))


if __name__ == "__main__":
    main()
