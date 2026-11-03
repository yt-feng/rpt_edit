#!/usr/bin/env python3
"""Exercise recovery admission, exact-attempt reads, and ambiguous writes offline."""
import copy
import json
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import recover_neutral_runner_loss as recovery


REPOSITORY = 'example/repo'
SHA = 'a' * 40


def fixture():
    run = dict(id=123, run_attempt=1, head_sha=SHA, head_branch='main',
               event='workflow_run', path=recovery.WORKFLOW, workflow_id=456,
               status='completed', conclusion='failure', created_at='2026-11-01T02:25:45Z',
               repository={'full_name': REPOSITORY}, head_repository={'full_name': REPOSITORY})
    job = dict(id=789, run_id=123, head_sha=SHA, name='prepare_release',
               status='completed', conclusion='failure', runner_id=1, runner_name='GitHub Actions',
               check_run_url=f'https://api.github.com/repos/{REPOSITORY}/check-runs/987',
               steps=[dict(number=1, name='Set up job', status='completed', conclusion='success'),
                      dict(number=31, name='Build Korean Japanese and Arabic static locales',
                           status='in_progress', conclusion=None),
                      dict(number=47, name=recovery.UPLOAD_STEP, status='pending', conclusion=None),
                      dict(number=56, name='Upload release validation artifact', status='pending', conclusion=None)])
    skipped = dict(id=790, run_id=123, head_sha=SHA, name='cutover', status='completed',
                   conclusion='skipped', runner_id=0, runner_name='', steps=[])
    return run, [job, skipped]


class FakeGitHub:
    repository = REPOSITORY

    def __init__(self):
        self.run, self.jobs = fixture()
        self.event = copy.deepcopy(self.run)
        self.check = dict(id=987, name='prepare_release', head_sha=SHA, status='completed',
                          conclusion='failure', output={'annotations_count': 1})
        self.annotations = [dict(annotation_level='failure', message=recovery.RUNNER_LOSS + ' Details.')]
        self.recent = []
        self.other_jobs = {}
        self.calls = []
        self.advance = True
        self.post_error = False
        self.before_second_read = None
        self.run_reads = 0

    def api(self, suffix, method='GET'):
        self.calls.append((suffix, method))
        if method == 'POST':
            if self.advance:
                self.run.update(run_attempt=2, status='queued', conclusion=None)
            if self.post_error:
                raise recovery.RecoveryError(self.post_error if isinstance(self.post_error, str) else 'rerun_response_unknown')
            return None
        if suffix == 'actions/runs/123':
            self.run_reads += 1
            if self.run_reads == 2 and self.before_second_read:
                self.before_second_read(self)
            return copy.deepcopy(self.run)
        if suffix == 'actions/runs/123/attempts/1/jobs?per_page=100':
            return dict(total_count=len(self.jobs), jobs=copy.deepcopy(self.jobs))
        if suffix == 'check-runs/987':
            return copy.deepcopy(self.check)
        if suffix == 'check-runs/987/annotations?per_page=100':
            return copy.deepcopy(self.annotations)
        if suffix.startswith('actions/workflows/456/runs?'):
            return dict(total_count=len(self.recent), workflow_runs=copy.deepcopy(self.recent))
        if suffix in self.other_jobs:
            return copy.deepcopy(self.other_jobs[suffix])
        raise AssertionError(suffix)

    @property
    def writes(self):
        return [call for call in self.calls if call[1] != 'GET']

    def execute(self):
        return recovery.recover(self, self.event, sleep=lambda _: None)


