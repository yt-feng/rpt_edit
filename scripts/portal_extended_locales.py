"""Public, static SEO/GEO locale expansion; no online inference provider.

This module deliberately leaves the established ko/ja/ar application mirrors,
private document APIs, memberships and production transaction workflow alone.
"""
from __future__ import annotations
import hashlib
import json
import re
from dataclasses import dataclass
from html import escape, unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlunsplit

from compare_hymt_translation import LANGUAGES, SCRIPT_PATTERNS

ORIGIN = 'https://kcdesk.com'
EXISTING = frozenset({'zh', 'ko', 'ja', 'ar'})
# English is text-only summary/interpretation: no full reading pages or charts.
# Keep its model capability and metadata for established summary consumers.
SUMMARY_ONLY = frozenset({'en'})
# Native labels are navigation labels, not machine-translation quality claims.
NATIVE = dict(zip(
    'zh en fr pt es ja tr ru ar ko th it de vi ms id tl hi zh-Hant pl cs nl km my fa gu ur te mr he bn ta uk bo kk mn ug yue'.split(),
    ['简体中文', 'English', 'Français', 'Português', 'Español', '日本語', 'Türkçe', 'Русский', 'العربية', '한국어', 'ไทย', 'Italiano', 'Deutsch', 'Tiếng Việt', 'Bahasa Melayu', 'Bahasa Indonesia', 'Filipino', 'हिन्दी', '繁體中文', 'Polski', 'Čeština', 'Nederlands', 'ខ្មែរ', 'မြန်မာ', 'فارسی', 'ગુજરાતી', 'اردو', 'తెలుగు', 'मराठी', 'עברית', 'বাংলা', 'தமிழ்', 'Українська', 'བོད་སྐད་', 'Қазақша', 'Монгол', 'ئۇيغۇرچە', '粵語'], strict=True))
