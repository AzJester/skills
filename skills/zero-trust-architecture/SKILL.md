---
name: zero-trust-architecture
description: Design and argue a zero trust architecture. Use when applying the DoD Zero Trust reference architecture, mapping a solution to the seven pillars, deciding target versus advanced activities, assessing current ZT maturity, or writing the zero trust section of a solution or proposal. Covers the architecture and its evidence, not the individual product choices that implement it.
---

# Zero trust architecture

Zero trust is one assumption with consequences: **the network is already compromised, so location proves nothing.** Every access decision is made per-request, on identity, device state, and context, against explicit policy.

That is why "we have a firewall and VPN" is not a zero trust answer. A VPN grants network position and then trusts it, which is the model zero trust exists to replace.

## The seven pillars

DoD structures ZT into seven pillars. A solution that addresses two of them thoroughly and ignores five is not a zero trust solution, and reviewers check.

| Pillar | Core question | Typical mechanisms |
| --- | --- | --- |
| **User** | Is this the right person, verified now? | Phishing-resistant MFA, privileged access management, continuous authentication |
| **Device** | Is this device known, healthy, and compliant right now? | Device inventory, posture checking, compliance enforcement at access time |
| **Application & workload** | Is this workload authorized and hardened? | Secure development, authorized software inventory, workload identity |
| **Data** | Is this data tagged, protected, and access-controlled by its own attributes? | Classification and tagging, encryption, rights management, DLP |
| **Network & environment** | Is the network segmented so a breach does not spread? | Macro and micro segmentation, software-defined perimeter, encrypted transit |
| **Automation & orchestration** | Do responses happen at machine speed? | SOAR, policy orchestration, automated remediation |
| **Visibility & analytics** | Would we see it? | Centralized logging, analytics, user and entity behavior analytics |

Two of these are consistently underdone and consistently asked about. **Data** is the pillar people defer because tagging is unglamorous and expensive, yet attribute-based access to data is where zero trust actually delivers. **Visibility** is the pillar without which none of the others can be shown to work — you cannot demonstrate a policy is enforced if nothing observes it.

## Target versus advanced

Each pillar has activities at two levels. Target is the baseline expected; advanced is the mature state.

The distinction matters commercially. Bidding advanced across all seven pillars for a program that needs target is over-engineering the price; claiming target where the customer specified advanced is non-responsive. Read what the requirement actually asks for, per pillar, and price to it.

For each pillar in a solution, state: current maturity, the target level required, the gap, and what closes it. That table is usually the most useful page in a ZT section.

## Designing to it

**Start from the protect surface, not the attack surface.** The attack surface is unbounded and changes daily. The protect surface — the specific data, applications, assets and services that matter — is small, knowable, and stable. Define it first; everything else is derived.

**Map the transaction flows.** How does traffic actually reach the protect surface? Who, from where, with what, to do what? Policy that does not match real flows either blocks legitimate work or gets exceptions until it means nothing.

**Put the policy enforcement point as close to the resource as possible.** A decision made at the perimeter and trusted thereafter is perimeter security with new vocabulary.

**Write policy in business terms.** "This role, on a compliant device, during a session authenticated within the last N minutes, may read these records" — not a firewall rule. Policy that cannot be read by the person who owns the data cannot be reviewed by them.

**Assume the policy decision point is a dependency.** If it is unavailable, what happens — fail closed and stop the mission, or fail open and stop being zero trust? Decide deliberately and document it; this is the question an assessor asks and most designs have not answered.

## Where this connects

- `rmf-ato` — ZT activities map onto 800-53 controls, and the ZT design is control implementation evidence rather than a separate story. Do not write it twice.
- `threat-modeling` — trust boundaries in the threat model and segmentation boundaries in the ZT design should be the same boundaries. Where they differ, one of them is wrong.
- `network-architecture` — segmentation is a network design decision with ZT consequences.
- `interface-control` — every crossing between segments is an interface with an owner on each side.

## Arguing it in a solution

Weak ZT sections list products. Strong ones show: the protect surface, the transaction flows, the policy model, the enforcement points, per-pillar maturity now versus target, and how enforcement is *observed*. A reviewer's question is almost always "how would you know it is working", and visibility is the answer.

## Reference

- `references/pillar-assessment.md` — per-pillar maturity assessment and gap table.
