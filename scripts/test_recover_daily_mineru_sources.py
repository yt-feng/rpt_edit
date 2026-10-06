#!/usr/bin/env python3
"""Exercise the complete source adapter with real ledger/cache/receipt code."""
import json
import shutil
import unittest

import recover_daily_mineru_sources as daily
import test_recover_durable_mineru_sources as fixture
from mineru_result_cache import ResultCache
from mineru_task_ledger import LedgerError
from mineru_terminal_recovery import AUTOMATIC_POLICY, POLICY
from recover_durable_mineru_sources import RecoveryError


ENV = {'GITHUB_ACTIONS': 'true', 'GITHUB_REPOSITORY': 'owner/repo',
       'GITHUB_REF': 'refs/heads/main', 'GITHUB_EVENT_NAME': 'schedule',
       'GITHUB_WORKFLOW_REF': 'owner/repo/.github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml@refs/heads/main',
       'GITHUB_RUN_ID': '456', 'GITHUB_SHA': 'b' * 40}


class DailyTests(unittest.TestCase):
    setUp = fixture.RecoveryTests.setUp
    save_manifest = fixture.RecoveryTests.save_manifest
    downloader = fixture.RecoveryTests.downloader
    validate = fixture.RecoveryTests.validate

    def recover(self, **kwargs):
        options = {'env': ENV, 'total_timeout': 30, 'interval': 1,
                   'downloader': self.downloader, 'asset_writer': fixture.assets}
        options.update(kwargs)
        return daily.recover_daily(self.ledger, self.input, self.output,
                                   len(self.rows), '261003', **options)

    def source_claims(self):
        return {p.name: p.read_bytes() for p in (self.store.root / 'sources').glob('*.json')}

    def controls(self):
        return {p.name: p.read_bytes() for p in (self.store.root / 'recoveries').glob('*.json')}

    def clock(self):
        self.now = 0
        self.ledger.clock = lambda: self.now
        self.ledger.sleep = lambda seconds: setattr(self, 'now', self.now + seconds)

    def test_complete_originals_require_zero_posts_and_complete_real_receipt(self):
        before = self.source_claims()
        receipt = self.recover()
        self.assertEqual((receipt['report_count'], receipt['provider_posts']), (7, 0))
        self.assertEqual(self.validate()['recovery_execution_sha'], ENV['GITHUB_SHA'])
        self.assertEqual(self.provider.posts, [])
        self.assertEqual(before, self.source_claims())

    def test_only_failed_members_submitted_after_every_success_zip_is_saved(self):
        self.provider.plans['root-1'] = ['done', 'failed', 'failed']
        before = self.source_claims()
        receipt = self.recover(result_cache=ResultCache(fixture.MemoryR2(), 'test'))
        self.assertEqual((receipt['report_count'], receipt['provider_posts']), (7, 1))
        self.assertEqual([item['id'] for item in self.provider.posts[0]],
                         [item['id'] for item in self.originals[0]['files'][1:]])
        first_post = self.provider.events.index('post')
        self.assertEqual(self.provider.events[:first_post].count('zip'), 5)
        self.assertEqual(before, self.source_claims())
        control = json.loads(next(iter(self.controls().values())))
        self.assertEqual(control['policy']['name'], AUTOMATIC_POLICY)
        self.assertEqual(len(control['children']), 1)
        self.assertEqual(len(self.validate()['reports']), 7)

    def test_existing_children_and_cache_resume_with_zero_new_posts(self):
        self.provider.plans['root-1'] = ['done', 'failed', 'failed']
        cache = ResultCache(fixture.MemoryR2(), 'test')
        self.recover(result_cache=cache)
        claims, controls = self.source_claims(), self.controls()
        shutil.rmtree(self.output)
        def unavailable(_):
            raise AssertionError('Cached source must not access the result CDN')
        result = self.recover(result_cache=cache, downloader=unavailable)
        self.assertEqual((result['provider_posts'], len(self.provider.posts)), (0, 1))
        self.assertEqual(self.source_claims(), claims)
        self.assertEqual(self.controls(), controls)

    def test_two_children_is_lifetime_limit_across_daily_retries(self):
        self.provider.plans.update({'root-1': ['done', 'failed', 'done'],
                                    'child-1': ['failed'], 'child-2': ['failed']})
        cache = ResultCache(fixture.MemoryR2(), 'test')
        for _ in range(2):
            with self.assertRaisesRegex(RecoveryError, 'recovery_task_incomplete'):
                self.recover(result_cache=cache)
            self.assertFalse(self.output.exists())
        self.assertEqual([len(items) for items in self.provider.posts], [1, 1])
        self.assertEqual(len(json.loads(next(iter(self.controls().values())))['children']), 2)

    def test_pending_task_only_gets_without_reservation_or_post(self):
        self.clock()
        self.provider.plans['root-1'] = ['done', 'running', 'done']
        claims = self.source_claims()
        with self.assertRaisesRegex(RecoveryError, 'original_task_incomplete'):
            self.recover(total_timeout=3)
        self.assertEqual(self.now, 3)
        self.assertGreater(len(self.provider.polls), 1)
        self.assertEqual(self.provider.posts, [])
        self.assertEqual(self.controls(), {})
        self.assertEqual(self.source_claims(), claims)

    def test_pending_then_failed_waits_for_terminal_before_child(self):
        self.clock()
        base_poll = self.provider.poll
        calls = 0
        def poll(batch_id, token, timeout):
            nonlocal calls
            if batch_id == 'root-1':
                calls += 1
                self.provider.plans[batch_id] = ['done', 'running' if calls == 1 else 'failed', 'done']
            return base_poll(batch_id, token, timeout)
        self.provider.poll = poll
        result = self.recover(total_timeout=10)
        self.assertEqual(result['report_count'], 7)
        self.assertEqual(len(self.provider.posts), 1)
        self.assertEqual(len(self.provider.posts[0]), 1)
        self.assertGreaterEqual(calls, 2)

    def test_legacy_manual_policy_and_proofs_are_reused_unchanged(self):
        self.provider.plans['root-1'] = ['done', 'failed', 'done']
        fixture.RecoveryTests.recover(self)
        claims, controls = self.source_claims(), self.controls()
        self.assertEqual(json.loads(next(iter(controls.values())))['policy']['name'], POLICY)
        shutil.rmtree(self.output)
        result = self.recover()
        self.assertEqual((result['provider_posts'], len(self.provider.posts)), (0, 1))
        self.assertEqual(self.controls(), controls)
        self.assertEqual(self.source_claims(), claims)

    def test_manual_continuation_reuses_automatic_controller_without_new_posts(self):
        self.provider.plans['root-1'] = ['done', 'failed', 'done']
        self.recover()
        controls = self.controls()
        shutil.rmtree(self.output)
        result = fixture.RecoveryTests.recover(self, allowed_error_codes=[])
        self.assertEqual((result['provider_posts'], len(self.provider.posts)), (0, 1))
        self.assertEqual(self.controls(), controls)

    def test_missing_source_claim_cannot_become_a_fresh_submission(self):
        next((self.store.root / 'sources').glob('*.json')).unlink()
        with self.assertRaisesRegex(RecoveryError, 'missing_original_claim'):
            self.recover()
        self.assertEqual(self.provider.polls, [])
        self.assertEqual(self.provider.posts, [])

    def test_corrupt_legacy_policy_stops_before_provider_activity(self):
        self.provider.plans['root-1'] = ['done', 'failed', 'done']
        self.recover()
        shutil.rmtree(self.output)
        path = next((self.store.root / 'recoveries').glob('*.json'))
        row = json.loads(path.read_bytes()); row['policy']['max_children'] = 3
        path.write_text(json.dumps(row))
        polls, posts = len(self.provider.polls), len(self.provider.posts)
        with self.assertRaisesRegex(LedgerError, 'fixed policy'):
            self.recover()
        self.assertEqual((len(self.provider.polls), len(self.provider.posts)), (polls, posts))

    def test_global_time_budget_stops_before_child_and_keeps_cached_success(self):
        self.clock()
        self.provider.plans['root-1'] = ['done', 'failed', 'done']
        cache = ResultCache(fixture.MemoryR2(), 'test')
        base = self.downloader
        def slow(url):
            result = base(url); self.now += 6; return result
        with self.assertRaisesRegex(RecoveryError, 'recovery_time_budget_exhausted'):
            self.recover(total_timeout=5, result_cache=cache, downloader=slow)
        self.assertEqual(self.provider.posts, [])
        self.assertFalse(self.output.exists())
        root = self.originals[0]; binding = root['files'][0]
        lineage = {'batch_id': root['batch_id'], 'batch_key': root['key'],
                   'parent_batch_key': root['key'], 'data_id': binding['id'], 'child_ordinal': 0}
        self.assertIsNotNone(cache.get(binding, lineage))

    def test_context_replay_and_identity_denials_have_no_provider_activity(self):
        for updates in ({'GITHUB_EVENT_NAME': 'pull_request'}, {'GITHUB_REF': 'refs/heads/branch'},
                        {'GITHUB_SHA': ''}, {'GITHUB_ACTIONS': 'false'},
                        {'GITHUB_RUN_ID': '0'}, {'REPLAY_SOURCE_RUN_ID': '123'},
                        {'MINERU_FORBID_NEW_SUBMISSIONS': '1'},
                        {'GITHUB_WORKFLOW_REF': 'owner/repo/other.yml@refs/heads/main'}):
            with self.subTest(updates=updates):
                with self.assertRaisesRegex(RecoveryError, 'daily_context_required'):
                    self.recover(env={**ENV, **updates})
        self.ledger.forbid_new_submissions = True
        with self.assertRaisesRegex(RecoveryError, 'replay_forbidden'):
            self.recover()
        self.assertEqual(self.provider.polls, [])
        self.assertEqual(self.provider.posts, [])


if __name__ == '__main__':
    unittest.main(verbosity=2)
