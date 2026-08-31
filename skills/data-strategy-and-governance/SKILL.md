---
name: data-strategy-and-governance
description: Make data usable and trustworthy as an asset. Use when establishing data ownership and stewardship, defining data quality measures, building a catalog or tracking lineage, setting retention and disposition, deciding how data is shared across programs or organizations, or preparing data to be dependable enough for analytics and AI. Sits upstream of ai-evaluation and ai-governance, which assume data whose provenance and quality are known.
---

# Data strategy and governance

Every AI and analytics skill in this repository assumes something this one has to establish. `ai-evaluation` requires evaluation sets representative of deployment. `ai-governance` requires knowing where training data came from. `data-storytelling` requires numbers somebody can stand behind. None of that exists by default.

The failure this exists to prevent is governance as a documentation exercise — a policy, a council and a catalog nobody uses, while the actual decisions continue to be made from spreadsheets of unknown provenance.

**Governance earns its cost only when it makes data more usable.** Every control below should be justifiable by naming the specific use it enables. Controls that cannot be justified that way are overhead, and they are why data governance has the reputation it has.

## Step 1: Start from decisions, not from an inventory

Cataloging everything you have is a project that ends when the budget does. Start instead from the questions the organization needs answered — the same discipline `mbse-sysml` applies to models.

- Which decisions depend on data, and which data?
- Where does that data come from, and who would notice if it were wrong?
- What is already being decided from data nobody has validated?

**Govern the data that supports real decisions, to the depth the decision warrants.** Everything else can wait, and much of it can be left alone permanently.

## Step 2: Ownership and stewardship, with names

The most common failure in data governance is that everything is "owned" by IT, which holds the systems and knows nothing about whether the values are right.

| Role | Owns | Is usually |
| --- | --- | --- |
| **Data owner** | Accountability for a data domain — what it means, who may use it, what quality is required | A business or mission leader |
| **Data steward** | Day-to-day quality, definitions, issue resolution | Someone who works with the data |
| **Custodian** | The systems, storage, access enforcement, backup | IT or the platform team |

**One named owner per domain.** Not a committee, not a department. The test is whether there is a person who can decide a disputed definition and make it stick.

**Definitions are the first deliverable.** Two systems reporting different numbers for the same-sounding metric is the most common data problem in any organization, and it is nearly always a definition problem rather than a technical one. Write the definitions down, in one place, with the owner's name on them.

## Step 3: Quality, measured against use

Data quality is not an absolute. It is fitness for a specific purpose, and the dimensions worth measuring are the ones that purpose depends on.

| Dimension | Asks |
| --- | --- |
| **Accuracy** | Does it match reality? |
| **Completeness** | Is what should be there, there? |
| **Consistency** | Do systems agree with each other? |
| **Timeliness** | Is it current enough for the decision? |
| **Validity** | Does it conform to its defined format and rules? |
| **Uniqueness** | Is the same thing recorded once? |

Three disciplines:

**Set thresholds per use, not globally.** A completeness level adequate for a trend report is inadequate for a payment. Blanket quality targets are either unaffordable or meaningless.

**Measure continuously and publish it.** Quality that is assessed during a project and never again degrades silently. A visible measure is what makes degradation someone's problem.

**Fix at the source.** Correcting data downstream means correcting it repeatedly, forever, and the two copies then disagree. This is the same principle as the authoritative source of truth in `digital-engineering`.

## Step 4: Lineage and provenance

Where data came from, what happened to it, and what depends on it. Necessary for three separate reasons:

- **Trust.** A number whose derivation cannot be traced cannot be defended when challenged.
- **Impact.** When a source changes or is found wrong, lineage says what else is affected. Without it, the answer is discovered by users.
- **Obligation.** Licensing, contractual restriction, export control and privacy all attach to origin. See `export-control-and-markings` and `contract-vehicles-and-clauses`.

**For AI this is not optional.** Training data provenance determines whether you may use the model, whether you can explain its behavior, and whether a claim about its evaluation means anything. `ai-governance` assumes you have this; it is built here.

**Capture lineage automatically from the pipelines**, not in a document. Manually maintained lineage is accurate on the day it is written.

## Step 5: Access, sharing and retention

**Classify, then control.** Access rules follow from what the data is, not from who asks. Where the data is CUI, export-controlled or otherwise restricted, the handling requirements are contractual and `export-control-and-markings` governs.

**Default to accessible within the boundary the classification allows.** Data locked away by default produces shadow copies, which are the actual governance failure — uncontrolled, unversioned and invisible.

**Make it findable.** A catalog people search is worth more than a comprehensive one nobody opens. Register what is used; let the rest be discovered when someone needs it.

**Retention is a decision with two failure modes.** Keeping everything forever grows cost and liability; deleting on a schedule that ignores contractual and records obligations destroys something you were required to keep. Get the schedule from the obligations, then automate it.

**Interoperability is a design property.** Common identifiers, standard formats, documented schemas and stable interfaces are what let data be linked later. The DoD data strategy framing — visible, accessible, understandable, linked, trustworthy, interoperable and secure — is a useful checklist precisely because it names the properties that have to be designed in rather than added.

## Step 6: Make it operate

- **Governance decisions need a route.** Somewhere a disputed definition or a new sharing request gets decided, quickly. A council that meets quarterly is not that.
- **Embed it where work happens** — in the pipeline, in the catalog, in the review — rather than as a separate compliance activity. See `devsecops-pipeline` for the same principle applied to security.
- **Measure the governance itself**: how long a definition dispute takes to resolve, how much of the data supporting real decisions has a named owner, how often quality thresholds are breached. If none of those improve, the program is documentation.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Inventory-first | Catalog project that never ends | Start from decisions that depend on data |
| IT owns everything | Nobody can settle what a field means | Named business owner per domain |
| Definitions undocumented | Two systems, two numbers, endless reconciliation | Write definitions once, with an owner |
| Global quality targets | Unaffordable or meaningless | Thresholds per use |
| Downstream correction | Copies diverge permanently | Fix at the source |
| Lineage in a document | Accurate the day it was written | Capture from the pipeline |
| Locked down by default | Shadow copies everywhere | Accessible within the classification boundary |
| Council as the operating model | Decisions take a quarter | A fast route for definition and sharing decisions |

The honest one is the last. Data governance fails far more often from being too slow to be used than from being too weak, and the shadow spreadsheet is what that failure looks like.
