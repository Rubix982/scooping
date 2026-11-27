# Verdicts

Two sections: claim C v2 (current), then claim C v1 (superseded, kept as it was).
Quotes are copied from the arXiv HTML or PDF text of each paper. Math symbols dropped
out during text extraction, so some quoted sentences have gaps.

---

## Verdicts against claim C v3 (2026-11-27)

v3's slots are in `claim.md`. The deciding slot is S3: the step must be located from the
**acting agent's own internals**. Quotes for each paper are in the v2 section below, or in
`search-log.md` for papers screened after it.

**Status (card closed 2026-11-27):** 61 candidates (43 with v2 verdicts, plus 18 abstract
screens since), **0 meet all four slots of v3.** One item is unresolved: LTS (OpenReview
fgfKz9Qhpx), whose representations' source is not stated in the abstract and whose PDF
could not be opened.

**Coverage pass 4 (same day):** four more light-read overlaps, all own-internals detection
or forecasting: 2610.37679 and 2606.22864 (probes for planted prompt injections),
openalex:W7164739120 "Felt, Not Granted" (internal probe vs LLM judge on each proposed
action), openalex:W7163149144 "No Better Than Behavioral" (residual stream vs tool entropy,
nothing planted). Quotes in `verdicts.generated.md`. Count: 0 of 65.

Nearest work by the slot it misses:

| Paper | S1 | S2 planted step | S3 agent's own internals | S4 scored on the step | Comparison arm in the paper | Misses |
|---|---|---|---|---|---|---|
| ReCast 2610.11334 | yes | yes (Who&When Pro) | **no**: frozen reader model; the agents are closed | yes (Hit@1) | — | S3 → becomes the reader arm |
| Tokengeist 2607.22610 | yes | **no**: LLM-produced labels | yes (matched-generator replay) | yes (turn recall) | reader (mismatched generator) | S2 |
| 2605.25310 tool-call dependency | yes | **no**: text-matching oracle | yes (residual stream) | yes (edge AUROC) | surface-form text decoder | S2 |
| The Agent Knew 2610.17301 | yes | yes | yes (residual stream) | **no**: forecasts the action | CoT monitors | S4 |
| 2610.24048 Window in the Reasoning | yes | yes | yes (hidden states) | **no**: forecasts compliance | text monitors, TF-IDF | S4 |
| 2610.18408 injection probes | yes | yes | yes (hidden states) | **no**: content detection | TF-IDF text classifier | S4 |
| 2608.02657 IPI exposure | yes | yes | yes | **no**: presence | — | S4 |
| Attnlocate 2608.24022 | partial | yes | yes (attention) | **no**: span IoU, one tool return | — | S1, S4 |
| AcMAS 2607.06807 | yes | partial (compromised agent) | yes | **no**: agent-level detection | graph baselines | S2, S4 |
| Goal-Drift Probes (OpenReview 7847AalUvX) | yes | **no**: natural failures | yes | **no**: forecast | behavioural baselines | S2, S4 |
| Who&When Pro, 2608.20627, AgenTracer, DriftNet, AgentTracer (IPI) | yes | yes | **no**: black-box | yes | — | S3 → text arm |
| 2610.28811, MASPrism, SOAP, OAT | yes | **no** (annotated) | **no** (reader) | yes | — | S2, S3 |

No paper has all three arms (own internals, reader internals, text) on planted steps.
Tokengeist is the only one with own-versus-reader on the same runs, and its labels are
LLM-produced.

---

## Verdicts against claim C v2 (2026-11-27)

Slots are in `claim.md`. All four slots must be matched by the same experiment; slots
matched in different experiments of one paper count as overlaps (this rule was already
applied to 2610.05295 under v1). "BB" marks a method that is black-box, which S3
currently excludes.

**Status (card closed 2026-11-27):** 43 candidates given a verdict, 0 match all four
slots. Rows 1–23 came from `recall/A–C` and citation hops; rows 24–43 from
`recall/D-step-localization.md`. Not given verdicts: D's 60 screened items and the
unresolved bibliography leads listed in `search-log.md`.

**What K = 0 rests on.** Under S3 as written, K = 0. If the S3 boundary on a different
model's internals were dropped, ReCast (row 27) would match all four slots. If
black-box methods counted, rows 1–3, 38 and 40 would. The claim survives only as "the
agent's own internals". That is the point the advisors need to see.

