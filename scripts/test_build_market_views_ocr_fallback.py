from __future__ import annotations

import json
import copy
from pathlib import Path
import re
import tempfile
import threading
import unittest
from unittest.mock import patch

import fitz

import build_market_views_ocr_fallback as fallback


def page_record(number: int, text: str) -> dict:
    return {"page": number, "method": "ocr", "text": text,
            "text_sha256": fallback.sha(text.encode()), "empty_text": not bool(text)}


def model_fixture(prompt: str, model: str, url: str) -> dict:
    if prompt.startswith("market-cross-report-v1 "):
        from test_market_views_cross_report import model as final_model
        return final_model(prompt, model, url)
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

    def test_explicit_cache_only_replays_without_api_key_and_rejects_changed_ocr_settings(self):
        manifest = self.originals_fixture(count=2)
        self.build(manifest, count=2, ocr_all_pages=True)
        with patch.dict('os.environ', {'DEEPSEEK_API_KEY': ''}):
            resumed = self.build(manifest, count=2, ocr_all_pages=True,
                                 invoke=fallback.call_model, extractor=fallback.extract_pages, cache_only=True)
        self.assertEqual((resumed['summarized_reports'], resumed['skipped_reports']), (2, 0))
        for changed in [{'dpi': 221, 'ocr_all_pages': True}, {'languages': 'eng', 'ocr_all_pages': True},
                        {'ocr_all_pages': False}, {'ocr_all_pages': True, 'chunk_chars': 256}]:
            with self.subTest(changed=changed), patch.object(fallback.subprocess, 'run') as ocr, \
                 patch.object(fallback, 'request_with_retry') as provider:
                with self.assertRaisesRegex(ValueError, 'cache_only_(pages|summary)_missing'):
                    self.build(manifest, count=2, invoke=fallback.call_model, extractor=fallback.extract_pages,
                               cache_only=True, **changed)
                ocr.assert_not_called(); provider.assert_not_called()

    def test_cache_only_summary_binds_model_and_base_url(self):
        manifest = self.originals_fixture(count=1)
        self.build(manifest, count=1)
        for changed in [{'model': 'different-model'}, {'base_url': 'https://other.invalid'}]:
            with self.subTest(changed=changed), patch.object(fallback, 'request_with_retry') as provider:
                with self.assertRaisesRegex(ValueError, 'cache_only_summary_missing'):
                    self.build(manifest, count=1, cache_only=True, invoke=fallback.call_model, **changed)
                provider.assert_not_called()

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

    def test_pdf_access_stays_on_main_thread_while_model_requests_overlap(self):
        manifest = self.originals_fixture(count=2, pages=1)
        main_thread = threading.get_ident()
        open_threads, pixel_threads, extractor_threads, model_threads = [], [], [], []
        real_open, real_pixmap = fitz.open, fitz.Page.get_pixmap
        first_model_started = threading.Event()
        simultaneous_models = threading.Barrier(2, timeout=5)

        def tracked_open(*args, **kwargs):
            open_threads.append(threading.get_ident())
            self.assertEqual(threading.get_ident(), main_thread)
            return real_open(*args, **kwargs)

        def tracked_pixmap(page, *args, **kwargs):
            pixel_threads.append(threading.get_ident())
            self.assertEqual(threading.get_ident(), main_thread)
            return real_pixmap(page, *args, **kwargs)

        def reader(page, **kwargs):
            # Exercise the actual raster API used by full-page Tesseract OCR.
            page.get_pixmap(dpi=72)
            return "OCR source text with demand growth 3.4 and 5.6 percent."

        def extractor(path, **kwargs):
            extractor_threads.append(threading.get_ident())
            if path.name.startswith("02_"):
                # The first summary must already be running while the main
                # thread prepares the next PDF, rather than batching all OCR.
                self.assertTrue(first_model_started.wait(5))
            return fallback.extract_pages(path, reader=reader, **kwargs)

        def invoke(prompt, *args):
            if not prompt.startswith(("将以下全部研究", "market-cross-report-v1 ")):
                model_threads.append(threading.get_ident())
                first_model_started.set()
                simultaneous_models.wait()
            return model_fixture(prompt, *args)

        with patch.object(fitz, "open", tracked_open), patch.object(fitz.Page, "get_pixmap", tracked_pixmap):
            receipt = self.build(manifest, count=2, extractor=extractor, invoke=invoke, ocr_all_pages=True)
            self.assertEqual(receipt["summarized_reports"], 2)
            self.assertEqual(len(set(model_threads)), 2)
            self.assertNotIn(main_thread, model_threads)
            self.assertEqual(extractor_threads, [main_thread, main_thread])
            self.assertTrue(open_threads)
            self.assertTrue(pixel_threads)
            self.assertEqual(set(open_threads + pixel_threads), {main_thread})
            calls_before_cache_resume = len(open_threads)
            def unexpected(*args, **kwargs):
                raise AssertionError("Cached extraction or model call was repeated")
            resumed = self.build(manifest, count=2, extractor=unexpected, invoke=unexpected, ocr_all_pages=True)
            self.assertEqual(resumed["summarized_reports"], 2)
            # Cache hits still verify real original-PDF page counts, on main.
            self.assertGreater(len(open_threads), calls_before_cache_resume)
            self.assertEqual(set(open_threads + pixel_threads), {main_thread})

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

    def test_editorial_filter_removes_explicit_disclosures_not_research_words(self):
        legal = [
            "本页为研究报告的合规披露与分销声明，不含公司经营或财务分析内容。",
            "研究仅面向专业投资者，不构成投资建议或公开发行。",
            "分析师薪酬与集团整体盈利挂钩，可能存在利益冲突。",
            "评级分布：买入55%、中性40%、卖出6%。",
            "瑞银印度SEBI注册号：INH000001204。",
            "未经许可不得复制或转载本报告，版权归研究机构所有。",
            "报告日期：2026年10月5日", "原始文件SHA256：" + "a" * 64,
        ]
        research = [
            "公司收入预计同比增长15%，下调目标价至675美元，维持买入评级。",
            "监管政策暂停数据中心项目，影响行业产能增长。",
            "行业监管趋严，未来可能导致供给减少。",
            "投资风险包括客户需求下降、供应中断及毛利率承压。",
            "估值仍有吸引力，但需求恢复时间存在不确定性。",
            "该公司评级由买入降至中性，价格下跌可能反映需求担忧。",
            "监管机构限制公司生产，预计收入下降10%。",
            "Spotify版权成本仍然高企，长期内容授权是主要议价约束。",
            "公司版权内容库没有明显扩张，但预计订阅收入增长15%。",
            "报告认为英国监管机构可能阻止这项并购。",
            "公司正以法律手段追讨专利许可费，诉讼进展将影响竞争格局。",
        ]
        for text in legal:
            with self.subTest(text=text): self.assertTrue(fallback.boilerplate_only(text))
        for text in research:
            with self.subTest(text=text): self.assertFalse(fallback.boilerplate_only(text))

    def test_mixed_summary_keeps_research_and_later_page_facts(self):
        first = fallback.validate_summary({
            "title": "公司研究", "institution": "研究机构", "pages": [1],
            "summary": "数据中心增长前景大体不变。报告后部为法律声明。预计收入同比增长15%。",
            "key_points": ["监管政策暂停数据中心项目，影响行业产能增长。"],
            "data_points": ["毛利率为32.9%。"], "differences": ["投资风险包括客户需求下降。"]}, [1])
        second = fallback.validate_summary({
            "title": "研究附录", "pages": [2], "summary": "本页为法律声明，不含新增研究数据。",
            "key_points": ["后续订单预计增长20%。"], "data_points": [], "differences": []}, [2])
        original = copy.deepcopy([first, second])
        result = fallback.assemble_research([first, second])
        body = result["thesis"] + result["narrative"]
        for retained in ("增长前景大体不变", "收入同比增长15%", "监管政策暂停", "32.9%", "客户需求下降", "订单预计增长20%"):
            self.assertIn(retained, body)
        self.assertNotIn("法律声明", body)
        self.assertEqual([first, second], original)

    def test_typographic_dedup_keeps_decimal_sign_and_distinct_values(self):
        value = fallback.validate_summary({"title": "增长", "pages": [1],
            "summary": "公司营业收入增长 15%，毛利率为 32.9%。",
            "key_points": ["公司营业收入增长15%，毛利率为32.9%。", "公司营业收入增长15%，毛利率为32.9%！"],
            "data_points": ["另一口径为3.29%。", "另一口径为32.9%。", "利润变化-5%。", "利润变化+5%。"]}, [1])
        result = fallback.assemble_research([value, copy.deepcopy(value)])
        self.assertEqual(result["removed_duplicate_sentences"], 9)
        self.assertNotIn("公司营业收入", result["narrative"])
        for retained in ("3.29%", "32.9%", "-5%", "+5%"):
            self.assertIn(retained, result["narrative"])

    def test_pure_legal_chunk_and_coverage_chart_do_not_enter_public_body(self):
        value = model_fixture("；页码：[2]", "", "")
        value.update(summary="本页为法律声明，不含新增研究观点。",
                     key_points=["仅向专业投资者分发。", "联系地址：伦敦办公室。"],
                     differences=["不构成投资建议。"], data_points=["SEBI注册号：INH000001204。"])
        value["charts"][0]["title"] = "评级覆盖占比"
        result = fallback.assemble_research([value])
        self.assertEqual(result["charts"], [])
        self.assertNotIn("伦敦", result["narrative"])
        self.assertGreater(result["removed_boilerplate_sentences"], 3)

    def test_dedup_preserves_opposite_views_and_accounting_negative_parentheses(self):
        positive = "公司营业收入增长将带来经营利润率持续改善以及未来自由现金流回升。"
        value = fallback.validate_summary({"title": "盈利分歧", "pages": [1],
            "summary": "管理层不再预计" + positive,
            "key_points": [positive],
            "data_points": ["2026年公司净收益（5.1亿元）。", "2026年公司净收益5.1亿元。"]}, [1])
        result = fallback.assemble_research([value])
        self.assertIn("不再预计", result["thesis"])
        self.assertIn(positive, result["narrative"])
        self.assertIn("（5.1亿元）", result["narrative"])
        self.assertIn("净收益5.1亿元", result["narrative"])
        self.assertEqual(result["removed_duplicate_sentences"], 0)

    def test_legal_summary_never_discards_actual_chart_or_uncertain_research_point(self):
        value = model_fixture("；页码：[2]", "", "")
        value.update(summary="本页仅为免责声明。", key_points=["竞争格局发生变化，未来仍需观察。"],
                     differences=[], data_points=[])
        value["charts"][0]["title"] = "订阅收入预测"
        result = fallback.assemble_research([value])
        self.assertEqual(result["charts"], value["charts"])
        self.assertIn("竞争格局发生变化", result["thesis"] + result["narrative"])
        value["summary"] = "需求逐季恢复\n渠道补库加快"
        result = fallback.assemble_research([value])
        self.assertIn("恢复\n渠道", result["thesis"])

    def test_publication_cleanup_reuses_old_cache_and_preserves_private_page_coverage(self):
        manifest = self.originals_fixture(count=1, pages=3)
        def extractor(path, **kwargs):
            return [page_record(n, f"Original page {n}. " + "x" * 200) for n in (1, 2, 3)]
        def invoke(prompt, *args):
            value = model_fixture(prompt, *args)
            if prompt.startswith(("将以下全部研究", "market-cross-report-v1 ")):
                return value
            page = value["pages"][0]
            if page == 1:
                value.update(summary="公司计划以6.84亿港元收购57%股权。", key_points=["公司计划以6.84亿港元收购57%股权。"],
                             differences=[], data_points=[])
            elif page == 2:
                value.update(summary="本页为法律声明，不含新的市场观点。", key_points=["分析师认证与薪酬披露。"],
                             differences=[], data_points=["注册号：INH00001204。"], charts=[])
            else:
                value.update(summary="后部研究附录预计收入增长20%，毛利率为32.9%。", key_points=[],
                             differences=[], data_points=[])
            return value
        first = self.build(manifest, count=1, extractor=extractor, invoke=invoke, chunk_chars=256)
        directory = self.root / "summaries/261005"
        cache_before = {str(path): path.read_bytes() for path in (self.root / "cache").rglob("*.json")}
        private_before = {str(path): path.read_bytes() for path in (directory / "ocr_sources").rglob("*.json")}
        def unexpected(*args, **kwargs):
            raise AssertionError("No new OCR or model request during cached publication cleanup")
        second = self.build(manifest, count=1, extractor=unexpected, invoke=unexpected, chunk_chars=256)
        self.assertEqual(first["reports"], second["reports"])
        self.assertEqual(second["reports"][0]["pages_covered"], [1, 2, 3])
        self.assertEqual(second["reports"][0]["chunks_completed"], 3)
        self.assertEqual(cache_before, {str(path): path.read_bytes() for path in (self.root / "cache").rglob("*.json")})
        self.assertEqual(private_before, {str(path): path.read_bytes() for path in (directory / "ocr_sources").rglob("*.json")})
        structured = json.loads((directory / "market_views_structured.json").read_text())
        section = structured["bank_roundup"]["sections"][0]
        self.assertIn("6.84亿港元", section["bank_views"][0]["view"])
        self.assertEqual(structured["synthesis_mode"], "cross-report-v1")
        self.assertIn("收入增长20%", section["bank_views"][0]["view"])
        self.assertNotIn("法律声明", json.dumps(structured, ensure_ascii=False))
        self.assertIn("法律声明", (directory / "ocr_sources/R001/summaries.json").read_text())
        self.assertGreater(second["reports"][0]["publication_editing"]["removed_boilerplate_sentences"], 0)
        from market_views_publication import validate_ocr_synthesis_receipt
        validate_ocr_synthesis_receipt(directory, date_folder="261005", expected_reports=1,
            source_run_id="37388263555", execution_sha="a" * 40)
        self.assertEqual(fallback.PROMPT_VERSION, "complete-ocr-synthesis-v1")

    def test_publication_titles_institutions_and_charts_remove_metadata_without_changing_cache(self):
        manifest = self.originals_fixture(count=1, pages=1)
        def invoke(prompt, *args):
            value = model_fixture(prompt, *args)
            if prompt.startswith("market-cross-report-v1 "):
                return value
            value.update(title="Author: John Analyst", institution="Morgan Stanley analyst John, Tel: +1 212 555 0000, john@bank.com")
            value["key_points"] = ["作者：John Analyst", "Email: john@bank.com", "MS预计收入增长15%。"]
            value["charts"] = [{**value["charts"][0], "title": "Ratings distribution: Buy 55%, Sell 5%."},
                               {**value["charts"][0], "title": "Copyright licensing revenue is expected to grow 15%."}]
            return value
        self.build(manifest, count=1, invoke=invoke)
        output = self.root / "summaries/261005"
        report = json.loads((output / "report_inputs.json").read_text())[0]
        figures = json.loads((output / "figure_candidates.json").read_text())
        self.assertEqual(report["institution_name"], "摩根士丹利")
        self.assertEqual(report["title"], "R001 研究主题")
        self.assertEqual(len(figures), 1)
        self.assertIn("licensing revenue", figures[0]["label"])
        for value in (report, figures):
            text = json.dumps(value, ensure_ascii=False)
            for absent in ("John", "john@", "555", "Ratings distribution"):
                self.assertNotIn(absent, text)
        self.assertIn("John Analyst", (output / "ocr_sources/R001/summaries.json").read_text())

    def test_clean_qualitative_points_and_pure_legal_report_has_no_placeholder_chart(self):
        spec = {"kind": "qualitative", "title": "行业监管变化影响需求", "points": ["Author: John Analyst", "评级分布：买入55%。", "GS预计收入增长15%。"], "source_pages": [1]}
        cleaned = fallback.publication_chart(spec)
        self.assertEqual(cleaned["points"], ["GS预计收入增长15%。"])
        self.assertEqual(len(spec["points"]), 3)
        manifest = self.originals_fixture(count=1, pages=1)
        def legal(prompt, *args):
            value = model_fixture(prompt, *args)
            if not prompt.startswith("market-cross-report-v1 "):
                value.update(summary="Disclaimer: for institutional clients only.", key_points=[], differences=[], data_points=[], charts=[])
            return value
        receipt = self.build(manifest, count=1, invoke=legal)
        output = self.root / "summaries/261005"
        self.assertEqual(json.loads((output / "figure_candidates.json").read_text()), [])
        self.assertEqual(receipt["reports"][0]["pages_covered"], [1])

    def test_explicit_legal_summary_does_not_erase_real_numeric_chart(self):
        manifest = self.originals_fixture(count=1, pages=1)
        def mixed(prompt, *args):
            value = model_fixture(prompt, *args)
            if not prompt.startswith("market-cross-report-v1 "):
                value.update(summary="免责声明：仅供参考。", key_points=[], differences=[], data_points=[])
            return value
        self.build(manifest, count=1, invoke=mixed)
        figures = json.loads((self.root / "summaries/261005/figure_candidates.json").read_text())
        self.assertEqual(len(figures), 1)
        self.assertEqual(figures[0]["chart_spec"]["series"][0]["values"], [3.4, 5.6])

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
        self.assertEqual(sum(prompt.startswith("你是中文研究编辑") for prompt in calls), 1)
        self.assertGreater(sum(prompt.startswith("market-cross-report-v1 ") for prompt in calls), 0)
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
