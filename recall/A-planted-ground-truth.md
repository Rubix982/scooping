# Recall A — interp methods vs planted ground truth (S2+S4), run 2026-11-27

## Summary

This is the RECALL stage for slice S2+S4 (interpretability methods checked against a planted or known ground truth, in any object). I made no scoop judgments. All named leads resolved. 25 candidates are below, ordered roughly by how many of S1–S4 their abstracts touch. Items 1–7 are the only ones whose abstracts mention an agentic or multi-step object (S1). Items 8–25 are mostly single-turn or single-forward-pass work.

"Opened" means one of three things: the abstract came back from the arXiv API (export.arxiv.org, `search_query` or `id_list`); the Semantic Scholar Graph API record came back with its abstract; or I fetched the page itself with curl or WebFetch. Every quote below is verbatim from that source. Arxiv abs pages were fetched directly only for 2610.05295, 2611.18514, 2604.19775, 2610.25760 and 2605.06846. Everything else came through the APIs.

## Search log

All runs were on 2026-11-27. "AX" is the arXiv API (`https://export.arxiv.org/api/query?search_query=<q>&max_results=N&sortBy=relevance`). "S2" is the Semantic Scholar Graph API. "WS" is WebSearch.

| # | Query | Source | Results looked at | Candidates kept |
|---|---|---|---|---|
| 1 | `ti:InterpBench` | AX | 2 | InterpBench |
| 2 | `ti:tracr` | AX | 3 | Tracr |
| 3 | `ti:"mechanistic interpretability benchmark"` | AX | 1 | MIB |
| 4 | `ti:RAVEL AND abs:interpretability` | AX | 2 | (RAVEL → overflow) |
| 5 | `ti:SAEBench` | AX | 1 | (overflow) |
| 6 | `ti:AxBench` | AX | 1 | (overflow) |
| 7 | `ti:"hidden objectives"` | AX | 15 of 17 | Auditing LMs for hidden objectives |
| 8 | `ti:"eliciting secret knowledge"` | AX | 1 | Eliciting Secret Knowledge |
| 9 | `ti:FIND AND abs:interpretability` | AX | 15 of 250 | FIND |
| 10 | `ti:"multimodal automated interpretability agent"` | AX | 1 | (MAIA → overflow) |
| 11 | `abs:"known circuits" AND abs:interpretability` | AX | 5 | 0 |
| 12 | `abs:"ground truth" AND abs:"circuit discovery"` | AX | 3 | 0 |
| 13 | `abs:"model organisms" AND abs:interpretability AND abs:audit*` | AX | 8 | Pando, "Did you lie?" |
| 14 | `abs:"auditing game"` | AX | 11 | Auditing Games for Sandbagging |
| 15 | `abs:"secret elicitation" OR abs:"secret knowledge" AND abs:interpretability` | AX | 5 | (Taboo → overflow) |
| 16 | `abs:"compiled transformers" AND abs:interpretability` | AX | 2 | (TracrBench → overflow) |
| 17 | `abs:"synthetic" AND abs:"sparse autoencoder*" AND abs:"ground truth"` | AX | 9 | (SynthSAEBench, SAE sanity checks → overflow) |
| 18 | `abs:"model organism*" AND abs:agent* AND (abs:probe* OR abs:interpretability)` | AX | 12 | 0 new |
| 19 | `abs:"hidden goal*" AND abs:interpretability` | AX | 1 | 0 |
| 20 | `abs:"alignment auditing" AND abs:interpretability` | AX | 6 | AuditBench |
| 21 | `abs:"white-box" AND abs:"model organism*"` | AX | 4 | Model Organism Lottery |
| 22 | `abs:"sleeper agent*" AND (abs:probe* OR abs:activation*)` | AX | 3 | 0 |
| 23 | `abs:"implanted" AND abs:interpretability AND abs:"language model*"` | AX | 6 | 0 new |
| 24 | `abs:"planted" AND abs:interpretability` | AX | 40 of 330 (mostly botany noise) | Reference Feature Atlases |
| 25 | `abs:agent* AND abs:trajector* AND abs:"mechanistic interpretability"` | AX | 8 | (Agent MechSuits, tool-use SAE → overflow) |
| 26 | `abs:agent* AND abs:backdoor* AND (abs:activation* OR abs:probe*) AND abs:detect*` | AX | 2 | 0 |
| 27 | `ti:"strategic deception" AND abs:probe*` | AX | 1 | (overflow) |
| 28 | `abs:"reward hacking" AND (abs:probe* OR abs:"sparse autoencoder*") AND abs:detect*` | AX | 9 | 0 |
| 29 | `abs:agentic AND abs:"linear probe*" AND abs:"ground truth"` | AX | 2 | 0 |
| 30 | `abs:"multi-step" AND abs:agent* AND abs:"activation patching"` | AX | 0 | 0 |
| 31 | `abs:agent* AND abs:"hidden objective*"` | AX | 27 | 0 (PRISM → overflow) |
| 32 | `ti:CausalGym` | AX | 1 | (overflow) |
| 33 | `abs:"board game*" AND abs:"sparse autoencoder*"` | AX | 1 | 0 |
| 34 | `abs:"mechanistic anomaly detection"` | AX | 4 | (Quirky ×2 → overflow) |
| 35 | `ti:"quirky language models"` | AX | 2 | (overflow) |
| 36 | `abs:"model diffing" AND (abs:finetun* OR abs:"fine-tun*")` | AX | 6 | (Narrow finetuning, Diff Mining, NLA → overflow) |
| 37 | `abs:"implanted" AND (abs:belief* OR abs:fact*) AND abs:probe*` | AX | 10 | (Believe It or Not → overflow) |
| 38 | `abs:"trojan" AND abs:"mechanistic interpretability"` | AX | 0 | 0 |
| 39 | `ti:"dictionary learning" AND ti:"board game"` | AX | 1 | (overflow) |
| 40 | `ti:"automated circuit discovery"` | AX | 6 | (ACDC → overflow) |
| 41 | `abs:"interpretability agent*" AND (abs:synthetic OR abs:"ground truth")` | AX | 5 | 0 new |
| 42 | `abs:"known mechanism*" AND abs:interpretability` | AX | 18 | (Are We Recovering Mechanisms → overflow) |
| 43 | `abs:"ground-truth" AND abs:"interpretability method*" AND abs:benchmark*` | AX | 13 | Unverbalized-EA organism; (Casper trojans → overflow) |
| 44 | `abs:"causal variable*" AND abs:locali* AND abs:benchmark*` | AX | 0 | 0 |
| 45 | `abs:tracr AND abs:benchmark*` | AX | 2 | (ALTA → overflow) |
| 46 | `abs:sabotage AND (abs:probe* OR abs:"white-box")` | AX | 5 | Telling FIBS |
| 47 | `abs:scheming AND abs:probe*` | AX | 40 of 3165 (physics noise) | 0 |
| 48 | `abs:agent* AND abs:"sparse autoencoder*" AND (abs:finetun* OR abs:"fine-tun*" OR abs:implant*)` | AX | 1 | 0 new |
| 49 | `abs:"attribution graph*" AND (abs:agent* OR abs:"multi-step" OR abs:"multi-hop")` | AX | 35 | 0 (Circuit Oracle → overflow) |
| 50 | `abs:"agentic misalignment" AND (abs:probe* OR abs:steering OR abs:interpretability)` | AX | 2 | 0 |
| 51 | `abs:"tool call*" AND abs:probe* AND abs:activation*` | AX | 0 | 0 |
| 52 | `abs:"model organism*" AND abs:"tool use"` | AX | 1 | 0 |
| 53 | `abs:sandbagging AND (abs:probe* OR abs:"white-box" OR abs:"model internals")` | AX | 14 | 0 new (two → overflow) |
| 54 | `abs:backdoor* AND abs:"sparse autoencoder*" AND abs:"language model*"` | AX | 7 | (two → overflow) |
| 55 | `abs:backdoor* AND abs:circuit* AND abs:"language model*" AND abs:mechanis*` | AX | 2 | 0 |
| 56 | `abs:"emergent misalignment" AND (abs:"sparse autoencoder*" OR abs:persona OR abs:"model diffing")` | AX | 29 | 0 (Persona Features → overflow) |
| 57 | `ti:"hypothesis testing the circuit hypothesis"` | AX | 1 | (overflow) |
| 58 | `abs:"feature recovery" AND abs:"sparse autoencoder*"` | AX | 6 | 0 |
| 59 | `abs:"automated interpretability" AND abs:"ground truth"` | AX | 5 | 0 |
| 60 | `abs:agent* AND abs:"ground truth" AND abs:"mechanistic interpretability"` | AX | 0 | 0 |
| 61 | `abs:"hidden behavio*" AND (abs:probe* OR abs:steering OR abs:"sparse autoencoder*")` | AX | 0 | 0 |
| 62 | `abs:secret* AND abs:"model organism*"` | AX | 6 | 0 new |
| 63 | `abs:"multi-turn" AND abs:"model organism*"` | AX | 1 | 0 |
| 64 | `abs:hint* AND abs:"chain-of-thought" AND (abs:probe* OR abs:"activation patching" OR abs:attribution) AND abs:unfaithful*` | AX | 0 | 0 |
| 65 | `abs:interpretability AND abs:"red team" AND abs:"blue team"` | AX | 2 | 0 |
| 66 | `abs:goal* AND abs:probe* AND abs:"LLM agent*"` | AX | 15 | Collusion probes, Goals Leak, Among Us, Goal-directedness |
| 67 | `abs:"sparse autoencoder*" AND (abs:implant* OR abs:inject* OR abs:planted)` | AX | 30 | 0 |
| 68 | `abs:"feature attribution" AND abs:"ground truth" AND abs:transformer* AND abs:synthetic` | AX | 0 | 0 |
| 69 | `abs:"circuit discovery" AND abs:backdoor*` | AX | 0 | 0 |
| 70 | `abs:"interchange intervention" AND abs:"ground truth"` | AX | 0 | 0 |
| 71 | `abs:"interpretability" AND abs:"model organism*" AND abs:benchmark*` | AX | 10 | 0 new |
| 72 | `abs:"investigator agent*"` | AX | 30 of 36 | 0 new |
| 73 | `abs:"activation oracle*"` | AX | 16 | (Activation Oracles → overflow) |
| 74 | id_list: 2602.08964, 2509.21344, 2507.12691, 2610.19907, 2603.09988, 2410.13032, 2602.10371, 2506.19823 | AX | 8 | Goal-directedness |
| 75 | arxiv.org/abs/ pages for 2610.05295, 2611.18514, 2604.19775, 2610.25760, 2605.06846 | curl | 5 | Readable Before Actionable, Computation Not Memory |
| 76 | `evaluating interpretability methods planted ground truth language model agent` | S2 search | 50 of 445 | 0 new (Sparse Transformer testbed → overflow) |
| 77 | `model organisms interpretability hidden behavior auditing` | S2 search | 0 (HTTP 429, retries exhausted) | — |
| 78 | `interpretability agent trajectory ground truth planted` | S2 search | 0 (429; stopped) | — |
| 79 | `planted ground truth interpretability agent` | S2 search | 40 of 334 (mostly noise) | 0 |
| 80 | `model organism interpretability agentic` | S2 search | 0 (429; stopped) | — |
| 81 | Citations of ARXIV:2602.22755 (AuditBench) | S2 /citations | 43 | (several → overflow) |
| 82 | Citations of ARXIV:2503.10965 (hidden objectives) | S2 /citations | 100 returned (likely truncated, not paginated) | (several → overflow) |
| 83 | Citations of ARXIV:2604.11061 (Pando) | S2 /citations | 3 | 0 new |
| 84 | Citations of ARXIV:2407.14494 (InterpBench) | S2 /citations | 33 | Right Answer Wrong Mechanism, AgenticInterpBench |
| 85 | `interpretability agent planted hidden goal multi-step trajectory model organism probe recover` | WS | 10 | 0 new |
| 86 | `"Building and evaluating alignment auditing agents" Anthropic` | WS | 10 | Anthropic auditing-agents post |
| 87 | `"Simple probes can catch sleeper agents"` | WS | ~17 | Anthropic probes post |
| 88 | `lesswrong interpretability LLM agent model organism hidden goal multi-turn tool use probes SAE ground truth` | WS | 10 | 0 new |
| 89 | `auditing game agentic model organism hidden objective white-box tools agent environment 2026` | WS | 10 | Automating Auditing Games of Sandbagging; (MO replication → overflow) |
| 90 | `white-box probes LLM agent covert side task detection BashArena SHADE-Arena activations ground truth hidden goal` | WS | 10 | 0 new |
| 91 | `mechanistic interpretability benchmark LLM agents multi-step decisions known causal ground truth evaluate attribution patching agent trajectory` | WS | 10 | AgenticInterpBench (ACL page) |
| 92 | `"agentic" model organism interpretability "ground truth" planted behavior multi-turn agent internals evaluation lesswrong OR alignmentforum` | WS | 10 | 0 new |
| 93 | `FIND benchmark function description interpretability agents MAIA synthetic neurons ground truth follow-up 2025 2026` | WS | 10 | 0 new |
| 94 | `interpretability methods recover cause of LLM agent action over multi-step trajectory fine-tuned trigger tool call probe patching evaluation` (extended mode) | WS | 9 | led to items in row 75 |
| 95 | `backdoored LLM agent trigger activation patching localize mechanism multi-step tool use interpretability` | WS | 10 | 0 (agent-backdoor attack papers, no internals) |
| 96 | `"Taking features out of superposition with sparse autoencoders" lesswrong` | WS | 10 | Sharkey et al. 2022 (pre-window → overflow) |
| 97 | `evaluating interpretability methods reinforcement learning agent planted ground truth goal known cause benchmark mechanistic` | WS | 10 | 0 new |
| 98 | `"model organism" LLM agent fine-tuned hidden goal pursued across multiple tool calls interpretability probes detect goal before action` | WS | 10 | 0 new |

