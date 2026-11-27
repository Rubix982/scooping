# Claim C — draft v1

## The claim

No published paper or public post applies a single-fact weight edit to a language model
(ROME, MEMIT or similar) and measures how much the answers to other facts change as a
function of their path length in hops from the edited fact in a typed graph, counting
changes to facts that should not have changed.

Secondary claim C-code (the "later" half): the same, with S2 replaced by a code
dependency graph (functions, modules or APIs joined by call, import or type edges).

## The four slots

| Slot | What must be true of the candidate | Does not match |
|---|---|---|
| S1 Object | A weight edit that targets one fact (ROME, MEMIT, AlphaEdit, constrained fine-tuning on one fact) | In-context or retrieval editing with no weight change; only large batch edits with no per-edit analysis |
| S2 Ground truth / data | A typed graph (e.g. Wikidata relations) that gives each test fact a path length from the edited fact | Distance only by embedding or semantic similarity; a related/unrelated split with no hop count |
| S3 Method / access | Edit the weights, then query the edited model on facts at known path lengths | No edit applied; only representations analysed |
| S4 Measurement | Change in each test fact's answer (probability, accuracy, or rank), reported against path length over three or more hop values, including facts whose correct answer is unchanged | One pooled locality score; near/far binary only; only intended propagation (multi-hop questions that should take the new answer) |

Boundaries written before searching:
- Unlearning a topic or concept is not S1 (not a single-fact edit). If a candidate does
  unlearning with graph distance, it is "overlaps", and I will ask the owner.
- Multi-hop question benchmarks (questions whose reasoning chain passes through the edit)
  measure intended propagation by question length, not spread by distance; they miss S4
  unless they also report unintended change by hop.

## Boundaries drawn with candidates already in view

- The unlearning line under S1 was written before reading RippleBench's text, but after
  the owner had named RippleBench, so it may have been drawn with that paper half in view.
- "Three or more hop values" in S4 was my choice, written before searching. It is what
  separates the claim from RippleEdits (capped at 2 hops).

Open calls for the owner (not settled here):
1. RippleBench states that "knowledge-graph path length is one valid instantiation" of its
   distance, but its experiments use embedding cosine similarity and RAG rank. Does a
   framework that names your variable without running it count as having done it?
   If yes: the direction is an instantiation of RippleBench, and the paper must be framed
   as the first run of that instantiation, on single-fact edits. If no: C v1 is open.
2. Would results at 1 and 2 hops, grouped by test type, count as your measurement?
   If yes: RippleEdits covers part of S4 (unintended change at 1 hop via Relation
   Specificity). If no: it stays an overlap.

## Claim owner's decisions
