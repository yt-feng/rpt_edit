"""Preserve GET-only metadata separately from source-bound MinerU admissions."""
from __future__ import annotations
import argparse
import base64
import json
import os
from pathlib import Path
import re

from inspect_legacy_mineru import MAX_BODY, canonical, classify_response, sha256, validate_request

PREFIX = '_workflow-cache/mineru-legacy-inspections/v1'
MAX_OBJECT = 3 * 1024 * 1024


def single_attempt_store():
    """This inspection never inherits the publishing client's retry policy."""
    import boto3
    from botocore.config import Config
    from portal_extended_r2 import R2Store, require_env
    client = boto3.client('s3',
        endpoint_url=f"https://{require_env('R2_ACCOUNT_ID')}.r2.cloudflarestorage.com",
        aws_access_key_id=require_env('R2_ACCESS_KEY_ID'),
        aws_secret_access_key=require_env('R2_SECRET_ACCESS_KEY'), region_name='auto',
        config=Config(retries={'total_max_attempts': 1, 'mode': 'standard'},
                      connect_timeout=10, read_timeout=30))
    return R2Store(client, require_env('R2_BUCKET'), PREFIX)


def persist(store, public, private, producer):
    request = validate_request(private['input'])
    request_hash = sha256(canonical(request))
    if (type(public.get('schema_version')) is not int or public['schema_version'] != 1
        or type(private.get('schema_version')) is not int or private['schema_version'] != 1
        or public.get('network_stop') is not False
        or any(type(public.get(field)) is not int or public[field] != 0
               for field in ('provider_posts', 'new_submissions', 'paid_requests'))
        or public.get('input_canonical_sha256') != request_hash
        or private.get('input_canonical_sha256') != request_hash):
        raise ValueError('Legacy inspection receipt differs from GET-only request')
    if (set(producer) != {'run_id', 'attempt', 'sha'}
        or any(not re.fullmatch(r'[1-9][0-9]{0,19}', str(producer[k])) for k in ('run_id', 'attempt'))
        or not isinstance(producer['sha'], str) or not re.fullmatch(r'[a-f0-9]{40}', producer['sha'])):
        raise ValueError('Legacy inspection producer identity is invalid')
    requested = {row['batch_id']: row for row in request['batches']}
    public_rows = {row['batch_id']: row for row in public['batches']}
    if len(public_rows) != len(public['batches']) or set(public_rows) != set(requested):
        raise ValueError('Legacy inspection public membership differs')
    for identity, row in public_rows.items():
        if row.get('response_sha256'):
            continue
        category = row.get('category')
        expected = {key: requested[identity][key] for key in ('run_id', 'job_id', 'batch_id')}
        expected.update(identified_complete=False, all_succeeded=False, membership_proven=False,
                        original_source_bytes_proven=False, historical_token_fingerprint_proven=False,
                        category=category)
        if category not in {'credential_unavailable', 'response_size'} or row != expected:
            raise ValueError('Legacy inspection absent response has an unsupported claim')
    expected_gets = len(requested) - sum(row['category'] == 'credential_unavailable' for row in public_rows.values())
    if (type(public.get('provider_gets')) is not int or public['provider_gets'] != expected_gets
        or type(public.get('uninspected_count')) is not int or public['uninspected_count'] != 0):
        raise ValueError('Legacy inspection GET coverage differs')
    objects = []; seen = set()
    # Verify all local receipt bytes before the first private write.
    payloads = []
    for row in private['batches']:
        batch = row['input']; identity = batch['batch_id']
        if identity in seen or batch != requested.get(identity):
            raise ValueError('Legacy inspection private membership differs')
        seen.add(identity)
        encoded = row['raw_response_base64']
        if not isinstance(encoded, str) or len(encoded) > 4 * ((MAX_BODY + 2) // 3):
            raise ValueError('Legacy inspection encoded response is too large')
        raw = base64.b64decode(encoded, validate=True)
        if len(raw) > MAX_BODY:
            raise ValueError('Legacy inspection decoded response is too large')
        if (sha256(raw) != row['response_sha256']
            or public_rows[identity].get('response_sha256') != sha256(raw)
            or row.get('input_canonical_sha256') != sha256(canonical(batch))):
            raise ValueError('Legacy inspection raw provider bytes differ')
        expected_public, _ = classify_response(row['http_status'], raw, batch)
        if public_rows[identity] != expected_public:
            raise ValueError('Legacy inspection public result differs from exact provider bytes')
        if 'provider_response' in row and json.loads(raw) != row['provider_response']:
            raise ValueError('Legacy inspection parsed provider metadata differs')
        payload = canonical(row)
        if len(payload) > MAX_OBJECT:
            raise ValueError('Legacy inspection private object is too large')
        payloads.append((identity, payload))
    if seen != {identity for identity, row in public_rows.items() if row.get('response_sha256')}:
        raise ValueError('Legacy inspection private responses are missing or extra')
    context = f"{producer['run_id']}-{producer['attempt']}"
    for identity, payload in payloads:
        checksum = sha256(payload)
        name = f'{context}/{request_hash}/{identity}-{checksum}.json'
        object_key = store.key(*name.split('/'))
        store._put(object_key, payload, metadata={'kind': 'legacy-provider-inspection'})
        if store._get(object_key, maximum=MAX_OBJECT) != payload:
            raise ValueError('Legacy inspection private object readback differs')
        objects.append({'batch_id': identity, 'object': name, 'sha256': checksum, 'bytes': len(payload)})
    receipt = {'schema_version': 1, 'policy': 'legacy-provider-inspection-only-v1',
               'producer': producer, 'input': request, 'input_canonical_sha256': request_hash,
               'objects': objects, 'original_source_bytes_proven': False,
               'historical_token_fingerprint_proven': False, 'canonical_task_admission': False}
    payload = canonical(receipt); checksum = sha256(payload)
    if len(payload) > 256 * 1024:
        raise ValueError('Legacy inspection receipt is too large')
    name = f'{context}/{request_hash}/receipt-{checksum}.json'
    object_key = store.key(*name.split('/'))
    store._put(object_key, payload, metadata={'kind': 'legacy-provider-inspection-receipt'})
    if store._get(object_key, maximum=256 * 1024) != payload:
        raise ValueError('Legacy inspection receipt readback differs')
    return {'private_receipt_sha256': checksum, 'private_metadata_objects': len(objects),
            'canonical_task_admission': False, 'source_bytes_proven': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--public-summary', type=Path, required=True)
    parser.add_argument('--private-result', type=Path, required=True)
    args = parser.parse_args()
    if (os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REF') != 'refs/heads/main'
        or os.environ.get('GITHUB_EVENT_NAME') != 'workflow_dispatch'
        or os.environ.get('GITHUB_WORKFLOW_REF') != os.environ.get('GITHUB_REPOSITORY', '')+
           '/.github/workflows/mineru-legacy-inspect.yml@refs/heads/main'):
        raise SystemExit('Legacy private receipt requires reviewed main inspection')
    public = json.loads(args.public_summary.read_bytes())
    private = json.loads(args.private_result.read_bytes())
    try:
        result = persist(single_attempt_store(), public, private,
                         {k: os.environ[v] for k, v in {'run_id': 'GITHUB_RUN_ID',
                          'attempt': 'GITHUB_RUN_ATTEMPT', 'sha': 'GITHUB_SHA'}.items()})
    except Exception:
        # A failed remote write/read is never retried or followed by publication.
        print(json.dumps({'status': 'legacy-private-receipt-stopped', 'remote_stop': True}))
        return 1
    public.update(result)
    args.public_summary.write_text(json.dumps(public, sort_keys=True)+'\n')
    print(json.dumps({'status': 'legacy-private-receipt-verified', **result}, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
