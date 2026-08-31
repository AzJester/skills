# STRIDE by element type

Applying all six threats to all four element types produces noise. This matrix is the conventional applicability set, with the question to ask in each cell.

| | External entity | Process | Data store | Data flow |
| --- | --- | --- | --- | --- |
| **Spoofing** | ✓ | ✓ | | |
| **Tampering** | | ✓ | ✓ | ✓ |
| **Repudiation** | ✓ | ✓ | ✓ | |
| **Information disclosure** | | ✓ | ✓ | ✓ |
| **Denial of service** | | ✓ | ✓ | ✓ |
| **Elevation of privilege** | | ✓ | | |

Blank does not mean impossible, it means the threat is usually expressed against a neighboring element instead. Cross a blank cell deliberately, not by accident.

## External entities

**Spoofing** — How is this entity authenticated? What happens if the credential leaks? Can one entity present as another? Is authentication checked on every request or only at session start?

**Repudiation** — If this entity does something damaging, what evidence survives? Is it timestamped, signed, and stored where the entity cannot reach it?

## Processes

**Spoofing** — Can something impersonate this service to its callers? Is service-to-service identity verified, or is network position treated as proof?

**Tampering** — Can the running code or its configuration be modified? Who can deploy? Is the artifact signed and the signature checked?

**Repudiation** — Does this process log its security-relevant actions with enough detail to reconstruct who did what?

**Information disclosure** — What does it leak through error messages, stack traces, timing, logs, or debug endpoints? Do logs contain the data they process?

**Denial of service** — What is the expensive path, and can an unauthenticated caller reach it? Are there rate limits, timeouts, and bounded concurrency?

**Elevation of privilege** — Where is authorization decided? Is it decided once at the edge and trusted thereafter? Can input reach an interpreter — SQL, shell, template, deserialiser?

## Data stores

**Tampering** — Who can write? Is write access as tightly held as the design assumes? Are changes detectable after the fact?

**Repudiation** — Are writes attributable and is the audit trail itself protected from the writer?

**Information disclosure** — Encrypted at rest? Who holds the key? What does a backup, a replica, or a stale snapshot expose? Are deleted records actually gone?

**Denial of service** — Can it be filled, locked, or made slow by a caller? Is there a quota per tenant?

## Data flows

**Tampering** — Integrity protected in transit? Is TLS terminated somewhere unexpected, and what carries the data onward from there?

**Information disclosure** — Encrypted in transit? Does it traverse a network, a log aggregator, or a vendor you have not counted as a party to the data?

**Denial of service** — Can the flow be flooded, blocked, or delayed? What does the receiver do when it stops — fail closed, or fail open?
