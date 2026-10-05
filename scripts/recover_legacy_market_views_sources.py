"""Materialize a complete legacy Daily handoff from exact verified cached ZIPs.

Legacy IDs and evidence remain distinct from canonical task admission. The cloud
producer authenticates original Actions evidence and GETs all accepted retries;
this stage has no submission or result-download operation and accepts no subset.
"""
from __future__ import annotations
import argparse
from contextlib import redirect_stdout, redirect_stderr
import io
import json
import math
import os
from pathlib import Path
import re
import shutil
import tempfile

from consume_legacy_mineru import chart_assets, figure_source_status, safe_unzip
from mineru_figure_sources import FigureSourceError, validate_figure_sources
import inspect_legacy_mineru as inspect
import seed_legacy_market_views_cache as legacy
from recover_durable_mineru_sources import digest, decode, manifest_bindings, MANIFEST, exact_date, frozen_inputs

WORKFLOW = '.github/workflows/market-views-legacy-recovery.yml'
RECEIPT = 'legacy-source-receipt.json'
POLICY = 'complete-source-bound-legacy-market-handoff-v1'
SAFE = {'source_context', 'source_inventory', 'source_receipt', 'source_reports', 'source_task',
        'source_images', 'source_markdown', 'source_incomplete', 'cached_result_missing',
        'destination_exists', 'source_inputs_changed', 'source_failed'}


class LegacySourceError(ValueError):
    """Literal public categories only."""


def fail(category):
    raise LegacySourceError(category)


def source_context(producer_run_id, execution_sha, original_run_id, original_sha, date_folder):
    exact_date(date_folder)
    if (not all(isinstance(value, str) and legacy.RUN.fullmatch(value) for value in (producer_run_id, original_run_id))
            or not all(isinstance(value, str) and legacy.SHA.fullmatch(value) for value in (execution_sha, original_sha))):
        fail('source_context')
    return {'producer_run_id': producer_run_id, 'execution_sha': execution_sha,
            'original_source_run_id': original_run_id, 'original_execution_sha': original_sha,
            'date_folder': date_folder, 'producer_workflow': WORKFLOW}


def file_inventory(root):
    files = []
    for path in sorted(Path(root).rglob('*')):
        if path.is_symlink():
            fail('source_inventory')
        if path.is_file() and path != Path(root) / RECEIPT:
            raw = path.read_bytes()
            files.append({'path': path.relative_to(root).as_posix(), 'sha256': digest(raw), 'bytes': len(raw)})
    return files


def terminal_projection(authority, private):
    requested = {row['batch_id']: row for group in authority['groups'] for row in group['batches']}
    if (private.get('input') != {'schema_version': 1, 'batches': list(requested.values())}
            or len(private.get('batches', [])) != len(requested)):
        fail('source_task')
    tasks = []
    for value in private['batches']:
        batch = value['input']
        if requested.get(batch['batch_id']) != batch:
            fail('source_task')
        rows = value['provider_response']['data']['extract_result']
        by_id = {row['data_id']: row for row in rows}
        if (len(by_id) != len(rows) or set(by_id) != set(batch['expected_data_ids'])
                or any(row.get('state') not in inspect.TERMINAL for row in rows)):
            fail('source_task')
        tasks.append({'batch_id': batch['batch_id'], 'job_id': batch['job_id'], 'credential_slot': batch['credential_slot'],
                      'response_sha256': value['response_sha256'],
                      'members': [{'data_id': identity, 'state': by_id[identity]['state']} for identity in batch['expected_data_ids']]})
    return tasks


