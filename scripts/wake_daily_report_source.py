#!/usr/bin/env python3
"""Start one missed Daily batch after its Dropbox originals have settled."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import time
from urllib.parse import urlencode
from zoneinfo import ZoneInfo

from download_dropbox_latest_pdfs import (
    dropbox_access_token, list_folder, parse_date_folder, select_date_folder,
)
from recover_neutral_runner_loss import GitHub, execution_started

WORKFLOW = '.github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml'
WAKEUP = '.github/workflows/daily-report-source-wakeup.yml'
ACTIVE = ('in_progress', 'queued', 'pending', 'waiting', 'requested')
BEIJING = ZoneInfo('Asia/Shanghai')


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def read_source(now, *, token=None, reader=list_folder):
    token = token or dropbox_access_token()
    folder = select_date_folder(reader(token, '/zip_backup', recursive=False))
    day = str(folder['name'])
    age = (now.astimezone(BEIJING).date() - parse_date_folder(day)).days
    if not 0 <= age <= 1:
        return {'state': 'waiting_for_fresh_source', 'date_folder': day}
    path = folder.get('path_lower') or folder.get('path_display')
    require(isinstance(path, str) and path.lower() == '/zip_backup/' + day,
            'source_folder_identity_invalid')
    pdfs = [row for row in reader(token, path, recursive=True)
            if row.get('.tag') == 'file' and str(row.get('name', '')).lower().endswith('.pdf')]
    if not pdfs:
        return {'state': 'source_empty', 'date_folder': day}
    modified = []
    for row in pdfs:
        stamp = row.get('server_modified', '')
        require(isinstance(stamp, str) and re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', stamp),
                'source_modification_time_unknown')
        modified.append(datetime.fromisoformat(stamp.replace('Z', '+00:00')))
    if (now - max(modified)).total_seconds() < 900:
        return {'state': 'source_still_arriving', 'date_folder': day}
    return {'state': 'ready', 'date_folder': day, 'pdf_count': len(pdfs)}


def trusted(run, repository):
    return (isinstance(run, dict) and type(run.get('id')) is int and run['id'] > 0
            and run.get('path') == WORKFLOW and run.get('head_branch') == 'main'
            and run.get('event') in {'schedule', 'workflow_dispatch'}
            and (run.get('head_repository') or {}).get('full_name') == repository
            and (run.get('repository') or {}).get('full_name') == repository)


def runs(github, *, status=None, since=None):
    query = {'branch': 'main', 'per_page': 100}
    if status:
        query['status'] = status
    if since:
        query['created'] = '>=' + since
    result = github.api('actions/workflows/' + WORKFLOW.rsplit('/', 1)[-1] + '/runs?' + urlencode(query))
    rows, total = result.get('workflow_runs'), result.get('total_count')
    require(isinstance(rows, list) and type(total) is int and total == len(rows) <= 100,
            'daily_run_inventory_incomplete')
    require(all(trusted(row, github.repository) for row in rows), 'daily_run_identity_invalid')
    return rows


def active_run(github):
    for status in ACTIVE:
        rows = runs(github, status=status)
        require(all(row.get('status') == status for row in rows), 'daily_run_status_changed')
        if rows:
            return rows[0]['id']
    return None


def title_for(day):
    parse_date_folder(day)
    return 'Daily report articles and translations [' + day + ']'


def artifacts_for(github, run_id):
    # Forty processing and translation shards can legitimately retain more than
    # one API page. Keep a complete bounded inventory before declaring a date.
    rows, total, seen = [], None, set()
    for page in range(1, 6):
        result = github.api(f'actions/runs/{run_id}/artifacts?per_page=100&page={page}')
        chunk, observed = result.get('artifacts'), result.get('total_count')
        require(isinstance(chunk, list) and type(observed) is int and 0 <= observed <= 500
                and (total is None or observed == total)
                and len(chunk) == min(100, observed - len(rows)), 'daily_artifact_inventory_incomplete')
        total = observed
        for row in chunk:
            require(isinstance(row, dict) and type(row.get('id')) is int and row['id'] > 0
                    and row['id'] not in seen, 'daily_artifact_inventory_incomplete')
            seen.add(row['id'])
        rows.extend(chunk)
        if len(rows) == total:
            return rows
    raise ValueError('daily_artifact_inventory_incomplete')


def attempted_date(github, run):
    match = re.fullmatch(r'Daily report articles and translations \[([0-9]{6}|[0-9]{8})\]',
                         str(run.get('display_title', '')))
    if match:
        return parse_date_folder(match[1])
    rows = artifacts_for(github, run['id'])
    days = set()
    for row in rows:
        name = str(row.get('name', ''))
        patterns = (
            rf'daily-source-batch-([0-9]{{6}}|[0-9]{{8}})-{run["id"]}',
            r'final-dropbox-shard-diagnostics-([0-9]{6}|[0-9]{8})-[0-9]+',
            rf'(?:xhs-notes-wechat-drafts|publish-ready|portal-translated-reports)-([0-9]{{6}}|[0-9]{{8}})-{run["id"]}(?:-attempt-[0-9]+)?',
        )
        for pattern in patterns:
            match = re.fullmatch(pattern, name)
            if match:
                days.add(parse_date_folder(match[1]))
    require(len(days) <= 1, 'daily_source_date_ambiguous')
    if days:
        return days.pop()
    # A failed source download can recover once fresh originals arrive. Only
    # prove that case when selection and every processing job never executed.
    result = github.api(f"actions/runs/{run['id']}/attempts/{run['run_attempt']}/jobs?per_page=100")
    jobs, total = result.get('jobs'), result.get('total_count')
    require(isinstance(jobs, list) and type(total) is int and total == len(jobs) <= 100,
            'daily_job_inventory_incomplete')
    require(jobs and all(row.get('run_id') == run['id'] for row in jobs), 'daily_job_identity_invalid')
    selections = [job for job in jobs if job.get('name') == 'select-macro-reports']
    require(len(selections) == 1, 'daily_source_identity_unproven')
    steps = selections[0].get('steps') or []
    selection = [step for step in steps if step.get('name') == 'Select reports with DeepSeek']
    downloads = [step for step in steps if step.get('name') == 'Download PDFs from latest Dropbox date folder']
    require(len(selection) == len(downloads) == 1 and selection[0].get('conclusion') == 'skipped'
            and downloads[0].get('conclusion') == 'failure'
            and all(not execution_started(job) for job in jobs
                    if str(job.get('name', '')).startswith('process-shard')),
            'daily_source_identity_unproven')
    return None


def dispatch(github, day):
    # A lost acknowledgement is inspected by wake(); never retry this POST.
    result = subprocess.run(
        ['gh', 'api', f'repos/{github.repository}/actions/workflows/{WORKFLOW.rsplit("/", 1)[-1]}/dispatches',
         '--method', 'POST', '--input', '-'],
        input=json.dumps({'ref': 'main', 'inputs': {'dropbox_date_folder': day}}),
        text=True, capture_output=True, timeout=35, check=False,
    )
    return result.returncode == 0


def wake(github, now, *, source_reader=read_source, submit=dispatch, sleep=time.sleep):
    require(now.tzinfo is not None, 'wakeup_clock_invalid')
    if now.astimezone(BEIJING).hour < 2:
        return {'state': 'before_daily_start'}
    active = active_run(github)
    if active:
        return {'state': 'daily_active', 'run_id': active}
    source = source_reader(now)
    if source['state'] != 'ready':
        return source
    day = source['date_folder']
    since = (now - timedelta(days=3)).strftime('%Y-%m-%dT%H:%M:%SZ')
    recent = runs(github, since=since)
    for run in recent:
        if attempted_date(github, run) == parse_date_folder(day):
            return {'state': 'batch_already_attempted', 'date_folder': day, 'run_id': run['id']}
    # Inspect the queue again immediately before the single dispatch.
    active = active_run(github)
    if active:
        return {'state': 'daily_active', 'run_id': active}
    previous = {run['id'] for run in recent}
    try:
        acknowledged = submit(github, day)
    except (OSError, subprocess.TimeoutExpired):
        acknowledged = False
    for attempt in range(3):
        observed = runs(github, since=since)
        accepted = [run for run in observed if run['id'] not in previous
                    and run.get('display_title') == title_for(day)]
        require(len(accepted) <= 1, 'daily_dispatch_identity_ambiguous')
        if accepted:
            return {'state': 'dispatched', 'date_folder': day, 'pdf_count': source['pdf_count'],
                    'run_id': accepted[0]['id']}
        if attempt < 2:
            sleep(3)
    raise ValueError('daily_dispatch_readback_pending' if acknowledged else 'daily_dispatch_outcome_unknown')


def main():
    repository = os.environ.get('GITHUB_REPOSITORY', '')
    require(os.environ.get('GITHUB_ACTIONS') == 'true' and os.environ.get('GITHUB_REF') == 'refs/heads/main'
            and os.environ.get('GITHUB_EVENT_NAME') in {'schedule', 'workflow_dispatch'}
            and os.environ.get('GITHUB_WORKFLOW_REF') == repository + '/' + WAKEUP + '@refs/heads/main',
            'daily_wakeup_requires_main')
    try:
        result = wake(GitHub(repository), datetime.now(timezone.utc))
    except Exception as error:
        # Provider messages can contain credentials or private filenames.
        result = {'state': 'blocked', 'error_type': type(error).__name__}
        if isinstance(error, ValueError) and re.fullmatch(r'[a-z_]+', str(error)):
            result['reason'] = str(error)
    print(json.dumps(result, sort_keys=True))
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with Path(os.environ['GITHUB_STEP_SUMMARY']).open('a') as output:
            output.write('Daily source wake-up: ' + json.dumps(result, sort_keys=True) + '\n')
    return int(result['state'] == 'blocked')


if __name__ == '__main__':
    raise SystemExit(main())
