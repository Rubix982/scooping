---
name: scoop-check
description: Decide whether a research direction has already been done ("scooped"), with evidence an advisor or reviewer can check, and record the thinking that leads to a restated direction. Use whenever the user asks "has this been done", "am I scooped", "is this novel", "check prior art for my idea", "who else is working on this", wants a novelty or positioning statement for advisors, reviewers or a proposal, finds a paper that might take their idea, or wants to restate a direction after overlapping work turns up. Built for mechanistic interpretability. Defaults to a quick check when only the user will read the result, and runs the full procedure (coverage passes, positioning statement) when advisors, reviewers or a proposal will. Runs a claim-as-slots check through the local `scope` knowledge-base CLI: logged searches, methods-level verdicts, an asymmetric rule (an unverified match is grounds to verify, never to shelve), boundary calls handed to the user, and restatement.
---

# Scoop check

A scoop is decided at the level of a specific question, not a topic. "Nobody does
interpretability of agents" is a field-map claim; "nobody locates a planted step from the
acting agent's own activations" is a scoop claim. This skill turns a direction into a
claim of the second kind, checks it with evidence someone else can rerun, and keeps going
until the direction stands or has been restated around the work that took it.

Two failures it exists to prevent, both seen in real projects:
- **False scoop.** A paper read from a search snippet looked like the same work; it was
  not, and an open question was dropped.
- **False opening.** A "suspected empty cell", never checked, shown to advisors.

The rule between them: **shelving needs stronger evidence than proceeding.** An unverified
match is grounds to verify, never to shelve.

## Quick or full: decided by who reads the result

Most checks are for the user alone: is this idea already taken, before a week goes into
it? Those run **quick**. A check whose result someone else will read (advisors, reviewers,
a proposal, a related-work section) runs **full**. Decide from the request. If it names no
other reader, run quick and say so in the first line of the closing message. A quick check
can be upgraded to full later under the same slug, since the knowledge base keeps every
query and verdict.

| | Quick | Full |
|---|---|---|
| Claim as slots, both outcomes, before searching | yes | yes |
| Recall | 12–20 queries over at least three sources (arXiv, OpenAlex, and ACL or OpenReview), plus forward citations of the nearest one or two papers | sliced recall, possibly delegated, then every coverage pass in step 6 |
| Verdicts | methods reads for the nearest few, light reads for the rest | methods reads for every close candidate, and a second read for any "same" |
| Boundary calls handed to the user | yes | yes |
| Restate on a match | yes | yes |
| Screen found-but-unjudged papers before closing | yes | yes |
| Positioning statement, legibility census | no; the closing message carries the result | yes |
| Rough size | the T-008 backtest: about 20 queries, 7 minutes | whatever coverage needs |

The rules that decide a verdict are the same in both modes: the asymmetry rule, the
same-experiment rule, a methods quote for every slot before "same", and boundary calls
handed to the user. Quick mode saves time by searching less, never by judging more
loosely. So a quick check ends with "open on a quick check" and a list of what it skipped,
never with "nobody has done this".

Forward citations are in quick mode because in the backtest the nearest paper turned up
only among the citers of an older one; keyword search missed it.

## The knowledge base does the searching

All searching and reading goes through the `scope` CLI at
`~/code/scooping/bin/scope`. It runs the query, stores every result in a DuckDB knowledge
base (`~/code/scooping/kb/scope.duckdb`) that persists across checks, logs the query with
its counts, and prints only results that are new to this check and pass a screen. Do not
fetch search pages, APIs or papers with curl or WebFetch and read the raw output: that
spends tokens on pages the KB would have stored and filtered, and leaves the query out of
the log. Use WebSearch only for what the CLI cannot reach (lab pages, blogs, LessWrong),
and record those with `scope logq` and `scope add`. Run `scope <command> -h` for options.

| Need | Command |
|---|---|
| start a check | `scope check new <slug>` (folder `~/code/scooping/checks/<slug>/`, stub files) |
| keyword search | `scope search arxiv <slug> "<query>" [--field abstract\|title] --screen "<regex>"` |
| journals, proceedings, venues off arXiv | `scope search openalex <slug> '"<phrase>" <word>' --since <YYMM> --screen "<regex>"` |
| ACL, EMNLP, NAACL, Findings, workshops | `scope search acl <slug> "<regex over title+abstract>" --since <YYMM>` (local copy of the Anthology) |
| a whole venue | `scope search openreview <slug> <terms…> --group <venue id> --screen "<regex>"` |
| people's recent work | `scope search authors <slug> <names or names.txt> --since <YYMM> --screen "<regex>"` |
| find labs from data | `scope census "<phrase>" --from <date>` (arXiv last authors); `--source openalex [--country US]` (institutions), then `--institution "<name or I-id>"` (people there); sweep them with `search authors` |
| forward citations | `scope search cites <slug> <arXiv ids…>` |
| Google Scholar | user pastes pages under `## N` headings → `scope search scholar <slug> <file>` |
| already known? | `scope seen "<id or title fragment>"` (shows verdicts from any check) |
| abstract, key sentences | `scope abstract <ids…> --terms "<slot regex>"` |
| methods read | `scope grep <id> --terms "<slot regex>" --max 8` (cached full text, with section headings; appendices included; records the arXiv version read, `<id>v1` for an older one) |
| record a verdict | `scope verdict <slug> <id> --version vN --s1 … --s4 … --verdict same\|overlaps\|different --read methods\|light --quote "S2: …"` |
| outside finds | `scope add <slug> --title … --url …`, `scope logq <slug> --source websearch --query … --n …` |
| progress, files | `scope status <slug>`, `scope report <slug>` (writes `search-log.generated.md`, `verdicts.generated.md`) |

