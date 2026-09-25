#!/usr/bin/env python3
"""Verify and assemble approved candidate pages into an INACTIVE site only.

This command does not upload, deploy, change DNS, touch credentials or bypass
an existing release lock. The established transactional publisher must publish
the resulting tree, after its ordinary complete-tree checks have passed.
"""
from __future__ import annotations
import argparse
import json
from html import escape
from pathlib import Path
import re
import xml.etree.ElementTree as ET
from portal_extended_locales import (
    ADDITIONAL, HREFLANG, ORIGIN, ExpansionError, PublicParser, digest, file_for_url,
    locale_url, select_locales, stable_bytes, validate_corpus,
)
from offline_translation import MODEL_ID

NS = 'http://www.sitemaps.org/schemas/sitemap/0.9'
XHTML = 'http://www.w3.org/1999/xhtml'
ET.register_namespace('', NS); ET.register_namespace('xhtml', XHTML)
MARKER_START = '<!-- kc-extended-alternates:start -->'
MARKER_END = '<!-- kc-extended-alternates:end -->'


def verified_candidate(directory: Path, corpus: dict, *, origin: str = ORIGIN) -> tuple[dict, dict[str, bytes]]:
    if directory.is_symlink() or not directory.is_dir():
        raise ExpansionError('Candidate root must be a regular directory')
    path = directory / 'candidate-manifest.json'
    if path.is_symlink() or not path.is_file() or path.stat().st_size > 1024 * 1024:
        raise ExpansionError('Missing/oversized candidate manifest')
    manifest = json.loads(path.read_text())
    if (manifest.get('schema_version') != 1 or manifest.get('locale') not in ADDITIONAL
        or manifest.get('status') != 'complete-candidate' or manifest.get('indexable') is not False
        or manifest.get('source_documents_sha256') != corpus['documents_sha256']
        or manifest.get('origin') != origin or manifest.get('model') != MODEL_ID
        or manifest.get('provider') != 'hymt' or manifest.get('paid_provider_requests') != 0
        or manifest.get('budget_exhausted') or manifest.get('failures')):
        raise ExpansionError('Candidate is not a complete matching offline build')
    docs = validate_corpus(corpus, origin=origin)
    by_url = {doc['url']: doc for doc in docs}
    pages = manifest.get('pages', [])
    if (len(pages) != len(docs) or manifest.get('completed_page_count') != len(docs)
        or manifest.get('files_sha256') != digest(stable_bytes(pages))
        or len({p.get('source_url') for p in pages}) != len(docs)):
        raise ExpansionError('Candidate coverage/digest mismatch')
    payloads = {}
    for record in pages:
        doc = by_url.get(record.get('source_url'))
        if not doc: raise ExpansionError('Unknown candidate source')
        relative = Path(manifest['locale']) / file_for_url(doc['url'], origin=origin)
        if record.get('path') != relative.as_posix(): raise ExpansionError('Unsafe candidate output path')
        source = directory / relative
        if any(p.is_symlink() for p in [source, *source.parents]
               if p == directory or directory in p.parents):
            raise ExpansionError('Candidate symlinks are forbidden')
        if not source.is_file() or source.stat().st_size > 4 * 1024 * 1024:
            raise ExpansionError('Candidate page absent or oversized')
        raw = source.read_bytes()
        if (digest(raw) != record.get('sha256') or len(raw) != record.get('bytes')
            or doc['content_sha256'] != record.get('source_content_sha256')
            or doc['source_html_sha256'] != record.get('source_html_sha256')):
            raise ExpansionError('Candidate file/source digest mismatch')
        text = raw.decode('utf-8')
        parser = PublicParser(); parser.feed(text); parser.close()
        if (parser.canonical != locale_url(doc['url'], manifest['locale'], origin=origin)
            or parser.content_lang != manifest['locale'] or 'noindex' not in parser.metadata.get('robots', '')):
            raise ExpansionError('Candidate canonical/language/robots mismatch')
        payloads[record['path']] = raw
    if origin + '/' not in by_url: raise ExpansionError('A localized homepage is required before activation')
    return manifest, payloads


