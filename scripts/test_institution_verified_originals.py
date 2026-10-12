"""Synthetic reviewed allowlists exercise read-only exact-source recovery."""
from __future__ import annotations

import copy
from contextlib import redirect_stderr, redirect_stdout
from datetime import datetime, timedelta, timezone
import io
import json
from pathlib import Path
import tempfile
import types
import unittest
from unittest.mock import patch

from pypdf import PdfWriter

import fetch_institution_latest_pdfs as f
import institution_original_cache as original
from institution_pending_intake import PendingIntake
import institution_source_health as health
import institution_verified_originals as verified
from mineru_task_ledger import digest, encoded

NOW = datetime(2026, 10, 12, 12, tzinfo=timezone.utc)


def item(number=1):
    return dict(title=f"Synthetic reviewed report {number}", guid=f"synthetic-{number}",
                date=(NOW - timedelta(days=1)).isoformat(),
                source_url=f"https://www.imf.org/en/publications/wp/issues/2026/10/11/synthetic-{number}",
                pdf_candidates=[f"https://www.imf.org/-/media/files/publications/wp/2026/english/wpiea2026{number:03d}.pdf"],
                scrape_url="", coveo_unique_id="")


def filename(source):
    return f"IMF_{f.slug(source['title'])}_{f.short_hash('imf:' + source['guid'])}.pdf"


def pdf(number=1, pages=2):
    writer = PdfWriter()
    for _ in range(pages):
        writer.add_blank_page(width=100, height=100)
    writer.add_metadata({"/Title": f"Synthetic test fixture {number}"})
    stream = io.BytesIO(); writer.write(stream)
    return stream.getvalue()


def record(source=None, payload=None):
    source = copy.deepcopy(source or item())
    payload = payload if payload is not None else pdf()
    binding = dict(source=filename(source), sha256=digest(payload), size=len(payload), scope="institution",
                   endpoint="https://mineru.net", options=copy.deepcopy(original.OPTIONS))
    binding["id"] = digest(encoded(binding))
    return dict(item=source, official_landing_url="https://www.elibrary.imf.org/view/journals/001/2026/001/article-A001-en.xml",
                official_pdf_url="https://www.elibrary.imf.org/downloadpdf/view/journals/001/2026/001/article-A001-en.pdf",
                doi="10.5089/0000000000001.001.A001", sha256=digest(payload), size=len(payload), pages=2, binding=binding,
                verification=dict(method="official_browser_download", review="approved", receipt_sha256="1"*64,
                                  reviewed_at=NOW.isoformat()))


def manifest(rows=None):
    # This is a generated synthetic fixture, not any of the real 17 originals.
    return dict(schema=1, institution="imf", frozen_pending_sha256="2"*64, records=rows or [record()])


class ReadOnlyR2:
    def __init__(self, row, payload):
        self.key = original.OriginalCache.key(row["binding"])
        self.payload = payload
        self.metadata = {"sha256": row["sha256"], "kind": "institution-original-proof"}
        self.content_type = "application/pdf"
        self.calls = []

    def get_object(self, **kwargs):
        self.calls.append(kwargs)
        if kwargs["Key"] != self.key:
            raise AssertionError("Unexpected object identity")
        return dict(Body=io.BytesIO(self.payload), ContentLength=len(self.payload),
                    ContentType=self.content_type, Metadata=self.metadata)

    def put_object(self, **kwargs):
        raise AssertionError("Recovery cannot write storage")


