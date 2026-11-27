"""Source adapters. Each returns plain dicts; nothing here touches the database.

What works and what does not (2026-11): arXiv search and abs pages work; the export API is
often empty or 429. OpenReview /notes/search works without login; /notes?id= and /pdf are
behind a bot challenge. Semantic Scholar's citations endpoint works with retries; its
keyword search is nearly always 429. Google Scholar blocks automated queries: the user
pastes result pages and parse_scholar reads them. OpenAlex works anonymously. The ACL
Anthology bibliography (with abstracts) downloads as one file and is grepped locally. DBLP's
API sits behind a proof-of-work bot challenge on all mirrors (checked 2026-11-27), so it is
not wrapped.
"""
import json
import os
import re
import subprocess
import time
import urllib.parse
import urllib.request

from .text import html_to_text, strip_tags

UA = {'User-Agent': 'Mozilla/5.0 (research literature check)'}


def _get3(url, timeout=60, retries=1, wait=15):
    """(status, body, final URL after redirects). arXiv redirects /html/<id> to the versioned page."""
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
                return r.status, r.read(), r.geturl()
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < retries:
                time.sleep(wait); continue
            return e.code, b'', url
        except Exception:
            if attempt < retries:
                time.sleep(wait); continue
            return 0, b'', url


def _get(url, timeout=60, retries=1, wait=15):
    code, body, _ = _get3(url, timeout, retries, wait)
    return code, body


def _arxiv_results(page):
    out = []
    for it in re.findall(r'<li class="arxiv-result">(.*?)</li>\s*(?=<li class="arxiv-result">|</ol>)', page, re.S):
        m = re.search(r'arxiv.org/abs/(\d{4}\.\d{4,5})', it)
        t = re.search(r'<p class="title is-5 mathjax">(.*?)</p>', it, re.S)
        if not (m and t):
            continue
        au = re.search(r'<p class="authors">(.*?)</p>', it, re.S)
        ab = re.search(r'<span class="abstract-full[^"]*"[^>]*>(.*?)<a class="is-size-7"', it, re.S)
        d = re.search(r'Submitted</span>\s*([^;<]+)', it)
        out.append({'id': 'arxiv:' + m.group(1), 'arxiv_id': m.group(1), 'title': strip_tags(t.group(1)),
                    'authors': [strip_tags(x) for x in re.findall(r'<a [^>]*>(.*?)</a>', au.group(1))] if au else [],
                    'abstract': strip_tags(ab.group(1)).replace('△ Less', '').strip() if ab else '',
                    'published': d.group(1).strip() if d else '', 'source': 'arxiv',
                    'url': 'https://arxiv.org/abs/' + m.group(1)})
    return out


def arxiv_search(query, field='abstract', size=200):
    q = {'query': query, 'searchtype': field, 'abstracts': 'show', 'order': '-announced_date_first', 'size': str(size)}
    code, body = _get('https://arxiv.org/search/?' + urllib.parse.urlencode(q))
    return code, _arxiv_results(body.decode('utf-8', 'replace'))


def arxiv_author(name, size=50):
    return arxiv_search(name, field='author', size=size)


def arxiv_last_author_census(phrase, date_from, pages=10):
    """Count last authors over papers whose abstract contains the exact phrase."""
    counts, n = {}, 0
    for start in range(0, pages * 200, 200):
        q = {'advanced': '1', 'terms-0-operator': 'AND', 'terms-0-term': f'"{phrase}"', 'terms-0-field': 'abstract',
             'classification-include_cross_list': 'include', 'date-filter_by': 'date_range', 'date-from_date': date_from,
             'date-to_date': time.strftime('%Y-%m-%d'), 'date-date_type': 'submitted_date', 'abstracts': 'hide',
             'size': '200', 'order': '-announced_date_first', 'start': str(start)}
        code, body = _get('https://arxiv.org/search/advanced?' + urllib.parse.urlencode(q))
        res = _arxiv_results(body.decode('utf-8', 'replace'))
        if not res:
            break
        for r in res:
            n += 1
            if r['authors']:
                counts[r['authors'][-1]] = counts.get(r['authors'][-1], 0) + 1
        time.sleep(4)
    return n, sorted(counts.items(), key=lambda x: -x[1])


