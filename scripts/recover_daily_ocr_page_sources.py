#!/usr/bin/env python3
"""Resume Daily articles from complete private OCR pages, without synthesis."""
from __future__ import annotations

import argparse
from contextlib import redirect_stderr, redirect_stdout
import json
import os
from pathlib import Path
import re
import tempfile

from ocr_page_sources import (DAILY_WORKFLOW, DAILY_PREFIX, RECEIPT, build_pages,
    validate_pages_receipt, digest)
from private_market_ocr_checkpoint import checkpoint_key
from private_workflow_handoff import require_env, upload_directory
from recover_durable_mineru_sources import frozen_inputs
from recover_ocr_cache_sources import (require, exact_head, download_verified,
    public_error_category, build_client)


def recovery_outcomes(mineru, ocr, mineru_saved, ocr_saved):
    """Use step outcomes, including failed continue-on-error attempts."""
    recognized = {'success', 'failure', 'cancelled', 'skipped', ''}
    require(all(value in recognized for value in (mineru, ocr, mineru_saved, ocr_saved)),
            'daily_recovery_outcome_invalid')
    ready = (mineru == mineru_saved == 'success') or (ocr == ocr_saved == 'success')
    return {'mineru_recovery_failed': str(mineru == 'failure').lower(),
            'ocr_attempted': str(ocr in {'success', 'failure'}).lower(),
            'article_source_ready': str(ready).lower()}


def identity(env):
    repository, run_id, sha = (env.get(key, '') for key in
        ('GITHUB_REPOSITORY', 'GITHUB_RUN_ID', 'GITHUB_SHA'))
    require(env.get('GITHUB_ACTIONS') == 'true' and env.get('GITHUB_REF') == 'refs/heads/main'
            and env.get('GITHUB_EVENT_NAME') in {'schedule', 'workflow_dispatch'}
            and re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository)
            and env.get('GITHUB_WORKFLOW_REF') == f'{repository}/{DAILY_WORKFLOW}@refs/heads/main'
            and re.fullmatch(r'[1-9][0-9]{0,19}', run_id) and re.fullmatch(r'[a-f0-9]{40}', sha),
            'daily_pages_identity_invalid')
    require(env.get('REPLAY_SOURCE_RUN_ID') == '' and env.get('PRIMARY_READY') == 'false'
            and env.get('MINERU_RECOVERY_FAILED') == env.get('OCR_ATTEMPTED') == 'true'
            and env.get('ARTICLE_SOURCE_READY') == 'false', 'daily_pages_fallback_not_eligible')
    return run_id, sha


def frozen_context(input_dir, env):
    run_id, sha = identity(env)
    count, date = env.get('EXPECTED_REPORTS', ''), env.get('DATE_FOLDER', '')
    require(re.fullmatch(r'[1-9][0-9]{0,3}', count) and int(count) <= 1000
            and re.fullmatch(r'[0-9]{6}', date), 'daily_pages_selection_invalid')
    manifest = input_dir/'selected_to_process_manifest.json'
    raw, _, _ = frozen_inputs(input_dir, manifest, int(count), date)
    return manifest, {'source_run_id': run_id, 'execution_sha': sha, 'date_folder': date,
                      'expected_reports': int(count)}, digest(raw)


def verify(source, context, manifest_sha):
    from recover_report_articles import load_sources
    receipt = validate_pages_receipt(source, **context, recovery_run_id=context['source_run_id'],
                                    recovery_execution_sha=context['execution_sha'])
    require('daily_cache_origin' in receipt and receipt['selected_manifest_sha256'] == manifest_sha,
            'daily_pages_source_changed')
    load_sources(source, 'ocr-pages', context['expected_reports'], context['date_folder'],
        source_run_id=context['source_run_id'], source_execution_sha=context['execution_sha'],
        source_handoff_run_id=context['source_run_id'], source_handoff_execution_sha=context['execution_sha'])
    return receipt


