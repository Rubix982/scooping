"""scope: a local knowledge base for scoop checks. Searches run here, results go into DuckDB,
and only new, screened lines are printed, so the model reading the output spends tokens on
candidates rather than on raw search pages.

Run `scope -h` or `scope <command> -h`. Every search is logged with its counts.
"""
import argparse
import os
import re
import sys
import time

from . import db, sources
from .text import grep_sections, key_sentences

DEFAULT_TERMS = (r'plant|inject|ground[- ]truth|known|label|probe|activation|hidden|attention|patching|'
                 r'gradient|locali|which step|accuracy|AUROC|Hit@|score')
CHECKS_ROOT = os.environ.get('SCOPE_CHECKS', os.path.join(db.ROOT, 'checks'))


def norm_id(x):
    x = x.strip()
    if re.fullmatch(r'\d{4}\.\d{4,5}(v\d+)?', x):
        return 'arxiv:' + re.sub(r'v\d+$', '', x)
    return x


def short(p, width=95):
    date = (p.get('published') or '')[:20]
    return f"{p['id']} | {date} | {(p.get('title') or '')[:width]}"


def screens(patterns):
    """--screen may be given several times; a record must match every pattern."""
    Ps = [re.compile(x, re.I) for x in (patterns or [])]
    return lambda text: all(P.search(text) for P in Ps)


def too_old(p, since):
    """since is YYMM. arXiv ids compare directly; other records by the year in 'published'."""
    if p.get('arxiv_id'):
        return p['arxiv_id'][:4] < since
    y = re.search(r'(19|20)\d\d', p.get('published') or '')
    return bool(y) and int(y.group(0)) < 2000 + int(since[:2])


def since_date(since, default='2024-01-01'):
    return f'20{since[:2]}-{since[2:4]}-01' if since else default


def run_search(con, slug, source, label, params, results, code, a):
    """Store every result; print only results new to this check that pass the screen."""
    if not con.execute("SELECT 1 FROM checks WHERE slug = ?", [slug]).fetchone():
        sys.exit(f"no check '{slug}'. Create it with: scope check new {slug}")
    ok = screens(getattr(a, 'screen', None))
    since = getattr(a, 'since', None)
    new, shown = [], []
    qid = con.execute("INSERT INTO queries (check_slug, source, query, params, status) VALUES (?, ?, ?, ?, ?) RETURNING qid",
                      [slug, source, label, params, str(code)]).fetchone()[0]
    for p in results:
        p['id'] = db.resolve_by_title(con, p)
        db.upsert_paper(con, p)
        con.execute("INSERT OR IGNORE INTO query_hits VALUES (?, ?)", [qid, p['id']])
        if db.is_seen(con, slug, p['id']):
            continue
        db.mark_seen(con, slug, p['id'], f'q{qid}')
        new.append(p)
        if since and too_old(p, since):
            continue
        if not ok((p.get('title') or '') + ' ' + (p.get('abstract') or '')):
            continue
        shown.append(p)
    con.execute("UPDATE queries SET n_results = ?, n_new = ?, n_shown = ? WHERE qid = ?", [len(results), len(new), len(shown), qid])
    print(f"q{qid} {source} {label!r}: {len(results)} results, {len(new)} new to '{slug}', {len(shown)} pass screen"
          + ('' if code in (200, '200') else f'  [HTTP {code}]'))
    for p in shown[:a.show]:
        print('  ' + short(p))
    if len(shown) > a.show:
        print(f'  … {len(shown) - a.show} more: scope hits {slug} --qid {qid}')