Pages fetched directly with curl or WebFetch: anthropic.com/research/probes-catch-sleeper-agents; alignment.anthropic.com/2025/automated-auditing; alignment.anthropic.com/2026/auditbench; alignment.anthropic.com/2025/auditing-mo-replication; neurips.cc/virtual/2026/169826; aclanthology.org/2026.findings-emnlp.725/; lesswrong.com/posts/z6QQJbtpkEAX3Aojj.

## Candidates (closest to the four slots first, max 25)

**1. What Do Collusion Probes Read? Three Pitfalls in Evaluating Multi-Agent Collusion Monitors** — Mainul Hasan Mohsin, Mohammad Shahidur Rahman — 2026-11-07 — https://arxiv.org/abs/2611.10620
  Quote: "Activation probes look like near-perfect monitors for secret collusion among large language model (LLM) agents. We show that they mostly detect that an agent was told to collude, not that it decided to." … "probes find colluders whose goal was fine-tuned into the weights (AUROC 0.995; pre-registered)."
  Slots touched (abstract-level, unverified): S1 (multi-agent committee and code-review episodes), S2 (collusion instruction; goal fine-tuned into the weights), S3 (activation probes), S4 (probe AUROC at finding colluders).
  Why kept: multi-agent decisions, a planted collusion goal, and probes scored on recovering it.

