"""Bounded continuation of registered daily generations, never historical discovery.

The production workflow concurrency group serializes source/claim/handoff writes.
Matrix workers only update their own locale ledger. Immutable origins and result
objects survive removal of acknowledged queue entries.
"""
from __future__ import annotations
import json
import os
from pathlib import Path
import re
from portal_extended_locales import (ExpansionError, daily_corpus_day, digest,
    select_locales, stable_bytes, validate_corpus)
from portal_extended_r2 import (HEX64, MAX_CHECKPOINT_BYTES, MAX_CANDIDATE_MANIFEST_BYTES,
    MAX_SOURCE_BYTES, R2NotFound, checkpoint_is_valid, partial_manifest_is_valid)

MAX_PENDING_GENERATIONS = 64
MAX_CONTINUATIONS = 3


def producer_identity(value):
    if (not isinstance(value, dict) or set(value) != {'run_id', 'attempt', 'sha'}
        or not re.fullmatch(r'[0-9a-f]{40}', str(value.get('sha', '')))
        or any(not re.fullmatch(r'[1-9][0-9]*', str(value.get(k, ''))) for k in ('run_id', 'attempt'))):
        raise ExpansionError('Invalid continuation producer identity')
    return {key: str(value[key]) for key in ('run_id', 'attempt', 'sha')}


def action_owner():
    """The source claim is valid for one exact Actions attempt, never a rerun."""
    if os.environ.get('GITHUB_ACTIONS') != 'true':
        return None  # Pure local callers/tests have no Actions identity.
    return producer_identity({'run_id': os.environ.get('GITHUB_RUN_ID'),
        'attempt': os.environ.get('GITHUB_RUN_ATTEMPT'), 'sha': os.environ.get('GITHUB_SHA')})


def require_active_owner(store, locale, generation, *, owner=None):
    row = queue(store, locale).get(generation)
    if row is None:
        return  # Existing unregistered paths are unchanged.
    if row['status'] not in {'started', 'claimed'}:
        raise ExpansionError('Locale retry requires a new source-job claim; refusing unbounded implicit replay')
    expected = producer_identity(row.get('owner'))
    current = producer_identity(owner) if owner is not None else action_owner()
    if current is not None and current != expected:
        raise ExpansionError('Locale retry requires a new source-job claim for this exact Actions attempt')


def origin_key(store, generation):
    if not HEX64.fullmatch(str(generation)):
        raise ExpansionError('Invalid continuation generation')
    return store.key('incremental', 'generation-origins', generation, 'receipt.json')


def read_origin(store, generation):
    try:
        raw = store._get(origin_key(store, generation), maximum=65536)
    except R2NotFound:
        return None
    value = json.loads(raw)
    if (value.get('schema_version') != 1 or value.get('generation') != generation
        or not HEX64.fullmatch(str(value.get('source_sha256', '')))
        or not isinstance(value.get('locales'), list)
        or list(select_locales(','.join(value['locales']))) != value['locales']):
        raise ExpansionError('Invalid generation origin receipt')
    producer_identity(value.get('producer'))
    corpus_raw = store._get(store.source_key(generation), maximum=MAX_SOURCE_BYTES)
    corpus = json.loads(corpus_raw)
    docs = validate_corpus(corpus)
    if (digest(corpus_raw) != value['source_sha256'] or corpus['documents_sha256'] != generation
        or daily_corpus_day(corpus) != value.get('source_day') or not daily_corpus_day(corpus)
        or len(docs) != value.get('pages') or not 1 <= len(docs) <= 24):
        raise ExpansionError('Generation origin differs from immutable daily source')
    if value.get('source_admission'):
        from portal_extended_daily_queue import batch_admission
        admitted = batch_admission(store, generation)
        if not admitted or admitted['admission'] != value['source_admission'] or admitted['day'] != value['source_day']:
            raise ExpansionError('Continuation source admission differs from immutable batch')
    return value


def origin_allows_locale(origin, locale):
    # An admitted source is explicitly shared by the 33 independent cursors.
    # Its first consumers are provenance, not a claim that later ones are ready.
    return locale in origin['locales'] or bool(origin.get('source_admission')) and select_locales(locale) == (locale,)