| # | Paper | S1 agent loop | S2 planted at a chosen step | S3 agent's own internals | S4 scored on picking the step | Verdict |
|---|---|---|---|---|---|---|
| 1 | 2607.09996 Who&When Pro | yes | yes | **no (BB: LLM judges)** | yes | overlaps, 3/4 |
| 2 | 2608.20627 Causal Failure Attribution in Agentic RAG | yes | yes | **no (BB: coverage, LLM judge, repair)** | yes | overlaps, 3/4 |
| 3 | 2509.03312 AgenTracer | yes | yes (injected subset) | **no (BB: fine-tuned LLM tracer)** | yes | overlaps, 3/4 |
| 4 | 2610.17301 The Agent Knew | yes | yes | yes | **no (forecasts the action)** | overlaps, 3/4 |
| 5 | 2610.24048 The Window Is in the Reasoning | yes | yes | yes | **no (forecasts compliance)** | overlaps, 3/4 |
| 6 | 2608.02657 IPI exposure in hidden states | yes | yes | yes | **no (presence)** | overlaps, 3/4 |
| 7 | 2610.05295 Readable Before Actionable | yes | yes | yes | **no** | overlaps, 3/4 split across experiments |
| 8 | 2610.28811 Mechanistic Study of Failure Attribution | yes | **no (human labels)** | **no (a reader model's internals)** | yes | overlaps, 2/4 |
| 9 | 2601.15075 The Why Behind the Action | yes | **no (human labels)** | partial (one gradient baseline) | partial | overlaps |
| 10 | 2608.06909 Trajectory Attribution benchmark | yes | **no (LLM labels)** | **no (likelihood ablation)** | yes | overlaps, 2/4 |
| 11 | 2610.25947 Claim Laundering | partial | yes | yes | **no** | overlaps |
| 12 | 2610.40588 Pre-Crime for Agents | yes | partial | yes | **no (forecasts the action)** | overlaps |
| 13 | 2611.18514 MI for web-agent hallucination | yes | **no (natural failures)** | yes | **no** | overlaps, 2/4 |
| 14 | 2602.07918 CausalArmor | yes | yes | **no (BB: likelihood on a proxy model)** | **no (attack success)** | overlaps, 2/4 |
| 15 | 2603.10749 AttriGuard | yes | yes | **no (BB: replay)** | **no (attack success)** | overlaps, 2/4 |
| 16 | 2609.06445 Causal Attribution for Agentic Decisions | **no (no LLM)** | yes | **no** | yes | overlaps, 2/4 |
| 17 | 2605.17113 The Point of No Return | **no (one reasoning trace)** | **no (resampling labels)** | yes | partial | overlaps |
| 18 | 2611.10620 What Do Collusion Probes Read? | unclear | **no (in the weights for the whole run)** | yes | **no (presence)** | overlaps |
| 19 | 2610.12445 Telling FIBS | yes | lenient yes (initial instruction) | yes | **no (transcript classification)** | overlaps |
| 20 | 2606.06223 Reward-hack activations in agents | yes | **no (adapter, no step)** | yes | **no** | overlaps (light read) |
| 21 | 2606.30449 Probes read the situation, not the action | yes | **no** | yes | **no** | overlaps (light read) |
| 22 | 2611.21799 Controllable CoTs | yes | **no** | **no (BB)** | **no** | overlaps (light read) |
| 23 | 2604.01151 HELIOS / NARCBench | yes | **no (instructed)** | yes | **no (presence)** | overlaps (light read) |
| 24 | 2605.25310 Tool-call dependency decodable in residual streams | yes | **no (oracle over natural runs, not planted)** | yes | yes (edges vs oracle) | overlaps, 3/4 |
| 25 | 2607.22610 Tokengeist | yes | **no (LLM-produced gold DAGs)** | yes (matched-generator replay) | yes (turn source recall) | overlaps, 3/4 |
| 26 | 2610.18408 Prompt-injection probes learn the conversation | yes | yes | yes | **no (content detection per tool output)** | overlaps, 3/4 |
| 27 | 2610.11334 ReCast | yes | yes (on Who&When Pro) | yes after call B reversed (frozen reader LLM) | yes (Hit@1) | **all four, after call B reversed; second read pending** |
| 28 | 2604.01194 AgentWatcher | yes | yes | yes (attention; may be the agent) | **no (ASR, utility)** | overlaps, 3/4 |
| 29 | 2608.24022 Attnlocate | partial (one tool return) | yes | yes | **no (span IoU, not step)** | overlaps |
| 30 | 2508.20412 MindGuard | partial | **no (poison in tool metadata)** | yes | partial (source attribution) | overlaps |
| 31 | 2605.07509 MASPrism | yes | **no (annotated)** | **no (Qwen3-0.6B reader)** | yes | overlaps, 2/4 |
| 32 | 2610.13105 SOAP | yes | **no (annotated)** | **no (reader model)** | yes | overlaps, 2/4 |
| 33 | 2605.03354 Agent-memory circuits | partial (pipeline stages) | **no (LLM-judge stage labels)** | yes | partial (stage) | overlaps |
| 34 | 2603.12564 Sell Me This Stock | yes | yes | yes | **no (turn found by contaminating inputs)** | overlaps, 3/4 (light) |
| 35 | 2609.33676 Query-conditioned attribution | yes | unclear | **no (proposer models)** | yes (source MRR) | overlaps (light) |
| 36 | 2611.15118 Lazare (dormant-neuron backdoor) | yes | yes | yes | **no (checkpoint-level)** | overlaps (light) |
| 37 | 2610.21708 Human interventions as labels | yes | **no** | yes | **no (layer depth)** | overlaps (light) |
| 38 | 2609.10892 DriftNet | yes | yes | **no (BB: text-only)** | yes | overlaps, 3/4 (light) |
| 39 | 2609.06972 AgentDrift | yes | yes | n/a (benchmark) | target only | overlaps (light) |
| 40 | 2610.09935 AgentTracer (IPI) | yes | yes | **no (BB)** | yes (injection-point acc.) | overlaps, 3/4 (light) |
| 41 | 2606.08275 Causal Agent Replay | **no (synthetic SCMs)** | yes | **no (BB)** | yes | overlaps (light) |
| 42 | 2602.22724 AgentSentry | yes | yes | **no (BB)** | **no (ASR)** | overlaps (light) |
| 43 | 2606.23277 GIF | partial | yes | yes (Jacobian) | **no (span flows)** | overlaps (light) |

"Light read": S4 was checked by the abstract plus a full-text search for step-level
scoring, not by reading the methods in full. A light read can only produce "overlaps",
so none of these could have shelved the claim; they are listed so the count is honest.

### The two groups of near-misses

- **Black-box version, run (rows 1–3).** A fault is planted at a chosen step of an
  agent trajectory and LLM judges are scored on finding that step. These miss only S3.
  If black-box methods counted, they would match all four slots.
- **Internals on agents with a planted cause, but not scored on the step (rows 4–7).**
  The planted content sits at a known step, and probes on the agent's own activations
  are scored on detecting it or forecasting the agent's action. These miss only S4.
- **Internals that output a step, but not the agent's internals and not a planted
  step (row 8).** 2610.28811 probes a separate reader model on human-labelled
  Who&When transcripts. It would still miss S2 if the S3 boundary were dropped.

### Per-candidate quotes

**1. 2607.09996 Who&When Pro** (Liu et al.; v1 2026-07-10, v2 2026-10-09)
- S1/S2, §1: "For each successful trajectory, we inject an error at a chosen step and then warm-start execution from that point to generate a failed continuation." §3.3: "The pipeline selects an injection step , constructs an erroneous action , replays to restore the agent's context and the environment state, substitutes for , and lets the original system run from step onward."
- S3 (BB), §4.1: "In All-at-Once, the LLM receives the full trajectory in one prompt and predicts the responsible agent, error step, and failure mode jointly." The other two methods (Step-by-step, Binary-search) are also LLM prompting. No internals terms appear in the paper.
- S4, §4.1: "Step is the accuracy of localizing the first decisive error step. It is scored as exact match against the dataset label."
- Note: the planted cause is an erroneous agent action at step k, not an external input.

**2. 2608.20627 Causal Failure Attribution in Agentic RAG** (Pothuru, Setty, Vidra; v2 2026-11-10)
- S1/S2, §4: "Content corruption instead changes one fact in retrieved documents while preserving topical relevance." Abstract: "The benchmark injects a certified fault at a specified hop, re-executes the downstream trajectory, and evaluates diagnosers against the known intervention site."
- S3 (BB), §4 Diagnosers: "The main comparisons use a coverage-based localizer (Doctor-RAG), a trace-reading LLM judge (LLM-Judge), frozen-hop counterfactual repair (Propagation-Aware), and suffix-regeneration repair (Suf-Regen)."
- S4, §3: "A diagnoser is identifiable at depth when its exact-hop accuracy is measured on failed injected traces whose certified injection depth is".

**3. 2509.03312 AgenTracer** (v2 2025-09-04)
- S2, §4.1: "take a known-good trajectory and programmatically introduce a fault, thereby creating a synthetic failure instance where the decisive error is known by construction."
- S3 (BB), §1: "AgenTracer-8B takes as input the trajectory log and associated environmental feedback, and outputs the identified decisive error step."
- S4, §5.1: step-level accuracy, on Who&When (human labels) and a held-out split of TracerTraj (which mixes injected and counterfactual-replay labels). I did not check how many scored items are injected ones.

**4. 2610.17301 The Agent Knew** (from the v1 read)
- S1/S2, §3.1: "Each task instance comes in two worlds that are identical except for one decisive fact , which first appears in the observation at the reveal".
- S3: linear readout of the agent's residual stream.
- S4: the label read from internals is the "later unauthorized action" (Table 1). The reveal step is known by construction and is never what a method is asked to find.
- The closest substrate to v2: a cause planted at a known step of an agent run, with the agent's internals read. Only the scoring differs.

**5. 2610.24048 The Window Is in the Reasoning** (Jia et al.; 2026-10-16)
- S1/S2, §4: AgentDojo agents; the monitor's judge "sees the user request, the tool output that carries the injection and the tool calls each continuation issues".
- S3, §4 Monitors: "Supervised monitors are TF-IDF classifiers and linear probes on the agent's hidden states (mean over the prefix, optionally de-meaned within each state)".
- S4 no: monitors "return the probability (0–100) that the agent will carry out the instruction". The injection step is the starting point of each branch, not something to localize. Its result on probes: "Hidden-state probes do not read the decision earlier than text."

**6. 2608.02657 IPI exposure in hidden states** (Dong et al.; v2 2026-08-24)
- S1/S2/S3, abstract: "simple linear probes trained on pre-generation hidden states can predict LLMs' IPI exposure", with "malicious side-tasks hidden in external tool results".
- S4 no: the label is binary exposure per detection point. Its related work names injected-span localization work (PromptLocate, Rennervate, PIShield) and says "Most studies focus on single-turn chatbot or direct prompt-injection settings." Those three are leads, not yet read.

**7. 2610.05295 Readable Before Actionable** (from the v1 read)
- The role probe (§4) classifies whether a span's role is instruction or data, on 1,440 controlled prompts with format varied independently of role. It does not pick a step. The AgentDojo part scores attack success under activation edits.

**8. 2610.28811 A Mechanistic Study of Automated Failure Attribution** (Zheng et al.; 2026-10-20)
- S1, §4.1: Who&When transcripts, "an average of 9 steps" (Algo.) and "29 steps" (Craft.).
- S2 no: §2.1 "Each transcript is annotated with the earliest step whose error ultimately causes the system to fail". Who&When (2505.00212 §3): "we conduct multiple rounds of annotation performed by three human experts".
- S3 no on boundary 2: §3.1 "For each transcript, we perform a single forward pass through the frozen LLM and extract hidden representations from every transformer layer". The frozen LLMs are Qwen 2.5 0.5–7B, Llama 3.2 1–3B and Gemma 3 1–4B, reading transcripts that other systems produced.
- S4 yes: "The predicted failing step is the highest-scoring step". Step accuracy: probing reaches 47.62% for Qwen 7B on Algo. against 14.29% for the best prompting baseline.
- The closest internals-based step localization found. It decodes the failing step from a reader model against human labels. v2 asks for the agent's own internals against a planted step.

**9. 2601.15075 The Why Behind the Action** (Qian et al.; v2 2026-02-05)
- S1, §4.1: "All trajectories are generated by Llama-3.1-70B-Instruct (Grattafiori et al., 2024) using the smolagents (Roucher et al., 2025) framework." Eight cases, seven custom-designed.
- S2 no: §4.3 "five human annotators independently annotate the attribution ground truth, identifying the sentences that are most likely to contribute to the model's final action."
- S3 partial: component level uses "the temporal dynamics of the model's likelihood" (output probabilities). One sentence-level baseline, "Saliency Score … based on gradient signals", is white-box.
- S4 partial: Hit@k for sentences inside the chosen component, against human labels.
- Asks the closest question in words ("identify the internal factors driving agent actions"), where "internal factors" means parts of the trajectory, not model internals.

**10. 2608.06909 Long-Horizon Agent Trajectory Attribution** (2026-08-07)
- S2 no, §4.3–4.4: annotation runs through "Benchmark-specific prompt templates", and failed annotations "are repaired through an additional round of LLM-based annotation".
- S3 no, §6: "two representative likelihood-based attribution baselines" (incremental and leave-one-out).
- S4 yes: "Primary attribution localization" ranks trajectory components against the annotated cause.

**11. 2610.25947 Claim Laundering** (2026-10-19)
- S1 partial, abstract: "Agent decision models select actions in a single forward pass from inputs that combine environmental observations with the agent's own record of previous actions." Earlier steps arrive as a record, not as a trajectory of steps.
- S2: "we construct paired states that independently vary the observation, the logged action, and an explicit success claim".
- S3: probes "predict whether the step took effect"; activation patching restores "the share of each input's effect" layer by layer.
- S4 no: the probe output is binary per state, and the patching measures where each input's effect arrives, not whether a method picks the planted input.

**12. 2610.40588 Pre-Crime for Agents** (2026-10-29)
- S1/S3, abstract: "a peer presses a target for up to 20 rounds to reveal a secret … Read at each model call before its output is written, the probe picks out the one that leaks."
- S2 partial: the pressure is constructed but applied every round, not at one chosen step.
- S4 no: it localizes the agent's own leaking call (a forecast of the action), not the step that carried the cause.

**13. 2611.18514 Can MI Help Explain LLM Agent Failures?** (Aghzal, Geva, Stein, Yao; 2026-11-13)
- S1/S3, abstract: Qwen2.5-7B-Instruct "as it interacts with live websites"; "a linear probe trained on the last prompt token can predict hallucinations before generation begins (0.80 AUC)".
- S2 no, §5: "In our case study, for example, nothing indicated which input the agent relied on for a given decision."
- S4 no: patching shows "the action list as a causal contributor", but "even the input span to corrupt is not stable across samples".
- For positioning and for in-flight risk, §5: "no MI benchmarks exist for agent applications. A benchmark for agentic MI must specify not just a task and a model but an environment, a trajectory distribution, and a ground truth for both a trajectory-level failure (as opposed to a surface-level one) and what triggered such failures."

**14. 2602.07918 CausalArmor** (2026-02-08)
- S1/S2: AgentDojo and DoomArena, injections in tool results.
- S3 (BB), §4.1: "we offload the attribution computation to a smaller, efficient proxy model (e.g., Gemma-3-12B-IT)", using leave-one-out likelihood.
- S4 no: scored on attack success rate and utility under attack.

**15. 2603.10749 AttriGuard** (v2 2026-06-10)
- S3 (BB), §4.2: "AttriGuard uses teacher-forced shadow replay … replaces only the observation history with its attenuated view . We then query the same base agent".
- S4 no, §5.1: "Attack Success Rate (ASR) measures the percentage of IPI attacks where the agent successfully fulfills the malicious task".

**16. 2609.06445 Causal Attribution for Agentic Decisions** (2026-09-06)
- S1 no, §5.2: "This is a result about samplers, established on synthetic categorical distributions. It has not been run against a language model."
- S2/S4: estimators are tested on a planted causal chain with an analytically known decisive step.

**17. 2605.17113 The Point of No Return** (Merrill, Srivastava; 2026-05-16)
- S1 no (boundary 1), §3: "we fix each sentence prefix and sample continuations to estimate the probability of a deceptive outcome." The localization is over sentences of one reasoning trace, although the environments are multi-turn games.
- S2 no: commitment junctures are labelled by that resampling, which is another method's output; the deception emerges from incentives and is not planted at a step.
- S3: "Attention features summarize, at each boundary, where the final prefix token attends".
- S4 partial: boundary-level prediction of junctures, scored against resampling labels. Fails S2 regardless of boundary 1.

**18. 2611.10620 What Do Collusion Probes Read?** (from the v1 read)
- S1 unclear: committee deliberation and a vote, "no tools or environment actions".
- S2 no on v2: the §10.2 goal is fine-tuned into the weights and applies to the whole run, not to a chosen step.
- S4 no: presence detection ("both probes separate implanted seats from both controls").

**19. 2610.12445 Telling FIBS** (from the v1 read)
- S2 lenient yes: the side task is in the initial instruction ("the agent is also instructed to complete a hidden side task"), which is step 0, not a chosen step among several.
- S4 no: probes classify transcripts (sabotage vs honest); they do not pick a step.

**20–23 (light reads).** 2606.06223 predicts next-step risk from activations of agents with fine-tuned reward-hack adapters. 2606.30449 tests whether internal readouts predict the next unsafe action. 2611.21799 measures CoT monitorability of a model organism with hidden side tasks (black-box). 2604.01151 detects collusion from per-agent probes (AUROC). None scores a method on picking a planted step; a full-text search for step-level scoring found none.

### Update 2026-11-27: call B reversed by the claim owner

ReCast, all four slots on a methods read: S2, App. C.2: "Who&When Pro constructs each
failed trajectory by injecting a controlled error into a successful execution …
providing causally grounded labels for the responsible agent and decisive step. Our
experiments use all text trajectories". S3: "hidden states extracted by prefilling
trajectories with a frozen LLM". S4, §5: "Table 2 reports the Hit@1 results on AFTraj-2K
and Who&When Pro … exceeding the same baselines by 27.84 and 8.71 points" (the Hit@1
value itself was lost in extraction). ASCon is one of those baselines on Who&When Pro and
needs checking for the same reason.

