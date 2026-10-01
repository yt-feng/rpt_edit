"""Shared portal presentation of already verified extended-locale content.

This layer runs AFTER candidate/checkpoint verification. It never translates,
changes article text, or adds unapproved reading URLs. Keeping the candidate
renderer stable lets old R2 checkpoints reproduce their approved bytes exactly.
"""
from __future__ import annotations

from html import escape, unescape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import urlsplit, urljoin

from portal_extended_locales import (
    ADDITIONAL, NATIVE, ORIGIN, ExpansionError, PublicParser, digest, direction,
    locale_url, walk_ld,
)

UI_VERSION = 'portal-shared-v1'
ASSETS = ('extended-locales.css', 'extended-locales.js')
ASSET_ROOT = Path(__file__).resolve().parent.parent / 'portal_suite/locale_assets'
SITE_ASSETS = ASSET_ROOT.parent / 'site_src/assets'


def ui_assets() -> dict[str, bytes]:
    return {'assets/' + name: (ASSET_ROOT / name).read_bytes() for name in ASSETS}


def asset_markup(*, index=False, origin=ORIGIN) -> str:
    def version(name):
        path = ASSET_ROOT / name if name in (*ASSETS, 'locale.css') else SITE_ASSETS / name
        return digest(path.read_bytes())[:12]
    css = ''.join(f'<link rel="stylesheet" href="/assets/{name}?v={version(name)}">'
                  for name in ('styles.css', 'blog.css', 'locale.css', 'extended-locales.css'))
    # Keep the established account/catalog handlers. Localized cards have their
    # own IDs so the source catalog cannot replace the approved collection.
    scripts = ''.join(f'<script defer src="/assets/{name}?v={version(name)}"></script>'
                      for name in ('contact.js', 'app.js'))
    if index:
        scripts += f'<script defer src="/assets/extended-locales.js?v={version("extended-locales.js")}"></script>'
    # Resolve relative data requests against the established root catalog.
    # Generated report/doc URLs also honor the explicit data-extended-ui marker.
    return f'<base href="{escape(origin, quote=True)}/"><link rel="icon" href="/favicon.svg" type="image/svg+xml">' + css + scripts


def page_parts(raw: bytes, locale: str, url: str, *, origin=ORIGIN) -> dict:
    if locale not in ADDITIONAL:
        raise ExpansionError('Shared presentation excludes English and established locales')
    text = raw.decode('utf-8')
    parsed = PublicParser(); parsed.feed(text); parsed.close()
    if (parsed.content_lang != locale or parsed.canonical != locale_url(url, locale, origin=origin)
            or 'noindex' in parsed.metadata.get('robots', '').lower()):
        raise ExpansionError('Shared presentation requires an approved indexable page')
    match = re.search(r'<main><h1>(.*?)</h1>(<aside class="notice">.*?</aside>)\s*(.*?)\s*</main>', text, re.S)
    header = re.search(r'<body><header><nav>.*?<a [^>]+>.*?</a><a [^>]+>(.*?)</a>', text, re.S)
    footer = re.search(r'<footer><p>(.*?)</p><a [^>]+>(.*?)</a></footer>', text, re.S)
    if not match or not header or not footer:
        raise ExpansionError('Unknown approved candidate presentation')
    nodes = [node for value in parsed.jsonld for node in walk_ld(value)
             if node.get('url') == parsed.canonical and node.get('@type') in {'Article', 'WebPage'}]
    if len(nodes) != 1:
        raise ExpansionError('Shared presentation requires one matching content identity')
    node = nodes[0]
    return dict(html=text, title=match[1], notice=match[2], content=match[3],
                home=header[1], access=footer[1], source=footer[2], canonical=parsed.canonical,
                description=parsed.metadata.get('description', ''), date=str(node.get('datePublished') or '')[:10],
                kind='blog' if '/blog/' in urlsplit(url).path else 'reports', url=url)