def validate_authority(authority, bindings, date_folder):
    keys = {'schema_version', 'repository', 'workflow_path', 'run_id', 'execution_sha', 'date_folder', 'manifest_sha256',
            'artifact_id', 'artifact_zip_sha256', 'code_sha256', 'expected_reports', 'groups', 'original_inventory',
            'original_sizes', 'authority_sha256'}
    if (not isinstance(authority, dict) or set(authority) != keys or type(authority['schema_version']) is not int
            or authority['schema_version'] != 1 or authority['workflow_path'] != legacy.PRODUCER
            or authority['code_sha256'] != legacy.ORIGINAL_CODE or authority['original_inventory'] != bindings
            or type(authority['expected_reports']) is not int or authority['expected_reports'] != len(bindings)
            or authority['date_folder'] != date_folder or not isinstance(authority['repository'], str)
            or not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', authority['repository'])
            or not all(isinstance(authority[key], str) and legacy.RUN.fullmatch(authority[key]) for key in ('run_id', 'artifact_id'))
            or not isinstance(authority['execution_sha'], str) or not legacy.SHA.fullmatch(authority['execution_sha'])
            or not all(isinstance(authority[key], str) and legacy.HASH.fullmatch(authority[key]) for key in
                       ('manifest_sha256', 'artifact_zip_sha256', 'authority_sha256'))
            or digest(legacy.canonical({key: value for key, value in authority.items() if key != 'authority_sha256'})) != authority['authority_sha256']):
        fail('source_inventory')
    names = sorted(row['source_pdf'] for row in bindings)
    sizes = authority['original_sizes']
    if (not isinstance(sizes, dict) or set(sizes) != set(names)
            or any(type(value) is not int or not 1 <= value <= legacy.consumer.MAX_MEMBER for value in sizes.values())
            or any(Path(row['dropbox_path']).parts[:3] != ('/', 'zip_backup', date_folder) for row in bindings)):
        fail('source_inventory')
    groups = authority['groups']
    if not isinstance(groups, list) or len(groups) != math.ceil(len(names) / 5):
        fail('source_task')
    all_batches = []
    job_ids = []
    for shard, group in enumerate(groups):
        if (not isinstance(group, dict) or set(group) != {'shard', 'job_id', 'job_log_sha256', 'accepted', 'members', 'batches'}
                or type(group['shard']) is not int or group['shard'] != shard
                or not isinstance(group['job_id'], str) or not legacy.RUN.fullmatch(group['job_id'])
                or not isinstance(group['job_log_sha256'], str) or not legacy.HASH.fullmatch(group['job_log_sha256'])
                or not isinstance(group['accepted'], list) or not 1 <= len(group['accepted']) <= 4):
            fail('source_task')
        job_ids.append(group['job_id'])
        members = [{'source_pdf': name, 'source_filename': legacy.consumer.copied_name(name, index),
                    'data_id': legacy.consumer.data_id(legacy.consumer.copied_name(name, index))}
                   for index, name in enumerate(names[shard * 5:(shard + 1) * 5], 1)]
        if group['members'] != members:
            fail('source_task')
        batches = []
        for attempt, accepted in enumerate(group['accepted'], 1):
            if (not isinstance(accepted, dict) or set(accepted) != {'attempt', 'credential_slot', 'batch_id'}
                    or type(accepted['attempt']) is not int or accepted['attempt'] != attempt
                    or not isinstance(accepted['credential_slot'], str) or accepted['credential_slot'] not in inspect.SLOTS
                    or not inspect.valid_uuid(accepted['batch_id'])):
                fail('source_task')
            batches.append({'run_id': authority['run_id'], 'job_id': group['job_id'], 'batch_id': accepted['batch_id'],
                            'credential_slot': accepted['credential_slot'], 'expected_data_ids': [row['data_id'] for row in members]})
        if group['batches'] != batches:
            fail('source_task')
        all_batches.extend(batches)
    if len(job_ids) != len(set(job_ids)):
        fail('source_task')
    inspect.validate_request({'schema_version': 1, 'batches': all_batches})


