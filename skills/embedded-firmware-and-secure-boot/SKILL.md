---
name: embedded-firmware-and-secure-boot
description: Build the software that runs on the box, and keep it trustworthy in the field. Use when planning a board support package or boot chain, designing secure boot and a hardware root of trust, planning firmware update for equipment that may never have reliable connectivity, designing anti-tamper or zeroization, or deciding what belongs in firmware versus hardware. Covers embedded software on a device; devsecops-pipeline covers the software factory that builds it.
---

# Embedded firmware and secure boot

Two things make firmware on a tactical edge device different from ordinary software, and both are about the field rather than the code.

**It may never have reliable connectivity.** Every assumption behind modern software delivery — push an update, roll back from a dashboard, watch telemetry — fails on a device that is disconnected for months and reachable only by someone physically standing next to it.

**A failed update is a brick in a place you cannot reach.** The cost of an update failure is not a rollback; it is a vehicle recovery, a maintainer visit, or a capability gap for the duration.

`devsecops-pipeline` covers the factory that builds and signs the software. This covers what runs on the device and how it stays trustworthy.

## Step 1: Decide what belongs in firmware

The decision that most affects the program, taken early:

**Put anything that might need to change in firmware.** Hardware changes cost a board spin and can invalidate qualification — see `hardware-product-development`. Firmware changes cost a build. Where a behavior is uncertain, implementing it in firmware buys you the option to be wrong.

**But firmware is not free.** It has to be developed, tested, qualified, signed, distributed and supported for the life of the product — which for defense hardware is far longer than the life of any toolchain, operating system or library you start with. A capability moved into firmware to save a board spin becomes a twenty-year maintenance obligation.

**Some things belong in hardware precisely because they must not change** — safety interlocks, and the root of trust itself. See `system-safety` on preferring mitigations that do not depend on software correctness.

## Step 2: Design the boot chain as a chain of trust

Each stage verifies the next before executing it, anchored in something that cannot be rewritten.

- **The root of trust is in hardware** — immutable boot code and keys held in a secure element, a trusted platform module, or fused into the device. A root of trust that software can rewrite is not one.
- **Every stage verifies a signature before transferring control.** Break the chain anywhere and everything above it is unverified.
- **Anti-rollback protection**, so an attacker cannot install an older signed image with a known vulnerability. Usually a monotonic counter in hardware. This is the control most often omitted, and reverting to a known-vulnerable signed image is a real attack.
- **Decide verified versus measured boot.** Verified boot refuses to run unsigned code; measured boot records what ran and lets something else decide. They serve different purposes and are not alternatives — a device that must operate regardless may need to measure rather than refuse.
- **Plan key management for the product's life.** Signing key custody, rotation, revocation, and what happens when a key is compromised on ten thousand fielded units. This is a program decision with contractual and security dimensions, not a build-system detail.
- **Decide what a verification failure does.** Refuse to boot, fall back to a known-good image, or boot degraded and report — and it is a mission decision, not an engineering preference. A sensor that refuses to boot is as unavailable as one that was destroyed.

## Step 3: Design update for the disconnected case

Assume the worst realistic case: no network, a maintainer with a laptop or removable media, and one attempt.

**Make updates atomic and recoverable.** The standard approach is two images: write the inactive one, verify it fully, then switch. Power loss at any point leaves a working device. A device that writes over its running image and loses power is the brick this whole section exists to prevent.

**Verify before switching, not after.** Signature, integrity and compatibility checked against the hardware revision and the current configuration while the old image is still intact.

**Automatic rollback on failure to boot.** A watchdog that reverts to the previous image after a failed boot attempt is what makes an unattended update survivable.

**Support offline delivery.** Signed update packages on removable media, verified by the device without contacting anything. This is the normal path, not the exception.

**Never require simultaneity across a system.** Devices will be at mixed versions for long periods, so interfaces must tolerate version skew in both directions — see `interface-control`.

**Keep the update path itself simple.** It is the one piece of software that must work when everything else is broken, and complexity in it is the least affordable complexity in the product.

## Step 4: Protect what is on the device

Tactical edge equipment is deployed where it can be captured, lost or examined. What it holds and what it reveals about how it works are both at risk.

- **Know what is sensitive**: cryptographic keys, mission data, configuration that reveals capability, and the software itself.
- **Zeroization** — a means to erase critical parameters reliably, invoked deliberately by an operator or automatically on a defined condition. Design what it erases, how long it takes, and how the operator knows it succeeded. An operator under pressure needs one control and unambiguous confirmation.
- **Tamper evidence and tamper response** are different levels. Evidence tells you afterwards; response acts at the time. Which is required comes from the threat and the customer, and response mechanisms have real false-trigger risk in a rough environment — a device that zeroizes itself during a hard landing is its own denial of service.
- **Debug interfaces must be closed in production.** Open JTAG or a serial console on a fielded device is the most common way a device gives up its secrets, and disabling them is a production step that has to be verified — see `manufacturing-and-npi`.
- **Where cryptography protects classified or otherwise regulated information**, the approval path for the implementation is set by the customer's security authority. Involve them early; it is not a decision the engineering team makes, and it has long lead time. See `industrial-security`.

## Step 5: Sustain it for the life of the platform

The obligation nobody prices at the start.

- **Pin and archive the whole toolchain**, not just the source. Being able to rebuild a bit-identical image in fifteen years means keeping compilers, libraries and build environments, not just a repository. `devsecops-pipeline` covers reproducible builds and provenance.
- **Generate an SBOM for the firmware.** Embedded software has dependencies with vulnerabilities like anything else, and a fielded device with no component inventory cannot be assessed when one is disclosed — see `supply-chain-security`.
- **Plan for the vulnerability you cannot patch quickly.** Where update requires physical access, the response to a disclosed vulnerability is a logistics operation. Knowing that in advance changes what you are willing to depend on.
- **Long-term support of the operating system and libraries is a selection criterion**, weighted like any other. A component with a two-year support horizon on a twenty-year platform is an obsolescence problem in software form — the same problem `component-selection-and-obsolescence` handles for parts.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Update assumes connectivity | Unusable in the field | Design offline update as the normal path |
| Single-image update | Power loss bricks the device | Two images, atomic switch, verify first |
| No anti-rollback | Old signed vulnerable image reinstalled | Monotonic counter in hardware |
| Root of trust in rewritable storage | Not actually a root of trust | Anchor in hardware |
| Verification failure behavior undecided | Device refuses to boot on a mission | Decide it as a mission question |
| Debug interfaces left open | Device gives up its secrets | Close in production; verify it as a test step |
| Toolchain not archived | Cannot rebuild in ten years | Pin and archive the build environment |
| No firmware SBOM | Cannot assess a disclosed vulnerability | Generate at build time |
| Crypto approval sought late | Long-lead approval blocks delivery | Involve the security authority early |

The honest one is the first pair together: a device that cannot be updated safely without connectivity, in a place where connectivity does not exist, has a security posture that is fixed at the moment it ships.
