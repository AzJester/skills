---
name: agentic-system-design
description: Design a system where a model takes actions rather than answers questions. Use when deciding whether a task actually needs an agent, designing the tool surface, choosing between a single loop and multiple agents, managing context across steps, setting stop conditions and budgets, evaluating trajectories rather than outputs, or diagnosing an agent that loops, drifts or misuses a tool. Expands the one row ai-solution-architecture gives agentic approaches.
---

# Agentic system design

`ai-solution-architecture` places agentic last on its ladder of commitment with an honest one-line warning: failure modes multiply, cost and latency scale with steps, and it is the hardest to evaluate. All three are true and none of them tells you how to build one.

**The defining difference is that the output is a trajectory, not an answer.** A prompting system produces text you can check. An agentic system produces a sequence of decisions and actions, most of which nobody sees, some of which change the world. Everything hard about designing, evaluating and operating one follows from that.

## Step 1: Establish that you need an agent

The most valuable step, because the answer is often no.

| Use | Instead of an agent |
| --- | --- |
| The task is one transformation of known inputs | A prompt |
| It needs facts the model lacks | Retrieval |
| It is a fixed sequence of steps | A pipeline with model calls in it — deterministic, cheap, debuggable |
| The steps depend on what earlier steps found | **An agent** |

**A fixed workflow with model calls is not an agent, and is usually better.** It is cheaper, faster, testable and its failures are localized. Reach for an agent when the path genuinely cannot be known in advance — when what to do next depends on what was just discovered.

**"Agentic" is frequently applied to a pipeline for the wrong reasons.** It costs more, fails in more ways, and is harder to explain to an accreditor. Where a pipeline suffices, that is the answer.

## Step 2: Design the tool surface, because it is the capability boundary

**The tools define what the system can do — and what it can do wrong.** This is the highest-leverage design decision, and it is a security boundary as much as a functional one.

- **Fewer, better tools.** A surface of forty tools produces selection errors; the model picks a plausible wrong one. Consolidate, and prefer tools that do one comprehensible thing.
- **Tool descriptions are prompts.** They are how the model decides. Vague descriptions produce misuse that looks like model failure and is actually specification failure. State what it does, when to use it, when not to, and what it returns.
- **Classify every tool by reversibility.**

| Class | Design response |
| --- | --- |
| **Read** | Cheap to allow; watch the data it exposes |
| **Write, reversible** | Allow with logging and a way back |
| **Write, irreversible** | Confirmation, a human, or make it impossible |
| **External and visible** | Sending, publishing, paying — treat as irreversible |

- **Scope credentials to the tool, not the system.** An agent's blast radius is the union of everything its tools can reach.
- **Return errors the model can act on.** "Error 500" produces a retry loop; "the date must be within 30 days" produces a correction.
- **The tool surface is an attack surface.** Untrusted content reaching a model that holds tools is the central agentic security problem — content can carry instructions. `threat-modeling` applies, and the mitigations are architectural: least privilege on tools, confirmation on irreversible actions, and never granting a tool an authority the task does not need.

## Step 3: Prefer one loop until it demonstrably fails

**Multi-agent is usually premature.** Splitting into specialized agents adds coordination, message passing, context duplication and a new class of failure where two agents disagree or each assumes the other did something. The cost is real and immediate; the benefit is usually theoretical.

Reach for more than one loop when there is a genuine reason: genuinely parallel independent work, a context that cannot fit in one window, or a hard isolation boundary — different credentials, different trust levels, different data classifications.

**Where you do split, define the interface between agents properly.** What is passed, what is assumed, who owns what — see `interface-control`. An agent boundary is an interface, and undocumented ones fail the same way here as anywhere else.

## Step 4: Manage context, cost and stopping

**Context is a budget.** Every step adds to it — tool outputs, intermediate reasoning, retrieved material. Long-running agents fill the window and then lose the earliest content, which is frequently the original instruction. Decide deliberately what is retained, what is summarized, and what is dropped.

**Errors compound multiplicatively.** A 95% per-step success rate over twenty steps is not 95%; it is about 36%. This single arithmetic fact explains most disappointing agentic systems, and it argues for fewer steps, more reliable steps, and checkpoints where a bad trajectory can be caught before it propagates.

**Cost and latency scale with steps and are hard to predict**, because the number of steps varies with the input. `ai-cost-modeling` covers the agentic step tail as one of the consumers people miss — model the distribution, not the average, because the tail is what breaks a budget.

**Every agent needs stop conditions.** A step budget, a cost ceiling, a wall-clock limit, and a rule for repeated failure. An agent with no stop condition is an outage waiting for the right input. Decide what happens when a limit is hit — stop and report, escalate to a human, or return partial work — and make sure it is reported rather than silent.

## Step 5: Evaluate the trajectory, not just the answer

The genuinely hard part, and where most agentic projects are weakest.

- **A correct answer reached by a bad path is a latent failure.** It got lucky, and it will not next time. Evaluating only end state hides this entirely.
- **Evaluate at three levels**: did it reach the right outcome; did it take a reasonable path; and did each tool call do what it should have. The middle one is the one that gets skipped and the one that predicts production behavior.
- **Build the evaluation set from real trajectories**, including failures. `ai-evaluation` covers evaluation sets representative of deployment rather than of training — for agents that means real tasks with their real messiness, not clean examples.
- **Regression-diff trajectories between versions.** A prompt or tool change can alter behavior on cases nobody tested; comparing trajectories case by case is how that gets caught.
- **Build the failure taxonomy explicitly.** The recurring modes are specific: looping, drift off the original task, tool misuse, confidently selecting the wrong tool, cascading from a bad early step, and premature success declaration. Naming them lets you count them.

## Step 6: Operate it

- **Log the whole trajectory**, not the result — every step, tool call, argument and return. Without it an agent failure cannot be diagnosed, only observed.
- **The human in the loop must be able to disagree.** A confirmation prompt showing a summary the reviewer cannot verify is accountability theater — `ai-governance` and `human-systems-integration` both make this point.
- **Watch for silent degradation.** Agents fail gradually — slightly longer trajectories, slightly more retries — long before they fail visibly. Track steps per task and cost per task as leading indicators.
- **Where it runs unattended, be explicit about what it may do alone.** The gap between what a system is permitted to do and what anyone realized it was permitted to do is where the incidents live.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Agent for a fixed workflow | Cost and failure modes for no benefit | Use a pipeline with model calls |
| Sprawling tool surface | Plausible wrong tool selected | Fewer, well-described tools |
| Vague tool descriptions | Misuse that looks like model failure | Descriptions are prompts; write them as such |
| Irreversible actions unguarded | One bad step, real consequences | Confirm, gate, or make impossible |
| Multi-agent by default | Coordination failures added to everything else | One loop until it demonstrably fails |
| No stop conditions | Runaway cost, silent loops | Step, cost and time budgets with reported outcomes |
| End-state-only evaluation | Lucky trajectories pass | Evaluate outcome, path and each call |
| Result logged, trajectory not | Failures cannot be diagnosed | Log every step |

The honest one is the error arithmetic. Most agentic systems that disappoint are not badly built — they are built with per-step reliability that would be excellent in a single-shot system and is not nearly enough over twenty steps.
