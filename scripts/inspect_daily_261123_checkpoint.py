#!/usr/bin/env python3
"""Read the exact private Daily checkpoint and print bounded diagnostics."""
import contextlib
import io
import json
import os
from pathlib import Path
import re
import tempfile

from inspect_market_views_r2_cache import HASH, ReadOnlyClient, bounded_size, build_client, validate_ocr_producer
from inspect_recovered_article_generation import CATEGORIES, diagnostic, read, require
from market_views_source_readiness import require_source_readiness
from private_workflow_handoff import download_directory, require_env
from recovered_article_delivery import api, jobs, digest, encode


REPOSITORY = 'yt-feng/rpt_edit'
RUN_ID = '45309350829'
JOB_ID = 138177407475
SHA = 'e0986573adf03fae063a467968a2770360ce4d0f'
MANIFEST = '525f0966a46a5736742344343f56139e317fed0c971e5f0262b9ce161f28231b'
PLAN = 'e7519864a22b19c8165d729fd2383df1cfb5b1e715f8522e4e2723a2adbdd5c3'
DATE = '261123'
COUNT = 48
SHA256_RE = re.compile(r'[a-f0-9]{64}')
ARCHIVE_LIMIT = 2 * 1024 ** 3
EXPANDED_LIMIT = 4 * 1024 ** 3
JSON_LIMIT = 16 * 1024 ** 2
EXCEPTION_TYPES = {
    'ArticleRecoveryError', 'ProgressError', 'TimeoutError', 'ConnectionError',
    'HTTPError', 'ReadTimeout', 'ConnectTimeout', 'SSLError', 'RequestException',
    'ChunkedEncodingError', 'JSONDecodeError', 'RuntimeError', 'ValueError',
    'TypeError', 'OSError', 'KeyError', 'AttributeError', 'UnicodeDecodeError',
    'FileNotFoundError', 'PermissionError',
}
FAILURE_CODES = set(CATEGORIES) | {
    'article_failure_diagnostics_unavailable', 'article_failure_checkpoint_unavailable',
}


def verify_original():
    run = api(REPOSITORY, RUN_ID)
    page = jobs(REPOSITORY, RUN_ID, attempt=1)
    require(validate_ocr_producer(run, {'source_run_id': RUN_ID}, REPOSITORY) == SHA
            and run['conclusion'] == 'failure' and run['run_attempt'] == 1, 'original_run_changed')
    require_source_readiness(run, page, source_kind='mineru-recovery')
    found = [item for item in page['jobs'] if item['id'] == JOB_ID]
    require(len(found) == 1, 'original_job_missing')
    job = found[0]
    require(job['run_id'] == int(RUN_ID) and job['head_sha'] == SHA
            and job['name'] == 'deliver-recovered-report-articles / generate'
            and job['status'] == 'completed' and job['conclusion'] == 'failure', 'original_job_changed')
    step_numbers = []
    for name, result in (
        ('Authenticate original upload and restore exact recovery sources', 'success'),
        ('Generate only missing bound report articles', 'failure'),
        ('Save generation progress even after interruption', 'success'),
    ):
        steps = [step for step in job['steps'] if step['name'] == name]
        require(len(steps) == 1 and steps[0]['status'] == 'completed'
                and steps[0]['conclusion'] == result, 'original_generation_state_changed')
        step_numbers.append(steps[0]['number'])
    require(step_numbers == sorted(set(step_numbers)), 'original_generation_state_changed')


def optional_file(path):
    if path.exists() or path.is_symlink():
        return read(path, JSON_LIMIT)
    return None