### Quotes for rows 24–43 (recall D)

- **24. 2605.25310** (Sun, Kazakov; 2026-05-25). §3: "a directed edge is added when a contiguous, case-sensitive, whitespace-normalised character substring … of call 's output occurs verbatim in the serialised JSON arguments of call". Probe on Qwen3-32B residual stream in τ-bench retail. Limits: "the agent's realised tool call does not move under the same intervention." The nearest S2 miss: ground truth is a deterministic oracle over natural runs, which is independent of the method but not planted. **Second-read point.**
- **25. 2607.22610 Tokengeist** (Tang, Barke, Agarwal; v2 2026-11-19). §6.5 matched generator: "the attributing model is the one that produced the assistant turns". §5: "the gold provenance DAGs are themselves LLM-produced".
- **26. 2610.18408** (Kale, Vishwanath; 2026-10-13). Probes "screen the tool outputs an agent reads" on AgentDojo; positives are tool outputs carrying an injection, whether or not it drove a decision.
- **27. 2610.11334 ReCast** (2026-10-08). §3: "hidden states extracted by prefilling trajectories with a frozen LLM"; evaluated on Who&When Pro, whose trajectories come from "GPT-4.1 [87] and Gemini 3 Flash" (2607.09996 App. G.2). The reader's activations cannot be the agent's, which is the case for boundary 2. Its related work names a family of "White-box Failure Attribution Methods" (MASPrism, OAT, others).
- **28. 2604.01194 AgentWatcher** (2026-04-01). "The attribution LLM can be the same LLM as the backend LLM or a separate LLM"; "We use Utility and ASR as evaluation metrics."
- **29. 2608.24022 Attnlocate** (2026-08-25). Attention-based span detection on InjecAgent and MCPTox; "mean IoU of 0.743". Context is one decision with injected tool output or metadata.
- **30. 2508.20412 MindGuard** (v3 2026-01-15). "Attribution Accuracy , defined as the ratio of correctly attributed attacks to the total number of detected attacks"; the planted source is tool metadata, not a trajectory step.
- **31–32. MASPrism, SOAP.** Reader models (Qwen3-0.6B; Qwen3.5-9B and others) on Who&When / TRAIL / TraceElephant / Correct-Error, which are annotated. Label provenance of TraceElephant and Correct-Error not checked.
- **33. 2605.03354.** "Stage labels come from pipeline observables and an LLM judge validated at 79–84% human agreement".
- **34–43 (light: abstract plus a targeted full-text search).** D's abstract quotes are in `recall/D-step-localization.md`. DriftNet "needs no access to the agent's model". AgentTracer (IPI) reports "94.17 percent injection-point accuracy" without internals. These two plus rows 1–3 make up the black-box mirror.

