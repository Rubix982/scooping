# Threads

Open questions that surfaced and are parked until the current card closes.

### T-001 · Build the field grid from the brief (v0 in scope-tool-brainstorm.md §8)

**Status:** parked
**Parent:** —
**Opened:** 2026-11-27
**Question:** Does a facet grid over 150–300 interp papers show where ground-truth-checked work clusters? Parked behind the scoop check; reuses its ingest when it resumes.
**Answer:** —

### T-002 · What baseline does the brief's backtest need?

**Status:** parked
**Parent:** T-001
**Opened:** 2026-11-27
**Question:** "Flagged open at mid-2024, filled later" counts as a hit only if the tool beats the baseline that cells next to dense, growing cells fill anyway. Which baseline exactly?
**Answer:** —

### T-003 · Write the positioning statement for the advisors

**Status:** answered
**Parent:** —
**Opened:** 2026-11-27
**Question:** One page: claim C v2, K = 0 of 43, the two near-miss groups, what K rests on (S3 boundaries), and the search gaps, so the advisors can judge it.
**Answer:** `positioning.md` (claim C v3, 0 of 65) approved by the owner to send to the advisors as is, 2026-11-27. Earlier: Draft at `positioning.md`, legibility pass done 2026-11-27 (census: ~25 defects before, 0 after; file pointers kept with one explaining sentence). Being rewritten around claim C v3 (2026-11-27).

### T-004 · Second read of the two calls K = 0 rests on

**Status:** answered
**Parent:** T-003
**Opened:** 2026-11-27
**Question:** Is a frozen reader model's internals (ReCast 2610.11334) really outside S3, and is a deterministic oracle over natural runs (2605.25310) really outside S2?
**Answer:** Both calls kept on a same-reader reread argued from the other side; reasons and the "if reversed" consequence are in `claim.md` (Second read). Final call is the claim owner's.

### T-005 · Can "which step" have more than one right answer?

**Status:** answered
**Parent:** —
**Opened:** 2026-11-27
**Question:** 2611.18514 found the agent recovers a value from its action history when the original span is corrupted; a planted-step design needs to rule out redundant sources of the same cause.
**Answer:** Yes. 2611.18514 saw the agent recover a value "from its action history" when the original span was corrupted, and 2608.20627 asks whether a trace "still identifies the injected hop after the suffix changes". Design rule: target = the step where the cause entered; planted content appears only there (checked by string search); removing it must change the decision; later steps that carry it forward are scored separately.

### T-006 · Fill the search gaps before positioning.md is sent

**Status:** answered
**Parent:** T-003
**Opened:** 2026-11-27
**Question:** IAB workshop list (needs a login), OpenReview, Google Scholar, security proceedings, D's 60 screened items, and unresolved bibliography leads: does any of them meet all four conditions?
**Answer:** Mostly filled (`search-log.md`, gap-filling pass): IAB workshop (129 papers via OpenReview search), OpenReview, USENIX/NDSS/S&P 2026, ACL Anthology, D's screened items. 0 plausible 4/4. Still open: Google Scholar (manual), LTS fgfKz9Qhpx (PDF behind challenge), Aghzal et al. Preprints.org paper, Rennervate, Pan et al. 2026, CCS 2026.

### T-007 · Restate the direction around what ReCast does not do

**Status:** answered
**Parent:** T-003
**Opened:** 2026-11-27
**Question:** With reader-model internals counting, ReCast (2610.11334) answers claim C v2. Which restatement (claim v3) is worth doing, not just narrower: the agent's own activations versus a reader's, planted outside inputs rather than injected errors, or localization without training on step labels?
**Answer:** Option 1 chosen by the claim owner: claim C v3 (own activations versus a reader model versus text, on planted steps). Checked: 0 of 61 meet all four slots; LTS unresolved.

### T-008 · Backtest the scoop-check skill on a case with a known answer

**Status:** answered
**Parent:** —
**Opened:** 2026-11-27
**Question:** Run ~/.claude/skills/scoop-check on the KnowledgeSmith case from edit-slice (a false scoop verdict that closed an open question): does the procedure reach the right verdict without being told it?
**Answer:** Yes. All six graded checks passed, including handing depth-vs-out-degree to the owner as a call; 7.4 min, $1.52. See `backtests/T-008/result.md`.

### T-009 · Does 2609.08067 take edit-slice's out-degree direction?

