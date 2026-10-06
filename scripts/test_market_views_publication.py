"""Exact edition upgrades and partial-but-all-attempted OCR publication."""
import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

import fitz

import market_views_publication as publication
import upload_market_view_to_r2 as uploader
from test_upload_market_view_to_r2 import FakeR2Client

DATE, RUN, SHA = "260802", "12345", "c" * 40


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")


def fixture(root):
    manifest = [{"process_local_path": f"originals/{name}.pdf", "content_sha256": digest * 64}
                for name, digest in (("good", "a"), ("skipped", "b"))]
    write_json(root / "selected_to_process_manifest.json", manifest)
    values = {
        "report_inputs.json": [{"id": "R001", "digest": "An actual report summary.", "source_pdf": "good.pdf"}],
        "figure_candidates.json": [{"figure_id": "F001", "report_id": "R001", "latex_path": "figures/F001.png"}],
        "market_views_structured.json": {"bank_roundup": {"sections": [{"heading": "Actual synthesis"}]},
                                        "skipped_reports": [{"source_pdf": "skipped.pdf", "reason": "ocr_timeout"}]},
        "ocr_sources/R001/pages.json": [{"page": 1, "text": "Source page text"}],
        "ocr_sources/R001/chunks.json": [{"pages": [1]}],
        "ocr_sources/R001/summaries.json": [{"pages": [1], "summary": "Actual summary"}],
    }
    for name, value in values.items():
        write_json(root / name, value)
    (root / "figures").mkdir()
    (root / "figures/F001.png").write_bytes(b"declared-test-chart-bytes")
    receipt = {
        "schema_version": 1, "source_kind": "ocr-synthesis", "complete": True,
        "date_folder": DATE, "source_run_id": RUN, "execution_sha": SHA,
        "expected_reports": 2, "attempted_reports": 2, "summarized_reports": 1,
        "skipped_reports": 1, "report_count": 1, "total_pages": 1,
        "selected_manifest_sha256": hashlib.sha256((root / "selected_to_process_manifest.json").read_bytes()).hexdigest(),
        "reports": [
            {"id": "R001", "source_pdf": "good.pdf", "content_sha256": "a" * 64,
             "status": "summarized", "page_count": 1, "pages_covered": [1],
             "chunk_count": 1, "chunks_completed": 1, "figure_ids": ["F001"]},
            {"id": "R002", "source_pdf": "skipped.pdf", "content_sha256": "b" * 64,
             "status": "skipped", "reason": "ocr_timeout"},
        ],
        "files": [{"path": name, "bytes": len((root / name).read_bytes()),
                   "sha256": hashlib.sha256((root / name).read_bytes()).hexdigest()}
                  for name in [*values, "figures/F001.png"]],
    }
    write_json(root / publication.RECEIPT_NAME, receipt)
    return receipt


