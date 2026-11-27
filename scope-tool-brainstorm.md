# `scope` — Research Scoping Tool (Brainstorm & Design Brief)

> Working name. A personal tool to map where mechanistic interpretability research stands — what has been claimed, what is in flight, and where the open cells are — so research directions can be scoped with a method rather than intuition.

---

## 1. Why this exists

Judging whether a direction is novel is currently guesswork. Two failure modes:

- **Published-work blindness** — the field moves too fast to read everything; overlap is discovered late.
- **In-flight blindness** — papers lag work by 6–12 months; what other labs are building now is invisible.

Novelty is not "nobody has touched this topic." It is a **defensible gap**: a specific *question × object × method × setting × validation* combination that has not been answered. Finding those gaps is permutational work — exactly what a tool should do, leaving the judgment to a human.

**First (and only) user for v0:** me, scoping my own research north star — making AI agents' decisions understandable, checkable, and correctable.

---

## 2. Questions the tool should answer

- Where does current interp work cluster? Which cells are dense, sparse, empty?
- Which cells are *growing* fastest over the last 12 months?
- Who (papers, labs, people) occupies the cells nearest to mine?
- What landed near my cell this week? *(scoop watch)*
- Which labs are moving toward agent-level / trajectory-level interpretability, and from which direction?
- For an empty cell: is it empty because it's **infeasible**, **uninteresting**, or **actually open**? *(tool drafts arguments; human decides)*

---

## 3. The method (what the tool encodes)

1. **Define facets** — the axes that characterize work in the field (hand-defined; this is my theory of the field).
2. **Seed corpus** — 10–20 anchor papers + seed queries; expand 1–2 citation hops; filter by date.
3. **Extract** — LLM fills facets per paper from abstract/intro, **with an evidence quote per value**.
4. **Normalize** — cluster free-text facet values into a canonical vocabulary (embeddings + manual merge table).
5. **Grid** — cross any 2–3 facets; show density + recency per cell.
6. **Triage gaps** — human labels each candidate gap: infeasible / uninteresting / open.
7. **Watch** — scheduled ingest; alert when new work lands near tracked cells.

---

## 4. Facet schema (draft — needs review)

Multi-valued per paper. Every value carries an evidence quote.

| Facet | Values (draft) |
|---|---|
| **Aim** | localize, explain, edit, steer, monitor, evaluate |
| **Object** | features/neurons, circuits, single-pass behavior, multi-step reasoning, agent trajectory, training dynamics, model diff |
| **Method** | patching/causal tracing, probing, SAEs/transcoders, attribution graphs, steering vectors, resampling/counterfactual sampling, model editing |
| **Setting** | toy/synthetic, factual recall, code, safety/deception, security, general language |
| **Validation** | qualitative only, planted ground truth, human labels, held-out prediction, intervention outcome |
| **Artifact** | method, tool/library, benchmark, dataset, analysis |
| **Org type** | academic, industry lab, independent |

**Open decisions**
- *Object* and *Validation* carry the north star — "agent trajectory × planted ground truth" is the suspected empty cell. Are they framed correctly?
- Add a **Scale** facet (model size bucket)? Add **Open-weights vs. closed** model studied?
- Keep an `other:<free text>` escape value per facet so the schema can evolve from data instead of being forced.
- Schema is versioned; re-extraction is cheap enough to rerun when facets change.

---

## 5. Data model (DuckDB)

```sql
-- core entities
CREATE TABLE papers (
  id            TEXT PRIMARY KEY,   -- OpenAlex work ID
  doi           TEXT,
  arxiv_id      TEXT,
  title         TEXT NOT NULL,
  abstract      TEXT,
  published     DATE,
  venue         TEXT,
  cited_by      INTEGER,
  source        TEXT,               -- openalex | arxiv | manual
  ingested_at   TIMESTAMP
);

CREATE TABLE authors (
  id            TEXT PRIMARY KEY,   -- OpenAlex author ID (ORCID when available)
  name          TEXT,
  orcid         TEXT
);

CREATE TABLE paper_authors (
  paper_id      TEXT REFERENCES papers(id),
  author_id     TEXT REFERENCES authors(id),
  position      INTEGER,
  institution   TEXT
);

-- facets
CREATE TABLE facet_values (
  paper_id        TEXT REFERENCES papers(id),
  facet           TEXT,             -- aim | object | method | ...
  raw_value       TEXT,             -- as extracted
  canonical_value TEXT,             -- after normalization
  evidence        TEXT,             -- supporting quote from the paper
  confidence      REAL,
  schema_version  INTEGER,
  model           TEXT              -- which LLM extracted it
);

-- human judgment
CREATE TABLE gap_triage (
  cell_key      TEXT,               -- e.g. "object=agent trajectory|validation=planted"
  verdict       TEXT,               -- infeasible | uninteresting | open
  note          TEXT,
  decided_at    TIMESTAMP
);

-- v1: labs layer
CREATE TABLE labs (
  id            TEXT PRIMARY KEY,
  name          TEXT,
  institution   TEXT,
  homepage      TEXT,
  github_org    TEXT
);

CREATE TABLE lab_members (
  lab_id        TEXT REFERENCES labs(id),
  author_id     TEXT REFERENCES authors(id),
  role          TEXT,               -- PI | postdoc | PhD | ...
  since         DATE,
  until         DATE
);
```

