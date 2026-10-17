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


def producer_manifest(payload=None):
    row = record(payload=payload)
    source, binding = row['item'], row['binding']
    publication = dict(institution='imf', title=source['title'], local_filename=binding['source'],
                       source_page_url=source['source_url'], published=source['date'],
                       pdf_url=source['pdf_candidates'][0], feed_pdf_candidates=source['pdf_candidates'],
                       sha256=binding['sha256'], bytes=binding['size'], date='261012')
    raw = json.dumps(dict(date='261012', downloaded_count=1, downloaded=[publication]))
    return dict(schema=2, institution='imf', frozen_pending_sha256='2'*64,
                producer=dict(run_id=123, head_sha='3'*40, artifact_id=456,
                              artifact_sha256='4'*64, manifest_sha256=digest(raw.encode())),
                source_manifest_json=raw, records=[dict(item=source, binding=binding)])


def change_producer_publication(value, mutate):
    source = json.loads(value['source_manifest_json'])
    mutate(source)
    value['source_manifest_json'] = json.dumps(source)
    value['producer']['manifest_sha256'] = digest(value['source_manifest_json'].encode())


class ReadOnlyR2:
    def __init__(self, row, payload):
        self.key = original.OriginalCache.key(row["binding"])
        self.payload = payload
        self.metadata = {"sha256": row["binding"]["sha256"], "kind": "institution-original-proof"}
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
    def test_october15_selection_contains_only_the_three_proven_pending_originals(self):
        path = Path('institution_feeds/reviewed_originals/imf-20261015-reviewed.json')
        selection = verified.VerifiedOriginals(path, cache_factory=lambda: self.fail('Unexpected R2 read'))
        self.assertEqual(digest(path.read_bytes()), 'c880842e7f022145eaca780dd52017934444ab7c7f1be7208a9cc7f74b81196b')
        pinned = json.loads(Path('scripts/fixtures/institution_sources/figure_metadata_20261015.json').read_bytes())
        expected = {row['local_filename']: (row['sha256'], row['bytes'])
                    for row in pinned['sources'] if row['local_filename'].startswith('IMF_')}
        actual = {row['binding']['source']: (row['sha256'], row['size']) for row in selection.records.values()}
        self.assertEqual(actual, expected)
        self.assertEqual(len(actual), 3)
        for row in selection.records.values():
            self.assertEqual(filename(row['item']), row['binding']['source'])
        self.assertEqual(sorted(row['pages'] for row in selection.records.values()), [9, 48, 214])

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

    def test_failed_producer_archive_restores_without_mineru_admission_or_state_writes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            selection, pending, store, dest = self.setup_selection(root, producer_manifest())
            before = pending.path.read_bytes()
            self.assertIsNone(selection.records['imf:synthetic-1']['pages'])
            result = selection.restore(item(), dest.name, pending, dest, original.MAX_PDF)
            self.assertEqual(dest.read_bytes(), pdf())
            self.assertEqual(result['verified_original_pages'], 2)
            self.assertEqual(result['pdf_url'], item()['pdf_candidates'][0])
            self.assertEqual(result['verified_original_receipt_sha256'],
                             producer_manifest()['producer']['manifest_sha256'])
            self.assertEqual(pending.path.read_bytes(), before)
            self.assertEqual(len(store.calls), 1)
            self.assertEqual(set(path.name for path in root.iterdir()),
                             {'pending.json', 'reviewed.json', dest.name})

    def test_europe_selection_binds_exact_original_failed_run_and_only_selected_publication(self):
        path = Path('institution_feeds/reviewed_originals/imf-europe-20261017-cached.json')
        raw = path.read_bytes()
        self.assertEqual(digest(raw), 'ab27239ae15d4680794800e46ed4b3102e7fdda8bccbdb312c9451c8337100e9')
        data = json.loads(raw)
        self.assertEqual(data['producer'], dict(run_id=38984663136,
            head_sha='ff052eff4b1b6843e86372ee93799a2454c529c0', artifact_id=12081923844,
            artifact_sha256='db3e297276f22c4cc2201205761b407420fe0bc4d90fd2d7b456321481e4f8b6',
            manifest_sha256='587458de79cc50be98567a062da0e5155b44c81344974ff7cb9fc7652d962c9f'))
        selection = verified.VerifiedOriginals(path, cache_factory=lambda: self.fail('Unexpected R2 read'))
        self.assertEqual(list(selection.records), ['imf:74d8db8233c171213861d1f872b00e7b34fdfffc2772b202becd9f42c84c'])
        row = next(iter(selection.records.values()))
        self.assertEqual(row['binding']['id'], 'de2a34bcfa661abcdf0c82db9702d1fb9d76f0f93759b6782bcb291504a11809')
        self.assertEqual(row['sha256'], '4c3172f10a8fe354088740510fc72254bd90c3577dcd95fc10c5fa3fced1ebfc')
        self.assertEqual(row['size'], 5643283)
        self.assertEqual(row['item']['date'], '2026-10-16T21:00:00+00:00')
        self.assertEqual(row['binding']['source'], filename(row['item']))
        self.assertEqual(row['official_landing_url'], row['item']['source_url'])
        self.assertEqual(row['official_pdf_url'],
                         'https://www.imf.org/-/media/files/publications/reo/eur/2026/october/english/text.pdf')
        self.assertEqual(json.loads(data['source_manifest_json'])['downloaded_count'], 4)

    def test_producer_receipt_and_exact_publication_are_validated_before_cache(self):
        mutations = [
            lambda x: x['producer'].update(run_id=True),
            lambda x: x['producer'].update(head_sha='bad'),
            lambda x: x['producer'].update(artifact_sha256='bad'),
            lambda x: x.update(source_manifest_json=x['source_manifest_json'] + '\n'),
            lambda x: x['records'][0]['item'].update(title='Different report'),
            lambda x: x['records'][0]['binding'].update(id='0'*64),
            lambda x: x['records'].append(copy.deepcopy(x['records'][0])),
        ]
        for field, replacement in (
                ('institution', 'other'), ('title', 'Other report'), ('published', item(2)['date']+' '),
                ('source_page_url', item(2)['source_url']), ('pdf_url', 'https://untrusted.invalid/report.pdf'),
                ('feed_pdf_candidates', []), ('sha256', '0'*64), ('bytes', True), ('date', '261011'),
                ('local_filename', 'Different.pdf')):
            mutations.append(lambda x, field=field, replacement=replacement: change_producer_publication(
                x, lambda source: source['downloaded'][0].update({field: replacement})))
        mutations.extend([
            lambda x: change_producer_publication(x, lambda source: source.update(downloaded_count=2)),
            lambda x: change_producer_publication(x, lambda source: source.update(date=None)),
            lambda x: change_producer_publication(x, lambda source: source['downloaded'].append(
                copy.deepcopy(source['downloaded'][0]))),
        ])
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'reviewed.json'
            for index, mutate in enumerate(mutations):
                value = producer_manifest(); mutate(value); path.write_text(json.dumps(value))
                with self.subTest(index=index), self.assertRaises(verified.VerifiedOriginalError):
                    verified.VerifiedOriginals(path, cache_factory=lambda: self.fail('Unexpected R2 read'))
            for raw, code in (('{private malformed content', 'producer_manifest_json'),
                              ('{"date":"261012","date":"261012"}', 'duplicate_json_key')):
                value = producer_manifest(); value['source_manifest_json'] = raw
                value['producer']['manifest_sha256'] = digest(raw.encode())
                path.write_text(json.dumps(value))
                with self.subTest(raw=raw), self.assertRaisesRegex(verified.VerifiedOriginalError, code):
                    verified.VerifiedOriginals(path)

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

    def test_book_original_requires_matching_isbn_path_pair_and_doi(self):
        isbn = "9798229056298"
        landing = f"https://www.elibrary.imf.org/display/book/{isbn}/{isbn}.xml"
        pdf_url = f"https://www.elibrary.imf.org/downloadpdf/display/book/{isbn}/{isbn}.pdf"
        row = record(); row.update(official_landing_url=landing, official_pdf_url=pdf_url, doi=f"10.5089/{isbn}.089")
        verified._validate_record(row)
        for field, value in (
            ("official_pdf_url", pdf_url.replace(".org/", ".org.evil.invalid/")),
            ("official_pdf_url", pdf_url.replace("9798229056298.pdf", "9798229056299.pdf")),
            ("official_pdf_url", pdf_url.replace(isbn, "9798229056299")),
            ("official_pdf_url", pdf_url.replace("/display/book/", "/display/books/")),
            ("official_pdf_url", pdf_url.replace(isbn, "979822905629")),
            ("official_pdf_url", pdf_url + "?private=token"),
            ("official_landing_url", landing.replace(isbn, "9798229056299")),
            ("doi", "10.5089/9798229056299.089"),
        ):
            changed = copy.deepcopy(row); changed[field] = value
            with self.subTest(field=field, value=value), self.assertRaises(verified.VerifiedOriginalError):
                verified._validate_record(changed)

    def test_only_observed_official_acquisition_methods_are_accepted(self):
        for method in ("official_browser_download", "official_https_download"):
            row = record(); row["verification"]["method"] = method
            verified._validate_record(row)
        for method in ("", "browser", "cache", "official_http_download", None, True, [], {}):
            row = record(); row["verification"]["method"] = method
            with self.subTest(method=method), self.assertRaises(verified.VerifiedOriginalError):
                verified._validate_record(row)

    def test_ieo_fiscal_route_requires_exact_pair_and_pending_source_identity(self):
        source = item()
        source.update(guid=verified.IEO_FISCAL_GUID, source_url=verified.IEO_FISCAL_SOURCE)
        row = record(source)
        row.update(official_landing_url=verified.IEO_FISCAL_LANDING,
                   official_pdf_url=verified.IEO_FISCAL_PDF, doi="10.5089/9798229064200.007")
        row["verification"]["method"] = "official_https_download"
        verified._validate_record(row)
        for field, value in (
            ("official_landing_url", verified.IEO_FISCAL_LANDING + "/other"),
            ("official_landing_url", verified.IEO_FISCAL_LANDING.replace("2025-1216", "2025-1217")),
            ("official_landing_url", record()["official_landing_url"]),
            ("official_pdf_url", verified.IEO_FISCAL_PDF.replace("ieo.imf.org", "ieo.imf.org.evil.invalid")),
            ("official_pdf_url", verified.IEO_FISCAL_PDF.replace("fp-mip.pdf", "other.pdf")),
            ("official_pdf_url", verified.IEO_FISCAL_PDF + "?token=private"),
            ("official_pdf_url", verified.IEO_FISCAL_PDF.replace("/-/media/", "/-/media/../media/")),
            ("official_pdf_url", verified.IEO_FISCAL_PDF.replace("https://", "http://")),
            ("official_pdf_url", record()["official_pdf_url"]),
        ):
            changed = copy.deepcopy(row); changed[field] = value
            with self.subTest(field=field, value=value), self.assertRaises(verified.VerifiedOriginalError):
                verified._validate_record(changed)
        for field, value in (("guid", "different"), ("source_url", item()["source_url"])):
            changed = copy.deepcopy(row); changed["item"][field] = value
            with self.subTest(identity=field), self.assertRaisesRegex(verified.VerifiedOriginalError, "ieo_identity"):
                verified._validate_record(changed)

    def fetch(self, root, *, enabled=True, sources=None, cache_missing=False, live_success=False, value=None):
        class Clock(datetime):
            @classmethod
            def now(cls, tz=None): return NOW
        value = value or manifest(); review = root/"reviewed.json"; review.write_text(json.dumps(value))
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

    def test_failed_producer_selection_follows_existing_fetch_and_pending_boundaries(self):
        for cache_missing in (False, True):
            with self.subTest(cache_missing=cache_missing), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                PendingIntake(root/'pending.json', {}, now=NOW).admit(item(), 7)
                code, data, status, live, factory = self.fetch(
                    root, value=producer_manifest(), cache_missing=cache_missing)
                self.assertEqual((live, factory, status['source_health']), (0, 1, 'degraded'))
                self.assertEqual((code, data['downloaded_count']), (2, 0) if cache_missing else (0, 1))
                self.assertIn('imf:synthetic-1', json.loads((root/'pending.json').read_text())['items'])
                if cache_missing:
                    self.assertEqual(data['skipped'][0]['reason'], 'verified_original_cache_missing')
                    self.assertNotIn('imf:synthetic-1', json.loads((root/'seen.json').read_text())['items'])
                else:
                    self.assertEqual(data['downloaded'][0]['sha256'], record()['sha256'])
                    self.assertEqual(data['downloaded'][0]['published'], item()['date'])
                    self.assertEqual(data['downloaded'][0]['verified_original_pages'], 2)

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
