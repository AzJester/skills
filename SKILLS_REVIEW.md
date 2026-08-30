# Skills Correctness Review

A correctness and accuracy review of the 85 author-written skills in this repository, run 2026-08-30. Vendored and third-party skills were out of scope.

**Method.** Three passes. First, a mechanical lint of all 85 skills: YAML frontmatter validity, name-to-directory match, description length and file references. Second, a review by 21 domain-grouped expert agents, each reading every file of its assigned skills and checking standards citations, formulas, worked-example arithmetic, framework definitions, internal consistency and cross-skill references. The `architecture-diagrams` scripts were actually run against the shipped example spec, and `which-skill` was checked route by route against the real inventory. Third, every medium and high finding went to an independent adversarial verifier told to refute it, with web lookup of primary sources where needed, and skills that came back clean got a second-pass audit of every checkable number, cite and formula.

**Result.** The collection is in good shape. Sixteen errors were confirmed by independent verification, one of them a formula that inverts its own intent. Eighteen minor issues were logged at low severity. Sixty-five skills came through both passes with nothing to report. Nothing the reviewers flagged was refuted, which says the confirmed list is conservative rather than padded.

| | Count |
| --- | --- |
| Skills reviewed | 85 |
| Confirmed errors (independently verified) | 16 |
| Minor issues (low severity) | 18 |
| Findings refuted on verification | 0 |
| Skills with no findings | 65 |

**Status:** all 16 confirmed errors below are fixed on this branch. The findings are kept as written, as the record of what was wrong and why. The 18 low-severity notes remain open.

---

## The one high-severity error

### ai-cost-modeling: the caching term in the cost formula is inverted

`SKILL.md`, Step 3 cost build-up:

> `÷ (1 − cache_hit_rate)ish, where caching applies`

Dividing by (1 − hit rate) makes modeled cost go **up** as the cache hit rate rises. At an 80% hit rate the formula multiplies cost by five. As the hit rate approaches 1 it diverges. That is the opposite of what caching does, and it contradicts the skill's own Step 4, which says prompt caching "often cuts input cost substantially." Anyone modeling a cached workload with this formula gets a unit cost that is wrong by a large factor, in the direction that kills good projects.

**Fix.** Apply the adjustment multiplicatively, and only to the cacheable slice of input cost (output tokens, retries, embeddings and surrounding compute are untouched by caching):

```
cacheable_input_cost × [(1 − h) + h × rate_cache_read / rate_in]
```

which is roughly × (1 − h) when cache reads are much cheaper than base input. Add the cache-write premium on misses if you want the exact number.

---

## Confirmed errors (medium severity)

Every item below was independently re-verified against the file and, where relevant, a primary source.

### technical-reviews and configuration-management: functional baseline placed at SRR

Both skills put establishment of the functional baseline at SRR, with SFR only refining it. `technical-reviews/SKILL.md` gates table says SRR establishes "Functional" and SFR "Functional (refined)", and `references/gate-criteria.md` repeats it in the SRR and SFR exit criteria. `configuration-management/SKILL.md` baseline table says "Functional | SRR", mirrored in `references/baseline-record.md`. In DoD practice (DoDI 5000.88, DAU, IEEE 15288.2) SRR establishes no baseline. The functional baseline is established at SFR, when the system performance specification goes under configuration control. The two skills are consistent with each other, which means the error propagates. PDR/allocated and CDR/product rows are correct in both.

### rmf-ato: RMF presented as six steps, missing Prepare

`SKILL.md` runs "Step 1: Categorize" through "Step 6: Monitor". That is the superseded SP 800-37 Rev 1 structure. Rev 2 (2018) has seven steps starting with Prepare, which covers the risk management strategy, authorization boundary determination and common control identification. The skill's own Step 4 boundary and inherited-control guidance would anchor naturally in a Prepare step. Everything else in the skill checked out, including the CNSSI 1253 versus FIPS 200 distinction, IATT and the package contents.