def chrome(locale: str, home_label: str, source_label: str, *, source: str,
           alternates: dict[str, str], origin=ORIGIN, index=False) -> tuple[str, str]:
    home = origin.rstrip('/') + '/' + locale + '/'
    nav = [(home, home_label), (home + '?type=blog', 'Blog'),
           (home + '?type=reports', 'Reports'), (origin + '/research.html', 'AI Research'),
           (origin + '/courses.html', 'Course'), (origin + '/charts', 'Charts'),
           (origin + '/newsfeed.html', 'Newsfeed')]
    links = []
    for i, (href, label) in enumerate(nav):
        current = ' aria-current="page"' if i == 0 and index else ''
        language = f' lang="{locale if i == 0 else "en"}"'
        links.append(f'<a class="topbar-link{" is-active" if i == 0 else ""}"{current}'
                     f' href="{escape(href, quote=True)}"{language}>{label}</a>')
    links = ''.join(links)
    # Only real, verified alternates are exposed; English never joins the menu.
    choices = []
    for code, href in alternates.items():
        key = 'zh' if code == 'zh-Hans' else code
        if key not in NATIVE or key == 'en':
            continue
        current = ' aria-current="page"' if code == locale else ''
        choices.append(f'<a href="{escape(href, quote=True)}" lang="{escape(code, quote=True)}"'
                       f'{current}>{escape(NATIVE[key])}</a>')
    if locale == 'yue':
        choices.append(f'<a href="{escape(home if index else locale_url(source, locale, origin=origin), quote=True)}" '
                       'lang="yue" aria-current="page">粵語</a>')
    switcher = ('<details class="extended-language-menu"><summary>' + escape(NATIVE[locale]) +
                '</summary><nav aria-label="Languages" lang="en">' + ''.join(choices) + '</nav></details>')
    top = f'''<header class="topbar blog-topbar">
<a class="brand" href="{escape(home, quote=True)}"><img src="/assets/app-mark.svg" alt="" width="34" height="34"><span>KC桌面</span></a>
<nav class="topbar-actions" aria-label="Navigation" lang="en">{links}
<button id="accountGate" class="account-button" type="button">Login</button>
<button class="account-button signup-button" type="button" data-auth-open="register" data-auth-placement="navigation" data-guest-only>Register</button></nav>
{switcher}</header>
<aside class="kc-locale-help"><a href="{escape(source, quote=True)}" hreflang="zh-Hans">{source_label} · 中文</a>
<a href="{escape(origin, quote=True)}/" lang="zh-Hans">中文 · kcdesk.com</a><a href="mailto:info@kcdesk.com">info@kcdesk.com</a></aside>'''
    bottom = f'''<footer class="legal-footer blog-footer" lang="en"><a href="{escape(home, quote=True)}">{home_label}</a>
<a href="{origin}/about.html">About KC桌面</a><a href="{origin}/terms.html">Terms of Service</a>
<a href="{origin}/privacy.html">Privacy</a><a href="{origin}/?request=support">Contact</a></footer>'''
    return top, bottom


def standard_detail(raw: bytes, locale: str, url: str, *, alternates: dict[str, str], origin=ORIGIN) -> bytes:
    parts = page_parts(raw, locale, url, origin=origin)
    top, footer = chrome(locale, parts['home'], parts['source'], source=url, alternates=alternates, origin=origin)
    head = parts['html'].split('</head>', 1)[0]
    head = re.sub(r'<style>.*?</style>', '', head, flags=re.S) + asset_markup(origin=origin)
    home = origin + '/' + locale + '/'
    # All content blocks, source links and notice copy survive verbatim.
    return (head + f'''</head><body class="blog-page blog-article-page extended-page" data-page="blog-article" data-extended-ui="{UI_VERSION}">
{top}<main class="blog-article-shell"><a class="blog-back" href="{home}">← {parts['home']}</a>
<article class="blog-article"><header class="blog-article-header">
<nav aria-label="Breadcrumb"><a href="{home}">{parts['home']}</a> › <span>{escape(NATIVE[locale])}</span></nav>
<div class="blog-card-meta"><time datetime="{escape(parts['date'], quote=True)}">{escape(parts['date'])}</time><span>{escape(NATIVE[locale])}</span></div>
<h1>{parts['title']}</h1></header>
{parts['notice']}<div class="blog-article-content">{parts['content']}</div>
<aside class="blog-next-step"><p>{parts['access']}</p><a class="btn" href="{escape(url, quote=True)}">{parts['source']}</a></aside>
</article></main>{footer}</body></html>\n''').encode()


