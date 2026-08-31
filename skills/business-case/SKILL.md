---
name: business-case
description: Build the case for an investment decision. Use when justifying a spend, calculating ROI, payback, NPV or IRR, framing options for an investment, testing which assumptions actually drive the answer, or writing the financial argument behind a proposal, an internal initiative, or a bid and proposal commitment. Builds the case for a course of action, where trade studies choose between them.
---

# Business case

A business case answers whether a course of action is worth its cost. It is a different instrument from a trade study, and the two get conflated.

`trade-study-analysis` and your account's `decision-tree-ev` choose **between** options on defined criteria. A business case argues **for** one against the alternative of not doing it — which is always an option and is the one most cases forget to include.

## Step 1: Frame the decision honestly

- **What is being decided**, and by whom, by when.
- **The baseline** — what happens with no investment. Not a strawman. The do-nothing case usually has costs of its own, and a case that ignores them overstates the benefit.
- **The alternatives**, including partial or deferred versions. "Do it now" versus "do nothing" is a false pair when "do a third of it and learn" exists.
- **The horizon** — over what period benefits and costs are counted, and why that period. Horizon choice can determine the answer on its own, which is why it is stated up front rather than chosen to suit.

## Step 2: Cost it completely

Understated cost is the most common defect, and it is usually omission rather than error.

| Category | Frequently missed |
| --- | --- |
| Acquisition | Integration, data migration, one-time licensing |
| Implementation | Internal labor at loaded rates, not just vendor cost |
| Transition | Parallel running, dual maintenance during changeover |
| Sustainment | Support, licenses, hosting, refresh over the horizon |
| Training and adoption | Time lost during ramp, not just course cost |
| Opportunity cost | What those people would otherwise deliver |
| Exit | What it costs to stop or replace later |

**Internal labor is a real cost**, whether or not it appears in a budget line. A case that treats the team as free because they are already employed will be challenged by anyone who thinks in terms of capacity.

## Step 3: Quantify benefits, and label what you cannot

Three tiers, and mixing them is what makes a case unbelievable:

- **Hard** — money that appears in a budget. Cost avoided, revenue won, headcount not added.
- **Soft** — real value, measurable, not appearing as cash. Hours saved, cycle time reduced, defect rate lowered.
- **Strategic** — genuine and not quantifiable. Capability positioned, risk reduced, option preserved.

Keep them separate and label them. **Converting soft benefits to cash with an assumed rate is where most cases lose credibility** — "40 hours saved per week × $95/hr = $198K/year" is only true if that time is actually redeployed or the headcount actually falls. State the conversion assumption explicitly and let the reader judge it, or present the hours and let them do the conversion.

## Step 4: The financial measures

| Measure | Answers | Watch |
| --- | --- | --- |
| **Payback period** | How long until cumulative benefit exceeds cost | Ignores everything after payback; easy to game with a short horizon |
| **ROI** | Return as a percentage of investment | Meaningless without a stated period |
| **NPV** | Value today of the cash flows, discounted | Depends entirely on the discount rate — state it and its source |
| **IRR** | The discount rate at which NPV is zero | Misleads on unconventional cash flows; compare against a hurdle rate |
| **TCO** | Total cost over the horizon, both options | Not a benefit measure; use alongside one |

For most internal cases, **payback and NPV together** are enough. Payback is the number people feel; NPV is the one that is correct.

State the discount rate and where it came from. An NPV with an unstated rate is a number the reader cannot evaluate.

## Step 5: Test which assumptions actually matter

The step that turns a spreadsheet into an argument.

Vary each significant assumption independently and record the effect on the answer. Usually two or three drive nearly everything, and the rest are precision that does not matter.

| Assumption | Base | Low | High | Effect on NPV | Confidence |
| --- | --- | --- | --- | --- | --- |

Then answer the two questions a reviewer will ask:

- **What would have to be true for this to be a bad decision?** If the answer is "adoption below 40%", that is the thing to manage and the thing to say.
- **What is the break-even on the driving assumption?** "This pays back as long as we process at least 1,200 cases a month" is a far stronger sentence than a point estimate, because it survives being wrong.

`applied-statistics` for confidence intervals where the inputs are estimated from data rather than assumed.

## Step 6: Present it so it can be challenged

Lead with the recommendation and the number — `executive-decision-memo` carries the structure. Then: what it costs, what it returns, over what period, under what assumptions, and what would change the answer.

**Include the case against.** A business case with no downside reads as advocacy, and readers discount it accordingly. Naming the strongest argument against your recommendation, and answering it, is what makes the rest credible.

## Common failures

| Failure | Reads as |
| --- | --- |
| Do-nothing baseline omitted or strawmanned | Advocacy |
| Soft benefits converted to cash without stating the assumption | Optimism |
| Internal labor treated as free | Not costed |
| Horizon chosen to make the answer work | Arithmetic |
| Discount rate unstated | Unevaluable |
| No sensitivity analysis | Untested |
| No downside named | Unexamined |
