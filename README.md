# scooping

A method, a local tool and a Claude Code skill for deciding whether a research direction
has already been done ("scooped"), with evidence someone else can check.

The method: write the claim as four slots (object, ground truth, method, measurement),
search in logged slices, and judge each close paper from its methods section, one quoted
sentence per slot. A paper takes the claim only if it matches all four slots in the same
experiment. An unverified match is grounds to verify, never to shelve. When a match is
confirmed, the claim is restated around what the matching paper cannot do.

## Layout

- `scope/`, `bin/scope`: the knowledge-base CLI. It runs searches, stores every result in a
  local DuckDB file (`kb/scope.duckdb`, not in this repo), logs each query with its counts,
  and prints only results that are new to the check and pass a screen. This keeps the
  model running the check from reading raw search pages. `bin/scope -h` lists commands.
  Design notes: `scope-tool-brainstorm.md`.
- `skill/scoop-check/`: the Claude Code skill that runs the procedure through `scope`.
  `references/` holds the templates, source notes, judgment lessons and a worked example.
- `checks/<slug>/`: one folder per check (`bin/scope check new <slug>`).
- The first check (interpretability of agent decisions against planted ground truth) lives
  at the root: `claim.md`, `verdicts.md`, `search-log.md`, `positioning.md`, `CARD.md`,
  `threads.md`, `recall/`.
- `backtests/`: the skill tested on a case with a known answer (`T-008/`: prompt, answer key,
  graded result).

## Sources `scope` can search

arXiv (keyword, author, last-author census, abstracts, full text), OpenReview (including
whole venues), Semantic Scholar forward citations, OpenAlex (works, institution and
per-institution author counts), the ACL Anthology (local copy with abstracts), and Google
Scholar pages pasted by the user (Scholar blocks automated queries). DBLP is not wrapped:
its API sits behind a bot challenge. What works and what fails at each source:
`skill/scoop-check/references/sources.md`.

## Setup

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
bin/scope check new my-check
```

The skill and the CLI assume the repo is cloned at `~/code/scooping`. To use the skill in
Claude Code, link it into your skills folder:

```bash
ln -s ~/code/scooping/skill/scoop-check ~/.claude/skills/scoop-check
```

Downloaded pages are cached under `kb/cache/`; they are treated as untrusted data and only
parsed.

## License

AGPL-3.0-or-later (`LICENSE`). If you distribute a modified version, or run one as a
network service for others, you must release its source under the same license.
