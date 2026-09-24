#!/usr/bin/env python3
"""Collect bounded, public canonical HTML only. No protected API or PDF reads."""
from __future__ import annotations
import argparse
import json
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlsplit
import requests
from portal_extended_locales import (
    ORIGIN, MAX_DOCUMENT_BYTES, ExpansionError, document_from_html, make_corpus, public_url, stable_bytes,
)

MAX_SITEMAPS = 24
MAX_SITEMAP_BYTES = 8 * 1024 * 1024


def read_public(session, url: str, *, sitemap=False) -> bytes:
    p = urlsplit(url)
    if sitemap:
        if (p.scheme != 'https' or p.netloc != urlsplit(ORIGIN).netloc or p.query or p.fragment
                or not p.path.startswith('/sitemap') or not p.path.endswith('.xml')
                or '..' in p.path or '%' in p.path):
            raise ExpansionError('Unsafe sitemap URL')
    else: public_url(url)
    maximum = MAX_SITEMAP_BYTES if sitemap else MAX_DOCUMENT_BYTES
    with session.get(url, timeout=(10, 30), stream=True, allow_redirects=False,
                     headers={'User-Agent': 'KCdesk-public-locale-build/1.0', 'Accept': 'application/xml,text/html'}) as response:
        if response.status_code != 200: raise ExpansionError(f'Public source returned HTTP {response.status_code}')
        kind = response.headers.get('Content-Type', '').lower()
        if not any(x in kind for x in (('xml',) if sitemap else ('text/html',))):
            raise ExpansionError('Unexpected source MIME type')
        if 'noindex' in response.headers.get('X-Robots-Tag', '').lower() and not sitemap:
            raise ExpansionError('Public source response is noindex')
        parts, size = [], 0
        for chunk in response.iter_content(65536):
            size += len(chunk)
            if size > maximum: raise ExpansionError('Public source exceeds byte limit')
            parts.append(chunk)
        return b''.join(parts)


def inventory(session) -> list[str]:
    pending, seen, urls = [ORIGIN + '/sitemap.xml'], set(), set()
    while pending:
        if len(seen) >= MAX_SITEMAPS: raise ExpansionError('Sitemap inventory exceeds the configured traversal limit')
        url = pending.pop(0)
        if url in seen: continue
        seen.add(url); raw = read_public(session, url, sitemap=True)
        if b'<!DOCTYPE' in raw.upper() or b'<!ENTITY' in raw.upper(): raise ExpansionError('Sitemap entities are forbidden')
        root = ET.fromstring(raw)
        kind = root.tag.rsplit('}', 1)[-1]
        if kind not in {'sitemapindex', 'urlset'}: raise ExpansionError('Unknown sitemap root')
        for node in root:
            loc = next((child.text for child in node if child.tag.rsplit('}', 1)[-1] == 'loc'), None)
            if not loc: continue
            if kind == 'sitemapindex':
                # Existing translated sitemaps are not Chinese source documents.
                if urlsplit(loc).path.startswith('/sitemap-extended'): continue
                if any(urlsplit(loc).path == f'/sitemap-{code}.xml' for code in ('ko', 'ja', 'ar')): continue
                if loc not in seen and loc not in pending: pending.append(loc)
            else:
                try: urls.add(public_url(loc))
                except ExpansionError: pass
            if len(urls) > 100000: raise ExpansionError('Public URL inventory too large')
    return sorted(urls)


def select_urls(urls: list[str], limit: int) -> list[str]:
    if not 1 <= limit <= 500: raise ExpansionError('max-pages must be 1..500')
    core = [u for u in urls if urlsplit(u).path in {'/', '/about.html', '/reports/', '/blog/'}]
    hubs = [u for u in urls if '/institutions/' in u or '/topics/' in u]
    # Date-prefixed Blog paths sort latest first. Report hashes do not encode
    # dates; their stable selection is not mislabeled as "latest reports".
    blogs = sorted([u for u in urls if '/blog/' in u and u.endswith('.html')], reverse=True)
    reports = [u for u in urls if '/reports/' in u and u.endswith('.html') and '/institutions/' not in u and '/topics/' not in u]
    chosen = list(core)
    for index in range(max(map(len, (hubs, blogs, reports)), default=0)):
        for group in (hubs, blogs, reports):
            if index < len(group) and len(chosen) < limit: chosen.append(group[index])
        if len(chosen) >= limit: break
    return chosen[:limit]


def collect_local(root: Path, limit: int) -> dict:
    """Use an inactive built Chinese tree for exact-generation assembly."""
    root = root.resolve()
    if not root.is_dir() or root == Path(root.anchor): raise ExpansionError('Invalid inactive source root')
    by_url = {}
    for path in root.rglob('*.html'):
        if path.is_symlink(): continue
        relative = path.relative_to(root).as_posix()
        route = '/' + (relative[:-10] if relative.endswith('index.html') else relative)
        try: url = public_url(ORIGIN + route)
        except ExpansionError: continue
        by_url[url] = path
    docs = [document_from_html(url, by_url[url].read_bytes()) for url in select_urls(sorted(by_url), limit)]
    result = make_corpus(docs)
    result['collection'] = {'inventory_count': len(by_url), 'collected_count': len(docs),
                            'scope': 'bounded-inactive-Chinese-tree-not-full-archive'}
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--max-pages', type=int, default=24)
    parser.add_argument('--site-root', type=Path, help='Optional inactive built Chinese source; no HTTP calls')
    args = parser.parse_args()
    if args.site_root:
        result = collect_local(args.site_root, args.max_pages)
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_bytes(stable_bytes(result))
        print(json.dumps(result['collection']))
        return 0
    with requests.Session() as session:
        session.trust_env = False
        urls = inventory(session)
        chosen = select_urls(urls, args.max_pages)
        docs, errors = [], []
        for url in chosen:
            try: docs.append(document_from_html(url, read_public(session, url)))
            except (ExpansionError, ValueError, requests.RequestException) as error:
                errors.append({'url': url, 'error': type(error).__name__})
            time.sleep(0.15)
    if not docs: raise ExpansionError('No valid public source documents')
    corpus = make_corpus(docs)
    corpus['collection'] = {'inventory_count': len(urls), 'selected_count': len(chosen),
                            'collected_count': len(docs), 'failed': errors,
                            'scope': 'bounded-public-canonical-pages-not-full-archive'}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_bytes(stable_bytes(corpus))
    print(json.dumps(corpus['collection'], ensure_ascii=False))
    return 1 if errors else 0

if __name__ == '__main__':
    raise SystemExit(main())
