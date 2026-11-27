# Search log — scoop check for claim C (run 2026-11-27)

Recall was split into three slices, each run by a separate agent. Each agent was told
to log every query, to list only items whose pages it opened, to quote abstracts
word for word, and not to judge scoop. The full logs, with every query string and
count, are in `recall/`:

- `recall/A-planted-ground-truth.md`: interp methods checked against planted or known ground truth, any object (S2+S4)
- `recall/B-agent-multistep.md`: interpretability of agents and multi-step reasoning, plus planted causes checked by any method (S1)
- `recall/C-non-arxiv-inflight.md`: venues off arXiv and work still in flight

## Coverage

| Slice | Searches | Main sources | Candidates listed (+ screened) |
|---|---|---|---|
| A | 98 rows | arXiv API; Semantic Scholar (citations of AuditBench, hidden objectives, Pando, InterpBench); WebSearch | 25 (+ ~60 overflow) |
| B | 100 rows | arXiv API (76 queries); Semantic Scholar citations of 7 seeds; WebSearch (14) | 25 (+ ~40 screened) |
| C | 28 rows, many batched | transformer-circuits.pub; alignment.anthropic.com; LessWrong/AF API (~50 queries); Goodfire, Transluce, Apollo, GDM, OpenAI, EleutherAI, FAR, METR, Redwood; ICML 2024, NeurIPS 2025 and ICML 2026 MI workshop poster pages; GitHub API (29 queries); MATS, SPAR | 25 (+ ~30 lower overlap, 17 in-flight) |

Date window: January 2023 to 2026-11-27.

## Gaps — what this search did not cover

These limit any "the lane is open" statement built on this log.

- **Semantic Scholar keyword search** returned HTTP 429 on almost every attempt in all three slices. Only its citations endpoint worked.
- **OpenReview** (API and forum pages) returned a bot challenge, so workshop and conference submissions that exist only there were not searched.
- **NeurIPS 2026 "Interpreting Agent Behavior" workshop:** the accepted-paper list needs a login. This is the venue most likely to hold S1 work. One poster was found through WebSearch.
- **Not searched at all:** Google Scholar, the ACL Anthology search, X/Twitter, talks, Discord/Slack, Anthropic and OpenAI system cards.
- **arXiv field search matches words, not meaning,** so papers using different vocabulary can be missed. Large citer lists were filtered by title keywords, not read.
- **Lab blogs:** OpenAI's index shows only its ~20 most recent items without JavaScript, and DeepMind's main blog was not crawled.

## Methods-level reads

See `verdicts.md`. 4 candidates read so far.

---

# Claim C v2 ("which step"), 2026-11-27

v2 is narrower than v1, so the v1 recall (`recall/A–C`) covers its candidates in
principle. Two things were added for v2.

**1. Supplementary recall for step-localization vocabulary:** `recall/D-step-localization.md`
(agent failure attribution, context attribution and traceback, prompt-injection
localization, trigger localization, step importance in agent trajectories, multi-turn
attribution). 62 log rows, 41 search calls; 24 ranked candidates, 60 screened, 7 dropped.
All 24 ranked were given verdicts (rows 24–43 of `verdicts.md`; the other 4 were already
read). D's own gaps: the Aghzal et al. Preprints.org paper "Understanding LLM Agents
Requires a Chain of Attribution" (DOI 10.20944/preprints202610.2861.v1) returned 403;
security proceedings and OpenReview not searched directly; no citation hops on the newest
seeds (Attnlocate, MindGuard, DriftNet, Tokengeist).

**2. Citation hops made while reading methods** (not keyword searches; logged here so
they can be rerun):

| From | Reference followed | Resolved to | How |
|---|---|---|---|
| 2608.06909 §2.2 | Qian et al. 2026, "The why behind the action" | 2601.15075 | arxiv.org title search |
| 2608.06909 §2.2 | Kim et al. 2026, CausalArmor | 2602.07918 | arxiv.org title search |
| 2608.06909 §2.2 | He et al. 2026, AttriGuard | 2603.10749 | arxiv.org title search |
| 2610.28811 §4.1 | Who&When (label provenance) | 2505.00212 | already known ID |