def validate_sources(root, expected_reports, date_folder, *, expected_producer_run_id=None, expected_execution_sha=None):
    root = Path(root)
    if root.is_symlink() or not root.is_dir() or not (root / RECEIPT).is_file() or (root / RECEIPT).is_symlink():
        fail('source_receipt')
    receipt = decode((root / RECEIPT).read_bytes())
    keys = {'schema_version', 'policy', 'source_context', 'original_authority', 'manifest_sha256',
            'original_inventory', 'report_count', 'unique_content_count', 'terminal_tasks', 'reports', 'files',
            'provider_posts', 'ledger_writes', 'canonical_task_admission', 'original_provider_bytes_proven'}
    if (not isinstance(receipt, dict) or set(receipt) != keys or type(receipt.get('schema_version')) is not int
            or receipt['schema_version'] != 1 or receipt.get('policy') != POLICY
            or receipt.get('canonical_task_admission') is not False or receipt.get('original_provider_bytes_proven') is not False
            or type(receipt.get('provider_posts')) is not int or receipt['provider_posts'] != 0
            or type(receipt.get('ledger_writes')) is not int or receipt['ledger_writes'] != 0
            or type(receipt.get('report_count')) is not int or receipt['report_count'] != expected_reports):
        fail('source_receipt')
    context = receipt['source_context']
    if not isinstance(context, dict) or set(context) != {'producer_run_id', 'execution_sha', 'original_source_run_id',
            'original_execution_sha', 'date_folder', 'producer_workflow'}:
        fail('source_context')
    wanted = source_context(context['producer_run_id'], context['execution_sha'], context['original_source_run_id'],
                            context['original_execution_sha'], date_folder)
    if context != wanted or (expected_producer_run_id is not None and context['producer_run_id'] != expected_producer_run_id) or (
            expected_execution_sha is not None and context['execution_sha'] != expected_execution_sha):
        fail('source_context')
    raw = (root / MANIFEST).read_bytes()
    bindings = manifest_bindings(raw, expected_reports, date_folder)
    authority = receipt['original_authority']
    validate_authority(authority, bindings, date_folder)
    if (not isinstance(authority, dict) or digest(raw) != receipt['manifest_sha256']
            or bindings != receipt['original_inventory'] or receipt['files'] != file_inventory(root)
            or digest(legacy.canonical({key: value for key, value in authority.items() if key != 'authority_sha256'})) != authority.get('authority_sha256')
            or authority.get('manifest_sha256') != digest(raw) or authority.get('original_inventory') != bindings
            or authority.get('expected_reports') != expected_reports or authority.get('date_folder') != date_folder
            or authority.get('run_id') != context['original_source_run_id']
            or authority.get('execution_sha') != context['original_execution_sha']
            or authority.get('code_sha256') != legacy.ORIGINAL_CODE or authority.get('workflow_path') != legacy.PRODUCER):
        fail('source_inventory')
    requested = {row['batch_id']: row for group in authority['groups'] for row in group['batches']}
    tasks = receipt['terminal_tasks']
    if not isinstance(tasks, list) or len(tasks) != len(requested):
        fail('source_task')
    task_map = {}
    for task in tasks:
        if (not isinstance(task, dict) or set(task) != {'batch_id', 'job_id', 'credential_slot', 'response_sha256', 'members'}
                or not isinstance(task.get('batch_id'), str) or task['batch_id'] not in requested or task['batch_id'] in task_map
                or task.get('job_id') != requested[task['batch_id']]['job_id']
                or task.get('credential_slot') != requested[task['batch_id']]['credential_slot']
                or not isinstance(task.get('response_sha256'), str) or not legacy.HASH.fullmatch(task['response_sha256'])
                or not isinstance(task.get('members'), list)):
            fail('source_task')
        members = task['members']
        if (any(not isinstance(row, dict) or set(row) != {'data_id', 'state'} or row.get('state') not in inspect.TERMINAL for row in members)
                or [row['data_id'] for row in members] != requested[task['batch_id']]['expected_data_ids']):
            fail('source_task')
        task_map[task['batch_id']] = task
    reports = receipt['reports']
    if not isinstance(reports, list) or len(reports) != expected_reports:
        fail('source_reports')
    first = {}
    directories = set()
    for index, (report, binding) in enumerate(zip(reports, bindings), 1):
        if not isinstance(report, dict) or set(report) != {'directory', 'source_pdf', 'content_sha256', 'binding', 'zip_sha256',
                'source_markdown_sha256', 'duplicate_of'}:
            fail('source_reports')
        task_binding = report['binding']
        identity = legacy.binding_identity(task_binding)
        directory_name = f'report_{index:04d}_{identity[:12]}'
        duplicate = first.setdefault(binding['content_sha256'], directory_name)
        duplicate = duplicate if duplicate != directory_name else None
        if (report['directory'] != directory_name or directory_name in directories or report['duplicate_of'] != duplicate
                or report['source_pdf'] != binding['source_pdf'] or report['content_sha256'] != binding['content_sha256']
                or any(task_binding.get(key) != value for key, value in binding.items())
                or task_binding['run_id'] != context['original_source_run_id']
                or task_binding['execution_sha'] != context['original_execution_sha']
                or task_binding['manifest_sha256'] != receipt['manifest_sha256']
                or task_binding['artifact_zip_sha256'] != authority['artifact_zip_sha256']
                or task_binding['original_pdf_bytes'] != authority['original_sizes'][binding['source_pdf']]
                or not all(isinstance(report.get(key), str) and legacy.HASH.fullmatch(report[key]) for key in ('zip_sha256', 'source_markdown_sha256'))):
            fail('source_reports')
        task = task_map.get(task_binding['batch_id'])
        groups = [group for group in authority['groups'] if group['job_id'] == task_binding['job_id']]
        if (task is None or task['job_id'] != task_binding['job_id'] or task['credential_slot'] != task_binding['credential_slot']
                or len(groups) != 1 or task_binding['job_log_sha256'] != groups[0]['job_log_sha256']
                or any(row['state'] != 'done' for row in task['members'])
                or task_binding['data_id'] not in {row['data_id'] for row in task['members']}
                or not any(member['source_pdf'] == binding['source_pdf'] and member['data_id'] == task_binding['data_id']
                           and member['source_filename'] == task_binding['source_filename'] for member in groups[0]['members'])):
            fail('source_task')
        directory = root / directory_name
        status = decode((directory / 'status.json').read_bytes())
        markdown = (directory / 'source_mineru.md').read_bytes()
        if (not markdown.strip() or digest(markdown) != report['source_markdown_sha256']
                or status.get('source_pdf') != binding['source_pdf'] or status.get('original_filename') != binding['original_filename']
                or status.get('original_pdf_sha256') != binding['content_sha256'] or status.get('mineru_state') != 'done'
                or status.get('chart_source_only') is not True or status.get('source_markdown') != 'source_mineru.md'
                or status.get('canonical_task_admission') is not False or status.get('original_provider_bytes_proven') is not False
                or status.get('mineru_legacy') != task_binding or status.get('duplicate_of') != duplicate):
            fail('source_markdown')
        images = status.get('images')
        if (not isinstance(images, list) or len(images) > 100 or any(not isinstance(image, str) for image in images)
                or len(images) != len(set(images)) or type(status.get('chart_source_image_count')) is not int
                or status['chart_source_image_count'] != len(images)):
            fail('source_images')
        for ordinal, image in enumerate(images, 1):
            if not re.fullmatch(r'assets/source_image_' + f'{ordinal:02d}' + r'\.(?:png|jpe?g|webp|gif|bmp|tiff?)', image) or not (directory / image).is_file():
                fail('source_images')
        mapping = decode((directory / 'source_image_map.json').read_bytes())
        if (not isinstance(mapping, dict) or set(mapping) != {'version', 'source_sha256', 'images'}
                or type(mapping.get('version')) is not int or mapping['version'] != 1
                or mapping.get('source_sha256') != digest(markdown) or not isinstance(mapping.get('images'), dict)
                or any(not isinstance(ref, str) or not ref or target not in images for ref, target in mapping['images'].items())
                or set(mapping['images'].values()) != set(images)):
            fail('source_images')
        try:
            selected = validate_figure_sources(directory, expected_original_sha256=binding['content_sha256'],
                expected_markdown_sha256=report['source_markdown_sha256'], expected_images=images)
            if selected is not None and any(mapping['images'].get(ref) != asset for ref, asset in selected.items()):
                fail('source_images')
        except FigureSourceError:
            fail('source_images')
        directories.add(directory_name)
    actual = {path.name for path in root.iterdir() if path.is_dir()}
    if actual != directories or type(receipt['unique_content_count']) is not int or receipt['unique_content_count'] != len(first):
        fail('source_inventory')
    return receipt


