---
name: business-unit-finance
description: Read and run the financials of a business unit. Use when interpreting bookings, backlog, revenue and cash as the four different things they are, understanding how indirect rates affect competitiveness, distinguishing allowable from unallowable costs, allocating bid and proposal or internal research budget, building or defending an annual forecast, or diagnosing where margin on a programme actually goes. Engineering leadership's view of the numbers, not accounting advice.
---

# Business unit finance

The layer above every programme. `cost-estimating-and-boe` prices a bid; `earned-value-management` measures a programme; `product-management` covers a product's unit economics. None of them covers the set of numbers a business unit is actually run on — and engineering leaders routinely make decisions that move those numbers without knowing which.

**This is not accounting advice.** Cost accounting standards, allowability determinations and disclosure statements are finance and contracts territory, and getting them wrong has consequences. What follows is what a technical leader needs to read the numbers, make decisions consistent with them, and ask the right question of the finance team.

## Step 1: Four numbers people conflate

The single most common source of confusion in a review.

| Number | Is | Recognised when |
| --- | --- | --- |
| **Bookings** | New contract value won | The award is signed |
| **Backlog** | Contract value not yet worked | Reduces as revenue is recognised |
| **Revenue** | Value earned by performing | Work is performed, per the contract type |
| **Cash** | Money actually received | Invoiced and paid — often much later |

**A record bookings quarter can coincide with a bad revenue quarter**, because bookings are future work. **A good revenue year can have a cash problem**, because invoicing and payment lag performance. Someone asking "how did we do" needs to say which number they mean.

**Backlog is the leading indicator engineering leaders should watch.** Falling backlog means the pipeline is not replacing the work being burned, and the effect appears in revenue a year later — by which point the correction is layoffs rather than a pursuit decision. `capture-management` is the lever, and it has to be pulled early.

**Funded versus unfunded backlog matters.** Contract value that is not yet funded is not work you can perform, and a healthy-looking total backlog can be mostly unfunded option years.

## Step 2: Indirect rates, and why they decide competitiveness

Direct costs are charged to a programme. Everything else — facilities, management, benefits, business development, general administration — sits in indirect pools recovered through rates applied to a base.

Three consequences that matter to an engineering leader:

**Your rates decide competitiveness as much as your technical approach.** A higher indirect rate raises every price you bid. Losing repeatedly on price against a similar technical solution is frequently a rate problem, not a solution problem — and no amount of `solution-shaping` fixes it.

**Rates are a fraction, and both parts move.** A rate is pool over base. Growing the direct base spreads fixed indirect cost across more work and lowers the rate for everyone; losing direct work raises rates on what remains, which makes the next bid less competitive. That feedback loop is why a downturn compounds.

**Where costs sit is a real decision with real consequences.** Charging discipline — what is direct, what is indirect, what is allowable — is governed by accounting rules and by the disclosure statement, and it is audited. Miscoding is a compliance matter, not an optimisation. **When in doubt, ask finance before charging, not after.**

**Some costs cannot be billed at all.** Certain categories are unallowable under federal cost principles regardless of how legitimate they are as business expenses. Knowing that a category exists is enough; the determination is finance's.

## Step 3: Where programme margin actually goes

Margin is quoted at bid and rarely arrives intact. The recurring causes, in rough order:

- **Scope absorbed without a modification.** Informal direction, helpfulness, work done to keep a customer happy — see `contract-vehicles-and-clauses` on constructive change. This is the largest single leak and it is invisible until the programme is underwater.
- **Estimating optimism.** Particularly integration, test, documentation and the support scope listed as commonly omitted in `cost-estimating-and-boe`.
- **Staffing mix drift.** Work planned for mid-level staff performed by senior staff costs more and is frequently not noticed until the variance report.
- **Rework.** Escaped defects, failed qualification, requalification after a change — `quality-management-system` measures this as cost of quality for exactly this reason.
- **Unbilled overtime and unrecovered travel.** Small individually, persistent in aggregate.
- **Extended periods of low utilisation** between programmes — see `resource-and-capacity-management`.

**Fixed price and cost-reimbursable behave differently and need different attention.** On fixed price, overrun is yours; on cost-reimbursable, fee is at risk and cost growth is visible to the customer but does not directly cost you the overrun. The management response differs and treating them alike is how one gets neglected.

## Step 4: Investment budgets are real money with rules

Bid and proposal, and internal research and development, are how a business unit buys its future, and both are treated specially in cost accounting.

- **They are finite and they compete.** Every pursuit consumes B&P that another pursuit does not get — `capture-management` qualification exists to allocate it.
- **They are recovered indirectly**, which means spending more raises rates and therefore prices. There is a real ceiling and it is not just a budget line.
- **IRAD is an investment portfolio and should be run like one** — `technology-roadmapping` covers demand, horizons and kill criteria. IRAD with no kill criteria is the most common way a business unit funds work that is going nowhere for years.
- **Allowability rules apply**, and they constrain what can be charged where. Structure the work with finance rather than around them.

## Step 5: Forecasting, and the fact that a forecast is a commitment

- **An annual operating plan is a commitment you will be measured against**, not a projection. Building an optimistic one to get approval creates a year of explaining variances.
- **Revenue forecasts depend on award timing**, which is outside your control and habitually late. A plan that assumes awards land on schedule is a plan that misses.
- **Weight the pipeline honestly**, using the same pWin discipline as `capture-management` and `resource-and-capacity-management`. The three should agree — a revenue forecast, a staffing plan and a pipeline that assume different win rates is a business unit planning three different futures.
- **Know your break-even.** What revenue covers the indirect structure. It determines how much of a downturn is survivable and how fast a decision has to be made.

## Step 6: Read a programme's financial health early

The point of all of this is intervening while intervention is cheap. Signals worth watching monthly:

- Cost performance deteriorating rather than merely poor — see `earned-value-management`
- Actual staffing mix richer than planned
- Backlog burning faster than bookings replace it
- Unbilled receivables growing — work performed and not invoiced, or invoiced and disputed
- Fee at risk on cost-plus work, or an overrun trend on fixed price
- A programme requesting scope absorption "to keep the customer happy"

Each of these is visible months before it appears in an annual result. `program-recovery` is what to do once one of them is real.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Four numbers conflated | Reviews argue past each other | Say which one you mean |
| Rates not understood by engineering | Losing on price, blaming the solution | Know your rates and what moves them |
| Scope absorbed informally | Margin gone, invisibly | Only the contracting officer changes the contract |
| Backlog watched too late | Correction becomes layoffs | Treat backlog as a leading indicator |
| B&P and IRAD unmanaged | Funding work going nowhere for years | Qualification gates and kill criteria |
| Optimistic operating plan | A year of variance explanations | Weight the pipeline honestly |
| Forecast, staffing and pipeline disagree | Three different futures planned | Reconcile them to one win-rate assumption |
| Charging questions resolved late | Compliance exposure | Ask finance before charging |

The honest one is the third. Most margin is not lost in a decision anyone remembers making — it is absorbed a favour at a time, by engineers being helpful, with nobody counting.
