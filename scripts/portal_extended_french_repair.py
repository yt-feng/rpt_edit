"""Exact complete-to-complete French fallback repair in the serialized queue."""
from __future__ import annotations

import copy
import json
import tempfile
from pathlib import Path

from portal_extended_continuation import (checkpoint_evidence,
    producer_identity, queue, read_origin, save_queue, verify_origin_run)
from portal_extended_daily_queue import batch_admission, immutable_record
from portal_extended_incremental import content_key, read_state, write_state
from portal_extended_locales import ExpansionError, daily_corpus_day, digest, stable_bytes
from portal_extended_r2 import (HEX64, MAX_CHECKPOINT_BYTES, MAX_SOURCE_BYTES,
    MAX_CANDIDATE_MANIFEST_BYTES, MAX_CANDIDATE_PAGE_BYTES, R2NotFound, R2Store, checkpoint_is_valid)

POLICY = 'fr-quantity-fallback-v1'
REVISION = 'fr-space-grouping-quarter-v1'
WORKFLOW = '.github/workflows/portal-extended-locales-r2.yml'
LOCALE = 'fr'


def require(condition, message):
    if not condition:
        raise ExpansionError(message)


def repair_key(store, repair, *parts):
    return store.key('source-fallback-repairs', REVISION, digest(stable_bytes(repair)), *parts)


def proof_key(store, identity):
    require(isinstance(identity, str) and HEX64.fullmatch(identity), 'Invalid French repair proof identity')
    return store.key('source-fallback-repair-proofs', identity, 'receipt.json')


def read_optional(store, name):
    try:
        raw = store._get(name, maximum=65536)
    except R2NotFound:
        return None
    value = json.loads(raw)
    require(raw == stable_bytes(value), 'French repair metadata is not canonical')
    return value


def claim_key(store, repair, owner):
    return repair_key(store, repair, 'claims', digest(stable_bytes(producer_identity(owner)))+'.json')


def check_generation(generation, locale):
    require(locale == LOCALE and isinstance(generation, str) and HEX64.fullmatch(generation),
            'French repair requires one exact French generation')


def frozen(store, generation, repair, workspace):
    """Read only immutable original evidence; never fall back to a latest memo."""
    from repair_portal_french_source_fallback import inspect_frozen
    origin = read_origin(store, generation)
    require(origin is not None and digest(stable_bytes(origin)) == repair['origin_sha256']
            and origin['producer'] == producer_identity(repair['producer'])
            and origin['source_sha256'] == repair['source_sha256'], 'French repair original source identity differs')
    raw = store._get(store.source_key(generation), maximum=MAX_SOURCE_BYTES)
    require(digest(raw) == repair['source_sha256'], 'French repair source bytes differ')
    corpus = json.loads(raw)
    checkpoint = store._get(store.checkpoint_object_key(LOCALE, generation, repair['checkpoint_sha256']),
                            maximum=MAX_CHECKPOINT_BYTES)
    require(digest(checkpoint) == repair['checkpoint_sha256'], 'French repair checkpoint bytes differ')
    candidate = workspace/'old-candidate'
    store.restore_candidate(LOCALE, generation, repair['candidate_id'], candidate)
    summary = inspect_frozen(corpus, checkpoint, candidate, repair)
    manifest = json.loads((candidate/'candidate-manifest.json').read_bytes())
    require(manifest['status'] == 'complete-candidate' and not manifest['failures']
            and not manifest['budget_exhausted'] and manifest['completed_page_count'] == len(corpus['documents']),
            'French repair requires the entire original complete page set')
    snapshot = {key: repair[key] for key in ('checkpoint_sha256', 'candidate_id', 'manifest_sha256')}
    snapshot.update(completed_pages=len(corpus['documents']),
                    resolved_units=len(checkpoint_evidence(store, LOCALE, generation, repair['checkpoint_sha256'])))
    return corpus, checkpoint, candidate, origin, snapshot, summary


def authenticate_original(store, origin, repository, api):
    producer = producer_identity(origin['producer'])
    path = f'repos/{repository}/actions/runs/{producer["run_id"]}/attempts/{producer["attempt"]}'
    run, page = api(path), api(path+'/jobs?per_page=100')
    jobs = page.get('jobs')
    require(type(page.get('total_count')) is int and 0 < page['total_count'] <= 100
            and isinstance(jobs, list) and len(jobs) == page['total_count'],
            'French repair original job inventory is incomplete')
    admitted = batch_admission(store, origin['generation'])
    verify_origin_run(origin, run, jobs, repository, admitted=admitted)
    matched = [job for job in jobs if job.get('name') == 'locale (fr)']
    require(len(matched) == 1 and matched[0].get('status') == 'completed'
            and matched[0].get('conclusion') == 'success'
            and matched[0].get('run_id') == int(producer['run_id'])
            and matched[0].get('head_sha') == producer['sha'], 'French repair original locale did not succeed')


