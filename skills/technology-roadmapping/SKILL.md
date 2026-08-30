---
name: technology-roadmapping
description: Decide what capability to build, when, and for whom across a portfolio. Use when building a technology or capability roadmap, allocating internal research and development investment, deciding what to build once and share across business units, sequencing technology maturation against programme need dates, setting kill criteria for an investment, or reconciling roadmaps that several units maintain separately.
---

# Technology roadmapping

The skill for anyone who has to answer the same capability question for several business units at once, and would prefer to answer it once.

A roadmap is not a schedule of projects. It is an argument that a set of capabilities, matured in a particular order, will be ready when specific opportunities need them. The argument is what makes it useful; the timeline is just how it is drawn.

The failure this exists to prevent is a roadmap built by collecting what each unit already intended to do and drawing it on one page. That produces a picture of current spending, not a plan, and it hides the two things a portfolio view exists to find: duplication, and gaps nobody owns.

## Step 1: Start from demand, not from technology

Three questions, in this order. Reversing them produces a roadmap of interesting technology with no customer.

1. **What capability will be needed, by whom, and when?** From pursuit pipelines, customer roadmaps, published strategy and budget documents, and programmes already running. `capture-management` is the demand signal for the pursuit side.
2. **What do we have today, honestly?** Present maturity, not intended maturity. `trl-assessment` is the instrument, and using it here rather than at proposal time is what makes the roadmap credible.
3. **What is the gap, and what would close it?** The distance between the two, expressed as work.

**The need date drives everything backwards.** A capability required at TRL 6 for a pursuit eighteen months out, currently at TRL 3, defines the maturation plan and tells you immediately whether it is feasible. Building the plan forwards from what is convenient produces roadmaps that arrive after the opportunity.

## Step 2: Find what is duplicated and what nobody owns

This is the specific value of looking across units rather than within one.

**Duplication.** Two or three units independently building similar capability is the most common finding, and it is rarely visible from inside any one of them. Not all of it should be consolidated — a shared component with three unwilling customers is worse than three purpose-built ones. The test is whether the units would genuinely adopt a shared version, which is a question to ask them before deciding, not after.

**Gaps.** Capability several units need and none is funding, usually because it is nobody's programme and therefore nobody's budget. These are the highest-value items a portfolio view finds and the hardest to fund, because the cost is concentrated and the benefit is distributed.

**Build once, share deliberately.** Shared capability needs a named owner, a funding line, and consumers who have agreed to use it. Without all three it becomes an orphan that each unit works around. `interface-control` applies — the seam between a shared component and its consumers is an interface with two parties.

## Step 3: Sequence by dependency and horizon

**Map the dependencies before the dates.** Some capabilities require others first. A roadmap drawn as parallel swim lanes usually hides a dependency that makes half of it infeasible.

Separating the portfolio by horizon keeps near-term delivery from consuming everything:

| Horizon | Character | Judged by |
| --- | --- | --- |
| **Near** | Committed, funded, needed by a known pursuit or programme | Delivery against the need date |
| **Mid** | Probable demand, maturation underway | Progress against maturation milestones |
| **Far** | Exploratory, may not pay off | Whether the uncertainty is being reduced |

**Fund the horizons separately, or the near term will eat the others.** Under any pressure, work with a named customer wins against work without one. That is rational each time and fatal repeated, because it consumes the pipeline that produces future discriminators. Protecting the allocation is the decision; enforcing it is a discipline.

## Step 4: Treat investments as investments

Internal research and development, and bid and proposal money, are finite and their treatment carries accounting and contractual consequence. Work with finance on allowability and structure — the engineering decision is which bets to place.

**Every investment states, before it starts:**

- The capability it produces and which pursuits or programmes need it.
- The maturity target — a TRL, with the evidence that would demonstrate it.
- The decision it is buying: what will be known at the end that is not known now.
- **The kill criteria.** What would have to be true to stop.

**Kill criteria are the part that gets omitted, and the reason portfolios ossify.** Without them, an investment that is not working continues because stopping requires someone to volunteer a failure. Written at the start, stopping becomes the plan working rather than a defeat.

**Review the portfolio on a fixed cadence**, and actually stop things. A review that never terminates anything is a status meeting. `business-case` covers arguing a single investment; this is about the set.

## Step 5: Make it a communication instrument

A roadmap is read by more people than build it, and most of them want different things from it.

- **One page that carries the argument** — capabilities, need dates, dependencies — plus the detail underneath for whoever needs it.
- **Show maturity honestly**, using `trl-assessment` levels backed by evidence. A roadmap showing everything as nearly ready is the version that gets believed once.
- **Distinguish committed from intended from aspirational.** The most common misuse of a roadmap is a customer or a proposal team treating an exploratory item as a commitment. Mark it on the page.
- **Date it and version it.** Roadmaps circulate and get quoted long after they are current.
- **Update it when the demand signal changes**, not annually. A roadmap refreshed once a year is describing last year's opportunities.

See `briefing-deck` for presenting it and `executive-decision-memo` for getting an allocation decision made.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Bottom-up collection | A picture of current spending | Start from demand and need dates |
| Technology-first | Capability with no customer | Demand, then gap, then plan |
| Duplication invisible | Three units building the same thing | Portfolio view; test willingness to adopt |
| Shared capability unowned | Everyone works around it | Named owner, funding line, agreed consumers |
| Horizons funded together | Near term consumes everything | Separate allocations, protected |
| No kill criteria | Failing investments continue indefinitely | Kill criteria written before start |
| Reviews that never stop anything | Status meeting in a portfolio's clothing | Terminate at least the worst item each cycle |
| Optimistic maturity | Roadmap believed once, then discounted | TRL with evidence |

The honest one: a roadmap's value is entirely in what it declines to do. One that includes everything anyone proposed has made no decisions and will not survive contact with a budget.
