# Claim C — draft v1 (2026-11-27)

First version, written before any search. The owner's earlier note said KnowledgeSmith
(arXiv 2510.02392) "already tested the out-degree hypothesis"; that note is treated as an
unverified match, to be checked at methods level, not as a reason to shelve.

## The claim

No published paper or public post tests whether the out-degree of an edited fact (the
number of other facts in a knowledge graph that depend on it, counted over a fixed set of
edge types) predicts how far a locate-and-edit change to that one fact spreads to those
dependent facts, measured as how many of them change and by how much.

## The four slots

| Slot | What must be true of the candidate | Does not match |
|---|---|---|
| S1 Object | A single fact is edited by changing the model's weights with a locate-and-edit method (ROME, MEMIT, PMET, AlphaEdit, …). | No weight change (in-context or retrieval editing such as IKE, MeLLo). Only large batches with no per-fact result. Fine-tuning or hypernetwork editors only (MEND, FT-L): **boundary call for the owner**, see below. |
| S2 Ground truth / data | A knowledge graph says which other facts depend on the edited fact, with a fixed edge-type vocabulary, so each edited fact has a countable set of dependents. | Related facts chosen without a graph (paraphrases, CounterFact "neighbourhood" prompts about other subjects). Multi-hop questions whose dependency count is fixed by construction and never varies across edits. |
| S3 Method / access | The number of dependents (out-degree, or an equivalent count of the edited fact's connections in that graph) is treated as a variable that differs across edited facts, and spread is analysed against it. | Degree used only to build or filter the dataset. A different predictor (gradient similarity, subject popularity or pretraining frequency, layer, relation type) with no degree analysis. Popularity as a proxy for degree: **boundary call for the owner**. |
| S4 Measurement | Spread to the dependent facts is measured per edit: how many change, and/or by how much (probability or accuracy change), and related to the S3 variable. | Only edit success, paraphrase generalisation, or locality on unrelated facts. Only an aggregate score across all edits with no link to degree. |

Slots describe the question, not the quality of a design. A candidate that asks the same
question with a weaker design still matches. All four slots must be matched in the same
experiment. Three of four is positioning, not a scoop.

## Boundaries drawn with candidates already in view

None. Calls A and C below sit on lines written before any search. Call B's line ("a count
of the edited fact's dependents") was also written before the search, but its importance
became clear only after reading 2609.08067, so a second reader should judge it.

## Calls for the claim owner (open, 2026-11-27)

| Call | The question to answer | If "yes" | If "no" |
|---|---|---|---|
| A | Does a batched fine-tuning update count as "editing a fact" for S1, or must the editor be locate-and-edit (ROME, MEMIT, AlphaEdit)? | 2609.08067 (FactProp) meets S1. | No candidate meets S1 together with a degree variable. |
| B | Does "in-degree of the answer entity" (how many facts in the graph point to the same object) count as the edited fact's out-degree (how many facts depend on it)? | 2609.08067 meets S3. With A = yes, it takes v1 and the claim must be restated. | 2609.08067 stays an overlap, and its in-degree becomes the baseline predictor the out-degree must beat. |
| C | Does KnowledgeSmith's three-way hierarchy level (root, intermediate, leaf) count as a degree variable? | 2510.02392 meets S3, but it still misses S4 per edit, so it stays an overlap. | No change. |

Each call goes to the owner. My reading of each (A no, B no, C no) is a single reader's
judgment, and none of the calls has had a second read.

## Claim owner's decisions

Asked 2026-11-27, answered the same day (owner's words in quotes):
- **A:** "Must be locate-and-edit." 2609.08067 misses S1.
- **B:** "No, different variable." Answer-entity in-degree is not the edited fact's
  out-degree; 2609.08067 misses S3.
- **C** was not asked: both answers leave KnowledgeSmith an overlap (no per-edit spread).

**Consequence:** of 8 candidates, 0 meet all four slots of v1. 2609.08067 stays the
nearest overlap, and its answer-entity in-degree becomes the baseline predictor that
out-degree has to beat. This rests on a quick check (arXiv, ACL, forward citations); the
OpenReview and author sweeps were not run.
