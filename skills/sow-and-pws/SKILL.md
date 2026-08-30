---
name: sow-and-pws
description: Write the document that defines the work. Use when drafting or reviewing a statement of work, performance work statement, statement of objectives or specification, selecting CDRLs and data item descriptions, writing measurable performance standards or a quality assurance surveillance plan, or diagnosing why a scope disagreement or change order keeps recurring. Covers writing the work description; contract-vehicles-and-clauses covers what the resulting contract commits you to.
---

# SOW, PWS and specifications

`contract-vehicles-and-clauses` covers what a contract type and its clauses commit you to. This covers writing the document that says what the work *is* — the one every later scope argument gets settled against.

The failure this exists to prevent is a work description that reads clearly to the person who wrote it and ambiguously to everyone else. Ambiguity in this document does not stay a writing problem: it becomes a change order, a cost overrun, or a dispute, and it becomes those things eighteen months later when nobody remembers what was meant.

## Step 1: Pick the right instrument

Three documents that are routinely confused, and the choice changes who owns the risk of the approach being wrong.

| Instrument | Says | Government supplies | Contractor supplies | Risk of the method sits with |
| --- | --- | --- | --- | --- |
| **SOO** | The objectives to be achieved | Objectives only | The PWS and the approach | Contractor |
| **PWS** | The outcomes required and how they are measured | Outcomes, standards, measures | The method | Contractor |
| **SOW** | The work to be performed, prescriptively | Tasks, methods, sequence | Execution | Government |

**The prescription test:** the more the document specifies *how*, the more the government owns the outcome of that method being wrong. A directive SOW that names the tools and the sequence has told the contractor what to do, and undercuts holding them accountable for whether it worked.

Federal policy favours performance-based work statements where the outcome can be described and measured. That preference is real but it is not universal: where the method genuinely matters — safety, interoperability, a mandated process — prescribe it deliberately and accept that you now own it.

**Specifications are a fourth thing, not a variant.** A specification says what the *product* must be; a SOW or PWS says what *work* must be done. Requirements on the delivered item belong in the specification (see `requirements-dev` for writing them well, and MIL-STD-961 where a defense specification format governs); tasks, meetings, reports and support belong in the work statement. Putting product requirements in the SOW is the most common structural error, and it makes both documents impossible to verify — the spec is incomplete and the SOW contains things no one performs.

## Step 2: Write a PWS that can actually be measured

A performance work statement is only performance-based if someone can tell, from evidence, whether the standard was met.

Every performance requirement carries four parts:

| Part | Is | Failure mode |
| --- | --- | --- |
| **Outcome** | What must result | Written as an activity rather than a result |
| **Standard** | The measurable threshold | "Timely", "as required", "high quality" |
| **Method of surveillance** | How it is observed | Undefined, so it is never checked |
| **Consequence** | What follows from missing it | Absent, so the standard is advisory |

**The standard has a number or a defined observable.** "Respond promptly to outages" is not a standard. "Acknowledge a Priority 1 outage within 15 minutes and restore service within 4 hours, measured from the ticket timestamp, during the hours in paragraph 3.2" is.

**An acceptable quality level is a decision, not a formality.** 100% is rarely the right answer and is usually unaffordable; naming the tolerated deviation is what makes the standard priceable. A PWS with no AQL is priced by every offeror as though it were 100%, or ignored.

**The surveillance plan is written with the PWS, not after it.** If nobody can say how a standard will be observed, it will not be. Each performance requirement maps to a surveillance method — inspection, sampling, customer feedback, or metrics from a system that already exists. A QASP written months later against a PWS full of unmeasurable standards is where performance-based acquisition quietly fails.

**Do not write standards you cannot afford to surveil.** Every measure costs someone's time to collect and adjudicate.

## Step 3: Write the work description so it cannot be read two ways

**One obligation per sentence.** The same rule as requirements writing, for the same reason: a compound sentence becomes two obligations and one gets missed. This is also the shred rule the compliance matrix depends on — see `proposal-writing`.

**Use "shall" for what is binding, and only that.** "Will" describes what the government does or what is expected to happen; "should" and "may" are not obligations and offerors will price them as optional. Mixing them is how a requirement becomes unenforceable.

**Name the actor.** "Testing shall be conducted" does not say by whom. Every obligation names who bears it — the contractor, the government, or a named third party.

**Define terms once, in one place**, and use them consistently. Two words for one concept in a work statement is a dispute waiting for a schedule slip.

**Quantify everything quantifiable.** Numbers of sites, users, transactions, hours of coverage, response times, travel, deliverable counts. Every unquantified quantity gets estimated by the bidder — some low, some high — and the resulting bids are not comparable.

**Say what is government-furnished**, explicitly: property, information, facilities, data, and *when* each is available. GFI and GFE assumptions that turn out wrong are among the most common sources of schedule claims.

**State the boundaries.** What is explicitly out of scope, what interfaces to other contracts, and who is responsible on each side of that seam — see `interface-control` when the seam is technical.

## Step 4: CDRLs and data item descriptions

Deliverables are scope. Each one costs real effort and is frequently added without anyone pricing it.

- **Every deliverable is a CDRL, and every CDRL cites a DID.** The DID defines the content and format; without one, "monthly report" means whatever the reviewer decides it means at review time.
- **Tailor the DID, and record the tailoring.** DIDs routinely require content a given programme does not need. Tailoring is normal and expected; silent non-compliance is not.
- **State frequency, format, medium, distribution and approval.** Whether the government approves or merely receives a deliverable changes its cost substantially, and the difference between "submit" and "submit for approval" is often unnoticed until the first rejection.
- **Count them before signing.** Forty CDRLs at monthly frequency is a full-time documentation effort, and it is routinely priced as though it were incidental.

`dod-technical-report` covers writing the reports these call for.

## Step 5: Review it as an adversary would read it

Before it is issued or accepted, read it looking for money:

- [ ] Every "shall" has one obligation and one named actor
- [ ] Every quantity is stated or explicitly bounded
- [ ] Every performance standard has a measure, a surveillance method and an AQL
- [ ] No product requirements hiding in the work statement, and no tasks hiding in the specification
- [ ] Every deliverable has a CDRL, a DID, a frequency and an approval status
- [ ] Government-furnished items listed with availability dates
- [ ] Terms defined once and used consistently
- [ ] Period of performance, place of performance and travel stated
- [ ] Interfaces to other contracts identified, with responsibility on each side
- [ ] Out-of-scope items stated explicitly
- [ ] Security, clearance, marking and data-rights requirements present — see `export-control-and-markings` and `contract-vehicles-and-clauses`
- [ ] Nothing prescribes a method the government does not intend to own

**Then read it as a bidder pricing it.** Every place you would have to guess is a place where bids will differ for reasons that have nothing to do with capability — and where the low bidder is the one who guessed most optimistically.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Product requirements in the SOW | Neither document verifiable | Specification says what it is; SOW says what work happens |
| Unmeasurable standards | QASP cannot be written | Number or defined observable, every time |
| No AQL | Priced at 100% or ignored | State the tolerated deviation |
| Prescriptive PWS | Government owns a method it did not want | Specify how only where the method genuinely matters |
| Unquantified scope | Bids not comparable | Quantify or explicitly bound |
| CDRLs unpriced | Documentation effort discovered late | Count them, cite DIDs, price them |
| GFI assumed | Schedule claim | List government-furnished items with dates |
| Mixed modal verbs | Requirements read as optional | "Shall" for binding, and nothing else |

The honest one: every ambiguity in this document is eventually resolved, by a person, under schedule pressure, in favour of whoever wrote it more carefully. Write it as though that person is not you.
