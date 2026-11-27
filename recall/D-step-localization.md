# Recall D — step and source localization vocabulary, run 2026-11-27

This pass covers the vocabularies that passes A–C did not target: agent failure attribution, context attribution and traceback, prompt-injection forensics, backdoor-trigger localization in agents, step importance inside agent trajectories, and multi-turn turn attribution. It is recall only. The tags below are read off abstracts (two papers also got a short methods check, marked where used), and no verdicts are made here.

## Summary

- 24 ranked candidates, 60 screened items, 7 opened-and-dropped. Every quote is copied from an abstract I opened in this session (arXiv API, or the Semantic Scholar payload for three non-arXiv items). The two LessWrong tl;drs came through a page summarizer, so they may not be verbatim; that is marked on each.
- The three remembered names all resolved: ContextCite = 2409.00729, TracLLM = 2506.04202, AttnTrace = 2508.03793.
- What this vocabulary turned up splits three ways:
  - **Internals-based localization of a planted cause, but not at step level.** Attnlocate (2608.24022) and MindGuard (2508.20412) read the acting agent's attention and localize an injected span or a poisoned tool. Neither one outputs a trajectory step scored against a planted step.
  - **Step-level localization against known injection points, without internals.** DriftNet/AgentDrift (2609.10892, 2609.06972), AgentTracer-IPI (2610.09935), Causal Agent Replay (2606.08275), AgentSentry, CausalArmor, AttriGuard. These are text classifiers, counterfactual re-execution, or leave-one-out ablation.
  - **Step-level failure attribution using some model's internals, scored against annotated rather than planted steps.** MASPrism, SOAP, ReCast and Tokengeist read the hidden states or attention of a separate diagnoser model, not the agent that acted.
- Several sources failed or were rate-limited:
  - **Semantic Scholar citations:** returned HTTP 429 on the first attempts for Who&When and AgenTracer; both worked on retry.
  - **preprints.org:** returned 403 twice.
  - **One author PDF:** returned 404.
  - Details are in Gaps.

## Search log

All runs were on 2026-11-27.

