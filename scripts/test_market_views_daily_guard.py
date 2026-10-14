import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import Mock, patch

import market_views_daily_guard as guard


NOW = datetime(2026, 10, 14, 1, 0, tzinfo=timezone.utc)  # Beijing 09:00
REPOSITORY = 'example/reports'
RUN_ID = '12345'
SOURCE_SHA = 'a' * 40
GUARD_SHA = 'b' * 40
PDF = b'%PDF-1.7\nexact-original\n'


def producer(**updates):
    value = {'id': int(RUN_ID), 'path': guard.DAILY_WORKFLOW, 'head_branch': 'main',
             'event': 'schedule', 'status': 'in_progress', 'head_sha': SOURCE_SHA,
             'repository': {'full_name': REPOSITORY}, 'head_repository': {'full_name': REPOSITORY},
             'created_at': '2026-10-13T18:00:00Z'}
    value.update(updates)
    return value


def rows(date='261013'):
    return [{'name': 'private-source.pdf', 'process_local_path': '/producer/01-private-source.pdf',
             'dropbox_path': f'/zip_backup/{date}/private-source.pdf',
             'content_sha256': hashlib.sha256(PDF).hexdigest()}]


def encoded_rows(date='261013'):
    return json.dumps(rows(date)).encode()


def environment(event='schedule'):
    return {'GITHUB_ACTIONS': 'true', 'GITHUB_EVENT_NAME': event, 'GITHUB_REF': 'refs/heads/main',
            'GITHUB_WORKFLOW_REF': REPOSITORY + '/' + guard.WORKFLOW + '@refs/heads/main',
            'GITHUB_REPOSITORY': REPOSITORY, 'GITHUB_RUN_ID': '98765', 'GITHUB_SHA': GUARD_SHA}


class PublicationDecisionTests(unittest.TestCase):
    def test_beijing_cutoff_uses_calendar_day_and_does_not_wait_for_shards(self):
        before = datetime(2026, 10, 13, 21, 59, tzinfo=timezone.utc)
        cutoff = datetime(2026, 10, 13, 22, 0, tzinfo=timezone.utc)
        self.assertFalse(guard.publication_decision('261013', before, False)['should_build'])
        self.assertTrue(guard.publication_decision('261013', cutoff, False)['should_build'])

    def test_complete_publication_is_idempotent_even_before_cutoff(self):
        decision = guard.publication_decision('261013', NOW, True)
        self.assertEqual(decision, {'should_build': False, 'reason': 'verified_private_publication'})

    def test_acceptance_bypasses_existing_publication_and_cutoff_only(self):
        early = datetime(2026, 10, 13, 20, 0, tzinfo=timezone.utc)
        self.assertTrue(guard.publication_decision('261013', early, True, acceptance_only=True)['should_build'])
        with self.assertRaisesRegex(guard.GuardError, 'stale_or_future'):
            guard.publication_decision('261011', early, True, acceptance_only=True)

    def test_stale_or_future_source_never_reuses_old_publication(self):
        for source in ('261012', '261015'):
            with self.subTest(source=source), self.assertRaisesRegex(guard.GuardError, 'stale_or_future'):
                guard.publication_decision(source, NOW, True)

    def test_forced_fallback_cannot_publish(self):
        with self.assertRaisesRegex(guard.GuardError, 'forced_fallback_requires_acceptance'):
            guard.validate_request('', '', False, True, 'workflow_dispatch')
        guard.validate_request('261013', RUN_ID, True, True, 'workflow_dispatch')

    def test_automatic_event_cannot_inject_manual_source_or_acceptance(self):
        for options in (('261013', '', False, False), ('', '', True, False)):
            with self.assertRaisesRegex(guard.GuardError, 'manual_controls'):
                guard.validate_request(*options, 'workflow_run')