The export.arxiv.org API returned empty bodies for these three title queries (probably
rate limiting while the recall agent was also querying it); the arxiv.org search page
worked.

**Leads seen in bibliographies, not yet resolved or read:**
- From 2608.02657: PromptLocate, Rennervate, PIShield (injected-span localization or detection from model features).
- From 2608.06909: TraceElephant (Chen et al. 2026), AgentRx (Barke et al. 2026), In et al. 2026, Causal agent replay (Shah 2026).
- From 2611.18514: Pan et al. 2026 (attribution over multi-token responses), Sankaranarayanan et al. 2026 (intervention points for distributed behaviours).

**Verdicts:** 43 candidates (`verdicts.md`, v2 section), of which 14 are light reads.

## Gap-filling pass (T-006), 2026-11-27

Screens here are abstract-level unless noted. A screen can rule a paper out but cannot
rule one in; anything that looked like a possible 4/4 would have gone to a methods read.

| Gap | What was done | Result |
|---|---|---|
| NeurIPS 2026 IAB workshop | OpenReview `api2.openreview.net/notes/search` with `group=NeurIPS.cc/2026/Workshop/IAB`, 12 terms (agent, interpret, probe, attribution, mechanistic, steering, trajectory, planted, causal, tool, injection, monitor). No login needed. | 129 workshop papers. 30 match an internals term plus a step term in the abstract; 16 abstracts read. 0 plausible 4/4. Step localizers there are black-box: call-level attribution with injected faults (eTcBmqkEF8), StepShield (imOHSXMkZx, annotated divergence steps), PIVOT (Dls5TK8t2H). Known items recur: Causal Probes (eOxoW6FSoV), Tokengeist (qYnCoxQM6N). |
| OpenReview generally | Same endpoint, 8 terms, no group filter. The `/notes?id=` and `/pdf` endpoints still return a bot challenge (403). | 97 forums since 2025-06; 8 OpenReview-only items checked. 0 plausible 4/4. **Unresolved: LTS (fgfKz9Qhpx, ACL ARR Oct 2026)**, which localizes failed steps from "cached step-level representations" and evaluates with "fault-injection replay"; whose model the representations come from is not in the abstract, and the PDF is behind the challenge. |
| Security proceedings | Program pages: USENIX Security 2026, NDSS 2026, IEEE S&P 2026 (titles and abstracts grepped for agent + attribution/localization/tracing/forensics/provenance). CCS 2026 page returned 404. | Only AttriGuard (already read). CCS not covered. |
| ACL Anthology | Full `anthology.bib.gz` (13.6 MB), titles grepped for agent/trajectory/tool + attribution/localization terms. | 30 title hits; 3 abstracts read (DealTrace, EDGE, ShapleyFlow). All black-box. 0 plausible 4/4. |
| D's 60 screened items | Re-screened D's one-line descriptions; 4 abstracts fetched (2609.27773 MTAG-Bench, 2607.17621 AGMR, 2607.12747 OAT, 2602.06841). | 0 plausible 4/4. MTAG-Bench is multi-turn chat (fails S1); AGMR and OAT have no planted step. |
| Bibliography leads | arxiv.org title search. | PromptLocate = 2510.12252 (single contaminated input, fails S1). AgentRx = 2602.02475 (manually annotated steps). Multi-perspective attribution = 2603.25001 (annotated; relevant to T-005). Sankaranarayanan et al. is a steering method, out of scope. **Unresolved:** Rennervate (no arXiv title match), Pan et al. 2026 (title not recoverable from the extracted bibliography). |
| Google Scholar | Not attempted: it blocks automated queries. | **Needs a manual search.** |
| Aghzal et al. Preprints.org paper | Not retried (403 for the recall agent). | **Needs a browser.** |

