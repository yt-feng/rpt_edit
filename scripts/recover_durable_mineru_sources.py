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
                                 download_once, figure_source_status, safe_unzip, valid_url)
from mineru_figure_sources import ERRORS as FIGURE_ERROR_CATEGORIES, FigureSourceError, validate_figure_sources
from mineru_task_ledger import (DONE, FAILED, Ledger, LedgerError, Provider, R2Store,
                               digest, encoded, exact_json, schema_v1)
from mineru_terminal_recovery import AUTOMATIC_POLICY, TerminalRecovery, task_identity
from mineru_result_cache import ResultCache, identity as result_identity
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


def download_result(url, **kwargs):
    # Workflow metadata checks import this module before dependencies are
    # installed. Only actual result delivery requires the transport packages.
    from mineru_daily_result_transport import download_result as retrieve
    return retrieve(url, **kwargs)


def persist_authentication(*args):
    from mineru_daily_result_cache import persist_authentication as persist
    return persist(*args)


def safe_figure_source_ordinal(error, expected_reports):
    """Only the bounded report position may accompany a fixed figure category."""
    ordinal = getattr(error, 'source_ordinal', None)
    if (isinstance(error, FigureSourceError) and type(ordinal) is int
            and type(expected_reports) is int and 1 <= expected_reports <= 1000
            and 1 <= ordinal <= expected_reports):
        return ordinal
    return None


