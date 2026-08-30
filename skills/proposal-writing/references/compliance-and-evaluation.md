# Compliance, evaluation and the evaluator's vocabulary

## The Uniform Contract Format

Most federal solicitations use the UCF. The sections that drive a response:

| Section | Holds | Matters because |
| --- | --- | --- |
| B | Supplies or services and prices | CLIN structure the price volume must match |
| C | Description, specifications, statement of work | The actual work — see `sow-and-pws` |
| F | Deliveries or performance | Period of performance, delivery schedule |
| H | Special contract requirements | Where unusual obligations hide |
| I | Contract clauses | Flow-down and data rights — see `contract-vehicles-and-clauses` |
| J | List of attachments | CDRLs, DD 254, PWS, and the attachments that carry real scope |
| K | Representations and certifications | Administrative, but a missing rep can void a bid |
| L | Instructions, conditions and notices to offerors | The required structure and format |
| M | Evaluation factors for award | The scoring rubric |

**Section J is where scope hides.** The CDRL list and the attached PWS routinely contain more work than Section C's prose implies. Read the attachments before estimating anything.

## How evaluators actually record findings

Federal source selection uses a defined vocabulary. Writing to produce strengths and avoid weaknesses is more useful than writing to sound good.

| Finding | Roughly means |
| --- | --- |
| Strength | Merit or exceeds a requirement in a way beneficial to the government |
| Significant strength | The same, to an appreciable degree |
| Weakness | A flaw that increases the risk of unsuccessful performance |
| Significant weakness | A flaw that appreciably increases that risk |
| Deficiency | A material failure to meet a requirement, or an unacceptable risk level |

A deficiency can make a proposal ineligible for award without discussions. Every compliance-matrix row exists to prevent one.

**Risk is scored separately from merit** in most trade-off selections. A technically strong approach with an unmitigated schedule or staffing risk can lose to a plainer approach that shows its risk handled. Feed `risk-management` output into the proposal rather than hiding exposure — the evaluator will find it, and finding it themselves scores worse.

## Evaluation approaches

**Lowest price technically acceptable (LPTA).** Technical is pass/fail; price decides. Writing effort goes into unambiguous demonstration of acceptability against each stated requirement — nothing more. Elaborating beyond acceptable earns no credit and costs pages.

**Trade-off / best value.** Non-price factors can justify a higher price. Here discriminators pay, and the proposal must make the value of the difference explicit rather than assuming the evaluator will price it.

Section M states the relative order of importance — factors among themselves, and non-price against price. That ordering should drive page allocation, theme emphasis, and which discriminators lead.

## Past performance

Usually evaluated on **relevancy** and **quality** together, and the two are scored differently.

- **Relevancy** turns on similarity of scope, magnitude and complexity. A large contract in an unrelated domain is often less relevant than a smaller one that matches the work. Argue the match explicitly rather than listing contract values.
- **Quality** comes from CPARS and from questionnaires the customer sends to references. It is largely outside the proposal's control by the time the RFP drops, which is a reason to manage it during performance rather than at bid time.
- **Address adverse past performance directly.** A known problem left unmentioned reads as either unaware or evasive. State it, state what changed, and state the evidence that the change held.

## Questions during the Q&A window

The window is a real instrument, not a formality:

- Ask about anything where L and M conflict, where a page limit is ambiguous, or where a requirement could be read two ways with materially different cost.
- Answers are published to all offerors, so a question can reveal your approach. Phrase it to resolve the ambiguity without describing your solution.
- After the window closes, an ambiguity is yours to absorb. Comply with the stricter reading and cross-reference.

## Orals

Where the solicitation uses oral presentations, the evaluated artefact is the presentation and often the answers to questions, not a written volume. Two things change:

- **Slides are usually not read afterwards.** They support the speaker and are frequently limited in count and content by Section L. See `briefing-deck` for how to build them.
- **The Q&A is scored.** Rehearse against the hardest questions the evaluation factors invite, including the ones about weaknesses in your own approach.

## Compliance matrix template

```
| ID | Source | Requirement (verbatim) | Vol/§/Page | Owner | Status |
|----|--------|------------------------|------------|-------|--------|
| L-001 | L.3.2.1 | "The Offeror shall describe its approach to..." | Vol II, §3.2, p.14 | — | drafted |
| M-002 | M.2 Factor 1 | "...the extent to which the proposed approach demonstrates..." | Vol II, §3.2, p.14–17 | — | reviewed |
```

Keep it in one file that everyone writes against. Two copies of a compliance matrix is the same failure as two authoritative requirement baselines, with a deadline attached.
