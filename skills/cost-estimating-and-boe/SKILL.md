---
name: cost-estimating-and-boe
description: Estimate what work will cost and write the basis that justifies it. Use when building a cost estimate for a bid or an internal investment, writing or reviewing a basis of estimate, choosing an estimating method, mapping labor categories and rates, preparing for a cost realism evaluation or a DCAA audit, sizing management reserve, or explaining why an estimate differs from what someone hoped. Covers estimating and its justification; earned-value-management reads the baseline that results.
---

# Cost estimating and the basis of estimate

The estimate is a number. The **basis of estimate** is why anyone should believe it — and on a government bid it is the artifact that gets audited, challenged and defended long after the number is set.

The failure this exists to prevent is an estimate built backwards from a target. The target may be right; deriving the estimate from it produces a number that cannot survive questioning, and worse, one nobody can execute to.

## Step 1: Choose the method deliberately

Four methods, each right for a different maturity of information. Most real estimates use several, one per WBS element.

| Method | How | Right when | Fails when |
| --- | --- | --- | --- |
| **Analogy** | Adjust a known actual from a similar past effort | Early, and a genuine analog exists | The analog is similar in name only |
| **Parametric** | Cost estimating relationship driven by a measurable parameter | The relationship is calibrated on real data in range | Extrapolated outside its data range |
| **Engineering build-up** | Bottom-up, task by task, by the people who will do the work | Scope is defined and decomposed | Scope is still moving; also the slowest |
| **Expert judgment** | Structured elicitation from people who have done it | Nothing else is available | Used alone, unstructured, by one optimist |

**Say which method each element used, in the BOE.** An estimate whose method is unstated cannot be evaluated, and reviewers assume the weakest one.

**Cross-check with a second method.** A build-up that lands within 15% of a parametric estimate is credible. A large divergence is information — usually that the scope is understood differently by the two, which is worth finding before submission rather than after award.

## Step 2: Estimate against the WBS

Every estimate element maps to a WBS element, and the WBS comes from `wbs-and-scheduling`. This is not bookkeeping — it is what makes the estimate traceable to scope, and later what makes the performance measurement baseline in `earned-value-management` possible.

Cost elements to account for, since the ones people forget are consistent:

- **Direct labor**, by labor category and hours, at the rates that will actually apply
- **Indirect** — fringe, overhead, G&A, applied per the disclosed rate structure
- **Materials and equipment**, including lead times that drive schedule
- **Subcontracts and consultants** — see `teaming-and-subcontracts`
- **Travel**, at the actual trip count nobody wants to admit to
- **Other direct costs** — licenses, cloud consumption, test facilities, shipping, certification
- **Escalation** across the period of performance
- **Fee or profit**, per the contract type

**The forgotten costs are consistent across bids:** integration and test effort, documentation and CDRLs (see `sow-and-pws`), program management and administration, security and accreditation work (see `rmf-ato`), transition-in (see `program-startup`), and the cost of the meetings the customer will require.

## Step 3: Rates and labor categories

**Map to the solicitation's labor categories, not your internal ones.** Where the RFP defines LCATs with qualification requirements, every proposed person must meet them, and the mapping is checked. An internal "Senior Engineer" that does not meet the RFP's "Senior Systems Engineer II" education and experience minimums is a finding.

**Use the rates that will apply**, from the approved rate structure — a forward pricing rate agreement where one exists, or the current recommendation where it does not. Rates invented for a bid become a problem at audit and a bigger one at contract close-out.

**Uncompensated overtime is a decision with consequences.** Bidding salaried staff at more than a standard week lowers the effective rate and is scrutinized in cost realism evaluation. Where it is used, it must reflect a real, disclosed and consistently applied practice.

## Step 4: Write the basis so it survives being read cold

Each BOE element answers four questions, in this order:

1. **What is being estimated** — the WBS element and its scope, stated so the boundary is unambiguous.
2. **How it was estimated** — the method, and the specific source: which historical program, which CER, which engineer and what qualifies them.
3. **The calculation** — inputs, quantities, rates, factors, arithmetic that can be reproduced.
4. **Why it is reasonable** — the sanity check, the comparison, the reason a reviewer should accept it.

Three disciplines that decide whether it holds up:

**Traceable to a source a third party can inspect.** "Based on engineering judgment" is not a basis. "Based on 4,200 actual hours for the equivalent element on program X, adjusted upward 18% for the added interface described in §3.2" is.

**Quantities separate from rates.** Hours and rates in separate columns, always. Merged, neither can be evaluated and a rate change requires re-deriving the estimate.

**Assumptions stated explicitly**, each one testable, each one flagged where it materially drives the number. Every assumption is a place the estimate is wrong if the assumption is — and stating it moves that risk to where it can be managed.

## Step 5: Realism, reserve and risk

**Cost realism is a different test from price reasonableness.** Reasonableness asks whether the price is too high. Realism asks whether the proposed costs are consistent with the proposed technical approach — whether you have priced the work you said you would do. On cost-reimbursement work an unrealistically low estimate is a finding against the technical approach, not a competitive advantage: it says you do not understand the scope, or do not intend to perform it as described.

**Management reserve is for realized risk within scope. It is not for scope growth**, and it is not a discount to be given away when the price comes back high. Size it from the risk register — see `risk-management` — rather than as a flat percentage.

**Do not bury risk in the estimate.** Padding every element hides where the exposure actually is and produces a number nobody can defend line by line. Estimate the most likely cost, identify the risk separately, and hold reserve against it explicitly.

**When the estimate exceeds the price-to-win**, that is information, not an error to correct silently. The honest responses are to reduce scope, change the technical approach, accept lower fee, or no-bid — each a decision for a person to make knowingly. Quietly shaving hours until the number fits is how programs are won and then lost. See `solution-shaping` for the descope ladder that should already exist.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Estimate derived from the target | Cannot be defended line by line | Estimate the work; handle the gap as a decision |
| Method unstated | Reviewer assumes the weakest | Name the method per element |
| Rates and hours merged | Neither can be evaluated | Separate columns, always |
| Assumptions unstated | Estimate silently wrong | List them; flag the ones that drive the number |
| Padding for risk | Exposure invisible, price uncompetitive | Most-likely cost plus explicit reserve |
| Support scope omitted | Overrun begins at award | PM, CDRLs, integration, security, travel, transition |
| Internal LCATs proposed | Mapping finding | Map to the solicitation's categories and minimums |
| Reserve given away in negotiation | Realized risk has no funding | Defend it as priced risk, with the register behind it |

The honest one is the first, and the reason it persists is that it usually works — right up until execution, where the estimate becomes a budget somebody has to live inside.

## Reference

- `references/estimate-review.md` — a review checklist and the cost element list in full.
