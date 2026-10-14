"""Deadline extraction, honest provenance and durable daily publication."""
import hashlib
import json
from pathlib import Path
import tempfile
import subprocess
import unittest
from unittest import mock

import fitz
import market_views_source_digest as digest
import market_views_publication as publication
from market_views_partial_sources import write_delivery_receipt
import upload_market_view_to_r2 as uploader
from test_upload_market_view_to_r2 import FakeR2Client


TEXT = ("We expect economic growth to improve as consumer demand strengthens, while inflation remains above the central bank target. "
        "The investment outlook depends on earnings growth and the path of interest rates over the coming year.")
DATE, RUN, SHA = "261014", "123456", "a" * 40


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def pdf(path, pages=1, chart=False):
    doc = fitz.open()
    for number in range(pages):
        page = doc.new_page()
        page.insert_textbox(fitz.Rect(40, 40, 550, 180), TEXT + f"\nPage {number + 1} economic outlook.", fontsize=11)
        if chart and number == 0:
            page.insert_text((40, 210), "Figure 1: Economic growth forecast")
            pixmap = fitz.Pixmap(fitz.csRGB, (0, 0, 400, 240))
            pixmap.clear_with(160)
            page.insert_image(fitz.Rect(40, 230, 440, 470), stream=pixmap.tobytes("png"))
    doc.save(path)
    doc.close()
    return hashlib.sha256(path.read_bytes()).hexdigest()


class ExtractionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def test_native_all_pages_are_read_and_only_original_chart_crop_is_kept(self):
        original = self.root / "research.pdf"
        sha = pdf(original, pages=27, chart=True)
        candidate = digest._extract_one(original, self.root / "source", sha,
                                       max_pages=24, ocr=False, deadline_seconds=10)
        evidence = json.loads((self.root / "source/source_excerpt_evidence.json").read_text())
        self.assertEqual([row["page"] for row in evidence["examined_pages"]], list(range(1, 28)))
        self.assertEqual(evidence["page_count"], 27)
        self.assertTrue(evidence["whole_report_coverage"])
        self.assertEqual(len(evidence["figures"]), 1)
        figure = evidence["figures"][0]
        self.assertLess((figure["crop_bbox"][2] - figure["crop_bbox"][0]) *
                        (figure["crop_bbox"][3] - figure["crop_bbox"][1]),
                        .70 * figure["page_size"][0] * figure["page_size"][1])
        self.assertIn(figure["path"], candidate["files"])
        manifest = self.root / "manifest.json"
        write_json(manifest, [{"process_local_path": original.name, "content_sha256": sha}])
        bundle = self.root / "bound"
        write_delivery_receipt(manifest, bundle, {original.name: candidate}, date_folder=DATE,
                               source_run_id=RUN, source_execution_sha=SHA)
        verified = publication.validate_daily_delivery_receipt(bundle, date_folder=DATE)
        self.assertEqual(verified["included_reports"], 1)

    def test_source_sentences_reject_boilerplate_and_placeholder(self):
        values = digest.substantive_sentences(TEXT + "\n\nDisclaimer: The market outlook is not investment advice. " * 3
            + "\n\n该报告提供了一条需要纳入本节判断的新增市场信号。" * 3)
        self.assertTrue(values)
        self.assertFalse(any("Disclaimer" in value or "新增市场信号" in value for value in values))

    def test_observed_filenames_and_strategy_headlines_are_not_research_assertions(self):
        filename = ('03-Bernstein-Asia Quant Strategy & Asia Semis & Internet：Asia Tech Strategy 4Q26：'
                    'Valuations Reset， Revisions Slow...Stick to Quality & Value tech names-261013')
        headline = ('Asia Quant Strategy & Asia Semis & Internet Asia Tech Strategy 4Q26: '
                    'Valuations Reset, Revisions Slow...Stick to Quality & Value tech names')
        assertion = ('As we argued in our recent note on the sector, we are in a narrative-driven market '
                     'which creates extreme sensitivity to headlines due to perceived terminal value changes.')
        text = '# ' + headline + '\n\n' + filename + '\n\n' + headline + '\n\n' + assertion + '\n\n' + TEXT
        selected = digest.substantive_sentences(text)
        self.assertEqual(selected[0], assertion)
        self.assertTrue(any('We expect economic growth' in value for value in selected))
        self.assertFalse(any('Valuations Reset' in value for value in selected))

    def test_missing_bad_and_slow_sources_do_not_block_later_originals(self):
        original = self.root / "good.pdf"
        sha = pdf(original)
        slow = self.root / "slow.pdf"
        slow.write_bytes(original.read_bytes())
        manifest = self.root / "manifest.json"
        write_json(manifest, [{"process_local_path": name, "content_sha256": sha}
                              for name in ("missing.pdf", "slow.pdf", "good.pdf")])
        def worker(path, destination, content_sha, **kwargs):
            if path.name == "slow.pdf":
                raise TimeoutError()
            return {"directory": str(destination), "content_sha256": content_sha,
                    "source_method": "source-digest", "files": []}
        candidates, reasons = digest.extract_candidates(manifest, self.root, self.root / "out", worker=worker)
        self.assertEqual(set(candidates), {"good.pdf"})
        self.assertEqual(reasons["slow.pdf"], "source_deadline_exceeded")
        self.assertEqual(reasons["missing.pdf"], "original_missing_or_ambiguous")
        with mock.patch.object(digest, "_run_worker") as call:
            candidates, reasons = digest.extract_candidates(manifest, self.root, self.root / "out", deadline_seconds=0)
            call.assert_not_called()
            self.assertEqual(set(reasons.values()), {"delivery_deadline_reached"})

    def test_actual_worker_has_no_model_dependency(self):
        original = self.root / "research.pdf"
        sha = pdf(original)
        candidate = digest._run_worker(original, self.root / "worker", sha, timeout=10, max_pages=24, ocr=False)
        self.assertEqual(candidate["source_method"], "source-digest")
        self.assertEqual(json.loads((self.root / "worker/status.json").read_text())["model_requests"], 0)

    def test_scan_over_page_limit_is_skipped_before_any_ocr_call(self):
        path = self.root / "scan.pdf"
        doc = fitz.open()
        for _ in range(25):
            doc.new_page()
        doc.save(path)
        doc.close()
        sha = hashlib.sha256(path.read_bytes()).hexdigest()
        with mock.patch.object(digest.subprocess, "run") as run:
            with self.assertRaisesRegex(ValueError, "ocr_page_limit"):
                digest._extract_one(path, self.root / "scan", sha, max_pages=24, ocr=True, deadline_seconds=10)
            run.assert_not_called()

    def test_timeout_kills_only_its_own_worker_group(self):
        process = mock.Mock(pid=1234)
        process.communicate.side_effect = [subprocess.TimeoutExpired("worker", 1), ("", "")]
        with mock.patch.object(digest.subprocess, "Popen", return_value=process) as spawn, mock.patch.object(digest.os, "killpg") as kill:
            with self.assertRaises(TimeoutError):
                digest._run_worker(Path("input.pdf"), Path("out"), "a" * 64, timeout=1, max_pages=24, ocr=True)
            self.assertTrue(spawn.call_args.kwargs["start_new_session"])
            kill.assert_called_once_with(1234, digest.signal.SIGKILL)


class DeliveryPublicationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        source = self.root / "candidate"
        source.mkdir()
        (source / "source_mineru.md").write_text(TEXT * 2)
        write_json(source / "status.json", {"original_pdf_sha256": "b" * 64})
        manifest = self.root / "manifest.json"
        write_json(manifest, [{"process_local_path": "report.pdf", "content_sha256": "b" * 64},
                              {"process_local_path": "omitted.pdf", "content_sha256": "c" * 64}])
        self.source_root = self.root / "sources"
        self.receipt = write_delivery_receipt(manifest, self.source_root,
            {"report.pdf": {"directory": source, "content_sha256": "b" * 64, "source_method": "mineru",
                            "files": ["status.json", "source_mineru.md"]}},
            date_folder=DATE, source_run_id=RUN, source_execution_sha=SHA)
        self.receipt_path = self.source_root / "daily_delivery_receipt.json"
        output = self.root / "output"
        output.mkdir()
        self.path = output / f"market_views_{DATE}.pdf"
        pdf(self.path, pages=2)
        included = next(row for row in self.receipt["reports"] if row["status"] == "included")
        reports = [{"id": "R001", "path": str(self.source_root / included["report_id"]), "title": "Economic outlook",
                    "source_group": "bank_research", "institution_name": "Research institution", "extract": TEXT}]
        summary = digest.make_summary(reports, [], self.receipt)
        write_json(output / "market_views_structured.json", summary)
        write_json(output / "market_views_render_stats.json", {"pdf_sha256": hashlib.sha256(self.path.read_bytes()).hexdigest(),
            "summary_sha256": hashlib.sha256((output / "market_views_structured.json").read_bytes()).hexdigest(),
            "page_count": 2, "module_count": 1})
        self.client = FakeR2Client()

    def upload(self):
        return uploader.upload_market_view(self.path, DATE, client=self.client, bucket="test",
            edition="daily-digest", source_receipt=self.receipt_path)

    def test_partial_edition_archives_receipt_and_verifies_full_readback(self):
        item = self.upload()
        self.assertEqual(item["quality_status"], "partial")
        self.assertEqual(item["source_summarized_reports"], 1)
        self.assertEqual(item["source_expected_reports"], 2)
        self.assertTrue(uploader.private_publication_complete(DATE, client=self.client, bucket="test"))
        self.client.objects[item["source_receipt_key"]]["Body"] += b" "
        self.assertFalse(uploader.private_publication_complete(DATE, client=self.client, bucket="test"))

    def test_evidence_quotes_own_their_pages_and_telecom_does_not_become_aerospace(self):
        included = next(row for row in self.receipt['reports'] if row['status'] == 'included')
        path = self.source_root / included['report_id']
        write_json(path / 'source_excerpt_evidence.json', {'excerpts': [
            {'page': 1, 'text': 'Asia Tech Strategy 4Q26: Valuations Reset, Revisions Slow and Quality Value Tech Names'},
            {'page': 2, 'text': 'We expect telecom demand to improve as household incomes recover over the coming year.'},
            {'page': 3, 'text': 'Broadband investment has increased while the market continues to expand in rural regions.'},
            {'page': 4, 'text': 'Subscriber earnings are expected to rise as demand strengthens over the coming quarter.'},
            {'page': 33, 'text': 'Satellite market revenues have grown substantially in a later appendix that is not quoted.'},
        ]})
        report = {'id': 'R001', 'path': str(path), 'title': 'Cables Satellite Telecom Market Outlook',
                  'source_group': 'bank_research', 'institution_name': 'Research institution',
                  'extract': '03-Bernstein-Asia Quant Strategy Valuations Reset Market Forecast-261013'}
        summary = digest.make_summary([report], [], self.receipt)
        section = summary['bank_roundup']['sections'][0]
        view = section['bank_views'][0]
        self.assertEqual(section['heading'], '电信、宽带与有线网络')
        self.assertTrue(view['view'].startswith('We expect telecom'))
        self.assertEqual(view['sources'], [{'report_id': 'R001', 'pages': [2, 3]}])
        self.assertNotIn('Valuations Reset', json.dumps(summary))

    def test_bound_source_bytes_date_and_rendered_bytes_cannot_be_substituted(self):
        with self.assertRaisesRegex(ValueError, "invalid_daily_delivery_receipt"):
            publication.validate_daily_delivery_receipt(self.source_root, date_folder="261013")
        original = self.path.read_bytes()
        self.path.write_bytes(original + b" ")
        with self.assertRaisesRegex(ValueError, "render_binding"):
            self.upload()
        self.assertFalse(self.client.objects)
        self.path.write_bytes(original)
        source = next(self.source_root.glob("report_*/source_mineru.md"))
        source.write_text("tampered")
        with self.assertRaisesRegex(ValueError, "file_hash_mismatch"):
            self.upload()

    def test_standard_upgrades_daily_but_daily_cannot_downgrade_standard(self):
        item = self.upload()
        self.assertFalse(uploader.private_publication_complete(DATE, expected_edition="standard",
            allow_edition_upgrade=True, client=self.client, bucket="test"))
        uploader.upload_market_view(self.path, DATE, client=self.client, bucket="test")
        self.client.calls.clear()
        preserved = self.upload()
        self.assertTrue(preserved["preserved_higher_or_equal_edition"])
        self.assertFalse(any(call[0] == "put" for call in self.client.calls))
        self.assertNotEqual(item.get("edition"), preserved.get("edition"))

    def test_readback_detects_metadata_coverage_disagreement(self):
        self.upload()
        key = f"_market-views/items/{DATE}.json"
        item = json.loads(self.client.objects[key]["Body"])
        item["source_summarized_reports"] = 2
        self.client.objects[key]["Body"] = json.dumps(item).encode()
        self.assertFalse(uploader.private_publication_complete(DATE, client=self.client, bucket="test"))

    def test_guard_can_repair_confirmed_corruption_without_mistaking_unavailable_for_missing(self):
        item = self.upload()
        self.client.objects[item["source_receipt_key"]]["Body"] += b"corrupt"
        repaired = self.upload()
        self.assertFalse(repaired.get("skipped_existing", False))
        self.assertTrue(uploader.private_publication_complete(DATE, client=self.client, bucket="test"))
        self.client.calls.clear()
        with mock.patch.object(self.client, "get_object", side_effect=TimeoutError("unavailable")):
            with self.assertRaises(TimeoutError):
                self.upload()
        self.assertFalse(any(call[0] == "put" for call in self.client.calls))

    def test_missing_downloads_are_counted_in_public_denominator(self):
        self.receipt.update(unavailable_originals=[{"source_pdf": "download-failed.pdf", "reason": "original_download_failed"}],
                            expected_source_reports=3, complete_source_inventory=False)
        write_json(self.receipt_path, self.receipt)
        summary_path = self.path.parent / "market_views_structured.json"
        summary = json.loads(summary_path.read_text())
        summary.update(unavailable_originals=self.receipt["unavailable_originals"], expected_source_reports=3)
        write_json(summary_path, summary)
        stats_path = self.path.parent / "market_views_render_stats.json"
        stats = json.loads(stats_path.read_text())
        stats["summary_sha256"] = hashlib.sha256(summary_path.read_bytes()).hexdigest()
        write_json(stats_path, stats)
        item = self.upload()
        self.assertEqual(item["source_expected_reports"], 3)
        self.assertEqual(item["source_selected_reports"], 2)
        self.assertEqual(item["source_unavailable_reports"], 1)
        self.assertIn("1/3", item["title"])
        self.assertTrue(uploader.private_publication_complete(DATE, client=self.client, bucket="test"))


if __name__ == "__main__":
    unittest.main()
