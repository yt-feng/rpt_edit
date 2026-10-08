"""Read exact accepted task metadata without submitting or changing task state."""
from __future__ import annotations
from collections import Counter
import json
import os
from pathlib import Path
import re

from inspect_legacy_mineru import NetworkStop, canonical, get_once, inspect_batches, sha256
from mineru_task_ledger import Ledger, LedgerError, R2Store, token_fingerprint, validate_scope
from persist_legacy_mineru_inspection import persist, single_attempt_store


def validate_request(value):
    if (not isinstance(value, dict)
            or not {'run_id', 'scope', 'batches'} <= set(value)
            or set(value) - {'run_id', 'scope', 'batches', 'include_completed_children', 'original_pdf_probe_sha256'}):
        raise ValueError('request_shape')
    if 'include_completed_children' in value and type(value['include_completed_children']) is not bool:
        raise ValueError('completed_children_flag')
    validate_scope(value['scope'])
    if 'original_pdf_probe_sha256' in value and (value['scope'] != 'institution'
            or not isinstance(value['original_pdf_probe_sha256'], str)
            or not re.fullmatch(r'[a-f0-9]{64}', value['original_pdf_probe_sha256'])):
        raise ValueError('original_probe_identity')
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


class ReadOnlyInspectionStore:
    """Reject mutation and changes to any stored proof during this inspection."""
    def __init__(self, store):
        self.store, self.snapshots = store, {}

    def get(self, key):
        value, version = self.store.get(key)
        raw = canonical(value)
        if key in self.snapshots and self.snapshots[key] != raw:
            raise LedgerError('Inspection stored binding changed')
        self.snapshots[key] = raw
        return value, version

    def put(self, *_args, **_kwargs):
        raise LedgerError('Inspection cannot write canonical task state')


class ReadOnlyInspectionProvider:
    """Reuse the original GET bytes; read accepted children at most once."""
    def __init__(self, getter, credentials, store, run_id):
        self.getter, self.credentials, self.store, self.run_id = getter, credentials, store, run_id
        self.responses, self.gets = {}, 0
        self.slots = {token_fingerprint(token): slot for slot, token in credentials.items() if token}
        self.job_id = None

    def get(self, endpoint, token, timeout):
        identity = (endpoint, token_fingerprint(token))
        if identity not in self.responses:
            self.gets += 1
            self.responses[identity] = self.getter(endpoint, token, timeout)
        return self.responses[identity]

    def poll(self, batch_id, token, _timeout):
        tasks = [json.loads(raw) for key, raw in self.store.snapshots.items() if key.startswith('batches/')]
        tasks = [row for row in tasks if isinstance(row, dict) and row.get('batch_id') == batch_id]
        if len(tasks) != 1 or tasks[0]['token_identity'] != token_fingerprint(token):
            raise LedgerError('Inspection GET differs from its accepted task binding')
        request = {'run_id': self.run_id, 'job_id': self.job_id, 'batch_id': batch_id,
                   'credential_slot': self.slots[token_fingerprint(token)],
                   'expected_data_ids': [row['id'] for row in tasks[0]['files']]}
        public, private = inspect_batches({'schema_version': 1, 'batches': [request]},
                                           self.credentials, getter=self.get)
        if public['network_stop']:
            raise NetworkStop('network_stop')
        row = public['batches'][0]
        # Missing pending rows remain pending. Unknown, duplicate, malformed or
        # URL-less completed rows cannot become an effective success.
        if (row.get('category') not in {'identified', 'membership_mismatch'}
                or any(row.get(key) != 0 for key in ('invalid_row_count', 'duplicate_member_count',
                    'unknown_member_count', 'completed_result_url_missing_count'))):
            raise LedgerError('Inspection accepted task GET response is invalid')
        return private['batches'][0]['provider_response']['data']['extract_result']

    def submit(self, *_args, **_kwargs):
        raise LedgerError('Inspection cannot submit provider tasks')

    def upload(self, *_args, **_kwargs):
        raise LedgerError('Inspection cannot upload provider files')


