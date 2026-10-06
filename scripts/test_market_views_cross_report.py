"""Offline cross-report coverage, budgets and final-cache recovery contracts."""
import copy
import json
from pathlib import Path
import tempfile
import threading
import time
import unittest
from unittest.mock import patch

import market_views_cross_report as cross
from build_market_views_ocr_fallback import boilerplate_only


def fixture(count=33):
    results, reports, figures = [], [], []
    names = ["Global Economic Weekly", "Treasuries", "Active managers holdings", "Agricultural sugar",
             "Battery energy storage", "Semiconductors", "Spotify Internet", "Asian Autos", "Luxury Prada", "Therapeutics"]
    for index in range(count):
        rid = f"R{index + 1:03d}"
        summaries = [{"title": names[index % len(names)], "institution": "JPM" if index % 2 else "GS",
            "summary": f"第{page}页实际研究观点：企业收入增长{index + 5}%，后续需求受资本开支影响。",
            "key_points": [f"第{page}页的条件差异保留。"], "differences": [], "data_points": [], "pages": [page], "charts": []}
            for page in [1, 40]]
        results.append({"id": rid, "content_sha256": str(index % 10) * 64, "summaries": summaries})
        reports.append({"id": rid, "title": summaries[0]["title"], "source_pdf": names[index % len(names)] + ".pdf", "institution_name": summaries[0]["institution"]})
        figures.append({"figure_id": f"F{index + 1:03d}", "report_id": rid, "label": "收入增长", "source_pages": [40]})
    return results, reports, figures


def model(prompt, *_):
    marker, payload = prompt.split("\n", 1)[0], json.loads(prompt[prompt.rfind("\n") + 1:])
    if marker.endswith("EVIDENCE"):
        return {"claims": [{"text": row["text"] or "该块无新增研究信息。", "evidence_ids": [row["id"]]} for row in payload]}
    if marker.endswith("PLAN"):
        return {"categories": [{"heading": "宏观与资产配置", "report_ids": [row["id"] for row in payload[::2]]},
                               {"heading": "产业与盈利", "report_ids": [row["id"] for row in payload[1::2]]}]} if len(payload) > 1 else {"categories": [{"heading": "综合研究", "report_ids": [payload[0]["id"]]}]}
    if marker.endswith("SECTION"):
        ids = [row["id"] for row in payload["reports"]]
        groups = [ids[index::4] for index in range(min(4, len(ids)))]
        views = []
        for group in groups:
            cards = [card for card in payload["evidence"] if card["sources"][0]["report_id"] in group]
            text = "；".join(card["text"] for card in cards)
            if len(text) > 500:
                text = "；".join(rid + "：收入增长并受资本开支制约，尾页仍需观察需求。" for rid in group)
            views.append({"bank": "GS / JPM", "view": text, "report_ids": group,
                          "evidence_ids": [eid for card in cards for eid in card["evidence_ids"]]})
        return {"thesis": "盈利修复与资本开支节奏分化，需要区分需求和估值。", "consensus": ["机构共同关注需求兑现。"],
            "divergences": ["不同报告对修复时间的条件判断不同。"], "catalysts": ["后续订单与收入数据。"],
            "data_points": ["所引报告记录各行业收入增速。"], "bank_views": views,
            "figure_ids": [row["figure_id"] for row in payload["figures"][:3]]}
    return {"executive_summary": ["宏观与盈利节奏分化，关注订单和投资。"], "closing": "以来源证据跟踪关键变量。"}


class CrossReportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.cache = Path(self.temp.name)

    def run_synthesis(self, data=None, invoke=model):
        return cross.synthesize(*(data or fixture()), cache_dir=self.cache, model="fixture", base_url="https://example.invalid",
                                invoke=invoke, is_boilerplate=boilerplate_only)

    def test_all_33_reports_compressed_into_topics_with_tail_evidence_and_sources(self):
        result, audit = self.run_synthesis()
        sections = result["bank_roundup"]["sections"]
        self.assertEqual(len(sections), 2)
        self.assertEqual(result["synthesis_status"], "model")
        self.assertEqual(len(audit["evidence"]), 66)
        self.assertEqual({row["pages"][0] for row in audit["evidence"]}, {1, 40})
        self.assertEqual(sorted(rid for section in sections for rid in section["references"]), [f"R{i:03d}" for i in range(1, 34)])
        for section in sections:
            self.assertLessEqual(len(section["figure_ids"]), 3)
            self.assertLessEqual(len(section["bank_views"]), 4)
            cited = {row["report_id"] for view in section["bank_views"] for row in view["sources"]}
            self.assertEqual(cited, set(section["references"]))
            self.assertTrue(all(40 in source["pages"] for view in section["bank_views"] for source in view["sources"]))

    def test_complete_final_cache_replay_uses_zero_model_calls(self):
        first, audit = self.run_synthesis()
        self.assertGreater(audit["metrics"]["model_submissions"], 0)
        def forbidden(*_): raise AssertionError("must not charge again")
        second, resumed = self.run_synthesis(invoke=forbidden)
        self.assertEqual(first, second)
        self.assertEqual(resumed["metrics"]["model_submissions"], 0)
        self.assertGreater(resumed["metrics"]["cache_hits"], 0)

    def test_unknown_model_submission_falls_back_and_never_reposts(self):
        calls = []
        def unknown(prompt, *_): calls.append(prompt); raise TimeoutError("private provider response")
        first, audit = self.run_synthesis(invoke=unknown)
        before = len(calls)
        second, resumed = self.run_synthesis(invoke=unknown)
        self.assertEqual(len(calls), before)
        self.assertEqual(first, second)
        self.assertEqual(resumed["metrics"]["model_submissions"], 0)
        self.assertEqual(len(first["bank_roundup"]["sections"]), 10)
        self.assertEqual(len({rid for section in first["bank_roundup"]["sections"] for rid in section["references"]}), 33)
        self.assertNotIn("private provider response", json.dumps(audit))
        for section in first["bank_roundup"]["sections"]:
            self.assertEqual(section["consensus"], [])
            self.assertEqual(section["divergences"], [])
            self.assertLessEqual(sum(len(view["view"]) for view in section["bank_views"]), 2000)

    def test_invalid_plan_missing_or_duplicate_report_uses_complete_deterministic_plan(self):
        def invalid(prompt, *args):
            if prompt.split("\n", 1)[0].endswith("PLAN"):
                return {"categories": [{"heading": "宏观", "report_ids": ["R001", "R001"]}]}
            return model(prompt, *args)
        result, audit = self.run_synthesis(invoke=invalid)
        refs = [rid for section in result["bank_roundup"]["sections"] for rid in section["references"]]
        self.assertEqual(len(refs), 33)
        self.assertEqual(len(set(refs)), 33)
        self.assertIn("plan", audit["metrics"]["fallback_stages"])

    def test_hallucinated_report_or_page_reference_cannot_pass_as_model_synthesis(self):
        def invalid(prompt, *args):
            value = model(prompt, *args)
            if prompt.split("\n", 1)[0].endswith("SECTION"):
                value["bank_views"][0]["evidence_ids"] = ["R999-C999-P999"]
            return value
        result, _ = self.run_synthesis(invoke=invalid)
        self.assertTrue(all(section["synthesis_status"] == "deterministic_fallback" for section in result["bank_roundup"]["sections"]))
        self.assertNotIn("R999", json.dumps(result))

    def test_full_large_middle_and_tail_are_present_in_evidence_packages(self):
        results, reports, figures = fixture(1)
        original = "头部。" + "中段需求与投资。" * 8000 + "尾页独有事实：自由现金流预测变化。"
        results[0]["summaries"][0]["summary"] = original
        clean = lambda text: cross.clean_research(text, boilerplate_only)
        rows = cross.evidence_inventory(results, clean)
        first_rows = [row for row in rows if row["chunk"] == 1]
        text = "".join(row["text"] for row in first_rows)
        self.assertIn(clean(original), text)
        self.assertIn("尾页独有事实", text)
        packs = cross.pack_evidence(rows)
        self.assertEqual(sum(len(pack) for pack in packs), len(rows))
        self.assertGreater(len(packs), 2)

    def test_chinese_english_metadata_removed_without_erasing_research(self):
        text = "作者：John Analyst\nTel: +1 212 555 0000\nEmail: person@bank.com\nRegistered address: 100 Wall Street\n免责声明：仅供参考。\nRatings distribution: Buy 55%, Sell 5%.\nGS认为监管变化会影响数据中心需求。\nMS预计公司收入增长15%，版权成本仍然较高。\n分析师认为尾部需求有韧性。"
        clean = cross.clean_research(text, boilerplate_only)
        for absent in ("John Analyst", "555", "person@", "Wall Street", "免责声明", "Buy 55"):
            self.assertNotIn(absent, clean)
        for kept in ("GS认为", "MS预计", "15%", "版权成本", "尾部需求"):
            self.assertIn(kept, clean)

    def test_mixed_english_disclaimer_and_author_intro_keep_adjacent_real_claim(self):
        text = "Disclaimer: for institutional clients only. Company revenue grew 15%.\nCopyright licensing revenue is expected to grow 15%.\n本报告由某某分析师撰写，MS预计收入增长20%。\nAuthor: Dr. John Analyst\nCopyright 2026. All rights reserved."
        cleaned = cross.clean_research(text, boilerplate_only)
        self.assertNotIn("John", cleaned)
        self.assertNotIn("disclaimer", cleaned.lower())
        self.assertNotIn("Copyright 2026", cleaned)
        self.assertIn("Company revenue grew 15%", cleaned)
        self.assertIn("Copyright licensing revenue", cleaned)
        self.assertIn("MS预计收入增长20%", cleaned)

    def test_empty_legal_blocks_remain_private_but_are_not_model_reduction_inputs(self):
        data = fixture(1)
        data[0][0]["summaries"][1].update(summary="免责声明：仅供参考。", key_points=[], data_points=[], differences=[])
        calls = []
        def capture(prompt, *args):
            calls.append(prompt)
            return model(prompt, *args)
        _, audit = self.run_synthesis(data, invoke=capture)
        self.assertEqual(len(audit["evidence"]), 2)
        self.assertEqual(audit["active_evidence_count"], 1)
        self.assertEqual(audit["omitted_empty_evidence_ids"], ["R001-C002-P001"])
        evidence_prompts = [prompt for prompt in calls if prompt.split("\n")[0].endswith("EVIDENCE")]
        self.assertNotIn("R001-C002-P001", "".join(evidence_prompts))
        self.assertNotIn("仅含出版杂项", json.dumps(audit, ensure_ascii=False))

    def test_fallback_preserves_every_report_fragment_even_long_institutions(self):
        results, reports, figures = fixture()
        for report in reports:
            report["institution_name"] = "A very long source institution name"
        rows = cross.evidence_inventory(results, lambda text: text)
        evidence = {row["id"]: row for row in rows}
        section = cross.fallback_section({"heading": "One topic", "report_ids": [row["id"] for row in reports]},
                    cross.fallback_cards(rows), evidence, {row["id"]: row for row in reports}, figures)
        for view in section["bank_views"]:
            self.assertLessEqual(len(view["view"]), 500)
            for rid in view["report_ids"]:
                self.assertIn(rid + " ", view["view"])
            self.assertEqual({row["report_id"] for row in view["sources"]}, set(view["report_ids"]))

    def test_overbudget_model_view_is_rejected_instead_of_losing_its_tail(self):
        def oversized(prompt, *args):
            value = model(prompt, *args)
            if prompt.split("\n")[0].endswith("SECTION"):
                value["bank_views"][0]["view"] = "需求增长。" * 150 + "末页独有事实。"
            return value
        result, audit = self.run_synthesis(invoke=oversized)
        self.assertTrue(all(section["synthesis_status"] == "deterministic_fallback" for section in result["bank_roundup"]["sections"]))
        self.assertIn("section-0", audit["metrics"]["fallback_stages"])

    def test_definite_provider_rejection_allows_corrected_account_retry(self):
        from build_market_views_ocr_fallback import ProviderConfigurationError
        def rejected(*_): raise ProviderConfigurationError("DeepSeek synthesis HTTP 402")
        _, first = self.run_synthesis(invoke=rejected)
        self.assertGreater(first["metrics"]["model_submissions"], 0)
        self.assertFalse(list(self.cache.rglob("*.pending.json")))
        repaired, audit = self.run_synthesis()
        self.assertEqual(repaired["synthesis_status"], "model")
        self.assertGreater(audit["metrics"]["model_submissions"], 0)

    def test_pack_and_topic_parallelism_is_bounded_and_results_keep_input_order(self):
        lock, active, maximum, calls = threading.Lock(), {}, {}, []
        def parallel(prompt, *args):
            stage = prompt.split("\n")[0].split()[-1]
            with lock:
                active[stage] = active.get(stage, 0) + 1
                maximum[stage] = max(maximum.get(stage, 0), active[stage])
                calls.append(stage)
            time.sleep(0.02)
            value = model(prompt, *args)
            with lock:
                active[stage] -= 1
            return value
        with patch.object(cross, "PACK_CHARS", 1600):
            result, audit = self.run_synthesis(invoke=parallel)
            replayed, replay = self.run_synthesis(invoke=lambda *_: self.fail("cached request repeated"))
        self.assertEqual(result, replayed)
        self.assertEqual(audit["metrics"]["model_submissions"], len(calls))
        self.assertEqual(replay["metrics"]["model_submissions"], 0)
        for stage in ("EVIDENCE", "SECTION"):
            self.assertGreater(maximum[stage], 1)
            self.assertLessEqual(maximum[stage], 4)
        self.assertEqual([eid for pack in audit["reductions"] for eid in pack["evidence_ids"]], [row["id"] for row in audit["evidence"]])
        self.assertEqual([section["heading"] for section in result["bank_roundup"]["sections"]], [row["heading"] for row in audit["topic_plan"]])

    def test_figure_selection_prefers_numeric_and_limits_qualitative_repetition(self):
        figures = [{"figure_id": f"F{i}", "report_id": "R001", "chart_spec": {"kind": kind}}
                   for i, kind in enumerate(["qualitative", "bar", "line", "bar"])]
        self.assertEqual(cross.selected_figures(figures, ["R001"]), ["F1", "F2", "F3"])
        self.assertEqual(cross.selected_figures([figures[0]] * 4, ["R001"]), ["F0"])

    def test_numeric_chart_is_active_source_bound_evidence_even_with_legal_summary(self):
        data = fixture(1)
        summary = data[0][0]["summaries"][0]
        summary.update(summary="免责声明：仅供参考。", key_points=[], differences=[], data_points=[],
            charts=[{"kind": "bar", "title": "Copyright licensing revenue", "unit": "%", "labels": ["2025", "2026"],
                "series": [{"name": "收入增长", "values": [14.7, 15]}], "source_pages": [1]}])
        rows = cross.evidence_inventory(data[0], lambda value: cross.clean_research(value, boilerplate_only))
        self.assertIn("14.7", rows[0]["text"])
        self.assertIn("Copyright licensing revenue", rows[0]["text"])
        self.assertEqual(rows[0]["pages"], [1])
        summary["charts"][0]["title"] = "Ratings distribution"
        rows = cross.evidence_inventory(data[0], lambda value: cross.clean_research(value, boilerplate_only))
        self.assertFalse(rows[0]["text"].strip())

    def test_two_hundred_same_topic_reports_fit_ten_bounded_fallback_modules(self):
        results, reports, figures = fixture(200)
        plan = cross.balance_plan([{"heading": "宏观", "report_ids": [row["id"] for row in reports]}])
        self.assertEqual(len(plan), 10)
        self.assertTrue(all(len(topic["report_ids"]) == 20 for topic in plan))
        rows = cross.evidence_inventory(results, lambda value: value)
        evidence = {row["id"]: row for row in rows}
        cards = cross.fallback_cards(rows)
        for topic in plan:
            section = cross.fallback_section(topic, cards, evidence, {row["id"]: row for row in reports}, figures)
            for view in section["bank_views"]:
                self.assertLessEqual(len(view["view"]), 500)
                self.assertTrue(all(rid + " " in view["view"] for rid in view["report_ids"]))


if __name__ == "__main__":
    unittest.main()