def verify_repair_producer(proof, run, jobs, repository, *, completion=None):
    """An immutable proof also needs its actual completed main recovery job."""
    owner = producer_identity((completion or proof)['producer'])
    require(run.get('id') == int(owner['run_id']) and run.get('run_attempt') == int(owner['attempt'])
            and run.get('head_sha') == owner['sha'] and run.get('path') == WORKFLOW
            and run.get('status') == 'completed' and run.get('conclusion') in {'success', 'failure'}
            and run.get('event') == 'workflow_dispatch' and run.get('head_branch') == 'main'
            and all((run.get(k) or {}).get('full_name') == repository for k in ('repository', 'head_repository'))
            and (run.get('repository') or {}).get('private') is False,
            'French repair producer is not an exact completed public main dispatch')
    for name in (('source',) if completion else ('source', 'locale (fr)')):
        selected = [job for job in jobs if job.get('name') == name]
        require(len(selected) == 1 and selected[0].get('status') == 'completed'
                and selected[0].get('conclusion') == 'success'
                and selected[0].get('run_id') == int(owner['run_id'])
                and selected[0].get('head_sha') == owner['sha'],
                'French repair producer job did not complete with the exact identity')
    if completion:
        require(completion['proof_sha256'] == digest(stable_bytes(proof))
                and completion['mode'] == 'prepared-tail-resume', 'French repair resumption proof differs')
        skipped = [job for job in jobs if job.get('name') in {'locale', 'locale (fr)'}]
        require(len(skipped) == 1 and skipped[0].get('status') == 'completed'
                and skipped[0].get('conclusion') == 'skipped'
                and skipped[0].get('run_id') == int(owner['run_id'])
                and skipped[0].get('head_sha') == owner['sha'],
                'French prepared resumption must skip locale inference')


def guard_current(store, corpus, snapshot, *, old_row=None, new_row=None):
    generation = corpus['documents_sha256']
    current = queue(store, LOCALE).get(generation)
    if old_row is None:
        require(isinstance(current, dict) and current.get('status') == 'complete'
                and current.get('snapshot') == snapshot, 'French repair cannot replace a newer or incomplete outcome')
    else:
        require(current == old_row or current == new_row, 'French repair registered outcome advanced')
    pages = read_state(store, 'completed', LOCALE, daily_corpus_day(corpus)).get('pages', {})
    require(isinstance(pages, dict), 'French repair completed receipts are invalid')
    candidates = {snapshot['candidate_id']}
    if new_row is not None:
        candidates.add(new_row['snapshot']['candidate_id'])
    for doc in corpus['documents']:
        row = pages.get(doc['url'])
        require(isinstance(row, dict) and row.get('content_key') == content_key(doc)
                and row.get('generation') == generation and row.get('candidate_id') in candidates,
                'French repair cannot replace newer completed page content')
    return copy.deepcopy(current), pages


def merge_latest_memo(store, old, new, accepted):
    """Merge only accepted exact keys into the verified current seed snapshot."""
    pointer = read_state(store, 'memo', LOCALE)
    generation, checksum = pointer.get('generation'), pointer.get('sha256')
    require(isinstance(generation, str) and HEX64.fullmatch(generation)
            and isinstance(checksum, str) and HEX64.fullmatch(checksum), 'French repair latest memo identity is invalid')
    raw = store._get(store.checkpoint_object_key(LOCALE, generation, checksum), maximum=MAX_CHECKPOINT_BYTES)
    require(digest(raw) == checksum, 'French repair latest memo checksum differs')
    value = json.loads(raw)
    checkpoint_is_valid(value, LOCALE, generation)
    require(isinstance(value.get('source_fallbacks', {}), dict), 'French repair latest memo fallbacks are invalid')
    merged = copy.deepcopy(value)
    for identity in accepted:
        replacement = new['rows'][identity]
        present = value['rows'].get(identity)
        fallback = value.get('source_fallbacks', {}).get(identity)
        require((present is None or present == replacement)
                and (fallback is None or fallback == old['source_fallbacks'][identity]),
                'French repair refuses to overwrite a newer memo unit')
        merged['rows'][identity] = replacement
        merged.setdefault('source_fallbacks', {}).pop(identity, None)
    merged_raw = stable_bytes(merged)
    require(len(merged_raw) <= MAX_CHECKPOINT_BYTES, 'French repair merged memo exceeds bound')
    after = {**pointer, 'sha256': digest(merged_raw)}
    return pointer, after, merged_raw


