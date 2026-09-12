"""Offline coverage for resumable Chinese report-title translation."""

from __future__ import annotations

import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import translate_portal_titles as titles


class TitleCheckpointTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.catalog_path = self.root / "catalog.json"
        self.cache_path = self.root / "cache-v1.json"
        self.model = titles.active_title_model()

    def write_catalog(self, items, **metadata):
        payload = {"schema_version": 1, "items": items, **metadata}
        titles.write_json(self.catalog_path, payload)
        return payload

    def catalog(self):
        return json.loads(self.catalog_path.read_text())

    def run_main(self, *arguments, model=None, api_key="test-key"):
        argv = ["translate_portal_titles.py", "--catalog-path", str(self.catalog_path),
                "--cache-path", str(self.cache_path), "--model", model or self.model,
                "--workers", "1", *arguments]
        with mock.patch.object(sys, "argv", argv), \
                mock.patch.dict(os.environ, {"DEEPSEEK_API_KEY": api_key}), \
                contextlib.redirect_stdout(io.StringIO()):
            return titles.main()

    def seed_cache(self, source="Report outlook", translation="报告展望"):
        cache = titles.load_title_cache(None)
        cache["entries"][titles.title_cache_key(source, self.model)] = {
            "source": source, "model": self.model, "prompt_version": titles.TITLE_PROMPT_VERSION,
            "title_zh": translation,
        }
        titles.write_json(self.cache_path, cache)

    def write_seed_catalog(self, items):
        path = self.root / "published-catalog.json"
        titles.write_json(path, {"items": items})
        return str(path)

    def test_published_seed_matches_public_normalization_and_keeps_raw_cache_source(self):
        source = "Reportify | GS：  Growth\u200b outlook"
        self.write_catalog([{"id": "report-one", "title": source, "available": True}])
        seed = self.write_seed_catalog([
            {"id": "report-one", "title": "GS: Growth outlook", "title_zh": "高盛增长展望",
             "available": False},
        ])
        with mock.patch.object(titles, "translate_title") as provider:
            self.assertEqual(self.run_main("--seed-catalog-path", seed, api_key=""), 0)
        provider.assert_not_called()
        self.assertEqual(self.catalog()["items"][0],
                         {"id": "report-one", "title": source, "title_zh": "高盛增长展望", "available": True})
        entry = titles.load_title_cache(self.cache_path)["entries"][titles.title_cache_key(source, self.model)]
        self.assertEqual(entry["source"], source)
        self.assertEqual(entry["title_zh"], "高盛增长展望")

        self.write_catalog([{"id": "report-one", "title": source}])
        with mock.patch.object(titles, "translate_title") as provider:
            self.assertEqual(self.run_main(), 0)
        provider.assert_not_called()
        self.assertEqual(self.catalog()["items"][0]["title_zh"], "高盛增长展望")

    def test_matching_id_alone_or_source_alone_cannot_seed_changed_report(self):
        for seed_rows in ([{"id": "one", "title": "Different source", "title_zh": "旧译文"}],
                          [{"id": "other-id", "title": "Report outlook", "title_zh": "旧译文"}],
                          [{"id": "one", "title": "Report outlook", "title_zh": " "}]):
            with self.subTest(seed=seed_rows):
                self.cache_path.unlink(missing_ok=True)
                self.write_catalog([{"id": "one", "title": "Report outlook"}])
                seed = self.write_seed_catalog(seed_rows)
                with mock.patch.object(titles, "translate_title", return_value="新译文") as provider:
                    self.assertEqual(self.run_main("--seed-catalog-path", seed), 0)
                provider.assert_called_once()
                self.assertEqual(self.catalog()["items"][0]["title_zh"], "新译文")

    def test_conflicting_seed_ids_or_sources_are_not_reused(self):
        conflicting_rows = [
            [{"id": "one", "title": "Report outlook", "title_zh": "译文一"},
             {"id": "one", "title": "Report outlook", "title_zh": "译文二"}],
            [{"id": "one", "title": "Report outlook", "title_zh": "译文一"},
             {"id": "one", "title": "Other report", "title_zh": "译文二"}],
            [{"id": "one", "title": "Report outlook", "title_zh": "译文一"},
             {"id": "two", "title": "Reportify | Report outlook", "title_zh": "译文二"}],
        ]
        for seed_rows in conflicting_rows:
            with self.subTest(seed=seed_rows):
                self.cache_path.unlink(missing_ok=True)
                self.write_catalog([{"id": "one", "title": "Report outlook"}])
                seed = self.write_seed_catalog(seed_rows)
                with mock.patch.object(titles, "translate_title", return_value="新译文") as provider:
                    self.assertEqual(self.run_main("--seed-catalog-path", seed), 0)
                provider.assert_called_once()
                self.assertEqual(self.catalog()["items"][0]["title_zh"], "新译文")

    def test_current_catalog_duplicate_ids_cannot_seed(self):
        self.write_catalog([{"id": "one", "title": "Report outlook"},
                            {"id": "one", "title": "Report outlook"}])
        seed = self.write_seed_catalog([{"id": "one", "title": "Report outlook", "title_zh": "旧译文"}])
        with mock.patch.object(titles, "translate_title", return_value="新译文") as provider:
            self.assertEqual(self.run_main("--seed-catalog-path", seed), 0)
        provider.assert_called_once()
        self.assertEqual([row["title_zh"] for row in self.catalog()["items"]], ["新译文", "新译文"])

    def test_seed_never_overwrites_existing_checkpoint_or_current_chinese_title(self):
        self.seed_cache()
        self.write_catalog([{"id": "one", "title": "Report outlook"},
                            {"id": "two", "title": "Reviewed report", "title_zh": "人工审核标题"}])
        seed = self.write_seed_catalog([
            {"id": "one", "title": "Report outlook", "title_zh": "较早发布标题"},
            {"id": "two", "title": "Reviewed report", "title_zh": "发布版本标题"},
        ])
        with mock.patch.object(titles, "translate_title") as provider:
            self.assertEqual(self.run_main("--seed-catalog-path", seed), 0)
        provider.assert_not_called()
        self.assertEqual([row["title_zh"] for row in self.catalog()["items"]], ["报告展望", "人工审核标题"])
        self.assertEqual(len(titles.load_title_cache(self.cache_path)["entries"]), 1)

    def test_seed_is_checkpointed_before_later_provider_failure(self):
        self.write_catalog([{"id": "one", "title": "Report outlook"},
                            {"id": "two", "title": "New report"}])
        seed = self.write_seed_catalog([{"id": "one", "title": "Report outlook", "title_zh": "已发布译文"}])
        with mock.patch.object(titles, "translate_title", side_effect=RuntimeError("provider unavailable")) as provider:
            self.assertEqual(self.run_main("--seed-catalog-path", seed, "--fail-on-error"), 1)
        provider.assert_called_once()
        self.assertEqual(provider.call_args.args[0], "New report")
        entry = titles.load_title_cache(self.cache_path)["entries"][titles.title_cache_key("Report outlook", self.model)]
        self.assertEqual(entry["title_zh"], "已发布译文")

    def test_repeat_run_reuses_checkpoint_without_provider_or_credentials(self):
        self.write_catalog([{"id": "old", "title": "Report outlook"}])
        with mock.patch.object(titles, "translate_title", return_value="报告展望") as provider:
            self.assertEqual(self.run_main(), 0)
        provider.assert_called_once()

        # Simulate a new checkout with the same untranslated title.
        self.write_catalog([{"id": "old", "title": "Report outlook"}])
        with mock.patch.object(titles, "translate_title") as provider:
            self.assertEqual(self.run_main(api_key=""), 0)
        provider.assert_not_called()
        self.assertEqual(self.catalog()["items"][0]["title_zh"], "报告展望")
        self.assertEqual(self.catalog()["title_translation"]["last_run_cached"], 1)
        self.assertEqual(self.catalog()["title_translation"]["last_run_translated"], 0)

    def test_exact_source_changes_require_new_translation(self):
        for source in ("Report outlook!", "report outlook", " Report outlook "):
            with self.subTest(source=source):
                self.seed_cache()
                self.write_catalog([{"id": "same-report", "title": source}])
                with mock.patch.object(titles, "translate_title", return_value="更新后的报告展望") as provider:
                    self.assertEqual(self.run_main(), 0)
                provider.assert_called_once()
                entries = titles.load_title_cache(self.cache_path)["entries"]
                self.assertEqual(len(entries), 2)
                self.assertEqual(entries[titles.title_cache_key(source, self.model)]["source"], source)

    def test_legacy_model_cli_cannot_switch_back_to_paid_provider(self):
        self.seed_cache()
        self.write_catalog([{"id": "same-report", "title": "Report outlook"}])
        with mock.patch.object(titles, "translate_title") as provider:
            self.assertEqual(self.run_main(model="deepseek-v4-flash"), 0)
        provider.assert_not_called()
        self.assertEqual(self.catalog()["items"][0]["title_zh"], "报告展望")

    def test_prompt_change_does_not_reuse_or_erase_old_entries(self):
        for changed_model, changed_prompt in ((self.model, "portal-title-zh-v2"),):
            with self.subTest(model=changed_model, prompt=changed_prompt):
                self.seed_cache()
                self.write_catalog([{"id": "same-report", "title": "Report outlook"}])
                with mock.patch.object(titles, "TITLE_PROMPT_VERSION", changed_prompt), \
                        mock.patch.object(titles, "translate_title", return_value="新翻译") as provider:
                    self.assertEqual(self.run_main(model=changed_model), 0)
                provider.assert_called_once()
                self.assertEqual(len(titles.load_title_cache(self.cache_path)["entries"]), 2)

    def test_exact_legacy_deepseek_result_survives_offline_switch(self):
        cache = {"schema_version": 1, "provider": "deepseek", "entries": {}}
        source = "Report outlook"
        legacy_model = "deepseek-v4-flash"
        key = titles.title_cache_key(source, legacy_model)
        cache["entries"][key] = {"source": source, "model": legacy_model,
                                 "prompt_version": titles.TITLE_PROMPT_VERSION, "title_zh": "已付费的报告展望"}
        titles.write_json(self.cache_path, cache)
        self.write_catalog([{"id": "same-report", "title": source}])
        with mock.patch.object(titles, "translate_title") as provider:
            self.assertEqual(self.run_main(api_key=""), 0)
        provider.assert_not_called()
        self.assertEqual(self.catalog()["items"][0]["title_zh"], "已付费的报告展望")
        self.assertIn(key, titles.load_title_cache(self.cache_path)["entries"])

    def test_conflicting_or_unknown_legacy_results_cannot_migrate(self):
        for rows in (("deepseek-v4-flash", "deepseek-chat"), ("unrelated-model",)):
            cache = {"schema_version": 1, "provider": "deepseek", "entries": {}}
            for index, model in enumerate(rows):
                cache["entries"][titles.title_cache_key("Report outlook", model)] = {
                    "source": "Report outlook", "model": model,
                    "prompt_version": titles.TITLE_PROMPT_VERSION, "title_zh": f"旧翻译{index}"}
            titles.write_json(self.cache_path, cache)
            self.write_catalog([{"id": "report", "title": "Report outlook"}])
            with mock.patch.object(titles, "translate_title", return_value="本地新译文") as provider:
                self.assertEqual(self.run_main(api_key=""), 0)
            provider.assert_called_once()
            self.assertEqual(self.catalog()["items"][0]["title_zh"], "本地新译文")
            row = titles.load_title_cache(self.cache_path)["entries"][titles.title_cache_key("Report outlook", self.model)]
            self.assertEqual(row["provider"], "argos-offline")

    def test_cache_only_fills_missing_titles_and_preserves_current_catalog(self):
        self.seed_cache()
        payload = self.write_catalog([
            {"id": "new-report-id", "title": "Report outlook", "date_folder": "260909",
             "available": True, "pages": 17, "new_metadata": {"revision": 3}},
            {"id": "reviewed", "title": "Report outlook", "title_zh": "人工审核的最新标题"},
            {"id": "new-record", "title": "New report", "title_zh": "新报告"},
        ], updated_at_bjt="2026-09-09 18:00:00", item_count=3)
        with mock.patch.object(titles, "translate_title") as provider:
            self.assertEqual(self.run_main(), 0)
        provider.assert_not_called()
        result = self.catalog()
        result.pop("title_translation")
        payload["items"][0]["title_zh"] = "报告展望"
        self.assertEqual(result, payload)

    def test_partial_success_survives_failure_and_next_run_only_retries_missing(self):
        original = [{"id": "ok", "title": "Successful report"},
                    {"id": "fail", "title": "Failing report"}]
        self.write_catalog(original)

        def translate(source, _args):
            if source == "Failing report":
                raise RuntimeError("temporary provider failure")
            return "已完成报告"

        with mock.patch.object(titles, "translate_title", side_effect=translate):
            self.assertEqual(self.run_main("--fail-on-error"), 1)
        self.assertEqual(len(titles.load_title_cache(self.cache_path)["entries"]), 1)
        self.assertEqual(self.catalog()["items"][0]["title_zh"], "已完成报告")
        self.assertNotIn("title_zh", self.catalog()["items"][1])

        self.write_catalog(original)
        with mock.patch.object(titles, "translate_title", return_value="补全报告") as provider:
            self.assertEqual(self.run_main("--fail-on-error"), 0)
        provider.assert_called_once()
        self.assertEqual(provider.call_args.args[0], "Failing report")
        self.assertEqual([row["title_zh"] for row in self.catalog()["items"]], ["已完成报告", "补全报告"])

    def test_completed_title_is_checkpointed_before_a_later_interruption(self):
        self.write_catalog([{"id": "one", "title": "First report"},
                            {"id": "two", "title": "Second report"}])
        before = self.catalog_path.read_bytes()

        def interrupt_after_first(futures):
            yield next(iter(futures))
            raise KeyboardInterrupt()

        with mock.patch.object(titles, "translate_title", return_value="已完成报告"), \
                mock.patch.object(titles.concurrent.futures, "as_completed", interrupt_after_first):
            with self.assertRaises(KeyboardInterrupt):
                self.run_main()
        self.assertEqual(self.catalog_path.read_bytes(), before)
        cache = titles.load_title_cache(self.cache_path)
        self.assertEqual(cache["entries"][titles.title_cache_key("First report", self.model)]["title_zh"],
                         "已完成报告")

    def test_successful_checkpoint_survives_catalog_write_failure(self):
        self.write_catalog([{"id": "one", "title": "First report"}])
        write_json = titles.write_json

        def fail_catalog(path, data):
            if path == self.catalog_path:
                raise OSError("catalog write interrupted")
            write_json(path, data)

        with mock.patch.object(titles, "translate_title", return_value="已完成报告"), \
                mock.patch.object(titles, "write_json", side_effect=fail_catalog):
            with self.assertRaisesRegex(OSError, "catalog write interrupted"):
                self.run_main()
        self.assertEqual(len(titles.load_title_cache(self.cache_path)["entries"]), 1)
        with mock.patch.object(titles, "translate_title") as provider:
            self.assertEqual(self.run_main(), 0)
        provider.assert_not_called()

    def test_failed_atomic_replacement_keeps_previous_checkpoint(self):
        self.seed_cache()
        before = self.cache_path.read_bytes()
        with mock.patch.object(Path, "replace", side_effect=OSError("replacement interrupted")):
            with self.assertRaisesRegex(OSError, "replacement interrupted"):
                titles.write_json(self.cache_path, {"incomplete": True})
        self.assertEqual(self.cache_path.read_bytes(), before)
        self.assertEqual(list(self.root.glob("*.tmp")), [])
        self.assertEqual(len(titles.load_title_cache(self.cache_path)["entries"]), 1)

    def test_corrupt_cache_is_not_silently_overwritten_or_retranslated(self):
        self.write_catalog([{"id": "one", "title": "First report"}])
        self.cache_path.write_text('{"schema_version":1,"provider":"deepseek","entries":{"bad":{}}}')
        before = self.cache_path.read_bytes()
        with mock.patch.object(titles, "translate_title") as provider:
            with self.assertRaisesRegex(RuntimeError, "Invalid title translation cache entry"):
                self.run_main()
        provider.assert_not_called()
        self.assertEqual(self.cache_path.read_bytes(), before)

    def test_duplicate_source_is_translated_once_for_all_current_reports(self):
        self.write_catalog([{"id": "one", "title": "Same report"},
                            {"id": "two", "title": "Same report"}])
        with mock.patch.object(titles, "translate_title", return_value="同一报告") as provider:
            self.assertEqual(self.run_main(), 0)
        provider.assert_called_once()
        self.assertEqual([row["title_zh"] for row in self.catalog()["items"]], ["同一报告", "同一报告"])

    def test_explicit_force_retranslates_and_updates_checkpoint(self):
        self.seed_cache()
        self.write_catalog([{"id": "one", "title": "Report outlook", "title_zh": "已有标题"}])
        with mock.patch.object(titles, "translate_title", return_value="明确要求的新标题") as provider:
            self.assertEqual(self.run_main("--force"), 0)
        provider.assert_called_once()
        self.assertEqual(self.catalog()["items"][0]["title_zh"], "明确要求的新标题")
        self.assertEqual(titles.load_title_cache(self.cache_path)["entries"][
            titles.title_cache_key("Report outlook", self.model)]["title_zh"], "明确要求的新标题")

    def test_dry_run_does_not_mutate_catalog_or_checkpoint(self):
        self.seed_cache()
        self.write_catalog([{"id": "one", "title": "New report"}])
        before = (self.catalog_path.read_bytes(), self.cache_path.read_bytes())
        with mock.patch.object(titles, "translate_title", return_value="新报告"):
            self.assertEqual(self.run_main("--dry-run"), 0)
        self.assertEqual((self.catalog_path.read_bytes(), self.cache_path.read_bytes()), before)


if __name__ == "__main__":
    unittest.main()