def queue(store, locale):
    from portal_extended_incremental import read_state
    rows = read_state(store, 'continuations', locale).get('generations', {})
    if not isinstance(rows, dict) or len(rows) > MAX_PENDING_GENERATIONS:
        raise ExpansionError('Continuation queue is invalid or exceeds its bound')
    for generation, row in rows.items():
        if (not HEX64.fullmatch(str(generation)) or not isinstance(row, dict)
            or row.get('status') not in {'started', 'claimed', 'incomplete', 'complete', 'blocked'}
            or type(row.get('continuations')) is not int or not 0 <= row['continuations'] <= MAX_CONTINUATIONS):
            raise ExpansionError('Invalid continuation queue entry')
    return rows


def save_queue(store, locale, rows):
    from portal_extended_incremental import write_state
    if len(rows) > MAX_PENDING_GENERATIONS:
        raise ExpansionError('Continuation queue is full; acknowledge published work before selecting more sources')
    write_state(store, 'continuations', locale, {'generations': rows})


def register(store, corpus, locales, producer):
    """Source-job only, before launching a new matrix; no blank checkpoint is made."""
    generation = corpus['documents_sha256']
    docs = validate_corpus(corpus)
    if not daily_corpus_day(corpus) or not 1 <= len(docs) <= 24:
        raise ExpansionError('Only bounded daily sources may be registered')
    locales = select_locales(','.join(locales))
    producer = producer_identity(producer)
    source_raw = store._get(store.source_key(generation), maximum=MAX_SOURCE_BYTES)
    if json.loads(source_raw) != corpus:
        raise ExpansionError('Registered source differs from stored source')
    old = read_origin(store, generation)
    value = {'schema_version': 1, 'generation': generation, 'source_day': daily_corpus_day(corpus),
        'source_sha256': digest(source_raw), 'pages': len(docs), 'locales': list(locales), 'producer': producer}
    from portal_extended_daily_queue import batch_admission
    admitted = batch_admission(store, generation)
    if admitted is not None:
        value['source_admission'] = admitted['admission']
    if old:
        if not all(origin_allows_locale(old, locale) for locale in locales):
            raise ExpansionError('Cannot extend a previously registered generation locale inventory')
        value = old
    # Validate all queue capacity before the first write; never evict an old job.
    queues = {locale: queue(store, locale) for locale in locales}
    if any(generation not in rows and len(rows) >= MAX_PENDING_GENERATIONS for rows in queues.values()):
        raise ExpansionError('Continuation queue is full; no historical work was dropped')
    if not old:
        raw = stable_bytes(value)
        store._put(origin_key(store, generation), raw, metadata={'kind': 'generation-origin'})
        if store._get(origin_key(store, generation), maximum=65536) != raw:
            raise ExpansionError('Generation origin did not persist')
    for locale, rows in queues.items():
        if generation not in rows:
            rows[generation] = {'status': 'started', 'continuations': 0, 'owner': producer}
            save_queue(store, locale, rows)
    return value


def checkpoint_evidence(store, locale, generation, checksum):
    if not HEX64.fullmatch(str(checksum)):
        raise ExpansionError('Invalid continuation checkpoint checksum')
    raw = store._get(store.checkpoint_object_key(locale, generation, checksum), maximum=MAX_CHECKPOINT_BYTES)
    if digest(raw) != checksum:
        raise ExpansionError('Continuation checkpoint checksum mismatch')
    value = json.loads(raw)
    checkpoint_is_valid(value, locale, generation)
    if value.get('source_generation') != generation or not isinstance(value.get('source_fallbacks', {}), dict):
        raise ExpansionError('Continuation checkpoint must explicitly bind the source generation')
    from build_portal_extended_locales import CHECKPOINT_VERSION, SOURCE_FALLBACK_VERSION, validate_text
    from offline_translation import MODEL_ID
    for kind in ('rows', 'source_fallbacks'):
        for key, row in value.get(kind, {}).items():
            if not isinstance(row, dict) or not isinstance(row.get('source'), str) or not isinstance(row.get('language'), str):
                raise ExpansionError('Invalid persisted checkpoint unit')
            parts = [CHECKPOINT_VERSION, MODEL_ID, locale, row['language'], row['source']]
            if key not in {digest(stable_bytes(parts)), digest(stable_bytes(parts+['markdown']))}:
                raise ExpansionError('Checkpoint unit key differs from its exact source')
            if kind == 'rows':
                validate_text(row['source'], row.get('text'), locale, row['language'])
            elif row.get('policy') != SOURCE_FALLBACK_VERSION or not isinstance(row.get('code'), str):
                raise ExpansionError('Checkpoint source fallback policy is invalid')
    keys = set(value['rows']) | set(value.get('source_fallbacks', {}))
    if any(not HEX64.fullmatch(str(key)) for key in keys):
        raise ExpansionError('Invalid checkpoint unit identity')
    return keys


