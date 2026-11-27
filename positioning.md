# Positioning: does an agent's own computation show which step caused its decision?

_Draft, 2026-11-27. One source could not be read (LTS, at the end). Everything else
listed under "How far the search went" has been checked._

**What I am asking you to decide.** Whether the question below is worth the work as
stated, and whether the unread LTS submission should hold it up.

Numbers like 2607.09996 are arXiv identifiers. Names in backticks (`claim.md`,
`verdicts.md`, `search-log.md`, `recall/`) point to my working notes, where every quote,
query and verdict is recorded. The argument below does not need them.

## The question

When an LLM agent makes a decision partway through a multi-step task, does the agent's
own internal computation show which earlier step caused that decision, and does it show
this better than a separate model reading the same run, or the text of the run alone? We
would test it on runs where we planted the cause at a step we chose, so the right answer
is known before any method is run.

The claim I checked is that nobody has published this test.

## How the question got here

I started broader and narrowed twice, each time because of a specific paper.

The first version asked whether any interpretability method can recover a cause planted
in an agent. The nearest paper, 2611.10620, detects that a planted goal is present in a
committee of agents, which comes close. So I narrowed the question to *which step*
carried the cause.

That version, with four conditions (agent loop, cause planted at a chosen step, method
reads internals, scored on picking the step), met no paper outright. It came down to
whether a separate model reading the transcript counts as "internals". ReCast
(2610.11334) finds the planted step on the Who&When Pro benchmark from the hidden states
of a frozen reader model. My first check excluded that. On reflection I decided that a reader's activations do
tell you something about how the agent decided, and on that reading ReCast answers the
"which step" question.

What ReCast cannot do is compare. Its benchmark agents are GPT-4.1 and Gemini 3 Flash, so
their own activations are unavailable. That gap is the current question: how much does the
agent's own computation add over a reader, or over the text?

## Has anyone done it?

To count as the same work, a paper had to:

1. study a decision by an agent acting in a loop, with at least two earlier steps;
2. use runs where the cause was planted at a chosen step;
3. locate the step from the acting agent's own internals;
4. score that on whether it picks the planted step.

A paper meeting all four without comparing against a reader or text still counts,
because those comparisons are cheap to add.

**Of 65 candidates, none meets all four** (`verdicts.md`). The nearest work falls into
three groups, by what each lacks.

**Planted step and step scoring, but not the agent's own internals.** ReCast (reader
model, above). Who&When Pro (2607.09996) injects an error at a chosen step of 12,326 runs
and scores LLM judges; step accuracy "falls from 94% on short traces under 3K tokens to
50% on traces exceeding 12K tokens". DriftNet (2609.10892) recovers the injection point in
98.7% of attacked runs in the synthetic AgentDrift corpus (2609.06972) using only text.
Two trace-reading tools (AgenTracer 2509.03312, AgentTracer 2610.09935) and an injected-
fault benchmark for agentic retrieval (2608.20627) are similar. These become the reader
and text baselines.

**The agent's own internals and a planted cause, but not scored on the step.** The Agent
Knew (2610.17301) plants one decisive fact at a known step and reads the agent's residual
stream, but scores whether the readout forecasts the later action. Three prompt-injection
studies (2610.24048, 2610.18408, 2608.02657) probe the agent's activations to forecast
compliance or detect an injection, and two more do the same for planted prompt injections
in tool-using and computer-use agents (2610.37679, 2606.22864). A file-system agent study,
"Felt, Not Granted" (found only through OpenAlex; I did not find an arXiv copy), tests an internal probe
on each proposed deletion against an LLM-judge baseline. Several of these do compare
against text monitors. None asks which step caused the decision.

**The agent's own internals and step scoring, but labels that were not planted.**
Tokengeist (2607.22610) traces which earlier turns an answer rests on, using the attention
of the model that generated the conversation, and compares it with a separate reader. It
reports that "the ranking of methods is the same whether the attribution model matches
the generator", but its correct answers were written by LLMs. A residual-stream study of
tool calls (2605.25310) decodes from the agent's own activations which earlier tool output
supplies a later call's arguments, scored against links found by text matching.

