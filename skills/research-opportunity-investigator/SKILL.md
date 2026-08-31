---
name: research-opportunity-investigator
description: Conduct systematic research and opportunity investigation for ACP protocol integration, collaboration, and enhancement opportunities. Use when the user wants to research external projects, protocols, or tools for potential collaboration; investigate gap-filling opportunities for IDE integrations; assess compatibility between ACP and external protocols; or identify opportunities for ACP adoption. Guides through discovery, analysis, validation, and RFC generation with mandatory gates and source grounding. Outputs include comprehensive summary documents, gap analyses, and formal RFC proposals.
---

# Research & Opportunity Investigator

Systematic research and opportunity analysis for ACP protocol integration with external projects, protocols, and tools.

## CRITICAL BEHAVIORAL REQUIREMENTS

**This skill operates under strict guardrails. The assistant MUST:**

### 1. NEVER Proceed Without Explicit User Confirmation
- Ask clarifying questions at EVERY phase gate before proceeding
- Do NOT proceed based on assumed understanding
- Wait for explicit user responses before moving forward
- Present findings and wait for validation

### 2. NEVER Make Ungrounded Claims
- All findings MUST reference specific sources (URLs, documentation, code)
- Format: `[Statement] (Source: [URL/document], [section])`
- If information cannot be verified, mark as: `[UNGROUNDED—requires verification]`
- Maintain running source registry throughout research

### 3. ALL Analysis Must Be Source-Grounded
- Every technical claim requires evidence
- Cite specific code, documentation, or announcements
- Distinguish between: `[VERIFIED]`, `[INFERRED]`, `[ASSUMED]`

### 4. Mandatory ACP Summary Document Before RFC
- MUST create comprehensive ACP summary document
- Summary MUST cover: existing RFCs, schemas, spec chapters
- Summary enables RFC validation against current state
- User MUST approve summary before RFC generation

### 5. RFCs Must Trace to Existing ACP Specification
- Every RFC proposal MUST reference existing spec sections
- Show which chapters/RFCs are affected
- Demonstrate compatibility with current design

---

## Workflow Overview

```
Research & Opportunity Investigation Workflow:

□ Phase 1: RESEARCH SCOPING
  ├─ Define research target and objectives
  ├─ Establish success criteria
  └─ GATE: User confirms research scope

□ Phase 2: DISCOVERY & COLLECTION
  ├─ Web search for documentation, repos, announcements
  ├─ Source registration and cataloging
  └─ GATE: User confirms source coverage

□ Phase 3: DEEP ANALYSIS
  ├─ Technical architecture analysis
  ├─ Feature mapping and comparison
  ├─ Gap identification
  └─ GATE: User confirms analysis accuracy

□ Phase 4: ACP CONTEXT SUMMARY
  ├─ Generate comprehensive ACP summary
  ├─ Map existing RFCs, schemas, spec chapters
  ├─ Identify integration points
  └─ GATE: User approves ACP summary document

□ Phase 5: OPPORTUNITY ASSESSMENT
  ├─ Gap analysis (what target lacks that ACP provides)
  ├─ Collaboration opportunities
  ├─ Implementation feasibility
  └─ GATE: User confirms opportunity assessment

□ Phase 6: RFC GENERATION
  ├─ Draft RFC for identified opportunities
  ├─ Validate against ACP summary
  ├─ Cross-reference existing specs
  └─ GATE: User approves RFC content

□ Phase 7: DELIVERABLES PACKAGING
  ├─ Final summary document
  ├─ Gap analysis report
  ├─ RFC proposal(s)
  └─ GATE: User confirms all deliverables
```

---

## Phase 1: Research Scoping

### 1.1 Scope Definition Template

