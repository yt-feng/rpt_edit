"""Exercise missed schedules, late originals, duplicate wakes and lost POSTs."""
import copy
from datetime import datetime, timezone
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
            return {'total_count': len(rows), 'workflow_runs': copy.deepcopy(rows)}
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


class WorkflowTests(unittest.TestCase):
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
