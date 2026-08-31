# Spec schema

One JSON object. Everything the renderer needs. Layout is computed, so geometry fields are
optional overrides you should reach for only after looking at a render.

## Top level

| Field | Type | Notes |
|---|---|---|
| `title` | string | Rendered top-left. Omit for a bare diagram. |
| `subtitle` | string | One line under the title. Good place for the architectural claim. |
| `style` | string | Style key. Overridden by `--styles` on the command line. |
| `max_per_row` | int | Nodes per row inside a tier before wrapping. Default 4. Drop to 3 for long labels. |
| `tiers` | array | Ordered top to bottom. Each becomes a labeled band. |
| `edges` | array | Connections between nodes, by node id. |
| `legend` | array | Optional `{label, color}` swatches along the bottom. |

## Tier

```json
{"label": "Application Tier", "note": "private subnets", "nodes": [ ... ]}
```

`label` prints upper-case in the accent color. `note` prints small and right-aligned, useful
for subnet ranges, availability zones, trust boundaries, or ownership. Optional `x`, `y`, `w`,
`h` override the computed band.

## Node

```json
{"id": "svc", "label": "ECS Fargate Services", "sub": "autoscaled 4-24 tasks",
 "icon": "aws:ecs", "badge": "Multi-AZ"}
```

| Field | Notes |
|---|---|
| `id` | Required, unique, referenced by edges. Short lowercase. |
| `label` | Required. Keep under 25 characters — the font shrinks above 24, again above 30, and clips at 34. |
| `sub` | Second line, muted. Capacity, version, protocol, SLA. Under 32 characters. |
| `icon` | `aws:*`, `azure:*`, `gcp:*`, or a generic key. See cloud-icons.md. |
| `badge` | Short pill top-right. Use for the one fact that matters most. |
| `x`, `y`, `w`, `h` | Manual override. Only after a visual check. |

## Edge

```json
{"from": "svc", "to": "queue", "label": "publish", "kind": "flow"}
```

`kind` is `solid` (default), `dashed` (async, optional, or cache-miss paths), or `flow`
(animated marching dashes in both the SVG and the `.drawio`, good for showing direction of
data movement in a live demo).

Edges between tiers route with an elbow at the midpoint. Parallel edges in the same band get
staggered automatically. Edges inside a tier route horizontally, and the renderer widens the
gap between nodes when any same-tier edge carries a label.

## Worked example

`assets/example-3tier.json` is the canonical one: four tiers, AWS icons, mixed edge kinds, a
legend. Copy it and replace the contents.

## Minimal example

```json
{
  "title": "Ingest Pipeline",
  "style": "blueprint",
  "tiers": [
    {"label": "Source", "nodes": [{"id": "sensor", "label": "Field Sensors", "icon": "network"}]},
    {"label": "Processing", "nodes": [
      {"id": "q", "label": "Message Queue", "icon": "queue"},
      {"id": "etl", "label": "Transform Service", "icon": "server"}]},
    {"label": "Storage", "nodes": [{"id": "wh", "label": "Warehouse", "icon": "database"}]}
  ],
  "edges": [
    {"from": "sensor", "to": "q", "label": "telemetry", "kind": "flow"},
    {"from": "q", "to": "etl"},
    {"from": "etl", "to": "wh", "label": "hourly batch"}
  ]
}
```

## Modeling guidance

Tiers should mean something: network zones, trust boundaries, layers, ownership, or physical
location. A tier that just holds leftovers reads as clutter.

Four to six tiers is the working range. Past that the page gets tall and the connector runs
get long. Split into two diagrams instead.

Label edges only where the label adds information. `HTTPS 443`, `gRPC`, `async`, `read
replica` earn their space. `sends data to` does not.

Show the failure and scale story through `sub` and `badge` text rather than extra nodes.
`primary + standby` on one node beats two nodes and a sync arrow.
