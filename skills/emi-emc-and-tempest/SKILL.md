---
name: emi-emc-and-tempest
description: Design equipment to meet electromagnetic requirements and pass the chamber. Use when selecting MIL-STD-461 requirements for a platform, designing grounding, shielding, filtering or cable termination for EMC, planning pre-compliance testing, diagnosing an emissions or susceptibility failure, planning chamber time, or scoping emanations security for equipment that processes classified information. The most common late failure in tactical hardware.
---

# EMI, EMC and emanations security

**This is where tactical hardware programs fail, and they fail at the end.** The design is frozen, the tooling is cut, chamber time is booked, and the unit fails radiated emissions by 12 dB. Every fix available at that point — shield cans, ferrites, a gasket change, a filtered connector — is worse and more expensive than the layout change that would have prevented it.

The reason is structural: EMC performance is set almost entirely by decisions taken in the first weeks (grounding topology, board stack-up, where cables enter the enclosure) and measured almost entirely in the last weeks. Nothing else in hardware development has that gap between when it is decided and when it is discovered.

## Step 1: Select the requirements from the platform

MIL-STD-461 defines a set of emissions and susceptibility requirements, and which apply depends on the platform and installation. Selecting them is the first engineering act, and applying all of them by default is expensive.

| Family | Concerns | Typical driver |
| --- | --- | --- |
| **CE** — conducted emissions | What the equipment injects onto its power leads | Switching supplies, load transients |
| **CS** — conducted susceptibility | What it must tolerate on power leads and cables | Platform transients, bulk cable injection |
| **RE** — radiated emissions | What it radiates, electric and magnetic | Clocks, high-speed digital, switching, cable radiation |
| **RS** — radiated susceptibility | The external fields it must operate through | Co-located transmitters on the platform |

Three things to establish before design:

**Confirm the applicable set from the contract and platform**, not from a general assumption — the applicability differs by service and installation, and limits are often modified for a specific platform. Where the requirement is ambiguous, resolve it early; discovering an additional requirement late is the same problem as failing one.

**Radiated susceptibility levels are frequently the binding constraint on a tactical platform**, because a platform with high-power transmitters imposes field strengths that ordinary commercial design does not contemplate. This drives shielding and cable design more than emissions usually do.

**Commercial EMC standards are not equivalent.** A product that meets commercial emissions limits is not close to meeting military limits, which are generally far more demanding and measured differently. A design reused from a commercial product usually needs real work.

## Step 2: Design for it in the first weeks

Nearly all EMC performance is decided here, and none of it is expensive at this stage.

**Grounding and bonding.**
- Decide the grounding topology deliberately — single point, multipoint, or hybrid by frequency — and document it. An undecided grounding scheme becomes an accidental one, and accidental ones radiate.
- Bond the enclosure properly: low impedance, large contact area, paint removed at bonding surfaces, corrosion-compatible finishes.
- The chassis is part of the circuit at high frequency whether or not the schematic says so.

**Board design.**
- Stack-up first: solid, uninterrupted reference planes adjacent to every signal layer. A split plane under a fast signal is a slot antenna.
- Keep return current paths short and continuous. Most radiated emissions problems are return path problems.
- Manage clocks: spread spectrum where permitted, controlled edge rates, series termination. A slower edge that still meets timing radiates far less.
- Contain switching supplies — tight loop areas, local filtering, deliberate placement away from the enclosure boundary and from cables.

**The enclosure boundary is where EMC is won or lost.**
- **Every cable leaving the enclosure is an antenna** unless it is shielded, terminated properly and filtered at the boundary. Shield termination is the detail that matters: a 360-degree termination at the connector backshell works; a pigtail to a ground pin does not, and pigtails are the single most common cause of a failed radiated emissions scan.
- Filter at the point of penetration, not further inside. A filter downstream of where the cable enters has already let the energy into the box.
- Apertures matter by their longest dimension. Vents, seams, displays and connector cut-outs all leak; gasket compression and fastener spacing determine how much.

