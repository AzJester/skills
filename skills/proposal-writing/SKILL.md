---
name: proposal-writing
description: Write the proposal itself. Use when responding to an RFP or RFQ, building a compliance matrix from Section L and Section M, writing or reviewing a technical volume, storyboarding sections before drafting, writing theme statements and action captions, preparing for or running a pink, red or gold team review, or working out why a proposal that read well scored badly. Sits after solution-shaping decided what to offer and consumes engineering-to-proposal evidence.
---

# Proposal writing

Two skills in this repository stop at the edge of this one. `solution-shaping` decides what to offer and says it "sits before proposal writing, not inside it." `engineering-to-proposal` harvests evidence and says it "does not write the proposal." This is the middle.

The failure this exists to prevent is a proposal written as an essay about how good the company is. Evaluators do not read essays. They score a document against Section M, section by section, looking for specific findings, and they cannot award credit for anything they cannot locate.

## The one rule everything else follows from

**Section M is the scoring rubric. Section L is the format the rubric expects.** An evaluator scores what Section M lists, using the structure Section L requires, and nothing else.

That produces two hard consequences most losing proposals violate:

1. **Anything Section M does not evaluate earns zero.** However true it is. Company history, unrequested detail, a technology you are proud of — if no evaluation factor covers it, it is page count spent for nothing.
2. **Anything Section M evaluates that an evaluator cannot find is scored as absent.** Not inferred. Not given benefit of the doubt. Content buried under a heading that does not match Section L's structure frequently scores as missing.

Before writing a sentence, read Section M, then Section L, then Section C. In that order. Reading Section C first is how a team writes a technically excellent volume against the wrong rubric.

## Step 1: Build the compliance matrix before anything else

The matrix is the spine of the whole response. One row per requirement, sourced from Section L and Section M and cross-walked to Section C.

| Column | Holds |
| --- | --- |
| Source | Exact citation — `L.3.2.1`, `M.2 Factor 2` |
| Requirement | The verbatim text, not a paraphrase |
| Where addressed | Volume, section, page — filled in as writing proceeds |
| Owner | One named person |
| Status | Not started / drafted / reviewed / complete |

Two disciplines make it real:

**Verbatim, then shred.** Copy the requirement exactly, then split any sentence carrying more than one obligation into separate rows. A single Section L sentence routinely contains three requirements, and compliance is judged on all three.

**The cross-walk is where the finding lives.** Section L tells you where to put content; Section M tells you what it is worth. Where an item appears in L but not M, it is mandatory and unscored — comply briefly and move on. Where it appears in M but not L, decide deliberately where it goes, because the RFP did not tell you and the evaluator still has to find it.

**When L and M contradict each other**, which is common, do not choose silently. Submit a written question during the Q&A window. If the window has closed, comply with both — structure to Section L, and add a cross-reference table pointing the Section M evaluator to where each factor is addressed.

## Step 2: Outline and storyboard before prose

Nobody writes a good proposal by starting at the first sentence. Build the structure, get it reviewed, then fill it.

**Annotated outline.** Every heading from Section L in order, each carrying: the Section M factor it serves, the page allocation, the theme, the proof points to be used, and the graphic planned. Reviewable in an hour. A structural problem found here costs an hour; found at red team it costs a weekend.

**Page allocation is proportional to evaluation weight, not to enthusiasm.** If management approach is 30% of the score, it gets roughly 30% of the pages. Teams routinely spend half the technical volume on the part they find most interesting, which is not usually the part being weighted most heavily.

**Storyboard each section** on one page before drafting: the theme statement, three or four proof points, the graphic and its action caption, and the specific Section M language the section must satisfy. Then draft against it.

## Step 3: Write sections that score

Every substantive section runs the same shape:

**Theme statement first.** One or two sentences at the top naming the benefit to *this* customer and the discriminator delivering it. Not a summary of what follows.

**Then the proof.** Specific, checkable, attributable. `engineering-to-proposal` exists to supply it: nouns and numbers from a real engineering record rather than adjectives from memory.

**Then the "so what".** State the consequence for the customer's mission. A feature with no stated consequence makes the evaluator do the work of connecting it to the evaluation factor, and evaluators under time pressure do not do that work.

Three habits that decide the score more than prose quality:

**Mirror the RFP's language.** If Section M says "surge capacity", write "surge capacity", not "elastic scaling". The evaluator is searching for their words. Reaching for a synonym to avoid repetition is a writing-class instinct that costs points here.

**Answer "how", not "that".** "We will provide a cleared team" is a promise. "Fourteen of the eighteen positions are filled today by cleared staff on the incumbent contract; the remaining four are in adjudication with an average of 31 days remaining" is evidence. Evaluators distinguish the two reliably.

**Graphics carry argument, with action captions.** A caption that reads "Figure 3-2. System Architecture" wastes the highest-attention element on the page. `Figure 3-2. Three independent transport paths keep the mission running through a 72-hour SATCOM outage.` states the claim; the figure proves it. Many evaluators read the headings, the graphics, and the captions before anything else — write those three assuming they are all that is read.

## Step 4: Review in colors, and know what each one checks

Each review answers a different question. Running them out of order, or collapsing them, is how a proposal reaches submission with a structural defect nobody was assigned to catch.

| Review | Timing | The one question it answers |
| --- | --- | --- |
| Blue | Outline stage | Is the structure compliant and is the strategy right? |
| Pink | ~50–60% draft | Is the approach and the story right, at the section level? |
| Red | ~90% draft | Would an evaluator score this well, reading it cold? |
| Gold | Near final | Is it consistent, is the executive story clean, is it approved to submit? |
| White glove | Production | Is it complete, formatted to Section L, and submittable? |

**Red team must be scored, not discussed.** Hand reviewers the actual Section M factors and have them assign findings — strengths, weaknesses, deficiencies — as an evaluator would. A red team that produces general commentary rather than scores has told you nothing about how the proposal will fare.

**Recovery time is the constraint.** A red team two days before submission is theater; nothing structural can be fixed. Schedule it where the findings can still be acted on, and protect that gap when the schedule slips.

## Step 5: The pre-submission pass

- Every compliance-matrix row shows a real volume, section and page.
- Page limits, font, margins and file format match Section L exactly — a non-compliant submission can be rejected without evaluation.
- Every cross-reference points where it claims to.
- Every acronym is expanded at first use in each volume, since volumes are often read by different people.
- Nothing claims capability the evidence does not support. Where a claim has no artifact behind it, a human decides knowingly whether to make it anyway — see `engineering-to-proposal`.
- Markings and export control reviewed — see `export-control-and-markings`.
- Submission mechanics rehearsed before the deadline, not at it. Portal upload failures are a routine cause of non-submission and they always happen in the last hour.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Writing before the matrix | Content that answers no requirement | Matrix first, always |
| Optimizing for reading, not scoring | Elegant prose, mediocre score | Write to Section M's words and structure |
| Adjectives instead of evidence | Robust, proven, world-class | Nouns and numbers from `engineering-to-proposal` |
| Unweighted page allocation | Half the volume on 15% of the score | Pages follow evaluation weight |
| Decorative captions | "Figure 4-1. Network Diagram" | Action captions that state the claim |
| Late red team | Findings nobody can act on | Schedule for recovery time, protect it |
| Ignoring an L/M contradiction | A guess, silently made | Ask in Q&A; if closed, comply with both |

The honest one is the first. A proposal is not a document that describes a solution. It is a document that makes a specific score easy for a tired evaluator to award, and it should be built backwards from that.

## Reference

- `references/compliance-and-evaluation.md` — evaluator vocabulary, evaluation approaches, and past-performance mechanics.