def candidate_evidence(store, locale, generation, candidate, checksum=''):
    if checksum and not HEX64.fullmatch(str(checksum)):
        raise ExpansionError('Invalid candidate manifest checksum')
    archived = store.key('incremental', 'continuation-manifests', generation, locale, checksum+'.json') if checksum else None
    try:
        if not archived:
            raise R2NotFound('No archived manifest selected')
        raw = store._get(archived, maximum=MAX_CANDIDATE_MANIFEST_BYTES)
    except R2NotFound:
        raw = store._get(store.candidate_manifest_key(locale, generation, candidate), maximum=MAX_CANDIDATE_MANIFEST_BYTES)
    if checksum and digest(raw) != checksum:
        raise ExpansionError('Continuation candidate checksum mismatch')
    manifest = partial_manifest_is_valid(json.loads(raw), locale, generation)
    origin = read_origin(store, generation)
    if (not origin or not origin_allows_locale(origin, locale) or manifest['files_sha256'] != candidate
        or manifest.get('source_document_count') != origin['pages']
        or not isinstance(manifest.get('failures'), list) or type(manifest.get('budget_exhausted')) is not bool):
        raise ExpansionError('Continuation candidate inventory or outcome is invalid')
    corpus = json.loads(store._get(store.source_key(generation), maximum=MAX_SOURCE_BYTES))
    source_urls = {doc['url'] for doc in corpus['documents']}
    completed = [row['source_url'] for row in manifest['pages']]
    if len(set(completed)) != len(completed) or not set(completed) <= source_urls:
        raise ExpansionError('Continuation page inventory differs from original source')
    return manifest, digest(raw)


def record_result(store, locale, corpus, result, *, checkpoint_sha=None, owner=None):
    """Called after checkpoint and candidate persistence, including exit 75."""
    from portal_extended_incremental import read_state
    generation = corpus['documents_sha256']
    rows = queue(store, locale)
    previous = rows.get(generation)
    if previous is None:
        return  # Legacy unregistered callers keep their existing behavior.
    require_active_owner(store, locale, generation, owner=owner)
    pointer = read_state(store, 'memo', locale)
    checksum = checkpoint_sha or (pointer.get('sha256') if pointer.get('generation') == generation else None)
    keys = checkpoint_evidence(store, locale, generation, checksum)
    manifest, manifest_sha = candidate_evidence(store, locale, generation, result['candidate_id'], result['manifest_sha256'])
    # Candidate IDs hash page inventories. Partial attempts can have the same
    # page set but different outcome metadata: retain exact manifest bytes too.
    manifest_raw = store._get(store.candidate_manifest_key(locale, generation, result['candidate_id']), maximum=MAX_CANDIDATE_MANIFEST_BYTES)
    if digest(manifest_raw) != manifest_sha:
        raise ExpansionError('Candidate manifest changed during outcome persistence')
    store._put(store.key('incremental', 'continuation-manifests', generation, locale, manifest_sha+'.json'),
               manifest_raw, metadata={'kind': 'continuation-manifest'})
    snapshot = {'checkpoint_sha256': checksum, 'candidate_id': result['candidate_id'],
        'manifest_sha256': manifest_sha, 'completed_pages': manifest['completed_page_count'], 'resolved_units': len(keys)}
    reason = ''
    if manifest['status'] == 'complete-candidate':
        status = 'complete'
    elif manifest['failures'] or not manifest['budget_exhausted']:
        status, reason = 'blocked', 'Non-budget or unknown candidate failure requires diagnosis'
    elif not keys:
        status, reason = 'blocked', 'No checkpoint progress; automatic continuation stopped'
    else:
        status = 'incomplete'
    if previous['status'] == 'claimed':
        before = previous['snapshot']
        old_keys = checkpoint_evidence(store, locale, generation, before['checkpoint_sha256'])
        if not old_keys <= keys or snapshot['completed_pages'] < before['completed_pages']:
            status, reason = 'blocked', 'Checkpoint or complete-page coverage regressed'
        elif status != 'complete' and not keys > old_keys and snapshot['completed_pages'] <= before['completed_pages']:
            status, reason = 'blocked', 'No continuation progress; automatic continuation stopped'
    rows[generation] = {'status': status, 'continuations': previous['continuations'], 'snapshot': snapshot}
    if reason:
        rows[generation]['reason'] = reason
    # Immutable attempt evidence survives later queue acknowledgement.
    raw = stable_bytes(rows[generation])
    store._put(store.key('incremental', 'continuation-results', generation, locale, digest(raw)+'.json'),
               raw, metadata={'kind': 'continuation-result'})
    save_queue(store, locale, rows)
    if status == 'blocked':
        raise ExpansionError(reason)


