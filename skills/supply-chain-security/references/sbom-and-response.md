# SBOM practice and vulnerability response

## Minimum useful SBOM

Below these fields, an SBOM cannot answer the questions it exists for.

| Field | Why it is needed |
| --- | --- |
| Component name and **version** | Version is the whole point; a name alone answers nothing |
| Unique identifier (purl, CPE) | Machine matching against advisories. Name matching fails on aliases and forks |
| Supplier / originator | Provenance, and who to ask |
| Dependency relationship | Direct versus transitive, and the path — needed for reachability |
| Hash of the component | Integrity, and detecting substitution |
| License | Obligation tracking, and a distribution question in its own right |
| Author of the SBOM and timestamp | Currency; a stale SBOM describes something you no longer ship |

**Insist on identifiers.** An SBOM without purl or CPE cannot be matched against advisory feeds automatically, which means the Friday-afternoon question is answered by a person reading a list.

## Storage

An SBOM lives with the artifact it describes, keyed to the build. One per build, retained as long as the artifact is deployed anywhere.

The common failure: SBOMs generated in the pipeline and dropped, so the current one describes the latest build while the version in production is two releases behind and no longer documented. Retention is what makes the inventory useful during an incident.

## Response runbook

The clock starts when the advisory publishes, not when someone notices.

**1. Affected? (target: minutes)**
Query the inventory for the component and affected version range. Cover every deployed artifact, not only the current release. If this step requires asking teams, the inventory is not doing its job.

**2. Where? (target: minutes)**
Products, versions, environments, customers. Include artifacts built but not yet deployed, and anything shipped to a customer who runs it themselves.

**3. Reachable? (target: hours)**
Is the vulnerable code path actually reachable in your usage? Record the determination as VEX so the answer is machine-readable and customers are not chasing a finding that does not apply.

Reachability changes priority, not obligation. An unreachable vulnerability still gets remediated on a normal cycle; it just does not warrant an emergency.

**4. Remediate**
Upgrade, patch, replace, or mitigate by configuration. Each is a change: it goes through `configuration-management`, and its impact assessment names which verification evidence it invalidates.

**5. Verify and notify**
Re-verify affected evidence. Notify customers, and the government where DFARS 7012 timelines apply.

## Health measures

| Measure | Signals |
| --- | --- |
| Time to answer "are we affected" | The only measure that matters; everything else supports it |
| Artifacts in production with a current SBOM | Inventory coverage |
| Supplier SBOM coverage | How much of the chain is dark |
| Unpinned dependencies | Uncontrolled configuration items |
| Mean age of known-vulnerable components | Whether remediation is happening or accumulating |
| Unsigned artifacts in the pipeline | Integrity gaps |

Rehearse the first measure before you need it. An inventory nobody has queried under pressure fails in ways that are obvious afterwards.
