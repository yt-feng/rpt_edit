#!/usr/bin/env python3
"""Private R2 conditional-write canary; synthetic bytes only, no provider calls.

Keep exact tiny objects and a cleanup manifest for review. This tool never lists
or deletes private objects and accepts no custom key, prefix, bucket or payload.
"""
from __future__ import annotations
import argparse
from contextlib import redirect_stderr, redirect_stdout
import json
import os
from pathlib import Path
import re

from mineru_task_ledger import R2Store, digest, encoded

NAMESPACE = '_workflow-smoke/mineru-cas/v1'
VALUE_KEY = 'batches/' + digest(b'public synthetic CAS value')[:32]
MARKER_KEY = 'sources/' + digest(b'public synthetic CAS retention marker')


def identity():
    values = [os.environ.get('GITHUB_RUN_ID', ''), os.environ.get('GITHUB_RUN_ATTEMPT', '')]
    if not all(re.fullmatch(r'[1-9][0-9]{0,19}', value) for value in values):
        raise ValueError('Canary requires numeric Actions run identity')
    return values


def expected_precondition_failure(client, bucket, key, value, **condition):
    try:
        client.put_object(Bucket=bucket, Key=key, Body=encoded(value),
                          ContentType='application/json', Metadata={'sha256': digest(encoded(value))}, **condition)
    except Exception as error:
        response = getattr(error, 'response', {})
        if response.get('ResponseMetadata', {}).get('HTTPStatusCode') == 412:
            return
        raise RuntimeError('Conditional operation did not return expected HTTP 412') from None
    raise RuntimeError('Conditional operation incorrectly permitted overwrite')


def canary(store, run_id, attempt):
    # The production store implementation performs exact digest/size/ETag readback.
    store.prefix = f'{NAMESPACE}/{run_id}/{attempt}/'
    marker = {'schema': 1, 'synthetic_only': True, 'run_id': run_id, 'run_attempt': attempt,
              'object_keys': [VALUE_KEY, MARKER_KEY], 'cleanup_mode': 'read_only_retained_for_review',
              'deletes_performed': 0, 'complete': False}
    marker_version = store.put(MARKER_KEY, marker)
    first = {'schema': 1, 'synthetic_only': True, 'value': 'first'}
    second = dict(first, value='second')
    old_version = store.put(VALUE_KEY, first)
    key = store.prefix + VALUE_KEY + '.json'
    expected_precondition_failure(store.client, store.bucket, key, second, IfNoneMatch='*')
    if store.get(VALUE_KEY) != (first, old_version):
        raise RuntimeError('Rejected create changed the durable object')
    new_version = store.put(VALUE_KEY, second, old_version)
    if new_version == old_version:
        raise RuntimeError('Changed value did not change its ETag')
    expected_precondition_failure(store.client, store.bucket, key, first, IfMatch=old_version)
    if store.get(VALUE_KEY) != (second, new_version):
        raise RuntimeError('Rejected stale update changed the durable object')
    marker.update(complete=True, retained_value_sha256=digest(encoded(second)))
    store.put(MARKER_KEY, marker, marker_version)
    return {'conditional_create_412': True, 'stale_update_412': True, 'valid_cas_readback': True,
            'objects_retained': 2, 'deletes_performed': 0,
            'retention_marker_sha256': digest(encoded(marker))}


def run(diagnostics):
    result = {'schema': 1, 'success': False, 'synthetic_only': True, 'provider_posts': 0,
              'wechat_calls': 0, 'deletes_performed': 0}
    # SDK exception strings may contain private endpoint or bucket names.
    with open(os.devnull, 'w') as sink, redirect_stdout(sink), redirect_stderr(sink):
        try:
            run_id, attempt = identity()
            store = R2Store('synthetic-canary')
            result.update(canary(store, run_id, attempt), success=True)
        except Exception:
            result['failure'] = 'private_conditional_write_canary_failed_review_retained_manifest'
    diagnostics.parent.mkdir(parents=True, exist_ok=True)
    diagnostics.write_text(json.dumps(result, sort_keys=True, indent=2) + '\n')
    print('Private MinerU checkpoint canary: success=' + str(result['success']).lower())
    return 0 if result['success'] else 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--diagnostics-out', type=Path, required=True)
    raise SystemExit(run(parser.parse_args().diagnostics_out))
