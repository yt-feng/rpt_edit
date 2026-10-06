"""Credential-free delegated approval boundary tests; never submit real reviews."""
import copy
from contextlib import chdir
import json
import os
from pathlib import Path
import tempfile
import subprocess
import unittest
from unittest.mock import MagicMock, patch

from offline_translation import MODEL_ID, PROVIDER
from portal_extended_locales import ExpansionError
from review_portal_extended_handoff import producer_is_valid, review_identity
import review_portal_extended_handoff as reviewer
from portal_extended_locales import make_corpus
from portal_extended_r2 import R2Store
from test_portal_extended_incremental import daily_doc
from test_portal_extended_r2 import FakeR2


class DailyReviewTests(unittest.TestCase):
    def setUp(self):
        self.active = [{'generation': 'a'*64, 'candidates': {'fr':'b'*64, 'pt':'c'*64}}]
        self.batch = {'generation':'d'*64, 'candidates':{'fr':'e'*64}}
        self.receipt = {'producer':{'run_id':'123', 'attempt':'1', 'sha':'f'*40},
                        'batch':self.batch, 'source_day':'2026-09-25', 'pages_per_locale':1}
        self.assembly = {'schema_version':2, 'status':'assembled', 'detail_only':True,
                         'locale_homepages':True,
                         'batches':self.active+[self.batch], 'locales':['fr','pt'],
                         'page_counts':{'fr':2, 'pt':1}, 'paid_provider_requests':0}
        ids = {'fr':'e'*64, 'pt':'c'*64}
        self.expected = {'commit_sha':'1'*40, 'static_tree_sha256':'2'*64, 'locales':'fr,pt',
                         'candidate_ids':ids, 'pages_per_locale':'1',
                         'candidate_specs':','.join(k+'='+v for k,v in ids.items())}
        self.identity = {'schema_version':1, 'operation':'migrate', 'commit_sha':'1'*40,
                         'static_tree_sha256':'2'*64, 'source_generation':'d'*64,
                         'locales':['fr','pt'], 'candidate_ids':ids, 'pages_per_locale':1,
                         'model':MODEL_ID, 'provider':PROVIDER, 'paid_provider_requests':0}
        self.run = {'id':123, 'run_attempt':1, 'head_sha':'f'*40, 'status':'completed',
                    'conclusion':'success', 'head_branch':'main', 'event':'workflow_run',
                    'path':'.github/workflows/portal-extended-locales-r2.yml',
                    'repository':{'full_name':'example/repo', 'private':False},
                    'head_repository':{'full_name':'example/repo'}}
        self.jobs = [{'name':'source', 'status':'completed', 'conclusion':'success',
                      'started_at':'2026-09-25T01:00:00Z', 'completed_at':'2026-09-25T01:10:00Z'},
                     {'name':'publication_handoff', 'status':'completed', 'conclusion':'success'}]

    def review(self, enabled='fr'):
        return review_identity(self.receipt, self.identity, self.assembly, self.active, enabled, self.expected)

    def test_exact_daily_candidate_preserves_other_approved_locales(self):
        variables = self.review()
        self.assertEqual(variables['PORTAL_EXTENDED_APPROVED_LOCALES'], 'fr,pt')
        self.assertEqual(variables['PORTAL_EXTENDED_APPROVED_CANDIDATE_IDS'], self.expected['candidate_specs'])
        self.assertEqual(variables['PORTAL_EXTENDED_APPROVED_STATIC_TREE'], '2'*64)
        self.assertEqual(variables['PORTAL_EXTENDED_LOCALES_ACTIVATION_APPROVED'], 'true')

    def test_first_time_locale_and_disabled_policy_cannot_be_approved(self):
        for enabled in ('', 'pt'):
            with self.subTest(enabled=enabled), self.assertRaises(ExpansionError): self.review(enabled)
        self.active = []
        with self.assertRaises(ExpansionError): self.review()

    def test_each_prepared_identity_field_is_exact(self):
        original = copy.deepcopy(self.identity)
        for field, value in {'schema_version':2, 'operation':'rehearse', 'commit_sha':'3'*40,
            'static_tree_sha256':'4'*64, 'source_generation':'5'*64, 'locales':['fr'],
            'candidate_ids':{'fr':'e'*64}, 'pages_per_locale':2, 'provider':'other',
            'model':'other', 'paid_provider_requests':1}.items():
            self.identity = {**original, field:value}
            with self.subTest(field=field), self.assertRaises(ExpansionError): self.review()

    def test_extra_missing_or_changed_approved_batches_are_rejected(self):
        original = copy.deepcopy(self.assembly)
        for batches in ([self.batch], self.active, self.active+[self.batch, {'generation':'6'*64,'candidates':{'de':'7'*64}}]):
            self.assembly = {**original, 'batches':batches}
            with self.assertRaises(ExpansionError): self.review()

    def test_incomplete_assembly_counts_and_candidate_spec_mismatch_are_rejected(self):
        original = copy.deepcopy(self.assembly)
        for change in ({'status':'incomplete'}, {'detail_only':False}, {'locale_homepages':False}, {'paid_provider_requests':1},
                       {'page_counts':{'fr':0,'pt':1}}, {'page_counts':{'fr':2}},
                       {'page_counts':{'fr':True,'pt':1}}, {'locales':['fr']}):
            self.assembly = {**original, **change}
            with self.subTest(change=change), self.assertRaises(ExpansionError): self.review()
        self.assembly = original
        self.expected['candidate_specs'] = 'fr='+'f'*64+',pt='+'c'*64
        with self.assertRaises(ExpansionError): self.review()

    def test_real_main_producer_can_finish_after_its_frozen_source_day(self):
        producer_is_valid(self.receipt, self.run, self.jobs, 'example/repo')
        # A slow locale may fail while other complete candidates are publishable.
        self.run['conclusion'] = 'failure'
        producer_is_valid(self.receipt, self.run, self.jobs, 'example/repo')

    def test_wrong_producer_attempt_branch_repository_or_cancelled_run_is_rejected(self):
        original = copy.deepcopy(self.run)
        for change in ({'id':124}, {'run_attempt':2}, {'head_sha':'8'*40}, {'status':'in_progress'},
                       {'conclusion':'cancelled'}, {'head_branch':'feature'}, {'event':'pull_request'},
                       {'path':'.github/workflows/other.yml'}, {'repository':{'full_name':'example/repo','private':True}},
                       {'head_repository':{'full_name':'other/repo'}}):
            with self.subTest(change=change), self.assertRaises(ExpansionError):
                producer_is_valid(self.receipt, {**original, **change}, self.jobs, 'example/repo')

    def test_historical_or_unfinished_handoff_cannot_be_automatically_reviewed(self):
        for index in (0,1):
            jobs = copy.deepcopy(self.jobs)
            jobs[index]['conclusion'] = 'skipped'
            with self.assertRaises(ExpansionError): producer_is_valid(self.receipt,self.run,jobs,'example/repo')
        self.receipt['source_day'] = '2026-09-24'
        with self.assertRaises(ExpansionError): producer_is_valid(self.receipt,self.run,self.jobs,'example/repo')

    def test_workflow_uses_normal_reviewer_gate_and_excludes_recovery(self):
        root = Path(__file__).resolve().parents[1]
        source = (root/'.github/workflows/neutral-edge-cutover.yml').read_text()
        review = source.split('  extended_daily_review:',1)[1].split('  extended_locales_approval:',1)[0]
        for text in ("inputs.extended_handoff != ''", "vars.PORTAL_EXTENDED_AUTO_REVIEW == 'true'",
                     "inputs.operation == 'migrate'", "inputs.translation_scope == 'incremental'",
                     'secrets.GH_DISPATCH_TOKEN', 'github.sha'):
            self.assertIn(text, review)
        approval = source.split('  extended_locales_approval:',1)[1].split('  cutover:',1)[0]
        self.assertIn('name: portal-extended-locales-production', approval)
        self.assertIn('Extended locale approval identity mismatch', approval)
        self.assertNotIn('extended_daily_review:', (root/'.github/workflows/neutral-locale-resume.yml').read_text())

    def run_delegated_review(self, *, can_approve=True, bad_identity=False, bad_readback=False,
                             frozen=False, bad_capture=False):
        """Exercise the complete orchestration without credentials or network."""
        store = R2Store(FakeR2(), 'private', '_extended-locales/staging/review')
        corpus = make_corpus([daily_doc()])
        store.put_source(corpus)
        generation = corpus['documents_sha256']
        receipt, assembly, identity = map(copy.deepcopy, (self.receipt, self.assembly, self.identity))
        receipt['batch']['generation'] = generation
        assembly['batches'][-1]['generation'] = generation
        identity['source_generation'] = generation
        capture_path = None
        capture_run, capture_jobs = None, None
        consumer_jobs = copy.deepcopy(self.jobs)
        if frozen:
            from portal_extended_daily_queue import WORKFLOW, admit, prepare_queued
            admission = admit(store, corpus['documents'], '2026-09-25',
                {'run_id':'321','attempt':'1','sha':'a'*40,'repository':'example/repo','workflow':WORKFLOW})
            prepare_queued(store, ('fr',))
            receipt['source_admission'] = admission['admission']
            consumer_jobs[0].update(started_at='2026-09-26T01:00:00Z', completed_at='2026-09-26T01:10:00Z')
            capture_path = 'repos/example/repo/actions/runs/321/attempts/1'
            capture_run = {**self.run, 'id':321, 'head_sha':'a'*40, 'path':WORKFLOW,
                           'conclusion':'failure' if bad_capture else 'success'}
            capture_jobs = [{'name':'source_snapshot','status':'completed','conclusion':'success',
                             'started_at':'2026-09-25T01:00:00Z','completed_at':'2026-09-25T01:10:00Z'}]
        if bad_identity:
            identity['static_tree_sha256'] = '9'*64
        previous = {'release_id': 'previous-release', 'tree_sha256': 'a'*64}
        self.api_calls, self.saved_variables, self.review_objects = [], {}, store.client.objects
        env_path = 'repos/example/repo/environments/'+reviewer.ENVIRONMENT
        pending_path = 'repos/example/repo/actions/runs/456/pending_deployments'
        producer_path = 'repos/example/repo/actions/runs/123/attempts/1'

        def api(path, payload=None, method=None):
            self.api_calls.append((path, method, payload))
            if path == 'repos/example/repo/actions/runs/456':
                return {**self.run, 'id': 456, 'head_sha': '1'*40, 'event': 'workflow_dispatch',
                        'path': '.github/workflows/neutral-edge-cutover.yml'}
            if path == 'repos/example/repo/actions/runs/456/approvals':
                return []
            if path == producer_path:
                return self.run
            if path == producer_path+'/jobs?per_page=100':
                return {'total_count': len(consumer_jobs), 'jobs': consumer_jobs}
            if capture_path and path == capture_path:
                return capture_run
            if capture_path and path == capture_path+'/jobs?per_page=100':
                return {'total_count': len(capture_jobs), 'jobs': capture_jobs}
            if path == env_path:
                return {'id': 789, 'name': reviewer.ENVIRONMENT,
                        'protection_rules': [{'type': 'required_reviewers', 'reviewers': [{'id': 42}]}]}
            if path == pending_path:
                if method == 'POST':
                    self.assertTrue(can_approve)
                    self.assertEqual(payload['environment_ids'], [789])
                    self.assertEqual(payload['state'], 'approved')
                    self.assertEqual(len(self.saved_variables), 7)
                    self.assertTrue(any('/publication-approvals/' in key for key in store.client.objects))
                    return [{'id': 999}]
                return [{'environment': {'id': 789}, 'current_user_can_approve': can_approve}]
            if path == env_path+'/variables?per_page=100':
                return {'total_count': len(self.saved_variables), 'variables': [
                    {'name': name, 'value': '' if bad_readback else value}
                    for name, value in self.saved_variables.items()]}
            if path.startswith(env_path+'/variables') and method in ('POST', 'PATCH'):
                self.saved_variables[payload['name']] = payload['value']
                return None
            self.fail('Unexpected API call: '+path)

        session = MagicMock()
        response = session.__enter__.return_value.get.return_value
        response.status_code, response.content = 200, json.dumps(previous).encode()
        response.json.return_value = previous
        environment = {'GITHUB_ACTIONS': 'true', 'GITHUB_REF': 'refs/heads/main',
                       'GITHUB_EVENT_NAME': 'workflow_dispatch', 'GITHUB_REPOSITORY': 'example/repo',
                       'GITHUB_RUN_ID': '456', 'GITHUB_SHA': '1'*40, 'GH_TOKEN': 'test-only-not-a-credential',
                       'GITHUB_RUN_ATTEMPT': '1',
                       'EXTENDED_HANDOFF': 'a'*64, 'ENABLED_LOCALES': 'fr',
                       'CANDIDATE_IDS': self.expected['candidate_specs'], 'CANDIDATE_LOCALES': 'fr,pt',
                       'CANDIDATE_STATIC_TREE': '2'*64, 'CANDIDATE_PAGES_PER_LOCALE': '1'}
        with tempfile.TemporaryDirectory() as temporary, chdir(temporary):
            files = {'previous/edge-state.json': previous, 'candidate/extended-assembly.json': assembly,
                     'candidate/extended-locale-review-identity.json': identity}
            for name, value in files.items():
                path = Path('_release_validation')/name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(json.dumps(value))
            with patch.dict(os.environ, environment, clear=True), \
                 patch.object(reviewer.R2Store, 'from_env', return_value=store), \
                 patch.object(reviewer, 'read_handoff', return_value=receipt), \
                 patch.object(reviewer, 'read_active_batches', return_value=self.active), \
                 patch.object(reviewer.requests, 'Session', return_value=session), \
                 patch.object(reviewer, 'api', side_effect=api), patch('builtins.print'):
                reviewer.main()

    def test_orchestrator_persists_and_reads_back_exact_identity_before_normal_approval(self):
        self.run_delegated_review()
        reviews = [row for row in self.api_calls if row[0].endswith('/pending_deployments') and row[1] == 'POST']
        self.assertEqual(len(reviews), 1)
        self.assertEqual(self.saved_variables['PORTAL_EXTENDED_APPROVED_LOCALES'], 'fr,pt')

    def test_frozen_queue_orchestrator_verifies_original_capture_before_normal_approval(self):
        self.run_delegated_review(frozen=True)
        self.assertTrue(any('/runs/321/attempts/1' in path for path, _method, _value in self.api_calls))
        self.assertEqual(len([row for row in self.api_calls if row[0].endswith('/pending_deployments') and row[1] == 'POST']), 1)

    def test_failed_original_capture_cannot_receive_delegated_approval(self):
        with self.assertRaises(ExpansionError): self.run_delegated_review(frozen=True, bad_capture=True)
        self.assertFalse(any(method for _path, method, _payload in self.api_calls))

    def test_orchestrator_mismatched_artifact_never_writes_approval_variables(self):
        with self.assertRaises(ExpansionError):
            self.run_delegated_review(bad_identity=True)
        self.assertFalse(any(method for _path, method, _payload in self.api_calls))

    def test_orchestrator_denied_reviewer_never_writes_or_bypasses_environment(self):
        with self.assertRaises(ExpansionError):
            self.run_delegated_review(can_approve=False)
        self.assertFalse(any(method for _path, method, _payload in self.api_calls))

    def test_orchestrator_variable_readback_mismatch_never_submits_approval(self):
        with self.assertRaises(ExpansionError):
            self.run_delegated_review(bad_readback=True)
        self.assertFalse(any(path.endswith('/pending_deployments') and method == 'POST'
                             for path, method, _payload in self.api_calls))
        self.assertFalse(any('/publication-approvals/' in key for key in self.review_objects))


