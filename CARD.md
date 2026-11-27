# The Card

One card open at a time. Six fields. Nothing starts until all six are filled,
nothing else starts until this one is closed.

---

## The six fields

**1. WHERE WE ARE.** The last thing that was established, as a number or a fact.
Not a summary of the project. One sentence.

**2. WHAT WE ARE DOING.** One action, stated so that a second person could carry
it out without asking. If it needs "and", it is two cards.

**3. WHY.** What is not known right now that will be known after. If the answer
is "it would be good to have", there is no why and the card does not open.

**4. WHAT IS AFFECTED.** Which existing claims, files, or numbers change if this
comes back either way. Written before the work, so a silent invalidation is
impossible.

**5. CONCLUSION IF WE DO IT.** Both branches, stated in advance. *If X, then we
claim A. If not-X, then we claim B.* A card where only one branch has a
consequence is not an experiment, it is a hope.

**6. CONSEQUENCE OF NOT DOING IT.** What breaks, stalls, or stays unknown if
this is skipped forever. If the honest answer is "nothing", close the card
unstarted. That is a success.

---

## The three rules

1. **One card open.** A second idea goes in `threads.md` as one line and is not
   discussed further in that sitting.
2. **A card closes with a number or a sentence that could have come out the
   other way.** Not with "explored" or "built".
3. **Field 6 is the one that kills cards.** Fill it honestly and most ideas die
   there, which is the point — it is cheaper than killing them after the work.

---

# CURRENT CARD

_Opened 2026-11-27 for claim C v3. Nothing else opens until this closes._

**1. WHERE WE ARE.**
Claim C v2 is taken under the claim owner's call B (ReCast, all four slots). Claim C v3
(`claim.md`) asks whether the agent's own activations beat a reader model and text; zero
candidates have been checked against it.

**2. WHAT WE ARE DOING.**
Re-scoring every candidate in `verdicts.md` that uses the acting agent's own internals
or has planted step labels against v3's four slots, and running a logged search for the
comparison itself (own versus reader versus text internals, matched generator), with
results in `verdicts.md` and `search-log.md`.

**3. WHY.**
Not known: whether anyone has located planted steps from the acting agent's own
activations. Known after: the work that does, or the nearest work and the slot each misses.

**4. WHAT IS AFFECTED.**
`claim.md` v3 becomes checked or withdrawn; `positioning.md` is rewritten around v3 or
around whatever answers it.

**5. CONCLUSION IF WE DO IT.**
If any candidate meets all four v3 slots on a methods read, confirmed by a second read →
v3 is taken; restate again. If none → proceed with v3 and rewrite the positioning
statement, naming the nearest work per slot.

**6. CONSEQUENCE OF NOT DOING IT.**
The advisors would see a direction restated after one paper and not checked again, which
is the failure this project exists to prevent.

**Closes with:** "Of N candidates, K meet all four slots of claim C v3."

**Closed 2026-11-27.** Of 61 candidates (43 with v2 verdicts plus 18 abstract screens),
0 meet all four slots of claim C v3 (`verdicts.md`). One item is unresolved: LTS
(fgfKz9Qhpx), PDF not readable from here. The targeted search for the comparison (7
arXiv abstract queries, 4 OpenReview queries) found nothing new beyond Goal-Drift Probes
(forecasting, natural failures). Field 5's second branch applies: proceed with v3.

**Addendum (coverage pass 4, same day).** OpenAlex and the full ACL Anthology added 615
records new to the check; 4 more overlaps recorded, none meeting all four slots. Count
becomes 0 of 65. See `search-log.md`, coverage pass 4.

---

# CLOSED CARDS


_Opened 2026-11-27 for claim C v2._

**1. WHERE WE ARE.**
Claim C was narrowed to v2 ("which step", `claim.md`) after 1 of 4 candidates read
matched v1 on a first read. Zero candidates have been checked against v2.

**2. WHAT WE ARE DOING.**
Giving every candidate in the v2 candidate set a verdict (same question / overlaps /
different) against claim C v2, with a quote from its methods section for each of the
four slots. The candidate set is the items in `recall/A`, `B` and `C` that touch step
localization or planted causes in agents, plus whatever a logged supplementary search
for step-localization vocabulary surfaces (`recall/D-step-localization.md`). Queries,
sources, dates and counts go in `search-log.md`; verdicts go in `verdicts.md`.

**3. WHY.**
Not known now: whether anyone has tested an internals method on finding the step of an
agent's trajectory that carried a planted cause. Known after: either the work that
does it, or the nearest work and which slot each one misses, backed by a search log
someone else can rerun.

