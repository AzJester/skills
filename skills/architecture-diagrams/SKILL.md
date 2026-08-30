---
name: architecture-diagrams
description: Generate architecture diagrams as draw.io (.drawio) XML plus matching SVG, PNG, and standalone HTML, rendered in any of 36 visual styles from clean corporate and AWS re:Invent through blueprint, TRON, ukiyo-e, LEGO, and surrealist. Use this skill whenever the user asks for an architecture diagram, system diagram, network or data-flow diagram, a draw.io or diagrams.net file, a .drawio file, an infrastructure picture, a "diagram of how this works," or asks to restyle or re-render an existing diagram. Also trigger when the user describes an architecture in prose and asks to visualize, sketch, draw, or illustrate it, when they mention diagram styles or want the same architecture in several looks, or when a proposal, brief, or deck needs a system graphic. Prefer this over hand-writing SVG or Mermaid whenever the subject is systems, infrastructure, cloud services, or component-and-connection structure.
---

# Architecture diagrams

Turn an architecture description into a `.drawio` file plus SVG, PNG, and a standalone HTML
page, in a chosen visual style. The diagram is defined once as a JSON spec and rendered by
`scripts/render.py`. Never hand-write draw.io XML unless the spec model genuinely cannot
express the diagram (see "Escape hatch").

## Workflow

**1. Extract the architecture.** From the user's prose, pull out components, what layer each
sits in, and what talks to what. Where the description is thin, fill the obvious gaps
(a public-facing app needs an entry point, a stateful service needs a data store) and say
plainly which pieces were inferred. Ask only when a real ambiguity would change the picture.

**2. Pick the style.** If the user named one, use it. If not, use `corporate` for internal
business audiences, `aws-reinvent` / `blueprint` for technical ones, and offer two or three
alternates by name. `python3 scripts/render.py --list-styles` prints the catalog. Read
`references/style-catalog.md` before recommending, since it says what each style is actually
good for and which ones are unreadable at small sizes.

**3. Write the spec.** JSON, structured as tiers of nodes plus edges between them. The schema,
every field, and worked examples are in `references/spec-schema.md`. Use
`assets/example-3tier.json` as the starting shape. Layout is automatic. Do not set x/y unless
a specific node needs to be moved.

**4. Render.**

```bash
python3 scripts/render.py spec.json --outdir out --styles blueprint
```

Multiple styles in one run also emit a comparison gallery:

```bash
python3 scripts/render.py spec.json --outdir out --styles corporate,tron,ghibli
```

The script validates the spec first. It refuses duplicate node IDs and warns about dangling
edges and unconnected nodes. Fix warnings rather than shipping past them, since an
unconnected node usually means a missing edge in the spec.

**5. Look at the PNG before delivering it.** Open it with the view tool. Check for overlapping
edge labels, text clipped inside nodes, and connectors crossing through boxes. Common fixes:
shorten labels, move a node to a different tier, set `max_per_row`, or give one node an
explicit `x`. Re-render and look again.

**6. Deliver.** Present the `.drawio` (editable source of truth), the PNG (drops into decks
and documents), the HTML (shareable, works offline), and the gallery when several styles were
generated. Tell the user the `.drawio` opens in the desktop app or at diagrams.net and that
every element stays individually editable.

## Cloud service icons

Set a node's `icon` to `aws:lambda`, `aws:rds`, `aws:s3` and so on to get official AWS
iconography in the `.drawio` output, rendered as a proper `mxgraph.aws4` shape. The SVG and
PNG fall back to a matching generic glyph, since the AWS shape library only exists inside
draw.io. Supported service keys and the Azure and GCP equivalents are in
`references/cloud-icons.md`. Generic icons (`database`, `queue`, `user`, `firewall` and
others) work everywhere and need no prefix.

## Style range

36 profiles across professional, nostalgic, artistic, cultural, playful, gaming, anime,
classical, retro, and abstract families. The weird ones are real deliverables, not jokes:
`blueprint` reads as engineering rigor, `chalkboard` disarms a room during a teaching
session, `newspaper` works for a retrospective. Match the style to the audience, and when a
diagram is going in front of a customer or an executive, say so before choosing something
loud. See `references/style-catalog.md`.

## Escape hatch

Hand-authored draw.io XML is warranted for swimlane process diagrams, sequence diagrams,
free-form layouts, or anything where tiers-and-edges is the wrong model. The XML format,
container semantics, style string grammar, geometry rules, and the animated-connector trick
are documented in `references/drawio-xml.md`. Write the XML to a `.drawio` file, then confirm
it parses:

```bash
python3 -c "import xml.etree.ElementTree as ET; ET.parse('diagram.drawio'); print('valid')"
```

## Reference files

- `references/spec-schema.md` — spec fields, defaults, and worked examples. Read before writing a spec.
- `references/style-catalog.md` — all 36 styles, what each is for, and where each falls apart.
- `references/layout.md` — the rules that keep output readable. Read when a render looks crowded.
- `references/cloud-icons.md` — AWS, Azure, and GCP icon keys and generic glyph names.
- `references/drawio-xml.md` — raw XML format, for the escape hatch only.