---

## Verdicts against claim C v1 (superseded 2026-11-27)

Methods-level reads, 2026-11-27. Quotes are copied from the arXiv HTML or PDF text of
each paper. Math symbols dropped out during text extraction, which is why some
sentences below have gaps (e.g. "A group of LLM agents, , has to…").

Read so far: 4 of the candidates surfaced by recall (`recall/`). The remaining
candidates have not been read at methods level.

---

### 2611.10620 — What Do Collusion Probes Read? (Mohsin, Rahman; 2026-11-07)

**Verdict: all four slots matched, by §10.2 only. Needs a second read before it counts as "same question".**

| Slot | Matched? | Quote (methods) |
|---|---|---|
| S1 | yes | §3: "A group of LLM agents, , has to reach a single decision together. They discuss it in public for rounds; in each round every agent writes one message, in a fixed order, and sees all earlier messages. The group then votes between two options." |
| S2 | yes, in the weights | §10.2: "We fine-tune two QLoRA adapters (Dettmers et al., 2023) of the agent model on scenario folds 1–4 only. The implanted adapter learns from the replies of colluders who acted, with the brief removed from their context" … "The only difference is the coalition seats' weights: implanted adapter, honest adapter, or the base model." |
| S3 | yes | §3: "For every agent and every round, the monitor sees the public message and the agent's internal activations while it wrote that message (white-box access)." §10.2: "Both probes are trained only on instructed data from folds 1–4." |
| S4 | yes, as detection | §10.2: "both probes separate implanted seats from both controls (Table 6) and meet the pre-registered criterion (AUROC against both controls, lower bounds above 0.5)." Table 6: instruction-level probe 0.995 [0.99, 1.00] against the honest adapter. |

