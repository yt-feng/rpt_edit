"""Hand complete daily R2 candidates to the existing protected release workflow.

This does not approve, activate, translate, or discover historical pages. Only
explicitly enabled locales already present in the verified active ledger can
be handed off. The ordinary exact-version approval and rollback still apply.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

import requests

from assemble_portal_extended_locales import verified_candidate
from check_portal_extended_publication import completed_candidates
from portal_extended_incremental import content_key, read_state
from portal_extended_locales import (ORIGIN, ExpansionError, daily_corpus_day,
                                     digest, publication_day, select_locales, stable_bytes, validate_corpus)
from portal_extended_publication import checked_batches, read_active_batches
from portal_extended_r2 import DEFAULT_PREFIX, HEX64, R2NotFound, R2Store, safe_part


def pending_batch(store, corpus, requested, enabled, active_batches, workspace):
    docs = validate_corpus(corpus)
    day = daily_corpus_day(corpus)
    if not day or not 1 <= len(docs) <= 24:
        raise ExpansionError('Handoff requires a bounded daily detail batch')
    requested = select_locales(requested)
    enabled = set(select_locales(enabled)) if enabled else set()
    active = checked_batches(active_batches)
    live = {locale for batch in active for locale in batch['candidates']}
    existing = {(locale, batch['generation'], candidate)
                for batch in active for locale, candidate in batch['candidates'].items()}
    selected = {}
    for locale in requested:
        if locale not in enabled or locale not in live:
            continue
        rows = read_state(store, 'completed', locale, day).get('pages', {})
        if not isinstance(rows, dict):
            raise ExpansionError('Invalid completed page receipts')
        # Missing/older receipts mean this locale is still incomplete. Storage
        # permissions, corrupt candidates and mismatched IDs remain hard errors.
        if any(not isinstance(rows.get(doc['url']), dict)
               or rows[doc['url']].get('generation') != corpus['documents_sha256']
               or rows[doc['url']].get('content_key') != content_key(doc) for doc in docs):
            continue
        batch = completed_candidates(store, corpus, (locale,))
        candidate = batch['candidates'][locale]
        if (locale, batch['generation'], candidate) in existing:
            continue
        directory = workspace/locale
        store.restore_candidate(locale, batch['generation'], candidate, directory)
        verified_candidate(directory, corpus)
        selected[locale] = candidate
    return {'generation': corpus['documents_sha256'], 'candidates': selected}


def save_handoff(store, batch, *, day, pages, producer):
    checked_batches([batch])
    if not re.fullmatch(r'[0-9a-f]{40}', producer['sha']):
        raise ExpansionError('Invalid producer commit')
    if any(not re.fullmatch(r'[1-9][0-9]*', str(producer[key])) for key in ('run_id', 'attempt')):
        raise ExpansionError('Invalid producer run identity')
    if type(pages) is not int or not 1 <= pages <= 24 or publication_day(day) != day:
        raise ExpansionError('Invalid handoff page count')
    value = {'schema_version': 1, 'producer': producer, 'source_day': day,
             'pages_per_locale': pages, 'batch': batch, 'paid_provider_requests': 0}
    from portal_extended_daily_queue import batch_admission
    admitted = batch_admission(store, batch['generation'])
    if admitted is not None:
        if admitted['day'] != day:
            raise ExpansionError('Handoff source admission day differs')
        value['source_admission'] = admitted['admission']
    raw = stable_bytes(value)
    identity = digest(raw)
    key = store.key('publication-handoffs', identity, 'receipt.json')
    try:
        existing = store._get(key, maximum=65536)
    except R2NotFound:
        store._put(key, raw, metadata={'kind': 'publication-handoff'})
        existing = store._get(key, maximum=65536)
    if existing != raw:
        raise ExpansionError('Immutable handoff receipt differs')
    return identity


def read_handoff(store, identity):
    safe_part(identity, label='handoff identity', pattern=HEX64)
    raw = store._get(store.key('publication-handoffs', identity, 'receipt.json'), maximum=65536)
    if digest(raw) != identity:
        raise ExpansionError('Handoff receipt checksum differs')
    value = json.loads(raw)
    if value.get('schema_version') != 1 or value.get('paid_provider_requests') != 0:
        raise ExpansionError('Invalid handoff receipt provenance')
    checked_batches([value['batch']])
    return value


def verify_handoff(store, identity, generation, candidates):
    value = read_handoff(store, identity)
    if value['batch'] != {'generation': generation, 'candidates': candidates}:
        raise ExpansionError('Release inputs do not match the immutable handoff')
    return value


def next_ready_batch(store, day, requested, enabled, active, workspace):
    """Drain today's durable completed receipts even after inference is a no-op.

    A failed/partial matrix or head-only refresh must not orphan a locale that
    finished earlier under another exact source generation. Select one bounded
    immutable generation; subsequent normal refreshes drain the next one.
    """
    require_day = publication_day(day)
    if not require_day or require_day != day:
        raise ExpansionError('Invalid daily handoff date')
    requested = select_locales(requested)
    enabled = set(select_locales(enabled)) if enabled else set()
    active = checked_batches(active)
    live = {locale for row in active for locale in row['candidates']}
    published = {(locale,row['generation'],candidate) for row in active
                 for locale,candidate in row['candidates'].items()}
    groups = {}
    for locale in requested:
        if locale not in enabled & live:
            continue
        rows = read_state(store, 'completed', locale, day).get('pages', {})
        if not isinstance(rows, dict):
            raise ExpansionError('Invalid completed page receipts')
        for row in rows.values():
            if not isinstance(row, dict):
                raise ExpansionError('Invalid completed page receipt')
            generation = safe_part(row.get('generation'), label='completed generation', pattern=HEX64)
            candidate = safe_part(row.get('candidate_id'), label='completed candidate', pattern=HEX64)
            if (locale, generation, candidate) not in published:
                groups.setdefault(generation, set()).add(locale)
    if len(groups) > 500:
        raise ExpansionError('Daily handoff generation inventory exceeds bound')
    for generation, locales in sorted(groups.items()):
        path = workspace/(generation+'.json')
        store.restore_source(generation, path)
        corpus = json.loads(path.read_text())
        if daily_corpus_day(corpus) != day:
            raise ExpansionError('Completed receipt points outside the selected source day')
        batch = pending_batch(store, corpus, ','.join(sorted(locales)), ','.join(sorted(enabled)),
                              active, workspace/generation)
        if batch['candidates']:
            return batch, corpus
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--generation', default='')
    parser.add_argument('--day', required=True)
    parser.add_argument('--locales', required=True)
    parser.add_argument('--enabled-locales', required=True)
    args = parser.parse_args()
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REF') != 'refs/heads/main':
        raise ExpansionError('Automatic handoff runs only on reviewed main in Actions')
    store = R2Store.from_env(DEFAULT_PREFIX)
    with tempfile.TemporaryDirectory(prefix='extended-handoff-') as temporary:
        workspace = Path(temporary)
        if args.generation:
            store.restore_source(args.generation, workspace/'source.json')
            corpus = json.loads((workspace/'source.json').read_text())
            if daily_corpus_day(corpus) != args.day:
                raise ExpansionError('Source day changed after daily selection')
        # Respect the environment's normal networking; never alter proxy state.
        with requests.Session() as session:
            response = session.get(ORIGIN+'/.well-known/edge-state', timeout=(10, 30), allow_redirects=False)
            response.raise_for_status()
            if len(response.content) > 65536:
                raise ExpansionError('Active release identity exceeds bound')
            active = read_active_batches(store, response.json())
        ready = next_ready_batch(store, args.day, args.locales, args.enabled_locales, active, workspace)
        if ready is None:
            print(json.dumps({'dispatched': False, 'reason': 'No new complete already-approved locale candidates'}))
            return
        batch, corpus = ready
        receipt = save_handoff(store, batch, day=args.day, pages=len(corpus['documents']), producer={
            'run_id': os.environ['GITHUB_RUN_ID'], 'attempt': os.environ['GITHUB_RUN_ATTEMPT'],
            'sha': os.environ['GITHUB_SHA']})
        subprocess.run(['gh', 'workflow', 'run', 'neutral-edge-cutover.yml', '--repo', os.environ['GITHUB_REPOSITORY'],
            '--ref', 'main', '-f', 'operation=migrate', '-f', 'translation_scope=incremental',
            '-f', 'extended_locales='+','.join(batch['candidates']), '-f', 'extended_source_generation='+batch['generation'],
            '-f', 'extended_candidate_ids='+','.join(k+'='+v for k, v in batch['candidates'].items()),
            '-f', 'extended_handoff='+receipt], check=True)
        print(json.dumps({'dispatched': True, 'handoff': receipt, 'locales': list(batch['candidates']),
                          'pages_per_locale': len(corpus['documents']), 'approved': False, 'deployed': False}))


if __name__ == '__main__':
    main()
