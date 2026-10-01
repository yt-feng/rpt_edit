#!/usr/bin/env python3
"""Audit real published locale homepages and detail routes."""
from __future__ import annotations

import argparse
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET

from portal_extended_locales import ExpansionError, direction, select_locales
from portal_extended_ui import UI_VERSION


class MetadataParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.canonical: list[str] = []
        self.robots: list[str] = []
        self.lang = ''
        self.direction = ''
        self.ui_version = ''
        self.portal = False
        self.classes = set()
        self.ids = set()
        self.styles = []
        self.scripts = []

    def handle_starttag(self, tag, attrs):
        values = {key.lower(): str(value or '') for key, value in attrs}
        self.classes.update(values.get('class', '').split())
        self.ids.add(values.get('id', ''))
        if tag.lower() == 'body':
            self.ui_version = values.get('data-extended-ui', '')
            self.portal = values.get('data-extended-portal') == 'full'
        if tag.lower() == 'link' and values.get('rel') == 'stylesheet':
            self.styles.append(values.get('href', ''))
        if tag.lower() == 'script' and values.get('src'):
            self.scripts.append(values['src'])
        if tag.lower() == 'html':
            self.lang = values.get('lang', '')
            self.direction = values.get('dir', '')
        elif tag.lower() == 'link' and 'canonical' in values.get('rel', '').lower().split():
            self.canonical.append(values.get('href', ''))
        elif tag.lower() == 'meta' and values.get('name', '').lower() == 'robots':
            self.robots.append(values.get('content', '').lower())


def parse_metadata(body: bytes) -> MetadataParser:
    parser = MetadataParser()
    parser.feed(body.decode('utf-8'))
    parser.close()
    return parser


def require_response(session, url: str) -> tuple[dict[str, str], bytes]:
    response = session.get(url, timeout=(10, 60), allow_redirects=False,
                           headers={'User-Agent': 'Extended-locale-live-audit/1.0',
                                    'Cache-Control': 'no-cache'})
    if response.status_code != 200:
        raise ExpansionError(f'Live extended route returned HTTP {response.status_code}: {url}')
    return dict(response.headers), response.content


def check_page(body: bytes, url: str, locale: str, *, require_standard_ui=False) -> None:
    parser = parse_metadata(body)
    if parser.canonical != [url]:
        raise ExpansionError(f'Live extended page is not self-canonical: {url}')
    if parser.lang != locale or parser.direction != direction(locale):
        raise ExpansionError(f'Live extended page language/direction is invalid: {url}')
    if any('noindex' in value for value in parser.robots):
        raise ExpansionError(f'Live extended page remains noindex: {url}')
    if require_standard_ui:
        home = urlsplit(url).path == f'/{locale}/'
        classes = {'topbar', 'topbar-actions', 'brand', 'legal-footer', 'extended-language-menu'}
        classes |= {'search-panel', 'filter-grid', 'blog-card-grid', 'pagination-bar'} if home else {'blog-article', 'blog-article-content', 'blog-article-header'}
        controls = {'accountGate'} | ({'extendedSearch', 'extendedType', 'extendedFrom', 'extendedTo', 'extendedPrev', 'extendedNext'} if home else set())
        if home and parser.portal:
            controls = {'accountGate', 'searchInput', 'bankFilter', 'industryFilter', 'availabilityFilter',
                        'scopeFilter', 'startDate', 'endDate', 'clearFilters', 'results', 'pageSize',
                        'extendedType', 'extendedPrev', 'extendedNext'}
        styles = {urlsplit(href).path for href in parser.styles}
        scripts = {urlsplit(href).path for href in parser.scripts}
        if (parser.ui_version != UI_VERSION or not classes <= parser.classes or not controls <= parser.ids
                or (home and not parser.portal)
                or not {'/assets/styles.css', '/assets/blog.css', '/assets/locale.css', '/assets/extended-locales.css'} <= styles
                or '/assets/app.js' not in scripts or (home and '/assets/extended-locales.js' not in scripts)):
            raise ExpansionError(f'Extended page lacks the standard portal UI: {url}')


def audit(origin: str, locales: str, *, require_standard_ui=False) -> dict:
    # Pure metadata validation is also used by the R2-only pre-cutover guard.
    # Keep the HTTP client scoped to the actual network audit.
    import requests

    parsed = urlsplit(origin.rstrip('/'))
    if parsed.scheme != 'https' or not parsed.netloc or parsed.path not in {'', '/'}:
        raise ExpansionError('Live origin must be a bare HTTPS origin')
    origin = f'{parsed.scheme}://{parsed.netloc}'
    selected = select_locales(locales)
    session = requests.Session()
    session.trust_env = False
    reports = []
    if require_standard_ui:
        for path in ('styles.css', 'blog.css', 'locale.css', 'extended-locales.css', 'extended-locales.js', 'app.js', 'contact.js'):
            headers, body = require_response(session, origin+'/assets/'+path)
            if not body or (path.endswith('.css') and 'text/css' not in headers.get('Content-Type', '').lower()):
                raise ExpansionError(f'Live extended UI asset is missing or invalid: {path}')
    for locale in selected:
        homepage_url = f'{origin}/{locale}/'
        homepage_headers, homepage_body = require_response(session, homepage_url)
        if homepage_headers.get('Content-Language', '').strip().lower() != locale.lower():
            raise ExpansionError(f'Live locale homepage Content-Language is invalid for {locale}')
        if 'noindex' in homepage_headers.get('X-Robots-Tag', '').lower():
            raise ExpansionError(f'Live locale homepage HTTP robots policy is noindex for {locale}')
        check_page(homepage_body, homepage_url, locale, require_standard_ui=require_standard_ui)
        sitemap_url = f'{origin}/sitemap-extended-{locale}.xml'
        _sitemap_headers, sitemap_body = require_response(session, sitemap_url)
        tree = ET.fromstring(sitemap_body)
        locations = [str(node.text or '').strip() for node in tree.findall('.//{*}loc')]
        prefix = f'{origin}/{locale}/'
        if not locations or len(set(locations)) != len(locations) or any(not value.startswith(prefix) for value in locations):
            raise ExpansionError(f'Live extended sitemap contains an invalid URL: {locale}')
        samples = sorted(set((sorted(locations)[0], sorted(locations)[-1])))
        for url in samples:
            headers, body = require_response(session, url)
            if headers.get('Content-Language', '').strip().lower() != locale.lower():
                raise ExpansionError(f'Live detail Content-Language is invalid for {locale}')
            if 'noindex' in headers.get('X-Robots-Tag', '').lower():
                raise ExpansionError(f'Live detail HTTP robots policy is noindex for {locale}')
            check_page(body, url, locale, require_standard_ui=require_standard_ui)
        reports.append({'locale': locale, 'homepage_url': homepage_url, 'homepage_status': 200,
                        'pages': len(locations),
                        'deep_samples': samples, 'deep_status': 200,
                        'content_language': locale})
    return {'schema_version': 1, 'origin': origin, 'locales': list(selected), 'reports': reports,
            'status': 'passed'}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--origin', required=True)
    parser.add_argument('--locales', required=True)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--require-standard-ui', action='store_true')
    args = parser.parse_args()
    result = audit(args.origin, args.locales, require_standard_ui=args.require_standard_ui)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=True, sort_keys=True, separators=(',', ':')) + '\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=True, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
