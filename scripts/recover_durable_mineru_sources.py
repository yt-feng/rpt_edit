"""Recover exact original MinerU tasks into a complete, private source handoff.

The reviewed Actions caller freezes the complete original manifest and PDF bytes.
Existing source claims reconstruct their original groups; no regrouping can turn a
missing or failed member into a fresh submission. PDF/LLM generation is downstream.
"""
from __future__ import annotations

import argparse
from contextlib import redirect_stderr, redirect_stdout
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import sys
import tempfile

from consume_legacy_mineru import (ConsumerError, NetworkStop, chart_assets,
                                 download_once, safe_unzip, valid_url)
from mineru_task_ledger import (DONE, FAILED, Ledger, LedgerError, Provider, R2Store,
                               digest, encoded, exact_json, schema_v1)
from mineru_terminal_recovery import TerminalRecovery, task_identity
from smoke_mineru_api import NoRedirectHTTP, credentials

WORKFLOW = '.github/workflows/market-views-mineru-recovery.yml'
PRODUCER = '.github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml'
POLICY = 'durable-mineru-complete-market-source-v1'
MANIFEST = 'selected_to_process_manifest.json'
RECEIPT = 'source-recovery-receipt.json'
OPTIONS = {'model': 'vlm', 'language': 'en', 'ocr': True}
HASH = re.compile(r'[a-f0-9]{64}')
RUN = re.compile(r'[1-9][0-9]{0,19}')
MAX_RECEIPT = 16 * 1024 * 1024


class RecoveryError(ValueError):
    """Fixed public categories only; private provider rows never escape."""


def reject(category):
    raise RecoveryError(category)


def decode(raw):
    if not isinstance(raw, bytes) or not 1 <= len(raw) <= MAX_RECEIPT:
        reject('metadata_size')
    def pairs(entries):
        result = {}
        for key, value in entries:
            if key in result:
                reject('metadata_duplicate_key')
            result[key] = value
        return result
    try:
        return json.loads(raw, object_pairs_hook=pairs)
    except (ValueError, UnicodeError):
        reject('metadata_json')


def exact_date(value):
    if not isinstance(value, str) or not re.fullmatch(r'[0-9]{6}', value):
        reject('date_contract')
    from datetime import datetime
    try:
        datetime.strptime(value, '%y%m%d')
    except ValueError:
        reject('date_contract')
    return value


def manifest_bindings(raw, expected_reports, date_folder):
    exact_date(date_folder)
    rows = decode(raw)
    if (type(expected_reports) is not int or not 1 <= expected_reports <= 1000
            or not isinstance(rows, list) or len(rows) != expected_reports):
        reject('manifest_count')
    result = []
    for row in rows:
        if not isinstance(row, dict):
            reject('manifest_entry')
        local = row.get('process_local_path')
        sha = row.get('content_sha256')
        dropbox = row.get('dropbox_path')
        if (not isinstance(local, str) or not local or '\\' in local
                or any(ord(char) < 32 for char in local)):
            reject('manifest_filename')
        source = PurePosixPath(local).name
        if (not source or not source.lower().endswith('.pdf') or ':' in source
                or len(source) > 512 or not isinstance(sha, str) or not HASH.fullmatch(sha)):
            reject('manifest_binding')
        if (not isinstance(dropbox, str) or '\\' in dropbox
                or date_folder not in PurePosixPath(dropbox).parts
                or '..' in PurePosixPath(dropbox).parts):
            reject('manifest_date')
        original = row.get('name', source)
        if not isinstance(original, str) or not original or any(ord(char) < 32 for char in original):
            reject('manifest_original_filename')
        result.append({'source_pdf': source, 'original_filename': original,
                       'content_sha256': sha, 'dropbox_path': dropbox})
    if len({item['source_pdf'] for item in result}) != len(result):
        reject('manifest_duplicate_filename')
    return result


