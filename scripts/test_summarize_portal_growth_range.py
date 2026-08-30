#!/usr/bin/env python3

from __future__ import annotations

import io
import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import summarize_portal_growth_range as growth


def event(
    event_id: str,
    day: str,
    session: str,
    visitor: str,
    *,
    event_type: str = "page_view",
    path: str = "/",
    report_id: str = "",
    referrer_host: str = "",
    query: str = "",
    action: str = "",
    status: str = "",
    returning: bool = True,
    **extra: object,
) -> dict[str, object]:
    row: dict[str, object] = {
        "id": event_id,
        "ts": f"{day}T09:00:00+08:00",
        "date": day,
        "type": event_type,
        "session_id": session,
        "session_started_at": f"{day}T09:00:00+08:00",
        "visitor_id": visitor,
        "is_returning": returning,
        "landing_path": path,
        "path": path,
        "report_id": report_id,
        "referrer_host": referrer_host,
        "query": query,
        "action": action,
        "status": status,
        "bot_hint": "likely_human",
        "device_type": "desktop",
    }
    row.update(extra)
    return row


class GrowthReviewTest(unittest.TestCase):
    def test_primary_backup_and_missing_id_fallback_are_deduplicated(self) -> None:
        first = event("event-a", "2026-08-12", "session-a", "visitor-a")
        mirror = dict(first)
        fallback = event("", "2026-08-12", "session-b", "visitor-b", event_type="report_open")
        fallback_mirror = dict(fallback)
        distinct_search = dict(fallback, type="search", query="different intent")
        rows, removed = growth.deduplicate_events([first, mirror, fallback, fallback_mirror, distinct_search])
        self.assertEqual(len(rows), 3)
        self.assertEqual(removed, 2)

    def test_bjt_human_session_channels_funnel_and_privacy(self) -> None:
        page = event(
            "page",
            "2026-08-12",
            "session-secret",
            "visitor-secret",
            path="/reports/example.html",
            report_id="report-a",
            referrer_host="google.example",
            query="private query",
            user_agent="private raw user agent",
            referrer="https://google.example/private-path",
            returning=False,
        )
        page["ts"] = "2026-08-11T16:30:00Z"
        rows = [
            page,
            event("open", "2026-08-12", "session-secret", "visitor-secret", event_type="report_open", path="/reports/example.html"),
            event("attempt", "2026-08-12", "session-secret", "visitor-secret", event_type="download_attempt", path="/reports/example.html"),
            event("success", "2026-08-12", "session-secret", "visitor-secret", event_type="download_success", path="/reports/example.html"),
            event("auth", "2026-08-12", "session-secret", "visitor-secret", event_type="account_auth", path="/reports/example.html", action="register", status="success"),
            event("bot", "2026-08-12", "bot-session", "bot-visitor", bot_hint="verified_bot"),
            event("admin", "2026-08-12", "admin-session", "admin-visitor", event_type="daily_file_download"),
            event("anonymous", "2026-08-12", "", ""),
        ]
        review = growth.build_growth_review(
            rows,
            "2026-08-12",
            "2026-08-12",
            site_host="portal.example.invalid",
            min_count=2,
        )
        self.assertEqual(review["totals"]["sessions"], 1)
        self.assertEqual(review["totals"]["visitors"], 1)
        self.assertEqual(review["totals"]["organic_search_sessions"], 1)
        self.assertEqual(review["totals"]["download_success_sessions"], 1)
        self.assertEqual(review["totals"]["registration_sessions"], 1)
        self.assertEqual(review["daily"][0]["date"], "2026-08-12")
        self.assertEqual(review["data_quality"]["known_bot_events_excluded"], 1)
        self.assertEqual(review["data_quality"]["administrative_events_excluded"], 1)
        self.assertEqual(review["data_quality"]["non_bot_events_without_session_identity_excluded"], 1)
        self.assertEqual(review["top_landing_pages"], [], "small landing cohorts must be suppressed")
        serialized = json.dumps(review, ensure_ascii=False)
        for secret in (
            "session-secret",
            "visitor-secret",
            "private query",
            "private raw user agent",
            "private-path",
        ):
            self.assertNotIn(secret, serialized)

    def test_search_intents_fanout_is_deduplicated(self) -> None:
        first = event("search-a", "2026-08-12", "session-a", "visitor-a", event_type="search", query=" AI 研究 ")
        second = event("search-b", "2026-08-12", "session-a", "visitor-a", event_type="search", query="ai  研究")
        second["ts"] = "2026-08-12T09:00:42+08:00"
        third = event("search-c", "2026-08-12", "session-a", "visitor-a", event_type="search", query="ai 研究")
        third["ts"] = "2026-08-12T09:02:00+08:00"
        self.assertEqual(growth.search_intent_count([first, second, third]), 2)

    def test_d1_and_d7_only_use_eligible_new_visitor_cohorts(self) -> None:
        rows = [
            event("d0", "2026-08-01", "new-d0", "new-visitor", returning=False),
            event("d1", "2026-08-02", "new-d1", "new-visitor"),
            event("d7", "2026-08-08", "new-d7", "new-visitor"),
            event("late", "2026-08-08", "late-d0", "late-visitor", returning=False),
        ]
        review = growth.build_growth_review(rows, "2026-08-01", "2026-08-08")
        retention = {row["metric"]: row for row in review["retention"]}
        self.assertEqual(retention["d1"]["eligible_new_visitors"], 1)
        self.assertEqual(retention["d1"]["retained_visitors"], 1)
        self.assertEqual(retention["d7"]["eligible_new_visitors"], 1)
        self.assertEqual(retention["d7"]["retained_visitors"], 1)

    def test_action_windows_catalog_treatment_control_washout_and_did(self) -> None:
        action = {
            "id": "action-a",
            "name": "专题动作",
            "effective_at": "2026-08-19T10:48:21+08:00",
            "pre_days": 7,
            "washout_days": 2,
            "post_days": 7,
            "institutions": ["Bernstein"],
            "landing_path_prefixes": ["/reports/institutions/bernstein/"],
            "control_page_families": ["public_report"],
            "minimum_target_sessions": 1,
        }
        rows = [
            event("pre-target", "2026-08-12", "pre-target", "v1", path="/reports/bern-a.html", report_id="bern-a", referrer_host="google.example"),
            event("washout-target", "2026-08-20", "wash-target", "v2", path="/reports/bern-a.html", report_id="bern-a", referrer_host="google.example"),
            event("direct-hub", "2026-08-22", "direct-hub", "v3", path="/reports/institutions/bernstein/", referrer_host=""),
        ]
        for index in range(2):
            rows.append(event(f"pre-control-{index}", "2026-08-13", f"pre-control-{index}", f"pc{index}", path=f"/reports/control-pre-{index}.html", report_id=f"control-pre-{index}", referrer_host="bing.example"))
            rows.append(event(f"post-control-{index}", "2026-08-23", f"post-control-{index}", f"oc{index}", path=f"/reports/control-post-{index}.html", report_id=f"control-post-{index}", referrer_host="bing.example"))
        rows.append(event(
            "later-bernstein-open",
            "2026-08-13",
            "pre-control-0",
            "pc0",
            event_type="report_open",
            path="/reports/bern-a.html",
            report_id="bern-a",
            referrer_host="bing.example",
            institution="Bernstein",
        ))
        for index in range(3):
            rows.append(event(f"post-target-{index}", "2026-08-22", f"post-target-{index}", f"pt{index}", path=f"/reports/bern-{index}.html", report_id="bern-a", referrer_host="google.example"))
        covered = [day.isoformat() for day in growth.date_range(date(2026, 8, 12), date(2026, 8, 28))]
        review = growth.build_growth_review(
            rows,
            "2026-08-12",
            "2026-08-28",
            [action],
            covered_dates=covered,
            catalog_institutions={"bern-a": {"bernstein", "伯恩斯坦"}},
        )
        impact = review["action_impacts"][0]
        self.assertEqual(impact["pre_window"], {"start": "2026-08-12", "end": "2026-08-18"})
        self.assertEqual(impact["washout_window"], {"start": "2026-08-19", "end": "2026-08-21"})
        self.assertEqual(impact["post_window"], {"start": "2026-08-22", "end": "2026-08-28"})
        self.assertEqual(impact["pre"]["target_external_landing_sessions"], 1)
        self.assertEqual(impact["post"]["target_external_landing_sessions"], 3)
        self.assertEqual(impact["pre"]["control_external_report_landing_sessions"], 2)
        self.assertEqual(impact["post"]["control_external_report_landing_sessions"], 2)
        self.assertEqual(impact["change"]["difference_in_relative_changes"], 2.0)
        self.assertEqual(impact["status"], "positive_directional_signal")
        self.assertTrue(impact["complete_window"])

        missing_coverage = [day for day in covered if day != "2026-08-28"]
        incomplete = growth.build_growth_review(
            rows,
            "2026-08-12",
            "2026-08-28",
            [action],
            covered_dates=missing_coverage,
            catalog_institutions={"bern-a": {"bernstein"}},
        )["action_impacts"][0]
        self.assertEqual(incomplete["status"], "incomplete_window")

    def test_auto_window_expands_only_for_overlapping_action(self) -> None:
        action = {
            "effective_at": "2026-08-19T10:48:21+08:00",
            "pre_days": 7,
            "washout_days": 2,
            "post_days": 7,
        }
        self.assertEqual(
            growth.resolve_review_window("", "", [action], today=date(2026, 8, 30)),
            (date(2026, 8, 12), date(2026, 8, 29)),
        )
        self.assertEqual(
            growth.resolve_review_window("", "", [action], today=date(2026, 9, 20)),
            (date(2026, 9, 6), date(2026, 9, 19)),
        )
        with self.assertRaisesRegex(ValueError, "provided together"):
            growth.resolve_review_window("2026-08-12", "", [action])
        with self.assertRaisesRegex(ValueError, "YYYY-MM-DD"):
            growth.resolve_review_window("not-a-date", "also-not-a-date", [action])

    def test_catalog_normalization_and_mirrored_read_fallback(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "catalog.json"
            path.write_text(json.dumps({"items": [{"id": "Report-A", "bank_code": "Bernstein", "bank_name": "伯恩斯坦"}]}), encoding="utf-8")
            institutions = growth.load_catalog_institutions(path)
        self.assertEqual(institutions["report-a"], {"bernstein", "伯恩斯坦"})

        class Client:
            def get_object(self, *, Bucket: str, Key: str) -> dict[str, io.BytesIO]:
                if Key == "primary":
                    raise ValueError("damaged mirror")
                return {"Body": io.BytesIO(b'{"id":"event-a","type":"page_view"}')}

        self.assertEqual(growth.read_event(Client(), "private", ["primary", "backup"])["id"], "event-a")

    def test_workflow_is_weekly_private_and_short_lived(self) -> None:
        workflow = (Path(__file__).resolve().parents[1] / ".github/workflows/portal-growth-review.yml").read_text(encoding="utf-8")
        self.assertIn("schedule:", workflow)
        self.assertIn("PORTAL_SITE_URL", workflow)
        self.assertIn("--auto-days 14", workflow)
        self.assertIn("$GITHUB_STEP_SUMMARY", workflow)
        self.assertIn("retention-days: 1", workflow)
        self.assertNotIn("portal.example.invalid", workflow)


if __name__ == "__main__":
    unittest.main()
