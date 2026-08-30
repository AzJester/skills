---
name: teaming-and-subcontracts
description: Decide who does the work and on what terms. Use when choosing to prime or sub, negotiating a teaming agreement, defining work share, making a make-or-buy decision, planning small business subcontracting, flowing down clauses to suppliers, checking for organisational conflicts of interest, or managing a subcontractor after award. Engineering and programme consequences of the arrangement, not legal advice.
---

# Teaming and subcontracts

Almost no defense work is performed by one company. The arrangement decided during capture determines who carries risk, who owns the customer relationship, and which problems are yours to fix at two in the morning.

The failure this exists to prevent is a team assembled to win rather than to perform. Those are different optimisations and the difference surfaces after award, when the partner brought in for their past performance turns out to have committed 5% of the work and 100% of the credit.

**This is not legal advice.** Teaming agreements, subcontracts and OCI determinations have real legal consequence and belong with contracts and counsel. What follows is what an engineering and programme leader needs to decide well and to know when to stop.

## Step 1: Prime or sub

A strategic choice, not a default.

| | Prime | Sub |
| --- | --- | --- |
| Customer relationship | Yours | Filtered through the prime |
| Past performance credit | Full, as prime | Partial, and harder to claim |
| Risk | All of it, including partners' | Bounded by your scope |
| Margin | Higher, with more exposed | Lower, more predictable |
| Fit when | You can carry the whole scope and want the position | The scope needs capability you lack, or the position is not winnable as prime |

**Priming something you cannot perform is the expensive mistake.** You inherit every partner's schedule, quality and staffing problem while the customer holds you accountable. Subbing on a pursuit you could have primed costs position and margin, which is recoverable; priming beyond your capacity is often not.

## Step 2: Make or buy, deliberately

Before deciding who to team with, decide what you should not build.

| Consider | Buy or subcontract when | Build when |
| --- | --- | --- |
| **Capability** | You do not have it and cannot economically develop it | It is core to what you sell |
| **Capacity** | You have the skill but not the people in the window | You have both |
| **Risk** | The risk is better carried by a specialist | You can manage it and the margin justifies it |
| **Strategy** | It is not a capability you want to own | It is a discriminator you intend to reuse |
| **Cost** | Genuinely cheaper after integration and management costs | The build-up plus reuse value wins |

Two habits worth keeping: **count the integration and management cost** — a subcontract is not free to run, and the effort to specify, monitor and integrate is routinely omitted from the comparison in `cost-estimating-and-boe`; and **record the decision and its basis**, because it will be revisited, sometimes by an auditor.

## Step 3: Structure the team around scope, not percentages

**Define work share by scope, not by percentage.** "40% of the work" is meaningless until somebody has to say which 40%, and by then the parties have different answers. Define it by WBS element — see `wbs-and-scheduling` — so the boundary is the same one the schedule and the estimate use.

**The seam between partners is an interface** and deserves the same treatment as a technical one: who owns what, what crosses the boundary, what each side assumes about the other, and how a change is agreed. `interface-control` applies directly, and a team that treats its work-share boundary informally will discover it during integration.

**Decide the exclusivity question explicitly.** Whether a partner may bid the same opportunity with someone else, and whether you may replace them, are the two clauses that matter most in a teaming agreement and the two most often left vague to avoid an awkward conversation during capture.

**Get an NDA in place before the technical discussion**, not after. Information exchanged first cannot be un-exchanged.

**Confirm the partner will actually staff it.** The capability demonstrated in the proposal and the people who show up after award are frequently different. Name key personnel, and write in what happens if they are not available.

## Step 4: Small business and set-aside obligations

These are contractual obligations with reporting attached, not goodwill.

- **Where a solicitation is set aside**, eligibility is determined by size standard and programme status, and there are limits on how much of the work may be performed by others. Getting this wrong is disqualifying and, in some circumstances, worse than that.
- **Where you are a large business on a contract above the applicable threshold**, a small business subcontracting plan with goals by category is normally required, and performance against it is reported and evaluated. Goals set to be approved rather than met produce a problem at the first report.
- **Plan the subcontracting mix during capture**, not after award. Finding qualified small business partners in the categories you committed to takes longer than the reporting cycle allows.

Confirm the specifics against the solicitation and with contracts. Thresholds, categories and rules change.

## Step 5: Organisational conflicts of interest

OCI can disqualify you from a competition, including one you helped shape. The common shapes:

| Type | Looks like |
| --- | --- |
| **Unequal access to information** | You hold non-public information from other work that would advantage this bid |
| **Impaired objectivity** | You would be evaluating, advising on, or overseeing your own work or a competitor's |
| **Biased ground rules** | You wrote, or materially influenced, the requirement you are now bidding |

**Check it early**, in qualification rather than at submission — see `capture-management`. Mitigation exists (firewalls, divestiture, recusal) but takes time and sometimes costs the opportunity, and it is the customer who decides whether the mitigation is acceptable. The same analysis applies to your partners: their conflicts can become yours.

## Step 6: Flow down what actually applies

Prime contract clauses do not automatically bind your suppliers. Flow-down is a deliberate act, and both directions of error are expensive.

- **Under-flowing** leaves you contractually obligated for something no supplier is required to deliver — cybersecurity requirements, data rights, quality standards, security obligations, reporting. The gap is yours.
- **Over-flowing** — passing the entire prime contract down verbatim — raises supplier prices for obligations that make no sense at their scope, and small suppliers may simply decline.

The clauses worth deliberate attention: cybersecurity and CUI handling (see `cmmc-readiness`), data and software rights (see `contract-vehicles-and-clauses`), export control (see `export-control-and-markings`), security requirements including the classification specification (see `industrial-security`), quality system requirements, and the deliverables the supplier owes into your CDRLs (see `sow-and-pws`).

**Each subcontract needs its own statement of work**, at the same standard as the prime's. `sow-and-pws` applies unchanged — a supplier SOW written loosely because "we know what we meant" is where the change orders come from.

## Step 7: Manage the subcontract after award

Award is the beginning of the obligation, not the end.

- **Someone owns each subcontract technically**, not only contractually. A supplier with no technical counterpart delivers to the specification's most convenient reading.
- **Insight before the milestone.** Waiting for a delivery to discover the state of the work removes every option except accepting it late. Agree what you see and how often, in the subcontract.
- **The measures apply to suppliers too.** Schedule, cost and technical performance — see `earned-value-management` and `measures-of-effectiveness` where the scope warrants it.
- **Their risks are your risks.** A supplier's staffing, clearance or supply problem reaches your customer as your problem. Carry them in your register — see `risk-management`.
- **Their security posture is your exposure.** See `supply-chain-security`.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Team built to win, not perform | Partner contributes a logo and little else | Define scope, name key personnel, price the work |
| Work share as a percentage | Boundary disputed after award | Define by WBS element |
| Informal partner seam | Integration finds the gap | Treat it as an interface |
| OCI checked late | Disqualified, or mitigation costs the bid | Check at qualification |
| Under-flowed clauses | Prime obligation with no supplier requirement | Deliberate flow-down analysis per clause |
| Loose supplier SOW | Change orders from your own supplier | Same standard as the prime's |
| Subcontracting plan goals unmet | Reported and evaluated | Plan the mix during capture |
| No technical counterpart | Supplier delivers to their own reading | Assign technical ownership per subcontract |

The honest one: the arrangement is decided under time pressure during capture and lived with for years. The half hour spent naming which WBS elements each party owns is the highest-return half hour in the pursuit.