def check_producer(value, source_run_id, repository):
    if (not isinstance(value, dict) or value.get('id') != int(source_run_id)
            or value.get('path') != PRODUCER or value.get('head_branch') != 'main'
            or value.get('repository', {}).get('full_name') != repository
            or not re.fullmatch(r'[a-f0-9]{40}', str(value.get('head_sha', '')))):
        reject('original_producer')
    return value['head_sha']


def frozen_inputs(input_dir, manifest_path, expected_reports, date_folder):
    root = Path(input_dir)
    manifest_path = Path(manifest_path)
    if root.is_symlink() or manifest_path.is_symlink() or not manifest_path.is_file():
        reject('input_regular_files')
    raw = manifest_path.read_bytes()
    bindings = manifest_bindings(raw, expected_reports, date_folder)
    inventory = {}
    for path in root.rglob('*'):
        if path.is_symlink():
            reject('input_symlink')
        if path.is_file() and path.suffix.lower() == '.pdf':
            if path.name in inventory:
                reject('input_duplicate_filename')
            inventory[path.name] = path
    if set(inventory) != {item['source_pdf'] for item in bindings}:
        reject('input_inventory')
    pairs = []
    for item in bindings:
        path = inventory[item['source_pdf']]
        payload = path.read_bytes()
        if not payload.startswith(b'%PDF-') or digest(payload) != item['content_sha256']:
            reject('input_pdf_hash')
        pairs.append((path, item['source_pdf']))
    return raw, bindings, pairs


def original_groups(ledger, pairs, *, source_run_id, allow_fresh):
    items = [ledger.bind(path, source) for path, source in pairs]
    inputs = {item['id']: pair for item, pair in zip(items, pairs)}
    references = [ledger.store.get('sources/' + item['id'])[0] for item in items]
    missing = sum(reference is None for reference in references)
    if missing:
        if missing != len(items) or source_run_id or allow_fresh is not True:
            reject('missing_original_claim')
        return [], [pairs[offset:offset + 5] for offset in range(0, len(pairs), 5)]
    groups = {}
    for item, reference in zip(items, references):
        if (not schema_v1(reference) or not exact_json(reference.get('binding'), item)
                or not isinstance(reference.get('batch_key'), str)):
            reject('original_claim_binding')
        groups.setdefault(reference['batch_key'], []).append(item)
    result = []
    for key, requested in groups.items():
        batch, _ = ledger._read_batch(key)
        if ('recovery_parent' in batch or batch['state'] not in {'accepted', 'uploaded', 'terminal'}
                or not isinstance(batch.get('batch_id'), str) or not batch['batch_id']):
            reject('original_task_not_accepted')
        bound = {item['id']: item for item in batch['files']}
        if (set(bound) != {item['id'] for item in requested}
                or any(not exact_json(bound.get(item['id']), item) for item in requested)):
            reject('original_task_inventory')
        result.append((batch, [inputs[item['id']] for item in batch['files']]))
    return result, []


def assert_inputs(ledger, pairs, bindings):
    for (path, source), binding in zip(pairs, bindings):
        item = ledger.bind(path, source)
        if item['sha256'] != binding['content_sha256']:
            reject('input_changed')


def regular_inventory(root):
    files = []
    for path in sorted(Path(root).rglob('*')):
        if path.is_symlink():
            reject('output_symlink')
        if path.is_file() and path != Path(root) / RECEIPT:
            raw = path.read_bytes()
            files.append({'path': path.relative_to(root).as_posix(), 'sha256': digest(raw), 'bytes': len(raw)})
    return files


