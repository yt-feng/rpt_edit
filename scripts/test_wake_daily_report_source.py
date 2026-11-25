"""Exercise missed schedules, late originals, duplicate wakes and lost POSTs."""
import copy
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import unittest
from urllib.parse import parse_qs, urlsplit
from unittest.mock import patch

import yaml
import wake_daily_report_source as wakeup

NOW = datetime(2026, 11, 10, 0, 45, tzinfo=timezone.utc)
DAY = '261109'
REPO = 'owner/repo'
RECEIPT_INPUTS = {'date_folder': DAY, 'upstream_run_id': '42', 'pdf_count': '2',
                  'manifest_sha256': '46447e144cddd66d4c0c80102ae54e164cdfbd6ba3728f0c93c8dd9cdd50622d'}
RECEIPT = wakeup.parse_source_receipt({'inputs': RECEIPT_INPUTS})


def run(identity=1, *, day=DAY, status='completed', conclusion='success', title=None):
    return {'id': identity, 'run_attempt': 1, 'path': wakeup.WORKFLOW, 'head_branch': 'main',
            'event': 'workflow_dispatch', 'status': status, 'conclusion': conclusion,
            'display_title': title or wakeup.title_for(day),
            'repository': {'full_name': REPO}, 'head_repository': {'full_name': REPO}}


class GitHub:
    repository = REPO

    def __init__(self, rows=()):
        self.rows, self.calls, self.artifacts, self.jobs = copy.deepcopy(list(rows)), [], {}, {}

    def api(self, path):
        self.calls.append(path)
        if '/runs?' in path:
            status = parse_qs(urlsplit(path).query).get('status', [None])[0]
            rows = [row for row in self.rows if not status or row['status'] == status]
            page = int(parse_qs(urlsplit(path).query).get('page', ['1'])[0])
            return {'total_count': len(rows), 'workflow_runs': copy.deepcopy(rows[(page-1)*100:page*100])}
        identity = int(path.split('/')[2])
        if '/artifacts?' in path:
            rows = self.artifacts.get(identity, [])
            page = int(parse_qs(urlsplit(path).query).get('page', ['1'])[0])
            indexed = [{'id': index + 1, **row} for index, row in enumerate(rows)]
            return {'total_count': len(rows), 'artifacts': copy.deepcopy(indexed[(page-1)*100:page*100])}
        rows = self.jobs.get(identity, [])
        return {'total_count': len(rows), 'jobs': copy.deepcopy(rows)}


