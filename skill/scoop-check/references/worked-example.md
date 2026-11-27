# Worked example: interpretability of agent decisions, checked against planted ground truth

Files: `~/code/scooping/` (claim.md, verdicts.md, search-log.md, positioning.md, recall/).
In the KB: slug `agent-step-localization` (its ids, the Scholar pages and 20 key verdicts were
loaded after the fact; the original searches ran before the CLI existed).
2026-11-27. One day, three claim versions.

- **v1:** "No work tests whether an interpretability method recovers a cause planted in an LLM
  agent." First methods read: 2611.10620 matched all four slots (weights-planted goal in an
  agent committee, probes, detection). Not shelved; narrowed instead.
- **v2:** "…which *step* carried the planted cause." 43 candidates, 0 matches on the slots as
  written, but the result rested on three boundary calls. The owner reversed one: a
  separate reader model's hidden states count. Then ReCast (2610.11334) matched all four.
- **v3:** "Does the acting agent's own computation locate the planted step better than a
  reader model or the text?" ReCast became the reader baseline, text-only localizers the text
  baseline. 61 candidates, 0 matches; one unreadable submission flagged.
- Coverage: arXiv, Semantic Scholar citations, OpenReview (including a whole workshop via
  `group=`), ACL Anthology, Google Scholar (pasted by the user), security programs, 89
  researchers' recent listings, forward citations.
- What made it defensible: verbatim quotes, the asymmetry, flagged boundaries, the owner's
  recorded decisions, and a statement that says what it rests on.
- What was costly: subagent recall (~300k tokens each), reading too much of each paper.
  Grep methods sections for the slot terms first; read only what a verdict needs.
