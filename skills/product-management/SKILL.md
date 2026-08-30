---
name: product-management
description: Run a product rather than a programme. Use when defining a product from market need rather than a customer SOW, setting unit cost targets and amortising development, deciding SKU and configuration strategy, prioritising a product backlog against demand from several customers, planning a technology refresh, or deciding whether to build a product at all versus bid the work. Distinct from program-startup and the contract skills, which assume a customer who specified the work.
---

# Product management

Almost everything else in this repository assumes a customer who told you what to build and is paying for the development: `requirements-dev`, `sow-and-pws`, `program-startup`, `earned-value-management`. A product inverts all of it. You decide what to build, you fund the development, and you recover it across units you have not sold yet.

That inversion changes the economics, the decision rights and the failure modes. Running a product like a programme produces something built to one customer's specification and sold once — which is a contract with extra steps and worse margin.

## Step 1: Know which one you are actually running

| | Programme | Product |
| --- | --- | --- |
| Requirements from | The customer's SOW | Many users, none of whom specified it |
| Development funded by | The contract | You, recovered across units |
| Success is | Delivering to the contract | Units sold at a margin, repeatedly |
| Scope changes via | The changes clause | Your own roadmap decision |
| Risk of being wrong | Managed with the customer | Yours entirely |
| The dangerous failure | Overrun | Building something nobody buys |

**The honest question early: is this a product, or a contract you are hoping to repeat?** A "product" with one customer, built to their requirements, funded by their programme, is a contract. That may be the right business — but calling it a product leads to investing in configurability, documentation and support that a single-customer contract does not repay.

**A second customer is the test.** Until someone who did not shape the design buys it, the product hypothesis is unproven.

## Step 2: Define it from demand, not from a single customer

- **Talk to users who are not your sponsor.** The most common product failure in a contracting organisation is building a generalised version of the last programme's deliverable, which turns out to fit only that programme.
- **Separate what is genuinely common** across customers from what one customer needed. The common part is the product; the rest is configuration, integration work, or out of scope.
- **Write requirements you own.** You are the requirements authority, which means you also carry the consequence of being wrong. `requirements-dev` still applies to writing them well; what changes is who decides.
- **Find the constraint that actually blocks adoption.** For tactical edge hardware this is often not performance — it is SWaP, an accreditation position, a platform interface, or a certification the customer cannot get without you. Solving that beats another increment of throughput.

## Step 3: Get the unit economics right, because they set everything

- **Set a unit cost target early and design to it.** Cost is designed in, not negotiated later. A design that meets every requirement at twice the target price is a failed design, and by the time it is known the decisions that caused it are frozen.
- **Track bill of materials cost continuously**, not at the end. It only goes up during development, and each increase is small and defensible on its own.
- **Amortise development honestly.** Non-recurring cost recovered across a volume forecast you believe, not one that makes the business case work. State the break-even volume explicitly — it is the number that determines whether this is a business.
- **Price against value and the alternative**, not cost plus a margin. On a defense product the alternative is frequently a custom development programme, which is expensive and slow — that comparison is where the value sits.
- **Count the whole cost of being a product company**: qualification, certification, documentation, spares, technical support, sustaining engineering and obsolescence management. These are ongoing and they are what people mean when they say products are harder than they look. See `cost-estimating-and-boe` and `reliability-and-sustainment`.

## Step 4: Decide the configuration strategy deliberately

The question every hardware product faces: one thing, or many variants?

- **Every variant multiplies cost across the whole life** — qualification, documentation, spares, test fixtures, firmware builds and support all fork. A second variant is rarely half the cost of the first product; it is often more than a quarter of it, forever.
- **Prefer configuration over variants.** One qualified hardware platform with configurable firmware, populated options or accessory modules beats three part numbers. This is where `mosa-and-open-standards` pays commercially as well as contractually — modular interfaces let a customer configure without you creating a variant.
- **Define what a "supported configuration" is**, and hold the line. Products die from a long tail of one-off variants each sold once, each requiring support forever.
- **Price the special.** Where a customer genuinely needs a variant, it is non-recurring engineering they pay for, plus a decision about whether it joins the catalogue.

## Step 5: Run a roadmap you can defend

- **Prioritise against demand across customers**, not by whoever asked most recently or most loudly. A named opportunity with a date beats an enthusiastic request.
- **Plan the technology refresh rather than being forced into one.** Component obsolescence will force a redesign eventually — see `component-selection-and-obsolescence`. A refresh planned every few years absorbs that and adds capability at the same time; one triggered by an end-of-life notice does neither.
- **Say no explicitly, and record it.** A roadmap that has never declined anything is a wish list, and it will not survive a budget.
- **Separate the product roadmap from the capability portfolio.** `technology-roadmapping` covers investment across business units; this is one product's plan, and it should feed that rather than duplicate it.

## Step 6: Sell it, support it, and keep it alive

- **Sales needs a technically honest story**, including limits. A product oversold into a mission it does not fit generates support cost, a bad reference, and an engineering team fixing something that was never going to work.
- **The evaluation unit is a sales instrument.** For hardware, getting a unit into a customer's hands early beats any amount of literature — and it also generates the requirements feedback you cannot get any other way.
- **Support is a product feature.** Response time, spares availability, and repair turnaround are frequently what a defense customer actually evaluates once the technical comparison is close.
- **Watch adoption, not shipment.** Units delivered and sitting in a store are not adoption — see `organizational-change`.
- **Decide end of life deliberately**, with notice and a transition path. A product quietly starved of engineering while still being sold damages the customer relationship more than an announced end of life.

## Where this connects

`capture-management` and `proposal-writing` sell into contracts; this sells a product, and the two frequently meet when a product is offered as part of a bid — the discriminator case in `solution-shaping`. `hardware-product-development` builds it. `manufacturing-and-npi` produces it. `technology-roadmapping` places it in the portfolio. `business-case` argues the investment.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| A contract called a product | Configurability built, sold once | Test the hypothesis with a second customer |
| Generalising the last deliverable | Fits only the original programme | Define from demand across customers |
| Unit cost addressed late | Meets requirements, unsellable price | Target early; track BOM continuously |
| Break-even volume unstated | Business case unfalsifiable | State it; test whether you believe it |
| Variant proliferation | Cost forks forever, margin gone | Configuration over variants; price the special |
| Roadmap by loudest request | No coherent product, no discriminator | Prioritise against demand with dates |
| Refresh forced by an EOL notice | Redesign with no added capability | Plan the refresh |
| Support treated as overhead | Loses evaluations on the non-technical half | Treat support as a product feature |

The honest one is the first, and it is worth asking bluntly before the investment: who is the second customer, and what makes you think they will buy this?