class VerifiedOriginalTests(unittest.TestCase):
    def setup_selection(self, root, value=None, payload=None):
        payload = payload if payload is not None else pdf()
        value = value or manifest()
        path = root / "reviewed.json"; path.write_text(json.dumps(value))
        pending = PendingIntake(root / "pending.json", {}, now=NOW)
        pending.admit(item(), 7)
        pending = PendingIntake(root / "pending.json", {}, now=NOW)
        store = ReadOnlyR2(value["records"][0], payload)
        cache = original.OriginalCache(store, "synthetic-private")
        selection = verified.VerifiedOriginals(path, cache_factory=lambda: cache)
        return selection, pending, store, root / filename(item())

    def test_exact_cache_read_preserves_bytes_and_leaves_state_untouched(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); selection, pending, store, dest = self.setup_selection(root)
            before = pending.path.read_bytes()
            result = selection.restore(item(), dest.name, pending, dest, original.MAX_PDF)
            self.assertEqual(dest.read_bytes(), pdf())
            self.assertEqual(result["acquisition_method"], "verified_original_cache")
            self.assertEqual(result["pdf_url"], record()["official_pdf_url"])
            self.assertEqual(result["verified_original_pages"], 2)
            self.assertEqual(pending.path.read_bytes(), before)
            self.assertEqual(len(store.calls), 1)
            self.assertEqual(list(root.glob(".verified-original-*")), [])

    def test_whole_manifest_is_validated_before_any_cache_read(self):
        mutations = [
            lambda x: x.update(schema=True), lambda x: x.update(extra="unreviewed"),
            lambda x: x.update(frozen_pending_sha256="bad"),
            lambda x: x["records"].append(copy.deepcopy(x["records"][0])),
            lambda x: x["records"][0].update(size=True),
            lambda x: x["records"][0].update(pages=0),
            lambda x: x["records"][0].update(sha256="0"*64),
            lambda x: x["records"][0]["binding"].update(id="0"*64),
            lambda x: x["records"][0]["verification"].update(review="pending"),
            lambda x: x["records"][0]["verification"].update(receipt_sha256="bad"),
            lambda x: x["records"][0]["verification"].update(reviewed_at="2026-10-12"),
            lambda x: x["records"][0]["item"].update(date="undated"),
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manifest.json"
            for mutate in mutations:
                value = manifest(); mutate(value); path.write_text(json.dumps(value))
                with self.subTest(mutate=mutate), self.assertRaises(verified.VerifiedOriginalError):
                    verified.VerifiedOriginals(path, cache_factory=lambda: self.fail("Unexpected R2 read"))

    def test_snapshot_hash_is_provenance_and_retry_counters_do_not_change_identity(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            value = manifest(); value["frozen_pending_sha256"] = "3" * 64
            selection, pending, store, dest = self.setup_selection(root, value)
            self.assertEqual(selection.frozen_pending_provenance_sha256, "3" * 64)
            self.assertNotEqual(digest(pending.path.read_bytes()), "3" * 64)
            before = pending.path.read_bytes()
            pending.admit(item(), 7)
            self.assertNotEqual(pending.path.read_bytes(), before)
            selection.restore(item(), dest.name, pending, dest, original.MAX_PDF)
            self.assertEqual(len(store.calls), 1)
            # A valid provenance label never permits changed report metadata.
            pending.items["imf:synthetic-1"]["item"]["title"] += " changed"
            with self.assertRaisesRegex(verified.VerifiedOriginalError, "pending_identity"):
                selection.restore(item(), dest.name, pending, dest, original.MAX_PDF)
            self.assertEqual(len(store.calls), 1)

    def test_exact_pending_identity_and_stable_filename_are_required_before_cache(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for field in ("guid", "title", "source_url", "date", "pdf_candidates", "scrape_url", "coveo_unique_id"):
                selection, pending, store, dest = self.setup_selection(root)
                candidate = item(); candidate[field] = ["https://www.imf.org/other.pdf"] if field == "pdf_candidates" else "changed"
                if field == "guid":
                    self.assertFalse(selection.contains(candidate))
                    continue
                with self.subTest(field=field), self.assertRaisesRegex(verified.VerifiedOriginalError, "pending_identity"):
                    selection.restore(candidate, dest.name, pending, dest, original.MAX_PDF)
                self.assertEqual(store.calls, [])
            selection, pending, store, dest = self.setup_selection(root)
            pending.initial_keys.clear()
            with self.assertRaisesRegex(verified.VerifiedOriginalError, "pending_identity"):
                selection.restore(item(), dest.name, pending, dest, original.MAX_PDF)
            pending.initial_keys.add("imf:synthetic-1")
            with self.assertRaisesRegex(verified.VerifiedOriginalError, "selected_identity"):
                selection.restore(item(), "different.pdf", pending, root/"different.pdf", original.MAX_PDF)
            self.assertEqual(store.calls, [])

    def test_invalid_cache_metadata_bytes_and_page_counts_cannot_materialize(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            changes = [lambda store: setattr(store, "payload", pdf()+b"tamper"),
                       lambda store: setattr(store, "content_type", "text/html"),
                       lambda store: setattr(store, "metadata", {"sha256": "0"*64, "kind": "institution-original-proof"})]
            for change in changes:
                selection, pending, store, dest = self.setup_selection(root); change(store)
                with self.assertRaises(verified.VerifiedOriginalError):
                    selection.restore(item(), dest.name, pending, dest, original.MAX_PDF)
                self.assertFalse(dest.exists())
            value = manifest(); value["records"][0]["pages"] = 3
            selection, pending, _, dest = self.setup_selection(root, value)
            with self.assertRaisesRegex(verified.VerifiedOriginalError, "page_count"):
                selection.restore(item(), dest.name, pending, dest, original.MAX_PDF)
            self.assertFalse(dest.exists())
            fake = b"%PDF-not-a-real-document"
            selection, pending, _, dest = self.setup_selection(root, manifest([record(payload=fake)]), fake)
            with self.assertRaisesRegex(verified.VerifiedOriginalError, "pdf_invalid"):
                selection.restore(item(), dest.name, pending, dest, original.MAX_PDF)
            self.assertFalse(dest.exists())

    def test_official_url_pair_cannot_downgrade_or_escape(self):
        for language in ("en", "es"):
            for prefix, suffix, is_pdf in (("/", ".xml?cid=580315-com-dsp-crossref", False), ("/downloadpdf/", ".pdf", True)):
                self.assertTrue(verified.official_url(
                    f"https://www.elibrary.imf.org{prefix}view/journals/019/2026/082/019.2026.issue-082-{language}{suffix}", pdf=is_pdf))
        self.assertFalse(verified.official_url(
            "https://www.elibrary.imf.org/downloadpdf/view/journals/019/2026/082/019.2026.issue-083-en.pdf", pdf=True))
        invalid = ["http://www.elibrary.imf.org/downloadpdf/view/journals/001/2026/001/article-A001-en.pdf",
                   "https://user@www.elibrary.imf.org/downloadpdf/view/journals/001/2026/001/article-A001-en.pdf",
                   "https://www.elibrary.imf.org:444/downloadpdf/view/journals/001/2026/001/article-A001-en.pdf",
                   "https://fake.invalid/downloadpdf/view/journals/001/2026/001/article-A001-en.pdf",
                   record()["official_pdf_url"]+"?auth=private", record()["official_pdf_url"]+"#private",
                   record()["official_pdf_url"].replace("/001/2026/001/", "/001/2026/002/")]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/"manifest.json"
            for url in invalid:
                value=manifest(); value["records"][0]["official_pdf_url"]=url; path.write_text(json.dumps(value))
                with self.subTest(url=url), self.assertRaises(verified.VerifiedOriginalError):
                    verified.VerifiedOriginals(path)

    def test_missing_duplicate_json_or_symlink_manifest_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/"manifest.json"
            with self.assertRaises(verified.VerifiedOriginalError): verified.VerifiedOriginals(path)
            path.write_text('{"schema":1,"schema":1}')
            with self.assertRaisesRegex(verified.VerifiedOriginalError, "duplicate_json_key"): verified.VerifiedOriginals(path)
            path.unlink(); target=Path(directory)/"target"; target.write_text(json.dumps(manifest())); path.symlink_to(target)
            with self.assertRaises(verified.VerifiedOriginalError): verified.VerifiedOriginals(path)

    def fetch(self, root, *, enabled=True, sources=None, cache_missing=False, live_success=False):
        class Clock(datetime):
            @classmethod
            def now(cls, tz=None): return NOW
        value = manifest(); review = root/"reviewed.json"; review.write_text(json.dumps(value))
        store = ReadOnlyR2(value["records"][0], pdf())
        cache = original.OriginalCache(store, "synthetic-private")
        if cache_missing:
            cache = types.SimpleNamespace(get=lambda binding: None)
        args = ["fetch", "--output-dir", str(root/"pdfs"), "--date", "261012", "--institutions", "imf",
                "--seen-state-path", str(root/"seen.json"), "--archive-path", str(root/"archive.jsonl"),
                "--pending-intake-path", str(root/"pending.json"), "--since-days", "7"]
        if enabled: args += ["--verified-originals-manifest", str(review)]
        def live(session, candidates, dest, *args, **kwargs):
            if live_success: dest.write_bytes(pdf(2)); return candidates[0], "ok"
            return None, "http_403"
        with (patch.object(f.sys,"argv",args), patch.object(f,"datetime",Clock),
              patch.dict(f.os.environ,{"PROXY_SUBSCRIPTION_URL":"","GITHUB_OUTPUT":"","GITHUB_STEP_SUMMARY":""}),
              patch.object(f,"collect_coveo_items",return_value=copy.deepcopy(sources if sources is not None else [item()])),
              patch.object(f,"download_pdf",side_effect=live) as download,
              patch.object(f,"http_get",side_effect=AssertionError("No live network")),
              patch.object(verified,"_cache",return_value=cache) as factory,
              redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO())):
            code=f.main()
        data=json.loads((root/"pdfs/institution_run_manifest.json").read_text())
        classified=health.classify(data,producer_exit_code=code,log_exit_code=0,date_folder="261012",institutions="imf")
        return code,data,classified,download.call_count,factory.call_count

    def test_cache_recovery_is_visible_degraded_and_downstream_failure_keeps_pending(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory); PendingIntake(root/"pending.json",{},now=NOW).admit(item(),7)
            code,data,status,live,factory=self.fetch(root)
            self.assertEqual((code,live,factory,status["source_health"]),(0,0,1,"degraded"))
            self.assertEqual(data["downloaded"][0]["published"],item()["date"])
            self.assertEqual(data["downloaded"][0]["source_page_url"],item()["source_url"])
            self.assertEqual(data["source_checks"][0]["verified_original_recovery_count"],1)
            self.assertEqual(data["downloaded"][0]["pdf_url"],record()["official_pdf_url"])
            self.assertIn("imf:synthetic-1",json.loads((root/"pending.json").read_text())["items"])
            # Existing workflow commits provisional seen only after translated handoff.
            (root/"seen.json").unlink()
            code,_,_,live,factory=self.fetch(root)
            self.assertEqual((code,live,factory),(0,0,1))

    def test_missing_cache_remains_queued_with_no_live_fallback_or_seen(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory); PendingIntake(root/"pending.json",{},now=NOW).admit(item(),7)
            code,data,status,live,_=self.fetch(root,cache_missing=True)
            self.assertEqual((code,live,data["downloaded_count"],status["source_health"]),(2,0,0,"degraded"))
            self.assertEqual(data["skipped"][0]["reason"],"verified_original_cache_missing")
            self.assertNotIn("imf:synthetic-1",json.loads((root/"seen.json").read_text())["items"])
            self.assertIn("imf:synthetic-1",json.loads((root/"pending.json").read_text())["items"])

    def test_new_matching_report_cannot_use_allowlist_without_previous_admission(self):
        with tempfile.TemporaryDirectory() as directory:
            code,data,_,live,factory=self.fetch(Path(directory))
            self.assertEqual((code,live,factory,data["downloaded_count"]),(2,0,0,0))
            self.assertEqual(data["skipped"][0]["reason"],"verified_original_pending_identity")

    def test_default_off_and_unlisted_items_retain_normal_live_path(self):
        with tempfile.TemporaryDirectory() as directory:
            code,data,status,live,factory=self.fetch(Path(directory),enabled=False,live_success=True)
            self.assertEqual((code,live,factory,status["source_health"]),(0,1,0,"healthy"))
            self.assertNotIn("verified_original_recovery_count",data["source_checks"][0])
            self.assertNotIn("acquisition_method",data["downloaded"][0])
        with tempfile.TemporaryDirectory() as directory:
            code,data,_,live,factory=self.fetch(Path(directory),sources=[item(2)],live_success=True)
            self.assertEqual((code,live,factory,data["downloaded_count"]),(0,1,0,1))

    def test_empty_discovery_and_inconsistent_recovery_health_stay_visible(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory); PendingIntake(root/"pending.json",{},now=NOW).admit(item(),7)
            code,data,status,_,_=self.fetch(root,sources=[])
            self.assertTrue(data["source_checks"][0]["discovery_error"])
            self.assertEqual(data["source_checks"][0]["status"], "error")
            self.assertEqual(status["source_health"],"degraded")
            self.assertEqual(status["source_health_backlog_only"], "false")
            for change in (lambda x:x["source_checks"][0].update(status="ok"),
                           lambda x:x["source_checks"][0].update(status="degraded"),
                           lambda x:x["source_checks"][0].update(verified_original_recovery_count=0),
                           lambda x:x["source_checks"][0].update(verified_original_manifest_sha256="0"*64),
                           lambda x:x["downloaded"][0].update(acquisition_method="live")):
                changed=copy.deepcopy(data);change(changed)
                with self.assertRaises(health.InvalidSourceHealth):
                    health.classify(changed,producer_exit_code=code,log_exit_code=0,date_folder="261012",institutions="imf")

    def test_cache_recovery_preserves_source_error_and_partial_live_success(self):
        for discovery, live_success, expected in ((True, False, "degraded"),
                                                  (False, False, "error"),
                                                  (False, True, "degraded")):
            with self.subTest(discovery=discovery, live_success=live_success), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                pending = PendingIntake(root/"pending.json", {}, now=NOW)
                pending.admit(item(), 7); pending.admit(item(2), 7)
                code, data, classified, live, _ = self.fetch(
                    root, sources=[item(), item(2)] if discovery else [], live_success=live_success)
                self.assertEqual((code, live, data["source_checks"][0]["status"]), (0, 1, expected))
                self.assertEqual(classified["source_health"], "degraded")
                self.assertEqual(data["source_checks"][0]["verified_original_recovery_count"], 1)

    def test_incomplete_or_unknown_recovery_proof_cannot_claim_healthy(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory); PendingIntake(root/"pending.json",{},now=NOW).admit(item(),7)
            code, data, _, _, _ = self.fetch(root)
            for missing in verified.RECOVERY_FIELDS:
                changed = copy.deepcopy(data)
                del changed["downloaded"][0][missing]
                check = changed["source_checks"][0]
                check.pop("verified_original_recovery_count")
                check.pop("verified_original_manifest_sha256")
                check["status"] = "ok"
                with self.subTest(missing=missing), self.assertRaises(health.InvalidSourceHealth):
                    health.classify(changed,producer_exit_code=code,log_exit_code=0,date_folder="261012",institutions="imf")
            changed = copy.deepcopy(data)
            changed["downloaded"][0]["verified_original_unknown"] = "unrecognized"
            with self.assertRaises(health.InvalidSourceHealth):
                health.classify(changed,producer_exit_code=code,log_exit_code=0,date_folder="261012",institutions="imf")
        with tempfile.TemporaryDirectory() as directory:
            code, data, _, _, _ = self.fetch(Path(directory), enabled=False, live_success=True)
            data["downloaded"][0]["verified_original_unknown"] = "unrecognized"
            with self.assertRaises(health.InvalidSourceHealth):
                health.classify(data,producer_exit_code=code,log_exit_code=0,date_folder="261012",institutions="imf")

    def test_summary_keeps_cache_recovery_visible_even_after_long_live_errors(self):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/"summary.md"
            with patch.dict(f.os.environ,{"GITHUB_STEP_SUMMARY":str(path)}):
                f.write_source_health_summary([dict(institution="imf",status="degraded",error="live error "*100,
                    item_count=2,new_pdf_count=1,verified_original_recovery_count=1)])
            self.assertIn("1 reviewed original(s) recovered from private cache",path.read_text())
            self.assertIn("Live PDF access remains unverified",path.read_text())


if __name__ == "__main__": unittest.main()