The export.arxiv.org API returned empty bodies again during this pass; arxiv.org abstract
and search pages worked.

## Coverage pass 2: people and forward citations, 2026-11-27

**Author sweep.** arxiv.org author search (`searchtype=author`, newest first, 50 per
person), 55 people (list: `recall/E-author-sweep-names.txt`): every author of the nearest
papers, plus established interpretability groups named as search targets (Bau, Belinkov,
Geiger, Mueller, Andreas, Wiegreffe, Steinhardt, Marks, Barez, Ghandeharioun, Wattenberg,
Potts, Sharkey, Lindsey). Kept listings since April 2026 with a relevant word in the
title that were not already in our files: 158. Most are off-target or come from a common
name shared with someone else. Five abstracts were read (2611.10457, 2610.31686,
2610.22723, 2604.18307, 2605.26037). **0 meet all four conditions.** Positioning
neighbour: 2604.18307 finds that reasoning models encode in their activations which
reasoning steps matter (single chain of thought, so it fails condition 1).

**Forward citations.** Semantic Scholar citations endpoint for 10 nearest papers. After
retries, 3 lookups (ReCast 2610.11334, 2601.15075, and on the first pass 2605.25310) still
returned HTTP 429 or no citers. 34 citing rows; 18 new relevant titles, 3 abstracts read.
0 meet all four. Design baseline found: 2610.16661, where a rule that always names the
last step is "correct 67% to 96% of the time" on failure-attribution benchmarks.

**Reader-model family re-screen (needed after call B was reversed).** ReCast's related
work separates "external trajectory representations" (ASCon, StepFinder, AgenTracer,
AgentForesight) from "White-box Failure Attribution Methods" (MASPrism, OAT, ReCast).
MASPrism and OAT are scored on Who&When / TRAIL, which have annotated labels, so they miss
condition 2. AFTraj-2K, ReCast's other benchmark, has "decisive-error annotations"; its
provenance was not checked. LTS is white-box and unresolved.

**Still not covered:** Google Scholar (manual), the LTS PDF, the Aghzal et al. preprint,
lab pages and talks of the groups above (only their arXiv listings were swept), X, and
system cards.

## Coverage pass 3: US university labs and Google Scholar, 2026-11-27

- **US university labs:** `recall/F-us-university-labs.md`. OpenAlex institution census
  (514 works, 31 US universities), arXiv last-author census (708 papers), 4 web searches,
  then an arXiv sweep of 34 new people (89 people in total across passes). 0 meet all four
  conditions.
- **Google Scholar:** cannot be queried automatically. 14 manual queries are in
  `recall/G-google-scholar-queries.md`.
- OpenAlex returned HTTP 429 on 11 of 41 institution lookups at first; all but Georgia Tech
  succeeded on retry.

## Google Scholar, manual (run by the claim owner), 2026-11-27

Results pasted under each query in `recall/G-google-scholar-queries.md`. **All 14 queries run**
(queries 1–2: 5 pages each; 3–7: 2 pages or more; 8–13: cited-by pages). 78 unique titles parsed: about 10 already in our
files; most of query 2 is off-topic (philosophy, psychiatry, robotics). Checked further:
- 2610.06576 "Before Agent Tells The Lie": predicts deception from the agent's internal
  representations before the decisive step. A forecast, so it misses condition 4.
- "One Reflex, Two Answers" (Scavotto, MDPI MAKE 2026): controlled fault injection, LLM
  judges scored. Black-box, so it misses condition 3.
- "Detect before you attribute": the snippet describes semantic embeddings and statistics
  over agent invocations. Not found on arXiv by title; abstract not read.
