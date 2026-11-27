# Claim C — draft v3 (2026-11-27)

v3 replaces v2 (kept below). Under the claim owner's decision that a reader model's
internals count, ReCast (2610.11334) answers v2. v3 asks what ReCast cannot: whether
access to the acting agent's own activations adds anything beyond a reader model or the
text.

## The claim

No published paper or public post tests, on LLM agent runs where a cause was planted at
a step the experimenters chose, whether the acting agent's own internal activations
locate that step better than a separate model reading the run, or the text of the run
alone.

## The four slots

| Slot | What must be true of the candidate | Does not match |
|---|---|---|
| **S1 Object** | As in v2: a decision by an LLM agent acting in a loop, with at least two earlier steps. | A single generation; a multi-turn chat with no actions. |
| **S2 Ground truth** | As in v2: the cause was planted at a chosen step, so the correct step is known without any method. | Human or LLM step labels; another method's output; oracle labels over ordinary runs. |
| **S3 Access** | The step is located from the **acting agent's own internals**: activations recorded during the run, or recomputed by the same model on its own run (what Tokengeist calls a matched generator). | Only a different model's internals (a reader model), or only text or black-box methods. |
| **S4 Measurement** | The own-internals localizer is scored on picking the planted step. | Detection, forecasting, or layer-level localization. |

**The comparison arms count toward positioning, not toward the match.** v3's
contribution is the comparison: own internals against a reader model and against text, on
the same runs. A candidate that meets S1–S4 without any comparison arm still counts as a
match, because adding those arms is cheap. The own-internals result is the part that can
be scooped.

**Why S3 is not the old boundary 2 brought back.** v2 asked whether any internals find the
step, and the claim owner ruled that a reader's do. v3 asks how much the agent's own
computation adds over a reader. A paper that has only reader internals cannot answer
that, whatever it scores. ReCast becomes the reader arm of the comparison.

## Verdict rules

As in v2: "same question" needs all four slots, each with a methods quote, confirmed by a
second read. All four slots must be matched in the same experiment. Three of four is
positioning.

---

## Superseded: draft v2 (2026-11-27)

The claim the scoop check tests. Every candidate paper or post is compared against
the four slots below, using a quote from its methods section for each slot. If any
slot is unquoted, it counts as unmatched.

v2 replaces v1 (kept at the bottom of this file). The change: v1 asked whether an
internals method can recover a planted cause in an agent at all. v2 asks whether it
can say **which step** of the agent's trajectory carried the cause. The nearest work
read against v1 (2611.10620 §10.2) detects that a planted cause is present, and does
not localize it to a step.

### The claim

No published paper or public post tests whether a method that reads or intervenes on
an LLM agent's internals can say which earlier step of a multi-step trajectory caused
the agent's decision, in a setup where the experimenters planted the cause at a step
they chose, so the right answer is known without the method.

### The four slots

A candidate answers the same question only if it matches **all four**.