**What it does not do (its own limits, §10.2):**
- One planted goal: "Without a brief, the goal the adapter can learn is "push, with partners, the option the evidence does not support"."
- The goal is acted on in the open: "The implanted seats act on it openly in their votes, and the strictest cut rests on only 133 messages."
- Not ruled out: "a probe could respond to a trace the colluders' replies left in the weights rather than to a goal."
- Scale: "The test covers 10 scenarios and one adapter fold".
- S4 is presence detection (are these seats implanted, yes or no). It does not test whether a method identifies *which* cause was planted, or *at which step* of the discussion it acted.
- The agents deliberate and vote. There are no tools or environment actions.

**Points for the second read:** whether multi-agent deliberation counts as "an LLM agent's decision" for S1, and whether presence detection counts as "recovered the planted cause" for S4. On the claim as written, both read as yes.

---

### 2610.12445 — Telling FIBS (Hollinsworth et al.; 2026-10-08)

**Verdict: overlaps.** S1, S3, S4 are matched in the agentic part, but its cause is an instruction. The cause fine-tuned into the weights is tested outside agent runs.

- Agentic part (§4.3), cause given by instruction: "In the side-task condition the agent is also instructed to complete a hidden side task the user did not ask for; in the honest condition it receives the main task only."
- Part with goals in the weights (§4.4.3), not agentic: "Each organism is fine-tuned to pursue a hidden goal and to deny holding it when asked." It is read on denial transcripts (Appendix L.5), not on agent trajectories. *My reading. Appendices F–H were not read in full.*

