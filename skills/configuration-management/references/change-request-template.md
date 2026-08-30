# Engineering change request

**ECR number** · **Raised by** · **Date** · **Class I / Class II**

## 1. Change

What changes, stated so someone who was not in the conversation can understand it. Reference the CIs and their current versions.

## 2. Reason

Why. One of: defect correction, requirement change, interface change, obsolescence, cost or schedule improvement, safety or security.

A change with no reason beyond "improvement" needs a sharper answer before it is assessed.

## 3. Affected configuration items

| CI | Current version | Proposed version | Baseline affected |
| --- | --- | --- | --- |

## 4. Impact assessment

The section that makes change control work. An ECR reaching the board with this incomplete is returned, not decided.

**Requirements** — which are added, changed, or deleted. Any that become untraceable.

**Interfaces** — which ICDs are affected, whether the change is backward compatible, and **whether the other side has been consulted**. An interface change assessed by one side only is not assessed. See `interface-control`.

**Verification** — which completed verification this invalidates. Name the VCRM rows that return to open and the events that must be re-run. This is the impact most often missed and the most expensive to discover later.

**Risk** — risks introduced, removed, or re-scored. Update `risk-management`.

**Measures** — which TPMs this moves, and in which direction. See `measures-of-effectiveness`.

**Cost and schedule** — including the cost of re-verification identified above, not only the cost of the change itself.

**Security** — whether the change crosses or alters a trust boundary. If so, the threat model needs revisiting. See `threat-modeling`.

## 5. Alternatives considered

Including doing nothing, and what happens if the change is not made. A change presented with no alternative invites the board to invent one.

## 6. Disposition

| | |
| --- | --- |
| Decision | Approved / Rejected / Deferred |
| Decided by | |
| Date | |
| Reason | |
| Conditions | |

Rejections carry reasons. A rejected ECR with no recorded reason gets raised again next quarter by someone who never learned why.

## 7. Implementation

Owner, target baseline, verification re-run required, closure criterion, and who confirms closure.
