---
name: technical-pilot
description: Run a pilot or proof of concept that leads somewhere. Use when scoping a POC with a customer, agreeing success criteria before it starts, planning the access, data and accreditation lead times that usually kill pilots, choosing pilot users, instrumenting it for evidence, or deciding whether to transition, iterate or stop at the end. The transition plan exists before the pilot does, or it is a demo.
---

# Technical pilot

**The standard outcome of a pilot is that it succeeds and then dies.** Everyone is pleased, the users liked it, the report is positive, and nothing follows — because no money was identified, no contract vehicle existed, and the sponsor moved on.

That is the failure this skill exists to prevent, and the fix is almost entirely in the setup. `verification-validation` names pilot deployment as a validation method and `trl-assessment` counts it as maturity evidence; neither covers running one, and running one badly is cheap to do.

## Step 1: Establish what decision this pilot informs

A pilot is an experiment that buys a decision. Name the decision first.

- **Whose decision, and when will they make it?** A pilot with no decision-maker waiting on it is a demonstration.
- **What would make the answer yes, and what would make it no?** Both, in advance, in writing. A pilot that cannot fail proves nothing, and a pilot whose criteria are settled afterwards is settled in favor of whoever is most invested.
- **What happens next if it succeeds?** This is the question that separates pilots that transition from pilots that do not. See Step 2.

**Write success criteria that are measurable and that the customer agrees to before it starts.** "Users found it valuable" is not a criterion. "Analysts complete the triage task in under four minutes with fewer than 5% escalation errors, on real data, across three weeks" is one — and it tells everyone what to instrument.

**Scope it to prove one thing.** A pilot built to impress covers breadth and proves nothing conclusively. A pilot built to answer one question can actually answer it, and a narrow pilot that convincingly answers its question beats a broad one that leaves everything arguable.

## Step 2: Plan the transition before the pilot starts

**The single highest-value thing in this skill.** If the answer to "what happens if this works?" is unclear at the start, it will be unclear at the end, when the enthusiasm has moved elsewhere.

Establish, before launch:

- **Who funds production**, from which appropriation or budget line, in which fiscal year.
- **Which contract vehicle** the follow-on could go on, and whether it exists — see `capture-management` and `contract-vehicles-and-clauses`.
- **What accreditation the production system would need**, and how long that takes — `rmf-ato`. Frequently longer than the pilot itself.
- **Who owns it operationally** afterwards. A capability with no operational owner is not sustainable regardless of how well it performed.
- **The realistic timeline** from a successful pilot to fielded capability. Say it out loud, because it is usually much longer than anyone assumes and it changes how the pilot should be scoped.

**Where there is no plausible transition path, say so and decide deliberately.** A pilot run purely to learn, or to build a relationship, is legitimate — but it should be chosen knowingly rather than discovered afterwards.

## Step 3: Start the lead-time items on day one

Pilots are rarely killed by technology. They are killed by access.

| Item | Typical lead time |
| --- | --- |
| **Data access** — agreements, sanitization, transfer approvals | Weeks to months, and the most common blocker |
| **Network access** — getting on the network at all, accounts, boundary approvals | Weeks to months |
| **Accreditation** — even an interim or limited authority to test | Months; see `rmf-ato` |
| **Security** — clearances, facility access, visit requests | Months; see `industrial-security` |
| **Users** — identified, freed from other duties, trained | Longer than anyone plans |

**Start all of them at kickoff, in parallel with the build.** A pilot whose software is ready in week four and whose data access arrives in week fourteen has a ten-week hole in it, and that hole is where sponsor attention is lost.

**Where the data cannot be obtained in time, change the pilot rather than the timeline.** A pilot on synthetic or sanitized data proves much less, and it is better to know that and scope the claim accordingly than to present a lab result as an operational one.

## Step 4: Run it in conditions that resemble reality

- **Real users, not enthusiasts.** The volunteer who loves new tools tells you the ceiling; you need the median operator on a normal day. `organizational-change` covers picking a pilot group that will tell you the truth.
- **Real data, real environment, real constraints.** Connectivity, classification, the actual hardware, the actual workload. A pilot in a laboratory answers a laboratory question.
- **Long enough to pass the novelty period.** Early enthusiasm decays; the interesting data is what usage looks like in week six. A two-week pilot measures novelty.
- **Instrument it for evidence, not impressions.** Usage, task completion, time, error rates, escalations, abandonment. Decide what to capture before starting — retrofitted measurement produces anecdote. For AI capabilities, `ai-evaluation` applies to the pilot as much as to development.
- **Capture what people work around.** Where users route around the system, they know something the design does not.
- **Support it properly.** A pilot with no support generates a bad reputation that outlives the pilot.

## Step 5: End it deliberately

**Decide, do not extend.** The most common ending is an indefinite extension, which is a free service delivered without a contract, consuming engineers who are no longer funded, with no decision ever made. Set the end date at the start and hold it.

The honest outcomes are:

| Outcome | Means |
| --- | --- |
| **Transition** | Criteria met, path exists — execute the plan from Step 2 |
| **Iterate** | Promising, one specific question unresolved — a second, narrower pilot with new criteria |
| **Stop** | It did not work, or it worked and there is no path. Say which |

**Report honestly, including what it does not establish.** `test-report` applies directly — its limitations section is the part that decides whether anyone trusts the rest. A pilot report claiming more than the pilot supports is discovered, and it costs the next one.

**Feed the result into `lessons-learned`**, and into `trl-assessment` where the pilot was maturity evidence. A pilot that ends without its evidence being recorded has to be re-run by somebody.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| No transition plan | Succeeds and dies | Funding, vehicle, accreditation and owner named before launch |
| Criteria set afterwards | Settled by whoever is most invested | Measurable criteria agreed before starting |
| Built to impress | Broad, proves nothing | Scope to one question |
| Access started late | Ten-week hole; sponsor attention lost | Every lead-time item begins at kickoff |
| Enthusiast users | Ceiling measured, not the median | Representative users on a normal day |
| Too short | Measures novelty | Long enough to pass the novelty period |
| Uninstrumented | Anecdote instead of evidence | Decide the measures before starting |
| Extended indefinitely | Unfunded service, no decision | Fixed end date; decide at it |

The honest one is the first, and it is worth asking before a pilot is agreed rather than after: if this works perfectly, who writes the contract, and with what money?