def standard_homepage(locale: str, pages: list[tuple[str, bytes]], *, origin=ORIGIN,
                      alternates: dict[str, str] | None = None, portal_home: str | None = None) -> bytes:
    if not pages:
        raise ExpansionError('Locale homepage requires approved details')
    parts = [page_parts(raw, locale, url, origin=origin) for url, raw in pages]
    parts.sort(key=lambda row: (row['date'], row['url']), reverse=True)
    first = parts[0]
    top, footer = chrome(locale, first['home'], first['source'], source=origin+'/',
                         alternates=alternates or {locale: origin+'/'+locale+'/'}, origin=origin, index=True)
    cards = []
    for row in parts:
        cards.append(f'''<article class="blog-card extended-result" data-kind="{row['kind']}" data-date="{escape(row['date'], quote=True)}">
<div class="blog-card-meta"><time datetime="{escape(row['date'], quote=True)}">{escape(row['date'])}</time><span>{escape(NATIVE[locale])}</span><span lang="en">{row['kind']}</span></div>
<h2><a href="{escape(row['canonical'], quote=True)}">{row['title']}</a></h2><p>{escape(row['description'])}</p></article>''')
    canonical = origin+'/'+locale+'/'
    schema = json.dumps({'@context': 'https://schema.org', '@type': 'CollectionPage', 'url': canonical,
                         'name': 'KC桌面 · '+NATIVE[locale], 'inLanguage': locale,
                         'mainEntity': {'@type': 'ItemList', 'numberOfItems': len(parts),
                                        'itemListElement': [{'@type': 'ListItem', 'position': i+1, 'url': p['canonical']}
                                                            for i, p in enumerate(parts)]}}, ensure_ascii=False).replace('<', '\\u003c')
    rendered = f'''<!doctype html><html lang="{locale}" dir="{direction(locale)}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>KC桌面 · {escape(NATIVE[locale])}</title>
<meta name="description" content="KC桌面 · {escape(NATIVE[locale], quote=True)}"><meta name="robots" content="index,follow">
<link rel="canonical" href="{escape(canonical, quote=True)}"><script type="application/ld+json">{schema}</script>{asset_markup(index=True, origin=origin)}</head>
<body class="blog-page extended-page" data-page="blog-article" data-extended-ui="{UI_VERSION}">{top}
<main class="shell"><section class="search-panel" aria-labelledby="extendedTitle">
<div class="search-copy"><p class="blog-kicker">KC桌面</p><h1 id="extendedTitle">{escape(NATIVE[locale])}</h1>
<p class="subtle">{first['access']}</p></div>
<label class="search-box search-main"><span lang="en">Search</span><input id="extendedSearch" type="search" autocomplete="off" aria-label="Search" placeholder="Search"></label>
<div class="filter-grid" lang="en">
<label class="filter-control"><span>Content</span><select id="extendedType"><option value="">All</option><option value="blog">Blog</option><option value="reports">Reports</option></select></label>
<label class="filter-control"><span>From</span><input id="extendedFrom" type="date"></label>
<label class="filter-control"><span>To</span><input id="extendedTo" type="date"></label>
<label class="filter-control"><span>Sort</span><select id="extendedSort"><option value="newest">Newest</option><option value="oldest">Oldest</option></select></label>
</div><div class="filter-actions"><span id="extendedCount" role="status" aria-live="polite">{len(parts)}</span><button id="extendedClear" type="button" lang="en">Clear</button></div></section>
<section class="results-section"><div class="results-heading"><h2>KC桌面 · {escape(NATIVE[locale])}</h2></div>
<div id="extendedResults" class="blog-card-grid">{''.join(cards)}</div><p id="extendedEmpty" class="empty-state" lang="en" hidden>No matching pages. <a href="{origin}/">Search the source catalog →</a></p>
<nav class="pagination-bar" lang="en" aria-label="Pagination"><button id="extendedPrev" type="button">Previous</button><span id="extendedPage" aria-live="polite">1</span><button id="extendedNext" type="button">Next</button></nav>
</section></main>{footer}</body></html>\n'''.encode()
    if portal_home is not None:
        rendered = portal_homepage(portal_home, rendered, locale, pages, origin=origin)
    return rendered


