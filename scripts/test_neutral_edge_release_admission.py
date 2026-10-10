"""Replay release admission and failed-review cleanup without network or credentials."""
from contextlib import redirect_stdout
import copy
import io
import os
from pathlib import Path
import re
import textwrap
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import review_portal_extended_handoff as reviewer
from portal_extended_locales import ExpansionError


WORKFLOW = Path(__file__).resolve().parents[1] / '.github/workflows/neutral-edge-cutover.yml'
SOURCE = WORKFLOW.read_text()


def job_block(name):
    return re.split(r'\n  [a-z_]+:\n', SOURCE.split('\n  ' + name + ':\n', 1)[1], maxsplit=1)[0]


def expression(source):
    return source.split('${{', 1)[1].split('}}', 1)[0]


def namespace(value):
    return SimpleNamespace(**{key: namespace(item) if isinstance(item, dict) else item
                              for key, item in value.items()})


def evaluate(source, context):
    # Only execute checked-in boolean/string GitHub expressions, not user data.
    code = ' '.join(expression(source).split()).replace('&&', ' and ').replace('||', ' or ')
    return eval(code, {'__builtins__': {}, 'always': lambda: True, 'failure': lambda: True,
                       'format': lambda template, *args: template.format(*args)},
                {key: namespace(value) if isinstance(value, dict) else value for key, value in context.items()})


class ReleaseAdmissionTests(unittest.TestCase):
    def setUp(self):
        self.context = {
            'github': {'event_name': 'workflow_run', 'repository': 'example/repo', 'run_id': 123,
                       'run_attempt': 1, 'event': {'repository': {'default_branch': 'main'},
                           'workflow_run': {'conclusion': 'success', 'head_branch': 'main',
                                            'head_repository': {'full_name': 'example/repo'}}}},
            'vars': {'NEUTRAL_SCHEDULE_ENABLED': 'true', 'PORTAL_MULTILINGUAL_ENABLED': 'true',
                     'PORTAL_MULTILINGUAL_LIVE': 'true'},
        }

    def group(self):
        return evaluate(SOURCE.split('\nconcurrency:\n', 1)[1].split('\njobs:', 1)[0], self.context)

    def test_ineligible_event_cannot_replace_pending_production_release(self):
        for event in ('workflow_run', 'schedule', 'workflow_dispatch'):
            for enabled in ('true', 'false'):
                for multilingual in ('true', 'false'):
                    for live in ('true', 'false'):
                        for conclusion in ('success', 'failure', 'cancelled', 'skipped'):
                            with self.subTest(event=event, enabled=enabled, multilingual=multilingual,
                                              live=live, conclusion=conclusion):
                                self.context['github']['event_name'] = event
                                self.context['github']['event']['workflow_run']['conclusion'] = conclusion
                                self.context['vars'].update(NEUTRAL_SCHEDULE_ENABLED=enabled,
                                    PORTAL_MULTILINGUAL_ENABLED=multilingual, PORTAL_MULTILINGUAL_LIVE=live)
                                admitted = bool(evaluate(job_block('prepare_release'), self.context))
                                expected = event == 'workflow_dispatch' or (enabled == 'true' and
                                    (multilingual != 'true' or live == 'true') and
                                    (event == 'schedule' or conclusion == 'success'))
                                self.assertEqual(admitted, expected)
                                self.assertEqual(self.group(), 'portal-production-release' if expected
                                                 else 'portal-release-ineligible-123-1')

    def test_foreign_and_nondefault_branch_completions_are_isolated(self):
        upstream = self.context['github']['event']['workflow_run']
        for change in ({'head_branch': 'feature'}, {'head_repository': {'full_name': 'fork/repo'}}):
            with self.subTest(change=change):
                original = copy.deepcopy(upstream)
                upstream.update(change)
                self.assertFalse(evaluate(job_block('prepare_release'), self.context))
                self.assertEqual(self.group(), 'portal-release-ineligible-123-1')
                upstream.clear(); upstream.update(original)
        upstream['conclusion'] = 'failure'
        self.context['github']['run_id'] = 124
        self.context['github']['run_attempt'] = 2
        self.assertEqual(self.group(), 'portal-release-ineligible-124-2')
        self.assertIn('cancel-in-progress: false', SOURCE)

    def test_manual_approval_handshake_stays_parallel_and_cutover_waits_for_review(self):
        for review, approval in (('english_daily_review', 'english_approval'),
                                 ('extended_daily_review', 'extended_locales_approval')):
            self.assertIn('needs: prepare_release', job_block(approval))
            self.assertNotIn(review, job_block(approval).split('runs-on:', 1)[0])
            self.assertIn('name: portal-extended-locales-production', job_block(approval))
            self.assertIn(review, job_block('cutover').split('if:', 1)[0])
        self.assertIn('Approve exact same-run English tree and private ledger', job_block('english_approval'))
        self.assertIn('Extended locale approval identity mismatch', job_block('extended_locales_approval'))
        outputs = {'multilingual_enabled': 'true', 'multilingual_live': 'true', 'locale_ready': 'true',
                   'changed': 'true', 'operation': 'migrate', 'english_requested': 'true',
                   'extended_requested': 'true'}
        for extended in ('success', 'skipped', 'failure', 'cancelled'):
            for english in ('success', 'skipped', 'failure', 'cancelled'):
                with self.subTest(extended=extended, english=english):
                    context = {'needs': {'prepare_release': {'result': 'success', 'outputs': outputs},
                        'extended_daily_review': {'result': extended}, 'english_daily_review': {'result': english},
                        'multilingual_approval': {'result': 'success'},
                        'extended_locales_approval': {'result': 'success'}, 'english_approval': {'result': 'success'}}}
                    self.assertEqual(bool(evaluate(job_block('cutover'), context)),
                                     extended in ('success', 'skipped') and english in ('success', 'skipped'))
                    self.assertEqual(bool(evaluate(job_block('reject_failed_daily_review'), context)),
                                     extended in ('failure', 'cancelled') or english in ('failure', 'cancelled'))
                    context['needs']['prepare_release']['result'] = 'failure'
                    self.assertFalse(evaluate(job_block('reject_failed_daily_review'), context))


