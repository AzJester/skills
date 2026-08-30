"""Style catalog. Each profile is a flat dict consumed by both emitters.

Keys
----
bg          canvas background
panel       tier/group container fill
panel_str   tier/group container stroke
node        node fill
node2       optional gradient end fill (None = flat)
node_str    node stroke
accent      accent bar / highlight
accent2     secondary accent
text        primary label colour
muted       sublabel colour
edge        connector colour
font        font family string
radius      corner radius in px
stroke_w    stroke width in px
dash        connector dash pattern ("" = solid)
fx          list of effect tokens (see render.py EFFECTS)
title_fx    "bar" | "tab" | "plain" | "banner"
"""

MONO = "Courier New, monospace"
SANS = "Helvetica, Arial, sans-serif"
SERIF = "Georgia, Times New Roman, serif"

STYLES = {
    # ---------------------------------------------------------- professional
    "aws-reinvent": dict(
        bg="#161E2D", panel="#1E2938", panel_str="#37475A", node="#232F3E", node2=None,
        node_str="#FF9900", accent="#FF9900", accent2="#00A1C9", text="#FFFFFF",
        muted="#B0BEC5", edge="#FF9900", font=SANS, radius=4, stroke_w=2, dash="",
        fx=["shadow", "accent_bar"], title_fx="bar"),
    "corporate": dict(
        bg="#F4F7FB", panel="#E8EFF7", panel_str="#B9CBDF", node="#FFFFFF", node2="#DCE9F7",
        node_str="#1F4E79", accent="#1F4E79", accent2="#2E86C1", text="#1B2A38",
        muted="#5A6B7B", edge="#1F4E79", font=SANS, radius=6, stroke_w=1.5, dash="",
        fx=["gradient", "shadow"], title_fx="bar"),
    "material": dict(
        bg="#FAFAFA", panel="#FFFFFF", panel_str="#E0E0E0", node="#FFFFFF", node2=None,
        node_str="#E0E0E0", accent="#6200EE", accent2="#03DAC6", text="#212121",
        muted="#757575", edge="#9E9E9E", font="Roboto, Helvetica, sans-serif", radius=4,
        stroke_w=1, dash="", fx=["shadow", "accent_bar"], title_fx="plain"),
    "minimal-flat": dict(
        bg="#FFFFFF", panel="#F7F7F7", panel_str="#E5E5E5", node="#EFEFEF", node2=None,
        node_str="#2B2B2B", accent="#E84A5F", accent2="#2A9D8F", text="#1A1A1A",
        muted="#6E6E6E", edge="#2B2B2B", font=SANS, radius=0, stroke_w=1.5, dash="",
        fx=[], title_fx="plain"),
    "swiss": dict(
        bg="#FFFFFF", panel="#FFFFFF", panel_str="#000000", node="#FFFFFF", node2=None,
        node_str="#000000", accent="#E4002B", accent2="#000000", text="#000000",
        muted="#555555", edge="#000000", font="Helvetica, Arial, sans-serif", radius=0,
        stroke_w=2, dash="", fx=["rule_grid"], title_fx="banner"),
    "blueprint": dict(
        bg="#0B3D66", panel="#0E4877", panel_str="#8FC6F0", node="#0B3D66", node2=None,
        node_str="#DCEEFF", accent="#FFFFFF", accent2="#8FC6F0", text="#EAF4FF",
        muted="#A9CBE8", edge="#DCEEFF", font=MONO, radius=0, stroke_w=1.2, dash="",
        fx=["grid", "ticks"], title_fx="banner"),

    # ------------------------------------------------------------- nostalgia
    "win95": dict(
        bg="#008080", panel="#C0C0C0", panel_str="#808080", node="#C0C0C0", node2=None,
        node_str="#FFFFFF", accent="#000080", accent2="#C0C0C0", text="#000000",
        muted="#404040", edge="#000000", font="MS Sans Serif, Tahoma, sans-serif",
        radius=0, stroke_w=2, dash="", fx=["bevel", "titlebar"], title_fx="tab"),
    "aqua": dict(
        bg="#DCE6F2", panel="#EFF4FA", panel_str="#9FB3CC", node="#F7FAFF", node2="#B7D4F2",
        node_str="#7D9BBF", accent="#2E7CE4", accent2="#FF5F57", text="#12233A",
        muted="#5E7290", edge="#5E7290", font="Lucida Grande, Helvetica, sans-serif",
        radius=14, stroke_w=1, dash="", fx=["gradient", "gloss", "shadow", "traffic"],
        title_fx="plain"),
    "dark-neon": dict(
        bg="#05060A", panel="#0B0F18", panel_str="#1E2A3A", node="#0D1420", node2=None,
        node_str="#00E5FF", accent="#FF2D95", accent2="#00E5FF", text="#E6FBFF",
        muted="#7BA3B5", edge="#FF2D95", font=SANS, radius=8, stroke_w=1.5, dash="",
        fx=["glow"], title_fx="plain"),
    "tron": dict(
        bg="#000000", panel="#02080C", panel_str="#0FF0FC", node="#000508", node2=None,
        node_str="#0FF0FC", accent="#FF4D00", accent2="#0FF0FC", text="#CFFDFF",
        muted="#4FB8C4", edge="#FF4D00", font=MONO, radius=0, stroke_w=1.5, dash="",
        fx=["grid", "glow", "flow"], title_fx="banner"),

    # ---------------------------------------------------------------- elegant
    "art-deco": dict(
        bg="#101014", panel="#17171E", panel_str="#C9A227", node="#1C1C25", node2=None,
        node_str="#C9A227", accent="#E8CE7A", accent2="#C9A227", text="#F3E9C8",
        muted="#9C8C5E", edge="#C9A227", font="Georgia, serif", radius=0, stroke_w=1.5,
        dash="", fx=["sunburst", "double_rule"], title_fx="banner"),
    "art-nouveau": dict(
        bg="#F3EEE2", panel="#EAE2CE", panel_str="#7A6A3F", node="#FAF6EA", node2=None,
        node_str="#4E6B4A", accent="#9C6B3C", accent2="#4E6B4A", text="#33291B",
        muted="#6E6250", edge="#4E6B4A", font=SERIF, radius=24, stroke_w=1.5, dash="",
        fx=["vines", "noise"], title_fx="banner"),
    "stained-glass": dict(
        bg="#0A0A12", panel="#12121F", panel_str="#000000", node="#1B3A8C", node2="#7B1E3A",
        node_str="#000000", accent="#E0A21E", accent2="#1F7A4C", text="#FFF6D8",
        muted="#C8B98A", edge="#000000", font=SERIF, radius=6, stroke_w=6, dash="",
        fx=["gradient", "leading", "glow"], title_fx="banner"),
    "noir": dict(
        bg="#0D0D0D", panel="#151515", panel_str="#8A8A8A", node="#1C1C1C", node2="#000000",
        node_str="#D8D8D8", accent="#FFFFFF", accent2="#8A8A8A", text="#F0F0F0",
        muted="#9A9A9A", edge="#D8D8D8", font="Georgia, serif", radius=0, stroke_w=1.2,
        dash="", fx=["blinds", "gradient", "vignette"], title_fx="banner"),

    # --------------------------------------------------------------- cultural
    "ukiyo-e": dict(
        bg="#EFE3CC", panel="#E3D3B4", panel_str="#2F4858", node="#F6EEDC", node2=None,
        node_str="#2F4858", accent="#C2452D", accent2="#3E6B8A", text="#22303A",
        muted="#6B6353", edge="#2F4858", font=SERIF, radius=2, stroke_w=2, dash="",
        fx=["waves", "noise"], title_fx="banner"),
    "samurai": dict(
        bg="#161314", panel="#1F1A1B", panel_str="#8B0E13", node="#241E1F", node2=None,
        node_str="#8B0E13", accent="#C8102E", accent2="#D9C89E", text="#EFE6D2",
        muted="#9A8E77", edge="#8B0E13", font=SERIF, radius=2, stroke_w=2, dash="",
        fx=["mon", "noise"], title_fx="banner"),
    "kente": dict(
        bg="#101010", panel="#1A1A1A", panel_str="#F4C20D", node="#0F5132", node2="#8B1E1E",
        node_str="#F4C20D", accent="#F4C20D", accent2="#0F5132", text="#FFF8E1",
        muted="#D8C89A", edge="#F4C20D", font=SANS, radius=0, stroke_w=3, dash="",
        fx=["weave", "gradient"], title_fx="banner"),
    "aztec": dict(
        bg="#2B1B12", panel="#3A2418", panel_str="#C77B32", node="#4A2E1D", node2=None,
        node_str="#C77B32", accent="#E0A458", accent2="#2E8B76", text="#F2E3CE",
        muted="#B79877", edge="#C77B32", font=SERIF, radius=0, stroke_w=2.5, dash="",
        fx=["steps", "noise"], title_fx="banner"),
    "constructivist": dict(
        bg="#EDE7DE", panel="#1A1A1A", panel_str="#C8102E", node="#C8102E", node2=None,
        node_str="#1A1A1A", accent="#1A1A1A", accent2="#C8102E", text="#FFFFFF",
        muted="#EDE7DE", edge="#1A1A1A", font="Impact, Haettenschweiler, sans-serif",
        radius=0, stroke_w=3, dash="", fx=["diagonal", "rule_grid"], title_fx="banner"),

    # --------------------------------------------------------------- thematic
    "chalkboard": dict(
        bg="#1E2B22", panel="#243328", panel_str="#DCE6DA", node="#1E2B22", node2=None,
        node_str="#E8EFE6", accent="#F3D27A", accent2="#9FD3C7", text="#F2F6F1",
        muted="#B9C6B6", edge="#E8EFE6", font="Comic Sans MS, Chalkboard, cursive",
        radius=6, stroke_w=2, dash="", fx=["sketch", "noise", "smudge"], title_fx="banner"),
    "newspaper": dict(
        bg="#F2EFE6", panel="#EAE6DA", panel_str="#1A1A1A", node="#FBF9F3", node2=None,
        node_str="#1A1A1A", accent="#1A1A1A", accent2="#8A8A8A", text="#111111",
        muted="#4A4A4A", edge="#1A1A1A", font="Georgia, Times New Roman, serif",
        radius=0, stroke_w=1.5, dash="", fx=["halftone", "double_rule", "noise"],
        title_fx="banner"),
    "comic": dict(
        bg="#FFF3C4", panel="#FFE066", panel_str="#111111", node="#FFFFFF", node2=None,
        node_str="#111111", accent="#E63946", accent2="#2A9D8F", text="#111111",
        muted="#444444", edge="#111111", font="Comic Sans MS, Impact, sans-serif",
        radius=10, stroke_w=4, dash="", fx=["benday", "sketch", "burst"], title_fx="banner"),
    "brutalist": dict(
        bg="#D9D6CF", panel="#C4C0B7", panel_str="#000000", node="#E6E3DC", node2=None,
        node_str="#000000", accent="#000000", accent2="#FF4A00", text="#000000",
        muted="#3A3A3A", edge="#000000", font=MONO, radius=0, stroke_w=5, dash="",
        fx=["concrete"], title_fx="banner"),

    # ----------------------------------------------------------------- gaming
    "minecraft": dict(
        bg="#4A7A3A", panel="#3C5E2E", panel_str="#20301A", node="#8A8A8A", node2=None,
        node_str="#3A3A3A", accent="#C0392B", accent2="#5B8C3E", text="#FFFFFF",
        muted="#DDE6D4", edge="#2B2B2B", font=MONO, radius=0, stroke_w=3,
        dash="", fx=["pixel", "bevel"], title_fx="tab"),
    "lego": dict(
        bg="#F2F2F2", panel="#FFE500", panel_str="#B8A600", node="#D01012", node2=None,
        node_str="#8E0B0C", accent="#0057A6", accent2="#00A651", text="#FFFFFF",
        muted="#F4F4F4", edge="#333333", font=SANS, radius=4, stroke_w=2, dash="",
        fx=["studs", "gloss", "shadow"], title_fx="tab"),
    "pipboy": dict(
        bg="#04160A", panel="#062010", panel_str="#2BE86A", node="#04180B", node2=None,
        node_str="#2BE86A", accent="#8DFFB0", accent2="#2BE86A", text="#8DFFB0",
        muted="#3F9A5C", edge="#2BE86A", font=MONO, radius=2, stroke_w=1.5, dash="",
        fx=["scanlines", "glow", "vignette"], title_fx="banner"),
    "origami": dict(
        bg="#F6F4EF", panel="#ECE7DD", panel_str="#B9AE9B", node="#FFFFFF", node2="#DCD5C7",
        node_str="#9C8F7A", accent="#C25B4E", accent2="#5B7C8D", text="#2E2A24",
        muted="#7B7365", edge="#9C8F7A", font=SANS, radius=0, stroke_w=1, dash="4 3",
        fx=["gradient", "folds", "shadow"], title_fx="plain"),

    # ------------------------------------------------------------------ anime
    "ghibli": dict(
        bg="#DCEBD8", panel="#C9E0C4", panel_str="#6E8E63", node="#FBF7E8", node2="#E7F1DC",
        node_str="#6E8E63", accent="#4A7C59", accent2="#E4A951", text="#33422E",
        muted="#6B7A63", edge="#6E8E63", font=SERIF, radius=18, stroke_w=1.5, dash="",
        fx=["gradient", "sketch", "noise", "clouds"], title_fx="banner"),
    "kawaii": dict(
        bg="#FFF0F6", panel="#FFE0EE", panel_str="#FFB3D1", node="#FFFFFF", node2="#FFE9F3",
        node_str="#FF8FC0", accent="#FF6FA8", accent2="#9AD6F0", text="#5A3A4A",
        muted="#A87C92", edge="#FFB3D1", font="Comic Sans MS, sans-serif", radius=22,
        stroke_w=2, dash="", fx=["gradient", "sparkle", "blush", "shadow"], title_fx="plain"),

    # ------------------------------------------------------------- classical
    "impressionist": dict(
        bg="#E8E3D3", panel="#DDE4D3", panel_str="#8FA37E", node="#F3EFE0", node2="#CDDCC6",
        node_str="#8FA37E", accent="#6C8EBF", accent2="#D4A06A", text="#3B4232",
        muted="#6F7A63", edge="#8FA37E", font=SERIF, radius=20, stroke_w=1, dash="",
        fx=["gradient", "dabs", "blur"], title_fx="plain"),
    "baroque": dict(
        bg="#1B1109", panel="#2A1B0F", panel_str="#C9A227", node="#3A2614", node2="#1B1109",
        node_str="#C9A227", accent="#E8CE7A", accent2="#7A1F1F", text="#F5E7C6",
        muted="#B79A63", edge="#C9A227", font=SERIF, radius=10, stroke_w=2, dash="",
        fx=["gradient", "filigree", "noise", "vignette"], title_fx="banner"),

    # ------------------------------------------------------------------ retro
    "vaporwave": dict(
        bg="#1B0B33", panel="#2A0F4A", panel_str="#FF6AD5", node="#3B1263", node2="#8A2BE2",
        node_str="#26F0F1", accent="#FF6AD5", accent2="#26F0F1", text="#F6E7FF",
        muted="#C09BE8", edge="#26F0F1", font="Georgia, serif", radius=4, stroke_w=2,
        dash="", fx=["horizon", "gradient", "glow", "sparkle"], title_fx="banner"),
    "synthwave": dict(
        bg="#0B0524", panel="#150A3A", panel_str="#FF2D95", node="#1B0D4A", node2="#2B1470",
        node_str="#00E5FF", accent="#FF2D95", accent2="#FFD319", text="#F2ECFF",
        muted="#A08BD6", edge="#FF2D95", font=SANS, radius=2, stroke_w=2, dash="",
        fx=["horizon", "grid", "glow", "gradient", "flow"], title_fx="banner"),
    "memphis": dict(
        bg="#FDF6E3", panel="#FFFFFF", panel_str="#111111", node="#00C2CB", node2=None,
        node_str="#111111", accent="#FF4E6A", accent2="#FFD23F", text="#111111",
        muted="#444444", edge="#111111", font=SANS, radius=0, stroke_w=3, dash="",
        fx=["confetti", "squiggle"], title_fx="banner"),

    # --------------------------------------------------------------- abstract
    "cubist": dict(
        bg="#D9CDB8", panel="#C4B49A", panel_str="#3A3129", node="#B08968", node2="#7F6A55",
        node_str="#2F2820", accent="#8C5E3C", accent2="#5B6E62", text="#241E17",
        muted="#5A4E42", edge="#2F2820", font=SANS, radius=0, stroke_w=2, dash="",
        fx=["facets", "gradient", "skew"], title_fx="banner"),
    "surrealist": dict(
        bg="#E7C79B", panel="#D7B183", panel_str="#3E2C1C", node="#F0DCC0", node2="#B98C5E",
        node_str="#3E2C1C", accent="#2E5E7E", accent2="#A33B2A", text="#2A1F14",
        muted="#5E4A34", edge="#3E2C1C", font=SERIF, radius=30, stroke_w=1.5, dash="",
        fx=["checker_floor", "melt", "gradient", "eyes", "vignette"], title_fx="banner"),
}

