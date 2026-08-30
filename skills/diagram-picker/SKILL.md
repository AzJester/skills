---
name: diagram-picker
description: Interview the user before drawing a diagram, then draw it. Asks what the diagram must show, what it is for, and what visual style to render it in, then picks the diagram type and hands off to the right builder.
disable-model-invocation: true
argument-hint: "[what you want to diagram]"
---

# Diagram Picker

Three things decide a diagram, and they are independent:

- **Content** — what it shows. Structure, flow, sequence, or state.
- **Fidelity** — what it is for. An onboarding sketch and a design-review exhibit contain different amounts of truth.
- **Style** — how it looks. This is orthogonal to the other two: the same architecture can be re-rendered in any style without re-deciding what it shows.

Most diagram requests collapse all three into "make me a diagram" and get a generic block chart. This skill separates them, asks once, then draws.

## Step 1: Ask

Make **one** `AskUserQuestion` call with all three questions. Three separate calls is an interrogation; one call is a form.

**Question 1** — header `Shows`, question "What should this diagram show?"

| Option | Description to give |
| --- | --- |
| Structure | What the pieces are and how they connect. The static picture. |
| Flow | How data or a request moves through the system, start to finish. |
| Sequence | What happens in what order, across participants, over time. |
| State | What states exist and what event moves the system between them. |

**Question 2** — header `Purpose`, question "What is it for?"

| Option | Description to give |
| --- | --- |
| Onboarding | Someone new needs the mental model fast. |
| Design review | Arguing a decision with people who will push back. |
| Documentation | A durable reference that has to stay true to the code. |
| Thinking | Working out whether the design holds up. Throwaway. |

**Question 3** — header `Style`, question "How should it look?"

| Option | Description to give |
| --- | --- |
| Technical clean | Semantic color, flat fills, neutral type. The safe default. |
| Blueprint | White linework on deep blue, drafting annotations. |
| Hand-drawn | Rough strokes, uneven boxes. Reads as provisional on purpose. |
| Surprise me | Render the same diagram in three contrasting styles and show them together. |

Full style definitions, including six more styles beyond the four offered, are in `references/styles.md`. Read it once the style is chosen. If the user picks "Other" and names something not in the catalog, follow their description directly.

### Do not ask what you already know

If the user's opening message answers a question, skip that question and say which answer you inferred. "Show me how a request flows through the API for the onboarding doc" answers Shows and Purpose; ask only about style. Asking a question whose answer is already on screen is the fastest way to make this skill annoying.

If the user gave no subject at all, ask what they want diagrammed as a plain question first. The picker needs something to point at.

## Step 2: Map the answers

**Shows** picks the diagram type and format:

| Shows | Type | Format |
| --- | --- | --- |
| Structure | Layered block or C4 container | Mermaid `graph TD`, or inline SVG when style is non-default |
| Flow | Data flow, left to right | Inline SVG |
| Sequence | Sequence diagram | Mermaid `sequenceDiagram` |
| State | State machine | Mermaid `stateDiagram-v2` |

Mermaid renders natively in Claude Code and in artifacts, so prefer it when the style is Technical clean. Any other style needs inline SVG, because Mermaid will not honor a visual treatment.

**Purpose** sets fidelity, not type:

| Purpose | What changes |
| --- | --- |
| Onboarding | Fewer boxes. Plain-language labels. Omit anything that does not change the mental model. Five to seven nodes is the ceiling. |
| Design review | Detail concentrated on the contested seam, everything else compressed. Annotate the tradeoff being argued. Name the alternatives rejected. |
| Documentation | Name real files, services, and endpoints so a reader can check the diagram against the code. Date it. Include the boring parts. |
| Thinking | Rough is fine. Show the uncertainty: dashed edges for "not sure", question marks on unresolved nodes. |

**Style** sets rendering only. It never changes which boxes exist or what the arrows mean. If a style is making you drop a component to fit the aesthetic, the style is wrong for this diagram — say so and offer Technical clean.

## Step 3: Say what you picked, then draw

One line before drawing: the type you chose and why, from the answers. `Structure + Documentation + Blueprint → layered block diagram, inline SVG, real service names, blueprint treatment.` If the user disagrees, that is the cheapest possible moment to find out.

Then draw it. Every diagram, regardless of style:

- Label every edge with why the connection exists, not just that it exists.
- No orphan nodes. If a box connects to nothing, it does not belong.
- Left to right for flows, top to bottom for layers and hierarchies.
- Text has to survive the style. If the treatment makes labels unreadable, the treatment loses.

For "Surprise me", draw the same diagram three times in three styles that differ from each other in structure of treatment, not just palette: pick one geometric, one organic, one typographic. Present them together and say which you would keep.

## Handing off

When the answers come back **Structure** with purpose **Documentation** or **Design review**, and the subject is a whole system rather than one component, this wants the full treatment: stop and invoke `architecture-diagrams`, passing the answers along. That skill renders a JSON spec to draw.io, SVG, PNG and standalone HTML across 36 styles, so the style answer maps straight onto its `--styles` flag and the editable `.drawio` becomes the source of truth.

Everything else, draw here.