def put_immutable_bytes(store, name, raw, *, kind, maximum):
    require(0 < len(raw) <= maximum, 'French repair immutable object exceeds bound')
    try:
        previous = store._get(name, maximum=maximum)
    except R2NotFound:
        store._put(name, raw, metadata={'kind': kind})
        previous = store._get(name, maximum=maximum)
    require(previous == raw, 'French repair cannot overwrite immutable evidence')


def upload_immutable_candidate(store, output, generation):
    """Finish an interrupted upload without overwriting any existing bytes."""
    class ImmutableCandidateStore:
        def __getattr__(self, name): return getattr(store, name)
        def _put(self, name, raw, *, metadata):
            limit = MAX_CANDIDATE_PAGE_BYTES if metadata['kind'] == 'candidate-page' else MAX_CANDIDATE_MANIFEST_BYTES
            put_immutable_bytes(store, name, raw, kind=metadata['kind'], maximum=limit)
            return {'sha256': digest(raw)}
    return R2Store.upload_candidate(ImmutableCandidateStore(), output, LOCALE, generation)


def verify_proof(store, identity, generation, candidate=None, checkpoint=None):
    from repair_portal_french_source_fallback import request, verify_rebuild
    proof = read_optional(store, proof_key(store, identity))
    require(proof is not None and digest(stable_bytes(proof)) == identity
            and set(proof) == {'schema_version', 'policy', 'generation', 'locale', 'request', 'producer',
                              'before_row', 'after_row', 'memo_before', 'memo_after', 'delta'}
            and type(proof['schema_version']) is int and proof['schema_version'] == 1
            and proof['policy'] == POLICY and proof['generation'] == generation and proof['locale'] == LOCALE,
            'French repair proof contract differs')
    repair = request(proof['request'])
    producer_identity(proof['producer'])
    claim = read_optional(store, claim_key(store, repair, proof['producer']))
    require(claim == {'request': repair, 'producer': proof['producer'], 'before_row': proof['before_row']},
            'French repair proof lacks its exact source-job claim')
    with tempfile.TemporaryDirectory(prefix='fr-repair-proof-') as temp:
        corpus, old_raw, old_dir, origin, snapshot, _ = frozen(store, generation, repair, Path(temp))
        delta = proof['delta']
        expected_after = copy.deepcopy(proof['before_row'])
        require(expected_after.get('status') == 'complete' and expected_after.get('snapshot') == snapshot,
                'French repair proof original outcome differs')
        new_raw = store._get(store.checkpoint_object_key(LOCALE, generation, delta['new']['checkpoint_sha256']),
                             maximum=MAX_CHECKPOINT_BYTES)
        new_dir = Path(temp)/'new-candidate'
        store.restore_candidate(LOCALE, generation, delta['new']['candidate_id'], new_dir)
        verify_rebuild(store, corpus, old_raw, new_raw, old_dir, new_dir, repair, delta)
        if delta['changed']:
            expected_after.pop('source_repair_sha256', None)
            expected_after.pop('source_repair_completion_sha256', None)
            expected_after['snapshot'] = {**snapshot, **delta['new']}
        require(proof['after_row'] == expected_after, 'French repair changed origin or continuation counters')
        if candidate is not None:
            require(delta['new']['candidate_id'] == candidate, 'French repair publication candidate differs')
        if checkpoint is not None:
            require(delta['new']['checkpoint_sha256'] == checkpoint, 'French repair publication checkpoint differs')
        if delta['changed']:
            before, after = proof['memo_before'], proof['memo_after']
            require(isinstance(before, dict) and isinstance(after, dict)
                    and {k:v for k,v in before.items() if k != 'sha256'} == {k:v for k,v in after.items() if k != 'sha256'},
                    'French repair moved the latest memo generation')
            # Validate the merge from the captured immutable latest snapshot,
            # independent of whether the mutable pointer already advanced.
            class CapturedStore:
                def __getattr__(self, name): return getattr(store, name)
                def _get(self, key, *, maximum):
                    from portal_extended_incremental import state_key
                    return stable_bytes(before) if key == state_key(store, 'memo', LOCALE) else store._get(key, maximum=maximum)
            _, expected_memo, merged = merge_latest_memo(CapturedStore(), json.loads(old_raw), json.loads(new_raw), delta['accepted_units'])
            require(expected_memo == after, 'French repair memo delta differs')
            persisted = store._get(store.checkpoint_object_key(LOCALE, after['generation'], after['sha256']), maximum=MAX_CHECKPOINT_BYTES)
            require(persisted == merged, 'French repair merged memo bytes differ')
        else:
            require(proof['memo_before'] is None and proof['memo_after'] is None,
                    'Unchanged French candidate cannot modify the memo')
    return proof


