# Layout

Layout is the difference between a diagram someone reads and one they skip. The renderer
handles placement; these are the decisions it cannot make for you.

## What the renderer does

Nodes are 210x92 by default. Tiers stack top to bottom with a 64px gutter and are centred on
the widest tier. Nodes fill left to right and wrap at `max_per_row` (default 4). Horizontal
spacing is 36px, widened to 96px when any same-tier edge carries a label. Cross-tier edges
route as an elbow at the vertical midpoint, and parallel edges in the same band are staggered
by 13px so their horizontal runs do not sit on top of each other. Canvas height follows the
content; width is the widest tier plus margins, minimum 900.

## Rules that keep it readable

**Order tiers by flow.** Top to bottom should trace the request path or the data path. A
diagram that reads downward needs no explanation of how to read it.

**Cap a tier at six nodes.** Beyond that, set `max_per_row` to 3 or 4 and let it wrap, or
split the tier. A row of eight boxes is a list, not a diagram.

**Put the busiest node in the middle of its row.** Edges fan out from the centre with shorter
runs and fewer crossings. If one service talks to everything below it, centre it.

**Order nodes within a tier to match the tier below.** If the app tier is API, service,
worker, and the data tier is cache, database, object store, arrange them so the arrows run
mostly straight down. Left-to-right order inside a tier is free; use it.

**Backward edges are expensive.** An edge from a lower tier to a higher one routes up the
outside and crosses everything in between. One is fine and often necessary (a callback, a
cache invalidation). Three means the tier assignment is wrong.

**Keep edge labels to two words.** They render at 11px on a background chip and collide with
each other when several edges share a band. Protocol, verb, or frequency. Nothing else.

## Fixing a crowded render

Look at the PNG first. Then, in rough order of preference:

1. Shorten labels. Most crowding is text, not geometry.
2. Lower `max_per_row` so tiers get taller instead of wider.
3. Reorder nodes within a tier so edges stop crossing.
4. Move a node to a different tier if its position is fighting the flow.
5. Drop edges that carry no information. Not every connection needs to be drawn.
6. Only then, set explicit `x` on a single node. Manual coordinates break when the spec
   changes, so use them last and sparingly.

## When to split into two diagrams

One diagram should answer one question. If the user wants request flow and deployment
topology and failover behaviour, that is three diagrams sharing a component list, not one
diagram with three legends. Splitting is almost always the right call once a single render
runs past about twenty nodes.

## Style interactions

Heavy stroke styles (`brutalist` at 5px, `stained-glass` at 6px) eat interior space. Keep
labels shorter for those. Glow and shadow styles (`dark-neon`, `tron`, `synthwave`, `aqua`)
need more breathing room between tiers because the effect bleeds outside the node bounds; if
it looks smudged, cut a node or raise the tier gap by giving tiers explicit `h`. Sketch-filter
styles (`chalkboard`, `ghibli`, `comic`) displace edges by a few pixels on purpose, so
connectors will not meet node borders exactly. That is the look, not a bug.