def materialize(authority, manifest, input_dir, results, private, cache, destination, context, *, asset_writer=chart_assets):
    if len(results) != authority['expected_reports'] or len({binding['source_pdf'] for binding, _ in results}) != authority['expected_reports']:
        fail('source_incomplete')
    destination = Path(destination)
    if destination.exists() or destination.is_symlink():
        fail('destination_exists')
    raw, originals, original_pairs = frozen_inputs(input_dir, manifest, authority['expected_reports'], authority['date_folder'])
    validate_authority(authority, originals, authority['date_folder'])
    if digest(raw) != authority['manifest_sha256'] or originals != authority['original_inventory']:
        fail('source_inputs_changed')
    by_source = {binding['source_pdf']: binding for binding, _ in results}
    original_paths = {name: path for path, name in original_pairs}
    tasks = terminal_projection(authority, private)
    destination.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix='.legacy-market-source-', dir=destination.parent))
    complete = False
    try:
        reports = []; first = {}
        with tempfile.TemporaryDirectory(prefix='legacy-market-raw-') as scratch:
            for index, original in enumerate(originals, 1):
                binding = by_source[original['source_pdf']]
                payload = cache.get(binding)
                if payload is None:
                    fail('cached_result_missing')
                raw_dir = Path(scratch) / str(index)
                markdown = safe_unzip(payload, raw_dir)
                directory_name = f'report_{index:04d}_{legacy.binding_identity(binding)[:12]}'
                directory = stage / directory_name; directory.mkdir()
                (directory / 'source_mineru.md').write_bytes(markdown)
                assets = directory / 'assets'; assets.mkdir()
                with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                    if asset_writer is chart_assets:
                        images = asset_writer(raw_dir, assets, 100,
                            original_pdf_sha256=original['content_sha256'],
                            auth_original_pdf=original_paths[original['source_pdf']],
                            markdown_sha256=digest(markdown))
                    else:
                        images = asset_writer(raw_dir, assets, 100)
                duplicate = first.setdefault(original['content_sha256'], directory_name)
                duplicate = duplicate if duplicate != directory_name else None
                status = {'source_pdf': original['source_pdf'], 'original_filename': original['original_filename'],
                          'original_pdf_sha256': original['content_sha256'], 'mineru_state': 'done', 'chart_source_only': True,
                          'source_markdown': 'source_mineru.md', 'images': images, 'chart_source_image_count': len(images),
                          'canonical_task_admission': False, 'original_provider_bytes_proven': False,
                          'mineru_legacy': binding, 'duplicate_of': duplicate}
                status.update(figure_source_status(directory))
                (directory / 'status.json').write_bytes(legacy.canonical(status))
                reports.append({'directory': directory_name, 'source_pdf': original['source_pdf'], 'content_sha256': original['content_sha256'],
                                'binding': binding, 'zip_sha256': digest(payload), 'source_markdown_sha256': digest(markdown), 'duplicate_of': duplicate})
        final, bindings, _ = frozen_inputs(input_dir, manifest, authority['expected_reports'], authority['date_folder'])
        if final != raw or bindings != originals:
            fail('source_inputs_changed')
        (stage / MANIFEST).write_bytes(raw)
        receipt = {'schema_version': 1, 'policy': POLICY, 'source_context': context, 'original_authority': authority,
                   'manifest_sha256': digest(raw), 'original_inventory': originals, 'report_count': len(reports),
                   'unique_content_count': len(first), 'terminal_tasks': tasks, 'reports': reports, 'files': file_inventory(stage),
                   'provider_posts': 0, 'ledger_writes': 0, 'canonical_task_admission': False, 'original_provider_bytes_proven': False}
        (stage / RECEIPT).write_bytes(legacy.canonical(receipt))
        validate_sources(stage, authority['expected_reports'], authority['date_folder'],
                         expected_producer_run_id=context['producer_run_id'], expected_execution_sha=context['execution_sha'])
        stage.replace(destination); complete = True
        return receipt
    finally:
        if not complete:
            shutil.rmtree(stage, ignore_errors=True)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=('recover', 'validate'))
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--source-run-id', default='')
    parser.add_argument('--artifact-id', default='')
    parser.add_argument('--date-folder', required=True)
    parser.add_argument('--expected-reports', type=int, required=True)
    parser.add_argument('--expected-producer-run-id')
    parser.add_argument('--expected-execution-sha')
    args = parser.parse_args(argv)
    try:
        if args.operation == 'validate':
            receipt = validate_sources(args.output_dir, args.expected_reports, args.date_folder,
                expected_producer_run_id=args.expected_producer_run_id, expected_execution_sha=args.expected_execution_sha)
        else:
            env = os.environ
            repository = env.get('GITHUB_REPOSITORY', '')
            if (env.get('GITHUB_ACTIONS') != 'true' or env.get('GITHUB_EVENT_NAME') != 'workflow_dispatch'
                    or env.get('GITHUB_REF') != 'refs/heads/main'
                    or env.get('GITHUB_WORKFLOW_REF') != repository + '/' + WORKFLOW + '@refs/heads/main'
                    or not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository)
                    or not legacy.RUN.fullmatch(args.source_run_id)
                    or args.artifact_id and not legacy.RUN.fullmatch(args.artifact_id)
                    or not 1 <= args.expected_reports <= 1000):
                fail('source_context')
            from private_workflow_handoff import require_env
            import boto3
            from botocore.config import Config
            client = boto3.client('s3', endpoint_url=f'https://{require_env("R2_ACCOUNT_ID")}.r2.cloudflarestorage.com',
                aws_access_key_id=require_env('R2_ACCESS_KEY_ID'), aws_secret_access_key=require_env('R2_SECRET_ACCESS_KEY'), region_name='auto',
                config=Config(connect_timeout=20, read_timeout=30, retries={'total_max_attempts': 1, 'mode': 'standard'}))
            cache = legacy.LegacyResultCache(client, require_env('R2_BUCKET'))
            with tempfile.TemporaryDirectory(prefix='legacy-market-originals-') as temporary:
                originals = Path(temporary) / 'originals'
                authority, manifest, _ = legacy.authenticate(legacy.Github(require_env('GH_TOKEN')), args.source_run_id,
                    repository, originals, args.expected_reports, args.date_folder, artifact_id=args.artifact_id)
                results, _, private = legacy.complete_results(authority, {slot: env.get(slot, '') for slot in inspect.SLOTS})
                context = source_context(require_env('GITHUB_RUN_ID'), require_env('GITHUB_SHA'), args.source_run_id,
                                         authority['execution_sha'], args.date_folder)
                receipt = materialize(authority, manifest, originals, results, private, cache, args.output_dir, context)
        print(json.dumps({'success': True, 'report_count': receipt['report_count'], 'unique_content_count': receipt['unique_content_count'],
                          'manifest_sha256': receipt['manifest_sha256'], 'provider_posts': 0, 'ledger_writes': 0,
                          'canonical_task_admission': False}, sort_keys=True))
        return 0
    except Exception as error:
        category = error.args[0] if isinstance(error, LegacySourceError) and len(error.args) == 1 and type(error.args[0]) is str and error.args[0] in SAFE else 'source_failed'
        print(json.dumps({'success': False, 'category': category, 'provider_posts': 0, 'canonical_task_admission': False}))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
