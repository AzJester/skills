# Authorization package contents

The package supports one decision. Anything in it that does not help the AO decide is overhead; anything missing that they need is a delay.

## Core artifacts

| Artifact | Answers | Fails when |
| --- | --- | --- |
| **Categorization** | How bad is a loss of confidentiality, integrity, availability? | Impact levels asserted with no information-type analysis behind them |
| **System security plan (SSP)** | How is each control satisfied in *this* system? | Control text restated from the catalog instead of described as implemented |
| **Security assessment report (SAR)** | What did testing find? | Findings without severity, or severity without a basis |
| **POA&M** | What is not fixed, who owns it, by when? | Items re-dated rather than closed |
| **Risk assessment** | What residual risk is the AO accepting? | Written for engineers rather than for the decision-maker |
| **Boundary description** | What is in, inherited, and out? | Ambiguity discovered during assessment |
| **Architecture and data flow** | How does it work and where does data go? | Diagrams that do not match the deployed system |
| **Configuration and hardening evidence** | Are baselines applied? | Scan results predating the current configuration |
| **Contingency and incident response plans** | What happens when it breaks or is attacked? | Untested, or naming staff who have moved on |

## The SSP control statement

Each control gets a statement answering four questions. The pattern that survives assessment:

> **Mechanism** — what satisfies the control.
> **Location** — where it is configured or enforced.
> **Operator** — who runs and maintains it.
> **Evidence** — what an assessor can look at.

A statement that reads like the control catalog tells the assessor the control was copied, not implemented.

## Inheritance

Every inherited control needs three things recorded, and missing any one is a standard finding:

1. The **provider** — named system or service, not "the enterprise".
2. The **agreement** — the provider acknowledges providing it to you.
3. The **boundary** — which part is inherited and which part remains yours. Most inheritance is partial: a provider supplies the mechanism, you supply the configuration.

## Before submission

- Every control has a disposition: implemented, inherited, tailored out, compensating, or on the POA&M. None left blank.
- Every tailoring decision has a reason a stranger could evaluate.
- Every inheritance names a provider who has agreed.
- Every piece of evidence is current against the configuration under authorization.
- The boundary in the SSP, the diagram, and the asset inventory are the same boundary.
- Self-identified findings are already on the POA&M rather than waiting to be discovered.
