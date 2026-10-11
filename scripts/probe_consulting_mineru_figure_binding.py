#!/usr/bin/env python3
"""Diagnose one admitted consulting PDF; no artifacts, submissions or writes.

Authenticate a completed original job and its exact source URL inventory before
reading the existing task. Public output is only bounded counts and hashes.
"""
from __future__ import annotations

import argparse
import copy
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
from urllib.parse import urlsplit

from mineru_task_ledger import DONE, Ledger, digest, encoded, exact_json
from mineru_completed_child_reuse import read_completed_batch
from mineru_result_cache import OPTIONS, ResultCache, identity
from probe_mineru_figure_binding import (MAX_PROBE_SECONDS, ProbeError, ReadOnlyProvider,
    ReadOnlyR2Client, ReadOnlyStore, compare_cached_pdf, require)

WORKFLOW = '.github/workflows/consulting-mineru-figure-probe.yml'
PRODUCER = '.github/workflows/consulting-latest-pdf-to-wechat.yml'
REPOSITORY = os.environ.get('GITHUB_REPOSITORY', 'example/report-repository')
MAX_LOG_BYTES = 4 * 1024 * 1024
PRODUCTION_MAX_IMAGES = 8  # Normal Consulting source-only wrapper default.


def gh_json(endpoint, operation):
    return json.loads(gh_bytes(endpoint, operation))


def github_failure_category(stderr, returncode):
    """Classify without releasing CLI response text, signed URLs or credentials."""
    message = stderr.decode('utf-8', 'replace').lower()[:65536]
    if 'the response contains terminal escape sequences' in message:
        return 'cli_escape_sequence_rejected'
    matches = re.findall(r'\bhttp(?:/\d(?:\.\d)?)?\s+([45][0-9]{2})\b', message)
    if matches:
        return 'http_' + matches[-1]
    if any(token in message for token in ('tls handshake', 'x509:', 'certificate',
            'dial tcp', 'no such host', 'network is unreachable', 'connection refused',
            'connection reset', 'i/o timeout', 'context deadline exceeded',
            'timeout awaiting response', 'timed out', 'error connecting to')):
        return 'network_stop'
    if returncode == 4 or 'gh auth login' in message:
        return 'authentication_required'
    return 'cli_error'


def job_log_flags():
    """Only allow raw log bytes into a captured pipe, never terminal output.

    gh >= 2.97 refuses escape sequences even in piped non-JSON responses.
    Feature detection is local and precedes the single log request, so older
    runners remain supported without a failed request followed by a retry.
    """
    try:
        help_result = subprocess.run(['gh', 'api', '--help'], capture_output=True, timeout=10)
    except (subprocess.TimeoutExpired, OSError):
        raise ProbeError('github_job_logs_cli_help_unavailable') from None
    require(help_result.returncode == 0 and 0 < len(help_result.stdout) <= 128 * 1024,
        'github_job_logs_cli_help_invalid')
    return ['--allow-escape-sequences'] if b'--allow-escape-sequences' in help_result.stdout else []


def gh_bytes(endpoint, operation):
    require(operation in {'run_metadata', 'job_metadata', 'job_logs'}, 'github_operation_invalid')
    flags = job_log_flags() if operation == 'job_logs' else []
    try:
        result = subprocess.run(['gh', 'api', endpoint, *flags], capture_output=True, timeout=60)
    except subprocess.TimeoutExpired:
        raise ProbeError('github_' + operation + '_network_stop') from None
    except OSError:
        raise ProbeError('github_' + operation + '_cli_unavailable') from None
    if result.returncode != 0:
        raise ProbeError('github_' + operation + '_' + github_failure_category(result.stderr, result.returncode))
    require(0 < len(result.stdout) <= MAX_LOG_BYTES, 'github_response_size')
    return result.stdout