def inspect_completed_children(value, store, provider, tokens, roots, original_gets):
    from mineru_completed_child_reuse import read_completed_batch

    batches = []
    for item, root in zip(value['batches'], roots):
        provider.job_id = item['job_id']
        ledger = Ledger(store, provider, value['scope'], root['endpoint'], root['options'], tokens)
        effective, counts = read_completed_batch(ledger, root)
        controller_key = 'recoveries/' + root['key'].split('/')[1]
        controller = json.loads(store.snapshots[controller_key])
        children = []
        for entry in (controller or {}).get('children', []):
            raw = store.snapshots.get(entry['key'])
            if raw is not None and json.loads(raw) is not None:
                children.append({'ordinal': entry['ordinal'], 'binding_sha256': sha256(raw)})
        batches.append({**counts, 'original_binding_sha256': sha256(canonical(root)),
            'controller_binding_sha256': sha256(canonical(controller)) if controller is not None else None,
            'checked_child_bindings': children,
            'completed_lineage_counts': dict(Counter(str(row['_recovery_lineage']['child_ordinal'])
                for row in effective.values() if row['state'] == 'done'))})
    for key in list(store.snapshots):
        store.get(key)
    # The legacy private receipt still authenticates precisely the original
    # GETs. Additional reads have separate explicit counters and proof hashes.
    return {'schema_version': 1, 'source_bytes_proven': False, 'canonical_task_admission': False,
            'canonical_ledger_writes': 0, 'provider_posts': 0,
            'original_provider_gets': original_gets,
            'additional_provider_gets': provider.gets - original_gets,
            'total_provider_gets': provider.gets,
            'effective_counts': {key: sum(row[key] for row in batches)
                                 for key in ('admitted', 'completed', 'failed', 'pending', 'reused_sources')},
            'all_succeeded': all(row['all_succeeded'] for row in batches), 'batches': batches}


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


def probe_original_pdf(source_hash, roots, public, private, store, *, downloader=None):
    """Inspect at most one already completed result with strict existing GET.

    This is an inventory diagnostic, not full-source recovery authorization.
    The selected original can only be proven by exact PDF bytes in its result;
    no filenames, report text, result URLs or PDF payloads leave this function.
    """
    from consume_legacy_mineru import ConsumerError, NetworkStop as ResultNetworkStop, download_once, safe_unzip
    import tempfile
    matches = [(root, item) for root in roots for item in root['files']
               if sha256(item['source'].encode()) == source_hash]
    if len(matches) != 1:
        raise ValueError('original_probe_ambiguous')
    root, item = matches[0]
    if 'recovery_parent' in root:
        raise ValueError('original_probe_requires_root')
    report = {'source_name_sha256': source_hash, 'source_binding_sha256': item['id'],
              'source_pdf_sha256': item['sha256'], 'source_pdf_bytes': item['size'],
              'original_members': sum(len(row['files']) for row in roots),
              'source_bytes_proven': False, 'selected_original_bytes_proven': False,
              'result_gets': 0, 'provider_posts': 0, 'canonical_ledger_writes': 0}
    # Do not inspect a result while any requested root has incomplete or
    # mismatched current membership, even if the selected row says done.
    if public['network_stop'] or not all(row.get('identified_complete') is True for row in public['batches']):
        return dict(report, status='original_membership_incomplete')
    batches = [row for row in private['batches'] if row['input']['batch_id'] == root['batch_id']]
    if len(batches) != 1:
        raise ValueError('original_probe_response')
    rows = batches[0]['provider_response']['data']['extract_result']
    selected = [row for row in rows if row['data_id'] == item['id']]
    if len(selected) != 1:
        raise ValueError('original_probe_member')
    row = selected[0]
    report['selected_state'] = row['state']
    if row['state'] != 'done':
        return dict(report, status='original_result_unavailable')
    # Check every source claim of the selected full original root before GET.
    for member in root['files']:
        claim, _ = store.get('sources/'+member['id'])
        if (not isinstance(claim, dict) or claim.get('schema') != 1
                or canonical(claim.get('binding')) != canonical(member) or claim.get('batch_key') != root['key']):
            raise ValueError('original_probe_source_claim')
    for key in list(store.snapshots):
        store.get(key)
    try:
        report['result_gets'] = 1
        raw = (downloader or download_once)(row['full_zip_url'])
        with tempfile.TemporaryDirectory(prefix='institution-original-probe-') as temporary:
            directory = Path(temporary)/'result'
            safe_unzip(raw, directory)
            pdfs = [path for path in directory.rglob('*') if path.is_file() and path.suffix.lower() == '.pdf']
            matched = 0
            for path in pdfs:
                if path.stat().st_size == item['size']:
                    payload = path.read_bytes()
                    matched += int(payload.startswith(b'%PDF-') and sha256(payload) == item['sha256'])
            report.update(result_zip_sha256=sha256(raw), result_zip_bytes=len(raw),
                          pdf_member_count=len(pdfs), matching_original_pdf_count=matched,
                          selected_original_bytes_proven=matched > 0, status='result_inventory_verified')
    except ConsumerError as error:
        report.update(status='result_inventory_stopped', category=str(error),
                      network_stop=isinstance(error, ResultNetworkStop))
        if getattr(error, 'http_status', None): report['http_status'] = error.http_status
        return report
    for key in list(store.snapshots):
        store.get(key)
    return report