Embeddings: DuckDB `vss` extension on paper abstracts + facet values (for normalization and "nearest to my cell" queries).

---

## 6. Sources (ordered by how early they signal work)

1. **Grant awards** (NSF and similar) — describe work years ahead of papers. *Reuse Advisor Atlas ingestion.*
2. **Lab / student pages** — in-progress projects, thesis proposals, talks.
3. **GitHub** — new repos depending on nnsight / TransformerLens / SAE libraries.
4. **Workshop papers & talks** — earlier, rougher signals of direction.
5. **Papers** — OpenAlex (author + institution IDs), arXiv (cs.LG, cs.CL, cs.AI) by query and by author.

Rules: prefer APIs over scraping, respect robots.txt, public research output only — this maps research, not people.

---

## 7. Architecture & stack

```
scope/
├── pyproject.toml
├── README.md
├── config/
│   ├── facets.v1.yaml        # facet schema (versioned)
│   ├── seeds.yaml            # anchor papers + seed queries
│   └── labs.yaml             # v1: curated lab roster
├── scope/                    # Python pipeline
│   ├── ingest/
│   │   ├── openalex.py
│   │   └── arxiv.py
│   ├── extract/
│   │   ├── prompt.py         # facet extraction prompt + JSON schema
│   │   └── run.py            # batch extraction, retries, caching
│   ├── normalize/
│   │   └── cluster.py
│   ├── store/
│   │   ├── schema.sql
│   │   └── db.py
│   └── grid/
│       └── views.sql         # cell counts, recency, growth
├── tests/
│   └── fixtures/             # recorded API responses for offline tests
└── cli/                      # v1: Go CLI over the DuckDB file
```

- **Python** for the pipeline (ingest → extract → normalize).
- **DuckDB** as the single-file store.
- **Go CLI** (v1) for fast querying:
  `scope grid --rows method --cols object --since 2025-01`
  `scope near --cell "object=agent trajectory,validation=planted"`
  `scope watch --since 7d`
  `scope lab "<lab name>"`
- **LLM extraction**: provider-agnostic interface, strict JSON output, cached by `(paper_id, schema_version, model)` so reruns are cheap.
- Everything idempotent: rerunning ingest/extract never duplicates rows.

---

## 8. Milestones

**v0 — the slice (one focused session)**
- OpenAlex ingest from seeds, 2023+, target 150–300 papers
- LLM facet extraction with evidence quotes
- SQL grid view; print a 2-facet table to terminal
- Done when: I can look at a real grid and recognize (or be surprised by) the shape of the field

**v0.5 — trust**
- Normalization pass (canonical vocabulary)
- Audit 30 random extractions by hand; measure agreement
- **Backtest**: freeze corpus at mid-2024; check whether cells flagged "open" were later filled

**v1 — labs & watch**
- Curated roster of ~10 labs nearest the north star
- Lab profiles: which cells each lab occupies, how that shifts over time
- Grant + GitHub signals
- Weekly scheduled ingest + "near my cell" alerts
- Go CLI

**v2 — maybe, only if v1 proves useful**
- Generalize beyond interp; open-source it for other researchers

---

## 9. Validation (trusting the tool)

- **Extraction audit:** hand-label a random sample; track per-facet agreement. A facet below ~80% agreement gets redefined, not tolerated.
- **Backtest:** the tool must recover past gaps before it's trusted on present ones.
- **Human check:** show the grid to people who know the field; their "that's wrong" is ground truth too.

---

## 10. Non-goals

- Not a general paper search engine or recommender.
- Not a literature review generator.
- Not tracking individuals beyond public research output.
- Not a replacement for asking people what's in flight — it narrows the questions to ask.

---

## 11. Risks

- **Schema drift** — facets framed wrong make the whole grid answer the wrong question. Mitigate: versioned schema, cheap re-extraction.
- **Extraction hallucination** — mitigate: mandatory evidence quotes, audits.
- **Author disambiguation** (v1) — lean on OpenAlex IDs / ORCID, hand-curate target labs.
- **Tool as procrastination** — time-box each milestone; the tool serves the research, not the reverse.

---

## 12. Open questions to settle before / during v0

- Final facet list — especially *Object* and *Validation*.
- Anchor papers for the seed list (10–20).
- Extraction model and cost budget per run.
- Abstract-only extraction for v0, or abstract + intro (needs PDF/full-text access)?
- Does "industry" mean papers from industry labs, or also blog posts / technical reports? (Many interp results appear as blog posts first.)

---

## 13. First Claude Code session — suggested prompt

> Read `scope-tool-brainstorm.md`. Build milestone v0 only: a Python package with OpenAlex ingest from `config/seeds.yaml`, a DuckDB store using the schema in section 5 (core + facet tables only), an LLM facet extractor driven by `config/facets.v1.yaml` that returns strict JSON with an evidence quote per value and caches results, and a SQL view that prints a 2-facet count grid. Make every step idempotent. Add offline tests using recorded fixtures. Don't build the labs layer, normalization, or Go CLI yet.
