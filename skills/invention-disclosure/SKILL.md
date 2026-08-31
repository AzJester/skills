---
name: invention-disclosure
description: Write an invention disclosure and protect a technical idea before publishing it. Use when documenting an invention for patent counsel, deciding whether to patent or keep something as a trade secret, working out whether a paper, proposal or demonstration will forfeit patent rights, identifying inventorship correctly, or handling subject-invention reporting on a government contract. A guardrail with a bias toward talking to counsel before disclosing, not legal advice.
---

# Invention disclosure

Two things make this urgent rather than administrative in a contractor setting: **the timing traps are irreversible**, and **government contracts create reporting obligations with deadlines** that run whether or not anyone is paying attention.

**This is not legal advice.** Patent law is jurisdictional, fact-specific and unforgiving of near-misses, and the consequences of getting it wrong cannot be undone later. Everything here is about getting the engineering record right and knowing when to stop and involve patent counsel — which is earlier than most engineers assume.

## The timing trap, first, because it is the one that costs the most

**Public disclosure before filing can forfeit patent rights permanently.**

- In the United States, an inventor's own public disclosure starts a **one-year grace period** to file. Miss it and the invention is unpatentable.
- **Most other jurisdictions have absolute novelty.** Any enabling public disclosure before filing forfeits foreign rights immediately, with no grace period. A conference paper published on Monday can end European and most Asian patent rights on Monday.

What counts as a public disclosure is broader than people expect and includes, depending on the facts: a published paper, a conference talk, a poster, a public demonstration, a non-confidential proposal or white paper, a data sheet, a public repository, and a sale or offer for sale.

**The practical rule: talk to counsel before it goes out, not after.** This applies to the whole publishing side of this repository — `ieee-publishing`, `acm-paper`, `dod-technical-report`, `nasa-sti`, `manuscript-submission`, `white-paper-and-baa` — and to demonstrations and proposal submissions. A provisional application filed the week before submission is routine and cheap relative to what it protects; the reverse order cannot be repaired.

**Additional constraints in a defense context**, both of which require counsel:

- Filing abroad is restricted; a foreign filing license is generally required before filing outside the United States, and it is normally granted with the US filing receipt.
- An invention with national-security implications can be placed under a **secrecy order**, which bars publication and foreign filing. Where the subject matter is export-controlled, `export-control-and-markings` applies to the disclosure itself — including sending a description to foreign patent counsel.

## Step 1: Write the disclosure while it is fresh

The invention disclosure record is the input to a patentability decision and, later, evidence. Write it when the idea works, not when someone remembers to.

| Section | Contains | Why it matters |
| --- | --- | --- |
| Title and inventors | Everyone who contributed to conception, with what each contributed | Inventorship is a legal determination and getting it wrong can invalidate a patent |
| Problem | The technical problem, and why existing approaches fall short | Frames non-obviousness |
| The invention | What it is, in enough detail that a skilled practitioner could build it | Enablement is a filing requirement, not a nicety |
| What is new | The specific difference from what already exists | This is the whole question |
| Prior art known | Papers, products, patents, your own prior work | Known art is disclosed; concealing it can be fatal to the patent |
| Variations | Other ways to achieve the same effect | Drives claim breadth; the version you built is rarely the broadest |
| Dates | Conception, first working implementation, any testing | Establishes the record |
| Disclosures | Anything already published, presented, demonstrated, sold or offered — with dates | Determines whether a bar has already run |
| Funding | Contract or program that funded the work | Determines government rights and reporting obligations |
| Commercial use | Where it would be used, by whom | Decides whether it is worth filing |

**Be specific about the difference.** "Uses machine learning for signal classification" describes a field, not an invention. What is patentable is usually narrower and more particular than the inventor thinks — the specific mechanism, structure or sequence that makes it work.

**Include what failed.** Approaches tried and abandoned support non-obviousness and are almost never recorded.

**Describe the variations.** Counsel drafts claims around the concept, not the prototype. An inventor who describes only what was built gets a narrow patent that a competitor designs around.

## Step 2: Get inventorship right

