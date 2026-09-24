#!/usr/bin/env python3
"""Audit activated extended-locale homepage and one deep page per locale."""
from __future__ import annotations

import argparse
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET

import requests

from portal_extended_locales import ExpansionError, direction, select_locales


class MetadataParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.canonical: list[str] = []
        self.robots: list[str] = []
        self.lang = ''
        self.direction = ''

    def handle_starttag(self, tag, attrs):
        values = {key.lower(): str(value or '') for key, value in attrs}
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
                           headers={'User-Agent': 'KCDesk-extended-locale-live-audit/1.0',
                                    'Cache-Control': 'no-cache'})
    if response.status_code != 200:
        raise ExpansionError(f'Live extended route returned HTTP {response.status_code}: {url}')
    return dict(response.headers), response.content


def check_page(body: bytes, url: str, locale: str) -> None:
    parser = parse_metadata(body)
    if parser.canonical != [url]:
        raise ExpansionError(f'Live extended page is not self-canonical: {url}')
    if parser.lang != locale or parser.direction != direction(locale):
        raise ExpansionError(f'Live extended page language/direction is invalid: {url}')
    if any('noindex' in value for value in parser.robots):
        raise ExpansionError(f'Live extended page remains noindex: {url}')


def audit(origin: str, locales: str) -> dict:
    parsed = urlsplit(origin.rstrip('/'))
    if parsed.scheme != 'https' or not parsed.netloc or parsed.path not in {'', '/'}:
        raise ExpansionError('Live origin must be a bare HTTPS origin')
    origin = f'{parsed.scheme}://{parsed.netloc}'
    selected = select_locales(locales)
    session = requests.Session()
    session.trust_env = False
    reports = []
    for locale in selected:
        homepage_url = f'{origin}/{locale}/'
        headers, homepage = require_response(session, homepage_url)
        expected_language = headers.get('Content-Language', '').strip().lower()
        if expected_language != locale.lower():
            raise ExpansionError(f'Live Content-Language is invalid for {locale}: {expected_language}')
        check_page(homepage, homepage_url, locale)
        sitemap_url = f'{origin}/sitemap-extended-{locale}.xml'
        _sitemap_headers, sitemap_body = require_response(session, sitemap_url)
        tree = ET.fromstring(sitemap_body)
        locations = [str(node.text or '').strip() for node in tree.findall('.//{*}loc')]
        prefix = f'{origin}/{locale}/'
        if not locations or any(not value.startswith(prefix) for value in locations):
            raise ExpansionError(f'Live extended sitemap contains an invalid URL: {locale}')
        deep_url = sorted(value for value in set(locations) if value.rstrip('/') != homepage_url.rstrip('/'))[0]
        deep_headers, deep_body = require_response(session, deep_url)
        if deep_headers.get('Content-Language', '').strip().lower() != locale.lower():
            raise ExpansionError(f'Live deep Content-Language is invalid for {locale}')
        check_page(deep_body, deep_url, locale)
        reports.append({'locale': locale, 'pages': len(locations), 'homepage': homepage_url,
                        'deep_sample': deep_url, 'homepage_status': 200, 'deep_status': 200,
                        'content_language': locale})
    return {'schema_version': 1, 'origin': origin, 'locales': list(selected), 'reports': reports,
            'status': 'passed'}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--origin', required=True)
    parser.add_argument('--locales', required=True)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    result = audit(args.origin, args.locales)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=True, sort_keys=True, separators=(',', ':')) + '\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=True, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
