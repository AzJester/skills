---
name: interface-control
description: Define and govern the boundary between two things that must work together. Use when writing or reviewing an interface control document (ICD) or interface requirements specification (IRS), defining an interface between subsystems, teams, or organizations, resolving a disagreement about who owns which side, or controlling a change to an interface that another party depends on. Covers the agreement and its change control, not the internal design either side. `mosa-and-open-standards` decides which interfaces are designated key and open.
---

# Interface control

Most integration failures are not failures of either side. They are failures of the agreement between them — two parties each built exactly what they believed, and the beliefs differed.

An interface control document exists to make that belief explicit, shared, and hard to change unilaterally. That last property is the one people skip, and it is the one that matters.

## Where this sits

`system-dev` models interfaces as typed registry slots (`intf-`) with behavioral contracts (`cntr-`). That is the *model* — what exists and what it connects. This skill covers the *agreement* — what two parties have committed to each other, who signs it, and what happens when one of them wants to change it.

Model an interface in `system-dev`. Govern it here. A program with modeled interfaces and no interface control discovers at integration that both sides evolved.

## Step 1: Establish the boundary and its two sides

An interface has exactly two sides, and each has exactly one owner. Where three parties meet, there are three interfaces, not one — resolving that early prevents the diffusion of responsibility that makes an interface nobody's problem.

For each side record: the owning party, the technical point of contact, and what that side is committing to provide or consume.

**The most common failure is an interface with one engaged owner.** One side writes the ICD, the other side never reads it, and everyone discovers at integration that it was a specification rather than an agreement. If the second side has not signed, there is no interface control — there is a document.

## Step 2: Specify what actually crosses

Cover every layer that applies. Omissions here are where integration surprises live.

| Layer | Specify |
| --- | --- |
| **Physical / transport** | Connector, medium, protocol, port, endpoint, addressing |
| **Data** | Format, schema, encoding, units, precision, byte order, mandatory versus optional fields |
| **Behavioral** | Sequencing, initiation, request/response versus event, idempotency, ordering guarantees |
| **Timing** | Rate, latency budget, timeout, retry policy and backoff |
| **Volume** | Message size limits, throughput, burst tolerance, quotas |
| **Error** | Error taxonomy, which side retries, what happens on partial failure, how each side degrades |
| **Security** | Authentication, authorization, transport protection, credential rotation |
| **Lifecycle** | Startup and shutdown ordering, versioning, deprecation policy |

Two fields cause more integration defects than the rest combined:

**Units and precision.** State them explicitly on every quantity. Meters or feet, milliseconds or seconds, UTC or local, inclusive or exclusive bounds. An unstated unit is an assumption held differently by two teams.

**Error behavior.** Most ICDs specify the happy path in detail and errors in a sentence. Integration then spends weeks discovering that one side retries indefinitely while the other treats a duplicate as a new transaction.

## Step 3: State the assumptions each side makes about the other

This section is usually missing and is often the most valuable. Each side records what it assumes about the other's behavior that the interface does not strictly require.

"We assume responses arrive in request order." "We assume the caller will not exceed 10 requests per second even though no quota is specified." "We assume this field is always populated even though the schema marks it optional."

Every such assumption is either a missing requirement or a latent defect. Writing them down converts a future integration surprise into a present conversation.

## Step 4: Baseline and control changes

An interface that either side can change is not controlled. Once agreed, the ICD is baselined under `configuration-management`, and changes follow change control.

For an interface change, the change request must state: what changes, which side initiates, whether it is backward compatible, what the other side must do, and by when. Both owners approve; where the interface crosses an organizational boundary, approval is contractual, not conversational.

**Backward-incompatible changes need a migration path, not a date.** "The v2 endpoint is removed on 1 June" is a plan for one side. "v1 and v2 run in parallel from 1 April, v1 removed 1 July, consumer confirms migration by 15 June" is a plan for both.

## Step 5: Verify the interface, separately

Interfaces get their own verification, because each side passing its own tests proves nothing about the pair. Feed these into `verification-validation`:

- Each side against the ICD, independently
- The pair together, at integration
- The error and boundary cases, deliberately — most interface verification exercises the happy path and discovers the rest in production

## ICD or IRS

Terminology varies and the distinction is worth keeping. An **IRS** states the requirements the interface must satisfy — the *what*, written early, often before either side is designed. An **ICD** documents the agreed design of the interface — the *how*, written once both sides are known. Small programs collapse them into one document, which is fine as long as everyone knows which one they are arguing about.

## Reference

- `references/icd-template.md` — the document structure, section by section.
