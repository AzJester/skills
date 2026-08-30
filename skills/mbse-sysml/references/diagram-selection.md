# Diagram selection and modelling patterns

## Choosing by the question

Start from the question, not from the diagram type. Most over-modelling comes from working the other way.

| The question | Diagram | Note |
| --- | --- | --- |
| What kinds of things exist, and what are they made of? | BDD | Types and composition, not a specific assembly |
| How is this assembly wired together? | IBD | Parts, ports, connectors, item flows |
| What crosses this boundary? | IBD with item flows | Then take it to `interface-control` for the agreement |
| What happens, in what order, to produce this output? | Activity | Object flows carry what moves between actions |
| Who talks to whom, and when? | Sequence | Best for protocols; shows where timeouts belong |
| What modes does it have, and what changes them? | State machine | The most under-built diagram in most models |
| Does this budget close? | Parametric | Mass, power, link, timing, thermal |
| Who uses it, for what? | Use case | Useful early, easy to overuse |
| What must it do, and what satisfies that? | Requirement relationships | The query matters; the diagram usually does not |

## Structure patterns

**Blocks are types; parts are usages.** A block `Battery` defined once may appear as three parts in an IBD. Modelling three separate blocks for three batteries is the most common structural error, and it breaks every roll-up that depends on the type.

**Ports carry interfaces.** A connector between two parts with no ports is a line. Proxy ports with interface blocks let the model say what actually crosses, which is what makes an interface checkable.

**Value properties carry the numbers.** Mass, power draw, latency, throughput — as typed value properties with units, not as text in a comment. Parametrics can only bind properties that exist.

**Keep logical and physical separate** where they differ. A logical function allocated to a physical component is a relationship worth recording; merging them discards the alternative allocations before anyone has evaluated them.

## Behaviour patterns

**Match the diagram to the question.** Activity for flow, sequence for interaction, state machine for modes. Modelling the same behaviour three ways produces three things to maintain and one to trust.

**State machines need the error states.** A state machine with only nominal states models the easy half. Degraded, failed, recovering, and safe states are where the design decisions live.

**Name events, not conditions.** `LossOfSignal` is an event; `signal < threshold` is a guard on a transition. Conflating them makes the machine hard to check.

**Model the timeout.** Every wait has a maximum. A sequence diagram showing a request and a response, with no timeout path, has documented the case that does not need documenting.

## Parametric patterns

The pillar with the highest return and the lowest adoption.

**Start with the tightest budget.** Whichever margin is smallest is where a constraint pays for itself first — usually mass, power, or timing.

**Roll up through composition.** Total mass binds to the sum of part masses, which bind to theirs. The model then tells you when an allocation breaks rather than a spreadsheet telling you three weeks later.

**Bind, do not compute.** Constraints are relationships that must hold, not one-way calculations. Modelled properly, a constraint can be solved in either direction — what mass budget does this leave for the payload?

**Carry margin explicitly.** Allocated, current best estimate, and margin as separate properties. A model showing only current values cannot say how much room is left, which is the question actually being asked at a review.

## Requirement patterns

| Relationship | Means |
| --- | --- |
| `satisfy` | This element meets this requirement |
| `verify` | This test case verifies this requirement |
| `derive` | This requirement follows from that one |
| `refine` | This element clarifies that requirement |
| `trace` | General dependency; use sparingly, since it says little |

The queries worth automating, and the reason to model requirements at all:

- Requirements with no `satisfy` — unallocated work
- Elements satisfying nothing — scope nobody asked for
- Requirements with no `verify` — feeds the VCRM in `verification-validation`
- Derived requirements whose parent has changed — the impact query

**`trace` is the escape hatch that hollows out a model.** When everything is traced to everything, no query returns anything useful. Prefer the specific relationship.

## Model review checklist

- [ ] Every element serves one of the model's stated questions
- [ ] Blocks are types; repeated things are parts, not duplicate blocks
- [ ] Interfaces have ports and item flows, not bare connectors
- [ ] Value properties carry units
- [ ] Behaviour exists beyond structure — state machines for anything with modes
- [ ] State machines include degraded and failure states
- [ ] At least the tightest budget is modelled parametrically, with margin visible
- [ ] Every requirement is allocated; no element satisfies nothing
- [ ] Depth follows responsibility boundaries rather than being uniform
- [ ] Orphan queries run automatically rather than by review
- [ ] Naming is consistent enough that search works
