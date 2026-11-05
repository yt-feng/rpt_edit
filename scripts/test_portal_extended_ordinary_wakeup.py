"""Fault injection for the actual ordinary wake-up route; no dispatch or models."""
import copy
from io import BytesIO
import json
from pathlib import Path
import re
import unittest
from urllib.error import HTTPError, URLError
from datetime import datetime, timezone

import yaml

import portal_extended_ordinary_wakeup as wakeup


ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = 'example/repo'


class FakeGitHub:
    def __init__(self, rows=()):
        self.rows = copy.deepcopy(list(rows))
        self.runs, self.calls, self.post_error = {}, [], False
        for row in self.rows:
            self.runs[row['run_id']] = self.run(row)

    @staticmethod
    def run(row):
        return {'id':row['run_id'], 'path':wakeup.WORKFLOW, 'display_title':row['run_name'],
            'event':'workflow_dispatch', 'head_branch':'main', 'status':row['status'],
            'created_at':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
            'head_repository':{'full_name':REPOSITORY}}

    def api(self, path, payload=None):
        self.calls.append((path, copy.deepcopy(payload)))
        if payload is not None:
            if self.post_error:
                raise wakeup.WakeupError('Ambiguous POST')
            return {}
        if '/concurrency_groups/' in path:
            return {'group_name':wakeup.GROUP, 'total_count':len(self.rows), 'group_members':copy.deepcopy(self.rows)}
        if '/runs?' in path:
            return {'total_count':len(self.runs), 'workflow_runs':copy.deepcopy(list(self.runs.values()))}
        return copy.deepcopy(self.runs[int(path.rsplit('/', 1)[1])])


def row(identity=1, *, locales='all-supported', status='pending', title=None):
    return {'run_id':identity, 'run_name':title or wakeup.ordinary_request(locales)[1], 'status':status}


class WakeupTests(unittest.TestCase):
    def test_pending_ordinary_is_reused_and_new_admission_does_not_add_a_scan(self):
        api = FakeGitHub([row()])
        for _ in range(5):
            self.assertEqual(wakeup.wake(api.api, REPOSITORY, 'all-supported')['reused_pending_run_id'], 1)
        self.assertFalse(any(payload for _, payload in api.calls))

    def test_active_same_request_still_gets_one_pending_successor(self):
        api = FakeGitHub([row(status='in_progress')])
        result = wakeup.wake(api.api, REPOSITORY, 'all-supported')
        self.assertTrue(result['dispatched'])
        posts = [payload for _, payload in api.calls if payload]
        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0], {'ref':'main', 'inputs':wakeup.ordinary_request('all-supported')[0]})

    def test_manual_and_exact_requests_are_retained_without_being_reused(self):
        original = [row(title='Extended locale R2 publication-resume (km)'),
                    row(2, title='Extended locale R2 candidate (all-supported)'), row(3, locales='fr')]
        api = FakeGitHub(original)
        self.assertTrue(wakeup.wake(api.api, REPOSITORY, 'all-supported')['dispatched'])
        self.assertEqual(api.rows, original)
        self.assertEqual(sum(payload is not None for _, payload in api.calls), 1)

    def test_exact_locale_order_and_defaults_are_part_of_identity(self):
        values, _ = wakeup.ordinary_request('fr,pt')
        self.assertNotEqual(values['ordinary_request_sha256'], wakeup.ordinary_request('pt,fr')[0]['ordinary_request_sha256'])
        self.assertEqual(values['locales'], 'fr,pt')
        self.assertEqual((values['seconds'], values['allow_source_fallback'], values['source_generation']), ('14400','true',''))

    def test_failed_queue_read_or_unproved_pending_identity_never_posts(self):
        api = FakeGitHub([row()]); api.runs[1]['head_branch'] = 'feature'
        with self.assertRaises(wakeup.WakeupError):
            wakeup.wake(api.api, REPOSITORY, 'all-supported')
        self.assertFalse(any(payload for _, payload in api.calls))
        calls = []
        def unavailable(path, payload=None):
            calls.append(payload)
            raise wakeup.WakeupError('Unavailable GET')
        with self.assertRaises(wakeup.WakeupError):
            wakeup.wake(unavailable, REPOSITORY, 'all-supported')
        self.assertEqual(calls, [None])

    def test_ambiguous_post_is_never_repeated_and_old_active_is_not_new_acceptance(self):
        api = FakeGitHub([row(status='in_progress')]); api.post_error = True
        with self.assertRaisesRegex(wakeup.WakeupError, 'unresolved'):
            wakeup.wake(api.api, REPOSITORY, 'all-supported')
        self.assertEqual(sum(payload is not None for _, payload in api.calls), 1)

    def test_accepted_post_after_transport_loss_is_found_without_another_post(self):
        api = FakeGitHub()
        def accepted(path, payload=None):
            if payload is not None:
                api.calls.append((path, payload))
                api.rows = [row(9)]; api.runs[9] = api.run(api.rows[0])
                raise wakeup.WakeupError('Lost acknowledgement')
            return api.api(path, payload)
        self.assertEqual(wakeup.wake(accepted, REPOSITORY, 'all-supported')['accepted_run_id'], 9)
        self.assertEqual(sum(payload is not None for _, payload in api.calls), 1)

    def test_completed_child_is_found_even_when_the_queue_api_is_unavailable(self):
        for conclusion in ('success', 'failure'):
            with self.subTest(conclusion=conclusion):
                api = FakeGitHub()
                posted = False
                def accepted_then_finished(path, payload=None):
                    nonlocal posted
                    if payload is not None:
                        posted = True; api.calls.append((path, payload))
                        api.runs[9] = {**api.run(row(9,status='completed')), 'conclusion':conclusion}
                        raise wakeup.WakeupError('Lost POST acknowledgement')
                    if posted and '/concurrency_groups/' in path:
                        raise wakeup.WakeupError('Queue API outage')
                    return api.api(path)
                result = wakeup.wake(accepted_then_finished, REPOSITORY, 'all-supported')
                self.assertEqual(result['accepted_run_id'], 9)
                self.assertEqual(sum(payload is not None for _, payload in api.calls), 1)

    def test_http_inspection_retries_are_bounded_and_post_is_attempted_once(self):
        calls, waits = [], []
        def offline(request, **kwargs):
            calls.append(request.method)
            raise URLError('offline')
        api = wakeup.GitHub(REPOSITORY, 'test-token', request=offline, sleep=waits.append)
        with self.assertRaises(wakeup.WakeupError): api.api('actions/concurrency_groups/'+wakeup.GROUP)
        self.assertEqual(calls, ['GET']*3); self.assertEqual(waits, [1, 3])
        calls.clear(); waits.clear()
        with self.assertRaises(wakeup.WakeupError): api.api('dispatch', {'inputs':{}})
        self.assertEqual(calls, ['POST']); self.assertEqual(waits, [])


