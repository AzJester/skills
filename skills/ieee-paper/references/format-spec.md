# Layout and type specification

**These are the conventional values for the IEEE conference template. Verify each against the template downloaded for your venue before relying on it.** IEEE revises templates, journals differ from conferences, and individual venues add constraints. Where this table and the template disagree, the template is right.

The safest workflow is to *write into the template file* rather than to reproduce its formatting in a fresh document. Most formatting errors come from rebuilding the layout by hand.

## Page and columns — conference template

| Property | Conventional value |
| --- | --- |
| Page size | US Letter, 8.5 × 11 in |
| Columns | Two |
| Column width | ~3.5 in (88.9 mm) |
| Gutter between columns | ~0.2 in (5 mm) |
| Body alignment | Justified |

Margins vary between the conference and journal templates and between template revisions — take them from the template rather than from any summary, this one included.

## Type sizes — conference template

| Element | Size | Style |
| --- | --- | --- |
| Title | 24 pt | Centred, title case |
| Author names | 11 pt | Centred |
| Author affiliation | 10 pt | Centred, italic |
| Abstract heading and text | 9 pt | Bold italic heading, body bold |
| Index Terms | 9 pt | Bold italic heading |
| Body text | 10 pt | Justified |
| Section heading (I.) | 10 pt | Centred, small caps, Roman numeral |
| Subsection heading (A.) | 10 pt | Flush left, italic, title case |
| Sub-subsection (1)) | 10 pt | Indented, italic, run into text |
| Figure caption | 8 pt | Below the figure |
| Table caption | 8 pt | Above the table, small caps, centred |
| Table body | 8 pt | |
| References | 8 pt | |
| Footnotes | 8 pt | |

Typeface is Times New Roman or an equivalent serif throughout, except where the template specifies otherwise for figure text.

**Journal and Transactions templates differ** — notably the title (often smaller and set differently) and figure captions (typically 10 pt rather than 8 pt). Do not carry conference values into a journal submission.

## Caption placement

The rule people get backwards, stated once more because it is the most common error:

| | Placement | Numbering | In-text form |
| --- | --- | --- | --- |
| **Figure** | Caption **below** | Arabic: Fig. 1, Fig. 2 | Abbreviated: "Fig. 1" |
| **Table** | Caption **above** | **Roman**: TABLE I, TABLE II | Spelled out: "Table I" |

Separate numbering sequences. Both Fig. 1 and Table I exist in the same paper.

## Table rules

IEEE tables are open. Horizontal rules above and below the header row and at the foot; **no vertical rules**, and interior horizontal rules only where a genuine grouping needs them.

Units belong in the column heading, not in each cell. Table notes sit beneath the table keyed with superscript letters, so they cannot be mistaken for citations.

## Spanning elements

A figure or table too wide for one column may span both, and is then placed at the top or bottom of the page rather than in the middle. In LaTeX this is the starred environment (`figure*`, `table*`); in Word it is a full-width text box or a single-column section break.

## Common submission rejections

Most automated rejections are mechanical rather than editorial:

- **Fonts not embedded** in the PDF. The most frequent cause by a wide margin.
- **Wrong page size** — A4 submitted where US Letter is required, or the reverse.
- **Page limit exceeded**, often because references were not counted.
- **Figures below the required resolution**, or raster where vector was expected.
- **Bookmarks, links, or metadata** left in by the authoring tool.

Where the venue provides a validation tool such as IEEE PDF eXpress, run it early rather than on the deadline. It checks exactly these and nothing about the content.