def summarize(root):
    context = json.loads(read(root / 'context.json', JSON_LIMIT))
    expected = {
        'schema_version': 1, 'source_run_id': RUN_ID, 'source_handoff_run_id': RUN_ID,
        'source_kind': 'mineru-recovery', 'date_folder': DATE, 'expected_articles': COUNT,
        'source_execution_sha': SHA, 'handoff_execution_sha': SHA,
        'manifest_sha256': MANIFEST, 'progressive_plan_sha256': PLAN,
    }
    require(set(context) == set(expected) | {'source_receipt_sha256'}
            and all(context[key] == value for key, value in expected.items())
            and SHA256_RE.fullmatch(context['source_receipt_sha256']), 'checkpoint_context_changed')
    provenance = json.loads(read(root / 'articles/source_provenance.json', JSON_LIMIT))
    require(provenance['manifest_sha256'] == MANIFEST and provenance['source_run_id'] == RUN_ID
            and digest(provenance['source_receipt_json'].encode()) == context['source_receipt_sha256'],
            'checkpoint_provenance_changed')
    require(len(provenance['sources']) == COUNT, 'checkpoint_source_count_changed')
    log = read(root / 'private-diagnostics/private-generation.log', 2 * 1024 ** 2).decode('utf-8', 'replace')
    terminal = re.findall(r'^Report article recovery stopped: ([a-z_]{1,80})(?: source_ordinal=(\d{1,4}))?$', log, re.M)
    completed = re.findall(r'^RECOVERED_ARTICLE ordinal=(\d{1,4}) reused=(?:true|false)$', log, re.M)
    failures, pending = [], []
    for ordinal, source in enumerate(provenance['sources'], 1):
        directory = source['directory']
        require(isinstance(directory, str) and Path(directory).name == directory
                and directory not in {'.', '..'}, 'invalid_report_path')
        progress = optional_file(root / 'generation-progress' / directory / 'article_generation_progress.json')
        for request in json.loads(progress or b'{}').get('requests', []):
            if request['state'] == 'pending' and request['kind'] in {'body', 'title'}:
                pending.append({'ordinal': ordinal, 'kind': request['kind']})
        failure = optional_file(root / 'private-diagnostics/article-failures' / f'ordinal_{ordinal:04d}.json')
        if failure is None:
            continue
        info = json.loads(failure)
        status = optional_file(root / 'articles' / directory / 'status.json')
        require(info['source_ordinal'] == ordinal
                and info['source_provenance_sha256'] == digest(encode(source['provenance']))
                and info['source_markdown_sha256'] == source['source_markdown_sha256'],
                'checkpoint_failure_binding_changed')
        category = info['category'] if info['category'] in FAILURE_CODES else 'unknown'
        current = (info['article_status_sha256'] == (digest(status) if status is not None else None)
                   and info['progress_receipt_sha256'] == (digest(progress) if progress is not None else None))
        typed = diagnostic(info['private_traceback'], json.loads(status or b'{}'))
        failures.append({
            'ordinal': ordinal, 'category': category, 'snapshot_current': current, 'phase': typed['phase'],
            'typed_causes': typed['typed_causes'], 'http_statuses': typed['http_statuses'],
            'exceptions': [name if name in EXCEPTION_TYPES else 'UnknownException'
                           for name in info['typed_exception_chain']],
            'saved_article_file_present': (root / 'articles' / directory / 'wechat_article.md').is_file(),
        })
    return {
        'source_reports': COUNT,
        'logged_completed_articles': len({int(n) for n in completed if 1 <= int(n) <= COUNT}),
        'complete_receipt_present': (root / 'articles/article_recovery_receipt.json').is_file(),
        'terminal_category': terminal[-1][0] if terminal and terminal[-1][0] in FAILURE_CODES else 'unknown',
        'terminal_ordinal': (int(terminal[-1][1]) if terminal and terminal[-1][1]
                             and 1 <= int(terminal[-1][1]) <= COUNT else None),
        'failure_snapshots': failures,
        'pending_requests': pending,
    }


def main():
    phase = 'validate_dispatch'
    try:
        require(os.environ.get('GITHUB_ACTIONS') == 'true'
                and os.environ.get('GITHUB_REPOSITORY') == REPOSITORY
                and os.environ.get('GITHUB_EVENT_NAME') == 'workflow_dispatch'
                and os.environ.get('GITHUB_REF') == 'refs/heads/codex/inspect-daily-261123'
                and os.environ.get('GITHUB_ACTOR') == 'yt-feng', 'invalid_dispatch')
        phase = 'verify_original'
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            verify_original()
            phase = 'download_checkpoint'
            client, bucket = build_client(), require_env('R2_BUCKET')
            key = f'_private-workflow-handoff/xhs-recovery/{RUN_ID}/{DATE}/{MANIFEST}/generation.tar.gz'
            head = client.head_object(Bucket=bucket, Key=key)
            size = bounded_size(head, ARCHIVE_LIMIT)
            require(bool(HASH.fullmatch((head.get('Metadata') or {}).get('sha256', ''))),
                    'archive_checksum_missing')
            reader = ReadOnlyClient(client, head, archive_limit=ARCHIVE_LIMIT, expanded_limit=EXPANDED_LIMIT)
            with tempfile.TemporaryDirectory(prefix='daily-checkpoint-') as temp:
                root = Path(temp) / 'checkpoint'
                download_directory(key, root, client=reader, bucket=bucket)
                phase = 'read_diagnostics'
                result = summarize(root)
    except Exception:
        print(json.dumps({'verified': False, 'inspection_phase': phase}))
        return 1
    print(json.dumps({'verified': True, 'archive_bytes': size, **result}, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