# Exact upstream messages only: no arbitrary provider, URL, source or storage
# exception text is ever copied to public diagnostics. Unknowns stay generic.
LEDGER_ERROR_CATEGORIES = {
    'Stored task scope, source, options or token identity mismatch': 'stored_task_identity_mismatch',
    'Stored source binding is malformed': 'stored_source_binding_invalid',
    'Stored task has duplicate source identities': 'stored_task_duplicate_sources',
    'No MinerU token identities available': 'credentials_missing',
    'All configured MinerU credentials were definitively rejected; saved batch is auth_rejected': 'credentials_rejected',
    'Accepted task refers to a definitively rejected credential': 'accepted_task_credential_rejected',
    'Stored authentication rejection history is malformed': 'credential_rejection_history_invalid',
    'Stored authentication rejection state is inconsistent': 'credential_rejection_state_invalid',
    'Interrupted or ambiguous submission; inspect saved task, never resubmit': 'saved_submission_ambiguous',
    'Ambiguous existing task blocks new submissions': 'saved_task_ambiguous',
    'Unrecognized saved task state': 'saved_task_state_invalid',
    'Requested PDF does not match accepted task bytes and scope': 'accepted_source_binding_mismatch',
    'Source claim binding mismatch': 'source_claim_binding_mismatch',
    'Source bytes changed after task admission': 'source_bytes_changed',
    'Source bytes changed during polling; results cannot be reused': 'source_bytes_changed',
    'Original source bytes changed before task submission': 'source_bytes_changed',
    'Original source bytes changed during terminal recovery': 'source_bytes_changed',
    'Task attempt time budget exhausted; saved task retained': 'task_budget_exhausted',
    'Malformed MinerU result rows': 'provider_result_rows_invalid',
    'Unknown or duplicate result source identity': 'provider_result_membership_invalid',
    'Unknown MinerU result state': 'provider_result_state_invalid',
    'Completed MinerU row lacks source result URL': 'provider_result_url_missing',
    'Previously terminal batch returned truncated or nonterminal results': 'terminal_result_membership_changed',
    'Ledger compare-and-swap conflict; no new submission': 'checkpoint_write_conflict',
    'Private checkpoint write outcome unresolved; no new submission': 'checkpoint_write_unresolved',
    'Private checkpoint durable readback mismatch; no new submission': 'checkpoint_readback_mismatch',
    'Private task checkpoint size, digest or version mismatch': 'checkpoint_binding_mismatch',
    'Task checkpoint size is invalid': 'checkpoint_size_invalid',
    'Task checkpoint exceeds size bound': 'checkpoint_size_invalid',
    'Malformed task checkpoint': 'checkpoint_json_invalid',
    'Malformed task checkpoint object': 'checkpoint_json_invalid',
    'Task checkpoint schema must be an integer': 'checkpoint_schema_invalid',
    'Terminal failure is not explicitly authorized for recovery': 'failure_not_authorized',
    'Only a complete freshly verified terminal task authorizes a recovery child': 'predecessor_not_complete',
    'Stored terminal recovery controller does not match its original task or fixed policy': 'recovery_controller_mismatch',
    'Stored terminal recovery child reservation is malformed': 'recovery_child_reservation_invalid',
    'Stored recovery children refer to different original manifests': 'recovery_manifest_mismatch',
    'Stored terminal recovery proof is malformed': 'recovery_proof_invalid',
    'Stored terminal recovery proof omits original members': 'recovery_proof_membership_invalid',
    'Stored terminal recovery proof has invalid member bindings': 'recovery_proof_membership_invalid',
    'Stored failure proof is not explicitly authorized': 'stored_failure_not_authorized',
    'Stored successful member has invalid failure evidence': 'recovery_success_proof_invalid',
    'Stored child inventory differs from its failed original members': 'recovery_child_inventory_mismatch',
    'Recovery child does not match its durable parent reservation': 'recovery_child_parent_mismatch',
    'Recovery child credential changed without its original definitive rejection': 'recovery_child_credential_mismatch',
    'Terminal recovery child limit reached; saved tasks retained': 'recovery_child_limit_exhausted',
    'Recovery authorization differs from the frozen original manifest': 'recovery_manifest_mismatch',
    'Fresh terminal membership differs from the saved recovery reservation': 'fresh_failure_membership_mismatch',
    'Fresh terminal failure proof differs from the saved recovery reservation': 'fresh_failure_proof_mismatch',
    'Ambiguous recovery child blocks new submissions; saved task retained': 'recovery_child_submission_ambiguous',
    'Unrecognized recovery child state': 'recovery_child_state_invalid',
    'Recovery returned duplicate successful source coverage': 'recovery_duplicate_sources',
    'MinerU GET transport outcome unknown; saved task retained': 'provider_get_transport_unknown',
    'MinerU POST transport outcome unknown; saved task retained': 'provider_post_transport_unknown',
    'MinerU PUT transport outcome unknown; saved task retained': 'provider_upload_transport_unknown',
    'MinerU get transport outcome unknown; saved task retained': 'provider_get_transport_unknown',
    'MinerU post transport outcome unknown; saved task retained': 'provider_post_transport_unknown',
    'MinerU put transport outcome unknown; saved task retained': 'provider_upload_transport_unknown',
    'MinerU submission acknowledgement is incomplete': 'provider_submission_ack_incomplete',
}
WRAPPED_RECOVERY_CATEGORIES = {
    'NetworkStop': 'child_result_network_stop',
    'ConsumerError': 'child_result_validation_failed',
    'ResultCacheError': 'child_result_cache_failed',
    'TimeoutError': 'terminal_recovery_timeout',
    'OSError': 'terminal_recovery_os_error',
    'KeyError': 'terminal_recovery_key_invalid',
    'ValueError': 'terminal_recovery_value_invalid',
    'TypeError': 'terminal_recovery_type_invalid',
    'ClientError': 'terminal_recovery_storage_failed',
}