class WakeTests(unittest.TestCase):
    def source(self, now):
        self.assertEqual(now, NOW)
        return {'state': 'ready', 'date_folder': DAY, 'pdf_count': 52}

    def wake(self, github, submit=None):
        return wakeup.wake(github, NOW, source_reader=self.source,
                           submit=submit or self.fail, sleep=lambda _: None)

    def test_missed_schedule_starts_exact_batch_then_every_later_wake_reuses_it(self):
        github, submissions = GitHub(), []
        def submit(api, day):
            submissions.append(day)
            api.rows.append(run(2, status='queued', conclusion=None))
            return True
        self.assertEqual(self.wake(github, submit)['run_id'], 2)
        for status, conclusion in [('queued', None), ('pending', None), ('in_progress', None),
                                   ('completed', 'success'), ('completed', 'failure'), ('completed', 'cancelled')]:
            github.rows[0].update(status=status, conclusion=conclusion)
            self.assertIn(self.wake(github)['state'], {'daily_active', 'batch_already_attempted'})
        self.assertEqual(submissions, [DAY])

    def test_previous_batches_do_not_consume_new_day(self):
        github = GitHub([run(day='261108')])
        def submit(api, day):
            api.rows.append(run(2))
            return True
        self.assertEqual(self.wake(github, submit)['state'], 'dispatched')

    def test_legacy_35_article_run_is_identified_by_date_bound_artifacts(self):
        github = GitHub([run(title='Daily report articles and translations')])
        github.artifacts[1] = [{'name': 'xhs-notes-wechat-drafts-261109-1-attempt-1'}]
        self.assertEqual(self.wake(github)['state'], 'batch_already_attempted')

    def test_source_marker_alone_consumes_attempt_even_if_classification_later_fails(self):
        github = GitHub([run(title='Daily report articles and translations [latest]', conclusion='failure')])
        github.artifacts[1] = [{'name': 'daily-source-batch-261109-1'}]
        self.assertEqual(self.wake(github)['state'], 'batch_already_attempted')

    def test_full_batch_artifacts_can_span_pages_without_triggering_duplicate_generation(self):
        github = GitHub([run(title='Daily report articles and translations [latest]')])
        github.artifacts[1] = [{'name': 'usage-' + str(index)} for index in range(140)]
        github.artifacts[1].append({'name': 'daily-source-batch-261109-1'})
        self.assertEqual(self.wake(github)['state'], 'batch_already_attempted')
        self.assertEqual(sum('/artifacts?' in path for path in github.calls), 2)

    def test_changing_or_repeated_artifact_pages_never_authorize_dispatch(self):
        for corruption in ('count', 'duplicate'):
            github = GitHub([run(title='Daily report articles and translations [latest]')])
            github.artifacts[1] = [{'name': 'usage-' + str(index)} for index in range(140)]
            original = github.api
            def request(path):
                result = original(path)
                if '/artifacts?' in path and 'page=2' in path:
                    if corruption == 'count':
                        result['total_count'] += 1
                    else:
                        result['artifacts'][0]['id'] = 1
                return result
            with self.subTest(corruption=corruption), patch.object(github, 'api', side_effect=request):
                with self.assertRaisesRegex(ValueError, 'daily_artifact_inventory_incomplete'):
                    self.wake(github)

    def test_unproven_legacy_progress_or_incomplete_inventories_never_dispatch(self):
        github = GitHub([run(title='Daily report articles and translations')])
        with self.assertRaisesRegex(ValueError, 'daily_job_identity_invalid'):
            self.wake(github)
        with patch.object(github, 'api', return_value={'total_count': 101, 'workflow_runs': []}):
            with self.assertRaisesRegex(ValueError, 'daily_run_inventory_incomplete'):
                self.wake(github)

    def test_cancelled_legacy_upload_uses_its_retained_selection_manifest(self):
        github = GitHub([run(title='Daily report articles and translations', conclusion='cancelled')])
        github.artifacts[1] = [{'name': 'selected-macro-manifest-1', 'expired': False}]

        def download(command, **kwargs):
            self.assertEqual(command[:4], ['gh', 'run', 'download', '1'])
            self.assertIn(REPO, command)
            directory = Path(command[command.index('--dir') + 1])
            (directory / 'selected_to_process_manifest.json').write_text(json.dumps([
                {'dropbox_path': '/zip_backup/261108/research.pdf'},
                {'dropbox_path': '/zip_backup/261108/nested/another.PDF'},
            ]))
            return subprocess.CompletedProcess(command, 0)

        def submit(api, day):
            api.rows.append(run(2))
            return True

        with patch.object(wakeup.subprocess, 'run', side_effect=download) as command:
            self.assertEqual(self.wake(github, submit)['state'], 'dispatched')
            command.assert_called_once()
        with patch.object(wakeup, 'selected_manifest_date', return_value=wakeup.parse_date_folder(DAY)):
            github.rows = github.rows[:1]
            self.assertEqual(self.wake(github)['state'], 'batch_already_attempted')

    def test_unavailable_or_duplicate_legacy_manifests_never_dispatch(self):
        for artifacts in ([{'name': 'selected-macro-manifest-1', 'expired': True}],
                          [{'name': 'selected-macro-manifest-1', 'expired': False}] * 2):
            github = GitHub([run(title='Daily report articles and translations', conclusion='cancelled')])
            github.artifacts[1] = artifacts
            with self.subTest(artifacts=artifacts), patch.object(wakeup, 'selected_manifest_date') as read:
                with self.assertRaisesRegex(ValueError, 'daily_selection_manifest_unavailable'):
                    self.wake(github)
                read.assert_not_called()

    def test_malformed_or_mixed_legacy_source_paths_never_authorize_dispatch(self):
        for rows in ([], [{}], [{'dropbox_path': '/different/261109/report.pdf'}],
                     [{'dropbox_path': '/zip_backup/261109/../report.pdf'}],
                     [{'dropbox_path': '/zip_backup/261108/report.pdf'},
                      {'dropbox_path': '/zip_backup/261109/report.pdf'}]):
            def download(command, **kwargs):
                directory = Path(command[command.index('--dir') + 1])
                (directory / 'selected_to_process_manifest.json').write_text(json.dumps(rows))
                return subprocess.CompletedProcess(command, 0)
            with self.subTest(rows=rows), patch.object(wakeup.subprocess, 'run', side_effect=download):
                with self.assertRaises(ValueError):
                    wakeup.selected_manifest_date(GitHub(), 1)

    def test_legacy_manifest_download_failure_is_not_treated_as_an_unattempted_batch(self):
        github = GitHub([run(title='Daily report articles and translations', conclusion='cancelled')])
        github.artifacts[1] = [{'name': 'selected-macro-manifest-1', 'expired': False}]
        with patch.object(wakeup.subprocess, 'run', return_value=subprocess.CompletedProcess([], 1)):
            with self.assertRaisesRegex(ValueError, 'daily_selection_manifest_read_failed'):
                self.wake(github)

    def test_failure_before_selection_can_recover_when_originals_arrive(self):
        github = GitHub([run(title='Daily report articles and translations', conclusion='failure')])
        github.jobs[1] = [{'id': 10, 'run_id': 1, 'name': 'select-macro-reports', 'steps': [
            {'name': 'Download PDFs from latest Dropbox date folder', 'conclusion': 'failure'},
            {'name': 'Select reports with DeepSeek', 'conclusion': 'skipped'}]}]
        def submit(api, day):
            api.rows.append(run(2))
            return True
        self.assertEqual(self.wake(github, submit)['state'], 'dispatched')
        github.rows.pop()
        github.jobs[1][0]['steps'][1]['conclusion'] = 'failure'
        with self.assertRaisesRegex(ValueError, 'daily_source_identity_unproven'):
            self.wake(github)

    def test_post_accepted_after_timeout_is_found_without_another_post(self):
        github, submitted = GitHub(), []
        def submit(api, day):
            submitted.append(day)
            api.rows.append(run(2))
            raise subprocess.TimeoutExpired('gh', 35)
        self.assertEqual(self.wake(github, submit)['state'], 'dispatched')
        self.assertEqual(submitted, [DAY])

    def test_unresolved_post_is_not_repeated(self):
        submitted = []
        with self.assertRaisesRegex(ValueError, 'daily_dispatch_outcome_unknown'):
            self.wake(GitHub(), lambda api, day: submitted.append(day))
        self.assertEqual(submitted, [DAY])

    def test_active_run_is_checked_again_before_post(self):
        github = GitHub()
        with patch.object(wakeup, 'active_run', side_effect=[None, 90]):
            self.assertEqual(self.wake(github), {'state': 'daily_active', 'run_id': 90})

    def test_before_daily_start_and_unready_sources_never_dispatch(self):
        github = GitHub()
        early = datetime(2026, 11, 9, 17, 59, tzinfo=timezone.utc)
        self.assertEqual(wakeup.wake(github, early)['state'], 'before_daily_start')
        self.assertEqual(github.calls, [])
        for state in ('waiting_for_fresh_source', 'source_empty', 'source_still_arriving'):
            result = wakeup.wake(github, NOW, source_reader=lambda _: {'state': state}, submit=self.fail)
            self.assertEqual(result['state'], state)

    def test_active_run_skips_dropbox_and_foreign_run_never_authorizes_dispatch(self):
        github = GitHub([run(status='in_progress')])
        with patch.object(wakeup, 'read_source', side_effect=AssertionError):
            self.assertEqual(self.wake(github)['state'], 'daily_active')
        github.rows[0]['head_repository']['full_name'] = 'foreign/repo'
        with self.assertRaisesRegex(ValueError, 'daily_run_identity_invalid'):
            self.wake(github)

    def test_trusted_active_candidate_stops_even_when_total_count_is_inconsistent(self):
        for total in (0, 2, 101, 1001):
            github = GitHub([run(43991573918, status='in_progress')])
            with self.subTest(total=total), patch.object(github, 'api', return_value={'total_count': total, 'workflow_runs': github.rows}) as api, patch.object(wakeup, 'read_source', side_effect=AssertionError('Dropbox must not be read')):
                self.assertEqual(self.wake(github), {'state': 'daily_active', 'run_id': 43991573918})
                api.assert_called_once()

    def test_active_status_transition_still_blocks_and_completed_transition_retries(self):
        github = GitHub()
        with patch.object(github, 'api', return_value={'total_count': 1, 'workflow_runs': [run(status='queued')]}) as api:
            self.assertEqual(self.wake(github)['state'], 'daily_active')
            api.assert_called_once()
        with patch.object(github, 'api', side_effect=[{'total_count': 1, 'workflow_runs': [run()]}, {'total_count': 1, 'workflow_runs': [run(status='in_progress')]}]) as api:
            self.assertEqual(self.wake(github)['state'], 'daily_active')
            self.assertEqual(api.call_count, 2)

    def test_empty_active_page_with_nonzero_total_is_retried_not_treated_as_absent(self):
        github = GitHub()
        with patch.object(github, 'api', side_effect=[{'total_count': 1, 'workflow_runs': []}, {'total_count': 1, 'workflow_runs': [run(status='in_progress')]}]) as api:
            self.assertEqual(self.wake(github)['state'], 'daily_active')
            self.assertEqual(api.call_count, 2)
        with patch.object(github, 'api', return_value={'total_count': 1, 'workflow_runs': []}) as api:
            with self.assertRaisesRegex(ValueError, 'daily_run_inventory_incomplete'):
                self.wake(github)
            self.assertEqual(api.call_count, 3)

    def test_recent_run_inventory_spans_pages_and_finds_previously_attempted_batch(self):
        github = GitHub([run(index, day='261108') for index in range(1, 102)] + [run(102)])
        self.assertEqual(self.wake(github), {'state': 'batch_already_attempted', 'date_folder': DAY, 'run_id': 102})
        recent_calls = [path for path in github.calls if 'created=' in path]
        self.assertEqual(len(recent_calls), 2)
        self.assertIn('page=2', recent_calls[1])

    def test_recent_count_drift_and_duplicate_pages_restart_before_authorizing_absence(self):
        for corruption in ('count', 'duplicate', 'short'):
            github = GitHub([run(index) for index in range(1, 103)])
            original = github.api
            changed = [False]
            def request(path):
                result = original(path)
                if 'page=2' in path and not changed[0]:
                    changed[0] = True
                    if corruption == 'count': result['total_count'] += 1
                    if corruption == 'duplicate': result['workflow_runs'][0] = run(1)
                    if corruption == 'short': result['workflow_runs'].pop()
                return result
            with self.subTest(corruption=corruption), patch.object(github, 'api', side_effect=request):
                result = wakeup.runs(github, since='2026-11-07T00:00:00Z', sleep=lambda _: None)
            self.assertEqual(len(result), 102)
            self.assertEqual(len(github.calls), 4)
            self.assertIn('page=1', github.calls[2])

    def test_persistent_recent_inventory_incompleteness_never_dispatches(self):
        github = GitHub([run(index, day='261108') for index in range(1, 103)])
        original = github.api
        def request(path):
            result = original(path)
            if 'created=' in path and 'page=2' in path:
                result['workflow_runs'][0] = run(1)
            return result
        with patch.object(github, 'api', side_effect=request), self.assertRaisesRegex(ValueError, 'daily_run_inventory_incomplete'):
            self.wake(github)
        self.assertEqual(sum('created=' in path for path in github.calls), 6)

    def test_active_shortcut_retains_repository_workflow_and_status_validation(self):
        for mutation, reason in (({'path': '.github/workflows/foreign.yml'}, 'identity'),
                                 ({'head_repository': {'full_name': 'foreign/repo'}}, 'identity'),
                                 ({'status': 'unrecognized'}, 'status')):
            github = GitHub()
            candidate = {**run(status='in_progress'), **mutation}
            with self.subTest(mutation=mutation), patch.object(github, 'api', return_value={'total_count': 1001, 'workflow_runs': [candidate]}):
                with self.assertRaisesRegex(ValueError, 'daily_run_' + reason + '_invalid'):
                    self.wake(github)


