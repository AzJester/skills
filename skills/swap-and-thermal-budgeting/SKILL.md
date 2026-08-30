---
name: swap-and-thermal-budgeting
description: Fit a system inside a size, weight, power and cooling envelope. Use when setting or allocating SWaP budgets, designing a thermal path for a sealed or conduction-cooled enclosure, sizing power against a platform's electrical characteristics, trading compute performance against thermal headroom, planning for altitude derating, or deciding whether a design fits the platform at all. Covers fitting the envelope; ruggedization-and-environmental-qual covers surviving the environment.
---

# SWaP and thermal budgeting

Size, weight, power and cooling — the constraint set that decides whether a tactical edge product is installable. It is a single optimisation because the four are coupled: more compute means more power, which means more heat, which means more mass to remove it, which means more volume.

**Cooling is the binding constraint far more often than people expect.** Modern compute is thermally limited long before it is electrically limited: the silicon can draw the power, and the box cannot get rid of it. A design that meets its power budget and cannot dissipate the heat has not met its budget.

The failure this exists to prevent is a design that performs beautifully on a bench, in open air, at sea level, and throttles to half performance inside a sealed enclosure at altitude on a hot day — which is the condition it was built for.

## Step 1: Establish the envelope from the platform, not from a category

Every number comes from the installation. Get them before designing:

| Dimension | Establish |
| --- | --- |
| **Size** | The actual volume, including connector engagement, service clearance and cable bend radius |
| **Weight** | The limit, and whether it is structural, human-carry, or a platform mass budget |
| **Power** | Available power, its characteristics, and whether it is shared |
| **Cooling** | What the platform provides — ambient air, conditioned air, cold plate, or nothing |
| **Mounting** | Orientation, interface, and whether the mount is a thermal path |
| **Environment** | Maximum ambient, altitude, and solar loading — from `ruggedization-and-environmental-qual` |

**The volume you are given is smaller than the volume you can use.** Connector mating depth, cable bend radius, service access and keep-outs for the mount consume a real fraction of the envelope, and they are usually discovered after the boards are laid out.

**Ask what else shares the power and cooling.** On a vehicle or aircraft, your box is one load among many, and the available allocation may be well below the platform's total capacity.

## Step 2: Budget power against the platform's real electrical characteristics

Platform power is not a clean supply. Military vehicle, aircraft and shipboard electrical systems each have their own defined characteristics — nominal voltage, transient and surge behaviour, ripple, and interruption durations — and the input stage has to survive all of it. Confirm which standard applies to the platform and design the front end to it.

Four things that get missed:

**Budget worst case, not typical.** Maximum load, at maximum ambient, at end of life, with every component at its tolerance limit. Typical-case budgets are how a design that measured fine fails at qualification.

**Inrush is a requirement.** An uncontrolled inrush trips platform protection and makes you the problem on someone else's power bus. Size it, limit it, and state it.

**Hold-up through interruptions.** Platform power drops out — during engine start, during load switching. How long the system must ride through, and whether it must ride through or shut down gracefully, is a requirement that drives bulk capacitance and therefore volume.

**Efficiency is a thermal decision.** Every point of conversion efficiency is heat you have to remove. A 90% efficient supply in a 200 W box dissipates 20 W you must find a path for.

## Step 3: Design the thermal path deliberately

In a sealed, fanless enclosure — the normal case for tactical edge — heat leaves by conduction to the chassis and then by convection and radiation from the outside surface. There is no other route. Every interface in that path is a thermal resistance, and the total determines junction temperature.

**Trace the path explicitly, junction to ambient**, and put a number on each stage: die to case, case to heat spreader, through the interface material, to the chassis wall, and out. Where the total gives a junction temperature above the limit at maximum ambient, the design does not work and no amount of testing will change that.

The stages that dominate:

- **Interface materials.** Thermal interface material selection, thickness and compression are frequently the largest single resistance and the easiest to get wrong. Thicker is worse; a pad squeezed to the wrong thickness by a tolerance stack is a real failure mode.
- **Conduction path cross-section.** Heat needs metal. A thin path is a bottleneck regardless of what the material is.
- **Mechanical retention.** Conduction-cooled card architectures rely on clamping the card edge into the chassis rails; the clamping force is a thermal parameter, not just a mechanical one.
- **External surface.** Area, finish and orientation determine what the chassis can shed. A box mounted against a bulkhead loses a face.

**Altitude degrades convection, and the effect is significant.** Air density falls, so any cooling that relies on air — including natural convection from the chassis — degrades with altitude. A design validated on a bench at sea level has not been validated for an aircraft or a high-altitude ground deployment. This is one of the strongest arguments for conduction-cooled architectures: conduction to a mounting surface does not care about air density.

**Solar loading is a real input** for anything mounted outdoors. It can add tens of degrees to the effective ambient.

## Step 4: Trade compute against thermal headroom honestly

This is the central trade in edge compute and it should be explicit.

- **State the performance requirement at the worst-case thermal condition**, not at room temperature. "Sustained throughput at maximum ambient, at altitude, sealed" is the number that matters. Peak burst performance in a lab is not a requirement anyone can use.
- **Design for the throttled case, or design so it does not throttle.** Both are legitimate; what is not legitimate is a specification that assumes full clocks and a thermal design that cannot sustain them. If the system throttles, the requirement must be met throttled.
- **Consider lower-power silicon before a bigger thermal solution.** A part with 60% of the performance at 40% of the power frequently wins the system trade once mass, volume and the cooling structure are counted. `trade-study-analysis` is where this belongs, with SWaP as weighted criteria rather than an afterthought.
- **Junction temperature drives reliability, not just performance.** Sustained high junction temperatures shorten life measurably — feed this into `reliability-and-sustainment` rather than treating thermal as a purely functional constraint.

## Step 5: Allocate and manage the budgets

Treat SWaP as budgets with margin and owners, exactly as a mass budget is managed on any constrained platform.

- **Allocate down the architecture** — per board, per subsystem — so designers know their share. This is a parametric constraint in the sense `mbse-sysml` means: model it, and the model tells you when an allocation breaks.
- **Carry margin explicitly**, and separately from the estimate. Allocated, current best estimate, and margin as three numbers. A budget showing only current values cannot answer how much room is left, which is the question at every review.
- **Margin gets consumed, always.** Growth over a development is normal; a design with no thermal or mass margin at critical design review will not have any at delivery.
- **Track it as a technical performance measure** with a planned profile — `measures-of-effectiveness` covers doing this so the chart is worth having.

## Step 6: Validate it, in the real configuration

- **Build a thermal mule early** — a heater block dissipating the design power in the real enclosure, on the real mount. It answers the thermal question months before real boards exist and costs very little. See `hardware-product-development`.
- **Correlate the model against measurement.** A thermal model that has never been checked against a real article is an argument, not evidence.
- **Instrument junction and case temperatures** in the real assembly, at maximum ambient, sealed, in the mounting orientation. Every one of those conditions matters and the bench has none of them.
- **Measure at altitude** where the platform requires it — reduced-pressure thermal testing is a defined environmental method and it belongs in the qualification campaign.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Bench performance specified | Throttles in the real enclosure | Specify at worst-case thermal condition |
| Typical-case power budget | Fails at qualification | Worst case, end of life, max ambient |
| Thermal path not traced | Junction temperature unknown until test | Junction-to-ambient resistance, stage by stage |
| Altitude ignored | Convection assumption fails in the air | Conduction path; test at reduced pressure |
| Usable volume overestimated | Boards do not fit with connectors mated | Subtract mating, bend radius, service access |
| Inrush unmanaged | Trips platform protection | Size and limit it; state it as a requirement |
| No margin at CDR | Negative margin at delivery | Allocate with explicit margin; track it |
| Thermal model uncorrelated | Confident numbers, wrong answer | Thermal mule early; correlate to measurement |

The honest one: the thermal design has to be right before the electrical design is finished, because the thermal answer determines which parts you are allowed to choose.