class RecoveryTests(unittest.TestCase):
    def test_exact_runner_loss_reruns_once_and_verifies_attempt(self):
        github = FakeGitHub()
        result = github.execute()
        self.assertEqual(result['status'], 'recovered')
        self.assertEqual(result['run_attempt'], 2)
        self.assertEqual(github.writes, [('actions/runs/123/rerun-failed-jobs', 'POST')])
        self.assertEqual(github.calls.count(('actions/runs/123/attempts/1/jobs?per_page=100', 'GET')), 2)

    def test_only_automatic_main_same_repository_first_attempt(self):
        cases = [{'event': 'workflow_dispatch'}, {'event': 'pull_request'}, {'head_branch': 'feature'},
                 {'head_repository': {'full_name': 'fork/repo'}}, {'repository': {'full_name': 'other/repo'}},
                 {'path': '.github/workflows/other.yml'}, {'run_attempt': 2}, {'head_sha': 'bad'}]
        for change in cases:
            with self.subTest(change=change):
                github = FakeGitHub()
                github.event.update(change)
                self.assertEqual(github.execute()['status'], 'skipped')
                self.assertEqual(github.writes, [])

    def test_dropbox_dispatch_retains_one_proven_preupload_runner_loss_retry(self):
        github = FakeGitHub()
        github.event['event'] = github.run['event'] = 'repository_dispatch'
        result = github.execute()
        self.assertEqual(result['run_attempt'], 2)
        self.assertEqual(github.writes, [('actions/runs/123/rerun-failed-jobs', 'POST')])

    def test_stale_event_or_nonfailure_run_never_writes(self):
        for change in [{'run_attempt': 2}, {'head_sha': 'b' * 40}, {'status': 'in_progress'},
                       {'conclusion': 'cancelled'}, {'conclusion': 'timed_out'}, {'conclusion': 'success'}]:
            with self.subTest(change=change):
                github = FakeGitHub()
                github.run.update(change)
                self.assertEqual(github.execute()['status'], 'skipped')
                self.assertEqual(github.writes, [])

    def test_downstream_execution_or_missing_cutover_blocks_retry(self):
        cases = [{'conclusion': 'success'}, {'status': 'in_progress'}, {'runner_id': 1},
                 {'runner_name': 'runner'}, {'steps': [{'status': 'completed', 'conclusion': 'success'}]},
                 {'name': 'other_job'}]
        for change in cases:
            with self.subTest(change=change):
                github = FakeGitHub()
                github.jobs[1].update(change)
                self.assertEqual(github.execute()['status'], 'skipped')
                self.assertEqual(github.writes, [])

    def test_upload_started_and_missing_boundary_block_retry(self):
        for change in [{'status': 'in_progress'}, {'status': 'completed', 'conclusion': 'success'},
                       {'name': 'renamed upload'}, {'number': 20}]:
            with self.subTest(change=change):
                github = FakeGitHub()
                github.jobs[0]['steps'][2].update(change)
                self.assertEqual(github.execute()['status'], 'skipped')
                self.assertEqual(github.writes, [])

    def test_application_failure_and_timeout_do_not_get_retried(self):
        for conclusion in ['failure', 'cancelled', 'timed_out']:
            github = FakeGitHub()
            github.jobs[0]['steps'][0]['conclusion'] = conclusion
            self.assertEqual(github.execute()['reason'], 'application_failure_or_upload_started')
            self.assertEqual(github.writes, [])

    def test_annotation_must_be_exclusively_runner_loss(self):
        for message in ['R2 ServiceUnavailable', 'The operation was canceled.', 'Timeout',
                        'prefix ' + recovery.RUNNER_LOSS]:
            github = FakeGitHub()
            github.annotations[0]['message'] = message
            self.assertEqual(github.execute()['reason'], 'not_exclusively_hosted_runner_loss')
            self.assertEqual(github.writes, [])
        github = FakeGitHub()
        github.annotations.append(dict(annotation_level='failure', message='Application failed'))
        github.check['output']['annotations_count'] = 2
        self.assertEqual(github.execute()['reason'], 'not_exclusively_hosted_runner_loss')
        self.assertEqual(github.writes, [])

    def test_incomplete_or_mismatched_check_evidence_never_retries(self):
        for change in [{'head_sha': 'b' * 40}, {'name': 'cutover'}, {'id': 999},
                       {'output': {'annotations_count': 2}}, {'output': {'annotations_count': 101}}]:
            github = FakeGitHub()
            github.check.update(change)
            self.assertEqual(github.execute()['status'], 'skipped')
            self.assertEqual(github.writes, [])

    def test_newer_active_or_executed_success_supersedes(self):
        for status, conclusion in [('queued', None), ('in_progress', None), ('completed', 'success')]:
            github = FakeGitHub()
            newer = {**github.run, 'id': 124, 'status': status, 'conclusion': conclusion}
            github.recent = [newer]
            jobs = copy.deepcopy(github.jobs)
            for job in jobs:
                job['run_id'] = 124
            jobs[0]['conclusion'] = 'success'
            github.other_jobs['actions/runs/124/attempts/1/jobs?per_page=100'] = dict(total_count=2, jobs=jobs)
            self.assertEqual(github.execute()['reason'], 'newer_refresh_supersedes')
            self.assertEqual(github.writes, [])

    def test_newer_ineligible_all_skipped_green_run_does_not_supersede(self):
        github = FakeGitHub()
        github.recent = [{**github.run, 'id': 124, 'conclusion': 'success'}]
        jobs = copy.deepcopy(github.jobs)
        for job in jobs:
            job.update(run_id=124, conclusion='skipped', runner_id=0, runner_name='', steps=[])
        github.other_jobs['actions/runs/124/attempts/1/jobs?per_page=100'] = dict(total_count=2, jobs=jobs)
        self.assertEqual(github.execute()['status'], 'recovered')

    def test_changed_attempt_or_job_before_post_never_writes(self):
        mutations = [lambda github: github.run.update(run_attempt=2),
                     lambda github: github.jobs[0].update(id=999),
                     lambda github: github.jobs[1].update(runner_id=1)]
        for mutation in mutations:
            github = FakeGitHub()
            github.before_second_read = mutation
            self.assertEqual(github.execute()['status'], 'skipped')
            self.assertEqual(github.writes, [])

    def test_lost_ack_is_reconciled_with_no_second_post(self):
        github = FakeGitHub()
        github.post_error = True
        self.assertEqual(github.execute()['status'], 'recovered')
        self.assertEqual(len(github.writes), 1)

    def test_unknown_or_delayed_rerun_is_never_blindly_replayed(self):
        for lost in [False, True]:
            github = FakeGitHub()
            github.advance, github.post_error = False, lost
            self.assertEqual(github.execute()['status'], 'unconfirmed')
            self.assertEqual(len(github.writes), 1)
            self.assertEqual(github.run_reads, 7)

    def test_definitive_post_permission_denial_is_reported_without_replay(self):
        github = FakeGitHub()
        github.advance, github.post_error = False, 'github_http_403'
        self.assertEqual(github.execute()['reason'], 'github_http_403')
        self.assertEqual(len(github.writes), 1)
        self.assertEqual(github.run_reads, 2)

    def test_get_client_retries_but_post_client_never_retries(self):
        client = recovery.GitHub(REPOSITORY, sleep=lambda _: None)
        with patch.object(recovery.subprocess, 'run', return_value=SimpleNamespace(returncode=1, stdout=b'', stderr=b'private')) as run:
            with self.assertRaisesRegex(recovery.RecoveryError, 'github_read_failed'):
                client.api('actions/runs/123')
            self.assertEqual(run.call_count, 3)
            run.reset_mock()
            with self.assertRaisesRegex(recovery.RecoveryError, 'rerun_response_unknown'):
                client.api('actions/runs/123/rerun-failed-jobs', 'POST')
            self.assertEqual(run.call_count, 1)

    def test_authentication_failure_is_distinct_and_not_retried(self):
        client = recovery.GitHub(REPOSITORY, sleep=lambda _: None)
        with patch.object(recovery.subprocess, 'run', return_value=SimpleNamespace(
                returncode=1, stdout=b'', stderr=b'gh: Forbidden (HTTP 403)')) as run:
            with self.assertRaisesRegex(recovery.RecoveryError, 'github_http_403'):
                client.api('actions/runs/123')
            self.assertEqual(run.call_count, 1)

    def test_workflow_runs_independently_with_scoped_permissions(self):
        root = Path(__file__).resolve().parents[1]
        text = (root / '.github/workflows/neutral-edge-runner-recovery.yml').read_text()
        self.assertIn('workflows: [Neutral edge catalog refresh]', text)
        self.assertIn('actions: write', text)
        self.assertIn('checks: read', text)
        self.assertIn('persist-credentials: false', text)
        self.assertIn('ref: main', text)
        self.assertIn('run_attempt == 1', text)
        self.assertNotIn('secrets.', text)
        self.assertIn('python3 -B scripts/recover_neutral_runner_loss.py', text)


if __name__ == '__main__':
    unittest.main()
