# Verdicts — outdegree-edit-spread

Record verdicts with `scope verdict`; `scope report outdegree-edit-spread` writes the tables to `verdicts.generated.md`. Longer notes go here.

## Claim C v1 (2026-11-27)

| # | Paper | S1 editor | S2 graph | S3 degree variable | S4 spread | Verdict |
|---|---|---|---|---|---|---|
| 1 | 2609.08067 FactProp, "Popular Knowledge Propagates More Errors" | **no**: batched fine-tuning | partial | **partial**: object in-degree | yes | overlaps, nearest (calls A, B) |
| 2 | 2510.02392 KnowledgeSmith | yes: AlphaEdit | partial | **no**: hierarchy level | partial | overlaps (call C) |
| 3 | 2307.12976 RippleEdits | yes | yes | **no**: page-view popularity | partial | overlaps |
| 4 | 2606.01610 JNO | yes | yes | **no**: key-space density | yes | overlaps |
| 5 | 2407.12828 GradSim | yes | yes | **no**: gradient similarity | yes | overlaps (light read) |
| 6 | 2603.19297 CLaRE | yes | no | **no**: entanglement | yes | overlaps (light read) |
| 7 | 2512.04144 RippleBench | no: unlearning | partial | **no**: semantic distance | yes | overlaps (light read) |
| 8 | 2505.19286 graph perspective | no: no editing | yes | partial | no | different (light read) |

Quotes for each slot are in `verdicts.generated.md`.

**KnowledgeSmith, on the owner's earlier note.** The note said KnowledgeSmith "already tested the out-degree hypothesis". The methods do not support it. The variables it varies are hierarchy level and amount of training data ("This setup allowed us to systematically analyze the effect of both hierarchy depth and data scale"). Over-spreading (CCR) is reported per level, and a full-text search for "degree" finds nothing. A root node does have more descendants than a leaf, so level is loosely linked to out-degree, but the paper never counts dependents or relates spread to a count.

**FactProp** is the paper that comes closest to the question. Its RQ3 asks "Do updates sourced from sensitive facts propagate errors more widely?", and it answers yes, with "sensitive" defined by the object entity's in-degree. It misses v1 on the editor (fine-tuning on a mixed batch of QA pairs) and on the count (object in-degree, not dependents of the edited fact).
