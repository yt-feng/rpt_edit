#!/usr/bin/env python3
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from build_market_views_pdf import require_primary_report_dirs, source_date_dirs, report_digest, report_extract, unique_original_report_dirs, source_inventory_counts


class SourceDateDirsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = TemporaryDirectory()
        base = Path(self.temp_dir.name)
        self.bank = base / "dropbox"
        self.institutions = base / "institutions"
        self.consulting = base / "consulting"

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    @staticmethod
    def make_dates(root: Path, *dates: str) -> None:
        for date in dates:
            (root / date).mkdir(parents=True)

    @staticmethod
    def make_report(root: Path, date: str) -> Path:
        report = root / date / "report"
        report.mkdir(parents=True, exist_ok=True)
        (report / "source_mineru.md").write_text("# Parsed report")
        return report

    def test_latest_issue_date_follows_bank_batch_and_excludes_future_auxiliary(self) -> None:
        self.make_dates(self.bank, "260718", "260719")
        self.make_dates(self.institutions, "260718", "260720")
        self.make_dates(self.consulting, "260717")
        for date in ("260718", "260720"):
            self.make_report(self.institutions, date)
        self.make_report(self.consulting, "260717")
        report_dir = self.bank / "260719" / "shard_0" / "bank-report"
        report_dir.mkdir(parents=True)
        (report_dir / "source_mineru.md").write_text("# Parsed bank report")

        report_date, source_dirs = source_date_dirs(
            self.bank,
            [self.institutions, self.consulting],
            "latest",
        )

        self.assertEqual(report_date, "260719")
        self.assertEqual(
            source_dirs,
            [
                self.bank / "260719",
                self.institutions / "260718",
                self.consulting / "260717",
            ],
        )
        self.assertEqual(require_primary_report_dirs(source_dirs[0]), [report_dir])

    def test_explicit_bank_date_includes_latest_usable_auxiliary_on_or_before_issue(self) -> None:
        self.make_dates(self.bank, "260718", "260719")
        self.make_dates(self.institutions, "260717", "260719")
        self.make_dates(self.consulting, "260716", "260720")
        self.make_report(self.institutions, "260717")
        self.make_report(self.consulting, "260716")

        report_date, source_dirs = source_date_dirs(
            self.bank,
            [self.institutions, self.consulting],
            "260718",
        )

        self.assertEqual(report_date, "260718")
        self.assertEqual(
            source_dirs,
            [
                self.bank / "260718",
                self.institutions / "260717",
                self.consulting / "260716",
            ],
        )

    def test_latest_requires_a_primary_bank_date(self) -> None:
        self.make_dates(self.institutions, "260720")

        with self.assertRaisesRegex(RuntimeError, "primary bank source root"):
            source_date_dirs(self.bank, [self.institutions], "latest")

    def test_explicit_date_rejects_non_date_paths(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "Invalid primary bank date folder"):
            source_date_dirs(self.bank, [], "../260720")

    def test_explicit_date_rejects_invalid_calendar_dates(self) -> None:
        for invalid in ("261099", "2610030", "20261301"):
            with self.subTest(invalid=invalid), self.assertRaisesRegex(RuntimeError, "Invalid primary bank date"):
                source_date_dirs(self.bank, [], invalid)

    def test_empty_auxiliary_date_falls_back_to_usable_older_source(self) -> None:
        self.make_dates(self.bank, "261003")
        self.make_dates(self.institutions, "261002")
        self.make_report(self.institutions, "261001")
        self.assertEqual(source_date_dirs(self.bank, [self.institutions, self.consulting], "latest"),
                         ("261003", [self.bank / "261003", self.institutions / "261001"]))

    def test_mixed_six_and_eight_digit_source_dates_follow_calendar_order(self) -> None:
        self.make_dates(self.bank, "261003", "20261001")
        self.make_report(self.institutions, "20261002")
        self.make_report(self.institutions, "261004")
        self.assertEqual(source_date_dirs(self.bank, [self.institutions], "latest"),
                         ("261003", [self.bank / "261003", self.institutions / "20261002"]))

    def test_native_pdf_source_reaches_report_discovery_and_summary_inputs(self) -> None:
        report = self.bank / "261003" / "shard_0" / "report-a"
        report.mkdir(parents=True)
        text = "# Original report title\n\n" + "Native original report evidence covering growth and inflation. " * 20
        (report / "source_native_pdf.md").write_text(text)
        self.assertEqual(require_primary_report_dirs(self.bank / "261003"), [report])
        self.assertIn("growth and inflation", report_digest(report, 2200)["digest"])
        self.assertIn("growth and inflation", report_extract(report, 2200))

    def test_ocr_pending_markers_survive_cleaning_and_actual_bank_prompt_composition(self) -> None:
        import argparse
        import json
        from unittest.mock import patch
        import build_market_views_pdf as market

        report = self.bank / "261003" / "shard_0" / "report-a"
        report.mkdir(parents=True)
        marker = "[数值待核对:n0001]"
        page_marker = "[数值待核对:p2n3]"
        (report / "source_native_pdf.md").write_text(
            "# Revenue outlook\n\n"
            f"Revenue increased from {marker}% to 22% and remains subject to exact numerical verification.\n\n"
            f"The operating margin reported as {page_marker}% is another numerical field awaiting source verification.\n\n"
            "Demand remains supported by product launches and greater customer engagement across the sector.\n\n"
            "Management sees stable operating conditions with capacity improving across its distribution footprint."
        )
        digest = report_digest(report, 2200)
        extract = report_extract(report, 2200)
        self.assertTrue(digest["has_pending_numeric_values"])
        for text in (digest["digest"], extract):
            self.assertIn(marker, text)
            self.assertIn(page_marker, text)
        args = argparse.Namespace(per_report_prompt_chars=2200, figures_per_bank_section=4)
        reports = [{"id": "R001", "title": digest["title"], "digest": digest["digest"],
                    "extract": extract, "institution_name": "JPM", "source_group": "bank_research",
                    "has_pending_numeric_values": True}]
        prompts = []
        def model(prompt, _args, label, _path):
            prompts.append((label, prompt))
            return {"categories": [{"heading": "Demand outlook", "report_ids": ["R001"]}]} if label == "bank category plan" else {}
        with patch.object(market, "request_model_json", side_effect=model):
            roundup = market.generate_bank_roundup(reports, [], args, Path(self.temp_dir.name), True)
        self.assertEqual(len(prompts), 2)
        for _, prompt in prompts:
            self.assertIn(market.OCR_NUMBER_POLICY, prompt)
        self.assertIn(marker, prompts[1][1])
        self.assertIn(page_marker, prompts[1][1])
        self.assertIn(market.OCR_NUMBER_POLICY, market.build_prompt(reports, [], args))
        self.assertIn(market.OCR_NUMBER_POLICY, market.supporting_roundup_prompt("institution", reports, [], args))
        fallback = json.dumps(roundup, ensure_ascii=False)
        self.assertIn("Demand remains supported", fallback)
        self.assertNotIn("Revenue increased from", fallback)
        self.assertNotIn("operating margin reported", fallback)
        self.assertNotIn("22%", fallback)
        self.assertEqual(roundup["sections"][0]["bank_views"][0]["report_ids"], ["R001"])

    def test_ocr_marker_truncation_drops_a_whole_quantitative_statement(self) -> None:
        from build_market_views_pdf import trim_text, clean_markdown_for_extract, signal_sentences, first_signal
        marker = "[数值待核对:n0001]"
        statement = f"Revenue increased from {marker}% to 22% and the long quantitative comparison remains unverified."
        text = "Independent qualitative demand evidence remains intact.\n" + statement + "\nOperating conditions remain stable and readable."
        for size in (40, 80, 120):
            trimmed = trim_text(text, size)
            if "Revenue increased" in trimmed or "22%" in trimmed:
                self.assertIn(statement, trimmed)
                self.assertIn(marker, trimmed)
            self.assertNotIn("数值待核对:n0001", trimmed.replace(marker, ""))
        self.assertEqual(clean_markdown_for_extract(f"[{marker}](https://source.example.invalid)"), marker)
        self.assertNotIn("22%", " ".join(signal_sentences(statement + "\n\nA independently supported qualitative conclusion remains available.")))
        self.assertNotIn("22%", first_signal(statement + "\n\nAn independently supported qualitative conclusion remains available."))

    def test_omitted_numeric_fields_keep_uncertainty_through_the_digest_and_fallback(self) -> None:
        import build_market_views_pdf as market
        report = self.bank / "261003" / "shard_0" / "report-missing-field"
        report.mkdir(parents=True)
        marker = "[漏识数值待核对:s0001]"
        statement = f"Revenue changed from {marker}% to 22% but the first read missed that field."
        qualitative = "Demand remains supported by independently documented changes in customer engagement."
        (report / "source_native_pdf.md").write_text("# Demand outlook\n\n" + statement + "\n\n" + qualitative)
        digest = market.report_digest(report, 2200)
        self.assertTrue(digest["has_pending_numeric_values"])
        self.assertIn(marker, digest["digest"])
        self.assertIn(marker, market.report_extract(report, 2200))
        self.assertNotIn("22%", " ".join(market.signal_sentences(statement + "\n\n" + qualitative)))
        self.assertNotIn("22%", market.first_signal(statement + "\n\n" + qualitative))
        for size in (40, 80, 120):
            trimmed = market.trim_text(qualitative + "\n" + statement + "\n" + qualitative, size)
            if "22%" in trimmed or "Revenue changed" in trimmed:
                self.assertIn(statement, trimmed)
            self.assertNotIn("漏识数值待核对:s0001", trimmed.replace(marker, ""))

    def test_system_prompt_applies_numeric_marker_contract_to_the_actual_model_request(self) -> None:
        import argparse
        import os
        from unittest.mock import Mock, patch
        import build_market_views_pdf as market
        response = Mock(status_code=200)
        response.json.return_value = {"choices": [{"message": {"content": "{}"}}]}
        args = argparse.Namespace(deepseek_base_url="https://api.deepseek.com", model="deepseek-flash")
        with patch.dict(os.environ, {"DEEPSEEK_API_KEY": "offline-test-key"}), \
                patch.object(market, "request_with_retry", return_value=response) as request:
            self.assertEqual(market.call_deepseek("Source contains [数值待核对:n0001].", args, "offline"), "{}")
        messages = request.call_args.kwargs["payload"]["messages"]
        self.assertIn(market.OCR_NUMBER_POLICY, messages[0]["content"])
        self.assertIn("[数值待核对:n0001]", messages[1]["content"])

    def test_byte_identical_original_aliases_are_all_verified_then_summarized_once(self) -> None:
        import hashlib
        import json
        from extract_native_market_sources import extract_sources, SourceValidationError
        from test_extract_native_market_sources import make_pdf

        originals = Path(self.temp_dir.name) / "originals"
        originals.mkdir()
        first = originals / "research-a.pdf"
        alias = originals / "research-a-copy.pdf"
        make_pdf(first, chart=True)
        alias.write_bytes(first.read_bytes())
        manifest = Path(self.temp_dir.name) / "manifest.json"
        manifest.write_text(json.dumps([
            {"process_local_path": str(path), "content_sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
            for path in (first, alias)
        ]))
        sources = self.bank / "261001" / "shard_0"
        receipt = extract_sources(originals, manifest, sources, 2)
        dirs = require_primary_report_dirs(self.bank / "261001")
        self.assertEqual(len(dirs), 2, "Input coverage still includes both selected files")
        unique, aliases = unique_original_report_dirs(dirs)
        self.assertEqual(len(unique), 1)
        self.assertEqual(aliases[str(unique[0])][0]["source_pdf"], alias.name)
        self.assertEqual(receipt["report_count"], 2)
        self.assertEqual(receipt["unique_content_count"], 1)
        counts = source_inventory_counts([{
            "source_group": "bank_research", "source_aliases": aliases[str(unique[0])],
        }])
        self.assertEqual(counts, {
            "original_source_count": 2, "summarized_content_count": 1, "duplicate_alias_count": 1,
            "bank_original_source_count": 2, "bank_summarized_content_count": 1, "bank_duplicate_alias_count": 1,
        })
        copied_alias = sources / receipt["reports"][1]["markdown"]["path"]
        copied_alias.unlink()
        with self.assertRaises(SourceValidationError):
            unique_original_report_dirs(dirs)

    def test_native_summary_rejects_a_subset_even_without_duplicate_aliases(self) -> None:
        import hashlib
        import json
        from extract_native_market_sources import extract_sources
        from test_extract_native_market_sources import make_pdf

        originals = Path(self.temp_dir.name) / "originals"
        originals.mkdir()
        first = originals / "research-a.pdf"
        second = originals / "research-b.pdf"
        make_pdf(first, chart=True)
        make_pdf(second, chart=False)
        manifest = Path(self.temp_dir.name) / "manifest.json"
        manifest.write_text(json.dumps([
            {"process_local_path": str(path), "content_sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
            for path in (first, second)
        ]))
        sources = self.bank / "261001" / "shard_0"
        extract_sources(originals, manifest, sources, 2)
        dirs = require_primary_report_dirs(self.bank / "261001")
        self.assertEqual(len(unique_original_report_dirs(dirs)[0]), 2)
        with self.assertRaisesRegex(RuntimeError, "complete validated report inventory"):
            unique_original_report_dirs(dirs[:1])

    def test_mineru_sources_remain_separate_without_original_pdf_alias_receipts(self) -> None:
        first = self.make_report(self.bank, "261001")
        second = self.make_report(self.institutions, "261001")
        self.assertEqual(unique_original_report_dirs([first, second]), ([first, second], {}))

    def test_primary_bank_date_must_contain_parsed_report_outputs(self) -> None:
        (self.bank / "260720").mkdir(parents=True)
        self.make_dates(self.institutions, "260720")
        (self.institutions / "260720" / "note.md").write_text("# Auxiliary only")

        with self.assertRaisesRegex(RuntimeError, "auxiliary sources alone"):
            require_primary_report_dirs(self.bank / "260720")

    def test_primary_bank_report_markers_are_accepted(self) -> None:
        report_dir = self.bank / "260720" / "shard_0" / "report-a"
        report_dir.mkdir(parents=True)
        (report_dir / "source_mineru.md").write_text("# Parsed bank report")

        self.assertEqual(require_primary_report_dirs(self.bank / "260720"), [report_dir])


if __name__ == "__main__":
    unittest.main()