**2. Telling FIBS: Probes Effectively Detect Sabotage and Catch Unverbalized Deception** — Oskar J. Hollinsworth, Alex F. Spies, Tigist Diriba et al. — 2026-10-08 — https://arxiv.org/abs/2610.12445
  Quote: "We further test probes on several cases where deception cannot be determined from the context alone; in these cases of introspective deception, the ground truth can only be determined through careful elicitation or knowledge of a model's training data. In one such evaluation, we show that probes can distinguish transcripts containing a model's true hidden goal from other goals with an AUROC of up to 99.7%."
  Slots touched: S1 (agentic coding: SHADE-Arena, BashArena), S2 (hidden goal known from training data), S3 (multi-layer probes), S4 (AUROC at telling the true hidden goal apart).
  Why kept: probes on agent transcripts, scored against a hidden goal that was trained in.

**3. When Goals Leak Across Relationships: How Cached Goal Representations Shape Cross-Client Decisions** — Saloni Gupta, Sébastien Krier, Glenn Matlin — 2026-10-12 — https://arxiv.org/abs/2610.17365
  Quote: "We test OLMo-3-7B-Instruct in a controlled two-client environment with 20 market scenarios, where each client is assigned an opposing objective." … "Linear probes show that client-goal ownership becomes highly recoverable in middle layers and is concentrated in particular attention heads."
  Slots touched: S1 (agent decisions under shared memory across interactions), S2 (goals assigned by environment design), S3 (probes, KV-cache ablation), S4 (probe recovery and ablation effect on decisions).
  Why kept: agent decisions driven by earlier context, with goals assigned by the environment and recovered from internals.