def inspect(value, store, credentials, *, getter=None, result_downloader=None):
    validate_request(value)
    include_children = value.get('include_completed_children', False)
    provider = None
    if include_children or 'original_pdf_probe_sha256' in value:
        store = ReadOnlyInspectionStore(store)
    if include_children:
        provider = ReadOnlyInspectionProvider(getter or get_once, credentials, store, value['run_id'])
        getter = provider.get
    tokens = [(slot, token) for slot, token in credentials.items() if token]
    slots = {token_fingerprint(token): slot for slot, token in tokens}
    requests = []
    bindings = []
    roots = []
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
        roots.append(batch)
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
    if include_children and not public['network_stop']:
        diagnostics['completed_child_inspection'] = inspect_completed_children(
            value, store, provider, tokens, roots, public['provider_gets'])
    if 'original_pdf_probe_sha256' in value:
        diagnostics['original_pdf_probe'] = probe_original_pdf(value['original_pdf_probe_sha256'],
            roots, public, private, store, downloader=result_downloader)
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
        if diagnostics.get('original_pdf_probe', {}).get('status') == 'result_inventory_stopped':
            # A failed result GET ends remote work, including receipt writes.
            report = {'provider_gets': public['provider_gets'], 'provider_posts': 0,
                      'original_pdf_probe': diagnostics['original_pdf_probe']}
            Path(os.environ['RUNNER_TEMP'], 'mineru-durable-summary.json').write_text(json.dumps(report)+'\n')
            print(json.dumps(report))
            return 2
        stage = 'private_receipt'
        public.update(persist(private_store, public, private,
                      {'run_id': os.environ['GITHUB_RUN_ID'], 'attempt': os.environ['GITHUB_RUN_ATTEMPT'],
                       'sha': os.environ['GITHUB_SHA']}))
        public.update(diagnostics)
        Path(os.environ['RUNNER_TEMP'], 'mineru-durable-summary.json').write_text(json.dumps(public, sort_keys=True)+'\n')
        # The full public receipt retains existing exact task bindings in its
        # artifact. Console output only carries counts and safe failure reasons.
        console = {key: public[key] for key in (
            'provider_gets', 'provider_posts', 'new_submissions', 'paid_requests',
            'network_stop', 'uninspected_count', 'failure_categories', 'failure_reasons',
            'private_receipt_sha256', 'canonical_ledger_writes')}
        if 'completed_child_inspection' in diagnostics:
            console['completed_child_inspection'] = {key: item for key, item in
                diagnostics['completed_child_inspection'].items() if key != 'batches'}
        if 'original_pdf_probe' in diagnostics:
            console['original_pdf_probe'] = diagnostics['original_pdf_probe']
        print(json.dumps(console, sort_keys=True))
        return 0
    except Exception as error:
        print(json.dumps({'status': 'inspection_failed', 'stage': stage, 'exception_class': type(error).__name__}))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
