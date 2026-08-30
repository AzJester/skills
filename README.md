# skills

A personal collection of Claude / AI agent skills.

## Layout

Each skill lives in its own directory under `skills/`, with a `SKILL.md` entry point at the directory root. Some skills also carry a `.claude-plugin/plugin.json` manifest so they can be installed as Claude Code plugins; others carry an `agents/openai.yaml` for Codex invocation policy.

## Skills

Vendored from two upstream collections. See [Attribution](#attribution) for provenance and licensing.

### Systems engineering

| Skill | Description |
|-------|-------------|
| [system-dev](skills/system-dev/) | AI-assisted systems design using INCOSE principles: a Design Registry with typed slots for components, interfaces, contracts, and requirement references, plus schema validation, change journaling, traceability, impact analysis, and D2/Mermaid diagram generation. |
| [concept-dev](skills/concept-dev/) | NASA Phase A concept development lifecycle: ideation, problem definition, black-box architecture, drill-down with gap analysis, and document generation. |
| [requirements-dev](skills/requirements-dev/) | Transform concept development artifacts into INCOSE-compliant formal requirements. |
| [specification-refiner](skills/specification-refiner/) | Systematic analysis and refinement of specifications with the SEAMS framework, sequential clarification questioning, and a multi-phase workflow. |
| [trade-study-analysis](skills/trade-study-analysis/) | Systematic trade study using the DAU 9-Step Process. |

### Root cause & quality analysis (RCCA)

| Skill | Description |
|-------|-------------|
| [rcca-master](skills/rcca-master/) | Orchestrate complete Root Cause and Corrective Action (RCCA) investigations using the 8D methodology, with integrated tool selection across the skills below. |
| [problem-definition](skills/problem-definition/) | RCCA/8D problem definition using 5W2H and IS/IS NOT analysis. |
| [five-whys-analysis](skills/five-whys-analysis/) | Rigorous 5 Whys root cause analysis with guided questioning, quality scoring, and report generation. |
| [fishbone-diagram](skills/fishbone-diagram/) | Fishbone (Ishikawa/cause-and-effect) diagrams for structured root cause brainstorming. |
| [pareto-analysis](skills/pareto-analysis/) | Pareto Analysis (80/20 rule) to identify the vital few causes driving the majority of problems. |
| [kepner-tregoe-analysis](skills/kepner-tregoe-analysis/) | Kepner-Tregoe Problem Solving and Decision Making: Situation Appraisal, Problem Analysis, Decision Analysis, and Potential Problem Analysis. |
| [fault-tree-analysis](skills/fault-tree-analysis/) | Fault Tree Analysis (FTA) of system failures using Boolean logic gates. |
| [fmea-analysis](skills/fmea-analysis/) | Failure Mode and Effects Analysis (FMEA) for risk assessment of potential failures in designs, processes, or systems. |

Test prompts for the RCCA toolkit: [skills/RCCA_TEST_PROMPTS.md](skills/RCCA_TEST_PROMPTS.md)

### Documentation, research & tooling

| Skill | Description |
|-------|-------------|
| [documentation-architect](skills/documentation-architect/) | Transform documentation using the Diátaxis framework. |
| [speckit-generator](skills/speckit-generator/) | Specification and task management with PLANS taxonomy, ADR-style decisions, SMART acceptance criteria, anti-pattern detection, verification levels, and execution orchestration. |
| [research-opportunity-investigator](skills/research-opportunity-investigator/) | Research and opportunity investigation for protocols. |
| [plugin-creator](skills/plugin-creator/) | Automatically generate Claude plugins from user prompts. |
| [skill-tester](skills/skill-tester/) | Deep test, analyze, and audit Claude skills. |
| [streaming-output](skills/streaming-output/) | Stream long-form content to markdown files with resume capability and context preservation. |
| [streaming-output-mcp](skills/streaming-output-mcp/) | Stream structured content to persistent SQLite storage with automatic session break recovery. |

### Engineering workflow

| Skill | Description |
|-------|-------------|
| [ask-matt](skills/ask-matt/) | Router over the user-invoked skills in this group: ask which skill or flow fits your situation. |
| [setup-matt-pocock-skills](skills/setup-matt-pocock-skills/) | Configure a repo for the engineering workflow skills (issue tracker, triage labels, domain doc layout). Run once per repo. |
| [to-spec](skills/to-spec/) | Turn the current conversation into a spec and publish it to the issue tracker. |
| [to-tickets](skills/to-tickets/) | Break a plan, spec, or conversation into tracer-bullet tickets, each declaring its blocking edges, as text in a local file or as native blocking links on a real tracker. |
| [implement](skills/implement/) | Build the work described by a spec or set of tickets, driving `tdd` at pre-agreed seams and closing out with `code-review` before committing. |
| [tdd](skills/tdd/) | Test-driven development with a red-green-refactor loop, building features or fixing bugs one vertical slice at a time. |
| [code-review](skills/code-review/) | Two-axis review of the diff since a fixed point: Standards (does it follow the repo's coding standards, plus a Fowler smell baseline?) and Spec (does it faithfully implement the originating issue?), run as parallel sub-agents. |
| [diagnosing-bugs](skills/diagnosing-bugs/) | Disciplined diagnosis loop for hard bugs and performance regressions: build a feedback loop that goes red on the bug, minimise, hypothesise, instrument, fix, regression-test. |
| [codebase-design](skills/codebase-design/) | Shared discipline and vocabulary for designing deep modules: small interfaces, clean seams, testable through the interface. |
| [domain-modeling](skills/domain-modeling/) | Actively build and sharpen a project's domain model by challenging terms and stress-testing with scenarios, updating `CONTEXT.md` and ADRs inline. |
| [grill-with-docs](skills/grill-with-docs/) | Grilling session that also builds the project's domain model, sharpening terminology and updating `CONTEXT.md` and ADRs as it goes. |
| [improve-codebase-architecture](skills/improve-codebase-architecture/) | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. |
| [wayfinder](skills/wayfinder/) | Plan a chunk of work larger than one agent session as a shared map of decision tickets on the issue tracker, resolved one at a time. |
| [triage](skills/triage/) | Move issues and external PRs through a state machine of triage roles: categorise, verify, grill if needed, and write agent-ready briefs. |
| [research](skills/research/) | Investigate a question against high-trust primary sources and capture the findings as a cited Markdown file in the repo, run as a background agent. |
| [prototype](skills/prototype/) | Build a throwaway prototype to answer a design question: a single shareable HTML file for state/logic, or several toggleable UI variations. |
| [resolving-merge-conflicts](skills/resolving-merge-conflicts/) | Work through an in-progress git merge or rebase conflict hunk by hunk, resolving by intent traced to each side's primary source, then finish the operation, never `--abort`. |
| [wizard](skills/wizard/) | Generate an interactive bash wizard that walks a human through steps only they can perform: provisioning infrastructure, setting up credentials or CI secrets, or running a one-off migration. |

### Productivity

| Skill | Description |
|-------|-------------|
| [grilling](skills/grilling/) | Grill the user relentlessly about a plan, decision, or idea to stress-test their thinking. |
| [grill-me](skills/grill-me/) | A relentless interview to sharpen a plan or design. |
| [handoff](skills/handoff/) | Compact the current conversation into a handoff document for another agent to pick up. |
| [teach](skills/teach/) | Teach the user a new skill or concept, within the current workspace. |
| [to-questionnaire](skills/to-questionnaire/) | Turn a decision you cannot fully answer into a questionnaire for someone else to fill in. |
| [wait-what](skills/wait-what/) | Stop and re-pitch a message that did not land. |
| [writing-for-agents](skills/writing-for-agents/) | Writing documents for agents: creating or editing skills, `AGENTS.md`, or `CLAUDE.md`. |

### Misc tooling

| Skill | Description |
|-------|-------------|
| [git-guardrails-claude-code](skills/git-guardrails-claude-code/) | Set up Claude Code hooks that block dangerous git commands (push, reset --hard, clean, branch -D) before they execute. |
| [setup-pre-commit](skills/setup-pre-commit/) | Set up Husky pre-commit hooks with lint-staged, Prettier, type checking, and tests. |
| [migrate-to-shoehorn](skills/migrate-to-shoehorn/) | Migrate test files from `as` type assertions to @total-typescript/shoehorn. |
| [scaffold-exercises](skills/scaffold-exercises/) | Create exercise directory structures with sections, problems, solutions, and explainers. |

### In progress (beta)

Upstream ships these as beta: they are excluded from the upstream plugin, and they can change or disappear without warning.

| Skill | Description |
|-------|-------------|
| [implement-spec](skills/implement-spec/) | Implement a whole spec on one branch, working the tickets as a task graph rather than a list and landing the result as a single PR. |
| [loop-me](skills/loop-me/) | Grill yourself into implementable workflow specs over multiple sessions, using the current directory as a stateful workspace. |
| [claude-handoff](skills/claude-handoff/) | Hand the current conversation off to a fresh background agent seeded with a handoff summary via `claude --bg`. |
| [setup-ts-deep-modules](skills/setup-ts-deep-modules/) | Wire dependency-cruiser into a TypeScript repo so each package is a deep module, reachable only through its entry-point files. |
| [writing-fragments](skills/writing-fragments/) | Grilling session that mines you for fragments and appends them to a single document as raw material for a future article. |
| [writing-beats](skills/writing-beats/) | Shape an article as a journey of beats, choose-your-own-adventure style, writing one beat at a time. |
| [writing-shape](skills/writing-shape/) | Take a markdown file of raw material and shape it into an article paragraph by paragraph, arguing format choices at each step. |
| [retro](skills/retro/) | Suggest improvements to the coding agent's environment after a session. Upstream marks this a stub: design notes only, not functional yet. |

### Architecture diagrams

| Skill | Description |
|-------|-------------|
| [diagram-picker](skills/diagram-picker/) | Ask what a diagram must show, what it is for, and what visual style to render it in, then pick the diagram type and draw it. Separates content, fidelity, and style into three independent choices, and carries a catalog of ten concrete visual styles. Hands off whole-system structure diagrams to `architecture-diagram-creator`. |
| [architecture-diagram-creator](skills/architecture-diagram-creator/) | Produce a single self-contained HTML architecture overview: business context, data flow, processing pipeline, layered system architecture, functional and non-functional features, and deployment, all drawn as inline SVG. Ships a page template, a rendered gallery of reusable SVG blocks, and a fully worked example. |
| [omm-scan](skills/omm-scan/) | Scan a codebase and generate `.omm/` architecture docs by perspective-driven recursive analysis: pick the perspectives that fit the project (overall architecture, request lifecycle, data flow, dependency map, storage, and others), then drill into each diagram element until it bottoms out at a leaf. |
| [omm-view](skills/omm-view/) | Start the local web viewer to explore the generated `.omm/` diagrams in a browser, auto-refreshing as the files change. |
| [omm-push](skills/omm-push/) | Push `.omm/` architecture docs to the oh-my-mermaid hosted service, handling the login, link, and push steps. Sends your architecture docs to a third-party service (`ohmymermaid.com`) and needs an account; the free tier is capped at one project. |

The three `omm-*` skills are a front end for the [`omm`](https://github.com/oh-my-mermaid/oh-my-mermaid) CLI rather than self-contained instructions. They shell out to it and will offer to `npm install -g oh-my-mermaid` if it is missing. `architecture-diagram-creator` has no such dependency.

## Attribution

Most skills here are vendored unmodified from their upstream repositories, each redistributed under the MIT License (a copy is included in every skill directory). Skills written for this repository are listed under [Original skills](#original-skills) and carry no third-party licence.

### ddunnock/claude-plugins

The [Systems engineering](#systems-engineering), [RCCA](#root-cause--quality-analysis-rcca), and [Documentation, research & tooling](#documentation-research--tooling) skills come from [ddunnock/claude-plugins](https://github.com/ddunnock/claude-plugins) at commit [`e22db30`](https://github.com/ddunnock/claude-plugins/tree/e22db30ce9da9ff3686cda59edd8855443451ba0/skills), authored by David Dunnock.

Omitted from the copy: the upstream author's internal planning history (`system-dev/.planning/`) and a committed code-index artifact (`concept-dev/.codegraph/`). All functional content (SKILL.md files, commands, agents, schemas, scripts, templates, tests, references, data, plugin manifests) is included unmodified.

Known upstream test-suite quirks at this commit (vendored as-is): 6 ReqIF-export tests fail in `requirements-dev` and one stale test module (`test_report_gen.py`) in `skill-tester` imports a function its script no longer exports; both reproduce identically in the upstream repository. The upstream repo also hosts MCP servers (`session-memory`, `knowledge-mcp`) that are not part of this skills collection.

### mattpocock/skills

The [Engineering workflow](#engineering-workflow), [Productivity](#productivity), [Misc tooling](#misc-tooling), and [In progress](#in-progress-beta) skills come from [mattpocock/skills](https://github.com/mattpocock/skills) at commit [`6654f6b`](https://github.com/mattpocock/skills/tree/6654f6b60cd9d5be8b54c6fafe44346dabeb3b76/skills), authored by Matt Pocock.

Upstream groups its skills into `skills/engineering/`, `skills/productivity/`, `skills/misc/`, and `skills/in-progress/`. Those buckets are flattened here to match this repo's one-directory-per-skill layout, and are preserved as the section headings above. Skill directory contents are byte-identical to upstream, including each skill's supporting reference files, `scripts/`, and `agents/openai.yaml`.

Omitted from the copy: upstream repo infrastructure that is not skill content (`docs/` marketing pages, `.agents/`, `.changeset/`, `.github/`, `CHANGELOG.md`, `CLAUDE.md`, `CONTEXT.md`, `package.json`, `scripts/`) and the root `.claude-plugin/` manifests, which describe the upstream plugin rather than these vendored copies. The upstream `skills/deprecated/` bucket is empty and was not copied.

Several of these skills expect repo-level configuration written by `setup-matt-pocock-skills` (issue tracker, triage labels, domain doc layout); run it once in a target repo before using `to-spec`, `to-tickets`, `triage`, `wayfinder`, or `implement`.

### oh-my-mermaid/oh-my-mermaid

The three `omm-*` skills under [Architecture diagrams](#architecture-diagrams) come from [oh-my-mermaid/oh-my-mermaid](https://github.com/oh-my-mermaid/oh-my-mermaid) at commit [`38ccdb6`](https://github.com/oh-my-mermaid/oh-my-mermaid/tree/38ccdb69298adec949177c92c88d6e3ddfb5bab7/skills), MIT licensed, Copyright (c) 2025 oh-my-mermaid.

All three of upstream's skills are included, byte-identical to upstream. Omitted: the `omm` CLI itself (`src/`, `package.json`, `tsconfig.json`, build config), which ships from npm as [`oh-my-mermaid`](https://www.npmjs.com/package/oh-my-mermaid), plus upstream's own `.omm/` architecture docs, `docs/`, `PLAN.md`, `CLAUDE.md`, `.github/`, and the root `.claude-plugin/` manifests.

These skills do not work on their own: install the CLI with `npm install -g oh-my-mermaid` first. `omm-push` additionally talks to the hosted service at `ohmymermaid.com` and requires an account there.

### Original skills

Written for this repository, not vendored:

- [architecture-diagram-creator](skills/architecture-diagram-creator/) — architecture overview pages as self-contained HTML.
- [diagram-picker](skills/diagram-picker/) — three-question interview (content, fidelity, style) before drawing a diagram.
