#!/usr/bin/env python3
"""Retry one proven pre-upload hosted-runner loss, never a deployment failure."""
from __future__ import annotations

import json
import os
from pathlib import Path
import re
import subprocess
import time
from urllib.parse import urlencode

WORKFLOW = '.github/workflows/neutral-edge-cutover.yml'
UPLOAD_STEP = 'Upload inactive static slot and immutable runtime'
RUNNER_LOSS = 'The hosted runner lost communication with the server.'
AUTOMATIC_EVENTS = {'schedule', 'workflow_run'}
ACTIVE = {'queued', 'requested', 'waiting', 'pending', 'in_progress'}
IDENTITY = ('id', 'run_attempt', 'head_sha', 'head_branch', 'event', 'path', 'workflow_id')


class RecoveryError(Exception):
    pass


def require(condition, reason):
    if not condition:
        raise RecoveryError(reason)


class GitHub:
    """Bound read retries; a mutation always has exactly one transport attempt."""
    def __init__(self, repository, *, sleep=time.sleep):
        require(re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository), 'invalid_repository')
        self.repository, self.sleep = repository, sleep

    def api(self, suffix, method='GET'):
        require(method in {'GET', 'POST'} and not suffix.startswith('/'), 'invalid_api_request')
        attempts = 3 if method == 'GET' else 1
        for attempt in range(attempts):
            try:
                result = subprocess.run(
                    ['gh', 'api', f'repos/{self.repository}/{suffix}', '--method', method],
                    capture_output=True, check=False, timeout=35,
                )
                if result.returncode == 0:
                    require(len(result.stdout) <= 4 * 1024 * 1024, 'github_response_oversized')
                    return json.loads(result.stdout) if result.stdout.strip() else None
                status = re.search(r'\bHTTP (\d{3})\b', result.stderr.decode('utf-8', errors='replace'))
                if status and int(status[1]) not in {408, 429, 500, 502, 503, 504}:
                    raise RecoveryError('github_http_' + status[1])
            except (OSError, subprocess.TimeoutExpired):
                pass
            except (ValueError, UnicodeError):
                raise RecoveryError('github_response_invalid') from None
            if attempt + 1 < attempts:
                self.sleep((1, 3)[attempt])
        raise RecoveryError('github_read_failed' if method == 'GET' else 'rerun_response_unknown')


def trusted(run, repository):
    return (isinstance(run, dict) and run.get('path') == WORKFLOW
            and run.get('head_branch') == 'main'
            and re.fullmatch(r'[a-f0-9]{40}', str(run.get('head_sha', '')))
            and type(run.get('id')) is int and run['id'] > 0
            and type(run.get('workflow_id')) is int and run['workflow_id'] > 0
            and type(run.get('run_attempt')) is int and run['run_attempt'] > 0
            and all((run.get(key) or {}).get('full_name') == repository
                    for key in ('repository', 'head_repository')))


def same_run(left, right, repository):
    return (trusted(left, repository) and trusted(right, repository)
            and all(left.get(key) == right.get(key) for key in IDENTITY))


def jobs_for(github, run):
    value = github.api(f"actions/runs/{run['id']}/attempts/{run['run_attempt']}/jobs?per_page=100")
    rows = value.get('jobs', [])
    require(isinstance(rows, list) and type(value.get('total_count')) is int
            and value['total_count'] == len(rows) <= 100 and rows, 'incomplete_job_inventory')
    require(all(isinstance(row, dict) and type(row.get('id')) is int
                and row['id'] > 0 and row.get('run_id') == run['id']
                and row.get('head_sha') == run['head_sha'] for row in rows)
            and len({row['id'] for row in rows}) == len(rows), 'job_identity_mismatch')
    return rows


def execution_started(job):
    return bool(job.get('runner_id') or job.get('runner_name')
                or any(step.get('status') == 'in_progress'
                       or step.get('conclusion') not in (None, 'skipped')
                       for step in job.get('steps') or []))


def prove_runner_loss(github, run):
    rows = jobs_for(github, run)
    preparation = [row for row in rows if row.get('name') == 'prepare_release']
    require(len(preparation) == 1, 'preparation_job_missing_or_ambiguous')
    job = preparation[0]
    require(job.get('status') == 'completed' and job.get('conclusion') == 'failure',
            'preparation_not_failed')
    downstream = [row for row in rows if row is not job]
    require(sum(row.get('name') == 'cutover' for row in downstream) == 1,
            'cutover_absence_unproven')
    require(all(row.get('status') == 'completed' and row.get('conclusion') == 'skipped'
                and not execution_started(row) for row in downstream), 'downstream_execution_present')
    steps = job.get('steps') or []
    uploads = [step for step in steps if step.get('name') == UPLOAD_STEP]
    interrupted = [step for step in steps if step.get('status') == 'in_progress']
    require(len(uploads) == 1 and type(uploads[0].get('number')) is int
            and len(interrupted) == 1 and type(interrupted[0].get('number')) is int
            and interrupted[0]['number'] < uploads[0]['number'], 'pre_upload_interruption_unproven')
    require(not any(step.get('conclusion') in {'failure', 'cancelled', 'timed_out'} for step in steps)
            and all(step.get('status') in {'pending', 'queued'}
                    or step.get('conclusion') == 'skipped'
                    for step in steps if step.get('number', 0) >= uploads[0]['number']),
            'application_failure_or_upload_started')
    match = re.fullmatch(r'https://api\.github\.com/repos/' + re.escape(github.repository)
                         + r'/check-runs/([1-9][0-9]*)', str(job.get('check_run_url', '')))
    require(match is not None, 'check_identity_missing')
    check_id = match.group(1)
    check = github.api(f'check-runs/{check_id}')
    require(check.get('id') == int(check_id) and check.get('name') == 'prepare_release'
            and check.get('head_sha') == run['head_sha'] and check.get('status') == 'completed'
            and check.get('conclusion') == 'failure', 'check_identity_mismatch')
    count = (check.get('output') or {}).get('annotations_count')
    require(type(count) is int and 1 <= count <= 100, 'annotation_inventory_unavailable')
    annotations = github.api(f'check-runs/{check_id}/annotations?per_page=100')
    require(isinstance(annotations, list) and len(annotations) == count
            and all(isinstance(row, dict) for row in annotations), 'incomplete_annotations')
    failures = [row for row in annotations if row.get('annotation_level') == 'failure']
    require(failures and all(str(row.get('message', '')).startswith(RUNNER_LOSS) for row in failures),
            'not_exclusively_hosted_runner_loss')
    return job['id']


