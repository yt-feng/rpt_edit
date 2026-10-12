"""Offline tests for the temporary, isolated 17-source cloud acceptance."""
import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import imf_exact_fetch_acceptance as acceptance
from institution_pending_intake import PendingIntake


class ExactAcceptanceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        fixture = self.root / acceptance.FIXTURE
        fixture.parent.mkdir(parents=True)
        shutil.copyfile(Path(__file__).resolve().parents[1] / acceptance.FIXTURE, fixture)
        self.seed = acceptance.read_json(fixture)
        for name in acceptance.PROTECTED:
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("{}\n")
        acceptance.prepare(self.root)
        self.output = self.root / acceptance.OUT
        rows = []
        for record in self.seed["items"].values():
            item = record["item"]
            suffix = hashlib.sha1(("imf:" + item["guid"]).encode()).hexdigest()[:8]
            filename = "IMF_offline_fixture_" + suffix + ".pdf"
            # Fake bytes are accepted only by our injected test inspector.
            data = b"%PDF-offline-test:" + item["guid"].encode()
            (self.output / filename).write_bytes(data)
            rows.append({"source_page_url": item["source_url"], "institution": "imf",
                         "published": item["date"], "local_filename": filename,
                         "pdf_url": "https://www.imf.org/-/media/files/publications/offline.pdf",
                         "bytes": len(data), "sha256": acceptance.sha(data)})
        self.manifest = {"downloaded_count": 17, "institutions": ["imf"], "downloaded": rows,
                         "skipped_count": 0, "skipped": [], "source_checks": [{
                             "institution": "imf", "status": "ok", "resolution_failure_count": 0,
                             "eligible_item_count": 17, "new_pdf_count": 17,
                             "deferred_retry_count": 0, "discovery_error": False, "error": ""}]}
        self.write_manifest()
        self.write_json("acceptance_scope.json", {
            "target_count": 17,
            "guids": sorted(record["item"]["guid"] for record in self.seed["items"].values()),
            "discovered_count": 60, "excluded_fresh_count": 43})

    def write_json(self, name, value):
        (self.output / name).write_text(json.dumps(value))

    def write_manifest(self):
        self.write_json("institution_run_manifest.json", self.manifest)

    @staticmethod
    def fake_inspector(path, preview):
        data = path.read_bytes()
        return {"bytes": len(data), "sha256": acceptance.sha(data), "pages": 1,
                "first_page_text": "Offline fixture", "first_page_text_sha256": acceptance.sha(b"Offline fixture"),
                "first_page_preview": preview.name}

    def verify(self, code=0):
        return acceptance.verify(self.root, code, inspect_pdf=self.fake_inspector)

    def test_exact_17_passes_machine_checks_but_never_approves_semantic_identity(self):
        result = self.verify()
        self.assertEqual([], result["errors"])
        self.assertEqual(17, result["verified_report_count"])
        self.assertEqual("machine_checks_passed_pending_identity_review", result["status"])
        self.assertTrue(result["production_state_unchanged"])
        self.assertTrue(all(row["identity_review"] == "pending" for row in result["reports"]))

    def test_missing_duplicate_and_wrong_sources_fail_even_at_reported_count_17(self):
        original = copy.deepcopy(self.manifest)
        for change in ("missing", "duplicate", "wrong"):
            with self.subTest(change=change):
                self.manifest = copy.deepcopy(original)
                if change == "missing":
                    self.manifest["downloaded"].pop()
                elif change == "duplicate":
                    self.manifest["downloaded"][-1] = self.manifest["downloaded"][0]
                else:
                    self.manifest["downloaded"][-1]["source_page_url"] += "-different-report"
                self.write_manifest()
                self.assertIn("exact_17_source_coverage_mismatch", self.verify()["errors"])

    def test_unmanifested_pdf_fails(self):
        (self.output / "extra.pdf").write_bytes(b"%PDF-extra")
        self.assertIn("pdf_files_do_not_match_manifest", self.verify()["errors"])

    def test_downloaded_file_bytes_and_hash_are_recomputed(self):
        row = self.manifest["downloaded"][0]
        (self.output / row["local_filename"]).write_bytes(b"%PDF-replaced-by-other-content")
        result = self.verify()
        self.assertEqual("failed", result["status"])
        self.assertIn("pdf_bytes_or_hash_mismatch", result["reports"][0]["errors"])

    def test_filename_binds_guid_and_publication_date_binds_source(self):
        for key, value, error in (("local_filename", "different.pdf", "source_filename_binding_invalid"),
                                  ("published", "2000-01-01T00:00:00Z", "source_publication_binding_invalid"),
                                  ("pdf_url", "https://unrelated.example/report.pdf", "official_pdf_url_invalid")):
            with self.subTest(field=key):
                old = self.manifest["downloaded"][0][key]
                self.manifest["downloaded"][0][key] = value
                self.write_manifest()
                self.assertIn(error, self.verify()["reports"][0]["errors"])
                self.manifest["downloaded"][0][key] = old

    def test_source_health_failures_cannot_be_hidden_by_17_downloads(self):
        check = self.manifest["source_checks"][0]
        for key, value in (("status", "degraded"), ("resolution_failure_count", 1),
                           ("deferred_retry_count", 1), ("discovery_error", True),
                           ("error", "source discovery failed"),
                           ("eligible_item_count", 18), ("new_pdf_count", 16)):
            with self.subTest(field=key):
                old = check[key]
                check[key] = value
                self.write_manifest()
                self.assertIn("source_health_not_clean", self.verify()["errors"])
                check[key] = old

    def test_producer_nonzero_and_skipped_sources_fail(self):
        self.assertIn("producer_failed", self.verify(2)["errors"])
        self.manifest.update(skipped_count=1, skipped=[{"reason": "publication_pending"}])
        self.write_manifest()
        self.assertIn("source_skipped", self.verify()["errors"])

    def test_each_production_state_file_is_protected(self):
        for name in acceptance.PROTECTED:
            with self.subTest(name=name):
                path = self.root / name
                original = path.read_bytes()
                path.write_bytes(original + b"changed")
                self.assertIn("production_state_changed", self.verify()["errors"])
                path.write_bytes(original)

    def test_seed_and_working_copy_cannot_change(self):
        path = self.output / "frozen_seed.json"
        path.write_bytes(path.read_bytes() + b" ")
        self.assertIn("frozen_working_copy_changed", self.verify()["errors"])
        fixture = self.root / acceptance.FIXTURE
        fixture.write_bytes(fixture.read_bytes() + b" ")
        self.assertEqual("failed", self.verify()["status"])
        with self.assertRaisesRegex(ValueError, "frozen_seed_hash_mismatch"):
            acceptance.frozen(self.root)

    def test_pending_records_cannot_be_lost_or_have_admission_changed(self):
        pending = copy.deepcopy(self.seed)
        key = next(iter(pending["items"]))
        pending["items"][key]["since_days"] = 100
        self.write_json("imf-pending-intake.json", pending)
        self.assertIn("pending_identity_or_admission_changed:" + key, self.verify()["errors"])
        del pending["items"][key]
        self.write_json("imf-pending-intake.json", pending)
        self.assertIn("pending_scope_changed", self.verify()["errors"])

    def test_source_attempt_scope_must_be_exact(self):
        self.write_json("acceptance_scope.json", {"target_count": 17, "guids": []})
        self.assertIn("fetch_attempt_scope_mismatch", self.verify()["errors"])

    def test_query_parameters_and_inspection_exception_messages_are_not_exposed(self):
        self.manifest["downloaded"][0]["pdf_url"] += "?token=private-value"
        self.write_manifest()
        result = self.verify()
        self.assertNotIn("private-value", json.dumps(result))
        def broken(*_):
            raise RuntimeError("sensitive request details")
        result = acceptance.verify(self.root, 0, inspect_pdf=broken)
        self.assertNotIn("sensitive request", json.dumps(result))
        self.assertEqual(["RuntimeError"], result["reports"][0]["errors"])

    def test_fetch_limits_attempts_to_exact_seed_and_preserves_discovery_evidence(self):
        current_argv = sys.argv
        observed = {}
        producer = SimpleNamespace(PendingIntake=PendingIntake)
        fresh = copy.deepcopy(next(iter(self.seed["items"].values()))["item"])
        fresh["guid"] = "new-unobserved-report"
        fresh["source_url"] += "-new-report"
        def run():
            observed["argv"] = sys.argv[:]
            intake = producer.PendingIntake(self.output / "imf-pending-intake.json", {},
                                             now=datetime.now(timezone.utc), retry_limit=17)
            observed["rows"] = intake.merge([fresh])
            observed["item_count"] = intake.item_count
            return 7
        producer.main = run
        self.assertEqual(7, acceptance.fetch(self.root, producer))
        self.assertIs(current_argv, sys.argv)
        self.assertIs(PendingIntake, producer.PendingIntake)
        self.assertEqual(17, len(observed["rows"]))
        self.assertEqual(set(self.seed["items"]), {"imf:" + row["guid"] for row in observed["rows"]})
        self.assertEqual(18, observed["item_count"])
        scope = acceptance.read_json(self.output / "acceptance_scope.json")
        self.assertEqual(1, scope["discovered_count"])
        self.assertEqual(1, scope["excluded_fresh_count"])
        self.assertIn(str(self.output / "test_seen.json"), observed["argv"])
        self.assertNotIn("institution_feeds/seen_state.json", observed["argv"])

    def test_real_producer_keeps_exact_scope_and_does_not_hide_discovery_outage(self):
        import fetch_institution_latest_pdfs as producer
        for path in self.output.glob("*.pdf"):
            path.unlink()
        fresh = copy.deepcopy(next(iter(self.seed["items"].values()))["item"])
        fresh["guid"] = "unobserved-fresh-source"
        fresh["source_url"] += "-fresh"
        def download(_session, candidates, destination, *_args, **_kwargs):
            destination.write_bytes(b"%PDF-offline-only:" + destination.name.encode())
            return "https://www.imf.org/-/media/files/publications/" + destination.name, "ok"
        for empty_discovery in (False, True):
            with self.subTest(empty_discovery=empty_discovery):
                self.write_json("imf-pending-intake.json", self.seed)
                (self.output / "test_seen.json").unlink(missing_ok=True)
                (self.output / "test_archive.jsonl").unlink(missing_ok=True)
                with (patch.dict(producer.os.environ, {"PROXY_SUBSCRIPTION_URL": ""}),
                      patch.object(producer, "INSTITUTIONS", copy.deepcopy(producer.INSTITUTIONS)),
                      patch.object(producer, "collect_coveo_items", return_value=[] if empty_discovery else [fresh]),
                      patch.object(producer, "collect_coveo_preview_candidates", return_value=[
                          "https://www.imf.org/-/media/files/publications/offline-preview.pdf"]),
                      patch.object(producer, "download_pdf", side_effect=download) as calls,
                      patch.object(producer, "http_get", side_effect=AssertionError("unexpected network call")),
                      patch.object(producer.requests.sessions.Session, "request", side_effect=AssertionError("unexpected network call")),
                      patch.object(producer, "write_github_output"),
                      patch.object(producer, "write_source_health_summary"),
                      patch.object(producer, "log"), patch.object(producer, "warn"), patch.object(producer, "github_warning")):
                    code = acceptance.fetch(self.root, producer)
                self.assertEqual(0, code)
                self.assertEqual(17, calls.call_count)
                manifest = acceptance.read_json(self.output / "institution_run_manifest.json")
                self.assertEqual(17, manifest["downloaded_count"])
                self.assertEqual(empty_discovery, manifest["source_checks"][0]["discovery_error"])
                result = self.verify(code)
                self.assertEqual(17, result["verified_report_count"])
                self.assertEqual(["source_health_not_clean"] if empty_discovery else [], result["errors"])

    def test_real_pdf_parser_renders_a_source_review_page_and_rejects_fake_pdf(self):
        import pymupdf as fitz
        path = self.output / "parser-test.pdf"
        with fitz.open() as doc:
            page = doc.new_page()
            page.insert_text((72, 72), "Offline PDF parser acceptance fixture")
            doc.save(path)
        preview = self.output / "parser-test.png"
        evidence = acceptance.pdf_evidence(path, preview)
        self.assertEqual(1, evidence["pages"])
        self.assertEqual(path.stat().st_size, evidence["bytes"])
        self.assertEqual(acceptance.sha(path.read_bytes()), evidence["sha256"])
        self.assertIn("Offline PDF parser", evidence["first_page_text"])
        self.assertTrue(preview.read_bytes().startswith(b"\x89PNG"))
        path.write_bytes(b"<html>Access denied</html>")
        with self.assertRaisesRegex(ValueError, "pdf_bytes_invalid"):
            acceptance.pdf_evidence(path, preview)


if __name__ == "__main__":
    unittest.main()
