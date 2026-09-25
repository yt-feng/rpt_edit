#!/usr/bin/env python3
"""Today-only private translation candidates; never activate or backfill history."""
from __future__ import annotations
import argparse
import json
from datetime import datetime
from pathlib import Path
import re
from urllib.parse import urlsplit
from zoneinfo import ZoneInfo
import requests

from collect_portal_extended_sources import inventory_entries, read_public
from portal_extended_locales import (
    DAILY_SCOPE, INCREMENTAL_START, ExpansionError, daily_corpus_day, daily_document,
    digest, document_from_html, make_corpus, publication_day, select_locales, stable_bytes,
    validate_corpus,
)
from portal_extended_r2 import (R2Store, R2NotFound, R2IntegrityError, HEX64, MODEL_ID, DEFAULT_PREFIX,
                               checkpoint_is_valid, MAX_CHECKPOINT_BYTES)
from assemble_portal_extended_locales import verified_candidate


def today() -> str:
    return datetime.now(ZoneInfo('Asia/Shanghai')).date().isoformat()


def eligible_url(url: str, lastmod: str, day: str) -> bool:
    path = urlsplit(url).path
    blog = re.fullmatch(r'/blog/(\d{8})-[A-Za-z0-9_.-]+\.html', path)
    if blog: return blog[1] == day.replace('-', '')
    return bool(re.fullmatch(r'/reports/[A-Za-z0-9_-]+\.html', path)
                and path not in {'/reports/index.html', '/reports/topics.html'}
                and publication_day(lastmod) == day)


def collect_today(session, day: str) -> list[dict]:
    if publication_day(day) != day or day < INCREMENTAL_START:
        raise ExpansionError('Daily collection date precedes incremental launch or is invalid')
    entries = inventory_entries(session)
    urls = sorted(url for url, modified in entries.items() if eligible_url(url, modified, day))
    if len(urls) > 500: raise ExpansionError('Today inventory exceeds 500 detail pages; explicit partitioning required')
    docs = []
    for url in urls:
        # A sitemap lastmod is a fetch hint, NOT proof that an old article is new.
        doc = document_from_html(url, read_public(session, url), exclude_related=True)
        if not daily_document(doc, day): continue
        docs.append(doc)
    admitted_urls = {doc['url'] for doc in docs}
    for doc in docs:
        # Only translate this detail and today's related URLs, not historic link labels.
        doc['links'] = [row for row in doc['links'] if row['url'] in admitted_urls]
        doc['selection_scope'], doc['selection_day'] = DAILY_SCOPE, day
        doc['content_sha256'] = digest(stable_bytes({k: v for k, v in doc.items() if k != 'content_sha256'}))
    return docs


def content_key(doc: dict) -> str:
    # Navigation/hreflang/head-only refreshes do not require new inference.
    return digest(stable_bytes({key: doc[key] for key in (
        'url', 'source_language', 'title', 'description', 'blocks', 'links', 'datePublished', 'dateModified')}))


def state_key(store: R2Store, kind: str, locale: str, day: str = '') -> str:
    if select_locales(locale) != (locale,): raise ExpansionError('Expected one non-English locale')
    if day and (publication_day(day) != day or day < INCREMENTAL_START):
        raise ExpansionError('Invalid incremental state date')
    return store.key('incremental', kind, locale, day or 'latest', 'state.json')


def read_state(store: R2Store, kind: str, locale: str, day: str = '') -> dict:
    try: raw = store._get(state_key(store, kind, locale, day), maximum=512 * 1024)
    except R2NotFound: return {}
    try: value = json.loads(raw)
    except (ValueError, UnicodeDecodeError): raise R2IntegrityError('Invalid incremental state JSON') from None
    if not isinstance(value, dict) or any(value.get(k) != v for k, v in
        {'schema_version': 1, 'scope': DAILY_SCOPE, 'model': MODEL_ID, 'locale': locale, 'day': day}.items()):
        raise R2IntegrityError('Incremental state identity mismatch')
    return value


def write_state(store: R2Store, kind: str, locale: str, fields: dict, day: str = '') -> None:
    value = {**fields, 'schema_version': 1, 'scope': DAILY_SCOPE, 'model': MODEL_ID, 'locale': locale, 'day': day}
    raw = stable_bytes(value)
    if len(raw) > 512 * 1024: raise R2IntegrityError('Incremental state exceeds bound')
    store._put(state_key(store, kind, locale, day), raw, metadata={'kind': kind, 'locale': locale})


