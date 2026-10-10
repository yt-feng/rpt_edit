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
from portal_extended_quality import publication_ready


def read_publication_batches(store):
    """Publication work survives source-day cursor pruning and runner midnight."""
    key = store.key('incremental', 'pending-publications', 'queue.json')
    try:
        value = json.loads(store._get(key, maximum=128 * 1024))
    except R2NotFound:
        return []
    if (not isinstance(value, dict) or set(value) != {'schema_version', 'entries'}
            or value['schema_version'] != 1 or not isinstance(value['entries'], list)
            or len(value['entries']) > 500):
        raise ExpansionError('Invalid pending locale publication queue')
    seen = set()
    for row in value['entries']:
        if (not isinstance(row, dict) or set(row) != {'day', 'generation'}
                or publication_day(row['day']) != row['day']):
            raise ExpansionError('Invalid pending locale publication day')
        generation = safe_part(row['generation'], label='pending generation', pattern=HEX64)
        if generation in seen:
            raise ExpansionError('Duplicate pending locale generation')
        seen.add(generation)
    return value['entries']


def queue_publication_batch(store, generation, day):
    from portal_extended_daily_queue import batch_admission, write_verified
    # Legacy explicit/manual batches keep their existing publication workflow.
    # Only provenance-verified admitted sources enter automatic cross-day work.
    admitted = batch_admission(store, generation)
    if admitted is None:
        return
    if admitted['day'] != day:
        raise ExpansionError('Pending publication day differs from frozen source')
    entries = read_publication_batches(store)
    row = {'day': day, 'generation': generation}
    if row not in entries:
        if len(entries) >= 500:
            raise ExpansionError('Pending locale publication queue exceeds bound')
        entries.append(row)
        write_verified(store, store.key('incremental', 'pending-publications', 'queue.json'),
                       {'schema_version': 1, 'entries': entries}, kind='pending-locale-publication')


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
        from portal_extended_quality import record_quality
        quality = record_quality(store, locale, batch['generation'], candidate)
        if not publication_ready(quality):
            continue
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
    from portal_extended_quality import record_quality
    qualities = {locale: record_quality(store, locale, batch['generation'], candidate)
                 for locale, candidate in batch['candidates'].items()}
    if not all(publication_ready(proof) for proof in qualities.values()):
        raise ExpansionError('Automatic handoff requires translated-ready or advisory numeric candidates')
    value['translation_quality_proofs'] = {locale: proof['proof_sha256'] for locale, proof in qualities.items()}
    from portal_extended_continuation import checkpoint_evidence, origin_allows_locale, queue, read_origin
    origin = read_origin(store, batch['generation'])
    if origin:
        if origin['source_day'] != day or not all(origin_allows_locale(origin, locale) for locale in batch['candidates']):
            raise ExpansionError('Handoff does not match its registered original source')
        value['source_origin_sha256'] = digest(stable_bytes(origin))
        checkpoints, repairs, completions = {}, {}, {}
        for locale, candidate in batch['candidates'].items():
            row = queue(store, locale).get(batch['generation'], {})
            snapshot = row.get('snapshot', {})
            if row.get('status') != 'complete' or snapshot.get('candidate_id') != candidate:
                raise ExpansionError('Handoff requires an exact complete registered outcome')
            checksum = snapshot.get('checkpoint_sha256')
            if not checkpoint_evidence(store, locale, batch['generation'], checksum):
                raise ExpansionError('Complete handoff lacks its immutable checkpoint')
            checkpoints[locale] = checksum
            if 'source_repair_sha256' in row:
                repairs[locale] = row['source_repair_sha256']
                if 'source_repair_completion_sha256' in row:
                    completions[locale] = row['source_repair_completion_sha256']
        value['continuation_checkpoints'] = checkpoints
        if repairs:
            value['source_repair_proofs'] = repairs
            if completions: value['source_repair_completions'] = completions
            proofs = source_repair_proofs(store, value)
            source_repair_completions(store, value, proofs)
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


def source_repair_proofs(store, receipt):
    if 'source_repair_proofs' not in receipt:
        if 'source_repair_completions' in receipt:
            raise ExpansionError('Source repair completion lacks its base proof')
        return {}
    from portal_extended_french_repair import read_repair_pipeline
    repairs = receipt['source_repair_proofs']
    if (not isinstance(repairs, dict) or not repairs or not receipt.get('source_origin_sha256')
        or not set(repairs) <= set(receipt['batch']['candidates'])
        or not set(repairs) <= set(receipt.get('continuation_checkpoints', {}))):
        raise ExpansionError('Invalid source repair publication evidence')
    proofs = {}
    for locale, identity in repairs.items():
        pipeline = read_repair_pipeline(store, identity)
        if pipeline.locale != locale: raise ExpansionError('Source repair locale differs')
        proof = pipeline.verify_proof(store, identity, receipt['batch']['generation'],
            receipt['batch']['candidates'][locale], receipt['continuation_checkpoints'][locale])
        if not proof['delta']['changed'] or proof['request']['origin_sha256'] != receipt['source_origin_sha256']:
            raise ExpansionError('Source repair did not replace this exact original candidate')
        proofs[locale] = proof
    return proofs


def source_repair_completions(store, receipt, proofs):
    if 'source_repair_completions' not in receipt: return {}
    from portal_extended_french_repair import pipeline_for_proof
    values = receipt['source_repair_completions']
    if not isinstance(values, dict) or not values or not set(values) <= set(proofs):
        raise ExpansionError('Invalid prepared resumption inventory')
    return {locale: pipeline_for_proof(proofs[locale]).verify_completion(store, identity,
        proofs[locale], receipt['source_repair_proofs'][locale]) for locale, identity in values.items()}


