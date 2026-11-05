"""Read complete GitHub attempt history before replaying any WeChat submission."""
from __future__ import annotations

import json
import os
import re
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class HistoryError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise HistoryError(message)


class GitHubHistory:
    def __init__(self, repository, run_id, token, *, request=None, sleep=None):
        require(isinstance(repository, str) and re.fullmatch(
            r'[A-Za-z0-9][A-Za-z0-9_.-]*/[A-Za-z0-9][A-Za-z0-9_.-]*', repository),
            'Invalid repository or source run ID')
        require(re.fullmatch(r'[1-9][0-9]*', str(run_id)), 'Invalid repository or source run ID')
        require(token, 'GH_TOKEN is required for source-run verification')
        self.base = f'https://api.github.com/repos/{repository}/actions/runs/{run_id}'
        self.token, self.request, self.sleep = token, request or urlopen, sleep or time.sleep

    def get(self, suffix=''):
        request = Request(self.base + suffix, headers={
            'Authorization': f'Bearer {self.token}', 'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28'})
        for attempt in range(3):
            try:
                with self.request(request, timeout=30) as response:
                    result = json.load(response)
                require(isinstance(result, dict), 'GitHub source-run verification returned an unexpected response')
                return result
            except HTTPError as error:
                status = error.code
                error.close()
                if status not in {408, 429, 500, 502, 503, 504} or attempt == 2:
                    raise HistoryError(f'GitHub source-run verification failed: HTTP {status}') from None
            except (URLError, TimeoutError):
                if attempt == 2:
                    raise HistoryError('GitHub source-run verification could not connect within the request timeout') from None
            except (json.JSONDecodeError, UnicodeError):
                if attempt == 2:
                    raise HistoryError('GitHub source-run verification returned invalid JSON') from None
            self.sleep((1, 3)[attempt])

    def pages(self, suffix, key):
        records, expected, identities = [], None, set()
        for page in range(1, 51):
            value = self.get(f'{suffix}?per_page=100&page={page}')
            total, rows = value.get('total_count'), value.get(key)
            require(type(total) is int and 0 <= total <= 5000 and isinstance(rows, list)
                    and len(rows) <= 100 and all(isinstance(row, dict) for row in rows),
                    'GitHub attempt history is incomplete or malformed')
            require(expected is None or total == expected, 'GitHub attempt history changed during pagination')
            expected = total
            for row in rows:
                identifier = row.get('id')
                require(type(identifier) is int and identifier not in identities,
                        'GitHub attempt history contains missing or duplicate identities')
                identities.add(identifier)
            records.extend(rows)
            require(len(records) <= total, 'GitHub attempt history count is inconsistent')
            if len(records) == total:
                return records
            require(rows, 'GitHub attempt history ended before all records were read')
        raise HistoryError('GitHub attempt history exceeds the bounded page limit')

    def jobs(self, attempt):
        require(type(attempt) is int and 1 <= attempt <= 100, 'Invalid source attempt number')
        return self.pages(f'/attempts/{attempt}/jobs', 'jobs')

    def artifacts(self):
        return self.pages('/artifacts', 'artifacts')


def never_submitted(jobs, job_name, submission_steps):
    """Absence is proof only after the caller fetched every page for this attempt."""
    require(isinstance(jobs, list) and all(isinstance(job, dict) for job in jobs),
            'GitHub attempt jobs are incomplete')
    require(isinstance(job_name, str) and job_name.strip() and isinstance(submission_steps, list)
            and submission_steps and len(set(submission_steps)) == len(submission_steps)
            and all(isinstance(step, str) and step.strip() for step in submission_steps),
            'Exact uploader job and submission step names are required')
    matches = [job for job in jobs if job.get('name') == job_name]
    require(len(matches) <= 1, 'Uploader job identity is ambiguous')
    if not matches:
        return True  # This job was not rerun in this complete attempt snapshot.
    job = matches[0]
    require(job.get('status') == 'completed', 'Prior uploader job outcome is unresolved')
    if job.get('conclusion') == 'skipped':
        return True
    steps = job.get('steps')
    require(isinstance(steps, list), 'Prior uploader submission steps are unavailable')
    for name in submission_steps:
        matches = [step for step in steps if isinstance(step, dict) and step.get('name') == name]
        require(len(matches) == 1 and matches[0].get('status') == 'completed'
                and matches[0].get('conclusion') == 'skipped',
                'Prior submission may have started; restore its checkpoint or verify existing drafts before retrying')
    return True


def choose_checkpoint(artifacts, current_attempt, base, jobs_for_attempt, job_name, submission_steps):
    require(type(current_attempt) is int and 1 <= current_attempt <= 100, 'Invalid restoration attempt; stop before uploading')
    require(isinstance(artifacts, list), 'Artifact inventory is incomplete')
    pattern = re.compile(re.escape(base) + r'-attempt-([1-9][0-9]*)(-retry)?$')
    candidates = {}
    for artifact in artifacts:
        require(isinstance(artifact, dict), 'Artifact inventory is malformed')
        name = artifact.get('name', '')
        if not isinstance(name, str):
            continue
        match = pattern.fullmatch(name)
        if match:
            attempt = int(match[1])
            if attempt < current_attempt:
                candidates.setdefault(attempt, []).append(artifact)
        elif name == base:
            candidates.setdefault(1, []).append(artifact)
    checked = []
    for attempt in range(current_attempt - 1, 0, -1):
        rows = candidates.get(attempt, [])
        if rows:
            names = [row['name'] for row in rows]
            require(len(names) == len(set(names)), 'Prior draft checkpoint name is ambiguous; stop before uploading')
            live = [row for row in rows if row.get('expired') is False]
            require(live, 'Prior draft receipt expired or unavailable; verify existing drafts before retrying')
            # Both uploads carry the same finished local checkpoint snapshot.
            # A retry has its own immutable name and never deletes the first copy.
            live.sort(key=lambda row: (row['name'] == base, row['name'].endswith('-retry')))
            return {'found': 'true', 'artifact_name': live[0]['name'],
                    'no_prior_submission': 'false', 'checked_attempts': json.dumps(checked)}
        never_submitted(jobs_for_attempt(attempt), job_name, submission_steps)
        checked.append(attempt)
    return {'found': 'false', 'no_prior_submission': 'true', 'checked_attempts': json.dumps(checked)}


def locate_from_environment():
    current = os.environ.get('CURRENT_RUN_ATTEMPT', '')
    require(re.fullmatch(r'[1-9][0-9]*', current), 'Invalid restoration attempt; stop before uploading')
    reader = GitHubHistory(os.environ['GITHUB_REPOSITORY'], os.environ['GITHUB_RUN_ID'], os.environ.get('GH_TOKEN', ''))
    result = choose_checkpoint(reader.artifacts(), int(current), os.environ['RECEIPT_ARTIFACT_NAME'],
        reader.jobs, os.environ['UPLOADER_JOB_NAME'],
        [line.strip() for line in os.environ.get('SUBMISSION_STEP_NAMES', '').splitlines() if line.strip()])
    with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as output:
        for key, value in result.items():
            output.write(f'{key}={value}\n')
    print('Restored checkpoint located.' if result['found'] == 'true'
          else 'Complete prior attempt history confirms no WeChat submission started.')


if __name__ == '__main__':
    locate_from_environment()