def safe_ledger_error_category(error):
    if not isinstance(error, LedgerError) or len(error.args) != 1 or type(error.args[0]) is not str:
        return 'ledger_error'
    message = error.args[0]
    if len(message) > 256:
        return 'ledger_error'
    if message in LEDGER_ERROR_CATEGORIES:
        return 'ledger_' + LEDGER_ERROR_CATEGORIES[message]
    for exception_name, category in WRAPPED_RECOVERY_CATEGORIES.items():
        if message == 'Terminal recovery stopped; saved tasks retained (' + exception_name + ')':
            # `raise ... from None` suppresses traceback display but retains
            # this immediate exception context. Accept only its fixed TLS
            # category, never arbitrary nested text or a rendered traceback.
            context = error.__context__
            if (exception_name == 'NetworkStop' and isinstance(context, NetworkStop)
                    and len(context.args) == 1 and type(context.args[0]) is str
                    and context.args[0] == 'tls_certificate_expired'):
                return 'ledger_child_result_tls_certificate_expired'
            return 'ledger_' + category
    # Only a numeric HTTP status in one of these exact provider templates is
    # recognized; it is not necessary to expose that status or the raw message.
    templates = {
        r'MinerU response is not valid JSON: HTTP [1-5][0-9]{2}': 'provider_response_json_invalid',
        r'MinerU request rejected or malformed: HTTP [1-5][0-9]{2}': 'provider_request_rejected',
        r'MinerU upload did not complete: HTTP [1-5][0-9]{2}': 'provider_upload_rejected',
    }
    for pattern, category in templates.items():
        if re.fullmatch(pattern, message):
            return 'ledger_' + category
    return 'ledger_error'


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
                or type(lineage['child_ordinal']) is not int or not 0 <= lineage['child_ordinal'] <= 3
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
        try:
            selected = validate_figure_sources(directory, expected_original_sha256=binding['content_sha256'],
                expected_markdown_sha256=report['source_markdown_sha256'], expected_images=status['images'])
            if selected is not None and any(mapping['images'].get(ref) != asset for ref, asset in selected.items()):
                reject('report_figure_source')
        except FigureSourceError:
            reject('report_figure_source')
        identities.append(report['source_id'])
    if set(identities) != set(admitted) or len(set(identities)) != expected_reports:
        reject('receipt_admission_coverage')
    return receipt