def validate_snapshot(store, locale, generation, row):
    snapshot = row.get('snapshot')
    if (not isinstance(snapshot, dict) or any(not HEX64.fullmatch(str(snapshot.get(key, '')))
        for key in ('candidate_id', 'manifest_sha256', 'checkpoint_sha256'))):
        raise ExpansionError('Continuation snapshot is missing or malformed')
    manifest, _ = candidate_evidence(store, locale, generation,
        snapshot.get('candidate_id'), snapshot.get('manifest_sha256'))
    keys = checkpoint_evidence(store, locale, generation, snapshot.get('checkpoint_sha256'))
    if (type(snapshot.get('resolved_units')) is not int or len(keys) != snapshot['resolved_units']
        or type(snapshot.get('completed_pages')) is not int
        or manifest['completed_page_count'] != snapshot['completed_pages']):
        raise ExpansionError('Continuation snapshot counts differ from persisted evidence')
    if row['status'] == 'complete' and manifest['status'] != 'complete-candidate':
        raise ExpansionError('Completed continuation has no complete candidate')
    if row['status'] in {'incomplete', 'claimed'} and (
        not keys or manifest['status'] != 'incomplete-candidate'
        or not manifest['budget_exhausted'] or manifest['failures']):
        raise ExpansionError('Pending continuation proof is inconsistent')
    return manifest, keys


def partition_stopped_locales(store, locales):
    """Keep known stopped cursors visible while healthy locales can advance.

    Storage, origin/hash, or schema failures still propagate; only recognized
    lifecycle stops are isolated. A separate workflow job reports them as failure.
    """
    eligible, stopped = [], []
    for locale in locales:
        blocked = []
        for generation, row in queue(store, locale).items():
            origin = read_origin(store, generation)
            if not origin or not origin_allows_locale(origin, locale):
                raise ExpansionError('Registered cursor has no valid original source')
            if row['status'] != 'started':
                validate_snapshot(store, locale, generation, row)
            if row['status'] == 'complete':
                # Backfill explicit debt for old rendered outcomes before a
                # no-op source job can hide them behind zero pending pages.
                from portal_extended_quality import record_quality
                record_quality(store, locale, generation, row['snapshot']['candidate_id'],
                               manifest_sha256=row['snapshot']['manifest_sha256'])
            if row['status'] in {'started', 'claimed'}:
                producer_identity(row.get('owner'))
            reason = ''
            if row['status'] in {'started', 'claimed'}:
                reason = 'Missing completed checkpoint outcome; diagnosis required'
            elif row['status'] == 'blocked':
                reason = row.get('reason')
                if not isinstance(reason, str) or not reason or len(reason) > 500:
                    raise ExpansionError('Stopped continuation diagnostic is malformed')
            elif row['status'] == 'incomplete' and row['continuations'] >= MAX_CONTINUATIONS:
                reason = 'Continuation bound reached; diagnosis required'
            if reason:
                blocked.append({'locale': locale, 'generation': generation, 'source_day': origin['source_day'],
                                'status': row['status'], 'continuations': row['continuations'],
                                'reason': reason, 'model_calls': 0})
        if blocked:
            first = sorted(blocked, key=lambda row: (row['source_day'], row['generation']))[0]
            stopped.append({**first, 'stopped_generation_count': len(blocked)})
        else:
            eligible.append(locale)
    return tuple(eligible), stopped