def authenticate(run, job, raw_log, run_id, job_id, expected_articles, ordinal):
    require(re.fullmatch(r'[1-9][0-9]{0,19}', run_id) is not None
        and re.fullmatch(r'[1-9][0-9]{0,19}', job_id) is not None, 'producer_id_invalid')
    require(type(expected_articles) is int and 1 <= ordinal <= expected_articles <= 25,
        'source_selection_invalid')
    require(run.get('id') == int(run_id) and run.get('status') == 'completed'
        and run.get('head_branch') == 'main' and run.get('path') == PRODUCER
        and run.get('event') in {'schedule', 'workflow_dispatch'}
        and run.get('repository', {}).get('full_name') == REPOSITORY
        and run.get('head_repository', {}).get('full_name') == REPOSITORY
        and re.fullmatch(r'[a-f0-9]{40}', str(run.get('head_sha', ''))), 'producer_identity')
    require(job.get('id') == int(job_id) and job.get('run_id') == int(run_id)
        and job.get('status') == 'completed' and job.get('name') == 'fetch-and-build'
        and job.get('head_sha') == run['head_sha'], 'producer_job_identity')
    require(0 < len(raw_log) <= MAX_LOG_BYTES, 'producer_log_size')
    plain = re.sub(r'\x1b\[[0-9;]*m', '', raw_log.decode('utf-8', 'strict'))
    lines = [re.sub(r'^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\.\d+Z ', '', line)
             for line in plain.splitlines()]
    resets = [match.group(1) for line in lines if (match := re.fullmatch(r'HEAD is now at ([a-f0-9]{7,40}) .*', line))]
    require(len(resets) == 1 and run['head_sha'].startswith(resets[0]), 'producer_checkout_changed')
    saved = []
    for line in lines:
        match = re.fullmatch(r'  saved (BCG_[A-Za-z0-9._-]+\.pdf) \([0-9]+ KB\) <- (https://\S+)', line)
        if not match:
            continue
        name, url = match.groups()
        parsed = urlsplit(url)
        require(parsed.scheme == 'https' and parsed.netloc == 'web-assets.bcg.com'
            and parsed.path.lower().endswith('.pdf') and not parsed.query and not parsed.fragment,
            'source_url_not_approved')
        saved.append((name, url))
    require(len(saved) == expected_articles and len({name for name, _ in saved}) == expected_articles,
        'original_source_inventory')
    summaries = [json.loads(line.split(': ', 1)[1]) for line in lines
                 if line.startswith('MinerU durable task summary: ')]
    require(len(summaries) == 1, 'original_summary_ambiguous')
    summary = summaries[0]
    require(summary.get('requested') == expected_articles and summary.get('completed') == expected_articles
        and summary.get('pending') == 0 and summary.get('failed') == 0
        and summary.get('ready_for_generation') is True, 'original_task_incomplete')
    keys = summary.get('batch_keys')
    require(isinstance(keys, list) and 1 <= len(keys) <= 5 and len(set(keys)) == len(keys)
        and all(isinstance(key, str) and re.fullmatch(r'batches/[a-f0-9]{32}', key) for key in keys),
        'original_batch_keys')
    return {'head': run['head_sha'], 'log_sha256': digest(raw_log),
        'inventory_sha256': digest(encoded(sorted(saved))), 'selected': sorted(saved)[ordinal - 1],
        'batch_keys': keys}


