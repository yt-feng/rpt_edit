from __future__ import annotations

import json
import base64
import math
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sync_bbg_show_blog as sync


SHOW_PATH = "rendered-clips/2026-09-07/highlight_plan.json"
OLD_PATH = "rendered-clips/top-videos/2026-09-02/example/highlight_plan.json"


def sample_clip() -> dict:
    return {
        "title": "收益率与增长", "speaker": "Example speaker", "start": 10, "end": 15,
        "secret": "private editorial prompt", "local_path": "/Users/private/file.mp4",
        "subtitles": [{"start": 10, "end": 15, "en": "Bond yields changed.", "zh": "原始中文",
                       "zh_filtered": "债券收益率出现变化。", "speaker_context": "private background"}],
    }


class FakeReader:
    def __init__(self, invalid=False):
        clip = sample_clip()
        if invalid:
            clip["subtitles"][0]["en"] = ""
        self.snapshots = {
            "new": {SHOW_PATH: {"clips": [sample_clip()]}},
            "old": {SHOW_PATH: {"clips": [dict(sample_clip(), title="旧标题")]},
                    OLD_PATH: {"source_url": "https://www.bloomberg.com/news/videos/example", "clips": [clip]}},
        }

    def revisions(self, ref, since):
        return ["new", "old"]

    def plans(self, ref):
        return {path: "fake-hash" for path in self.snapshots[ref]}

    def read_json(self, ref, path, optional=False):
        if optional:
            return {"SHOW_URL": "https://www.bloomberg.com/news/videos/2026-09-07/china-show", "OUTPUT_DIR": "/private/work"}
        return self.snapshots[ref][path]