```
═══════════════════════════════════════════════════════════════════════════════
🔍 RESEARCH SCOPE DEFINITION
═══════════════════════════════════════════════════════════════════════════════

RESEARCH TARGET:
  Name: [Project/Protocol/Tool name]
  Type: [IDE/Protocol/Framework/Tool]
  Primary URL: [Main website/repository]

RESEARCH OBJECTIVES:
  Primary Goal: [What are we trying to learn/achieve?]
  
  Specific Questions:
    1. [Question 1]
    2. [Question 2]
    3. [Question 3]

SUCCESS CRITERIA:
  □ [Criterion 1 - measurable outcome]
  □ [Criterion 2 - measurable outcome]
  □ [Criterion 3 - measurable outcome]

ACP INTEGRATION FOCUS:
  □ Gap-filling opportunity (target lacks capability ACP provides)
  □ Protocol integration (technical compatibility)
  □ Collaboration opportunity (partnership/adoption)
  □ Competitive analysis (understanding landscape)
  □ Other: _______________

───────────────────────────────────────────────────────────────────────────────
⚠️  Please confirm this scope before proceeding with discovery.
═══════════════════════════════════════════════════════════════════════════════
```

### 1.2 Scoping Questions

Ask these questions to establish research scope (2-3 per message max):

**Target Identification:**
- What specific project/protocol/tool are we researching?
- What is the primary URL or repository?
- What problem does this target solve?

**Objective Clarification:**
- What do you hope to achieve through this research?
- Are you looking for integration, collaboration, or competitive understanding?
- What would a successful outcome look like?

**Constraints:**
- Are there any aspects that are out of scope?
- What timeline or resource constraints exist?
- Are there any competing priorities?

---

## Phase 2: Discovery & Collection

### 2.1 Source Registration Template

```
═══════════════════════════════════════════════════════════════════════════════
📚 SOURCE REGISTRATION
═══════════════════════════════════════════════════════════════════════════════

REGISTERED SOURCES:

  [SRC-001] Official Documentation
    └─ URL: [url]
    └─ Type: documentation
    └─ Accessed: [date]
    └─ Relevance: [high/medium/low]
    └─ Key Sections: [list relevant sections]

  [SRC-002] GitHub Repository
    └─ URL: [url]
    └─ Type: source_code
    └─ Accessed: [date]
    └─ Relevance: [high/medium/low]
    └─ Key Files: [list relevant files]

  [SRC-003] ...

───────────────────────────────────────────────────────────────────────────────
SOURCE GAPS (information needed but not found):

  □ [Gap 1] - Required for: [analysis area]
  □ [Gap 2] - Required for: [analysis area]

───────────────────────────────────────────────────────────────────────────────
⚠️  Please confirm these sources are sufficient or identify additional sources.
═══════════════════════════════════════════════════════════════════════════════
```

### 2.2 Discovery Search Strategy

For each research target, systematically search:

**Tier 1 - Primary Sources (MUST search):**
```
□ Official documentation site
□ GitHub/GitLab repository
□ Official announcements/blog posts
□ API/Protocol specifications
```

**Tier 2 - Secondary Sources (SHOULD search):**
```
□ Technical blog posts from team members
□ Conference talks/presentations
□ Community discussions (Discord, Slack, Forums)
□ Integration guides from partners
```

**Tier 3 - Tertiary Sources (MAY search):**
```
□ Third-party reviews and analyses
□ Comparison articles
□ Issue tracker discussions
□ Social media announcements
```

### 2.3 Evidence Grounding Format

All findings MUST use this grounding format:

```markdown
[Finding Statement]
  └─ Source: [SRC-XXX], [specific section/line/page]
  └─ Evidence Type: [VERIFIED|INFERRED|ASSUMED]
  └─ Confidence: [HIGH|MEDIUM|LOW]
  └─ Quote/Reference: "[relevant excerpt]"
```

---

## Phase 3: Deep Analysis

### 3.1 Technical Architecture Analysis

For each research target, analyze:

```
═══════════════════════════════════════════════════════════════════════════════
🏗️ TECHNICAL ARCHITECTURE ANALYSIS
═══════════════════════════════════════════════════════════════════════════════

CORE ARCHITECTURE:
  
  Components:
    □ [Component 1]: [Description] (Source: [SRC-XXX])
    □ [Component 2]: [Description] (Source: [SRC-XXX])
  
  Data Flow:
    [Component A] → [Component B] → [Component C]
  
  Key Abstractions:
    □ [Abstraction 1]: [Purpose]
    □ [Abstraction 2]: [Purpose]

PROTOCOL/API DESIGN:
  
  Communication Pattern: [request-response/streaming/event-driven]
  Data Format: [JSON/Protocol Buffers/Other]
  Transport: [HTTP/WebSocket/IPC/Other]
  
  Key Endpoints/Methods:
    □ [Endpoint 1]: [Purpose] (Source: [SRC-XXX])
    □ [Endpoint 2]: [Purpose] (Source: [SRC-XXX])

EXTENSION POINTS:
  
  □ [Extension Point 1]: [How external tools integrate]
  □ [Extension Point 2]: [How external tools integrate]

───────────────────────────────────────────────────────────────────────────────
```

### 3.2 Feature Mapping Template

```markdown
## Feature Comparison Matrix

| Feature Area | Target Has | ACP Provides | Gap/Overlap |
|--------------|------------|--------------|-------------|
| [Feature 1] | [Yes/No/Partial] | [Yes/No/Partial] | [Gap/Overlap/None] |
| [Feature 2] | [Yes/No/Partial] | [Yes/No/Partial] | [Gap/Overlap/None] |

### Gap Details

#### Gap G-001: [Gap Name]
- **Target Status**: [What target lacks]
- **ACP Capability**: [What ACP provides]
- **Integration Potential**: [HIGH/MEDIUM/LOW]
- **Evidence**: (Source: [SRC-XXX])

#### Gap G-002: ...
```

---

## Phase 4: ACP Context Summary

### 4.1 Summary Generation Requirements

**BEFORE generating any RFC, MUST create comprehensive ACP summary covering:**

```
═══════════════════════════════════════════════════════════════════════════════
📋 ACP PROTOCOL SUMMARY DOCUMENT
═══════════════════════════════════════════════════════════════════════════════

Generated: [timestamp]
Purpose: Reference document for RFC validation and integration planning

───────────────────────────────────────────────────────────────────────────────
SECTION 1: SPECIFICATION OVERVIEW
───────────────────────────────────────────────────────────────────────────────

Current ACP Version: [version]
Spec Location: acp-protocol/acp-spec/spec/

Key Chapters:
  □ 01-introduction.md: [Summary of goals and non-goals]
  □ 03-cache-format.md: [Summary of cache structure]
  □ 04-config-format.md: [Summary of configuration options]
  □ 05-annotations.md: [Summary of annotation syntax]
  □ 06-constraints.md: [Summary of constraint system]
  □ [Additional relevant chapters...]

───────────────────────────────────────────────────────────────────────────────
SECTION 2: EXISTING RFCs
───────────────────────────────────────────────────────────────────────────────

RFC-001: Self-Documenting Annotations
  Status: [status]
  Summary: [brief summary]
  Key Changes: [what it introduced]
  Relevance to Research: [how it relates to current investigation]

RFC-002: Documentation References
  Status: [status]
  Summary: [brief summary]
  Key Changes: [what it introduced]
  Relevance to Research: [how it relates]

RFC-003: Annotation Provenance
  Status: [status]
  Summary: [brief summary]
  Key Changes: [what it introduced]
  Relevance to Research: [how it relates]

[Continue for all RFCs...]

───────────────────────────────────────────────────────────────────────────────
SECTION 3: SCHEMA INVENTORY
───────────────────────────────────────────────────────────────────────────────

Location: acp-protocol/acp-spec/schemas/

Schemas:
  □ cache.schema.json: [purpose, key fields]
  □ config.schema.json: [purpose, key fields]
  □ vars.schema.json: [purpose, key fields]
  □ sync.schema.json: [purpose, key fields]
  [Continue for all schemas...]

───────────────────────────────────────────────────────────────────────────────
SECTION 4: INTEGRATION POINTS
───────────────────────────────────────────────────────────────────────────────

Existing Integration Mechanisms:
  □ MCP Integration (acp-mcp): [current capabilities]
  □ CLI Interface (acp-cli): [current capabilities]
  □ LSP Planning (acp-lsp): [planned capabilities]

Extension Points for External Protocols:
  □ [Extension point 1]: [how external tools would integrate]
  □ [Extension point 2]: [how external tools would integrate]

───────────────────────────────────────────────────────────────────────────────
SECTION 5: DESIGN PRINCIPLES
───────────────────────────────────────────────────────────────────────────────

Core Principles (from spec):
  □ Self-documenting annotations
  □ Token efficiency
  □ Deterministic constraints
  □ Language-agnostic syntax
  □ Progressive disclosure

Compatibility Requirements:
  □ Backward compatibility policy
  □ Versioning approach
  □ RFC process requirements

═══════════════════════════════════════════════════════════════════════════════
⚠️  User MUST approve this summary before RFC generation proceeds.
═══════════════════════════════════════════════════════════════════════════════
```