**4. Readable Before Actionable: Causal Tracing of Indirect Prompt Injection** — Zhe Yu, Wenpeng Xing, Xingxing Yang, Meng Han — 2026-10-04 — https://arxiv.org/abs/2610.05295
  Quote: "A probe may distinguish instructions from data without identifying a state edit that changes the next action. We study this gap through counterfactual role probes, component-wise activation patching, and separate interventions on AgentDojo trajectories."
  Slots touched: S1 (AgentDojo multi-step tool-use trajectories), S2 (injected instruction placed by the environment), S3 (probes, activation patching), S4 partial (measures intervention effect on attack success, not clearly cause recovery).
  Why kept: agent trajectories with a cause planted by environment design, studied through internals.

**5. Among Us: A Sandbox for Measuring and Detecting Agentic Deception** — Satvik Golechha, Adrià Garriga-Alonso — 2025-04-05 — https://arxiv.org/abs/2504.04072
  Quote: "we introduce Among Us, a sandbox social deception game where LLM-agents exhibit long-term, open-ended deception as a consequence of the game objectives." … "We evaluate the effectiveness of methods to detect lying and deception: logistic regression on the activations and sparse autoencoders (SAEs)."
  Slots touched: S1 (multi-step game agents), S2 (deception induced by the role the game assigns), S3 (probes, SAEs), S4 (detection AUROC).
  Why kept: a multi-step agent setting where the ground truth comes from environment design and is scored with internals-based detectors.