def key_for(context):
    return f'{DAILY_PREFIX}/{context["source_run_id"]}/{context["date_folder"]}/shard_0.tar.gz'


def recover(input_dir, workspace, env, client, bucket):
    manifest, context, manifest_sha = frozen_context(input_dir, env)
    source = workspace/'source'
    key = key_for(context)
    existing = exact_head(client, bucket, key, optional=True)
    if existing is not None:
        download_verified(client, bucket, key, source, existing)
        verify(source, context, manifest_sha)
        return {'reused': True, 'reports': context['expected_reports']}
    cache_key = checkpoint_key(manifest, context['date_folder'], context['expected_reports'])
    pinned_head = exact_head(client, bucket, cache_key)
    cache = workspace/'cache'
    download_verified(client, bucket, cache_key, cache, pinned_head)
    origin = {'schema_version': 1, 'workflow': DAILY_WORKFLOW,
        'source_run_id': context['source_run_id'], 'source_execution_sha': context['execution_sha'],
        'manifest_sha256': manifest_sha, 'checkpoint_identity': cache_key.rsplit('/', 1)[-1][:-7],
        'archive_sha256': pinned_head['Metadata']['sha256'], 'archive_size_bytes': pinned_head['ContentLength'],
        'cache_only': True, 'ocr_calls': 0, 'provider_posts': 0}
    build_pages(input_dir, manifest, cache, source, **context, daily_origin=origin)
    verify(source, context, manifest_sha)
    return {'reused': False, 'reports': context['expected_reports']}


def archive(input_dir, workspace, env, client, bucket):
    _, context, manifest_sha = frozen_context(input_dir, env)
    source, key = workspace/'source', key_for(context)
    verify(source, context, manifest_sha)
    head = exact_head(client, bucket, key, optional=True)
    with tempfile.TemporaryDirectory(prefix='daily-ocr-pages-readback-', dir=workspace) as temp:
        readback = Path(temp)/'source'
        if head is None:
            upload_directory(source, key, client=client, bucket=bucket, include_ocr_page_originals=True)
            head = exact_head(client, bucket, key)
        download_verified(client, bucket, key, readback, head)
        verify(readback, context, manifest_sha)
        require((readback/RECEIPT).read_bytes() == (source/RECEIPT).read_bytes(),
                'daily_pages_existing_receipt_changed')
    return {'reports': context['expected_reports'], 'archive_verified': True}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('outcomes', 'recover', 'archive'))
    parser.add_argument('--input-dir', type=Path)
    parser.add_argument('--workspace', type=Path)
    args = parser.parse_args(argv)
    if args.command == 'outcomes':
        result = recovery_outcomes(*(os.environ.get(key, '') for key in
            ('MINERU_OUTCOME', 'OCR_OUTCOME', 'MINERU_SAVE_OUTCOME', 'OCR_SAVE_OUTCOME')))
        with open(require_env('GITHUB_OUTPUT'), 'a') as output:
            for name, value in result.items(): output.write(f'{name}={value}\n')
        return 0
    if args.workspace is None or args.input_dir is None:
        parser.error('--input-dir and --workspace are required for recovery/archive')
    args.workspace.mkdir(parents=True, exist_ok=True)
    try:
        with (args.workspace/'private-recovery.log').open('a') as log, redirect_stdout(log), redirect_stderr(log):
            result = (recover if args.command == 'recover' else archive)(
                args.input_dir, args.workspace, os.environ, build_client(), require_env('R2_BUCKET'))
        print(json.dumps({'stage': args.command, 'success': True, 'ocr_calls': 0, 'provider_posts': 0, **result}))
        return 0
    except Exception as error:
        import traceback
        with (args.workspace/'private-recovery.log').open('a') as log: traceback.print_exc(file=log)
        print(json.dumps({'stage': args.command, 'success': False, 'category': public_error_category(error),
                          'ocr_calls': 0, 'provider_posts': 0}))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
