#!/usr/bin/env python3
from __future__ import annotations

from contextlib import redirect_stdout
from datetime import timedelta
import gzip
import hashlib
from io import BytesIO, StringIO
import json
from pathlib import Path
import threading
import time
import unittest
from unittest.mock import patch

import build_research_news_snapshot as builder

NOW = builder.utc("2026-09-08T02:00:00Z")
TEXT = "Artificial intelligence investment is expanding electricity demand as data center operators build new facilities and power infrastructure across several regions."


def raw(**changes):
    return {"date": "2026-09-08T01:31:00.000Z", "url": "https://example.org/energy-report", "domain": "example.org", "outletName": "Example News", "outletLogo": "https://example.org/logo.jpg", "outletTwitter": "example", "title": "AI investment expands electricity demand", "image": "https://example.org/photo.jpg", "desc": TEXT, "lang": "en", "author": "Reporter", **changes}


def record(**changes):
    return builder.normalize_record(raw(**changes), NOW)


def compressed(rows):
    return gzip.compress(("\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n").encode())


class Missing(Exception):
    response = {"Error": {"Code": "NoSuchKey"}}


class FakeR2:
    def __init__(self, previous=None, mismatch=False):
        self.content = json.dumps(previous).encode() if previous is not None else None
        self.operations = []
        self.mismatch = mismatch

    def get_object(self, **kwargs):
        self.operations.append(("get", kwargs))
        if self.content is None:
            raise Missing()
        content = self.content + (b" " if self.mismatch and any(op == "put" for op, _ in self.operations) else b"")
        return {"Body": BytesIO(content)}

    def put_object(self, **kwargs):
        self.operations.append(("put", kwargs))
        self.content = kwargs["Body"]


