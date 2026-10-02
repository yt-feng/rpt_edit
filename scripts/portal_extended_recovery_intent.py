"""Explicit legacy recovery intent; registration never mutates CPU continuation state.

One registration workflow owns the bounded append-only index. The serialized
ordinary source job owns adoption and separate immutable acknowledgements. A
consumer never rewrites the index, including when a concurrent intent arrives.
"""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import re

from portal_extended_continuation import (adopt_existing, candidate_evidence, checkpoint_evidence,
    producer_identity, queue, read_origin, record_result, register, validate_existing)
from portal_extended_daily_queue import immutable_record, write_verified
from portal_extended_locales import ExpansionError, daily_corpus_day, digest, file_for_url, select_locales, stable_bytes, validate_corpus
from portal_extended_r2 import DEFAULT_PREFIX, HEX64, MAX_SOURCE_BYTES, MAX_CANDIDATE_MANIFEST_BYTES, MAX_CANDIDATE_PAGE_BYTES, R2NotFound, R2Store

POLICY = 'explicit-legacy-recovery-intent-v1'
MAX_INTENTS = 64
MAX_RECORD_BYTES = 65536
WORKFLOW = '.github/workflows/portal-extended-recovery-intent.yml'


def key(store, *parts):
    return store.key('incremental', 'legacy-recovery-intents', *parts)


def read_index(store):
    try:
        value = json.loads(store._get(key(store, 'index.json'), maximum=MAX_RECORD_BYTES))
    except R2NotFound:
        return []
    if (not isinstance(value, dict) or set(value) != {'schema_version', 'policy', 'entries'}
        or type(value['schema_version']) is not int or value['schema_version'] != 1 or value['policy'] != POLICY
        or not isinstance(value['entries'], list) or len(value['entries']) > MAX_INTENTS):
        raise ExpansionError('Invalid explicit recovery intent index')
    seen, generations = set(), set()
    for row in value['entries']:
        if (not isinstance(row, dict) or set(row) != {'intent', 'generation'}
            or any(not isinstance(v, str) or not HEX64.fullmatch(v) for v in row.values())
            or row['intent'] in seen or row['generation'] in generations):
            raise ExpansionError('Duplicate or invalid recovery intent identity')
        seen.add(row['intent']); generations.add(row['generation'])
    return value['entries']


def checked_receipt(value):
    if (not isinstance(value, dict)
        or set(value) != {'schema_version', 'policy', 'repository', 'generation', 'source_sha256', 'evidence'}
        or type(value['schema_version']) is not int or value['schema_version'] != 1 or value['policy'] != POLICY
        or not isinstance(value['repository'], str)
        or not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', value['repository'])
        or any(not isinstance(value[k], str) or not HEX64.fullmatch(value[k]) for k in ('generation', 'source_sha256'))):
        raise ExpansionError('Invalid explicit recovery intent receipt')
    evidence = value['evidence']
    if not isinstance(evidence, dict) or set(evidence) != {'producer', 'locales'}:
        raise ExpansionError('Invalid recovery intent evidence')
    producer_identity(evidence['producer'])
    proofs = evidence['locales']
    if not isinstance(proofs, dict) or not proofs or set(select_locales(','.join(proofs))) != set(proofs):
        raise ExpansionError('Invalid recovery intent locales')
    for proof in proofs.values():
        if (not isinstance(proof, dict) or set(proof) != {'checkpoint_sha256', 'candidate_id', 'manifest_sha256'}
            or any(not isinstance(v, str) or not HEX64.fullmatch(v) for v in proof.values())):
            raise ExpansionError('Invalid exact recovery intent proof')
    return value


def read_receipt(store, entry):
    raw = store._get(key(store, entry['intent'], 'receipt.json'), maximum=MAX_RECORD_BYTES)
    value = checked_receipt(json.loads(raw))
    if digest(raw) != entry['intent'] or value['generation'] != entry['generation'] or raw != stable_bytes(value):
        raise ExpansionError('Recovery intent receipt differs from exact index identity')
    return value


def source(store, value):
    raw = store._get(store.source_key(value['generation']), maximum=MAX_SOURCE_BYTES)
    corpus = json.loads(raw)
    docs = validate_corpus(corpus)
    if (digest(raw) != value['source_sha256'] or corpus['documents_sha256'] != value['generation']
        or not daily_corpus_day(corpus) or not 1 <= len(docs) <= 24):
        raise ExpansionError('Recovery intent source differs from frozen corpus')
    return corpus


