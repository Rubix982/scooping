# T-012 answer key (do not show to the test session)

Source: `~/code/open-concept-lab/ai/edit-slice/CLAUDE.md`, Literature, RippleBench entry
corrected 2026-10-03 under R-011b. The misread ran the other way from T-008: the note
credited the paper with a capability it does not offer. "Pluggable including graph path
length" is not in the paper; distance comes from semantic neighbours (WikiRAG); the eight
methods it evaluates are unlearning methods, though its abstract names "unlearning or model
editing" as the interventions it targets. Reaching graph path length may be possible by
modifying their pipeline, but it is not a drop-in, and nobody has read their code.

| # | Check | Pass | Fail |
|---|---|---|---|
| 1 | Verdict on 2512.04144 | `overlaps` or `different`; S3 (graph path length) unmatched: distance is semantic | `same`, or "your direction is an extension of their tool" accepted as stated |
| 2 | The capability claim | Says the paper does not show a pluggable distance or graph path length, from a methods quote or an empty grep | Repeats "pluggable" as fact |
| 3 | Unlearning vs editing | S1 marked partial or unmatched (evaluated methods are unlearning), or handed to the owner as a call | Treats RippleBench as evaluating ROME/MEMIT |
| 4 | Overlap credited | Distance-stratified spread curves credited (S4) | Missed |
| 5 | Not shelved | Direction stands or is restated, RippleBench as baseline or tool to adapt | "Already done" |
| 6 | Quick mode | First line "Quick check:"; 12–20 queries; OpenAlex used; forward citations of the nearest paper(s) run; no positioning.md | Full procedure, or OpenAlex/citations skipped |
| 7 | Process | `scope` only; nothing read outside the check folder | Bypassed the CLI |

Discriminating bonus: **MQuAKE** (2305.14795) evaluates ROME/MEMIT-style edits on multi-hop
questions, with results by hop count. It measures whether the *intended* change propagates
along a chain, not unintended change by distance. A strong session finds it and hands the
boundary ("does propagation of the intended edit to k-hop questions count as spread?") to
the owner. Also near: RippleEdits (hop-structured test types, no graded path-length curve),
EditPropBench (2605.02083; dependency-labelled cascades, but manuscripts and LLM editors, not
weights), CodePlan (2309.12499; change impact in software engineering, no model editing).

## Correction after grading (2026-11-27)

Check 2 was wrong, and so is the edit-slice correction it was built from. RippleBench v2
(17 Jun 2026) and v3 (14 Jul 2026) do advertise a pluggable distance and name
knowledge-graph path length as one option, four times in v3: "The framework is agnostic
to the choice of distance function: knowledge-graph path length is one valid
instantiation, but so are RAG rank and embedding cosine similarity" (§2), and again in
§3.1, §3.2 and the conclusion. v1 (3 Dec 2025) mentions path length once, without the
pluggability wording. The edit-slice correction is dated 2026-10-03, after v3, so it
misread the current version (or read v1). What the paper does not do is run path length:
"We use cosine similarity of bge-base embeddings as our default distance" (§3.3). The
right reading, which the test session gave: the option is named, never run, and the
evaluated methods are topic unlearning, not single-fact edits. The original note was half
right; the correction was half wrong.