def cmd_check_new(a):
    con = db.connect()
    d = a.dir or os.path.join(CHECKS_ROOT, a.slug)
    os.makedirs(os.path.join(d, 'recall'), exist_ok=True)
    stubs = {
        'CARD.md': '# CURRENT CARD\n\n1. WHERE WE ARE.\n2. WHAT WE ARE DOING.\n3. WHY.\n4. WHAT IS AFFECTED.\n5. CONCLUSION IF WE DO IT.\n6. CONSEQUENCE OF NOT DOING IT.\n\nCloses with: "Of N candidates, K meet all four slots of claim C vN."\n',
        'claim.md': '# Claim C — draft v1\n\n## The claim\n\nNo published paper or public post …\n\n## The four slots\n\n| Slot | What must be true of the candidate | Does not match |\n|---|---|---|\n| S1 Object | | |\n| S2 Ground truth / data | | |\n| S3 Method / access | | |\n| S4 Measurement | | |\n\n## Boundaries drawn with candidates already in view\n\n## Claim owner\'s decisions\n',
        'search-log.md': f'# Search log — {a.slug}\n\nQueries and counts are in the knowledge base; `scope report {a.slug}` writes them to `search-log.generated.md`. Record gaps and coverage passes here.\n\n## Gaps\n',
        'verdicts.md': f'# Verdicts — {a.slug}\n\nRecord verdicts with `scope verdict`; `scope report {a.slug}` writes the tables to `verdicts.generated.md`. Longer notes go here.\n',
        'threads.md': '# Threads\n',
    }
    for name, body in stubs.items():
        path = os.path.join(d, name)
        if not os.path.exists(path):
            open(path, 'w').write(body)
    con.execute("INSERT OR IGNORE INTO checks (slug, dir) VALUES (?, ?)", [a.slug, d])
    print(f"check '{a.slug}' at {d}")


def cmd_search(a):
    con = db.connect()
    if a.source == 'arxiv':
        for q in a.args:
            code, res = sources.arxiv_search(q, a.field)
            run_search(con, a.slug, 'arxiv', q, f'field={a.field}', res, code, a); time.sleep(3)
    elif a.source == 'authors':
        names = [l.strip() for l in open(a.args[0]) if l.strip()] if len(a.args) == 1 and os.path.exists(a.args[0]) else a.args
        for n in names:
            code, res = sources.arxiv_author(n)
            run_search(con, a.slug, 'arxiv-author', n, f'since={a.since}', res, code, a); time.sleep(3)
    elif a.source == 'openreview':
        for t in a.args:
            code, res = sources.openreview_search(t, a.group)
            run_search(con, a.slug, 'openreview', t, f'group={a.group}', res, code, a); time.sleep(2)
    elif a.source == 'cites':
        for x in a.args:
            aid = norm_id(x).replace('arxiv:', '')
            code, res = sources.s2_citations(aid)
            run_search(con, a.slug, 's2-cites', aid, '', res, code, a); time.sleep(5)
    elif a.source == 'openalex':
        for q in a.args:
            code, res = sources.openalex_search(q, since_date(a.since))
            run_search(con, a.slug, 'openalex', q, f'from={since_date(a.since)}', res, code, a); time.sleep(1)
    elif a.source == 'acl':
        y = 2000 + int(a.since[:2]) if a.since else 0
        for rx in a.args:
            code, res = sources.acl_search(rx, db.CACHE, y)
            run_search(con, a.slug, 'acl', rx, f'year>={y}', res, code, a)
    elif a.source == 'scholar':
        by_sec = {}
        for sec, p in sources.parse_scholar(a.args[0]):
            by_sec.setdefault(sec, []).append(p)
        for sec, res in by_sec.items():
            run_search(con, a.slug, 'scholar', f'{os.path.basename(a.args[0])}#{sec}', 'pasted', res, 200, a)


def cmd_census(a):
    if a.source == 'arxiv':
        n, top = sources.arxiv_last_author_census(a.phrase, a.date_from)
        print(f'arXiv: {n} papers with "{a.phrase}" in the abstract since {a.date_from}; top last authors:')
    else:
        code, label, top = sources.openalex_census(a.phrase, a.date_from, a.institution, a.country, a.top)
        print(f'OpenAlex "{a.phrase}" since {a.date_from}' + (f' (papers with a {a.country.upper()} institution)' if a.country else '')
              + f': {label}' + ('' if code == 200 else f'  [HTTP {code}]'))
    print('  ' + ', '.join(f'{x} {c}' for x, c in top[:a.top]))


