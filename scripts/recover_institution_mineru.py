"""Recover accepted institution tasks only after complete original-byte proof.

Official URLs are discovered from authenticated producer logs and the existing
public archive. They never authorize a replacement source: every byte must match
its original durable source claim before any task can be retried.
"""
from __future__ import annotations
import json
import os
from pathlib import Path
import re
import subprocess
from urllib.parse import urljoin, urlsplit

from mineru_task_ledger import FAILED, Ledger, LedgerError, Provider, R2Store, digest, encoded, exact_json
from mineru_terminal_recovery import TerminalRecovery, failure_hash, task_identity
from mineru_completed_child_reuse import _read_once
from inspect_durable_mineru import failure_message_hash
from persist_legacy_mineru_inspection import single_attempt_store
from smoke_mineru_api import NoRedirectHTTP, credentials
from fetch_institution_latest_pdfs import source_request_headers

WORKFLOW = '.github/workflows/institution-mineru-recovery.yml'
PRODUCER = '.github/workflows/institution-latest-pdf-to-wechat.yml'
DOMAINS = {'imf.org', 'worldbank.org', 'bis.org', 'oecd.org', 'adb.org', 'weforum.org', 'unctad.org', 'wto.org', 'bruegel.org'}
MAX_PDF = 64 * 1024 * 1024
MAX_TOTAL = 512 * 1024 * 1024
MAX_SOURCE_URLS = 4


class SourceHTTPError(ValueError):
    def __init__(self, status):
        super().__init__('source_http_status')
        self.status = status


def require(condition, code):
    if not condition: raise ValueError(code)


def request(value):
    require(isinstance(value, dict) and set(value) == {'source_runs', 'batches', 'allowed_error_hashes'}, 'request_shape')
    for key, maximum, pattern in [('source_runs', 6, r'[1-9][0-9]{0,19}'),
                                 ('batches', 40, r'batches/[a-f0-9]{32}'),
                                 ('allowed_error_hashes', 10, r'[a-f0-9]{64}')]:
        rows = value[key]
        require(isinstance(rows, list) and 1 <= len(rows) <= maximum
                and all(isinstance(row, str) and re.fullmatch(pattern, row) for row in rows)
                and len(set(rows)) == len(rows), 'request_'+key)
    return value


def official_url(url):
    parts = urlsplit(url)
    host = parts.hostname or ''
    require(parts.scheme == 'https' and not parts.username and not parts.password and parts.port in {None, 443}
            and not parts.fragment and any(host == domain or host.endswith('.'+domain) for domain in DOMAINS), 'source_url')
    return url


def producer(value, run_id, repository):
    require(isinstance(value, dict) and value.get('id') == int(run_id) and value.get('path') == PRODUCER
            and value.get('head_branch') == 'main' and value.get('event') in {'schedule', 'workflow_dispatch'}
            and value.get('repository', {}).get('full_name') == repository
            and value.get('head_repository', {}).get('full_name') == repository
            and value.get('status') == 'completed' and re.fullmatch(r'[a-f0-9]{40}', value.get('head_sha', '')), 'source_producer')


def log_urls(raw, wanted=None):
    require(len(raw.encode()) <= 8*1024*1024, 'source_log_size')
    result = {}
    for name, url in re.findall(r' saved ([^/\\\r\n]+\.pdf) \([0-9]+ KB\) <- (https://[^\s]+)', raw):
        if wanted is None or name in wanted:
            official_url(url); result.setdefault(name, set()).add(url)
    return result


def gh(*args):
    result = subprocess.run(['gh', *args], capture_output=True, text=True, timeout=120)
    require(result.returncode == 0, 'github_read_failed')
    require(len(result.stdout.encode()) <= 8*1024*1024, 'github_response_size')
    return result.stdout


def registry(value, repository, wanted):
    urls = {}
    for run_id in value['source_runs']:
        metadata = json.loads(gh('api', f'repos/{repository}/actions/runs/{run_id}'))
        producer(metadata, run_id, repository)
        for name, values in log_urls(gh('run', 'view', run_id, '--repo', repository, '--log'), wanted).items():
            urls.setdefault(name, set()).update(values)
    archive = Path('institution_feeds/institution_pdf_archive.jsonl')
    require(archive.is_file() and archive.stat().st_size <= 16*1024*1024, 'archive_size')
    for line in archive.read_text().splitlines():
        row = json.loads(line); name, url = row.get('local_filename'), row.get('pdf_url')
        if name in wanted and isinstance(url, str):
            official_url(url); urls.setdefault(name, set()).add(url)
    return urls


