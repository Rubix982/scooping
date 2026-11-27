# CURRENT CARD

1. WHERE WE ARE. A note from an earlier session says RippleBench (arXiv 2512.04144)
   already produces distance-stratified ripple curves with a pluggable distance function,
   graph path length included. That note has not been checked against the paper's text.
2. WHAT WE ARE DOING. Quick scoop check of claim C v1 (claim.md): 12–20 logged queries over
   arXiv, OpenAlex and ACL, forward citations of the nearest paper, methods reads of the
   nearest few.
3. WHY. Unknown now: whether any paper measures edit spread against hop count in a typed
   graph, and whether RippleBench's distance really is pluggable graph path length.
4. WHAT IS AFFECTED. The earlier note's claim about RippleBench; the decision to build the
   code-dependency-graph version as "a drop-in".
5. CONCLUSION IF WE DO IT. If a paper meets all four slots, C v1 is taken and the direction
   is restated (the code graph version or something the paper cannot do) with that paper
   as baseline. If none does, C v1 is open on a quick check, and RippleBench is placed by
   which slot it misses.
6. CONSEQUENCE OF NOT DOING IT. A week of building on an unverified note: either rebuilding
   a published tool or dropping an open question.

Closes with: "Of N candidates, K meet all four slots of claim C vN."

CLOSED 2026-11-27 (quick check): Of 11 candidates, 0 meet all four slots of claim C v1.
Nearest: RippleBench (misses S1, S2), CLaRE (misses S2), RippleEdits (misses S4).
The earlier note on RippleBench is half right: the paper says graph path length is a
valid distance, but the experiments run cosine similarity and RAG rank, on unlearning.
