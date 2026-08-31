# Evaluation framework

The chain from mission question to collected data. A break anywhere means an issue that cannot be decided.

```
Critical operational issue      Can the unit accomplish the mission with this system?
  └─ MOE   effectiveness        Mission outcome achieved, in operational conditions
  └─ MOS   suitability          Can it be operated, maintained and sustained by real units?
       └─ MOP  performance      Technical parameter driving the above
            └─ Data element     What is actually recorded during an event
```

## Critical operational issues

Few — typically three to six. Each is a question whose answer could stop fielding. Phrased as a question, not a statement.

Good: *Can a company-sized element sustain operations for 72 hours without external resupply of the system's consumables?*

Poor: *System sustainment.* That is a topic, not an issue.

## MOEs, MOSs, MOPs

| | Asks | Owner's view |
| --- | --- | --- |
| **MOE** | Was the mission outcome achieved? | Operational |
| **MOS** | Can real units operate, maintain and support it? | Operational, sustainment |
| **MOP** | Does the technical parameter meet its value? | Engineering |

MOPs live in `measures-of-effectiveness` and are tracked as TPMs through development. The TEMP's job is committing to measure them under operational conditions, where they behave differently than on a bench.

**Suitability is where programs fail.** Reliability, maintainability, availability, logistics footprint, training burden, human factors, interoperability. A system that performs and cannot be sustained does not field. Give MOSs equal weight in the framework rather than treating them as secondary to effectiveness.

## Data requirements

For each measure, before the plan is agreed:

| Measure | Data elements | Event | Trials needed | Collection method | Fidelity |
| --- | --- | --- | --- | --- | --- |

**Trials needed** deserves a real answer rather than a convenient one. How many events are required to distinguish the system's performance from noise? `applied-statistics` covers sample size properly; a framework whose confidence claims are not supportable by its trial count will be challenged, correctly.

## Backward check

Run this before the framework is agreed, and again whenever resources change:

1. Every COI has measures beneath it.
2. Every measure has data elements.
3. Every data element has an event that produces it.
4. Every event has a resource line funding it.
5. Every measure has a threshold with a stated origin.

Any break in that chain is an issue that will not be decided, discovered at the point where it is most expensive to fix.