- **arXiv API:** `http://export.arxiv.org/api/query?search_query=<q>&max_results=<n>&sortBy=relevance`. "id fetch" rows use `id_list=` to pull full abstracts for IDs already surfaced; they are not searches.
- **Semantic Scholar:** `https://api.semanticscholar.org/graph/v1/paper/arXiv:<id>/citations?fields=title,externalIds,publicationDate,abstract&limit=1000`. Citer lists were screened with regexes over title and abstract:
  - Who&When (#33): `hidden state|attention weight|attention pattern|internal signal|internal state|internal representation|activation|gradient|probe|probing|saliency|interpretab|white-box|logit|likelihood|attribution graph|sparse autoencoder|mechanistic`.
  - Second pass on Who&When: `inject|plant|synthetic error|controlled error|counterfactual|ground[- ]truth` AND `attribut|locali|decisive|which step|root cause|diagnos`.
  - ContextCite (#45): `\bagent|tool|trajector|multi-turn|conversation|injection|turn\b`.
  - AgenTracer (#50): `hidden state|attention|internal|activation|gradient|probe|probing|saliency|interpretab|white-box|logit|mechanistic|inject|plant`.
- **GitHub:** `https://api.github.com/search/repositories?q=<q>&per_page=15|20`, no auth.

| # | Query (exact string) | Source | Date | Results | IDs kept / opened |
|---|---|---|---|---|---|
| 1 | `abs:"failure attribution" AND abs:agent` (n=50) | arXiv API | 2026-11-27 | 75 total / 50 returned | 2601.15075, 2605.07509, 2610.11334, 2610.13105, 2607.12747, 2610.17747, 2610.18780, + screened |
| 2 | `abs:"failure attribution" AND (abs:"hidden states" OR abs:attention OR abs:"internal" OR abs:gradient)` (n=50) | arXiv API | 2026-11-27 | 19 | 2606.03467, 2608.10646 |
| 3 | id fetch 2606.03467, 2608.10646, 2611.23346, 2610.24383 | arXiv id_list | 2026-11-27 | 4 | screened |
| 4 | `ti:ContextCite OR ti:TracLLM OR ti:AttnTrace OR abs:ContextCite` (n=50) | arXiv API | 2026-11-27 | 4 | 2409.00729, 2508.03793, 2506.04202 |
| 5 | id fetch 2409.00729, 2508.03793, 2506.04202 | arXiv id_list | 2026-11-27 | 3 | (abstracts for #4) |
| 6 | citations of arXiv:2508.03793 (AttnTrace) | Semantic Scholar | 2026-11-27 | 11 | 2610.09935, 2608.24022, 2607.22610, 2608.29942, 2609.30830, 2611.26221 |
| 7 | citations of arXiv:2506.04202 (TracLLM) | Semantic Scholar | 2026-11-27 | 24 | 2609.33676, 2610.30738, 2610.25966, 2604.01194, 2510.14005 |
| 8 | id fetch of 9 citers from #6–#7 | arXiv id_list | 2026-11-27 | 9 | 2608.24022, 2607.22610, 2609.33676, 2610.09935, + screened |
| 9 | `(abs:"context attribution" OR abs:"context traceback" OR abs:"source attribution") AND (abs:agent OR abs:agents OR abs:"tool")` (n=50) | arXiv API | 2026-11-27 | 48 | 2508.20412, 2602.22724 |
| 10 | id fetch 2508.20412, 2602.22724, 2607.17149, 2606.29279 | arXiv id_list | 2026-11-27 | 4 | 2508.20412, 2602.22724, + screened |
| 11 | `abs:"prompt injection" AND (abs:attention OR abs:"hidden states" OR abs:activations OR abs:gradient) AND (abs:localize OR abs:localization OR abs:attribution OR abs:trace OR abs:pinpoint)` (n=50) | arXiv API | 2026-11-27 | 28 | 2511.10720, 2606.23277, 2602.20708 |
| 12 | id fetch 2511.10720, 2606.23277, 2602.20708 | arXiv id_list | 2026-11-27 | 3 | same |
| 13 | `abs:"indirect prompt injection" AND abs:agent AND (abs:forensic OR abs:forensics OR abs:"post-attack" OR abs:"root cause" OR abs:provenance OR abs:traceback)` (n=50) | arXiv API | 2026-11-27 | 22 | 2604.23374 (rest system-level provenance, not kept) |
| 14 | id fetch 2604.23374, 2609.36570 | arXiv id_list | 2026-11-27 | 2 | screened |
| 15 | `attention-based attribution which tool call output caused LLM agent action indirect prompt injection localization hidden states` | WebSearch standard | 2026-11-27 | 10 | 2603.10749, 2610.28988, 2602.07918 |
| 16 | id fetch 2603.10749, 2610.28988, 2602.07918, 2604.01194, 2510.14005 | arXiv id_list | 2026-11-27 | 5 | 2603.10749, 2602.07918, 2604.01194, + screened |
| 17 | `abs:backdoor AND (abs:agent OR abs:agents) AND abs:trigger AND (abs:observation OR abs:"tool output" OR abs:environment OR abs:trajectory) AND (abs:activation OR abs:attention OR abs:"hidden states" OR abs:neuron OR abs:interpretability OR abs:localize)` (n=50) | arXiv API | 2026-11-27 | 29 | 2601.04566, 2606.12896, 2610.05793, 2407.15168 |
| 18 | id fetch 2601.04566, 2606.12896, 2610.05793, 2407.15168 | arXiv id_list | 2026-11-27 | 4 | screened |
| 19 | `LLM agent backdoor trigger in tool observation detection using hidden states activations which step triggered malicious action` | WebSearch standard | 2026-11-27 | 10 | 2611.15118, 2604.24542, 2607.24893, 2402.11208 |
| 20 | id fetch 2611.15118, 2604.24542, 2607.24893, 2402.11208 | arXiv id_list | 2026-11-27 | 4 | 2611.15118, + screened |
| 21 | `(abs:agent OR abs:agentic) AND (abs:"step attribution" OR abs:"turn attribution" OR abs:"step importance" OR abs:"critical step" OR abs:"critical steps" OR abs:"decisive step" OR abs:"pivotal step") AND (abs:attention OR abs:gradient OR abs:saliency OR abs:"hidden states" OR abs:activations OR abs:probe)` (n=50) | arXiv API | 2026-11-27 | 29 (mostly noise) | 2610.17633, 2607.17621 |
| 22 | id fetch 2610.17633, 2607.17621 | arXiv id_list | 2026-11-27 | 2 | screened |
| 23 | `abs:"multi-turn" AND (abs:jailbreak OR abs:conversation OR abs:dialogue) AND (abs:"which turn" OR abs:"turn-level attribution" OR abs:"turn attribution" OR abs:"attribution" ) AND (abs:attention OR abs:gradient OR abs:activations OR abs:"hidden states" OR abs:probe OR abs:interpretability)` (n=50) | arXiv API | 2026-11-27 | 21 | 2609.27773 |
| 24 | id fetch 2609.27773 | arXiv id_list | 2026-11-27 | 1 | screened |
| 25 | `abs:"multi-turn jailbreak" AND (abs:activations OR abs:"hidden states" OR abs:representation OR abs:probe OR abs:attention OR abs:steering OR abs:mechanistic)` (n=40) | arXiv API | 2026-11-27 | 18 | 2507.02956, 2603.15684 |
| 26 | id fetch 2507.02956, 2603.15684 | arXiv id_list | 2026-11-27 | 2 | screened (positioning) |
| 27 | citations of arXiv:2505.00212 (Who&When) | Semantic Scholar | 2026-11-27 | HTTP 429 twice (15 s backoff) | – (retried in #33) |
| 28 | `"failure attribution" agent trajectories hidden states internal signals step representation Who&When` | WebSearch standard | 2026-11-27 | 10 | 2606.00765 (rest dups) |
| 29 | `interpretability LLM agent which earlier observation caused tool call attribution integrated gradients attention trajectory steps` | WebSearch standard | 2026-11-27 | 10 | 2512.12597, 2602.06841, 2610.09624 |
| 30 | id fetch 2512.12597, 2602.06841, 2610.09624 | arXiv id_list | 2026-11-27 | 3 | screened |
| 31 | citations of arXiv:2601.15075 (agentic attribution) | Semantic Scholar | 2026-11-27 | 11 | 2610.16071, 2605.28732, 2605.08715 (2608.06909 already found) |
| 32 | id fetch 2610.16071, 2605.28732, 2605.08715 | arXiv id_list | 2026-11-27 | 3 | screened |
| 33 | citations of arXiv:2505.00212 (Who&When), retry, regex-screened | Semantic Scholar | 2026-11-27 | 258 (48 internals-regex hits; 40 inject/counterfactual-regex hits) | 2605.03354, 2609.10892, 2609.06972, 2606.08275, + others in #34 |
| 34 | id fetch 2609.10892, 2609.06972, 2606.08275, 2611.05650, 2610.41025, 2608.29228, 2605.03354, 2604.17761, 2509.14295, 2611.31063 | arXiv id_list | 2026-11-27 | 10 | 2609.10892, 2609.06972, 2606.08275, 2605.03354, + screened |
| 35 | read abstracts of 3 non-arXiv citers from the #33 payload | Semantic Scholar | 2026-11-27 | 3 | DOI 10.1111/exsy.70392; DOI 10.1109/AIoTC71250.2026.11688433; DOI 10.1109/ICERA72709.2026.11666599 (all screened) |
| 36 | citations of arXiv:2509.03312 (AgenTracer) | Semantic Scholar | 2026-11-27 | HTTP 429 twice | – (retried in #50) |
| 37 | GitHub `q=agent+failure+attribution+hidden+states`; `q=prompt+injection+attribution+attention+agent`; `q=context+traceback+agent` (3 calls) | GitHub search API | 2026-11-27 | 0 / 0 / 5 (irrelevant) | – |
| 38 | GitHub `q=failure+attribution+multi-agent`; `q=agentic+attribution`; `q=step+attribution+agent+trajectory` (3 calls) | GitHub search API | 2026-11-27 | 35 / 1080 / 6 | jaineet17/causal-agent-replay (= 2606.08275); two awesome lists used as seeds |
| 39 | README fetch + grep (internals terms) of IcyFeather233/Awesome-LLM-Agent-Trajectory-Analysis and yzhao062/awesome-auditable-ai | GitHub raw | 2026-11-27 | 283 + 656 lines | – (dups only) |
| 40 | `site:lesswrong.com OR site:alignmentforum.org interpretability agent trajectory which step caused decision attribution tool output` | WebSearch standard | 2026-11-27 | 10 (no LW/AF pages) | preprints.org 22ffa933… (WebFetch 403) |
| 41 | `preprints.org behavioral mechanistic interpretability localize responsible step agent failure 2026` | WebSearch standard | 2026-11-27 | 10 | 2610.21708; leads: preprints 202610.2861, Aghzal PDF |
| 42 | id fetch 2610.21708, 2605.22719 | arXiv id_list | 2026-11-27 | 2 | 2610.21708 (2605.22719 dropped) |
| 43 | WebFetch preprints.org/manuscript/202610.2861; mohamedaghzal.github.io/papers/toward_mi_for_agents.pdf | WebFetch | 2026-11-27 | 403 / 404 | – (gap) |
| 44 | `au:Aghzal OR (ti:"mechanistic interpretability" AND (ti:agent OR ti:agents)) OR ti:"chain of attribution"` (n=30) | arXiv API | 2026-11-27 | 13 | – (Aghzal preprints not on arXiv; 2611.18514 already found) |
| 45 | citations of arXiv:2409.00729 (ContextCite), regex-screened | Semantic Scholar | 2026-11-27 | 152 (44 after filter) | 2607.21106, 2610.09493, 2410.03055, 2610.16349 |
| 46 | id fetch 2607.21106, 2610.09493, 2410.03055, 2610.16349 | arXiv id_list | 2026-11-27 | 4 | screened / dropped |
| 47 | `(abs:"LLM agent" OR abs:"LLM agents" OR abs:"language agent" OR abs:"tool-using") AND (abs:"integrated gradients" OR abs:"attention rollout" OR abs:saliency OR abs:"gradient-based attribution" OR abs:"feature attribution" OR abs:"input attribution" OR abs:"token attribution")` (n=50) | arXiv API | 2026-11-27 | 24 (mostly noise) | – |
| 48 | `(abs:"tool output" OR abs:"tool outputs" OR abs:"tool result" OR abs:"tool response" OR abs:observation) AND (abs:"linear probe" OR abs:"residual stream" OR abs:"activation patching" OR abs:"attention heads" OR abs:"sparse autoencoder") AND (abs:agent OR abs:agents)` (n=50) | arXiv API | 2026-11-27 | 41 | 2605.25310, 2610.18408, 2606.00566, 2603.12564 |
| 49 | id fetch 2605.25310, 2610.18408, 2606.00566, 2603.12564 | arXiv id_list | 2026-11-27 | 4 | 2605.25310, 2610.18408, 2603.12564, + screened |
| 50 | citations of arXiv:2509.03312 (AgenTracer), retry; 70 citers not already in #33, regex-screened | Semantic Scholar | 2026-11-27 | 156 (70 new) | – (no internals terms matched; fault-injection titles noted in Leads) |
| 51 | `(abs:"credit assignment" OR abs:"turn-level credit" OR abs:"step-level credit") AND (abs:"LLM agent" OR abs:"LLM agents" OR abs:"multi-turn") AND (abs:attention OR abs:"hidden states" OR abs:gradient OR abs:saliency OR abs:attribution)` (n=40) | arXiv API | 2026-11-27 | 32 (RL training methods) | – |
| 52 | `localize which tool output step caused agent hijack using model internals residual stream probe attention injected at known step benchmark 2026` | WebSearch extended | 2026-11-27 | 10 | 2606.16364, 2609.36138, 2605.18646 (rest dups) |
| 53 | id fetch 2606.16364, 2609.36138, 2605.18646 | arXiv id_list | 2026-11-27 | 3 | screened |
| 54 | `(abs:"multi-agent" OR abs:"multi-turn") AND (abs:"earlier turn" OR abs:"earlier turns" OR abs:"previous turns" OR abs:"prior turns" OR abs:"which message" OR abs:"which turn" OR abs:"message-level attribution") AND (abs:attention OR abs:"hidden states" OR abs:activations OR abs:gradient OR abs:probe OR abs:patching)` (n=40) | arXiv API | 2026-11-27 | 7 | – |
| 55 | `(abs:"memory poisoning" OR abs:"tool poisoning" OR abs:"poisoned memory" OR abs:"poisoned observation" OR abs:"environmental injection") AND (abs:attention OR abs:"hidden states" OR abs:activations OR abs:gradient OR abs:probe OR abs:interpretability) AND (abs:attribution OR abs:localize OR abs:localization OR abs:trace OR abs:source)` (n=40) | arXiv API | 2026-11-27 | 7 | – (dups) |
| 56 | `au:"Jinyuan Jia" AND (abs:agent OR abs:agents) AND (abs:attribution OR abs:traceback OR abs:forensic OR abs:attribute)` (n=40) | arXiv API | 2026-11-27 | 4 | – (dups) |
| 57 | `lesswrong agent interpretability prompt injection tool result probe attribution earlier step` (allowed_domains lesswrong.com, alignmentforum.org) | WebSearch standard | 2026-11-27 | 10 | two LW posts (screened) |
| 58 | WebFetch of the two LW posts from #57 | WebFetch | 2026-11-27 | 2 | tl;drs via summarizer |
| 59 | `(abs:"context attribution" OR abs:"input attribution" OR abs:"feature attribution") AND (abs:"multi-turn" OR abs:dialogue OR abs:conversation OR abs:conversations) AND (abs:LLM OR abs:"language model")` (n=40) | arXiv API | 2026-11-27 | 5 | – |
| 60 | WebFetch arxiv.org/abs/2607.22610 and arxiv.org/html/2607.22610v2 (methods check, first 100k of 224k chars) | WebFetch | 2026-11-27 | 2 | tags for 2607.22610 |
| 61 | `ti:"learning to attribute with attention" OR (abs:AT2 AND abs:attribution AND abs:attention)` (n=10) | arXiv API | 2026-11-27 | 1 | 2504.13752 |
| 62 | WebFetch arxiv.org/html/2608.24022v1 (setup check) | WebFetch | 2026-11-27 | 1 | tags for 2608.24022 |

Totals across the 62 rows:
- **Search calls (41):**
  - arXiv: 19 searches.
  - Semantic Scholar: 8 citation calls, 2 of them failed with 429.
  - WebSearch: 8.
  - GitHub: 6 searches.
- **Other network calls:**
  - 2 GitHub README fetches.
  - 19 arXiv id fetches.
  - 8 WebFetch page reads, 3 of them failed (403, 403, 404).

## Candidates (closest to the four slots first, 24 total)

The ranking puts items that read some model's internals ahead of items that do not, because S3 is the slot that defines the claim. Within each group, items closer to S1, S2 and S4 come first. The tags come from the abstracts, plus the two methods checks marked "(methods check)". None of them is a verdict.

**1. What Guides the Agent? Adjudicating Unauthorized Behavior via Localizing Behavior-Guiding Instructions (Attnlocate)** — Yichao Gao, Yumo Zhang, Yunhao Yao, Haohua Du, Puhan Luo, Ruiqi Li, Zhiqiang Wang — 2026-08-25 — https://arxiv.org/abs/2608.24022
  Quote: "We propose Attnlocate, a runtime framework for fine-grained localization of context spans that genuinely influence tool-calling decisions, i.e., behavior-guiding instructions." / "We evaluate Attnlocate across ten agent configurations from five LLM families, covering scenarios involving indirect prompt injection and tool poisoning. Attnlocate achieves a mean IoU of 0.743, an average AUROC of 0.956, and a 0.934 true-positive rate at 0.067 false-positive rate."
  Slots touched (abstract-level, unverified):
  - S1: partial. These are tool-calling decisions. The methods check found the context "can include execution results returned from prior operations", but the paper does not give episode lengths.
  - S2: likely. The payload sits in the tool output (InjecAgent) or in tool metadata (MCPTox), but the paper does not say how the reference spans were produced.
  - S3: yes. It reads attention matrices.
  - S4: partial. It reports span IoU against a reference span. There is no step-level or tool-return-level metric.
  Uses internals of the agent model? yes. The methods check says it needs "white-box access to the underlying model to retrieve the attention matrices generated during inference".
  Outputs a step scored against a planted step? no (span-level only)
  Why kept: of everything found, this is the closest internals-based localization of an injected cause inside an agent's context. Its authors overlap with MindGuard (#2).

**2. MindGuard: Intrinsic Decision Inspection for Securing LLM Agents Against Metadata Poisoning** — Zhiqiang Wang, Haohua Du, Guanquan Shi, Junyang Zhang, HaoRan Cheng, Yunhao Yao, Kaiwen Guo, Xiang-Yang Li — 2025-08-28 — https://arxiv.org/abs/2508.20412
  Quote: "Thus, we propose MindGuard, a decision-level guardrail for LLM agents, providing provenance tracking of call decisions, policy-agnostic detection, and poisoning source attribution against TPA." / "Extensive experiments on real-world datasets demonstrate that MindGuard achieves 94\%-99\% average precision in detecting poisoned invocations, 95\%-100\% attribution accuracy, with processing times under one second and no additional token cost."
  Slots touched (abstract-level, unverified):
  - S1: partial. The decision is a tool invocation. The poison sits in tool metadata in the context, not in an observation at a step.
  - S2: yes. The poisoned tool is known.
  - S3: yes. It builds an attention-based "Decision Dependence Graph".
  - S4: partial. It attributes the decision to a poisoning source.
  Uses internals of the agent model? yes (attention of the LLM making the call; abstract-level)
  Outputs a step scored against a planted step? no (it scores source or tool attribution accuracy)
  Why kept: an attention-based attribution of an agent's decision to a planted poison, scored on attribution accuracy.

**3. The Why Behind the Action: Unveiling Internal Drivers via Agentic Attribution** — Chen Qian, Peng Wang, Dongrui Liu, Junyao Yang, Dadi Guo, Ling Tang, Jilin Mei, Qihan Ren, Shuai Shao, Yong Liu, Jie Fu, Jing Shao, Xia Hu — 2026-01-21 — https://arxiv.org/abs/2601.15075
  Quote: "Specifically, at the \textit{component level}, we employ temporal likelihood dynamics to identify critical interaction steps; then at the \textit{sentence level}, we refine this localization using perturbation-based analysis to isolate the specific textual evidence." / "Experimental results demonstrate that the proposed framework reliably pinpoints pivotal historical events and sentences behind the agent behavior, offering a critical step toward safer and more accountable agentic systems."
  Slots touched (abstract-level, unverified):
  - S1: yes. The scenarios cover tool use and memory.
  - S2: unclear. The scenarios include "memory-induced bias", but the abstract does not say whether causes were planted at chosen steps.
  - S3: borderline. The method uses the agent's likelihoods plus text perturbation. No hidden states or attention are named.
  - S4: yes. It outputs critical steps.
  Uses internals of the agent model? unclear. It uses output likelihoods, not activations.
  Outputs a step scored against a planted step? unclear
  Why kept: it is framed as step attribution for any agent action, not only failures. A WebSearch result summary (#57) described an injection example where "the tool return in Step 3" is the decisive event. I did not open that passage.

**4. Prompt-Injection Probes Learn the Conversation, Not Just the Injection** — Kaan Kale, Sriram Vishwanath — 2026-10-13 — https://arxiv.org/abs/2610.18408
  Quote: "Linear probes on a model's hidden states are used as cheap monitors for indirect prompt injection: they screen the tool outputs an agent reads and send suspicious ones to a slower second check, so every false alarm has a cost." / "When each attack is compared with the same conversation without the injection, or with harmless text formatted like an injection, standard probes flag most of these harmless cases."
  Slots touched (abstract-level, unverified):
  - S1: yes. Agent conversations with tool outputs.
  - S2: yes. Injections are inserted, with matched no-injection controls.
  - S3: yes. Hidden-state probes.
  - S4: partial. The probes flag individual tool outputs, but they are scored as injection detection, not as which step caused the action.
  Uses internals of the agent model? yes (the abstract says "a model's hidden states")
  Outputs a step scored against a planted step? unclear (per-tool-output flags)
  Why kept: probes are applied per tool output in agent conversations with planted injections and matched controls.

**5. Auditing Agent Actions through Query-Conditioned Attribution** — Yifan Liu, Praveen Venkateswaran, Abdulhamid Adebayo, Dong Wang — 2026-09-27 — https://arxiv.org/abs/2609.33676
  Quote: "We therefore formulate query-conditioned agent action attribution, a new task that takes a natural-language auditing query as input and recovers the source and ordered intermediate evidence for the query-specified aspect of an action." / "To enable efficient, query-specific attribution, we use small open-weight models as attribution proposers that combine query-conditioned gradient saliency with query-semantic relevance to rank history units."
  Slots touched (abstract-level, unverified):
  - S1: yes.
  - S2: unclear. The abstract does not say how A^3Bench was built. Its query types include "unsafe-behavior tracing".
  - S3: yes, but in proposer models. Gradient saliency is computed in small proposer models, and the acting model may be API-only.
  - S4: yes. It reports source MRR over history units.
  Uses internals of the agent model? no; it uses a different model's internals (gradients)
  Outputs a step scored against a planted step? unclear (scored against benchmark labels)
  Why kept: gradient-based ranking of earlier history units, scored on recovering the source of an agent action.

**6. Tokengeist: Multi-Turn Attribution Tracing in Agentic Conversations** — Jessica Tang, Shraddha Barke, Sharad Agarwal — 2026-06-14 (v2 2026-11-19) — https://arxiv.org/abs/2607.22610
  Quote: "When a model answers after several turns of dialogue and tool use, an overseer needs to know which earlier turns and intermediate steps it rests on." / "Across four open-weight models, flat attribution methods fail to recover multi-hop dependencies, with source recall improving from 11-38% under flat attribution to 82-94% under Tokengeist."
  Slots touched (abstract-level plus methods check):
  - S1: yes. Tool-use transcripts from TauBench and ConFETTI.
  - S2: no. The methods check says "Gold provenance DAGs are model-produced".
  - S3: yes. Avg. Attention, AT2 and AttnTrace are among its back-ends.
  - S4: yes. Turn-level source recall against the gold provenance.
  Uses internals of the agent model? no. The open-weight attributing model re-reads recorded transcripts; per the methods check, the TauBench rollouts came from gpt-4.1.
  Outputs a step scored against a planted step? no (scored against annotated provenance)
  Why kept: attention-based attribution of a later output to earlier turns and tool steps in agent traces.

**7. MASPrism: Lightweight Failure Attribution for Multi-Agent Systems Using Prefill-Stage Signals** — Yang Liu, Hongjiang Feng, Junsong Pu, Zhuangbin Chen — 2026-05-08 — https://arxiv.org/abs/2605.07509
  Quote: "MASPrism first extracts token-level negative log-likelihood and attention weights during a prefill pass to identify symptom-like steps and earlier candidate sources, without decoding." / "Using Qwen3-0.6B as the SLM, MASPrism achieves the best performance on three of the four evaluated subsets across Who&When and TRAIL, improving Top-1 accuracy on Who&When-HC by 33.41% over the best baseline."
  Slots touched (abstract-level, unverified):
  - S1: yes.
  - S2: partial. Who&When labels are annotated.
  - S3: yes. Attention and NLL, but of a small separate model.
  - S4: yes. Top-1 step accuracy.
  Uses internals of the agent model? no; it uses a different model's internals (Qwen3-0.6B)
  Outputs a step scored against a planted step? no (scored against annotated steps)
  Why kept: attention-based step localization over agent trajectories.

**8. Can Failed Trajectories Reveal Where Agents Go Wrong? Agentic Failure Attribution Without Step-Level Labels (SOAP)** — Do Nguyen-Thanh, Junlin Fang, Bing Li, Zhen Fang, Sean Du — 2026-10-09 — https://arxiv.org/abs/2610.13105
  Quote: "SOAP first constructs a spectral reference space from LLM representations and assigns each step a base error score according to its projection behavior." / "To address this downstream contamination, SOAP derives soft step dependencies from attention patterns and propagates downstream error evidence toward its likely upstream sources."
  Slots touched (abstract-level, unverified):
  - S1: yes.
  - S2: unclear.
  - S3: yes. Representations and attention.
  - S4: yes. Decisive-step scores.
  Uses internals of the agent model? unclear. The abstract says "LLM representations"; a WebSearch summary (#28) said they come from a frozen model.
  Outputs a step scored against a planted step? unclear
  Why kept: an internals-derived step-dependency graph, used to push blame upstream to the decisive step.

**9. ReCast: Attribution-Oriented Step Representation Learning for LLM-Based Agent Systems** — Weilin Jin, Mingyu Wang, Taiyu Zhu, Ziqi Zhou, Wenbo Li, Haoyang Huang, Nan Duan, Yifan Wu, Ying Li, Zhonghai Wu — 2026-10-08 — https://arxiv.org/abs/2610.11334
  Quote: "Recent methods leverage LLM internal signals for failure attribution, typically using hidden states as step representations. We therefore conduct an empirical study to evaluate how effectively these representations distinguish root-cause steps from other steps and find limited separation." / "ReCast first selects attribution-relevant layers, then constructs complementary pattern and deviation features, and finally learns contextualized step representations through an encoder trained with contrastive and ranking objectives."
  Slots touched (abstract-level, unverified):
  - S1: yes.
  - S2: partial. Who&When labels are annotated.
  - S3: yes. Hidden states of a frozen LLM.
  - S4: yes. Hit@1.
  Uses internals of the agent model? no; it uses a different model's internals (frozen LLM)
  Outputs a step scored against a planted step? no (scored against annotated steps)
  Why kept: it states that hidden-state step representations are an established family in failure attribution. The prior methods it refers to were not identified (see Leads).

**10. Sell Me This Stock: Unsafe Recommendation Drift in LLM Agents** — Zekun Wu, Adriano Koshiyama, Sahan Bulathwela, Maria Perez-Ortiz — 2026-03-13 — https://arxiv.org/abs/2603.12564
  Quote: "We replay 23-turn financial advisory conversations across eight language models, running each dialogue twice with clean and manipulated tool data." / "The damage is not memory-driven: contaminating only the current turn still produces 95% of the violations. The model internally distinguishes the manipulation (sparse autoencoder features separate adversarial from random perturbations), but this does not translate into safer output."
  Slots touched (abstract-level, unverified):
  - S1: yes. Multi-turn agent with tool calls.
  - S2: yes. Manipulated tool data, with the contaminated turn chosen by the experimenters.
  - S3: yes. SAE features and activation interventions.
  - S4: no. Localization by turn is done by contaminating inputs, not by internals.
  Uses internals of the agent model? yes
  Outputs a step scored against a planted step? no
  Why kept: planted tool-output manipulation at chosen turns, with internals read in the same agent.

**11. Tool-Call Dependency Structure is Linearly Decodable in LLM Agent Residual Streams** — Tianda Sun, Dimitar Kazakov — 2026-05-25 — https://arxiv.org/abs/2605.25310
  Quote: "A low-capacity edge probe on the residual stream of Qwen3-32B decodes the tool-call dependency graph well above both a Hewitt--Liang random-label control and a positional baseline." / "Our claims concern representation, not behavioural control, and span two model families and one primary domain."
  Slots touched (abstract-level, unverified):
  - S1: yes.
  - S2: partial. Dependencies are known from an oracle, but no cause is planted.
  - S3: yes. Probe and per-layer patching.
  - S4: partial. It decodes which earlier tool output feeds a later call, scored against the oracle graph.
  Uses internals of the agent model? yes
  Outputs a step scored against a planted step? no (it outputs dependency edges scored against an oracle)
  Why kept: an internals readout of which earlier step a later call depends on. Recall B logged it at its query 17; it is not in the skip list.

**12. What Happens Inside Agent Memory? Circuit Analysis from Emergence to Diagnosis** — Xutao Mao, Jinman Zhao, Gerald Penn, Cong Wang — 2026-05-05 — https://arxiv.org/abs/2605.03354
  Quote: "Building on this circuit structure, we develop an unsupervised stage-level diagnostic that localizes silent failures to the responsible operation at 76.2% accuracy. It outperforms a strong LLM trace judge by 3.1 points as well as a supervised hidden-state probe by 8.8 points."
  Slots touched (abstract-level, unverified):
  - S1: partial. A memory write-manage-read pipeline across sessions.
  - S2: unclear.
  - S3: yes. Feature circuits.
  - S4: partial. It localizes to a pipeline stage or operation, not a trajectory step.
  Uses internals of the agent model? yes
  Outputs a step scored against a planted step? no (stage-level, against unclear labels)
  Why kept: an internals-based localizer of the responsible operation in an agent pipeline, compared against an LLM judge and a hidden-state probe.

**13. AttnTrace: Contextual Attribution of Prompt Injection and Knowledge Corruption** — Yanting Wang, Runpeng Geng, Ying Chen, Jinyuan Jia — 2025-08-05 — https://arxiv.org/abs/2508.03793
  Quote: "In this work, we propose AttnTrace, a new context traceback method based on the attention weights produced by an LLM for a prompt." / "As a real-world application, we demonstrate that AttnTrace can effectively pinpoint injected instructions in a paper designed to manipulate LLM-generated reviews."
  Slots touched (abstract-level, unverified):
  - S1: no. A single long context; agents appear only as motivation.
  - S2: yes. Injected texts.
  - S3: yes. Attention.
  - S4: yes, at text level.
  Uses internals of the agent model? yes (of the LLM that produced the response)
  Outputs a step scored against a planted step? no (it scores texts, not steps)
  Why kept: attention-based traceback to injected text. Tokengeist and AgentWatcher build on this line.

**14. Lazare, veni foras: Reprogramming Dormant Neurons to Backdoor AI Agents** — Yuchen Zeng, Giorgio Severi, Blake Bullwinkel, Eric Horvitz, Dimitris Papailiopoulos — 2026-11-11 — https://arxiv.org/abs/2611.15118
  Quote: "The trigger can be an ordinary string appearing anywhere in the agent's context." / "On Nemotron-Terminal-8B, seven of 12,000+ neurons, fitted on 23 trigger/no-trigger trajectories, fire the payload on at least 98.8% of triggered test trajectories, with no observed payload leakage on the evaluated benign trajectories." / "Agent built defenses, given no reference model, flag 91.4% of edited test checkpoints at a 9.7% FP rate."
  Slots touched (abstract-level, unverified):
  - S1: yes. Terminal-agent trajectories.
  - S2: yes. A trigger in the context.
  - S3: yes. Neuron edits, and defenses on weights.
  - S4: no. Detection is at checkpoint level.
  Uses internals of the agent model? yes
  Outputs a step scored against a planted step? no
  Why kept: a trigger planted in an agent's observations, with an internals-level mechanism. A WebSearch summary (#19) mentions a hidden-state probe at the trigger token; I did not verify this in the paper.

**15. DriftNet: A Dual-Head Trajectory Transformer for Detecting and Localizing Prompt Injection in LLM Agents** — Asif Pinjari, Mithun Paul Saint-Germain — 2026-09-09 — https://arxiv.org/abs/2609.10892
  Quote: "A frozen sentence encoder and four identity-free world features embed each step; the trained trunk, under two million parameters and optimized with a class-weighted joint objective over both heads, needs no access to the agent's model." / "On the task-disjoint split of the AgentDrift benchmark (12,536 trajectories, 71,024 labeled steps), with a 20-configuration sweep bounding hyperparameter sensitivity to 0.011 F1 and the test part evaluated exactly once, DriftNet reaches trajectory-level F1 of 0.983, exact injection-point recovery on 98.7% of attacked trajectories, hijacked-span IoU of 0.979, zero flags on 218 resisted attacks, and 2.9% flags on hard negatives."
  Slots touched (abstract-level, unverified):
  - S1: yes.
  - S2: yes. Injection-point labels by construction.
  - S3: no.
  - S4: yes. Exact injection-point recovery.
  Uses internals of the agent model? no. It reads text through a separate sentence encoder.
  Outputs a step scored against a planted step? yes
  Why kept: the cleanest S1+S2+S4 match without S3. It is a text-only baseline that an internals method would have to beat.

**16. AgentDrift: A Step-Labeled Benchmark of Injection-Hijacked LLM Agent Trajectories** — Asif Pinjari, Mithun Paul Saint-Germain — 2026-09-07 — https://arxiv.org/abs/2609.06972
  Quote: "Existing benchmarks measure whether such attacks succeed against live agents, and existing guard models judge a trace as a whole; no public corpus labels, step by step, where an injection enters a trajectory and which steps it corrupts." / "We present AgentDrift, a benchmark of 12,536 synthetic tool-call trajectories over five agent domains in which every one of the 71,024 steps carries one of four labels: benign, injection point, hijacked, or failed injection." / "Trajectories were generated by a single open model under category-specific protocols, enforced by a closed-vocabulary structural validator, screened by an LLM judge, and audited by hand on 1,200 trajectories; we show that the LLM judge was itself fooled by the hard negatives."
  Slots touched (abstract-level, unverified):
  - S1: yes.
  - S2: yes. The injection point is labeled by construction.
  - S3: n/a. It is a benchmark.
  - S4: yes, as a target.
  Uses internals of the agent model? n/a (benchmark). The trajectories are synthetic, so it is unclear whether an acting model's activations exist for them.
  Outputs a step scored against a planted step? yes (the labels are planted steps)
  Why kept: a step-labeled planted-injection corpus, the kind of ground truth the claim's setup needs.

**17. Causal Agent Replay: Counterfactual Attribution for LLM-Agent Failures** — Jaineet Shah — 2026-06-06 — https://arxiv.org/abs/2606.08275
  Quote: "We present Causal Agent Replay (CAR), which answers the question by intervention: it models an agent run as a structural causal model, applies a do-operation to a step, and re-executes the trajectory forward under the same stochastic policy, measuring the shift in the outcome distribution." / "We validate against synthetic structural causal models with planted ground truth: the contrastive estimator recovers the pivotal step, and Shapley recovers a two-step interaction (0.44, 0.45, ~0; efficiency sum 0.909 versus the analytic 0.91)."
  Slots touched (abstract-level, unverified):
  - S1: yes (the tool targets LLM agents).
  - S2: yes, but in synthetic SCMs rather than LLM runs.
  - S3: no.
  - S4: yes. It recovers the pivotal step.
  Uses internals of the agent model? no
  Outputs a step scored against a planted step? yes (in synthetic SCMs)
  Why kept: it checks step attribution against planted ground truth, using intervention instead of internals. Code is at github.com/jaineet17/causal-agent-replay.

**18. CausalArmor: Efficient Indirect Prompt Injection Guardrails via Causal Attribution** — Minbeom Kim, Mihir Parmar, Phillip Wallis, Lesly Miculicich, Kyomin Jung, Krishnamurthy Dj Dvijotham, Long T. Le, Tomas Pfister — 2026-02-08 — https://arxiv.org/abs/2602.07918
  Quote: "We revisit IPI through a causal ablation perspective: a successful injection manifests as a dominance shift where the user request no longer provides decisive support for the agent's privileged action, while a particular untrusted segment, such as a retrieved document or tool output, provides disproportionate attributable influence." / "Based on this signature, we propose CausalArmor, a selective defense framework that (i) computes lightweight, leave-one-out ablation-based attributions at privileged decision points, and (ii) triggers targeted sanitization only when an untrusted segment dominates the user intent."
  Slots touched (abstract-level, unverified):
  - S1: yes (AgentDojo, DoomArena).
  - S2: yes (injection benchmarks).
  - S3: no. It uses input ablation.
  - S4: partial. It attributes an action to an untrusted segment, but is scored on defense metrics.
  Uses internals of the agent model? no
  Outputs a step scored against a planted step? unclear
  Why kept: attribution of an agent action to a tool-output segment. 2608.29942 (screened) audits this family's signals.

**19. AgentSentry: Mitigating Indirect Prompt Injection in LLM Agents via Temporal Causal Diagnostics and Context Purification** — Tian Zhang, Yiwei Xu, Juan Wang, Keyan Guo, Xiaoyang Xu, Bowen Xiao, Quanlong Guan, Jinlin Fan, Jiawei Liu, Zhiquan Liu, Hongxin Hu — 2026-02-26 — https://arxiv.org/abs/2602.22724
  Quote: "Multi-turn IPI is especially challenging because injected content can persist across steps and trigger unauthorized state-changing actions only after merging with user intent. This creates a source-attribution problem" / "We propose AgentSentry, an inference-time defense that operationalizes temporal causal diagnostics through boundary-local counterfactual re-executions at tool-return boundaries."
  Slots touched (abstract-level, unverified):
  - S1: yes.
  - S2: yes (AgentDojo injections).
  - S3: no. It uses "three black-box LLM backbones".
  - S4: partial. It attributes at tool-return boundaries, but is scored on ASR and utility.
  Uses internals of the agent model? no
  Outputs a step scored against a planted step? unclear
  Why kept: an explicit step-level (tool-return boundary) source attribution of a multi-turn injection.

**20. AttriGuard: Defeating Indirect Prompt Injection in LLM Agents via Causal Attribution of Tool Invocations** — Yu He, Haozhe Zhu, Yiming Li, Shuo Shao, Hongwei Yao, Zhihao Liu, Zhan Qin — 2026-03-11 — https://arxiv.org/abs/2603.10749 (USENIX Security 2026 listing seen in WebSearch #15)
  Quote: "We propose a new paradigm, action-level causal attribution, which secures agents by asking why a particular tool call is produced." / "For each proposed tool call, AttriGuard verifies its necessity by re-executing the agent under a control-attenuated view of external observations."
  Slots touched (abstract-level, unverified):
  - S1: yes.
  - S2: yes (benchmark injections).
  - S3: no.
  - S4: partial. Scored on ASR.
  Uses internals of the agent model? no
  Outputs a step scored against a planted step? no
  Why kept: attributes a tool call to observations versus user intent through counterfactual replay.

**21. AgentTracer: Tracing Indirect Prompt Injection Attack through Fine-Grained Intention-Execution Alignment** — Zitong Yao, Jiangrong Wu, Yixi Lin, Anrui Huang, Luoyun Zhang, Yuhong Nan — 2026-10-07 — https://arxiv.org/abs/2610.09935
  Quote: "Starting from an anomalous tool call under audit, AgentTracer performs target-based pruning and backward tracing to reconstruct the attack chain and locate the injection source and injection point." / "In end-to-end experiments, AgentTracer achieves 94.17 percent injection-point accuracy and 93.56 percent path precision."
  Slots touched (abstract-level, unverified):
  - S1: yes (AgentDyn, InjecAgent logs).
  - S2: yes (successful IPI logs).
  - S3: no.
  - S4: yes. Injection-point accuracy.
  Uses internals of the agent model? no
  Outputs a step scored against a planted step? yes
  Why kept: step-level injection-point recovery without internals. The name differs by one letter from AgenTracer (2509.03312).

**22. AgentWatcher: A Rule-based Prompt Injection Monitor** — Yanting Wang, Wei Zou, Runpeng Geng, Jinyuan Jia — 2026-04-01 — https://arxiv.org/abs/2604.01194
  Quote: "To address the first limitation, AgentWatcher attributes the LLM's output (e.g., the action of an agent) to a small set of causally influential context segments." / "We conduct a comprehensive evaluation on tool-use agent benchmarks and long-context understanding datasets."
  Slots touched (abstract-level, unverified):
  - S1: partial.
  - S2: yes.
  - S3: unclear. The abstract does not name the attribution method.
  - S4: partial. Scored on detection.
  Uses internals of the agent model? unclear
  Outputs a step scored against a planted step? no
  Why kept: from the AttnTrace/TracLLM group; it attributes agent actions to context segments.

**23. Human Interventions as Labels: Localizing, Steering, and (Sometimes) Editing the Computations Behind LLM Agent Failures** — Cesare Zavattari, Alessandro Tommasi, Giuseppe Prencipe — 2026-10-15 — https://arxiv.org/abs/2610.21708
  Quote: "We treat it instead as a measurement: a label pointing at the internal computation that failed." / "First, the ask-vs-act decision is causally localizable in every eligible family: a direction learned from intervention labels flips 72-100% of held-out over-asks at a definite residual-stream depth, with site and dose chosen on training data, and random directions under the same procedure flip at most one episode."
  Slots touched (abstract-level, unverified):
  - S1: yes. A controlled agent environment.
  - S2: no.
  - S3: yes. Directions, probes and steering.
  - S4: no. It localizes to a layer depth, not a step.
  Uses internals of the agent model? yes
  Outputs a step scored against a planted step? no
  Why kept: internals-based localization of an agent decision, but along depth rather than across steps.

**24. GIF: Locally Sound Geometric Information Flow Control for LLMs** — Adam Storek, Nikolaus Holzer, Zhuo Zhang, Suman Jana — 2026-06-22 — https://arxiv.org/abs/2606.23277
  Quote: "GIF uses the LLM Jacobian and local output geometry to upper-bound the Shannon mutual information between perturbed input spans and model outputs, yielding a scalable measure computable on large models via automatic differentiation and low-rank approximation." / "GIF achieves near-perfect recall even without a downstream declassifier, outperforming attention-based baselines."
  Slots touched (abstract-level, unverified):
  - S1: partial (agentic IFC motivation).
  - S2: yes (prompt-injection benchmarks).
  - S3: yes. The Jacobian; surrogate models also transfer.
  - S4: partial. It flags input-span flows.
  Uses internals of the agent model? yes, or a surrogate model's
  Outputs a step scored against a planted step? no
  Why kept: gradient-based flow from injected spans to outputs in agent-security benchmarks.

## Screened (lower overlap)

All of these were opened (arXiv abstract, Semantic Scholar abstract, or page). Each gets one line on what it is and why it ranks lower.

Context attribution, single context:
- 2511.10720 PISanitizer (Geng et al., 2025-11-13). Attention-located injected tokens are sanitized in a long context. It is a single call, not agent steps.
- 2506.04202 TracLLM (Wang, Zou, Geng, Jia, 2025-06-04). Context traceback by perturbation-based feature attribution, used for injection forensics. It does not use internals, and works on a single context.
- 2409.00729 ContextCite (Cohen-Wang, Shah, Georgiev, Madry, 2024-09-01). Ablation-based context attribution with poisoning detection. It does not use internals, and works on a single context.
- 2504.13752 AT2, "Learning to Attribute with Attention" (Cohen-Wang, Chuang, Madry, 2025-04-18). Treats attention heads as features for token attribution. Single context; it is one of Tokengeist's back-ends.
- 2610.16349 RIFT (2026-10-12). Attention-resistance token influence, checked against token replacement. Single prompt.

Internals plus prompt injection, but detection or defense only (no source step):
- 2602.20708 ICON (2026-02-24). A latent-space trace prober plus attention steering against IPI. Detection and mitigation only.
- 2610.28988 AttnDA (Kawasaki, Lee, 2026-10-20). Attention-focus IPI detection evaluated on AgentDojo. Detection only.
- 2510.14005 PIShield (Zou et al., 2025-10-15). A residual-stream linear classifier for injection detection.
- 2606.00566 Same Payload, Different Channel (2026-05-30). Channel trust asymmetry; activation patching recovers the channel signal. No step output.
- 2609.36570 CounterSteer (Russinovich, 2026-09-29). Subtracts a residual direction from tool-result tokens. It is a defense. It notes the decision is "linearly readable at argument emission".
- 2604.24542 LCF (2026-04-27). A layerwise hidden-state runtime monitor for backdoors, jailbreaks and injection. Detection only.
- LessWrong, "Steering Role Confusion" (Kevin Zhang, Daniel Lee, Jaewoo Park, 2026-08-20), https://www.lesswrong.com/posts/uz9pFutDAT7trygM9/steering-role-confusion. Tl;dr via summarizer, may not be verbatim: "Our work provides evidence that interventions on latent role representations causally drive downstream compliance..." A multi-step ReAct agent with a role probe and steering. No step attribution.
- LessWrong, "A Mechanistic Explanation of Prompt Injection (and why you should study roles)" (charles_ye, Jasmine C., 2026-06-22), https://www.lesswrong.com/posts/d8xDGzCEYE639qqEv/a-mechanistic-explanation-of-prompt-injection-and-why-you. Tl;dr via summarizer: "We've been building a theory of how prompt injections work under the hood." Role probes flag injected spans. No step attribution in a live agent trace.

Internals in agents, but no step attribution:
- 2607.17621 AGMR (2026-07-20). Retrieval-head attention over memory segments and decision steps of an agent. Not scored against a planted cause.
- 2610.09624 Tool-call vector (2026-10-07). Transcoder and causal analysis of the call-or-not decision; extends to τ²-Bench trajectories. No step attribution.
- 2606.16364 Looking Is Not Picking (2026-06-15). Attention to tool-definition segments. Single-turn.
- 2609.36138 SAKIKO (2026-09-28). Audits steering interventions on pre-tool decisions.
- 2605.18646 Language-switching trigger circuit (2026-05-18). A backdoor-trigger circuit in a single prompt.
- 2604.17761 Contrastive attribution in the wild (2026-04-20). LRP attribution graphs for realistic LLM failures. Not agentic.
- 2602.06841 From Features to Actions (2026-02-06). Attribution methods, including IG, are unreliable for diagnosing agentic trajectories; a trace rubric localizes better.
- 2611.26221 Sightline (2026-11-19). Attention-reading data-flow summaries for LLM calls, applied to agent IFC. No planted step.
- 2410.03055 Permissive information-flow analysis (2024-10-04). Influence-based label propagation in an LLM agent setting.
- 2610.25966 Behavioral probes for information flow in LLM swarms (2026-10-19). ECS/PKS scores per node.

Failure attribution without internals of the acting agent (black-box judges or text models):
- 2604.22708 TraceElephant (2026-04-24). Full-trace failure-attribution benchmark.
- 2610.17747 Auditing Failure Attribution (Xu, Gao, 2026-10-13). Cue tests. Quote: "In one of them, error injection leaves no reasoning after the faulty step; judges fine-tuned on its labels beat GPT-4.1 by 41 points." Who&When Pro uses error injection, which is S2-relevant.
- 2610.18780 BLADE (2026-10-13). Audits information use with probabilistic LLM judgments.
- 2610.01256 DeFA (2026-10-01). Dependency-graph failure attribution.
- 2608.24361 Adaptive Influence Graphs (2026-08-25). LLM navigates a trace graph.
- 2509.13782 FAMAS (2025-09-17). Spectrum-based attribution from replays.
- 2609.04749 DCFA (2026-09-04). Causal-inspired dependency graphs plus counterfactual reasoning.
- 2606.00765 FALAT (2026-05-30). Dependency-guided search.
- 2606.03467 StepFinder (2026-06-02). LLM encodes logs, then a temporal model.
- 2608.10646 ASCon (2026-08-11). Graph-attention model over trajectory representations.
- 2607.12747 OAT (2026-07-14). One-class neural CDE over successful-trajectory latents.
- 2509.14295 Aegis (2025-09-17). An LLM manipulator injects errors into successful MAS trajectories, so the faulty steps are planted. Used to train attributors; no internals.
- 2610.17633 Executable Prefix Values (2026-10-13). Restarting from prefixes measures the decisive step; judges' labels mostly miss it. An intervention-based ground truth.
- 2611.05650 Executed counterfactual reporting standard (2026-11-03). Argues attribution to history needs executed interventions.
- 2610.41025 ReplayRCA (2026-10-29). Scores diagnoses by causal repair.
- 2608.29228 Minimal repair families via counterfactual replay (2026-08-29). Controlled DAG benchmark.
- "Lost in the Trajectory: Serial-Position Bias in LLM-as-Judge Step-Level Error Attribution on Agent Trajectories" (2026-07-01, DOI 10.1109/AIoTC71250.2026.11688433). Judges' step localization degrades with error position and with injected distractors.
- "Are Agents Listening to Each Other? Measuring What Drives Agent Actions in LLM-Based Multi-Agent Systems" (2026-08-23, DOI 10.1111/exsy.70392). Black-box per-message counterfactual attribution.
- "Containing the Cascade" (2026-07-01, DOI 10.1109/ICERA72709.2026.11666599). A fault-injection testbed in simulation.
- 2605.08715 AgentForesight; 2610.16071 Dream2Discern; 2605.28732 MemTrace. Online auditing and memory error tracing; black-box.
- 2611.23346 State-transfer auditing (2026-11-17). Root-cause localization on 240 fault-injection trajectories using harness records.

Security provenance without internals:
- 2604.23374 NeuroTaint (2026-04-25). Offline taint tracking over agent traces.
- 2608.29942 Influence Is Not Authority (2026-08-30). Audits causal-influence guardrail signals that use Llama/Gemma scorers.
- 2610.30738 AgentTriage and 2609.30830 AGATE. Deterministic provenance graphs.
- 2512.12597 AgentSHAP (2025-12-14). Monte Carlo Shapley over tools; black-box.

Backdoor and trigger positioning (S2-style triggers in observations):
- 2402.11208 Watch Out for Your Agents! (2024-02-17). Defines triggers that "appear in an intermediate observation returned by the external environment". No internals method.
- 2601.04566 BackdoorAgent (2026-01-08). Triggers planted at one stage persist and propagate across steps. No internals.
- 2610.05793 Topology-conditioned backdoors (2026-10-05). A trainable backdoor; detected by a blind audit.
- 2607.24893 Distributed backdoors in MAS (2026-07-27). Prefix detectors over text.
- 2407.15168 DRL backdoors in activation space (2024-07-21). Non-LLM RL agent.
- 2606.12896 PolicyGuard (2026-06-11). Step-level backdoor detection for RL agents via GP variance. Non-LLM.

Multi-turn conversation attribution (fails S1 by construction; logged for positioning):
- 2609.27773 MTAG-Probe (2026-08-17). Turn- and span-level evidence localization for multi-turn safety failures, with counterfactual supervision. The abstract does not say whether the probe reads internals.
- 2507.02956 Representation-engineering view of Crescendo (2025-06-29). Representations drift toward "benign" across turns.
- 2603.15684 STAR state-dependent safety failures (2026-03-15). Monotonic drift away from refusal representations across turns.

Opened and dropped as off-topic (7):
- 2610.24383 IF-MAP.
- 2607.17149 Diagnostic framework perspective.
- 2606.29279 Manufactured Confidence. Planted hedged memory is acted on as fact, with no internals.
- 2611.31063 REPA error propagation.
- 2607.21106 AttriMem.
- 2610.09493 Attribution Blind Spot (RAG).
- 2605.22719 GPT-2 IOI SAE audit.

## Leads that did not resolve

- **Aghzal, Geva, Hassan, Stein, Yao, "Understanding LLM Agents Requires a Chain of Attribution"**, Preprints.org, DOI 10.20944/preprints202610.2861.v1. The WebSearch #41 summary says it was posted 2026-10-28 and is a position paper whose pipeline includes "Localize step & component" and "Explain mechanism". preprints.org returned 403, so it is not opened.
- **Aghzal et al., "Toward Mechanistic Interpretability of LLM Agents"**: the PDF at mohamedaghzal.github.io returned 404. The related "Can Mechanistic Interpretability Help Explain LLM Agent Failures?" is 2611.18514, already found.
- **A Preprints.org paper by Scavotto (July 2026)** on judges localizing the causative step near chance. Seen only in the WebSearch #41 summary; not opened.
- **The methods ReCast (2610.11334) cites** as "Recent methods leverage LLM internal signals for failure attribution, typically using hidden states as step representations" were not identified. "CHIEF" appeared as a baseline name in the WebSearch #28 summary but was not resolved.
- **Attention Tracker (Hung et al., 2025)**, the white-box IPI detector cited by 2610.28988, was not opened. It is detection, not localization.
- **USPTO patent 12292915**, "Security for generative models using attention analysis", surfaced in WebSearch #15 and was not opened.
- **Titles seen only in Semantic Scholar AgenTracer citers (#50)**, regex-screened with no internals terms, not opened: "AgentChaosBench: Benchmarking External Fault Detection and Localization in Agentic Systems" (no arXiv ID), 2608.06790 AgentChaos, 2611.33022 RecordRoute, 2606.09071 REFLECT, 2610.06163.
- **The role-confusion paper (Ye et al., 2026)** cited by the LessWrong posts and by 2610.40396 was not opened.
- **Lazarus (2611.15118)**: the hidden-state probe on observation triggers, described in the WebSearch #19 summary, was not checked in the paper body.

## Gaps

- **Semantic Scholar.** The keyword search endpoint was not used, because it is known to return 429. The citations endpoint returned 429 on the first attempts for Who&When (#27) and AgenTracer (#36). Both worked on a later retry (#33, #50). AttnTrace showed only 11 citers, so Semantic Scholar's citation coverage may be incomplete. Citer lists were screened by regex over title and abstract, so citers with no abstract in Semantic Scholar (several had none) could be missed.
- **Seeds without citation hops.** I did not run citation hops on Attnlocate (2608.24022), MindGuard (2508.20412), DriftNet/AgentDrift or Tokengeist. These are the closest new seeds.
- **Security and NLP venues searched directly: none.** OpenReview, ACL Anthology, USENIX Security, NDSS, CCS and IEEE S&P proceedings were not searched; I reached their papers only through arXiv. IPI forensics papers often appear first at security venues.
- **LessWrong and Alignment Forum.** Site-filtered search #40 returned no forum pages. #57 returned two posts, both role-probe work with no step attribution. Coverage of forum posts is thin.
- **preprints.org and the author site.** Fetches returned 403 twice and 404 once (see Leads).
- **Page reads through a summarizer.** The LessWrong tl;drs and the two methods checks (Attnlocate HTML; Tokengeist HTML, first 100k of 224k characters) came through the WebFetch summarizer. Treat those details as unverified until someone reads the PDFs.
- **Vocabularies reached thinly or not at all:**
  - "blame assignment" and "responsibility attribution" as standalone terms.
  - Influence functions over in-context steps.
  - Taint tracking that uses neural signals, beyond GIF, Sightline and NeuroTaint.
  - "trajectory-level SHAP" with log-probabilities.
  - Non-English venues and patents.
  - RL credit assignment (#51) was searched, but it returns training methods that are never scored against planted steps, so I did not mine it further.
- **GitHub.** The internals-specific repository queries returned 0 hits (#37). The broader queries returned black-box failure-attribution repositories only.
- **Tags.** All slot tags are read from abstracts, except the two methods checks noted above. "Uses internals" and "outputs a step scored against a planted step" need confirming in methods sections.
