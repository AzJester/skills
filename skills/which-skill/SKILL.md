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
| Work an opportunity before the RFP | Programme & business | `capture-management`; `teaming-and-subcontracts` for the team |
| Respond to an RFP | Technical writing | `solution-shaping` decides the offer, `proposal-writing` writes it |
| Estimate what something costs | Programme & business | `cost-estimating-and-boe`; `ai-cost-modeling` for AI workloads |
| Plan and schedule the work | Programme & business | `wbs-and-scheduling` builds what `earned-value-management` reads |
| Stand up a programme after award | Programme & business | `program-startup` |
| Plan capability across business units | Programme & business | `technology-roadmapping`; `trl-assessment` for maturity |
| Design a cloud solution | Solution domains | `cloud-architecture`; `rmf-ato` for the authorization |
| Develop a physical product | Hardware | `hardware-product-development` for the lifecycle |
| Run a product, not a contract | Hardware | `product-management`; the contract skills assume a customer SOW |
| Meet an open architecture requirement | Hardware | `mosa-and-open-standards` |
| Make it survive the environment | Hardware | `ruggedization-and-environmental-qual` — 810 is a tailoring framework |
| Fit a size, weight and power envelope | Hardware | `swap-and-thermal-budgeting` |
| Pass the EMC chamber | Hardware | `emi-emc-and-tempest` — start in the first weeks, not at DVT |
| Keep parts available for twenty years | Hardware | `component-selection-and-obsolescence` |
| Get it built repeatably | Hardware | `manufacturing-and-npi` |
| Write the software on the device | Hardware | `embedded-firmware-and-secure-boot`; `devsecops-pipeline` builds it |
| Build a delivery pipeline | Solution domains | `devsecops-pipeline` |
| Replace a system already running | Solution domains | `modernization-and-migration` |
| Make data trustworthy enough to use | Solution domains | `data-strategy-and-governance` — before the AI skills |
| Design for availability and support | Solution domains | `reliability-and-sustainment` |
| Manage hazards to accepted risk | Solution domains | `system-safety`; FTA and FMEA are its techniques |
| Design around the operator | Solution domains | `human-systems-integration` |
| Run a session that must decide | Working across units | `technical-workshop-facilitation` |
| Get a delivered system used | Working across units | `organizational-change` |
| Run or certify a quality system | Working across units | `quality-management-system` |
| Handle classified work | Defense | `industrial-security`; `export-control-and-markings` for markings |
| Meet federal accessibility rules | Defense | `section-508-conformance`; `ui-ux-pro-max` to build it |
| Chase research or prototyping money | Technical writing | `white-paper-and-baa` for BAA, CSO, SBIR and STTR |
| Define the work in a contract | Technical writing | `sow-and-pws`; `contract-vehicles-and-clauses` for what it commits you to |
| Edit someone else's document | Technical writing | `technical-editing` — agree the level of edit first |
| Write instructions someone follows | Technical writing | `procedural-documentation` |
| Report what a test found | Technical writing | `test-report` |
| Brief leadership | Technical writing | `briefing-deck`; `executive-decision-memo` when a deck is wrong |
| Protect an idea before publishing | Technical writing | `invention-disclosure` — before submission, not after |
| Build or test a skill | Documentation & tooling | `plugin-creator`, `skill-tester`, `writing-for-agents` |
| Hand off to another session | Productivity | `handoff` writes a document; `claude-handoff` spawns an agent |

## Distinctions worth stating

These are the overlaps people actually get wrong.

**Incident versus root cause.** `incident-response` is for a live problem — mitigate first, understand later. The RCCA family is for unhurried investigation. Reaching for `five-whys-analysis` while a service is down is the classic error; reaching for it in the postmortem is correct.

**Bug versus incident.** `diagnosing-bugs` assumes you have time to build a reproduction. `incident-response` assumes you do not. The test is whether users are affected right now.

**The diagram skills.** `diagram-picker` interviews you and picks; `architecture-diagrams` renders a spec into draw.io, SVG, PNG and HTML across 36 styles; `omm-scan` extracts architecture from a codebase into `.omm/` docs and needs the `omm` CLI installed. Different jobs despite the shared noun.

**The three modelling skills.** `mbse-sysml` is the modelling practice — which diagram answers which question, how deep to decompose, parametrics for budgets. `digital-engineering` is the strategy around it — what is authoritative, what the digital thread links, whether a twin earns its cost. `system-dev` is this repository's own Design Registry implementation, with typed slots and commands. Reaching for `system-dev` when the question is which SysML diagram to draw is the usual mistake.

**Requirements versus spec.** `requirements-dev` produces formal, verifiable, traceable requirements for a system. `to-spec` produces a spec for a piece of software work and publishes it to a tracker. The first is INCOSE; the second is a ticket.

**The proposal chain.** Three skills in sequence, and using the wrong one wastes the work. `solution-shaping` decides what to offer and stops before writing. `engineering-to-proposal` harvests evidence from delivered work. `proposal-writing` builds the response around Section M. For a BAA, CSO or SBIR the chain is different — `white-paper-and-baa`, because a white paper sells an idea where a proposal demonstrates compliance.

**The pursuit chain, end to end.** `capture-management` runs the pursuit before the RFP and decides bid or no-bid. `solution-shaping` decides what to offer. `engineering-to-proposal` harvests the evidence. `cost-estimating-and-boe` prices it. `proposal-writing` writes it. `program-startup` stands it up after award. Reaching for `proposal-writing` when the RFP has not dropped yet means the pursuit is already a year behind.

**Product versus programme.** The contract skills — `requirements-dev`, `sow-and-pws`, `program-startup`, `earned-value-management` — assume a customer who specified the work and is funding it. `product-management` inverts that: you decide, you fund it, you recover across units. Running a product like a programme produces something built to one customer's specification and sold once.

**Surviving versus fitting.** `ruggedization-and-environmental-qual` is about surviving the environment — shock, vibration, temperature, ingress. `swap-and-thermal-budgeting` is about fitting the envelope — size, weight, power, cooling. Thermal appears in both: thermal *design* is a budgeting problem and lives in SWaP; thermal *testing* is a qualification method and lives in ruggedization.

**The three planning skills.** `wbs-and-scheduling` builds the WBS and the schedule. `cost-estimating-and-boe` prices them. `earned-value-management` measures performance against the resulting baseline. They run in that order and each depends on the one before.

**Writing versus formatting.** The technical writing skills cover documents you produce — proposals, procedures, test reports, work statements, briefings. The technical publishing skills (`ieee-paper`, `acm-paper`, `apa-7`, `chicago-turabian`, `dod-technical-report`, `nasa-sti`, `latex-authoring`) cover formatting for a venue that has published requirements. `technical-editing` applies to all of them.

**The grilling trio.** `grilling` is model-invocable and can be reached automatically; `grill-me` and `grill-with-docs` are user-invoked only, and the latter writes ADRs and glossary entries as it goes. Pick by whether you want documentation to fall out of the session.

## When nothing fits

Say so rather than routing to the nearest thing. A skill applied to the wrong task costs more than no skill, because its structure will be followed anyway.

If the gap looks recurring rather than one-off, `plugin-creator` builds a new skill and `writing-for-agents` covers how to write one that triggers reliably.
