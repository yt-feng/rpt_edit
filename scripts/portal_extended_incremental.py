#!/usr/bin/env python3
"""Continue registered daily candidates before selecting today; never discover history."""
from __future__ import annotations
import argparse
import json
import os
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
                               R2StoreError, checkpoint_is_valid, MAX_CHECKPOINT_BYTES)
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


def collect_today(session, day: str, *, on_source=None) -> list[dict]:
    if publication_day(day) != day or day < INCREMENTAL_START:
        raise ExpansionError('Daily collection date precedes incremental launch or is invalid')
    entries = inventory_entries(session)
    urls = sorted(url for url, modified in entries.items() if eligible_url(url, modified, day))
    if len(urls) > 500: raise ExpansionError('Today inventory exceeds 500 detail pages; explicit partitioning required')
    docs = []
    for url in urls:
        # A sitemap lastmod is a fetch hint, NOT proof that an old article is new.
        raw = read_public(session, url)
        doc = document_from_html(url, raw, exclude_related=True)
        if not daily_document(doc, day): continue
        if on_source is not None:
            on_source(doc, raw)
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
    # Validate even empty days, before any storage access or matrix generation.
    if select_locales(','.join(locales)) != locales:
        raise ExpansionError('Expected distinct non-English expansion locales')
    if docs:
        validated = make_corpus(docs)
        if daily_corpus_day(validated) != day: raise ExpansionError('Only today detail pages may enter this batch')
    receipts = {locale: read_state(store, 'completed', locale, day).get('pages', {}) for locale in locales}
    if any(not isinstance(rows, dict) for rows in receipts.values()): raise R2IntegrityError('Invalid page receipts')
    pending = [doc for doc in sorted(docs, key=lambda doc: doc['url'])
               if not all(receipts[locale].get(doc['url'], {}).get('content_key') == content_key(doc) for locale in locales)]
    selected = pending[:limit]
    # A slower locale must not restart an already completed locale. All remaining
    # jobs still share the same immutable source; unit memos reuse partial work.
    active_locales = [locale for locale in locales if any(
        receipts[locale].get(doc['url'], {}).get('content_key') != content_key(doc) for doc in selected)]
    result = {'day': day, 'scope': DAILY_SCOPE, 'today_page_count': len(docs), 'pending_page_count': len(pending),
              'selected_page_count': min(len(pending), limit), 'remaining_page_count': max(0, len(pending)-limit),
              'has_work': bool(pending), 'generation': '', 'locales_json': json.dumps(active_locales),
              'requested_locale_count': len(locales), 'pending_locale_count': len(active_locales),
              'paid_provider_requests': 0}
    if not pending: return result
    corpus = make_corpus(selected)
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
    from portal_extended_continuation import require_active_owner
    require_active_owner(store, locale, generation)
    result = store.put_checkpoint(locale, generation, checkpoint)
    write_state(store, 'memo', locale, {'generation': generation, 'sha256': result['sha256']})
    return result


def remember_candidate(store: R2Store, locale: str, corpus: dict, directory: Path) -> dict:
    validate_corpus(corpus)
    day = daily_corpus_day(corpus)
    if not day: raise ExpansionError('Only new daily content may update incremental receipts')
    generation = corpus['documents_sha256']
    from portal_extended_continuation import require_active_owner
    require_active_owner(store, locale, generation)
    manifest = json.loads((directory/'candidate-manifest.json').read_text())
    if manifest.get('status') == 'complete-candidate': verified_candidate(directory, corpus)
    result = store.upload_candidate(directory, locale, generation)
    from portal_extended_continuation import record_result
    record_result(store, locale, corpus, result)
    if not result['ready']: return result
    pages = read_state(store, 'completed', locale, day).get('pages', {})
    if not isinstance(pages, dict): raise R2IntegrityError('Invalid page receipts')
    for doc in corpus['documents']:
        pages[doc['url']] = {'content_key': content_key(doc), 'generation': generation, 'candidate_id': result['candidate_id']}
    write_state(store, 'completed', locale, {'pages': pages}, day)
    return result


