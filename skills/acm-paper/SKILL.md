---
name: acm-paper
description: Format a paper for an ACM venue. Use when submitting to an ACM conference or journal, applying the acmart template, choosing between its formats, handling CCS concepts and ACM Reference Format, or converting a manuscript into ACM style. Distinct from IEEE despite the superficial similarity, and the differences matter at submission.
---

# ACM paper

ACM and IEEE papers look alike at a glance and are not interchangeable. The template, the citation format, the metadata requirements and the submission mechanics all differ, and a paper prepared for one and submitted to the other will be returned.

## The template

ACM publishes a single LaTeX class, **acmart**, with format options rather than separate templates. A Word template exists; the LaTeX path is better supported.

Common formats:

| Format | Used for |
| --- | --- |
| `sigconf` | Most conference proceedings — two column |
| `acmsmall` | Most journals — single column |
| `acmlarge`, `acmtog` | Certain journals with their own trim |
| `manuscript` | Single column, for review or preprints |
| `sigplan`, `sigchi` | SIG-specific variants where a community requires one |

**The venue tells you which.** Do not choose by preference — the call for papers or the journal's instructions specify it, and it affects length limits, which are counted in that format's pages.

**Use the template as distributed.** Redefining margins, spacing, or fonts to fit more in is detectable and is a standard reason for rejection at the formatting check. If the paper does not fit, cut it.

Two document-class options that catch people: `review` adds line numbers for reviewers, and `anonymous` handles blind submission. Set them for review and remove them for camera-ready — a camera-ready paper still carrying line numbers signals it was submitted without a final pass.

## Required metadata

ACM requires structured metadata that IEEE does not. Missing it blocks camera-ready acceptance.

**CCS concepts.** ACM's Computing Classification System. Generate them from ACM's CCS tool, which produces the LaTeX to paste. They appear after the abstract and are how the paper is classified in the Digital Library. Choose specifically — broad concepts make the paper less findable, not more.

**Keywords.** Author-chosen, alongside CCS concepts rather than instead of them.

**Rights and conference commands.** The publication workflow issues a rights form whose output includes the exact LaTeX commands for copyright, DOI, ISBN, conference name and dates. Paste them in verbatim. Guessing or reusing them from a previous paper produces the wrong copyright block, which is a rejection at the publishing stage.

## Structure

Title, authors with affiliations, abstract, CCS concepts, keywords, then the body, references, and appendices.

The body arc is conventional for computing venues: introduction, related work, approach, evaluation, discussion, conclusion. Related work placement varies by community — early in most systems venues, sometimes late in theory venues.

**Authors and affiliations** use structured commands in acmart rather than free text. Each author gets institution, city and country as separate fields. This is metadata for the Digital Library, not just layout, so filling it as a single string breaks the record.

## ACM Reference Format

The citation style. Numbered, bracketed, and — the difference that matters — **the reference list is ordered alphabetically by author, not by order of appearance.**

That single fact separates it from IEEE. A paper with references numbered in citation order has IEEE's system with ACM's brackets, and it will be flagged.

Use BibTeX with the ACM style; hand-formatting ACM references is error-prone and unnecessary. The `\citestyle` command selects between numeric and author-year for venues that use the latter.

Practical points:

- Include DOIs. ACM's format expects them and the Digital Library links on them.
- Full author lists rather than `et al.` in the reference list.
- Conference names as ACM formats them, which BibTeX with the ACM style handles.

## Length and submission

- Length limits are in the specified format's pages, and whether references count varies by venue. Read the call.
- Many ACM venues require submission through a system that runs an automated format check before a human sees the paper. Run any provided validation tool early.
- Supplementary material and artifacts are handled separately; many venues run artifact evaluation with its own deadline and its own badging.
- **Accessibility** is increasingly required: alt text on figures, tagged PDF, readable structure. ACM has been raising expectations here, and it is worth doing rather than deferring.

## Against IEEE

| | ACM | IEEE |
| --- | --- | --- |
| Template | One class, `acmart`, with format options | Separate conference and journal templates |
| Reference order | **Alphabetical** | **Order of first appearance** |
| Classification | CCS concepts required | Index terms |
| Rights block | Generated by the rights workflow, pasted in | Set by the template |
| Citation in text | `[1]` | `[1]` |

The reference ordering is the one that produces real rework if discovered late. Converting a paper between the two is not a formatting pass.

## Reference

Use the current acmart documentation and the venue's call for papers. Both override anything here, and acmart's own documentation is unusually good.
