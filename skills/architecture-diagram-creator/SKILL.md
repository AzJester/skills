---
name: architecture-diagram-creator
description: Create comprehensive single-file HTML architecture diagrams covering business context, data flow, processing pipeline, layered system architecture, features, and deployment, drawn as inline SVG. Use when the user asks to "create an architecture diagram", "generate a high-level overview", "document system architecture", "show the data flow", "diagram the processing pipeline", or wants an architecture overview page for a project.
---

# Architecture Diagram Creator

Produce a single self-contained HTML file that documents a project's architecture: what it does for the business, where its data comes from, how that data is processed, how the system is layered, what it guarantees, and how it is deployed.

The output is one file. No build step, no external assets, no CDN dependencies. Inline SVG for every diagram so the file opens anywhere and survives being emailed around.

## When to use

- "Create architecture diagram for [project]"
- "Generate high-level overview"
- "Document system architecture"
- "Show data flow and processing pipeline"

## Workflow

### 1. Analyze the project

Read the README, then the code structure. Look for:

- Entry points (`main`, `index`, `app`, CLI definitions, route tables)
- Manifests (`package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`) for the tech stack
- Config files and environment variables for external dependencies
- Database connections, queue clients, HTTP clients for integration points

### 2. Extract the six inputs

Before writing any HTML, be able to answer:

| Input | What you are looking for |
| --- | --- |
| Purpose | What the system is for, and who it serves |
| Data sources | Where data enters, in what format, at what volume and cadence |
| Processing | The stages between input and output, and what each stage does |
| Tech stack | Languages, frameworks, cloud services, third-party APIs |
| Outputs | What the system produces, where it lands, who consumes it |
| Deployment | Where it runs, what it needs, how someone operates it |

Use real project details. Never ship the placeholder text.

### 3. Build the six sections

1. **Business Context** — objectives, end users, business value, key metrics
2. **Data Flow** — sources → processing → outputs, as an SVG diagram
3. **Processing Pipeline** — the stages, as a multi-stage SVG diagram
4. **System Architecture** — layered components (data / processing / services / output)
5. **Features** — functional and non-functional requirements, as card grids
6. **Deployment** — deployment model, prerequisites, typical workflow

Start from `assets/template.html`, which carries the full page shell, CSS, and section scaffolding with placeholders. Copy the SVG building blocks from `assets/svg-components.html`.

### 4. Apply the color semantics

Color carries meaning here; it is not decoration. Every diagram uses the same mapping, and the page legend states it.

| Role | Fill | Stroke |
| --- | --- | --- |
| Data sources / inputs | `#4299e1` (blue) | `#2b6cb0` |
| Processing / logic | `#ed8936` (orange) | `#c05621` |
| AI/ML services | `#9f7aea` (purple) | `#6b46c1` |
| Output / success | `#48bb78` (green) | `#2f855a` |
| Configuration | `#f59e0b` (amber) | `#d97706` |
| Supporting tools | `#718096` (gray) | `#4a5568` |
| Warning / critical | `#e53e3e` (red) | `#c53030` |
| Information | `#38b2ac` (teal) | `#2c7a7b` |
| Special / highlight | `#805ad5` (purple) | `#6b46c1` |

Text: `#2d3748` dark, `#4a5568` medium, `#718096` light. Surfaces: `#f7fafc` background, `#e2e8f0` border.

### 5. Write the file

Write to `[project]-architecture.html` in the project root, then tell the user the path.

## Diagram rules

- Every SVG gets a `viewBox` and no fixed `width`/`height`, so it scales. The stylesheet already sets `svg { width: 100%; height: auto; }`.
- Define arrow markers once in a `<defs>` block per SVG. Marker `id`s must be unique across the whole document, so suffix them per diagram (`arrowhead-flow`, `arrowhead-pipeline`, `arrowhead-arch`).
- Label every arrow with why the connection exists, not just that it exists.
- Keep box text to a heading, a subtitle, and three or four detail lines. More than that and the box needs to be split.
- Left-to-right for flows, top-to-bottom for layers.
- Dashed strokes (`stroke-dasharray="5,5"`) mark optional or conditional paths.
- Give real numbers where the project has them: record counts, latencies, SLAs. Vague boxes make a useless diagram.

## Files

| File | Use |
| --- | --- |
| `assets/template.html` | Page shell: CSS, section scaffolding, legend, footer, placeholders |
| `assets/svg-components.html` | Rendered gallery of every reusable SVG block, with its markup |
| `references/example-etl-pipeline.html` | A complete worked example, all six sections filled in |

Open `references/example-etl-pipeline.html` in a browser before starting to see what "done" looks like.