### 4.2 Summary Validation Checklist

Before proceeding to RFC generation:

```
□ All existing RFCs cataloged with summaries
□ All relevant spec chapters summarized
□ All schemas inventoried with key fields
□ Integration points identified
□ Design principles extracted
□ User has reviewed and approved summary
```

---

## Phase 5: Opportunity Assessment

### 5.1 Gap Analysis Framework

```
═══════════════════════════════════════════════════════════════════════════════
🎯 OPPORTUNITY ASSESSMENT
═══════════════════════════════════════════════════════════════════════════════

GAP ANALYSIS:

  What [TARGET] Lacks That ACP Provides:
  
    GAP-001: [Gap Name]
      └─ Target Status: [Current capability or lack]
      └─ ACP Capability: [What ACP offers]
      └─ Strategic Value: [HIGH/MEDIUM/LOW]
      └─ Implementation Effort: [HIGH/MEDIUM/LOW]
      └─ Evidence: (Source: [SRC-XXX])
    
    GAP-002: ...

COLLABORATION OPPORTUNITIES:

  OPP-001: [Opportunity Name]
    └─ Description: [What could be achieved]
    └─ Mutual Benefit: [How both parties benefit]
    └─ Required Changes:
        - ACP: [What ACP would need to change/add]
        - Target: [What target would need to change/add]
    └─ Feasibility: [HIGH/MEDIUM/LOW]
    └─ Evidence: (Source: [SRC-XXX])

  OPP-002: ...

RISK ASSESSMENT:

  RISK-001: [Risk Name]
    └─ Description: [What could go wrong]
    └─ Likelihood: [HIGH/MEDIUM/LOW]
    └─ Impact: [HIGH/MEDIUM/LOW]
    └─ Mitigation: [How to address]

───────────────────────────────────────────────────────────────────────────────
RECOMMENDATION:

  □ Proceed with RFC development for: [specific opportunities]
  □ Defer: [what to defer and why]
  □ Decline: [what to decline and why]

───────────────────────────────────────────────────────────────────────────────
⚠️  Please confirm this assessment before RFC generation.
═══════════════════════════════════════════════════════════════════════════════
```

---

## Phase 6: RFC Generation

### 6.1 RFC Requirements

**MUST follow ACP RFC structure. See `references/rfc-template.md` for complete template.**

Key RFC sections required:
- Summary (2-3 sentences)
- Motivation with research basis and gap analysis
- Specification with affected components
- Backward compatibility analysis
- Implementation guidance
- Alternatives considered
- References to sources

### 6.2 RFC Validation Checklist

Before finalizing RFC:

```
RFC VALIDATION CHECKLIST:

Structure:
  □ All required sections present
  □ RFC number follows convention
  □ Status correctly set to Draft

Content:
  □ Summary is concise (2-3 sentences)
  □ Motivation clearly explains problem
  □ Research basis documented with sources
  □ Gap analysis included with IDs

Specification:
  □ All affected components identified
  □ Changes reference existing spec sections
  □ Proposed changes are specific and implementable
  □ Examples provided where helpful

Compatibility:
  □ Breaking changes identified (or stated as none)
  □ Migration path provided if needed
  □ Deprecation schedule if applicable

Validation:
  □ Cross-referenced against ACP Summary document
  □ No conflicts with existing RFCs
  □ Consistent with ACP design principles
  □ User has reviewed and approved
```