def evaluate(expression, values):
    source = expression.strip().removeprefix('${{').removesuffix('}}')
    source = re.sub(r'\b(?:github|inputs|vars)\.[A-Za-z0-9_.]+', lambda m:repr(values.get(m[0], '')), source)
    source = re.sub(r'\btrue\b', 'True', source)
    source = re.sub(r'\bfalse\b', 'False', source)
    source = source.replace('&&', ' and ').replace('||', ' or ')
    return eval('('+source+')', {'__builtins__':{}, 'format':lambda s,*v:s.format(*v)})


class WakeupWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.consumer = yaml.safe_load((ROOT/wakeup.WORKFLOW).read_text())
        self.wake = yaml.safe_load((ROOT/'.github/workflows/portal-extended-consumer-wakeup.yml').read_text())

    def test_only_fast_wakeup_receives_source_completions_and_shares_followup_lock(self):
        self.assertNotIn('workflow_run', self.consumer[True])
        self.assertEqual(self.wake[True]['workflow_run']['workflows'], ['Extended locale source admission'])
        self.assertEqual(self.wake['concurrency'], self.consumer['jobs']['continue_admitted_batches']['concurrency'])
        self.assertEqual(self.wake['concurrency']['queue'], 'max')
        text = (ROOT/'.github/workflows/portal-extended-consumer-wakeup.yml').read_text()
        self.assertNotIn('R2_', text)
        self.assertNotIn('gh run watch', text)
        checkout = self.wake['jobs']['wake_pending_scan']['steps'][0]['with']
        self.assertIs(checkout['sparse-checkout-cone-mode'], False)

    def test_wakeup_rejects_unsuccessful_foreign_private_and_nonmain_events(self):
        baseline = {'github.event_name':'workflow_run', 'github.event.repository.private':False, 'github.ref':'refs/heads/main',
            'github.repository':REPOSITORY, 'github.event.repository.default_branch':'main',
            'github.event.workflow_run.conclusion':'success', 'github.event.workflow_run.head_branch':'main',
            'github.event.workflow_run.head_repository.full_name':REPOSITORY}
        guard = self.wake['jobs']['wake_pending_scan']['if']
        self.assertTrue(evaluate(guard, baseline))
        for key, value in [('github.event.workflow_run.conclusion','skipped'),
                ('github.event.workflow_run.conclusion','failure'), ('github.event.workflow_run.head_branch','feature'),
                ('github.event.workflow_run.head_repository.full_name','fork/repo'),
                ('github.event.repository.private',True), ('github.ref','refs/heads/other')]:
            with self.subTest(key=key, value=value):
                self.assertFalse(evaluate(guard, {**baseline, key:value}))
        manual = {'github.event_name':'workflow_dispatch', 'github.event.repository.private':False,
                  'github.ref':'refs/heads/main'}
        self.assertTrue(evaluate(guard, manual))
        self.assertFalse(evaluate(guard, {**manual,'github.ref':'refs/heads/feature'}))
        self.assertFalse(evaluate(guard, {**manual,'github.event.repository.private':True}))

    def test_run_title_identity_cannot_hide_manual_or_nondefault_options(self):
        request, title = wakeup.ordinary_request('fr,pt')
        values = {'inputs.'+key: value for key,value in request.items()}
        values.update({'inputs.allow_source_fallback':True, 'inputs.diagnose_runtime':False})
        self.assertEqual(evaluate(self.consumer['run-name'], values), title)
        for key, value in [('source_generation','a'*64), ('continuation_evidence','{}'),
                ('operation','publication-resume'), ('seconds','900'), ('allow_source_fallback',False),
                ('diagnose_runtime',True), ('ordinary_request_sha256','')]:
            with self.subTest(key=key):
                self.assertNotEqual(evaluate(self.consumer['run-name'], {**values,'inputs.'+key:value}), title)


if __name__ == '__main__':
    unittest.main()
