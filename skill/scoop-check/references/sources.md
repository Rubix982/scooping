# Source access: what worked and what did not (learned 2026-11)

The `scope` CLI wraps every source below that can be automated. This table is for
understanding its failures (an HTTP code in a query line) and for the sources it cannot reach.

| Source | Use | Notes |
|---|---|---|
| arXiv search pages (`arxiv.org/search/`, `/search/advanced`) | keyword, title, abstract, author search; date ranges | Reliable. `scope search arxiv` / `authors`. Lexical only: papers with other vocabulary are missed. |
| arXiv export API (`export.arxiv.org/api/query`) | — | Often returns empty bodies or 429, especially when another agent queries in parallel. Prefer the search pages and abs pages. |
| arXiv abs / html pages | abstracts, full text | `scope abstract`, `scope grep` (HTML, falls back to PDF + pdftotext; cached in `kb/cache/`). Math symbols drop out of extracted text. |
| OpenReview `api2.openreview.net/notes/search` | venue enumeration with `group=`, keyword search, ARR and ICLR submissions | Works without login. `/notes?id=` and `/pdf` hit a bot challenge (403), so PDFs of OpenReview-only papers need the user's browser. `scope search openreview`. |
| Semantic Scholar citations endpoint | forward citations | Mostly works with retries. The keyword search endpoint is nearly always 429. `scope search cites`. Very new papers have few or no citers. |
| OpenAlex | journals and proceedings with venue names; institution and per-institution author counts | Works anonymously. `scope search openalex` (put a phrase in double quotes, or words match separately and other fields leak in), `scope census --source openalex [--country US] [--institution …]`. Affiliations come from each paper's authorships; author profiles (`last_known_institutions`) are unreliable. The institution lookup prints its first match and alternatives: check the country, since names collide. Affiliation coverage for very recent arXiv-only papers is thin, so per-institution author counts run low. |
| Google Scholar | keyword and "Cited by" | Blocks automated queries and its terms forbid them. Write a query file; the user pastes raw result pages under `## N` headings; import with `scope search scholar`. No "Cited by" link under a result means zero citers. |
| ACL Anthology | ACL, EMNLP, NAACL, EACL, Findings, TACL, workshops | `scope search acl` downloads `anthology+abstracts.bib.gz` (~47 MB, about a minute) into `kb/cache/acl/`, refreshes it weekly, and greps titles and abstracts locally (about 6 s). The argument is a regex, not a keyword query. |
| DBLP | — | API and both mirrors sit behind a proof-of-work bot challenge (HTTP 202, checked 2026-11-27). Not wrapped. |
| Conference programs (USENIX Security, NDSS, IEEE S&P) | security venues | Program pages are fetchable and greppable. CCS pages move each year. |
| Lab blogs, LessWrong / Alignment Forum, GitHub | non-paper work | WebSearch with `site:`; GitHub search API without auth. |
| Preprints.org | some position papers | Often 403 to automated fetches; needs the user's browser. |
| WebSearch | lab pages, people | Returns pages one at a time; not a census. Good for verifying a lab page, poor for listing labs. |

## Finding people (labs, faculty)

Do not list labs from memory. Build the list from data, then sweep each person:
1. Institution census in OpenAlex for the field's phrase (`scope census "<phrase>" --source
   openalex --country US`), then the people at each institution that matters
   (`--institution "<name>"`).
2. arXiv last-author census (`scope census`). Flat distributions
   are normal; many groups avoid the exact phrase.
3. Authors of the nearest papers, plus groups the user names.
4. `scope search authors <slug> names.txt --since <YYMM> --screen <field terms>`.
Say plainly which institutions came out thin.