---

## Phase 7: Deliverables Packaging

### 7.1 Deliverable Checklist

```
═══════════════════════════════════════════════════════════════════════════════
📦 DELIVERABLES PACKAGE
═══════════════════════════════════════════════════════════════════════════════

RESEARCH DELIVERABLES:

  □ research-summary-[target]-[date].md
    └─ Complete research findings
    └─ All sources cataloged
    └─ Technical analysis complete
    
  □ gap-analysis-[target]-[date].md
    └─ All gaps identified with IDs
    └─ Opportunity assessment
    └─ Recommendations

ACP CONTEXT DELIVERABLES:

  □ acp-summary-[date].md
    └─ Current RFCs summarized
    └─ Schemas inventoried
    └─ Spec chapters mapped
    └─ Integration points identified

RFC DELIVERABLES:

  □ RFC-XXXX-[title].md
    └─ Complete RFC proposal
    └─ Validated against ACP summary
    └─ All sections complete

───────────────────────────────────────────────────────────────────────────────
QUALITY VERIFICATION:

  □ All sources cited with [SRC-XXX] format
  □ No ungrounded claims remain
  □ All assumptions marked as [ASSUMED]
  □ User approved each phase gate
  □ RFC traces to existing specification

───────────────────────────────────────────────────────────────────────────────
⚠️  Please confirm all deliverables are complete and accurate.
═══════════════════════════════════════════════════════════════════════════════
```

---

## Guardrails Reference

### Prohibited Behaviors

| Prohibited | Required Instead |
|------------|------------------|
| Making claims without sources | Cite specific source [SRC-XXX] |
| Proceeding without confirmation | Wait for explicit user approval at gates |
| Generating RFC without ACP summary | Create and approve summary first |
| Assuming target capabilities | Verify with source evidence |
| Skipping phases | Execute all mandatory gates |
| Ungrounded RFC proposals | Trace all changes to existing spec |

### Evidence Grounding Standards

| Evidence Type | When to Use | Example |
|---------------|-------------|---------|
| `[VERIFIED]` | Directly confirmed from primary source | Official docs, source code |
| `[INFERRED]` | Logically derived from verified facts | Architectural implications |
| `[ASSUMED]` | Reasonable assumption, needs validation | User must confirm |
| `[UNGROUNDED]` | Cannot find source | Flag for investigation |

### Source Confidence Levels

| Level | Definition | Usage |
|-------|------------|-------|
| HIGH | Official docs, source code, announcements | Core claims |
| MEDIUM | Blog posts, talks, community discussions | Supporting evidence |
| LOW | Third-party analyses, speculation | Context only |

---

## Reference Documents

- **RFC Template**: See `references/rfc-template.md` for complete RFC structure
- **Research Checklist**: See `references/research-checklist.md` for comprehensive checklist
- **ACP Spec Locations**: 
  - Specification: `acp-protocol/acp-spec/spec/`
  - RFCs: `acp-protocol/acp-spec/rfcs/`
  - Schemas: `acp-protocol/acp-spec/schemas/`

---

## Quick Reference

### Common Research Targets

| Target Type | Key Areas to Investigate |
|-------------|-------------------------|
| IDE | Extension API, LSP support, agent framework |
| Protocol | Message format, transport, extension points |
| AI Tool | Context handling, constraint system, codebase awareness |
| Framework | Plugin architecture, configuration, integration hooks |

### Common ACP Integration Points

| Integration Point | Relevance |
|-------------------|-----------|
| Bootstrap prompts | Minimal context injection |
| Cache format | Structured codebase metadata |
| Constraint system | Lock levels and guardrails |
| Annotation syntax | Self-documenting directives |
| Query interface | CLI commands for AI access |
| MCP integration | Dynamic tool connection |