def verify_production_figures(original_path, payload, original_sha256, budget=lambda: None):
    """Exercise the real producer and downstream consumer using local inputs.

    Everything materialized here lives in a disposable private report directory.
    The admitted original, provider ZIP and external caches are never modified.
    No source handoff, article, draft or publication is created by this check.
    """
    from contextlib import redirect_stderr, redirect_stdout
    import io
    import shutil
    import mineru_figure_sources as figures
    from consume_legacy_mineru import chart_assets, figure_source_status, safe_unzip
    from pdf_to_xhs_batch import find_markdown
    result = {'status': 'rejected', 'diagnostic_only': True, 'production_acceptance': False,
        'production_consumer_verified': False, 'complete_source_handoff': False,
        'private_handoff_replay_verified': False, 'max_images': PRODUCTION_MAX_IMAGES}
    try:
        budget(); original_path = Path(original_path)
        require(digest(original_path.read_bytes()) == original_sha256, 'production_original_bytes_changed')
        zip_sha256 = digest(payload)
        with tempfile.TemporaryDirectory(prefix='consulting-production-figures-') as temporary, \
                redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()), figures._silent_mupdf():
            report = Path(temporary) / 'report'; raw = report / 'mineru_raw'
            safe_unzip(payload, raw)
            markdown_path = find_markdown(raw)
            require(markdown_path is not None, 'production_markdown_missing')
            # Match process_pdf's real text normalization before asset binding.
            markdown = markdown_path.read_text(encoding='utf-8', errors='ignore').encode('utf-8')
            source = report / 'source_mineru.md'; source.write_bytes(markdown)
            markdown_sha256 = digest(markdown)
            budget()
            images = chart_assets(raw, report / 'assets', PRODUCTION_MAX_IMAGES,
                original_pdf_sha256=original_sha256, auth_original_pdf=original_path,
                markdown_sha256=markdown_sha256)
            status = {'chart_source_only': True, 'source_markdown': 'source_mineru.md',
                'original_pdf_sha256': original_sha256, 'images': images,
                'chart_source_image_count': len(images), **figure_source_status(report)}
            require('source_figure_map' in status, 'production_figure_sidecar_missing')
            (report / 'status.json').write_bytes(encoded(status))
            selected = figures.validate_figure_sources(report,
                expected_original_sha256=original_sha256, expected_markdown_sha256=markdown_sha256,
                expected_images=images)
            require(isinstance(selected, dict), 'production_figure_sidecar_missing')
            mapping_bytes = (report / 'source_image_map.json').read_bytes()
            mapping = json.loads(mapping_bytes)
            require(mapping.get('version') == 1 and mapping.get('source_sha256') == markdown_sha256
                and isinstance(mapping.get('images'), dict)
                and all(mapping['images'].get(ref) == asset for ref, asset in selected.items()),
                'production_image_map_mismatch')
            proof_bytes = (report / figures.SIDECAR).read_bytes(); proof = json.loads(proof_bytes)
            require(proof.get('authenticated_original_render') is True
                and len(proof['assets']) == len(images)
                and all(asset.get('mode') == 'authenticated_original_crop' for asset in proof['assets']),
                'production_original_crop_required')
            budget()
            # Downstream private handoffs retain source carriers, not raw MinerU.
            # Delete only this disposable extraction, then run the real consumer.
            shutil.rmtree(raw)
            replay = figures.validate_figure_sources(report,
                expected_original_sha256=original_sha256, expected_markdown_sha256=markdown_sha256,
                expected_images=images)
            require(exact_json(replay, selected), 'production_handoff_replay_mismatch')
            require(digest(original_path.read_bytes()) == original_sha256 and digest(payload) == zip_sha256,
                'production_input_changed')
            result.update(status='verified', production_consumer_verified=True,
                private_handoff_replay_verified=True, original_pdf_sha256=original_sha256,
                result_zip_sha256=zip_sha256, source_markdown_sha256=markdown_sha256,
                sidecar_sha256=digest(proof_bytes), image_map_sha256=digest(mapping_bytes),
                figure_policy=proof['policy'], restoration_policy=(proof.get('embedded_pdf_render_restoration') or {}).get('policy'),
                selected_page_count=len(proof['pages']), image_count=len(images),
                validated_reference_count=len(selected), image_map_reference_count=len(mapping['images']))
            budget()
    except Exception as error:
        result.update(status='rejected', production_consumer_verified=False, private_handoff_replay_verified=False,
            category=error.category if isinstance(error, figures.FigureSourceError) else
            str(error) if isinstance(error, ProbeError) else type(error).__name__)
    return result


