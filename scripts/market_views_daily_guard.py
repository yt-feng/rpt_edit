#!/usr/bin/env python3
"""Prepare a missing fresh Market Views issue independently of Daily completion.

This entrypoint only reads cloud state and writes private runner files. It never
dispatches a workflow, submits a model/MinerU task, publishes or sends a message.
The Actions caller serializes the later publisher with the normal PDF workflow.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys
import time
import tempfile
from zoneinfo import ZoneInfo

WORKFLOW = '.github/workflows/market-views-daily-guard.yml'
DAILY_WORKFLOW = '.github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml'
MANIFEST = 'selected_to_process_manifest.json'
SOURCE_ROOT = '/zip_backup'
BEIJING = ZoneInfo('Asia/Shanghai')
MAX_MANIFEST_BYTES = 16 * 1024 * 1024
MAX_REPORTS = 1000
RUN = re.compile(r'[1-9][0-9]{0,19}')
SHA = re.compile(r'[a-f0-9]{40}')
HASH = re.compile(r'[a-f0-9]{64}')


class GuardError(ValueError):
    """Fixed diagnostic categories; private metadata is never reflected."""


class DropboxUnavailable(GuardError):
    """Discovery could not read Dropbox, rather than observing an old batch."""


def reject(category):
    raise GuardError(category)


def exact_date(value):
    if not isinstance(value, str) or not re.fullmatch(r'[0-9]{6}', value):
        reject('invalid_source_date')
    try:
        return datetime.strptime('20' + value, '%Y%m%d').date()
    except ValueError:
        reject('invalid_source_date')


def validate_request(date_folder, source_run_id, acceptance_only, force_fallback, event):
    if date_folder:
        exact_date(date_folder)
    if source_run_id and (not RUN.fullmatch(source_run_id) or not date_folder):
        reject('exact_source_run_requires_date')
    if force_fallback and not acceptance_only:
        reject('forced_fallback_requires_acceptance')
    if event != 'workflow_dispatch' and any((date_folder, source_run_id, acceptance_only, force_fallback)):
        reject('manual_controls_require_manual_event')


def require_cloud_main(env, *, acceptance_only=False):
    repository = env.get('GITHUB_REPOSITORY', '')
    reference = env.get('GITHUB_REF', '')
    accepted_branch = (acceptance_only is True and env.get('GITHUB_EVENT_NAME') == 'workflow_dispatch'
                       and re.fullmatch(r'refs/heads/[A-Za-z0-9_./-]+', reference))
    if (env.get('GITHUB_ACTIONS') != 'true'
            or env.get('GITHUB_EVENT_NAME') not in {'schedule', 'workflow_run', 'workflow_dispatch'}
            or (reference != 'refs/heads/main' and not accepted_branch)
            or not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository)
            or env.get('GITHUB_WORKFLOW_REF') != repository + '/' + WORKFLOW + '@' + reference
            or not RUN.fullmatch(env.get('GITHUB_RUN_ID', ''))
            or not SHA.fullmatch(env.get('GITHUB_SHA', ''))):
        reject('reviewed_main_guard_required')
    return repository


def publication_decision(date_folder, now, complete, *, acceptance_only=False, cutoff_hour=6):
    """Publication failure and unavailable storage must be distinguished upstream."""
    if now.tzinfo is None or type(complete) is not bool or not 0 <= cutoff_hour <= 23:
        reject('invalid_guard_clock_or_publication_state')
    local = now.astimezone(BEIJING)
    age = (local.date() - exact_date(date_folder)).days
    if not 0 <= age <= 1:
        reject('latest_source_is_stale_or_future')
    if complete and not acceptance_only:
        return {'should_build': False, 'reason': 'verified_private_publication'}
    if not acceptance_only and local.hour < cutoff_hour:
        return {'should_build': False, 'reason': 'before_daily_publication_cutoff'}
    return {'should_build': True, 'reason': 'acceptance_requested' if acceptance_only else 'missing_daily_publication'}


def checked_producer(value, source_run_id, repository):
    if (not isinstance(value, dict) or not RUN.fullmatch(str(source_run_id))
            or value.get('id') != int(source_run_id)
            or value.get('path') != DAILY_WORKFLOW or value.get('head_branch') != 'main'
            or value.get('event') not in {'schedule', 'workflow_dispatch'}
            or value.get('status') not in {'queued', 'in_progress', 'completed', 'waiting', 'pending', 'requested'}
            or value.get('repository', {}).get('full_name') != repository
            or value.get('head_repository', {}).get('full_name') != repository
            or not SHA.fullmatch(str(value.get('head_sha', '')))):
        reject('daily_source_producer_mismatch')
    # A running Daily is intentionally accepted: original selection precedes
    # report processing, translation and all complete-batch gates.
    return value


def checked_manifest(raw, date_folder):
    if not isinstance(raw, bytes) or not 1 <= len(raw) <= MAX_MANIFEST_BYTES:
        reject('selected_manifest_size')
    def unique(entries):
        result = {}
        for key, value in entries:
            if key in result:
                reject('selected_manifest_duplicate_key')
            result[key] = value
        return result
    try:
        rows = json.loads(raw, object_pairs_hook=unique)
    except (ValueError, UnicodeError):
        reject('selected_manifest_json')
    if not isinstance(rows, list) or not 1 <= len(rows) <= MAX_REPORTS:
        reject('selected_manifest_count')
    dates, names = set(), set()
    for row in rows:
        if not isinstance(row, dict):
            reject('selected_manifest_entry')
        dropbox = row.get('dropbox_path')
        local = row.get('process_local_path')
        if (not isinstance(dropbox, str) or '\\' in dropbox
                or any(ord(char) < 32 for char in dropbox)
                or not isinstance(local, str) or '\\' in local
                or any(ord(char) < 32 for char in local)):
            reject('selected_manifest_path')
        parts = PurePosixPath(dropbox).parts
        source = PurePosixPath(local).name
        if (len(parts) < 4 or parts[:2] != ('/', 'zip_backup') or '..' in parts
                or not source.lower().endswith('.pdf') or ':' in source
                or source in names or not HASH.fullmatch(str(row.get('content_sha256', '')))):
            reject('selected_manifest_binding')
        exact_date(parts[2])
        dates.add(parts[2])
        names.add(source)
    if len(dates) != 1:
        reject('selected_manifest_mixed_dates')
    if date_folder is not None and next(iter(dates)) != date_folder:
        return None
    return rows


class Github:
    def __init__(self, repository, *, runner=subprocess.run, sleep=time.sleep):
        self.repository, self.runner, self.sleep = repository, runner, sleep

    def command(self, args, *, timeout=60):
        # Metadata failures never become an empty list or an absent artifact.
        for attempt in range(3):
            try:
                result = self.runner(['gh', *args], check=False, capture_output=True, timeout=timeout)
                if result.returncode == 0:
                    return result.stdout
            except (subprocess.TimeoutExpired, OSError):
                pass
            if attempt < 2:
                self.sleep(2 ** attempt)
        reject('github_read_unavailable_after_retries')

    def api(self, suffix):
        raw = self.command(['api', f'repos/{self.repository}/{suffix}'])
        if len(raw) > 8 * 1024 * 1024:
            reject('github_metadata_size')
        try:
            value = json.loads(raw)
        except (ValueError, UnicodeError):
            reject('github_metadata_json')
        if not isinstance(value, dict):
            reject('github_metadata_shape')
        return value

    def run(self, run_id):
        return checked_producer(self.api(f'actions/runs/{run_id}'), run_id, self.repository)

    def candidates(self, now):
        value = self.api('actions/workflows/dropbox-latest-pdf-to-xhs-sharded.yml/runs?branch=main&per_page=30')
        rows = value.get('workflow_runs')
        if not isinstance(rows, list) or len(rows) > 30:
            reject('daily_run_listing_invalid')
        result = []
        for row in rows:
            if not isinstance(row, dict):
                reject('daily_run_listing_invalid')
            # Explicitly exclude PR/fork contexts before opening any artifact.
            if row.get('event') not in {'schedule', 'workflow_dispatch'} or row.get('head_branch') != 'main':
                continue
            try:
                created = datetime.fromisoformat(str(row.get('created_at', '')).replace('Z', '+00:00'))
                recent = now - timedelta(days=3) <= created <= now + timedelta(minutes=5)
            except (ValueError, TypeError):
                reject('daily_run_created_at_invalid')
            if recent:
                result.append(self.run(str(row.get('id', ''))))
        return result

    def has_artifact(self, run_id, name):
        matches = []
        for page in range(1, 6):
            value = self.api(f'actions/runs/{run_id}/artifacts?per_page=100&page={page}')
            rows, count = value.get('artifacts'), value.get('total_count')
            if (not isinstance(rows, list) or len(rows) > 100 or type(count) is not int
                    or not 0 <= count <= 500 or any(not isinstance(row, dict) for row in rows)):
                reject('daily_artifact_listing_invalid')
            matches.extend(row for row in rows if row.get('name') == name and row.get('expired') is False)
            if page * 100 >= count:
                break
        if len(matches) > 1:
            reject('daily_artifact_ambiguous')
        return bool(matches)

    def download(self, run_id, name, destination):
        destination.mkdir(parents=True, exist_ok=True)
        # A failed extraction may leave files behind. Retry in a fresh private
        # directory, then materialize one successful download atomically.
        for attempt in range(3):
            with tempfile.TemporaryDirectory(dir=destination.parent, prefix='artifact-') as temporary:
                try:
                    result = self.runner(['gh', 'run', 'download', str(run_id), '--repo', self.repository,
                                          '--name', name, '--dir', temporary], check=False,
                                         capture_output=True, timeout=300)
                    if result.returncode == 0:
                        shutil.copytree(temporary, destination, dirs_exist_ok=True)
                        return
                except (subprocess.TimeoutExpired, OSError):
                    pass
            if attempt < 2:
                self.sleep(2 ** attempt)
        reject('github_read_unavailable_after_retries')


def discover_source(github, date_folder, workspace, now, source_run_id='', *, diagnostics=None):
    """Choose only authenticated manifests, isolating an unusable candidate.

    A null date is used only after Dropbox discovery is unavailable. In that
    case the newest source date proven by a fresh Daily manifest is chosen;
    today's manual replay of an older batch cannot hide a newer source date.
    """
    def omitted(category):
        if diagnostics is not None:
            diagnostics[category] = diagnostics.get(category, 0) + 1
    candidates = [github.run(source_run_id)] if source_run_id else github.candidates(now)
    best = (None, None, None)
    best_date = None
    for producer in candidates:
        run_id = str(producer['id'])
        name = f'selected-macro-manifest-{run_id}'
        try:
            if not github.has_artifact(run_id, name):
                if source_run_id:
                    reject('requested_daily_manifest_unavailable')
                omitted('candidate_manifest_missing')
                continue
            destination = workspace / 'candidate-manifests' / run_id
            github.download(run_id, name, destination)
            manifest = destination / MANIFEST
            if not manifest.is_file() or manifest.is_symlink():
                reject('selected_manifest_file_missing')
            raw = manifest.read_bytes()
            rows = checked_manifest(raw, date_folder)
        except (GuardError, OSError, UnicodeError) as error:
            if source_run_id:
                raise
            omitted('candidate_manifest_unavailable' if isinstance(error, GuardError)
                    and str(error) == 'github_read_unavailable_after_retries' else 'candidate_manifest_invalid')
            continue
        if rows is not None:
            if date_folder is not None:
                return producer, raw, rows
            candidate_date = PurePosixPath(rows[0]['dropbox_path']).parts[2]
            age = (now.astimezone(BEIJING).date() - exact_date(candidate_date)).days
            if not 0 <= age <= 1:
                omitted('candidate_manifest_stale_or_future')
                continue
            if best_date is None or exact_date(candidate_date) > exact_date(best_date):
                best, best_date = (producer, raw, rows), candidate_date
            if age == 0:
                return best
            continue
        if source_run_id:
            reject('requested_daily_manifest_date_mismatch')
        omitted('candidate_manifest_other_date')
    return best


def restore_originals(github, producer, raw, rows, original_dir):
    original_dir.mkdir(parents=True, exist_ok=True)
    run_id = str(producer['id'])
    name = f'selected-macro-pdfs-{run_id}'
    if github.has_artifact(run_id, name):
        github.download(run_id, name, original_dir)
        downloaded = original_dir / MANIFEST
        if not downloaded.is_file() or downloaded.is_symlink() or downloaded.read_bytes() != raw:
            reject('original_and_selection_manifests_differ')
        return True
    return False


def verify_originals(original_dir, raw, rows):
    expected = {PurePosixPath(row['process_local_path']).name: row['content_sha256'] for row in rows}
    actual = {}
    for path in original_dir.rglob('*'):
        if path.is_symlink():
            reject('original_input_symlink')
        if path.is_file() and path.suffix.lower() == '.pdf':
            if path.name in actual:
                reject('original_input_duplicate_name')
            actual[path.name] = path
    if set(actual) - set(expected) or (original_dir / MANIFEST).read_bytes() != raw:
        reject('original_input_inventory_mismatch')
    verified, omitted = [], []
    for name, digest in expected.items():
        path = actual.get(name)
        if path is None:
            omitted.append({'source_pdf': name, 'reason': 'original_missing'})
            continue
        payload = path.read_bytes()
        if not payload.startswith(b'%PDF-') or hashlib.sha256(payload).hexdigest() != digest:
            omitted.append({'source_pdf': name, 'reason': 'original_hash_mismatch'})
            continue
        verified.append(name)
    return {'verified_count': len(verified), 'omitted_count': len(omitted), 'omissions': omitted}


def latest_dropbox_date(now, requested=''):
    from download_dropbox_latest_pdfs import dropbox_access_token, list_folder, latest_date_folder
    try:
        token = dropbox_access_token()
        entries = list_folder(token, SOURCE_ROOT, recursive=False)
    except Exception:
        # Only failed external reads get this category. A successful listing
        # proving stale/future sources or an explicit-date mismatch still fails.
        raise DropboxUnavailable('dropbox_discovery_unavailable') from None
    entry = latest_date_folder(entries)
    name = str(entry['name'])
    exact_date(name)
    if requested and requested != name:
        reject('requested_date_is_not_latest_dropbox_batch')
    if not 0 <= (now.astimezone(BEIJING).date() - exact_date(name)).days <= 1:
        reject('latest_source_is_stale_or_future')
    return name


def download_original_bounded(token, path, target, *, deadline, request=None, clock=time.monotonic,
                              sleep=time.sleep):
    """At most two read-only downloads, with per-file and whole-intake bounds."""
    import requests
    from download_dropbox_latest_pdfs import DROPBOX_CONTENT
    request = request or requests.post
    file_deadline = min(deadline, clock() + 65)
    for attempt in range(2):
        remaining = file_deadline - clock()
        if remaining <= 0:
            reject('original_download_deadline')
        try:
            response = request(DROPBOX_CONTENT + '/files/download',
                headers={'Authorization': 'Bearer ' + token,
                         'Dropbox-API-Arg': json.dumps({'path': path})},
                timeout=(min(10, remaining), min(25, remaining)), stream=True, allow_redirects=False)
            with response:
                if response.status_code != 200:
                    if response.status_code not in {408, 425, 429, 500, 502, 503, 504}:
                        reject('original_download_rejected')
                    raise requests.ConnectionError('retryable_download_status')
                target.parent.mkdir(parents=True, exist_ok=True)
                total = 0
                with target.open('wb') as stream:
                    for chunk in response.iter_content(chunk_size=65536):
                        total += len(chunk)
                        if clock() > file_deadline or total > 512 * 1024 * 1024:
                            reject('original_download_bound')
                        stream.write(chunk)
                return
        except (requests.RequestException, OSError):
            target.unlink(missing_ok=True)
            if attempt == 1:
                reject('original_download_unavailable')
            sleep(min(1, max(0, file_deadline - clock())))
    reject('original_download_unavailable')


def download_fresh_originals(date_folder, original_dir):
    from download_dropbox_latest_pdfs import dropbox_access_token, list_folder
    from select_macro_trend_pdfs import sanitize_filename
    import fitz
    token = dropbox_access_token()
    entries = list_folder(token, f'{SOURCE_ROOT}/{date_folder}', recursive=True)
    pdfs = [entry for entry in entries if entry.get('.tag') == 'file'
            and str(entry.get('name', '')).lower().endswith('.pdf')]
    if not 1 <= len(pdfs) <= MAX_REPORTS:
        reject('fresh_source_count_invalid')
    download_dir = original_dir.parent / 'dropbox-originals'
    download_dir.mkdir(parents=True, exist_ok=True)
    original_dir.mkdir(parents=True, exist_ok=True)
    rows, unavailable = [], []
    deadline = time.monotonic() + 600
    for index, entry in enumerate(sorted(pdfs, key=lambda item: str(item.get('path_lower', ''))), 1):
        path = entry.get('path_lower') or entry.get('path_display')
        if (not isinstance(path, str) or PurePosixPath(path).parts[:3] != ('/', 'zip_backup', date_folder)
                or '..' in PurePosixPath(path).parts or '\\' in path):
            reject('fresh_source_path_invalid')
        target = download_dir / f'{index:04d}.pdf'
        source_name = sanitize_filename(str(entry.get('name') or ''), f'report-{index}.pdf')
        # Keep failed downloads distinct even if Dropbox folders reuse the same
        # basename. Private Dropbox paths never enter the publication receipt.
        unavailable_name = f'unavailable-{index:04d}-{source_name}'
        try:
            download_original_bounded(token, path, target, deadline=deadline)
        except Exception:
            target.unlink(missing_ok=True)
            unavailable.append({'source_pdf': unavailable_name, 'reason': 'original_download_unavailable'})
            continue
        selected_target = original_dir / f'{index:04d}-{source_name}'
        try:
            payload = target.read_bytes()
            if not payload.startswith(b'%PDF-'):
                raise ValueError('invalid_original_pdf')
            with fitz.open(stream=payload, filetype='pdf') as document:
                if document.needs_pass or document.page_count <= 0:
                    raise ValueError('invalid_original_pdf')
        except Exception:
            unavailable.append({'source_pdf': unavailable_name, 'reason': 'original_invalid_pdf'})
            continue
        try:
            selected_target.write_bytes(payload)
        except OSError:
            selected_target.unlink(missing_ok=True)
            unavailable.append({'source_pdf': unavailable_name, 'reason': 'original_materialization_failed'})
            continue
        rows.append({'dropbox_path': path, 'local_path': str(target), 'name': entry['name'],
                     'process_rank': index, 'process_local_path': str(selected_target),
                     'content_sha256': hashlib.sha256(payload).hexdigest()})
    if not rows:
        reject('no_fresh_original_bytes_available')
    selected = rows
    raw = json.dumps(selected, ensure_ascii=False, indent=2).encode()
    checked_manifest(raw, date_folder)
    (original_dir / MANIFEST).write_bytes(raw)
    return raw, selected, unavailable


def restore_handoffs(client, bucket, source_run_id, date_folder, workspace):
    from private_workflow_handoff import list_keys, download_shards
    result = {}
    for label, namespace in (('handoff', 'xhs'), ('available', 'market-views-available')):
        destination = workspace / (label + '-sources')
        destination.mkdir(parents=True, exist_ok=True)
        result[label + '_dir'] = str(destination)
        result[label + '_shards'] = 0
        if not source_run_id:
            continue
        prefix = f'_private-workflow-handoff/{namespace}/{source_run_id}/{date_folder}'
        try:
            keys = list_keys(prefix, client=client, bucket=bucket)
            if any(re.fullmatch(re.escape(prefix) + r'/shard_[0-9]+\.tar\.gz', key) for key in keys):
                result[label + '_shards'] = download_shards(prefix, destination, expected_count=0,
                                                           client=client, bucket=bucket)
        except Exception:
            # These snapshots are optional accelerators, never the sole path
            # to today's issue. A failed download must not expose its partially
            # extracted directory to the source collector.
            shutil.rmtree(destination)
            destination.mkdir(parents=True)
            result[label + '_restore_status'] = 'unavailable_original_fallback_required'
    return result


def retained_reports_per_shard(handoff_dir, available_dir, *, source_run_id, source_sha, manifest_sha):
    """Return a legacy-only hint; new snapshots authenticate their own mapping."""
    values = []
    for path in Path(handoff_dir).glob('shard_*/shard_run_summary.md'):
        if path.is_symlink() or path.stat().st_size > 100_000:
            return 0
        matches = re.findall(r'^- Reports per shard: ([1-9][0-9]*)\s*$', path.read_text(), re.M)
        if len(matches) != 1 or not 1 <= int(matches[0]) <= MAX_REPORTS:
            return 0
        values.append(int(matches[0]))
    if len(set(values)) > 1:
        # The assembly can still read each fully bound available receipt; do
        # not apply any positional assumptions to legacy handoffs.
        return 0
    return values[0] if values else 0


def prepare(workspace, *, now, repository, date_folder='', source_run_id='', acceptance_only=False,
            force_fallback=False, env=None, github=None, client=None, bucket=None,
            discover_date=None, publication_check=None):
    from private_workflow_handoff import build_r2_client, r2_bucket
    from upload_market_view_to_r2 import private_publication_complete
    env = os.environ if env is None else env
    validate_request(date_folder, source_run_id, acceptance_only, force_fallback, env['GITHUB_EVENT_NAME'])
    workspace = Path(workspace).resolve()
    workspace.mkdir(parents=True, exist_ok=True)
    discovery_omissions = {}
    date_authority = 'dropbox-latest'
    prefetched = None
    try:
        date_folder = (discover_date or latest_dropbox_date)(now, date_folder)
    except DropboxUnavailable:
        github = github or Github(repository)
        prefetched = discover_source(github, date_folder or None, workspace, now, source_run_id,
                                     diagnostics=discovery_omissions)
        if prefetched[0] is None:
            reject('dropbox_unavailable_and_no_fresh_daily_manifest')
        date_folder = PurePosixPath(prefetched[2][0]['dropbox_path']).parts[2]
        if not 0 <= (now.astimezone(BEIJING).date() - exact_date(date_folder)).days <= 1:
            reject('latest_source_is_stale_or_future')
        date_authority = 'authenticated-daily-manifest-dropbox-unavailable'
    client = client or build_r2_client()
    bucket = bucket or r2_bucket()
    # Do not catch authentication, transport or truncated R2 response errors:
    # they cannot authorize treating an existing publication as missing.
    complete = (publication_check or private_publication_complete)(date_folder, client=client, bucket=bucket)
    decision = publication_decision(date_folder, now, complete, acceptance_only=acceptance_only)
    plan = {'schema_version': 1, 'date_folder': date_folder, **decision,
            'private_publication_verified': complete, 'acceptance_only': acceptance_only,
            'force_fallback': force_fallback, 'provider_posts': 0, 'model_calls': 0,
            'workflow_dispatches': 0, 'production_writes': 0,
            'date_discovery_authority': date_authority,
            'source_discovery_omissions': discovery_omissions}
    if not decision['should_build']:
        return plan
    github = github or Github(repository)
    fallback_reason = ''
    try:
        producer, raw, rows = prefetched or discover_source(github, date_folder, workspace, now, source_run_id,
                                                           diagnostics=discovery_omissions)
    except GuardError as error:
        if str(error) != 'github_read_unavailable_after_retries' or source_run_id:
            raise
        # Source metadata unavailable is not evidence that Daily failed. An
        # independent Dropbox-bound source can still produce today's issue.
        producer, raw, rows = None, None, None
        fallback_reason = 'daily_metadata_unavailable_using_independent_dropbox'
    original_dir = workspace / 'originals'
    unavailable = []
    if producer is not None:
        try:
            restored = restore_originals(github, producer, raw, rows, original_dir)
        except GuardError as error:
            if str(error) != 'github_read_unavailable_after_retries' or source_run_id:
                raise
            restored = False
        if not restored:
            if source_run_id:
                reject('requested_daily_original_artifact_unavailable')
            producer, raw, rows = None, None, None
            fallback_reason = 'daily_original_artifact_unavailable_using_independent_dropbox'
            shutil.rmtree(original_dir)
    if producer is None:
        raw, rows, unavailable = download_fresh_originals(date_folder, original_dir)
        source_run_id = env['GITHUB_RUN_ID']
        source_kind = 'fresh-dropbox'
        source_sha = env['GITHUB_SHA']
    else:
        source_run_id = str(producer['id'])
        source_sha = producer['head_sha']
        source_kind = 'daily-selected-originals'
    original_validation = verify_originals(original_dir, raw, rows)
    retained = restore_handoffs(client, bucket, source_run_id if producer else '', date_folder, workspace)
    reports_per_shard = retained_reports_per_shard(retained['handoff_dir'], retained['available_dir'],
        source_run_id=source_run_id, source_sha=source_sha, manifest_sha=hashlib.sha256(raw).hexdigest())
    context = {'schema_version': 1, 'repository': repository, 'date_folder': date_folder,
               'source_kind': source_kind, 'source_run_id': source_run_id,
               'source_execution_sha': source_sha, 'source_workflow': DAILY_WORKFLOW if producer else WORKFLOW,
               'guard_run_id': env['GITHUB_RUN_ID'], 'guard_execution_sha': env['GITHUB_SHA'],
               'selected_manifest_sha256': hashlib.sha256(raw).hexdigest(), 'expected_reports': len(rows),
               'original_validation': original_validation, 'unavailable_originals': unavailable,
               'expected_source_reports': len(rows) + len(unavailable), 'fallback_reason': fallback_reason,
               'date_discovery_authority': date_authority, 'source_discovery_omissions': discovery_omissions,
               'reports_per_shard': reports_per_shard,
               'originals_dir': str(original_dir), 'manifest_path': str(original_dir / MANIFEST),
               'source_producer': producer, **retained}
    context_path = workspace / 'source-context.json'
    context_path.write_text(json.dumps(context, indent=2) + '\n')
    plan.update({key: context[key] for key in ('source_run_id', 'expected_reports', 'manifest_path',
                                              'originals_dir', 'handoff_dir', 'available_dir')})
    plan['context_path'] = str(context_path)
    return plan


def write_outputs(plan, workspace, env):
    (workspace / 'plan.json').write_text(json.dumps(plan, indent=2) + '\n')
    output = env.get('GITHUB_OUTPUT')
    if output:
        with open(output, 'a', encoding='utf-8') as stream:
            for key, value in plan.items():
                if type(value) is bool:
                    value = str(value).lower()
                if isinstance(value, (str, int)):
                    if '\n' in str(value) or '\r' in str(value):
                        reject('invalid_workflow_output')
                    stream.write(f'{key}={value}\n')
    summary = env.get('GITHUB_STEP_SUMMARY')
    if summary:
        with open(summary, 'a', encoding='utf-8') as stream:
            stream.write(f"Market Views guard: `{plan['reason']}`; source date `{plan['date_folder']}`.\n")
    print(f"Market Views guard: {plan['reason']}; date={plan['date_folder']}; should_build={plan['should_build']}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['prepare'])
    parser.add_argument('--workspace', type=Path, required=True)
    parser.add_argument('--date-folder', default='')
    parser.add_argument('--source-run-id', default='')
    parser.add_argument('--acceptance-only', action='store_true')
    parser.add_argument('--force-fallback', action='store_true')
    args = parser.parse_args()
    try:
        repository = require_cloud_main(os.environ, acceptance_only=args.acceptance_only)
        plan = prepare(args.workspace, now=datetime.now(timezone.utc), repository=repository,
                       date_folder=args.date_folder, source_run_id=args.source_run_id,
                       acceptance_only=args.acceptance_only, force_fallback=args.force_fallback)
        write_outputs(plan, args.workspace.resolve(), os.environ)
    except Exception as error:
        category = str(error) if isinstance(error, GuardError) else type(error).__name__
        print('Market Views guard preparation failed: ' + category, file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
