# Variance analysis report

One per control account breaching threshold. Written by the control account manager, not by a analyst reformatting numbers.

## Header

| | |
| --- | --- |
| Control account | |
| CAM | |
| Period | |
| BAC / EV / AC / PV | |
| CV / CPI · SV / SPI | |
| EAC / VAC / TCPI | |
| Threshold breached | cost / schedule / both |

## 1. What the variance is

One or two sentences. The numbers, current period and cumulative. Cumulative matters more — a single bad period may be timing; a trend is performance.

## 2. Why — the actual cause

The section that determines whether the report is worth writing.

A cause explains something the arithmetic does not. Test it: could someone unfamiliar with the account act on this? "Costs exceeded plan" fails. "The environmental test article failed at 80% of qualification level, requiring redesign of the mounting bracket and a second test entry" passes.

Categorize honestly — estimating error, scope growth, technical difficulty, resource availability, supplier performance, external dependency, rework. The category matters because it predicts recurrence: estimating error on one package suggests estimating error on similar ones.

## 3. Impact

- Effect on this account's EAC
- Effect on other accounts — resources moved, dependencies delayed
- Effect on the critical path, from the IMS rather than from SPI
- Effect on technical scope, if any

## 4. Corrective action

| Action | Owner | Date | Expected effect on CPI/SPI |
| --- | --- | --- | --- |

Each action names an expected effect. An action with no expected effect cannot be judged next period, which is how corrective actions become a recurring list nobody assesses.

## 5. Previous corrective actions

Did the last period's actions work? This section is the one most often omitted and the one that reveals whether the program is managing or reporting.

| Prior action | Expected | Actual | Continue / change / abandon |
| --- | --- | --- | --- |

Three periods of the same corrective action with no measurable effect means the cause was misdiagnosed. Say so rather than restating the action.

## 6. Risk linkage

Was this variance a risk on the register? If yes, update it — a realized risk becomes an issue. If no, ask why it was not foreseen, and whether similar exposure exists elsewhere unrecorded. See `risk-management`.

## Reviewer's checks

- Is the cause a cause, or a restatement of the variance?
- Is the EAC consistent with the CPI actually being achieved?
- Does TCPI require performance the program has never demonstrated?
- Are corrective actions from prior periods assessed, or only re-listed?
- Has the account been rebaselined, and if so, does the history still show the original variance?
