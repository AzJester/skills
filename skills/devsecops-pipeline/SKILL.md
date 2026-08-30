---
name: devsecops-pipeline
description: Build the pipeline that delivers software continuously and safely. Use when designing a CI/CD pipeline, choosing and ordering security gates, standing up a software factory, generating SBOMs and provenance, wiring a pipeline to support continuous authorization, deciding what blocks a build versus what warns, or diagnosing why a pipeline everyone bypasses is not delivering the assurance it claims.
---

# DevSecOps pipeline

The pipeline is where security either becomes automatic or becomes advisory. In defense software the pipeline is also increasingly the accreditation argument itself: `rmf-ato` covers continuous authorization, and what makes it credible is a pipeline that demonstrably enforces what the authorization assumes.

The failure this exists to prevent is a pipeline with impressive gates that teams have learned to route around. A control that can be bypassed under schedule pressure is not a control, and the assurance claimed from it is fiction.

## Step 1: Decide what the pipeline is asserting

Before choosing tools, write down what a green pipeline is supposed to prove. Usually some subset of:

- The code builds reproducibly from a known source revision.
- Tests at the levels agreed actually ran and passed.
- No known-vulnerable dependency above the agreed threshold is present.
- The configuration deployed matches the approved baseline.
- What was deployed is what was built, and it can be proven.
- Everything that happened is recorded and attributable.

**Anything the pipeline does not assert is asserted by a human, or by nobody.** Being explicit about which is the point of this step, and it is what makes the security argument to an assessor coherent rather than a tool inventory.

## Step 2: Order the gates by feedback speed

Gates cost developer time. Ordering them badly makes the pipeline slow, and a slow pipeline gets bypassed.

| Stage | Gate | Blocks? |
| --- | --- | --- |
| **Pre-commit / local** | Format, lint, secrets scan, fast unit tests | Yes — cheapest place to fail |
| **Pull request** | Full unit tests, SAST, dependency scan, IaC scan, code review | Yes |
| **Build** | Reproducible build, SBOM generation, artifact signing | Yes |
| **Post-build** | Container and image scanning against the hardened base | Yes on threshold breach |
| **Deploy to test** | Integration tests, DAST, configuration compliance check | Yes |
| **Pre-production** | Performance, resilience, manual approval where required | Per policy |
| **Continuous** | Runtime monitoring, drift detection, new-CVE re-evaluation | Alerts, not blocks |

Three rules that decide whether this works:

**Fail fast and locally.** A secret caught pre-commit costs seconds; the same secret caught after it reaches a shared repository is an incident with rotation and reporting.

**Every gate has an owner and a documented threshold.** "Fails on high severity" needs to say which scoring system, which threshold, and who can grant an exception. Undocumented thresholds get quietly lowered.

**Exceptions are logged, time-boxed and reviewed.** A permanent exception is a control that does not exist, recorded as though it does. Give every exception an expiry and a named owner, and review the list — its length is a real measure of pipeline health.

## Step 3: Supply chain — generate what you will be asked to produce

`supply-chain-security` covers consuming SBOMs and responding to vulnerabilities. The pipeline is where you produce the evidence.

- **Generate an SBOM at build time**, from the build, in a standard format. An SBOM produced later by scanning a running system is a guess about what you shipped.
- **Sign artifacts and record provenance** — what source revision, which builder, which inputs. This is what makes "what is running is what we built" checkable rather than assumed.
- **Build from hardened, curated base images** where a programme provides them. It removes a large share of findings before the first scan.
- **Pin dependencies and control the upstream.** An unpinned transitive dependency means the thing you tested is not necessarily the thing you shipped.
- **Store artifacts immutably**, with retention that matches how long you may have to answer questions about a release.

## Step 4: Wire it to the authorization

Continuous authorization rests on demonstrating that the pipeline enforces the controls the ATO assumes. To make that argument:

- **Map pipeline gates to controls explicitly.** A table showing which control each gate satisfies, and what evidence it produces, is what an assessor can actually work from.
- **Produce evidence automatically as an artifact of running**, not by screenshotting dashboards before an assessment. Evidence assembled by hand is evidence that stops existing when someone is busy.
- **Monitor drift continuously.** An accredited baseline maintained by hand diverges; detecting divergence is part of the argument. See `cloud-architecture` on infrastructure as code and `stig-and-hardening` on the baselines themselves.
- **Know what changes require re-authorization** and what falls inside the approved envelope. Agree that boundary with the authorizing official in advance — discovering it during a release is how a pipeline stops being continuous.

## Step 5: Make it fast enough that nobody routes around it

This is the engineering problem underneath the security problem.

- **Measure the time from commit to feedback**, and treat it as a first-class metric. Past roughly ten minutes for the pull request stage, developers start batching changes, and large batched changes are where defects hide.
- **Parallelise the slow scanners**, and run the deep ones on a schedule rather than on every commit where that is defensible.
- **Cache aggressively**, but never the security scan results in a way that lets a stale pass stand in for a real one.
- **Keep the pipeline itself under version control and review.** Pipeline definitions are production code with production credentials — the most privileged code in many organisations and frequently the least reviewed.
- **Protect the credentials the pipeline holds.** Short-lived, scoped, never in the repository. A compromised pipeline is a compromise of everything it can deploy to.

## Step 6: The organisational half

Tooling is the easy part.

- **Developers must be able to run the gates locally**, or they will discover failures only in CI and resent the pipeline rather than use it.
- **Security findings need triage, not just volume.** A scanner producing four hundred findings with no prioritisation trains everyone to ignore it. Route real findings to `threat-modeling` and `risk-management`; suppress the noise deliberately and record why.
- **The pipeline is a product with users.** It needs an owner, a backlog and someone who cares whether it is fast.
- **Bypasses are a signal, not a discipline problem.** When a team routes around a gate, the gate was too slow, too noisy, or in the wrong place. Fix the gate.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Gates that can be bypassed | Assurance claimed but not enforced | Enforce in the pipeline, log every exception |
| Slow pipeline | Batched changes, developer workarounds | Measure commit-to-feedback; parallelise |
| Scanner noise | Findings universally ignored | Triage, prioritise, suppress deliberately |
| SBOM generated after the fact | Describes a guess, not the build | Generate at build time from the build |
| Evidence assembled by hand | Vanishes when someone is busy | Produce evidence as an artifact of running |
| Undocumented thresholds | Quietly lowered over time | Document threshold, owner and exception path |
| Permanent exceptions | Control exists on paper only | Expiry and owner on every exception |
| Pipeline unreviewed | Most privileged code, least scrutiny | Version control and review it like production |

The honest one is the first, and it is testable: ask how a release ships when the pipeline is red and the deadline is tomorrow. The answer describes the controls you actually have.
