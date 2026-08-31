---
name: incident-response
description: Run a live production incident and close it out properly. Use when something is broken in production right now, a service is down or degraded, an alert fired, users are reporting errors, a deploy needs rolling back, or afterwards when writing the postmortem or the runbook. Covers severity triage, stabilizing before diagnosing, timeline reconstruction, blameless postmortem, and turning the fix into a runbook.
---

# Incident response

An incident is not a bug. A bug is diagnosed at leisure; an incident is bleeding users while you work, and the first job is to stop the bleeding, not to understand it.

This repo already has eight root-cause skills — `rcca-master`, `five-whys-analysis`, `fault-tree-analysis`, `fmea-analysis`, `kepner-tregoe-analysis`, `fishbone-diagram`, `pareto-analysis`, `problem-definition`. They are for design reviews and quality investigations with time to think. Do not reach for them while the pager is going off. Reach for them in step 5, once the incident is closed and you are deciding what to change.

## Step 0: Is this actually an incident?

| Signal | Then |
| --- | --- |
| Users affected now, or data at risk | Incident. Continue. |
| Broken but not user-facing, no data risk | Not an incident. Use `diagnosing-bugs`. |
| Failure already over, want to understand it | Skip to step 4, then step 5. |

Say which one you concluded and why, in one line, before doing anything else.

## Step 1: Severity, out loud

Severity sets how much process the incident gets. Guessing high wastes people; guessing low loses trust.

| Sev | Test | Response |
| --- | --- | --- |
| **1** | Total outage, data loss, or security breach | Everything stops. Communicate every 30 min. |
| **2** | Major feature broken, or severe degradation for many users | Focused response. Communicate hourly. |
| **3** | Minor or partial, workaround exists | Normal working hours. |

State the severity, the user-visible symptom, and the blast radius (who, how many, since when). If you cannot say since when, say that — an unknown start time is itself a finding.

## Step 2: Stabilize before you diagnose

The instinct to understand first is the most expensive instinct in incident response. Mitigation and diagnosis are separate activities, and mitigation wins.

Try, in order:

1. **Revert.** If a deploy correlates with the start time, roll it back. Being wrong costs one deploy; being slow costs users. Do not require proof of causation first.
2. **Disable.** Feature flag off, traffic shifted, non-essential load shed.
3. **Scale or restart.** Buys time when the failure is resource exhaustion or a wedged process.
4. **Nothing safe available.** Say so explicitly and go to diagnosis, having stated that users stay affected meanwhile.

Record the time and content of each mitigation attempt as you make it. Reconstructing this afterwards from memory does not work.

## Step 3: Diagnose under time pressure

Narrow before you deepen. What changed, and what does the failure have in common?

- **What changed** — deploys, config, flags, infrastructure, upstream dependencies, certificate expiry, a scheduled job, traffic shape. Most incidents are a change; a few are a threshold finally crossed.
- **What is common** — one region, one tenant, one code path, one version, one shard. The dimension that separates working from broken is the diagnosis.
- **What the graphs say** — error rate, latency percentiles, saturation, queue depth. Correlate against the start time you established in step 1.

Hold one hypothesis at a time, name the observation that would disprove it, and check that. A hypothesis nobody tried to kill is a guess.

## Step 4: Timeline, from evidence

Build the timeline from artifacts with timestamps: alerts, deploy records, log entries, chat messages, graph inflection points. Not from recollection.

```
14:02  Deploy abc123 to prod (deploy log)
14:06  Error rate 0.1% → 12% (dashboard)
14:11  First alert fires (pager)
14:19  Responder acknowledges (chat)
14:31  Rollback started (deploy log)
14:36  Error rate normal (dashboard)
```

Two numbers fall out of this and both are worth knowing: detection delay (14:06 → 14:11) and time to mitigate (14:11 → 14:36). A long detection delay is a monitoring problem, not a people problem.

## Step 5: Blameless postmortem

Blameless is a technical stance, not a courtesy. "The engineer deployed without testing" ends the investigation; "the pipeline allowed an untested deploy to reach production" continues it. Every time a human appears as a cause, ask what made the wrong action possible or attractive, and put that in the postmortem instead.

Write these sections:

- **Summary** — what broke, for whom, how long, in three sentences.
- **Impact** — users, requests, revenue, data. Numbers, or a stated estimate with its basis.
- **Timeline** — from step 4.
- **Root cause** — this is where the RCCA skills earn their place. Use `five-whys-analysis` for a linear causal chain, `fault-tree-analysis` when several conditions had to coincide, `kepner-tregoe-analysis` when it is unclear which of many changes was responsible.
- **What went well** — genuinely. If detection was fast, say so; the next incident depends on knowing which defenses worked.
- **Action items** — each with an owner and a date. An action item without an owner is a wish.

Sort action items by whether they prevent recurrence, shorten detection, or shorten mitigation. All three are valid; conflating them hides that a "fix" only helps next time it happens.

## Step 6: Runbook

If a human had to reason from scratch during the incident, the next person will too. Write `references/runbook-template.md` filled in for this failure: symptom, how to confirm, how to mitigate, how to escalate, what not to do.

An action item that says "improve monitoring" is not done until an alert exists that would have fired at 14:06 rather than 14:11.

## Reference

- `references/postmortem-template.md` — the document skeleton, ready to fill.
- `references/runbook-template.md` — the per-failure runbook skeleton.
