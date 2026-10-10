#!/usr/bin/env python3
"""Recover exact historical OCR sources using verified cache bytes only."""
from __future__ import annotations

import argparse
from contextlib import redirect_stderr, redirect_stdout
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile

from inspect_market_views_r2_cache import (HASH, MAX_BYTES, ReadOnlyClient, bounded_size,
    build_client, validate_ocr_producer, validate_ocr_request)
from private_market_ocr_checkpoint import checkpoint_key
from private_workflow_handoff import download_directory, require_env, upload_directory
from recover_durable_mineru_sources import frozen_inputs

WORKFLOW = '.github/workflows/recover-ocr-cache-sources.yml'
PREFIX = '_private-workflow-handoff/market-ocr-cache-recovery'
RECEIPT = 'ocr_synthesis_receipt.json'


class CacheRecoveryError(ValueError):
    """Public errors contain fixed categories, never source/provider text."""


def require(condition, category):
    if not condition:
        raise CacheRecoveryError(category)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def public_error_category(error):
    from ocr_page_sources import OCRPagesError
    if isinstance(error, OCRPagesError):
        return str(error)
    if isinstance(error, CacheRecoveryError):
        return str(error)
    fixed = {
        'cache_only_pages_missing': 'cache_only_pages_missing',
        'cache_only_summary_missing': 'cache_only_summary_missing',
        'cache_only_final_synthesis_missing': 'cache_only_final_synthesis_missing',
        'Model cache identity mismatch': 'summary_cache_identity_invalid',
        'Final synthesis cache mismatch': 'final_synthesis_cache_identity_invalid',
        'Cached extraction has incomplete or corrupt page coverage': 'cached_pages_incomplete_or_corrupt',
        'Final synthesis submission already pending': 'final_synthesis_submission_pending',
        'archive_hash_mismatch': 'archive_hash_mismatch',
        'object_size_mismatch': 'archive_size_mismatch',
        'archive_changed': 'archive_changed',
        'archive_path': 'archive_unsafe_path',
        'archive_member_limit': 'archive_members_invalid',
        'archive_expansion_limit': 'archive_expansion_limit',
        'archive_duplicate_member': 'archive_duplicate_member',
    }
    if isinstance(error, (ValueError, RuntimeError)):
        message = str(error)
        if message in fixed:
            return fixed[message]
        if message.startswith('Prior model submission has unknown/incomplete outcome; inspect checkpoint '):
            return 'summary_submission_pending'
    return type(error).__name__


def request_from_env(env):
    source_mode(env)
    request = validate_ocr_request(*(env.get(name, '') for name in
        ('SOURCE_RUN_ID', 'DATE_FOLDER', 'EXPECTED_REPORTS', 'MANIFEST_SHA256')))
    require(request is not None, 'exact_source_request_required')
    checksum, size = env.get('ARCHIVE_SHA256', ''), env.get('ARCHIVE_SIZE_BYTES', '')
    require(bool(HASH.fullmatch(checksum)) and bool(re.fullmatch(r'[1-9][0-9]{0,9}', size))
            and int(size) <= MAX_BYTES, 'pinned_archive_request_invalid')
    return {**request, 'archive_sha256': checksum, 'archive_size_bytes': int(size)}


def source_mode(env):
    mode = env.get('SOURCE_MODE', 'synthesis')
    require(mode in {'synthesis', 'pages'}, 'source_mode_invalid')
    return mode


def source_contract(mode):
    if mode == 'pages':
        from ocr_page_sources import PREFIX as prefix, RECEIPT as receipt, KIND as kind
        return prefix, receipt, kind
    require(mode == 'synthesis', 'source_mode_invalid')
    return PREFIX, RECEIPT, 'ocr-synthesis'


def recovery_identity(env, request):
    repository, run_id, sha = (env.get(name, '') for name in
        ('GITHUB_REPOSITORY', 'GITHUB_RUN_ID', 'GITHUB_SHA'))
    require(env.get('GITHUB_ACTIONS') == 'true' and env.get('GITHUB_REF') == 'refs/heads/main'
            and env.get('GITHUB_EVENT_NAME') == 'workflow_dispatch'
            and env.get('GITHUB_WORKFLOW_REF') == f'{repository}/{WORKFLOW}@refs/heads/main'
            and bool(re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository))
            and bool(re.fullmatch(r'[1-9][0-9]{0,19}', run_id))
            and bool(re.fullmatch(r'[a-f0-9]{40}', sha))
            and run_id != request['source_run_id'], 'recovery_main_identity_invalid')
    return repository, run_id, sha