| Slot | What must be true of the candidate | Does not match |
|---|---|---|
| **S1 Object** | A decision by an LLM agent that acts in a loop: the model takes actions (tool calls or environment actions) and receives inputs from outside itself (tool outputs, observations, other agents' messages) between calls. At least two such steps come before the decision. | A single generation, including a single chain of thought. A multi-turn chat in which the model takes no actions. |
| **S2 Ground truth** | The experimenters put the cause into a step they chose (for example, content in the tool output at step k, or a trigger that a fine-tuned behaviour responds to), so which step carries the cause is known without the method under test. Content placed in context counts. | Step labels from human annotators or LLM judges. Labels produced by another interpretability method. Failures that happened naturally and were labelled afterwards. |
| **S3 Method under test** | A method that reads or intervenes on the internals of the agent model that made the decision: probes, activation patching, attention-based or gradient-based attribution, SAEs/transcoders, attribution graphs, steering. | Black-box methods: LLM judges, reading the chain of thought, resampling or replaying steps, editing the text of a step. Internals of a different model, such as a judge that reads the trajectory. |
| **S4 Measurement** | The method outputs a step, or a ranking or score over steps, and is scored on whether it picks the planted step (accuracy, rank of the planted step, AUROC over steps). | Detecting that a planted cause is present somewhere in the run without naming the step. Forecasting the agent's later action. A step-importance map that is never scored against a planted step. |

**Slots describe the question, not the quality of a design.** Design choices that
would make our version better than a candidate (a counterfactual check that the
planted step really drives the decision, distractor steps that look like causes but
are not, several planted steps per run) go in positioning, not in a slot. A candidate
that asks the same question with a weaker design still matches.

### Verdicts

- **Same question:** all four slots matched, each with a methods quote, confirmed
  by a second read. This is the only verdict that can shelve the direction.
- **Overlaps:** some slots matched. The default whenever the first bar is not met.
  Recorded with which slots match and which do not, so it can be positioned against.
- **Different:** no slot matched on reading. Dropped, with one line why.

All four slots must be matched by the same experiment. Slots matched in different
experiments of one paper count as overlaps. (This rule was already applied under v1,
to 2610.05295; it is written down here for the first time.)

A paper that matches three of four slots is a positioning problem, not a scoop.

### Boundaries drawn with candidates already in view

These lines were written after I had read the abstracts of the papers they exclude.
A boundary drawn that way can be drawn to dodge a paper, so the second read should
judge each one on its merits:

1. **S1 excludes a single chain of thought.** Thought Anchors (2506.19143) and The
   Point of No Return (2605.17113) localize steps inside one reasoning trace. On this
   line they go to positioning. The reason for the line: in an agent loop the cause
   can enter from outside the model at a step the experimenter controls, which a
   single generation does not have.
2. **S3 excludes the internals of a model other than the agent.** 2610.28811 probes
   a judge model that does failure attribution. On this line it goes to positioning.
   The reason: the claim is about explaining the agent's decision from the agent's
   own internals, which was also the intent of v1.

### Second read of the two calls K = 0 rests on (T-004, 2026-11-27)

This reread was done by the same reader who made the first calls, arguing the other
side on purpose. It is not independent, and the final call belongs to the person whose
claim this is.

**Call 1: a frozen reader model's internals are outside S3 (ReCast, 2610.11334).**
- *Case for counting it.* ReCast reads hidden states and outputs the planted step on
  Who&When Pro, scored by Hit@1. To a reviewer skimming it, that looks like "internals
  find the planted step". v1's S3 said "model internals" without saying whose.
- *Case for excluding it.* v1's claim, written before ReCast was seen, says "a cause
  that was deliberately planted in an LLM agent" and asks whether interpretability can
  recover it. That is about the agent's own computation. In Who&When Pro the agents are
  GPT-4.1 and Gemini 3 Flash (2607.09996 App. G.2), so ReCast's Qwen reader can only
  see the text of the run. Its activations show what a reader notices in the text, not
  whether the agent's decision carries a trace of the step.
- *Kept.* ReCast is the nearest work and becomes a baseline: run a reader model on the
  same planted runs and compare it with the agent's own activations. If the reader does
  as well, the own-internals result adds nothing beyond monitoring, and that would be
  a finding.

**Call 2: an oracle over ordinary runs is outside S2 (2605.25310).**
- *Case for counting it.* The ground truth (which earlier tool output supplies a later
  call's argument) is known without the probe, and the probe reads the agent's own
  residual stream, edge by edge. The question is very close.
- *Case for excluding it.* The planting requirement was already in v1 ("put there on
  purpose"), so this line was not drawn to avoid the paper. There is also a difference
  in the question itself, not only in design quality. The oracle captures only causes
  that are copied word for word into the arguments. A planted cause can be an
  instruction or a fact that changes which action is taken without being copied
  anywhere, and planting lets the experimenter check by removal that the step really
  drives the decision. 2605.25310 itself reports that "the agent's realised tool call
  does not move" under its patching.
- *Kept.* 2605.25310 shows that step-dependency structure is linearly readable from an
  agent's residual stream, which supports feasibility. Verbatim copying becomes one
  condition of the planted design, alongside causes that are not copied.

**If either call is reversed:** reversing call 1 makes K = 1 (ReCast). Reversing call 2
makes K = 1 (2605.25310). Either way the direction would need restating around what
that paper does not do.

**Claim owner's decisions (2026-11-27):**
- Call A (black-box excluded): kept. "how an agent is involved does count."
- Call B (reader model excluded): **reversed.** Asked whether a separate model's
  activations reading a GPT-4.1 transcript tell you anything about how GPT-4.1 decided:
  "yes, it would." S3 now counts the internals of any model, not only the agent's.
- Call C (text matching is not planting): kept, on my reading of "both are valuable to
  have" as two different questions. Confirmed by the owner, 2026-11-27: "Yes, two
  questions".

**Consequence:** ReCast (2610.11334) matches all four slots on a methods read
(`verdicts.md`), so claim C v2 is taken under these decisions. Second read of that
verdict still pending. The other reader-model failure-attribution methods (SOAP,
MASPrism, OAT, ASCon, LTS) need re-screening for planted labels.

### Open decisions

1. **Black-box methods do not count for S3.** This was the v1 default and v2 keeps
   it. v2 depends on it: work that plants a fault at a known step and scores LLM
   judges against it exists (Who&When Pro 2607.09996, 2608.20627, AgenTracer
   2509.03312; abstract level, to be read). If black-box methods counted, those
   papers would likely match all four slots. Every verdict row records whether the
   method is black-box, so this decision can be reversed without rereading.

---

## Superseded: draft v1 (2026-11-27)

Superseded the same day. Against v1, 4 candidates were read at methods level, and 1
(2611.10620 §10.2) matched all four slots on a first read. No second read was done.
The user chose to narrow the claim to "which step" (option (a)) instead of finishing
the v1 check, so whether 2611.10620 answers v1 is still unconfirmed. Verdicts against
v1 are in `verdicts.md`.

**Claim (v1):** No published paper or public post tests whether a mechanistic
interpretability method can recover a cause that was deliberately planted in an LLM
agent, where the decision that cause drives unfolds over a multi-step trajectory, and
the planted cause is known independently of the method being tested.

| Slot | What must be true of the candidate | Does not match |
|---|---|---|
| **S1 Object** | The thing explained is a decision by an LLM agent that depends on two or more earlier steps (actions, tool calls, or reasoning steps). | Explaining a single forward pass or a single-turn answer. |
| **S2 Ground truth** | The cause was put there on purpose (fine-tuning, compiled weights, construction, or environment design) and is known without using the method under test. | Ground truth from human labels, or from another interp method's output. |
| **S3 Method under test** | A method that reads or intervenes on model internals: probes, patching, SAEs/transcoders, attribution graphs, steering. | Black-box methods (open decision; written as do not count). |
| **S4 Measurement** | The outcome measured is whether the method recovered the planted cause (a rate, a precision, a pass/fail per case). | Showing that the method produces an explanation, without scoring it against the planted cause. |

Gap found in v1 while reading: S2 accepted an instruction in the prompt as a planted
cause without saying so. v2 accepts content placed in context explicitly, because in
v2 the thing planted is the step, and placing content at a chosen step is the direct
way to plant one.