**4. WHAT IS AFFECTED.**
Claim C v2 becomes a checked claim or a withdrawn one. The direction statement the
advisors see. The four v1 verdicts in `verdicts.md` get a v2 row each. The field grid
(T-001, T-002) keeps waiting. No existing number changes.

**5. CONCLUSION IF WE DO IT.**
If any candidate matches all four slots on a methods-level reading, confirmed by a
second read → claim C v2 is taken. We restate the direction around what that work
does not do, and tell the advisors so.
If no candidate matches all four → we proceed, with a positioning statement that
names the nearest candidates and the slot each one misses, plus the search log. If the
only work that would otherwise match is black-box, the statement says so plainly: the
black-box version of the question has been run and the internals version has not, and
that rests on the S3 decision in `claim.md`, which the advisors should see.
A three-of-four match never counts as scooped. It goes in the positioning.

**6. CONSEQUENCE OF NOT DOING IT.**
The advisors' precondition stays unmet. Worse than before: we would bring them a claim
that was narrowed to step around one paper and never checked itself, which is the same
unchecked verdict as the "suspected empty cell", one level down.

**Closes with:** "Of N candidates in the v2 set, K match all four slots of claim C v2"
— where K = 0 and K ≥ 1 are both live outcomes.

**Closed 2026-11-27.** Of 43 candidates in the v2 set, 0 match all four slots of claim
C v2 (`verdicts.md`). K = 0 holds only under S3 as written. Dropping the boundary on a
different model's internals makes it K = 1 (ReCast, 2610.11334). Counting black-box
methods makes it K ≥ 5. Field 5's second branch applies: proceed, with a positioning
statement. Not given verdicts: D's 60 screened items and the bibliography leads in
`search-log.md`. Search gaps (OpenReview, the IAB workshop list, Google Scholar,
security proceedings) still limit any "lane is open" sentence.

**Amended 2026-11-27.** The claim owner reversed call B (reader-model internals count).
Under that decision ReCast matches all four slots on a methods read, so K = 1 and claim
C v2 is taken, pending a second read. Field 5's first branch now applies: restate the
direction around what ReCast does not do.


---


_Opened 2026-11-27 for claim C v1._

**1. WHERE WE ARE.**
The direction to check is fixed: interpretability of agent decisions, checked
against planted ground truth. Claim C (`claim.md`) is a draft, and zero papers
have been checked against it.

**2. WHAT WE ARE DOING.**
Giving every candidate that a logged search of the named interp sources surfaces
as close to claim C a verdict (same question / overlaps / different), with a quote
from its methods section for each of the four slots in `claim.md`. The search
queries, sources, dates and counts go in `search-log.md`; the verdicts go in
`verdicts.md`.

**3. WHY.**
Not known now: whether claim C is already answered in a paper or a public post.
Known after: either the work that answers it, or the nearest work and which slot
each one misses, backed by a search log someone else can rerun.

**4. WHAT IS AFFECTED.**
The "suspected empty cell" in `scope-tool-brainstorm.md` §4 becomes a checked
claim or a withdrawn one. Whether the north-star direction continues in its
current form, since the advisors require this check first. The field grid
(T-001) waits on this card. No existing number changes.

**5. CONCLUSION IF WE DO IT.**
If any candidate matches all four slots on a methods-level reading, confirmed by
a second read → claim C as stated is taken. We restate the direction around what
that work does not do, and tell the advisors so.
If no candidate matches all four → we proceed, with a positioning statement that
names the nearest candidates and the slot each one misses, plus the search log.
A three-of-four match never counts as scooped. It goes in the positioning.

**6. CONSEQUENCE OF NOT DOING IT.**
The advisors' precondition stays unmet and the north-star work does not continue.
The "suspected empty cell" stays a guess, which is the kind of unchecked verdict
that already cost work once (KnowledgeSmith, in edit-slice), only pointed the
other way.

**Closes with:** "Of N candidates from the search in `search-log.md`, K match all
four slots of claim C" — where K = 0 and K ≥ 1 are both live outcomes.

**Closed 2026-11-27, superseded before the reads finished.** Of 4 candidates read at
methods level, 1 (2611.10620 §10.2) matched all four slots of claim C v1 on a first
read, with no second read. The claim was narrowed to v2 ("which step") instead of
finishing the v1 check, so this K = 1 stays provisional. It was never treated as
grounds to shelve.