The screen regex is the main token control: write it from the slot terms. Repeat
`--screen` to require several at once (one per slot works well). `--show` caps the lines
printed; `scope hits <slug> --qid N [M …] --unjudged --screen …` re-lists stored results
later, without papers already judged, with different screens if the first were too tight.
Never dump stored records with ad-hoc scripts; if a filter is missing, it belongs in the CLI.

## Where the work lives

`scope check new <slug>` creates `~/code/scooping/checks/<slug>/` with `CARD.md`,
`claim.md`, `search-log.md` (gaps and coverage notes), `verdicts.md` (longer notes),
`threads.md` and `recall/`. Templates for each file: `references/templates.md`. The
user's conventions apply: one card open at a time, side questions as one line in
`threads.md`, never generate a citation from memory, never put the user's name or
affiliation in a query or in anything published.

## The procedure

### 1. Write the claim as slots

Ask what the user would actually claim in a paper. Write one sentence beginning "No
published paper or public post…", then split it into four slots (object, ground truth or
data, method or access, measurement), each with a "does not match" column. Slots define
the question; design quality belongs in positioning. Write the card before searching,
with both outcomes stated. Before anything else, `scope seen` the papers the user already
knows about: an earlier check may have judged them.

### 2. Recall, logged

Search in slices that come at the slots from different directions (for example: the
ground-truth method in any setting; the object with any method; venues off arXiv and work
in flight). One `scope search` per query, each with a screen built from the slot terms.
Note sources you could not reach in `search-log.md` under Gaps as you go. What works at
each source and what fails: `references/sources.md`.

In full mode, recall can be delegated to subagents, one per slice, if they also use
`scope` with the same slug. Tell them not to judge scoop, and where to write. In quick
mode, run it inline within the budget in the table above.

### 3. Verdicts from methods sections

For each close candidate, `scope grep` its full text with the slot terms and take one
quoted sentence per slot. Record it with `scope verdict`, which stores the version of the
text you read. Verdicts are "same" (all four
slots, in the same experiment, then a second read), "overlaps" (record which slots and
why), or "different". A light read (abstract plus a keyword grep) can only produce
"overlaps". Grep before reading: most verdicts need a handful of sentences, not a paper.

### 4. When a verdict turns on how a slot is read

Do not settle it quietly. Write the boundary next to the slot, say if it was drawn after
seeing the paper it excludes, and give the user one plain question per call with what each
answer means ("If yes, paper X takes the claim"). Record their words in `claim.md`. A
reread by the same reader is not independent; say so.

### 5. If something matches: restate, don't shelve

A confirmed match closes that version of the claim, not the direction. Restate around what
the matching paper cannot do, and check that the new claim is worth doing on its own (the
user's test: would it still matter to the field?). Good restatements turn the match into a
baseline. Keep every version in `claim.md` with the paper that forced it. If the new claim
is a comparison ("X versus Y"), a paper doing X alone still counts when adding Y is cheap.
Then repeat steps 3–4 under the new version (`--version v2`, …); the KB keeps everything
already seen.

### 6. Coverage passes before any "nobody has done this" sentence (full mode)

In quick mode, skip this step and list each pass under what was not reached.

Keyword search misses vocabulary. Before the statement goes out, add:
- **people:** authors of the nearest papers, plus labs found from data (`scope census`, by
  last author or by institution, then `scope search authors`), not from memory;
- **venues off arXiv:** OpenReview workshops and submissions (`--group`), the ACL
  Anthology (`search acl`), journals and proceedings through OpenAlex (`search openalex`),
  and the others listed in `references/sources.md`;
- **forward citations** of the nearest papers (`scope search cites`);
- **Google Scholar**, run by the user from a query file you write (keyword queries two
  pages deep, "Cited by" pages in full; no "Cited by" link means zero), then imported.

Say plainly what was not reached.

### 7. The positioning statement (full mode)

In quick mode, skip this; the closing message carries the result.

Write `positioning.md` only after a card closes. Skeleton in `references/templates.md`.
It opens with what the reader is asked to decide, tells how the question got here (each
restatement and the paper behind it, in order), groups the nearest work by the condition
each misses, says what the result rests on and who made each call, names the baselines the
work must beat, and ends with scoop risk and unreached sources. Then run the
`research-legibility` census on it.

## Closing a check

First, screen what was found but never judged:
`scope hits <slug> --unjudged --screen "<object terms>" --screen "<variable terms and
synonyms>"`. Write the variable screen wide (for a distance variable: hop, multi-hop,
path, distance, neighbour). Judge every hit that names both, even if only to record
"different", and note the pass in `search-log.md`. `scope status` shows how many papers
are still unjudged.

The card closes with a number: "Of N candidates, K meet all four slots of claim C vN."
Run `scope report <slug>`, update `threads.md`, and tell the user, in this order: the
count, what it rests on (including any boundary call, as a plain question), what is
unread, numbered next steps with a recommendation. A quick check opens the message with
"Quick check:" and, when the direction is still open, offers the full passes as a next step.

## Judgment notes

`references/judgment.md` holds the lessons from the first full check (flagged boundaries,
owner decisions, the same-experiment rule, light reads, trivial baselines, recall versus
verdicts). Read it before step 3 the first few times. `references/worked-example.md`
summarises that check (slug `agent-step-localization` in the KB) and points to its files.