def arxiv_abs(aid):
    code, body = _get('https://arxiv.org/abs/' + aid)
    s = body.decode('utf-8', 'replace')
    t = re.search(r'<meta name="citation_title" content="(.*?)"', s)
    d = re.search(r'<meta name="citation_date" content="(.*?)"', s)
    a = re.search(r'<blockquote class="abstract[^"]*">(.*?)</blockquote>', s, re.S)
    au = re.findall(r'<meta name="citation_author" content="(.*?)"', s)
    if not t:
        return None
    return {'id': 'arxiv:' + aid, 'arxiv_id': aid, 'title': strip_tags(t.group(1)),
            'abstract': strip_tags(a.group(1)).replace('Abstract:', '').strip() if a else '',
            'published': d.group(1) if d else '', 'authors': [strip_tags(x) for x in au],
            'source': 'arxiv', 'url': 'https://arxiv.org/abs/' + aid}


def arxiv_latest_version(aid):
    """'v3' etc., read from the abs page's og:url (citation_pdf_url carries no version); '' if not found."""
    code, body = _get('https://arxiv.org/abs/' + aid)
    m = re.search(r'og:url" content="[^"]*?/abs/[^"]*?(v\d+)"', body.decode('utf-8', 'replace'))
    return m.group(1) if m else ''


def arxiv_fulltext(aid, cache_dir, version='', refresh=False):
    """Cached full text: arXiv HTML first, PDF + pdftotext as fallback. Returns (path, how, version).
    With no version requested this is the latest, and the version it turned out to be is recorded
    next to the text. Texts cached before versions were recorded get 'vN?': the latest version now,
    which the cached copy may predate; --refresh refetches."""
    d = os.path.join(cache_dir, 'arxiv', aid + version)
    path, vfile = os.path.join(d, 'text.txt'), os.path.join(d, 'version.txt')
    if not refresh and os.path.exists(path) and os.path.getsize(path) > 1000:
        if not os.path.exists(vfile):
            open(vfile, 'w').write(version or (arxiv_latest_version(aid) + '?'))
        return path, 'cache', open(vfile).read().strip()
    os.makedirs(d, exist_ok=True)
    code, body, final = _get3('https://arxiv.org/html/' + aid + version)
    if code == 200 and len(body) > 20000:
        open(path, 'w').write(html_to_text(body.decode('utf-8', 'replace')))
        m = re.search(r'(v\d+)/?$', final)
        v = version or (m.group(1) if m else arxiv_latest_version(aid))
        open(vfile, 'w').write(v)
        return path, 'html', v
    code, body = _get('https://arxiv.org/pdf/' + aid + version)
    if code == 200 and body[:4] == b'%PDF':
        pdf = os.path.join(d, 'paper.pdf'); open(pdf, 'wb').write(body)
        subprocess.run(['pdftotext', pdf, path], check=False, capture_output=True)
        if os.path.exists(path):
            v = version or arxiv_latest_version(aid)
            open(vfile, 'w').write(v)
            return path, 'pdf', v
    return None, f'failed ({code})', ''


def openreview_search(term, group=None, limit=100):
    q = {'term': term, 'limit': str(limit), 'source': 'forum'}
    if group:
        q['group'] = group
    code, body = _get('https://api2.openreview.net/notes/search?' + urllib.parse.urlencode(q))
    try:
        notes = json.loads(body).get('notes', [])
    except Exception:
        return code, []
    out = []
    for n in notes:
        c = n.get('content', {})
        v = lambda k: (c.get(k) or {}).get('value') if isinstance(c.get(k), dict) else c.get(k)
        if group and group not in str(v('venueid') or ''):
            continue
        out.append({'id': 'openreview:' + n['forum'], 'openreview_id': n['forum'], 'title': v('title') or '',
                    'abstract': v('abstract') or '', 'venue': str(v('venue') or ''), 'authors': v('authors') or [],
                    'source': 'openreview', 'url': 'https://openreview.net/forum?id=' + n['forum']})
    return code, out