Inventorship is not authorship and not seniority. It turns on **contribution to the conception** of at least one claimed invention.

- A manager who funded, directed or approved the work is not an inventor on that basis.
- A technician who built exactly what was specified is not an inventor on that basis.
- Someone who contributed a conceptual element that ends up in a claim **is** an inventor, regardless of title or hours.
- Inventorship can change as claims change during prosecution — it is counsel's determination, made against the claims, not a courtesy list agreed at disclosure time.

Getting it wrong is not a formality problem. Incorrect inventorship, particularly if deliberate, can render a patent unenforceable. Record contributions factually in the disclosure and let counsel decide.

## Step 3: Decide whether to patent at all

Not everything worth inventing is worth patenting.

| Route | Gives | Costs | Fits when |
| --- | --- | --- | --- |
| **Patent** | Time-limited exclusivity; a licensable, valuable asset | Filing and prosecution cost, and **publication** — the application generally publishes at 18 months | Infringement would be detectable, and the advantage outlasts the filing timeline |
| **Trade secret** | Protection with no disclosure and no expiry | No protection against independent development or lawful reverse engineering; requires real secrecy measures | The advantage is not visible in the product and can genuinely be kept |
| **Defensive publication** | Prevents others patenting it | No exclusivity | You want freedom to operate more than exclusivity |
| **Do nothing** | Nothing | Nothing | It is neither detectable nor durable |

Three questions decide it more reliably than enthusiasm:

- **Could you tell if someone else used it?** A patent on something undetectable in a competitor's product is difficult to enforce and may be worth less than keeping it quiet.
- **Will it still matter in three to five years?** That is the realistic horizon for prosecution and value. Fast-moving software methods often age out of usefulness before a patent issues.
- **Who owns it?** Employment agreements, contract clauses and any research partner's agreement all bear on this — and on a government contract, so do the patent rights clauses.

## Step 4: Government-funded inventions have reporting obligations

Where work is performed under a federal contract, an invention conceived or first actually reduced to practice in performing it may be a **subject invention**, and the contract's patent rights clause governs. The exact clause and its deadlines depend on the contract — read the clause, do not assume.

The common shape, under the Bayh-Dole framework and its FAR and DFARS implementations:

- **The contractor may generally elect to retain title**, subject to conditions.
- **Disclosure to the government is required within a set period** after the invention is reported to the people in the company responsible for patent matters, followed by a deadline to elect title and then a deadline to file.
- **The government retains a nonexclusive, irrevocable, paid-up license** to practice the invention worldwide on its behalf.
- **March-in rights** exist in defined circumstances.
- Reporting typically runs through the government's invention reporting system, and a final invention statement is normally required at contract close-out.

Two failure modes worth naming:

**The clock starts internally.** It runs from when the inventor tells the company, not from when someone gets round to filing. An invention sitting in an engineer's notebook because they were not sure it was worth disclosing is a compliance exposure as well as a lost asset.

**Missing the deadline can cost title.** Failure to disclose or elect within the required period can put the invention at risk of the government taking title. This is administrative, entirely avoidable, and it happens.

**Funding source belongs in the disclosure**, on the first pass, including where work spans several contracts or mixes contract and internal funding. Which contract funded which contribution is materially harder to reconstruct a year later, and it decides who owns what.

## Common failures

| Failure | Symptom | Fix |
| --- | --- | --- |
| Publishing first | Foreign rights gone; US clock running | Counsel before submission, demo or proposal |
| Disclosure written late | Dates and contributions reconstructed | Write it when it works |
| Only the built version described | Narrow patent, easily designed around | Describe the variations |
| Courtesy inventorship | Patent enforceability at risk | Record contributions; counsel decides |
| Funding source omitted | Ownership and reporting unclear | Record the contract on the first pass |
| Reporting clock ignored | Title at risk on a subject invention | Route disclosures to patent staff immediately |
| Patenting reflexively | Cost and publication for no advantage | Detectable? Durable? Owned? |

The honest one is the first, and it is the reason this skill exists next to the publishing skills rather than apart from them. Publication and patenting compete for the same moment, and only one order of operations preserves both options.