class SourceTests(unittest.TestCase):
    def source(self, day=DAY, modified='2026-11-09T23:30:41Z', pdf=True):
        def reader(token, path, recursive):
            self.assertEqual(token, 'TOKEN')
            if not recursive:
                return [{'.tag': 'folder', 'name': day, 'path_lower': '/zip_backup/' + day}]
            return [{'.tag': 'file', 'name': 'a.pdf', 'server_modified': modified}] if pdf else []
        return wakeup.read_source(NOW, token='TOKEN', reader=reader)

    def test_late_52_source_pattern_is_ready_without_pdf_body_downloads(self):
        self.assertEqual(self.source(), {'state': 'ready', 'date_folder': DAY, 'pdf_count': 1})

    def test_stale_future_empty_and_unsettled_sources_cannot_start_paid_work(self):
        self.assertEqual(self.source(day='261108')['state'], 'waiting_for_fresh_source')
        self.assertEqual(self.source(day='261111')['state'], 'waiting_for_fresh_source')
        self.assertEqual(self.source(pdf=False)['state'], 'source_empty')
        self.assertEqual(self.source(modified='2026-11-10T00:44:00Z')['state'], 'source_still_arriving')
        with self.assertRaisesRegex(ValueError, 'source_modification_time_unknown'):
            self.source(modified='unknown')