class BBGBlogSyncTest(unittest.TestCase):
    def test_contract_preserves_bilingual_pairs_and_excludes_internal_metadata(self):
        clip = sample_clip()
        row = sync.clip_article(clip, {}, {"SHOW_URL": "https://www.bloomberg.com/news/videos/show"}, SHOW_PATH)
        self.assertEqual(set(row), {"schema_version", "id", "slug", "date", "title", "speaker", "category", "source_url", "start", "end", "segments"})
        self.assertEqual(row["segments"], [{"start": 10.0, "end": 15.0, "en": "Bond yields changed.", "zh": "债券收益率出现变化。"}])
        self.assertEqual(len(row["id"]), 64)
        self.assertTrue(row["slug"].startswith("bbg-20260907-"))
        encoded = json.dumps(row)
        self.assertNotIn("private", encoded)
        self.assertNotIn("local_path", encoded)
        revised = dict(clip, title="更新标题")
        self.assertEqual(row["id"], sync.clip_article(revised, {}, {"SHOW_URL": row["source_url"]}, SHOW_PATH)["id"])

    def test_invalid_bilingual_or_timestamp_data_is_rejected(self):
        for field, value in (("en", ""), ("start", math.nan), ("end", 10), ("start", -2), ("end", 30)):
            clip = sample_clip()
            clip["subtitles"][0][field] = value
            with self.assertRaises(sync.ImportErrorDetail):
                sync.clip_article(clip, {}, {"SHOW_URL": "https://www.bloomberg.com/video"}, SHOW_PATH)
        for value in ("https://bloomberg.com.evil.test/video", "file:///private.mp4", "http://www.bloomberg.com/video", "https://name:password@www.bloomberg.com/video"):
            with self.assertRaises(sync.ImportErrorDetail):
                sync.source_url(value)
        self.assertEqual(sync.source_url("https://www.youtube.com/watch?v=abc&token=private#fragment"), "https://www.youtube.com/watch?v=abc")
        self.assertEqual(sync.source_url("https://www.bloomberg.com/video?token=private"), "https://www.bloomberg.com/video")

    def test_history_restores_cleaned_paths_but_latest_revision_wins_and_reruns_are_idempotent(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp)
            reader = FakeReader()
            first = sync.sync_archive(reader, "main", date(2026, 9, 1), date(2026, 9, 7), output)
            self.assertEqual(first["articles"], 2)
            self.assertEqual(first["added"], 2)
            self.assertEqual(first["dates"], ["2026-09-02", "2026-09-07"])
            self.assertEqual(first["plans_read"], 2)
            self.assertEqual(first["clip_records"], 2)
            self.assertEqual(first["duplicate_clips"], 0)
            self.assertTrue(all(json.loads(path.read_text())["title"] == "收益率与增长" for path in output.glob("*.json")))
            second = sync.sync_archive(reader, "main", date(2026, 9, 1), date(2026, 9, 7), output)
            self.assertEqual(second["unchanged"], 2)
            self.assertEqual(second["added"], 0)

    def test_republication_retains_existing_permalink(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp)
            reader = FakeReader()
            sync.sync_archive(reader, "main", date(2026, 9, 1), date(2026, 9, 7), output)
            target = next(path for path in output.glob("*.json") if json.loads(path.read_text())["category"] == "shows")
            previous = json.loads(target.read_text())
            previous["date"] = "2026-09-06"
            previous["slug"] = "bbg-20260906-" + previous["id"][:16]
            target.write_text(json.dumps(previous))
            sync.sync_archive(reader, "main", date(2026, 9, 1), date(2026, 9, 7), output)
            revised = json.loads(target.read_text())
            self.assertEqual(revised["date"], "2026-09-06")
            self.assertEqual(revised["slug"], previous["slug"])

    def test_invalid_batch_never_partially_writes_and_skip_is_explicit(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "archive"
            with self.assertRaises(sync.ImportErrorDetail):
                sync.sync_archive(FakeReader(invalid=True), "main", date(2026, 9, 1), date(2026, 9, 7), output)
            self.assertFalse(output.exists())
            result = sync.sync_archive(FakeReader(invalid=True), "main", date(2026, 9, 1), date(2026, 9, 7), output, skip_invalid=True)
            self.assertEqual(result["skipped_invalid_clips"], 1)
            self.assertEqual(result["articles"], 1)

    def test_github_mode_reads_only_plan_and_source_metadata(self):
        class MockGitHub(sync.GitHubReader):
            def __init__(self):
                super().__init__("yt-feng/bbg-show")
                self.requests = []

            def request_json(self, path):
                self.requests.append(path)
                if path == "commits/main":
                    return {"sha": "head"}
                if path.startswith("commits?"):
                    return []
                if path == "git/trees/head?recursive=1":
                    return {"tree": [
                        {"type": "blob", "path": SHOW_PATH, "sha": "plan"},
                        {"type": "blob", "path": SHOW_PATH.replace("highlight_plan.json", "show.json"), "sha": "show"},
                        {"type": "blob", "path": "rendered-clips/2026-09-07/movie.mp4", "sha": "media"},
                    ]}
                if path.startswith("contents/"):
                    payload = {"clips": [sample_clip()]} if "highlight_plan.json" in path else {"SHOW_URL": "https://www.bloomberg.com/video"}
                    return {"encoding": "base64", "content": base64.b64encode(json.dumps(payload).encode()).decode()}
                raise AssertionError("unexpected request")

        with tempfile.TemporaryDirectory() as temp:
            reader = MockGitHub()
            result = sync.sync_archive(reader, "main", date(2026, 9, 1), date(2026, 9, 7), Path(temp))
            self.assertEqual(result["articles"], 1)
            self.assertFalse(any("mp4" in path for path in reader.requests))
            self.assertEqual(reader.requests.count("git/trees/head?recursive=1"), 1)

    def test_all_history_resolves_latest_path_versions_without_a_date_log_cutoff(self):
        class HistoryGit(sync.GitReader):
            def git(self, *args):
                if args[0] == "rev-parse":
                    return b"new\n"
                if args[0] == "log":
                    self.log_args = args
                    return f"COMMIT:new\n{SHOW_PATH}\nCOMMIT:old\n{SHOW_PATH}\n{OLD_PATH}\n".encode()
                raise AssertionError("unexpected source read")
        reader = HistoryGit(Path("/unused"))
        sources, revisions = reader.all_plan_sources("main")
        self.assertEqual(sources, [(SHOW_PATH, "new"), (OLD_PATH, "old")])
        self.assertEqual(revisions, 2)
        self.assertFalse(any(arg.startswith("--since") for arg in reader.log_args))
        self.assertIn("--no-renames", reader.log_args)

    def test_skip_invalid_never_masks_a_git_or_network_failure(self):
        class FailingReader(FakeReader):
            def read_json(self, ref, path, optional=False):
                if path == OLD_PATH:
                    raise sync.SourceReadError("source failed")
                return super().read_json(ref, path, optional)
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "archive"
            with self.assertRaises(sync.SourceReadError):
                sync.sync_archive(FailingReader(), "main", date(2026, 9, 1), date(2026, 9, 7), output, skip_invalid=True, read_workers=2)
            self.assertFalse(output.exists())

    def test_existing_archive_validation_finishes_before_any_update(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp)
            reader = FakeReader()
            sync.sync_archive(reader, "main", date(2026, 9, 1), date(2026, 9, 7), output)
            files = sorted(output.glob("*.json"))
            broken = json.loads(files[-1].read_text())
            broken["date"] = "2026-02-31"
            files[-1].write_text(json.dumps(broken))
            before = {path: path.read_bytes() for path in files}
            for snapshot in reader.snapshots.values():
                for plan in snapshot.values():
                    plan["clips"][0]["title"] = "修订标题"
            with self.assertRaises(sync.ImportErrorDetail):
                sync.sync_archive(reader, "main", date(2026, 9, 1), date(2026, 9, 7), output)
            self.assertEqual({path: path.read_bytes() for path in files}, before)

    def test_duplicate_clips_and_empty_plans_are_reported_separately_from_invalid_data(self):
        reader = FakeReader()
        reader.snapshots["new"][SHOW_PATH]["clips"].append(sample_clip())
        reader.snapshots["old"][OLD_PATH]["clips"] = []
        with tempfile.TemporaryDirectory() as temp:
            result = sync.sync_archive(reader, "main", date(2026, 9, 1), date(2026, 9, 7), Path(temp))
            self.assertEqual(result["clip_records"], 2)
            self.assertEqual(result["articles"], 1)
            self.assertEqual(result["duplicate_clips"], 1)
            self.assertEqual(result["empty_plans"], 1)
            self.assertEqual(result["skipped_invalid_clips"], 0)


if __name__ == "__main__":
    unittest.main()