### network-architecture: DIL expanded with four words

`SKILL.md` line 23: "DIL — denied, disrupted, intermittent, limited". A three-letter acronym with a four-word expansion. The four-condition concept is DDIL (denied, degraded, intermittent, limited). If you keep DIL, its expansion is disconnected, intermittent, limited-bandwidth.

### acm-paper: `sigchi` listed as a live format

The common-formats table offers `sigchi` as a SIG-specific variant a community may require. acmart retired `sigchi` and `sigchi-a` in v1.71 (2020). Current acmart warns and silently switches it to `sigconf`, which is what SIGCHI venues actually use. `sigplan` in the same row is still real.

### nasa-sti: data compilations attributed to the wrong series

The series table gives the Technical Memorandum "extensive data compilations". Under NASA's definitions (NPR 2200.2), compilations of significant data with continuing reference value are Technical Publications. The TM is for preliminary or specialized findings and explicitly does not carry extensive analysis. Following the table routes a data compilation to the wrong series.

### chicago-turabian: the multi-author rule matches no edition of Chicago

`SKILL.md` line 97: "Three or more authors: in notes, first author plus `et al.`; in the bibliography, all listed up to ten." The notes half is CMOS 18. The bibliography half is CMOS 17. Under CMOS 17 the notes rule is wrong (et al. starts at four authors, not three). Under CMOS 18 the bibliography rule is wrong (list up to six, then first three plus et al., not ten). The skill elsewhere aligns itself with current Chicago, so the bibliography half is the one to fix.

### latex-authoring: two different float errors conflated

The error table maps "Float(s) lost" to the too-many-unplaced-floats diagnosis and fix. Those are different errors. "Too many unprocessed floats" is the full float queue, and placing floats earlier or relaxing placement fixes it. "Float(s) lost" means a float was discarded because it sat in inner mode (minipage, parbox, footnote, marginpar), and the fix is moving it into the main text flow. The table's advice will not fix the error it names.

### ruggedization-and-environmental-qual: sealed enclosures do not solve altitude

The altitude row claims "Convection cooling degrades with air density; sealed enclosures avoid this." Sealing preserves internal air density at best. The chassis still has to reject heat to thin ambient air, so external convection degrades all the same. The sibling `swap-and-thermal-budgeting` gets this right and names a conduction path to the mount as the mitigation, so the two skills currently disagree.

### diagram-picker: offered styles do not map onto the renderer

The skill claims the style answer "maps straight onto" architecture-diagrams' `--styles` flag. Of the three concrete styles it offers, only Blueprint is a valid key. `render.py --styles hand-drawn` exits with "Unknown style", and "technical clean" is not a key or alias either. The handoff needs an explicit mapping: technical clean → corporate or minimal-flat, hand-drawn → chalkboard, blueprint passes through.

### which-skill: routing map points at README sections that do not exist

The router tells readers to narrow to a README section and read its table, but several "Look under" labels name sections the README does not have ("Programme & business", "Working across units", "Solution domains", "Security", "Defense", "Incident", "Digital engineering"), and some skills are attributed to the wrong existing section (section-508-conformance belongs under "UI & UX"). Every one of the ~100 skill names the router mentions does exist, and every spot-checked description matched the target skill. Only the section navigation is broken. Either rename the labels to the README's real headings or drop section navigation and rely on skill names.

### architecture-diagrams: four confirmed defects