def superseding_run(github, source):
    created = source.get('created_at', '')
    require(re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', created), 'source_creation_time_invalid')
    query = urlencode({'branch': 'main', 'per_page': 100, 'created': '>=' + created})
    value = github.api(f"actions/workflows/{source['workflow_id']}/runs?{query}")
    rows = value.get('workflow_runs', [])
    require(isinstance(rows, list) and type(value.get('total_count')) is int
            and value['total_count'] == len(rows) <= 100
            and all(isinstance(row, dict) for row in rows), 'recent_run_inventory_incomplete')
    for row in rows:
        if (not trusted(row, github.repository) or row['id'] <= source['id']
                or row['workflow_id'] != source['workflow_id']
                or row.get('event') not in AUTOMATIC_EVENTS | {'workflow_dispatch'}):
            continue
        if row.get('status') in ACTIVE:
            return row['id']
        if row.get('status') == 'completed' and row.get('conclusion') == 'success':
            # Ineligible upstream completions produce all-skipped green runs.
            # Only a successful, executed preparation supersedes this refresh.
            jobs = jobs_for(github, row)
            if any(job.get('name') == 'prepare_release' and job.get('conclusion') == 'success'
                   and execution_started(job) for job in jobs):
                return row['id']
    return None


def recover(github, event_run, *, sleep=time.sleep):
    result = {'status': 'skipped', 'reason': '', 'run_id': event_run.get('id')}
    if not trusted(event_run, github.repository) or event_run.get('event') not in AUTOMATIC_EVENTS:
        return {**result, 'reason': 'ineligible_source'}
    if event_run.get('run_attempt') != 1:
        return {**result, 'reason': 'automatic_retry_budget_exhausted'}
    path = f"actions/runs/{event_run['id']}"
    try:
        current = github.api(path)
        require(same_run(current, event_run, github.repository), 'source_attempt_changed')
        require(current.get('status') == 'completed' and current.get('conclusion') == 'failure',
                'source_not_completed_failure')
        job_id = prove_runner_loss(github, current)
        superseded = superseding_run(github, current)
        if superseded is not None:
            return {**result, 'reason': 'newer_refresh_supersedes', 'superseding_run_id': superseded}
        # Re-read the exact attempt and job evidence immediately before the write.
        latest = github.api(path)
        require(same_run(latest, current, github.repository)
                and latest.get('status') == 'completed' and latest.get('conclusion') == 'failure',
                'source_attempt_changed')
        require(prove_runner_loss(github, latest) == job_id, 'preparation_job_changed')
        superseded = superseding_run(github, latest)
        if superseded is not None:
            return {**result, 'reason': 'newer_refresh_supersedes', 'superseding_run_id': superseded}
    except RecoveryError as error:
        return {**result, 'reason': str(error)}
    acknowledged = False
    try:
        github.api(path + '/rerun-failed-jobs', 'POST')
        acknowledged = True
    except RecoveryError as error:
        if str(error).startswith('github_http_'):
            return {**result, 'status': 'failed', 'reason': str(error)}
        # A lost response may hide an accepted rerun. Never send another POST.
        pass
    for poll in range(5):
        try:
            observed = github.api(path)
            if (trusted(observed, github.repository)
                    and all(observed.get(key) == current.get(key) for key in IDENTITY if key != 'run_attempt')
                    and observed['run_attempt'] > current['run_attempt']):
                return {**result, 'status': 'recovered', 'reason': 'new_attempt_observed',
                        'run_attempt': observed['run_attempt'], 'job_id': job_id}
        except RecoveryError:
            pass
        if poll < 4:
            sleep(3)
    return {**result, 'status': 'unconfirmed',
            'reason': 'rerun_accepted_readback_pending' if acknowledged else 'rerun_outcome_unknown'}


def main():
    require(os.environ.get('GITHUB_ACTIONS') == 'true'
            and os.environ.get('GITHUB_EVENT_NAME') == 'workflow_run'
            and os.environ.get('GITHUB_REF') == 'refs/heads/main', 'recovery_requires_main_completion_event')
    event = json.loads(Path(os.environ['GITHUB_EVENT_PATH']).read_text())
    require(isinstance(event.get('workflow_run'), dict), 'completion_event_missing')
    result = recover(GitHub(os.environ['GITHUB_REPOSITORY']), event['workflow_run'])
    print(json.dumps(result, sort_keys=True))
    summary = os.environ.get('GITHUB_STEP_SUMMARY')
    if summary:
        with Path(summary).open('a', encoding='utf-8') as output:
            output.write('Neutral refresh runner recovery: ' + json.dumps(result, sort_keys=True) + '\n')
    return 1 if result['status'] in {'failed', 'unconfirmed'} else 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (RecoveryError, KeyError, OSError, ValueError) as error:
        print(f'Neutral refresh runner recovery could not complete: {type(error).__name__}')
        raise SystemExit(1)
