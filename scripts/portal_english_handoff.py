"""Hand real complete editorial candidates to the protected site publisher."""
from __future__ import annotations
import json
import os
from pathlib import Path
import subprocess
import tempfile

import requests
from portal_english_commentary import PREFIX, POLICY, exact, require
from portal_english_pipeline import (batch_admission, checked_cpu_producer, hash_value,
                                    put_verified, read_ready_queue, restore_candidate)
from portal_english_publication import checked_batches, read_active
from portal_extended_locales import ORIGIN, digest, stable_bytes
from portal_extended_r2 import DEFAULT_PREFIX, R2Store


def save_handoff(store, row, ready, manifest):
    checked_batches([row]); checked_cpu_producer(ready['producer'])
    require(ready['generation'] == row['generation'] and ready['candidate_id'] == row['candidate_id'])
    value = {'schema_version': 1, 'policy': POLICY, 'batch': row,
             'producer': ready['producer'], 'source_admission': ready['admission'],
             'day': manifest['day'], 'page_count': manifest['completed_page_count']}
    identity = digest(stable_bytes(value))
    put_verified(store, store.key('publication-handoffs', identity, 'receipt.json'), value,
                 'english-publication-handoff', immutable=True)
    return identity


def read_handoff(store, identity):
    hash_value(identity)
    raw = store._get(store.key('publication-handoffs', identity, 'receipt.json'), maximum=65536)
    require(digest(raw) == identity, 'English handoff checksum differs')
    value = json.loads(raw)
    exact(value, ['schema_version', 'policy', 'batch', 'producer', 'source_admission', 'day', 'page_count'])
    require(value['schema_version'] == 1 and value['policy'] == POLICY)
    checked_batches([value['batch']]); checked_cpu_producer(value['producer']); hash_value(value['source_admission'])
    require(type(value['page_count']) is int and 1 <= value['page_count'] <= 24)
    return value


def verify_handoff(store, original, identity, workspace):
    value = read_handoff(store, identity); row = value['batch']
    ready, manifest, source = restore_candidate(store, original, row['generation'], row['candidate_id'], workspace)
    require(ready['producer'] == value['producer'] and ready['admission'] == value['source_admission']
            and source['day'] == value['day'] and manifest['completed_page_count'] == value['page_count'],
            'English handoff source/producer/page count differs')
    _, admission, _ = batch_admission(store, original, row['generation'])
    return value, admission


def next_ready(store, original, active, workspace):
    published = active['batches'] if active else []
    for index, queued in enumerate(sorted(read_ready_queue(store), key=lambda row: (row['day'], row['generation']), reverse=True)):
        row = {key: queued[key] for key in ('generation', 'candidate_id')}
        if row in published: continue
        ready, manifest, source = restore_candidate(store, original, row['generation'], row['candidate_id'], workspace/str(index))
        require(source['day'] == queued['day'], 'English ready queue source day differs')
        return save_handoff(store, row, ready, manifest)
    return None


def main():
    require(os.environ.get('GITHUB_ACTIONS') == 'true' and os.environ.get('GITHUB_REF') == 'refs/heads/main'
            and os.environ.get('KC_PUBLIC_REPOSITORY') == 'true', 'English automatic handoff requires reviewed main public Actions')
    require(os.environ.get('KC_ENGLISH_AUTO_PUBLISH') == 'true', 'English automatic publication is not enabled')
    store = R2Store.from_env(PREFIX); original = R2Store(store.client, store.bucket, DEFAULT_PREFIX)
    with requests.Session() as session:
        response = session.get(ORIGIN+'/.well-known/edge-state', timeout=(10, 30), allow_redirects=False)
        require(response.status_code == 200 and len(response.content) <= 65536, 'Live version cannot be pinned for English handoff')
        active = read_active(store, response.json())
    with tempfile.TemporaryDirectory(prefix='english-handoff-') as temporary:
        identity = next_ready(store, original, active, Path(temporary))
    if identity is None:
        print(json.dumps({'dispatched': False, 'reason': 'No new complete KC commentary candidates'})); return
    subprocess.run(['gh', 'workflow', 'run', 'neutral-edge-cutover.yml', '--repo', os.environ['GITHUB_REPOSITORY'],
                    '--ref', 'main', '-f', 'operation=migrate', '-f', 'translation_scope=incremental',
                    '-f', 'english_handoff='+identity], check=True)
    print(json.dumps({'dispatched': True, 'handoff': identity, 'deployed': False}))


if __name__ == '__main__': main()
