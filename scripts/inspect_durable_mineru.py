"""Read exact accepted task metadata without submitting or changing task state."""
from __future__ import annotations
from collections import Counter
import json
import os
from pathlib import Path
import re

from inspect_legacy_mineru import canonical, inspect_batches, sha256
from mineru_task_ledger import Ledger, R2Store, token_fingerprint, validate_scope
from persist_legacy_mineru_inspection import persist, single_attempt_store


def validate_request(value):
    if not isinstance(value, dict) or set(value) != {'run_id', 'scope', 'batches'}:
        raise ValueError('request_shape')
    validate_scope(value['scope'])
    if not isinstance(value['run_id'], str) or not re.fullmatch(r'[1-9][0-9]{0,19}', value['run_id']):
        raise ValueError('run_identity')
    batches = value['batches']
    if not isinstance(batches, list) or not 1 <= len(batches) <= 40:
        raise ValueError('batch_count')
    seen = set()
    for row in batches:
        if (not isinstance(row, dict) or set(row) != {'key', 'job_id'}
                or not isinstance(row['key'], str) or not re.fullmatch(r'batches/[a-f0-9]{32}', row['key'])
                or row['key'] in seen or not isinstance(row['job_id'], str)
                or not re.fullmatch(r'[1-9][0-9]{0,19}', row['job_id'])):
            raise ValueError('batch_identity')
        seen.add(row['key'])
    return value


def error_category(row):
    text = str(row.get('err_msg') or row.get('error') or '').lower()
    patterns = [
        ('page_limit', r'page.{0,40}(limit|exceed)|页.{0,20}(限制|超过)'),
        ('quota', r'quota|balance|credit|额度|余额|配额'),
        ('encrypted_pdf', r'encrypt|password|加密|密码'),
        ('unsupported_file', r'unsupported|invalid.{0,20}(pdf|file)|不支持|无效'),
        ('file_download', r'download|下载'),
        ('file_upload', r'upload|上传'),
        ('empty_file', r'empty|空文件'),
        ('provider_timeout', r'timeout|timed out|超时'),
        ('provider_internal', r'internal|unexpected|解析失败|服务异常'),
    ]
    return next((name for name, pattern in patterns if re.search(pattern, text)), 'other_provider_failure')


def inspect(value, store, credentials, *, getter=None):
    validate_request(value)
    tokens = [(slot, token) for slot, token in credentials.items() if token]
    slots = {token_fingerprint(token): slot for slot, token in tokens}
    requests = []
    bindings = []
    # Validate every stored binding before any provider request.
    for item in value['batches']:
        raw, _ = store.get(item['key'])
        if not isinstance(raw, dict):
            raise ValueError('missing_task')
        ledger = Ledger(store, None, value['scope'], 'https://mineru.net', raw.get('options'), tokens)
        batch, _ = ledger._read_batch(item['key'])
        if batch.get('state') not in {'accepted', 'uploaded', 'terminal'}:
            raise ValueError('unaccepted_task')
        requests.append({'run_id': value['run_id'], 'job_id': item['job_id'],
                         'batch_id': batch['batch_id'], 'credential_slot': slots[batch['token_identity']],
                         'expected_data_ids': [row['id'] for row in batch['files']]})
        bindings.append({'key': item['key'], 'binding_sha256': sha256(canonical(batch))})
    kwargs = {} if getter is None else {'getter': getter}
    public, private = inspect_batches({'schema_version': 1, 'batches': requests}, credentials, **kwargs)
    categories = Counter(); hashes = Counter()
    for original in private['batches']:
        rows = original.get('provider_response', {}).get('data', {}).get('extract_result', [])
        if not isinstance(rows, list):
            continue
        for row in rows:
            if isinstance(row, dict) and row.get('state') == 'failed':
                categories[error_category(row)] += 1
                hashes[sha256(canonical({k: row.get(k) for k in ('err_msg', 'error', 'err_code')}))] += 1
    diagnostics = {'failure_categories': dict(categories), 'failure_message_hashes': dict(hashes),
                   'verified_task_bindings': bindings, 'canonical_ledger_writes': 0}
    return public, private, diagnostics


def main():
    expected = os.environ.get('GITHUB_REPOSITORY', '') + '/.github/workflows/mineru-durable-inspect.yml@refs/heads/main'
    if (os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REF') != 'refs/heads/main'
            or os.environ.get('GITHUB_EVENT_NAME') != 'workflow_dispatch'
            or os.environ.get('GITHUB_WORKFLOW_REF') != expected):
        raise SystemExit('Reviewed main cloud workflow required')
    stage = 'input'
    try:
        raw = os.environ.get('INSPECTION_REQUEST', '')
        if len(raw.encode()) > 16384:
            raise ValueError('input_size')
        value = validate_request(json.loads(raw))
        private_store = single_attempt_store()
        store = R2Store(value['scope'], client=private_store.client, bucket=private_store.bucket)
        credentials = {slot: os.environ.get(slot, '').strip() for slot in ('MINER_U', 'MINER_U_2', 'MINER_U_3', 'MINER_U_4')}
        stage = 'inspection'
        public, private, diagnostics = inspect(value, store, credentials)
        if public['network_stop']:
            print(json.dumps({'status': 'network_stop', 'provider_gets': public['provider_gets']}))
            return 2
        stage = 'private_receipt'
        public.update(persist(private_store, public, private,
                      {'run_id': os.environ['GITHUB_RUN_ID'], 'attempt': os.environ['GITHUB_RUN_ATTEMPT'],
                       'sha': os.environ['GITHUB_SHA']}))
        public.update(diagnostics)
        Path(os.environ['RUNNER_TEMP'], 'mineru-durable-summary.json').write_text(json.dumps(public, sort_keys=True)+'\n')
        print(json.dumps(public, sort_keys=True))
        return 0
    except Exception as error:
        print(json.dumps({'status': 'inspection_failed', 'stage': stage, 'exception_class': type(error).__name__}))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
