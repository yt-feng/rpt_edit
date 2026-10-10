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
        self.model = titles.MODEL_ID

    def test_direct_title_translation_uses_offline_model_without_key(self):
        from argparse import Namespace
        args = Namespace(model="deepseek-v4-pro")
        with mock.patch.dict(os.environ, {}, clear=True), \
                mock.patch.object(titles, "OfflineTranslator") as factory:
            factory.return_value.translate.return_value = "报告展望"
            self.assertEqual(titles.translate_title("Report outlook", args), "报告展望")
            titles.translate_title("Another report", args)
        factory.assert_called_once()
        factory.return_value.translate.assert_called_with("Another report", target="zh", source="en", markdown=False)

    def test_title_identifiers_are_exact_but_financial_assertion_stays_in_model_context(self):
        from argparse import Namespace
        from hymt_offline_translation import OfflineTranslator
        engine = mock.Mock()
        engine.translate.return_value = '__KC_PH_0002__-示例__KC_PH_0000__2026年第四季度增长12.5%__KC_PH_0001__'
        translator = OfflineTranslator(cache_dir=self.root / 'memo', engine_factory=lambda *_: engine)
        source = 'Citi-Example（2338.HK）4Q26 growth 12.5%-260918'
        result = titles.translate_title(source, Namespace(_offline_translator=translator))
        self.assertEqual(result, '花旗-示例（2338.HK）2026年第四季度增长12.5%-260918')
        self.assertEqual(engine.translate.call_args.args[0],
                         '__KC_PH_0002__-Example__KC_PH_0000__4Q26 growth 12.5%__KC_PH_0001__')

    def test_mixed_title_keeps_source_language_from_before_identifier_protection(self):
        from argparse import Namespace
        from hymt_offline_translation import OfflineTranslator
        source = '中海油(CNOOC.US) ESG Update-260918'
        protected, _identifiers = titles.protect_title_identifiers(source)
        self.assertEqual(titles._detect_source(source), 'en')
        self.assertEqual(titles._detect_source(protected), 'zh')
        engine = mock.Mock()
        engine.translate.return_value = '中海油__KC_PH_0000__ESG更新__KC_PH_0001__'
        translator = OfflineTranslator(cache_dir=self.root / 'memo', engine_factory=lambda *_: engine)
        result = titles.translate_title(source, Namespace(_offline_translator=translator))
        self.assertEqual(result, '中海油(CNOOC.US)ESG更新-260918')
        engine.translate.assert_called_once_with(protected, 'en', 'zh')

    def test_identifier_mask_never_protects_amounts_years_or_invalid_calendar_suffixes(self):
        source = 'Outlook (2026): earnings -5%, debt USD 120 million, plants (12)-260230'
        self.assertEqual(titles.protect_title_identifiers(source), (source, {}))
        protected, identifiers = titles.protect_title_identifiers('Example（002050） FY26 outlook-20260918')
        self.assertEqual(list(identifiers.values()), ['（002050）', '-20260918'])
        self.assertIn('FY26', protected)

    def test_rejected_title_model_output_is_available_only_for_explicit_diagnostics(self):
        from argparse import Namespace
        from hymt_offline_translation import OfflineTranslator, OfflineTranslationError
        engine = mock.Mock()
        engine.translate.return_value = '增长15%'
        calls = []
        translator = OfflineTranslator(cache_dir=self.root / 'memo', engine_factory=lambda *_: engine,
                                       diagnostic_callback=calls.append)
        args = Namespace(_offline_translator=translator, _offline_title_calls=calls,
                         diagnostics_out=self.root / 'diagnostics.json')
        with self.assertRaises(OfflineTranslationError) as caught:
            titles.translate_title('Growth 12.5%', args)
        self.assertEqual(caught.exception.translation_diagnostics[0]['raw_translation'], '增长15%')
        self.assertFalse(list((self.root / 'memo').rglob('*.json')))

    def test_failures_write_resumable_opt_in_diagnostic_artifact(self):
        self.write_catalog([{'id': 'bad', 'title': 'Growth 12.5%'},
                            {'id': 'good', 'title': 'Market outlook'}])
        diagnostics = self.root / 'diagnostics.json'
        error = RuntimeError('quantity rejected')
        error.translation_diagnostics = [{'model_input': 'Growth 12.5%', 'raw_translation': '增长15%'}]
        with mock.patch.object(titles, 'translate_title', side_effect=[error, '市场展望']):
            self.assertEqual(self.run_main('--diagnostics-out', str(diagnostics), '--fail-on-error'), 1)
        self.assertEqual(json.loads(diagnostics.read_text())['failed_titles'], [{
            'ids': ['bad'], 'source': 'Growth 12.5%', 'error': 'quantity rejected',
            'model_calls': error.translation_diagnostics,
        }])
        self.assertEqual(len(titles.load_title_cache(self.cache_path)['entries']), 1)

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

    def test_model_and_prompt_changes_do_not_reuse_or_erase_old_entries(self):
        for changed_model, changed_prompt in (("another-model", titles.TITLE_PROMPT_VERSION),
                                             (self.model, "portal-title-zh-v2")):
            with self.subTest(model=changed_model, prompt=changed_prompt):
                self.seed_cache()
                self.write_catalog([{"id": "same-report", "title": "Report outlook"}])
                with mock.patch.object(titles, "TITLE_PROMPT_VERSION", changed_prompt), \
                        mock.patch.object(titles, "MODEL_ID", changed_model), \
                        mock.patch.object(titles, "translate_title", return_value="新翻译") as provider:
                    self.assertEqual(self.run_main(model=changed_model), 0)
                provider.assert_called_once()
                self.assertEqual(len(titles.load_title_cache(self.cache_path)["entries"]), 2)

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

    def test_default_partial_failure_publishes_original_and_only_retries_missing_translation(self):
        from build_portal_suite_site import item_display_title
        original = [{'id': 'ok', 'title': 'Successful report'},
                    {'id': 'fail', 'title': 'Growth 12.5%', 'available': True}]
        self.write_catalog(original)
        with mock.patch.object(titles, 'translate_title', side_effect=[
                '已完成报告', RuntimeError('Hy-MT2 quantity validation failed')]):
            self.assertEqual(self.run_main(), 0)
        catalog = self.catalog()
        self.assertEqual(catalog['title_translation']['last_run_failed'], 1)
        self.assertEqual(catalog['title_translation']['last_run_translated'], 1)
        self.assertEqual(catalog['items'][1], original[1])
        self.assertEqual(item_display_title(catalog['items'][1]), 'Growth 12.5%')
        self.assertEqual(catalog['items'][0]['title_zh'], '已完成报告')
        entries = titles.load_title_cache(self.cache_path)['entries']
        self.assertEqual(len(entries), 1)
        self.assertNotIn(titles.title_cache_key('Growth 12.5%', self.model), entries)
        with mock.patch.object(titles, 'translate_title', return_value='增长12.5%') as provider:
            self.assertEqual(self.run_main(), 0)
        provider.assert_called_once()
        self.assertEqual(provider.call_args.args[0], 'Growth 12.5%')
        self.assertEqual(self.catalog()['items'][1]['title_zh'], '增长12.5%')

    def test_completed_title_is_checkpointed_before_a_later_interruption(self):
        self.write_catalog([{"id": "one", "title": "First report"},
                            {"id": "two", "title": "Second report"}])
        before = self.catalog_path.read_bytes()

        with mock.patch.object(titles, "translate_title", side_effect=["已完成报告", KeyboardInterrupt()]):
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

    def test_real_offline_deadline_defers_without_fake_cache_and_resumes_new_titles_first(self):
        import hymt_offline_translation as offline
        from build_portal_suite_site import item_display_title
        original = [
            {'id': 'historical', 'title': 'Historical difficult report', 'date_folder': '261009'},
            {'id': 'new-first', 'title': 'Fresh market report', 'date_folder': '261008'},
            {'id': 'new-second', 'title': 'Fresh sector report', 'date_folder': '261007'},
            {'id': 'new-duplicate', 'title': 'Fresh sector report', 'date_folder': '261007'},
            {'id': 'checkpoint', 'title': 'Report outlook', 'date_folder': '260701'},
            {'id': 'published', 'title': 'Published report', 'date_folder': '260701'},
        ]
        self.write_catalog(original)
        self.seed_cache()
        seed = self.write_seed_catalog([
            {'id': 'historical', 'title': 'Historical difficult report', 'title_zh': ''},
            {'id': 'published', 'title': 'Published report', 'title_zh': '已发布报告'},
        ])
        engine = object.__new__(offline._HyMTEngine)
        engine.port = 1
        translator = offline.OfflineTranslator(cache_dir=self.root / 'memo', engine_factory=lambda *_: engine)
        clock = [100.0]
        requests = []

        def request(_port, _route, payload, timeout):
            requests.append((payload['messages'][0]['content'], timeout))
            if len(requests) == 1:
                clock[0] += 1
                return {'choices': [{'finish_reason': 'stop', 'message': {'content': '最新市场报告'}}]}
            clock[0] += timeout
            raise TimeoutError('runner model reached its remaining budget')

        diagnostics = self.root / 'diagnostics.json'
        with mock.patch.object(titles, 'OfflineTranslator', return_value=translator), \
                mock.patch.object(offline, 'request_json', side_effect=request), \
                mock.patch.object(titles.time, 'monotonic', side_effect=lambda: clock[0]):
            self.assertEqual(self.run_main('--seed-catalog-path', seed, '--time-budget-seconds', '3',
                                           '--diagnostics-out', str(diagnostics), '--fail-on-error'), 0)
        self.assertEqual(len(requests), 2)
        self.assertTrue(requests[0][0].endswith('Fresh market report'))
        self.assertTrue(requests[1][0].endswith('Fresh sector report'))
        self.assertEqual([row[1] for row in requests], [3, 2])
        catalog = self.catalog()
        self.assertEqual(catalog['title_translation']['last_run_deferred'], 3)
        self.assertEqual(catalog['title_translation']['last_run_failed'], 0)
        self.assertEqual(catalog['items'][1]['title_zh'], '最新市场报告')
        self.assertEqual(catalog['items'][4]['title_zh'], '报告展望')
        self.assertEqual(catalog['items'][5]['title_zh'], '已发布报告')
        for index in (0, 2, 3):
            self.assertEqual(catalog['items'][index], original[index])
            self.assertEqual(item_display_title(catalog['items'][index]), original[index]['title'])
        entries = titles.load_title_cache(self.cache_path)['entries']
        self.assertEqual(len(entries), 3)
        for title in ('Fresh sector report', 'Historical difficult report'):
            self.assertNotIn(titles.title_cache_key(title, self.model), entries)
        self.assertEqual(json.loads(diagnostics.read_text())['deferred_title_count'], 3)

        # A fresh runner reuses every completed seed/checkpoint and retries only
        # unfinished exact sources, including one call for duplicated reports.
        self.write_catalog(original)
        with mock.patch.object(titles, 'translate_title', side_effect=['最新行业报告', '历史报告']) as model:
            self.assertEqual(self.run_main('--seed-catalog-path', seed, '--time-budget-seconds', '3'), 0)
        self.assertEqual([call.args[0] for call in model.call_args_list],
                         ['Fresh sector report', 'Historical difficult report'])
        self.assertEqual(self.catalog()['title_translation']['last_run_deferred'], 0)
        self.assertEqual(len(titles.load_title_cache(self.cache_path)['entries']), 5)

    def test_expired_budget_still_applies_all_reusable_titles_without_starting_model(self):
        self.write_catalog([{'id': 'new', 'title': 'New report'},
                            {'id': 'cache', 'title': 'Report outlook'},
                            {'id': 'seed', 'title': 'Published report'}])
        self.seed_cache()
        seed = self.write_seed_catalog([{'id': 'seed', 'title': 'Published report', 'title_zh': '已发布报告'}])
        with mock.patch.object(titles.time, 'monotonic', side_effect=[100, 280]), \
                mock.patch.object(titles, 'OfflineTranslator') as factory:
            self.assertEqual(self.run_main('--seed-catalog-path', seed), 0)
        factory.assert_not_called()
        self.assertEqual([row.get('title_zh') for row in self.catalog()['items']], [None, '报告展望', '已发布报告'])
        self.assertEqual(self.catalog()['title_translation']['last_run_deferred'], 1)
        self.assertEqual(len(titles.load_title_cache(self.cache_path)['entries']), 2)

    def test_budget_expiring_after_success_keeps_checkpoint_and_does_not_queue_next_title(self):
        self.write_catalog([{'id': 'first', 'title': 'First report'}, {'id': 'second', 'title': 'Second report'}])
        with mock.patch.object(titles.time, 'monotonic', side_effect=[100, 100, 280]), \
                mock.patch.object(titles, 'translate_title', return_value='首篇报告') as model:
            self.assertEqual(self.run_main(), 0)
        model.assert_called_once()
        self.assertEqual(self.catalog()['items'][0]['title_zh'], '首篇报告')
        self.assertNotIn('title_zh', self.catalog()['items'][1])
        self.assertEqual(self.catalog()['title_translation']['last_run_deferred'], 1)
        self.assertEqual(len(titles.load_title_cache(self.cache_path)['entries']), 1)

    def test_invalid_budget_is_rejected_before_catalog_or_checkpoint_changes(self):
        self.write_catalog([{'id': 'one', 'title': 'First report'}])
        before = self.catalog_path.read_bytes()
        for value in ('0', '-1', 'nan', 'inf'):
            with self.subTest(value=value), contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit) as error:
                    self.run_main('--time-budget-seconds', value)
                self.assertEqual(error.exception.code, 2)
                self.assertEqual(self.catalog_path.read_bytes(), before)
                self.assertFalse(self.cache_path.exists())

    def test_production_title_work_has_a_budget_and_manual_resume_stays_inference_free(self):
        from build_portal_locale_resume_workflow import SOURCE, TARGET, generate
        source = SOURCE.read_text()
        step = source.split('      - name: Translate missing report titles\n', 1)[1].split('      - name:', 1)[0]
        self.assertIn('--time-budget-seconds 180', step)
        self.assertNotIn('--fail-on-error', step)
        self.assertEqual(TARGET.read_text(), generate(source))
        self.assertNotIn('scripts/translate_portal_titles.py', TARGET.read_text())


if __name__ == "__main__":
    unittest.main()