class APIRecoveryTests(unittest.TestCase):
    def response(self, status=200, body=b'{}', error=b'', headers=b''):
        return subprocess.CompletedProcess([], 0 if status < 400 and not error else 1,
            b'HTTP/2.0 '+str(status).encode()+b' Test\r\n'+headers+b'\r\n'+body, error)

    def test_read_transients_are_bounded_and_preserve_original_request(self):
        failed = self.response(502, error=b'gh: HTTP 502 private response')
        with patch.object(reviewer.subprocess, 'run', side_effect=[failed]*3+[self.response()]) as run, \
                patch.object(reviewer.time, 'sleep') as sleep, patch('builtins.print'):
            self.assertEqual(reviewer.api('repos/example/repo/actions/runs/456'), {})
        self.assertEqual(run.call_count, 4)
        self.assertEqual([call.args[0] for call in sleep.call_args_list], [5, 15, 30])
        self.assertTrue(all(call == run.call_args_list[0] for call in run.call_args_list))

    def test_timeout_is_retried_but_write_is_never_blindly_repeated(self):
        with patch.object(reviewer.subprocess, 'run', side_effect=[subprocess.TimeoutExpired('gh', 60), self.response()]) as run, \
                patch.object(reviewer.time, 'sleep'), patch('builtins.print'):
            reviewer.api('repos/example/repo'); self.assertEqual(run.call_count, 2)
        with patch.object(reviewer.subprocess, 'run', return_value=self.response(502, error=b'HTTP 502')) as run, \
                patch.object(reviewer.time, 'sleep') as sleep:
            with self.assertRaises(reviewer.ReviewAPIError): reviewer.api('repos/example/repo', {'state': 'approved'}, 'POST')
        self.assertEqual(run.call_count, 1); sleep.assert_not_called()

    def test_gh_connection_failure_is_retried_without_transport_changes(self):
        failed = subprocess.CompletedProcess([], 1, b'', b'error connecting to api.github.com')
        with patch.object(reviewer.subprocess, 'run', side_effect=[failed, self.response()]) as run, \
                patch.object(reviewer.time, 'sleep') as sleep, patch('builtins.print'):
            self.assertEqual(reviewer.api('repos/example/repo/actions/runs/456'), {})
        self.assertEqual(run.call_count, 2)
        self.assertEqual(run.call_args_list[0], run.call_args_list[1])
        sleep.assert_called_once_with(5)

    def test_auth_certificate_and_unclassified_failures_do_not_retry_or_echo_details(self):
        for status, error in [(401, b'HTTP 401 secret'), (403, b'HTTP 403 secret'),
                              (502, b'x509: certificate signed by unknown authority secret'),
                              (200, b'unknown client failure secret')]:
            with self.subTest(status=status, error=error), \
                    patch.object(reviewer.subprocess, 'run', return_value=self.response(status, error=error)) as run, \
                    patch.object(reviewer.time, 'sleep') as sleep:
                with self.assertRaises(reviewer.ReviewAPIError) as caught: reviewer.api('repos/example/repo')
                self.assertNotIn('secret', str(caught.exception))
                self.assertEqual(run.call_count, 1); sleep.assert_not_called()

    def test_retry_after_is_respected_and_fourth_failure_stops(self):
        for status in (408, 429, 503):
            failed = self.response(status, error=f'HTTP {status}'.encode(), headers=b'Retry-After: 20\r\n')
            with self.subTest(status=status), patch.object(reviewer.subprocess, 'run', return_value=failed) as run, \
                    patch.object(reviewer.time, 'sleep') as sleep, patch('builtins.print'):
                with self.assertRaises(reviewer.ReviewAPIError): reviewer.api('repos/example/repo')
                self.assertEqual(run.call_count, 4)
                self.assertEqual([call.args[0] for call in sleep.call_args_list], [20, 20, 30])


class ApprovalRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.environment = {'id': 789, 'name': reviewer.ENVIRONMENT,
                            'protection_rules': [{'type': 'required_reviewers', 'reviewers': [{'id': 42}]}]}
        self.variables = {'PORTAL_EXTENDED_APPROVED_STATIC_TREE': '2'*64}
        self.run = {'id': 456, 'run_attempt': 1, 'head_sha': '1'*40, 'head_branch': 'main',
                    'event': 'workflow_dispatch', 'path': '.github/workflows/neutral-edge-cutover.yml',
                    'repository': {'full_name': 'example/repo'}, 'head_repository': {'full_name': 'example/repo'}}
        self.job = {'id': 1234, 'run_id': 456, 'head_sha': '1'*40, 'name': 'extended_locales_approval',
                    'status': 'in_progress', 'started_at': '2026-10-06T18:00:00Z'}
        self.history, self.calls, self.posts = [], [], []
        self.pending = [{'environment': {'id': 789}, 'current_user_can_approve': True}]
        self.on_failure = lambda payload: None
        self.failure = reviewer.ReviewAPIError(502, transient=True)
        self.always_fail = False

    def api(self, path, payload=None, method=None):
        self.calls.append((path, method))
        if method == 'POST':
            self.posts.append(copy.deepcopy(payload))
            if len(self.posts) == 1 or self.always_fail:
                self.on_failure(payload)
                raise self.failure
            return [{'id': 999}]
        if path.endswith('/runs/456'): return copy.deepcopy(self.run)
        if path.endswith('/approvals'): return copy.deepcopy(self.history)
        if path.endswith('/pending_deployments'): return copy.deepcopy(self.pending)
        if '/attempts/1/jobs' in path: return {'total_count': 1, 'jobs': [copy.deepcopy(self.job)]}
        if path.endswith('/variables?per_page=100'):
            return {'total_count': len(self.variables), 'variables': [
                {'name': key, 'value': value} for key, value in self.variables.items()]}
        if '/environments/' in path: return copy.deepcopy(self.environment)
        self.fail('Unexpected API route')

    def invoke(self, revalidate=None):
        with patch.dict(os.environ, {'GITHUB_RUN_ATTEMPT': '1', 'GITHUB_SHA': '1'*40}), \
                patch.object(reviewer.time, 'sleep') as sleep, patch('builtins.print'):
            self.sleeps = sleep
            return reviewer.submit_approval('example/repo', '456', copy.deepcopy(self.environment),
                copy.deepcopy(self.variables), 'Exact approved release.', approval_job='extended_locales_approval',
                revalidate=revalidate or (lambda: None), api_call=self.api)

    def accept(self, payload):
        self.pending = []
        self.history.append({'state': 'approved', 'comment': payload['comment'],
                             'environments': [{'id': 789, 'name': reviewer.ENVIRONMENT}]})

    def test_502_not_applied_requires_exact_pending_identity_before_retry(self):
        revalidate = MagicMock()
        self.assertEqual(self.invoke(revalidate), [{'id': 999}])
        self.assertEqual(len(self.posts), 2); self.assertEqual(self.posts[0], self.posts[1])
        revalidate.assert_called_once()
        self.assertEqual([call.args[0] for call in self.sleeps.call_args_list], [5])
        self.assertIn(('repos/example/repo/actions/runs/456/pending_deployments', None), self.calls)

    def test_502_after_acceptance_does_not_submit_twice_or_claim_deployment(self):
        self.on_failure = self.accept
        self.assertEqual(self.invoke(), [])
        self.assertEqual(len(self.posts), 1)
        self.assertTrue(any('/attempts/1/jobs' in path for path, _ in self.calls))

    def test_empty_pending_without_exact_new_review_is_not_success(self):
        self.on_failure = lambda payload: setattr(self, 'pending', [])
        with self.assertRaisesRegex(ExpansionError, 'remains unverified'): self.invoke()
        self.assertEqual(len(self.posts), 1)

    def test_old_approval_history_cannot_prove_the_current_write_was_accepted(self):
        marker = reviewer.digest(reviewer.stable_bytes({'run_id': '456', 'attempt': '1', 'sha': '1'*40,
            'environment_id': 789, 'variables': self.variables}))
        self.history = [{'state': 'approved', 'comment': f'Exact approved release. Review identity: {marker}.',
                         'environments': [{'id': 789, 'name': reviewer.ENVIRONMENT}]}]
        self.on_failure = lambda payload: setattr(self, 'pending', [])
        with self.assertRaisesRegex(ExpansionError, 'remains unverified'): self.invoke()
        self.assertEqual(len(self.posts), 1)

    def test_accepted_review_for_another_environment_is_not_success(self):
        def wrong_environment(payload):
            self.accept(payload)
            self.history[-1]['environments'][0]['id'] = 790
        self.on_failure = wrong_environment
        with self.assertRaisesRegex(ExpansionError, 'remains unverified'): self.invoke()
        self.assertEqual(len(self.posts), 1)

    def test_accepted_queued_job_is_observed_until_it_starts_without_another_post(self):
        self.on_failure = self.accept
        original = self.api
        reads = 0
        def api(path, payload=None, method=None):
            nonlocal reads
            if '/attempts/1/jobs' in path:
                reads += 1
                self.job.update(status='queued' if reads == 1 else 'in_progress',
                                started_at=None if reads == 1 else '2026-10-06T18:00:00Z')
            return original(path, payload, method)
        self.api = api
        self.assertEqual(self.invoke(), [])
        self.assertEqual(len(self.posts), 1); self.assertEqual(reads, 2)

    def test_wrong_attempt_sha_environment_variables_or_review_authority_stops_retry(self):
        changes = [lambda: self.run.update(run_attempt=2), lambda: self.run.update(head_sha='f'*40),
                   lambda: self.environment.update(protection_rules=[]),
                   lambda: self.variables.update(PORTAL_EXTENDED_APPROVED_STATIC_TREE='3'*64),
                   lambda: self.pending[0].update(current_user_can_approve=False)]
        for change in changes:
            with self.subTest(change=change):
                self.setUp()
                self.on_failure = lambda payload: change()
                with self.assertRaises(ExpansionError): self.invoke()
                self.assertEqual(len(self.posts), 1)

    def test_accepted_history_requires_exact_current_attempt_job_to_start(self):
        for update in ({'run_id': 999}, {'head_sha': 'a'*40}, {'status': 'completed', 'conclusion': 'skipped'},
                       {'status': 'queued', 'started_at': None}):
            with self.subTest(update=update):
                self.setUp(); self.on_failure = self.accept; self.job.update(update)
                with self.assertRaises(ExpansionError): self.invoke()
                self.assertEqual(len(self.posts), 1)

    def test_auth_failure_and_live_state_change_never_resubmit(self):
        self.failure = reviewer.ReviewAPIError(403)
        with self.assertRaises(reviewer.ReviewAPIError): self.invoke()
        self.assertEqual(len(self.posts), 1); self.sleeps.assert_not_called()
        self.setUp()
        with self.assertRaisesRegex(ExpansionError, 'live changed'):
            self.invoke(MagicMock(side_effect=ExpansionError('live changed')))
        self.assertEqual(len(self.posts), 1)

    def test_write_budget_is_four_total_and_final_result_is_still_reconciled(self):
        self.always_fail = True
        with self.assertRaisesRegex(ExpansionError, 'budget exhausted'): self.invoke()
        self.assertEqual(len(self.posts), 4)
        self.assertEqual([call.args[0] for call in self.sleeps.call_args_list], [5, 15, 30])
        self.setUp(); self.always_fail = True
        self.on_failure = lambda payload: self.accept(payload) if len(self.posts) == 4 else None
        self.assertEqual(self.invoke(), []); self.assertEqual(len(self.posts), 4)


if __name__ == '__main__':
    unittest.main()
