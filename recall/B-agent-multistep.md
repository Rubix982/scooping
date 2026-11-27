# Recall B — agent / multi-step side (S1), run 2026-11-27

## Summary
- I found 25 candidates. Each one comes from a page I opened in this session, and every quote below is copied from that page.
- No single source scanned clearly matches all four slots at abstract level. Several come close, mostly on the "planted cause in an agent, recovered with internals" side: #1–#7.
- Several sources failed:
  - **Semantic Scholar:** the search endpoint returned HTTP 429 every time. Its citations endpoint worked later, so citation hops come from there.
  - **OpenAlex:** citation queries returned 429.
  - **OpenReview:** the API returned a 403 challenge.
  - **NeurIPS 2026 IAB workshop:** its paper list needs a login. The workshop is "Interpreting Agent Behavior", a directly relevant venue.

## Search log
All runs were on 2026-11-27.

arXiv API details: `http://export.arxiv.org/api/query?search_query=<q>&max_results=<n>&sortBy=relevance`, with n=50 unless noted. "Results looked at" is the number returned, capped at n.

| # | Query | Source | Date run | Results looked at | Candidates kept |
|---|---|---|---|---|---|
| 1 | `ti:"say what they think"` (n=20) | arXiv API | 2026-11-27 | 3 | 2505.05410, 2305.04388, 2609.38972 |
| 2 | `ti:"thought anchors"` | arXiv API | 2026-11-27 | 1 | 2506.19143 |
| 3 | `ti:"strategic deception" AND ti:probes` | arXiv API | 2026-11-27 | 1 | 2502.03407 |
| 4 | `ti:SHADE-Arena` | arXiv API | 2026-11-27 | 1 | 2506.15740 |
| 5 | `abs:"SHADE-Arena"` | arXiv API | 2026-11-27 | 13 | 2610.12445 |
| 6 | `abs:"linear probes" AND abs:agent AND abs:deception` | arXiv API | 2026-11-27 | 1 | – (2608.24037 screened) |
| 7 | `abs:probes AND abs:agent AND abs:sabotage` | arXiv API | 2026-11-27 | 3 | 2610.12445 (dup) |
| 8 | `abs:"activation" AND abs:monitor AND abs:agentic AND abs:probe` | arXiv API | 2026-11-27 | 25 | 2611.10620, 2604.01151, 2610.40588, 2610.04575, 2606.04141, 2607.06503, 2605.06890 |
| 9 | `abs:"white-box" AND abs:monitor AND abs:agent` | arXiv API | 2026-11-27 | 14 | dup only |
| 10 | `abs:interpretability AND abs:"LLM agents" AND abs:activations` | arXiv API | 2026-11-27 | 26 | 2611.23403, 2604.19775 |
| 11 | `abs:"sparse autoencoder" AND abs:agent AND abs:"tool"` | arXiv API | 2026-11-27 | 9 | 2604.11061, 2605.06890 |
| 12 | `abs:"ground truth" AND abs:interpretability AND abs:agent AND abs:planted` | arXiv API | 2026-11-27 | 0 | – |
| 13 | `abs:"model organism" AND abs:agent AND abs:interpretability` | arXiv API | 2026-11-27 | 10 | 2604.11061, 2610.10203 |
| 14 | `abs:"hidden objective" AND abs:auditing` | arXiv API | 2026-11-27 | 4 | 2503.10965 |
| 15 | `abs:backdoor AND abs:agent AND abs:interpretability AND abs:activations` | arXiv API | 2026-11-27 | 6 | – |
| 16 | `abs:"implanted" AND abs:interpretability AND abs:"ground truth"` | arXiv API | 2026-11-27 | 3 | – |
| 17 | `abs:"chain of thought" AND abs:"activation patching"` | arXiv API | 2026-11-27 | 14 | 2611.31015, 2605.25310, 2610.30630, 2602.03994, 2609.29875 |
| 18 | `abs:"reasoning trace" AND abs:resampling AND abs:causal` | arXiv API | 2026-11-27 | 1 | 2605.17113 |
| 19 | `abs:planning AND abs:lookahead AND abs:interpretability AND abs:"language model"` | arXiv API | 2026-11-27 | 2 | – |
| 20 | `abs:"multi-turn" AND abs:probe AND abs:deception AND abs:activations` | arXiv API | 2026-11-27 | 2 | 2610.39377, 2606.24251 (screened) |
| 21 | `abs:unverbalized` | arXiv API | 2026-11-27 | 6 | 2611.09945, 2608.29464, 2602.10117, 2607.23458 |
| 22 | `abs:"CoT monitor" AND abs:"reward hacking"` | arXiv API | 2026-11-27 | 11 | 2503.11926 (screened) |
| 23 | `ti:"monitoring reasoning models"` | arXiv API | 2026-11-27 | 1 | dup |
| 24 | `abs:"reward hacking" AND abs:probe AND abs:activations` | arXiv API | 2026-11-27 | 5 | – |
| 25 | `abs:sandbagging AND abs:probe AND abs:agent` | arXiv API | 2026-11-27 | 3 | – |
| 26 | `abs:scheming AND abs:interpretability AND abs:agent` | arXiv API | 2026-11-27 | 50 of 92 (noisy) | – |
| 27 | `abs:"multi-step" AND abs:"mechanistic interpretability" AND abs:agent` | arXiv API | 2026-11-27 | 3 | dup |
| 28 | `abs:"reasoning model" AND abs:"sparse autoencoder" AND abs:steering` | arXiv API | 2026-11-27 | 2 | – |
| 29 | `abs:"agentic" AND abs:"attribution graph"` | arXiv API | 2026-11-27 | 21 | – |
| 30 | `abs:"agent" AND abs:trajectory AND abs:"activation patching"` | arXiv API | 2026-11-27 | 5 | 2610.05295, 2610.25947, 2609.34686 |
| 31 | `abs:"hidden goal" AND abs:agent AND abs:detect` | arXiv API | 2026-11-27 | 4 | 2611.21799 |
| 32 | `ti:agent AND ti:probing` | arXiv API | 2026-11-27 | 50 of 64 | dup |
| 33 | `ti:agents AND ti:interpretability` | arXiv API | 2026-11-27 | 50 of 225 | 2603.20101, 2605.13625 (screened) |
| 34 | `ti:agentic AND ti:interpretability` | arXiv API | 2026-11-27 | 50 of 225 (same set as #33) | – |
| 35 | `ti:agent AND ti:mechanistic` | arXiv API | 2026-11-27 | 21 | 2606.06223, 2611.18514, 2610.28811, 2606.22673, 2605.27935 |
| 36 | `ti:agents AND ti:activations` | arXiv API | 2026-11-27 | 50 of 259 | 2609.37176 (screened) |
| 37 | `abs:"chain of thought" AND abs:hint AND abs:probe` | arXiv API | 2026-11-27 | 12 | 2603.17199, 2611.01620 |
| 38 | `abs:"thought anchors"` | arXiv API | 2026-11-27 | 4 | – |
| 39 | `abs:"model organism" AND abs:"chain of thought"` | arXiv API | 2026-11-27 | 10 | 2611.21799, 2606.12618, 2602.13904 |
| 40 | `abs:"alignment auditing" AND abs:agent` | arXiv API | 2026-11-27 | 5 | 2602.22755 |
| 41 | `abs:"auditing game"` | arXiv API | 2026-11-27 | 11 | 2512.07810 |
| 42 | `abs:planning AND abs:"language model" AND abs:probe AND abs:ahead` | arXiv API | 2026-11-27 | 1 | 2502.06258 (lead check) |
| 43 | `ti:"planning" AND abs:"mechanistic" AND abs:"language model"` | arXiv API | 2026-11-27 | 6 | 2508.18098, 2511.13371 (lead check) |
| 44 | `abs:"backtracking" AND abs:"reasoning model" AND abs:steering` | arXiv API | 2026-11-27 | 5 | – |
| 45 | `abs:"reasoning models" AND abs:"steering vectors"` | arXiv API | 2026-11-27 | 11 | 2608.29070 (screened) |
| 46 | `abs:"chain of thought" AND abs:"causal" AND abs:"interpretability" AND abs:steps AND abs:attribution` | arXiv API | 2026-11-27 | 2 | – |
| 47 | `ti:"Ctrl-Z"` | arXiv API | 2026-11-27 | 3 | 2504.10374 (screened) |
| 48 | `ti:"CoT Red-Handed"` | arXiv API | 2026-11-27 | 1 | – (title only) |
| 49 | `abs:"sleeper agent" AND abs:probe` | arXiv API | 2026-11-27 | 3 | – |
| 50 | `abs:"side task" AND abs:monitor AND abs:"chain of thought"` | arXiv API | 2026-11-27 | 7 | 2608.04735, 2611.07586 (screened) |
| 51 | `abs:backdoor AND abs:"LLM agent" AND abs:detection AND abs:trigger` | arXiv API | 2026-11-27 | 1 | – |
| 52 | `abs:"ground truth" AND abs:"interpretability" AND abs:"agentic"` | arXiv API | 2026-11-27 | 50 of 118 | 2609.19124 (screened) |
| 53 | `abs:"fine-tuned" AND abs:"hidden goal" AND abs:probe` | arXiv API | 2026-11-27 | 1 | – |
| 54 | `abs:"interpretability" AND abs:benchmark AND abs:"known mechanism" AND abs:agent` | arXiv API | 2026-11-27 | 0 | – |
| 55 | `abs:"reasoning trace" AND abs:"interpretability" AND abs:"ground truth" AND abs:"fine-tun"` | arXiv API | 2026-11-27 | 0 | – |
| 56 | `abs:"implanted" AND abs:agent AND abs:behavior AND abs:audit` | arXiv API | 2026-11-27 | 2 | dup |
| 57 | One batch of 5 queries (`ti:"Thought Branches"`; `abs:resampling AND abs:"chain-of-thought" AND abs:interpretability`; `abs:"unfaithful" AND abs:"chain of thought" AND abs:"in the wild"`; `abs:"steganograph" AND abs:"chain of thought" AND abs:probe`; `abs:"evaluation awareness" AND abs:probe AND abs:agent`) | arXiv API | 2026-11-27 | FAILED (HTTP 429). The 1st, 2nd and 5th were rerun as #58–60; the 3rd and 4th were never rerun | – |
| 58 | `ti:"Thought Branches"` (rerun) | arXiv API | 2026-11-27 | 1 | 2510.27484 |
| 59 | `abs:resampling AND abs:"chain-of-thought" AND abs:interpretability` | arXiv API | 2026-11-27 | 5 | dup |
| 60 | `abs:"evaluation awareness" AND abs:probe AND abs:agent` | arXiv API | 2026-11-27 | 1 | – |
| 61 | `abs:"prompt injection" AND abs:"activation patching"` | arXiv API | 2026-11-27 | 3 | 2609.37737 (screened) |
| 62 | `abs:"agentic misalignment" AND abs:interpretability` | arXiv API | 2026-11-27 | 2 | dup |
| 63 | `abs:"agent" AND abs:"goal" AND abs:"linear probe" AND abs:"language model" AND abs:"plan"` | arXiv API | 2026-11-27 | 0 | – |
| 64 | `abs:blackmail AND abs:agent AND abs:"chain of thought"` | arXiv API | 2026-11-27 | 2 | dup |
| 65 | `abs:backdoor AND abs:"tool" AND abs:agent AND abs:probe` | arXiv API | 2026-11-27 | 3 | – |
| 66 | `abs:"multi-turn" AND abs:"interpretability" AND abs:"steering" AND abs:agent` | arXiv API | 2026-11-27 | 2 | dup |
| 67 | `abs:"reasoning trace" AND abs:"sparse autoencoder" AND abs:agent` | arXiv API | 2026-11-27 | 0 | – |
| 68 | `abs:"monitor" AND abs:"activations" AND abs:"long-horizon"` | arXiv API | 2026-11-27 | 21 | dup |
| 69 | `ti:AgenTracer` (n=30) | arXiv API | 2026-11-27 | 1 | 2509.03312 |
| 70 | `abs:"failure attribution" AND abs:agent AND abs:inject` (n=30) | arXiv API | 2026-11-27 | 6 | 2607.09996, 2608.20627 |
| 71 | `ti:"Which Agent Causes Task Failures"` (n=30) | arXiv API | 2026-11-27 | 1 | – (title only) |
| 72 | `abs:"fault injection" AND abs:"multi-agent" AND abs:attribution` (n=30) | arXiv API | 2026-11-27 | 4 | dup |
| 73 | `abs:"failure attribution" AND abs:probe` (n=30) | arXiv API | 2026-11-27 | 7 | dup |
| 74 | `abs:"injected" AND abs:agent AND abs:"activation patching"` (n=30) | arXiv API | 2026-11-27 | 2 | dup |
| 75 | `abs:"known" AND abs:"injected" AND abs:"interpretability" AND abs:"reasoning"` (n=30) | arXiv API | 2026-11-27 | 2 | – |
| 76 | `abs:"hidden objective" AND abs:"activation"` (n=30) | arXiv API | 2026-11-27 | 10 | 2606.09563 |
| 77 | 11 relevance searches, e.g. "mechanistic interpretability LLM agents multi-step trajectory", "interpretability planted ground truth agent behavior recovery", "chain-of-thought faithfulness planted hint reasoning model verbalize", "activation probes monitor agent sabotage deception trajectory", "resampling reasoning trace counterfactual importance sentences", "model organism hidden goal agent detection interpretability", "planning lookahead language model internal representation" | Semantic Scholar /paper/search | 2026-11-27 | FAILED (HTTP 429 on every attempt) | – |
| 78 | Citations of arXiv:2510.27484 (Thought Branches) | Semantic Scholar /citations | 2026-11-27 | 15 (all read) | 2610.24048, 2608.02657, 2603.05488 |
| 79 | Citations of arXiv:2506.19143 (Thought Anchors) | Semantic Scholar /citations | 2026-11-27 | 168, title-filtered to ~45 | 2605.25052, 2611.05650, 2610.17444, 2610.25760, 2608.27348, 2606.21821, 2603.04069 |
| 80 | Citations of arXiv:2604.11061 (Pando) | Semantic Scholar /citations | 2026-11-27 | 3 | 2610.10203, 2610.18727 (screened) |
| 81 | Citations of arXiv:2502.03407 (deception probes) | Semantic Scholar /citations | 2026-11-27 | 87, title-filtered to ~20 | 2504.04072, 2511.06626 |
| 82 | Citations of arXiv:2505.05410 (Reasoning models don't always say) | Semantic Scholar /citations | 2026-11-27 | 598, title-filtered to ~30 | 2610.17301, 2606.17478, 2610.24613 |
| 83 | Citations of arXiv:2610.12445 (FIBS) | Semantic Scholar /citations | 2026-11-27 | 1 | 2611.10620 (dup) |
| 84 | Citations of arXiv:2506.15740 (SHADE-Arena) | Semantic Scholar /citations | 2026-11-27 | 95, title-filtered to 3 | – |
| 85 | DOI lookups for 5 seed papers; `filter=cites:` for 4 seeds | OpenAlex | 2026-11-27 | Lookups OK; cites queries FAILED (429) | – |
| 86 | `interpretability LLM agent planted ground truth probes multi-step trajectory alignmentforum OR lesswrong` | WebSearch | 2026-11-27 | 10 | 2602.08964, NeurIPS "Causal Probes" poster |
| 87 | `"model organism" agent hidden behavior interpretability detect multi-turn trajectory 2026` | WebSearch | 2026-11-27 | 10 | 2602.22755, 2510.13900, 2605.06846, 2602.22303 (screened) |
| 88 | `"Thought Branches" interpreting LLM reasoning requires resampling` | WebSearch | 2026-11-27 | 10 | 2510.27484 |
| 89 | `lesswrong interpretability agentic trajectories white-box probes coding agent sabotage ground truth` | WebSearch | 2026-11-27 | 10 | LW posts by H. Tatsat (screened) |
| 90 | `alignmentforum "model organism" agent "interpretability" recover planted behavior multi-turn agentic environment probes SAE` | WebSearch | 2026-11-27 | 10 | led to #91 |
| 91 | `alignment.anthropic.com 2026 auditing saboteur model organism sabotage` | WebSearch | 2026-11-27 | 10 | Anthropic "overt saboteur" post |
| 92 | `site:lesswrong.com probes agentic model organism trajectory "white-box" sabotage detection results` | WebSearch | 2026-11-27 | 10 | 2509.21344, 2512.07810, 2604.16286, 2 LW posts |
| 93 | `benchmark interpretability methods agent decisions known ground-truth cause fine-tuned "multi-step" recover cause SAE attribution 2026 arxiv` (extended) | WebSearch | 2026-11-27 | 10 | 2609.06445, 2608.06909 |
| 94 | `probes detect reward hacking coding agent activations model organism trained to reward hack arxiv 2025 2026` | WebSearch | 2026-11-27 | 10 | 2602.15515, 2610.03055, 2611.14996, 2604.01476, 2610.29129 (screened) |
| 95 | `"chain-of-thought" faithfulness agentic tasks hint tool output planted cue verbalization multi-step agent 2026 arxiv` | WebSearch | 2026-11-27 | 10 | 2608.29464 (dup) |
| 96 | `site:lesswrong.com interpretability "reasoning model" planted hint probe unverbalized cue detection activations` | WebSearch | 2026-11-27 | 10 | LW OLMo-3 hint post, 2603.01437, 2601.07663 (screened) |
| 97 | `site:alignmentforum.org agent interpretability trajectory steering probes "multi-turn" decision` | WebSearch | 2026-11-27 | 10 | 2606.30449, 2610.27295 |
| 98 | `attribution graphs OR transcoders OR circuit tracing applied to LLM agent multi-turn tool-use decision trajectory 2026` | WebSearch | 2026-11-27 | 10 | 2606.28548, 2605.25603 (screened) |
| 99 | `"model organism" fine-tuned agent hidden side task interpretability probes SAE recover objective agentic environment evaluation 2026 lesswrong OR arxiv` | WebSearch | 2026-11-27 | 10 | nothing new |
| 100 | Direct opens: neurips.cc/virtual/2026/168989 (abstract text); neurips.cc/virtual/2026/workshop/137495 (no paper list); OpenReview API id=eOxoW6FSoV (403); alignment.anthropic.com/2026/auditing-overt-saboteur/; LessWrong GraphQL for 6 post IDs; Aghzal et al. project page (WebFetch only) | Direct fetch | 2026-11-27 | – | listed items |

## Candidates (closest to the four slots first, 25 total)

**1. What Do Collusion Probes Read? Three Pitfalls in Evaluating Multi-Agent Collusion Monitors** — Mainul Hasan Mohsin, Mohammad Shahidur Rahman (org not checked) — 2026-11-07 — https://arxiv.org/abs/2611.10620
  Quote: "We show that they mostly detect that an agent was told to collude, not that it decided to." / "The decision is still there: a probe trained on agents' own choices reads it (AUROC 0.73 without the instruction), and probes find colluders whose goal was fine-tuned into the weights (AUROC 0.995; pre-registered)."
  Slots touched (abstract-level, unverified): S1 (multi-agent committee/code-review episodes), S2 (goal fine-tuned into weights; refuser controls), S3 (probes), S4 (detect colluder)
  Uses internals? yes
  Why kept: a fine-tuned goal driving a multi-turn agent decision, with probes scored on recovering it.

**2. Telling FIBS: Probes Effectively Detect Sabotage and Catch Unverbalized Deception** — Oskar J. Hollinsworth, Alex F. Spies, Tigist Diriba, Adam Gleave, Chris Cundy (org not checked) — 2026-10-08 — https://arxiv.org/abs/2610.12445
  Quote: "Our probes surpass black-box monitors on agentic coding benchmarks, achieving 98.3% AUROC in SHADE-Arena and 98.0% in BashArena (vs. 97.7%, 97.6% resp. for action-only text monitors), and show improved efficacy as the underlying model is scaled up." / "In one such evaluation, we show that probes can distinguish transcripts containing a model's true hidden goal from other goals with an AUROC of up to 99.7%."
  Slots touched (abstract-level, unverified): S1 (agentic sabotage trajectories), S2 (side tasks; a hidden goal known "through ... knowledge of a model's training data"), S3 (probes), S4
  Uses internals? yes
  Why kept: probes recovering a known hidden goal in multi-step agent settings.

**3. From Reward-Hack Activations to Agentic Risk States: Context-Calibrated Mechanistic Monitoring in LLM Agents** — Patrick Wilhelm, Odej Kao (org not checked) — 2026-06-04 — https://arxiv.org/abs/2606.06223
  Quote: "We find that adapters fine-tuned on \textit{School-of-Reward-Hacks} dataset can transfer reward-hack tendencies into agentic action selection, especially when the environment exposes proxy-reward affordances." / "High reward-hack activation identifies a latent policy state, but does not necessarily imply an immediate exploit action."
  Slots touched (abstract-level, unverified): S1 (ReAct agents in ALFWorld/WebShop), S2 (fine-tuned adapters, gameable environment), S3 (activation scores, steering), S4 (partial: next-step risk prediction)
  Uses internals? yes
  Why kept: a fine-tuned tendency planted in multi-step agents, monitored through activations.

**4. Readable Before Actionable: Causal Tracing of Indirect Prompt Injection** — Zhe Yu, Wenpeng Xing, Xingxing Yang, Meng Han (org not checked) — 2026-10-04 — https://arxiv.org/abs/2610.05295
  Quote: "We study this gap through counterfactual role probes, component-wise activation patching, and separate interventions on AgentDojo trajectories." / "These findings distinguish a readable role signal from an effective behavioral intervention: depth matters in controlled tool choice, while position and context also matter in attack trajectories."
  Slots touched (abstract-level, unverified): S1 (AgentDojo trajectories), S2 (injected span, known by construction), S3 (probes, patching), S4 (partial)
  Uses internals? yes
  Why kept: an environment-planted cause traced with internals across agent trajectories.

**5. The Agent Knew: Internal States Forecast Unauthorized Actions and Stop Them, and the Lies That Follow** — Arya Fayyazi, Mehdi Kamal, Massoud Pedram (org not checked) — 2026-10-12 — https://arxiv.org/abs/2610.17301
  Quote: "On CAPE-Bench, matched agent tasks in which one fact decides whether an action is authorized, frontier open-weight agents do both, and one behavior marks the lie" / "A linear readout of the agent's residual stream forecasts the violation before the action (AUROC 0.94) and the false report before the report, and beats chain-of-thought monitors when the agent is pressured to hide its reasoning."
  Slots touched (abstract-level, unverified): S1 (whole episodes), S2 (a constructed deciding fact), S3 (residual readout, steering), S4 (forecast vs CoT monitor)
  Uses internals? yes
  Why kept: matched tasks with a planted deciding fact, residual-stream readout of the decision, preregistered.

**6. Internal-State Probes Read the Situation, Not the Action: Three Negative Results for Pre-Action Misalignment Monitoring** — Max Fomin, Elad David, Amit LeVi (org not checked) — 2026-06-29 — https://arxiv.org/abs/2606.30449
  Quote: "Probes on model internals could help monitor agentic systems if they identify harmful text or tool actions before those actions are generated." / "The Qwen direction separates fine-tune from base at AUC 1.000, yet crosses its threshold on 0/143 audited pre-assistant turn contexts and on 0/342 Qwen prefill rows where the model continues the unsafe trajectory."
  Slots touched (abstract-level, unverified): S1 (blackmail tool-action scenario, trajectories), S2 (fine-tune vs base), S3 (probes, concept vectors, steering), S4 (whether the readout predicts the action)
  Uses internals? yes
  Why kept: negative results on whether internal readouts recover what drives an agent's next action.

**7. Can Latent Reasoning Drive LLM Outputs Without a Trace?** — Tomer Ashuach, Zorik Gekhman, Avi Caciularu, Ori Ram, Jonathan Herzig (org not checked) — 2026-11-23 — https://arxiv.org/abs/2611.31015
  Quote: "Then, in two common tasks, decision-making and code generation, we train a model to pursue such a hidden objective, which decides a loan or plants a vulnerability. The model's CoT justifies the output with no trace of the hidden objective, and a strong LLM monitor does not flag it. Finally, using activation patching, we find that the latent computation is completed before the model generates its CoT, which takes no part in it."
  Slots touched (abstract-level, unverified): S1 (partial: a multi-step latent computation plus CoT, not an agent), S2 (trained hidden objective), S3 (activation patching), S4 (monitor fails to recover it)
  Uses internals? yes
  Why kept: a planted hidden objective in a reasoning model, tested with both a CoT monitor and patching.

**8. Pando: Do Interpretability Methods Work When Models Won't Explain Themselves?** — Ziqian Zhong, Aashiq Muhamed, Mona T. Diab, Virginia Smith, Aditi Raghunathan (org not checked) — 2026-04-13 — https://arxiv.org/abs/2604.11061
  Quote: "We introduce Pando, a model-organism benchmark that breaks this confound via an explanation axis: models are trained to produce either faithful explanations of the true rule, no explanation, or confident but unfaithful explanations of a disjoint distractor rule." / "when explanations are absent or misleading, gradient-based attribution improves accuracy by 3-5 percentage points, and relevance patching, RelP, gives the largest gains, while logit lens, sparse autoencoders, and circuit tracing provide no reliable benefit."
  Slots touched (abstract-level, unverified): S2, S3, S4 strongly; S1 not suggested (single decision over input fields)
  Uses internals? yes
  Why kept: the closest planted-ground-truth interpretability benchmark found; it lacks the multi-step slot.

**9. A Model Organism for Studying Unverbalized Evaluation Awareness** — Daniel Donnelly, Evan Chapple, Haritz Puerto, Sahar Abdelnabi (org not checked) — 2026-10-16 — https://arxiv.org/abs/2611.09945
  Quote: "Using synthetic document fine-tuning, SFT, and DPO, we train Qwen3.5-27B to emit a marker (a designated token) in its final response when it recognizes an evaluation, while suppressing the marker and verbalized awareness in its reasoning." / "Using the marker as a label, we benchmark linear probes, the Jacobian Lens, and Activation Oracles, built on the base model and blind to the marker. None recovers the label reliably."
  Slots touched (abstract-level, unverified): S2, S3, S4; S1 partial (reasoning model, not an agent trajectory)
  Uses internals? yes
  Why kept: an instance-level planted label in a reasoning model, used to score interpretability methods.

**10. Thought Branches: Interpreting LLM Reasoning Requires Resampling** — Uzay Macar, Paul C. Bogdan, Senthooran Rajamanoharan, Neel Nanda (org not checked) — 2025-10-31 — https://arxiv.org/abs/2510.27484
  Quote: "First, when a model states a reason for its action, does that reason actually cause the action? In "agentic misalignment" scenarios, we find that self-preservation sentences have small causal impact, suggesting they do not meaningfully drive blackmail." / "Adapting causal mediation analysis, we find that hints that causally affect the output without being explicitly mentioned exert a subtle and cumulative influence on the CoT that persists even if the hint is removed."
  Slots touched (abstract-level, unverified): S1 (agentic-misalignment decisions over reasoning traces), S2 (planted hints), S3 (resampling, which is black-box), S4 (partial)
  Uses internals? no (resampling); unclear for the mediation part
  Why kept: a resampling-based causal method on agentic decisions plus planted hints. Follow-up to the Thought Anchors lead.

**11. The Window Is in the Reasoning: When LLM Agents Decide to Follow Prompt Injections** — Haoxuan Jia, Yang Liu, Bin Chong, Yingguang Yang, Yancheng Chen, Jiayu Liang et al. (org not checked) — 2026-10-16 — https://arxiv.org/abs/2610.24048
  Quote: "We test this assumption with branching rollouts that replay an episode exactly up to the step at which the agent reads an injection and then resample the rest of the episode many times, splitting the outcome variance into a part fixed at read time and a part decided afterwards." / "Zero-shot chain-of-thought monitors built on cheaper models miss much of what is already decided, whereas stronger monitors, and a lookahead monitor that judges simulated next actions, come close to what the prefix determines."
  Slots touched (abstract-level, unverified): S1, S2 (injection), S4 (monitors vs resampled ground truth); S3 not suggested
  Uses internals? no
  Why kept: a planted cause in multi-step agent episodes, with black-box monitors scored against it.

**12. Your Agentic LLMs Secretly Encode Indirect Prompt-Injection Exposure in Hidden States** — Jianshuo Dong, Yiming Liu, Maosen Zhang, Nan Deng, Peng Xu, Xiaoping Zhang et al. (org not checked) — 2026-08-01 — https://arxiv.org/abs/2608.02657
  Quote: "(1) Probing: Across eight models, including the 753B-parameter GLM-5.2 and the 2.8T-parameter Kimi-K3, simple linear probes trained on pre-generation hidden states can predict LLMs' IPI exposure." / "post-trained LLMs encode signals predictive of IPI exposure, yet do not reliably bind these signals to safe agentic actions."
  Slots touched (abstract-level, unverified): S1 (agentic, AgentDojo), S2 (injected side-tasks in tool results), S3 (probes), S4 (detect exposure)
  Uses internals? yes
  Why kept: probes recovering an environment-planted cause in agents.

**13. Making LLMs Say What They Think: Measuring and Improving CoT-Interpretability Alignment** — Yihuai Hong, Shauli Ravfogel, Chen Zhao, Eunsol Choi (org not checked) — 2026-09-30 — https://arxiv.org/abs/2609.38972
  Quote: "We propose CoT-Interpretability Alignment (CIA), a metric that measures the agreement between a model's CoT traces and its internal reasoning strategies as detected by interpretability tools. We evaluate CIA on three tasks (two-hop question answering, hint intervention, and integer multiplication) across three LLMs, finding that LLMs exhibit limited alignment across all tasks (44.8-75.9%)."
  Slots touched (abstract-level, unverified): S1 partial (CoT), S2 (hint intervention), S3, S4 partial
  Uses internals? yes
  Why kept: interpretability tools set against CoT on planted hints.

**14. Catching rationalization in the act: detecting motivated reasoning before and after CoT via activation probing** — Parsa Mirtaheri, Mikhail Belkin (org not checked) — 2026-03-17 — https://arxiv.org/abs/2603.17199
  Quote: "In multiple-choice settings with an injected hint favoring a particular option, models may shift their final answer toward the hinted option and produce a CoT that rationalizes the response without acknowledging the hint - an instance of motivated reasoning." / "(i) pre-generation probes, applied before any CoT tokens are generated, predict motivated reasoning as well as a LLM-based CoT monitor that accesses the full CoT trace, and (ii) post-generation probes, applied after CoT generation, outperform the same monitor."
  Slots touched (abstract-level, unverified): S1 partial (single-turn CoT), S2 (injected hint), S3 (probes), S4 (probe vs CoT monitor)
  Uses internals? yes
  Why kept: a planted cause, probes against a CoT monitor; not agentic.

**15. The Point of No Return: Counterfactual Localization of Deceptive Commitment in Language-Model Reasoning** — Scott Merrill, Shashank Srivastava (org not checked) — 2026-05-16 — https://arxiv.org/abs/2605.17113
  Quote: "We introduce counterfactual localization: for each sentence prefix in a reasoning trace, we fix the prefix, resample continuations, and estimate the probability of a deceptive outcome." / "we construct five environments (spanning strategic bluffing, maze guidance, financial advice, used-car sales, and offer negotiation) in which deception is never prompted but emerges from strategic incentives and labels follow mechanically from environment state rather than subjective human judgment."
  Slots touched (abstract-level, unverified): S1 (decision over reasoning trajectory), S2 partial (environment-designed incentives, mechanical labels), S3 (attention-head sets that causally suppress), S4 partial
  Uses internals? yes (attention heads); localization itself is resampling
  Why kept: environment-designed ground truth combined with step-level localization and head interventions.

**16. When Failures Propagate: Causal Failure Attribution in Agentic Retrieval-Augmented Generation** — Lauren Pothuru, Spurthi Setty, Natan Vidra (org not checked) — 2026-08-20 — https://arxiv.org/abs/2608.20627
  Quote: "The benchmark injects a certified fault at a specified hop, re-executes the downstream trajectory, and evaluates diagnosers against the known intervention site. Its central question is whether a post-hoc trace still identifies the injected hop after the suffix changes."
  Slots touched (abstract-level, unverified): S1, S2, S4; S3 not suggested (LLM judge, coverage, repair)
  Uses internals? no
  Why kept: the black-box mirror of the claim (planted fault, multi-hop, scored recovery).

**17. Causal Attribution for Agentic Decisions: Estimators, Coupling, and a Traceability Specification** — Ajay Pravin Mahale (org not checked) — 2026-09-06 — https://arxiv.org/abs/2609.06445
  Quote: "Under the marginal estimand a causally inert step has the identical total effect to the decisive one on every run of our planted chain, an algebraic identity and not a coincidence at one draw."
  Slots touched (abstract-level, unverified): S1, S2 (planted chain), S4 (estimator recovery); S3 not suggested
  Uses internals? no
  Why kept: a planted causal chain in agentic decisions used to test attribution estimators.

**18. Who&When Pro: Can LLMs Really Attribute Failures in AI Agents?** — Jiale Liu, Huajun Xi, Shaokun Zhang, Yifan Zeng, Tianwei Yue, Chi Wang et al. (org not checked) — 2026-07-10 — https://arxiv.org/abs/2607.09996
  Quote: "Using a strictly controlled pipeline that injects a failure only after exactly replaying a successful prefix, we construct 12,326 failed trajectories with golden labels across 3 modalities and 26 benchmarks covering various scenarios."
  Slots touched (abstract-level, unverified): S1, S2, S4; S3 not suggested
  Uses internals? no
  Why kept: a large benchmark of agent trajectories with injected, known failure steps. The attributors are LLMs.

**19. Reasoning Models Don't Always Say What They Think** — Yanda Chen, Joe Benton, Ansh Radhakrishnan, Jonathan Uesato, Carson Denison, John Schulman et al. (org not verified) — 2025-05-08 — https://arxiv.org/abs/2505.05410
  Quote: "We evaluate CoT faithfulness of state-of-the-art reasoning models across 6 reasoning hints presented in the prompts and find: (1) for most settings and models tested, CoTs reveal their usage of hints in at least 1% of examples where they use the hint, but the reveal rate is often below 20%" / "(3) when reinforcement learning increases how frequently hints are used (reward hacking), the propensity to verbalize them does not increase, even without training against a CoT monitor."
  Slots touched (abstract-level, unverified): S1 partial (reasoning traces; RL environments), S2 (planted hints), S4 (CoT verbalization as the recovery method)
  Uses internals? no
  Why kept: lead; the canonical planted-hint CoT-faithfulness test.

**20. Causal Probes for Interpreting Agent Behavior** — Mohammadreza Sediqin, Zahra Fatemi — NeurIPS 2026 IAB workshop poster (session 2026-12-12; posting date not shown) — https://neurips.cc/virtual/2026/168989 (OpenReview forum eOxoW6FSoV; not opened, 403)
  Quote: "Checkpoint resumption rebuilds the model's context at a stored reasoning block, substitutes the reasoning, and samples only the next action, so a counterfactual at one step of a long-horizon run costs a single completion rather than a full re-execution." / "so inspection alone cannot determine which parts of a reasoning chain steer behavior."
  Slots touched (abstract-level, unverified): S1 (long-horizon agent runs, 324 trajectories), S2 partial (substituted reasoning known by construction), S4 partial
  Uses internals? no (interventions on reasoning text)
  Why kept: step-level causal interventions on agent trajectories. Comes from the workshop I could not enumerate.

**21. Chain-of-Thought Faithfulness of Reasoning Models Varies with Where and How Preference Cues Are Delivered** — Aryo Pradipta Gema, Neel Rajani, Rohit Saxena, Wai-Chung Kwan, Pasquale Minervini (org not checked) — 2026-08-29 — https://arxiv.org/abs/2608.29464
  Quote: "Existing faithfulness tests often place explicit bias cues in the user message, while agents may encounter preferences through tool returns or raw artifacts. We introduce FACE-Eval (Faithful Attribution of Cue Effects Evaluation), a 5,100-sample evaluation that varies cue location (user message or tool return) and explicitness (direct summary or raw artifact)." / "within the single-call, prefilled-tool setting tested here."
  Slots touched (abstract-level, unverified): S1 weak (tool-return channel, single call), S2 (planted cues), S4 (verbalization, transcript monitors)
  Uses internals? no
  Why kept: planted cues delivered through the agent's tool channel.

**22. SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents** — Jonathan Kutasov, Yuqi Sun, Paul Colognese, Teun van der Weij, Linda Petrini, Chen Bo Calvin Zhang et al. (org not checked) — 2025-06-17 — https://arxiv.org/abs/2506.15740
  Quote: "SHADE-Arena consists of complex pairs of benign main tasks and harmful side objectives in complicated environments. Agents are evaluated on their ability to complete the side task without appearing suspicious to an LLM monitor."
  Slots touched (abstract-level, unverified): S1, S2 (assigned side objective), S4 (monitor AUC); S3 not suggested
  Uses internals? no
  Why kept: lead; the substrate that #2 used for probes.

**23. Detecting Strategic Deception Using Linear Probes** — Nicholas Goldowsky-Dill, Bilal Chughtai, Stefan Heimersheim, Marius Hobbhahn (Apollo Research, per code links in the abstract) — 2025-02-05 — https://arxiv.org/abs/2502.03407
  Quote: "We test whether these probes generalize to realistic settings where Llama-3.3-70B-Instruct behaves deceptively, such as concealing insider trading (Scheurer et al., 2023) and purposely underperforming on safety evaluations (Benton et al., 2024). We find that our probe distinguishes honest and deceptive responses with AUROCs between 0.96 and 0.999 on our evaluation datasets."
  Slots touched (abstract-level, unverified): S1 partial (the insider-trading scenario is agentic), S3, S4; S2 unclear (deception is elicited by the scenario, not trained in)
  Uses internals? yes
  Why kept: lead.

**24. Thought Anchors: Which LLM Reasoning Steps Matter?** — Paul C. Bogdan, Uzay Macar, Neel Nanda, Arthur Conmy (org not checked) — 2025-06-23 — https://arxiv.org/abs/2506.19143
  Quote: "We introduce a black-box method that measures each sentence's counterfactual importance by repeatedly sampling replacement sentences from the model, filtering for semantically different ones, and continuing the chain of thought from that point onwards to quantify the sentence's impact on the distribution of final answers."
  Slots touched (abstract-level, unverified): S1 (multi-step reasoning trace), S3 partial (attention heads); no planted cause suggested
  Uses internals? partly (attention-head analysis alongside black-box resampling)
  Why kept: lead; the step-attribution method used by #10 and #15.

**25. Pre-deployment auditing can catch an overt saboteur** — Johannes Treutlein, Samuel R. Bowman, Trenton Bricken, Alex Cloud, Misha Wagner, Rowan Wang, Evan Hubinger, Fabien Roger, Sam Marks (Anthropic Alignment Science Blog) — 2026-01-28 — https://alignment.anthropic.com/2026/auditing-overt-saboteur/
  Quote (tl;dr, since a blog post has no abstract): "We test whether our production pre-deployment alignment auditing methods can catch overt saboteurs: models trained to sabotage Anthropic but not to conceal this behavior. A human working together with an automated auditing agent successfully identified three overt sabotage agents, without flagging two benign models."
  Slots touched (abstract-level, unverified): S1 (Claude Code-style agentic transcripts), S2 (sabotage trained in by SFT), S4 (audit recovers it); I found no interpretability mention on the page
  Uses internals? no (page text has no mention of interpretability, probes or SAEs)
  Why kept: a planted cause in an agent, recovered by a blind audit.

**Other items opened and screened.** These ranked below the cutoff. Abstracts were fetched; tags are abstract-level and unverified.
- 2611.21799 Controllable CoTs Can Reveal Less: model organism with hidden side tasks in agentic environments, CoT monitorability (S1, S2, S4; black-box).
- 2610.25947 Claim Laundering: constructed paired states and injected silent failures; probes and patching in agent decision models (S1, S2, S3).
- 2606.09563 PRISM: decodes instruction sets, including hidden objectives and prompt injection, from activations (S2, S3, S4).
- 2602.22755 AuditBench and 2503.10965 Auditing LMs for hidden objectives: implanted behaviors; white-box and black-box tools; target models are not agents (S2, S3, S4).
- 2512.07810 Auditing Games for Sandbagging: planted sandbagging, probes (S2, S3, S4).
- 2603.04069 Monitoring emergent reward hacking via activations: fine-tuned reward hacking, SAE probes during CoT (S2, S3).
- 2610.30630 Behavioral counterfactuals: unacknowledged suggestion; residual edits and attribution (S2, S3).
- 2604.01151 HELIOS/NARCBench: multi-agent collusion probes, instructed collusion (S1, S2, S3, S4).
- 2610.40588 Pre-Crime for Agents: per-call probe across up to 20 rounds (S1, S3, S4).
- 2504.04072 Among Us: agentic deception; probes and SAEs (S1, S3).
- 2509.03312 AgenTracer: programmed fault injection; black-box tracer (S1, S2, S4).
- 2608.06909 Trajectory attribution benchmark (S1, S4).
- 2611.05650 Executed-counterfactual reporting standard (S1).
- 2610.28811 Mechanistic study of automated failure attribution, with probes on the judge model (S1, S3).
- Agent-internals work without a planted cause (S1, S3): 2605.25310, 2611.18514, 2605.06890, 2610.17444, 2602.08964, 2605.27935, 2606.22673, 2609.34686, 2610.03055, 2611.14996, 2604.19775.
- 2611.01620 and 2605.25052 (BonaFide): ground-truth faithfulness labels (S2, S4).
- 2608.04735: implicit nudges, CoT monitor (S2, S4).
- 2602.15515 Obfuscation Atlas (S2 via environment, S3).
- 2606.12618 "Did you lie?" (S2, S3, S4).
- 2509.21344: probes rely on textual evidence (S2, S3).
- 2305.04388 Turpin et al., lead (S2, S4; black-box, single-turn).
- LessWrong posts:
  - "Another Slice of Swiss Cheese for Untrusted Monitoring" (2026-09-14): probe on a collusion model organism (S2, S3, S4).
  - "What Happens When a Collusion Probe Only Finds a Thin Signal?" (2026-07-26; S1, S3).
  - "Where does hint-following and concealment arise? OLMo-3" (2026-07-24; S2, S4).

## Leads: resolution
- "Reasoning models don't always say what they think" resolved to 2505.05410 (#19).
- "Language models don't always say what they think" resolved to 2305.04388. Opened; it is in the screened list.
- "Thought anchors" resolved to 2506.19143 (#24). Its follow-up 2510.27484 is #10.
- "Detecting strategic deception using linear probes" resolved to 2502.03407 (#23).
- SHADE-Arena resolved to 2506.15740 (#22).
- Planning/lookahead: opened 2502.06258, 2508.18098, 2511.13371 and 2605.27935. None involves a planted cause in a multi-step agent.
- Probes/monitors in agents and activation monitoring of trajectories: covered by #1–6, #12 and the screened list.

## Leads that did not resolve
None of the given leads failed to resolve. These items surfaced but I did not open them, or could not get a verbatim abstract:
- "Toward Mechanistic Interpretability of LLM Agents: Explaining Trajectories Demands New Methods" (Aghzal, Geva, Stein, Yao). I opened the project page through WebFetch only, so I could not extract a verbatim abstract. It may be the same work as 2611.18514; not verified.
- Titles seen in search results only, not opened:
  - CoT Red-Handed (2505.23575)
  - Who&When (2505.00212)
  - 2601.21112
  - Hodoscope (2604.11072)
  - 2602.08877
  - 2605.06840
  - 2608.00218
  - 2605.03354
  - 2505.14300
  - 2610.33011
  - 2508.05625
  - Anthropic "probes catch sleeper agents" post
  - The intentionallydense.github.io blog on hint-influence probes
  - The SPAR Fall 2026 project page

## Gaps: sources I could not search, and why
- **Semantic Scholar relevance search:** every attempt (11 queries) returned HTTP 429, so there is no keyword-relevance sweep from S2. Only the citations endpoint worked, later in the session.
- **OpenAlex citation filters:** HTTP 429. DOI lookups worked.
- **OpenReview:** the API answered with a 403 challenge. Submissions that exist only on OpenReview (workshop papers, ICLR 2027 submissions) were not searched.
- **NeurIPS 2026 "Interpreting Agent Behavior" workshop:** the accepted-paper list needs a login. I found only one poster from it, via WebSearch. This is the biggest blind spot for slot S1.
- **LessWrong / Alignment Forum:** no native search. I covered them through WebSearch `site:` queries and GraphQL lookups by post ID only.
- **arXiv:** one batch of 5 queries was rate-limited; 3 were rerun, and the "unfaithful … in the wild" and "steganograph … probe" queries were never rerun. arXiv field search is lexical, so papers using different vocabulary would be missed. There was no full-text search.
- **Citation-hop depth:** hops ran on 7 seed papers only. The large citer lists (598, 168, 95, 87 papers) were filtered by title keywords, not read in full.
- **Not searched at all:**
  - Google Scholar
  - ACL Anthology, ICML or ICLR proceedings directly
  - transformer-circuits.pub
  - GDM and OpenAI safety blogs
  - Apollo, METR and Redwood blogs

Working files with raw query output and abstracts are in a session scratchpad folder (not kept)/ (scratchpad only, nothing written to the project).