def cmd_abstract(a):
    con = db.connect()
    for x in a.ids:
        pid = norm_id(x)
        row = con.execute("SELECT title, abstract, published FROM papers WHERE id = ?", [pid]).fetchone()
        if (not row or not row[1] or row[0] in ('(imported id)', '(untitled)')) and pid.startswith('arxiv:'):
            p = sources.arxiv_abs(pid[6:]); time.sleep(2)
            if p:
                db.upsert_paper(con, p)
                row = (p['title'], p['abstract'], p['published'])
        if not row:
            print(f'{pid}: not found'); continue
        print(f'{pid} | {row[2] or ""} | {row[0][:100]}')
        ks = key_sentences(row[1] or '', a.terms, a.k)
        print('   ' + (' '.join(ks) if ks else (row[1] or '(no abstract)')[:400]))


def cmd_grep(a):
    con = db.connect()
    pid = norm_id(a.id)
    if not pid.startswith('arxiv:'):
        print(f'{pid}: full text is only fetched for arXiv papers; for others ask the user for the PDF and use --file')
        if not a.file:
            return
    m = re.search(r'(v\d+)$', a.id.strip())
    want = a.paper_version or (m.group(1) if m else '')
    if a.file:
        path, how, ver = a.file, 'file', want or 'unknown'
    else:
        path, how, ver = sources.arxiv_fulltext(pid[6:], db.CACHE, want, a.refresh)
    if not path:
        print(f'{pid}: full text unavailable ({how})'); return
    con.execute("INSERT INTO reads (paper_id, paper_version, how) VALUES (?, ?, ?)", [pid, ver, how])
    hits = grep_sections(open(path, errors='replace').read(), a.terms, a.max)
    print(f'{pid} {ver}: {len(hits)} matching sentences ({how}); terms /{a.terms}/')
    for h, s in hits:
        print(f'  [{h}] {s[:a.width]}')


