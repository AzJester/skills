---
name: which-skill
description: Find the right skill in this collection for the task at hand. Use when unsure which skill applies, when several look like they overlap, when a search of the skill list came back ambiguous, or when asked what is available for a kind of work. Routes across the whole repository rather than any one family.
disable-model-invocation: true
argument-hint: "[what you are trying to do]"
---

# Which skill

A router over this collection. `ask-matt` covers only the engineering-workflow family it shipped with; this one covers everything.

## How to route

Do not pattern-match on nouns. "Diagram" appears in five skills that do different jobs. Route on **what stage of work the user is in**, which is usually recoverable from their verb.

Read `README.md` for the current list before answering — it is maintained alongside the skills and this file is not. Use the map below to narrow to a section, then read that section's table.

| They are trying to… | Look under | Notable |
| --- | --- | --- |
| Decide whether an idea is worth building | Systems engineering | `concept-dev` for the lifecycle; `grilling` to stress-test |
| Turn an idea into requirements | Systems engineering | `requirements-dev`, `system-dev` for INCOSE rigour |
| Build a system model | Systems engineering / Digital engineering | `mbse-sysml` for SysML practice; `digital-engineering` for the strategy around it |
| Choose between options | Systems engineering | `trade-study-analysis` (DAU 9-step) |
| Sharpen thinking before committing | Productivity | `grilling` (model-invocable), `grill-me` (user-only), `grill-with-docs` (also writes ADRs) |
| Turn a conversation into work items | Engineering workflow | `to-spec` then `to-tickets`; `wayfinder` when it exceeds one session |
| Build the thing | Engineering workflow | `implement` drives `tdd`; `prototype` when the question is still open |
| Review code | Engineering workflow | `code-review` |
| Fix something broken | Engineering workflow / Incident | `diagnosing-bugs` if it can wait; `incident-response` if users are affected now |
| Find out why something failed | RCCA | `rcca-master` routes the eight; use after the incident is closed, not during |
| Secure a design | Security | `threat-modeling` |
| Draw a picture of a system | Architecture diagrams | `diagram-picker` if unsure what to draw; `architecture-diagrams` to render |
| Design or fix an interface | UI & UX | `ui-ux-pro-max`; `vercel-react-best-practices` for React performance |
| Write documentation | Documentation | `documentation-architect` |
| Write prose or an article | Productivity | `writing-fragments` → `writing-shape` → `writing-beats` |
| Present analysis to people | Analytics communication | `data-storytelling` |
| Turn delivered work into proposal material | Proposal bridge | `engineering-to-proposal` |
| Build or test a skill | Documentation & tooling | `plugin-creator`, `skill-tester`, `writing-for-agents` |
| Hand off to another session | Productivity | `handoff` writes a document; `claude-handoff` spawns an agent |

## Distinctions worth stating

These are the overlaps people actually get wrong.

**Incident versus root cause.** `incident-response` is for a live problem — mitigate first, understand later. The RCCA family is for unhurried investigation. Reaching for `five-whys-analysis` while a service is down is the classic error; reaching for it in the postmortem is correct.

**Bug versus incident.** `diagnosing-bugs` assumes you have time to build a reproduction. `incident-response` assumes you do not. The test is whether users are affected right now.

**The diagram skills.** `diagram-picker` interviews you and picks; `architecture-diagrams` renders a spec into draw.io, SVG, PNG and HTML across 36 styles; `omm-scan` extracts architecture from a codebase into `.omm/` docs and needs the `omm` CLI installed. Different jobs despite the shared noun.

**The three modelling skills.** `mbse-sysml` is the modelling practice — which diagram answers which question, how deep to decompose, parametrics for budgets. `digital-engineering` is the strategy around it — what is authoritative, what the digital thread links, whether a twin earns its cost. `system-dev` is this repository's own Design Registry implementation, with typed slots and commands. Reaching for `system-dev` when the question is which SysML diagram to draw is the usual mistake.

**Requirements versus spec.** `requirements-dev` produces formal, verifiable, traceable requirements for a system. `to-spec` produces a spec for a piece of software work and publishes it to a tracker. The first is INCOSE; the second is a ticket.

**The grilling trio.** `grilling` is model-invocable and can be reached automatically; `grill-me` and `grill-with-docs` are user-invoked only, and the latter writes ADRs and glossary entries as it goes. Pick by whether you want documentation to fall out of the session.

## When nothing fits

Say so rather than routing to the nearest thing. A skill applied to the wrong task costs more than no skill, because its structure will be followed anyway.

If the gap looks recurring rather than one-off, `plugin-creator` builds a new skill and `writing-for-agents` covers how to write one that triggers reliably.
