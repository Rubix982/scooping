# Search log — pathlength-edit-spread

Queries and counts are in the knowledge base; `scope report pathlength-edit-spread` writes them to `search-log.generated.md`. Record gaps and coverage passes here.

Quick mode, 2026-11-27: 17 logged queries (arXiv 11 incl. two forward-citation pulls, ACL 1, OpenAlex 2; three arXiv queries returned 0).

## Gaps

- Forward citations of RippleBench (2512.04144) returned 0 from Semantic Scholar; the paper is too new or not yet indexed. Rerun later.
- "The Missing Piece in Model Editing" (GIE, s2:d6f7bdd4…) is not on arXiv; full text not read. Needs a PDF via `--file`.
- KnowledgeSmith (2510.02392) and UniEdit (2505.12345) were read by grep only; neither showed a change-vs-hop curve, but a figure-level read was not done.
- Not run (full-mode passes): people/labs sweep, OpenReview venues, Google Scholar, forward citations of CLaRE (2603.19297) and GradSim-style ripple predictors, LessWrong/blogs.
- Code side: only two queries (API-update editing). No search for edits on code knowledge graphs or repository dependency graphs specifically.
