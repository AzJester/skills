# skills

A personal collection of Claude / AI agent skills.

## Layout

Each skill lives in its own directory under `skills/`, with a `SKILL.md` entry point at the directory root. Most skills also carry a `.claude-plugin/plugin.json` manifest so they can be installed as Claude Code plugins.

## Skills

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

## Attribution

All skills above were vendored unmodified from [ddunnock/claude-plugins](https://github.com/ddunnock/claude-plugins) at commit [`e22db30`](https://github.com/ddunnock/claude-plugins/tree/e22db30ce9da9ff3686cda59edd8855443451ba0/skills), authored by David Dunnock and redistributed under the MIT License (a copy is included in each skill directory).

Omitted from the copy: the upstream author's internal planning history (`system-dev/.planning/`) and a committed code-index artifact (`concept-dev/.codegraph/`). All functional content (SKILL.md files, commands, agents, schemas, scripts, templates, tests, references, data, plugin manifests) is included unmodified.

Known upstream test-suite quirks at this commit (vendored as-is): 6 ReqIF-export tests fail in `requirements-dev` and one stale test module (`test_report_gen.py`) in `skill-tester` imports a function its script no longer exports; both reproduce identically in the upstream repository. The upstream repo also hosts MCP servers (`session-memory`, `knowledge-mcp`) that are not part of this skills collection.
