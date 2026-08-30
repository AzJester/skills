# skills

A personal collection of Claude / AI agent skills.

## Layout

Each skill lives in its own directory under `skills/`, with a `SKILL.md` entry point at the directory root. Some skills also carry a `.claude-plugin/plugin.json` manifest so they can be installed as Claude Code plugins; others carry an `agents/openai.yaml` for Codex invocation policy.

## Skills

Vendored from several upstream collections, plus skills written for this repository. See [Attribution](#attribution) for provenance and licensing.

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
| [which-skill](skills/which-skill/) | Router across the whole collection: picks the right skill by what stage of work you are in rather than by keyword, and spells out the overlaps people actually get wrong (incident versus root cause, bug versus incident, the diagram skills, requirements versus spec). |
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
| [architecture-diagrams](skills/architecture-diagrams/) | Render an architecture from a JSON spec to a draw.io `.drawio` file plus matching SVG, PNG, and standalone HTML, in any of 36 visual styles (corporate, AWS re:Invent, blueprint, TRON, ukiyo-e, LEGO, surrealist, and more). Automatic layout, AWS/Azure/GCP service icons, and a comparison gallery when several styles are rendered at once. Python 3 stdlib only; `cairosvg` optional, for PNG. |
| [diagram-picker](skills/diagram-picker/) | Ask what a diagram must show, what it is for, and what visual style to render it in, then pick the diagram type and draw it. Separates content, fidelity, and style into three independent choices, and carries a catalog of ten concrete visual styles. Hands off whole-system structure diagrams to `architecture-diagrams`. |
| [omm-scan](skills/omm-scan/) | Scan a codebase and generate `.omm/` architecture docs by perspective-driven recursive analysis: pick the perspectives that fit the project (overall architecture, request lifecycle, data flow, dependency map, storage, and others), then drill into each diagram element until it bottoms out at a leaf. |
| [omm-view](skills/omm-view/) | Start the local web viewer to explore the generated `.omm/` diagrams in a browser, auto-refreshing as the files change. |
| [omm-push](skills/omm-push/) | Push `.omm/` architecture docs to the oh-my-mermaid hosted service, handling the login, link, and push steps. Sends your architecture docs to a third-party service (`ohmymermaid.com`) and needs an account; the free tier is capped at one project. |

The three `omm-*` skills are a front end for the [`omm`](https://github.com/oh-my-mermaid/oh-my-mermaid) CLI rather than self-contained instructions. They shell out to it and will offer to `npm install -g oh-my-mermaid` if it is missing. `architecture-diagrams` and `diagram-picker` have no such dependency.

### UI & UX

| Skill | Description |
|-------|-------------|
| [ui-ux-pro-max](skills/ui-ux-pro-max/) | Searchable offline UI/UX database with a Python CLI: 88 styles, 192 product palettes and reasoning profiles, 74 font pairings, 1,934 Google Fonts, 119 UX guidelines, 105 icons, 17 motion presets, 25 chart types, and 22 technology stacks. Generates a whole design system from one query, with optional variance/motion/density dials, and persists it as a master document plus per-page overrides. |

Largest skill here by a wide margin (3.7 MB, mostly font and icon catalogs). Runs on the Python 3 standard library with no external packages and makes no network calls.

### Framework performance

| Skill | Description |
|-------|-------------|
| [vercel-react-best-practices](skills/vercel-react-best-practices/) | 70 React and Next.js performance rules from Vercel Engineering, across eight categories ordered by impact: eliminating waterfalls and bundle size (critical), server-side and client-side data fetching, re-render and rendering performance, JavaScript micro-optimizations, and advanced patterns. Each rule is its own file with an incorrect example, a correct example, and the reasoning; `AGENTS.md` is the same content compiled into one document. |

### Analytics communication

| Skill | Description |
|-------|-------------|
| [data-storytelling](skills/data-storytelling/) | Turn analysis into a narrative that lands: setup/conflict/resolution structure, a six-beat arc from hook to call-to-action, and the three pillars (data as evidence, narrative as meaning, visuals as clarity). `references/details.md` carries worked story frameworks end to end. |

### Operations & security

| Skill | Description |
|-------|-------------|
| [incident-response](skills/incident-response/) | Run a live production incident and close it out: severity triage, stabilise before diagnosing, timeline reconstruction from timestamped artefacts, blameless postmortem, and turning the fix into a runbook. Hands off to the RCCA skills for root cause once the incident is closed, rather than during it. |
| [threat-modeling](skills/threat-modeling/) | Find security weaknesses in a design before they are built: STRIDE applied per element over a data-flow model with explicit trust boundaries, then each mitigation traced out to a requirement and mapped to its NIST SP 800-53 control family. |

### Proposal bridge

| Skill | Description |
|-------|-------------|
| [engineering-to-proposal](skills/engineering-to-proposal/) | Turn delivered engineering work into proposal evidence: harvest past-performance material from a finished project, build a technical volume from a real architecture, and crosswalk delivered requirements into compliance-matrix rows. Every claim traces to an artefact or is marked unsupported. |

### Systems engineering management

The technical-management layer above the design skills: what could stop the programme, how each requirement gets proven, what state the system is in, and whether a gate should pass.

| Skill | Description |
|-------|-------------|
| [verification-validation](skills/verification-validation/) | Plan and run V&V: the four methods (inspection, analysis, demonstration, test), a VCRM mapping every requirement to its method, level, event and evidence, test campaign sequencing, and honest judgement of whether evidence actually closes a requirement. Consumes `requirements-dev` output; feeds `technical-reviews`. |
| [risk-management](skills/risk-management/) | A programmatic risk register: if–then–because risk statements, 1–5 likelihood and consequence on published scales, inherent versus residual scoring, the four handling strategies, triggers, and burn-down. Distinct from `fmea-analysis`, which analyses design failure modes rather than programme exposure. |
| [technical-reviews](skills/technical-reviews/) | Plan, run and close SRR, SFR, PDR, CDR, TRR and FCA/PCA gates: entry and exit criteria per gate, the artefact package each depends on, written RIDs before the meeting, four honest outcomes, and action-item closure. Establishes the baselines that `configuration-management` then holds. |
| [interface-control](skills/interface-control/) | Govern the boundary between two things that must work together: ICD authoring across all eight layers from transport to lifecycle, the assumptions each side makes about the other, two-party signature, and interface change control. `system-dev` models interfaces; this is the agreement about them. |
| [measures-of-effectiveness](skills/measures-of-effectiveness/) | Define and track MOEs, MOPs, KPPs and TPMs: threshold and objective for every measure, planned profiles with tolerance bands, honest source labelling (measured, analysed, estimated), and the three failure patterns that make a tracking chart worse than none. |
| [configuration-management](skills/configuration-management/) | Control what the system is: configuration items, the functional, allocated and product baselines, change control with a real impact assessment (including which verification a change invalidates), deviations versus waivers, FCA/PCA audits, and status accounting. |
| [trl-assessment](skills/trl-assessment/) | Assess technology readiness on TRL 1–9 against demonstrated evidence rather than confidence, identify critical technology elements, and plan maturation level by level with fallbacks and decision points. Covers MRL and IRL where a programme requires them. |

### Technical writing

The documents you produce and review, as distinct from the publishing formats below, which cover how to format a paper for a venue.

| Skill | Description |
|-------|-------------|
| [proposal-writing](skills/proposal-writing/) | Write the RFP response itself: Section M as the scoring rubric and Section L as the format it expects, a compliance matrix built before any prose, annotated outlines and storyboards, theme-proof-consequence sections, action captions that let a graphic carry its claim, and what each colour team review actually checks. Picks up where `solution-shaping` stops and consumes `engineering-to-proposal` evidence. |
| [white-paper-and-baa](skills/white-paper-and-baa/) | White papers and research proposals for BAAs, CSOs, SBIR and STTR: a white paper earns an invitation rather than winning an award, the falsifiable claim that replaces "leverages AI/ML", naming your own hard part, and the SBIR phase traps — answering the topic as written, eligibility, and transition scored from Phase I. |
| [technical-editing](skills/technical-editing/) | Edit someone else's technical writing: the four levels of edit and why inverting their order wastes the work, the substantive pass, where technical prose actually fails, plain language for a non-engineer reader, and review comments phrased to be accepted rather than defended against. |
| [procedural-documentation](skills/procedural-documentation/) | Instructions someone follows while doing something: task analysis before writing, one action per step, warnings placed before the hazard rather than after it, observable results so a failed step cannot be carried forward, recovery paths and stop conditions, and validation by watching someone follow it. |
| [test-report](skills/test-report/) | The document that delivers test results: as-tested configuration recorded so results can support a fielding decision, results organised by objective rather than chronology, deficiencies categorised by operational impact, and the limitations section that decides whether the report survives scrutiny. Sits after `test-and-evaluation` plans the event and `verification-validation` judges the evidence. |
| [sow-and-pws](skills/sow-and-pws/) | Write the document that defines the work: SOO versus PWS versus SOW and who owns the risk of the method being wrong, performance standards with a measure and an AQL, why product requirements in a work statement make both documents unverifiable, and CDRLs and DIDs as real priced scope. |
| [briefing-deck](skills/briefing-deck/) | Briefings that work when presented: BLUF because senior audiences interrupt, slide titles written as assertions so a forwarded deck still argues, backup that carries the proof, the five questions a decision brief must already answer, and rehearsing to two-thirds of the scheduled slot. |
| [invention-disclosure](skills/invention-disclosure/) | Protect an idea before publishing it: the disclosure record written while the work is fresh, inventorship as a legal determination rather than a courtesy list, patent versus trade secret, subject-invention reporting on federal contracts, and the timing trap — publishing first can forfeit foreign patent rights outright. Not legal advice. |

### Defense cyber & accreditation

| Skill | Description |
|-------|-------------|
| [rmf-ato](skills/rmf-ato/) | Run the Risk Management Framework and assemble an authorization package: categorisation against FIPS 199 / CNSSI 1253, control selection and tailoring with defensible reasons, the SSP written during implementation rather than after, assessment preparation, the AO decision, and continuous monitoring. Consumes `threat-modeling` findings as control rationale. |
| [zero-trust-architecture](skills/zero-trust-architecture/) | Design and argue a zero trust architecture across the seven DoD pillars, from the protect surface and transaction flows outward, with per-pillar target-versus-advanced maturity and the visibility that lets enforcement be demonstrated rather than asserted. |
| [stig-and-hardening](skills/stig-and-hardening/) | Apply STIGs, SRGs and CIS benchmarks, verify by SCAP scan rather than by assertion, tailor with reasons that survive an assessor reading them cold, and stop configuration drift. Feeds `rmf-ato` as control evidence. |
| [cmmc-readiness](skills/cmmc-readiness/) | Your own company's compliance rather than a delivered system's: DFARS 7012/7019/7020/7021, CUI discovery and scoping, 800-171 assessment against the 800-171A objectives, honest SPRS scoring, and C3PAO assessment preparation. |
| [supply-chain-security](skills/supply-chain-security/) | SBOM generation and consumption, the SSDF practice groups and attestation, artifact provenance and signing, and a vulnerability response runbook built around one measure: how long it takes to answer "are we affected". |

### Test, evaluation & digital engineering

| Skill | Description |
|-------|-------------|
| [test-and-evaluation](skills/test-and-evaluation/) | DoD T&E: developmental versus operational test, TEMP structure, the evaluation framework from critical operational issues down to data elements, the six cybersecurity T&E phases, and VV&A for models and simulation. Sits above `verification-validation`, which proves requirements rather than fieldability. |
| [digital-engineering](skills/digital-engineering/) | Digital engineering as DoD means it: an authoritative source of truth that is enforced rather than declared, SysML modelled to answer questions rather than for completeness, the three digital thread links worth building first, model governance and curation, and when a digital twin earns its cost. Extends `system-dev`. |
| [mbse-sysml](skills/mbse-sysml/) | The MBSE modelling practice itself: writing down the questions the model must answer before opening a tool, the four pillars with effort put where it is usually missing (behaviour and parametrics rather than more structure), allocation queries that find orphans in both directions, depth that follows responsibility boundaries, and the SysML v1 versus v2 decision. `digital-engineering` covers the strategy; this covers the model. |

### Networks

| Skill | Description |
|-------|-------------|
| [network-architecture](skills/network-architecture/) | Network solutions for defense programs: mission flows before topology, designing for the disconnected case first, layered transport diversity with explicit failover behaviour, segmentation that matches the zero trust boundaries, DoDIN connection lead times, and JADC2 framing that turns on data and decision timelines rather than diagrams. |

### Artificial intelligence

| Skill | Description |
|-------|-------------|
| [ai-governance](skills/ai-governance/) | Govern an AI system so its risk is managed and demonstrable: the NIST AI RMF functions, use-case mapping with an explicit operating envelope, impact determination, DoD Responsible AI principles, and human oversight designed so the reviewer can actually disagree. Consumes `ai-evaluation` as its Measure function. |
| [ai-evaluation](skills/ai-evaluation/) | Prove an AI system is good enough to field: acceptance criteria set before measuring, evaluation sets representative of deployment rather than training, metrics matched to the decision, validated human review, per-case regression diffing, and a failure taxonomy that says which failures are caught downstream. AI TEVV sits inside `test-and-evaluation`. |
| [ai-solution-architecture](skills/ai-solution-architecture/) | Choose and justify an AI architecture: prompting through retrieval, fine-tuning and agentic in ascending order of commitment, model selection as a trade, and the failure design — unavailability, malformed output, confidently wrong output, refusal, logging — that separates a system from a demo. |
| [ai-cost-modeling](skills/ai-cost-modeling/) | What an AI solution costs at contract volume: cost per unit of work rather than per token, the consumers people miss (system prompts, retrieved context, retries, agentic step tails, conversation growth), the levers in order of effect, and the commercial shape under a given contract type. |

### Program & contract

| Skill | Description |
|-------|-------------|
| [earned-value-management](skills/earned-value-management/) | Read and run EVM: the three numbers and what the derived indices mean, why SPI misleads late in a program, EAC methods and the TCPI reality check, the measurement-method choices that decide whether the baseline is honest, and variance analysis that names causes rather than restating arithmetic. |
| [contract-vehicles-and-clauses](skills/contract-vehicles-and-clauses/) | What a contract type and its clauses commit you to: who carries risk under each type, CLIN structure and funding, CDRLs as real scope, data rights and what determines them, the changes clause and constructive change, and flow-down. Engineering consequences, not legal advice. |
| [export-control-and-markings](skills/export-control-and-markings/) | Handle export-controlled and CUI material correctly: ITAR versus EAR, deemed exports and why cloud and AI services are transmissions, the CUI marking system, distribution statements A through F, and a pre-release checklist. A guardrail, with a bias toward asking before disclosing. |

### Executive & professional practice

| Skill | Description |
|-------|-------------|
| [solution-shaping](skills/solution-shaping/) | Shape the technical solution before the proposal exists: the customer's actual problem rather than the stated requirement, an evaluation-factor crosswalk, discriminators tested against four conditions, competitive position including transition risk, and a descope ladder agreed before the price forces one. |
| [executive-decision-memo](skills/executive-decision-memo/) | The one-page memo that gets a decision from someone who will read it without you: the ask in the first line, why now, options with a recommendation, and what executives actually check — total cost, the do-nothing case, the real risk, and who disagrees. |
| [business-case](skills/business-case/) | Argue for a course of action against doing nothing: complete costing including internal labour and opportunity cost, benefits separated into hard, soft and strategic rather than converted optimistically, payback and NPV with a stated discount rate, and sensitivity that names what would have to be true for this to be a bad decision. |
| [applied-statistics](skills/applied-statistics/) | Statistics on real decisions: sizing the sample before collecting, choosing the test by question and data, reporting effect sizes with intervals rather than p-values alone, experiment design that isolates what you are testing, and the seven questions that find most defects in someone else's analysis. |
| [structured-interviewing](skills/structured-interviewing/) | Interviews that predict performance: attributes with described evidence, a scorecard written before anyone is seen, behavioural and work-sample questions, and independent scoring before debrief — the single highest-leverage rule in the process. |
| [performance-feedback](skills/performance-feedback/) | Feedback that changes behaviour: behaviour, effect, and ask; one-to-ones that belong to the other person; reviews where nothing is a surprise; and performance conversations where the person leaves knowing they had one. |
| [manuscript-submission](skills/manuscript-submission/) | Get a paper through peer review: venue choice before finishing, submission preparation, reading a decision properly, the response-to-reviewers document that is frequently done badly, handling rejection, and reviewing others' work. |

### Technical publishing

| Skill | Description |
|-------|-------------|
| [ieee-paper](skills/ieee-paper/) | Write or format a paper to IEEE requirements: conference versus journal templates (which differ), section numbering, the figure-caption-below/table-caption-above rule, equations, and IEEE numbered-bracket references with patterns for every source type. Treats the venue's own downloaded template as authoritative rather than hardcoding values that drift between revisions. |
| [dod-technical-report](skills/dod-technical-report/) | DoD technical reports for DTIC and contract delivery: the three determinations made before writing, report structure, and the SF 298 block by block — with the abstract and subject terms that decide whether the report is ever retrieved again. |
| [nasa-sti](skills/nasa-sti/) | NASA STI reports: the series types and which one a contractor produces, the self-contained Summary, subject categories, availability determination, and the review path. Export control is not softened by the sponsor being civil. |
| [acm-paper](skills/acm-paper/) | ACM venues via the `acmart` class: format options set by the venue, required CCS concepts and rights commands, and the difference that produces real rework — ACM orders references alphabetically where IEEE orders by first appearance. |
| [apa-7](skills/apa-7/) | APA 7th edition: student versus professional papers, the five heading levels including the two that run into the paragraph, author–date citation with `et al.` from the first citation, sentence-case titles, and the statistics conventions reviewers in these fields notice. |
| [chicago-turabian](skills/chicago-turabian/) | Chicago's two citation systems and how to choose: notes–bibliography for archives, government documents and policy writing; author–date where the date should be visible. Turabian as the student adaptation. |
| [latex-authoring](skills/latex-authoring/) | Building any of the above in LaTeX: writing into a publisher's class rather than fighting it, BibTeX versus BibLaTeX and the brace-protection problem, float placement, the compile sequence, and the errors worth recognising on sight. |

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

- [diagram-picker](skills/diagram-picker/) — three-question interview (content, fidelity, style) before drawing a diagram.
- [incident-response](skills/incident-response/) — live incident handling, postmortem, and runbook authoring.
- [threat-modeling](skills/threat-modeling/) — STRIDE over a data-flow model, traced to NIST 800-53 control families.
- [engineering-to-proposal](skills/engineering-to-proposal/) — delivered engineering work into past-performance and technical-volume evidence.
- [which-skill](skills/which-skill/) — router across the whole collection.
- [verification-validation](skills/verification-validation/) — V&V planning, VCRM, and evidence closure.
- [risk-management](skills/risk-management/) — programmatic risk register, 5×5 scoring, burn-down.
- [technical-reviews](skills/technical-reviews/) — SRR/PDR/CDR/TRR gates with entry and exit criteria.
- [interface-control](skills/interface-control/) — ICD authoring and interface change control.
- [measures-of-effectiveness](skills/measures-of-effectiveness/) — MOE/MOP/KPP definition and TPM tracking.
- [configuration-management](skills/configuration-management/) — baselines, change control, and audits.
- [trl-assessment](skills/trl-assessment/) — technology readiness assessment and maturation planning.
- [ieee-paper](skills/ieee-paper/) — papers in IEEE conference or journal format.
- [rmf-ato](skills/rmf-ato/) — RMF process and authorization package assembly.
- [zero-trust-architecture](skills/zero-trust-architecture/) — DoD zero trust across the seven pillars.
- [stig-and-hardening](skills/stig-and-hardening/) — benchmark application, tailoring, and drift control.
- [cmmc-readiness](skills/cmmc-readiness/) — CUI scoping, 800-171 assessment, SPRS scoring.
- [supply-chain-security](skills/supply-chain-security/) — SBOM, SSDF, provenance, vulnerability response.
- [test-and-evaluation](skills/test-and-evaluation/) — DT&E, OT&E, TEMP, cyber T&E, and VV&A.
- [digital-engineering](skills/digital-engineering/) — authoritative source of truth, MBSE, digital thread.
- [mbse-sysml](skills/mbse-sysml/) — SysML modelling practice: four pillars, allocation, parametrics, v1 versus v2.
- [network-architecture](skills/network-architecture/) — mission flows, DIL operation, transport diversity.
- [ai-governance](skills/ai-governance/) — NIST AI RMF, impact determination, oversight design.
- [ai-evaluation](skills/ai-evaluation/) — eval harness, acceptance criteria, regression, failure taxonomy.
- [ai-solution-architecture](skills/ai-solution-architecture/) — approach selection and failure design.
- [ai-cost-modeling](skills/ai-cost-modeling/) — unit economics of an AI solution at volume.
- [earned-value-management](skills/earned-value-management/) — CPI, SPI, EAC, and variance analysis.
- [contract-vehicles-and-clauses](skills/contract-vehicles-and-clauses/) — contract types, CLINs, data rights.
- [export-control-and-markings](skills/export-control-and-markings/) — ITAR/EAR, CUI, distribution statements.
- [solution-shaping](skills/solution-shaping/) — technical solution strategy before the proposal.
- [executive-decision-memo](skills/executive-decision-memo/) — the one-pager that gets a decision.
- [business-case](skills/business-case/) — ROI, payback, NPV, and sensitivity.
- [applied-statistics](skills/applied-statistics/) — hypothesis testing, sample size, experiment design.
- [structured-interviewing](skills/structured-interviewing/) — scorecards, evidence, independent scoring.
- [performance-feedback](skills/performance-feedback/) — feedback, one-to-ones, reviews.
- [manuscript-submission](skills/manuscript-submission/) — peer review and responding to reviewers.
- [dod-technical-report](skills/dod-technical-report/) — DTIC reports and the SF 298.
- [nasa-sti](skills/nasa-sti/) — NASA STI report series and NTRS submission.
- [acm-paper](skills/acm-paper/) — ACM venues via the acmart class.
- [apa-7](skills/apa-7/) — APA 7th edition.
- [chicago-turabian](skills/chicago-turabian/) — Chicago's two citation systems.
- [latex-authoring](skills/latex-authoring/) — LaTeX mechanics across every format above.
- [proposal-writing](skills/proposal-writing/) — RFP response: compliance matrix, storyboards, colour team reviews.
- [white-paper-and-baa](skills/white-paper-and-baa/) — BAA, CSO, SBIR and STTR white papers and proposals.
- [technical-editing](skills/technical-editing/) — levels of edit, plain language, review comments that land.
- [procedural-documentation](skills/procedural-documentation/) — procedures, warnings, verification and recovery.
- [test-report](skills/test-report/) — delivering test results with deficiencies and limitations.
- [sow-and-pws](skills/sow-and-pws/) — SOO, PWS, SOW, performance standards, CDRLs and DIDs.
- [briefing-deck](skills/briefing-deck/) — decision and information briefings, BLUF, backup.
- [invention-disclosure](skills/invention-disclosure/) — disclosure records, inventorship, publish-before-file timing.
- [architecture-diagrams](skills/architecture-diagrams/) — spec-driven draw.io/SVG/PNG/HTML renderer with 36 styles. Added from a bundle supplied by the repo owner; it carries no upstream licence or authorship of its own.

### nextlevelbuilder/ui-ux-pro-max-skill

[ui-ux-pro-max](skills/ui-ux-pro-max/) comes from [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) at commit [`8bd29e7`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/8bd29e775453ebcae52b6e6514fbf134df0c5770/.claude/skills/ui-ux-pro-max) (v2.13.0), MIT licensed, Copyright (c) 2024 Next Level Builder.

Vendored byte-identical to upstream apart from the added `LICENSE` and a stripped `__pycache__`. Upstream ships seven skills (`banner-design`, `brand`, `design`, `design-system`, `slides`, `ui-styling`, and this one) plus an npm CLI installer; only `ui-ux-pro-max` is taken here, since it is self-contained and the others overlap skills this repo already has.

Verified at vendoring time: every advertised catalogue count matches the data exactly; upstream's own suite passes 153 tests and 7,936 subtests; and all 1,344 text-on-surface pairs across the 192 palettes clear the WCAG AA 4.5:1 contrast ratio the skill itself makes its top rule, the tightest at 4.60:1.

Note that upstream's `skill.json` and `.claude-plugin/plugin.json` are stale at this commit, advertising "84 styles" and "98 UX guidelines" where the data holds 88 and 119. `SKILL.md` states the correct figures, and the table above follows the data rather than the manifests.

### vercel-labs/agent-skills

[vercel-react-best-practices](skills/vercel-react-best-practices/) comes from [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) at commit [`063bee9`](https://github.com/vercel-labs/agent-skills/tree/063bee94c3f4df8453406c830b0a7df0f2860278/skills/react-best-practices), vendored byte-identical.

Upstream declares MIT in its [README](https://github.com/vercel-labs/agent-skills#license) and in the skill's own frontmatter (`license: MIT`), but the repository ships no `LICENSE` file, so unlike every other vendored skill here this directory carries no licence copy. There was nothing to copy, and writing one would mean inventing a copyright line upstream never stated.

The upstream directory is `react-best-practices` while the skill's frontmatter name is `vercel-react-best-practices`. The directory here follows the frontmatter, keeping this repo's invariant that a skill's directory name matches the name it is invoked by.

Verified at vendoring time: 70 rule files, 70 rules listed in `SKILL.md`, every listed rule backed by a file and no orphan files. Note that the skill's `metadata.json` understates the catalogue as "40+ rules" where `SKILL.md` and the files both say 70; the table above follows the files.

Upstream also ships `composition-patterns`, `deploy-to-vercel`, `react-native-skills`, `react-view-transitions`, `vercel-cli-with-tokens`, `vercel-optimize`, `web-design-guidelines`, and `writing-guidelines`, none of which are taken here.

### wshobson/agents

[data-storytelling](skills/data-storytelling/) comes from [wshobson/agents](https://github.com/wshobson/agents) at commit [`38e19c2`](https://github.com/wshobson/agents/tree/38e19c20d2b154510b0e624a2e3e186b19b5c527/plugins/business-analytics/skills/data-storytelling), MIT licensed, Copyright (c) 2024 Seth Hobson. Vendored byte-identical apart from the added `LICENSE`.

Upstream organises 181 skills under 91 plugins; this one sits in the `business-analytics` plugin alongside `kpi-dashboard-design`, which is not taken here. The nesting is flattened to this repo's one-directory-per-skill layout, and the directory name already matched the skill's frontmatter name.
