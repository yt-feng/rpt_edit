from __future__ import annotations

import copy
import unittest

from scripts.portal_locale_history import plan_history_release


class HistoryReleaseTests(unittest.TestCase):
    def plan(self, candidates, *, today="2026-09-05", previous=None, daily_limit=100, **overrides):
        options = {
            "history_start_date": "2026-08-05", "launch_date": "2026-09-05",
            "today": today, "previous": previous, "daily_limit": daily_limit,
        }
        options.update(overrides)
        return plan_history_release(candidates, **options)

    def pages(self, count):
        return {f"/blog/{index:04d}.html": "2026-09-04" for index in range(count)}

    def test_initial_release_caps_at_100_latest_first_then_canonical(self):
        candidates = self.pages(105)
        candidates["/blog/older.html"] = "2026-08-05"
        candidates["/blog/latest.html"] = "2026-09-03"
        result = self.plan(candidates)
        self.assertEqual(result["schema_version"], 1)
        self.assertEqual(result["released"], sorted(self.pages(100)))
        self.assertEqual(result["selected_today"], result["released"])
        self.assertEqual(result["pending_count"], 7)
        self.assertEqual(result["last_release_date"], "2026-09-05")

    def test_latest_publication_precedes_lexicographic_order(self):
        result = self.plan({"/a": "2026-08-05", "/z": "2026-09-04", "/b": "2026-09-04"}, daily_limit=2)
        self.assertEqual(result["released"], ["/b", "/z"])

    def test_same_day_rerun_has_no_advance_even_if_new_candidates_arrive(self):
        previous = self.plan(self.pages(3))
        result = self.plan(self.pages(150), previous=previous)
        self.assertEqual(result["released"], previous["released"])
        self.assertEqual(result["selected_today"], previous["selected_today"])
        self.assertEqual(result["pending_count"], 147)

    def test_tomorrow_releases_one_more_batch(self):
        candidates = self.pages(250)
        previous = self.plan(candidates)
        result = self.plan(candidates, previous=previous, today="2026-09-06")
        self.assertEqual(len(result["released"]), 200)
        self.assertEqual(result["selected_today"], sorted(self.pages(200).keys() - self.pages(100).keys()))
        self.assertEqual(result["pending_count"], 50)

    def test_missed_days_do_not_multiply_allowance(self):
        candidates = self.pages(550)
        previous = self.plan(candidates)
        result = self.plan(candidates, previous=previous, today="2026-10-01")
        self.assertEqual(len(result["released"]), 200)
        self.assertEqual(len(result["selected_today"]), 100)
        self.assertEqual(result["pending_count"], 350)
        self.assertEqual(result["history_start_date"], "2026-08-05")

    def test_boundaries_new_old_and_future_content_do_not_use_history_quota(self):
        candidates = {
            "/old": "2026-08-04", "/first": "2026-08-05", "/last": "2026-09-04",
            "/new": "2026-09-05", "/newer": "2026-09-06", "/future": "2027-01-01",
        }
        result = self.plan(candidates)
        self.assertEqual(result["released"], ["/first", "/last"])
        self.assertEqual(result["pending_count"], 0)
        self.assertEqual(result["out_of_scope_count"], 4)

    def test_removed_source_is_not_advertised_and_same_day_cannot_refill(self):
        candidates = self.pages(3)
        previous = self.plan(candidates, daily_limit=2)
        del candidates["/blog/0000.html"]
        result = self.plan(candidates, previous=previous, daily_limit=2)
        self.assertEqual(result["released"], ["/blog/0001.html"])
        self.assertEqual(result["selected_today"], ["/blog/0001.html"])
        self.assertEqual(result["pending_count"], 1)
        restored = self.plan(self.pages(3), previous=result, today="2026-09-06", daily_limit=2)
        self.assertEqual(restored["released"], sorted(self.pages(3)))
        self.assertEqual(restored["selected_today"], ["/blog/0000.html", "/blog/0002.html"])

    def test_changed_source_date_outside_window_is_not_advertised(self):
        previous = self.plan({"/a": "2026-08-05"})
        result = self.plan({"/a": "2026-08-04"}, previous=previous)
        self.assertEqual(result["released"], [])
        self.assertEqual(result["out_of_scope_count"], 1)

    def test_prelaunch_does_not_release_or_use_a_day(self):
        candidates = self.pages(150)
        preview = self.plan(candidates, today="2026-09-04")
        self.assertEqual(preview["released"], [])
        self.assertEqual(preview["selected_today"], [])
        self.assertIsNone(preview["last_release_date"])
        self.assertEqual(preview["pending_count"], 150)
        launch = self.plan(candidates, previous=preview)
        self.assertEqual(len(launch["released"]), 100)

    def test_empty_day_cannot_open_a_later_same_day_batch(self):
        previous = self.plan({})
        self.assertEqual(previous["last_release_date"], "2026-09-05")
        result = self.plan(self.pages(2), previous=previous)
        self.assertEqual(result["released"], [])
        self.assertEqual(result["pending_count"], 2)

    def test_backwards_clock_and_future_previous_ledger_fail(self):
        previous = self.plan(self.pages(1), today="2026-09-06")
        for today in ("2026-09-05", "2026-08-01"):
            with self.subTest(today=today), self.assertRaisesRegex(ValueError, "future|backwards"):
                self.plan(self.pages(1), today=today, previous=previous)

    def test_configuration_changes_fail(self):
        previous = self.plan(self.pages(1))
        for overrides in (
            {"history_start_date": "2026-08-06"}, {"launch_date": "2026-09-06"}, {"daily_limit": 50},
        ):
            with self.subTest(overrides=overrides), self.assertRaisesRegex(ValueError, "configuration differs"):
                self.plan(self.pages(1), previous=previous, **overrides)

    def test_invalid_dates_or_limit_fail(self):
        for key, value in (
            ("today", "2026-02-30"), ("today", "20260905"), ("today", "2026-09-05T00:00:00Z"),
            ("history_start_date", "invalid"), ("history_start_date", "2026-09-05"),
            ("launch_date", "2026-08-04"), ("daily_limit", 0), ("daily_limit", True), ("daily_limit", 1.1),
        ):
            with self.subTest(key=key, value=value), self.assertRaises(ValueError):
                self.plan({}, **{key: value})
        with self.assertRaises(ValueError):
            self.plan({"/page": "not-a-date"})

    def test_malformed_previous_ledgers_fail(self):
        valid = self.plan(self.pages(3), daily_limit=2)
        for key, value in (
            ("schema_version", 2), ("schema_version", True), ("schema_version", "1"),
            ("released", "not-a-list"), ("released", ["/a", "/a"]),
            ("selected_today", ["/not-released"]), ("selected_today", ["/a", "/a"]),
            ("last_release_date", None), ("last_release_date", "2026-09-04"),
            ("last_release_date", "2026-13-01"), ("pending_count", -1),
            ("out_of_scope_count", True), ("daily_limit", True),
        ):
            previous = copy.deepcopy(valid)
            previous[key] = value
            with self.subTest(key=key, value=value), self.assertRaises(ValueError):
                self.plan(self.pages(3), previous=previous, daily_limit=2)
        for previous in ({}, [], "draft"):
            with self.subTest(previous=previous), self.assertRaises(ValueError):
                self.plan(self.pages(3), previous=previous)
        del valid["last_release_date"]
        with self.assertRaises(ValueError):
            self.plan(self.pages(3), previous=valid, daily_limit=2)

    def test_too_large_previous_daily_selection_fails(self):
        previous = self.plan(self.pages(3), daily_limit=2)
        previous["released"] = sorted(self.pages(3))
        previous["selected_today"] = sorted(self.pages(3))
        with self.assertRaises(ValueError):
            self.plan(self.pages(3), previous=previous, daily_limit=2)

    def test_canonical_paths_and_absolute_urls_supported_origin_is_callers_job(self):
        candidates = {"/": "2026-08-06", "https://portal.example.invalid/blog/one": "2026-08-07"}
        self.assertEqual(self.plan(candidates)["released"], sorted(candidates))
        for canonical in (
            "", "relative/page", "//host/page", "javascript:alert(1)", "/page?q=1", "/page#fragment",
            "/../page", "/%2e%2e/page", "/space here", "https://user:pass@host/page", "https://host:bad/page",
            "/back\\slash", "/control\x00", " https://portal.example.invalid/page",
        ):
            with self.subTest(canonical=canonical), self.assertRaises(ValueError):
                self.plan({canonical: "2026-08-05"})

    def test_deterministic_and_does_not_mutate_inputs(self):
        candidates = self.pages(201)
        previous = self.plan(candidates)
        snapshot = copy.deepcopy(previous)
        reversed_candidates = dict(reversed(list(candidates.items())))
        result = self.plan(candidates, previous=previous, today="2026-09-06")
        self.assertEqual(result, self.plan(reversed_candidates, previous=previous, today="2026-09-06"))
        self.assertEqual(previous, snapshot)
        self.assertEqual(candidates, self.pages(201))

    def test_balances_blog_report_other_with_latest_first_inside_each_cohort(self):
        candidates = {
            "https://portal.example.invalid/blog/old": "2026-08-05",
            "https://portal.example.invalid/blog/new": "2026-09-03",
            "https://portal.example.invalid/reports/a-new": "2026-09-04",
            "https://portal.example.invalid/reports/b-new": "2026-09-04",
            "https://portal.example.invalid/reports/c-new": "2026-09-04",
            "https://portal.example.invalid/other-old": "2026-08-10",
        }
        result = self.plan(candidates, daily_limit=4)
        self.assertEqual(result["selected_today"], sorted((
            "https://portal.example.invalid/blog/new", "https://portal.example.invalid/reports/a-new",
            "https://portal.example.invalid/other-old", "https://portal.example.invalid/blog/old",
        )))
        self.assertEqual(result["selected_counts"], {"blog": 2, "report": 1, "other": 1})
        self.assertEqual(result["pending_count"], 2)

    def test_paused_initial_plan_has_no_selection_or_release_date(self):
        result = self.plan(self.pages(150), paused=True)
        self.assertTrue(result["paused"])
        self.assertEqual(result["released"], [])
        self.assertEqual(result["selected_today"], [])
        self.assertIsNone(result["last_release_date"])
        self.assertEqual(result["pending_count"], 150)

    def test_pause_preserves_released_pages_and_date_then_resumes_one_batch(self):
        candidates = self.pages(350)
        previous = self.plan(candidates)
        paused = self.plan(candidates, previous=previous, today="2026-09-06", paused=True)
        self.assertEqual(paused["released"], previous["released"])
        self.assertEqual(paused["last_release_date"], previous["last_release_date"])
        self.assertEqual(paused["selected_today"], [])
        resumed = self.plan(candidates, previous=paused, today="2026-09-20")
        self.assertEqual(len(resumed["released"]), 200)
        self.assertEqual(len(resumed["selected_today"]), 100)
        self.assertFalse(resumed["paused"])

    def test_same_day_pause_and_unpause_does_not_advance(self):
        candidates = self.pages(250)
        previous = self.plan(candidates)
        paused = self.plan(candidates, previous=previous, paused=True)
        resumed = self.plan(candidates, previous=paused)
        self.assertEqual(resumed["released"], previous["released"])
        self.assertEqual(resumed["selected_today"], previous["selected_today"])
        with self.assertRaisesRegex(ValueError, "paused"):
            self.plan({}, paused="false")


if __name__ == "__main__":
    unittest.main()