class SourceAuthenticationTests(unittest.TestCase):
    def test_accepts_main_daily_while_its_shards_are_still_running(self):
        self.assertEqual(guard.checked_producer(producer(), RUN_ID, REPOSITORY)['status'], 'in_progress')

    def test_rejects_fork_branch_workflow_sha_and_run_substitution(self):
        for updates in ({'head_repository': {'full_name': 'fork/reports'}}, {'head_branch': 'feature'},
                        {'path': guard.WORKFLOW}, {'head_sha': 'bad'}, {'id': 12}, {'event': 'pull_request'}):
            with self.subTest(updates=updates), self.assertRaises(guard.GuardError):
                guard.checked_producer(producer(**updates), RUN_ID, REPOSITORY)

    def test_guard_must_be_reviewed_main_workflow(self):
        self.assertEqual(guard.require_cloud_main(environment()), REPOSITORY)
        for key, value in (('GITHUB_REF', 'refs/heads/test'), ('GITHUB_EVENT_NAME', 'pull_request'),
                           ('GITHUB_WORKFLOW_REF', REPOSITORY + '/unexpected.yml@refs/heads/main')):
            env = environment()
            env[key] = value
            with self.assertRaises(guard.GuardError):
                guard.require_cloud_main(env)

    def test_manual_acceptance_can_run_exact_branch_while_production_cannot(self):
        env = environment('workflow_dispatch')
        env['GITHUB_REF'] = 'refs/heads/codex/daily-closure'
        env['GITHUB_WORKFLOW_REF'] = REPOSITORY + '/' + guard.WORKFLOW + '@' + env['GITHUB_REF']
        self.assertEqual(guard.require_cloud_main(env, acceptance_only=True), REPOSITORY)
        with self.assertRaises(guard.GuardError):
            guard.require_cloud_main(env)

    def test_manifest_exact_root_date_and_hash_bindings(self):
        self.assertEqual(guard.checked_manifest(encoded_rows(), '261013'), rows())
        self.assertIsNone(guard.checked_manifest(encoded_rows('261014'), '261013'))
        for value in ('/unrelated/261013/private-source.pdf', '/zip_backup/261013/../private-source.pdf'):
            bad = rows()
            bad[0]['dropbox_path'] = value
            with self.assertRaises(guard.GuardError):
                guard.checked_manifest(json.dumps(bad).encode(), '261013')

    def test_manifest_mixed_dates_and_duplicate_sources_rejected(self):
        for bad in (rows() + rows(), rows() + [dict(rows('261014')[0], process_local_path='02-other.pdf')]):
            with self.assertRaises(guard.GuardError):
                guard.checked_manifest(json.dumps(bad).encode(), '261013')

    def test_one_missing_or_corrupt_original_is_recorded_without_losing_good_sources(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            records = rows() + [dict(rows()[0], process_local_path='02-absent.pdf')]
            raw = json.dumps(records).encode()
            (root / guard.MANIFEST).write_bytes(raw)
            (root / '01-private-source.pdf').write_bytes(PDF)
            result = guard.verify_originals(root, raw, records)
            self.assertEqual((result['verified_count'], result['omitted_count']), (1, 1))
            self.assertEqual(result['omissions'][0]['reason'], 'original_missing')
            (root / '02-absent.pdf').write_bytes(b'corrupt')
            result = guard.verify_originals(root, raw, records)
            self.assertEqual(result['omissions'][0]['reason'], 'original_hash_mismatch')

    def test_unselected_extra_originals_are_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / guard.MANIFEST).write_bytes(encoded_rows())
            (root / 'other.pdf').write_bytes(PDF)
            with self.assertRaisesRegex(guard.GuardError, 'inventory_mismatch'):
                guard.verify_originals(root, encoded_rows(), rows())

    def test_legacy_shard_size_requires_explicit_consistent_producer_summaries(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            options = dict(source_run_id=RUN_ID, source_sha=SOURCE_SHA, manifest_sha='a' * 64)
            self.assertEqual(guard.retained_reports_per_shard(root, root / 'available', **options), 0)
            for index in range(2):
                shard = root / f'shard_{index}'
                shard.mkdir()
                (shard / 'shard_run_summary.md').write_text('- Reports per shard: 3\n')
            self.assertEqual(guard.retained_reports_per_shard(root, root / 'available', **options), 3)
            (root / 'shard_1/shard_run_summary.md').write_text('- Reports per shard: 5\n')
            self.assertEqual(guard.retained_reports_per_shard(root, root / 'available', **options), 0)

    def test_optional_handoff_read_failure_clears_partial_download_and_preserves_fallback(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            def fail(prefix, destination, **kwargs):
                (destination / 'partial.txt').write_text('incomplete')
                raise RuntimeError('unavailable')
            with patch('private_workflow_handoff.list_keys', side_effect=lambda prefix, **kwargs: [prefix + '/shard_0.tar.gz']), \
                    patch('private_workflow_handoff.download_shards', side_effect=fail):
                result = guard.restore_handoffs(Mock(), 'bucket', RUN_ID, '261013', root)
            self.assertEqual(result['handoff_restore_status'], 'unavailable_original_fallback_required')
            self.assertEqual(result['available_restore_status'], 'unavailable_original_fallback_required')
            self.assertFalse(list(root.rglob('partial.txt')))


class GithubRecoveryTests(unittest.TestCase):
    def test_read_timeout_retries_bounded_and_never_becomes_no_source(self):
        runner = Mock(side_effect=subprocess.TimeoutExpired('gh', 60))
        sleep = Mock()
        github = guard.Github(REPOSITORY, runner=runner, sleep=sleep)
        with self.assertRaisesRegex(guard.GuardError, 'unavailable_after_retries'):
            github.api('actions/runs/12345')
        self.assertEqual(runner.call_count, 3)
        self.assertEqual([item.args[0] for item in sleep.call_args_list], [1, 2])

    def test_transient_failure_recovers_exact_response(self):
        runner = Mock(side_effect=[subprocess.CompletedProcess([], 1, b'', b'timeout'),
                                   subprocess.CompletedProcess([], 0, b'{"id":12345}', b'')])
        github = guard.Github(REPOSITORY, runner=runner, sleep=Mock())
        self.assertEqual(github.api('actions/runs/12345')['id'], 12345)

    def test_artifact_absence_requires_a_successful_well_formed_listing(self):
        github = guard.Github(REPOSITORY)
        with patch.object(github, 'api', return_value={'artifacts': [], 'total_count': 0}):
            self.assertFalse(github.has_artifact(RUN_ID, 'selected-macro-pdfs-12345'))
        with patch.object(github, 'api', return_value={}), self.assertRaises(guard.GuardError):
            github.has_artifact(RUN_ID, 'selected-macro-pdfs-12345')

    def test_latest_matching_manifest_selected_without_terminal_run_gate(self):
        github = Mock()
        github.candidates.return_value = [producer(id=22345), producer()]
        github.has_artifact.return_value = True
        def download(run_id, name, destination):
            destination.mkdir(parents=True)
            (destination / guard.MANIFEST).write_bytes(encoded_rows('261014' if run_id == '22345' else '261013'))
        github.download.side_effect = download
        with tempfile.TemporaryDirectory() as temporary:
            chosen, raw, selected = guard.discover_source(github, '261013', Path(temporary), NOW)
        self.assertEqual(chosen['id'], int(RUN_ID))
        self.assertEqual(selected, rows())

    def test_automatic_empty_or_bad_manifest_does_not_mask_valid_same_day_source(self):
        for bad in (b'[]', b'{bad json', json.dumps([{'dropbox_path': '/unbound/261013/source.pdf'}]).encode()):
            with self.subTest(bad=bad), tempfile.TemporaryDirectory() as temporary:
                github = Mock()
                github.candidates.return_value = [producer(id=22345), producer()]
                github.has_artifact.return_value = True
                def download(run_id, name, destination):
                    destination.mkdir(parents=True)
                    (destination / guard.MANIFEST).write_bytes(bad if run_id == '22345' else encoded_rows())
                github.download.side_effect = download
                diagnostics = {}
                chosen, _, selected = guard.discover_source(github, '261013', Path(temporary), NOW,
                                                             diagnostics=diagnostics)
            self.assertEqual(chosen['id'], int(RUN_ID))
            self.assertEqual(selected, rows())
            self.assertEqual(diagnostics, {'candidate_manifest_invalid': 1})

    def test_explicit_empty_manifest_remains_a_strict_failure(self):
        github = Mock()
        github.run.return_value = producer()
        github.has_artifact.return_value = True
        def download(run_id, name, destination):
            destination.mkdir(parents=True)
            (destination / guard.MANIFEST).write_bytes(b'[]')
        github.download.side_effect = download
        with tempfile.TemporaryDirectory() as temporary, self.assertRaisesRegex(guard.GuardError, 'manifest_count'):
            guard.discover_source(github, '261013', Path(temporary), NOW, RUN_ID)

    def test_fallback_date_prefers_newest_source_date_over_newest_run(self):
        github = Mock()
        github.candidates.return_value = [producer(id=22345), producer()]
        github.has_artifact.return_value = True
        def download(run_id, name, destination):
            destination.mkdir(parents=True)
            (destination / guard.MANIFEST).write_bytes(encoded_rows('261013' if run_id == '22345' else '261014'))
        github.download.side_effect = download
        with tempfile.TemporaryDirectory() as temporary:
            chosen, _, selected = guard.discover_source(github, None, Path(temporary), NOW)
        self.assertEqual(chosen['id'], int(RUN_ID))
        self.assertEqual(selected, rows('261014'))

    def test_fallback_date_never_uses_stale_or_future_manifests(self):
        for date in ('261012', '261015'):
            with self.subTest(date=date), tempfile.TemporaryDirectory() as temporary:
                github = Mock()
                github.candidates.return_value = [producer()]
                github.has_artifact.return_value = True
                def download(run_id, name, destination):
                    destination.mkdir(parents=True)
                    (destination / guard.MANIFEST).write_bytes(encoded_rows(date))
                github.download.side_effect = download
                diagnostics = {}
                result = guard.discover_source(github, None, Path(temporary), NOW, diagnostics=diagnostics)
            self.assertEqual(result, (None, None, None))
            self.assertEqual(diagnostics, {'candidate_manifest_stale_or_future': 1})


class DateDiscoveryTests(unittest.TestCase):
    def test_only_failed_external_reads_receive_unavailable_category(self):
        with patch('download_dropbox_latest_pdfs.dropbox_access_token', side_effect=RuntimeError('token unavailable')):
            with self.assertRaises(guard.DropboxUnavailable):
                guard.latest_dropbox_date(NOW)
        for date, requested in (('261012', ''), ('261015', ''), ('261014', '261013')):
            with self.subTest(date=date, requested=requested), \
                    patch('download_dropbox_latest_pdfs.dropbox_access_token', return_value='token'), \
                    patch('download_dropbox_latest_pdfs.list_folder', return_value=[{'.tag': 'folder', 'name': date}]):
                with self.assertRaises(guard.GuardError) as rejected:
                    guard.latest_dropbox_date(NOW, requested)
                self.assertNotIsInstance(rejected.exception, guard.DropboxUnavailable)


class BoundedOriginalDownloadTests(unittest.TestCase):
    def test_expired_intake_budget_makes_no_request(self):
        request = Mock()
        with tempfile.TemporaryDirectory() as temporary, self.assertRaisesRegex(guard.GuardError, 'deadline'):
            guard.download_original_bounded('test-token', '/zip_backup/261013/source.pdf',
                Path(temporary) / 'source.pdf', deadline=1, clock=lambda: 2, request=request)
        request.assert_not_called()

    def test_transient_read_failure_has_only_two_attempts(self):
        import requests
        request = Mock(side_effect=requests.Timeout())
        with tempfile.TemporaryDirectory() as temporary, self.assertRaisesRegex(guard.GuardError, 'unavailable'):
            guard.download_original_bounded('test-token', '/zip_backup/261013/source.pdf',
                Path(temporary) / 'source.pdf', deadline=200, clock=lambda: 1, request=request, sleep=Mock())
        self.assertEqual(request.call_count, 2)
        self.assertFalse(request.call_args.kwargs['allow_redirects'])

    def test_fresh_download_failures_and_malformed_pdf_preserve_healthy_sources(self):
        import fitz
        from market_views_partial_sources import _unavailable, read_selection
        document = fitz.open()
        document.new_page().insert_text((40, 40), 'Market research evidence')
        valid = document.tobytes()
        document.close()
        entries = [{'.tag': 'file', 'name': 'same.pdf', 'path_lower': f'/zip_backup/261013/{index}/same.pdf'}
                   for index in range(3)]
        def download(token, path, target, **kwargs):
            if '/0/' in path:
                raise TimeoutError()
            target.write_bytes(b'not a PDF' if '/1/' in path else valid)
        with tempfile.TemporaryDirectory() as temporary, \
                patch('download_dropbox_latest_pdfs.dropbox_access_token', return_value='token'), \
                patch('download_dropbox_latest_pdfs.list_folder', return_value=entries), \
                patch.object(guard, 'download_original_bounded', side_effect=download):
            root = Path(temporary) / 'originals'
            raw, selected, unavailable = guard.download_fresh_originals('261013', root)
            self.assertEqual(len(selected), 1)
            self.assertEqual(len(unavailable), 2)
            self.assertEqual(len({row['source_pdf'] for row in unavailable}), 2)
            self.assertEqual({row['reason'] for row in unavailable},
                             {'original_download_unavailable', 'original_invalid_pdf'})
            self.assertTrue(all(set(row) == {'source_pdf', 'reason'} for row in unavailable))
            _, bindings = read_selection(root / guard.MANIFEST)
            self.assertEqual(_unavailable(bindings, unavailable), unavailable)
            self.assertEqual(guard.verify_originals(root, raw, selected)['verified_count'], 1)


class PreparationTests(unittest.TestCase):
    def prepare(self, root, publication_check, **kwargs):
        return guard.prepare(root, now=NOW, repository=REPOSITORY, env=environment(), client=Mock(),
                             bucket='test', discover_date=lambda now, requested: '261013',
                             publication_check=publication_check, **kwargs)

    def test_completed_issue_never_downloads_sources_or_calls_github(self):
        with tempfile.TemporaryDirectory() as temporary, patch.object(guard, 'discover_source') as source:
            result = self.prepare(Path(temporary), Mock(return_value=True))
        self.assertFalse(result['should_build'])
        source.assert_not_called()

    def test_r2_unavailable_does_not_authorize_a_rebuild(self):
        with tempfile.TemporaryDirectory() as temporary, patch.object(guard, 'discover_source') as source:
            with self.assertRaisesRegex(RuntimeError, 'storage unavailable'):
                self.prepare(Path(temporary), Mock(side_effect=RuntimeError('storage unavailable')))
        source.assert_not_called()

    def test_missing_issue_keeps_exact_producer_and_original_lineage(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            def restore(github, source, raw, selected, destination):
                destination.mkdir()
                (destination / guard.MANIFEST).write_bytes(raw)
                (destination / '01-private-source.pdf').write_bytes(PDF)
                return True
            retained = {'handoff_dir': str(root / 'handoff'), 'available_dir': str(root / 'available')}
            with patch.object(guard, 'discover_source', return_value=(producer(), encoded_rows(), rows())), \
                    patch.object(guard, 'restore_originals', side_effect=restore), \
                    patch.object(guard, 'restore_handoffs', return_value=retained):
                result = self.prepare(root, Mock(return_value=False))
            context = json.loads(Path(result['context_path']).read_text())
        self.assertTrue(result['should_build'])
        self.assertEqual(context['source_execution_sha'], SOURCE_SHA)
        self.assertEqual(context['selected_manifest_sha256'], hashlib.sha256(encoded_rows()).hexdigest())
        self.assertEqual(context['source_run_id'], RUN_ID)
        self.assertEqual(context['original_validation']['verified_count'], 1)

    def test_metadata_outage_uses_new_dropbox_lineage_without_mixing_old_handoffs(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            def fresh(date_folder, destination):
                destination.mkdir()
                (destination / guard.MANIFEST).write_bytes(encoded_rows())
                (destination / '01-private-source.pdf').write_bytes(PDF)
                return encoded_rows(), rows(), []
            with patch.object(guard, 'discover_source', side_effect=guard.GuardError('github_read_unavailable_after_retries')), \
                    patch.object(guard, 'download_fresh_originals', side_effect=fresh), \
                    patch.object(guard, 'restore_handoffs', return_value={'handoff_dir': '', 'available_dir': ''}) as retained:
                result = self.prepare(root, Mock(return_value=False))
            context = json.loads(Path(result['context_path']).read_text())
            self.assertEqual(context['source_run_id'], environment()['GITHUB_RUN_ID'])
        self.assertEqual(context['source_kind'], 'fresh-dropbox')
        self.assertEqual(context['source_execution_sha'], GUARD_SHA)
        self.assertEqual(retained.call_args.args[2], '')

    def test_dropbox_outage_uses_authenticated_daily_manifest_date_for_noop(self):
        with tempfile.TemporaryDirectory() as temporary, \
                patch.object(guard, 'discover_source', return_value=(producer(), encoded_rows(), rows())) as sources, \
                patch.object(guard, 'restore_originals') as restore:
            result = guard.prepare(Path(temporary), now=NOW, repository=REPOSITORY, env=environment(),
                client=Mock(), bucket='test',
                discover_date=Mock(side_effect=guard.DropboxUnavailable('dropbox_discovery_unavailable')),
                publication_check=Mock(return_value=True))
        self.assertFalse(result['should_build'])
        self.assertEqual(result['date_folder'], '261013')
        self.assertEqual(result['date_discovery_authority'], 'authenticated-daily-manifest-dropbox-unavailable')
        self.assertIsNone(sources.call_args.args[1])
        restore.assert_not_called()

    def test_exact_manual_source_can_recover_during_dropbox_outage(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            def restore(github, source, raw, selected, destination):
                destination.mkdir()
                (destination / guard.MANIFEST).write_bytes(raw)
                (destination / '01-private-source.pdf').write_bytes(PDF)
                return True
            with patch.object(guard, 'discover_source', return_value=(producer(), encoded_rows(), rows())) as sources, \
                    patch.object(guard, 'restore_originals', side_effect=restore), \
                    patch.object(guard, 'restore_handoffs', return_value={'handoff_dir': '', 'available_dir': ''}):
                result = guard.prepare(root, now=NOW, repository=REPOSITORY, env=environment('workflow_dispatch'),
                    client=Mock(), bucket='test', date_folder='261013', source_run_id=RUN_ID,
                    acceptance_only=True, discover_date=Mock(side_effect=guard.DropboxUnavailable('unavailable')),
                    publication_check=Mock(return_value=True))
                context = json.loads(Path(result['context_path']).read_text())
        self.assertTrue(result['should_build'])
        self.assertEqual(sources.call_count, 1)
        self.assertEqual(sources.call_args.args[1], '261013')
        self.assertEqual(sources.call_args.args[4], RUN_ID)
        self.assertEqual(context['source_run_id'], RUN_ID)
        self.assertEqual(context['date_discovery_authority'], 'authenticated-daily-manifest-dropbox-unavailable')

    def test_known_bad_latest_date_never_falls_back_to_previous_daily(self):
        for reason in ('latest_source_is_stale_or_future', 'requested_date_is_not_latest_dropbox_batch'):
            with self.subTest(reason=reason), tempfile.TemporaryDirectory() as temporary, \
                    patch.object(guard, 'discover_source') as sources:
                with self.assertRaisesRegex(guard.GuardError, reason):
                    guard.prepare(Path(temporary), now=NOW, repository=REPOSITORY, env=environment(),
                        client=Mock(), bucket='test', discover_date=Mock(side_effect=guard.GuardError(reason)),
                        publication_check=Mock(return_value=True))
                sources.assert_not_called()

    def test_outage_without_fresh_daily_cannot_fabricate_current_date(self):
        with tempfile.TemporaryDirectory() as temporary, \
                patch.object(guard, 'discover_source', return_value=(None, None, None)), \
                patch.object(guard, 'download_fresh_originals') as fresh:
            with self.assertRaisesRegex(guard.GuardError, 'no_fresh_daily_manifest'):
                guard.prepare(Path(temporary), now=NOW, repository=REPOSITORY, env=environment(),
                    client=Mock(), bucket='test', discover_date=Mock(side_effect=guard.DropboxUnavailable('unavailable')),
                    publication_check=Mock(return_value=False))
        fresh.assert_not_called()

    def test_all_automatic_bad_manifests_still_attempt_independent_fresh_dropbox(self):
        github = Mock()
        github.candidates.return_value = [producer()]
        github.has_artifact.return_value = True
        def download(run_id, name, destination):
            destination.mkdir(parents=True)
            (destination / guard.MANIFEST).write_bytes(b'[]')
        github.download.side_effect = download
        def fresh(date_folder, destination):
            destination.mkdir()
            (destination / guard.MANIFEST).write_bytes(encoded_rows())
            (destination / '01-private-source.pdf').write_bytes(PDF)
            return encoded_rows(), rows(), []
        with tempfile.TemporaryDirectory() as temporary, \
                patch.object(guard, 'download_fresh_originals', side_effect=fresh) as fallback, \
                patch.object(guard, 'restore_handoffs', return_value={'handoff_dir': '', 'available_dir': ''}):
            result = self.prepare(Path(temporary), Mock(return_value=False), github=github)
            context = json.loads(Path(result['context_path']).read_text())
        fallback.assert_called_once()
        self.assertEqual(context['source_kind'], 'fresh-dropbox')
        self.assertEqual(context['source_run_id'], environment()['GITHUB_RUN_ID'])
        self.assertEqual(context['source_discovery_omissions'], {'candidate_manifest_invalid': 1})


class WorkflowContractTests(unittest.TestCase):
    def test_independent_schedule_exact_triggers_and_shared_publication_lock(self):
        text = (Path(__file__).resolve().parents[1] / '.github/workflows/market-views-daily-guard.yml').read_text()
        self.assertIn("cron: '17 * * * *'", text)
        self.assertIn('workflow_run:', text)
        self.assertIn("types: [completed]", text)
        self.assertIn("'market-views-daily-pdf'", text)
        self.assertIn('cancel-in-progress: false', text)
        self.assertIn("inputs.acceptance_only == true", text)
        self.assertNotIn('gh workflow run', text)
        self.assertNotIn('send_portal_ops_alert', text)
        self.assertNotIn('DEEPSEEK_API_KEY:', text)
        self.assertNotIn('MINER_U:', text)
        self.assertIn('scripts/inspect_market_views_live.py --dates', text)


if __name__ == '__main__':
    unittest.main()