def pending(store, locales, output, *, generation=None, producer=None):
    """Select and claim one already-started generation before any daily collection."""
    groups = {}
    all_queues = {locale: queue(store, locale) for locale in locales}
    for locale, rows in all_queues.items():
        for current, row in rows.items():
            if generation and current != generation:
                continue
            if row['status'] == 'complete':
                continue
            origin = read_origin(store, current)
            if not origin or not origin_allows_locale(origin, locale):
                raise ExpansionError('Pending generation lacks its original source proof')
            if row['status'] != 'incomplete':
                raise ExpansionError(f'Continuation stopped for {locale}/{current}: '+row.get('reason', 'missing completed checkpoint outcome'))
            if row['continuations'] >= MAX_CONTINUATIONS:
                raise ExpansionError(f'Continuation bound reached for {locale}/{current}; retained for diagnosis')
            manifest, _ = candidate_evidence(store, locale, current, row['snapshot']['candidate_id'], row['snapshot']['manifest_sha256'])
            keys = checkpoint_evidence(store, locale, current, row['snapshot']['checkpoint_sha256'])
            if (not keys or len(keys) != row['snapshot']['resolved_units']
                or manifest['completed_page_count'] != row['snapshot']['completed_pages']
                or manifest['status'] != 'incomplete-candidate' or not manifest['budget_exhausted'] or manifest['failures']):
                raise ExpansionError('Pending continuation proof is inconsistent')
            groups.setdefault((origin['source_day'], current), []).append(locale)
    if not groups:
        return None
    (day, selected), active = sorted(groups.items())[0]
    owner = producer_identity(producer) if producer is not None else action_owner()
    # All validation precedes claims. Restore original bytes; no collect_today.
    store.restore_source(selected, output)
    for locale in active:
        rows = all_queues[locale]
        rows[selected] = {**rows[selected], 'status': 'claimed', 'continuations': rows[selected]['continuations'] + 1,
                          'owner': owner or read_origin(store, selected)['producer']}
        save_queue(store, locale, rows)
    return {'has_work': True, 'generation': selected, 'locales_json': json.dumps(active), 'day': day,
        'selected_page_count': read_origin(store, selected)['pages'], 'continuation': True,
        'paid_provider_requests': 0}


def restore_claimed_checkpoint(store, locale, generation, output):
    """A continuation must use the exact claimed immutable snapshot, not latest."""
    row = queue(store, locale).get(generation)
    require_active_owner(store, locale, generation)
    if row and row['status'] == 'claimed':
        checksum = row['snapshot']['checkpoint_sha256']
        checkpoint_evidence(store, locale, generation, checksum)
        raw = store._get(store.checkpoint_object_key(locale, generation, checksum), maximum=MAX_CHECKPOINT_BYTES)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(raw)
        return {'present': True, 'locale': locale, 'generation': generation, 'sha256': checksum, 'immutable_claim': True}
    if row and row['status'] != 'started':
        raise ExpansionError('Locale retry requires a new source-job claim; refusing unbounded implicit replay')
    return store.restore_checkpoint(locale, generation, output)


def tracked_generations(store, locales):
    generations = {}
    for locale in locales:
        for generation, row in queue(store, locale).items():
            if row['status'] == 'complete':
                origin = read_origin(store, generation)
                if not origin or not origin_allows_locale(origin, locale):
                    raise ExpansionError('Completed generation lacks original source proof')
                generations.setdefault((origin['source_day'], generation), set()).add(locale)
    return generations


def acknowledge_published(store, locales, active):
    """Remove only exact live triples; immutable origins/results are retained."""
    published = {(locale, row['generation'], candidate) for row in active for locale, candidate in row['candidates'].items()}
    for locale in locales:
        rows = queue(store, locale)
        # Preserve quality debt before ACK removes a legacy active render receipt.
        from portal_extended_quality import record_quality
        for generation, row in rows.items():
            if row['status'] == 'complete' and (locale, generation, row['snapshot']['candidate_id']) in published:
                record_quality(store, locale, generation, row['snapshot']['candidate_id'])
        keep = {generation: row for generation, row in rows.items() if not (
            row['status'] == 'complete' and (locale, generation, row['snapshot']['candidate_id']) in published)}
        if keep != rows:
            save_queue(store, locale, keep)


