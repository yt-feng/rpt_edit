"""Manually cache done results of exact accepted original Daily tasks, with zero POSTs.

All original file bytes and every batch's complete terminal membership are
verified before any result request. Failed parses are counted, never resubmitted.
Cache seeding is not a complete source handoff or a restored PDF pipeline.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys

from inspect_legacy_mineru import ENDPOINT, get_once, valid_uuid
from mineru_task_ledger import DONE, FAILED, Ledger, R2Store, digest, encoded
from mineru_result_cache import ResultCache, MAX_RECEIPT, identity, validate_zip
from mineru_pinned_result_transport import (AUTH_MODE, PinnedResultTransport, PinnedTransportError,
                                           prepare_authentication, require_before_cutoff, require_cloud_manual,
                                           fixed_result_uri, verified_authentication)
from recover_durable_mineru_sources import (MANIFEST, OPTIONS, check_producer, decode, frozen_inputs,
                                           original_groups, assert_inputs)
from smoke_mineru_api import credentials

AUTH_PREFIX = '_workflow-cache/mineru-result-auth/v1/dropbox'
SAFE_ERRORS = {
    'canonical_ledger_writes_forbidden', 'accepted_batch_get_rejected', 'accepted_batch_get_invalid',
    'provider_posts_forbidden', 'provider_uploads_forbidden', 'complete_terminal_task_required',
    'authentication_receipt_size', 'read_only_original_dropbox_required', 'read_only_ledger_required',
    'result_limit_invalid', 'exact_original_date_required', 'accepted_original_tasks_required',
    'complete_original_membership_required', 'original_manifest_changed', 'cache_readback_failed',
    'source_run_invalid', 'original_producer_invalid', 'completed_original_producer_required',
    'pinned_auth_window_closed', 'reviewed_manual_cloud_required', 'fixed_result_origin_required',
    'expected_leaf_expiry_not_observed', 'complete_peer_chain_required', 'fixed_leaf_fingerprint_mismatch',
    'fixed_leaf_metadata_mismatch', 'peer_intermediate_not_current', 'historical_chain_or_hostname_failed',
    'authentication_preflight_failed', 'prepared_authentication_required', 'result_http_rejected',
    'result_content_encoding_rejected', 'result_size_rejected', 'result_read_budget_exhausted',
    'result_body_invalid', 'result_body_incomplete', 'pinned_result_transport_failed', 'no_done_results',
}


class SeedError(ValueError):
    """Fixed categories only, with no source names or API response text."""


class ReadOnlyStore:
    def __init__(self, original):
        self.original = original

    def get(self, key):
        return self.original.get(key)

    def put(self, *args, **kwargs):
        raise SeedError('canonical_ledger_writes_forbidden')


class SingleGetProvider:
    """A fixed official read endpoint, no POST/upload method or repeat GET."""
    def __init__(self, getter=get_once):
        self.getter, self.seen = getter, set()

    def poll(self, batch_id, token, timeout):
        if not valid_uuid(batch_id) or batch_id in self.seen:
            raise SeedError('accepted_batch_get_rejected')
        self.seen.add(batch_id)
        status, raw = self.getter(ENDPOINT + batch_id, token, 20)
        data = decode(raw)
        body = data.get('data') if isinstance(data, dict) else None
        code = data.get('code') if isinstance(data, dict) else None
        if (type(status) is not int or status != 200
                or not (type(code) is int and code == 0 or type(code) is str and code == '0')
                or not isinstance(body, dict) or body.get('batch_id', batch_id) != batch_id):
            raise SeedError('accepted_batch_get_invalid')
        return body.get('extract_result')

    def submit(self, *args, **kwargs):
        raise SeedError('provider_posts_forbidden')

    def upload(self, *args, **kwargs):
        raise SeedError('provider_uploads_forbidden')


def stop_polling(_):
    raise SeedError('complete_terminal_task_required')


class CutoffCacheClient:
    """Recheck the fixed window before each immutable R2 publication."""
    def __init__(self, client, cutoff_check):
        self.client, self.cutoff_check = client, cutoff_check

    def get_object(self, **kwargs):
        return self.client.get_object(**kwargs)

    def put_object(self, **kwargs):
        self.cutoff_check()
        return self.client.put_object(**kwargs)


def write_authentication(cache, binding, lineage, payload, authentication):
    authentication = verified_authentication(authentication)
    identity_sha = identity(binding, lineage)
    zip_sha = digest(payload)
    receipt = {'schema_version': 1, 'policy': 'manual-exact-leaf-result-cache-v1',
               'identity_sha256': identity_sha, 'source_binding': binding, 'lineage': lineage,
               'zip_sha256': zip_sha, 'zip_bytes': len(payload), 'authentication': authentication}
    raw = encoded(receipt)
    if len(raw) > MAX_RECEIPT:
        raise SeedError('authentication_receipt_size')
    cache._immutable(f'{AUTH_PREFIX}/{identity_sha}/{zip_sha}.json', raw,
                     content_type='application/json', identity_sha=identity_sha, maximum=MAX_RECEIPT)
    return digest(raw)


def seed_results(ledger, input_dir, manifest, expected_reports, date_folder, source_run_id, cache, *,
                 max_results=1, transport_factory=None, cutoff_check=require_before_cutoff):
    if ledger.scope != 'dropbox' or ledger.options != OPTIONS or not isinstance(ledger.provider, SingleGetProvider):
        raise SeedError('read_only_original_dropbox_required')
    if not isinstance(ledger.store, ReadOnlyStore):
        raise SeedError('read_only_ledger_required')
    if type(max_results) is not int or max_results not in (0, 1):
        raise SeedError('result_limit_invalid')
    cutoff_check()
    raw, bindings, pairs = frozen_inputs(input_dir, manifest, expected_reports, date_folder)
    rows = decode(raw)
    if any(PurePosixPath(row['dropbox_path']).parts[:3] != ('/', 'zip_backup', date_folder) for row in rows):
        raise SeedError('exact_original_date_required')
    groups, fresh = original_groups(ledger, pairs, source_run_id=source_run_id, allow_fresh=False)
    if fresh or not groups:
        raise SeedError('accepted_original_tasks_required')
    done, failed = [], 0
    # Every GET is single-attempt and read-only. Missing/nonterminal members
    # reject the whole preflight before a single ZIP connection is attempted.
    for batch, _ in groups:
        cutoff_check()
        results, counts = ledger._poll(batch['key'], batch['files'], ledger.clock() + 60, 1, 0,
                                       persist_terminal=False)
        if counts['missing'] or counts['pending'] or len(results) != len(batch['files']):
            raise SeedError('complete_terminal_task_required')
        for binding in batch['files']:
            row = results[binding['id']]
            if str(row['state']).lower() in FAILED:
                failed += 1
                continue
            if str(row['state']).lower() not in DONE:
                raise SeedError('complete_terminal_task_required')
            fixed_result_uri(row['full_zip_url'])
            lineage = {'batch_id': batch['batch_id'], 'batch_key': batch['key'],
                       'parent_batch_key': batch['key'], 'child_ordinal': 0, 'data_id': binding['id']}
            identity(binding, lineage)
            done.append((binding, lineage, row['full_zip_url']))
    if len(done) + failed != expected_reports:
        raise SeedError('complete_original_membership_required')
    if not done:
        raise SeedError('no_done_results')
    if Path(manifest).read_bytes() != raw:
        raise SeedError('original_manifest_changed')
    assert_inputs(ledger, pairs, bindings)
    selected = done if max_results == 0 else done[:max_results]
    summary = {'schema_version': 1, 'status': 'cache_seed_only', 'complete_source_handoff': False,
               'production_acceptance': False, 'pipeline_restored': False,
               'requested_auth_mode': AUTH_MODE, 'pki_verified_now': False,
               'original_members_verified': expected_reports, 'completed_members': len(done),
               'failed_members': failed, 'selected_results': len(selected), 'cached_results': 0,
               'existing_cache_hits': 0, 'new_result_downloads': 0, 'provider_gets': len(groups),
               'provider_posts': 0, 'canonical_ledger_writes': 0, 'model_calls': 0, 'pdf_count': 0,
               'manifest_sha256': digest(raw), 'results': []}
    transport = None
    for binding, lineage, url in selected:
        cutoff_check()
        payload = cache.get(binding, lineage)
        hit = payload is not None
        auth_sha = None
        if not hit:
            if transport is None:
                transport = (transport_factory() if transport_factory is not None
                             else PinnedResultTransport(prepare_authentication()))
                verified_authentication(transport.authentication)
            payload = transport(url)
            validate_zip(payload)
            if Path(manifest).read_bytes() != raw:
                raise SeedError('original_manifest_changed')
            assert_inputs(ledger, pairs, bindings)
            cutoff_check()
            auth_sha = write_authentication(cache, binding, lineage, payload, transport.authentication)
            cutoff_check()
            cache.put(binding, lineage, payload)
            summary['new_result_downloads'] += 1
        else:
            summary['existing_cache_hits'] += 1
        if cache.get(binding, lineage) != payload:
            raise SeedError('cache_readback_failed')
        summary['cached_results'] += 1
        summary['results'].append({'identity_sha256': identity(binding, lineage), 'zip_sha256': digest(payload),
                                   'zip_bytes': len(payload), 'authentication_receipt_sha256': auth_sha,
                                   'auth_mode': 'existing_verified_cache' if hit else AUTH_MODE})
    summary['all_done_results_cached'] = len(selected) == len(done) == summary['cached_results']
    summary['result_gets'] = transport.result_gets if transport is not None else 0
    summary['authentication'] = transport.authentication if transport is not None else None
    summary['success'] = summary['cached_results'] == len(selected)
    return summary


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-dir', type=Path, required=True)
    parser.add_argument('--producer-json', type=Path, required=True)
    parser.add_argument('--source-run-id', required=True)
    parser.add_argument('--date-folder', required=True)
    parser.add_argument('--expected-reports', type=int, required=True)
    parser.add_argument('--max-results', choices=('1', 'all'), default='1')
    parser.add_argument('--summary', type=Path, required=True)
    args = parser.parse_args(argv)
    summary = {'schema_version': 1, 'success': False, 'category': 'seed_failed', 'provider_posts': 0,
               'model_calls': 0, 'pdf_count': 0, 'complete_source_handoff': False,
               'production_acceptance': False, 'pipeline_restored': False}
    try:
        require_cloud_manual()
        require_before_cutoff()
        if not re.fullmatch(r'[1-9][0-9]{0,19}', args.source_run_id):
            raise SeedError('source_run_invalid')
        if args.producer_json.is_symlink() or not args.producer_json.is_file():
            raise SeedError('original_producer_invalid')
        producer = decode(args.producer_json.read_bytes())
        check_producer(producer, args.source_run_id, os.environ.get('GITHUB_REPOSITORY', ''))
        if producer.get('status') != 'completed' or producer.get('conclusion') not in {'success', 'failure'}:
            raise SeedError('completed_original_producer_required')
        import boto3
        from botocore.config import Config
        from private_workflow_handoff import require_env
        client = boto3.client('s3', endpoint_url=f"https://{require_env('R2_ACCOUNT_ID')}.r2.cloudflarestorage.com",
                             aws_access_key_id=require_env('R2_ACCESS_KEY_ID'),
                             aws_secret_access_key=require_env('R2_SECRET_ACCESS_KEY'), region_name='auto',
                             config=Config(connect_timeout=20, read_timeout=30,
                                           retries={'total_max_attempts': 1, 'mode': 'standard'}))
        bucket = require_env('R2_BUCKET')
        store = ReadOnlyStore(R2Store('dropbox', client=client, bucket=bucket))
        ledger = Ledger(store, SingleGetProvider(), 'dropbox', 'https://mineru.net', OPTIONS,
                        credentials(os.environ), sleep=stop_polling)
        cache = ResultCache(CutoffCacheClient(client, require_before_cutoff), bucket)
        summary = seed_results(ledger, args.input_dir, args.input_dir / MANIFEST, args.expected_reports,
                               args.date_folder, args.source_run_id, cache,
                               max_results=0 if args.max_results == 'all' else 1)
        code = 0 if summary['success'] else 3
    except Exception as error:
        # Nested source/provider validators may contain private report names.
        # No raw exception, response, URL, credential or filename is published.
        if isinstance(error, (SeedError, PinnedTransportError)) and str(error) in SAFE_ERRORS:
            summary['category'] = str(error)
        code = 2
    try:
        from audit_market_views_ocr_receipt import write_summary
        write_summary(args.summary, summary, source_dir=args.input_dir)
    except Exception:
        print('Result cache seeding stopped: diagnostic_output_invalid', file=sys.stderr)
        return 2
    print(json.dumps(summary, sort_keys=True))
    return code


if __name__ == '__main__':
    raise SystemExit(main())