def read_handoff(store, identity):
    safe_part(identity, label='handoff identity', pattern=HEX64)
    raw = store._get(store.key('publication-handoffs', identity, 'receipt.json'), maximum=65536)
    if digest(raw) != identity:
        raise ExpansionError('Handoff receipt checksum differs')
    value = json.loads(raw)
    if value.get('schema_version') != 1 or value.get('paid_provider_requests') != 0:
        raise ExpansionError('Invalid handoff receipt provenance')
    checked_batches([value['batch']])
    from portal_extended_quality import handoff_quality
    handoff_quality(store, value)
    proofs = source_repair_proofs(store, value)
    source_repair_completions(store, value, proofs)
    return value


def verify_handoff(store, identity, generation, candidates):
    value = read_handoff(store, identity)
    if value['batch'] != {'generation': generation, 'candidates': candidates}:
        raise ExpansionError('Release inputs do not match the immutable handoff')
    return value


def next_ready_batch(store, day, requested, enabled, active, workspace, *, admitted_only=False):
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
        if admitted_only:
            from portal_extended_daily_queue import batch_admission
            admitted = batch_admission(store, generation)
            if admitted is None:
                continue
            if admitted['day'] != day:
                raise ExpansionError('Pending candidate admission date differs')
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


def next_registered_batch(store, requested, enabled, active, workspace, *, generation=None):
    """Drain only explicitly registered generations, including cross-day results."""
    from portal_extended_continuation import acknowledge_published, queue, tracked_generations
    locales = select_locales(requested)
    active = checked_batches(active)
    acknowledge_published(store, locales, active)
    allowed = set(select_locales(enabled)) if enabled else set()
    live = {locale for row in active for locale in row['candidates']}
    if generation is not None:
        safe_part(generation, label='repair handoff generation', pattern=HEX64)
    for (_day, ready_generation), ready_locales in sorted(tracked_generations(store, locales).items()):
        if generation is not None and ready_generation != generation:
            continue
        selected = sorted(ready_locales & allowed & live)
        if not selected:
            continue
        source = workspace/(ready_generation+'.json')
        store.restore_source(ready_generation, source)
        corpus = json.loads(source.read_bytes())
        candidates = {}
        for locale in selected:
            snapshot = queue(store, locale)[ready_generation]['snapshot']
            directory = workspace/ready_generation/locale
            store.restore_candidate(locale, ready_generation, snapshot['candidate_id'], directory)
            verified_candidate(directory, corpus)
            if digest((directory/'candidate-manifest.json').read_bytes()) != snapshot['manifest_sha256']:
                raise ExpansionError('Completed continuation manifest differs from exact outcome')
            from portal_extended_quality import record_quality
            quality = record_quality(store, locale, ready_generation, snapshot['candidate_id'],
                                     manifest_sha256=snapshot['manifest_sha256'])
            if publication_ready(quality):
                candidates[locale] = snapshot['candidate_id']
        if not candidates:
            continue
        return {'generation': ready_generation, 'candidates': candidates}, corpus
    return None


def next_ready_refresh(store, day, requested, enabled, active, workspace):
    from portal_extended_daily_queue import read_queue
    if publication_day(day) != day:
        raise ExpansionError('Invalid selected publication day')
    # These dates come exclusively from private admitted/ready receipts, never
    # a historical public crawl. Complete but unpublished days stay drainable.
    days = {day} | {entry['day'] for entry in read_queue(store)}
    for row in read_publication_batches(store):
        from portal_extended_daily_queue import batch_admission
        admitted = batch_admission(store, row['generation'])
        if admitted is None or admitted['day'] != row['day']:
            raise ExpansionError('Pending publication lost its source admission')
        days.add(row['day'])
    for selected in sorted(days, reverse=True):
        ready = next_ready_batch(store, selected, requested, enabled, active, workspace/selected,
                                 admitted_only=selected != day)
        if ready is not None:
            return ready
    return None


def repair_handoff_generation(operation, generation, source_has_work, locale_result):
    """A repair can publish only its successful exact registered outcome.

    A validated prepared repair finishes its durable tail in the source job
    without running a locale job. Ordinary daily partial matrices keep their
    existing drain behavior.
    """
    if operation != 'checkpoint-repair':
        return None
    safe_part(generation, label='repair handoff generation', pattern=HEX64)
    if (source_has_work, locale_result) not in {('true', 'success'), ('false', 'skipped')}:
        raise ExpansionError('Failed or unproved checkpoint repair cannot hand off publication')
    return generation


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--generation', default='')
    parser.add_argument('--day', required=True)
    parser.add_argument('--locales', required=True)
    parser.add_argument('--enabled-locales', required=True)
    parser.add_argument('--operation', default='candidate')
    parser.add_argument('--source-has-work', default='')
    parser.add_argument('--locale-result', default='')
    args = parser.parse_args()
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REF') != 'refs/heads/main':
        raise ExpansionError('Automatic handoff runs only on reviewed main in Actions')
    repair_generation = repair_handoff_generation(args.operation, args.generation,
                                                 args.source_has_work, args.locale_result)
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
        ready = next_registered_batch(store, args.locales, args.enabled_locales, active, workspace,
                                      generation=repair_generation)
        if ready is None and repair_generation is None:
            ready = next_ready_refresh(store, args.day, args.locales, args.enabled_locales, active, workspace)
        if ready is None:
            from portal_extended_quality import quality_summary
            print(json.dumps({'dispatched': False, 'reason': 'No new translated-ready already-approved locale candidates',
                              **quality_summary(store, select_locales(args.locales))}))
            return
        batch, corpus = ready
        receipt = save_handoff(store, batch, day=daily_corpus_day(corpus), pages=len(corpus['documents']), producer={
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
