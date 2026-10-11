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
    def test_legacy_json_rendering_does_not_invent_download_intersections(self) -> None:
        # Captured from the pre-diagnostics builder at 9e46db30, with an attempt
        # and a success in different sessions. The old JSON has totals only.
        legacy = json.loads(Path(__file__).with_name("fixtures").joinpath("portal_growth_review_legacy.json").read_text())
        self.assertNotIn("download_diagnostics", legacy)
        self.assertEqual(legacy["totals"]["download_attempt_sessions"], 1)
        self.assertEqual(legacy["totals"]["download_success_sessions"], 1)
        rendered = growth.markdown_summary(legacy)
        self.assertIn("尝试下载会话：1；同会话观测到成功：未观测（不可视作 0）；错误：未观测（不可视作 0）；准备中：未观测（不可视作 0）", rendered)
        legacy["download_diagnostics"] = None
        del legacy["totals"]["download_attempt_sessions"]
        self.assertIn("尝试下载会话：未观测（不可视作 0）", growth.markdown_summary(legacy))

        current = growth.build_growth_review([
            event("attempt", "2026-10-01", "a", "v", event_type="download_attempt"),
            event("success", "2026-10-01", "b", "w", event_type="download_success"),
        ], "2026-10-01", "2026-10-01")
        self.assertIn("尝试下载会话：1；同会话观测到成功：0；错误：0；准备中：0", growth.markdown_summary(current))

    def test_intentional_engagement_excludes_passive_exposures_and_empty_searches(self) -> None:
        rows = [
            event("auto-page", "2026-10-01", "auto", "auto-v"),
            event("auto-exposure", "2026-10-01", "auto", "auto-v", event_type="report_chat_interaction", action="entry_impression"),
            event("empty-search", "2026-10-01", "empty", "empty-v", event_type="search", query="   "),
            event("query", "2026-10-01", "query", "query-v", event_type="search", query="private research query"),
            event("click", "2026-10-01", "click", "click-v", event_type="report_chat_interaction", action="entry_click"),
            event("form-auto", "2026-10-01", "form", "form-v", event_type="membership_request", action="form_impression"),
            event("form-open", "2026-10-01", "form", "form-v", event_type="membership_request", action="form_open"),
            event("form-start", "2026-10-01", "form-start", "form-start-v", event_type="membership_request", action="form_start"),
            event("failed-login", "2026-10-01", "failed", "failed-v", event_type="account_auth", action="login", status="error"),
            event("login", "2026-10-01", "login", "login-v", event_type="account_auth", action="login", status="success"),
            event("reward-exposure", "2026-10-01", "reward-auto", "reward-auto-v", event_type="reward_checkin", action="impression"),
            event("reward-action", "2026-10-01", "reward", "reward-v", event_type="reward_checkin", action="daily", status="success"),
            event("unknown-action", "2026-10-01", "unknown", "unknown-v", event_type="report_chat_interaction", action="private-action"),
        ]
        review = growth.build_growth_review(rows, "2026-10-01", "2026-10-01")
        self.assertEqual(review["totals"]["intentional_engaged_sessions"], 5)
        self.assertEqual(review["totals"]["engaged_sessions"], 6, "the legacy definition remains separate")
        self.assertEqual(review["daily"][0]["intentional_engaged_sessions"], 5)
        self.assertEqual(review["acquisition_channels"][0]["intentional_engagement_rate"], round(5 / 11, 4))
        serialized = json.dumps(review) + growth.markdown_summary(review)
        self.assertNotIn("private research query", serialized)
        self.assertIn("AI 入口自动曝光", growth.markdown_summary(review))

    def test_daily_concentration_marks_observed_peaks_without_exclusion(self) -> None:
        rows = [event(f"{day}-{index}", day, f"{day}-s-{index}", f"{day}-v-{index}")
                for day, count in (("2026-10-01", 1), ("2026-10-02", 6), ("2026-10-03", 3))
                for index in range(count)]
        rows.append(event("excluded-bot", "2026-10-01", "bot", "bot-v", bot_hint="verified_bot"))
        review = growth.build_growth_review(rows, "2026-10-01", "2026-10-03")
        concentration = review["daily_session_concentration"]
        self.assertEqual(concentration["total_sessions"], 10)
        self.assertEqual(concentration["top_day"], {"date": "2026-10-02", "sessions": 6, "share_of_all_sessions": 0.6})
        self.assertEqual([row["date"] for row in concentration["top_two_days"]], ["2026-10-02", "2026-10-03"])
        self.assertEqual(concentration["top_two_sessions"], 9)
        self.assertEqual(concentration["top_two_share"], 0.9)
        self.assertEqual(concentration["automatically_excluded_dates"], [])
        self.assertEqual(review["totals"]["sessions"], 10)
        empty = growth.build_growth_review([], "2026-10-01", "2026-10-03")
        self.assertIsNone(empty["daily_session_concentration"]["top_day"])
        self.assertIsNone(empty["daily_session_concentration"]["top_two_share"])
        self.assertIn("未观测", growth.markdown_summary(empty))

    def test_membership_journey_preserves_controlled_placements_and_states(self) -> None:
        rows = [
            event(f"event-{index}", "2026-10-11", f"session-{index}", f"visitor-{index}",
                  event_type="membership_request", action="form_open", request_kind="membership",
                  measurement_version="membership-v1", placement=placement, status=status)
            for index, (placement, status) in enumerate((
                ("account", "guest"), ("membership", "signed_in"), ("access", "pending"),
                ("support", "abandoned"), ("privacy", "guest"), ("refund", "guest"),
                ("deep_link", "guest"), ("private-placement", "private-status"),
            ))
        ]
        review = growth.build_growth_review(rows, "2026-10-11", "2026-10-11")
        actions = review["journey_diagnostics"]["client_actions"]
        pairs = {(row["placement"], row["status"]) for row in actions}
        self.assertEqual(pairs, {
            ("account", "guest"), ("membership", "signed_in"), ("access", "pending"),
            ("support", "abandoned"), ("privacy", "guest"), ("refund", "guest"),
            ("deep_link", "guest"), ("other", "other"),
        })
        serialized = json.dumps(review) + growth.markdown_summary(review)
        self.assertNotIn("private-placement", serialized)
        self.assertNotIn("private-status", serialized)

    def test_historical_membership_measurement_is_unavailable_not_zero(self) -> None:
        rows = [
            event("page", "2026-10-01", "session", "visitor"),
            event("support", "2026-10-01", "session", "visitor", event_type="membership_request",
                  action="submitted", request_kind="support"),
            event("missing-kind", "2026-10-01", "session", "visitor", event_type="membership_request",
                  action="submitted"),
        ]
        review = growth.build_growth_review(rows, "2026-10-01", "2026-10-01")
        self.assertIsNone(review["totals"]["membership_application_sessions"])
        self.assertIsNone(review["totals"]["access_application_sessions"])
        steps = {row["step"]: row for row in review["funnel"]}
        self.assertIsNone(steps["membership_application_sessions"]["rate_from_landing"])
        diagnostic = review["membership_request_diagnostics"]
        self.assertEqual(diagnostic["coverage"], "legacy_observations_only")
        stages = {row["action"]: row for row in diagnostic["stages"]}
        self.assertIsNone(stages["form_impression"]["sessions"])
        self.assertIsNone(stages["form_impression"]["rate_from_observed_version_sessions"])
        self.assertEqual(stages["submitted"]["sessions"], 1)
        self.assertIn("未观测（不可视作 0）", growth.markdown_summary(review))

    def test_membership_versioned_stages_kind_deduplication_and_privacy(self) -> None:
        rows = []
        for session, kind, action in (
            ("member-session", "membership", "form_impression"),
            ("member-session", "membership", "form_open"),
            ("member-session", "membership", "form_start"),
            ("member-session", "membership", "form_submit"),
            ("member-session", "membership", "submitted"),
            ("member-session", "membership", "deduplicated"),
            ("member-session", "access", "submitted"),
            ("access-session", "access", "submitted"),
            ("support-session", "support", "submitted"),
            ("privacy-session", "privacy", "form_open"),
            ("bot-session", "membership", "submitted"),
        ):
            rows.append(event(f"{session}-{kind}-{action}", "2026-10-11", session, "private-visitor",
                              event_type="membership_request", action=action, request_kind=kind,
                              measurement_version="membership-v1", contact_value="private-contact",
                              requester_email="private@example.invalid", note="private-note",
                              bot_hint="verified_bot" if session == "bot-session" else "unknown"))
        rows.append(dict(rows[4]))
        rows.append(event("no-session", "2026-10-11", "", "private-fallback", event_type="membership_request",
                          action="submitted", request_kind="membership", measurement_version="membership-v1"))
        review = growth.build_growth_review(rows, "2026-10-01", "2026-10-11")
        self.assertEqual(review["totals"]["membership_application_sessions"], 1)
        self.assertEqual(review["totals"]["access_application_sessions"], 2)
        self.assertEqual(review["totals"]["membership_or_access_application_sessions"], 2)
        diagnostics = review["membership_request_diagnostics"]
        self.assertEqual(diagnostics["first_versioned_observed_date"], "2026-10-11")
        self.assertEqual(diagnostics["observed_version_sessions"], 4)
        steps = {row["step"]: row for row in review["funnel"]}
        self.assertIsNone(steps["membership_application_sessions"]["rate_from_landing"])
        kinds = {row["request_kind"]: row for row in diagnostics["by_request_kind"]}
        stages = {row["action"]: row for row in kinds["privacy"]["stages"]}
        self.assertEqual(stages["submitted"]["sessions"], 0)
        self.assertEqual(stages["submitted"]["coverage"], "instrumented_no_event")
        self.assertEqual(kinds["refund"]["coverage"], "unavailable")
        serialized = json.dumps(review) + growth.markdown_summary(review)
        for secret in ("private-contact", "private@example.invalid", "private-note", "member-session", "private-visitor", "private-fallback"):
            self.assertNotIn(secret, serialized)

    def test_download_diagnostics_keep_overlapping_outcomes_and_controlled_errors(self) -> None:
        rows = [
            event("attempt", "2026-10-01", "a", "v", event_type="download_attempt"),
            event("pending", "2026-10-01", "a", "v", event_type="download_pending"),
            event("error", "2026-10-01", "a", "v", event_type="download_error", status="403", error="private-detail"),
            event("success", "2026-10-01", "a", "v", event_type="download_success"),
            event("attempt-b", "2026-10-01", "b", "w", event_type="download_attempt"),
            event("success-c", "2026-10-01", "c", "x", event_type="download_success"),
            event("error-c", "2026-10-01", "c", "x", event_type="download_error", status="private-status"),
        ]
        review = growth.build_growth_review(rows, "2026-10-01", "2026-10-01")
        diagnostic = review["download_diagnostics"]
        self.assertEqual(diagnostic["attempt_sessions"], 2)
        self.assertEqual(diagnostic["attempt_and_success_sessions"], 1)
        self.assertEqual(diagnostic["attempt_and_error_sessions"], 1)
        self.assertEqual(diagnostic["attempt_and_pending_sessions"], 1)
        self.assertEqual(diagnostic["attempt_without_observed_success_sessions"], 1)
        self.assertEqual(diagnostic["success_without_observed_attempt_sessions"], 1)
        self.assertEqual(diagnostic["attempt_with_observed_success_rate"], 0.5)
        self.assertEqual(diagnostic["error_categories"], [{"category": "403", "sessions": 1}, {"category": "other", "sessions": 1}])
        self.assertEqual(review["totals"]["download_error_sessions"], 2)
        serialized = json.dumps(review) + growth.markdown_summary(review)
        self.assertNotIn("private-status", serialized)
        self.assertNotIn("private-detail", serialized)

    def test_session_segments_use_first_observation_and_preserve_unknown(self) -> None:
        rows = [
            event("first", "2026-10-01", "a", "v", returning=False, device_type="mobile",
                  first_seen_at="2026-10-01T09:00:00+08:00"),
            event("later", "2026-10-01", "a", "v", event_type="download_success", device_type="desktop",
                  ts="2026-10-01T10:00:00+08:00"),
            event("unknown", "2026-10-01", "b", "w", is_returning=None, device_type="private-device"),
            event("returning", "2026-10-01", "c", "x", device_type="tablet",
                  first_seen_at="2026-09-01T09:00:00+08:00"),
        ]
        review = growth.build_growth_review(rows, "2026-10-01", "2026-10-01", min_count=1)
        devices = {row["segment"]: row for row in review["session_segments"]["device"]}
        visitors = {row["segment"]: row for row in review["session_segments"]["visitor_status"]}
        self.assertEqual(set(devices), {"mobile", "tablet", "unknown"})
        self.assertEqual(devices["mobile"]["download_success_sessions"], 1)
        self.assertEqual(set(visitors), {"new", "returning", "unknown"})
        self.assertIsNone(visitors["new"]["membership_or_access_application_rate"])
        self.assertNotIn("private-device", json.dumps(review))
        suppressed = growth.build_growth_review(rows, "2026-10-01", "2026-10-01", min_count=2)
        self.assertEqual(suppressed["session_segments"]["device"], [])

    def test_worker_default_false_without_valid_first_seen_is_unknown(self) -> None:
        rows = [
            event("legacy", "2026-10-01", "legacy-session", "legacy-visitor", returning=False),
            event("invalid", "2026-10-01", "invalid-session", "invalid-visitor", returning=False,
                  first_seen_at="private-invalid-timestamp"),
            event("new", "2026-10-01", "new-session", "new-visitor", returning=False,
                  first_seen_at="2026-10-01T09:00:00+08:00"),
        ]
        review = growth.build_growth_review(rows, "2026-10-01", "2026-10-01", min_count=1)
        visitors = {row["segment"]: row for row in review["session_segments"]["visitor_status"]}
        self.assertEqual(visitors["unknown"]["sessions"], 2)
        self.assertEqual(visitors["new"]["sessions"], 1)
        self.assertNotIn("private-invalid-timestamp", json.dumps(review))
        self.assertIn("历史缺失回访标记", growth.markdown_summary(review))

    def test_journey_actions_separate_server_audits_and_preserve_privacy(self) -> None:
        page = event("page", "2026-09-07", "private-session", "private-browser")
        submit = event(
            "submit", "2026-09-07", "private-session", "private-feature-hash",
            event_type="report_chat_interaction", action="submit", context="report",
            placement="research_tab", query="private question", user_agent="private ua",
        )
        rows = [
            page, submit, dict(submit),
            event("ready", "2026-09-07", "private-session", "private-feature-hash",
                  event_type="report_chat_interaction", action="export_docx_ready", context="report", chart_count=0, source_count=3),
            event("signup", "2026-09-07", "private-session", "private-browser",
                  event_type="account_auth", action="form_submit", status="register", placement="navigation"),
            event("signup-fail", "2026-09-07", "private-session", "private-browser",
                  event_type="account_auth", action="register", status="error", error="private-person 验证码错误"),
            event("audit", "2026-09-07", "", "", event_type="report_chat", action="answer",
                  status="success", ip_hash="private-server-ip", session_started_at=""),
            event("legacy", "2026-09-07", "", "private-legacy-hash",
                  event_type="report_chat_interaction", action="popular_click"),
            event("untrusted", "2026-09-07", "private-session", "private-browser",
                  event_type="reward_checkin", action="private-action", status="private-status",
                  placement="private-placement", context="private-context"),
            event("bot", "2026-09-07", "bot-session", "bot-browser",
                  event_type="report_chat_interaction", action="submit", bot_hint="verified_bot"),
            event("outside", "2026-09-06", "other-session", "other-browser",
                  event_type="reward_checkin", action="daily"),
        ]
        review = growth.build_growth_review(rows, "2026-09-07", "2026-09-07")
        journey = review["journey_diagnostics"]
        by_action = {row["action"]: row for row in journey["client_actions"]}
        self.assertEqual(by_action["submit"]["events"], 1, "primary and backup must not double count")
        self.assertEqual(by_action["submit"]["client_sessions"], 1)
        self.assertEqual(by_action["form_submit"]["status"], "register")
        self.assertEqual(by_action["form_submit"]["placement"], "navigation")
        self.assertEqual(by_action["export_docx_ready"]["numeric_metric_coverage"]["chart_count"]["zero_events"], 1)
        self.assertEqual(by_action["export_docx_ready"]["numeric_metric_coverage"]["source_count"]["positive_events"], 1)
        self.assertEqual(by_action["submit"]["numeric_metric_coverage"]["chart_count"]["missing_events"], 1)
        self.assertEqual(by_action["submit"]["numeric_metric_coverage"]["chart_count"]["zero_events"], 0)
        self.assertEqual(by_action["popular_click"]["client_sessions"], 0)
        self.assertEqual(by_action["popular_click"]["events_without_client_session"], 1)
        self.assertNotIn("entry_impression", by_action, "missing exposure must not be fabricated as zero exposure")
        self.assertEqual(journey["server_audit_actions"][0]["events"], 1)
        self.assertEqual(journey["registration_error_categories"], [{
            "category": "captcha", "events": 1, "client_sessions": 1, "events_without_client_session": 0,
        }])
        self.assertIsNone(journey["server_audit_actions"][0]["client_sessions"])
        self.assertEqual(review["data_quality"]["server_audit_events_excluded_from_sessions"], 1)
        self.assertEqual(review["totals"]["registration_sessions"], 0)
        self.assertEqual(review["totals"]["sessions"], 2, "only explicit browser session and legacy client fallback remain")
        self.assertEqual(sum(row["sessions"] for row in review["landing_page_families"]), 2)
        serialized = json.dumps(review) + growth.markdown_summary(review)
        for secret in ("private-session", "private-browser", "private-feature-hash", "private-server-ip",
                       "private question", "private ua", "private-action", "private-status",
                       "private-placement", "private-context"):
            self.assertNotIn(secret, serialized)
        self.assertNotIn("private-person", serialized)

    def test_journey_session_counts_do_not_count_feature_hashes_as_new_people(self) -> None:
        rows = [
            event("a", "2026-09-07", "same-session", "browser-id", event_type="report_chat_interaction", action="submit"),
            event("b", "2026-09-07", "same-session", "feature-hash", event_type="report_chat_interaction", action="submit"),
            event("c", "2026-09-07", "second-session", "another-hash", event_type="report_chat_interaction", action="submit"),
        ]
        journey = growth.build_growth_review(rows, "2026-09-07", "2026-09-07")["journey_diagnostics"]
        self.assertEqual(journey["client_actions"][0]["events"], 3)
        self.assertEqual(journey["client_actions"][0]["client_sessions"], 2)
        self.assertEqual(journey["daily_actions"][0]["client_sessions"], 2)
        self.assertEqual(growth.controlled_journey_value("blog_article", growth.JOURNEY_PLACEMENTS), "blog_article")

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

    def test_controlled_search_dimensions_use_builder_aliases_and_word_boundaries(self) -> None:
        self.assertEqual(len(growth.INSTITUTION_HUBS), 12)
        self.assertEqual(len(growth.TOPIC_HUBS), 14)
        self.assertIn("Morgan Stanley · 摩根士丹利", growth.institution_demand_labels("MS AI outlook"))
        self.assertIn("Bernstein Research · 伯恩斯坦", growth.institution_demand_labels("伯恩斯坦 半导体"))
        self.assertNotIn(
            "Morgan Stanley · 摩根士丹利",
            growth.institution_demand_labels("semis outlook"),
            "the short MS code must not match inside semis",
        )
        topic_labels = growth.topic_demand_labels("Goldman Sachs real estate policy and AI")
        self.assertIn("Real Estate", topic_labels)
        self.assertIn("Policy / Geopolitics", topic_labels)
        self.assertIn("Tech / AI / Semis", topic_labels)

    def test_search_demand_is_overlapping_funnel_aggregate_without_private_text(self) -> None:
        private_query = "Goldman Sachs AI private-demand-needle"
        first = event(
            "search-source-a",
            "2026-08-12",
            "private-search-session-a",
            "private-search-visitor-a",
            event_type="search",
            query=private_query,
            source="current_catalog",
            referrer="https://search.example/private-referrer-path",
            user_agent="private-demand-user-agent",
        )
        fanout = dict(first, id="search-source-b", source="archive_catalog")
        fanout["ts"] = "2026-08-12T09:00:37+08:00"
        rows = [
            first,
            fanout,
            event("open-a", "2026-08-12", "private-search-session-a", "private-search-visitor-a", event_type="report_open"),
            event("download-a", "2026-08-12", "private-search-session-a", "private-search-visitor-a", event_type="download_success"),
            event(
                "register-a",
                "2026-08-12",
                "private-search-session-a",
                "private-search-visitor-a",
                event_type="account_auth",
                action="register",
                status="success",
            ),
            event(
                "search-second-session",
                "2026-08-12",
                "private-search-session-b",
                "private-search-visitor-b",
                event_type="search",
                query=private_query,
            ),
            event(
                "search-uncategorized",
                "2026-08-12",
                "private-search-session-c",
                "private-search-visitor-c",
                event_type="search",
                query="private-uncategorized-needle",
            ),
        ]
        review = growth.build_growth_review(rows, "2026-08-12", "2026-08-12")
        demand = review["onsite_search_demand"]
        self.assertEqual(demand["minimum_intent_count"], 2)
        self.assertEqual(demand["total_deduplicated_intents"], 3)
        self.assertEqual(demand["uncategorized_intents"], 1)
        institution = demand["institutions"][0]
        topic = demand["topics"][0]
        expected_keys = {
            "label",
            "intent_count",
            "searching_sessions",
            "report_open_sessions",
            "download_success_sessions",
            "registration_sessions",
        }
        self.assertEqual(set(institution), expected_keys)
        self.assertEqual(set(topic), expected_keys)
        self.assertEqual(institution["label"], "Goldman Sachs · 高盛")
        self.assertEqual(topic["label"], "Tech / AI / Semis")
        for row in (institution, topic):
            self.assertEqual(row["intent_count"], 2, "two fanout events in one minute are one intent")
            self.assertEqual(row["searching_sessions"], 2)
            self.assertEqual(row["report_open_sessions"], 1)
            self.assertEqual(row["download_success_sessions"], 1)
            self.assertEqual(row["registration_sessions"], 1)

        serialized = json.dumps(review, ensure_ascii=False)
        markdown = growth.markdown_summary(review)
        for private_value in (
            private_query,
            "private-uncategorized-needle",
            "private-search-session-a",
            "private-search-visitor-a",
            "private-referrer-path",
            "private-demand-user-agent",
            "current_catalog",
            "archive_catalog",
        ):
            self.assertNotIn(private_value, serialized)
            self.assertNotIn(private_value, markdown)

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
