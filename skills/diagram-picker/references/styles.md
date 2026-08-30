# Style catalog

Style is a rendering treatment. It changes how a diagram looks and never what it says. Every style below draws the same nodes and the same edges as Technical clean would; only the paint differs.

Each entry gives concrete direction because "make it look like a blueprint" is not enough to act on. Use the hex values and line treatments as written unless the user says otherwise.

A style earns its place when it helps a reader: a hand-drawn treatment tells a room that a design is still up for debate, and that saves an argument. A style fails when it costs legibility. If a treatment makes labels hard to read or forces a component off the canvas, abandon it and say why.

---

## Technical clean

The default. Semantic color doing real work, nothing decorative.

- Fills: `#4299e1` inputs, `#ed8936` processing, `#9f7aea` services, `#48bb78` outputs, `#718096` tooling. Strokes one shade darker.
- Type: system sans. 16px node titles, 10–11px detail.
- Lines: 2–3px solid, arrowheads on every edge, right angles or straight diagonals.
- Ground: white or `#f7fafc`.

Good for anything. Reach for it whenever the diagram has to be correct more than it has to be interesting.

---

## Blueprint

Drafting-table treatment. Reads as considered and slightly formal.

- Ground: `#0d3b66` deep blue, flat.
- Everything else: `#e8f1f8` near-white. Lines 1.5px, no fills — boxes are outlines only.
- Grid: `#ffffff` at 8% opacity, 40px pitch, behind everything.
- Type: monospace, letter-spaced, uppercase for titles.
- Add drafting furniture: dimension ticks on major spans, a title block bottom-right with the diagram name and date.

Good for structure diagrams that want to feel like a specification. Poor for anything with more than two color-coded categories, since it is monochrome by construction.

---

## Hand-drawn

Deliberately provisional. The most *useful* non-default style.

- Strokes: 2–3px, `#2d3748`, with intentional wobble — offset path points 1–3px so no line is truly straight and no rectangle truly closes.
- Fills: pale washes at 15–25% opacity that overshoot their outlines slightly, like a marker bleeding.
- Type: a handwriting-adjacent face with a real fallback (`'Comic Neue', 'Segoe Print', cursive`), or system sans at a slight rotation.
- Arrowheads: open V strokes, not filled triangles.

Good for design reviews and early thinking: it signals "argue with this" in a way a crisp diagram cannot. Bad for documentation, where it reads as unfinished.

---

## Terminal

Phosphor on black. Compact and a little severe.

- Ground: `#0c0c0c`. Foreground `#33ff66`, secondary `#1a8f3a`, alert `#ff5555`.
- Type: monospace throughout, one size, uppercase titles.
- Boxes: drawn from box-drawing characters or 1px rectangles with no radius.
- Edges: straight runs with `>` or `v` terminators rather than SVG markers.
- Optional: a scanline overlay, 2px repeating linear gradient at 4% opacity.

Good for CLI tools, pipelines, and anything where the audience lives in a terminal. Bad for executives.

---

## Subway map

Transit-diagram geometry. Genuinely clarifying for flows with several parallel paths.

- Lines run at 0°, 45°, or 90° only. Never an arbitrary angle. Corners are rounded at a fixed radius.
- Each path gets its own saturated color and holds it end to end.
- Nodes: white circles with a dark ring. Interchanges (a node on two or more paths) get a larger double ring.
- Type: system sans, labels set horizontally even where the line is diagonal.
- Ground: white or a very pale warm gray.

Good for request flows and multi-path pipelines where the question is "which route does this take". Bad for hierarchy — it flattens everything into a network.

---

## Isometric

2.5D blocks on a 30° axis. Impressive, expensive, easy to get wrong.

- Project on a true isometric grid: 30° from horizontal on both axes.
- Each component is a box with a lit top face, a mid-tone left face, and a dark right face — one light source, top-left, held consistently.
- Stack layers vertically with visible separation so the tiers read as tiers.
- Edges travel along grid axes only.

Good for deployment and infrastructure diagrams where physical grouping matters. Bad for anything with more than about eight components, where the geometry starts costing more than it gives.

---

## Circuit board

PCB traces and silkscreen.

- Ground: `#0b3d2e` board green, or `#1a1a1a` for a black board.
- Traces: `#d4af37` gold, 2px, routed at 45° with rounded corners. Vias as small filled circles at direction changes.
- Components: silkscreen white outlines with reference designators (`U1`, `R4`) beside real names.
- Type: small monospace, white.

Good for hardware, embedded, and signal-path diagrams. Elsewhere it is decoration, and it will read that way.

---

## Botanical

Organic growth forms. The weird one, and honest about it.

- Edges are curves, not lines: quadratic béziers that taper from thick at the source to thin at the target, like stems.
- Nodes are leaf or seed shapes, not rectangles. Size by importance.
- Palette: `#2d5016`, `#5a8f29`, `#a8c66c`, `#e8f0d8`, with `#8b4513` for roots or origins.
- Ground: warm cream `#faf7f0`.

Good for showing growth, propagation, or dependency spread where the branching *is* the point. Bad for anything needing precision. This is the style that proves content and treatment are separable — and the one most likely to be the wrong choice.

---

## Brutalist

Heavy, stark, unapologetic.

- Ground: white. Everything else pure black `#000000`, plus exactly one accent, usually `#ff0000`.
- Rules: 4–6px. Boxes are hard rectangles, zero radius, thick borders, no fills.
- Type: a heavy grotesque, oversized, tight leading, uppercase titles. Let labels be bigger than feels comfortable.
- No gradients, no shadows, no rounded anything.

Good for a single diagram that has to dominate a slide or a page. Bad in a series, where it exhausts.

---

## Corporate deck

Boardroom-ready, numbered and captioned.

- Palette: one deep neutral `#051c2c`, one saturated accent `#2251ff`, one data accent `#00a9f4`, on white.
- Every diagram gets an exhibit number and a title that states the finding, not the topic: "Exhibit 3: Three services share one database" rather than "Exhibit 3: Architecture".
- Type: a serif for the exhibit title, sans for everything inside the diagram.
- Source line in small gray type bottom-left.

Good for anything going to executives. Note this repo has an `mcbranding` skill carrying a fuller version of this system — use it if the deck is going out under that identity.

---

## Combining and inventing

Two styles rarely combine well; the result usually reads as a mistake rather than a choice. If the user asks for a mix, pick the dominant one and borrow a single element from the other — blueprint geometry with a hand-drawn stroke, say, and nothing else.

If the user names a style not in this catalog, follow their description directly rather than snapping to the nearest entry here. The catalog is a starting set, not a closed list.
