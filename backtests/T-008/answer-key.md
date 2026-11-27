# T-008 answer key (do not show to the test session)

Source: `~/code/open-concept-lab/ai/edit-slice/CLAUDE.md`, Literature section, the
KnowledgeSmith entry corrected 2026-11-09 under R-003.

## What happened in the original case

The note said KnowledgeSmith (2510.02392) had "already tested the out-degree hypothesis"
and told the project not to re-derive it. That was wrong:

- "out-degree", "outdegree", "branching factor", "degree" and "fan-out" never appear in the
  paper.
- What it varies is a node's level in a hierarchy (root, intermediate, leaf). Its finding
  is that "different hierarchical branches exhibit distinct ceilings for achievable
  accuracy", with the root lowest and the leaf highest.
- The over-spread finding is real and quotable. §5.2.1 says "editing tends to over-spread,
  unintentionally altering related nodes", in contrast with unlearning, which "often
  under-spreads".
- Neither out-degree nor any kind of frequency is an independent variable in the paper.

The note had closed a question that was never answered.

## Grading

| # | Check | Pass | Fail |
|---|---|---|---|
| 1 | Verdict on 2510.02392 | `overlaps` or `different`, with the independent-variable slot (out-degree) marked unmatched | `same`, or the direction shelved |
| 2 | Evidence | A methods-level quote showing that hierarchy level is what varies, and a check that out-degree, branching or fan-out is absent (a `scope grep` of those terms coming back empty counts) | Verdict resting on the abstract or the earlier note |
| 3 | The real boundary | Raises, as a question for the owner, whether hierarchy level stands in for out-degree. In a tree the root has the most descendants, so the two are correlated. The skill should hand this over rather than settle it quietly. | Treats depth and out-degree as the same variable without asking, or never notices they are correlated |
| 4 | Overlap credited | Records the over-spread finding (§5.2.1) as the part that does overlap | Misses it, or uses it to claim a scoop |
| 5 | Not shelved | The claim stands, or is restated, with KnowledgeSmith as a baseline or point of comparison | "Already done, move on" |
| 6 | Process | Searches and reads went through `scope`; queries logged; no raw curl or WebFetch on search pages or PDFs | Bypassed the CLI |
| 7 | Nearby work (bonus) | Finds RippleBench (2512.04144; spread curves stratified by semantic distance, eight unlearning methods) or JNO (2606.01610) and judges them on slots | — |

Checks 1 to 3 decide the backtest: pass all three and the procedure would have caught the
original misread. Check 3 is the hardest and tells the most. The original correction says
depth "is not the same variable as" out-degree, but it never addressed how strongly the
two are correlated. A session that raises this has done better than the original
correction did.

Record the tokens and time next to the result, in threads.md under T-008.
