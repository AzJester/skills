---
name: cloud-architecture
description: Design a cloud solution for a government or defense customer. Use when choosing an impact level or authorization path, deciding between lift-and-shift and cloud-native, designing a landing zone or account structure, working out which security controls are inherited from the provider, sizing cloud cost at real volume, planning connectivity into a government network, or judging whether a workload belongs in cloud at all. Covers the architecture and its accreditation path; rmf-ato covers the authorization process itself.
---

# Cloud architecture for government

Commercial cloud guidance assumes an internet-connected enterprise that owns its own risk decisions. Defense and federal work assumes neither. The architecture that results is different, and the differences are mostly about **what the environment is allowed to be** rather than what it could technically do.

The failure this exists to prevent is a technically sound architecture that cannot be accredited, cannot be connected, or cannot hold the data it was built for.

## Step 1: Establish the impact level before designing anything

The sensitivity of the data determines the environment, the provider offerings available, the connectivity, and the cost. Deciding it late invalidates the design.

| Level | Broadly holds | Consequence |
| --- | --- | --- |
| **IL2** | Public or non-critical mission information | Widest choice of services and regions |
| **IL4** | CUI | Restricted regions and services; provider must hold the authorization |
| **IL5** | Higher-sensitivity CUI and national security systems | Narrower still; separation requirements tighten |
| **IL6** | Classified up to Secret | Specialised environments, very limited service catalogue |

Two things follow immediately:

**Not every service is authorized at every level.** A design assuming a managed service that exists only at IL2 has to be rebuilt when the data turns out to be CUI. Check the provider's authorized service list for the actual level before committing to any managed service.

**The authorization path differs.** FedRAMP authorization at a given baseline and a DoD provisional authorization are related but not identical; reciprocity exists but is not automatic. Confirm the current position for the specific provider, service and level with the authorizing official rather than assuming — this changes, and it changes per service.

**Classify the data first.** Where the data type is genuinely uncertain, that is a question for the customer's information owner, and it is worth blocking on. See `export-control-and-markings` for what marking and handling then apply.

## Step 2: Know what you inherit and what remains yours

The shared responsibility model is the single most consequential thing to get right, because it determines how much of the accreditation work is already done.

| Model | Provider handles | You still own |
| --- | --- | --- |
| **IaaS** | Physical, hypervisor, network fabric | OS, patching, configuration, everything above |
| **PaaS** | The above plus runtime and platform | Application, data, identity, configuration |
| **SaaS** | Nearly all of it | Data, identity, configuration, and your use of it |

**Control inheritance is the practical payoff and it is not automatic.** A provider's authorization package lets you inherit a defined set of controls into your own body of evidence, and inheriting them properly can remove a very large share of the assessment burden. But:

- **You must document what you inherited and from where.** An assessor will not take it on trust.
- **Hybrid controls are the trap.** Many controls are partly the provider's and partly yours; treating one as fully inherited leaves a real gap that an assessment finds.
- **Configuration is always yours.** The provider being authorized says nothing about whether you configured their service securely. Public storage, over-permissive identity policies and unencrypted data are your findings, not theirs.

Feed all of this into `rmf-ato`, which runs the authorization, and `stig-and-hardening` for the configuration baselines that remain yours.

## Step 3: Choose the migration approach honestly

| Approach | Means | Right when | Real cost |
| --- | --- | --- | --- |
| **Rehost** | Lift and shift, largely unchanged | Deadline-driven, data centre exit | Cloud economics never arrive; you rent the same inefficiency |
| **Replatform** | Modest changes — managed database, container runtime | Some benefit wanted, appetite for change is limited | Moderate, and usually the best return |
| **Refactor** | Rebuilt cloud-native | The workload is strategic and will keep changing | Highest, and frequently underestimated |
| **Repurchase** | Replace with a SaaS product | The capability is not a discriminator | Data migration and process change |
| **Retire** | Turn it off | Nobody could name a user | Only the discovery effort |
| **Retain** | Leave it where it is | It works, moving it earns nothing | Nothing, and this is a legitimate answer |

