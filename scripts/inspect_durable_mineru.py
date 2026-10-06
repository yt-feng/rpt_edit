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


# Public diagnostics are a projection onto a fixed vocabulary, never a copy of
# provider text. Unknown words/numbers remain private in the existing R2 receipt.
ERROR_FIELDS = ('err_msg', 'error', 'err_code', 'error_code', 'error_message', 'message')
SAFE_ERROR_WORDS = frozenset('''a an the to of for from in on at with without and or is was were be been
not no unable cannot could failed failure error errors unknown unexpected internal server service
request response task job document file pdf zip image format invalid unsupported corrupt corrupted
malformed empty encrypted password protected page pages limit exceeded exceeds maximum too many
large size quota balance credits insufficient exhausted timeout timed out expired cancelled canceled
aborted interrupted killed memory allocation worker process processing parse parsing parser extract
extraction convert converting conversion upload uploading download downloading read reading write writing
connection connect network reset refused unavailable denied permission access authentication unauthorized
forbidden token rate retry retries attempts storage resource resources busy queue queued capacity
decode decoding encode encoding open opening close closed eof stream streams data content length
check validation validate valid missing found exists result results code status api http https
please try again later failure reason exception runtime system operating io input output execution
model backend pipeline vlm ocr cuda gpu cpu oom segmentation fault crash crashed initialization
initialize initialized init dependency dependencies version supported unprocessable'''.split())


def error_text(row):
    values = []
    for field in ERROR_FIELDS:
        value = row.get(field)
        if isinstance(value, str):
            values.append(value[:8192])
        elif isinstance(value, dict):
            # Some providers wrap their failure in {code, message, reason}.
            values.extend(item[:8192] for key in ('message', 'msg', 'reason', 'code')
                          if isinstance((item := value.get(key)), str))
    return '\n'.join(values)


def error_category(row):
    text = error_text(row).lower()
    patterns = [
        ('page_limit', r'page.{0,40}(limit|exceed)|页.{0,20}(限制|超过)'),
        ('quota', r'quota|balance|credit|额度|余额|配额'),
        ('encrypted_pdf', r'encrypt|password|加密|密码'),
        ('unsupported_file', r'unsupported|invalid.{0,20}(pdf|file)|不支持|无效'),
        ('file_download', r'download|下载'),
        ('file_upload', r'upload|上传'),
        ('empty_file', r'empty|空文件'),
        ('provider_timeout', r'timeout|timed out|超时'),
        ('provider_memory', r'out.of.memory|\boom\b|cuda|内存不足|显存'),
        ('provider_worker', r'worker|killed|segmentation|crash|进程|执行失败|任务.{0,12}失败'),
        ('document_processing', r'pars(?:e|er|ing)|extract|convert|process|解析|提取|转换|处理失败'),
        ('provider_internal', r'internal|unexpected|服务异常|系统错误'),
        ('provider_unknown', r'unknown|未知'),
    ]
    return next((name for name, pattern in patterns if re.search(pattern, text)), 'other_provider_failure')