RTL = frozenset({'ar', 'fa', 'ur', 'ug', 'he'})
OG_LOCALES = {'en': 'en_US', 'fr': 'fr_FR', 'pt': 'pt_BR', 'es': 'es_ES', 'tr': 'tr_TR', 'ru': 'ru_RU', 'th': 'th_TH', 'it': 'it_IT', 'de': 'de_DE', 'vi': 'vi_VN', 'ms': 'ms_MY', 'id': 'id_ID', 'tl': 'tl_PH', 'hi': 'hi_IN', 'pl': 'pl_PL', 'cs': 'cs_CZ', 'nl': 'nl_NL', 'km': 'km_KH', 'my': 'my_MM', 'fa': 'fa_IR', 'gu': 'gu_IN', 'ur': 'ur_PK', 'te': 'te_IN', 'mr': 'mr_IN', 'he': 'he_IL', 'bn': 'bn_BD', 'ta': 'ta_IN', 'uk': 'uk_UA', 'bo': 'bo_CN', 'kk': 'kk_KZ', 'mn': 'mn_MN', 'ug': 'ug_CN', 'zh-Hant': 'zh_TW'}
ADDITIONAL = tuple(code for code in LANGUAGES if code not in EXISTING | SUMMARY_ONLY)
# Google documents ISO-639-1 plus optional script/region. yue is valid BCP-47
# but is NOT advertised here as a supported Google hreflang code.
HREFLANG = {code: code for code in LANGUAGES if code != 'yue'}
HREFLANG['zh'] = 'zh-Hans'
COPY = {
    'home': 'Home', 'source': 'Source page', 'research': 'Research library',
    'source_note': 'This is a machine-translated reading page. Verify financial figures and forecasts against the source. It does not replace the original research report.',
    'access_note': 'Open the source page for original figures, document access and membership functions.',
    'machine': 'Machine translation', 'links': 'Related source links',
}
HTML_BLOCKS = frozenset({'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'blockquote', 'caption', 'figcaption', 'dt', 'dd', 'tr'})
DROP_TAGS = frozenset({'script', 'style', 'nav', 'footer', 'form', 'button', 'noscript', 'svg'})
VOID = frozenset('area base br col embed hr img input link meta param source track wbr'.split())
MAX_DOCUMENT_BYTES = 2 * 1024 * 1024
SCHEMA = 1

class ExpansionError(ValueError):
    pass


def stable_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')) + '\n').encode()


def digest(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def select_locales(value: str) -> tuple[str, ...]:
    result = ADDITIONAL if value == 'all-supported' else tuple(value.split(','))
    if not result or len(set(result)) != len(result) or any(code not in ADDITIONAL for code in result):
        raise ExpansionError('Use all-supported or distinct additional locale codes; English is summary-only and existing mirrors are not expansion targets')
    return result


def direction(locale: str) -> str:
    if locale not in LANGUAGES:
        raise ExpansionError('Unknown locale')
    return 'rtl' if locale in RTL else 'ltr'


def public_url(value: str, *, origin: str = ORIGIN, base: str | None = None) -> str:
    """Accept only public, same-origin, non-credential URLs. Never follow APIs."""
    parsed = urlsplit(urljoin(base or origin + '/', value))
    reference = urlsplit(origin)
    if (parsed.scheme != 'https' or parsed.netloc != reference.netloc or parsed.username or parsed.password
        or parsed.query or parsed.fragment or '%' in parsed.path or '\\' in parsed.path
        or '//' in parsed.path or any(p in {'.', '..'} for p in parsed.path.split('/'))):
        raise ExpansionError('Unsafe public source URL')
    path = parsed.path or '/'
    if path not in {'/', '/about.html'} and not re.fullmatch(r'/(?:reports|blog)/(?:[A-Za-z0-9_.-]+/)*[A-Za-z0-9_.-]*', path):
        raise ExpansionError('Not a public index/report/Blog route')
    if path.startswith('/blog/bbg-') or path in {'/blog/bbg-show.html'}:
        raise ExpansionError('BBG remains on its established reviewed language pair')
    return urlunsplit(('https', parsed.netloc, path, '', ''))


def file_for_url(url: str, *, origin: str = ORIGIN) -> Path:
    path = urlsplit(public_url(url, origin=origin)).path.lstrip('/')
    if not path or path.endswith('/'):
        return Path(path) / 'index.html'
    return Path(path)


def locale_url(url: str, locale: str, *, origin: str = ORIGIN) -> str:
    if locale not in ADDITIONAL:
        raise ExpansionError('Unknown expansion locale')
    source = public_url(url, origin=origin)
    return origin + '/' + locale + urlsplit(source).path


class PublicParser(HTMLParser):
    """Extract whole public text blocks, not sentence fragments or script state.

    Charts stay on the source page. Public headings, paragraphs, table rows and
    source-link labels survive. No login forms or embedded account data survive.
    """
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.capture = None
        self.blocks = []
        self.fallback = []
        self.metadata = {}
        self.canonical = ''
        self.alternates = {}
        self.links = []
        self.anchor = None
        self.title = []
        self.jsonld = []
        self.script_buffer = None
        self.in_main = False
        self.has_main = False
        self.main_level = None
        self.content_lang = ''

    def suppressed(self):
        return any(tag in DROP_TAGS or blocked for tag, blocked in self.stack)

    def flush(self):
        if self.capture:
            tag, pieces, inside = self.capture
            text = re.sub(r'\s+', ' ', ''.join(pieces)).strip()
            if text:
                (self.blocks if inside else self.fallback).append({'tag': tag, 'text': text})
            self.capture = None

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == 'html': self.content_lang = values.get('lang', '')
        if tag == 'meta':
            name = (values.get('name') or values.get('property') or '').lower()
            self.metadata[name] = values.get('content') or ''
        if tag == 'link':
            if values.get('rel') == 'canonical': self.canonical = values.get('href') or ''
            if values.get('rel') == 'alternate' and values.get('hreflang'):
                self.alternates[values['hreflang']] = values.get('href') or ''
        if tag == 'script' and values.get('type') == 'application/ld+json':
            self.script_buffer = []
        if tag == 'main' or (tag == 'article' and not self.has_main):
            self.flush(); self.has_main = self.in_main = True; self.main_level = len(self.stack)
        hidden = ('hidden' in values or values.get('aria-hidden') == 'true'
                  or bool(re.search(r'display\s*:\s*none|visibility\s*:\s*hidden', values.get('style') or '', re.I)))
        if tag not in VOID: self.stack.append((tag, hidden))
        if self.suppressed(): return
        if tag in HTML_BLOCKS:
            if tag == 'p' and self.capture and self.capture[0] in {'li', 'blockquote', 'tr'}:
                self.capture[1].append(' ')
            else:
                self.flush(); self.capture = [tag, [], self.in_main]
        if tag in {'td', 'th'} and self.capture and self.capture[1]: self.capture[1].append(' | ')
        if tag == 'br' and self.capture: self.capture[1].append(' ')
        if tag == 'a' and values.get('href'):
            self.anchor = {'url': values['href'], 'parts': [], 'inside': self.in_main}

    def handle_endtag(self, tag):
        if tag == 'script' and self.script_buffer is not None:
            try: self.jsonld.append(json.loads(''.join(self.script_buffer)))
            except (ValueError, TypeError): pass
            self.script_buffer = None
        if not self.suppressed():
            if tag == 'a' and self.anchor:
                if self.anchor['inside']:
                    self.links.append({'url': self.anchor['url'], 'label': ''.join(self.anchor['parts']).strip()})
                self.anchor = None
            if self.capture and tag == self.capture[0]: self.flush()
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                if self.main_level is not None and index <= self.main_level:
                    self.flush(); self.in_main = False; self.main_level = None
                del self.stack[index:]; break

    def handle_data(self, text):
        if self.script_buffer is not None: self.script_buffer.append(text)
        if self.stack and self.stack[-1][0] == 'title': self.title.append(text)
        if self.suppressed(): return
        if self.capture: self.capture[1].append(text)
        if self.anchor: self.anchor['parts'].append(text)

    def close(self):
        super().close(); self.flush()


def walk_ld(value):
    if isinstance(value, dict):
        yield value
        for item in value.values(): yield from walk_ld(item)
    elif isinstance(value, list):
        for item in value: yield from walk_ld(item)


def document_from_html(url: str, body: bytes, *, origin: str = ORIGIN) -> dict:
    url = public_url(url, origin=origin)
    if not body or len(body) > MAX_DOCUMENT_BYTES:
        raise ExpansionError('Empty or oversized public HTML')
    source = body.decode('utf-8', errors='strict')
    if re.search(r'cf-chl-|challenge-platform|<title>Just a moment', source, re.I):
        raise ExpansionError('Challenge page is not translatable content')
    parsed = PublicParser(); parsed.feed(source); parsed.close()
    if parsed.canonical and public_url(parsed.canonical, origin=origin, base=url) != url:
        raise ExpansionError('Requested page is not its own canonical')
    if 'noindex' in parsed.metadata.get('robots', '').lower():
        raise ExpansionError('Source page is noindex')
    blocks = parsed.blocks if parsed.has_main else parsed.fallback
    if not blocks: raise ExpansionError('Source has no readable public text blocks')
    title = next((b['text'] for b in blocks if b['tag'] == 'h1'), ''.join(parsed.title).strip())
    if not title: raise ExpansionError('Source has no title')
    links = []
    for link in parsed.links:
        try: target = public_url(link['url'], origin=origin, base=url)
        except (ValueError, ExpansionError): continue
        if target != url and target not in {row['url'] for row in links}:
            links.append({'url': target, 'label': link['label'] or target})
    # Read dates from the page's own Article node, never a related article.
    published = modified = ''
    own = [node for value in parsed.jsonld for node in walk_ld(value)
           if node.get('@type') in ('Article', 'BlogPosting', 'NewsArticle')
           and (node.get('url') == url or str(node.get('@id', '')).split('#')[0] == url
                or node.get('mainEntityOfPage') == url)]
    if len(own) == 1:
        published = str(own[0].get('datePublished') or '')
        modified = str(own[0].get('dateModified') or '')
    result = {'url': url, 'source_html_sha256': digest(body), 'source_language': parsed.content_lang or 'zh-Hans',
              'title': title, 'description': parsed.metadata.get('description', title),
              'blocks': blocks, 'links': links[:80], 'datePublished': published,
              'dateModified': modified, 'source_alternates': parsed.alternates}
    result['content_sha256'] = digest(stable_bytes(result))
    return result


def validate_document(doc: dict, *, origin: str = ORIGIN) -> None:
    if not isinstance(doc, dict): raise ExpansionError('Invalid source document')
    public_url(doc['url'], origin=origin)
    expected = {key: value for key, value in doc.items() if key != 'content_sha256'}
    if doc.get('content_sha256') != digest(stable_bytes(expected)):
        raise ExpansionError('Source document digest mismatch')
    if not doc.get('blocks') or not doc.get('title'): raise ExpansionError('Empty source document')
    if len(stable_bytes(doc)) > MAX_DOCUMENT_BYTES: raise ExpansionError('Oversized source document')
    for item in doc['blocks']:
        if item.get('tag') not in HTML_BLOCKS or not isinstance(item.get('text'), str):
            raise ExpansionError('Invalid source block')


def validate_corpus(corpus: dict, *, origin: str = ORIGIN) -> list[dict]:
    if corpus.get('schema_version') != SCHEMA or corpus.get('origin') != origin:
        raise ExpansionError('Corpus origin/schema mismatch')
    docs = corpus.get('documents')
    if not isinstance(docs, list) or not 1 <= len(docs) <= 500:
        raise ExpansionError('Corpus must contain 1..500 public documents')
    if len({doc['url'] for doc in docs}) != len(docs): raise ExpansionError('Duplicate source URL')
    for doc in docs: validate_document(doc, origin=origin)
    paths = [file_for_url(doc['url'], origin=origin).as_posix() for doc in docs]
    if len(set(paths)) != len(paths):
        raise ExpansionError('Source URLs collide on the same output file')
    if corpus.get('documents_sha256') != digest(stable_bytes(docs)):
        raise ExpansionError('Corpus digest mismatch')
    return docs


def make_corpus(documents: list[dict], *, origin: str = ORIGIN) -> dict:
    result = {'schema_version': SCHEMA, 'origin': origin, 'documents': documents,
              'documents_sha256': digest(stable_bytes(documents))}
    validate_corpus(result, origin=origin)
    return result


STYLE = '''body{font-family:system-ui,sans-serif;max-width:1000px;margin:auto;padding:24px;line-height:1.75;color:#17212b;background:#fff}header,footer{border-block-end:1px solid #ddd;padding-block:12px}h1{line-height:1.3}a{color:#075b85;overflow-wrap:anywhere}.notice{background:#f5f7f9;padding:16px;border-inline-start:3px solid #789}nav{display:flex;gap:12px;flex-wrap:wrap}table{border-collapse:collapse;width:100%}td{border:1px solid #ccc;padding:8px}blockquote{margin-inline:0;padding-inline-start:16px;border-inline-start:3px solid #ccc}main{overflow-wrap:anywhere}@media(prefers-color-scheme:dark){body{color:#eee;background:#15191e}a{color:#91cdf0}.notice{background:#202a35}}'''


def render_document(doc: dict, translated: dict, locale: str, urls: set[str], *, origin: str = ORIGIN) -> str:
    canonical = locale_url(doc['url'], locale, origin=origin)
    copy = translated['copy']; title = translated['title']; description = translated['description']
    source = doc['url']
    og_locale = f'<meta property="og:locale" content="{OG_LOCALES[locale]}">' if locale in OG_LOCALES else ''
    article = '/blog/' in urlsplit(source).path and source.endswith('.html')
    node = {'@context': 'https://schema.org', '@type': 'Article' if article else 'WebPage',
            '@id': canonical + '#content', 'url': canonical, 'name': title,
            'description': description, 'inLanguage': locale,
            'isBasedOn': {'@type': 'CreativeWork', 'url': source, 'inLanguage': doc['source_language']},
            'publisher': {'@type': 'Organization', 'name': 'KC桌面', 'url': origin}}
    if article:
        node['headline'] = title
        node['articleBody'] = '\n\n'.join(block['text'] for block in translated['blocks'])
        for key in ('datePublished', 'dateModified'):
            if doc.get(key): node[key] = doc[key]
    blocks = []
    in_table = False
    for block in translated['blocks']:
        tag, text = block['tag'], escape(block['text'])
        if tag == 'h1': tag = 'h2'
        if tag == 'li': tag = 'p'
        if tag in {'dt', 'dd', 'caption', 'figcaption'}: tag = 'p'
        if tag == 'tr':
            if not in_table: blocks.append('<table><tbody>'); in_table = True
            blocks.append('<tr>' + ''.join('<td>' + cell.strip() + '</td>' for cell in text.split('|')) + '</tr>')
        else:
            if in_table: blocks.append('</tbody></table>'); in_table = False
            blocks.append(f'<{tag}>{text}</{tag}>')
    if in_table: blocks.append('</tbody></table>')
    related = []
    for original, translated_link in zip(doc['links'], translated['links'], strict=True):
        href = locale_url(original['url'], locale, origin=origin) if original['url'] in urls else original['url']
        related.append(f'<li><a href="{escape(href, quote=True)}">{escape(translated_link["label"])}</a></li>')
    jsonld = json.dumps(node, ensure_ascii=False).replace('<', '\\u003c').replace('>', '\\u003e')
    return f'''<!doctype html>
<html lang="{locale}" dir="{direction(locale)}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title)} | KC桌面</title>
<meta name="description" content="{escape(description, quote=True)}">
<meta name="robots" content="noindex,follow">
<link rel="canonical" href="{escape(canonical, quote=True)}">
{og_locale}
<meta property="og:type" content="{'article' if article else 'website'}">
<meta property="og:title" content="{escape(title, quote=True)}">
<meta property="og:description" content="{escape(description, quote=True)}">
<meta property="og:url" content="{escape(canonical, quote=True)}">
<meta name="twitter:card" content="summary">
<script type="application/ld+json">{jsonld}</script><style>{STYLE}</style></head>
<body><header><nav><a href="{origin}">KC桌面</a><a href="{origin}/{locale}/">{escape(copy['home'])}</a><span>{NATIVE[locale]}</span></nav></header>
<main><h1>{escape(title)}</h1><aside class="notice"><strong>{escape(copy['machine'])}</strong><p>{escape(copy['source_note'])}</p><a href="{escape(source, quote=True)}" lang="{escape(doc['source_language'], quote=True)}">{escape(copy['source'])}</a></aside>
{''.join(blocks)}
<section><h2>{escape(copy['links'])}</h2><ul>{''.join(related)}</ul></section></main>
<footer><p>{escape(copy['access_note'])}</p><a href="{escape(source, quote=True)}">{escape(copy['source'])}</a></footer></body></html>\n'''