**Rehost is not failure, but be honest about what it buys.** Moving a workload unchanged relocates cost rather than reducing it, and frequently increases it. That can still be the right decision — a data centre closing is a real constraint — but it should be a decision, not a claim about modernisation. See `modernization-and-migration` for the legacy assessment that precedes this choice.

**Retire and retain both get skipped** because neither produces a project. Both are often correct.

## Step 4: Design the environment

**Landing zone before workloads.** Account and subscription structure, identity, logging, network boundaries and guardrails established first. Retrofitting isolation onto an environment where twenty teams already deployed is the most expensive avoidable cloud work there is.

**Separate by blast radius**, not by org chart. Production from non-production, sensitive from routine, one programme's data from another's — enforced by account or subscription boundaries rather than by naming conventions and good intentions.

**Identity is the actual perimeter.** Federated to the customer's identity provider where possible, least privilege by role, no long-lived static credentials, and every human and machine identity attributable to something. This is the foundation `zero-trust-architecture` builds on.

**Log centrally, immutably, from day one.** Continuous monitoring is a condition of most authorizations, and logging retrofitted after an incident does not cover the incident.

**Encrypt in transit and at rest, and know where the keys live.** Key custody is frequently a contractual and accreditation question, not only a technical one.

**Automate the environment as code.** An accredited baseline that is maintained by hand drifts, and drift is what re-assessment finds. See `devsecops-pipeline`.

## Step 5: Connectivity is usually the schedule risk

The design is rarely the long pole. Connecting it is.

- **Reaching a government network takes time.** Approved connection paths, boundary protection, and the approvals that go with them have lead times measured in months. Start them in parallel with design, not after it.
- **Latency and bandwidth to the user population** decide whether the architecture works in practice. A cloud region far from the users is a performance problem no amount of application tuning fixes.
- **Plan for degraded and disconnected operation** where the mission requires it. Cloud availability assumptions do not hold at the tactical edge — `network-architecture` covers designing for the disconnected case first.
- **Egress is the cost nobody models.** Data leaving the provider, crossing regions, or moving between accounts is charged, and analytics or AI workloads move a great deal of data. See Step 6.

## Step 6: Cost, at real volume

Cloud cost is consumption, so the architecture is the cost model.

- **Model at production volume**, not at pilot. The shape changes: storage accumulates, egress grows with users, and logging at production scale is frequently a top-three line item.
- **Data gravity is a design constraint.** Move compute to data rather than data to compute, wherever the volumes are meaningful.
- **Managed services trade cost for lock-in.** Both directions are defensible; what is not defensible is choosing without pricing the exit.
- **Commitment discounts require a demand forecast** you actually believe, and a contract period that matches. On a programme whose funding is annual, a three-year commitment is a risk to name.
- **Idle non-production is the most common waste**, and it is the easiest to fix.

For AI workloads specifically, `ai-cost-modeling` covers the consumers people miss.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Impact level decided late | Design invalidated; services unavailable | Classify the data first |
| Inheritance assumed | Assessment finds gaps in hybrid controls | Document what is inherited, from where, and what remains |
| Provider authorization read as your security | Public buckets, over-broad roles | Configuration is always yours |
| Workloads before landing zone | Expensive retrofit of isolation | Structure, identity, logging, guardrails first |
| Rehost sold as modernisation | Costs rise, benefits do not arrive | Name the approach honestly |
| Connectivity started after design | Months of schedule discovered late | Start approvals in parallel |
| Cost modelled at pilot scale | Budget breached in the first quarter | Model at production, including egress and logging |
| Environment maintained by hand | Drift, then re-assessment findings | Infrastructure as code |

The honest one is the first. Almost every serious cloud rework in government starts with data that turned out to be more sensitive than the design assumed.
