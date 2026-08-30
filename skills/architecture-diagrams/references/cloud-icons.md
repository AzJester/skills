# Icons

## How icons resolve

Set `icon` on a node. Two paths:

- **`.drawio` output** — an `aws:` prefix emits a real `mxgraph.aws4` resource icon cell
  overlaid on the node box, so the file opens in draw.io with official AWS iconography and
  the label offset to make room.
- **SVG, PNG, HTML output** — every icon maps to a generic vector glyph drawn by the
  renderer. The AWS, Azure, and GCP shape libraries live inside draw.io and cannot be
  embedded in a standalone SVG without shipping licensed artwork, so `aws:lambda` renders as
  the generic function glyph outside draw.io. This is the intended behaviour, not a
  degradation. If the user needs official icons in a PNG, open the `.drawio` in draw.io and
  export from there.

## AWS keys

Prefix with `aws:`. Mapped services:

`lambda` `s3` `ec2` `rds` `aurora` `dynamodb` `sqs` `sns` `cloudfront` `route53`
`apigateway` `elb` `alb` `ecs` `eks` `waf` `cloudwatch` `kms` `elasticache` `sagemaker`
`cognito` `eventbridge` `step`

An unmapped `aws:` key falls back to a styled box with a generic glyph, which still looks
correct. To add one, extend `AWS_RES` in `scripts/render.py` with the draw.io `resIcon` name;
the full list of names lives in the draw.io AWS 2019/2021 shape library under
`mxgraph.aws4.*`.

## Azure and GCP

Use `azure:` or `gcp:` prefixes for readability in the spec. Both currently resolve to
generic glyphs in every output including `.drawio`. For GCP, follow the `AWS_RES` pattern
with the `shape=mxgraph.gcp2.*` stencils. Azure is different: draw.io's Azure2 set is
image-based, not a stencil namespace, so native Azure shapes need an image style —
`image;aspect=fixed;image=img/lib/azure2/<category>/<Icon>.svg` — or the legacy
`mxgraph.azure.*` stencils. The node-plus-overlay emitter in `render_drawio` needs no other
change.

## Generic glyphs

These work identically in every output format and need no prefix. Aliases in parentheses
resolve to the same drawing.

| Key | Aliases |
|---|---|
| `server` | compute, vm, ec2 |
| `database` | db, rds, sql, aurora, dynamodb |
| `cache` | redis, memory, elasticache |
| `queue` | sqs, sns, kafka, topic, eventbridge |
| `storage` | s3, bucket, blob |
| `cdn` | cloudfront, dns, route53, internet |
| `lb` | loadbalancer, alb, elb |
| `api` | apigateway, rest |
| `function` | lambda, serverless, step |
| `container` | ecs, eks, kubernetes, docker, pod |
| `user` | client, actor, users |
| `browser` | web, ui, frontend |
| `mobile` | app |
| `firewall` | waf, security, iam |
| `monitor` | metrics, logging, cloudwatch |
| `network` | vpc, mesh, router |
| `ml` | ai, model, sagemaker |
| `search` | elasticsearch, opensearch |
| `secret` | vault, kms, auth, cognito |
| `gateway` | onprem, datacenter |
| `generic` | fallback for anything unmatched |

A node with no `icon` renders as a plain box with the label at the left edge. Mixing icon and
no-icon nodes in one tier looks inconsistent, so pick one and stay with it per tier.

## Adding a glyph

`scripts/glyphs.py` holds 24x24 SVG fragments. Add a function, then register it plus any
aliases in the `GLYPHS` dict. Keep to stroked paths with `fill="none"` so the glyph inherits
the style accent colour and reads on both light and dark backgrounds.
