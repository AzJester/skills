---
name: component-selection-and-obsolescence
description: Choose parts that will still be available in ten years and prove they are genuine. Use when selecting components for a long-life product, managing DMSMS and end-of-life notices, planning lifetime or bridge buys, establishing counterfeit part avoidance, qualifying distributors, checking country of origin and prohibited sources, or deciding how to respond when a critical part goes obsolete. Hardware parts; supply-chain-security covers the software and firmware supply chain.
---

# Component selection and obsolescence

The defining tension in defense hardware: **commercial silicon lives three to five years; the platform lives twenty to thirty.** Every component you select will go obsolete during the product's service life, most of them several times over. Managing that is not a sustainment activity that starts after delivery — it is a design activity, and the decisions that make it manageable are made when the part is chosen.

`supply-chain-security` covers software and firmware provenance, SBOMs and vulnerability response. This covers the physical parts: whether they will exist, whether they are genuine, and whether you are permitted to use them.

The failure this exists to prevent is a design whose critical component goes end-of-life during qualification, with no alternate identified and no lifetime buy placed.

## Step 1: Select with the whole life in mind

At selection time, for anything on the critical path:

- **Where is the part in its life cycle?** A part introduced two years ago has a different outlook from one that has been shipping for a decade. Both can be right; the difference is what you plan around it.
- **Is there a real second source?** Not a functionally similar part — a form, fit and function alternate you could actually drop in. Where there is none, that is a single point of supply failure and belongs in `risk-management`.
- **Who makes it, and where?** Country of origin, and whether the manufacturer or any of its supply chain falls under a prohibited-source restriction. This is a live compliance issue for communications and video equipment in particular, and it disqualifies parts rather than merely complicating them.
- **What grade is it?** Commercial, industrial, automotive and military temperature grades differ in rated range and in screening. Using a commercial-grade part across a military temperature range is a decision requiring analysis, not an oversight to discover at qualification.
- **Does it have export or trade implications?** Classification and trade agreement compliance affect what you may ship and to whom — see `export-control-and-markings`.

**Prefer parts with long-life or extended-availability programmes** where the performance permits, and accept that they cost more. The cost difference is almost always smaller than one unplanned redesign.

**Concentrate the risk deliberately.** A design using four hundred unique parts has four hundred obsolescence exposures. Reducing unique part count — reuse across boards, standard values, a preferred parts list — is one of the cheapest reliability and sustainment decisions available.

## Step 2: Set up monitoring, because notices arrive without warning

**Product change notices and end-of-life notices are the input to the whole process**, and they arrive on the manufacturer's schedule, not yours. Missing one costs you the last-time-buy window, which is usually the cheapest option you will ever have.

- **Monitor the bill of materials continuously**, through a commercial obsolescence service or directly with the manufacturers. Manual annual checks miss notices.
- **Route notices to someone who acts on them.** A notice landing in a purchasing inbox with no engineering owner is a notice nobody assessed.
- **Assess each one against the design**, not just the part: what uses it, what a change would invalidate, and whether requalification would be triggered.

**The last-time-buy window is short and it is a real deadline.** Deciding what to do usually takes longer than the window allows unless the groundwork is already done.

## Step 3: Know the responses, and their real costs

When a part goes obsolete, the options are known. Choosing between them is the work.

| Response | Means | Costs |
| --- | --- | --- |
| **Existing stock** | Use what is on hand | Nothing, until it runs out |
| **Alternate source** | Qualify a drop-in equivalent | Qualification effort; may be quick if pre-identified |
| **Lifetime or bridge buy** | Buy enough for the remaining life, or to bridge to a redesign | Capital, storage, shelf life, and the forecast being wrong |
| **Aftermarket source** | Authorised aftermarket manufacturer | Cost premium; verify authorisation |
| **Emulation** | A functionally equivalent part manufactured to the original spec | Expensive; used for genuinely irreplaceable parts |
| **Redesign** | Change the design to use available parts | Most expensive; may trigger requalification |

Three disciplines:

**Identify alternates during design, not during a crisis.** A pre-identified and pre-qualified alternate turns an emergency into a purchase order. This is the single highest-return habit in the discipline.

**A lifetime buy is a forecast, and forecasts are wrong.** Size it from a real production and spares projection, add for yield and attrition, and be honest that a demand upside you cannot serve is the failure mode. Also plan the storage: parts have shelf life, moisture sensitivity and solderability limits, and a lifetime buy stored badly is a lifetime buy wasted.

**Understand what a change requalifies.** Substituting a part can invalidate completed environmental or EMC qualification — see `ruggedization-and-environmental-qual` and `emi-emc-and-tempest` — and it is a configuration change under `configuration-management`. That cost belongs in the decision, not after it.

## Step 4: Counterfeit avoidance is a system, not a habit

Counterfeit electronic parts are a real and regulated concern in defense procurement, and contractors are generally required to have a detection and avoidance system with obligations that flow down to suppliers.

The practices that carry most of the weight:

- **Buy from the original manufacturer or its authorised distributors.** This is the single most effective control by a wide margin. The overwhelming majority of counterfeit parts enter through the open market.
- **Where the open market is unavoidable** — which happens for obsolete parts — treat it as a risk-managed exception: qualified brokers, documented traceability back toward the manufacturer, and inspection and test proportionate to the criticality.
- **Inspect and test to a recognised standard.** Visual inspection, marking permanency, X-ray, decapsulation and electrical test each catch different things, and the level applied should follow criticality.
- **Keep traceability records.** Where a part came from, through whom, with what documentation. This is what lets you answer the question after a failure, and answering it is the point.
- **Flow the requirement to suppliers**, including your contract manufacturer — see `teaming-and-subcontracts` and `manufacturing-and-npi`.
- **Report suspect parts** through the required channels. The obligation is real, and the reporting is what protects everyone else.

**Obsolescence and counterfeiting are the same problem viewed twice.** Parts become counterfeit targets precisely because they are obsolete and still in demand. Good obsolescence management is therefore the most effective counterfeit avoidance available.

## Step 5: Plan it as programme work

- **Assign an owner.** Obsolescence management with no owner does not happen; it surfaces as an emergency instead.
- **Prioritise by criticality, not by part count.** Concentrate effort on parts that are single-sourced, hard to replace, or expensive to requalify.
- **Cost it into the estimate.** Monitoring, alternates qualification, lifetime buys and storage are real costs that estimates routinely omit — put them in, per `cost-estimating-and-boe`.
- **Feed the product roadmap.** A technology refresh planned every few years is far cheaper than a series of unplanned redesigns, and it can be aligned with capability improvements rather than forced by a notice — see `technology-roadmapping` and `product-management`.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Life cycle position ignored at selection | Part obsolete during development | Assess life cycle stage when choosing |
| No alternates identified | Every notice is an emergency | Identify and pre-qualify alternates in design |
| Notices unmonitored | Last-time-buy window missed | Continuous monitoring with an engineering owner |
| Lifetime buy from a hopeful forecast | Runs out, or capital wasted | Real projection, plus attrition; plan storage |
| Requalification cost ignored | Substitution costs more than expected | Assess what a change invalidates |
| Open market as routine sourcing | Counterfeit exposure | Manufacturer and authorised distribution first |
| High unique part count | Hundreds of obsolescence exposures | Preferred parts list; reuse across the product |
| Obsolescence unowned and uncosted | Emergencies, unbudgeted | Named owner, priority by criticality, in the estimate |

The honest one: nearly every emergency in this discipline was foreseeable years earlier, and the reason it was not foreseen is that nobody was assigned to look.