class ReceiptTests(unittest.TestCase):
    def reader(self, *, changed=False, visible=True):
        def read(token, path, recursive):
            self.assertEqual(token, 'TOKEN')
            if not recursive:
                self.assertEqual(path, '/zip_backup')
                # A concurrent newer batch and an equivalent date alias must
                # never replace the date given in the producer receipt.
                names = ['261110', '20261109']
                if visible:
                    names.append(DAY)
                return [{'.tag': 'folder', 'name': name, 'path_lower': '/zip_backup/' + name} for name in names]
            self.assertEqual(path, '/zip_backup/' + DAY)
            return [{'.tag': 'file', 'name': 'B.PDF', 'id': 'id:b', 'rev': '001d' if changed else '001c'},
                    {'.tag': 'folder', 'name': 'nested.pdf'},
                    {'.tag': 'file', 'name': 'A.pdf', 'id': 'id:a', 'rev': '001a'},
                    {'.tag': 'file', 'name': 'metadata.json'}]
        return read

    def test_blank_dispatch_is_reconciliation_and_malformed_receipts_fail_closed(self):
        self.assertIsNone(wakeup.parse_source_receipt({}))
        self.assertIsNone(wakeup.parse_source_receipt({'inputs': dict.fromkeys(RECEIPT_INPUTS, '')}))
        self.assertEqual(RECEIPT, wakeup.SourceReceipt(DAY, 42, 2, RECEIPT_INPUTS['manifest_sha256']))
        for key, value in [('date_folder', '20261109'), ('date_folder', '261332'), ('date_folder', '261109\n'),
                           ('upstream_run_id', ''), ('upstream_run_id', '0001'), ('upstream_run_id', 42),
                           ('upstream_run_id', '1' * 17), ('pdf_count', '0'), ('pdf_count', None),
                           ('pdf_count', '1' * 9), ('manifest_sha256', 'F' * 64)]:
            with self.subTest(key=key, value=value), self.assertRaisesRegex(ValueError, 'source_receipt_'):
                wakeup.parse_source_receipt({'inputs': {**RECEIPT_INPUTS, key: value}})

    def test_exact_metadata_receipt_is_ready_without_waiting_for_server_modified(self):
        source = wakeup.read_source(NOW, receipt=RECEIPT, token='TOKEN', reader=self.reader())
        self.assertEqual(source, {'state': 'ready', 'date_folder': DAY, 'pdf_count': 2})

    def test_missing_exact_folder_and_mismatched_readback_never_try_another_date(self):
        for reader, receipt, state in [
            (self.reader(visible=False), RECEIPT, 'source_not_visible'),
            (self.reader(changed=True), RECEIPT, 'source_inventory_changed'),
            (self.reader(), wakeup.SourceReceipt(DAY, 42, 3, RECEIPT.manifest_sha256), 'source_inventory_changed'),
        ]:
            with self.subTest(state=state, receipt=receipt):
                def source(tick, *, receipt):
                    return wakeup.read_source(tick, receipt=receipt, token='TOKEN', reader=reader)
                result = wakeup.wake(GitHub(), NOW, receipt=receipt, source_reader=source, submit=self.fail)
                self.assertEqual(result, {'state': state, 'date_folder': DAY})

    def test_revision_digest_requires_distinct_ids_and_unambiguous_records(self):
        for rows, reason in [
            ([{'id': 'id:a', 'rev': '1'}, {'id': 'id:a', 'rev': '2'}], 'source_pdf_identity_duplicate'),
            ([{'id': 'id:a', 'rev': '1\n'}], 'source_pdf_revision_invalid'),
            ([{'id': 'id:a'}], 'source_pdf_revision_invalid'),
        ]:
            with self.subTest(rows=rows), self.assertRaisesRegex(ValueError, reason):
                wakeup.pdf_manifest_sha256(rows)

    def test_verified_event_and_timers_share_existing_daily_attempt_deduplication(self):
        github, submissions = GitHub(), []

        def source(tick, *, receipt):
            return wakeup.read_source(tick, receipt=receipt, token='TOKEN', reader=self.reader())

        def submit(api, day):
            submissions.append(day)
            api.rows.append(run(identity=2, day=day))
            return True

        result = wakeup.wake(github, NOW, receipt=RECEIPT, source_reader=source, submit=submit)
        self.assertEqual(result['state'], 'dispatched')
        verified_retry = wakeup.wake(github, NOW, receipt=RECEIPT, source_reader=source, submit=submit)
        timer_retry = wakeup.wake(github, NOW, source_reader=lambda tick: source(tick, receipt=RECEIPT), submit=submit)
        self.assertEqual(verified_retry['state'], 'batch_already_attempted')
        self.assertEqual(timer_retry['state'], 'batch_already_attempted')
        self.assertEqual(submissions, [DAY])

    def test_verified_event_reports_proof_while_daily_is_active(self):
        github = GitHub([run(identity=2, status='in_progress')])

        def source(tick, *, receipt):
            return wakeup.read_source(tick, receipt=receipt, token='TOKEN', reader=self.reader())

        result = wakeup.wake(github, NOW, receipt=RECEIPT, source_reader=source, submit=self.fail)
        self.assertEqual(result, {'state': 'daily_active', 'run_id': 2, 'source_proof': 'verified',
                                  'date_folder': DAY, 'pdf_count': 2})

        def changed_source(tick, *, receipt):
            return wakeup.read_source(tick, receipt=receipt, token='TOKEN', reader=self.reader(changed=True))

        result = wakeup.wake(github, NOW, receipt=RECEIPT, source_reader=changed_source, submit=self.fail)
        self.assertEqual(result, {'state': 'source_inventory_changed', 'date_folder': DAY})

    def test_receipt_keeps_freshness_bounds(self):
        for day in ('261108', '261111'):
            receipt = wakeup.SourceReceipt(day, 42, 2, RECEIPT.manifest_sha256)
            state = wakeup.read_source(NOW, receipt=receipt, reader=self.fail)
            self.assertEqual(state, {'state': 'waiting_for_fresh_source', 'date_folder': day})

    def test_overnight_admission_requires_an_exact_previous_day_proof(self):
        github = GitHub()
        before_two = datetime(2026, 11, 9, 17, 59, tzinfo=timezone.utc)

        def source(tick, *, receipt):
            assert tick == before_two
            return wakeup.read_source(tick, receipt=receipt, token='TOKEN', reader=self.reader())

        def submit(api, day):
            api.rows.append(run(identity=2, day=day))
            return True

        for early_day in ('261108', '261110'):
            receipt = wakeup.SourceReceipt(early_day, 42, 2, RECEIPT.manifest_sha256)
            state = wakeup.wake(github, before_two, receipt=receipt, source_reader=self.fail, submit=self.fail)
            self.assertEqual(state, {'state': 'before_daily_start'})
        self.assertEqual(github.calls, [])
        result = wakeup.wake(github, before_two, receipt=RECEIPT, source_reader=source, submit=submit)
        self.assertEqual(result['state'], 'dispatched')
        self.assertEqual(result['source_proof'], 'verified')
        self.assertEqual(result['date_folder'], DAY)


