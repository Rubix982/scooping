# US university labs working on mechanistic interpretability: who was swept (2026-11-27)

## How the list was built (rerunnable)

1. **OpenAlex institution census.** Works with "mechanistic interpretability" in title or
   abstract, from 2025-01-01, any US affiliation: 514. Grouped by institution; the 31 US
   universities with 5 or more works were kept. For each one, the most frequent *last*
   authors affiliated with it (usually the lab lead) were listed.
2. **arXiv last-author census.** arXiv advanced search, phrase "mechanistic
   interpretability" in the abstract, submitted 2025-06-01 to 2026-11-27: 708 papers. Last
   authors counted. The distribution is flat (maximum 5), because many interpretability
   groups do not use the exact phrase.
3. **Web search** for lab pages (4 queries).
4. **Union**, then each person's arXiv listing since April 2026 was swept for titles that
   contain both an agent term and a method term, and screened against the four conditions.

**Caveats.** "Top" here means "most mechanistic interpretability output in OpenAlex",
not a ranking of universities. The phrase "mechanistic interpretability" also matches
biology and chemistry papers, so some last authors in step 1 are not interpretability
labs. OpenAlex author profiles gave clearly wrong current institutions for several common
names, so affiliations below come from the institution recorded on the person's own
interpretability papers where available. Labs whose papers avoid the exact phrase, or
whose arXiv affiliations OpenAlex failed to parse, can be missed.

## Institutions by output (OpenAlex, 2025+, works)

Stanford 32 · Harvard 26 · USC 20 · CMU 19 · MIT 18 · NYU 17 · Berkeley 16 · (one institution omitted from the public copy) 14
· Brown 14 · Yale 14 · UVA 14 · JHU 13 · Purdue 12 · UChicago 12 · UIUC 11 · UMD 11 · BU 9 ·
Georgia Tech 9 · Utah 9 · UF 9 · UCSD 9 · Columbia 9 · Princeton 8 · Penn 8 · UT Austin 8 ·
Rutgers 7 · NJIT 7 · UCLA 7 · Michigan 7 · Cornell 6 · Northwestern 5.

## People swept, by institution (as recorded on their interpretability papers)

| Institution | People swept | Source of affiliation |
|---|---|---|
| Stanford | Mykel J. Kochenderfer, James Zou | institution census |
| Harvard | Himabindu Lakkaraju, Chirag Agarwal, Stefan Heimersheim; Martin Wattenberg (earlier sweep) | institution census; Wattenberg not verified |
| MIT | Pat Pataranutaporn, Max Tegmark; Jacob Andreas (earlier sweep) | institution census; Andreas not verified |
| NYU | He He, Tim G. J. Rudner | institution census |
| Brown | Ellie Pavlick, Asma Ghandeharioun (earlier sweep) | institution census |
| Yale | R. Thomas McCoy, Zhuoran Yang | institution census |
| UVA | Jundong Li (earlier sweep), Aidong Zhang, Chirag Agarwal | institution census |
| UIUC | Julia Hockenmaier | institution census |
| UMD | Sarah Wiegreffe (earlier sweep), Sanghamitra Dutta | UMD news page; institution census |
| BU | Aaron Mueller (earlier sweep), Mark Crovella, Deepti Ghadiyaram | arXiv 2408.01416 contact; institution census |
| UCSD | Tsui-Wei Weng | institution census |
| Princeton | Danqi Chen, Thomas L. Griffiths | institution census |
| Penn | Lyle Ungar | institution census |
| UT Austin | Kyle Mahowald | institution census |
| Rutgers | Sean Trott | institution census |
| Northwestern | Manling Li | institution census |
| NJIT | Mengnan Du | institution census |
| UChicago | Chenhao Tan, Victor Veitch | institution census; cs.uchicago.edu page |
| Purdue | Rohan Paleja | institution census |
| George Mason | Ziyu Yao (earlier sweep) | arXiv census |
| Berkeley / CMU / Stanford (others) | Jacob Steinhardt, Christopher Potts (earlier sweep) | not verified; the censuses surfaced no clear interpretability lead at Berkeley or CMU |

Lab pages seen in web search (not swept as people beyond the above): Harvard SEAS CRISP
group (crisp.seas.harvard.edu); a student group working with the Bau lab; BU hosted the 3rd New England Mechanistic
Interpretability Workshop on 2026-08-14 (bu.edu/cs news), whose speaker list was not
pulled.

## Sweep result

34 new people: 141 new titles since April 2026; 6 contain both an agent term and a method
term; 1 abstract read (2607.18754 AgentDebugX: black-box debugging, scored on Who&When).
**0 meet all four conditions.** Combined with the earlier 55-person sweep: 89 people.
