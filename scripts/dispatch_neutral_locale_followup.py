#!/usr/bin/env python3
"""Queue one locale catch-up after a verified catalog cycle; never replay a POST."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import time
from typing import Any, Callable
from urllib.parse import urlencode

WORKFLOW = 'neutral-edge-cutover.yml'
TITLE = 'Neutral edge migrate (incremental; locales)'
PENDING = {'queued', 'pending', 'requested', 'waiting'}
HEAD_RE = re.compile(r'[0-9a-f]{40}')


class FollowupError(RuntimeError):
    pass


def require(condition: Any, message: str) -> None:
    if not condition:
        raise FollowupError(message)


class GitHub:
    def get(self, path: str) -> dict[str, Any]:
        for attempt in range(3):
            try:
                result = subprocess.run(['gh', 'api', path], capture_output=True, text=True, timeout=30)
                if result.returncode == 0:
                    value = json.loads(result.stdout)
                    require(isinstance(value, dict), 'GitHub response is not an object')
                    return value
                if re.search(r'HTTP (?:401|403|404|422)', result.stderr):
                    raise FollowupError('GitHub read was rejected')
            except (subprocess.TimeoutExpired, json.JSONDecodeError):
                pass
            if attempt < 2:
                time.sleep((1, 3)[attempt])
        raise FollowupError('GitHub read did not complete after bounded retries')

    def dispatch(self, path: str, payload: dict[str, Any]) -> None:
        # A timeout or nonzero exit can occur after GitHub accepted the request.
        # The caller reads back before reporting; this mutation is sent once.
        try:
            result = subprocess.run(['gh', 'api', '--method', 'POST', path, '--input', '-'],
                                    input=json.dumps(payload), capture_output=True, text=True, timeout=30)
        except subprocess.TimeoutExpired as error:
            raise FollowupError('Dispatch outcome is unknown') from error
        require(result.returncode == 0, 'Dispatch did not acknowledge success')


def workflow_runs(api: Any, repository: str, **filters: Any) -> list[dict[str, Any]]:
    rows = []
    for page in range(1, 11):
        query = urlencode({'branch': 'main', 'per_page': 100, 'page': page, **filters})
        response = api.get(f'repos/{repository}/actions/workflows/{WORKFLOW}/runs?{query}')
        batch = response.get('workflow_runs')
        require(isinstance(batch, list) and all(isinstance(row, dict) for row in batch),
                'Workflow inventory is invalid')
        rows.extend(batch)
        if len(batch) < 100:
            return rows
    raise FollowupError('Workflow inventory exceeded the bounded dispatch scan')


def locale_runs(rows: list[dict[str, Any]], repository: str, head: str | None = None) -> list[dict[str, Any]]:
    pattern = re.compile(re.escape(TITLE) + r'(?: \[source [1-9][0-9]*:[1-9][0-9]*\])?')
    return [row for row in rows if type(row.get('id')) is int and row['id'] > 0
            and row.get('event') == 'workflow_dispatch' and row.get('head_branch') == 'main'
            and isinstance(row.get('head_sha'), str) and HEAD_RE.fullmatch(row['head_sha'])
            and (head is None or row['head_sha'] == head)
            and row.get('path') == '.github/workflows/' + WORKFLOW
            and (row.get('head_repository') or {}).get('full_name') == repository
            and isinstance(row.get('display_title'), str) and pattern.fullmatch(row['display_title'])]


def ensure_followup(api: Any, repository: str, source_run_id: int, source_attempt: int,
                    expected_head: str, *, sleep: Callable[[float], None] = time.sleep) -> dict[str, Any]:
    require(re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository), 'Repository is invalid')
    require(type(source_run_id) is int and source_run_id > 0 and type(source_attempt) is int
            and source_attempt > 0 and HEAD_RE.fullmatch(expected_head), 'Source identity is invalid')
    source = api.get(f'repos/{repository}/actions/runs/{source_run_id}')
    require(source.get('id') == source_run_id and source.get('run_attempt') == source_attempt
            and source.get('head_sha') == expected_head and source.get('head_branch') == 'main'
            and source.get('path') == '.github/workflows/' + WORKFLOW
            and (source.get('head_repository') or {}).get('full_name') == repository,
            'Catalog source identity changed')
    created = source.get('created_at')
    require(isinstance(created, str) and re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', created),
            'Catalog creation time is invalid')
    jobs = api.get(f'repos/{repository}/actions/runs/{source_run_id}/attempts/{source_attempt}/jobs?per_page=100')
    rows = jobs.get('jobs')
    require(isinstance(rows, list), 'Catalog job inventory is invalid')
    by_name = {row.get('name'): row for row in rows if isinstance(row, dict)}
    require(by_name.get('prepare_release', {}).get('conclusion') == 'success'
            and by_name.get('cutover', {}).get('conclusion') in {'success', 'skipped'},
            'Catalog validation or acceptance has not completed successfully')
    head = api.get(f'repos/{repository}/git/ref/heads/main').get('object', {}).get('sha')
    require(isinstance(head, str) and HEAD_RE.fullmatch(head), 'Current main identity is invalid')
    source_key = f'{source_run_id}:{source_attempt}'
    expected_title = TITLE + f' [source {source_key}]'
    # The same source may already have dispatched a later main commit, or main
    # may advance between the ref read and POST. Match that intent across heads.
    before = locale_runs(workflow_runs(api, repository, event='workflow_dispatch', created='>=' + created), repository)
    same_source = [row for row in before if row['display_title'] == expected_title]
    if same_source:
        require(len(same_source) == 1, 'Duplicate source follow-ups need inspection')
        row = same_source[0]
        require(row.get('conclusion') in {None, 'success'}, 'Previous source follow-up did not succeed')
        return {'state': 'already_dispatched', 'run_id': row['id'], 'source_run_id': source_run_id}
    pending = [row for row in locale_runs(workflow_runs(api, repository, head_sha=head), repository, head)
               if row.get('status') in PENDING]
    if pending:
        # A queued job has not captured Chinese yet. Under the shared release
        # lock it will read the latest accepted snapshot when it starts.
        row = min(pending, key=lambda value: value['id'])
        return {'state': 'coalesced', 'run_id': row['id'], 'source_run_id': source_run_id}
    previous_ids = {row['id'] for row in before}
    try:
        api.dispatch(f'repos/{repository}/actions/workflows/{WORKFLOW}/dispatches', {
            'ref': 'main', 'inputs': {'operation': 'migrate', 'translation_scope': 'incremental',
                                    'publication_mode': 'locales', 'locale_followup_source': source_key},
        })
    except Exception:
        # Never repeat a potentially accepted POST. Read back the exact intent.
        pass
    for delay in (0, 2, 5, 10):
        if delay:
            sleep(delay)
        matches = [row for row in locale_runs(workflow_runs(api, repository, event='workflow_dispatch',
                                                           created='>=' + created), repository)
                   if row['id'] not in previous_ids and row['display_title'] == expected_title]
        require(len(matches) <= 1, 'Dispatch readback found duplicate source follow-ups')
        if matches:
            return {'state': 'accepted', 'run_id': matches[0]['id'], 'source_run_id': source_run_id}
    raise FollowupError('Dispatch outcome was not confirmed; inspect the queue before retrying')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repository', required=True)
    parser.add_argument('--source-run-id', required=True, type=int)
    parser.add_argument('--source-run-attempt', required=True, type=int)
    parser.add_argument('--expected-head', required=True)
    args = parser.parse_args()
    try:
        result = ensure_followup(GitHub(), args.repository, args.source_run_id,
                                 args.source_run_attempt, args.expected_head)
    except FollowupError as error:
        print(json.dumps({'state': 'unconfirmed', 'error': str(error)}, sort_keys=True))
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
