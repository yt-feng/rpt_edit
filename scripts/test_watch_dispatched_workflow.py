"""Fault-inject accepted-run visibility, transport and actual child failures."""
import copy
import contextlib
import io
from pathlib import Path
import unittest

import yaml

from recover_neutral_runner_loss import RecoveryError
import watch_dispatched_workflow as watcher

WORKFLOW = '.github/workflows/market-views-latex-pdf.yml'


def run(status='completed', conclusion='success', **changes):
    return {'id': 123, 'path': WORKFLOW, 'head_branch': 'main', 'event': 'workflow_dispatch',
            'repository': {'full_name': 'owner/repo'}, 'head_repository': {'full_name': 'owner/repo'},
            'status': status, 'conclusion': conclusion, **changes}


class GitHub:
    repository = 'owner/repo'

    def __init__(self, rows):
        self.rows, self.calls = list(rows), []

    def api(self, path):
        self.calls.append(path)
        value = self.rows.pop(0) if len(self.rows) > 1 else self.rows[0]
        if isinstance(value, Exception):
            raise value
        return copy.deepcopy(value)


class WatchTests(unittest.TestCase):
    def setUp(self):
        self.time, self.waits = 0, []

    def sleep(self, seconds):
        self.assertGreater(seconds, 0)
        self.time += seconds
        self.waits.append(seconds)

    def watch(self, api, **kwargs):
        with contextlib.redirect_stdout(io.StringIO()):
            return watcher.watch(api, 123, WORKFLOW, clock=lambda: self.time, sleep=self.sleep, **kwargs)

    def test_newly_dispatched_404_becomes_visible_without_any_mutation(self):
        api = GitHub([RecoveryError('github_http_404'), RecoveryError('github_http_404'),
                      run('queued', None), run('in_progress', None), run()])
        self.assertEqual(self.watch(api), 123)
        self.assertEqual(self.waits, [5, 5, 15, 15])
        self.assertEqual(api.calls, ['actions/runs/123'] * 5)

    def test_transport_loss_during_execution_waits_for_same_child(self):
        api = GitHub([run('in_progress', None), RecoveryError('github_read_failed'), run()])
        self.assertEqual(self.watch(api), 123)
        self.assertEqual(api.calls, ['actions/runs/123'] * 3)

    def test_permission_and_authentication_failures_are_immediate(self):
        for status in ('401', '403'):
            api = GitHub([RecoveryError('github_http_' + status)])
            with self.assertRaisesRegex(RecoveryError, 'github_http_' + status):
                self.watch(api)
            self.assertEqual(len(api.calls), 1)
            self.assertEqual(self.waits, [])

    def test_missing_run_and_long_running_child_have_bounded_waits(self):
        with self.assertRaisesRegex(RecoveryError, 'accepted_child_read_unavailable'):
            self.watch(GitHub([RecoveryError('github_http_404')]), read_grace=10)
        self.assertEqual(self.time, 10)
        self.time = 0
        with self.assertRaisesRegex(TimeoutError, 'wait_deadline'):
            self.watch(GitHub([run('in_progress', None)]), timeout=20)
        self.assertEqual(self.time, 20)

    def test_actual_child_failures_never_pass_or_retry_the_child(self):
        for conclusion in ('failure', 'cancelled', 'timed_out', 'skipped', None):
            api = GitHub([run(conclusion=conclusion)])
            with self.assertRaisesRegex(RecoveryError, 'did_not_succeed'):
                self.watch(api)
            self.assertEqual(api.calls, ['actions/runs/123'])

    def test_wrong_run_repository_branch_event_and_workflow_cannot_pass(self):
        for changes in ({'id': 124}, {'head_branch': 'feature'}, {'event': 'pull_request'},
                        {'head_repository': {'full_name': 'foreign/repo'}}, {'path': '.github/workflows/other.yml'}):
            with self.subTest(changes=changes), self.assertRaisesRegex(ValueError, 'identity_invalid'):
                self.watch(GitHub([run(**changes)]))

    def test_daily_job_checks_out_waiter_and_keeps_one_dispatch(self):
        root = Path(__file__).resolve().parents[1]
        daily = yaml.safe_load((root / '.github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml').read_text())
        steps = daily['jobs']['trigger-market-views']['steps']
        checkout = next(step for step in steps if step.get('uses') == 'actions/checkout@v4')
        for path in ('scripts/watch_dispatched_workflow.py', 'scripts/recover_neutral_runner_loss.py'):
            self.assertIn(path, checkout['with']['sparse-checkout'])
        script = next(step['run'] for step in steps if 'run' in step)
        self.assertEqual(script.count('gh workflow run'), 1)
        self.assertIn('--run-id "$MARKET_RUN_ID"', script)
        self.assertIn('--workflow .github/workflows/market-views-latex-pdf.yml', script)
        self.assertNotIn('gh run watch', script)


if __name__ == '__main__':
    unittest.main()