def s2_citations(aid):
    code, body = _get(f'https://api.semanticscholar.org/graph/v1/paper/arXiv:{aid}/citations'
                      '?fields=title,externalIds,publicationDate,abstract,authors&limit=500', retries=2, wait=20)
    try:
        rows = json.loads(body).get('data', [])
    except Exception:
        return code, []
    out = []
    for r in rows:
        p = r.get('citingPaper') or {}
        ax = (p.get('externalIds') or {}).get('ArXiv')
        pid = ('arxiv:' + ax) if ax else ('s2:' + (p.get('paperId') or p.get('title', '')[:40]))
        out.append({'id': pid, 'arxiv_id': ax, 'title': p.get('title') or '', 'abstract': p.get('abstract') or '',
                    'published': p.get('publicationDate') or '', 'authors': [a.get('name', '') for a in p.get('authors') or []],
                    'source': 's2'})
    return code, out


def parse_scholar(path):
    """Read pasted Google Scholar pages grouped under '## N' headings. Yields (section, paper dict)."""
    import hashlib
    lines = open(path).read().split('\n')
    sec = None
    for i, l in enumerate(lines[:-1]):
        m = re.match(r'^##\s*(\S+)', l)
        if m:
            sec = m.group(1); continue
        s, nxt = l.strip(), lines[i + 1]
        if sec and s and s != 'Quick read' and not re.match(r'^\[(PDF|HTML)\]', s) and ' - ' in nxt and re.search(r'\b(19|20)\d\d\b', nxt):
            title = re.sub(r'^\[(CITATION|BOOK|B)\]\s*', '', s)
            ax = re.search(r'arXiv:(\d{4}\.\d{4,5})', nxt)
            pid = ('arxiv:' + ax.group(1)) if ax else 'scholar:' + hashlib.sha1(re.sub(r'\W', '', title.lower()).encode()).hexdigest()[:12]
            snippet = ' '.join(x.strip() for x in lines[i + 2:i + 4] if x.strip() and not x.startswith('Save'))
            yield sec, {'id': pid, 'arxiv_id': ax.group(1) if ax else None, 'title': title,
                        'abstract': snippet, 'source': 'scholar', 'authors': [a.strip() for a in nxt.split(' - ')[0].split(',')]}


# --- OpenAlex: works with venue and per-paper affiliations; group_by for census ---------
# Anonymous use works (no key, no contact address). Affiliations are taken from each paper's
# authorships, not from author profiles, whose "last known institution" proved unreliable.
OA = 'https://api.openalex.org'


def _oa_get(path, params):
    code, body = _get(OA + path + '?' + urllib.parse.urlencode(params), retries=2, wait=10)
    try:
        return code, json.loads(body)
    except Exception:
        return code, {}


def _oa_abstract(inv):
    if not inv:
        return ''
    pos = sorted((i, w) for w, idx in inv.items() for i in idx)
    return ' '.join(w for _, w in pos)


def _oa_filter(phrase, date_from, extra=()):
    f = [f'title_and_abstract.search:{phrase}', f'from_publication_date:{date_from}']
    return ','.join(f + list(extra))


def openalex_search(query, date_from='2024-01-01', limit=200):
    code, js = _oa_get('/works', {'filter': _oa_filter(query, date_from), 'per-page': str(min(limit, 200)),
                                  'select': 'id,doi,title,publication_date,authorships,primary_location,abstract_inverted_index'})
    out = []
    for w in js.get('results', []):
        loc = w.get('primary_location') or {}
        hay = (w.get('doi') or '') + ' ' + (loc.get('landing_page_url') or '')
        ax = re.search(r'arxiv[./](?:abs/)?(\d{4}\.\d{4,5})', hay, re.I)
        au = w.get('authorships') or []
        out.append({'id': ('arxiv:' + ax.group(1)) if ax else 'openalex:' + w['id'].rsplit('/', 1)[-1],
                    'arxiv_id': ax.group(1) if ax else None, 'doi': (w.get('doi') or '').replace('https://doi.org/', ''),
                    'title': w.get('title') or '', 'abstract': _oa_abstract(w.get('abstract_inverted_index')),
                    'published': w.get('publication_date') or '', 'venue': ((loc.get('source') or {}).get('display_name') or ''),
                    'authors': [(a.get('author') or {}).get('display_name') or '' for a in au],
                    'affils': ['; '.join(i.get('display_name', '') for i in a.get('institutions') or []) for a in au],
                    'source': 'openalex', 'url': loc.get('landing_page_url') or w['id']})
    return code, out