**Design in provisions you may not need.** Footprints for additional filtering, space for a shield can, a gasket groove. Unpopulated provisions cost almost nothing at layout and are the difference between a fix and a spin.

## Step 3: Test early, informally, and often

**Pre-compliance testing is the highest-return activity in this discipline.** A bench setup with near-field probes and a spectrum analyzer, used on the first real board, will not tell you whether you pass — but it will tell you where the energy is and whether you are 5 dB or 30 dB away. That distinction changes what you do next.

- **Near-field probing** locates sources on a board in minutes.
- **A partial radiated scan** in a modest setup gives you a relative measure, and relative is enough to know if a change helped.
- **Test at every build stage.** Engineering unit, EVT, DVT — see `hardware-product-development`. Each is an opportunity to find the problem while the design can still absorb the fix.
- **Test the real configuration.** Cables, mounting, grounding and the actual enclosure dominate the result. A bare board on a bench is not predictive of the assembled unit.

**Book formal chamber time early**, with margin for a re-test. Chamber capacity is a real constraint, and a program that assumes a single pass has an unmanaged schedule risk.

## Step 4: Diagnose failures methodically

A failure is a finding, and the temptation is to start adding ferrites. Work it instead:

1. **Characterize it.** Frequency, amplitude, margin to the limit, and whether it is broadband or narrowband. Narrowband at a clock harmonic and broadband from a switching supply are different problems.
2. **Locate the source.** Near-field probing, and selectively disabling subsystems.
3. **Determine the coupling path.** Is it radiating from the board, from a cable, or leaking through an aperture? Wrapping a cable in foil or temporarily closing a seam is a crude test that answers this in minutes.
4. **Fix at the source or the path**, in that order of preference. Source fixes are permanent; path fixes are add-ons with cost and reliability implications.
5. **Re-test the whole requirement**, because a fix can move energy rather than remove it.

**Record what you changed and what it bought**, in dB. This is the institutional knowledge that makes the next product easier, and it is almost never written down.

## Step 5: Emanations security, where classified processing is involved

Where equipment processes classified information, unintentional emanations are a separate concern from EMC, with separate requirements.

**The specific standards and limits are classified, and this skill does not contain them.** What is useful to know at an unclassified level:

- **It is a distinct requirement from MIL-STD-461** and passing EMC does not satisfy it. The concerns overlap in mechanism and differ in what is being protected against.
- **Involve the certified TEMPEST technical authority early.** The requirements depend on the equipment, the information, the installation and the inspectable space around it, and only that authority can tell you what applies.
- **It cannot be retrofitted.** The mitigations — separation of processing and unprotected signals, filtering, enclosure treatment, cable and connector selection, and installation constraints — are architectural. A design that reaches DVT before anyone asks the question is usually a redesign.
- **The installation is part of the solution.** Some requirements are met by the facility and the physical separation around the equipment rather than by the box, which makes this a shared problem with the customer — see `industrial-security`.

**Ask the question at concept.** "Will this ever process classified information?" is a one-minute question at the start and a redesign at the end.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| First EMC test at DVT | Fails with a frozen design | Pre-compliance from the first real board |
| Pigtail shield termination | Radiated emissions failure | 360-degree termination at the backshell |
| Split reference plane under fast signals | Broadband radiation | Solid, continuous planes; short return paths |
| Filtering placed inside the box | Energy already admitted | Filter at the penetration |
| Grounding topology undecided | Becomes accidental, radiates | Decide and document it early |
| Bare board tested | Not predictive of the assembly | Test the real configuration with cables |
| Commercial design reused | Nowhere near military limits | Expect real work; budget it |
| Emanations question asked late | Architectural change required | Ask at concept; involve the authority early |
| Single chamber booking | No room for a re-test | Book with margin; carry the risk |

The honest one is the first, and it is a management problem rather than an engineering one. Pre-compliance testing produces no deliverable and no milestone, so it is the easiest thing to defer — and deferring it is what makes the last month of the program expensive.
