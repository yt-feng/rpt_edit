import unittest
from datetime import datetime, timezone

import check_portal_ops_alert_window as alerts


NOW = datetime(2026, 8, 16, 20, 0, tzinfo=timezone.utc)


class PortalOpsAlertWindowTests(unittest.TestCase):
    def test_recent_success_suppresses_alert(self):
        decision = alerts.evaluate_recent_runs(
            [
                {
                    "databaseId": 200,
                    "status": "in_progress",
                    "conclusion": "",
                    "createdAt": "2026-08-16T20:00:00Z",
                    "startedAt": "2026-08-16T20:00:00Z",
                },
                {
                    "databaseId": 100,
                    "status": "completed",
                    "conclusion": "success",
                    "createdAt": "2026-08-15T20:30:00Z",
                    "startedAt": "2026-08-15T20:30:00Z",
                },
            ],
            current_run_id="200",
            now=NOW,
        )
        self.assertFalse(decision["should_alert"])
        self.assertEqual(decision["reason"], "recent_success")

    def test_success_before_window_does_not_suppress_alert(self):
        decision = alerts.evaluate_recent_runs(
            [
                {
                    "databaseId": 200,
                    "status": "in_progress",
                    "conclusion": "",
                    "createdAt": "2026-08-16T20:00:00Z",
                    "startedAt": "2026-08-16T20:00:00Z",
                },
                {
                    "databaseId": 100,
                    "status": "completed",
                    "conclusion": "success",
                    "createdAt": "2026-08-15T19:59:59Z",
                    "startedAt": "2026-08-15T19:59:59Z",
                },
            ],
            current_run_id="200",
            now=NOW,
        )
        self.assertTrue(decision["should_alert"])
        self.assertEqual(decision["reason"], "no_success_in_window")

    def test_active_run_does_not_hide_a_24_hour_success_outage(self):
        decision = alerts.evaluate_recent_runs(
            [
                {
                    "databaseId": 200,
                    "status": "in_progress",
                    "conclusion": "",
                    "createdAt": "2026-08-16T20:00:00Z",
                    "startedAt": "2026-08-16T20:00:00Z",
                },
                {
                    "databaseId": 201,
                    "status": "queued",
                    "conclusion": "",
                    "createdAt": "2026-08-16T20:05:00Z",
                    "startedAt": "2026-08-16T20:05:00Z",
                },
            ],
            current_run_id="200",
            now=NOW,
        )
        self.assertTrue(decision["should_alert"])
        self.assertEqual(decision["reason"], "no_success_in_window")

    def test_only_failures_in_window_send_alert(self):
        decision = alerts.evaluate_recent_runs(
            [
                {
                    "databaseId": 200,
                    "status": "in_progress",
                    "conclusion": "",
                    "createdAt": "2026-08-16T20:00:00Z",
                    "startedAt": "2026-08-16T20:00:00Z",
                },
                {
                    "databaseId": 199,
                    "status": "completed",
                    "conclusion": "failure",
                    "createdAt": "2026-08-16T19:00:00Z",
                    "startedAt": "2026-08-16T19:00:00Z",
                },
            ],
            current_run_id="200",
            now=NOW,
        )
        self.assertTrue(decision["should_alert"])

    def test_rerun_uses_attempt_started_at_instead_of_original_creation(self):
        decision = alerts.evaluate_recent_runs(
            [
                {
                    "databaseId": 200,
                    "status": "in_progress",
                    "conclusion": "",
                    "createdAt": "2026-08-01T00:00:00Z",
                    "startedAt": "2026-08-16T20:00:00Z",
                },
                {
                    "databaseId": 100,
                    "status": "completed",
                    "conclusion": "success",
                    "createdAt": "2026-08-01T00:00:00Z",
                    "startedAt": "2026-08-15T20:30:00Z",
                },
            ],
            current_run_id="200",
            current_started_at="2026-08-16T20:00:00Z",
            now=NOW,
        )
        self.assertFalse(decision["should_alert"])
        self.assertEqual(decision["reason"], "recent_success")

    def test_dedupe_key_is_stable_per_workflow(self):
        self.assertEqual(
            alerts.workflow_dedupe_key("  Final   PDF to XHS notes "),
            "workflow-failure:Final PDF to XHS notes",
        )


if __name__ == "__main__":
    unittest.main()