def probe(ledger, cache, plan, download, *, expected_articles, ordinal):
    readonly = copy.copy(ledger)
    deadline = ledger.clock() + MAX_PROBE_SECONDS
    readonly.store = ReadOnlyStore(ledger.store)
    readonly.provider = ReadOnlyProvider(ledger.provider, ledger.clock, deadline)
    readonly.forbid_new_submissions = True
    selected_name, selected_url = plan['selected']
    matches = []
    for key in plan['batch_keys']:
        root, _ = readonly._read_batch(key)
        require('recovery_parent' not in root and root['state'] in {'accepted', 'uploaded', 'terminal'},
            'original_root_invalid')
        matches.extend((root, item) for item in root['files'] if item['source'] == selected_name)
    require(len(matches) == 1, 'selected_source_ambiguous')
    root, binding = matches[0]
    claim, _ = readonly.store.get('sources/' + binding['id'])
    require(isinstance(claim, dict) and claim.get('schema') == 1
        and exact_json(claim.get('binding'), binding) and claim.get('batch_key') == root['key'],
        'selected_source_claim')
    rows, counts = read_completed_batch(readonly, root)
    require(counts.get('all_succeeded') is True, 'selected_root_incomplete')
    row = rows.get(binding['id'])
    require(isinstance(row, dict) and str(row.get('state', '')).lower() in DONE, 'selected_result_incomplete')
    original = download(selected_url)
    require(len(original) == binding['size'] and digest(original) == binding['sha256']
        and original.startswith(b'%PDF-'), 'original_source_bytes_changed')
    lineage = row['_recovery_lineage']
    payload = cache.get(binding, lineage)
    cache_hit = payload is not None
    if payload is None:
        payload = download(row.get('full_zip_url'))
    with tempfile.TemporaryDirectory(prefix='consulting-figure-probe-') as temporary:
        path = Path(temporary) / 'original.pdf'
        path.write_bytes(original)
        comparison = compare_cached_pdf(path, payload, original_sha256=binding['sha256'],
            clock=ledger.clock, deadline=deadline)
        def budget():
            require(ledger.clock() < deadline, 'probe_deadline')
        production_figures = verify_production_figures(path, payload, binding['sha256'], budget)
    readonly.store.verify()
    return {'schema': 1, 'diagnostic_only': True, 'production_acceptance': False,
        'provider_posts': 0, 'provider_uploads': 0, 'model_calls': 0, 'canonical_ledger_writes': 0,
        'cache_writes': 0, 'artifact_downloads': 0, 'original_downloads': 1,
        'provider_zip_downloads': 0 if cache_hit else 1, 'cache_hit': cache_hit,
        'provider_gets': readonly.provider.gets, 'source_ordinal': ordinal,
        'original_report_count': expected_articles, 'source_binding_sha256': binding['id'],
        'cache_identity_sha256': identity(binding, lineage), 'comparison': comparison,
        'production_figure_consumer': production_figures}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-run-id', required=True)
    parser.add_argument('--source-job-id', required=True)
    parser.add_argument('--expected-articles', required=True, type=int)
    parser.add_argument('--source-ordinal', required=True, type=int)
    parser.add_argument('--output', required=True)
    args = parser.parse_args(argv)
    result = {'schema': 1, 'diagnostic_only': True, 'production_acceptance': False,
        'provider_posts': 0, 'provider_uploads': 0, 'model_calls': 0,
        'canonical_ledger_writes': 0, 'cache_writes': 0, 'artifact_downloads': 0}
    code = 2
    try:
        env = os.environ
        require(env.get('GITHUB_ACTIONS') == 'true' and env.get('GITHUB_EVENT_NAME') == 'workflow_dispatch'
            and env.get('GITHUB_REF') == 'refs/heads/main' and env.get('GITHUB_REPOSITORY') == REPOSITORY
            and env.get('GITHUB_WORKFLOW_REF') == REPOSITORY + '/' + WORKFLOW + '@refs/heads/main',
            'reviewed_main_probe_required')
        require(all(re.fullmatch(r'[1-9][0-9]{0,19}', value) for value in
            (args.source_run_id, args.source_job_id)), 'producer_id_invalid')
        run = gh_json(f'repos/{REPOSITORY}/actions/runs/{args.source_run_id}', 'run_metadata')
        job = gh_json(f'repos/{REPOSITORY}/actions/jobs/{args.source_job_id}', 'job_metadata')
        log = gh_bytes(f'repos/{REPOSITORY}/actions/jobs/{args.source_job_id}/logs', 'job_logs')
        plan = authenticate(run, job, log, args.source_run_id, args.source_job_id,
            args.expected_articles, args.source_ordinal)
        import boto3
        from botocore.config import Config
        import requests
        from private_workflow_handoff import require_env
        from mineru_task_ledger import Provider, R2Store
        from smoke_mineru_api import credentials, NoRedirectHTTP
        from consume_legacy_mineru import download_once
        client = ReadOnlyR2Client(boto3.client('s3',
            endpoint_url='https://' + require_env('R2_ACCOUNT_ID') + '.r2.cloudflarestorage.com',
            aws_access_key_id=require_env('R2_ACCESS_KEY_ID'), aws_secret_access_key=require_env('R2_SECRET_ACCESS_KEY'),
            region_name='auto', config=Config(connect_timeout=20, read_timeout=30,
                retries={'total_max_attempts': 1, 'mode': 'standard'})))
        bucket = require_env('R2_BUCKET')
        ledger = Ledger(R2Store('consulting', client=client, bucket=bucket),
            Provider(NoRedirectHTTP(requests.request), 'https://mineru.net'), 'consulting',
            'https://mineru.net', OPTIONS, credentials(env))
        result = probe(ledger, ResultCache(client, bucket), plan,
            lambda url: download_once(url, timeout=30), expected_articles=args.expected_articles,
            ordinal=args.source_ordinal)
        result.update(source_run_id=args.source_run_id, source_job_id=args.source_job_id,
            source_execution_sha=plan['head'], source_job_log_sha256=plan['log_sha256'],
            original_inventory_sha256=plan['inventory_sha256'], probe_execution_sha=env['GITHUB_SHA'])
        code = 0
    except Exception as error:
        result.update(status='stopped', category=str(error) if isinstance(error, ProbeError) else type(error).__name__)
    Path(args.output).write_bytes(encoded(result) + b'\n')
    print(json.dumps(result, sort_keys=True))
    return code


if __name__ == '__main__':
    raise SystemExit(main())
