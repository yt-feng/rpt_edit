"""Real recovered-source contracts, durable article progress and zero reparsing."""
from contextlib import ExitStack
import copy
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import recover_report_articles as articles
import pdf_to_xhs_batch as producer
import test_recover_durable_mineru_sources as mineru_fixture
import test_mineru_segmented_delivery as segment_fixture
import test_build_market_views_ocr_fallback as ocr_fixture
from wechat_editorial_binding import read_bound_article

TITLE = "国际清算银行：企业交付数量出现变化"
BODY = f"# {TITLE}\n\n本次样本记录了企业交付数量变化。\n\n## 企业样本提供交付证据\n\n企业产出保持稳定。\n"


class ArticleRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.args = producer.build_arg_parser().parse_args([])
        self.args.wechat_prompt_template = str(Path(__file__).resolve().parents[1] / self.args.wechat_prompt_template)
        self.calls = []

    def fixtures(self, cls):
        value = cls()
        value.setUp()
        self.addCleanup(value.doCleanups)
        return value

    def mineru(self, *, figures=False):
        fixture = self.fixtures(mineru_fixture.RecoveryTests)
        if figures:
            fixture.test_real_chart_wrapper_receipt_validates_fractional_page_status_map_and_proof()
        else:
            fixture.recover(recovery_execution_sha="b" * 40)
        return fixture

    def paid(self, *, fail_at=None):
        stack = ExitStack()
        def body(prompt, args, label, **kwargs):
            self.calls.append(prompt)
            if fail_at == len(self.calls):
                raise RuntimeError("PRIVATE model response must stay out of CLI")
            return BODY
        stack.enter_context(patch.object(producer, "safe_generate_text", side_effect=body))
        stack.enter_context(patch.object(producer, "wechat_title_from_filename", return_value=(TITLE, {
            "needs_model_repair": False, "selected_quality_issues": []})))
        for name in ("download_and_unzip", "run_source_batch", "download_cached_result", "mineru_tokens_from_env"):
            stack.enter_context(patch.object(producer, name, side_effect=AssertionError("MinerU must not run")))
        stack.enter_context(patch("requests.Session.request", side_effect=AssertionError("No external calls")))
        return stack

    def recover(self, fixture, *, expected=7, date="261003", kind="mineru-recovery", output=None, **kwargs):
        source = fixture.output if kind == "mineru-recovery" else fixture.root / "summaries" / "261005"
        return articles.recover_articles(source, kind, output or self.root / "articles", expected, date, self.args, **kwargs)

    def test_schema1_distinct_original_and_handoff_identity_and_zero_call_replay(self):
        fixture = self.mineru()
        source_before = articles.inventory(fixture.output)
        with self.paid():
            receipt = self.recover(fixture, source_run_id="123", source_execution_sha="a" * 40,
                source_handoff_run_id="456", source_handoff_execution_sha="b" * 40)
            self.assertEqual(len(self.calls), 7)
            before = articles.inventory(self.root / "articles")
            repeated = self.recover(fixture)
        self.assertEqual(receipt, repeated)
        self.assertEqual(len(self.calls), 7)
        self.assertEqual(articles.inventory(self.root / "articles"), before)
        self.assertEqual(articles.inventory(fixture.output), source_before)
        self.assertEqual((receipt["source_run_id"], receipt["source_handoff_run_id"]), ("123", "456"))
        self.assertEqual((receipt["source_execution_sha"], receipt["source_handoff_execution_sha"]), ("a" * 40, "b" * 40))
        self.assertEqual((receipt["complete"], receipt["report_count"]), (True, 7))
        self.assertTrue(all(row["editorial_binding"]["version"] == 2 for row in receipt["reports"]))
        self.assertEqual(fixture.provider.posts, [])

    def test_real_fractional_pdf_figures_survive_generation_and_strict_validation(self):
        fixture = self.mineru(figures=True)
        with self.paid():
            receipt = self.recover(fixture)
        root = self.root / "articles"
        self.assertEqual(articles.validate_articles(root, 7, "261003"), receipt)
        for row in receipt["reports"]:
            directory = root / row["directory"]
            status = articles.read_json(directory / "status.json")
            self.assertEqual(status["images"], ["assets/source_image_01.png"])
            self.assertEqual((directory / status["images"][0]).read_bytes(),
                             (fixture.output / row["directory"] / status["images"][0]).read_bytes())
            self.assertIn(status["images"][0], read_bound_article(directory).article)

    def test_schema2_40_real_pdfs_include_202_page_segmented_source_without_provider_calls(self):
        fixture = self.fixtures(segment_fixture.SegmentedDeliveryTests)
        source_receipt = fixture.recover(recovery_execution_sha="b" * 40)
        self.assertEqual(source_receipt["schema_version"], 2)
        self.assertEqual(source_receipt["reports"][36]["delivery"]["kind"], "page_segments")
        posts = copy.deepcopy(fixture.provider.posts)
        with self.paid(), patch.object(fixture.provider, "poll", side_effect=AssertionError("No provider GET required")):
            receipt = self.recover(fixture, expected=40, date="261009", source_run_id="123",
                source_handoff_run_id="456", source_execution_sha="a" * 40, source_handoff_execution_sha="b" * 40)
        self.assertEqual((receipt["report_count"], len(self.calls)), (40, 40))
        self.assertEqual(fixture.provider.posts, posts)
        directory = self.root / "articles" / receipt["reports"][36]["directory"]
        self.assertEqual(articles.read_json(directory / "status.json")["mineru_state"], "segmented_complete")

    def test_failure_checkpoints_completed_articles_and_resumes_only_missing_items(self):
        fixture = self.mineru()
        with self.paid(fail_at=3), self.assertRaises(articles.ArticleRecoveryError) as failure:
            self.recover(fixture)
        self.assertEqual(failure.exception.source_ordinal, 3)
        output = self.root / "articles"
        self.assertFalse((output / articles.RECEIPT).exists())
        self.assertEqual(sum(read_bound_article(path) is not None for path in output.glob("report_*")), 2)
        before = len(self.calls)
        with self.paid():
            receipt = self.recover(fixture)
        self.assertEqual(len(self.calls) - before, 5)
        self.assertEqual(receipt["report_count"], 7)

    def test_unknown_identity_missing_source_and_zero_count_fail_before_paid_call(self):
        fixture = self.mineru()
        for change in ({"source_run_id": "456"}, {"source_handoff_run_id": "123"},
                       {"source_execution_sha": "b" * 40}, {"source_handoff_execution_sha": "a" * 40},
                       {"expected": 0}, {"expected": 6}):
            with self.subTest(change=change), self.paid(), self.assertRaises(Exception):
                self.recover(fixture, **change)
            self.assertEqual(self.calls, [])
        report = next(fixture.output.glob("report_*"))
        (report / "source_mineru.md").write_text("unexpected extraction")
        with self.paid(), self.assertRaises(Exception):
            self.recover(fixture)
        self.assertEqual(self.calls, [])

    def test_changed_output_text_or_receipt_cannot_pass_even_with_fresh_inventory_hashes(self):
        fixture = self.mineru()
        with self.paid():
            receipt = self.recover(fixture)
        output = self.root / "articles"
        article = output / receipt["reports"][0]["directory"] / "wechat_article.md"
        article.write_text(BODY + "untracked content")
        receipt["files"] = articles.inventory(output, exclude=(articles.RECEIPT,))
        articles.write_json(output / articles.RECEIPT, receipt)
        with self.assertRaises(articles.ArticleRecoveryError):
            articles.validate_articles(output, 7, "261003")

    def test_new_recovery_bookkeeping_reuses_original_complete_package_byte_for_byte(self):
        fixture = self.mineru()
        with self.paid():
            receipt = self.recover(fixture)
        before = articles.inventory(self.root / "articles")
        source = articles.read_json(fixture.output / mineru_fixture.r.RECEIPT)
        source.update(recovery_run_id="999", recovery_execution_sha="d" * 40, provider_posts=0)
        articles.write_json(fixture.output / mineru_fixture.r.RECEIPT, source)
        with self.paid():
            second = self.recover(fixture, source_handoff_run_id="999", source_handoff_execution_sha="d" * 40)
        self.assertEqual(second, receipt)
        self.assertEqual(second["source_handoff_run_id"], "456")
        self.assertEqual(articles.inventory(self.root / "articles"), before)
        self.assertEqual(len(self.calls), 7)

    def ocr(self, *, partial=False):
        fixture = self.fixtures(ocr_fixture.OCRSynthesisTests)
        manifest = fixture.originals_fixture(count=2, pages=2)
        if partial:
            def extract(path, **kwargs):
                if path.name.startswith("02"):
                    raise ValueError("No source")
                return fixture.extract_fixture(path, **kwargs)
            fixture.build(manifest, count=2, extractor=extract)
        else:
            fixture.build(manifest, count=2)
        return fixture

    def test_real_ocr_receipt_uses_raw_page_text_not_summaries_and_distinct_binding(self):
        fixture = self.ocr()
        with self.paid():
            receipt = self.recover(fixture, expected=2, date="261005", kind="ocr-synthesis")
        self.assertEqual(receipt["report_count"], 2)
        self.assertEqual(len(self.calls), 2)
        self.assertTrue(all("cl0ud,7x 99 ocr?" in prompt and "LAST_PAGE_FACT" in prompt for prompt in self.calls))
        self.assertTrue(all("逐页完整整理报告观点" not in prompt for prompt in self.calls))
        for row in receipt["reports"]:
            directory = self.root / "articles" / row["directory"]
            self.assertFalse((directory / "source_mineru.md").exists())
            self.assertTrue((directory / "source_ocr_pages.json").is_file())
            status = articles.read_json(directory / "status.json")
            self.assertEqual((status["source_method"], status["image_source_kind"]), ("ocr", "ocr_reconstructed_chart"))
            self.assertEqual(read_bound_article(directory).binding["source_kind"], "ocr-synthesis")
        self.assertEqual(articles.validate_articles(self.root / "articles", 2, "261005"), receipt)

    def test_ocr_partial_and_rehashed_wrong_page_identity_reject_before_generation(self):
        fixture = self.ocr(partial=True)
        with self.paid(), self.assertRaisesRegex(articles.ArticleRecoveryError, "ocr_article_sources_incomplete"):
            self.recover(fixture, expected=2, date="261005", kind="ocr-synthesis")
        self.assertEqual(self.calls, [])
        full = self.ocr()
        root = full.root / "summaries" / "261005"
        path = root / "ocr_sources/R001/pages.json"
        pages = articles.read_json(path)
        pages[0]["page"] = 2
        articles.write_json(path, pages)
        source = articles.read_json(root / "ocr_synthesis_receipt.json")
        for item in source["files"]:
            if item["path"] == "ocr_sources/R001/pages.json":
                item.update(bytes=path.stat().st_size, sha256=articles.digest(path.read_bytes()))
        articles.write_json(root / "ocr_synthesis_receipt.json", source)
        with self.paid(), self.assertRaisesRegex(articles.ArticleRecoveryError, "ocr_page_evidence"):
            self.recover(full, expected=2, date="261005", kind="ocr-synthesis")
        self.assertEqual(self.calls, [])

    def test_real_cli_uses_all_four_producer_identity_arguments(self):
        fixture = self.mineru()
        command = ["recover", "--source-dir", str(fixture.output), "--source-kind", "mineru-recovery",
            "--output-dir", str(self.root / "cli"), "--expected-reports", "7", "--date-folder", "261003",
            "--source-run-id", "123", "--source-execution-sha", "a" * 40,
            "--source-handoff-run-id", "456", "--source-handoff-execution-sha", "b" * 40]
        with patch("sys.argv", command), self.paid():
            self.assertEqual(articles.main(), 0)
        articles.validate_articles(self.root / "cli", 7, "261003")
        with patch("sys.argv", command), self.paid(), patch.object(articles, "load_sources", side_effect=ValueError("PRIVATE")), \
                patch("sys.stderr", new_callable=io.StringIO) as errors:
            self.assertEqual(articles.main(), 2)
        self.assertNotIn("PRIVATE", errors.getvalue())

    def test_empty_model_body_never_becomes_a_complete_article_receipt(self):
        fixture = self.mineru()
        with self.paid(), patch.object(producer, "safe_generate_text", return_value=""), \
                self.assertRaisesRegex(articles.ArticleRecoveryError, "generated_article_unbound"):
            self.recover(fixture)
        self.assertFalse((self.root / "articles" / articles.RECEIPT).exists())

    def test_source_symlink_and_ocr_provenance_traversal_do_not_reach_generation(self):
        fixture = self.mineru()
        source = next(fixture.output.glob("report_*/source_mineru.md"))
        raw = source.read_bytes()
        saved = fixture.root / "external.md"
        saved.write_bytes(raw)
        source.unlink()
        source.symlink_to(saved)
        with self.paid(), self.assertRaisesRegex(articles.ArticleRecoveryError, "tree_symlink"):
            self.recover(fixture)
        self.assertEqual(self.calls, [])


if __name__ == "__main__":
    unittest.main()