def cmd_verdict(a):
    con = db.connect()
    pid = norm_id(a.id)
    pv = a.paper_version
    if not pv:
        r = con.execute("SELECT paper_version FROM reads WHERE paper_id = ? ORDER BY read_at DESC LIMIT 1", [pid]).fetchone()
        pv = r[0] if r else ''
    if not pv and pid.startswith('arxiv:'):
        pv = (sources.arxiv_latest_version(pid[6:]) or '?') + ' (latest; abstract only)'
    con.execute("INSERT OR REPLACE INTO verdicts (check_slug, version, paper_id, s1, s2, s3, s4, verdict, read_level, quotes, note, paper_version) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                [a.slug, a.version, pid, a.s1, a.s2, a.s3, a.s4, a.verdict, a.read, ' || '.join(a.quote or []), a.note, pv or None])
    db.mark_seen(con, a.slug, pid, 'verdict')
    print(f'{a.slug} {a.version} {pid}: {a.verdict} (S1 {a.s1}, S2 {a.s2}, S3 {a.s3}, S4 {a.s4}; {a.read} read of {pv or "unknown version"})')


def cmd_seen(a):
    con = db.connect()
    q = norm_id(a.query)
    rows = con.execute("SELECT id, published, title FROM papers WHERE id = ? OR lower(title) LIKE ? LIMIT 10",
                       [q, f'%{a.query.lower()}%']).fetchall()
    if not rows:
        print('not in the knowledge base'); return
    for pid, d, t in rows:
        checks = [r[0] for r in con.execute("SELECT check_slug FROM seen WHERE paper_id = ?", [pid]).fetchall()]
        vs = con.execute("SELECT check_slug, version, verdict, paper_version FROM verdicts WHERE paper_id = ?", [pid]).fetchall()
        print(f'{pid} | {d or ""} | {t[:90]}\n   seen in: {", ".join(checks) or "-"}; verdicts: '
              + ('; '.join(f'{c} {v}: {x}' + (f' (read {pv})' if pv else '') for c, v, x, pv in vs) or '-'))


def cmd_hits(a):
    con = db.connect()
    sql = ("SELECT DISTINCT p.id, p.published, p.title, p.abstract FROM query_hits h JOIN papers p ON p.id = h.paper_id "
           "JOIN queries q ON q.qid = h.qid WHERE q.check_slug = ?")
    args = [a.slug]
    if a.qid:
        sql += f" AND h.qid IN ({','.join('?' * len(a.qid))})"; args += a.qid
    if a.unjudged:
        sql += " AND p.id NOT IN (SELECT paper_id FROM verdicts WHERE check_slug = ?)"; args.append(a.slug)
    rows = con.execute(sql + " ORDER BY p.id DESC", args).fetchall()
    ok = screens(a.screen)
    rows = [r for r in rows if ok((r[2] or '') + ' ' + (r[3] or ''))]
    if a.screen:  # titles that match more screens first: they are the likeliest near papers
        Ps = [re.compile(x, re.I) for x in a.screen]
        rows.sort(key=lambda r: -sum(bool(P.search(r[2] or '')) for P in Ps))
    print(f'{len(rows)} hits' + (' matching ' + ' AND '.join(f'/{x}/' for x in a.screen) + ', title matches first' if a.screen else ''))
    for r in rows[:a.show]:
        print('  ' + short({'id': r[0], 'published': r[1], 'title': r[2]}))


def cmd_status(a):
    con = db.connect()
    q = con.execute("SELECT count(*), coalesce(sum(n_results),0) FROM queries WHERE check_slug = ?", [a.slug]).fetchone()
    s = con.execute("SELECT count(*) FROM seen WHERE check_slug = ?", [a.slug]).fetchone()[0]
    j = con.execute("SELECT count(DISTINCT paper_id) FROM verdicts WHERE check_slug = ?", [a.slug]).fetchone()[0]
    v = con.execute("SELECT version, verdict, count(*) FROM verdicts WHERE check_slug = ? GROUP BY 1, 2 ORDER BY 1, 2", [a.slug]).fetchall()
    t = con.execute("SELECT count(*) FROM papers").fetchone()[0]
    print(f"'{a.slug}': {q[0]} queries ({q[1]} results), {s} papers seen, {j} judged, {s - j} not judged; KB holds {t} papers")
    print(f"  before closing: scope hits {a.slug} --unjudged --screen '<object terms>' --screen '<variable terms and synonyms>'")
    for ver, verdict, n in v:
        print(f'  {ver}: {verdict} {n}')


def cmd_report(a):
    con = db.connect()
    row = con.execute("SELECT dir FROM checks WHERE slug = ?", [a.slug]).fetchone()
    if not row:
        sys.exit(f"no check '{a.slug}'")
    d = row[0]
    qs = con.execute("SELECT qid, run_at, source, query, params, n_results, n_new, n_shown, status FROM queries "
                     "WHERE check_slug = ? ORDER BY qid", [a.slug]).fetchall()
    with open(os.path.join(d, 'search-log.generated.md'), 'w') as f:
        f.write(f'# Search log (generated by `scope report {a.slug}`)\n\n| q | when | source | query | params | results | new | shown | HTTP |\n|---|---|---|---|---|---|---|---|---|\n')
        for r in qs:
            f.write('| ' + ' | '.join(str(x).replace('|', '/') for x in (r[0], str(r[1])[:16]) + tuple(r[2:])) + ' |\n')
    vs = con.execute("SELECT v.version, v.paper_id, p.title, v.s1, v.s2, v.s3, v.s4, v.verdict, v.read_level, v.quotes, v.note, v.paper_version "
                     "FROM verdicts v LEFT JOIN papers p ON p.id = v.paper_id WHERE v.check_slug = ? ORDER BY v.version DESC, v.verdict, v.paper_id",
                     [a.slug]).fetchall()
    with open(os.path.join(d, 'verdicts.generated.md'), 'w') as f:
        f.write(f'# Verdicts (generated by `scope report {a.slug}`)\n')
        cur = None
        for r in vs:
            if r[0] != cur:
                cur = r[0]
                f.write(f'\n## {cur}\n\n| Paper | S1 | S2 | S3 | S4 | Verdict | Read |\n|---|---|---|---|---|---|---|\n')
            f.write(f'| {r[1]} {(r[2] or "")[:60]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} | {r[7]} | {r[8]}{(" " + r[11]) if r[11] else ""} |\n')
        f.write('\n## Quotes and notes\n\n')
        for r in vs:
            if r[9] or r[10]:
                f.write(f'- **{r[0]} {r[1]}**: {r[9] or ""} {("— " + r[10]) if r[10] else ""}\n')
    print(f'wrote {len(qs)} queries and {len(vs)} verdicts to {d}/search-log.generated.md and verdicts.generated.md')


def cmd_import_ids(a):
    con = db.connect()
    ids = sorted(set(re.findall(r'\b\d{4}\.\d{4,5}\b', open(a.file).read())))
    for i in ids:
        con.execute("INSERT OR IGNORE INTO papers (id, arxiv_id, title, source) VALUES (?, ?, '(imported id)', 'import')", ['arxiv:' + i, i])
        db.mark_seen(con, a.slug, 'arxiv:' + i, 'import')
    print(f"marked {len(ids)} arXiv ids as seen in '{a.slug}'")


def cmd_add(a):
    """Record a paper or post found outside the CLI (web search, a lab page, the user)."""
    import hashlib
    con = db.connect()
    m = re.search(r'(\d{4}\.\d{4,5})', a.url or '') if a.url and 'arxiv.org' in a.url else None
    pid = ('arxiv:' + m.group(1)) if m else ('url:' + hashlib.sha1((a.url or a.title).encode()).hexdigest()[:12])
    p = {'id': pid, 'title': a.title, 'url': a.url, 'source': a.source, 'published': a.date, 'abstract': a.note or ''}
    p['id'] = db.resolve_by_title(con, p)
    db.upsert_paper(con, p)
    db.mark_seen(con, a.slug, p['id'], 'added:' + a.source)
    print(f"added {p['id']} to '{a.slug}'")


def cmd_logq(a):
    """Log a query that ran outside the CLI (WebSearch, manual Google Scholar), with its count."""
    con = db.connect()
    qid = con.execute("INSERT INTO queries (check_slug, source, query, params, n_results, n_new, n_shown, status) "
                      "VALUES (?, ?, ?, ?, ?, ?, ?, 'external') RETURNING qid",
                      [a.slug, a.source, a.query, a.note or '', a.n, a.kept, a.kept]).fetchone()[0]
    print(f'logged q{qid} {a.source} {a.query!r} ({a.n} results, {a.kept} kept)')


def main(argv=None):
    p = argparse.ArgumentParser(prog='scope', description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest='cmd', required=True)

    c = sub.add_parser('check', help='create a check folder and register it'); c.add_argument('action', choices=['new'])
    c.add_argument('slug'); c.add_argument('--dir'); c.set_defaults(f=cmd_check_new)

    s = sub.add_parser('search', help='search a source; store everything, print only new screened hits')
    s.add_argument('source', choices=['arxiv', 'authors', 'openreview', 'cites', 'scholar', 'openalex', 'acl'])
    s.add_argument('slug'); s.add_argument('args', nargs='+', help='queries (arxiv; openalex, where "quotes" make a phrase) / names or a names file (authors) / '
                   'terms (openreview) / arXiv ids (cites) / pasted Scholar file (scholar) / regex over title+abstract (acl)')
    s.add_argument('--field', default='abstract', choices=['abstract', 'title', 'all'])
    s.add_argument('--group', help='OpenReview venue id, e.g. NeurIPS.cc/2026/Workshop/IAB')
    s.add_argument('--since', help='YYMM, e.g. 2601: arXiv ids by prefix, other records by year; sets the OpenAlex start date'); s.add_argument('--screen', action='append', help='regex over title + abstract; repeat to require several (AND)')
    s.add_argument('--show', type=int, default=15); s.set_defaults(f=cmd_search)

    ce = sub.add_parser('census', help='who works on a phrase, from data: arXiv last authors, or OpenAlex institutions / people at one')
    ce.add_argument('phrase'); ce.add_argument('--from', dest='date_from', default='2025-01-01'); ce.add_argument('--top', type=int, default=60)
    ce.add_argument('--source', default='arxiv', choices=['arxiv', 'openalex'])
    ce.add_argument('--institution', help='OpenAlex: authors affiliated with this institution (name or I-id) on matching papers; prints the match and alternatives')
    ce.add_argument('--country', help='OpenAlex: only papers with an institution in this country code, e.g. US')
    ce.set_defaults(f=cmd_census)

    ab = sub.add_parser('abstract', help='abstracts (cached), key sentences only'); ab.add_argument('ids', nargs='+')
    ab.add_argument('--terms', default=DEFAULT_TERMS); ab.add_argument('-k', type=int, default=3); ab.set_defaults(f=cmd_abstract)

    g = sub.add_parser('grep', help='sentences in the full text matching slot terms, with section headings')
    g.add_argument('id'); g.add_argument('--terms', required=True); g.add_argument('--max', type=int, default=8)
    g.add_argument('--width', type=int, default=300); g.add_argument('--file', help='local text file instead of fetching')
    g.add_argument('--paper-version', help="read a specific arXiv version, e.g. v1 (or write the id as 2512.04144v1); default: latest")
    g.add_argument('--refresh', action='store_true', help='refetch even if cached (a newer version may exist)')
    g.set_defaults(f=cmd_grep)

    v = sub.add_parser('verdict', help='record a verdict for one paper under one claim version')
    v.add_argument('slug'); v.add_argument('id'); v.add_argument('--version', required=True)
    for k in ('s1', 's2', 's3', 's4'):
        v.add_argument('--' + k, required=True)
    v.add_argument('--verdict', required=True, choices=['same', 'overlaps', 'different'])
    v.add_argument('--read', default='methods', choices=['methods', 'light'])
    v.add_argument('--quote', action='append', help='"S2: copied sentence" (repeatable)'); v.add_argument('--note')
    v.add_argument('--paper-version', help='version the verdict rests on; default: the last `scope grep` of this paper')
    v.set_defaults(f=cmd_verdict)

    se = sub.add_parser('seen', help='is a paper (id or title fragment) already in the knowledge base?'); se.add_argument('query')
    se.set_defaults(f=cmd_seen)
    h = sub.add_parser('hits', help='re-list stored hits for a check'); h.add_argument('slug')
    h.add_argument('--qid', type=int, nargs='+', help='one or more query ids')
    h.add_argument('--unjudged', action='store_true', help='leave out papers that already have a verdict in this check')
    h.add_argument('--screen', action='append', help='regex; repeat to require several (AND)'); h.add_argument('--show', type=int, default=30); h.set_defaults(f=cmd_hits)
    st = sub.add_parser('status', help='counts for a check'); st.add_argument('slug'); st.set_defaults(f=cmd_status)
    r = sub.add_parser('report', help='write search-log.generated.md and verdicts.generated.md'); r.add_argument('slug')
    r.set_defaults(f=cmd_report)
    im = sub.add_parser('import-ids', help='mark every arXiv id found in a file as seen'); im.add_argument('slug'); im.add_argument('file')
    im.set_defaults(f=cmd_import_ids)

    ad = sub.add_parser('add', help='record a paper or post found outside the CLI'); ad.add_argument('slug')
    ad.add_argument('--title', required=True); ad.add_argument('--url'); ad.add_argument('--source', default='web')
    ad.add_argument('--date'); ad.add_argument('--note'); ad.set_defaults(f=cmd_add)
    lq = sub.add_parser('logq', help='log a query run outside the CLI (WebSearch, manual Scholar)'); lq.add_argument('slug')
    lq.add_argument('--source', required=True); lq.add_argument('--query', required=True); lq.add_argument('--n', type=int, default=0)
    lq.add_argument('--kept', type=int, default=0); lq.add_argument('--note'); lq.set_defaults(f=cmd_logq)

    a = p.parse_args(argv)
    a.f(a)


if __name__ == '__main__':
    main()