---

### 2610.17301 — The Agent Knew (Fayyazi, Kamal, Pedram; 2026-10-12)

**Verdict: overlaps.** S1, S2 (cause given in context) and S3 are matched. S4 differs: it forecasts the agent's later action, not the cause.

- S1/S2, §3.1: "Each task instance comes in two worlds that are identical except for one decisive fact , which first appears in the observation at the reveal ; both worlds share the task, the tools and the sampling seed."
- S4, Table 1: the label read from internals is the "later unauthorized action". The planted fact is known to the experimenters and is not what the readout is scored on.

---

### 2610.05295 — Readable Before Actionable (Yu et al.; 2026-10-04)

**Verdict: overlaps.** S2 (cause injected in context) and S3 are matched. S1 and S4 are measured in different experiments.

- Probes decode which span is the injected instruction, but on controlled prompts. Table 1: "Decode source role — 1,440 prompts/model — Role AUROC".
- The multi-step part (§3: "AgentDojo supplies multi-step tool-use trajectories") measures attack success under activation edits (§6.3). It does not score recovery of the planted cause.

---

### A gap in claim C that these reads exposed

S2 says "put there on purpose (fine-tuning, compiled weights, construction, or
environment design)". That accepts an instruction in the prompt as a planted cause.
FIBS, The Agent Knew, Readable Before Actionable, and the main experiments of
2611.10620 would all match S2 on that reading. The 2611.10620 §10.2 match does
**not** depend on this, because its cause is in the weights. Any revision of claim C
should say whether the cause is in context or in the weights.