1. **`references/cloud-icons.md` promises a glyph fallback that does not exist.** The doc says an unmapped `aws:` key "falls back to a styled box with a generic glyph". `glyphs.py get()` returns None for unmatched keys and never reaches the `generic` entry, so the node renders with no icon at all. Six AWS keys the same file documents as mapped (aurora, dynamodb, elasticache, cognito, eventbridge, step) have no glyph entry. Rendering the shipped example proves it: the `aws:elasticache` node is the only icon-less node in its tier, violating the file's own warning about mixing icon and no-icon nodes. Fix both halves: add the six aliases and make `get()` return the generic glyph for unmatched non-empty keys.
2. **PNG output depends on an undocumented package.** `SKILL.md` step 5 requires looking at the PNG before delivering, but PNG export needs cairosvg, which is mentioned nowhere in the skill. Without it, render.py prints "PNG export skipped" to stderr and exits successfully with no PNG. Document the dependency and the fallback (inspect the SVG or HTML).
3. **The canonical example renders with a defect the skill tells users to fix.** In `assets/example-3tier.json` the Application Tier orders nodes api, svc, fn, queue, so the same-tier svc→queue "publish" edge runs under the Lambda Workers box. The label hides behind the node and the edge reads as a false ECS→Lambda connection. Reorder to api, svc, queue, fn.
4. **`mxgraph.azure2.*` is not a stencil namespace.** `cloud-icons.md` (and the prefix list in `drawio-xml.md`) tell users to add Azure shapes via `shape=mxgraph.azure2.*`. draw.io's Azure2 set is image-based (`image=img/lib/azure2/<category>/<Icon>.svg`), and the old stencil set is `mxgraph.azure.*`. Following the doc produces blank shapes. The gcp2, kubernetes, cisco19 and veeam2 prefixes in the same list are real.

---

## Minor issues (low severity)

Logged by the reviewers but not independently re-verified, so spot-check before editing. All were quoted verbatim from the files.

