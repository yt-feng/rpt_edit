"""Coalesce pending ordinary locale scans without suppressing exact recoveries."""
from __future__ import annotations

import hashlib
import json
import os
import re
import time
from datetime import datetime, timedelta, timezone
from urllib.parse import quote
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


WORKFLOW = '.github/workflows/portal-extended-locales-r2.yml'
GROUP = 'extended-locales-r2-pipeline'
MAX_BYTES = 2 * 1024 * 1024


class WakeupError(RuntimeError):
    pass


class DispatchRejected(WakeupError):
    pass


def ordinary_request(locales):
    # Preserve locale ordering: it is part of source-selection fairness.
    if (not isinstance(locales, str) or not locales or len(locales) > 200
            or (locales != 'all-supported' and (
                any(not re.fullmatch(r'[a-z]{2,3}(?:-[A-Za-z]{4}|-[A-Z]{2})?', code)
                    for code in locales.split(','))
                or len(set(locales.split(','))) != len(locales.split(','))))):
        raise WakeupError('Ordinary locale request is malformed')
    values = {'operation':'candidate', 'locales':locales, 'source_generation':'',
        'continuation_evidence':'', 'seconds':'14400', 'allow_source_fallback':'true',
        'diagnose_runtime':'false'}
    raw = json.dumps(values, sort_keys=True, separators=(',', ':')).encode()
    identity = hashlib.sha256(raw).hexdigest()
    return {**values, 'ordinary_request_sha256':identity}, f'Extended locale R2 ordinary {identity} ({locales})'


class GitHub:
    def __init__(self, repository, token, *, request=None, sleep=None):
        if (not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*/[A-Za-z0-9][A-Za-z0-9_.-]*', repository)
                or not token):
            raise WakeupError('Repository and GitHub token are required')
        self.repository, self.token = repository, token
        self.request, self.sleep = request or urlopen, sleep or time.sleep
        self.started, self.reads = time.monotonic(), 0

    def api(self, path, payload=None):
        request = Request(f'https://api.github.com/repos/{self.repository}/' + path,
            data=None if payload is None else json.dumps(payload).encode(),
            headers={'Authorization':f'Bearer {self.token}', 'Accept':'application/vnd.github+json',
                     'X-GitHub-Api-Version':'2022-11-28', 'Content-Type':'application/json'},
            method='GET' if payload is None else 'POST')
        attempts = 3 if payload is None else 1  # A dispatch POST is never blindly repeated.
        for attempt in range(attempts):
            if self.reads >= 12 or time.monotonic() - self.started >= 120:
                raise WakeupError('GitHub ordinary wake-up inspection budget exhausted')
            self.reads += 1
            try:
                with self.request(request, timeout=20) as response:
                    raw = response.read(MAX_BYTES + 1)
                if len(raw) > MAX_BYTES:
                    raise WakeupError('GitHub queue response exceeds its byte bound')
                value = json.loads(raw) if raw else {}
                if not isinstance(value, dict):
                    raise WakeupError('GitHub queue response is malformed')
                return value
            except HTTPError as error:
                status = error.code
                error.close()
                if payload is None and status == 404 and path == 'actions/concurrency_groups/' + GROUP:
                    return {'group_name':GROUP, 'total_count':0, 'group_members':[]}
                if payload is not None and 400 <= status < 500:
                    raise DispatchRejected('GitHub ordinary dispatch was rejected: HTTP ' + str(status)) from None
                if status not in {408, 429, 500, 502, 503, 504} or attempt == attempts - 1:
                    raise WakeupError('GitHub queue request failed: HTTP ' + str(status)) from None
            except (URLError, TimeoutError, json.JSONDecodeError, UnicodeError):
                if attempt == attempts - 1:
                    raise WakeupError('GitHub queue request outcome is unavailable') from None
            self.sleep((1, 3)[attempt])


def group_members(api):
    value = api('actions/concurrency_groups/' + GROUP)
    rows, total = value.get('group_members'), value.get('total_count')
    if (value.get('group_name') != GROUP or not isinstance(rows, list)
            or type(total) is not int or total != len(rows) or not 0 <= total <= 101
            or any(not isinstance(row, dict) or type(row.get('run_id')) is not int
                   or row['run_id'] <= 0 for row in rows)
            or len({row['run_id'] for row in rows}) != total):
        raise WakeupError('GitHub ordinary queue inventory is incomplete')
    return rows


