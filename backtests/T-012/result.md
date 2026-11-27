# T-012 result (graded 2026-11-27)

Headless run from an empty folder, fresh KB (`kb/backtest-t012.duckdb`), same tool limits
as T-008. Session 99c5d1cf; 6.7 min, 64 turns, 21.6k output tokens, 2.2M cache-read
tokens, $1.28 (API key). 11 candidates, 0 meet all four slots; "open on a quick check".

| # | Check | Result |
|---|---|---|
| 1 | Verdict on 2512.04144 | **Pass.** `overlaps`; spread is measured against embedding or rank distance, never path length. |
| 2 | The capability claim | **Pass, and better than the key.** It quoted the paper naming path length as a pluggable option and said it is never run. The key, built from edit-slice's correction, said the paper advertises no pluggability; that is false for v2 and v3 (verified; see the correction in `answer-key.md`). |
| 3 | Unlearning vs editing | **Pass.** S1 "no: eight concept-unlearning methods (WMDP-Bio checkpoints), not single-fact weight edits". |
| 4 | Overlap credited | **Pass.** "accuracy delta vs distance curve including unintended items". |
| 5 | Not shelved | **Pass.** Handed the owner the call that matters ("does a framework that names your variable but never runs it count as having done it?") and framed the work, if yes, as the first run of that option on single-fact edits. |
| 6 | Quick mode | **Pass.** Opened "Quick check:"; 17 queries (12 arXiv, 2 OpenAlex, 1 ACL, 2 forward-citation); no positioning.md. |
| 7 | Process | **Pass.** 67 Bash calls, all `scope`; no curl or WebFetch; 2 refusals were shell forms outside the allowlist. |
| bonus | MQuAKE | **Miss.** MQuAKE was retrieved (ACL record, and MQuAKE-Remastered among citers) but never judged. It evaluates edits on 2–4-hop questions, which bears directly on the session's own call 2 (are 1–2 hops enough?). |

Also found: CLaRE (2603.19297), named as the baseline a hop-count curve must beat;
RippleEdits; the code-editing benchmarks (CodeUpdateArena and one more), whose side
effects are one pooled score with no dependency graph.

Weak spots: a retrieved paper on the claim's exact variable went unjudged, so retrieval
is not the bottleneck; screening the stored hits is. The verdicts do not record which
arXiv version was read, and in this case the version decided the answer.
