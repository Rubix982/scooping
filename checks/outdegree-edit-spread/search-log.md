# Search log — outdegree-edit-spread

Queries and counts are in the knowledge base; `scope report outdegree-edit-spread` writes them to `search-log.generated.md`. Record gaps and coverage passes here.

This was a quick check (20 logged queries, 2026-11-27), run to keep token use low.

## Coverage passes done

- arXiv keyword search: q1–q13 (ripple effects, degree, hub, centrality, popularity, fan-out, dependent facts).
- ACL Anthology, 2022 onward: q14 (regex for editing plus degree, hub or centrality). The hits were noise ("degree" in its ordinary sense).
- Forward citations: KnowledgeSmith (q15), the graph-perspective paper 2505.19286 (q16), JNO 2606.01610 (q17), RippleEdits (q18, 372 citing papers, screened down to degree terms), GradSim (q19), FactProp 2609.08067 (q20, 0 citing papers yet).
- The nearest paper (2609.08067) was found only through forward citations of RippleEdits. The keyword queries missed it because it says "popularity" and "in-degree", not "edit" plus "out-degree".

## Gaps

- No author sweep. The FactProp (2609.08067) and KnowledgeSmith authors were not searched for follow-up work.
- No OpenReview sweep (ICLR 2027 submissions, NeurIPS 2026 workshops). This is where in-flight work would show up.
- No OpenAlex (journals, proceedings off arXiv).
- No Google Scholar. No query file was written yet.
- No lab or blog search (LessWrong, Alignment Forum).
- Screen caveat: the `hub` term in early screens also matched "github", so those screens were loose. The final re-list used `\bhubs?\b`.