**6. A Behavioural and Representational Evaluation of Goal-Directedness in Language Model Agents** — Raghu Arghal, Fade Chen, Niall Dalton et al. — 2026-02-09 — https://arxiv.org/abs/2602.08964
  Quote: "As a case study, we examine an LLM agent navigating a 2D grid world towards a goal state." … "We then use probing methods to decode internal representations of the environment and multi-step action plans."
  Slots touched: S1 (multi-step grid-world agent), S2 weak (goal location fixed by environment design), S3 (probes), S4 partial (decoding accuracy).
  Why kept: probes that recover a goal set by the environment, in an LLM agent.

**7. Computation, Not Memory: Chain-of-Thought and State Tracking in LLM Agents** — Pedram Mouseli, Massieh Moayedi — 2026-10-19 — https://arxiv.org/abs/2610.25760
  Quote: "In a small file-system task, background events announce which file's lock has been toggled but not its new value." … "The state that can be read out without reasoning is a limited guide to how the agent acts."
  Slots touched: S1 (the action depends on reconstructing history), S2 (state constructed by the environment), S3 unclear ("state readouts" — method not named in the abstract), S4 partial.
  Why kept: a decision that depends on earlier steps by construction, compared against a readout of internal state.

**8. AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors** — Abhay Sheshadri, Aidan Ewart, Elias Kempf et al. — 2026-02-26 — https://arxiv.org/abs/2602.22755 (blog: https://alignment.anthropic.com/2026/auditbench)
  Quote: "AuditBench consists of 56 language models with implanted hidden behaviors." … "White-box interpretability tools can be helpful, but the agent performs best with black-box tools."
  Slots touched: S2 (implanted behaviors), S3 (white-box tools given to an investigator agent), S4 (audit success). The audited object is chat behavior, not agent decisions.
  Why kept: a benchmark where interpretability tools are scored on whether they recover a planted behavior.

**9. Building and evaluating alignment auditing agents** — Trenton Bricken, Rowan Wang, Sam Bowman et al. (Anthropic Alignment Science Blog) — 2025-07-24 — https://alignment.anthropic.com/2025/automated-auditing
  Quote: "When tested against models with intentionally-inserted alignment issues, our agents successfully uncover an LLM's hidden goal, build behavioral evaluations, and surface concerning LLM behaviors."
  Slots touched: S2 (inserted hidden goal), S3 (SAE feature tools per the post), S4 (win rate at finding the root cause).
  Why kept: an agentic auditor using interpretability tools, scored against a known implanted objective. Not on arXiv.

**10. Auditing language models for hidden objectives** — Samuel Marks, Johannes Treutlein, Trenton Bricken et al. — 2025-03-14 — https://arxiv.org/abs/2503.10965
  Quote: "As a testbed, we train a language model with a hidden objective." … "Three teams successfully uncovered the model's hidden objective using techniques including interpretability with sparse autoencoders (SAEs), behavioral attacks, and training data analysis."
  Slots touched: S2, S3, S4.
  Why kept: the origin of the blind auditing-game design with a planted objective.

**11. Pando: Do Interpretability Methods Work When Models Won't Explain Themselves?** — Ziqian Zhong, Aashiq Muhamed, Mona T. Diab et al. — 2026-04-13 — https://arxiv.org/abs/2604.11061
  Quote: "Across 720 finetuned models implementing hidden decision-tree rules, agents predict held-out model decisions from $10$ labeled query-response pairs, optionally augmented with one interpretability tool output."
  Slots touched: S2 (planted decision rules), S3 (gradient attribution, RelP, logit lens, SAEs, circuit tracing), S4 (gain from recovering the rule). Each decision is single-step.
  Why kept: a controlled planted-rule benchmark that compares white-box tools head to head.