def prepare(store: R2Store, docs: list[dict], locales: tuple[str, ...], day: str, output: Path,
            *, limit=24) -> dict:
    if not 1 <= limit <= 24: raise ExpansionError('Daily batch must be 1..24 detail pages')
    if docs:
        validated = make_corpus(docs)
        if daily_corpus_day(validated) != day: raise ExpansionError('Only today detail pages may enter this batch')
    receipts = {locale: read_state(store, 'completed', locale, day).get('pages', {}) for locale in locales}
    if any(not isinstance(rows, dict) for rows in receipts.values()): raise R2IntegrityError('Invalid page receipts')
    pending = [doc for doc in sorted(docs, key=lambda doc: doc['url'])
               if not all(receipts[locale].get(doc['url'], {}).get('content_key') == content_key(doc) for locale in locales)]
    result = {'day': day, 'scope': DAILY_SCOPE, 'today_page_count': len(docs), 'pending_page_count': len(pending),
              'selected_page_count': min(len(pending), limit), 'remaining_page_count': max(0, len(pending)-limit),
              'has_work': bool(pending), 'generation': '', 'locales_json': json.dumps(list(locales)), 'paid_provider_requests': 0}
    if not pending: return result
    corpus = make_corpus(pending[:limit])
    # No varying timestamps/counts in the immutable source object.
    store.put_source(corpus)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(stable_bytes(corpus))
    result['generation'] = corpus['documents_sha256']
    return result


def restore_seed(store: R2Store, locale: str, output: Path) -> dict:
    pointer = read_state(store, 'memo', locale)
    if not pointer: return {'present': False, 'locale': locale}
    generation, checksum = pointer.get('generation', ''), pointer.get('sha256', '')
    if not HEX64.fullmatch(generation) or not HEX64.fullmatch(checksum):
        raise R2IntegrityError('Invalid incremental memo identity')
    # Follow the immutable snapshot, not the mutable per-generation latest pointer.
    key = store.checkpoint_object_key(locale, generation, checksum)
    raw = store._get(key, maximum=MAX_CHECKPOINT_BYTES)
    if digest(raw) != checksum:
        raise R2IntegrityError('Incremental memo checksum mismatch')
    checkpoint_is_valid(json.loads(raw), locale, generation)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(raw)
    return {'present': True, 'locale': locale, 'generation': generation, 'sha256': checksum, 'bytes': len(raw)}


def remember_checkpoint(store: R2Store, locale: str, generation: str, checkpoint: Path) -> dict:
    result = store.put_checkpoint(locale, generation, checkpoint)
    write_state(store, 'memo', locale, {'generation': generation, 'sha256': result['sha256']})
    return result


def remember_candidate(store: R2Store, locale: str, corpus: dict, directory: Path) -> dict:
    validate_corpus(corpus)
    day = daily_corpus_day(corpus)
    if not day: raise ExpansionError('Only new daily content may update incremental receipts')
    generation = corpus['documents_sha256']
    manifest = json.loads((directory/'candidate-manifest.json').read_text())
    if manifest.get('status') == 'complete-candidate': verified_candidate(directory, corpus)
    result = store.upload_candidate(directory, locale, generation)
    if not result['ready']: return result
    pages = read_state(store, 'completed', locale, day).get('pages', {})
    if not isinstance(pages, dict): raise R2IntegrityError('Invalid page receipts')
    for doc in corpus['documents']:
        pages[doc['url']] = {'content_key': content_key(doc), 'generation': generation, 'candidate_id': result['candidate_id']}
    write_state(store, 'completed', locale, {'pages': pages}, day)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=['prepare', 'restore-seed', 'checkpoint', 'candidate'])
    parser.add_argument('--prefix', default=DEFAULT_PREFIX)
    parser.add_argument('--locale', default='fr')
    parser.add_argument('--locales', default='fr')
    parser.add_argument('--corpus', type=Path)
    parser.add_argument('--checkpoint', type=Path)
    parser.add_argument('--directory', type=Path)
    parser.add_argument('--generation')
    parser.add_argument('--github-output', type=Path)
    args = parser.parse_args()
    store = R2Store.from_env(args.prefix)
    if args.operation == 'prepare':
        locales = select_locales(args.locales)
        day = today()
        if args.generation:
            store.restore_source(args.generation, args.corpus)
            corpus = json.loads(args.corpus.read_text())
            validate_corpus(corpus)
            if daily_corpus_day(corpus) != day: raise ExpansionError('Refusing to resume a historical or mixed-directory batch')
            result = {'has_work': True, 'generation': args.generation, 'locales_json': json.dumps(list(locales)),
                      'day': day, 'selected_page_count': len(corpus['documents'])}
            if len(corpus['documents']) > 24: raise ExpansionError('Daily batch exceeds 24 pages')
        else:
            with requests.Session() as session:
                # Use normal runner networking; no local proxy or network changes.
                docs = collect_today(session, day)
            result = prepare(store, docs, locales, day, args.corpus)
        if args.github_output:
            with args.github_output.open('a') as stream:
                for key in ('has_work', 'generation', 'locales_json'):
                    value = str(result[key]).lower() if isinstance(result[key], bool) else result[key]
                    stream.write(f'{key}={value}\n')
    else:
        if select_locales(args.locale) != (args.locale,): raise ExpansionError('Expected one locale')
        if args.operation == 'restore-seed': result = restore_seed(store, args.locale, args.checkpoint)
        elif args.operation == 'checkpoint': result = remember_checkpoint(store, args.locale, args.generation, args.checkpoint)
        else:
            corpus = json.loads(args.corpus.read_text())
            if corpus.get('documents_sha256') != args.generation: raise ExpansionError('Candidate source generation mismatch')
            result = remember_candidate(store, args.locale, corpus, args.directory)
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
