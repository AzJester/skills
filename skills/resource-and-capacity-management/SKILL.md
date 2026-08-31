---
name: resource-and-capacity-management
description: Match the people you have to the work you have committed to. Use when planning staffing across several programs, assessing whether the organization can deliver what it is bidding, managing a matrix where people report two ways, setting utilization targets, planning hiring against need dates and clearance lead times, or diagnosing why every program is short-staffed while utilization looks high.
---

# Resource and capacity management

`program-startup` staffs one program. `structured-interviewing` hires one person. This is the layer above both: whether the organization can actually supply what it has committed to, across everything running and everything being bid at once.

The failure this exists to prevent is the staffing profile that was credible in each proposal separately and is impossible in aggregate — which is discovered after the wins, when three programs need the same six cleared engineers in the same quarter.

## Step 1: Know what you actually have

Not headcount. Capacity is people, with specific skills, actually available.

Subtract honestly from headcount: leave, training, non-billable overhead, proposal and bid support, internal investment, onboarding time for anyone recent, and the fraction of senior people's time consumed by everything other than the work.

**Maintain a skill inventory that reflects reality**, including clearance status and eligibility — see `industrial-security`. On classified work, a cleared engineer and an uncleared one with identical skills are not interchangeable resources, and treating them as the same number is how a plan becomes fiction.

**Distinguish the constrained few from the general many.** Most organizations have a handful of people who are on every critical path — the one person who knows the legacy interface, the only cleared architect, the sole authority on a qualification. Capacity planning that averages across headcount hides exactly the constraint that will bind.

## Step 2: Know what you have committed to, and what you might

| Demand | Certainty | Treat as |
| --- | --- | --- |
| **Running programs** | Committed | Full requirement, by month, by skill |
| **Won, not yet started** | Committed | Full requirement, with ramp |
| **Bids submitted** | Probabilistic | Weighted by an honest pWin — see `capture-management` |
| **Pursuits in capture** | Speculative | Weighted, and low |
| **Internal investment** | Discretionary | Real, and the first thing raided |
| **Proposal and bid support** | Recurring | Real, and consistently unplanned |

**Weight the pipeline honestly or the plan is decoration.** An organization planning as though it will win everything is over-committed; one planning as though it will win nothing has no people ready when it does. The weighted view is the only useful one, and it depends on pWin assessments that are scored rather than felt.

**Bid and proposal effort is real capacity consumption**, and it consistently comes from the same senior people the programs need. Planning it as though it is free is one of the most common causes of program staffing shortfalls.

## Step 3: Understand why high utilization makes everything late

The counter-intuitive result that most capacity problems come down to.

**As utilization approaches 100%, waiting time rises sharply rather than smoothly.** A system loaded near its capacity has no absorptive slack, so any variation — an illness, a slipped dependency, a surprise — propagates instead of being absorbed. This is a property of loaded systems generally, and it is why an organization at 98% planned utilization delivers later than one at 85%, despite doing less work on paper.

Three consequences worth acting on:

**Target utilization below full.** The right number depends on how variable the work is, but planning every person to full allocation guarantees that nothing can absorb a surprise, and surprises are certain.

**Multitasking is not free.** Splitting a person across three programs does not give each a third of them; context switching and coordination take a real cut, and each program experiences them as unreliable. Fewer, longer allocations deliver more.

**Protect the constrained people.** The individuals on every critical path should be the least fragmented, not the most. In practice they are usually the most, because everyone needs a piece of them.

## Step 4: Manage the matrix without pretending it is not one

Where people report functionally and are assigned to programs, two authorities exist and the ambiguity is the point of friction.

- **Decide who allocates and who directs.** Typically the functional manager owns who goes where and their development; the program directs the work. Write it down — undefined, it is settled repeatedly by whoever escalates hardest.
- **One allocation decision-maker across programs.** Peer negotiation between program managers for the same scarce person produces the loudest winning, not the best outcome.
- **Escalation needs to be fast.** A resource conflict that takes three weeks to resolve has already cost more than either resolution.
- **Career development belongs to someone.** In a matrix it falls between the two roles, and the people who leave are usually the constrained ones you could least afford to lose.

## Step 5: Hire against need dates, not against gaps

- **Work backwards from the need date** through offer, notice period, onboarding and — on classified work — clearance processing. That total is frequently six months or more, and it means hiring decisions must be made well before the gap appears.
- **Where the gap is inside the lead time, hiring is not the answer.** The options are subcontract or teaming (`teaming-and-subcontracts`), descope, re-sequence, or decline the work. Planning a hire that cannot arrive in time is a way of not deciding.
- **Cleared staff are a competitive market and a constrained supply.** A plan that assumes hiring cleared people at will is a risk, not a plan — carry it in `risk-management`.
- **Count the ramp.** New people consume the experienced ones for a period before contributing. On a late program, that is a cost before it is a benefit — see `program-recovery`.

## Step 6: Feed it back into what you bid

This is where capacity management earns its keep, and where it is most often ignored.

- **Capacity is a bid/no-bid input.** "Can we perform?" is one of the qualification questions in `capture-management`, and it should be answered from the capacity plan rather than from optimism.
- **Test the aggregate, not each bid.** Model what happens if you win everything currently bid. Where that is impossible, decide now which you would rather win and act accordingly — including no-bidding something.
- **The staffing profile in a proposal is a commitment.** Key personnel are contractual, and proposing people who are committed elsewhere is a promise that will be tested at award.
- **Feed real ramp rates and availability into estimates**, not idealized ones — see `cost-estimating-and-boe`, where an unachievable staffing profile is a cost estimate defect as much as a resourcing one.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Headcount treated as capacity | Plans that cannot be executed | Subtract leave, overhead, B&P, onboarding |
| Pipeline unweighted | Over- or under-committed | Weight by honest pWin |
| Planning at full utilization | Everything late despite high utilization | Target below full; keep absorptive slack |
| Constrained people fragmented | The critical path is one distracted person | Protect them; fewer, longer allocations |
| Cleared and uncleared counted alike | Plan fails at award | Track clearance status in the inventory |
| Allocation by peer negotiation | Loudest program wins | One decision-maker, fast escalation |
| Hiring inside the lead time | The gap persists anyway | Work backwards from need dates; otherwise subcontract or descope |
| Aggregate never modeled | Three wins, six engineers | Model winning everything bid |

The honest one is the last, and it is a leadership question rather than a planning one: which of the things you are currently bidding would you rather not win, and does anyone know the answer?