def download(url, expected_size):
    import requests
    require(type(expected_size) is int and 0 < expected_size <= MAX_PDF, 'source_size')
    for _ in range(4):
        official_url(url)
        with requests.get(url, timeout=(20, 120), allow_redirects=False, stream=True,
                          headers=source_request_headers()) as response:
            if response.status_code in {301, 302, 303, 307, 308}:
                url = official_url(urljoin(url, response.headers.get('Location', ''))); continue
            if response.status_code != 200:
                raise SourceHTTPError(response.status_code)
            length = response.headers.get('Content-Length')
            require(length is None or int(length) == expected_size, 'source_length')
            parts, size = [], 0
            for part in response.iter_content(65536):
                size += len(part); require(size <= expected_size, 'source_length'); parts.append(part)
            payload = b''.join(parts)
            require(size == expected_size and payload.startswith(b'%PDF-'), 'source_pdf')
            return payload
    raise ValueError('source_redirect_limit')


def prepare(ledger, value, urls, directory, *, fetch=download, restore=None):
    require(ledger.scope == 'institution', 'source_scope')
    require(not directory.exists() or not any(directory.iterdir()), 'source_directory')
    roots, bindings, root_bytes = [], {}, {}
    for key in sorted(value['batches']):
        root, _ = ledger._read_batch(key)
        require('recovery_parent' not in root and root['state'] in {'accepted', 'uploaded', 'terminal'}
                and root.get('batch_id'), 'source_task')
        roots.append(root); root_bytes[key] = encoded(root)
        for item in root['files']:
            require(item['id'] not in bindings, 'source_duplicate')
            require(item['source'] == Path(item['source']).name, 'source_filename')
            bindings[item['id']] = item
    require(sum(item['size'] for item in bindings.values()) <= MAX_TOTAL, 'source_total_size')
    restored = {}
    if restore is not None:
        for item in bindings.values():
            payload = restore(item)
            if payload is not None:
                require(isinstance(payload, bytes) and payload.startswith(b'%PDF-')
                        and len(payload) == item['size'] and digest(payload) == item['sha256'], 'private_source_mismatch')
                restored[item['id']] = payload
    if callable(urls):
        wanted = {item['source'] for item in bindings.values() if item['id'] not in restored}
        urls = urls(wanted) if wanted else {}
    # A stable publication filename can have different chapter URLs over time.
    # Only the original ledger bytes select a candidate; recency never does.
    missing = [item for item in bindings.values() if item['id'] not in restored
               and not 1 <= len(urls.get(item['source'], set())) <= MAX_SOURCE_URLS]
    if missing:
        return {'verified': False, 'original_members': len(bindings), 'missing_url_count': len(missing),
                'missing_source_hashes': [digest(item['source'].encode()) for item in missing],
                'source_url_counts': [{'source_sha256': digest(item['source'].encode()),
                                       'candidate_count': len(urls.get(item['source'], set()))} for item in missing],
                'provider_posts': 0}
    directory.mkdir(parents=True, exist_ok=True)
    verified = 0
    for item in bindings.values():
        raw = restored.get(item['id']); url = None
        try:
            for url in (() if raw is not None else sorted(urls[item['source']])):
                try:
                    candidate = fetch(url, item['size'])
                except ValueError as error:
                    # A different-size or non-PDF official chapter is not this source.
                    # Transport/status failures still stop instead of being retried.
                    if str(error) in {'source_length', 'source_pdf'}: continue
                    raise
                if len(candidate) == item['size'] and digest(candidate) == item['sha256']:
                    raw = candidate; break
            require(raw is not None, 'original_source_bytes_changed')
            path = directory/item['id']; path.write_bytes(raw)
            require(exact_json(ledger.bind(path, item['source']), item), 'source_binding_changed')
            verified += 1
        except Exception as error:
            error.source_diagnostic = {'source_name_sha256': digest(item['source'].encode()),
                'candidate_url_sha256': digest(url.encode()) if url else None,
                'verified_original_members': verified, 'original_members': len(bindings), 'provider_posts': 0}
            raise
    # _original checks every source claim, accepted task, credential and option,
    # and requires the full original inventory; no regrouping or fresh admission.
    terminal = TerminalRecovery(ledger, allowed_error_hashes=value['allowed_error_hashes'])
    for root in roots:
        checked, _ = terminal._original([(directory/item['id'], item['source']) for item in root['files']])
        require(encoded(checked) == root_bytes[root['key']], 'source_task_changed')
    proof = {'schema_version': 1, 'scope': 'institution', 'roots': roots,
             'allowed_error_hashes': value['allowed_error_hashes']}
    raw = encoded(proof); (directory/'proof.json').write_bytes(raw)
    return {'verified': True, 'original_members': len(bindings), 'original_batches': len(roots),
            'restored_original_members': len(restored), 'downloaded_original_members': len(bindings)-len(restored),
            'proof_sha256': digest(raw), 'provider_posts': 0}