- Aghzal, Geva, Hassan, Stein, Yao, "Understanding LLM Agents Requires a Chain of
  Attribution" (preprints.org): Scholar shows a PDF link. The snippet reads as a position
  paper ("interpreting LLM agents requires pairing …"; "a chain of attributions tracing an
  agent's action back"). Not read.
- Other new titles are black-box failure attribution, taxonomies or benchmarks with
  annotated labels.
**0 plausible matches for all four conditions from queries 1–2.**

**Google Scholar, queries 3–14 (same file).** About 270 titles across all 14 queries. Query 8
captured the Who&When Pro arXiv page, not its cited-by list; its citers were already
pulled from Semantic Scholar (pass 2). Query 9 (ReCast): 0 citers. Query 14: LTS not
found (the only hit is an unrelated 2025 paper). Abstracts read for the four titles whose
snippets suggested internals plus localization:
- 2609.37737 "Where Do LLMs Decide to Break the Rules?": activation patching localizes
  injection compliance to a late-layer bottleneck. That is depth, not a trajectory step.
- 2604.22888 RouteGuard: "attention hijacking" from trusted context to poisoned skill
  spans; a detector of skill poisoning. Misses condition 4.
- 2607.06807 AcMAS: activation-based detection of compromised agents in multi-agent
  systems (F1 0.94 vs 0.72). It names an agent, not a step, and scores detection.
- "Typed Slot Policies …" (OpenReview ghjnWi5a2o, COLM 2026 workshop): activation
  patching checks that a region-attribution signal is faithful ("pooled Spearman
  ρ=0.38"), in a "degenerate single-step" setting. Misses condition 1.
Other new titles are black-box failure attribution, injection attacks and defenses,
surveys, or off-topic (vehicle trajectory prediction, philosophy).
**0 plausible matches for all four conditions from Google Scholar.**

## Claim C v3 check, 2026-11-27

Targeted search for the comparison itself. arXiv abstract search: "matched generator",
"own activations" agent, "white-box" "failure attribution", "self-attribution" agent,
"hidden states" "failure attribution", "own hidden states" agent step, "agent's own"
activations trajectory. OpenReview search: 4 terms (own activations / matched generator /
white-box failure attribution / planted step activations). New relevant item: Goal-Drift
Probes (OpenReview 7847AalUvX, ICML 2026 AIWILD workshop), which forecasts natural
failures from a Qwen2.5-7B ReAct agent's residual stream (AUC 0.989, three steps ahead).
It misses S2 and S4. Everything else was already logged, black-box, or off-topic.

## Coverage pass 4: OpenAlex and the full ACL Anthology, through `scope` (2026-11-27)

The first pass run entirely through the `scope` CLI; queries q12–q17 are in the knowledge
base (`bin/scope report agent-step-localization` writes them out).

- ACL Anthology, titles and abstracts (anthology+abstracts.bib, local grep), 2025 on: two
  regexes, 189 results, 180 new to this check.
- OpenAlex `title_and_abstract.search`, from 2025-01: four queries, 528 results, 435 new.
- Screen over the 615 new records: internals term AND planted/attribution term AND agent
  term → 97. Read by title and key sentences; 8 pulled for a closer look; 4 recorded as
  v3 light-read overlaps (2610.37679, 2606.22864, openalex:W7164739120,
  openalex:W7163149144). None meets all four slots. All four use the agent's own internals
  and detect or forecast; none locates the step.
- What this pass adds over passes 1–3: OpenAlex reaches records with no arXiv copy
  (Zenodo, SSRN, theses, journals). Two of the four overlaps came only from there.
- DBLP was tried and is not reachable (bot challenge on API and mirrors).

## LTS read (T-010, 2026-11-28)

OpenReview's PDF and API attachment both returned 403 again, and LTS is not on arXiv
(title search). The owner saved the PDF to `notes/lts.pdf` (not committed); read with
`scope grep openreview:fgfKz9Qhpx --file notes/lts.pdf`. The text is two-column and partly
interleaved; quoted sentences were checked whole. Verdict: overlaps (S3 fails).