def verify_origin_run(origin, run, jobs, repository, *, admitted=None):
    """A historical corpus is admissible only as a proved original daily run."""
    from portal_extended_locales import publication_day
    producer = producer_identity(origin['producer'])
    if (run.get('id') != int(producer['run_id']) or run.get('run_attempt') != int(producer['attempt'])
        or run.get('head_sha') != producer['sha'] or run.get('status') != 'completed'
        or run.get('conclusion') not in {'success', 'failure'}
        or run.get('path') != '.github/workflows/portal-extended-locales-r2.yml'
        or run.get('head_branch') != 'main' or run.get('event') not in {'workflow_run', 'workflow_dispatch'}
        or any((run.get(k) or {}).get('full_name') != repository for k in ('repository', 'head_repository'))
        or (run.get('repository') or {}).get('private') is not False):
        raise ExpansionError('Original daily producer identity is not verified')
    source = [row for row in jobs if row.get('name') == 'source']
    frozen = (admitted is not None and origin.get('source_admission') == admitted.get('admission')
              and origin['source_day'] == admitted.get('day'))
    if (len(source) != 1 or source[0].get('status') != 'completed' or source[0].get('conclusion') != 'success'
        or (not frozen and origin['source_day'] not in {publication_day(source[0].get(k, '')) for k in ('started_at', 'completed_at')})):
        raise ExpansionError('Original source job does not prove the daily source date')


def validate_existing(store, corpus, locales, evidence, repository, api):
    """Read-only verification of exact pre-ledger objects; no listing/backfill."""
    import tempfile
    from inspect_portal_extended_continuation import inspect
    generation = corpus['documents_sha256']
    if not isinstance(evidence, dict) or set(evidence) != {'producer', 'locales'}:
        raise ExpansionError('Invalid exact existing-generation evidence')
    producer = producer_identity(evidence['producer'])
    proofs = evidence['locales']
    if not isinstance(proofs, dict) or set(proofs) != set(locales):
        raise ExpansionError('Adoption locale proof must exactly match the requested locales')
    origin = {'producer': producer, 'source_day': daily_corpus_day(corpus)}
    path = f'repos/{repository}/actions/runs/{producer["run_id"]}/attempts/{producer["attempt"]}'
    jobs = api(path+'/jobs?per_page=100')
    if type(jobs.get('total_count')) is not int or jobs['total_count'] > 100 or len(jobs.get('jobs', [])) != jobs['total_count']:
        raise ExpansionError('Original producer job inventory is incomplete')
    verify_origin_run(origin, api(path), jobs['jobs'], repository)
    validated = {}
    with tempfile.TemporaryDirectory(prefix='continuation-adoption-') as temporary:
        for locale, proof in proofs.items():
            if not isinstance(proof, dict) or set(proof) != {'checkpoint_sha256', 'candidate_id', 'manifest_sha256'}:
                raise ExpansionError('Invalid immutable continuation proof')
            summary = inspect(store, generation, locale, proof['checkpoint_sha256'], proof['candidate_id'], Path(temporary)/locale)
            locale_jobs = [row for row in jobs['jobs'] if row.get('name') == f'locale ({locale})']
            if (len(locale_jobs) != 1 or locale_jobs[0].get('status') != 'completed'
                or locale_jobs[0].get('conclusion') not in {'success', 'failure'}
                or summary['manifest_sha256'] != proof['manifest_sha256']
                or summary['status'] != 'incomplete-candidate' or summary['budget_exhausted'] is not True
                or summary['failure_count'] != 0 or not checkpoint_evidence(store, locale, generation, proof['checkpoint_sha256'])):
                raise ExpansionError('Existing generation is not a proved checkpointed budget continuation')
            validated[locale] = proof
    return producer, validated


def adopt_existing(store, corpus, locales, evidence, repository, api):
    """One explicit migration of exact pre-ledger objects; no listing/backfill."""
    if read_origin(store, corpus['documents_sha256']) is not None:
        raise ExpansionError('Generation is already registered; adoption cannot reset continuation limits')
    producer, validated = validate_existing(store, corpus, locales, evidence, repository, api)
    # Every locale and GitHub origin has been verified before any private writes.
    register(store, corpus, locales, producer)
    for locale, proof in validated.items():
        record_result(store, locale, corpus, proof, checkpoint_sha=proof['checkpoint_sha256'], owner=producer)
