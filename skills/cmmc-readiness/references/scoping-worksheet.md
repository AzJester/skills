# Scoping worksheet

Scope decides cost. Do this before assessing anything.

## Stage 1: Find the CUI

You cannot draw a boundary around information you have not located. Work through every place it plausibly lives:

| Location | CUI present? | Category | How it arrives | How it leaves | Owner |
| --- | --- | --- | --- | --- | --- |
| Email | | | | | |
| File shares | | | | | |
| Engineering / CAD / modelling tools | | | | | |
| Requirements and PLM tools | | | | | |
| Source control | | | | | |
| Laptops and endpoints | | | | | |
| Backups and archives | | | | | |
| Cloud services (each, named) | | | | | |
| Subcontractor and partner portals | | | | | |
| Print, scan, physical | | | | | |
| Personal or shadow copies | | | | | |

The last row is the one that breaks scopes. Somebody has a contract folder synced to a personal drive because it was convenient. Find it during scoping rather than during assessment.

## Stage 2: Categorise assets

| Asset | Category | Justification | Separation mechanism | Assessed? |
| --- | --- | --- | --- | --- |
| | CUI / Security protection / Contractor risk managed / Specialized / Out of scope | | | |

**Separation mechanism** is the column that makes a boundary defensible. For anything marked out of scope, name what prevents CUI reaching it — network segmentation, no data path, physical separation, enforced DLP. "Policy says not to" is not a mechanism, and an assessor will test it.

## Stage 3: Test the boundary

Before accepting a scope, try to break it:

- Can a user move a CUI file from an in-scope system to an out-of-scope one? By email, by USB, by cloud sync, by copy-paste, by print?
- Does an out-of-scope backup ever contain in-scope data?
- Does an out-of-scope administrator have credentials into the enclave? Administrative reach across a boundary pulls the administrator's system into scope.
- Do out-of-scope monitoring, patching, or identity systems reach into the enclave? If so, they are security protection assets, not out of scope.

Every yes either moves the asset in scope or requires a mechanism that turns it into a no.

## Stage 4: Cost the alternatives

Scoping is an engineering trade, and worth treating as one — `trade-study-analysis` applies.

| Option | In-scope assets | Assessment cost | Sustainment cost | User friction | Risk |
| --- | --- | --- | --- | --- | --- |
| Enclave — separate environment for CUI work | Fewest | Lowest | Moderate | Highest | Boundary leakage |
| Segmented — CUI zone within the enterprise | Moderate | Moderate | Moderate | Moderate | Segmentation drift |
| Whole enterprise in scope | All | Highest | Highest | Lowest | Cost, and every asset must meet every practice |

The enclave is usually cheapest to certify and hardest for users to live with, which is why enclaves fail by workaround rather than by design. Whichever option is chosen, the friction it creates is the thing to plan for — an enclave people route around is a boundary that no longer exists.
