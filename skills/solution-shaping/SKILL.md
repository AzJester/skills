---
name: solution-shaping
description: Shape the technical solution for a pursuit before the proposal is written. Use when deciding what to offer against a customer's problem, identifying discriminators, testing a solution against evaluation criteria, positioning against an incumbent or a likely competitor, aligning technical approach with price-to-win, or preparing the solution for a capture or gate review. Sits before proposal writing, not inside it — `proposal-writing` covers that.
---

# Solution shaping

A proposal describes a solution. Shaping decides what that solution should be — and that decision is made against the customer's problem, the evaluation, and the competition, not against what you would build if left alone.

The failure this exists to prevent: a technically excellent solution that scores badly. It happens when the solution is designed by engineering to be good, then handed to proposal to be described, with nobody having checked it against how it will be evaluated.

## Step 1: Understand the problem the customer actually has

The stated requirement and the underlying problem are related and not identical. Requirements are written by people compressing a problem into procurable language, and something is always lost.

Establish:

- **The mission outcome** they need, in their words.
- **Why now** — what changed. A recompete, a failure, a new threat, expiring authority, a mandate.
- **Who is affected**, including the people who will operate it and who rarely write the requirement.
- **What they have tried**, and why it did not work. This is where discriminators come from.
- **What they are afraid of.** Programmes are shaped by the customer's fear more than their ambition — of another failed integration, of an ATO that never lands, of a vendor who disappears.

`grilling` is useful here on your own understanding. A capture team that cannot articulate the customer's fear has not talked to enough people.

## Step 2: Read the evaluation, not just the requirement

The solution is scored against stated criteria. A feature that no factor rewards is unpaid scope; a factor with no solution behind it is lost points.

Build the crosswalk early:

| Evaluation factor | Weight / importance | What it rewards | Our approach | Evidence | Strength or gap |
| --- | --- | --- | --- | --- | --- |

Two things fall out. **Where you have no evidence, that is a gap to close before submission** — see `engineering-to-proposal`. And **where you are strong but the factor is unweighted**, reconsider how much you are investing there.

## Step 3: Find real discriminators

A discriminator is something the customer values, that you can substantiate, that competitors cannot readily match. All three conditions, or it is a feature.

Test every candidate:

| Test | Fails when |
| --- | --- |
| Does the customer value it? | It matters to engineers and to nobody evaluating |
| Can we prove it? | No past performance, no evidence, no demonstration |
| Can competitors claim it too? | Everyone says it — then it is a ticket to play, not a discriminator |
| Does it address the problem? | It is impressive and irrelevant |

Most claimed discriminators fail the third test. "Experienced team", "proven methodology", "commitment to quality" are claims every bidder makes. What survives is usually specific: a working system already operating in their environment, a cleared team already in place, a completed accreditation on a comparable system, a measured outcome on a comparable programme.

**Ghosting** — framing an evaluation factor so a competitor's known weakness becomes visible without naming them — is legitimate when the weakness is real and the framing is honest. It backfires when the weakness is imagined or when the customer likes the incumbent.

## Step 4: Shape against the competition

Assume the incumbent is the competitor unless there is none.

- **What does the incumbent do well?** You will not win by claiming they do everything badly; the customer chose them and lives with them.
- **What is genuinely broken?** Talk to people. Programme frustrations are usually known.
- **What does a change cost the customer?** Transition risk is the incumbent's strongest asset. A solution that does not address transition credibly loses to inertia.
- **Where does a competitor's standard approach create a weakness** you can frame the evaluation around?

## Step 5: Align technical and price

The most common shaping failure: a solution designed without a price target, priced late, found unaffordable, and cut in the last week by people optimising for cost rather than score.

- Establish the **price-to-win** range early, however uncertain.
- **Cost the solution as you shape it**, not after. `ai-cost-modeling` for AI content, `earned-value-management` reasoning for effort.
- Know **which scope you would cut and in what order** if the price does not close, and check that the cuts are ones the evaluation does not reward.
- Know **which contract type you are pricing into**. FFP on immature technology is a decision to absorb the maturation — see `contract-vehicles-and-clauses` and `trl-assessment`.

## Step 6: Test the shape before committing

Take the shaped solution through a review that is allowed to fail it — `technical-reviews` posture applies. The questions:

- Does it solve the problem the customer actually has, or the one the requirement describes?
- Does every evaluation factor have an approach and evidence?
- Are the discriminators real by all three tests?
- Is it affordable within the price-to-win, and what gets cut if not?
- Is the risk honest, and is the mitigation credible? A solution with no risks reads as one nobody stress-tested.
- Could a competent competitor say the same thing? If yes, it is not shaped yet.

## Where this connects

`engineering-to-proposal` harvests the evidence this needs. `trade-study-analysis` decides between technical options within the shape. `risk-management` carries the pursuit and delivery risks. `executive-decision-memo` gets the bid decision made. The capture-side skills on your account handle the customer relationship; this handles the solution.

## Reference

- `references/shaping-worksheet.md` — the evaluation crosswalk, discriminator tests, and competitive position.