def validate_sources(output_dir, expected_reports, date_folder, *, expected_recovery_run_id=None,
                     expected_execution_sha=None):
    root = Path(output_dir)
    if root.is_symlink() or not root.is_dir():
        reject('output_directory')
    receipt_path = root / RECEIPT
    if receipt_path.is_symlink() or not receipt_path.is_file():
        reject('receipt_missing')
    receipt = decode(receipt_path.read_bytes())
    expected_keys = {'schema_version', 'policy', 'date_folder', 'source_run_id', 'recovery_run_id',
                     'source_execution_sha', 'recovery_execution_sha', 'manifest_sha256', 'original_inventory', 'report_count',
                     'original_tasks', 'provider_posts', 'reports', 'files'}
    if (not isinstance(receipt, dict) or set(receipt) != expected_keys
            or type(receipt['schema_version']) is not int or receipt['schema_version'] != 1
            or receipt['policy'] != POLICY or receipt['date_folder'] != exact_date(date_folder)
            or receipt['report_count'] != expected_reports or type(receipt['report_count']) is not int
            or not isinstance(receipt['recovery_run_id'], str) or not RUN.fullmatch(receipt['recovery_run_id'])
            or not isinstance(receipt['source_run_id'], str)
            or (receipt['source_run_id'] and not RUN.fullmatch(receipt['source_run_id']))
            or not re.fullmatch(r'[a-f0-9]{40}', str(receipt['source_execution_sha']))
            or not re.fullmatch(r'[a-f0-9]{40}', str(receipt['recovery_execution_sha']))
            or type(receipt['provider_posts']) is not int or receipt['provider_posts'] < 0):
        reject('receipt_contract')
    if (expected_recovery_run_id is not None
            and (not isinstance(expected_recovery_run_id, str) or not RUN.fullmatch(expected_recovery_run_id)
                 or receipt['recovery_run_id'] != expected_recovery_run_id)):
        reject('receipt_recovery_run')
    if (expected_execution_sha is not None
            and (not isinstance(expected_execution_sha, str) or not re.fullmatch(r'[a-f0-9]{40}', expected_execution_sha)
                 or receipt['recovery_execution_sha'] != expected_execution_sha)):
        reject('receipt_execution_sha')
    manifest_path = root / MANIFEST
    if manifest_path.is_symlink() or not manifest_path.is_file():
        reject('manifest_missing')
    raw = manifest_path.read_bytes()
    bindings = manifest_bindings(raw, expected_reports, date_folder)
    if (receipt['manifest_sha256'] != digest(raw)
            or not exact_json(receipt['original_inventory'], bindings)
            or not exact_json(receipt['files'], regular_inventory(root))):
        reject('receipt_inventory_hash')
    tasks = receipt['original_tasks']
    if not isinstance(tasks, list) or not tasks:
        reject('receipt_tasks')
    task_map, admitted = {}, []
    for task in tasks:
        if (not isinstance(task, dict) or set(task) != {'key', 'task_identity_sha256', 'batch_id', 'data_ids'}
                or not re.fullmatch(r'batches/[a-f0-9]{32}', str(task['key']))
                or not HASH.fullmatch(str(task['task_identity_sha256']))
                or not isinstance(task['batch_id'], str) or not task['batch_id']
                or not isinstance(task['data_ids'], list) or not 1 <= len(task['data_ids']) <= 5
                or any(not isinstance(value, str) or not HASH.fullmatch(value) for value in task['data_ids'])
                or len(set(task['data_ids'])) != len(task['data_ids']) or task['key'] in task_map):
            reject('receipt_task_binding')
        task_map[task['key']] = task
        admitted.extend(task['data_ids'])
    reports = receipt['reports']
    if (not isinstance(reports, list) or len(reports) != expected_reports
            or len(admitted) != expected_reports or len(set(admitted)) != len(admitted)):
        reject('receipt_source_count')
    identities = []
    for report, binding in zip(reports, bindings):
        if (not isinstance(report, dict) or set(report) != {'directory', 'binding', 'source_binding', 'source_id', 'task',
                                                        'zip_sha256', 'source_markdown_sha256'}
                or not exact_json(report['binding'], binding)
                or not isinstance(report['source_id'], str) or not HASH.fullmatch(report['source_id'])
                or not re.fullmatch(r'report_[0-9]{4}_[a-f0-9]{12}', str(report['directory']))
                or not HASH.fullmatch(str(report['zip_sha256']))
                or not HASH.fullmatch(str(report['source_markdown_sha256']))):
            reject('receipt_report_binding')
        source_binding = report['source_binding']
        if (not isinstance(source_binding, dict)
                or set(source_binding) != {'id', 'source', 'sha256', 'size', 'scope', 'endpoint', 'options'}
                or source_binding['id'] != report['source_id'] or source_binding['source'] != binding['source_pdf']
                or source_binding['sha256'] != binding['content_sha256']
                or type(source_binding['size']) is not int or source_binding['size'] <= 0
                or source_binding['scope'] != 'dropbox' or source_binding['endpoint'] != 'https://mineru.net'
                or not exact_json(source_binding['options'], OPTIONS)
                or digest(encoded({key: value for key, value in source_binding.items() if key != 'id'})) != report['source_id']):
            reject('receipt_source_binding')
        lineage = report['task']
        if (not isinstance(lineage, dict) or set(lineage) != {'root_key', 'batch_key', 'batch_id', 'data_id', 'parent_batch_key', 'child_ordinal'}
                or lineage['root_key'] not in task_map
                or report['source_id'] not in task_map[lineage['root_key']]['data_ids']
                or lineage['data_id'] != report['source_id']
                or not re.fullmatch(r'batches/[a-f0-9]{32}', str(lineage['batch_key']))
                or not isinstance(lineage['batch_id'], str) or not lineage['batch_id']
                or type(lineage['child_ordinal']) is not int or not 0 <= lineage['child_ordinal'] <= 2
                or lineage['parent_batch_key'] != lineage['root_key']
                or (lineage['child_ordinal'] == 0 and (lineage['batch_key'] != lineage['root_key']
                    or lineage['batch_id'] != task_map[lineage['root_key']]['batch_id']))
                or (lineage['child_ordinal'] > 0 and (lineage['batch_key'] == lineage['root_key']
                    or lineage['parent_batch_key'] == lineage['batch_key']))):
            reject('receipt_lineage')
        directory = root / report['directory']
        status_path, source_path = directory / 'status.json', directory / 'source_mineru.md'
        if not status_path.is_file() or not source_path.is_file():
            reject('report_missing')
        status = decode(status_path.read_bytes())
        markdown = source_path.read_bytes()
        if (not markdown.strip() or digest(markdown) != report['source_markdown_sha256']
                or not isinstance(status, dict) or status.get('source_pdf') != binding['source_pdf']
                or status.get('original_filename') != binding['original_filename']
                or status.get('original_pdf_sha256') != binding['content_sha256']
                or status.get('mineru_state') != 'done' or status.get('chart_source_only') is not True
                or status.get('source_markdown') != 'source_mineru.md'
                or not exact_json(status.get('mineru_recovery'), report['task'])
                or not isinstance(status.get('images'), list)
                or not all(isinstance(image, str) for image in status['images'])
                or not 0 <= len(status['images']) <= 100
                or type(status.get('chart_source_image_count')) is not int
                or status['chart_source_image_count'] != len(status['images'])
                or len(set(status['images'])) != len(status['images'])):
            reject('report_status')
        for ordinal, image in enumerate(status['images'], 1):
            if (not isinstance(image, str)
                    or not re.fullmatch(r'assets/source_image_' + f'{ordinal:02d}' + r'\.(?:png|jpe?g|webp|gif|bmp|tiff?)', image)
                    or not (directory / image).is_file()):
                reject('report_image')
        mapping = decode((directory / 'source_image_map.json').read_bytes())
        if (not isinstance(mapping, dict) or set(mapping) != {'version', 'source_sha256', 'images'}
                or type(mapping['version']) is not int or mapping['version'] != 1
                or mapping.get('source_sha256') != digest(markdown)
                or not isinstance(mapping.get('images'), dict)
                or any(not isinstance(ref, str) or not ref or target not in status['images']
                       for ref, target in mapping['images'].items())
                or set(mapping['images'].values()) != set(status['images'])):
            reject('report_image_map')
        identities.append(report['source_id'])
    if set(identities) != set(admitted) or len(set(identities)) != expected_reports:
        reject('receipt_admission_coverage')
    return receipt