def pdf(root, *, source_pages=False):
    path = root / f"market_views_{DATE}.pdf"
    with fitz.open() as doc:
        page = doc.new_page()
        page.insert_text((40, 50), "Actual generated research summaries and observations.\n" * 15)
        page.draw_rect(fitz.Rect(40, 300, 500, 500), color=(0.2, 0.3, 0.7))
        page.insert_text((50, 330), "Chart: observed source relationships and documented limitations.")
        doc.set_metadata({"subject": "degraded source-page edition" if source_pages else "OCR synthesis"})
        doc.save(path)
    return path


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.receipt = fixture(self.root)

    def validate(self, **changes):
        args = dict(date_folder=DATE, expected_reports=2, source_run_id=RUN, execution_sha=SHA)
        args.update(changes)
        return publication.validate_ocr_synthesis_receipt(self.root, **args)

    def save(self, value):
        write_json(self.root / publication.RECEIPT_NAME, value)

    def rehash(self, relative):
        for row in self.receipt["files"]:
            if row["path"] == relative:
                data = (self.root / relative).read_bytes()
                row.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
        self.save(self.receipt)

    def test_partial_report_is_valid_only_when_all_originals_are_attempted_and_disclosed(self):
        result = self.validate()
        self.assertEqual(result["summarized_reports"], 1)
        self.assertEqual(result["skipped_reports"], 1)
        self.assertEqual(result["source_inventory_sha256"], publication.source_inventory_sha256(self.receipt["reports"]))
        for field, value in (("attempted_reports", 1), ("summarized_reports", 0),
                             ("skipped_reports", 0), ("report_count", 2), ("complete", False)):
            with self.subTest(field=field):
                self.save({**self.receipt, field: value})
                with self.assertRaises(ValueError): self.validate()

    def test_cross_report_modules_cover_sources_once_and_validate_citations(self):
        inputs = json.loads((self.root / "report_inputs.json").read_text())
        inputs.append({"id": "R002", "digest": "Second actual report summary.", "source_pdf": "skipped.pdf"})
        write_json(self.root / "report_inputs.json", inputs)
        for name in ("pages", "chunks", "summaries"):
            write_json(self.root / f"ocr_sources/R002/{name}.json", [{"page": 1, "text": "Second source evidence"}])
        write_json(self.root / "cross_report_evidence.json", {"source_ids": ["R001", "R002"]})
        second = {**self.receipt["reports"][0], "id": "R002", "source_pdf": "skipped.pdf", "content_sha256": "b" * 64}
        self.receipt["reports"][1] = second
        self.receipt.update(summarized_reports=2, skipped_reports=0, report_count=2, total_pages=2)
        summary = {"synthesis_mode": "cross-report-v1", "publication_limits": {"max_modules": 10, "max_pages": 70},
                   "bank_roundup": {"sections": [{"heading": "Macro", "references": ["R001", "R002"],
                       "figure_ids": ["F001"], "bank_views": [{"report_ids": ["R001", "R002"],
                           "view": "Both reports discuss growth with different assumptions.",
                           "sources": [{"report_id": "R002", "pages": [1]}, {"report_id": "R001", "pages": [1]}]}]}]}}
        def save_summary(value):
            write_json(self.root / "market_views_structured.json", value)
            self.receipt["files"] = [{"path": p.relative_to(self.root).as_posix(), "bytes": len(p.read_bytes()),
                                      "sha256": hashlib.sha256(p.read_bytes()).hexdigest()}
                                     for p in self.root.rglob("*") if p.is_file() and p.name != publication.RECEIPT_NAME]
            self.save(self.receipt)
        save_summary(summary)
        self.assertEqual(self.validate()["summarized_reports"], 2)
        for refs in (["R001"], ["R001", "R001"], ["R001", "R003"]):
            changed = copy.deepcopy(summary)
            changed["bank_roundup"]["sections"][0]["references"] = refs
            save_summary(changed)
            with self.assertRaisesRegex(ValueError, "source_coverage"):
                self.validate()
        changed = copy.deepcopy(summary)
        changed["bank_roundup"]["sections"][0]["bank_views"][0]["sources"][0]["pages"] = [2]
        save_summary(changed)
        with self.assertRaisesRegex(ValueError, "evidence_page"):
            self.validate()
        changed = copy.deepcopy(summary)
        changed["bank_roundup"]["sections"] *= 11
        save_summary(changed)
        with self.assertRaisesRegex(ValueError, "module_count"):
            self.validate()
        for mutation, reason in (("no_views", "missing_cross_report_views"),
                                 ("no_ids", "view_source"), ("no_sources", "view_evidence"),
                                 ("no_pages", "evidence_page"), ("wrong_attribution", "attribution_mismatch")):
            changed = copy.deepcopy(summary)
            section = changed["bank_roundup"]["sections"][0]
            if mutation == "no_views": section["bank_views"] = []
            elif mutation == "no_ids": section["bank_views"][0]["report_ids"] = []
            elif mutation == "no_sources": section["bank_views"][0]["sources"] = []
            elif mutation == "no_pages": section["bank_views"][0]["sources"][0]["pages"] = []
            else: section["bank_views"][0]["sources"] = [{"report_id": "R001", "pages": [1]}]
            save_summary(changed)
            with self.subTest(mutation=mutation), self.assertRaisesRegex(ValueError, reason): self.validate()

    def test_exact_date_producer_and_inventory_are_bound(self):
        for args in ({"date_folder": "260803"}, {"source_run_id": "999"}, {"execution_sha": "d" * 40},
                     {"expected_reports": 3}):
            with self.subTest(args=args), self.assertRaises(ValueError): self.validate(**args)
        changed = copy.deepcopy(self.receipt)
        changed["reports"][1]["content_sha256"] = "e" * 64
        self.save(changed)
        with self.assertRaisesRegex(ValueError, "manifest_identity"): self.validate()
        self.assertNotEqual(publication.source_inventory_sha256(changed["reports"]),
                            publication.source_inventory_sha256(self.receipt["reports"]))
        self.assertEqual(publication.source_inventory_sha256(self.receipt["reports"]),
                         publication.source_inventory_sha256(list(reversed(self.receipt["reports"]))))

    def test_hash_mismatch_and_omitted_source_evidence_are_rejected(self):
        target = self.root / "ocr_sources/R001/pages.json"
        target.write_text("[]")
        with self.assertRaisesRegex(ValueError, "hash_mismatch"): self.validate()
        self.rehash("ocr_sources/R001/pages.json")
        changed = copy.deepcopy(self.receipt)
        changed["files"] = [r for r in changed["files"] if r["path"] != "ocr_sources/R001/pages.json"]
        self.save(changed)
        with self.assertRaisesRegex(ValueError, "missing_synthesis_document"): self.validate()

    def test_skipped_disclosure_cannot_be_removed_even_with_recomputed_file_hash(self):
        path = self.root / "market_views_structured.json"
        write_json(path, {"bank_roundup": {"sections": [{"heading": "Actual synthesis"}]}})
        self.rehash(path.name)
        with self.assertRaisesRegex(ValueError, "missing_skipped_report_disclosure"): self.validate()

    def test_old_successful_report_cannot_replace_this_runs_successful_set(self):
        write_json(self.root / "report_inputs.json", [{"id": "R999", "digest": "Old report"}])
        self.rehash("report_inputs.json")
        with self.assertRaisesRegex(ValueError, "missing_summarized_report_content"): self.validate()

    def test_path_escape_is_rejected_before_reading_external_file(self):
        self.receipt["files"][0]["path"] = "../secret.json"
        self.save(self.receipt)
        with self.assertRaisesRegex(ValueError, "invalid_synthesis_path"): self.validate()

    def test_source_pages_pdf_is_rebuilt_without_reusing_private_archive(self):
        client = FakeR2Client()
        plan = publication.publication_plan(pdf(self.root, source_pages=True), DATE,
                                            source_kind="mineru-recovery", client=client, bucket="test")
        self.assertTrue(plan["should_build"])
        self.assertEqual(plan["edition"], "standard")
        self.assertEqual(client.calls, [])

    def seed(self, edition):
        client = FakeR2Client()
        path = pdf(self.root)
        uploader.upload_market_view(path, DATE, client=client, bucket="test")
        key = f"_market-views/items/{DATE}.json"
        item = json.loads(client.objects[key]["Body"])
        item.update(edition=edition, quality_status="degraded", title="Old source-page edition")
        client.objects[key]["Body"] = json.dumps(item).encode()
        client.calls.clear()
        return client, path

    def test_lower_private_editions_upgrade_even_if_local_pdf_looks_standard(self):
        for edition in ("source-pages", "ocr-synthesis"):
            with self.subTest(edition=edition):
                client, path = self.seed(edition)
                plan = publication.publication_plan(path, DATE, source_kind="xhs", client=client, bucket="test")
                self.assertTrue(plan["should_build"])
                self.assertFalse(any(call[0] == "put" for call in client.calls))
                with self.assertRaisesRegex(RuntimeError, "editions disagree"):
                    uploader.private_publication_complete(DATE, expected_edition="standard", client=client, bucket="test")

    def test_ocr_receipt_upload_replaces_old_label_and_records_real_coverage(self):
        client, path = self.seed("source-pages")
        item = uploader.upload_market_view(path, DATE, client=client, bucket="test",
                                           edition="ocr-synthesis", source_receipt=self.root / publication.RECEIPT_NAME)
        self.assertEqual(item["edition"], "ocr-synthesis")
        self.assertEqual(item["quality_status"], "partial")
        self.assertIn("1/2", item["title"])
        self.assertEqual(item["source_expected_reports"], 2)
        self.assertEqual(item["source_summarized_reports"], 1)
        self.assertEqual(item["source_skipped_reports"], 1)
        self.assertTrue(uploader.private_publication_complete(DATE, expected_edition="ocr-synthesis",
            expected_source_inventory_sha256=item["source_inventory_sha256"], client=client, bucket="test"))
        self.assertFalse(uploader.private_publication_complete(DATE, expected_edition="ocr-synthesis",
            expected_source_inventory_sha256="f" * 64, client=client, bucket="test"))
        standard = uploader.upload_market_view(path, DATE, client=client, bucket="test")
        self.assertEqual(standard["title"], "Market Views · 2026-08-02")
        self.assertNotIn("quality_status", standard)
        self.assertNotIn("source_inventory_sha256", standard)

    def test_source_pages_cannot_be_relabelled_to_claim_actual_synthesis(self):
        path = pdf(self.root, source_pages=True)
        with self.assertRaisesRegex(ValueError, "relabelled"):
            uploader.upload_market_view(path, DATE, client=FakeR2Client(), bucket="test",
                                       edition="ocr-synthesis", source_receipt=self.root / publication.RECEIPT_NAME)


if __name__ == "__main__":
    unittest.main()
