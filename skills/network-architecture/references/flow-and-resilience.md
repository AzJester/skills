# Mission flow and resilience worksheet

## Flow inventory

Complete this before drawing a topology. The design follows from it.

| ID | Flow | From → to | Payload | Volume | Rate / burst | Latency tolerance | Loss tolerance | Classification | Priority | Consequence of failure |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

**Latency tolerance** — a real number, not "low". Interactive control, voice, situational awareness updates and bulk transfer differ by orders of magnitude, and GEO SATCOM rules out some of them regardless of bandwidth.

**Loss tolerance** — some flows tolerate loss and cannot tolerate delay; others the reverse. This determines transport and queuing more than raw bandwidth does.

**Priority** — used when capacity is insufficient, which in a contested environment is the expected case. A design with no priority scheme degrades arbitrarily.

**Consequence of failure** — where the design effort goes. A flow whose failure stops the mission justifies diverse paths; one whose failure is an inconvenience does not.

## Bandwidth derivation

Sum the flows, apply overhead, add growth, and state the assumptions:

| | Value | Assumption |
| --- | --- | --- |
| Sum of flow requirements | | |
| Protocol and encryption overhead | | typically 15–30%, state which |
| Peak-to-average ratio | | |
| Growth allowance | | over what period |
| **Derived requirement** | | |
| **Available capacity** | | per path |
| **Margin** | | |

A derived number with visible assumptions survives review. A number with no derivation gets challenged and cannot be defended, which is a bad position in an evaluation.

## Degraded mode matrix

The table that separates a real design from a nominal one.

| Capability | Full connectivity | Degraded (reduced bandwidth) | Intermittent | Fully disconnected | Reconnection behavior |
| --- | --- | --- | --- | --- | --- |

Fill every cell. "Not available" is a legitimate answer where the mission accepts it; a blank means the case was not considered.

**Reconnection behavior** is the column most often left empty and the one that causes integration problems. When two sides have diverged, what happens? Last-write-wins, merge, queue and replay, operator adjudication? Each has consequences the operator will experience, and choosing by default means choosing badly.

## Path diversity

| Path | Capacity | Latency | Availability assumption | Fails when | Failover trigger | Failover time |
| --- | --- | --- | --- | --- | --- | --- |

**Failover time** is what the operator experiences. Sub-second is a blip; ninety seconds is an outage they will report. State it, because it will be asked.

## Schedule dependencies

Network solutions are usually gated by approval processes rather than engineering:

| Dependency | Lead time | Owner | Started? | Blocks |
| --- | --- | --- | --- | --- |
| DoDIN connection approval | | | | |
| Cross-domain solution accreditation | | | | |
| Spectrum approval | | | | |
| Circuit provisioning | | | | |
| PKI and credential issuance | | | | |
| IP and DNS allocation | | | | |

Cross-domain and spectrum are the two that most often exceed the schedule allowed for them. Both belong in `risk-management` with realistic lead times from the start rather than as discoveries at integration.