class SnapshotTests(unittest.TestCase):
    def test_verified_gal_schema_keeps_description_and_observation_time(self):
        item = record()
        self.assertEqual(item["summary"], TEXT)
        self.assertEqual(item["observed_at"], "2026-09-08T01:31:00Z")
        self.assertEqual(item["published_at"], "")
        self.assertEqual(item["id"], "news:" + hashlib.sha256(item["source_url"].encode()).hexdigest())
        self.assertEqual(item["provider"], "gdelt-gal")
        self.assertEqual(item["evidence_kind"], "news_description")
        self.assertFalse({"image", "author", "outletLogo", "outletTwitter"} & item.keys())

    def test_english_chinese_only_and_valid_description_required(self):
        for changes in ({"lang": "fr"}, {"desc": ""}, {"desc": "Short"}, {"desc": raw()["title"]}, {"desc": (raw()["title"] + ". ") * 5}, {"desc": ". " * 100}, {"date": ""}, {"date": "invalid"}, {"title": ""}):
            self.assertIsNone(record(**changes))
        chinese = record(lang="zh-Hant", title="人工智慧和電力需求", desc="人工智慧投資帶動資料中心與電力需求持續增加，各地企業正在評估新的基礎設施建設方案。" * 4)
        self.assertEqual(chinese["language"], "zh")
        self.assertLessEqual(len(record(desc=TEXT * 10)["summary"]), 700)

    def test_promo_and_unrelated_content_are_excluded(self):
        self.assertIsNone(record(desc="Register now for our artificial intelligence investment webinar. " * 3))
        self.assertIsNone(record(title="Football match", desc="The local football club won its match against a rival club following an impressive performance during the weekend championship."))

    def test_public_https_url_boundary(self):
        for url in ["http://example.org/news", "https://localhost/news", "https://a.local/news", "https://127.0.0.1/news", "https://[::1]/news", "https://user:pass@example.org/news", "https://example.org:8443/news", "javascript:alert(1)", "https://example.org", "https://host.internal/news", "https://example.org\\@localhost/news", "//example.org/news"]:
            self.assertEqual(builder.canonical_url(url), "", url)
        self.assertEqual(builder.canonical_url("https://Example.org/a?utm_campaign=foo&story=7#part"), "https://example.org/a?story=7")

    def test_xss_and_numeric_entities_are_cleaned(self):
        item = record(desc="<script>bad()</script>&lt;img src=x onerror=bad()&gt;" + TEXT + "&#8212;details", title="<b>AI</b> investment")
        self.assertNotIn("<", item["summary"])
        self.assertNotIn("bad()", item["summary"])
        self.assertIn("—details", item["summary"])
        self.assertEqual(item["title"], "AI investment")

    def test_gzip_stream_handles_arbitrary_chunk_boundaries_and_bad_lines(self):
        content = gzip.compress((json.dumps(raw()) + "\nnot-json\n" + json.dumps(raw(url="https://example.org/other"))).encode())
        rows = builder.decode_gal((content[index:index + 7] for index in range(0, len(content), 7)), NOW)
        self.assertEqual(len(rows), 2)
        self.assertEqual({row["summary"] for row in rows}, {TEXT})
        self.assertEqual(builder.decode_gal([compressed([raw(), raw()])], NOW), [record()])

    def test_streaming_size_limits_and_invalid_gzip(self):
        with patch.object(builder, "MAX_COMPRESSED", 20):
            with self.assertRaisesRegex(builder.SnapshotError, "compressed_limit"):
                builder.decode_gal([compressed([raw()])], NOW)
        with patch.object(builder, "MAX_DECOMPRESSED", 100):
            with self.assertRaisesRegex(builder.SnapshotError, "decompressed_limit"):
                builder.decode_gal([gzip.compress(b"x" * 100000)], NOW)
        for content in [b"not gzip", compressed([raw()])[:-5], compressed([raw()]) + compressed([raw()])]:
            with self.assertRaisesRegex(builder.SnapshotError, "invalid_gzip"):
                builder.decode_gal([content], NOW)

    def test_incremental_merge_expires_old_rows_and_deduplicates_urls(self):
        old = record()
        old["observed_at"] = "2026-08-01T00:00:00Z"
        prior = record(url="https://example.org/prior")
        fresh = record(url="https://example.org/energy-report?utm_source=new", date="2026-09-08T01:50:00Z")
        content, count = builder.make_snapshot({"items": [old, prior]}, [fresh], NOW)
        payload = json.loads(content)
        self.assertEqual(count, 2)
        self.assertEqual(payload["window_days"], 7)
        self.assertEqual(payload["items"][0]["observed_at"], "2026-09-08T01:50:00Z")
        self.assertEqual(payload["updated_at"], "2026-09-08T02:00:00Z")
        self.assertIsNone(record(date=builder.iso(NOW + timedelta(hours=1))))

    def test_snapshot_item_and_utf8_byte_limits(self):
        rows = [record(url=f"https://news{i}.org/story", desc=TEXT * 8) for i in range(1900)]
        content, count = builder.make_snapshot({"items": []}, rows, NOW)
        self.assertLessEqual(count, 1800)
        self.assertLessEqual(len(content), 2 * 1024 * 1024)
        with patch.object(builder, "MAX_SNAPSHOT_BYTES", 2500):
            content, count = builder.make_snapshot({"items": []}, rows, NOW)
            self.assertLessEqual(len(content), 2500)
            self.assertGreater(count, 0)

    def test_capture_uses_last_75_complete_minutes_at_most_six_workers(self):
        active = maximum = 0
        minutes = []
        lock = threading.Lock()
        def fetch(stamp, now):
            nonlocal active, maximum
            self.assertEqual(now, NOW)
            with lock:
                minutes.append(stamp)
                active += 1
                maximum = max(maximum, active)
            time.sleep(0.001)
            with lock:
                active -= 1
            return [record()]
        rows, stats = builder.collect_recent(NOW, fetcher=fetch)
        self.assertEqual(len(rows), 1)
        self.assertEqual(stats, {"requested_files": 75, "completed_files": 75, "failed_files": 0})
        self.assertLessEqual(maximum, 6)
        self.assertEqual(max(minutes), NOW - timedelta(minutes=1))
        self.assertEqual(min(minutes), NOW - timedelta(minutes=75))
        with self.assertRaises(builder.SnapshotError):
            builder.collect_recent(NOW, 76, fetcher=fetch)

    def test_no_new_data_never_reads_or_overwrites_r2(self):
        client = FakeR2({"schema_version": 1, "items": [record()]})
        previous = client.content
        result = builder.publish_snapshot(client, "bucket", [], NOW)
        self.assertEqual(result["status"], "skipped")
        self.assertEqual(client.operations, [])
        self.assertEqual(client.content, previous)

    def test_publish_verifies_exact_bytes_and_fails_on_mismatch(self):
        client = FakeR2()
        result = builder.publish_snapshot(client, "bucket", [record()], NOW)
        self.assertEqual(result["status"], "published")
        self.assertEqual([op for op, _ in client.operations], ["get", "put", "get"])
        self.assertTrue(all(args["Key"] == builder.KEY for _, args in client.operations))
        uploaded = client.operations[1][1]
        self.assertEqual(uploaded["Metadata"]["sha256"], hashlib.sha256(uploaded["Body"]).hexdigest())
        with self.assertRaisesRegex(builder.SnapshotError, "verify_failed"):
            builder.publish_snapshot(FakeR2(mismatch=True), "bucket", [record()], NOW)

    def test_corrupt_previous_snapshot_prevents_any_upload(self):
        client = FakeR2({"schema_version": 99, "items": []})
        with self.assertRaisesRegex(builder.SnapshotError, "schema_invalid"):
            builder.publish_snapshot(client, "bucket", [record()], NOW)
        self.assertEqual([op for op, _ in client.operations], ["get"])

    def test_404_is_empty_and_redirects_are_not_followed(self):
        class Connection:
            instances = []
            status = 404
            def __init__(self, host, timeout):
                self.host, self.timeout, self.sock = host, timeout, self
                self.calls = []
                self.instances.append(self)
            def connect(self): pass
            def settimeout(self, seconds): self.calls.append(("timeout", seconds))
            def request(self, method, path, headers): self.calls.append((method, path))
            def getresponse(self): return self
            def close(self): pass
        with patch.object(builder.http.client, "HTTPSConnection", Connection):
            self.assertEqual(builder.fetch_minute(NOW - timedelta(minutes=1), NOW), [])
            instance = Connection.instances[0]
            self.assertEqual(instance.host, "data.gdeltproject.org")
            self.assertEqual(instance.timeout, 12)
            self.assertIn(("GET", "/gdeltv3/gal/20260908015900.gal.json.gz"), instance.calls)
            Connection.status = 302
            with self.assertRaisesRegex(builder.SnapshotError, "upstream_status"):
                builder.fetch_minute(NOW, NOW)

    def test_body_stream_stops_when_total_request_deadline_expires(self):
        ticks = [0.0]
        class Connection:
            status = 200
            delay = 0
            def __init__(self, host, timeout):
                self.sock = self.transport_socket = self
                self.body = BytesIO(compressed([raw()]))
            def connect(self): pass
            def settimeout(self, seconds):
                self.asserted_timeout = seconds
            def request(self, method, path, headers): pass
            def getresponse(self): return self
            def getheader(self, name, default): return default
            def read1(self, count):
                ticks[0] += self.delay
                return self.body.read(count)
            def close(self): pass
        with patch.object(builder.http.client, "HTTPSConnection", Connection), patch.object(builder.time, "monotonic", side_effect=lambda: ticks[0]):
            self.assertEqual(builder.fetch_minute(NOW, NOW), [record()])
            Connection.delay = 13
            with self.assertRaisesRegex(builder.SnapshotError, "upstream_timeout"):
                builder.fetch_minute(NOW, NOW)

    def test_cli_logs_counts_without_article_text_or_urls(self):
        output = StringIO()
        with patch.object(builder, "collect_recent", return_value=([record()], {"requested_files": 75, "completed_files": 75, "failed_files": 0})), patch.dict(builder.os.environ, {"GITHUB_STEP_SUMMARY": ""}), redirect_stdout(output):
            self.assertEqual(builder.main([]), 0)
        self.assertNotIn(TEXT, output.getvalue())
        self.assertNotIn("https://", output.getvalue())
        self.assertEqual(json.loads(output.getvalue())["item_count"], 1)

    def test_workflow_is_separate_tests_before_capture_and_never_commits_payloads(self):
        workflow = Path(__file__).parents[1].joinpath(".github/workflows/research-news-refresh.yml").read_text()
        self.assertIn("group: research-news-snapshot", workflow)
        self.assertIn("cron: '17 * * * *'", workflow)
        self.assertLess(workflow.index("scripts/test_research_news_snapshot.py"), workflow.index("--lookback-minutes 75 --publish"))
        self.assertNotIn("git commit", workflow)
        self.assertNotIn("upload-artifact", workflow)
        self.assertIn("contents: read", workflow)


if __name__ == "__main__":
    unittest.main()