def recover_sources(ledger, input_dir, manifest_path, output_dir, expected_reports, date_folder, *,
                    source_run_id='', allow_fresh=False, recovery_run_id, source_execution_sha,
                    recovery_execution_sha=None,
                    allowed_error_codes=(), allowed_error_hashes=(), downloader=download_once,
                    asset_writer=chart_assets, timeout=1800, interval=15, queue_budget=300, result_cache=None,
                    authenticated_downloader=None, terminal_factory=None, total_timeout=None,
                    continue_batches=False):
    if type(continue_batches) is not bool or (continue_batches and (terminal_factory is None or allow_fresh)):
        reject('daily_batch_continuation_requires_bound_terminal_factory')
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
    if total_timeout is not None and (type(total_timeout) not in {int, float}
            or not 0 < total_timeout <= 3600):
        reject('recovery_time_budget_invalid')
    deadline = None if total_timeout is None else ledger.clock() + total_timeout
    def remaining():
        if deadline is None:
            return timeout
        budget = min(timeout, deadline - ledger.clock())
        if budget <= 0:
            reject('recovery_time_budget_exhausted')
        return budget
    destination = Path(output_dir)
    if destination.exists() or destination.is_symlink():
        reject('destination_exists')
    destination.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix='.mineru-market-source-', dir=destination.parent))
    complete = False
    try:
        with tempfile.TemporaryDirectory(prefix='mineru-source-results-') as cache_dir:
            cache, deferred, root_for_id, resolved, posts, tasks = {}, {}, {}, {}, 0, []
            active_batch_deadline, verified_outcomes = None, {}
            source_bindings = {item['id']: item for item in (ledger.bind(path, source) for path, source in pairs)}
            source_ordinals = {ledger.bind(path, source)['id']: index
                               for index, (path, source) in enumerate(pairs, 1)}
            def daily_progress(index, batch, status, *, ready=False, summary=None, category=None):
                outcomes = {row.get('data_id'): row for row in (summary or {}).get('source_outcomes', [])
                            if isinstance(row, dict)}
                sources = []
                for item in batch['files']:
                    outcome = outcomes.get(item['id'], verified_outcomes.get(item['id'], {}))
                    state = outcome.get('status')
                    count = outcome.get('retry_count')
                    sources.append({'source_ordinal': source_ordinals[item['id']],
                                    'status': state if state in {'done', 'retry_exhausted', 'pending',
                                                                 'submission_unknown', 'failed'} else 'unobserved',
                                    'reserved_retry_count': count if type(count) is int and 0 <= count <= 3 else None})
                value = {'event': 'daily_mineru_batch', 'batch_ordinal': index, 'batch_count': len(groups),
                         'status': status, 'ready': ready, 'sources': sources}
                if category is not None:
                    value['category'] = category
                print(json.dumps(value, sort_keys=True), flush=True)
            def check_download_budget():
                if (continue_batches and active_batch_deadline is not None
                        and ledger.clock() >= active_batch_deadline):
                    reject('daily_batch_time_budget_exhausted')
            def verify_done(path, row):
                if not continue_batches:
                    remaining()
                if str(row.get('state', '')).lower() not in DONE:
                    return
                source_id = row.get('data_id')
                if source_id not in source_bindings:
                    reject('result_unknown_source')
                url = row.get('full_zip_url'); valid_url(url)
                cache_key = (source_id, url)
                lineage = row.get('_recovery_lineage')
                deferred_key = result_identity(source_bindings[source_id], lineage)
                # A result already diagnosed in this attempt needs no second
                # GET when TerminalRecovery returns its same successful row.
                if deferred_key in deferred:
                    if not exact_json(deferred[deferred_key], lineage):
                        reject('deferred_result_lineage_changed')
                    return
                if cache_key not in cache:
                    check_download_budget()
                    payload = result_cache.get(source_bindings[source_id], lineage) if result_cache is not None else None
                    cache_hit = payload is not None
                    authentication = None
                    if not cache_hit:
                        check_download_budget()
                        try:
                            if result_cache is not None and authenticated_downloader is not None:
                                payload, authentication = authenticated_downloader(url, strict_downloader=downloader)
                            else:
                                payload = downloader(url)
                        except NetworkStop as error:
                            child = (isinstance(lineage, dict) and type(lineage.get('child_ordinal')) is int
                                     and lineage['child_ordinal'] in {1, 2, 3}
                                     and lineage.get('parent_batch_key') == root_for_id.get(source_id)
                                     and lineage.get('batch_key') != lineage.get('parent_batch_key'))
                            if (not child or len(error.args) != 1 or type(error.args[0]) is not str
                                    or error.args[0] != 'tls_certificate_expired'):
                                raise
                            # Validate complete accepted source/task identity;
                            # no ZIP bytes or completed source receipt is created.
                            deferred[deferred_key] = dict(lineage)
                            return
                    folder = Path(cache_dir) / str(len(cache))
                    markdown = safe_unzip(payload, folder / 'raw')
                    if result_cache is not None and not cache_hit:
                        if authentication is not None:
                            persist_authentication(result_cache, source_bindings[source_id], lineage,
                                                   payload, authentication)
                        result_cache.put(source_bindings[source_id], lineage, payload)
                    cache[cache_key] = (folder / 'raw', markdown, digest(payload))
                verified_outcomes[source_id] = {'status': 'done', 'retry_count': lineage['child_ordinal']}
            def record_task(batch):
                tasks.append({'key': batch['key'], 'task_identity_sha256': task_identity(batch),
                              'batch_id': batch['batch_id'], 'data_ids': [item['id'] for item in batch['files']]})
                for item in batch['files']:
                    root_for_id[item['id']] = batch['key']
            default_terminal = TerminalRecovery(ledger, allowed_error_codes=allowed_error_codes,
                                                allowed_error_hashes=allowed_error_hashes)
            terminals = {}
            # Validate every stored controller before any provider operation.
            # Daily's per-batch continuation never makes malformed saved state
            # an excuse to create an unrelated fresh source task.
            for batch, group_pairs in groups:
                terminal = (terminal_factory(ledger, batch) if terminal_factory is not None else default_terminal)
                if terminal_factory is None:
                    control, _ = ledger.store.get('recoveries/' + batch['key'].split('/')[1])
                    if isinstance(control, dict) and isinstance(control.get('policy'), dict) and control['policy'].get('name') == AUTOMATIC_POLICY:
                        # A manual continuation resumes the already authorized
                        # Daily controller; it cannot reset its child budget.
                        terminal = TerminalRecovery(ledger, automatic=True)
                if not isinstance(terminal, TerminalRecovery) or terminal.ledger is not ledger:
                    reject('terminal_recovery_factory_invalid')
                terminal._read_control(batch)
                terminals[batch['key']] = terminal
                record_task(batch)
            incomplete_batches = []
            if continue_batches:
                for index, (batch, group_pairs) in enumerate(groups, 1):
                    assert_inputs(ledger, pairs, bindings)
                    # A pending first batch cannot consume the whole Daily run.
                    # Unused time is redistributed to the remaining batches.
                    budget = timeout if deadline is None else min(
                        timeout, max(0, deadline - ledger.clock()) / (len(groups) - index + 1))
                    if budget <= 0:
                        incomplete_batches.append(batch['key'])
                        daily_progress(index, batch, 'budget_exhausted')
                        continue
                    terminal = terminals[batch['key']]
                    counted_posts = False
                    active_batch_deadline = ledger.clock() + budget
                    try:
                        rows, summary = terminal.run(group_pairs,
                            authorization={'run_id': str(recovery_run_id), 'manifest_sha256': digest(raw_manifest)},
                            timeout=budget, interval=interval, queue_budget=queue_budget,
                            done_verifier=verify_done, partial=True)
                        posts += summary['provider_posts']
                        counted_posts = True
                        for path, row in rows:
                            verify_done(path, row)
                            resolved[row['data_id']] = row
                        ready = (summary.get('ready_for_generation') is True and len(rows) == len(group_pairs)
                                 and all((row['data_id'], row['full_zip_url']) in cache for _, row in rows))
                        if not ready:
                            incomplete_batches.append(batch['key'])
                        daily_progress(index, batch, 'complete' if ready else 'incomplete', ready=ready, summary=summary)
                    except (LedgerError, ConsumerError, RecoveryError) as error:
                        if not counted_posts:
                            posts += ledger.submission_posts
                        incomplete_batches.append(batch['key'])
                        category = safe_ledger_error_category(error) if isinstance(error, LedgerError) else type(error).__name__
                        daily_progress(index, batch, 'incomplete', category=category)
                        # Accepted/ambiguous tasks and completed ZIP cache entries
                        # remain durable; proceed without resubmitting this group.
                    finally:
                        active_batch_deadline = None
            else:
                # Manual strict mode keeps its complete original GET/ZIP
                # preflight before admitting even one failed recovery member.
                preflight = []
                for batch, group_pairs in groups:
                    terminal = terminals[batch['key']]
                    rows, summary = ledger._poll(batch['key'], batch['files'], ledger.clock() + remaining(),
                                                 interval, queue_budget, persist_terminal=False)
                    if (summary['missing'] or summary['pending'] or len(rows) != len(batch['files'])):
                        reject('original_task_incomplete')
                    terminal._proof(batch, rows)
                    preflight.append((batch, rows))
                for batch, rows in preflight:
                    terminal = terminals[batch['key']]
                    for row in rows.values():
                        verify_done(None, terminal._lineage(row, batch, batch, 0))
                assert_inputs(ledger, pairs, bindings)
                for batch, group_pairs in groups:
                    terminal = terminals[batch['key']]
                    rows, summary = terminal.run(group_pairs,
                        authorization={'run_id': str(recovery_run_id), 'manifest_sha256': digest(raw_manifest)},
                        timeout=remaining(), interval=interval, queue_budget=queue_budget, done_verifier=verify_done)
                    posts += summary['provider_posts']
                    if summary.get('ready_for_generation') is not True or len(rows) != len(group_pairs):
                        reject('recovery_task_incomplete')
                    for path, row in rows:
                        verify_done(path, row)
                        resolved[row['data_id']] = row
            for group_pairs in fresh:
                rows, summary = ledger.run(group_pairs, timeout=remaining(), interval=interval, queue_budget=queue_budget)
                posts += summary['provider_posts']
                if summary.get('ready_for_generation') is not True or len(rows) != len(group_pairs):
                    reject('fresh_task_incomplete')
                batch, _ = ledger._read_batch(summary['batch_keys'][0]); record_task(batch)
                for path, row in rows:
                    row['_recovery_lineage'] = {'batch_key': batch['key'], 'batch_id': batch['batch_id'],
                        'parent_batch_key': batch['key'], 'child_ordinal': 0, 'data_id': row['data_id']}
                    verify_done(path, row)
                    resolved[row['data_id']] = row
                if group_pairs is not fresh[-1]:
                    ledger.sleep(10)  # At most five fresh files per ten seconds.
            assert_inputs(ledger, pairs, bindings)
            # Deferral permits only other bounded parser work. Even one absent
            # child ZIP forbids every complete-source handoff and downstream PDF.
            if deferred:
                reject('ledger_child_result_tls_certificate_expired')
            if incomplete_batches:
                reject('recovery_task_incomplete')
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
                try:
                    with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                        if asset_writer is chart_assets:
                            images = asset_writer(raw_dir, assets, 100,
                                original_pdf_sha256=binding['content_sha256'], auth_original_pdf=path,
                                markdown_sha256=digest(markdown))
                        else:
                            images = asset_writer(raw_dir, assets, 100)
                except FigureSourceError as error:
                    error.source_ordinal = index
                    raise
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
                status.update(figure_source_status(directory))
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
            bucket = require_env('R2_BUCKET')
            store = R2Store('dropbox', client=client, bucket=bucket)
            ledger = Ledger(store, Provider(NoRedirectHTTP(requests.request), 'https://mineru.net'), 'dropbox',
                            'https://mineru.net', OPTIONS, credentials(env))
            receipt = recover_sources(ledger, args.input_dir, Path(args.input_dir) / MANIFEST,
                args.output_dir, args.expected_reports, args.date_folder, source_run_id=args.source_run_id,
                allow_fresh=args.allow_fresh, recovery_run_id=env.get('GITHUB_RUN_ID', ''), source_execution_sha=sha,
                recovery_execution_sha=env.get('GITHUB_SHA', ''),
                allowed_error_codes=codes, allowed_error_hashes=hashes, result_cache=ResultCache(client, bucket),
                authenticated_downloader=download_result)
    except (RecoveryError, LedgerError, ConsumerError, OSError, ValueError, KeyError, TypeError) as error:
        if isinstance(error, FigureSourceError):
            candidate = getattr(error, 'category', None)
            category = candidate if type(candidate) is str and candidate in FIGURE_ERROR_CATEGORIES else 'figure_proof_invalid'
        else:
            category = (safe_ledger_error_category(error) if isinstance(error, LedgerError)
                        else str(error) if isinstance(error, (RecoveryError, NetworkStop)) else type(error).__name__)
        ordinal = safe_figure_source_ordinal(error, args.expected_reports)
        suffix = ' source_ordinal=' + str(ordinal) if ordinal is not None else ''
        print('MinerU source recovery stopped: ' + category + suffix, file=sys.stderr)
        return 2
    except Exception as error:
        print('MinerU source recovery stopped: ' + type(error).__name__, file=sys.stderr)
        return 2
    print('MinerU source recovery complete: reports=' + str(receipt['report_count'])
          + ', manifest_sha256=' + receipt['manifest_sha256'])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
