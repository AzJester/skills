---
name: stig-and-hardening
description: Apply and evidence security configuration hardening. Use when implementing STIGs or CIS benchmarks, running SCAP scans, tailoring a benchmark to a system, documenting a hardening exception or deviation, building hardening evidence for an accreditation package, or answering why a control is not applied as written.
---

# Hardening and STIGs

A benchmark is a set of configuration settings someone else decided are safe defaults. Applying one is easy; the work is deciding which settings genuinely do not apply to your system, evidencing that judgement, and keeping the configuration from drifting back.

## Sources

- **STIGs** — DISA Security Technical Implementation Guides. Product-specific, DoD-authoritative, tied to 800-53 controls. Where a STIG exists for your product, it is the expected baseline.
- **SRGs** — Security Requirements Guides. Technology-class rather than product-specific. Where no STIG exists for a product, the applicable SRG is what you tailor against, and you say so.
- **CIS Benchmarks** — community consensus, often broader product coverage, two levels of severity. Useful where no STIG or SRG fits, with the gap stated.
- **Vendor guidance** — sometimes conflicts with the STIG. When it does, that conflict is a documented decision, not something to resolve silently.

## Severity

STIG findings carry categories, and they are not a to-do ordering — they describe consequence.

| Category | Means |
| --- | --- |
| **CAT I** | Directly and immediately results in loss of confidentiality, availability or integrity |
| **CAT II** | May result in loss, or provides significant opportunity for it |
| **CAT III** | Degrades measures toward defence in depth |

An open CAT I is an authorization problem, not a backlog item. Treat the category as what it is — a statement about consequence, not about effort.

## Step 1: Scope honestly

Identify every component with a configurable security posture: operating systems, databases, web and application servers, containers and their base images, network devices, hypervisors, browsers, and the pipeline that builds and deploys all of it.

The components most often missed are the ones that build the system rather than run it. A hardened production host built by an unhardened pipeline from an unhardened base image is hardened in one place out of three.

## Step 2: Apply, then verify by scanning

Apply the benchmark, then verify with SCAP against the benchmark content. The distinction matters: applying a hardening script asserts a state, scanning observes it, and they disagree more often than teams expect — a setting overridden by a later policy, a service that resets on restart, a container layer that reintroduces a default.

Automate application where possible so it is reproducible and reappliable. Hardening performed by hand on a machine that is later rebuilt is hardening that lasts until the rebuild.

## Step 3: Tailor, with reasons that survive review

Not every item applies. Tailoring is legitimate and needs to survive an assessor reading it cold.

For each item not applied as written, record: the item, the reason, what compensates, and who approved.

Reasons that hold:
- The feature is not installed or the interface does not exist.
- The setting breaks a documented mission function, with the function named and a compensating control described.
- A more restrictive setting is applied instead, and here it is.

Reasons that do not hold, and are recognised on sight:
- "Not applicable to our environment" with nothing after it.
- "Operational impact" with no named function.
- "Accepted by the programme" with no named accepter.

A finding marked *not applicable* that an assessor determines *is* applicable becomes an open finding plus a credibility problem affecting everything else you marked.

## Step 4: Evidence for the package

Hardening evidence feeds `rmf-ato` directly as control implementation evidence. What the package needs:

- Scan results **current against the configuration under authorization** — a scan predating the last change proves nothing about the current system.
- The benchmark and version used, with the STIG or SRG release identified.
- The tailoring record, with approvals.
- Open findings, on the POA&M with owners and dates — not a separate spreadsheet.
- Evidence the configuration is enforced going forward, not applied once.

## Step 5: Stop the drift

Configuration decays. Patches reset defaults, an admin fixes an outage by loosening a setting, a new image is built from an old base.

- Scan on a schedule and on change, not only before an assessment.
- Bake hardening into the image and pipeline so a rebuild reapplies it by construction.
- Treat a drifted setting as a change that bypassed `configuration-management`, and ask how it got there rather than only correcting it.
- Track the exception count as a health measure. A steadily rising count means the baseline no longer matches how the system is actually run, and the correct response is to revisit the baseline rather than approve another exception.

## Reference

- `references/hardening-record.md` — the tailoring and exception record, and what makes an entry defensible.
