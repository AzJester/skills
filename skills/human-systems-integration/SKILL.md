---
name: human-systems-integration
description: Design the system around the people who will operate and maintain it. Use when writing human performance requirements, analysing operator workload or task allocation, deciding what a human versus the system should do, planning manpower and training implications of a design, assessing human error potential, or arguing that a design is unusable by the people who will actually be given it. Covers the HSI domains as a programme discipline.
---

# Human systems integration

The discipline that asks whether the people who will operate, maintain and support the system can actually do so — at the manning level the programme assumed, with the training the programme funded, under the conditions the mission imposes.

It is the discipline most often cut first and most often implicated afterwards. "Operator error" as a mishap cause is usually a design finding written in the language of blame.

The failure this exists to prevent is a system that meets every technical requirement and requires more people, more skill, or more attention than the customer has.

## Step 1: The domains, and why they are one discipline

The exact list varies by service and framework, but the substance is consistent, and the point of treating them together is that they trade against each other.

| Domain | Asks |
| --- | --- |
| **Manpower** | How many people does operating and maintaining it require? |
| **Personnel** | What aptitudes and skills must they have? |
| **Training** | What training, how long, and how is currency maintained? |
| **Human factors engineering** | Can the tasks be performed correctly and quickly by those people? |
| **Safety** | What hazards does the human interaction create? — see `system-safety` |
| **Occupational health** | What exposures does operating or maintaining it produce? |
| **Habitability** | Are the living and working conditions adequate to sustain performance? |
| **Survivability** | Can the crew survive and continue in the threat environment? |

**The trades between them are the whole point.** Automation reduces manpower and raises training and skill requirements. Simplifying the interface reduces training and may raise development cost. Reducing crew size raises workload on those remaining and can affect survivability. Optimising any one domain in isolation moves cost into another, usually into manpower — which is the most expensive and the one the programme office does not pay for.

**Manpower is the dominant life-cycle cost driver** in most crewed systems. A design decision that adds one maintainer per unit across a fleet, for thirty years, outweighs a great deal of acquisition saving. `reliability-and-sustainment` covers the sustainment side of that same calculation.

## Step 2: Get in early, because the leverage is all at the front

HSI influence decays sharply with programme maturity. In concept and requirements it shapes the architecture; at design review it can change an interface; at test it can only document that the system is hard to use.

**Requirements are where the discipline is either real or decorative.** Human performance requirements should be written and verifiable like any other — see `requirements-dev` and `verification-validation`:

- Task completion within a stated time, by a defined operator population, under defined conditions
- Workload within acceptable bounds during defined mission segments
- Maximum training time to qualification
- Manning levels by watch or shift
- Error rates for critical tasks, where the task warrants it

**"User friendly" is not a requirement.** It cannot be allocated, designed to, or verified. Every unverifiable human requirement becomes an opinion argued at test.

## Step 3: Allocate function deliberately

What the human does and what the system does is an architecture decision, and defaulting it is how workload problems are created.

- **Do not automate simply because you can.** Automation changes the human's task from doing to monitoring, and humans are poor at sustained monitoring. The classic outcome is an operator who is bored for hours and then required to take over, without context, at the worst moment.
- **Keep the human in the loop where judgement is needed**, and give them the information to exercise it. An operator asked to approve a decision they cannot evaluate is providing accountability, not oversight. `ai-governance` makes this same point about human oversight designed so the reviewer can actually disagree.
- **Design the takeover.** Where automation can hand control back, the handover is the highest-risk moment in the system and needs designing as carefully as any other interface.
- **Consider the degraded case.** Function allocation that works when everything is nominal may put an impossible load on the operator when half the system is down — which is exactly when it matters. See `network-architecture` on designing for the degraded case first.

## Step 4: Analyse the work, with methods that produce evidence

- **Task analysis.** Decompose what the operator and maintainer actually do, in sequence, with the information and controls each step requires. The same discipline `procedural-documentation` uses, applied to design rather than to instructions.
- **Workload assessment.** Where a mission segment is demanding, assess it rather than assuming. Established subjective instruments and timeline analysis both give defensible numbers, and both are far cheaper than discovering the problem in operational test.
- **Error analysis.** What errors are possible, what makes them likely, and what the consequence is. Design out the likely and consequential ones rather than warning against them — this is the mitigation order of precedence from `system-safety` applied to human error.
- **Anthropometry and physical accommodation.** Reach, strength, visibility and clearance across the actual user population, wearing what they will wear. Design to the population range, not to the average, since the average person does not exist.
- **Test with representative users.** Not engineers who built it, and not only the exceptional operator. The population the system will actually be given to.

## Step 5: Manpower, personnel and training are outputs of design

These three are usually treated as someone else's problem and they are set by design decisions.

- **Manning estimates follow from task analysis**, not from the previous system's numbers. Inheriting the legacy manning figure is how a design that needs more people ships with the assumption that it does not.
- **Skill requirements must match who is actually available.** A design requiring an aptitude the customer's pipeline does not produce cannot be manned, however good it is.
- **Training time is a cost and a constraint.** A system requiring twice the training of the one it replaces has a fleet-wide availability consequence during transition.
- **Design for the maintainer as well as the operator.** Maintenance tasks are frequently harder, performed in worse conditions, and designed last. `reliability-and-sustainment` covers the access, isolation and standardisation decisions that decide whether maintenance is feasible.

## Step 6: Verify it like anything else

- Human performance requirements go in the VCRM with methods and events — see `verification-validation`.
- Workload, task time and error rate get measured with representative users during developmental test rather than discovered in operational test, where the finding is expensive and public. `test-and-evaluation` covers the operational side; `test-report` covers reporting the results honestly.
- **Suitability findings are findings.** A system that is effective but unsuitable — too hard to use, too demanding to man, too long to train — fails operationally, and the report should say so plainly.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| HSI engaged at test | Can only document the problem | Engage at requirements, where leverage is |
| "User friendly" as a requirement | Unverifiable; argued at test | Measurable human performance requirements |
| Domains optimised separately | Cost moves into manpower | Trade them together, explicitly |
| Automation by default | Bored monitor, bad takeover | Allocate function deliberately; design the handover |
| Nominal-case allocation | Impossible workload when degraded | Analyse the degraded case |
| Legacy manning inherited | Ships under-manned | Manning from task analysis |
| Design to the average user | Excludes much of the population | Design to the population range |
| Maintainer considered last | Maintenance infeasible in the field | Analyse maintenance tasks during design |

The honest one: "operator error" in a mishap report is nearly always a design decision that made the error easy, taken by someone who never watched the task performed.
