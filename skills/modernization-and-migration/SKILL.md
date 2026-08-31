---
name: modernization-and-migration
description: Replace or move a system that is already running. Use when assessing a legacy system, choosing between rehosting, refactoring, replacing and retiring, planning an incremental migration, moving data between systems, planning a cutover with a rollback, or arguing against a big-bang replacement. Covers migrating an existing system; cloud-architecture covers the target environment when that target is cloud.
---

# Modernization and migration

Replacing a system that works is harder than building one that does not exist yet, because the old one keeps running, keeps changing, and keeps being depended on in ways nobody wrote down.

The failure this exists to prevent is the big-bang rewrite: a multi-year parallel build, no incremental value, and a cutover date that slips until the program is canceled with both systems still running. This pattern has an unusually consistent track record and it is chosen anyway, because it is the easiest one to plan.

## Step 1: Find out what the system actually does

Before deciding anything, establish the ground truth. This takes longer than people expect and it is where most migration failures are actually caused.

- **What does it do that anyone depends on?** Including the reports someone runs monthly, the extract another team consumes, and the behavior a downstream system has come to rely on.
- **Who are the real users, and what do they actually do with it?** Usually a broader set than the sponsor believes.
- **What does it integrate with**, in both directions, including the interfaces nobody documented and the ones that are a scheduled file drop.
- **What is the data**, where does it come from, and what is its quality? See `data-strategy-and-governance`. Migration surfaces every quality problem that the old system has been tolerating.
- **What are the compliance and contractual obligations** attached to it — records retention, accreditation, data rights, audit trails?
- **What does nobody understand any more?** Name it explicitly. There is always some, and pretending otherwise puts it on the critical path unannounced.

**Behavior beats documentation.** Where the documentation and the running system disagree, the system is right — users have built their work around what it actually does, including its bugs. Some of those bugs are now requirements.

## Step 2: Choose the disposition per component, not per system

Applying one strategy to a whole system is the first mistake. Assess component by component.

| Option | Means | Right when |
| --- | --- | --- |
| **Retire** | Turn it off | Nobody could name a user or a dependency |
| **Retain** | Leave it alone | It works, it is stable, moving it earns nothing |
| **Rehost** | Move it, unchanged | A deadline forces the move; the system is otherwise fine |
| **Replatform** | Move with modest changes | Some benefit wanted for limited risk — often the best return |
| **Repurchase** | Replace with a product | The capability is not a discriminator |
| **Refactor** | Rebuild it | It is strategic, it changes often, and the current form blocks that |

**Retire and retain are the under-used answers**, because neither produces a project. A modernisation effort that begins by switching off three unused subsystems has already delivered value and reduced its own scope.

**Refactor is the most expensive option and should require the most justification.** "The technology is old" is not sufficient. The question is whether the current form is actually blocking something the organization needs to do. Where it is not, `cloud-architecture` on rehosting applies: relocate honestly rather than modernize ceremonially.

## Step 3: Migrate incrementally

**Strangle rather than replace.** Put a boundary in front of the old system, move one capability at a time behind it, and let the old system shrink until what remains can be switched off. Each increment delivers value, each is individually reversible, and the risk at any moment is bounded by one capability rather than the whole system.

This requires a seam. Where the legacy system has no clean boundary, creating one — a facade, an interface layer, an anti-corruption layer between the new model and the old one — is the first increment, and it is worth it. `codebase-design` covers the interface discipline and `interface-control` covers the agreement where the two sides have different owners.

**Sequence by risk and by learning, not by ease.** Doing the easy parts first feels productive and defers every hard question. Take one genuinely representative slice early — it is what tells you whether the approach works while changing course is still cheap.

**Run both systems in parallel where you can afford it**, and compare outputs. Parallel running is the single most effective way to find behavioral differences, and the differences it finds are always more numerous than expected.

**Do not let the old system freeze.** A migration lasting a year cannot stop the legacy system from changing, because the business does not stop. Plan for keeping up with changes as ongoing work, or the target is permanently behind.

## Step 4: Data is the hard part

It is almost always underestimated, and it is where cutovers fail.

- **Profile the data before designing the migration.** Actual values, actual quality, actual volume. Every legacy system contains records that violate its own rules.
- **Decide what to migrate.** Not everything deserves to move. Archive rather than migrate where the obligation is retention rather than use — and confirm the obligation before deciding.
- **Write the transformation rules explicitly**, including what happens to records that do not conform. "Handle exceptions manually" is not a plan when there are forty thousand of them.
- **Reconcile after every trial run.** Counts, totals, checksums, and spot checks of real records by people who know what right looks like. Automated reconciliation that only compares row counts misses the failures that matter.
- **Rehearse the migration repeatedly**, on production-scale data, timed. Cutover windows are set from these rehearsals rather than from an estimate.

## Step 5: Plan the cutover backwards from rollback

**Decide the rollback plan before the cutover plan.** If you cannot describe how to get back, you are not ready to go. This one discipline prevents most cutover disasters.

- **State the decision points and who decides.** At what time, on what evidence, does someone call it off? Agree it before the night, when everyone is tired and invested.
- **Know the point of no return.** Usually the moment users start writing to the new system. Everything before it is reversible; everything after is a forward fix.
- **Rehearse the rollback too**, not just the migration. An untested rollback is a hope.
- **Plan for the support surge.** The first week generates questions from users doing things nobody tested. Staff it deliberately, and expect a temporary productivity dip — see `organizational-change`.
- **Keep the old system available, read-only, longer than you think.** It is cheap insurance and it answers the questions that only arise afterwards.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Big-bang rewrite | Years of parallel build, slipping cutover | Strangle incrementally behind a seam |
| One strategy for the whole system | Refactoring things that should be retired | Disposition per component |
| Discovery skipped | Undocumented dependencies break at cutover | Establish ground truth first |
| Easy parts first | Hard questions deferred past the point of choice | A representative slice early |
| Legacy frozen in the plan | Target permanently behind | Plan to track ongoing changes |
| Data underestimated | Cutover fails on exception records | Profile early; explicit transformation rules |
| No rollback plan | Forward-only under pressure | Plan rollback first; rehearse it |
| Old system switched off immediately | No way to answer later questions | Keep it read-only for a while |

The honest one: the reason big-bang rewrites keep being chosen is that incremental migration requires building a seam that produces no visible feature, and that work is hard to fund. It is also the work that decides whether the rest succeeds.