def commit_prepared(store, identity):
    value = read_optional(store, proof_key(store, identity))
    require(value is not None, 'French repair prepared proof is missing')
    proof = verify_proof(store, identity, value['generation'])
    if not proof['delta']['changed']:
        return proof
    repair, generation = proof['request'], proof['generation']
    with tempfile.TemporaryDirectory(prefix='fr-repair-commit-') as temp:
        corpus, _, _, _, snapshot, _ = frozen(store, generation, repair, Path(temp))
        before, after = proof['before_row'], proof['after_row']
        published_after = {**after, 'source_repair_sha256': identity}
        previous = queue(store, LOCALE).get(generation, {})
        completion = previous.get('source_repair_completion_sha256')
        if completion is not None and previous != before:
            verify_completion(store, completion, proof, identity)
            published_after['source_repair_completion_sha256'] = completion
        current, pages = guard_current(store, corpus, snapshot, old_row=before, new_row=published_after)
        memo = read_state(store, 'memo', LOCALE)
        require(memo == proof['memo_before'] or memo == proof['memo_after'], 'French repair latest memo advanced after preparation')
        pointer_path = Path(temp)/'current-checkpoint.json'
        pointer = store.restore_checkpoint(LOCALE, generation, pointer_path)
        require(pointer.get('present') and pointer['sha256'] in
                {snapshot['checkpoint_sha256'], after['snapshot']['checkpoint_sha256']},
                'French repair per-generation checkpoint advanced')
        # Every mutable target was checked before any tail write. Interrupted
        # tails accept only the exact before/after values on replay.
        new_raw = store._get(store.checkpoint_object_key(LOCALE, generation, after['snapshot']['checkpoint_sha256']),
                             maximum=MAX_CHECKPOINT_BYTES)
        pointer_path.write_bytes(new_raw)
        store.put_checkpoint(LOCALE, generation, pointer_path)
        memo_fields = {k:v for k,v in proof['memo_after'].items()
                       if k not in {'schema_version', 'scope', 'model', 'locale', 'day'}}
        write_state(store, 'memo', LOCALE, memo_fields)
        for doc in corpus['documents']:
            pages[doc['url']] = {**pages[doc['url']], 'candidate_id': after['snapshot']['candidate_id']}
        write_state(store, 'completed', LOCALE, {'pages': pages}, daily_corpus_day(corpus))
        rows = queue(store, LOCALE)
        require(rows.get(generation) == current, 'French repair outcome changed during commit')
        rows[generation] = published_after
        immutable_record(store, store.key('incremental', 'continuation-results', generation, LOCALE,
                         digest(stable_bytes(published_after))+'.json'), published_after, kind='continuation-result')
        save_queue(store, LOCALE, rows)
        require(queue(store, LOCALE).get(generation) == published_after
                and read_state(store, 'memo', LOCALE) == proof['memo_after'], 'French repair tail readback differs')
    return proof


def prepared_proof(store, repair):
    value = read_optional(store, repair_key(store, repair, 'prepared.json'))
    if value is None: return None
    require(set(value) == {'proof_sha256'} and isinstance(value['proof_sha256'], str)
            and HEX64.fullmatch(value['proof_sha256']), 'French repair prepared pointer is invalid')
    return value['proof_sha256']


def completion_key(store, identity):
    require(isinstance(identity, str) and HEX64.fullmatch(identity), 'Invalid French resumption identity')
    return store.key('source-fallback-repair-completions', identity, 'receipt.json')