class FailedReviewCleanupTests(unittest.TestCase):
    def setUp(self):
        self.env = {'GITHUB_ACTIONS': 'true', 'GITHUB_REF': 'refs/heads/main',
                    'GITHUB_EVENT_NAME': 'workflow_dispatch', 'GITHUB_REPOSITORY': 'example/repo',
                    'GITHUB_RUN_ID': '123', 'GITHUB_RUN_ATTEMPT': '2', 'GITHUB_SHA': 'a'*40,
                    'EXTENDED_REVIEW_RESULT': 'skipped', 'ENGLISH_REVIEW_RESULT': 'failure'}
        self.environment = {'id': 9, 'name': reviewer.ENVIRONMENT,
                            'protection_rules': [{'type': 'required_reviewers', 'reviewers': [{'id': 1}]}]}
        self.run = {'id': 123, 'run_attempt': 2, 'head_sha': 'a'*40, 'head_branch': 'main',
                    'event': 'workflow_dispatch', 'path': '.github/workflows/neutral-edge-cutover.yml',
                    'repository': {'full_name': 'example/repo'}, 'head_repository': {'full_name': 'example/repo'}}
        self.jobs = {'total_count': 3, 'jobs': [
            {'name': 'english_daily_review', 'run_id': 123, 'head_sha': 'a'*40,
             'status': 'completed', 'conclusion': 'failure'},
            {'name': 'english_approval', 'run_id': 123, 'head_sha': 'a'*40,
             'status': 'waiting', 'conclusion': None},
            {'name': 'cutover', 'run_id': 123, 'head_sha': 'a'*40, 'status': 'queued', 'conclusion': None}]}
        self.pending = [{'environment': {'id': 9, 'name': reviewer.ENVIRONMENT}, 'current_user_can_approve': True}]
        self.calls = []
        self.lose_ack = False
        self.reject_transport_failure = False
        self.delayed_pending = 0
        source = job_block('reject_failed_daily_review').split("python3 -B - <<'PY'\n", 1)[1].split('\n          PY', 1)[0]
        self.code = compile(textwrap.dedent(source), str(WORKFLOW), 'exec')

    def api(self, path, payload=None, method=None):
        self.calls.append((path, copy.deepcopy(payload), method))
        base = 'repos/example/repo/actions/runs/123'
        if path == 'repos/example/repo/environments/' + reviewer.ENVIRONMENT:
            return copy.deepcopy(self.environment)
        if path == base:
            return copy.deepcopy(self.run)
        if path == base + '/attempts/2/jobs?per_page=100':
            return copy.deepcopy(self.jobs)
        if path == base + '/pending_deployments':
            if method == 'POST':
                if self.reject_transport_failure:
                    raise reviewer.ReviewAPIError(transient=False)
                self.assertEqual(payload['state'], 'rejected')
                self.assertEqual(payload['environment_ids'], [9])
                self.pending = []
                self.jobs['jobs'][1].update(status='completed', conclusion='failure')
                if self.lose_ack:
                    raise reviewer.ReviewAPIError(transient=True)
                return [{'state': 'failure'}]
            if self.delayed_pending:
                self.delayed_pending -= 1
                return []
            return copy.deepcopy(self.pending)
        raise AssertionError('Unexpected API call: ' + path)

    def execute(self):
        with patch.dict(os.environ, self.env, clear=True), patch.object(reviewer, 'api', self.api), \
                patch('time.sleep'), redirect_stdout(io.StringIO()):
            exec(self.code, {'__name__': '__main__'})

    def writes(self):
        return [call for call in self.calls if call[2] == 'POST']

    def test_real_failed_review_releases_only_its_exact_pending_environment(self):
        self.execute()
        self.assertEqual(len(self.writes()), 1)
        self.assertEqual(self.jobs['jobs'][1]['conclusion'], 'failure')
        self.assertIn('attempt 2 at ' + 'a'*40, self.writes()[0][1]['comment'])

    def test_lost_rejection_ack_is_reconciled_without_second_write(self):
        self.lose_ack = True
        self.execute()
        self.assertEqual(len(self.writes()), 1)

    def test_delayed_pending_environment_is_bounded_and_then_rejected(self):
        self.delayed_pending = 2
        self.execute()
        self.assertEqual(len(self.writes()), 1)
        self.assertGreaterEqual(sum(call[0].endswith('/pending_deployments') for call in self.calls), 4)

    def test_already_cancelled_approval_needs_no_write(self):
        self.pending = []
        self.jobs['jobs'][1].update(status='completed', conclusion='cancelled')
        self.execute()
        self.assertEqual(self.writes(), [])

    def test_legitimate_manual_skipped_review_is_never_rejected(self):
        for result in ('success', 'skipped'):
            with self.subTest(result=result):
                self.env['ENGLISH_REVIEW_RESULT'] = result
                with self.assertRaises(ExpansionError):
                    self.execute()
                self.assertEqual(self.writes(), [])

    def test_changed_run_attempt_sha_or_fork_cannot_be_rejected(self):
        original = copy.deepcopy(self.run)
        for change in ({'run_attempt': 3}, {'head_sha': 'b'*40}, {'head_branch': 'feature'},
                       {'head_repository': {'full_name': 'fork/repo'}}, {'event': 'schedule'}):
            with self.subTest(change=change):
                self.run = {**original, **change}
                with self.assertRaises(ExpansionError):
                    self.execute()
                self.assertEqual(self.writes(), [])

    def test_changed_review_job_or_started_approval_cannot_be_rejected(self):
        original = copy.deepcopy(self.jobs)
        for index, change in ((0, {'conclusion': 'success'}), (0, {'head_sha': 'b'*40}),
                              (0, {'run_id': 124}), (1, {'status': 'in_progress'}),
                              (1, {'status': 'completed', 'conclusion': 'success'})):
            with self.subTest(index=index, change=change):
                self.jobs = copy.deepcopy(original)
                self.jobs['jobs'][index].update(change)
                with self.assertRaises(ExpansionError):
                    self.execute()
                self.assertEqual(self.writes(), [])

    def test_environment_protections_and_reviewer_identity_remain_required(self):
        self.environment['protection_rules'] = []
        with self.assertRaises(ExpansionError):
            self.execute()
        self.assertEqual(self.writes(), [])
        self.environment['protection_rules'] = [{'type': 'required_reviewers', 'reviewers': [{'id': 1}]}]
        self.pending[0]['current_user_can_approve'] = False
        with self.assertRaises(ExpansionError):
            self.execute()
        self.assertEqual(self.writes(), [])

    def test_extended_review_uses_the_same_cleanup_without_manual_bypass(self):
        self.env.update(EXTENDED_REVIEW_RESULT='failure', ENGLISH_REVIEW_RESULT='skipped')
        self.jobs['jobs'][0]['name'] = 'extended_daily_review'
        self.jobs['jobs'][1]['name'] = 'extended_locales_approval'
        self.execute()
        self.assertEqual(len(self.writes()), 1)

    def test_timed_out_and_cancelled_review_results_release_the_wait(self):
        for result, conclusion in (('failure', 'timed_out'), ('cancelled', 'cancelled')):
            with self.subTest(result=result, conclusion=conclusion):
                self.setUp()
                self.env['ENGLISH_REVIEW_RESULT'] = result
                self.jobs['jobs'][0]['conclusion'] = conclusion
                self.execute()
                self.assertEqual(len(self.writes()), 1)

    def test_never_pending_and_nontransient_failure_are_reported(self):
        self.delayed_pending = 99
        with self.assertRaises(SystemExit):
            self.execute()
        self.assertEqual(self.writes(), [])
        self.delayed_pending = 0
        self.reject_transport_failure = True
        with self.assertRaises(reviewer.ReviewAPIError):
            self.execute()
        self.assertEqual(len(self.writes()), 1)