## What the result rests on

- **Black-box methods do not count as interpretability of the agent.** I made this call
  explicitly. They enter the design as the text baseline.
- **The comparison is the question.** A paper with only a reader model cannot answer it,
  however well it scores. That is why ReCast, which answered the earlier version, does not
  answer this one.
- **Text matching is not planting.** The tool-call study covers only causes copied word
  for word. A planted cause can change which action is taken without being copied
  anywhere, and planting lets us remove the step and check that the decision changes.

## What the work would add, and the obvious objection

No public dataset can support the test. Who&When Pro's runs come from closed models and
AgentDrift is synthetic, so neither has activations from the acting agent. The work needs
new planted-step runs from an open-weight agent, with activations saved. That dataset
would be usable by others whichever way the comparison comes out.

The objection: text alone already finds injected steps 98.7% of the time, and on existing
failure benchmarks a rule that always names the last step is "correct 67% to 96% of the
time" (2610.16661). So accuracy on easy plants cannot be the point. The design has to
include causes that text cannot reveal, such as a plain fact or a benign-looking
instruction that changes the decision, and it has to beat the last-step rule. If the
agent's own activations do no better than a reader or the text, that is a result: it would
mean access to internals adds nothing to this kind of localization. That kind of
result has already been reported for a related task. A pre-registered study posted on
Zenodo, "No Better Than Behavioral", asked whether a coding agent's residual stream warns
earlier that a run is drifting off course than a cheap signal from its tool use does. On
99 runs, the residual-stream readout reached an AUROC of 0.695 against 0.688 for the tool
signal, a difference the authors could not distinguish from zero. Nothing was planted there
and the task is forecasting, not finding a step, so it does not answer our question. I have
read only its abstract.

One design rule: the target is the step where the cause entered. The planted content
appears only there, removing it must change the decision, and later steps that carry the
cause forward are scored separately. One reason: 2611.18514 saw an agent recover a value
from its own action history after the original was corrupted.

## Scoop risk

- **Tokengeist is one step away.** Its matched-generator mode on runs with planted steps
  would answer most of this. Its authors were included in the author sweep
  (`recall/E-author-sweep-names.txt`) and are people to watch.
- **Others are calling for it.** Aghzal, Geva, Stein and Yao (2611.18514) write that "no MI
  benchmarks exist for agent applications" (MI meaning mechanistic interpretability) and
  that one needs ground truth for "what triggered such failures". A newer preprint by the
  same group, "Understanding LLM Agents Requires a Chain of Attribution", reads as a
  position paper from its abstract.
- **The area is moving fast.** Most of the nearest work appeared between August and
  November 2026.

## How far the search went, and what it did not reach

Covered: arXiv, Semantic Scholar citations, OpenReview, the ACL Anthology (titles and
abstracts), OpenAlex (4 queries; it indexes journals, proceedings and preprint servers), Google Scholar
(14 queries), the 129 papers of the NeurIPS 2026 "Interpreting Agent Behavior" workshop,
the USENIX Security, NDSS and IEEE S&P 2026 programs, lab blogs and LessWrong, the recent
arXiv listings of 89 researchers (including lead authors of interpretability papers at
most of the 31 US universities with the most such papers; Berkeley and CMU are thin), and
forward citations of the nearest papers.

Not reached:
- **LTS** (OpenReview fgfKz9Qhpx, an anonymous ACL Rolling Review submission). It finds
  failed steps from "cached step-level representations" and checks against injected
  faults. If those are the acting agent's own representations, it could meet all four
  conditions. The PDF is behind a bot check.
- **The Aghzal et al. preprint** above (the page returned a 403).
- Lab pages and talks of the groups swept (only their arXiv listings were checked), X,
  model system cards, and the CCS 2026 program.
