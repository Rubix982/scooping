"""DuckDB store for `scope`. One file, idempotent writes (re-running never duplicates rows).

Paper ids are prefixed by where the canonical record lives: arxiv:2610.11334,
openreview:fgfKz9Qhpx, s2:<paperId>, scholar:<hash>. The papers / authors / paper_authors
tables follow the design brief (scope-tool-brainstorm.md §5); queries, seen and verdicts
are what a scoop check adds.
"""
import os
import re

import duckdb

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.environ.get('SCOPE_DB', os.path.join(ROOT, 'kb', 'scope.duckdb'))
CACHE = os.environ.get('SCOPE_CACHE', os.path.join(ROOT, 'kb', 'cache'))

SCHEMA = """
CREATE TABLE IF NOT EXISTS papers (
  id TEXT PRIMARY KEY, arxiv_id TEXT, openreview_id TEXT, doi TEXT,
  title TEXT NOT NULL, abstract TEXT, published TEXT, venue TEXT,
  source TEXT, url TEXT, ingested_at TIMESTAMP DEFAULT current_timestamp);
CREATE TABLE IF NOT EXISTS authors (id TEXT PRIMARY KEY, name TEXT, orcid TEXT);
CREATE TABLE IF NOT EXISTS paper_authors (
  paper_id TEXT, author_id TEXT, position INTEGER, institution TEXT,
  PRIMARY KEY (paper_id, position));
CREATE TABLE IF NOT EXISTS checks (
  slug TEXT PRIMARY KEY, dir TEXT, created_at TIMESTAMP DEFAULT current_timestamp);
CREATE SEQUENCE IF NOT EXISTS qseq START 1;
CREATE TABLE IF NOT EXISTS queries (
  qid INTEGER PRIMARY KEY DEFAULT nextval('qseq'), check_slug TEXT, source TEXT,
  query TEXT, params TEXT, n_results INTEGER, n_new INTEGER, n_shown INTEGER,
  status TEXT, run_at TIMESTAMP DEFAULT current_timestamp);
CREATE TABLE IF NOT EXISTS query_hits (qid INTEGER, paper_id TEXT, PRIMARY KEY (qid, paper_id));
CREATE TABLE IF NOT EXISTS seen (
  check_slug TEXT, paper_id TEXT, how TEXT,
  first_seen TIMESTAMP DEFAULT current_timestamp, PRIMARY KEY (check_slug, paper_id));
CREATE TABLE IF NOT EXISTS verdicts (
  check_slug TEXT, version TEXT, paper_id TEXT, s1 TEXT, s2 TEXT, s3 TEXT, s4 TEXT,
  verdict TEXT, read_level TEXT, quotes TEXT, note TEXT,
  decided_at TIMESTAMP DEFAULT current_timestamp,
  PRIMARY KEY (check_slug, version, paper_id));
"""


def connect():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    con = duckdb.connect(DB_PATH)
    con.execute(SCHEMA)
    return con


def upsert_paper(con, p):
    """p: dict with id, title and any of arxiv_id, openreview_id, doi, abstract, published,
    venue, source, url, authors (list of names), affils (parallel list). Fills empty fields, never overwrites."""
    con.execute("INSERT OR IGNORE INTO papers (id, title) VALUES (?, ?)", [p['id'], p['title'] or '(untitled)'])
    if p.get('title'):
        con.execute("UPDATE papers SET title = ? WHERE id = ? AND title IN ('(imported id)', '(untitled)')", [p['title'], p['id']])
    for f in ('arxiv_id', 'openreview_id', 'doi', 'abstract', 'published', 'venue', 'source', 'url'):
        if p.get(f):
            con.execute(f"UPDATE papers SET {f} = ? WHERE id = ? AND ({f} IS NULL OR {f} = '')", [p[f], p['id']])
    for i, name in enumerate(p.get('authors') or []):
        if not isinstance(name, str) or not name.strip():
            continue
        aid = 'name:' + ' '.join(name.lower().split())
        con.execute("INSERT OR IGNORE INTO authors (id, name) VALUES (?, ?)", [aid, name])
        con.execute("INSERT OR IGNORE INTO paper_authors (paper_id, author_id, position) VALUES (?, ?, ?)", [p['id'], aid, i])
        aff = (p.get('affils') or [])[i:i + 1]
        if aff and aff[0]:
            con.execute("UPDATE paper_authors SET institution = ? WHERE paper_id = ? AND position = ? AND institution IS NULL",
                        [aff[0], p['id'], i])


def is_seen(con, slug, pid):
    return con.execute("SELECT 1 FROM seen WHERE check_slug = ? AND paper_id = ?", [slug, pid]).fetchone() is not None


def mark_seen(con, slug, pid, how):
    con.execute("INSERT OR IGNORE INTO seen (check_slug, paper_id, how) VALUES (?, ?, ?)", [slug, pid, how])


def resolve_by_title(con, p):
    """Map a non-arXiv record (Scholar, S2, OpenReview) onto a paper already stored under
    another id when the normalized titles match, so one paper is one row."""
    if p['id'].startswith('arxiv:') or not p.get('title'):
        return p['id']
    key = re.sub(r'[^a-z0-9]', '', p['title'].lower())[:80]
    if len(key) < 25:
        return p['id']
    row = con.execute("SELECT id FROM papers WHERE left(regexp_replace(lower(title), '[^a-z0-9]', '', 'g'), 80) = ? "
                      "ORDER BY (id LIKE 'arxiv:%') DESC LIMIT 1", [key]).fetchone()
    return row[0] if row else p['id']
