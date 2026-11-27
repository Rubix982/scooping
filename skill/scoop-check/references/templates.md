# Templates for a scoop check

One folder per check, created by `scope check new <slug>` at `~/code/scooping/checks/<slug>/`.
Query logs and verdict tables live in the knowledge base; `scope report <slug>` writes them to
`search-log.generated.md` and `verdicts.generated.md`. The hand-written files below hold what the
KB does not: the claim, judgment calls, gaps, notes and the positioning statement.

```
<slug>/
├── CARD.md          the open card for this check (six fields), closed with a number
├── claim.md         the claim as slots, every version kept, owner decisions recorded
├── search-log.md    every query, source, date, count; gaps; coverage passes
├── verdicts.md      one row per candidate per claim version, with methods quotes
├── positioning.md   the statement for advisors/reviewers (only after a card closes)
├── threads.md       side questions, one line each
└── recall/          raw logs from recall passes (agents write here), pasted Scholar pages
```

## claim.md

```markdown
# Claim C — draft vN (YYYY-MM-DD)

<one paragraph: what changed from v(N-1) and which paper forced it>

## The claim
No published paper or public post <does X>, where <conditions in plain words>.

## The four slots
| Slot | What must be true of the candidate | Does not match |
|---|---|---|
| S1 Object | … | … |
| S2 Ground truth / data | … | … |
| S3 Method / access | … | … |
| S4 Measurement | … | … |

Slots describe the question, not the quality of a design. A candidate that asks the same
question with a weaker design still matches. All four slots must be matched in the same
experiment. Three of four is positioning, not a scoop.

## Boundaries drawn with candidates already in view
1. <line> — drawn after reading <paper>. Reason: <…>. Second read should judge it.

## Claim owner's decisions (date)
- Call A (<line>): kept / reversed — "<owner's words>"
- Consequence: <which verdict changes>

---
## Superseded: draft v(N-1) … (kept verbatim below)
```

## verdicts.md

Summary table per claim version, newest version first:

```markdown
| # | Paper (arXiv id, short name) | S1 | S2 | S3 | S4 | Verdict |
|---|---|---|---|---|---|---|
| 1 | 2607.09996 Who&When Pro | yes | yes | **no (black-box)** | yes | overlaps, 3/4 |
```

Then per candidate: date, authors, one methods quote per slot (copied, not paraphrased),
and one line on what it does not do. Mark "light read" when only the abstract plus a
full-text keyword search was done; a light read can only produce "overlaps".

## search-log.md

```markdown
| # | Query (exact) | Source | Date | Results | Kept ids |
```
Plus: a Gaps section (sources not reached and why), and one section per coverage pass.

## CARD.md (the check as a card)

1. WHERE WE ARE — claim vN written; K candidates checked.
2. WHAT WE ARE DOING — verdicts for every candidate in the set against vN's slots.
3. WHY — whether vN is answered somewhere.
4. WHAT IS AFFECTED — claim.md, positioning.md, the direction the user shows advisors.
5. CONCLUSION — all four slots on a methods read + second read → vN taken, restate.
   None → proceed, positioning names the nearest work per slot.
6. CONSEQUENCE OF NOT DOING IT — the direction rests on an unchecked verdict.
Closes with: "Of N candidates, K meet all four slots of claim C vN."

## Owner decision table (when a verdict turns on a boundary)

| Call | The question to answer | If "no" (or "yes") |
|---|---|---|
| A | <one plain question> | <which paper then takes the claim> |

## positioning.md skeleton

1. Status line (what is unread / unconfirmed) and "What I am asking you to decide".
2. One sentence on identifiers and file pointers, once.
3. The question, in plain words. "The claim I checked is that nobody has published this."
4. How the question got here — each restatement and the paper that forced it, in order.
5. Has anyone done it — conditions as a numbered list; N candidates, K matches; nearest
   work grouped by the condition each misses.
6. What the result rests on — each judgment call and who made it.
7. What the work would add, and the obvious objection (baselines the work must beat).
8. Scoop risk — who is one step away, who is calling for it, how fast the area moves.
9. How far the search went, and what it did not reach.