def exact_head(client, bucket, key, *, optional=False):
    try:
        head = client.head_object(Bucket=bucket, Key=key)
    except Exception as error:
        code = str(getattr(error, 'response', {}).get('Error', {}).get('Code', ''))
        if optional and code in {'NoSuchKey', '404', 'NotFound'}:
            return None
        raise CacheRecoveryError('private_object_unavailable') from None
    bounded_size(head)
    require(bool(HASH.fullmatch(str((head.get('Metadata') or {}).get('sha256', '')))),
            'archive_checksum_missing')
    return head


def download_verified(client, bucket, key, destination, head):
    # The adapter binds every HEAD/GET to required size/hash and bounds expansion.
    download_directory(key, destination, client=ReadOnlyClient(client, head), bucket=bucket)


def verified_sources(root, request, original_sha, run_id, sha, mode='synthesis'):
    from market_views_publication import validate_ocr_synthesis_receipt
    from recover_report_articles import load_sources
    validator = validate_ocr_synthesis_receipt
    if mode == 'pages':
        from ocr_page_sources import validate_pages_receipt
        validator = validate_pages_receipt
    _, _, kind = source_contract(mode)
    receipt = validator(root, date_folder=request['date_folder'],
        expected_reports=request['expected_reports'], source_run_id=request['source_run_id'],
        execution_sha=original_sha, recovery_run_id=run_id, recovery_execution_sha=sha)
    envelope = receipt['cache_recovery']
    require(receipt['selected_manifest_sha256'] == request['manifest_sha256']
            and envelope['archive_sha256'] == request['archive_sha256']
            and envelope['archive_size_bytes'] == request['archive_size_bytes'], 'recovery_checkpoint_changed')
    # Includes every page's actual text hash and full page ordering, before upload.
    load_sources(root, kind, request['expected_reports'], request['date_folder'],
        source_run_id=request['source_run_id'], source_execution_sha=original_sha,
        source_handoff_run_id=run_id, source_handoff_execution_sha=sha)
    return receipt


def frozen_context(input_dir, producer, request, env):
    repository, run_id, sha = recovery_identity(env, request)
    original_sha = validate_ocr_producer(producer, request, repository)
    manifest = input_dir / 'selected_to_process_manifest.json'
    raw, bindings, pairs = frozen_inputs(input_dir, manifest, request['expected_reports'], request['date_folder'])
    require(digest(raw) == request['manifest_sha256'], 'frozen_manifest_changed')
    import fitz
    for path, _ in pairs:
        with fitz.open(path) as document:
            require(not document.needs_pass and document.page_count > 0, 'original_pdf_pages_invalid')
    return manifest, original_sha, run_id, sha