def freeze_sources(store, directory, expected_proof):
    from portal_extended_r2 import R2NotFound
    raw = (directory/'proof.json').read_bytes(); require(digest(raw) == expected_proof, 'proof_changed')
    proof = json.loads(raw)
    files = [(directory/item['id'], item['sha256'], item['size'], '.pdf')
             for root in proof['roots'] for item in root['files']]
    files.append((directory/'proof.json', expected_proof, len(raw), '.json'))
    for path, checksum, size, suffix in files:
        payload = path.read_bytes()
        require(len(payload) == size and digest(payload) == checksum, 'original_source_bytes_changed')
        key = '_workflow-cache/institution-originals/v1/'+checksum+suffix
        try: previous = store._get(key, maximum=MAX_PDF)
        except R2NotFound: previous = None
        require(previous is None or previous == payload, 'private_source_conflict')
        if previous is None: store._put(key, payload, metadata={'kind': 'institution-original-proof'})
        require(store._get(key, maximum=MAX_PDF) == payload, 'private_source_readback')


class ReviewedRecovery(TerminalRecovery):
    """Bridge reviewed diagnostic digests without changing durable v1 proofs."""

    def __init__(self, ledger, requested, resolved):
        self.requested = frozenset(requested)
        super().__init__(ledger, allowed_error_hashes=resolved)

    def _allowed(self, row):
        # The v1 digest omits three current diagnostic fields. Recheck the
        # reviewed full error on every fresh root/child proof, so a changed
        # message cannot inherit authority through that lossy conversion.
        return (super()._allowed(row) and (failure_hash(row) in self.requested
                or failure_message_hash(row) in self.requested))


def recover(ledger, directory, *, run_id, expected_proof, verifier):
    require(re.fullmatch(r'[1-9][0-9]{0,19}', run_id), 'recovery_run')
    raw = (directory/'proof.json').read_bytes(); require(digest(raw) == expected_proof, 'proof_changed')
    proof = json.loads(raw); require(proof['scope'] == ledger.scope == 'institution', 'source_scope')
    terminal = TerminalRecovery(ledger, allowed_error_hashes=proof['allowed_error_hashes'])
    # Validate all frozen files and roots again BEFORE first provider POST.
    for root in proof['roots']:
        actual, _ = terminal._original([(directory/item['id'], item['source']) for item in root['files']])
        require(exact_json(actual, root), 'source_task_changed')
    # Only freshly read, exact original inventories may translate a reviewed
    # six-field diagnostic hash to the three-field v1 recovery identity. No
    # static error mapping, provider POST, ledger write or proof rewrite occurs.
    requested = set(proof['allowed_error_hashes'])
    resolved = set(requested)
    observations = []
    for root in proof['roots']:
        rows, _ = _read_once(ledger, root)
        if not terminal._terminal(rows, root['files']):
            raise LedgerError('Only a complete freshly verified terminal task authorizes a recovery child')
        for row in rows.values():
            if str(row['state']).lower() in FAILED and failure_message_hash(row) in requested:
                resolved.add(failure_hash(row))
        observations.append(rows)
    terminal = ReviewedRecovery(ledger, requested, resolved)
    for root, rows in zip(proof['roots'], observations):
        terminal._proof(root, rows)  # Unknown failures in later roots stop all POSTs.
        _, control, _ = terminal._read_control(root)
        if control is not None and control['children']:
            manifests = {entry['authorization']['manifest_sha256'] for entry in control['children']}
            manifests.update(auth['manifest_sha256'] for auth in
                             (control.get('daily_retry_extension') or {}).get('authorizations', []))
            if expected_proof not in manifests:
                raise LedgerError('Recovery authorization differs from the frozen original manifest')
    summaries = []
    for root in proof['roots']:
        _, summary = terminal.run([(directory/item['id'], item['source']) for item in root['files']],
            authorization={'run_id': run_id, 'manifest_sha256': expected_proof}, timeout=900, interval=15,
            queue_budget=120, done_verifier=verifier)
        summaries.append({key: summary[key] for key in ('requested', 'completed', 'failed', 'pending', 'provider_posts', 'ready_for_generation')})
    return {'verified': True, 'original_members': sum(row['requested'] for row in summaries),
            'completed': sum(row['completed'] for row in summaries), 'failed': sum(row['failed'] for row in summaries),
            'pending': sum(row['pending'] for row in summaries), 'provider_posts': sum(row['provider_posts'] for row in summaries),
            'ready_for_generation': all(row['ready_for_generation'] for row in summaries)}