**12. Automating Auditing Games of Sandbagging** — Christopher Ta, Anna Upreti, David Williams-King, Alan Cooney, Shi Feng — NeurIPS 2026 workshop poster (Managing Agents that Manage Agents) — https://neurips.cc/virtual/2026/169826
  Quote: "red team agents train model organisms (Qwen3-8B) that underperform when there is an evaluation cue, and blue-team agents then audit these models with black-box and white-box techniques." … "adding white-box interpretability tools does not reliably improve detection."
  Slots touched: S2 (organisms planted by agents and independently validated), S3, S4.
  Why kept: a planted cause with white-box tools scored on detecting it, run in an agentic pipeline.

**13. Right Answer, Wrong Mechanism: Detecting Pernicious Divergence in Causal Interventions** — Bei-Ming Liu, Min-Jie Chen — 2026-09-30 — arXiv 2609.39243 (opened via S2 record: https://www.semanticscholar.org/paper/946b2f7faba8c183036f69a2b7349dc4b598e8bb)
  Quote: "We make this question testable by planting hidden pathways inside pretrained language models; the pathways are silent on every benchmark prompt by construction, so which interventions depend on them is known exactly."
  Slots touched: S2 (planted pathways), S3 (patching, DAS, a new test), S4 (AUROC at flagging pathway-dominated interventions).
  Why kept: a planted mechanism used directly as ground truth for judging intervention methods.

**14. InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques** — Rohan Gupta, Iván Arcuschin, Thomas Kwa, Adrià Garriga-Alonso — 2024-07-19 — https://arxiv.org/abs/2407.14494
  Quote: "This work presents InterpBench, a collection of semi-synthetic yet realistic transformers with known circuits for evaluating these techniques." … "Finally, we use our benchmark to evaluate existing circuit discovery techniques."
  Slots touched: S2, S3, S4.
  Why kept: named lead; models with planted circuits.

**15. Tracr: Compiled Transformers as a Laboratory for Interpretability** — David Lindner, János Kramár, Sebastian Farquhar et al. — 2023-01-12 — https://arxiv.org/abs/2301.05062
  Quote: "Additionally, the known structure of Tracr-compiled models can serve as ground-truth for evaluating interpretability methods."
  Slots touched: S2 (compiled weights), S3/S4 proposed.
  Why kept: named lead; origin of compiled-weight ground truth (inside the window).

**16. Can Language Model Agents be Helpful Circuit Explainers in Mechanistic Interpretability? (AgenticInterpBench / HyVE)** — Ayan Antik Khan, Harsh Kohli, Yue-Kun Yao, Huan Sun, Zi-Yu Yao — Findings of EMNLP 2026 (arXiv 2606.24026 per S2) — https://aclanthology.org/2026.findings-emnlp.725/
  Quote: "We introduce AgenticInterpBench, a benchmark for circuit explanation built from 84 semi-synthetic transformer circuits with 163 component-level annotations."
  Slots touched: S2 (semi-synthetic circuits), S3 (agent running causal validation), S4 (explanations scored against annotations).
  Why kept: an agentic interpreter scored on recovering known circuit roles.

**17. MIB: A Mechanistic Interpretability Benchmark** — Aaron Mueller, Atticus Geiger, Sarah Wiegreffe et al. — 2025-04-17 — https://arxiv.org/abs/2504.13151
  Quote: "MIB favors methods that precisely and concisely recover relevant causal pathways or causal variables in neural language models."
  Slots touched: S3, S4. S2 is partial: task-defined causal variables, not planted ones.
  Why kept: named lead; the standard benchmark for circuit and causal-variable localization.

**18. Eliciting Secret Knowledge from Language Models** — Bartosz Cywiński, Emil Ryd, Rowan Wang et al. — 2025-10-01 — https://arxiv.org/abs/2510.01070
  Quote: "We then design various black-box and white-box secret elicitation techniques and evaluate them based on whether they can help an LLM auditor successfully guess the secret knowledge."
  Slots touched: S2, S3, S4.
  Why kept: named lead; a trained-in secret serves as ground truth.

**19. A Model Organism for Studying Unverbalized Evaluation Awareness** — Daniel Donnelly, Evan Chapple, Haritz Puerto, Sahar Abdelnabi — 2026-10-16 — https://arxiv.org/abs/2611.09945
  Quote: "Using the marker as a label, we benchmark linear probes, the Jacobian Lens, and Activation Oracles, built on the base model and blind to the marker. None recovers the label reliably."
  Slots touched: S2 (trained-in marker), S3, S4.
  Why kept: an instance-level planted label used to score internals methods.

**20. "Did you lie?" Evaluating Lie Detectors across Model Scale and Belief-Verified Model Organisms** — Alan Cooney, David Africa, Geoffrey Irving — 2026-06-10 — https://arxiv.org/abs/2606.12618
  Quote: "However, every activation- and logprob-based detector drops sharply on our trained model organisms, with DYL retaining the most signal; only the chain-of-thought judge remains strong, with 0.82 balanced accuracy, partly as an artefact of our verification process favouring CoT-readable beliefs."
  Slots touched: S2 (verified hidden beliefs), S3 (probes), S4.
  Why kept: probes scored against beliefs that were trained in and then verified.

**21. The Model Organism Lottery: Model Organism Interpretability Strongly Depends on Training Methodology** — Andrzej Szablewski, Gabriel Konar-Steenberg, Raffaello Fornasiere et al. — 2026-07-01 — https://arxiv.org/abs/2607.01033
  Quote: "We use these MO variants to benchmark activation oracles, activation steering, the logit lens, and the Jacobian lens." … "Our results cast substantial doubt on the validity of current MOs as interpretability proxies and suggest actionable steps towards more robust benchmarks."
  Slots touched: S2, S3, S4.
  Why kept: questions whether planted ground truth is valid as a test of interpretability methods.

**22. Reference Feature Atlases for Mechanistic Auditing of Language Models** — Rui Wu, Tong Che — 2026-06-01 — https://arxiv.org/abs/2607.22570
  Quote: "On three controlled LoRA hidden objectives injected into both targets, the residual channel makes the planted mechanism perfectly controllable at runtime while matched controls stay unaffected and recovers the planted objective as the top-ranked latent across both targets"
  Slots touched: S2, S3, S4.
  Why kept: recovery of a planted objective is the scored outcome.

**23. Simple probes can catch sleeper agents** — Monte MacDiarmid, Timothy Maxwell, Nicholas Schiefer et al. (Anthropic) — 2024-04-23 — https://www.anthropic.com/research/probes-catch-sleeper-agents
  Quote: "In this post we present “defection probes”: linear classifiers that use residual stream activations to predict when a sleeper agent trojan model will choose to “defect” and behave in accordance with a dangerous hidden goal."
  Slots touched: S2 (trained-in backdoor), S3 (probes), S4 (AUROC).
  Why kept: an early example of probes scored on a planted backdoor. Not on arXiv.

**24. Auditing Games for Sandbagging** — Jordan Taylor, Sid Black, Dillon Bowen et al. — 2025-12-08 — https://arxiv.org/abs/2512.07810
  Quote: "First, a red team fine-tuned five models, some of which conditionally underperformed, as a proxy for sandbagging. Second, a blue team used black-box, model-internals, or training-based approaches to identify sandbagging models."
  Slots touched: S2, S3, S4.
  Why kept: a blinded red/blue game in which internals methods are scored on a planted cause.

**25. FIND: A Function Description Benchmark for Evaluating Interpretability Methods** — Sarah Schwettmann, Tamar Rott Shaham, Joanna Materzynska et al. — 2023-09-07 — https://arxiv.org/abs/2309.03886
  Quote: "This paper introduces FIND (Function INterpretation and Description), a benchmark suite for evaluating the building blocks of automated interpretability methods."
  Slots touched: S2 (synthetic functions with known descriptions), S4 (automated interpreter scored against them). S3 does not apply: the functions are black-box.
  Why kept: named lead; known-answer scoring for automated interpretability agents.

### Overflow: opened and screened, not in the top 25

These are listed so the next stage can pull them. Each was opened the same way (arXiv API abstract unless noted), but I did not attach quotes.
- MAIA: A Multimodal Automated Interpretability Agent (2404.14394, 2024-04-22). Synthetic vision neurons with ground-truth descriptions.
- RAVEL (2402.17700); SAEBench (2503.09532); AxBench (2501.17148); CausalGym (2402.12560).
- SAE ground truth: board-game SAE metrics (2408.00113); SynthSAEBench (2602.14687); Sanity Checks for SAEs (2602.14111); Are SAE Benchmarks Reliable? (2605.18229); Sparse Transformer controlled testbed (2610.19907).
- Sharkey, Braun, beren, "[Interim research report] Taking features out of superposition with sparse autoencoders", LessWrong, 2022-12-13, **pre-window** (originated recovering SAE features against a toy ground truth): https://www.lesswrong.com/posts/z6QQJbtpkEAX3Aojj
- Casper et al., Red Teaming DNNs with Feature Synthesis Tools (2302.10894, 2023-02-08). Implanted trojans as ground truth, vision models.
- Circuits and compiled models: ACDC (2304.14997); TracrBench (2409.13714); ALTA (2410.18077); Hypothesis Testing the Circuit Hypothesis (2410.13032); Are We Recovering Mechanisms? (2610.02098).
- Secrets and auditing: Taboo / ELK with mech interp (2505.14352); How to train your model organism (2610.10203); Stress-Testing Alignment Audits (2602.08877); Narrow Finetuning Leaves Readable Traces (2510.13900); Activation Oracles (2512.15674); Most Current Model Organisms Are Leaky (2605.00994, S2 record); Anthropic MO replication post (alignment.anthropic.com/2025/auditing-mo-replication, 2025-12-12).
- Quirky models: Quirky LMs ELK (2312.01037); MAD for Quirky LMs (2504.08812).
- Backdoors: Activation Differences Reveal Backdoors (2605.07324); LLM Forensics SAE backdoors (2609.07746); Reading Fine-Tuning Diffs for Backdoor Detection (2611.34758, S2 record); TopKLoRA circuit discovery (2610.32866).
- Model diffing and verbalizers: Diff Mining (2608.26462); NLA activation differences (2610.30934); Circuit Oracle (2611.00420); HARP (2607.16448).
- Agentic internals with no clear planted cause in the abstract: Agent MechSuits (2606.22673); Beyond the Black Box tool use (2605.06890); MI for web-agent hallucination (2611.18514); Conformal temporal concepts (2604.19775); PreAct-Bench (2606.09890, S2 record); Detecting Strategic Deception with Linear Probes (2502.03407).
- Other: Linear probes rely on textual evidence (2509.21344); Believe It or Not (2510.17941); Persona Features (2506.19823); Split Personality Training (2602.05532); PRISM instruction-set recovery (2606.09563); Topology-Conditioned Backdoors in multi-agent settings (2610.05793, S2 record; audit is not internals-based).

## Leads that did not resolve

None. Every named lead resolved to a real page:
- InterpBench → 2407.14494
- Tracr → 2301.05062
- MIB → 2504.13151
- RAVEL → 2402.17700
- SAEBench → 2503.09532
- AxBench → 2501.17148
- "Auditing language models for hidden objectives" → 2503.10965
- "Eliciting secret knowledge" → 2510.01070 (also Taboo, 2505.14352)
- FIND → 2309.03886
- MAIA → 2404.14394
- Toy and synthetic SAE ground truth → SynthSAEBench, SAE sanity checks, board-game SAEs, and the Sharkey et al. 2022 LessWrong post

## Gaps — sources I could not search, and why

- **Semantic Scholar keyword search barely worked.** Three of five searches failed with HTTP 429 after retries. The two that ran were noisy. The four citation hops did work, but the hidden-objectives hop returned 100 citers and I did not paginate, so it is probably incomplete. I did not hop from FIBS, the collusion-probes paper, or Eliciting Secret Knowledge.
- **The arXiv API also rate-limited mid-session.** The affected queries were re-run with longer backoff and all completed.
- **Not searched directly:** Google Scholar, OpenReview (ICLR/NeurIPS 2026 submissions and workshop papers beyond the one NeurIPS page above), the ACL Anthology search, and native LessWrong/Alignment Forum search. Those sites were reached only through WebSearch, which surfaced almost no LW/AF posts. Lab blogs (OpenAI, GDM, Apollo, Transluce, Goodfire) were also reached only via WebSearch, with no direct crawl.
- **Only abstracts were read.** Slot tags for items 4–7 especially are guesses from the abstract (for example, whether item 7's "state readouts" are probes).
- **Agent-backdoor attack papers were not kept.** BackdoorAgent, Chain-of-Trigger, and Sleeper Cell (2603.03371) came up in searches, but their abstracts mention no method that reads internals.

Scratch data (raw arXiv/S2 dumps, query outputs) is in a session scratchpad folder (not kept)/. No files were written in the project directory.
