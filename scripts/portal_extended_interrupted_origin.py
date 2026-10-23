"""Explicit provenance for admitted sources interrupted before any locale ran.

The immutable proof describes independent capture and the unused original run,
never a replacement run. Consumers must separately prove actual locale completion.
"""
from __future__ import annotations

import json

from portal_extended_continuation import producer_identity, read_origin
from portal_extended_daily_queue import batch_admission, immutable_record
from portal_extended_locales import ExpansionError, digest, stable_bytes
from portal_extended_r2 import HEX64, R2NotFound

POLICY = 'interrupted-admitted-source-origin-v1'
MAX_BYTES = 65536


def require(condition, code):
    if not condition:
        raise ExpansionError(code)


def proof_key(store, origin):
    return store.key('incremental', 'interrupted-source-origins', origin['generation'],
                     digest(stable_bytes(origin))+'.json')


def bound_proof(value, origin, repository):
    require(isinstance(value, dict) and set(value) == {'schema_version', 'policy', 'repository',
        'generation', 'origin_sha256', 'source_sha256', 'source_day', 'source_admission',
        'admission_producer', 'original_unused'} and value['schema_version'] == 1
        and value['policy'] == POLICY and value['repository'] == repository
        and value['generation'] == origin['generation']
        and value['origin_sha256'] == digest(stable_bytes(origin))
        and value['source_sha256'] == origin['source_sha256'] and value['source_day'] == origin['source_day']
        and bool(origin.get('source_admission')) and value['source_admission'] == origin['source_admission']
        and isinstance(value['original_unused'], dict)
        and value['original_unused'].get('owner') == producer_identity(origin['producer']),
        'interrupted_origin_proof_binding_invalid')
    return value


def read_proof(store, origin, *, identity=None):
    if identity is not None:
        require(isinstance(identity, str) and HEX64.fullmatch(identity), 'interrupted_origin_identity_invalid')
    try:
        raw = store._get(proof_key(store, origin), maximum=MAX_BYTES)
    except R2NotFound:
        require(identity is None, 'interrupted_origin_proof_missing')
        return None
    value = json.loads(raw)
    require(raw == stable_bytes(value) and (identity is None or digest(raw) == identity),
            'interrupted_origin_proof_checksum_invalid')
    bound_proof(value, origin, value.get('repository') if isinstance(value, dict) else None)
    return value


def prove(store, origin, repository, api):
    """Read-only: authenticate capture and exact original no-worker API evidence."""
    from portal_extended_unstarted_claims import all_jobs, unused_owner
    from review_portal_extended_handoff import admission_is_valid
    current = read_origin(store, origin['generation'])
    require(current == origin and bool(origin.get('source_admission')), 'interrupted_origin_requires_admission')
    admitted = batch_admission(store, origin['generation'])
    require(admitted is not None and admitted['admission'] == origin['source_admission']
            and admitted['day'] == origin['source_day'], 'interrupted_origin_admission_binding_invalid')
    capture = admitted['producer']
    owner = producer_identity({key: capture[key] for key in ('run_id', 'attempt', 'sha')})
    path = f'repos/{repository}/actions/runs/{owner["run_id"]}/attempts/{owner["attempt"]}'
    jobs = all_jobs(api, path, owner)
    admission_is_valid(admitted, api(path), jobs, repository)
    evidence = unused_owner(api, origin['producer'], repository)
    return {'schema_version': 1, 'policy': POLICY, 'repository': repository,
        'generation': origin['generation'], 'origin_sha256': digest(stable_bytes(origin)),
        'source_sha256': origin['source_sha256'], 'source_day': origin['source_day'],
        'source_admission': admitted['admission'], 'admission_producer': capture,
        'original_unused': evidence}


def record(store, origin, proof):
    bound_proof(proof, origin, proof.get('repository'))
    immutable_record(store, proof_key(store, origin), proof, kind=POLICY)
    return digest(stable_bytes(proof))


def authenticate(store, origin, repository, api, *, identity=None):
    proof = read_proof(store, origin, identity=identity)
    require(proof is not None, 'interrupted_origin_proof_missing')
    bound_proof(proof, origin, repository)
    require(prove(store, origin, repository, api) == proof, 'interrupted_origin_evidence_changed')
    return proof


def handoff_proof(store, receipt):
    identity = receipt.get('interrupted_origin_sha256')
    if identity is None:
        require('interrupted_origin_results' not in receipt, 'interrupted_handoff_proof_missing')
        return None
    origin = read_origin(store, receipt['batch']['generation'])
    require(origin is not None and receipt.get('source_origin_sha256') == digest(stable_bytes(origin))
            and receipt.get('source_admission') == origin.get('source_admission'),
            'interrupted_handoff_origin_binding_invalid')
    results = receipt.get('interrupted_origin_results')
    require(isinstance(results, dict) and set(results) == set(receipt['batch']['candidates'])
            and all(isinstance(value, str) and HEX64.fullmatch(value) for value in results.values()),
            'interrupted_handoff_result_inventory_invalid')
    return read_proof(store, origin, identity=identity)


def authenticate_handoff(store, receipt, origin, repository, api):
    from portal_extended_completion import authenticate as completed
    from portal_extended_continuation import queue
    require(handoff_proof(store, receipt) is not None, 'interrupted_handoff_proof_missing')
    proof = authenticate(store, origin, repository, api, identity=receipt['interrupted_origin_sha256'])
    for locale, candidate in receipt['batch']['candidates'].items():
        identity = receipt['interrupted_origin_results'][locale]
        raw = store._get(store.key('incremental', 'continuation-results', origin['generation'],
                                  locale, identity+'.json'), maximum=MAX_BYTES)
        row = json.loads(raw)
        require(raw == stable_bytes(row) and digest(raw) == identity, 'interrupted_handoff_result_checksum_invalid')
        snapshot = row.get('snapshot', {})
        require(row.get('status') == 'complete' and snapshot.get('candidate_id') == candidate
                and snapshot.get('checkpoint_sha256') == receipt.get('continuation_checkpoints', {}).get(locale),
                'interrupted_handoff_completion_binding_invalid')
        # Acknowledgement removes the queue row, not the exact immutable result.
        current = queue(store, locale).get(origin['generation'])
        completed(store, origin, locale, repository, api, expected_snapshot=snapshot,
                  completed_row=row if current is None else None)
    return proof
