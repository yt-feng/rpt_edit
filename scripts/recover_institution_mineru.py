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

from mineru_task_ledger import Ledger, LedgerError, Provider, R2Store, digest, encoded, exact_json
from mineru_terminal_recovery import TerminalRecovery, task_identity
from persist_legacy_mineru_inspection import single_attempt_store
from smoke_mineru_api import NoRedirectHTTP, credentials

WORKFLOW = '.github/workflows/institution-mineru-recovery.yml'
PRODUCER = '.github/workflows/institution-latest-pdf-to-wechat.yml'
DOMAINS = {'imf.org', 'worldbank.org', 'bis.org', 'oecd.org', 'adb.org', 'weforum.org', 'unctad.org', 'wto.org', 'bruegel.org'}
MAX_PDF = 64 * 1024 * 1024
MAX_TOTAL = 512 * 1024 * 1024


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
        with requests.get(url, timeout=(20, 120), allow_redirects=False, stream=True) as response:
            if response.status_code in {301, 302, 303, 307, 308}:
                url = official_url(urljoin(url, response.headers.get('Location', ''))); continue
            require(response.status_code == 200, 'source_http_status')
            length = response.headers.get('Content-Length')
            require(length is None or int(length) == expected_size, 'source_length')
            parts, size = [], 0
            for part in response.iter_content(65536):
                size += len(part); require(size <= expected_size, 'source_length'); parts.append(part)
            payload = b''.join(parts)
            require(size == expected_size and payload.startswith(b'%PDF-'), 'source_pdf')
            return payload
    raise ValueError('source_redirect_limit')


def prepare(ledger, value, urls, directory, *, fetch=download):
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
    # Missing URLs are diagnosed before downloading anything or polling tasks.
    missing = [item for item in bindings.values() if len(urls.get(item['source'], set())) != 1]
    if missing:
        return {'verified': False, 'original_members': len(bindings), 'missing_url_count': len(missing),
                'missing_source_hashes': [digest(item['source'].encode()) for item in missing], 'provider_posts': 0}
    directory.mkdir(parents=True, exist_ok=True)
    for item in bindings.values():
        raw = fetch(next(iter(urls[item['source']])), item['size'])
        require(len(raw) == item['size'] and digest(raw) == item['sha256'], 'original_source_bytes_changed')
        path = directory/item['id']; path.write_bytes(raw)
        require(exact_json(ledger.bind(path, item['source']), item), 'source_binding_changed')
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


def recover(ledger, directory, *, run_id, expected_proof, verifier):
    require(re.fullmatch(r'[1-9][0-9]{0,19}', run_id), 'recovery_run')
    raw = (directory/'proof.json').read_bytes(); require(digest(raw) == expected_proof, 'proof_changed')
    proof = json.loads(raw); require(proof['scope'] == ledger.scope == 'institution', 'source_scope')
    terminal = TerminalRecovery(ledger, allowed_error_hashes=proof['allowed_error_hashes'])
    # Validate all frozen files and roots again BEFORE first provider POST.
    for root in proof['roots']:
        actual, _ = terminal._original([(directory/item['id'], item['source']) for item in root['files']])
        require(exact_json(actual, root), 'source_task_changed')
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
        stage = 'source_verification'
        wanted = {item['source'] for key in value['batches'] for item in ledger._read_batch(key)[0]['files']}
        summary = prepare(ledger, value, registry(value, os.environ['GITHUB_REPOSITORY'], wanted), directory)
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
        print(json.dumps({'status': 'stopped', 'stage': stage, 'exception_class': type(error).__name__}))
        return 1


if __name__ == '__main__': raise SystemExit(main())
