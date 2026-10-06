#!/usr/bin/env python3
"""Exercise the complete source adapter with real ledger/cache/receipt code."""
import json
import io
from contextlib import redirect_stdout
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

    def test_only_failed_members_submitted_after_their_original_success_zips_are_saved(self):
        self.provider.plans['root-1'] = ['done', 'failed', 'failed']
        before = self.source_claims()
        receipt = self.recover(result_cache=ResultCache(fixture.MemoryR2(), 'test'))
        self.assertEqual((receipt['report_count'], receipt['provider_posts']), (7, 1))
        self.assertEqual([item['id'] for item in self.provider.posts[0]],
                         [item['id'] for item in self.originals[0]['files'][1:]])
        first_post = self.provider.events.index('post')
        self.assertEqual(self.provider.events[:first_post].count('zip'), 1)
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

    def test_three_children_is_lifetime_limit_and_later_batch_still_cached(self):
        self.provider.plans.update({'root-1': ['done', 'failed', 'done'],
                                    'child-1': ['failed'], 'child-2': ['failed'], 'child-3': ['failed']})
        cache = ResultCache(fixture.MemoryR2(), 'test')
        captured = io.StringIO()
        with redirect_stdout(captured):
            for _ in range(2):
                with self.assertRaisesRegex(RecoveryError, 'recovery_task_incomplete'):
                    self.recover(result_cache=cache)
                self.assertFalse(self.output.exists())
        self.assertEqual([len(items) for items in self.provider.posts], [1, 1, 1])
        self.assertEqual(len(json.loads(next(iter(self.controls().values())))['children']), 3)
        self.assertIn('root-2', self.provider.polls)
        root = self.originals[1]
        for binding in root['files']:
            lineage = {'batch_id': root['batch_id'], 'batch_key': root['key'],
                       'parent_batch_key': root['key'], 'data_id': binding['id'], 'child_ordinal': 0}
            self.assertIsNotNone(cache.get(binding, lineage))
        events = [json.loads(line) for line in captured.getvalue().splitlines()]
        exhausted = next(row for event in events for row in event['sources'] if row['status'] == 'retry_exhausted')
        self.assertEqual((exhausted['source_ordinal'], exhausted['reserved_retry_count']), (3, 3))
        self.assertEqual([event['batch_ordinal'] for event in events], [1, 2, 1, 2])
        for secret in ('report-', 'results.invalid', 'private-token', 'full_zip_url'):
            self.assertNotIn(secret, captured.getvalue())

    def test_pending_task_only_gets_without_reservation_or_post(self):
        self.clock()
        self.provider.plans['root-1'] = ['done', 'running', 'done']
        claims = self.source_claims()
        cache = ResultCache(fixture.MemoryR2(), 'test')
        with self.assertRaisesRegex(RecoveryError, 'recovery_task_incomplete'):
            self.recover(total_timeout=3, result_cache=cache)
        self.assertLess(self.now, 3)
        self.assertGreater(len(self.provider.polls), 1)
        self.assertIn('root-2', self.provider.polls)
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
        # Daily appends its separately authenticated third-retry extension;
        # every prior policy field, reservation and proof remains unchanged.
        after = self.controls()
        self.assertEqual(set(after), set(controls))
        for name, previous in controls.items():
            prior, current = json.loads(previous), json.loads(after[name])
            self.assertEqual({key: current[key] for key in prior}, prior)
            self.assertEqual(set(current) - set(prior), {'daily_retry_extension'})
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
        with self.assertRaisesRegex(RecoveryError, 'recovery_task_incomplete'):
            self.recover(total_timeout=5, result_cache=cache, downloader=slow)
        self.assertEqual(self.provider.posts, [])
        self.assertFalse(self.output.exists())
        root = self.originals[0]; binding = root['files'][0]
        lineage = {'batch_id': root['batch_id'], 'batch_key': root['key'],
                   'parent_batch_key': root['key'], 'data_id': binding['id'], 'child_ordinal': 0}
        self.assertIsNotNone(cache.get(binding, lineage))

    def test_slow_zip_stops_only_its_batch_and_reserves_time_for_later_batch(self):
        self.clock()
        cache = ResultCache(fixture.MemoryR2(), 'test')
        fetched = []
        def slow_first(url):
            fetched.append(url)
            result = self.downloader(url)
            if len(fetched) == 1:
                self.now += 6
            return result
        with self.assertRaisesRegex(RecoveryError, 'recovery_task_incomplete'):
            self.recover(total_timeout=10, result_cache=cache, downloader=slow_first)
        # Batch 1 owns five seconds. Its first verified ZIP is saved even when
        # that single call overruns; no more batch-1 downloads use batch 2's time.
        self.assertEqual(sum('/root-1/' in url for url in fetched), 1)
        self.assertEqual(sum('/root-2/' in url for url in fetched), 4)
        self.assertIn('root-2', self.provider.polls)
        self.assertEqual(self.provider.posts, [])
        first = self.originals[0]
        binding = first['files'][0]
        self.assertIsNotNone(cache.get(binding, {'batch_id': first['batch_id'], 'batch_key': first['key'],
            'parent_batch_key': first['key'], 'data_id': binding['id'], 'child_ordinal': 0}))

    def test_third_retry_success_has_a_valid_complete_receipt_and_manual_resume(self):
        self.provider.plans.update({'root-1': ['done', 'failed', 'done'],
                                    'child-1': ['failed'], 'child-2': ['failed'], 'child-3': ['done']})
        receipt = self.recover()
        self.assertEqual(receipt['provider_posts'], 3)
        self.assertEqual(sum(report['task']['child_ordinal'] == 3 for report in self.validate()['reports']), 1)
        shutil.rmtree(self.output)
        resumed = fixture.RecoveryTests.recover(self, allowed_error_codes=[])
        self.assertEqual(resumed['provider_posts'], 0)
        self.assertEqual(len(self.provider.posts), 3)

    def test_third_child_expired_zip_defers_but_later_batch_is_still_cached(self):
        from consume_legacy_mineru import NetworkStop
        self.provider.plans.update({'root-1': ['done', 'failed', 'done'],
                                    'child-1': ['failed'], 'child-2': ['failed'], 'child-3': ['done']})
        cache = ResultCache(fixture.MemoryR2(), 'test')
        def download(url):
            if '/child-3/' in url:
                raise NetworkStop('tls_certificate_expired')
            return self.downloader(url)
        with self.assertRaisesRegex(RecoveryError, 'ledger_child_result_tls_certificate_expired'):
            self.recover(result_cache=cache, downloader=download)
        self.assertEqual(len(self.provider.posts), 3)
        root = self.originals[1]
        binding = root['files'][0]
        self.assertIsNotNone(cache.get(binding, {'batch_id': root['batch_id'], 'batch_key': root['key'],
            'parent_batch_key': root['key'], 'data_id': binding['id'], 'child_ordinal': 0}))
        self.assertFalse(self.output.exists())

    def test_ambiguous_child_is_not_resubmitted_and_later_batch_keeps_progress(self):
        self.provider.plans['root-1'] = ['done', 'failed', 'done']
        original_submit = self.provider.submit
        def unknown(*args):
            original_submit(*args)
            raise TimeoutError('provider response lost')
        self.provider.submit = unknown
        cache = ResultCache(fixture.MemoryR2(), 'test')
        for _ in range(2):
            with self.assertRaisesRegex(RecoveryError, 'recovery_task_incomplete'):
                self.recover(result_cache=cache)
        self.assertEqual(len(self.provider.posts), 1)
        self.assertGreaterEqual(self.provider.polls.count('root-2'), 2)
        self.assertFalse(self.output.exists())

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