class PortalLinks(HTMLParser):
    """Resolve root-template links without inventing untranslated locale routes."""
    def __init__(self, locale, approved, origin):
        super().__init__(convert_charrefs=False)
        self.locale, self.approved, self.origin, self.parts = locale, approved, origin, []

    def handle_starttag(self, tag, attrs):
        rewritten = []
        for key, value in attrs:
            if value and key in {'href', 'src', 'action'} and not value.startswith(('#', 'mailto:', 'data:', 'tel:')):
                value = urljoin(self.origin+'/', value)
                if key == 'href' and value in self.approved:
                    value = locale_url(value, self.locale, origin=self.origin)
            rewritten.append(key if value is None else f'{key}="{escape(value, quote=True)}"')
        self.parts.append('<'+tag+(' '+ ' '.join(rewritten) if rewritten else '')+'>')

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
    def handle_endtag(self, tag): self.parts.append('</'+tag+'>')
    def handle_data(self, value): self.parts.append(value)
    def handle_entityref(self, value): self.parts.append('&'+value+';')
    def handle_charref(self, value): self.parts.append('&#'+value+';')
    def handle_comment(self, value): self.parts.append('<!--'+value+'-->')


def portal_homepage(source: str, collection: bytes, locale: str, pages, *, origin=ORIGIN) -> bytes:
    """Reuse the complete released search/application main, not a lookalike form.

    Catalog search, institution/industry/PDF filters, external reports, member
    gates, and pagination keep their established IDs and application handlers.
    They continue to use the source catalog. The approved localized collection
    is additionally searchable above the source results, without historical
    translation or fake locale detail links.
    """
    main = re.search(r'<main\b[^>]*>.*?</main>', source, re.S)
    required = ('searchInput', 'searchTitle', 'bankFilter', 'industryFilter', 'availabilityFilter',
                'scopeFilter', 'startDate', 'endDate', 'clearFilters', 'results', 'pageSize')
    if not main or any(f'id="{name}"' not in main[0] for name in required):
        raise ExpansionError('Extended homepage requires the complete released portal search template')
    parser = PortalLinks(locale, {url for url, raw in pages}, origin)
    parser.feed(main[0]); parser.close()
    body = ''.join(parser.parts)
    body = re.sub(r'(<h1\b[^>]*id="searchTitle"[^>]*>).*?(</h1>)',
                  lambda m: m[1]+'KC桌面 · '+escape(NATIVE[locale])+m[2], body, count=1, flags=re.S)
    html = collection.decode()
    local_results = re.search(r'<section class="results-section">.*?</section>', html, re.S)[0]
    controls = f'''<div class="filter-grid" lang="en"><label class="filter-control"><span>Content</span>
<select id="extendedType"><option value="">All</option><option value="blog">Blog</option><option value="reports">Reports</option></select></label>
<label class="filter-control"><span>Sort</span><select id="extendedSort"><option value="newest">Newest</option><option value="oldest">Oldest</option></select></label></div>
<p id="extendedCount" role="status" aria-live="polite">{len(pages)}</p>'''
    local_results = local_results.replace('<div id="extendedResults"', controls+'<div id="extendedResults"', 1)
    anchor = '<section class="results-section">'
    if anchor not in body:
        raise ExpansionError('Portal search result section is missing')
    body = body.replace(anchor, local_results+'\n'+anchor, 1)
    html = re.sub(r'<main\b[^>]*>.*?</main>', lambda _m: body, html, count=1, flags=re.S)
    html = html.replace('data-page="blog-article"', 'data-page="index" data-extended-portal="full"', 1)
    return html.encode()