| Skill | Issue |
| --- | --- |
| stig-and-hardening | CIS Level 1/2 called "levels of severity". They are hardening profiles (baseline versus defense-in-depth), not severity ratings. Severity categories are a STIG concept. |
| wbs-and-scheduling | The checklist introduced as the DCMA 14-point assessment lists 13 items. CPLI (metric 13) is missing, and "completion index" is not a DCMA metric name. The two index metrics are CPLI and BEI. |
| quality-management-system | Says `rcca-master` "routes across the eight methods". It orchestrates 8D (eight disciplines) and routes five D4 analysis tools. No eight-method set exists. |
| program-recovery | OTB described as baselining "above the contract value". The threshold is the Contract Budget Base (negotiated cost plus authorized unpriced work, excluding fee). |
| solution-shaping | Prose and Step 6 say three discriminator tests. The table in the same file and the worksheet require four. Pick one count. |
| engineering-to-proposal | Hands off to `executive-summary-builder` and `mck-pyramid-checker`, neither of which is in this repo (both are account-level skills in one environment). Qualify or relocate. |
| business-case | Cites `decision-tree-ev` as if a sibling. Not in the repo. executive-decision-memo handles the same situation correctly by saying "your account's". |
| chicago-turabian | Page-range elision "exceptions in the teens and for numbers ending in zero" misstates Chicago (the teens exception is Hart's, and only multiples of 100 keep all digits). It also contradicts the file's own correct 120–45 example. |
| structured-interviewing | Behavioural questions called "the best available predictor" one paragraph before work samples are "the strongest signal available". Both cannot be top. |
| swap-and-thermal-budgeting | Inverted bolded rule: "The volume you are given is smaller than the volume you can use." Its own following sentence and failure table say the opposite, which is the intended point. |
| component-selection-and-obsolescence | Attributes obsolescence line items to `cost-estimating-and-boe`'s commonly-omitted list. That skill names none of them. |
| ai-governance | `references/use-case-record.md` uses the rights-impacting/safety-impacting split from OMB M-24-10, rescinded April 2025 by M-25-21, which uses a single high-impact category. The obligations list already matches M-25-21. |
| section-508-conformance | Undue burden described as assessed "against the agency's overall resources". E202.6.1 scopes it to the resources of the program or component involved. |
| diagram-picker | "Six more styles beyond the four offered" is wrong under any reading: the catalog has 10 entries and only three of the four offered options are styles. Also, `references/styles.md` points at an `mcbranding` skill that is not in this repo. |
| architecture-diagrams (scripts) | Three script-level nits: literal `%%` lands in the shadow/glow SVG filter attributes (invalid lengths, renderers fall back to the default filter region), eight `fx` style tokens are declared but never consumed and the docstring points at a `render.py EFFECTS` registry that does not exist, and `spec-schema.md`'s label guidance says the font shrinks past 30 characters when the code shrinks at 24. |

---

## What held up

The clean half of the review matters as much as the findings. Things checked hard and found correct:

- **Every EVM formula and worked example** in earned-value-management: CV, SV, CPI, SPI, all three EAC variants, TCPI, the SPI end-of-program caveat and the CPI-stability research claim.
- **The full STRIDE-per-element matrix and every NIST SP 800-53 control family code** in threat-modeling, and the SP 800-61 lifecycle in incident-response.
- **CMMC and SPRS mechanics**: DFARS 7012/7019/7020/7021, the 110 requirements, the 1/3/5-point deduction methodology starting at 110 with negative scores possible.
- **MIL-STD-882E** severity categories, probability levels and order of precedence in system-safety, and all 12 IPS elements in reliability-and-sustainment.
- **The IL2/4/5/6 table** against the DoD Cloud Computing SRG, and the seven DoD zero trust pillar names.
- **TRL 1-9, MRL 1-10 and IRL 1-9** definitions in trl-assessment.
- **Data rights categories and triggers** per DFARS 252.227-7013/7014, distribution statements A-F, ITAR/EAR splits, CUI marking rules.
- **Every statistics formula and the full worked example** in applied-statistics, recomputed by hand. Same for agentic-system-design's 0.95^20 ≈ 36% compounding claim and the arithmetic in business-case, business-unit-finance, lessons-learned and technical-pilot.
- **APA 7 rules** in apa-7, including the et-al-from-first-citation and 20-author rules. The apa-7 skill had zero findings.
- **SF 298 block facts** in dod-technical-report and the patent-law content in invention-disclosure (grace period, absolute novelty abroad, Bayh-Dole shape) came through clean.
- **The architecture-diagrams pipeline runs**: CLI matches SKILL.md, the claimed 36 styles are really 36, validation behavior matches the docs, and the multi-style gallery builds.
- **which-skill's inventory**: all ~100 referenced skill names exist and every spot-checked route description was honest.

One judgment call was left unreported: human-systems-integration lists 8 HSI domains where DoDI 5000.95 has 7, but the skill explicitly says the list varies by service and framework and claims no count, so it was not treated as a defect.

## Fixes applied

All 16 confirmed errors are fixed on this branch, with the corrections validated before committing:

- The rewritten ai-cost-modeling caching term applies multiplicatively to the cacheable input slice only.
- Functional baseline moved to SFR in technical-reviews (gates table and gate-criteria exit rows) and configuration-management (baseline table and record) together, keeping the two skills consistent.
- rmf-ato now runs seven steps with Prepare first.
- DIL keeps its three-term expansion (disconnected, intermittent, limited-bandwidth), matching the README's "DIL operation".
- The acm-paper table marks `sigchi` retired, nasa-sti routes data compilations to TP, chicago-turabian states the CMOS 18 rule with the 17th/Turabian 9 variant noted, latex-authoring splits the two float errors into separate rows, and the ruggedization altitude row now matches swap-and-thermal-budgeting.
- diagram-picker states the explicit style-key mapping, and every which-skill "Look under" label now matches a real README section heading (checked programmatically against the skill links in each section).
- architecture-diagrams: `glyphs.py` gained the six missing AWS aliases and a real generic fallback, SKILL.md documents the cairosvg dependency, the example spec's Application Tier is reordered, and the Azure2 guidance now describes image styles. The full pipeline was re-run on the fixed example and the PNG inspected: every node has a glyph and no edge passes under a node.

The low-severity list is mostly single-line edits, left for a later pass since those findings were not independently re-verified.