def compatible_run(api, repository, rows, title, *, accepted=False, exclude=()):
    states = {'pending', 'in_progress', 'queued', 'completed'} if accepted else {'pending'}
    checked = 0
    for row in rows:
        if (row['run_id'] in exclude or row.get('job_id') is not None
                or row.get('run_name') != title or row.get('status') not in states):
            continue
        checked += 1
        if checked > 3:
            raise WakeupError('Pending ordinary queue changed during bounded inspection')
        run = api('actions/runs/' + str(row['run_id']))
        if (run.get('id') != row['run_id'] or run.get('path') != WORKFLOW
                or run.get('display_title') != title or run.get('event') != 'workflow_dispatch'
                or run.get('head_branch') != 'main'
                or (run.get('head_repository') or {}).get('full_name') != repository):
            raise WakeupError('Pending ordinary request identity could not be verified')
        if run.get('status') in states:
            return row['run_id']
    return None


def recent_runs(api, since):
    path = ('actions/workflows/portal-extended-locales-r2.yml/runs?event=workflow_dispatch'
            '&branch=main&per_page=30&created=' + quote('>=' + since, safe=''))
    value = api(path)
    rows, total = value.get('workflow_runs'), value.get('total_count')
    if (not isinstance(rows, list) or type(total) is not int or total != len(rows)
            or not 0 <= total <= 30 or any(not isinstance(row, dict)
                or type(row.get('id')) is not int or row['id'] <= 0
                or not isinstance(row.get('created_at'), str) or row['created_at'] < since for row in rows)
            or len({row['id'] for row in rows}) != total):
        raise WakeupError('GitHub recent ordinary request inventory is incomplete')
    return [{'run_id':row['id'], 'run_name':row.get('display_title'), 'status':row.get('status')} for row in rows]


def wake(api, repository, locales):
    values, title = ordinary_request(locales)
    before = group_members(api)
    existing = compatible_run(api, repository, before, title)
    if existing is not None:
        return {'dispatched':False, 'reused_pending_run_id':existing,
                'ordinary_request_sha256':values['ordinary_request_sha256']}
    # Snapshot the short acceptance window so an older completed same-request
    # child cannot be confused with a newly accepted POST after an outage.
    since = (datetime.now(timezone.utc) - timedelta(minutes=2)).strftime('%Y-%m-%dT%H:%M:%SZ')
    previous = {row['run_id'] for row in before} | {row['run_id'] for row in recent_runs(api, since)}
    try:
        api('actions/workflows/portal-extended-locales-r2.yml/dispatches', {'ref':'main', 'inputs':values})
    except DispatchRejected:
        raise
    except WakeupError:
        # Inspect an ambiguous acceptance once, preserving the exact request.
        # Absence is not proof of rejection; never issue another POST here.
        try:
            after = group_members(api)
        except WakeupError:
            after = []  # An independent workflow-run read can still prove acceptance.
        accepted = compatible_run(api, repository, after, title, accepted=True,
                                  exclude=previous)
        if accepted is None:
            accepted = compatible_run(api, repository, recent_runs(api, since), title,
                                      accepted=True, exclude=previous)
        if accepted is None:
            raise WakeupError('Ordinary dispatch acceptance is unresolved; no duplicate POST was sent') from None
        return {'dispatched':True, 'accepted_run_id':accepted,
                'ordinary_request_sha256':values['ordinary_request_sha256']}
    return {'dispatched':True, 'ordinary_request_sha256':values['ordinary_request_sha256']}


def main():
    if (os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REF') != 'refs/heads/main'
            or os.environ.get('KC_PUBLIC_REPOSITORY') != 'true'):
        raise WakeupError('Ordinary wake-up requires public main Actions')
    repository = os.environ['GITHUB_REPOSITORY']
    reader = GitHub(repository, os.environ.get('GH_TOKEN', ''))
    print(json.dumps(wake(reader.api, repository, os.environ.get('SOURCE_LOCALES') or 'all-supported'), sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