class WorkflowTests(unittest.TestCase):
    def test_daily_and_late_schedules_share_the_same_deduplicating_dispatcher(self):
        root = Path(__file__).resolve().parents[1]
        daily = yaml.safe_load((root / wakeup.WORKFLOW).read_text())
        wake = yaml.safe_load((root / wakeup.WAKEUP).read_text())
        events = lambda workflow: workflow.get('on', workflow.get(True, {}))
        self.assertNotIn('schedule', events(daily), 'A late independent cron can queue duplicate paid work')
        self.assertIn('workflow_dispatch', events(daily))
        self.assertEqual({item['cron'] for item in events(wake)['schedule']}, {'0 18 * * *', '47 * * * *'})
        self.assertEqual(set(events(wake)['workflow_dispatch']['inputs']), set(RECEIPT_INPUTS))
        self.assertTrue(all(field.get('type') == 'string' and not field.get('required')
                            for field in events(wake)['workflow_dispatch']['inputs'].values()))
        self.assertIs(wake['concurrency']['cancel-in-progress'], False)
        self.assertEqual(wake['concurrency']['queue'], 'max')
        self.assertIn("|| 'main'", wake['concurrency']['group'])

    def test_admission_precedes_classification_and_wakeup_retains_existing_delivery_defaults(self):
        root = Path(__file__).resolve().parents[1]
        daily = yaml.safe_load((root / wakeup.WORKFLOW).read_text())
        self.assertEqual(daily['concurrency']['queue'], 'max')
        steps = daily['jobs']['select-macro-reports']['steps']
        names = [step.get('name') for step in steps]
        self.assertLess(names.index('Retain source admission identity'), names.index('Select reports with DeepSeek'))
        wake = yaml.safe_load((root / wakeup.WAKEUP).read_text())
        self.assertEqual(wake['jobs']['wake']['permissions']['actions'], 'write')
        self.assertIn("github.event_name != 'pull_request'", wake['jobs']['wake']['if'])
        with patch.object(wakeup.subprocess, 'run') as command:
            command.return_value.returncode = 0
            self.assertTrue(wakeup.dispatch(GitHub(), DAY))
        import json
        self.assertEqual(json.loads(command.call_args.kwargs['input']),
                         {'ref': 'main', 'inputs': {'dropbox_date_folder': DAY}})
        self.assertEqual(command.call_count, 1)


if __name__ == '__main__':
    unittest.main()
