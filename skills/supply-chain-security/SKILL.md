---
name: supply-chain-security
description: Secure and evidence the software and component supply chain. Use when producing or consuming an SBOM, applying the Secure Software Development Framework, establishing component provenance, signing or verifying artifacts, responding to a vulnerability in a dependency, completing a secure software development attestation, or assessing supplier risk.
---

# Supply chain security

Most software in a delivered system was written by someone else. Supply chain security is the discipline of knowing what those components are, where they came from, whether they can be trusted, and what happens when one of them turns out to be vulnerable.

The question that organises it: **when a vulnerability is announced in a widely used library on a Friday afternoon, how long does it take to answer "are we affected, where, and how bad"?** Organisations that can answer in an hour built for it. Organisations that take three weeks are doing archaeology, and they discover during the exercise that they do not know what they shipped.

## Step 1: Know what is in it — SBOM

A software bill of materials lists components, versions, and relationships. It exists to make the Friday-afternoon question answerable.

**Formats.** SPDX and CycloneDX are the two that matter. Pick one as primary, be able to consume both — customers and suppliers will not agree with you.

**Generate at build, from the build.** An SBOM produced by scanning a finished artifact misses what the scanner cannot see; one written by hand is wrong within a sprint. Generation belongs in the pipeline, producing an SBOM per build, stored with the artifact it describes.

**Depth.** Direct dependencies alone are close to useless — the vulnerabilities that matter are usually transitive. Capture the full resolved graph.

**Consume, do not just produce.** An SBOM you generate satisfies a deliverable. SBOMs you *ingest* from suppliers are what let you answer the question about components you did not build. Ask for them, and have somewhere to put them.

An SBOM nobody queries is a compliance artifact. The value is entirely in the querying.

## Step 2: Develop securely — SSDF

NIST SP 800-218, the Secure Software Development Framework, organises practice into four groups:

| Group | Concern |
| --- | --- |
| **Prepare the organisation** | People, process and tooling ready — roles, training, security requirements defined |
| **Protect the software** | Protect code and artifacts from tampering; control access to repositories and the pipeline |
| **Produce well-secured software** | Design review, secure coding, code review, testing, third-party component vetting |
| **Respond to vulnerabilities** | Identify, assess, remediate, and disclose |

Federal acquisition increasingly requires **attestation** to SSDF practices. An attestation is a representation, signed. Treat it with the seriousness of any other signed statement: attest to what you actually do, and fix what you cannot attest to rather than describing it optimistically.

## Step 3: Establish provenance and integrity

Knowing what a component is matters less than knowing it is what it claims to be.

- **Pin versions.** A floating dependency means the artifact you tested is not necessarily the one you shipped. This is also a `configuration-management` requirement — an unpinned dependency is an uncontrolled configuration item.
- **Verify signatures and checksums** on ingest, not on trust.
- **Sign your own artifacts**, so downstream consumers can do the same.
- **Record build provenance** — what source, what toolchain, what inputs produced this artifact. Reproducibility is the strong form; recorded provenance is the practical minimum.
- **Protect the pipeline.** A compromised build system inserts itself into everything downstream, and the artifact still passes every check because it was signed by you.

The pipeline is a high-value target precisely because its output is trusted. Harden it as a production system — see `stig-and-hardening` — rather than as developer infrastructure.

## Step 4: Respond

When a vulnerability lands:

1. **Are we affected?** Query the SBOM inventory. This is the step that takes an hour or three weeks.
2. **Where, and in what?** Which products, versions, deployments, customers.
3. **Is it reachable?** A vulnerable component present but not on any reachable path is a different priority from one in the request path. VEX (Vulnerability Exploitability eXchange) exists to state this and to stop customers chasing findings that do not apply to them.
4. **Remediate or mitigate**, then re-verify — see `verification-validation`; a dependency change may invalidate closed verification evidence.
5. **Tell people.** Customers, and where obligations apply, the government. Under DFARS 7012, incident reporting timelines are contractual.

Pre-deciding steps 1 and 2 is the whole game. They are cheap to build and impossible to improvise.

## Step 5: Suppliers

Your supply chain includes organisations, not only libraries.

Assess suppliers on: their own secure development practice, whether they provide SBOMs, their vulnerability disclosure and response commitments, flow-down of your contractual obligations, and their sub-tier visibility. Under DFARS 7020, flow-down is an obligation rather than a preference — see `cmmc-readiness`.

Concentration risk is worth naming separately. A single supplier behind several critical components is a programme risk belonging in `risk-management`, whatever their security practices.

## Reference

- `references/sbom-and-response.md` — SBOM fields worth insisting on, and the response runbook.
