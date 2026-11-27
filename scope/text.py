"""Text helpers: HTML to text, and sentence-level grep with the nearest section heading.
Downloaded pages are untrusted data; this only parses them, never executes them."""
import html
import re
from html.parser import HTMLParser


class _P(HTMLParser):
    SKIP = ('script', 'style', 'nav', 'header', 'footer', 'math')

    def __init__(self):
        super().__init__(); self.out = []; self.skip = 0

    def handle_starttag(self, t, a):
        if t in self.SKIP: self.skip += 1
        if t in ('h1', 'h2', 'h3', 'h4'): self.out.append('\n\n### ')
        if t in ('p', 'div', 'li', 'tr', 'br', 'figcaption', 'table'): self.out.append('\n')

    def handle_endtag(self, t):
        if t in self.SKIP and self.skip: self.skip -= 1
        if t in ('h1', 'h2', 'h3', 'h4'): self.out.append('\n')

    def handle_data(self, d):
        if not self.skip: self.out.append(d)


def html_to_text(s):
    p = _P(); p.feed(s)
    t = ''.join(p.out)
    t = re.sub(r'[ \t]+', ' ', t)
    return re.sub(r'\n\s*\n+', '\n\n', t)


def strip_tags(s):
    return ' '.join(html.unescape(re.sub('<[^>]+>', '', s or '')).split())


def sentences(t):
    return [x for x in re.split(r'(?<=[.!?])\s+', ' '.join(t.split())) if x]


def key_sentences(text, terms, k=3):
    K = re.compile(terms, re.I)
    return [s for s in sentences(text) if K.search(s)][:k]


def grep_sections(text, terms, max_hits=8, skip_refs=True):
    """Yield (heading, sentence) for sentences matching terms, in document order.
    Skips the reference list when skip_refs is set, but resumes at appendix headings
    ("Appendix …", "C.2 …"), where setups and benchmark details often live."""
    K = re.compile(terms, re.I)
    heading, out, in_refs = '(top)', [], False
    for block in text.split('\n'):
        b = block.strip()
        if b.startswith('### '):
            heading = b[4:].strip()[:60] or heading
            if re.match(r'(references|bibliography)\b', heading, re.I):
                in_refs = skip_refs
            elif re.match(r'(appendix\b|[A-Z](\.\d+)*\s)', heading):
                in_refs = False
            continue
        if in_refs:
            continue
        for s in sentences(b):
            if K.search(s) and len(s) > 30:
                out.append((heading, s))
                if len(out) >= max_hits:
                    return out
    return out
