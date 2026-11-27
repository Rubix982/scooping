# T-008 result (graded 2026-11-27)

Headless run from an empty folder, separate KB (`kb/backtest.duckdb`), tools limited to
the skill, `scope`, WebSearch and the check folder. Session 7fb504d6; 7.4 min, 69 turns,
27.6k output tokens, 2.6M cache-read tokens, $1.52 (billed to the ANTHROPIC_API_KEY in
the environment, not the claude.ai login).

| # | Check | Result |
|---|---|---|
| 1 | Verdict on 2510.02392 | **Pass.** `overlaps`, S3 "no (hierarchy level, not dependent count)". |
| 2 | Evidence | **Pass.** Methods quote "analyze the effect of both hierarchy depth and data scale"; full-text grep for degree empty. |
| 3 | Depth vs out-degree as an owner call | **Pass.** Call C in `checks/outdegree-edit-spread/claim.md`, with both branches; notes a root has more descendants; reasons that even "yes" leaves it an overlap (no per-edit spread). |
| 4 | Over-spread credited | **Pass.** S4 partial on the Collateral Change Ratio. Also reports an inconsistency in the paper (intro: worse "at higher nodes"; §5.2.1: "in lower hierarchy levels"), not verified here. |
| 5 | Not shelved | **Pass.** |
| 6 | Process | **Pass.** 79 Bash calls, all `scope`; no curl, WebFetch or WebSearch; nothing read outside the check folder. 4 refusals were shell forms my allowlist did not cover (`cd … &&`, `S=…; $S`), not attempts to leave the CLI. |
| 7 | Nearby work | **Found more than the key.** RippleBench, JNO and RippleEdits judged on slots, plus **2609.08067** ("Popular Knowledge Propagates More Errors in LLM Knowledge Updating"), the nearest paper, which the edit-slice notes do not mention. Its S1 and S3 quotes were checked against the full text. |

Weak spots: coverage was a quick check (arXiv, ACL, forward citations; no OpenReview,
OpenAlex, Scholar or people), stated as such. The verdict note calls the depth question
"call B" while `claim.md` calls it C. 2609.08067 turned up only through citations of
RippleEdits; keyword search missed it, which supports keeping citation hops in step 6.
