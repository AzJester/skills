---
name: manuscript-submission
description: Get a paper through peer review. Use when choosing a venue, preparing a submission, writing a cover letter, responding to reviewers, handling a rejection, deciding whether to appeal, or reviewing someone else's manuscript. Covers the review cycle; formatting is handled by ieee-paper and the other format skills.
---

# Manuscript submission

Formatting a paper is solved. Getting it through review is a different problem, and it is mostly about understanding that the people deciding are three busy volunteers and an overloaded editor.

## Step 1: Choose the venue before finishing the paper

Venue determines length, structure, expected contribution, and audience. Writing first and choosing after produces a paper reshaped badly to fit somewhere.

Judge on:

- **Scope match.** Read the aims and a recent issue. The most common desk rejection is a paper that is fine and belongs somewhere else.
- **Contribution type.** Venues differ in whether they want theory, method, system, or evaluation. A strong systems paper submitted where theory is expected loses on novelty grounds that are really fit grounds.
- **Audience.** Who do you need to read this? Citation counts matter less than reaching the people whose work it should change.
- **Timeline.** Conference deadlines are fixed and review is fast; journal review is slower and iterative. If the work must be public by a date, that constrains the choice.
- **Legitimacy.** Predatory venues solicit aggressively, promise fast review, and charge fees. Check whether the editorial board is real and whether anyone you respect publishes there.

For DoD-related work, add: is publication permitted, and has the release review been done? See `export-control-and-markings`. That review precedes submission, not publication — submitting is a disclosure.

## Step 2: Prepare the submission

- **The abstract does most of the work.** Editors decide whether to desk-reject from it, and reviewers form their expectation from it. State what was done and what was found, not what the paper will discuss.
- **Make the contribution explicit.** Reviewers look for it, and a paper that leaves them to infer it gets a weaker read. Say plainly what is new.
- **Position against related work honestly.** The reviewer is likely an author of some of it. Overstating your novelty relative to work they know is the fastest route to a hostile review.
- **State limitations yourself.** A limitations section pre-empts the reviewer's strongest objection and reads as competence. Omitting it does not hide the limitation; it just lets a reviewer discover it.
- **Cover letter** — short. What the paper contributes, why it fits this venue, and any procedural matters: conflicts, related submissions, prior conference version being extended.
- **Anonymise properly** where review is blind. Author names, acknowledgements, self-citations phrased in first person, identifying repository URLs, and document metadata.

## Step 3: Read the decision properly

Decisions are typically: accept (rare on first submission), minor revision, major revision, reject-and-resubmit, or reject.

**Major revision is good news.** It means the editor believes the paper can work. Treat it as an invitation, not a criticism.

Read the reviews, then wait a day before responding to anything. The first reaction to a review that misunderstands your work is not the reaction to act on.

Then read again for what is actually being said. **When a reviewer misunderstands something, that is usually a writing problem rather than a reading problem.** Two reviewers misunderstanding the same passage is definitive.

## Step 4: Respond to reviewers

The response document is a genuine skill and is frequently done badly.

**Structure:** a short summary of the changes, then every comment quoted verbatim with your response beneath it, in order. Number them. Point to where in the revised manuscript the change appears — section and page.

**Tone:** courteous throughout, including with the reviewer who plainly did not read carefully. The editor reads your responses, and how you handle a poor review is visible.

**For each comment, one of three:**

1. **Agreed and changed** — say what you changed and where. Most comments get this.
2. **Agreed and changed differently** — explain why your approach addresses the concern. Reviewers usually accept a different solution to a problem they correctly identified.
3. **Respectfully disagree** — with a reason and evidence. Legitimate, and it must be rare. A response disagreeing with most comments will be rejected regardless of who is right.

**Never ignore a comment.** An unanswered comment reads as evasion and the editor will notice.

Where a reviewer asks for something out of scope — a whole additional study — say what it would require, explain why it is a separate contribution, and where possible add a smaller version that addresses the underlying concern.

## Step 5: Rejection

Most papers are rejected somewhere. It is a normal part of the process, not a verdict on the work.

- **Mine the reviews.** Even a hostile review usually contains a real objection worth fixing before the next submission.
- **Revise before resubmitting elsewhere.** Submitting the same paper unchanged to a second venue frequently reaches the same reviewers, who remember.
- **Appeal rarely.** Only for a factual error in the review that changes the decision, never for disagreement about significance. Appeals succeed occasionally and cost editorial goodwill either way.
- **Down-shift deliberately, not reflexively.** A paper rejected from a top venue may belong at a good one, or may need another year of work. The reviews usually tell you which.

## Reviewing others' work

You will be asked, and reviewing well improves your own writing more than most things.

- **Decline promptly** if you lack expertise or time. A late review holds up someone's career.
- **Declare conflicts.**
- **Review the paper submitted**, not the one you would have written.
- **Be specific.** "The evaluation is weak" helps nobody. "The evaluation uses a single dataset from the same distribution as training, so the generalisation claim in Section 5 is not supported" does.
- **Separate must-fix from would-improve.** Editors need to know which objections are load-bearing.
- **Be courteous.** There is a person on the other end, often an early-career one, and anonymity is not licence.
- **Check the statistics.** `applied-statistics` covers the questions that find most problems — sample size justification, multiple comparisons, effect sizes with intervals.

## Where this connects

`ieee-paper` and the other format skills handle the manuscript itself. `applied-statistics` for the analysis and for reviewing others'. `export-control-and-markings` for release review before submission. `storm-research` on your account for the literature work that precedes writing.