def head_alternates(source: str, alternates: dict[str, str]) -> str:
    start, sep, tail = source.partition('</head>')
    if not sep: raise ExpansionError('Missing HTML head')
    start = re.sub(re.escape(MARKER_START) + r'.*?' + re.escape(MARKER_END), '', start, flags=re.S)
    # Replace language alternatives as a coherent set; preserve every other
    # head field and the entire Chinese body byte-for-byte.
    start = re.sub(r'<link\b(?=[^>]*\brel=["\']alternate["\'])(?=[^>]*\bhreflang=)[^>]*>', '', start, flags=re.I)
    links = '\n'.join(f'<link rel="alternate" hreflang="{escape(code, quote=True)}" href="{escape(url, quote=True)}">'
                      for code, url in sorted(alternates.items()))
    return start + MARKER_START + '\n' + links + '\n' + MARKER_END + sep + tail


def assemble(
    root: Path,
    corpus: dict,
    directories: list[Path],
    approved: tuple[str, ...],
    *,
    apply=False,
    origin=ORIGIN,
    existing_locales: tuple[str, ...] = (),
) -> dict:
    docs = validate_corpus(corpus, origin=origin)
    root = root.resolve()
    if not root.is_dir() or root == Path(root.anchor) or not (root / 'index.html').is_file():
        raise ExpansionError('Require a complete inactive site root')
    if (root / 'data/extended-locales/assembly.json').exists():
        raise ExpansionError('Require a fresh inactive tree and the complete approved locale set')
    # Fresh per-locale candidates are added independently, so a failed language
    # does not relabel or overwrite established ko/ja/ar mirrors.
    manifests, payloads = {}, {}
    for directory in directories:
        manifest, files = verified_candidate(directory, corpus, origin=origin)
        code = manifest['locale']
        if code in manifests: raise ExpansionError('Duplicate candidate locale')
        manifests[code] = manifest; payloads.update(files)
    if set(manifests) != set(approved) or not approved:
        raise ExpansionError('Explicit approvals must exactly match supplied complete candidates')
    for code in approved:
        if (root / code).exists(): raise ExpansionError('Existing locale directory will not be overwritten')
    planned, all_alternates = {}, {}
    for doc in docs:
        relative = file_for_url(doc['url'], origin=origin)
        source = root / relative
        if not source.is_file() or source.is_symlink() or digest(source.read_bytes()) != doc['source_html_sha256']:
            raise ExpansionError('Inactive source differs from the reviewed corpus; rebuild against this source generation')
        alternatives = {'zh-Hans': doc['url'], 'x-default': doc['url']}
        # Preserve an existing alternate only when its matching local page is
        # present and correctly self-canonical. Do not invent ko/ja/ar URLs.
        existing_alternates = dict(doc.get('source_alternates', {}))
        for code in existing_locales:
            if code not in {'ko', 'ja', 'ar'}:
                raise ExpansionError('Unknown established locale')
            existing_alternates[code] = origin + '/' + code + urlsplit_path(doc['url'])
        for code, url in existing_alternates.items():
            if code in {'zh-Hans', 'x-default'} or code not in {'ko', 'ja', 'ar'}: continue
            expected = origin + '/' + code + urlsplit_path(doc['url'])
            local = root / code / relative
            if url != expected or not local.is_file(): continue
            page = local.read_text(); parsed = PublicParser(); parsed.feed(page); parsed.close()
            if parsed.canonical == url and parsed.content_lang == code and 'noindex' not in parsed.metadata.get('robots', ''):
                alternatives[code] = url
        for code in approved:
            if code in HREFLANG: alternatives[HREFLANG[code]] = locale_url(doc['url'], code, origin=origin)
        all_alternates[doc['url']] = alternatives
        planned[relative.as_posix()] = head_alternates(source.read_text(), alternatives).encode()
        for code in ('ko', 'ja', 'ar'):
            if code in alternatives:
                p = root / code / relative
                if p.is_file():
                    planned[(Path(code) / relative).as_posix()] = head_alternates(p.read_text(), alternatives).encode()
        for code in approved:
            key = (Path(code) / relative).as_posix()
            html = payloads[key].decode()
            needle = '<meta name="robots" content="noindex,follow">'
            if html.count(needle) != 1: raise ExpansionError('Missing candidate robots guard')
            html = html.replace(needle, '<meta name="robots" content="index,follow">', 1)
            planned[key] = (head_alternates(html, alternatives) if code in HREFLANG else html).encode()
    sitemap_index = ET.Element(f'{{{NS}}}sitemapindex')
    for code in approved:
        xml = ET.Element(f'{{{NS}}}urlset')
        lines = [f'# KC桌面 — {code}', '', 'Machine-translated public reading pages. See each page for source attribution.', '']
        for doc in docs:
            canonical = locale_url(doc['url'], code, origin=origin)
            node = ET.SubElement(xml, f'{{{NS}}}url'); ET.SubElement(node, f'{{{NS}}}loc').text = canonical
            if code in HREFLANG:
                for language, href in all_alternates[doc['url']].items():
                    ET.SubElement(node, f'{{{XHTML}}}link', {'rel': 'alternate', 'hreflang': language, 'href': href})
            lines.append(f'- {canonical}')
        planned[f'sitemap-extended-{code}.xml'] = ET.tostring(xml, encoding='utf-8', xml_declaration=True)
        child = ET.SubElement(sitemap_index, f'{{{NS}}}sitemap')
        ET.SubElement(child, f'{{{NS}}}loc').text = origin + f'/sitemap-extended-{code}.xml'
        planned[f'{code}/llms.txt'] = ('\n'.join(lines) + '\n').encode()
    planned['sitemap-extended.xml'] = ET.tostring(sitemap_index, encoding='utf-8', xml_declaration=True)
    robots = root / 'robots.txt'
    if not robots.is_file(): raise ExpansionError('Existing robots.txt is required; crawler policies must not be fabricated')
    original_robots = robots.read_text()
    line = f'Sitemap: {origin}/sitemap-extended.xml'
    planned['robots.txt'] = (original_robots.rstrip() + '\n' + (line + '\n' if line not in original_robots else '')).encode()
    result = {'status': 'assembled' if apply else 'dry-run', 'locales': list(approved),
              'source_documents_sha256': corpus['documents_sha256'],
              'pages_per_locale': len(docs), 'planned_files': len(planned),
              'paid_provider_requests': 0, 'deployment_performed': False}
    planned['data/extended-locales/assembly.json'] = stable_bytes(result)
    # No write until every candidate, every original and every generated file
    # has been verified. This directory must still go through the normal slot
    # upload, exact-generation acceptance and rollback mechanism.
    if apply:
        for relative, raw in planned.items():
            target = root / relative
            if any(p.is_symlink() for p in [target, *target.parents] if p != root.parent):
                raise ExpansionError('Symlink in inactive site')
        for relative, raw in planned.items():
            target = root / relative; target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(raw)
    return result


def urlsplit_path(url):
    from urllib.parse import urlsplit
    return urlsplit(url).path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', required=True, type=Path)
    parser.add_argument('--corpus', required=True, type=Path)
    parser.add_argument('--candidate', action='append', required=True, type=Path)
    parser.add_argument('--approved-locales', required=True)
    parser.add_argument('--apply', action='store_true', help='Write only to the supplied inactive local directory; never deploy')
    args = parser.parse_args()
    approved = select_locales(args.approved_locales)
    result = assemble(args.root, json.loads(args.corpus.read_text()), args.candidate, approved, apply=args.apply)
    print(json.dumps(result, ensure_ascii=False))
    return 0

if __name__ == '__main__': raise SystemExit(main())