class FailedReviewCancellationTests(unittest.TestCase):
    def setUp(self):
        self.fixture = FailedReviewCleanupTests()
        self.fixture.setUp()
        self.fixture.env['GH_TOKEN'] = 'builtin-test-token'
        self.fixture.run.update(status='in_progress', conclusion=None)
        step = job_block('reject_failed_daily_review').split(
            '      - name: Cancel this failed release if delegated rejection is unavailable\n', 1)[1]
        self.condition = '${{ ' + step.split('        if: ', 1)[1].split('\n', 1)[0] + ' }}'
        source = step.split("python3 -B - <<'PY'\n", 1)[1].split('\n          PY', 1)[0]
        self.code = compile(textwrap.dedent(source), str(WORKFLOW), 'exec')
        self.calls = []

    def cli(self, command, **kwargs):
        self.assertEqual(command[:2], ['gh', 'api'])
        self.assertEqual(command[3], '--method')
        self.assertEqual(os.environ['GH_TOKEN'], 'builtin-test-token')
        self.assertEqual(kwargs['timeout'], 45)
        path, method = command[2], command[4]
        self.calls.append((path, method))
        base = 'repos/example/repo/actions/runs/123'
        if path == base and method == 'GET':
            result = self.fixture.run
        elif path == base + '/attempts/2/jobs?per_page=100' and method == 'GET':
            result = self.fixture.jobs
        elif path == base + '/cancel' and method == 'POST':
            return SimpleNamespace(returncode=0, stdout=b'', stderr=b'')
        else:
            raise AssertionError('Unexpected cancellation request: ' + path)
        import json
        return SimpleNamespace(returncode=0, stdout=json.dumps(result).encode(), stderr=b'')

    def execute(self):
        with patch.dict(os.environ, self.fixture.env, clear=True), patch('subprocess.run', self.cli), \
                redirect_stdout(io.StringIO()):
            exec(self.code, {'__name__': '__main__'})

    def writes(self):
        return [call for call in self.calls if call[1] == 'POST']

    def test_missing_or_forbidden_reviewer_token_still_cancels_only_current_run(self):
        for status in (None, 403):
            with self.subTest(status=status):
                self.setUp()
                self.fixture.env['GH_TOKEN'] = '' if status is None else 'expired-reviewer-test-token'
                with patch.object(self.fixture, 'api', side_effect=reviewer.ReviewAPIError(status)), \
                        self.assertRaises(reviewer.ReviewAPIError):
                    self.fixture.execute()
                self.assertEqual(self.fixture.writes(), [])
                self.fixture.env['GH_TOKEN'] = 'builtin-test-token'
                self.execute()
                self.assertEqual(self.writes(), [('repos/example/repo/actions/runs/123/cancel', 'POST')])

    def test_fallback_only_runs_after_failed_rejection_and_uses_independent_token(self):
        block = job_block('reject_failed_daily_review')
        self.assertIn('actions: write', block.split('steps:', 1)[0])
        fallback = block.split('Cancel this failed release if delegated rejection is unavailable', 1)[1]
        self.assertIn('GH_TOKEN: ${{ github.token }}', fallback)
        self.assertNotIn('GH_DISPATCH_TOKEN', fallback)
        self.assertIn('id: reject_review\n        if: always()\n        timeout-minutes: 5', block)
        self.assertIn('timeout-minutes: 3', fallback)
        for outcome in ('failure', 'success', 'skipped', 'cancelled'):
            self.assertEqual(bool(evaluate(self.condition, {'steps': {'reject_review': {'outcome': outcome}}})),
                             outcome == 'failure')

    def test_successful_or_manual_skipped_review_never_cancels(self):
        for result in ('success', 'skipped'):
            with self.subTest(result=result):
                self.fixture.env['ENGLISH_REVIEW_RESULT'] = result
                with self.assertRaises(SystemExit):
                    self.execute()
                self.assertEqual(self.writes(), [])

    def test_different_run_attempt_commit_or_repository_never_cancels(self):
        original = copy.deepcopy(self.fixture.run)
        for change in ({'id': 124}, {'run_attempt': 3}, {'head_sha': 'b'*40},
                       {'repository': {'full_name': 'other/repo'}}, {'head_branch': 'feature'},
                       {'path': '.github/workflows/another.yml'}):
            with self.subTest(change=change):
                self.fixture.run = {**original, **change}
                with self.assertRaises(SystemExit):
                    self.execute()
                self.assertEqual(self.writes(), [])

    def test_started_cutover_or_incomplete_job_inventory_never_cancels(self):
        original = copy.deepcopy(self.fixture.jobs)
        for change in ({'status': 'in_progress'}, {'status': 'completed', 'conclusion': 'success'},
                       {'status': 'queued', 'steps': [{'status': 'completed', 'conclusion': 'success'}]},
                       {'run_id': 124}, {'head_sha': 'b'*40}):
            with self.subTest(change=change):
                self.fixture.jobs = copy.deepcopy(original)
                self.fixture.jobs['jobs'][2].update(change)
                with self.assertRaises(SystemExit):
                    self.execute()
                self.assertEqual(self.writes(), [])
        self.fixture.jobs = copy.deepcopy(original)
        self.fixture.jobs['total_count'] = 101
        with self.assertRaises(SystemExit):
            self.execute()
        self.assertEqual(self.writes(), [])

    def test_review_failure_must_be_verified_in_current_attempt(self):
        self.fixture.jobs['jobs'][0]['conclusion'] = 'success'
        with self.assertRaises(SystemExit):
            self.execute()
        self.assertEqual(self.writes(), [])

    def test_finished_failure_does_not_need_another_cancellation(self):
        self.fixture.run.update(status='completed', conclusion='failure')
        self.fixture.jobs['jobs'][2].update(status='completed', conclusion='skipped')
        self.execute()
        self.assertEqual(self.writes(), [])


if __name__ == '__main__':
    unittest.main()
