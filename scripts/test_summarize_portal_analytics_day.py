#!/usr/bin/env python3

import unittest

from summarize_portal_analytics_day import build_summary


class AnalyticsSummaryTest(unittest.TestCase):
    def test_summary_keeps_aggregates_and_drops_identifiers(self) -> None:
        summary = build_summary([
            {
                "id": "event-1",
                "ts": "2026-07-23T00:00:00Z",
                "type": "page_view",
                "visitor_id": "visitor-secret-a",
                "ip_hash": "hash-secret-a",
                "path": "/report.html?id=private-value",
                "referrer": "https://search.example/path?q=private-value",
                "country": "cn",
                "user_agent": "Mozilla/5.0 Chrome/140.0",
            },
            {
                "id": "event-2",
                "ts": "2026-07-23T00:02:00Z",
                "type": "report_open",
                "visitor_id": "visitor-secret-a",
                "country": "cn",
                "user_agent": "Mozilla/5.0 Chrome/140.0",
            },
            {
                "id": "event-3",
                "ts": "2026-07-23T01:00:00Z",
                "type": "page_view",
                "ip_hash": "hash-secret-b",
                "path": "/",
                "referrer": "",
                "country": "us",
                "user_agent": "ExampleCrawler/1.0",
            },
        ], "2026-07-23")

        self.assertEqual(summary["totals"]["events"], 3)
        self.assertEqual(summary["totals"]["page_views"], 2)
        self.assertEqual(summary["totals"]["unique_visitors"], 2)
        self.assertEqual(summary["totals"]["bot_hint_unique_visitors"], 1)
        self.assertEqual(summary["top_paths"][0], {"value": "/report.html", "count": 1})
        self.assertIn({"value": "search.example", "count": 1}, summary["top_referrer_hosts"])
        serialized = str(summary)
        for private_value in ["visitor-secret", "hash-secret", "private-value", "ExampleCrawler"]:
            self.assertNotIn(private_value, serialized)


if __name__ == "__main__":
    unittest.main()
