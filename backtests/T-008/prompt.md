# T-008 backtest — run instructions

Tests whether the scoop-check skill and the `scope` CLI reach the right verdict on a case
whose answer is already known, without being told it. The answer key is in
`answer-key.md` next to this file. Do not paste it, and do not open it in the test
session.

## Launch (in a terminal, not this session)

The test session has to start somewhere that has no project memory and no files that
mention the answer. `~/code/scooping` fails both: its memory and its CARD.md and
threads.md name the paper. So start it from an empty folder, with a separate knowledge
base so a wrong verdict cannot leak into the real one:

```bash
mkdir -p ~/code/scoop-backtest && cd ~/code/scoop-backtest
SCOPE_DB=~/code/scooping/kb/backtest.duckdb claude
```

When it finishes, note the session's total tokens and wall time (`/cost`), then come back
here and say "grade T-008".

## Prompt to paste

```
I need a scoop check before I spend more time on this, and my advisors will read the result.

The direction: when you edit a single fact in a language model with a locate-and-edit
method (ROME, MEMIT and similar), the edit also changes the model's answers to other
facts. I want to test whether a fact's out-degree, meaning the number of other facts in a
knowledge graph that depend on it, predicts how far the edit spreads to those related
facts. The independent variable is out-degree, counted over a fixed edge-type vocabulary.
The outcome is the spread: how many related facts change, and by how much.

Earlier I wrote myself a note that KnowledgeSmith (arXiv 2510.02392, ICLR 2026) "already
tested the out-degree hypothesis" and that I shouldn't re-derive it. I'm not sure that note
was right. Has this been done?

Use the scoop-check skill. Use the slug outdegree-edit-spread. Work only in the check
folder the skill creates. Do not open anything under ~/code/open-concept-lab or any other
project folder, since those hold my old notes on this question and I want an independent
answer. Keep token use low.
```

## What to record afterwards

- Total tokens and wall time.
- Whether the session stayed inside the CLI. Look for curl, WebFetch or raw page reads in
  the transcript; `scope status outdegree-edit-spread` shows how many queries were logged.
- The verdict on 2510.02392 and the quotes it rests on:
  `SCOPE_DB=~/code/scooping/kb/backtest.duckdb ~/code/scooping/bin/scope report outdegree-edit-spread`
