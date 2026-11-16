#!/usr/bin/env python3
import copy
import unittest

import dispatch_neutral_locale_followup as followup

REPOSITORY = 'owner/repository'
SOURCE_HEAD = 'a' * 40
MAIN_HEAD = 'b' * 40


def run(run_id=22, *, key='11:1', status='queued', conclusion=None, head=MAIN_HEAD):
    return {'id': run_id, 'display_title': followup.TITLE + (f' [source {key}]' if key else ''),
            'status': status, 'conclusion': conclusion, 'head_sha': head, 'head_branch': 'main',
            'head_repository': {'full_name': REPOSITORY}, 'event': 'workflow_dispatch',
            'path': '.github/workflows/' + followup.WORKFLOW}


class FakeGitHub:
    def __init__(self, inventories):
        self.source = {'id': 11, 'run_attempt': 1, 'head_sha': SOURCE_HEAD, 'head_branch': 'main',
                       'created_at': '2026-11-17T00:00:00Z',
                       'head_repository': {'full_name': REPOSITORY},
                       'path': '.github/workflows/' + followup.WORKFLOW}
        self.jobs = [{'name': 'prepare_release', 'conclusion': 'success'},
                     {'name': 'cutover', 'conclusion': 'success'}]
        self.inventories = list(inventories)
        self.current_head_rows = copy.deepcopy(inventories[0])
        self.posts = []
        self.reads = []
        self.post_error = None

    def get(self, path):
        self.reads.append(path)
        if path.endswith('/actions/runs/11'):
            return copy.deepcopy(self.source)
        if '/attempts/1/jobs?' in path:
            return {'jobs': copy.deepcopy(self.jobs)}
        if path.endswith('/git/ref/heads/main'):
            return {'object': {'sha': MAIN_HEAD}}
        if f'/actions/workflows/{followup.WORKFLOW}/runs?' in path:
            if 'head_sha=' in path:
                assert 'head_sha=' + MAIN_HEAD in path
                return {'workflow_runs': copy.deepcopy(self.current_head_rows)}
            assert 'created=' in path
            rows = self.inventories[0]
            if len(self.inventories) > 1:
                self.inventories.pop(0)
            return {'workflow_runs': copy.deepcopy(rows)}
        raise AssertionError(path)

    def dispatch(self, path, payload):
        self.posts.append((path, payload))
        if self.post_error:
            raise self.post_error


class FollowupTests(unittest.TestCase):
    def ensure(self, api):
        return followup.ensure_followup(api, REPOSITORY, 11, 1, SOURCE_HEAD, sleep=lambda _: None)

    def test_coalesces_pending_locale_work_that_will_capture_latest_chinese(self):
        for status in followup.PENDING:
            with self.subTest(status=status):
                api = FakeGitHub([[run(key='9:1', status=status)]])
                self.assertEqual(self.ensure(api), {'state': 'coalesced', 'run_id': 22, 'source_run_id': 11})
                self.assertEqual(api.posts, [])

    def test_exact_prior_source_dispatch_is_idempotent_after_completion(self):
        api = FakeGitHub([[run(status='completed', conclusion='success')]])
        self.assertEqual(self.ensure(api)['state'], 'already_dispatched')
        self.assertEqual(api.posts, [])

    def test_failed_same_source_requires_inspection_without_blind_replay(self):
        api = FakeGitHub([[run(status='completed', conclusion='failure')]])
        with self.assertRaisesRegex(followup.FollowupError, 'did not succeed'):
            self.ensure(api)
        self.assertEqual(api.posts, [])

    def test_dispatches_current_main_after_catalog_acceptance_with_exact_marker(self):
        api = FakeGitHub([[], [run()]])
        self.assertEqual(self.ensure(api)['state'], 'accepted')
        self.assertEqual(len(api.posts), 1)
        self.assertEqual(api.posts[0][1], {
            'ref': 'main', 'inputs': {'operation': 'migrate', 'translation_scope': 'incremental',
                                    'publication_mode': 'locales', 'locale_followup_source': '11:1'},
        })
        self.assertIn('/git/ref/heads/main', '\n'.join(api.reads))

    def test_timed_out_dispatch_is_read_back_without_a_second_post(self):
        api = FakeGitHub([[], [], [run()]])
        api.post_error = TimeoutError('reply was lost after acceptance')
        self.assertEqual(self.ensure(api)['state'], 'accepted')
        self.assertEqual(len(api.posts), 1)

    def test_unknown_outcome_stops_after_bounded_readback_without_reposting(self):
        api = FakeGitHub([[]])
        api.post_error = TimeoutError('reply was lost')
        with self.assertRaisesRegex(followup.FollowupError, 'not confirmed'):
            self.ensure(api)
        self.assertEqual(len(api.posts), 1)
        self.assertEqual(sum('/runs?' in path for path in api.reads), 6)

    def test_source_marker_is_idempotent_across_main_head_changes(self):
        api = FakeGitHub([[run(head=SOURCE_HEAD, status='completed', conclusion='success')]])
        self.assertEqual(self.ensure(api)['state'], 'already_dispatched')
        self.assertEqual(api.posts, [])

    def test_main_advance_during_dispatch_is_confirmed_across_heads(self):
        api = FakeGitHub([[], [run(head='c' * 40)]])
        api.post_error = TimeoutError('response was lost while main advanced')
        self.assertEqual(self.ensure(api)['state'], 'accepted')
        self.assertEqual(len(api.posts), 1)

    def test_completed_other_source_and_wrong_head_are_not_pending_work(self):
        for row in (run(21, key='9:1', status='completed', conclusion='failure'),
                    run(21, key='9:1', head='c' * 40)):
            with self.subTest(row=row['status']):
                api = FakeGitHub([[row], [row, run()]])
                self.assertEqual(self.ensure(api)['state'], 'accepted')
                self.assertEqual(len(api.posts), 1)

    def test_changed_source_or_failed_catalog_gate_cannot_dispatch(self):
        for field, value in (('head_sha', 'c' * 40), ('run_attempt', 2), ('head_branch', 'topic')):
            api = FakeGitHub([[]])
            api.source[field] = value
            with self.subTest(field=field), self.assertRaises(followup.FollowupError):
                self.ensure(api)
            self.assertEqual(api.posts, [])
        for job, result in (('prepare_release', 'failure'), ('cutover', 'failure'), ('cutover', None)):
            api = FakeGitHub([[]])
            next(row for row in api.jobs if row['name'] == job)['conclusion'] = result
            with self.subTest(job=job, result=result), self.assertRaises(followup.FollowupError):
                self.ensure(api)
            self.assertEqual(api.posts, [])


if __name__ == '__main__':
    unittest.main()
