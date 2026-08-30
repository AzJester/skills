---
name: manufacturing-and-npi
description: Take a design from prototype to repeatable production. Use when applying design for manufacturability, assembly or test, selecting and qualifying a contract manufacturer, planning a production test strategy, running first article inspection or a production readiness review, setting workmanship class, diagnosing yield problems, or planning the transition from prototype builds to rate production.
---

# Manufacturing and new product introduction

A design that one skilled engineer can build once is not a product. The transition to something that can be built repeatably, by people who did not design it, at a yield that makes the cost model true, is a distinct engineering discipline — and it is the one most often assumed to be someone else's problem.

The failure this exists to prevent is throwing a working prototype over the wall to a contract manufacturer and discovering that it cannot be built at cost, at rate, or at all.

## Step 1: Design for it, while the design is still soft

The three disciplines, and what each actually asks:

| | Asks | Typical findings |
| --- | --- | --- |
| **DFM** — manufacturability | Can the boards and parts be fabricated reliably? | Trace and space below the fabricator's capability, hole sizes, panelisation, tolerances tighter than the process |
| **DFA** — assembly | Can it be assembled correctly and quickly? | Parts that fit two ways, hidden fasteners, connectors requiring three hands, assembly order that traps a screw |
| **DFT** — testability | Can it be tested in production? | No test access, no way to isolate a subsystem, no way to tell a good unit from a bad one |

**Run a DFM review with the actual fabricator and assembler, before layout is final.** Their capability data is what matters, not a generic guideline, and the review costs a meeting. Done after layout, every finding is a spin.

**DFT is the one most often skipped and the most expensive to add later.** Test points, boundary scan access, the ability to power subsections independently, and a way for the test to report which part failed rather than that the unit failed. Without it, production failures become debugging exercises, and debugging at rate is not viable.

**Design for the operator you will actually have.** Assembly instructions get followed by someone working quickly on their eighth unit of the shift — `procedural-documentation` covers writing them, and the same rules apply: one action per step, obvious right and wrong.

**Poka-yoke where the cost of error is high.** A connector that cannot be inserted backwards is worth more than a warning in the work instruction.

## Step 2: Choose and qualify the manufacturer deliberately

- **Match capability to the product**, not to price. Fine-pitch, high layer count, press-fit, conformal coating, potting and specialised finishes are not universal capabilities.
- **Check the quality system.** For defense and aerospace work, the relevant aerospace quality standard is usually expected, and it is a meaningful filter.
- **Agree the workmanship class explicitly.** Electronics assembly acceptability standards define classes with genuinely different requirements, and high-reliability class costs more and takes longer. Agreeing it after the quote is a dispute.
- **Understand who owns what** — consigned versus turnkey parts, tooling ownership, test fixture ownership, and what happens to all of it if you change manufacturers. Tooling you do not own is a switching cost you discover later. See `teaming-and-subcontracts`.
- **Visit.** A supplier audit finds things a questionnaire does not.
- **Flow down the real requirements**: counterfeit avoidance and traceability (see `component-selection-and-obsolescence`), ESD control, configuration control, and change notification. **A manufacturer who may substitute a part without telling you can invalidate your qualification silently.**

## Step 3: Build the test strategy before the first production build

Production test is a system with a cost, a cycle time and a fixture lead time, and it is routinely started too late.

| Stage | Catches | Note |
| --- | --- | --- |
| **Bare board test** | Fabrication defects | Done by the fabricator |
| **Automated optical inspection** | Placement and solder defects | Fast, catches the common assembly failures |
| **X-ray** | Hidden joints under packages | Necessary where leads are not visible |
| **In-circuit or flying probe** | Component presence, value, orientation, shorts | Needs test access designed in |
| **Boundary scan** | Digital interconnect | Cheap coverage if designed for |
| **Functional test** | Does it actually work? | The one that matters; needs a fixture and software |
| **Environmental stress screening** | Infant mortality | Decide deliberately — it costs time and consumes life |
| **Final and configuration check** | Right build, right firmware, right markings | Catches the mistakes that embarrass you |

Three decisions:

**Decide what "pass" means and what happens to failures.** A failed unit needs a route: rework, quarantine, analysis. Failures with no route accumulate on a shelf and teach nobody anything.

**Test fixtures are long lead and are always underestimated.** Design and build them in parallel with the product, not after it.

**Feed failures back.** Production test data is the best defect information you will ever get, and `pareto-analysis` on failure modes is what turns it into design and process improvement. `rcca-master` routes root cause when a mode recurs.

## Step 4: Run the introduction as a sequence

- **Pilot build first**, on production tooling, with production work instructions, by production operators — with the designers watching and not helping. Every question an operator asks is a work instruction defect; every time they hesitate is an assembly ambiguity.
- **First article inspection** verifies that the first unit off the process matches the drawing and the specification in every dimension and characteristic. It is a formal deliverable in aerospace work and it catches the drawing errors that would otherwise repeat across the run.
- **Production readiness review** before committing to rate — see `technical-reviews`. Its exit criteria are honest ones: process capable, yield understood, test coverage known, supply secured, documentation complete, operators trained.
- **Ramp deliberately.** Rate production magnifies everything, including problems that were tolerable at ten units.

## Step 5: Yield is a cost, and it is a design output

**First pass yield is the number that determines whether the cost model is true.** A design costed at 98% yield and running at 85% has a different unit cost and a different cycle time, and the gap usually surfaces after the price is committed.

- **Measure yield by stage and by failure mode**, not as a single number. One number tells you there is a problem; the distribution tells you where.
- **Most yield problems are design problems**, not workmanship. A joint that fails intermittently across many units is a footprint, thermal profile or tolerance problem.
- **Understand process capability against your tolerances.** A tolerance tighter than the process can reliably hold produces a permanent yield loss that inspection cannot fix.
- **Feed the real yield back into the cost model** — see `cost-estimating-and-boe`. An optimistic yield assumption is a quiet way to under-price a product.

## Step 6: Documentation and configuration, because production runs on it

- **The manufacturing data package is a deliverable**: drawings, bill of materials, assembly instructions, test procedures, acceptance criteria, and the approved parts and sources.
- **Every change goes through change control** — see `configuration-management`. A production line running to a revision nobody recorded produces units nobody can characterise later.
- **Know what a change requalifies.** A part substitution or a process change can invalidate environmental or EMC qualification.
- **Record what was actually built.** Serial number, revision, part lots, test results, firmware version. When a field failure arrives, this record is what tells you the scope of the problem — and without it every unit is suspect.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| DFM review after layout | Every finding is a board spin | Review with the fabricator before layout is final |
| DFT skipped | Production failures become debug exercises | Design test access in from the start |
| Workmanship class agreed late | Cost and schedule dispute | Agree the class before the quote |
| Test fixtures started after design | Ready weeks after the first build | Develop them in parallel |
| Pilot build assisted by designers | Work instruction defects hidden | Watch without helping; every question is a defect |
| Yield as one number | Problem visible, cause invisible | Measure by stage and failure mode |
| Optimistic yield in the cost model | Unit cost wrong after price commitment | Feed real yield back |
| Supplier substitution unnoticed | Qualification silently invalidated | Contractual change notification, enforced |
| As-built record incomplete | Field failure scope unknowable | Record serial, revision, lots, test, firmware |

The honest one: nearly every yield problem blamed on the factory is a tolerance, footprint or thermal decision made months earlier by someone who never saw the line.
