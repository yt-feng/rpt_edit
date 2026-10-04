"""Reserve a complete private original batch, then admit each root task once.

The immutable intake authority exists before any canonical claim or provider
POST. Resumption can finish only that authority's previously unsubmitted roots;
accepted and ambiguous submissions are never repeated. No polling, result ZIP,
OCR, model, source handoff or PDF operation is performed here.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import sys
import uuid

import archive_market_views_originals as archive
from mineru_task_ledger import Ledger, LedgerError, Provider, R2Store, digest, encoded, exact_json
from mineru_result_cache import ResultCache
from recover_durable_mineru_sources import OPTIONS, MANIFEST, decode, frozen_inputs, safe_ledger_error_category
from smoke_mineru_api import NoRedirectHTTP, credentials

WORKFLOW = '.github/workflows/market-views-fresh-mineru-intake.yml'
PREFIX = '_workflow-cache/mineru-fresh-intake/v1/dropbox'
POLICY = 'complete-archive-fresh-root-intake-v1'
MAX_AUTHORITY = 16 * 1024 * 1024
RUN = re.compile(r'[1-9][0-9]{0,19}')
SHA = re.compile(r'[a-f0-9]{40}')
HASH = re.compile(r'[a-f0-9]{64}')
SAFE_ERRORS = frozenset({
    'fresh_original_archive_not_verified', 'intake_authority_size', 'reviewed_fresh_intake_workflow_required',
    'intake_authority_mismatch', 'intake_existing_root_mismatch', 'ambiguous_intake_submission_retained',
    'intake_unsubmitted_root_mismatch', 'intake_initial_credential_unavailable', 'intake_claim_root_missing',
    'intake_existing_claim_mismatch', 'intake_accepted_claim_missing', 'intake_authorization_invalid',
    'existing_claims_without_intake_authority', 'intake_authority_readback_failed', 'intake_inputs_changed',
})


class IntakeError(ValueError):
    pass


def fail(category):
    raise IntakeError(category)


def verified_archive(input_dir, producer, archive_run_id, repository, expected_reports, date_folder):
    """Authenticate a fresh archive's complete inventory, including its receipt."""
    try:
        if not isinstance(archive_run_id, str) or not RUN.fullmatch(archive_run_id):
            raise ValueError('run')
        execution_sha = producer.get('head_sha') if isinstance(producer, dict) else None
        if not isinstance(execution_sha, str) or not SHA.fullmatch(execution_sha):
            raise ValueError('sha')
        archive.check_restore_producer(producer, archive_run_id, repository, execution_sha)
        context = archive.context(archive_run_id, date_folder, execution_sha, '')
        path = Path(input_dir) / archive.RECEIPT
        if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_AUTHORITY:
            raise ValueError('receipt')
        raw_receipt = path.read_bytes()
        receipt = archive.checked_receipt(decode(raw_receipt), context, expected_reports)
        raw, bindings, pairs = archive.checked_inputs(input_dir, expected_reports, date_folder)
        if (receipt['manifest_sha256'] != digest(raw) or not exact_json(receipt['original_inventory'], bindings)
                or path.read_bytes() != raw_receipt):
            raise ValueError('binding')
    except (ValueError, TypeError, AttributeError, KeyError, OSError):
        fail('fresh_original_archive_not_verified')
    authority = {'archive_context': context, 'archive_receipt_sha256': digest(raw_receipt),
                 'manifest_sha256': digest(raw), 'report_count': expected_reports, 'repository': repository}
    return authority, raw, pairs


class AuthorityStore:
    """Separate immutable storage; a failed create never grants a new claim."""
    def __init__(self, client, bucket):
        self.cache = ResultCache(client, bucket)

    def get(self, identity):
        raw = self.cache._read(f'{PREFIX}/{identity}/authority.json', maximum=MAX_AUTHORITY,
                              content_type='application/json', identity_sha=identity, allow_missing=True)
        return decode(raw) if raw is not None else None

    def create(self, identity, value):
        raw = encoded(value)
        if len(raw) > MAX_AUTHORITY:
            fail('intake_authority_size')
        self.cache._immutable(f'{PREFIX}/{identity}/authority.json', raw, content_type='application/json',
                              identity_sha=identity, maximum=MAX_AUTHORITY)