ALIASES = {
    "aws": "aws-reinvent", "reinvent": "aws-reinvent", "enterprise": "corporate",
    "flat": "minimal-flat", "windows95": "win95", "win98": "win95", "macos": "aqua",
    "neon": "dark-neon", "deco": "art-deco", "nouveau": "art-nouveau",
    "japanese": "ukiyo-e", "soviet": "constructivist", "propaganda": "constructivist",
    "fallout": "pipboy", "studio-ghibli": "ghibli", "monet": "impressionist",
    "cyberpunk": "synthwave", "dali": "surrealist", "picasso": "cubist",
    "chalk": "chalkboard", "print": "newspaper",
}

GROUPS = {
    "Professional & clean": ["aws-reinvent", "corporate", "material", "minimal-flat",
                             "swiss", "blueprint"],
    "Tech nostalgia": ["win95", "aqua", "dark-neon", "tron"],
    "Elegant artistic": ["art-deco", "art-nouveau", "stained-glass", "noir"],
    "Cultural heritage": ["ukiyo-e", "samurai", "kente", "aztec", "constructivist"],
    "Thematic & playful": ["chalkboard", "newspaper", "comic", "brutalist"],
    "Gaming & pop culture": ["minecraft", "lego", "pipboy", "origami"],
    "Anime & cute": ["ghibli", "kawaii"],
    "Classical art": ["impressionist", "baroque"],
    "Retro aesthetic": ["vaporwave", "synthwave", "memphis"],
    "Abstract & surreal": ["cubist", "surrealist"],
}


def resolve(name):
    key = (name or "corporate").strip().lower().replace("_", "-").replace(" ", "-")
    key = ALIASES.get(key, key)
    if key not in STYLES:
        raise SystemExit(
            "Unknown style '%s'. Available: %s" % (name, ", ".join(sorted(STYLES)))
        )
    return key, STYLES[key]
