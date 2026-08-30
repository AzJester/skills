---
name: briefing-deck
description: Build a briefing that works when presented. Use when preparing a decision brief, information brief or programme review for senior leadership or a government customer, structuring slides around BLUF, deciding what belongs in backup, preparing a read-ahead, cutting a deck to its time limit, or working out why a briefing keeps getting derailed. Distinct from executive-decision-memo, which is the written instrument, and data-storytelling, which covers analytics presentations.
---

# Briefing deck

`executive-decision-memo` covers the case where a deck is the wrong instrument. This covers the case where a briefing is what has been scheduled — which, in defense programmes and executive reviews, is most of the time.

The failure this exists to prevent is a deck built as a document. A deck that is complete enough to read alone is too dense to present, and a deck sparse enough to present cleanly is useless as a leave-behind. Deciding which one you are building, first, resolves most slide-design arguments before they start.

## Step 1: Establish four things before opening any tool

**What kind of briefing this is.** They have different shapes and mixing them is why briefings get derailed.

| Type | Purpose | Ends with |
| --- | --- | --- |
| **Decision** | Get a specific decision made | The decision, or the reason it cannot be made yet |
| **Information** | Establish shared understanding | Questions answered |
| **Progress or review** | Report status against a plan | Agreement on status, and issues raised |
| **Technical interchange** | Work a problem with peers | A shared position, or a named disagreement |

A decision brief that never states the ask becomes an information brief, and the decision does not get made.

**Who is in the room, and who decides.** The decision-maker's questions drive the content. So do the questions of whoever will speak against it — brief to both.

**How long you actually have.** Not the scheduled slot: the realistic time after the meeting starts late and the previous item overruns. Build for two-thirds of the slot. A briefing that cannot reach its recommendation before time runs out has failed regardless of quality.

**Whether it is read ahead or briefed cold.** A read-ahead can carry detail; a cold brief cannot. If a read-ahead was sent, assume some people read it and some did not, and open with a recap short enough not to punish the ones who did.

## Step 2: BLUF, and mean it

**The bottom line goes on the first substantive slide.** The recommendation, the decision requested, or the status — not the agenda, not the background, not the outline.

This inverts how technical people naturally present. Engineering reasoning builds to its conclusion; briefings state the conclusion and then defend it. The reason is structural: senior audiences interrupt. If the point comes last, the interruption arrives before the point does, and the briefing never recovers. If the point comes first, every interruption is about the point.

A decision brief's opening slide holds four things:
- **The ask.** One sentence, specific enough to be approved or refused.
- **Why now.** What forces the timing.
- **The recommendation**, with the alternatives named.
- **What it costs** — money, schedule, people, risk.

Everything after that exists to support those four, and anything that does not support them is backup.

## Step 3: One message per slide, in the title

**The title is the message, written as a full assertion.** "Three transport paths keep the mission running through a 72-hour SATCOM outage" is a title. "Network Architecture" is a label — it tells the reader the topic and nothing about what to conclude.

This is the highest-leverage change available to a technical briefer. Someone who reads only the slide titles, in order, should get the whole argument. That is also exactly what happens when the deck is forwarded to someone who was not in the room.

The rest of the slide proves the title. One idea per slide. If a slide needs two titles, it is two slides — or one slide and one backup.

**The body supports the spoken word rather than replacing it.** Text a briefer reads aloud is text the audience is already reading faster than it is being said, which is why they stop listening. Put the evidence on the slide and the connective reasoning in your mouth.

**Graphics carry the argument.** A system diagram with an action caption does more than three bullets — see `architecture-diagrams` for building them and `data-storytelling` for presenting quantitative results.

## Step 4: Backup is where the deck gets its confidence

Most good briefings are short with substantial backup. This is not a way to evade the page limit — it is how a briefer answers hard questions without cluttering the main path.

- **The main deck carries the argument.** The minimum needed to reach the ask.
- **Backup carries the proof.** Detailed data, methodology, cost build-up, risk register, the alternatives analysis, the assumptions.
- **Know the backup cold and index it.** Being able to turn to a slide that answers a challenge is the single most credibility-building moment available in a briefing.

If a question you expect is answered nowhere in the deck, that is a gap in the analysis, not a gap in the deck. Fix the analysis.

## Step 5: Anticipate the room

Before presenting, write down the five hardest questions and answer them on paper. In a defense or executive setting they are usually predictable:

- What does it cost, in total, including the parts not in this budget line?
- What happens if we do nothing?
- What is the risk, and what happens if the mitigation does not work?
- Who disagrees with this, and why?
- What decision are you actually asking for, and what happens if I say no today?

The last one exposes decision briefs that are really information briefs. If nothing changes when the answer is no, there was no decision to make.

**Name the dissent yourself.** A senior audience usually knows there is disagreement. Presenting a united front that is not real is discovered, and it costs more than the disagreement would have.

## Step 6: Cut it

Almost every deck is too long, and the cut is where quality comes from.

- Everything not supporting the ask goes to backup or out.
- Two slides making the same point become one.
- Any slide the briefer would skip under time pressure is already backup — move it before the meeting, not during.
- Background is the most over-weighted section in technical briefings. The audience usually has more context than the briefer assumes; if they do not, one slide fixes it.

**Rehearse aloud, timed.** Silent reading runs at roughly twice speaking speed, which is why decks that felt right on screen run long in the room. Rehearsal also finds the slides you cannot actually explain.

## Housekeeping that gets noticed when wrong

- **Markings on every slide** where classification or distribution applies, including portion markings where required — see `export-control-and-markings`.
- **Date and version** on the title slide. Decks circulate and get quoted months later.
- **Readable at the back of the room** — assume a projector worse than your monitor and an audience further away than you expect.
- **Numbers with their units and their as-of date**, and a stated source for anything anyone might challenge.
- **Acronyms expanded on first use**, including for the senior attendee who does not work in your programme daily.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Conclusion last | Interrupted before the point lands | BLUF on the first substantive slide |
| Label titles | Forwarded deck communicates nothing | Titles are full assertions |
| Document as deck | Too dense to present, briefer reads aloud | Decide: read-ahead or brief, then build for it |
| No stated ask | Decision brief ends without a decision | One sentence, approvable or refusable |
| Everything in the main deck | Runs out of time before the recommendation | Move proof to backup, know it cold |
| Unrehearsed | Overruns; slides the briefer cannot explain | Rehearse aloud, timed, to two-thirds of the slot |
| Hidden disagreement | Discovered in the room | Name the dissent yourself |

The honest one: the deck is not the briefing. The briefing is what is said, and the deck's job is to make what is said easy to follow and hard to forget.
