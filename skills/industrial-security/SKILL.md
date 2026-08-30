---
name: industrial-security
description: Handle classified work as a cleared contractor. Use when pursuing or holding a facility clearance, reading or writing a DD Form 254, sponsoring and tracking personnel clearances, planning classified storage or a secure area, running an insider threat programme, handling foreign ownership or influence, or reporting a security incident. Covers facility and personnel security; export-control-and-markings covers marking and export of controlled information.
---

# Industrial security

`export-control-and-markings` covers what a document is marked and who may receive it. This covers the facility, the people and the programme — the machinery that makes classified work possible at all, and the constraints it puts on schedules and staffing.

Two things make this a programme concern rather than a security-office concern: **clearance lead times drive schedules**, and **a security incident can affect the organisation's ability to hold classified contracts**. Both are consequences an engineering leader has to plan around.

The governing framework for cleared contractors is the National Industrial Security Program, implemented in federal regulation and administered by the cognisant security agency. Requirements change and are specific — work with your facility security officer rather than from memory, and treat what follows as what to plan for, not as authority.

## Step 1: Facility clearance, and what it does not give you

A facility clearance establishes that an organisation is eligible to access classified information at a given level. Three things about it that surprise people:

- **You cannot request one for yourself.** It must be sponsored — by a government contracting activity or by a cleared prime with a classified subcontract for you. This is why the teaming arrangement in `teaming-and-subcontracts` can determine whether you can bid at all.
- **A facility clearance is not permission to store classified material.** Storage requires separate approval, with physical safeguarding requirements that take time and money to meet. Many cleared facilities hold a clearance and store nothing.
- **Foreign ownership, control or influence must be resolved.** Ownership structure, foreign investment, foreign board members and foreign business relationships are examined, and where FOCI exists it must be mitigated through an approved arrangement before or alongside the clearance. This is a corporate matter with long lead times, and it is a live issue for any organisation with foreign investors or parent companies.

**The facility security officer is a required, cleared appointment**, and the role carries real personal responsibility. Insider threat programme responsibility is a related required appointment.

## Step 2: Personnel clearances are the schedule risk

**Plan clearances as a critical path item, because on classified programmes they usually are.** The sequence is sponsorship, submission of the security questionnaire, investigation, adjudication, then eligibility — and each stage has queues that do not compress for programme urgency.

Practical consequences for planning:

- **Start every clearance action immediately at award**, for everyone who will need one, regardless of their start date. See `program-startup`.
- **A clearance is not a badge to a specific programme.** Eligibility plus a need to know plus programme access are three separate things, and access to a specific compartment or programme may take substantial additional time after eligibility exists.
- **Cleared staff are a scarce, expensive resource** and hiring them is a competitive market. A staffing plan assuming you will hire cleared people at will is a risk, not a plan.
- **Continuous vetting means clearances can be affected mid-programme.** Financial difficulty, foreign contacts and unreported changes can all trigger review. This is a real staffing risk to carry in the register — see `risk-management`.
- **Reciprocity between agencies exists but is not automatic**, and a person cleared elsewhere may still take time to be granted access with you.

## Step 3: The DD Form 254

The contract security classification specification is the document that tells you what security requirements actually apply to a given contract. It is issued by the government, it is contractually binding, and it is frequently read for the first time long after award.

Read it for:

- **The classification level** authorised, and for what — access, generation, storage.
- **Whether performance is at your facility or the government's**, which changes everything about what you must provide.
- **Whether you may generate or only access** classified material.
- **Special access requirements**, compartments, or additional programme-specific controls.
- **Whether subcontracting is permitted**, and the requirement to issue your own DD 254 to any cleared subcontractor. Flow-down here is mandatory, not a choice — see `teaming-and-subcontracts`.
- **The classification guide** it invokes, which is what actually tells your engineers what is classified and at what level.

**Read the DD 254 during the pursuit, not at award.** It determines whether you can perform at all, and what infrastructure you would need. A programme discovering at kickoff that it requires storage the facility does not have is discovering a multi-month problem.

## Step 4: Physical safeguarding

Where classified work happens, the environment is part of the security control set.

- **Storage requires approved containers or approved areas**, with construction, access control and alarm requirements set by classification level and by the type of area.
- **Secure areas and sensitive compartmented information facilities have detailed construction and accreditation standards**, and accreditation takes time — plan it as a facility project with a schedule, not as a fit-out.
- **Classified processing on information systems is separately authorised.** A cleared facility does not imply an accredited system; that is `rmf-ato` work with additional constraints.
- **Visitor control and access records** apply, and visits between cleared facilities go through a formal process rather than a phone call.

The lead times here are long enough that facility capability should be an input to `capture-management` qualification. Bidding work that requires infrastructure you would have to build is a decision, and it should be a knowing one.

## Step 5: Insider threat and reporting

**A cleared contractor runs an insider threat programme.** Its purpose is to detect and address concerning behaviour before it becomes a compromise, and it involves gathering and reviewing indicators across security, human resources and information systems.

**Reporting obligations are broad and personal.** Cleared individuals are required to report a range of matters — foreign contacts and travel, financial problems, arrests, changes in personal circumstance, and concerning behaviour by others. The obligation to report on colleagues is uncomfortable and is nonetheless a condition of holding a clearance.

**Security incidents are reported, promptly.** Infractions and violations differ in seriousness but both are reported, investigated and recorded. Two things worth stating plainly to any team doing classified work:

- **Self-reporting a mistake is nearly always better than being found out.** The consequences of an unreported incident are consistently worse, for the individual and the organisation.
- **A pattern of incidents is an organisational finding**, not a series of individual ones, and it can affect the facility clearance itself.

## Step 6: What this means for engineering leadership

- **Classified work is slower**, and the schedule must reflect it. No working from home on it, no personal devices, no convenient collaboration tools, restricted hours in accredited spaces, and every document movement controlled.
- **Staffing is constrained by clearance eligibility**, not just skill. The best engineer for the work may be ineligible, and eligibility itself takes time.
- **Classification decisions come from a guide, not from judgement.** Where the guide is unclear, the answer comes from the government security authority. Guessing upward wastes money; guessing downward is a security violation.
- **Unclassified work adjacent to classified work needs a deliberate boundary**, or it drifts into classified by aggregation. Aggregation — where individually unclassified facts become classified together — is the subtlest classification problem in practice and it catches experienced people.
- **The programme's security requirements belong in the estimate.** Cleared labour, facility costs, and the productivity effect of a secure environment all cost money — see `cost-estimating-and-boe`, where security is one of the most commonly omitted elements.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Clearances started at need date | Staffing is the critical path | Start at award, for everyone |
| DD 254 read at kickoff | Infrastructure requirement found too late | Read it during the pursuit |
| Facility clearance assumed sufficient | No storage or accredited system | Confirm what is actually authorised |
| FOCI unexamined | Clearance blocked by ownership structure | Resolve early; it is a corporate lead-time item |
| Security cost omitted from the estimate | Overrun from cleared labour and facilities | Price cleared labour, facilities, productivity |
| Aggregation ignored | Unclassified work drifts classified | Deliberate boundary; ask the guide |
| Incidents unreported | Far worse consequences than the incident | Self-report; make it safe to |
| Subcontractor DD 254 not issued | Mandatory flow-down missed | Issue one for every cleared subcontract |

The honest one is the first, and it is the one that most reliably costs money: schedules on classified programmes are frequently built as if the people are already cleared, and they are not.
