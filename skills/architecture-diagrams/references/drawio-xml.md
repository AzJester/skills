# draw.io XML

For the escape hatch only. When tiers-and-edges fits, use the spec and the renderer.

## Skeleton

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" agent="claude" version="24.0.0">
  <diagram name="Architecture">
    <mxGraphModel dx="1400" dy="900" grid="0" gridSize="10" guides="1" tooltips="1"
                  connect="1" arrows="1" fold="1" page="1" pageScale="1"
                  pageWidth="1400" pageHeight="1000" math="0" shadow="0" background="#161E2D">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <!-- content cells go here, parent="1" -->
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

Cells `0` and `1` are mandatory. `0` is the model root, `1` is the default layer, and every
content cell parents to `1` unless it lives inside a container.

## Vertex

```xml
<mxCell id="api" value="API Gateway" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#232F3E;strokeColor=#FF9900;fontColor=#FFFFFF;"
        vertex="1" parent="1">
  <mxGeometry x="120" y="240" width="200" height="80" as="geometry"/>
</mxCell>
```

`as="geometry"` is required and easy to forget. Without it the cell has no position and
draw.io stacks everything at the origin.

## Edge

```xml
<mxCell id="e1" value="HTTPS 443"
        style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;strokeColor=#FF9900;endArrow=blockThin;endFill=1;"
        edge="1" parent="1" source="alb" target="api">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

`source` and `target` are cell IDs. A dangling reference silently drops the edge, so validate
IDs before writing.

## Geometry and stacking

Coordinates are absolute within the layer, origin top-left, y increasing downward. There is no
z-index attribute: paint order is document order, so containers and background bands must be
written before the cells that sit on top of them.

For a cell parented to a container rather than to `1`, geometry is relative to the container's
origin. Mixing the two is the usual source of "everything is 40 pixels off" bugs. The renderer
sidesteps this entirely by parenting everything to `1` and drawing bands first.

## Containers

```xml
<mxCell id="vpc" value="VPC 10.0.0.0/16"
        style="rounded=0;html=1;fillColor=none;strokeColor=#8C4FFF;dashed=1;verticalAlign=top;align=left;spacingLeft=12;container=1;collapsible=0;"
        vertex="1" parent="1">
  <mxGeometry x="60" y="160" width="1200" height="620" as="geometry"/>
</mxCell>
```

`container=1` makes children move with the parent, which is what you want for VPC, subnet,
region, and trust boundaries. `collapsible=0` stops the user from accidentally folding it.

## Swimlanes

```xml
style="swimlane;html=1;startSize=30;horizontal=0;fillColor=#EAF2FB;strokeColor=#1F4E79;"
```

`horizontal=0` gives a horizontal lane with a vertical title bar, the usual arrangement for
process diagrams. `startSize` is the header thickness. Lane children parent to the lane cell.

## Style string grammar

Semicolon-separated `key=value` pairs, no spaces, trailing semicolon harmless. The ones that
matter:

`rounded=0|1` and `arcSize` for corner radius, `fillColor`, `strokeColor`, `strokeWidth`,
`gradientColor` plus `gradientDirection=north|south|east|west`, `fontColor`, `fontFamily`,
`fontSize`, `fontStyle=1` for bold, `dashed=1` with `dashPattern=8 8`, `shadow=1`,
`opacity=0-100`, `whiteSpace=wrap`, `html=1` to allow markup in `value`, `align` and
`verticalAlign`, `spacingLeft` for label offset, `sketch=1;curveFitting=1;jiggle=2` for the
hand-drawn look.

`value` accepts HTML when `html=1`, so a two-line label is
`Service<br><font style="font-size:10px">detail</font>`. Escape `&` as `&amp;` since the
attribute lands inside XML.

## Animated connectors

```
edgeStyle=orthogonalEdgeStyle;dashed=1;flowAnimation=1;
```

`flowAnimation=1` marches the dashes along the edge in the draw.io viewer and in exported
HTML. It does nothing in a PNG export. Reserve it for the two or three edges that carry the
main data flow, since every edge animating at once is unreadable.

## Shape libraries

Cloud icons come from bundled shape libraries referenced in the style string:

```
shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.lambda;aspect=fixed;
```

Prefixes: `mxgraph.aws4.*`, `mxgraph.gcp2.*`, `mxgraph.kubernetes.*`, `mxgraph.cisco19.*`,
`mxgraph.veeam2.*`. Azure2 icons are image styles (`image=img/lib/azure2/...`), not
stencils; the legacy Azure stencil set is `mxgraph.azure.*`. Resource icons are fixed-aspect and look wrong when
stretched, so give them a square geometry (52x52 works) and put the text on a separate box
cell underneath or beside them.

## Validate before delivering

```bash
python3 -c "import xml.etree.ElementTree as ET; ET.parse('diagram.drawio'); print('valid')"
```

Parsing proves it is well-formed XML, not that it looks right. There is no headless draw.io
renderer in this environment, so a hand-authored file cannot be previewed here. Either keep
the geometry conservative and tell the user to open it, or build the same diagram through the
spec so you get a PNG to inspect.