def safe_failure_reason(row, private_terms=()):
    """Keep readable error-operation words; omit every unapproved literal."""
    text = error_text(row)
    sensitive = list(private_terms) + [row.get(key) for key in ('data_id', 'file_name', 'filename', 'name')]
    for value in sorted((value for value in sensitive if isinstance(value, str) and value), key=len, reverse=True):
        text = re.sub(re.escape(value), ' [redacted] ', text, flags=re.I)
    text = re.sub(r'https?://\S+|(?:[A-Za-z]:)?[/\\][^\s]+', ' [redacted] ', text, flags=re.I)
    text = re.sub(r'\S+\.(?:pdf|zip|png|jpe?g|json|txt)\b', ' [redacted] ', text, flags=re.I)
    words = []
    for token in re.findall(r'[A-Za-z0-9_./?&=%@+\\:-]+|[\u4e00-\u9fff]+', text):
        safe = token.lower() if token.lower() in SAFE_ERROR_WORDS else '[redacted]'
        if safe != '[redacted]' or not words or words[-1] != safe:
            words.append(safe)
    codes = []
    for field in ('err_code', 'error_code'):
        value = row.get(field)
        # A free-form identifier can be a token; only numeric/official-style
        # short codes may be copied into public diagnostics.
        if type(value) is int and abs(value) <= 999999 and str(value) not in sensitive:
            codes.append(str(value))
        elif isinstance(value, str) and re.fullmatch(r'(?:[AB][0-9]{4}|-?[0-9]{1,6})', value):
            if value not in sensitive:
                codes.append(value)
    return {'category': error_category(row), 'error_codes': sorted(set(codes)),
            'error_message_safe': ' '.join(words[:80]) if words else '[no safe message tokens]',
            'message_redacted': True,
            'error_fields_present': [key for key in ERROR_FIELDS if row.get(key) is not None],
            'failure_message_sha256': sha256(canonical({key: row.get(key) for key in ERROR_FIELDS}))}


def inspect(value, store, credentials, *, getter=None):
    validate_request(value)
    tokens = [(slot, token) for slot, token in credentials.items() if token]
    slots = {token_fingerprint(token): slot for slot, token in tokens}
    requests = []
    bindings = []
    private_terms = list(credentials.values())
    # Validate every stored binding before any provider request.
    for item in value['batches']:
        raw, _ = store.get(item['key'])
        if not isinstance(raw, dict):
            raise ValueError('missing_task')
        ledger = Ledger(store, None, value['scope'], 'https://mineru.net', raw.get('options'), tokens)
        batch, _ = ledger._read_batch(item['key'])
        private_terms.extend([batch['key'], batch.get('batch_id', '')])
        private_terms.extend(value for row in batch['files'] for value in (row['source'], row['id']))
        if batch.get('state') not in {'accepted', 'uploaded', 'terminal'}:
            raise ValueError('unaccepted_task')
        requests.append({'run_id': value['run_id'], 'job_id': item['job_id'],
                         'batch_id': batch['batch_id'], 'credential_slot': slots[batch['token_identity']],
                         'expected_data_ids': [row['id'] for row in batch['files']]})
        bindings.append({'key': item['key'], 'binding_sha256': sha256(canonical(batch))})
    kwargs = {} if getter is None else {'getter': getter}
    public, private = inspect_batches({'schema_version': 1, 'batches': requests}, credentials, **kwargs)
    categories = Counter(); hashes = Counter(); reasons = Counter()
    for original in private['batches']:
        rows = original.get('provider_response', {}).get('data', {}).get('extract_result', [])
        if not isinstance(rows, list):
            continue
        for row in rows:
            if isinstance(row, dict) and row.get('state') == 'failed':
                categories[error_category(row)] += 1
                hashes[sha256(canonical({k: row.get(k) for k in ('err_msg', 'error', 'err_code')}))] += 1
                reasons[canonical(safe_failure_reason(row, private_terms))] += 1
    diagnostics = {'failure_categories': dict(categories), 'failure_message_hashes': dict(hashes),
                   'failure_reasons': [dict(json.loads(reason), count=count)
                                       for reason, count in sorted(reasons.items())],
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
        # The full public receipt retains existing exact task bindings in its
        # artifact. Console output only carries counts and safe failure reasons.
        print(json.dumps({key: public[key] for key in (
            'provider_gets', 'provider_posts', 'new_submissions', 'paid_requests',
            'network_stop', 'uninspected_count', 'failure_categories', 'failure_reasons',
            'private_receipt_sha256', 'canonical_ledger_writes')}, sort_keys=True))
        return 0
    except Exception as error:
        print(json.dumps({'status': 'inspection_failed', 'stage': stage, 'exception_class': type(error).__name__}))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