def recover_sources(ledger, input_dir, manifest_path, output_dir, expected_reports, date_folder, *,
                    source_run_id='', allow_fresh=False, recovery_run_id, source_execution_sha,
                    recovery_execution_sha=None,
                    allowed_error_codes=(), allowed_error_hashes=(), downloader=download_once,
                    asset_writer=chart_assets, timeout=1800, interval=15, queue_budget=300):
    if ledger.scope != 'dropbox' or not exact_json(ledger.options, OPTIONS):
        reject('ledger_scope_options')
    if (not RUN.fullmatch(str(recovery_run_id)) or (source_run_id and not RUN.fullmatch(str(source_run_id)))
            or not re.fullmatch(r'[a-f0-9]{40}', source_execution_sha)):
        reject('recovery_authorization')
    if recovery_execution_sha is None:
        recovery_execution_sha = source_execution_sha
    if not isinstance(recovery_execution_sha, str) or not re.fullmatch(r'[a-f0-9]{40}', recovery_execution_sha):
        reject('recovery_execution_sha')
    raw_manifest, bindings, pairs = frozen_inputs(input_dir, manifest_path, expected_reports, date_folder)
    groups, fresh = original_groups(ledger, pairs, source_run_id=source_run_id, allow_fresh=allow_fresh)
    destination = Path(output_dir)
    if destination.exists() or destination.is_symlink():
        reject('destination_exists')
    destination.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix='.mineru-market-source-', dir=destination.parent))
    complete = False
    try:
        with tempfile.TemporaryDirectory(prefix='mineru-source-results-') as cache_dir:
            cache, root_for_id, resolved, posts, tasks = {}, {}, {}, 0, []
            allowed_ids = {ledger.bind(path, source)['id'] for path, source in pairs}
            def verify_done(path, row):
                if str(row.get('state', '')).lower() not in DONE:
                    return
                source_id = row.get('data_id')
                if source_id not in allowed_ids:
                    reject('result_unknown_source')
                url = row.get('full_zip_url'); valid_url(url)
                cache_key = (source_id, url)
                if cache_key not in cache:
                    payload = downloader(url)
                    folder = Path(cache_dir) / str(len(cache))
                    markdown = safe_unzip(payload, folder / 'raw')
                    cache[cache_key] = (folder / 'raw', markdown, digest(payload))
            def record_task(batch):
                tasks.append({'key': batch['key'], 'task_identity_sha256': task_identity(batch),
                              'batch_id': batch['batch_id'], 'data_ids': [item['id'] for item in batch['files']]})
                for item in batch['files']:
                    root_for_id[item['id']] = batch['key']
            terminal = TerminalRecovery(ledger, allowed_error_codes=allowed_error_codes,
                                        allowed_error_hashes=allowed_error_hashes)
            # Complete all original GETs and validate every successful original ZIP
            # before even one failed member can be admitted to a recovery child.
            preflight = []
            for batch, group_pairs in groups:
                rows, summary = ledger._poll(batch['key'], batch['files'], ledger.clock() + timeout,
                                             interval, queue_budget, persist_terminal=False)
                if (summary['missing'] or summary['pending'] or len(rows) != len(batch['files'])):
                    reject('original_task_incomplete')
                terminal._proof(batch, rows)  # Validate every original failure before any child POST.
                preflight.append(rows)
                record_task(batch)
            for rows in preflight:
                for row in rows.values():
                    verify_done(None, row)
            assert_inputs(ledger, pairs, bindings)
            for batch, group_pairs in groups:
                rows, summary = terminal.run(group_pairs,
                    authorization={'run_id': str(recovery_run_id), 'manifest_sha256': digest(raw_manifest)},
                    timeout=timeout, interval=interval, queue_budget=queue_budget, done_verifier=verify_done)
                posts += summary['provider_posts']
                if summary.get('ready_for_generation') is not True or len(rows) != len(group_pairs):
                    reject('recovery_task_incomplete')
                for path, row in rows:
                    verify_done(path, row)
                    resolved[row['data_id']] = row
            for group_pairs in fresh:
                rows, summary = ledger.run(group_pairs, timeout=timeout, interval=interval, queue_budget=queue_budget)
                posts += summary['provider_posts']
                if summary.get('ready_for_generation') is not True or len(rows) != len(group_pairs):
                    reject('fresh_task_incomplete')
                batch, _ = ledger._read_batch(summary['batch_keys'][0]); record_task(batch)
                for path, row in rows:
                    verify_done(path, row)
                    row['_recovery_lineage'] = {'batch_key': batch['key'], 'batch_id': batch['batch_id'],
                        'parent_batch_key': batch['key'], 'child_ordinal': 0, 'data_id': row['data_id']}
                    resolved[row['data_id']] = row
                if group_pairs is not fresh[-1]:
                    ledger.sleep(10)  # At most five fresh files per ten seconds.
            assert_inputs(ledger, pairs, bindings)
            if len(resolved) != expected_reports:
                reject('complete_source_gate')
            reports = []
            for index, ((path, source), binding) in enumerate(zip(pairs, bindings), 1):
                source_id = ledger.bind(path, source)['id']
                row = resolved.get(source_id)
                if row is None or str(row.get('state', '')).lower() not in DONE:
                    reject('complete_source_gate')
                raw_dir, markdown, zip_sha = cache[(source_id, row['full_zip_url'])]
                directory_name = f'report_{index:04d}_{source_id[:12]}'
                directory = stage / directory_name; directory.mkdir()
                (directory / 'source_mineru.md').write_bytes(markdown)
                assets = directory / 'assets'; assets.mkdir()
                with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                    images = asset_writer(raw_dir, assets, 100)
                value = row.get('_recovery_lineage')
                if not isinstance(value, dict):
                    reject('result_lineage_missing')
                if set(value) != {'batch_id', 'batch_key', 'parent_batch_key', 'data_id', 'child_ordinal'}:
                    reject('result_lineage_contract')
                task = dict(value, root_key=root_for_id[source_id])
                status = {'source_pdf': source, 'original_filename': binding['original_filename'],
                          'original_pdf_sha256': binding['content_sha256'], 'mineru_state': 'done',
                          'chart_source_only': True, 'source_markdown': 'source_mineru.md', 'images': images,
                          'chart_source_image_count': len(images), 'mineru_recovery': task}
                (directory / 'status.json').write_bytes(encoded(status))
                reports.append({'directory': directory_name, 'binding': binding,
                                'source_binding': ledger.bind(path, source), 'source_id': source_id,
                                'task': task, 'zip_sha256': zip_sha, 'source_markdown_sha256': digest(markdown)})
            (stage / MANIFEST).write_bytes(raw_manifest)
            receipt = {'schema_version': 1, 'policy': POLICY, 'date_folder': date_folder,
                       'source_run_id': source_run_id, 'recovery_run_id': str(recovery_run_id),
                       'source_execution_sha': source_execution_sha, 'recovery_execution_sha': recovery_execution_sha,
                       'manifest_sha256': digest(raw_manifest),
                       'original_inventory': bindings, 'report_count': expected_reports, 'original_tasks': tasks,
                       'provider_posts': posts, 'reports': reports, 'files': regular_inventory(stage)}
            (stage / RECEIPT).write_bytes(encoded(receipt))
            validate_sources(stage, expected_reports, date_folder)
            stage.replace(destination); complete = True
            return receipt
    finally:
        if not complete:
            shutil.rmtree(stage, ignore_errors=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['recover', 'validate'])
    parser.add_argument('--output-dir', required=True)
    parser.add_argument('--expected-reports', required=True, type=int)
    parser.add_argument('--date-folder', required=True)
    parser.add_argument('--input-dir')
    parser.add_argument('--source-run-id', default='')
    parser.add_argument('--producer-json')
    parser.add_argument('--expected-recovery-run-id')
    parser.add_argument('--expected-execution-sha')
    parser.add_argument('--allow-fresh', action='store_true')
    parser.add_argument('--allowed-error-codes', default='[]')
    parser.add_argument('--allowed-error-hashes', default='[]')
    args = parser.parse_args()
    try:
        if args.command == 'validate':
            receipt = validate_sources(args.output_dir, args.expected_reports, args.date_folder,
                                       expected_recovery_run_id=args.expected_recovery_run_id,
                                       expected_execution_sha=args.expected_execution_sha)
        else:
            env = os.environ
            if (env.get('GITHUB_EVENT_NAME') != 'workflow_dispatch'
                    or env.get('GITHUB_REF') != 'refs/heads/main'
                    or env.get('GITHUB_WORKFLOW_REF') != env.get('GITHUB_REPOSITORY', '') + '/' + WORKFLOW + '@refs/heads/main'):
                reject('reviewed_main_workflow_required')
            if not args.input_dir:
                reject('input_required')
            sha = env.get('GITHUB_SHA', '')
            if args.source_run_id:
                if not RUN.fullmatch(args.source_run_id) or not args.producer_json:
                    reject('original_producer_required')
                sha = check_producer(decode(Path(args.producer_json).read_bytes()), args.source_run_id,
                                     env.get('GITHUB_REPOSITORY', ''))
            codes, hashes = decode(args.allowed_error_codes.encode()), decode(args.allowed_error_hashes.encode())
            if not isinstance(codes, list) or not isinstance(hashes, list):
                reject('recovery_allowlist')
            import requests
            from botocore.config import Config
            from private_workflow_handoff import require_env
            import boto3
            client = boto3.client('s3', endpoint_url=f"https://{require_env('R2_ACCOUNT_ID')}.r2.cloudflarestorage.com",
                aws_access_key_id=require_env('R2_ACCESS_KEY_ID'), aws_secret_access_key=require_env('R2_SECRET_ACCESS_KEY'),
                region_name='auto', config=Config(connect_timeout=20, read_timeout=30,
                                                retries={'total_max_attempts': 1, 'mode': 'standard'}))
            store = R2Store('dropbox', client=client, bucket=require_env('R2_BUCKET'))
            ledger = Ledger(store, Provider(NoRedirectHTTP(requests.request), 'https://mineru.net'), 'dropbox',
                            'https://mineru.net', OPTIONS, credentials(env))
            receipt = recover_sources(ledger, args.input_dir, Path(args.input_dir) / MANIFEST,
                args.output_dir, args.expected_reports, args.date_folder, source_run_id=args.source_run_id,
                allow_fresh=args.allow_fresh, recovery_run_id=env.get('GITHUB_RUN_ID', ''), source_execution_sha=sha,
                recovery_execution_sha=env.get('GITHUB_SHA', ''),
                allowed_error_codes=codes, allowed_error_hashes=hashes)
    except (RecoveryError, LedgerError, ConsumerError, OSError, ValueError, KeyError, TypeError) as error:
        category = str(error) if isinstance(error, (RecoveryError, NetworkStop)) else type(error).__name__
        print('MinerU source recovery stopped: ' + category, file=sys.stderr)
        return 2
    except Exception as error:
        print('MinerU source recovery stopped: ' + type(error).__name__, file=sys.stderr)
        return 2
    print('MinerU source recovery complete: reports=' + str(receipt['report_count'])
          + ', manifest_sha256=' + receipt['manifest_sha256'])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