def validate_frozen_evidence(store, corpus, locales, evidence, repository, api):
    validate_existing(store, corpus, locales, evidence, repository, api)
    # A manifest alone does not prove its already completed private files still
    # exist. Read their bounded bytes and exact source descriptors as well.
    generation = corpus['documents_sha256']
    documents = {doc['url']: doc for doc in corpus['documents']}
    for locale, proof in evidence['locales'].items():
        raw = store._get(store.candidate_manifest_key(locale, generation, proof['candidate_id']),
                         maximum=MAX_CANDIDATE_MANIFEST_BYTES)
        if digest(raw) != proof['manifest_sha256']:
            raise ExpansionError('Recovery intent candidate manifest changed during verification')
        for row in json.loads(raw)['pages']:
            doc = documents[row['source_url']]
            if (row['path'] != (Path(locale)/file_for_url(doc['url'])).as_posix()
                or row.get('source_content_sha256') != doc['content_sha256']
                or row.get('source_html_sha256') != doc['source_html_sha256']):
                raise ExpansionError('Recovery intent completed page source differs')
            body = store._get(store.candidate_key(locale, generation, proof['candidate_id'], row['path']),
                              maximum=MAX_CANDIDATE_PAGE_BYTES)
            if len(body) != row['bytes'] or digest(body) != row['sha256']:
                raise ExpansionError('Recovery intent completed page bytes differ')


def acknowledged(store, identity):
    try:
        raw = store._get(key(store, identity, 'ack.json'), maximum=MAX_RECORD_BYTES)
    except R2NotFound:
        return False
    if raw != stable_bytes({'schema_version': 1, 'policy': POLICY, 'intent': identity, 'status': 'adopted'}):
        raise ExpansionError('Invalid immutable recovery intent acknowledgement')
    return True


def register_intent(store, generation, evidence, repository, api):
    """Only the independent registration workflow writes this index."""
    if not isinstance(generation, str) or not HEX64.fullmatch(generation):
        raise ExpansionError('Invalid recovery intent generation')
    raw = store._get(store.source_key(generation), maximum=MAX_SOURCE_BYTES)
    value = checked_receipt({'schema_version': 1, 'policy': POLICY, 'repository': repository,
        'generation': generation, 'source_sha256': digest(raw), 'evidence': evidence})
    identity = digest(stable_bytes(value))
    entries = read_index(store)
    matches = [row for row in entries if row['generation'] == generation]
    if matches:
        if matches != [{'generation': generation, 'intent': identity}] or read_receipt(store, matches[0]) != value:
            raise ExpansionError('Generation already has a different immutable recovery intent')
        # Idempotent retries do not inspect a later mutable manifest or reset work.
        return identity
    if len(entries) >= MAX_INTENTS:
        raise ExpansionError('Explicit recovery intent index is full; no entries were discarded')
    if read_origin(store, generation) is not None:
        raise ExpansionError('Already registered generation cannot become a legacy recovery intent')
    corpus = source(store, value)
    locales = tuple(evidence['locales'])
    if any(generation in queue(store, locale) for locale in locales):
        raise ExpansionError('Legacy recovery generation already has continuation state')
    validate_frozen_evidence(store, corpus, locales, evidence, repository, api)
    immutable_record(store, key(store, identity, 'receipt.json'), value, kind='legacy-recovery-intent')
    # Write receipt first. A crash here leaves an inert orphan that retry can
    # safely index. All registration jobs share one concurrency group.
    entries.append({'generation': generation, 'intent': identity})
    write_verified(store, key(store, 'index.json'), {'schema_version': 1, 'policy': POLICY, 'entries': entries},
                   kind='legacy-recovery-intent-index')
    return identity


