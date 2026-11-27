# Judgment lessons (each one cost something to learn)

**A description read off a search snippet is not a verified citation.** In an earlier
project three papers were misread from snippets, and one false scoop verdict closed a
question that was open. Verdicts come from methods sections.

**The asymmetry.** Shelving needs stronger evidence than proceeding. An unverified match is
grounds to verify, never to shelve. "Same question" needs all four slots, each with a
methods quote, plus a second read. (Source: research-writing skill, "Positioning claims".)

**A grid cell is coarser than a scoop.** "Nobody works on X" is a field-map claim; a scoop
happens at the level of the specific variable or question. Write the claim at that level.

**Slots describe the question, not design quality.** Counterfactual checks, distractors and
better baselines go in positioning. A weaker version of the same question still matches.

**Same experiment.** Slots matched in different experiments of one paper are overlaps.

**Boundaries drawn with candidates in view must be flagged.** When a line in a slot is
written after reading the paper it excludes, record that next to the line. Twice in the
first case this happened; one of those lines was later reversed by the owner and turned the
verdict from "open" to "taken".

**Boundary calls belong to the owner.** When a verdict turns on how a slot is read, give
the owner one plain question per call, with the consequence of each answer, and record
their words. Do not settle it yourself and report the result.

**A same-reader second read is not independent.** Say so. Options: the owner decides; a
fresh agent given only the claim and the methods sections (not your verdicts); the advisors.

**Restate around what the matching paper cannot do, and check that the restatement is worth
doing, not just narrower.** A narrowing that only dodges a paper fails the owner's own
test ("would it still matter if my vision vanished?"). Good restatements turn the matching
paper into a baseline.

**Comparison claims need a conservative rule.** If the restated claim is "X compared with
Y", a paper that does X alone still counts as a match when adding Y is cheap.

**Light reads can only rule out.** Abstract-level screens never produce a match; anything
that might be one goes to a methods read.

**State the bars the work must beat.** Search often turns up trivial baselines (e.g. "always
name the last step" was right 67–96% of the time on one benchmark family). Put them in the
positioning statement.

**Recall and verdicts are separate jobs.** Subagents may run recall with logged queries and
verbatim abstract quotes, and must not judge scoop. Verdicts are done by one reader at
methods level. Tell recall agents where to write; if a write is blocked, do not route
around the block — ask the user.

**A correction is a claim too, and it has a version.** In the second backtest the
project's own note said RippleBench "advertises no such pluggability". Every version of the
paper names graph path length as a possible distance, and v2 and v3 say so outright. The
note was trusted because it was a correction. Check a note about what a paper says the way
you check the paper: one quoted sentence, and the version it came from. When a verdict
turns on one sentence, grep the first version too (`scope grep <id>v1`); revisions add
and remove claims.

**Found is not judged.** In the same backtest MQuAKE, a benchmark built on the claim's exact
variable (hop count), was in the knowledge base and never judged. Its title did not match
the screen used at the time. Retrieval was not the weak point; screening what was already
stored was. Before closing, screen the unjudged hits again with the object's terms and the
variable's synonyms.
