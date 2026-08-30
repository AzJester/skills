---
name: technical-editing
description: Edit someone else's technical writing. Use when reviewing a colleague's document, editing a report, paper, proposal section or specification for clarity and correctness, deciding how heavily to intervene, writing review comments that get accepted, applying plain-language principles, or rewriting engineering prose for a non-technical reader. Covers editing existing text rather than drafting it, and the judgement about how much to change.
---

# Technical editing

Editing is not proofreading with opinions. It is a set of distinct interventions at different depths, and the most common failure is doing them in the wrong order — copyediting a document whose structure is about to change discards the work and annoys the author.

The second most common failure is rewriting someone's document into your own voice, which produces a better sentence and a worse working relationship, and teaches the author nothing.

## Step 1: Decide the level of edit, and say so

Editing has levels. Naming which one you are doing, before starting, is what separates a review from a rewrite. The framework below descends from the classic JPL *Levels of Edit*; the useful part is that the levels are cumulative and ordered.

| Level | Question | Touches |
| --- | --- | --- |
| **Substantive** | Is the argument right, complete, and in the right order? | Structure, logic, what is missing, what does not belong |
| **Line** | Does each paragraph and sentence do its job? | Flow, emphasis, wordiness, transitions, ambiguity |
| **Copy** | Is it correct and consistent? | Grammar, terminology, units, numbering, references, style |
| **Proofread** | Is it clean as produced? | Typos, formatting, figure and table numbering, cross-references |

**Do them in that order and never invert it.** Copyediting before the structure is settled wastes both people's time — every sentence you polished may be cut. If the document needs substantive work, say so and stop; do not deliver a copyedit of a document that needs restructuring, because the polish will be read as approval of the structure.

**Agree the level with the author first.** "Do you want a structural read or a clean-up pass?" takes ten seconds and prevents the two worst outcomes: a heavy rewrite the author did not want, and a light pass on a document that needed rescuing.

## Step 2: The substantive pass

Read it once through without touching anything. Editing while first reading produces line comments on paragraphs that should be deleted.

Then ask, in order:

- **What is the document for, and who reads it?** An unstated audience is the root cause of most structural problems.
- **Does the opening state the point?** Technical writers routinely bury the conclusion in a final paragraph after the reasoning. For most technical documents the conclusion belongs first — see `executive-decision-memo` and `briefing-deck` for the strong forms of this.
- **Is the order the reader's order or the author's?** Chronological narration of how the work was done is the author's order. What the reader needs first is usually what was found.
- **What is missing?** Assumptions, limitations, the alternative not taken, the number behind the claim.
- **What does not belong?** Content that serves the author's sense of completeness rather than the reader's question.
- **Does every claim have support, and is the support where the claim is?** Evidence three sections away from the assertion it supports is functionally absent.

## Step 3: The line pass

Where technical prose actually goes wrong, in rough order of frequency:

**Nominalisation.** Verbs turned into nouns: "perform an analysis of" → "analyse", "make a determination" → "decide". This single fix removes more words than any other.

**Buried agency.** "It was determined that the interface would be modified" hides who decided and who acts. Passive voice is not banned — it is right when the actor is unknown, irrelevant, or when the object is genuinely the topic — but unintentional passive is how accountability disappears from an engineering document.

**Sentences carrying more than one idea.** Especially in requirements and procedures, where a compound sentence becomes two obligations, one of which gets missed.

**Ambiguous reference.** "This causes the system to fail" — *this* what? Pronouns pointing at whole preceding paragraphs are a leading cause of misread specifications.

**Undefined precision.** "Significantly faster", "minimal impact", "as required". Either it has a number or it is an opinion; both are fine, but they should be distinguishable.

**Acronym density.** Expand at first use in each document, and reconsider any acronym used fewer than three times. A paragraph a reader has to decode is a paragraph they skim.

## Step 4: Plain language, when the reader is not an engineer

Federal writing is subject to plain-language expectations, and defense work routinely puts engineering prose in front of contracting officers, programme staff and general officers who will not decode it.

Plain language is **not** simplification of the content. It is removal of the barrier between the reader and the content:

- **Short sentences carrying one idea.** Long sentences are not the problem; long sentences with three subordinate clauses are.
- **Concrete subjects doing things.** "The team tested" beats "testing was conducted".
- **The reader's vocabulary.** Domain terms where they carry real meaning, defined once. Jargon where a plain word exists is a cost with no return.
- **Structure that supports scanning.** Informative headings, short paragraphs, lists for parallel items, tables for anything with two dimensions.
- **State the bottom line first**, then the support. Readers who stop early should still have the answer.

Readability scores are a rough smoke alarm, not a target. A formula counts syllables and sentence length; it cannot see that a short sentence is ambiguous. Use one to find the worst passages, then read them.

## Step 5: Comments that get accepted

An edit only counts if it lands. The mechanics of the comment matter as much as its correctness.

- **Say why, briefly.** "Unclear" gets ignored. "Unclear whether *this* refers to the failure or the workaround" gets fixed.
- **Distinguish must-fix from preference,** explicitly, and keep the must-fix list short. A review where every comment carries the same weight forces the author to triage on your behalf, and they will guess wrong.
- **Query, do not overwrite, on anything substantive.** Suggest a change and ask; reserve direct edits for mechanical corrections. Rewritten paragraphs invite defence of the original rather than consideration of the point.
- **Preserve the author's voice.** Your job is that the document works, not that it sounds like you wrote it. If you cannot articulate why a change improves it beyond preference, drop the change.
- **Comment on patterns once.** Twenty instances of the same nominalisation is one comment with a note that it recurs, not twenty comments.
- **Say what works.** Not for morale — so the author knows what to preserve when they revise.

## Step 6: The consistency sweep

Mechanical, best done last, and best done with a checklist because the eye stops seeing these:

- [ ] Terminology consistent — one term per concept, throughout
- [ ] Acronyms expanded at first use; the list matches the text
- [ ] Units consistent and stated; significant figures not implying false precision
- [ ] Numbers, dates and ranges in one format
- [ ] Figure and table numbering sequential; every one cited in the text
- [ ] Captions follow the format the venue requires — see `ieee-publishing`, `acm-paper`, `apa-7`
- [ ] Cross-references resolve to what they claim
- [ ] References complete and in one style
- [ ] Headings parallel in grammatical form
- [ ] Markings, distribution statement and classification correct — see `export-control-and-markings`

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Wrong level, wrong order | Polished sentences in a section about to be cut | Substantive first; agree the level up front |
| Rewriting into your voice | Author defends the original | Query rather than overwrite |
| Undifferentiated comments | Author cannot tell what matters | Separate must-fix from preference |
| Editing while first reading | Line notes on doomed paragraphs | Read it through once, untouched |
| Formula as target | Chopped sentences, no clearer | Use readability to locate, then read |
| Silent structural approval | Copyedit implies the structure passed | Say when a document needs restructuring |

The honest one is the last. Delivering a clean copyedit on a document with a broken argument is not a neutral act — it tells the author it is ready, and they will send it.

## Reference

- `references/editing-checklists.md` — pass-by-pass checklists and a document-type table.
