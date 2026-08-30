# IEEE reference style

Based on the IEEE Reference Guide. Rules marked (checked) are enforced by `validate_ieee.py`.

## Contents
- General rules
- In-text citation
- Entry formats by source type
- BibTeX practice
- Common defects

## General rules

- References are numbered **by order of first citation**, never alphabetically. Use `\bibliographystyle{IEEEtran}`. Styles like `plain`, `alpha`, and `apalike` alphabetize and are wrong. (checked)
- Reference numbers sit on the line in square brackets, not superscript, not parentheses.
- Given names are abbreviated to initials, which precede the surname: `J. K. Author`.
- List **all authors up to six**. With seven or more, give the primary author followed by `et al.` For non-IEEE publications, `et al.` is acceptable when names are not provided. (checked)
- Include a **DOI for every reference that has one**. (checked as advisory)
- Every entry ends with a **period**, including entries with a DOI. The exception is an entry ending with a URL, which takes no terminal period. When an entry has both a DOI and a URL, the DOI goes after the URL and the entry ends with a period. (checked)
- Page ranges use an **en dash**: `pp. 123–145`, written `123--145` in BibTeX. (checked)
- Journal and conference titles are abbreviated using IEEE's standard abbreviations. Book and journal titles are italicized. Article titles go in quotation marks with sentence-style capitalization.
- Where an issue lists two months, join them with a slash: `Jul./Aug.`
- Commas surround `Jr.`, `Sr.`, and `III`.

## In-text citation

```latex
Recent work improves throughput \cite{smith2024}.        % [1]
Several studies address this \cite{a,b,c}.               % [1], [3], [7] or [1]-[3] with the cite package
As shown in \cite[p.~23]{smith2024}.                     % [1, p. 23]
```

- The bracket goes **before** the sentence punctuation: `improves throughput [1].`
- Multiple sources each get their own bracket, comma separated: `[1], [3], [7]`. Consecutive runs collapse with an en dash: `[4]–[6]`.
- Do not write "in reference [3]" or "in [3] the authors show". Write "in [3]" or name the authors: "Smith et al. [3] show".
- A reference number is not a noun. "As described in [5]" is right; "[5] describes" is discouraged in formal IEEE prose, though it appears in practice.

Load the `cite` package so runs compress and sort automatically.

## Entry formats by source type

**Journal article**
> J. K. Author, "Title of paper," *Abbrev. Journal Title*, vol. 12, no. 3, pp. 123–145, Mar. 2024, doi: 10.1109/XXXX.2024.0000000.

**Conference paper (published proceedings)**
> J. K. Author, "Title of paper," in *Proc. Abbrev. Conf. Name*, City, State, Country, 2024, pp. 233–238, doi: 10.1109/XXXX.2024.0000000.

**Conference paper (presented, not published)**
> J. K. Author, "Title of paper," presented at the *Abbrev. Conf. Name*, City, State, Country, Mar. 3–5, 2024.

**Book**
> J. K. Author, *Title of Book*, 3rd ed. City, State, Country: Publisher, 2020.

**Chapter in a book**
> J. K. Author, "Title of chapter," in *Title of Book*, 2nd ed., E. Editor, Ed. City, State, Country: Publisher, 2019, ch. 4, pp. 55–70.

**Technical report**
> J. K. Author, "Title of report," Abbrev. Dept., Abbrev. Univ. or Org., City, State, Country, Rep. 85, Aug. 2023.

**Thesis or dissertation**
> J. O. Williams, "Narrow-band analyzer," Ph.D. dissertation, Dept. Elect. Eng., Harvard Univ., Cambridge, MA, USA, 1993.

**Standard**
> *Title of Standard*, IEEE Standard 802.11-2020, 2020.

**Patent**
> J. K. Author, "Title of patent," U.S. Patent 5 555 555, Sep. 10, 1996.

**Online source**
> Organization. "Title of page." Site Name. URL (accessed Mar. 3, 2026).

**Dataset**
> J. K. Author, "Title of dataset," Repository Name, 2024. [Online]. Available: URL

**Preprint**
> J. K. Author, "Title of paper," 2024, *arXiv:2401.00000*.

Preprints are cited as preprints. When a preprint has since been published, cite the published version instead: reviewers check this.

**Government or defense document**
> Department of Defense, "Title of document," Washington, DC, USA, DoDI 5000.02, Jan. 23, 2020.

Do not cite controlled, classified, or distribution-limited documents in a public paper. Flag this to the user rather than deciding it, since the distribution statement governs whether it can be referenced at all.

## BibTeX practice

```bibtex
@article{turner2026,
  author  = {S. Turner and A. B. Coauthor},
  title   = {Adaptive threat classification for airborne electronic warfare},
  journal = {IEEE Trans. Aerosp. Electron. Syst.},
  volume  = {62},
  number  = {2},
  pages   = {1123--1135},
  month   = apr,
  year    = {2026},
  doi     = {10.1109/TAES.2026.0000000}
}
```

- Use `--` for page ranges. (checked)
- Protect capitalization that must survive with braces: `{MIMO}`, `{IEEE}`, `{L}-band`.
- Use `month = apr` (the BibTeX macro), not `month = {April}`.
- Journal titles go in abbreviated form in the `journal` field. IEEEtran does not abbreviate for you.
- One `.bib` file per paper. Shared library files accumulate entries the paper does not cite, and a stale entry that slips into the reference list is a credibility problem.

Run `bibtex` between LaTeX passes or `build.sh` handles it.

## Common defects

| Defect | Why it happens |
|---|---|
| Alphabetized reference list | Wrong `\bibliographystyle` (checked) |
| Hyphen instead of en dash in page ranges | Copy-paste from a publisher page (checked) |
| Seven or more authors listed in full | Reference manager export (checked) |
| Missing DOI | Manual entry (checked) |
| Full given names | Reference manager set to a non-IEEE style |
| Unabbreviated journal titles | Same |
| Reference numbers out of sequence | Citations added during revision without rebuilding |
| A cited preprint that has since been published | Stale library entry |
| Reference to a retracted paper | Nobody checked |

When importing from a reference manager, set the export style to IEEE and then still verify. Exports get author counts, page dashes, and journal abbreviations wrong routinely.