**Status:** answered
**Parent:** T-008
**Opened:** 2026-11-27
**Question:** The backtest found "Popular Knowledge Propagates More Errors in LLM Knowledge Updating" (2609.08067: batched fine-tuning, answer-entity in-degree, per-hop spread), absent from edit-slice's notes; it takes the direction only if the owner answers yes to calls A and B in `checks/outdegree-edit-spread/claim.md`.
**Answer:** No. Owner calls A ("Must be locate-and-edit") and B ("No, different variable") keep it an overlap; its in-degree becomes the baseline. Recorded in `checks/outdegree-edit-spread/claim.md`.

### T-010 · Does LTS use the acting agent's own representations?

**Status:** open
**Parent:** T-007
**Opened:** 2026-11-27
**Question:** LTS (OpenReview fgfKz9Qhpx) finds failed steps from "cached step-level representations" checked against injected faults; if those are the acting agent's own, it may meet all four slots of v3. Needs the PDF saved by hand (bot check).
**Answer:** —

### T-011 · Does the out-degree direction survive an OpenReview and author sweep?

**Status:** answered
**Parent:** T-009
**Opened:** 2026-11-27
**Question:** "0 of 8" for edit-slice's direction rests on arXiv, ACL and forward citations only; in-flight ICLR 2027 work and the nearest papers' authors are unchecked (slug outdegree-edit-spread).
**Answer:** Yes, it survives: 0 of 13 after authors, ICLR 2027 OpenReview, OpenAlex, citations and the unjudged screen. New second baseline: Knowledge Spectrum (2509.17482), popularity predicts side effects, so out-degree must add beyond popularity. `checks/outdegree-edit-spread/claim.md`.

### T-012 · Does the skill pass a second misread case?

**Status:** answered
**Parent:** T-008
**Opened:** 2026-11-27
**Question:** One pass (KnowledgeSmith) is one data point; RippleBench or Forgetting is Not Erasure from edit-slice would show whether it generalises.
**Answer:** Yes, on the RippleBench case: all seven checks passed, quick mode included, and its reading beat the answer key, which inherited a wrong edit-slice correction; missed MQuAKE. 6.7 min, $1.28. `backtests/T-012/result.md`.

### T-013 · Does the skill need a quick mode for checks only the owner reads?

**Status:** answered
**Parent:** T-008
**Opened:** 2026-11-27
**Question:** For self use the skill still ends in positioning.md plus a legibility census; the backtest's quick check reached the right answer in 7.4 min for $1.52 without them. Should those steps run only when someone else will read the result?
**Answer:** Yes. The skill now runs quick by default when only the owner reads the result (12–20 queries, three sources, one citation hop, no positioning or census) and full when someone else will; verdict rules are identical in both. `skill/scoop-check/SKILL.md`, "Quick or full".

### T-014 · Edit-slice's RippleBench correction is itself wrong

**Status:** answered
**Parent:** T-012
**Opened:** 2026-11-27
**Question:** The 2026-10-03 correction says RippleBench "advertises no such pluggability"; v2 and v3 name knowledge-graph path length as a pluggable distance (never run). Fix the entry in `~/code/open-concept-lab/ai/edit-slice/CLAUDE.md`? Needs the owner's OK (other project).
**Answer:** Done 2026-11-27: dated correction appended to the RippleBench entry in edit-slice's CLAUDE.md (every version names path length; none runs it). Uncommitted in open-concept-lab.

### T-015 · Should `scope` record which paper version a verdict read?

**Status:** answered
**Parent:** T-012
**Opened:** 2026-11-27
**Question:** The full-text cache and verdicts store no arXiv version, and in T-012 the version decided the answer (v1 lacks the wording v2/v3 have). Record the version at fetch time and in each verdict?
**Answer:** Yes, done: `scope grep` records the arXiv version read (`reads` table, `version.txt` beside cached text; `<id>v1` reads an older one); verdicts store `paper_version`, shown in `seen` and reports.

### T-016 · How should a check catch retrieved-but-unjudged near papers?

**Status:** answered
**Parent:** T-012
**Opened:** 2026-11-27
**Question:** MQuAKE was in the T-012 KB but never judged; should closing a check require a pass over `scope hits --unjudged` with the slot screens?
**Answer:** Yes, done: the skill's closing step screens `scope hits --unjudged` with object terms and wide variable synonyms; `scope status` shows the unjudged count; lesson added to judgment.md.