def verify_completion(store, identity, proof, proof_identity):
    value = read_optional(store, completion_key(store, identity))
    require(value is not None and digest(stable_bytes(value)) == identity
            and set(value) == {'schema_version', 'policy', 'proof_sha256', 'producer', 'mode'}
            and type(value['schema_version']) is int and value['schema_version'] == 1
            and value['policy'] == POLICY and value['proof_sha256'] == proof_identity
            and value['mode'] == 'prepared-tail-resume' and proof['delta']['changed']
            and prepared_proof(store, proof['request']) == proof_identity,
            'French resumption does not bind its exact immutable prepared proof')
    producer_identity(value['producer'])
    return value


def record_completion(store, identity, proof, owner):
    """Bind source-only tail recovery to its own future completed Actions run."""
    if not proof['delta']['changed']:
        return
    value = {'schema_version': 1, 'policy': POLICY, 'proof_sha256': identity,
             'producer': producer_identity(owner), 'mode': 'prepared-tail-resume'}
    checksum = digest(stable_bytes(value))
    immutable_record(store, completion_key(store, checksum), value, kind='fr-source-fallback-repair-completion')
    verify_completion(store, checksum, proof, identity)
    rows = queue(store, LOCALE)
    current = rows.get(proof['generation'], {})
    expected = {**proof['after_row'], 'source_repair_sha256': identity}
    require({k:v for k,v in current.items() if k != 'source_repair_completion_sha256'} == expected,
            'French resumption cannot replace an advanced result')
    rows[proof['generation']] = {**expected, 'source_repair_completion_sha256': checksum}
    completed = rows[proof['generation']]
    immutable_record(store, store.key('incremental', 'continuation-results', proof['generation'], LOCALE,
                     digest(stable_bytes(completed))+'.json'), completed, kind='continuation-result')
    save_queue(store, LOCALE, rows)


def persist(store, generation, repair, owner, checkpoint, output):
    from repair_portal_french_source_fallback import verify_rebuild
    prior = prepared_proof(store, repair)
    if prior is not None:
        return commit_prepared(store, prior)
    claim = read_optional(store, claim_key(store, repair, owner))
    require(claim is not None and claim['request'] == repair and claim['producer'] == producer_identity(owner),
            'French repair requires its exact source-job claim')
    with tempfile.TemporaryDirectory(prefix='fr-repair-persist-') as temp:
        corpus, old_raw, old_dir, origin, snapshot, _ = frozen(store, generation, repair, Path(temp))
        current, _ = guard_current(store, corpus, snapshot, old_row=claim['before_row'])
        new_raw = checkpoint.read_bytes()
        delta = json.loads((output.parent/'fr-source-fallback-repair-proof.json').read_bytes())
        verify_rebuild(store, corpus, old_raw, new_raw, old_dir, output, repair, delta)
        after = copy.deepcopy(current)
        memo_before = memo_after = None
        if delta['changed']:
            require(delta['new']['candidate_id'] != repair['candidate_id'], 'French repair cannot overwrite a same-ID manifest')
            after.pop('source_repair_sha256', None)
            after.pop('source_repair_completion_sha256', None)
            after['snapshot'] = {**snapshot, **delta['new']}
            memo_before, memo_after, merged = merge_latest_memo(store, json.loads(old_raw), json.loads(new_raw), delta['accepted_units'])
            put_immutable_bytes(store, store.checkpoint_object_key(LOCALE, memo_after['generation'], memo_after['sha256']),
                                merged, kind='translation-checkpoint', maximum=MAX_CHECKPOINT_BYTES)
            put_immutable_bytes(store, store.checkpoint_object_key(LOCALE, generation, delta['new']['checkpoint_sha256']),
                                new_raw, kind='translation-checkpoint', maximum=MAX_CHECKPOINT_BYTES)
            upload_immutable_candidate(store, output, generation)
        proof = {'schema_version': 1, 'policy': POLICY, 'generation': generation, 'locale': LOCALE,
                 'request': repair, 'producer': producer_identity(owner), 'before_row': current, 'after_row': after,
                 'memo_before': memo_before, 'memo_after': memo_after, 'delta': delta}
        identity = digest(stable_bytes(proof))
        immutable_record(store, proof_key(store, identity), proof, kind='fr-source-fallback-repair-proof')
        verify_proof(store, identity, generation)
        immutable_record(store, repair_key(store, repair, 'prepared.json'), {'proof_sha256': identity},
                         kind='fr-source-fallback-repair-prepared')
    return commit_prepared(store, identity)


