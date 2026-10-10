"""Freeze new source days before CPU queues; independent <=24-page locale cursors.

Only the fast admission workflow writes the queue. Consumers never mutate it;
their existing per-locale completed receipts advance each deterministic cursor.
Older work may resume only from a previously admitted, immutable R2 inventory,
never by discovering/scraping historical URLs.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import tempfile
import time
from urllib.parse import urlsplit

import requests

from portal_extended_incremental import collect_today, content_key, read_state, today
from portal_extended_locales import (ADDITIONAL, DAILY_SCOPE, ExpansionError, daily_corpus_day,
                                     INCREMENTAL_START, digest, make_corpus, publication_day, select_locales,
                                     stable_bytes, validate_corpus)
from portal_extended_r2 import (DEFAULT_PREFIX, HEX64, MAX_SOURCE_BYTES,
                               R2IntegrityError, R2NotFound, R2Store, R2StoreError, require_staging_prefix, safe_part)

POLICY = 'daily-source-admission-v1'
WORKFLOW = '.github/workflows/portal-extended-locales-source.yml'
MAX_DAYS = 32
MAX_RECORD_BYTES = 65536


def checked_producer(value):
    if (not isinstance(value, dict) or set(value) != {'run_id', 'attempt', 'sha', 'repository', 'workflow'}
        or value['workflow'] != WORKFLOW or not re.fullmatch(r'[0-9a-f]{40}', value['sha'])
        or not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', value['repository'])
        or any(not re.fullmatch(r'[1-9][0-9]*', str(value[key])) for key in ('run_id', 'attempt'))):
        raise ExpansionError('Invalid source-admission producer')
    return value


def queue_key(store):
    return store.key('incremental', 'admitted-source-days', 'queue.json')


def checked_entry(value):
    if not isinstance(value, dict) or set(value) != {'day', 'admission'} or publication_day(value['day']) != value['day']:
        raise R2IntegrityError('Invalid source-day queue entry')
    safe_part(value['admission'], label='source admission', pattern=HEX64)
    return value


def read_queue(store):
    try:
        value = json.loads(store._get(queue_key(store), maximum=MAX_RECORD_BYTES))
    except R2NotFound:
        return []
    if (not isinstance(value, dict) or set(value) != {'schema_version', 'policy', 'entries'}
        or value['schema_version'] != 1 or value['policy'] != POLICY
        or not isinstance(value['entries'], list) or len(value['entries']) > MAX_DAYS):
        raise R2IntegrityError('Invalid source-day queue identity')
    entries = [checked_entry(entry) for entry in value['entries']]
    if len({entry['day'] for entry in entries}) != len(entries):
        raise R2IntegrityError('Duplicate admitted source day')
    return entries


def all_queued(store):
    """Read both admission routes; only the fast source job writes either one."""
    from portal_extended_recovered_admission import read_queue as recovered_queue
    entries = read_queue(store) + recovered_queue(store)
    if len({entry['admission'] for entry in entries}) != len(entries):
        raise R2IntegrityError('Duplicate source admission across queues')
    return entries


def write_verified(store, key, value, *, kind):
    raw = stable_bytes(value)
    if len(raw) > MAX_RECORD_BYTES:
        raise R2IntegrityError('Source-admission record exceeds bound')
    store._put(key, raw, metadata={'kind': kind})
    if store._get(key, maximum=MAX_RECORD_BYTES) != raw:
        raise R2IntegrityError('Source-admission readback differs')


def immutable_record(store, key, value, *, kind):
    raw = stable_bytes(value)
    try:
        existing = store._get(key, maximum=MAX_RECORD_BYTES)
    except R2NotFound:
        write_verified(store, key, value, kind=kind)
        return
    if existing != raw:
        raise R2IntegrityError('Immutable admission record differs')


def read_admission(store, identity):
    safe_part(identity, label='source admission', pattern=HEX64)
    raw = store._get(store.key('source-admissions', identity, 'receipt.json'), maximum=MAX_RECORD_BYTES)
    if digest(raw) != identity:
        raise R2IntegrityError('Source-admission checksum differs')
    value = json.loads(raw)
    if isinstance(value, dict) and value.get('schema_version') == 3:
        from portal_extended_recovered_admission import POLICY as RECOVERED_POLICY, read_proof as recovered_proof
        if (set(value) != {'schema_version', 'policy', 'scope', 'day', 'generation', 'pages',
                          'producer', 'capture_day', 'recovery'}
            or value['policy'] != RECOVERED_POLICY or value['scope'] != DAILY_SCOPE
            or publication_day(value['day']) != value['day'] or type(value['pages']) is not int
            or not 1 <= value['pages'] <= 500):
            raise R2IntegrityError('Invalid recovered source-admission scope')
        checked_producer(value['producer'])
        corpus = read_corpus(store, value['generation'])
        proof = recovered_proof(store, value['recovery'], corpus)
        if (proof['day'] != value['day'] or proof['capture_day'] != value['capture_day']
            or len(corpus['documents']) != value['pages']):
            raise R2IntegrityError('Recovered source admission differs from proof')
        return value
    from portal_extended_source_refresh import POLICY as REFRESH_POLICY, read_proof
    base = {'schema_version', 'policy', 'scope', 'day', 'generation', 'pages', 'producer'}
    modern = isinstance(value, dict) and value.get('schema_version') == 2
    if (not isinstance(value, dict) or set(value) != (base | {'capture_day', 'refresh'} if modern else base)
        or value['schema_version'] != (2 if modern else 1)
        or value['policy'] != (REFRESH_POLICY if modern else POLICY) or value['scope'] != DAILY_SCOPE
        or publication_day(value['day']) != value['day'] or type(value['pages']) is not int or not 1 <= value['pages'] <= 500):
        raise R2IntegrityError('Invalid source-admission scope')
    safe_part(value['generation'], label='inventory generation', pattern=HEX64)
    checked_producer(value['producer'])
    if modern:
        proof = read_proof(store, value['refresh'], read_corpus(store, value['generation']))
        if proof['day'] != value['day'] or proof['capture_day'] != value['capture_day']:
            raise R2IntegrityError('Source refresh capture date differs from admission')
    return value


def read_corpus(store, generation):
    safe_part(generation, label='source generation', pattern=HEX64)
    corpus = json.loads(store._get(store.source_key(generation), maximum=MAX_SOURCE_BYTES))
    validate_corpus(corpus)
    if corpus['documents_sha256'] != generation:
        raise R2IntegrityError('Admitted source generation differs')
    return corpus


def inventory(store, entry):
    admission = read_admission(store, entry['admission'])
    corpus = read_corpus(store, admission['generation'])
    if (admission['day'] != entry['day'] or daily_corpus_day(corpus) != admission['day']
        or len(corpus['documents']) != admission['pages']):
        raise R2IntegrityError('Admitted inventory scope differs')
    return admission, corpus


def pending_docs(store, docs, locale, day):
    rows = read_state(store, 'completed', locale, day).get('pages', {})
    if not isinstance(rows, dict):
        raise R2IntegrityError('Invalid locale completed receipts')
    for row in rows.values():
        if not isinstance(row, dict) or any(not isinstance(row.get(key), str) or not HEX64.fullmatch(row[key])
            for key in ('content_key', 'generation', 'candidate_id')):
            raise R2IntegrityError('Malformed locale completed receipt')
    return [doc for doc in sorted(docs, key=lambda value: value['url'])
            if not isinstance(rows.get(doc['url']), dict)
            or rows[doc['url']].get('content_key') != content_key(doc)]


def admit(store, docs, day, producer, *, refresh=None):
    checked_producer(producer)
    if publication_day(day) != day or day < INCREMENTAL_START:
        raise ExpansionError('Invalid admission day')
    if not docs:
        return {'admitted': False, 'day': day, 'pages': 0}
    corpus = make_corpus(sorted(docs, key=lambda doc: doc['url']))
    if daily_corpus_day(corpus) != day:
        raise ExpansionError('Admission accepts only new pages from its own source day')
    entries = read_queue(store)
    if refresh is not None and entries and day < max(entry['day'] for entry in entries):
        raise ExpansionError('Newest source day moved backwards; no historical batch was admitted')
    retained = []
    for entry in entries:
        if entry['day'] == day:
            continue
        _, previous = inventory(store, entry)
        if any(pending_docs(store, previous['documents'], locale, entry['day']) for locale in ADDITIONAL):
            retained.append(entry)
    if len(retained) >= MAX_DAYS:
        raise ExpansionError('Unfinished admitted days exceed queue bound; nothing was discarded')
    store.put_source(corpus)
    receipt = {'schema_version': 1, 'policy': POLICY, 'scope': DAILY_SCOPE, 'day': day,
               'generation': corpus['documents_sha256'], 'pages': len(docs), 'producer': producer}
    if refresh is not None:
        from portal_extended_source_refresh import POLICY as REFRESH_POLICY, save_proof
        receipt.update(schema_version=2, policy=REFRESH_POLICY, capture_day=refresh['capture_day'],
                       refresh=save_proof(store, refresh, corpus))
    identity = digest(stable_bytes(receipt))
    immutable_record(store, store.key('source-admissions', identity, 'receipt.json'), receipt, kind='source-admission')
    # Last pointer only after the complete immutable corpus and admission verify.
    retained.append({'day': day, 'admission': identity})
    write_verified(store, queue_key(store), {'schema_version': 1, 'policy': POLICY,
                   'entries': sorted(retained, key=lambda entry: entry['day'])}, kind='source-day-queue')
    return {'admitted': True, 'day': day, 'pages': len(docs), 'admission': identity,
            'generation': corpus['documents_sha256'], 'queued_days': len(retained), 'paid_provider_requests': 0}


def batch_admission(store, generation):
    safe_part(generation, label='batch generation', pattern=HEX64)
    try:
        value = json.loads(store._get(store.key('batch-admissions', generation, 'receipt.json'), maximum=MAX_RECORD_BYTES))
    except R2NotFound:
        return None
    if not isinstance(value, dict) or set(value) != {'schema_version', 'policy', 'generation', 'admission'}:
        raise R2IntegrityError('Invalid batch admission')
    if value['schema_version'] != 1 or value['policy'] != POLICY or value['generation'] != generation:
        raise R2IntegrityError('Batch admission identity differs')
    admitted = read_admission(store, value['admission'])
    full = read_corpus(store, admitted['generation'])
    batch = read_corpus(store, generation)
    originals = {doc['url']: doc for doc in full['documents']}
    if (daily_corpus_day(full) != admitted['day'] or len(full['documents']) != admitted['pages']
        or daily_corpus_day(batch) != admitted['day'] or not 1 <= len(batch['documents']) <= 24
        or any(originals.get(doc['url']) != doc for doc in batch['documents'])):
        raise R2IntegrityError('Batch does not match its immutable admitted inventory')
    return {**admitted, 'admission': value['admission']}


def prepare_queued(store, locales, *, limit=24):
    locales = select_locales(','.join(locales))
    if type(limit) is not int or not 1 <= limit <= 24:
        raise ExpansionError('Locale cursor must retain the 1..24-page bound')
    entries = sorted(all_queued(store), key=lambda value: value['day'], reverse=True)
    # Hot new source days take priority; older items are only previously admitted
    # R2 work, not historical discovery. Each locale advances its own cursor.
    for entry in entries:
        _, full = inventory(store, entry)
        pending = {locale: pending_docs(store, full['documents'], locale, entry['day']) for locale in locales}
        if not any(pending.values()):
            continue
        jobs, counts = [], {}
        for locale, docs in pending.items():
            if not docs:
                continue
            corpus = make_corpus(docs[:limit])
            store.put_source(corpus)
            generation = corpus['documents_sha256']
            # A later head-only refresh can reuse an existing admitted batch.
            # Preserve its first verified provenance instead of overwriting it.
            if batch_admission(store, generation) is None:
                immutable_record(store, store.key('batch-admissions', generation, 'receipt.json'),
                    {'schema_version': 1, 'policy': POLICY, 'generation': generation, 'admission': entry['admission']},
                    kind='batch-admission')
            # The serialized source job is the only queue writer. Concurrent
            # locale workers only persist their own ready/completion receipts.
            from portal_extended_handoff import queue_publication_batch
            queue_publication_batch(store, generation, entry['day'])
            jobs.append({'locale': locale, 'generation': generation, 'day': entry['day']})
            counts[locale] = {'selected': min(limit, len(docs)), 'remaining': max(0, len(docs)-limit)}
        generations = {job['generation'] for job in jobs}
        return {'has_work': True, 'day': entry['day'], 'generation': next(iter(generations)) if len(generations) == 1 else '',
                'locale_jobs_json': json.dumps(jobs), 'locales_json': json.dumps([job['locale'] for job in jobs]),
                'pending_locale_count': len(jobs), 'per_locale_counts': counts,
                'source_admission': entry['admission'],
                'pending_counts_json': json.dumps({locale: len(docs) for locale, docs in pending.items()}),
                'remaining_page_count': max(row['remaining'] for row in counts.values()), 'paid_provider_requests': 0}
    return {'has_work': False, 'day': entries[0]['day'] if entries else today(), 'generation': '',
            'locale_jobs_json': '[]', 'locales_json': '[]', 'pending_locale_count': 0,
            'per_locale_counts': {}, 'remaining_page_count': 0, 'paid_provider_requests': 0}


def followup_needed(store, identity, locales, before):
    locales = select_locales(','.join(locales))
    admitted = read_admission(store, identity)
    corpus = read_corpus(store, admitted['generation'])
    if daily_corpus_day(corpus) != admitted['day'] or len(corpus['documents']) != admitted['pages']:
        raise R2IntegrityError('Continuation inventory differs')
    if (not isinstance(before, dict) or set(before) != set(locales)
        or any(type(count) is not int or not 0 <= count <= admitted['pages'] for count in before.values())):
        raise ExpansionError('Invalid continuation frontier')
    after = {locale: len(pending_docs(store, corpus['documents'], locale, admitted['day'])) for locale in locales}
    progress = any(after[locale] < before[locale] for locale in locales)
    # A failed language cannot prevent other cursors advancing; no-progress
    # failures never self-dispatch forever. A normal new source event can retry.
    remaining = any(after.values())
    if progress and not remaining:
        for entry in all_queued(store):
            if entry['admission'] == identity:
                continue
            _, queued = inventory(store, entry)
            if any(pending_docs(store, queued['documents'], locale, entry['day']) for locale in locales):
                remaining = True
                break
    if progress and not remaining:
        # A completed ordinary turn hands the next serialized slot back to old
        # quality debt. Its planner still filters terminal/unknown units and only
        # accepted repair progress may continue after that one bounded scan.
        from portal_extended_quality import debt_rows
        remaining = any(debt_rows(store, locale) for locale in locales)
    return {'continue': progress and remaining, 'progress': progress,
            'pending_counts': after, 'paid_provider_requests': 0}


def staging_probe(store):
    """Real private storage I/O with synthetic data and zero model calls."""
    from build_portal_extended_locales import Memo
    from datetime import date, timedelta
    from portal_extended_locales import ORIGIN, document_from_html
    from portal_extended_source_refresh import POLICY as REFRESH_POLICY
    require_staging_prefix(store.prefix)
    capture_day = today()
    day = max(INCREMENTAL_START, (date.fromisoformat(capture_day) - timedelta(days=1)).isoformat())
    url = ORIGIN + '/blog/' + day.replace('-', '') + '-0000000000000001.html'
    schema = json.dumps({'@type': 'BlogPosting', 'url': url, 'datePublished': day, 'dateModified': day})
    body = ('<html lang="zh-Hans"><head><link rel="canonical" href="' + url
        + '"><script type="application/ld+json">' + schema + '</script></head>'
        + '<main><h1>Isolated synthetic queue test</h1><p>Not production content.</p></main></html>').encode()
    doc = document_from_html(url, body)
    doc.update(selection_scope=DAILY_SCOPE, selection_day=day)
    doc['content_sha256'] = digest(stable_bytes({key: value for key, value in doc.items() if key != 'content_sha256'}))
    refresh = {'schema_version': 1, 'policy': REFRESH_POLICY, 'capture_day': capture_day, 'day': day,
               'release': {'slot': 'a', 'release_id': '0'*32, 'tree_sha256': '0'*64},
               'inventory': {url: day}}
    admitted = admit(store, [doc], day, {'run_id':'1','attempt':'1','sha':'0'*40,
                                     'repository':'synthetic/staging','workflow':WORKFLOW}, refresh=refresh)
    if read_admission(store, admitted['admission'])['capture_day'] != capture_day:
        raise R2IntegrityError('Staging source-refresh capture proof differs')
    prepared = prepare_queued(store, ('fr', 'pt'))
    generation = prepared['generation']
    if batch_admission(store, generation)['admission'] != admitted['admission']:
        raise R2IntegrityError('Staging batch admission differs')
    with tempfile.TemporaryDirectory(prefix='source-queue-staging-') as temporary:
        checkpoint = Path(temporary)/'checkpoint.json'
        # An empty checkpoint is honest: no production translations are invented.
        memo = Memo(checkpoint, 'fr', None, time.monotonic(), source_generation=generation)
        memo.save()
        written = store.put_checkpoint('fr', generation, checkpoint)
        restored = store.restore_checkpoint('fr', generation, Path(temporary)/'restored.json')
        if not restored['present'] or written['sha256'] != restored['sha256']:
            raise R2IntegrityError('Staging checkpoint restore differs')
        restored_corpus = Path(temporary)/'corpus.json'
        store.restore_source(generation, restored_corpus)
        if json.loads(restored_corpus.read_text()) != make_corpus([doc]):
            raise R2IntegrityError('Staging source restore differs')
    # Cursor-only synthetic receipt; no ready candidate exists, so the ordinary
    # handoff would refuse this unserved staging fixture even if mis-selected.
    write = {'pages': {url: {'content_key': content_key(doc), 'generation': generation, 'candidate_id': '0'*64}}}
    from portal_extended_incremental import write_state
    write_state(store, 'completed', 'fr', write, day)
    resumed = prepare_queued(store, ('fr', 'pt'))
    if json.loads(resumed['locales_json']) != ['pt']:
        raise R2IntegrityError('Staging independent cursor restore differs')
    return {'staging_only': True, 'source_restore': 'passed', 'checkpoint_restore': 'passed',
            'source_refresh_proof_restore': 'passed', 'capture_day': capture_day, 'source_day': day,
            'batch_admission': 'passed', 'independent_cursor_simulation': 'passed',
            'source_generation': generation, 'checkpoint_sha256': written['sha256'],
            'ready_candidates': 0, 'translation_calls': 0, 'deployed': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prefix', default=DEFAULT_PREFIX)
    parser.add_argument('--operation', choices=['admit', 'followup', 'staging-probe'], default='admit')
    parser.add_argument('--admission')
    parser.add_argument('--locales', default='all-supported')
    parser.add_argument('--before')
    parser.add_argument('--github-output', type=Path)
    parser.add_argument('--recovered-publication-run', default='')
    args = parser.parse_args()
    if args.operation == 'staging-probe':
        if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('KC_PUBLIC_REPOSITORY') != 'true':
            raise ExpansionError('Staging storage probe requires public Actions')
        require_staging_prefix(args.prefix)
        print(json.dumps(staging_probe(R2Store.from_env(args.prefix)), sort_keys=True))
        return
    if (os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REF') != 'refs/heads/main'
        or os.environ.get('KC_PUBLIC_REPOSITORY') != 'true'):
        raise ExpansionError('Source admission requires reviewed main on public Actions')
    store = R2Store.from_env(args.prefix)
    if args.operation == 'followup':
        result = followup_needed(store, args.admission, select_locales(args.locales), json.loads(args.before))
        if args.github_output:
            with args.github_output.open('a') as stream:
                stream.write('continue=' + str(result['continue']).lower() + '\n')
        print(json.dumps(result, sort_keys=True))
        return
    producer = {'run_id': os.environ['GITHUB_RUN_ID'], 'attempt': os.environ['GITHUB_RUN_ATTEMPT'],
                'sha': os.environ['GITHUB_SHA'], 'repository': os.environ['GITHUB_REPOSITORY'], 'workflow': WORKFLOW}
    capture_day = today()
    if args.recovered_publication_run:
        from portal_extended_recovered_admission import GitHub, authenticate, collect, admit as admit_recovered
        publication = authenticate(GitHub(os.environ['GITHUB_REPOSITORY']), args.recovered_publication_run)
        if publication is None:
            print(json.dumps({'admitted': False, 'pages': 0, 'paid_provider_requests': 0,
                              'reason': 'no-published-articles'}, sort_keys=True))
            return
        with requests.Session() as session:
            corpus, proof = collect(session, publication, capture_day)
        result = admit_recovered(store, corpus, proof, producer)
        result.update(capture_day=capture_day, selection_policy=proof['policy'],
                      source_release=proof['release']['release_id'])
        print(json.dumps(result, sort_keys=True))
        return
    # Read each current public page only once. English gets an explicit editorial
    # projection of those SAME bytes, never the generic translated report body.
    from portal_english_commentary import PREFIX as ENGLISH_PREFIX, extract_editorial, freeze_editorial
    english_docs, english_skipped = [], []
    def editorial_sink(doc, raw):
        if not re.fullmatch(r'/blog/\d{8}-[a-f0-9]{16}\.html', urlsplit(doc['url']).path):
            return
        try:
            editorial = extract_editorial(doc['url'], raw, publication_day(doc['datePublished']))
        except (ExpansionError, UnicodeError, ValueError, TypeError):
            english_skipped.append('unsafe-editorial-source')
            return
        if editorial is not None:
            english_docs.append(editorial)
        else:
            english_skipped.append('no-explicit-kc-comment')
    with requests.Session() as session:
        from portal_extended_source_refresh import collect_refresh
        day, docs, refresh = collect_refresh(session, capture_day, on_source=editorial_sink)
    result = admit(store, docs, day or capture_day, producer, refresh=refresh if docs else None)
    result.update(capture_day=capture_day, source_day=day,
                  selection_policy=refresh['policy'], source_release=refresh['release']['release_id'])
    if result['admitted']:
        # A custom staging namespace never causes writes to production English.
        prefix = ENGLISH_PREFIX if args.prefix == DEFAULT_PREFIX else store.prefix + '/english-commentary'
        try:
            result['english_editorial'] = freeze_editorial(R2Store(store.client, store.bucket, prefix),
                                                          english_docs, day, producer, result['admission'])
        except (ExpansionError, R2StoreError):
            # Do not stall all 33 non-English consumers for an English-only
            # persistence failure. No English receipt is claimed complete.
            result['english_editorial'] = {'admitted': False, 'capture_incomplete': True, 'day': day,
                                          'code': 'english-private-capture-failed'}
        result['english_editorial']['excluded_page_count'] = len(english_skipped)
        result['english_editorial']['exclusion_codes'] = sorted(set(english_skipped))
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
