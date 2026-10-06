from __future__ import annotations

import json
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import patch

import fitz

import build_market_views_ocr_fallback as fallback


def page_record(number: int, text: str) -> dict:
    return {"page": number, "method": "ocr", "text": text,
            "text_sha256": fallback.sha(text.encode()), "empty_text": not bool(text)}


def model_fixture(prompt: str, model: str, url: str) -> dict:
    if prompt.startswith("将以下全部研究"):
        return {"executive_summary": ["全球需求温和修复，资本开支与盈利增长存在分化。"], "closing": "后续观察需求与盈利兑现。"}
    pages = json.loads(re.search(r"；页码：(\[[^\n]+\])", prompt).group(1))
    return {"title": "需求、盈利与资本开支", "institution": "研究机构", "pages": pages,
            "summary": "逐页完整整理报告观点，包括后部数据与条件差异。" + ("尾页事实保留。" if "LAST_PAGE_FACT" in prompt else ""),
            "key_points": ["需求扩张存在行业差异", "新增供给需要时间消化"],
            "differences": ["盈利改善取决于价格与销量"], "data_points": ["2024 年约 3.4%，2025 年约 5.6%。"],
            "charts": [{"kind": "bar", "title": "需求增速比较", "unit": "%", "labels": ["2024", "2025"],
                        "series": [{"name": "需求增速", "values": [3.4, 5.6]}], "source_pages": [pages[-1]]}]}


class OCRSynthesisTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.originals = self.root / "originals"
        self.originals.mkdir()

    def originals_fixture(self, count=3, pages=2):
        manifest = []
        for index in range(1, count + 1):
            path = self.originals / f"{index:02d}_Research.pdf"
            with fitz.open() as doc:
                for number in range(1, pages + 1):
                    page = doc.new_page()
                    page.insert_text((50, 60), f"Source {index}, page {number}. " + "Market demand and earnings. " * 10)
                doc.save(path)
            manifest.append({"process_local_path": "/selected/" + path.name, "content_sha256": fallback.sha(path.read_bytes())})
        path = self.root / "manifest.json"
        path.write_text(json.dumps(manifest))
        return path

    def extract_fixture(self, path, **kwargs):
        with fitz.open(path) as doc:
            count = doc.page_count
        return [page_record(number, ("cl0ud,7x 99 ocr? " if number == 1 else "LAST_PAGE_FACT ") + "正文内容与完整数据。" * 45)
                for number in range(1, count + 1)]

    def build(self, manifest, count=3, **kwargs):
        return fallback.build(self.originals, manifest, count, "261005", self.root / "summaries", self.root / "cache",
                              source_run_id="37388263555", execution_sha="a" * 40, workers=2,
                              invoke=kwargs.pop("invoke", model_fixture), extractor=kwargs.pop("extractor", self.extract_fixture), **kwargs)

    def test_long_page_and_empty_page_chunks_do_not_drop_a_character(self):
        pages = [page_record(1, "a" * 513), page_record(2, ""), page_record(3, "TAIL" * 123)]
        chunks = fallback.chunk_pages(pages, 256)
        for page in pages:
            spans = [part for chunk in chunks for part in chunk["segments"] if part["page"] == page["page"]]
            self.assertEqual("".join(part["text"] for part in spans), page["text"])
            self.assertEqual(spans[0]["start"], 0)
            self.assertEqual(spans[-1]["end"], len(page["text"]))
        self.assertEqual({p for chunk in chunks for p in chunk["pages"]}, {1, 2, 3})

    def test_image_on_text_page_is_also_full_page_ocr(self):
        path = self.originals / "mixed.pdf"
        with fitz.open() as doc:
            page = doc.new_page()
            page.insert_text((50, 50), "Native text " * 20)
            image = fitz.Pixmap(fitz.csRGB, fitz.IRect(0, 0, 20, 20), False)
            image.clear_with(230)
            page.insert_image(fitz.Rect(40, 100, 140, 200), pixmap=image)
            doc.save(path)
        calls = []
        rows = fallback.extract_pages(path, reader=lambda page, **kw: calls.append(page.number) or "图中数据 5.6%")
        self.assertEqual(calls, [0])
        self.assertIn("图中数据", rows[0]["text"])
        self.assertEqual(rows[0]["method"], "native+ocr")

    def test_garbled_structure_is_sent_to_model_and_last_page_survives(self):
        manifest = self.originals_fixture()
        seen = []
        def invoke(prompt, *args):
            seen.append(prompt)
            return model_fixture(prompt, *args)
        receipt = self.build(manifest, invoke=invoke, chunk_chars=256)
        self.assertEqual(receipt["summarized_reports"], 3)
        self.assertTrue(any("cl0ud,7x 99 ocr?" in prompt for prompt in seen))
        self.assertTrue(any("LAST_PAGE_FACT" in prompt for prompt in seen))
        summary_dir = self.root / "summaries/261005"
        reports = json.loads((summary_dir / "report_inputs.json").read_text())
        self.assertTrue(all("尾页事实保留" in report["extract"] for report in reports))
        for row in receipt["reports"]:
            self.assertEqual(row["pages_covered"], [1, 2])
            self.assertEqual(row["chunk_count"], row["chunks_completed"])
        for record in receipt["files"]:
            self.assertEqual(fallback.sha((summary_dir / record["path"]).read_bytes()), record["sha256"])

    def test_third_bad_pdf_does_not_stop_remaining_30_selected_sources(self):
        manifest = self.originals_fixture(count=33, pages=1)
        attempted = []
        def extractor(path, **kwargs):
            attempted.append(path.name)
            if path.name.startswith("03_"):
                raise ValueError("unreadable page 4")
            return self.extract_fixture(path)
        receipt = self.build(manifest, count=33, extractor=extractor)
        self.assertEqual(len(attempted), 33)
        self.assertEqual(receipt["attempted_reports"], 33)
        self.assertEqual(receipt["summarized_reports"], 32)
        self.assertEqual(receipt["skipped_reports"], 1)
        self.assertEqual(receipt["reports"][2]["status"], "skipped")
        self.assertEqual(receipt["reports"][-1]["status"], "summarized")
        summary = json.loads((self.root / "summaries/261005/market_views_structured.json").read_text())
        self.assertEqual(summary["skipped_reports"][0]["source_pdf"], "03_Research.pdf")
        self.assertIn("32/33", summary["subtitle"])

    def test_all_skipped_is_not_success(self):
        manifest = self.originals_fixture()
        with self.assertRaisesRegex(RuntimeError, "No selected PDF"):
            self.build(manifest, extractor=lambda *a, **kw: (_ for _ in ()).throw(ValueError("failed OCR")))
        receipt = json.loads((self.root / "summaries/261005" / fallback.RECEIPT_NAME).read_text())
        self.assertFalse(receipt["complete"])
        self.assertEqual(receipt["attempted_reports"], 3)

    def test_provider_credential_failure_is_global_not_a_green_partial(self):
        manifest = self.originals_fixture()
        def unavailable(*args):
            raise fallback.ProviderConfigurationError("DeepSeek synthesis HTTP 402")
        with self.assertRaises(fallback.ProviderConfigurationError):
            self.build(manifest, invoke=unavailable)
        self.assertFalse((self.root / "summaries/261005" / fallback.RECEIPT_NAME).exists())

    def test_complete_cache_resumes_without_model_submission(self):
        manifest = self.originals_fixture(count=1)
        first = self.build(manifest, count=1)
        def unexpected(*args):
            raise AssertionError("A cached paid request was resubmitted")
        second = self.build(manifest, count=1, invoke=unexpected)
        self.assertEqual(first["reports"], second["reports"])

    def test_changed_original_sha_does_not_reuse_old_model_results(self):
        manifest = self.originals_fixture(count=1)
        self.build(manifest, count=1)
        source = self.originals / "01_Research.pdf"
        source.write_bytes(source.read_bytes() + b"\n% changed original revision\n")
        bindings = json.loads(manifest.read_text())
        bindings[0]["content_sha256"] = fallback.sha(source.read_bytes())
        manifest.write_text(json.dumps(bindings))
        calls = []
        def changed_source(prompt, *args):
            calls.append(prompt)
            return model_fixture(prompt, *args)
        self.build(manifest, count=1, invoke=changed_source)
        self.assertEqual(len(calls), 2)
        self.assertIn(bindings[0]["content_sha256"], calls[0])

    def test_uncertain_request_is_not_blindly_repeated(self):
        calls = []
        def timeout(*args):
            calls.append(1)
            raise TimeoutError("unknown provider completion")
        with self.assertRaises(TimeoutError):
            fallback.cached_model("test", self.root / "cache", "model", "https://api.deepseek.com", timeout)
        with self.assertRaisesRegex(RuntimeError, "unknown/incomplete outcome"):
            fallback.cached_model("test", self.root / "cache", "model", "https://api.deepseek.com", timeout)
        self.assertEqual(len(calls), 1)

    def test_real_client_wrapper_records_usage_and_never_retries_timeout(self):
        import requests
        from unittest.mock import Mock
        response = Mock(status_code=200)
        response.json.return_value = {"choices": [{"message": {"content": '{"ok":true}'}}],
                                      "usage": {"prompt_tokens": 12, "completion_tokens": 3, "total_tokens": 15}}
        usage = self.root / "usage"
        with patch.dict("os.environ", {"DEEPSEEK_API_KEY": "fixture-only", "DEEPSEEK_USAGE_DIR": str(usage)}):
            with patch("deepseek_http.requests.post", return_value=response) as post:
                self.assertEqual(fallback.call_model("private fixture text", "deepseek-flash", "https://api.deepseek.com"), {"ok": True})
                self.assertEqual(post.call_count, 1)
            events = [json.loads(path.read_text()) for path in usage.rglob("*.json")]
            self.assertEqual(events[0]["usage"]["total_tokens"], 15)
            self.assertNotIn("private fixture text", json.dumps(events))
            with patch("deepseek_http.requests.post", side_effect=requests.exceptions.Timeout("unknown")) as post:
                with self.assertRaises(requests.exceptions.Timeout):
                    fallback.call_model("fixture", "deepseek-flash", "https://api.deepseek.com")
                self.assertEqual(post.call_count, 1)

    def test_incomplete_model_chunk_skips_only_that_report(self):
        manifest = self.originals_fixture(count=3)
        def incomplete(prompt, *args):
            value = model_fixture(prompt, *args)
            if "文件：02_Research.pdf" in prompt:
                value["pages"] = []
            return value
        receipt = self.build(manifest, invoke=incomplete)
        self.assertEqual(receipt["summarized_reports"], 2)
        self.assertEqual([row["status"] for row in receipt["reports"]], ["summarized", "skipped", "summarized"])

    def test_manifest_missing_extra_or_tampered_pdf_is_rejected(self):
        manifest = self.originals_fixture(count=1)
        with (self.originals / "01_Research.pdf").open("ab") as stream:
            stream.write(b"tampered")
        with self.assertRaisesRegex(ValueError, "SHA"):
            self.build(manifest, count=1)

    def test_chart_shape_and_page_origin_checked_without_numeric_thresholds(self):
        chart = model_fixture("；页码：[1]", "", "")["charts"][0]
        chart["series"][0]["values"] = [-171.25, 1.71]
        self.assertIsNotNone(fallback.chart_spec(chart, [1]))
        for values in ([True, 1], [float("nan"), 1], [1]):
            chart["series"][0]["values"] = values
            self.assertIsNone(fallback.chart_spec(chart, [1]))
        chart["series"][0]["values"] = [1, 2]
        self.assertIsNone(fallback.chart_spec(chart, [2]))

    def test_missing_numeric_chart_becomes_qualitative_not_invented_series(self):
        manifest = self.originals_fixture(count=1)
        def no_chart(prompt, *args):
            value = model_fixture(prompt, *args)
            value["charts"] = []
            return value
        self.build(manifest, count=1, invoke=no_chart)
        figures = json.loads((self.root / "summaries/261005/figure_candidates.json").read_text())
        self.assertEqual(figures[0]["chart_spec"]["kind"], "qualitative")
        self.assertNotIn("series", figures[0]["chart_spec"])

    def test_normal_renderer_embeds_font_and_shows_skipped_inventory(self):
        from render_market_views_reportlab_pdf import build_pdf
        manifest = self.originals_fixture(count=2)
        def extractor(path, **kwargs):
            if path.name.startswith("02_"):
                raise ValueError("cannot parse")
            return self.extract_fixture(path)
        self.build(manifest, count=2, extractor=extractor)
        directory = self.root / "summaries/261005"
        output = directory / "market_views_261005.pdf"
        build_pdf(directory, output)
        with fitz.open(output) as document:
            text = "".join(page.get_text() for page in document)
            self.assertIn("02_Research.pdf", text)
            self.assertIn("正文重绘图表", text)
            self.assertIn("尾页事实保留", text)
            self.assertNotIn("正文原始图表", text)
            fonts = [font for page in document for font in page.get_fonts()]
            self.assertTrue(any(document.extract_font(font[0])[3] for font in fonts if "Droid" in font[3]))
        self.assertGreater(output.stat().st_size, 20000)


if __name__ == "__main__":
    unittest.main()