def resume_adoption(store, value, corpus):
    """Repair only this intent's interrupted zero-claim adoption, never replay."""
    generation, evidence = value['generation'], value['evidence']
    origin = read_origin(store, generation)
    locales, producer = tuple(evidence['locales']), producer_identity(evidence['producer'])
    if (origin['producer'] != producer or origin['source_sha256'] != value['source_sha256']
        or set(origin['locales']) != set(locales)):
        raise ExpansionError('Interrupted intent adoption differs from original source owner')
    # Check every locale before repairing a single missing write. Workers never
    # start until consume_one has persisted the acknowledgement.
    started = []
    for locale, proof in evidence['locales'].items():
        row = queue(store, locale).get(generation)
        if row is None or row == {'status': 'started', 'continuations': 0, 'owner': producer}:
            started.append(locale)
            continue
        manifest, manifest_sha = candidate_evidence(store, locale, generation, proof['candidate_id'], proof['manifest_sha256'])
        snapshot = {**proof, 'manifest_sha256': manifest_sha, 'completed_pages': manifest['completed_page_count'],
            'resolved_units': len(checkpoint_evidence(store, locale, generation, proof['checkpoint_sha256']))}
        if row != {'status': 'incomplete', 'continuations': 0, 'snapshot': snapshot}:
            raise ExpansionError('Recovery intent cannot reset an advanced or changed continuation')
    register(store, corpus, locales, producer)
    for locale in started:
        proof = evidence['locales'][locale]
        record_result(store, locale, corpus, proof, checkpoint_sha=proof['checkpoint_sha256'], owner=producer)


def consume_one(store, requested, repository, api):
    """Called only by ordinary prepare while the existing pipeline lock is held."""
    requested = set(select_locales(','.join(requested)))
    # Snapshot only. A registration appended after this read remains for the
    # next source job; this function never overwrites or removes index entries.
    for entry in read_index(store):
        value = read_receipt(store, entry)
        if value['repository'] != repository:
            raise ExpansionError('Recovery intent belongs to a different repository')
        if acknowledged(store, entry['intent']) or not set(value['evidence']['locales']) <= requested:
            continue
        corpus = source(store, value)
        locales = tuple(value['evidence']['locales'])
        validate_frozen_evidence(store, corpus, locales, value['evidence'], repository, api)
        identity = entry['intent']
        stage = {'schema_version': 1, 'policy': POLICY, 'intent': identity, 'status': 'adopting'}
        stage_key = key(store, identity, 'adopting.json')
        origin = read_origin(store, entry['generation'])
        if origin is not None:
            # Mere origin existence is not evidence of an interrupted adoption.
            if store._get(stage_key, maximum=MAX_RECORD_BYTES) != stable_bytes(stage):
                raise ExpansionError('Missing exact recovery intent adoption marker')
            resume_adoption(store, value, corpus)
        else:
            if any(entry['generation'] in queue(store, locale) for locale in locales):
                raise ExpansionError('Recovery intent found unowned continuation state')
            immutable_record(store, stage_key, stage, kind='legacy-recovery-intent-adopting')
            adopt_existing(store, corpus, locales, value['evidence'], repository, api)
        immutable_record(store, key(store, identity, 'ack.json'),
            {'schema_version': 1, 'policy': POLICY, 'intent': identity, 'status': 'adopted'},
            kind='legacy-recovery-intent-ack')
        return identity
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--generation', required=True)
    parser.add_argument('--evidence', required=True)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    if (os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REF') != 'refs/heads/main'
        or os.environ.get('GITHUB_EVENT_NAME') != 'workflow_dispatch'
        or os.environ.get('KC_PUBLIC_REPOSITORY') != 'true'
        or os.environ.get('GITHUB_WORKFLOW_REF') != os.environ.get('GITHUB_REPOSITORY', '')+'/'+WORKFLOW+'@refs/heads/main'):
        raise ExpansionError('Explicit intent registration requires reviewed main public dispatch')
    from review_portal_extended_handoff import api
    identity = register_intent(R2Store.from_env(DEFAULT_PREFIX), args.generation,
        json.loads(args.evidence), os.environ['GITHUB_REPOSITORY'], api)
    # Public Actions output deliberately contains no private source identifiers.
    summary = {'schema_version': 1, 'intent': identity, 'generation': args.generation,
        'status': 'registered', 'paid_provider_requests': 0, 'translation_calls': 0}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(stable_bytes(summary))
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except Exception:
        # Never expose private source text, R2 paths or arbitrary exception data.
        print(json.dumps({'status': 'rejected', 'code': 'legacy-intent-validation-failed'}))
        raise SystemExit(1) from None