def include_english_matrix(store, result):
    """One English editorial job in the SAME two-CPU matrix, not a third runner."""
    from portal_english_commentary import PREFIX
    from portal_english_pipeline import prepare_queued
    prefix = PREFIX if store.prefix == DEFAULT_PREFIX else store.prefix+'/english-commentary'
    result = dict(result)
    result.update(english_admission='', english_pending_count='0', english_prepare_incomplete=False)
    try:
        english = prepare_queued(R2Store(store.client, store.bucket, prefix), store)
    except (ExpansionError, R2StoreError):
        result['english_prepare_incomplete'] = True
        result['english_prepare_code'] = 'english-admission-unavailable'
        return result
    if english['job'] is not None:
        # The non-English approval list/source day retain their exact meaning.
        # Each matrix row already owns its separate source generation/day.
        jobs = json.loads(result['locale_jobs_json'])
        if any(row['locale'] == 'en' for row in jobs): raise ExpansionError('Duplicate English matrix row')
        result['locale_jobs_json'] = json.dumps([english['job']] + jobs)
        result['has_work'] = True
        result['english_admission'] = english['admission']
        result['english_pending_count'] = str(english['pending_count'])
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=['prepare', 'prepare-recovery', 'prepare-publication', 'restore-seed', 'restore-checkpoint', 'checkpoint', 'candidate'])
    parser.add_argument('--prefix', default=DEFAULT_PREFIX)
    parser.add_argument('--locale', default='fr')
    parser.add_argument('--locales', default='all-supported')
    parser.add_argument('--corpus', type=Path)
    parser.add_argument('--checkpoint', type=Path)
    parser.add_argument('--directory', type=Path)
    parser.add_argument('--generation')
    parser.add_argument('--github-output', type=Path)
    parser.add_argument('--continuation-evidence', default='')
    parser.add_argument('--include-english', action='store_true', help='Add separately admitted KC comments to the existing CPU matrix')
    args = parser.parse_args()
    if args.include_english and (args.operation != 'prepare' or args.generation):
        raise ExpansionError('English inclusion is only for normal admitted daily cursors, not explicit/recovery generations')
    if args.include_english and (os.environ.get('GITHUB_ACTIONS') != 'true'
        or os.environ.get('GITHUB_REF') != 'refs/heads/main' or os.environ.get('KC_PUBLIC_REPOSITORY') != 'true'):
        raise ExpansionError('English daily inclusion requires reviewed main public Actions')
    store = R2Store.from_env(args.prefix)
    if args.operation in {'prepare', 'prepare-recovery', 'prepare-publication'}:
        requested_locales = locales = select_locales(args.locales)
        day = today()
        recovery = args.operation == 'prepare-recovery'
        publication = args.operation == 'prepare-publication'
        if (recovery or publication) and not args.generation:
            raise ExpansionError('Recovery/publication requires an exact stored source generation')
        from portal_extended_continuation import (adopt_existing, pending, queue, read_origin, register)
        producer = None
        if os.environ.get('GITHUB_ACTIONS') == 'true' and os.environ.get('GITHUB_REF') == 'refs/heads/main':
            producer = {'run_id': os.environ['GITHUB_RUN_ID'], 'attempt': os.environ['GITHUB_RUN_ATTEMPT'],
                        'sha': os.environ['GITHUB_SHA']}
        if args.continuation_evidence and not publication:
            raise ExpansionError('Existing-generation adoption is only allowed by explicit publication-resume')
        stopped = []
        if producer and not recovery:
            from portal_extended_continuation import partition_stopped_locales
            locales, stopped = partition_stopped_locales(store, locales)
        if not locales:
            result = {'has_work': False, 'generation': '', 'locales_json': '[]', 'day': day}
        elif args.generation:
            store.restore_source(args.generation, args.corpus)
            corpus = json.loads(args.corpus.read_text())
            validate_corpus(corpus)
            corpus_day = daily_corpus_day(corpus)
            if not corpus_day or (corpus_day != day and not (recovery or publication)):
                raise ExpansionError('Refusing to resume a historical or mixed-directory batch')
            if len(corpus['documents']) > 24: raise ExpansionError('Daily batch exceeds 24 pages')
            result = {'has_work': True, 'generation': args.generation, 'locales_json': json.dumps(list(locales)),
                      'day': corpus_day, 'selected_page_count': len(corpus['documents']),
                      'recovery_test_only': recovery}
            if publication:
                if not producer:
                    raise ExpansionError('Publication continuation runs only on reviewed main Actions')
                if args.continuation_evidence:
                    from review_portal_extended_handoff import api
                    adopt_existing(store, corpus, locales, json.loads(args.continuation_evidence),
                                   os.environ['GITHUB_REPOSITORY'], api)
                origin = read_origin(store, args.generation)
                if not origin or any(args.generation not in queue(store, locale) for locale in locales):
                    raise ExpansionError('Publication resume requires a registered original generation and existing checkpoint outcome')
                result = pending(store, locales, args.corpus, generation=args.generation)
                if result is None:
                    result = {'has_work': False, 'generation': args.generation, 'locales_json': '[]',
                              'day': corpus_day, 'continuation': True}
            elif not recovery and producer:
                # Manual same-day candidates must obey the same existing queue.
                existing = pending(store, locales, args.corpus, generation=args.generation)
                if existing:
                    result = existing
                else:
                    # An explicit generation is immutable: never let per-page
                    # receipts silently select a different sub-corpus here.
                    active = []
                    for locale in locales:
                        row = queue(store, locale).get(args.generation, {})
                        if row.get('status') == 'complete':
                            continue
                        pages = read_state(store, 'completed', locale, corpus_day).get('pages', {})
                        if not isinstance(pages, dict):
                            raise R2IntegrityError('Invalid page receipts')
                        if any(not isinstance(pages.get(doc['url']), dict)
                               or pages[doc['url']].get('content_key') != content_key(doc) for doc in corpus['documents']):
                            active.append(locale)
                    result.update(has_work=bool(active), locales_json=json.dumps(active))
                    if active:
                        register(store, corpus, tuple(active), producer)
        else:
            result = pending(store, locales, args.corpus) if producer else None
            if result is None:
                from portal_extended_daily_queue import read_queue, prepare_queued, read_corpus
                if read_queue(store):
                    result = prepare_queued(store, locales)
                    if result['has_work'] and producer:
                        # Independent admitted locale cursors may use different
                        # immutable corpora. Register each exact group separately.
                        groups = {}
                        for job in json.loads(result['locale_jobs_json']):
                            groups.setdefault(job['generation'], []).append(job['locale'])
                        from portal_extended_continuation import MAX_PENDING_GENERATIONS
                        for generation, selected in groups.items():
                            if any(generation not in queue(store, locale) and len(queue(store, locale)) >= MAX_PENDING_GENERATIONS
                                   for locale in selected):
                                raise ExpansionError('Continuation queue is full; no independent locale was registered')
                        for generation, selected in groups.items():
                            register(store, read_corpus(store, generation), tuple(selected), producer)
                else:
                    with requests.Session() as session:
                        # Transitional/manual runs retain today-only collection.
                        docs = collect_today(session, day)
                    result = prepare(store, docs, locales, day, args.corpus)
                    if result['has_work'] and producer:
                        register(store, json.loads(args.corpus.read_text()),
                                 tuple(json.loads(result['locales_json'])), producer)
        if 'locale_jobs_json' not in result:
            result['locale_jobs_json'] = json.dumps([{'locale': locale, 'generation': result['generation'], 'day': result['day']}
                for locale in json.loads(result['locales_json'])])

        # Retain the admitted source's complete per-locale frontier for upstream
        # progress-driven followup, including diagnosed (never inferred) cursors.
        if not result.get('source_admission') and result.get('generation'):
            origin = read_origin(store, result['generation'])
            if origin and origin.get('source_admission'):
                result['source_admission'] = origin['source_admission']
        if result.get('source_admission'):
            from portal_extended_daily_queue import read_admission, read_corpus, pending_docs
            admitted = read_admission(store, result['source_admission'])
            full = read_corpus(store, admitted['generation'])
            result['pending_counts_json'] = json.dumps({locale: len(pending_docs(store, full['documents'], locale, admitted['day']))
                                                       for locale in requested_locales})
        result['stopped_locales_json'] = json.dumps(stopped)
        if args.include_english:
            result = include_english_matrix(store, result)
        if args.github_output:
            with args.github_output.open('a') as stream:
                for key in ('has_work', 'generation', 'locales_json', 'locale_jobs_json', 'day', 'stopped_locales_json'):
                    value = str(result[key]).lower() if isinstance(result[key], bool) else result[key]
                    stream.write(f'{key}={value}\n')
                stream.write('requested_locales='+','.join(requested_locales)+'\n')
                for key in ('source_admission', 'pending_counts_json', 'english_admission', 'english_pending_count'):
                    stream.write(key + '=' + result.get(key, '') + '\n')

    else:
        if select_locales(args.locale) != (args.locale,): raise ExpansionError('Expected one locale')
        if args.operation != 'restore-seed':
            from portal_extended_continuation import read_origin
            if read_origin(store, args.generation) and not (
                os.environ.get('GITHUB_ACTIONS') == 'true' and os.environ.get('GITHUB_REF') == 'refs/heads/main'
            ):
                raise ExpansionError('Registered generation continuation requires reviewed main Actions')
        if args.operation == 'restore-seed': result = restore_seed(store, args.locale, args.checkpoint)
        elif args.operation == 'restore-checkpoint':
            from portal_extended_continuation import restore_claimed_checkpoint
            result = restore_claimed_checkpoint(store, args.locale, args.generation, args.checkpoint)
        elif args.operation == 'checkpoint': result = remember_checkpoint(store, args.locale, args.generation, args.checkpoint)
        else:
            corpus = json.loads(args.corpus.read_text())
            if corpus.get('documents_sha256') != args.generation: raise ExpansionError('Candidate source generation mismatch')
            result = remember_candidate(store, args.locale, corpus, args.directory)
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