def recover(input_dir, producer, request, workspace, env, client, bucket, *,
            model='deepseek-flash', base_url='https://api.deepseek.com'):
    manifest, original_sha, run_id, sha = frozen_context(input_dir, producer, request, env)
    mode = source_mode(env)
    prefix, receipt_name, _ = source_contract(mode)
    source = workspace / 'source'
    key = f'{prefix}/{run_id}/{request["date_folder"]}/shard_0.tar.gz'
    existing = exact_head(client, bucket, key, optional=True)
    if existing is not None:
        download_verified(client, bucket, key, source, existing)
        receipt = verified_sources(source, request, original_sha, run_id, sha, mode)
        if mode == 'synthesis': require(receipt['model'] == model, 'recovery_model_changed')
        return {'reused': True, 'reports': request['expected_reports']}

    cache_key = checkpoint_key(manifest, request['date_folder'], request['expected_reports'])
    head = exact_head(client, bucket, cache_key)
    require(head['ContentLength'] == request['archive_size_bytes']
            and head['Metadata']['sha256'] == request['archive_sha256'], 'pinned_checkpoint_changed')
    cache = workspace / 'cache'
    download_verified(client, bucket, cache_key, cache, head)
    envelope = {
        'schema_version': 1, 'workflow': WORKFLOW, 'recovery_run_id': run_id, 'recovery_execution_sha': sha,
        'source_run_id': request['source_run_id'], 'source_execution_sha': original_sha,
        'manifest_sha256': request['manifest_sha256'],
        'checkpoint_identity': cache_key.rsplit('/', 1)[-1].removesuffix('.tar.gz'),
        'archive_sha256': request['archive_sha256'], 'archive_size_bytes': request['archive_size_bytes'],
        'cache_only': True, 'ocr_calls': 0, 'provider_posts': 0}
    if mode == 'pages':
        from ocr_page_sources import build_pages
        built = workspace / 'built' / request['date_folder']
        build_pages(input_dir, manifest, cache, built, expected_reports=request['expected_reports'],
            date_folder=request['date_folder'], source_run_id=request['source_run_id'], execution_sha=original_sha,
            recovery=envelope)
        verified_sources(built, request, original_sha, run_id, sha, mode)
        require(not source.exists(), 'recovery_destination_not_fresh')
        built.rename(source)
        return {'reused': False, 'reports': request['expected_reports']}
    from build_market_views_ocr_fallback import build, write_json
    # No OCR/model credentials are passed by the producer workflow. Cache-only
    # guards are still enforced even when such credentials exist in an environment.
    receipt = build(input_dir, manifest, request['expected_reports'], request['date_folder'],
        workspace / 'built', cache, source_run_id=request['source_run_id'], execution_sha=original_sha,
        model=model, base_url=base_url, ocr_all_pages=True, cache_only=True)
    require(receipt['summarized_reports'] == request['expected_reports'] and receipt['skipped_reports'] == 0,
            'complete_cached_source_coverage_required')
    receipt['cache_recovery'] = envelope
    built = workspace / 'built' / request['date_folder']
    write_json(built / RECEIPT, receipt)
    verified_sources(built, request, original_sha, run_id, sha)
    require(not source.exists(), 'recovery_destination_not_fresh')
    built.rename(source)
    return {'reused': False, 'reports': request['expected_reports']}


def archive(input_dir, producer, request, workspace, env, client, bucket):
    _, original_sha, run_id, sha = frozen_context(input_dir, producer, request, env)
    mode = source_mode(env)
    prefix, receipt_name, _ = source_contract(mode)
    source = workspace / 'source'
    verified_sources(source, request, original_sha, run_id, sha, mode)
    key = f'{prefix}/{run_id}/{request["date_folder"]}/shard_0.tar.gz'
    head = exact_head(client, bucket, key, optional=True)
    with tempfile.TemporaryDirectory(prefix='ocr-source-readback-', dir=workspace) as temp:
        readback = Path(temp) / 'source'
        if head is None:
            extra = {'include_ocr_page_originals': True} if mode == 'pages' else {}
            upload_directory(source, key, client=client, bucket=bucket, **extra)
            head = exact_head(client, bucket, key)
        download_verified(client, bucket, key, readback, head)
        verified_sources(readback, request, original_sha, run_id, sha, mode)
        # Never overwrite an existing source receipt: accepted consumer contexts
        # bind these exact bytes, including completion time and cache metrics.
        require((readback / receipt_name).read_bytes() == (source / receipt_name).read_bytes(),
                'existing_handoff_receipt_changed')
    return {'reports': request['expected_reports'], 'archive_verified': True}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('recover', 'archive'))
    parser.add_argument('--input-dir', type=Path, required=True)
    parser.add_argument('--producer-json', type=Path, required=True)
    parser.add_argument('--workspace', type=Path, required=True)
    args = parser.parse_args(argv)
    args.workspace.mkdir(parents=True, exist_ok=True)
    try:
        with (args.workspace / 'private-recovery.log').open('a') as log, redirect_stdout(log), redirect_stderr(log):
            request = request_from_env(os.environ)
            producer = json.loads(args.producer_json.read_bytes())
            params = (args.input_dir, producer, request, args.workspace, os.environ, build_client(), require_env('R2_BUCKET'))
            result = recover(*params, model=os.environ.get('SOURCE_MODEL', 'deepseek-flash'),
                             base_url=os.environ.get('SOURCE_BASE_URL', 'https://api.deepseek.com')) \
                if args.command == 'recover' else archive(*params)
        print(json.dumps({'stage': args.command, 'success': True, 'ocr_calls': 0, 'provider_posts': 0, **result}))
        return 0
    except Exception as error:
        import traceback
        with (args.workspace / 'private-recovery.log').open('a') as log:
            traceback.print_exc(file=log)
        category = public_error_category(error)
        print(json.dumps({'stage': args.command, 'success': False, 'category': category,
                          'ocr_calls': 0, 'provider_posts': 0}))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
