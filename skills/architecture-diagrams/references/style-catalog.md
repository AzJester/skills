# Style catalog

36 profiles. `python3 scripts/render.py --list-styles` prints the keys and their effects.
Aliases are accepted: `aws`, `flat`, `neon`, `cyberpunk`, `fallout`, `dali`, `picasso`,
`soviet`, `japanese`, `macos`, `windows95`, `chalk`, `monet`, `studio-ghibli`, `deco`,
`nouveau`, `print`, `enterprise`.

## Professional and clean

**aws-reinvent** — dark navy, AWS orange, accent bars. The default for anything cloud. Pairs
with `aws:` icons for official service iconography in the .drawio.

**corporate** — blue gradients on light grey, drop shadows. Survives any design review. Use
for executive audiences and anything that lands in a proposal.

**material** — white cards, restrained purple accent, soft shadows. Good for product and
application architecture rather than infrastructure.

**minimal-flat** — no gradients, no shadows, square corners. Reproduces cleanly in black and
white and at small sizes. Best choice when the diagram will be printed.

**swiss** — Helvetica, hairline rules, red accent, ruthless grid. Looks deliberate rather than
decorative. Strong for a single-page summary graphic.

**blueprint** — white line work on drafting blue with a grid. Reads as engineering rigor.
Excellent for physical systems, test architectures, and anything hardware-adjacent.

## Tech nostalgia

**win95** — grey bevels, teal desktop, title bars on every node. Legacy modernization decks.
Effective when you want the audience to feel the age of the current state.

**aqua** — glossy gel surfaces, traffic-light dots. Dated on purpose.

**dark-neon** — glowing components on near-black. Modern, high contrast, works well on screen
and badly on paper.

**tron** — cyan circuits on black with animated orange connectors in the .drawio. Use `flow`
edges to get the moving light-cycle trails.

## Elegant artistic

**art-deco** — gold on black, sunburst rays, double rules. Anniversary decks, launch events.

**art-nouveau** — cream, botanical curves, muted greens. Slow and decorative.

**stained-glass** — heavy black leading, jewel colours. Striking as a single hero image,
illegible with more than about ten nodes.

**noir** — high-contrast greyscale, venetian blind shadows, vignette. Good for incident
retrospectives and threat modelling.

## Cultural heritage

**ukiyo-e** — woodblock palette, wave patterns. **samurai** — lacquer black and crimson.
**kente** — woven gold, green, and red bands. **aztec** — stepped motifs on terracotta.
**constructivist** — red and black diagonals, Impact type, revolutionary poster energy.

Use these deliberately, and never as an aesthetic borrowed from a culture that is the subject
of the work. Constructivist reads as bold and slightly ironic in a Western business setting;
the others carry more weight and are better for internal or personal work.

## Thematic and playful

**chalkboard** — hand-drawn on green slate. Disarms a room. Ideal for teaching sessions and
whiteboard-style working diagrams where you want people to challenge the content.

**newspaper** — halftone dots, serif type, heavy rules. Retrospectives and postmortems.

**comic** — thick outlines, Ben-Day dots, yellow field. Internal all-hands and onboarding.

**brutalist** — 5px black borders, monospace, raw concrete. Aggressively functional. Reads as
honest, which suits a warts-and-all current-state diagram.

## Gaming and pop culture

**minecraft** — pixel bevels on stone and grass. **lego** — studded bricks, primary colours.
**pipboy** — green phosphor CRT with scanlines and vignette, surprisingly readable.
**origami** — folded paper creases, dashed fold lines, quiet and elegant.

## Anime and cute

**ghibli** — watercolour greens, sketch filter, clouds. **kawaii** — pastel pink, rounded
corners, blush marks, sparkles. Both are warm rather than serious. Fine for a team page,
wrong for a customer deliverable.

## Classical art

**impressionist** — soft blurred edges, dappled palette. **baroque** — gold filigree on deep
brown, vignette, ornate. Both trade legibility for atmosphere; keep the node count low.

## Retro aesthetic

**vaporwave** — magenta and cyan with a perspective horizon and sun. **synthwave** — neon
grid, glow, animated connectors. **memphis** — 1980s confetti and squiggles on cream.

## Abstract and surreal

**cubist** — faceted overlays, rotated nodes, earth tones. **surrealist** — melting drips,
floating eyes, checkerboard floor, desert palette. The most unhinged of the set and the
hardest to read. Use as a conference title slide, not as documentation.

## Choosing

For a customer, an executive, or anything that outlives the meeting: professional family
only. For an internal working session: chalkboard, brutalist, blueprint, comic. For a
conference talk or a title slide: anything, the weirder the more memorable. When the diagram
will be printed in greyscale, check minimal-flat, swiss, newspaper, and noir first, since the
rest depend on colour to carry the structure.

Rendering the same spec in several styles costs one command. When the user is undecided,
generate three and send the gallery.