def result(corpus, *, has_work):
    generation, day = corpus['documents_sha256'], daily_corpus_day(corpus)
    return {'has_work': has_work, 'generation': generation, 'day': day, 'requested_locales': LOCALE,
            'locales_json': json.dumps([LOCALE] if has_work else []),
            'locale_jobs_json': json.dumps([{'locale': LOCALE, 'generation': generation, 'day': day}] if has_work else []),
            'source_admission': '', 'english_admission': '', 'stopped_locales_json': '[]'}


def run(args, value, owner, *, store, repository, api):
    from repair_portal_french_source_fallback import request, rebuild
    check_generation(args.generation, args.locale)
    inspecting = args.operation == 'inspect'
    if inspecting:
        # Read-only discovery may fill these two previously unknown hashes from
        # authenticated private origin evidence; mutation must pin them itself.
        origin = read_origin(store, args.generation)
        require(origin is not None, 'French inspection needs a registered original source')
        value = dict(value)
        value.setdefault('source_sha256', origin['source_sha256'])
        value.setdefault('origin_sha256', digest(stable_bytes(origin)))
    repair = request(value, require_units=not inspecting)
    with tempfile.TemporaryDirectory(prefix='fr-source-repair-') as temp:
        corpus, old_raw, old_dir, origin, snapshot, summary = frozen(store, args.generation, repair, Path(temp))
        authenticate_original(store, origin, repository, api)
        prior = prepared_proof(store, repair)
        if args.operation == 'prepare' and prior is not None:
            proof = commit_prepared(store, prior)
            record_completion(store, prior, proof, owner)
            outcome = result(corpus, has_work=False)
        elif inspecting:
            guard_current(store, corpus, snapshot)
            outcome = {**result(corpus, has_work=False), 'inspection': summary, 'frozen_request': repair}
        elif args.operation == 'prepare':
            before, _ = guard_current(store, corpus, snapshot)
            immutable_record(store, claim_key(store, repair, owner),
                {'request': repair, 'producer': producer_identity(owner), 'before_row': before}, kind='fr-repair-claim')
            outcome = result(corpus, has_work=True)
        else:
            claim = read_optional(store, claim_key(store, repair, owner))
            require(claim is not None and claim['request'] == repair and claim['producer'] == producer_identity(owner),
                    'French repair requires its exact source-job claim')
            if args.operation != 'persist': guard_current(store, corpus, snapshot, old_row=claim['before_row'])
            if args.operation == 'restore':
                args.checkpoint.write_bytes(old_raw)
                args.corpus.write_bytes(stable_bytes(corpus))
                outcome = {'present': True, 'exact_snapshot': True}
            elif args.operation == 'build':
                from offline_translation import OfflineTranslator
                require(args.checkpoint.is_file() and args.checkpoint.read_bytes() == old_raw,
                        'French repair build requires its exact restored checkpoint')
                fresh_checkpoint = Path(temp)/'rebuilt-checkpoint.json'
                translator = OfflineTranslator(validation_attempts=1)
                delta = rebuild(store, corpus, old_raw, old_dir, args.output, fresh_checkpoint, repair,
                                owner, translator, seconds=args.seconds)
                args.checkpoint.write_bytes(fresh_checkpoint.read_bytes())
                (args.output.parent/'fr-source-fallback-repair-proof.json').write_bytes(stable_bytes(delta))
                outcome = {'status': 'complete-candidate', 'changed': delta['changed'],
                           'selected_units': len(repair['units']), 'accepted_units': len(delta['accepted_units']),
                           'terminal_units': len(delta['terminal_units']), 'residual_fallbacks': delta['fallbacks_after']}
                from build_portal_extended_locales import public_translation_diagnostics
                outcome.update(public_translation_diagnostics(translator, LOCALE))
            elif args.operation == 'persist':
                proof = persist(store, args.generation, repair, owner, args.checkpoint, args.output)
                outcome = {'status': 'complete-candidate', 'proof_sha256': digest(stable_bytes(proof)),
                           'changed': proof['delta']['changed'], 'residual_fallbacks': proof['delta']['fallbacks_after']}
            else:
                raise ExpansionError('Unsupported French repair operation')
    if args.github_output:
        with args.github_output.open('a') as file:
            for key, item in outcome.items():
                if key not in {'inspection', 'frozen_request'}:
                    file.write(f'{key}={str(item).lower() if isinstance(item, bool) else item}\n')
    print(json.dumps(outcome, sort_keys=True))
    return 0