def require_cloud_main(env):
    repository = env.get('GITHUB_REPOSITORY', '')
    if (env.get('GITHUB_ACTIONS') != 'true' or env.get('GITHUB_EVENT_NAME') != 'workflow_dispatch'
            or env.get('GITHUB_REF') != 'refs/heads/main'
            or not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository)
            or env.get('GITHUB_WORKFLOW_REF') != repository + '/' + WORKFLOW + '@refs/heads/main'
            or not RUN.fullmatch(env.get('GITHUB_RUN_ID', '')) or not SHA.fullmatch(env.get('GITHUB_SHA', ''))):
        fail('reviewed_fresh_intake_workflow_required')


def _identity(original, ledger):
    return digest(encoded({'policy': POLICY, 'original': original,
                           'scope': ledger.scope, 'endpoint': ledger.endpoint, 'options': ledger.options}))


def _check_authority(value, original, bindings, ledger):
    keys = {'schema_version', 'policy', 'source_ready', 'complete_source_handoff', 'original',
            'initial_intake', 'source_bindings', 'batches'}
    if (not isinstance(value, dict) or set(value) != keys or type(value.get('schema_version')) is not int
            or value['schema_version'] != 1 or value['policy'] != POLICY or value['source_ready'] is not False
            or value['complete_source_handoff'] is not False or not exact_json(value['original'], original)
            or not exact_json(value['source_bindings'], bindings) or not isinstance(value['batches'], list)):
        fail('intake_authority_mismatch')
    initial = value['initial_intake']
    if (not isinstance(initial, dict) or set(initial) != {'run_id', 'execution_sha', 'workflow_path'}
            or not isinstance(initial['run_id'], str) or not RUN.fullmatch(initial['run_id'])
            or not isinstance(initial['execution_sha'], str) or not SHA.fullmatch(initial['execution_sha'])
            or initial['workflow_path'] != WORKFLOW or len(value['batches']) != (len(bindings) + 4) // 5):
        fail('intake_authority_mismatch')
    seen = set()
    for offset, batch in enumerate(value['batches']):
        expected = bindings[offset * 5:(offset + 1) * 5]
        if (not isinstance(batch, dict) or set(batch) != {'key', 'file_ids', 'initial_token_identity'}
                or not isinstance(batch['key'], str) or not re.fullmatch(r'batches/[a-f0-9]{32}', batch['key'])
                or batch['key'] in seen or batch['file_ids'] != [item['id'] for item in expected]
                or not isinstance(batch['initial_token_identity'], str) or not HASH.fullmatch(batch['initial_token_identity'])):
            fail('intake_authority_mismatch')
        seen.add(batch['key'])


def _planned_row(entry, bindings, ledger):
    ids = set(entry['file_ids'])
    return {'schema': 1, 'key': entry['key'], 'scope': ledger.scope, 'endpoint': ledger.endpoint,
            'options': ledger.options, 'token_identity': entry['initial_token_identity'],
            'files': [item for item in bindings if item['id'] in ids], 'state': 'claiming', 'batch_id': None}


def _check_existing(ledger, authority, bindings):
    """Check every root and claim before any canonical mutation or POST."""
    for entry in authority['batches']:
        expected = _planned_row(entry, bindings, ledger)
        row, _ = ledger.store.get(entry['key'])
        if row is not None:
            row, _ = ledger._read_batch(entry['key'])
            if ('recovery_parent' in row or not exact_json(row['files'], expected['files'])
                    or row['state'] not in {'claiming', 'auth_rejected', 'accepted', 'uploaded', 'terminal', 'submitting'}):
                fail('intake_existing_root_mismatch')
            rejections = row.get('auth_rejections', [])
            if ((rejections and rejections[0]['token_identity'] != entry['initial_token_identity'])
                    or (row['token_identity'] != entry['initial_token_identity'] and not rejections)):
                fail('intake_existing_root_mismatch')
            if row['state'] == 'submitting':
                fail('ambiguous_intake_submission_retained')
            if row['state'] == 'claiming' and not exact_json(row, expected):
                fail('intake_unsubmitted_root_mismatch')
            if row['state'] == 'auth_rejected':
                if not row.get('auth_rejections') or row['auth_rejections'][0]['token_identity'] != entry['initial_token_identity']:
                    fail('intake_existing_root_mismatch')
            if row['state'] in {'accepted', 'uploaded', 'terminal'} and (not isinstance(row.get('batch_id'), str) or not row['batch_id']):
                fail('intake_existing_root_mismatch')
        elif entry['initial_token_identity'] not in ledger.tokens:
            fail('intake_initial_credential_unavailable')
        for item in expected['files']:
            reference, _ = ledger.store.get('sources/' + item['id'])
            wanted = {'schema': 1, 'binding': item, 'batch_key': entry['key']}
            if reference is not None and row is None:
                fail('intake_claim_root_missing')
            if reference is not None and not exact_json(reference, wanted):
                fail('intake_existing_claim_mismatch')
            if row is not None and row['state'] in {'accepted', 'uploaded', 'terminal', 'auth_rejected'} and reference is None:
                fail('intake_accepted_claim_missing')


def intake_sources(ledger, authority_store, input_dir, producer, *, archive_run_id, repository,
                   expected_reports, date_folder, intake_run_id, execution_sha, timeout=1800):
    if (ledger.scope != 'dropbox' or ledger.endpoint != 'https://mineru.net' or not exact_json(ledger.options, OPTIONS)
            or not isinstance(intake_run_id, str) or not RUN.fullmatch(intake_run_id)
            or not isinstance(execution_sha, str) or not SHA.fullmatch(execution_sha)
            or type(timeout) not in (int, float) or not 0 < timeout <= 3600):
        fail('intake_authorization_invalid')
    original, manifest_raw, pairs = verified_archive(input_dir, producer, archive_run_id, repository, expected_reports, date_folder)
    bindings = [ledger.bind(path, name) for path, name in pairs]
    identity = _identity(original, ledger)
    authority = authority_store.get(identity)
    if authority is None:
        if any(ledger.store.get('sources/' + item['id'])[0] is not None for item in bindings):
            fail('existing_claims_without_intake_authority')
        token = next(iter(ledger.tokens))
        authority = {'schema_version': 1, 'policy': POLICY, 'source_ready': False, 'complete_source_handoff': False,
                     'original': original, 'initial_intake': {'run_id': intake_run_id, 'execution_sha': execution_sha,
                                                            'workflow_path': WORKFLOW},
                     'source_bindings': bindings,
                     'batches': [{'key': 'batches/' + uuid.uuid4().hex,
                                  'file_ids': [item['id'] for item in bindings[offset:offset + 5]],
                                  'initial_token_identity': token} for offset in range(0, len(bindings), 5)]}
        authority_store.create(identity, authority)
    stored = authority_store.get(identity)
    if not exact_json(stored, authority):
        fail('intake_authority_readback_failed')
    _check_authority(authority, original, bindings, ledger)
    _check_existing(ledger, authority, bindings)
    # All fifty bindings and root reservations precede the first provider POST.
    for entry in authority['batches']:
        expected = _planned_row(entry, bindings, ledger)
        if ledger.store.get(entry['key'])[0] is None:
            ledger.store.put(entry['key'], expected)
        for item in expected['files']:
            if ledger.store.get('sources/' + item['id'])[0] is None:
                ledger.store.put('sources/' + item['id'], {'schema': 1, 'binding': item, 'batch_key': entry['key']})
    _check_existing(ledger, authority, bindings)
    deadline, posted = ledger.clock() + timeout, 0
    paths = {item['id']: pair[0] for item, pair in zip(bindings, pairs)}
    for entry in authority['batches']:
        current, fresh_raw, _ = verified_archive(input_dir, producer, archive_run_id, repository, expected_reports, date_folder)
        if not exact_json(current, original) or fresh_raw != manifest_raw or not exact_json(authority_store.get(identity), authority):
            fail('intake_inputs_changed')
        _check_existing(ledger, authority, bindings)
        row, version = ledger._read_batch(entry['key'])
        if row['state'] in {'accepted', 'uploaded', 'terminal'}:
            continue
        # Only exact prepared claiming roots, or durable definitive credential
        # rejections, can reach the existing submission guard.
        if posted:
            ledger.sleep(10)
        ledger.submission_posts = 0
        ledger._submit_claimed(row, version, paths, deadline)
        posted += ledger.submission_posts
    current, fresh_raw, _ = verified_archive(input_dir, producer, archive_run_id, repository, expected_reports, date_folder)
    if not exact_json(current, original) or fresh_raw != manifest_raw:
        fail('intake_inputs_changed')
    _check_existing(ledger, authority, bindings)
    states = [ledger._read_batch(entry['key'])[0]['state'] for entry in authority['batches']]
    accepted = sum(state in {'accepted', 'uploaded', 'terminal'} for state in states)
    uploaded = sum(state in {'uploaded', 'terminal'} for state in states)
    return {'schema_version': 1, 'success': accepted == uploaded == len(states),
            'category': 'fresh_original_intake_complete' if accepted == uploaded == len(states) else 'accepted_upload_incomplete',
            'source_ready': False, 'complete_source_handoff': False, 'production_acceptance': False,
            'task_intake_only': True, 'archive_run_id': archive_run_id, 'date_folder': date_folder,
            'manifest_sha256': digest(manifest_raw), 'authority_identity_sha256': identity,
            'authority_sha256': digest(encoded(authority)), 'original_file_count': len(bindings),
            'planned_root_count': len(states), 'accepted_root_count': accepted, 'uploaded_root_count': uploaded,
            'provider_posts': posted, 'provider_gets': 0, 'result_gets': 0, 'model_calls': 0, 'pdf_count': 0}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-dir', type=Path, required=True)
    parser.add_argument('--producer-json', type=Path, required=True)
    parser.add_argument('--archive-run-id', required=True)
    parser.add_argument('--date-folder', required=True)
    parser.add_argument('--expected-reports', type=int, required=True)
    parser.add_argument('--summary', type=Path, required=True)
    args = parser.parse_args(argv)
    summary = {'schema_version': 1, 'success': False, 'category': 'fresh_intake_failed', 'source_ready': False,
               'complete_source_handoff': False, 'production_acceptance': False, 'task_intake_only': True,
               'model_calls': 0, 'pdf_count': 0, 'result_gets': 0, 'provider_gets': 0}
    try:
        require_cloud_main(os.environ)
        if args.producer_json.is_symlink() or not args.producer_json.is_file():
            fail('fresh_original_archive_not_verified')
        producer = decode(args.producer_json.read_bytes())
        import boto3
        import requests
        from botocore.config import Config
        from private_workflow_handoff import require_env
        client = boto3.client('s3', endpoint_url=f'https://{require_env("R2_ACCOUNT_ID")}.r2.cloudflarestorage.com',
            aws_access_key_id=require_env('R2_ACCESS_KEY_ID'), aws_secret_access_key=require_env('R2_SECRET_ACCESS_KEY'),
            region_name='auto', config=Config(connect_timeout=20, read_timeout=30,
            retries={'total_max_attempts': 1, 'mode': 'standard'}))
        bucket = require_env('R2_BUCKET')
        ledger = Ledger(R2Store('dropbox', client, bucket), Provider(NoRedirectHTTP(requests.request), 'https://mineru.net'),
                        'dropbox', 'https://mineru.net', OPTIONS, credentials(os.environ))
        summary = intake_sources(ledger, AuthorityStore(client, bucket), args.input_dir, producer,
            archive_run_id=args.archive_run_id, repository=os.environ['GITHUB_REPOSITORY'],
            expected_reports=args.expected_reports, date_folder=args.date_folder,
            intake_run_id=os.environ['GITHUB_RUN_ID'], execution_sha=os.environ['GITHUB_SHA'])
        code = 0 if summary['success'] else 3
    except Exception as error:
        if type(error) is IntakeError and str(error) in SAFE_ERRORS:
            summary['category'] = str(error)
        elif isinstance(error, LedgerError):
            summary['category'] = safe_ledger_error_category(error)
        code = 2
    try:
        from audit_market_views_ocr_receipt import write_summary
        write_summary(args.summary, summary, source_dir=args.input_dir)
    except Exception:
        print('Fresh intake stopped: diagnostic_output_invalid', file=sys.stderr)
        return 2
    print(json.dumps(summary, sort_keys=True))
    return code


if __name__ == '__main__':
    raise SystemExit(main())