def main():
    expected = os.environ.get('GITHUB_REPOSITORY', '')+'/'+WORKFLOW+'@refs/heads/main'
    require(os.environ.get('GITHUB_ACTIONS') == 'true' and os.environ.get('GITHUB_REF') == 'refs/heads/main'
            and os.environ.get('GITHUB_EVENT_NAME') == 'workflow_dispatch' and os.environ.get('GITHUB_WORKFLOW_REF') == expected,
            'reviewed_main_workflow_required')
    stage = 'request'
    try:
        import requests
        value = request(json.loads(os.environ['RECOVERY_REQUEST']))
        private = single_attempt_store(); store = R2Store('institution', client=private.client, bucket=private.bucket)
        ledger = Ledger(store, Provider(NoRedirectHTTP(requests.request), 'https://mineru.net'), 'institution',
                        'https://mineru.net', {'model': 'vlm', 'language': 'en', 'ocr': True}, credentials(os.environ))
        directory = Path(os.environ['RUNNER_TEMP'])/'institution-originals'
        if os.environ.get('RECOVERY_OPERATION') == 'check-holds':
            from institution_dependency_backlog import check_holds
            stage = 'dependency_hold_check'
            summary = check_holds(ledger, value['batches'])
            Path(os.environ['RUNNER_TEMP'], 'institution-recovery-summary.json').write_bytes(encoded(summary))
            print(json.dumps(summary, sort_keys=True))
            return 0
        if os.environ.get('RECOVERY_OPERATION') == 'seed-holds':
            from institution_dependency_backlog import seed
            stage = 'dependency_hold_seed'
            from institution_hold_provenance import get_original_versions
            summary = seed(ledger, value['batches'],
                version_loader=lambda bindings: get_original_versions(value['source_runs'], bindings))
            Path(os.environ['RUNNER_TEMP'], 'institution-recovery-summary.json').write_bytes(encoded(summary))
            print(json.dumps(summary, sort_keys=True))
            return 0
        stage = 'source_verification'
        from institution_original_cache import OriginalCache
        originals = OriginalCache.single_attempt(store.client, store.bucket)
        summary = prepare(ledger, value, lambda wanted: registry(value, os.environ['GITHUB_REPOSITORY'], wanted), directory,
                          restore=originals.get)
        Path(os.environ['RUNNER_TEMP'], 'institution-recovery-summary.json').write_bytes(encoded(summary))
        print(json.dumps(summary, sort_keys=True))
        if not summary['verified']: return 1
        # Source objects are independently immutable and read back, including
        # every original member, before permitting any recovery request.
        stage = 'freeze_private_sources'
        freeze_sources(private, directory, summary['proof_sha256'])
        if os.environ.get('RECOVERY_OPERATION') == 'recover':
            from mineru_result_cache import ResultCache
            from pdf_to_xhs_batch import download_cached_result
            cache = ResultCache.single_attempt(store.client, store.bucket)
            proof = json.loads((directory/'proof.json').read_bytes())
            bindings = {item['id']: item for root in proof['roots'] for item in root['files']}
            def verify(path, row):
                binding = bindings[row['data_id']]
                target = directory.parent/'verified-results'/binding['id']; target.parent.mkdir(exist_ok=True)
                download_cached_result(path, row, target, cache, {path.resolve(): (binding, row['_recovery_lineage'])})
            stage = 'terminal_recovery'
            summary = recover(ledger, directory, run_id=os.environ['GITHUB_RUN_ID'], expected_proof=summary['proof_sha256'], verifier=verify)
        Path(os.environ['RUNNER_TEMP'], 'institution-recovery-summary.json').write_bytes(encoded(summary))
        print(json.dumps(summary, sort_keys=True))
        return 0 if summary.get('ready_for_generation', True) else 1
    except Exception as error:
        report = {'status': 'stopped', 'stage': stage, 'exception_class': type(error).__name__}
        if type(error) in {ValueError, SourceHTTPError} and re.fullmatch(r'[a-z_]{1,64}', str(error)):
            report['error_code'] = str(error)
        if isinstance(error, SourceHTTPError): report['source_http_status'] = error.status
        report.update(getattr(error, 'source_diagnostic', {}))
        Path(os.environ['RUNNER_TEMP'], 'institution-recovery-summary.json').write_bytes(encoded(report))
        print(json.dumps(report))
        return 1


if __name__ == '__main__': raise SystemExit(main())