def openalex_census(phrase, date_from, institution=None, country=None, top=40):
    """Without institution: institutions on papers matching the phrase, by paper count.
    With institution (a name): authors affiliated there on those papers, by paper count."""
    extra, label, label_alts = [], 'institutions', ''
    if country:
        extra.append(f'authorships.institutions.country_code:{country.upper()}')
    if institution:
        if re.fullmatch(r'I\d+', institution):
            code, inst = _oa_get('/institutions/' + institution, {'select': 'id,display_name,country_code'})
        else:
            code, js = _oa_get('/institutions', {'search': institution, 'per-page': '3', 'select': 'id,display_name,country_code'})
            alts = js.get('results') or []
            if not alts:
                return code, f'no institution matching {institution!r}', []
            inst = alts[0]
            if len(alts) > 1:
                label_alts = '; also: ' + ', '.join(f"{x['display_name']} ({x.get('country_code')}, {x['id'].rsplit('/', 1)[-1]})" for x in alts[1:])
        extra.append('authorships.institutions.id:' + inst['id'].rsplit('/', 1)[-1])
        label = f"authors at {inst['display_name']} ({inst.get('country_code')}, {inst['id'].rsplit('/', 1)[-1]})" + label_alts
    code, js = _oa_get('/works', {'filter': _oa_filter(f'"{phrase}"', date_from, extra),
                                  'group_by': 'authorships.author.id' if institution else 'authorships.institutions.id'})
    rows = [(g.get('key_display_name') or g.get('key'), g.get('count', 0)) for g in js.get('group_by', [])]
    n = (js.get('meta') or {}).get('count')
    return code, f'{n} works; {label}', rows[:top]


# --- ACL Anthology: the full bibliography with abstracts, cached and grepped locally -----
ACL_URL = 'https://aclanthology.org/anthology+abstracts.bib.gz'


def acl_search(regex, cache_dir, year_from=0, max_age_days=7):
    import gzip
    path = os.path.join(cache_dir, 'acl', 'anthology+abstracts.bib.gz')
    if not os.path.exists(path) or time.time() - os.path.getmtime(path) > max_age_days * 86400:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        code, body = _get(ACL_URL, timeout=300)
        if code != 200 or body[:2] != b'\x1f\x8b':
            if not os.path.exists(path):
                return code, []
        else:
            open(path, 'wb').write(body)
    K = re.compile(regex, re.I)
    out = []
    for e in gzip.open(path, 'rt', encoding='utf-8', errors='replace').read().split('\n@')[1:]:
        if not K.search(e):
            continue
        f = {k.lower(): ' '.join(v.split()) for k, v in re.findall(r'^\s*(\w+)\s*=\s*"(.*?)"\s*,?\s*$(?=\n\s*\w+\s*=|\n\})', e, re.M | re.S)}
        title = re.sub(r'[{}]', '', f.get('title', ''))
        abstract = re.sub(r'[{}]', '', f.get('abstract', ''))
        year = int(f.get('year', '0') or 0)
        if year < year_from or not K.search(title + ' ' + abstract):
            continue
        aid = re.search(r'aclanthology\.org/([^/]+)/?', f.get('url', ''))
        authors = [' '.join(reversed([x.strip() for x in a.split(',', 1)])) for a in re.split(r'\s+and\s+', f.get('author', '')) if a.strip()]
        out.append({'id': 'acl:' + (aid.group(1) if aid else e.split(',', 1)[0].split('{', 1)[-1]), 'title': title,
                    'abstract': abstract, 'published': str(year), 'venue': re.sub(r'[{}]', '', f.get('booktitle') or f.get('journal') or ''),
                    'doi': f.get('doi', ''), 'authors': authors, 'source': 'acl', 'url': f.get('url', '')})
    return 200, out
