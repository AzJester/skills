---
name: network-architecture
description: Design and argue a network solution for a defense program. Use when architecting transport, designing segmentation, planning tactical or disconnected operation, addressing DoDIN connection requirements, framing a solution against JADC2 or CJADC2, sizing bandwidth against mission need, or writing the network section of a technical volume. Covers architecture and its justification, not device-level configuration.
---

# Network architecture

A network solution is judged on whether the mission still works when the network does not. Nominal-case designs are easy and are not what distinguishes a bid.

## Step 1: Start from mission flows, not topology

Before any topology, establish what actually has to move: which parties exchange what, how much, how often, how urgently, and what happens if it does not arrive.

| Flow | From → to | Volume | Rate | Latency tolerance | Loss tolerance | Classification | If it fails |
| --- | --- | --- | --- | --- | --- | --- | --- |

The last two columns carry the design. Classification determines separation and cross-domain handling. "If it fails" determines whether you need redundancy, buffering, or a degraded mode — and it is the column that most often reveals that a flow everyone assumed was critical is actually tolerant, or the reverse.

Sizing from flows produces a defensible bandwidth number. Sizing from a link speed someone mentioned produces a number that gets challenged and cannot be defended.

## Step 2: Design for the disconnected case first

In tactical and expeditionary contexts, DIL — disconnected, intermittent, limited-bandwidth — is the normal condition, not the exception. A design that works well connected and fails disconnected has solved the easy half.

Decide explicitly, per capability:

- **What must work with no connectivity at all.** Local processing, cached data, autonomous operation.
- **What degrades gracefully**, and to what. Reduced fidelity, longer intervals, queued rather than live.
- **What genuinely requires connectivity**, and what the mission does without it.
- **How state reconciles on reconnection.** This is the hard part and the part most designs leave until integration: two sides diverged, both changed things, and something has to merge them without losing data or duplicating actions.

Store-and-forward, opportunistic sync, and conflict resolution belong in the architecture, not in the implementation phase.

## Step 3: Transport, layered and diverse

Assume every path fails sometimes. Diversity is what turns that from an outage into a degradation.

| Path | Typical role | Fails when |
| --- | --- | --- |
| Terrestrial fibre / commercial | Bulk, fixed sites | Cut, contested, unavailable forward |
| SATCOM (GEO) | Wide reach, beyond line of sight | Weather, jamming, terminal availability; latency limits interactive use |
| SATCOM (LEO) | Lower latency, growing capacity | Coverage gaps, terminal cost, constellation dependency |
| Line-of-sight radio | Local, high rate | Terrain, range, emissions concerns |
| Cellular / commercial wireless | Convenient, permissive environments | Not available or trustworthy in contested ones |

Design the failover between them explicitly: what detects a path failure, how fast, what moves, and what the user experiences during the transition. Automatic failover that takes ninety seconds is an outage from the operator's point of view.

Where emissions matter, EMCON posture is an architectural constraint, not an operational afterthought.

## Step 4: Segment for containment

Segmentation exists to bound a compromise. It is also the network half of `zero-trust-architecture`, and the two should describe the same boundaries.

- **Macro segmentation** — mission systems, management plane, user enclaves, external interfaces.
- **Micro segmentation** — workload to workload, so lateral movement inside a segment is not free.
- **Cross-domain** — where classification boundaries are crossed, this is a cross-domain solution with its own accreditation, lead time and constraints. Assume both are longer than the schedule allows and plan accordingly.
- **Management plane separation** — the path administrators use is the path an adversary wants. Separating it is basic and frequently missed.

Every segment boundary is an interface with an owner on each side — see `interface-control`. Boundaries whose ownership is unclear are where exceptions accumulate until segmentation stops meaning anything.

## Step 5: DoDIN connection realities

Connecting to the DoDIN carries process that dominates schedule if discovered late:

- Connection approval processes with their own lead times and artifacts.
- Boundary protection at defined points, not wherever convenient.
- The accreditation package — see `rmf-ato`. Network boundary and system boundary must be the same boundary.
- IP addressing, DNS, and PKI governed centrally, not chosen by the programme.
- Spectrum, where RF is involved, with its own approval path.

These are schedule items with dependencies, and they belong in the IMS from the start rather than being discovered at integration.

## Step 6: JADC2 framing

Where a solution is positioned against JADC2 or CJADC2, the reviewers are looking for whether it *joins* rather than whether it works. The substance is:

- **Data first.** Open, documented, tagged data with defined interfaces — not a proprietary format behind an API.
- **Interoperability with named things**, and the standards that make it real. Vague claims about openness read as vague.
- **Decision timeline effect.** What sensor-to-effect timeline does this change, and by how much? An answer with a number is worth more than an architecture diagram.
- **Degradation.** Contested environments are the premise. A JADC2 story that assumes connectivity misses the point of the concept.

## Reference

- `references/flow-and-resilience.md` — the flow worksheet and the degraded-mode matrix.
