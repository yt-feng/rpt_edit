#!/usr/bin/env python3
import io
import gzip
import json
import tarfile
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import publish_customer_content as subject


class StorageError(Exception):
    def __init__(self, code):
        self.response = {"Error": {"Code": code}}


class MemoryR2:
    def __init__(self):
        self.rows = {}
        self.version = 0
        self.fail_key = ""
        self.conflict = False
        self.headers = {}
        self.after_put = None
        self.reads = []

    def get_object(self, *, Bucket, Key):
        self.reads.append(Key)
        if Key not in self.rows:
            raise StorageError("NoSuchKey")
        raw, etag = self.rows[Key]
        return {"Body": io.BytesIO(raw), "ETag": etag, "ContentLength": len(raw), **self.headers.get(Key, {})}

    def put_object(self, *, Bucket, Key, Body, **kwargs):
        if self.fail_key and self.fail_key in Key:
            raise StorageError("AccessDenied")
        old = self.rows.get(Key)
        if kwargs.get("IfNoneMatch") == "*" and old or kwargs.get("IfMatch") and (not old or old[1] != kwargs["IfMatch"]):
            raise StorageError("PreconditionFailed")
        if self.conflict and "IfMatch" in kwargs:
            self.conflict = False
            raise StorageError("PreconditionFailed")
        self.version += 1
        self.rows[Key] = (Body, f'"v{self.version}"')
        self.headers[Key] = {key: kwargs[key] for key in ("ContentType", "Metadata") if key in kwargs}
        if self.after_put:
            self.after_put(Key)

    def list_objects_v2(self, *, Bucket, Prefix, MaxKeys):
        rows = [{"Key": key, "Size": len(raw)} for key, (raw, _etag) in self.rows.items() if key.startswith(Prefix)]
        return {"Contents": rows[:MaxKeys], "IsTruncated": len(rows) > MaxKeys}


class PublisherTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.report = self.root / "report"
        self.report.mkdir()
        self.client = MemoryR2()
        self.catalog = [{"id": "a" * 24, "title": "Energy outlook", "date_folder": "261012", "r2_key": "private.pdf", "password": "SECRET"}]
        (self.report / "status.json").write_text(json.dumps({"source_pdf": "/runner/private/Energy outlook.pdf", "full_zip_url": "https://private.invalid/SECRET"}))
        (self.report / "source_mineru.md").write_text("# Energy outlook\nDemand grows.\n")

    def publish(self):
        return subject.publish_directory(self.client, "bucket", self.root, self.catalog, "2026-10-12")

    def manifest(self):
        return json.loads(self.client.rows[f"{subject.PREFIX}/reports/{'a' * 24}/manifest.json"][0])

    def test_only_selected_content_and_allowlisted_metadata_are_published(self):
        (self.report / "prompt_for_wechat.md").write_text("SYSTEM SECRET")
        (self.report / "config.json").write_text('{"secret":"SECRET"}')
        result = self.publish()
        self.assertEqual(result, {"reports": 1, "artifacts": 2})
        all_bytes = b"".join(raw for raw, _ in self.client.rows.values())
        for marker in (b"SECRET", b"/runner", b"full_zip_url", b"password", b"r2_key"):
            self.assertNotIn(marker, all_bytes)
        self.assertEqual({row["kind"] for row in self.manifest()["artifacts"]}, {"text", "metadata"})

    def test_retry_does_not_duplicate_artifacts_and_translation_merges(self):
        self.publish()
        self.client.conflict = True
        self.publish()
        self.assertEqual(len(self.manifest()["artifacts"]), 2)
        translated = self.root / "translation"
        translated.mkdir()
        (translated / "translation_status.json").write_text(json.dumps({"source_title": "Energy outlook"}))
        (translated / "translated.md").write_text("# 能源展望\n需求增长。")
        self.publish()
        self.assertEqual(len(self.manifest()["artifacts"]), 4)
        self.assertEqual({row["language"] for row in self.manifest()["artifacts"]}, {"und", "zh"})

    def test_incomplete_upload_never_publishes_manifest_or_index(self):
        self.client.fail_key = "/blobs/"
        with self.assertRaises(StorageError):
            self.publish()
        self.assertFalse(any(key.endswith("manifest.json") or key.endswith("index.json") for key in self.client.rows))

    def test_extraction_method_requires_completed_mineru_status(self):
        for state, expected in ((None, "stored_text"), ("failed", "stored_text"), ("done", "mineru")):
            status = {"source_pdf": "Energy outlook.pdf"}
            if state is not None:
                status["mineru_state"] = state
            (self.report / "status.json").write_text(json.dumps(status))
            _row, metadata = subject.report_binding(self.report, self.catalog, "2026-10-12")
            self.assertEqual(metadata["extraction_method"], expected)

    def test_symlink_content_is_rejected(self):
        (self.report / "source_mineru.md").unlink()
        outside = self.root / "private.txt"
        outside.write_text("PRIVATE")
        (self.report / "source_mineru.md").symlink_to(outside)
        with self.assertRaises(ValueError):
            self.publish()
        self.assertEqual(self.client.rows, {})

    def test_ambiguous_title_gets_distinct_processed_report_no_guessed_pdf(self):
        self.catalog.append({"id": "b" * 24, "title": "Energy outlook", "date_folder": "261012"})
        row, _ = subject.report_binding(self.report, self.catalog, "2026-10-12")
        self.assertNotIn(row["id"], {"a" * 24, "b" * 24})
        self.assertFalse(row["available"])
        self.assertEqual(row["source"], "processed")

    def test_invalid_date_and_unknown_run_never_scan_bucket(self):
        with self.assertRaises(ValueError):
            subject.date_iso("2026-02-31")
        with self.assertRaises(ValueError):
            subject.publish_run(self.client, "bucket", "../secret", [])

    def test_same_title_on_another_date_does_not_inherit_catalog_access(self):
        self.catalog[0]["date_folder"] = "261011"
        row, _ = subject.report_binding(self.report, self.catalog, "2026-10-12")
        self.assertNotEqual(row["id"], "a" * 24)
        self.catalog[0]["date_folders"] = ["261011", "261012"]
        row, _ = subject.report_binding(self.report, self.catalog, "2026-10-12")
        self.assertEqual(row["id"], "a" * 24)

    def test_both_image_directories_are_rewritten_to_delivered_filenames(self):
        hashed = "a" * 64 + ".jpg"
        for folder, name in (("images", hashed), ("assets", "source_image_1.png")):
            (self.report / folder).mkdir()
            (self.report / folder / name).write_bytes(b"synthetic-image")
        (self.report / "source_mineru.md").write_text(f"![A](images/{hashed})\n![B](assets/source_image_1.png)")
        body = subject.content_files(self.report)[0][3].decode()
        self.assertEqual(body, f"![A]({hashed})\n![B](source_image_1.png)")

    def test_source_alias_and_translation_token_use_actual_images_without_private_locators(self):
        assets = self.report / "assets"
        assets.mkdir()
        image = b"synthetic-image"
        (assets / "source_image_01.png").write_bytes(image)
        (assets / "fig001.jpg").write_bytes(b"translation-image")
        reference = "images/" + "d" * 64 + ".jpg"
        (self.report / "images").mkdir()
        (self.report / reference).write_bytes(b"provider-thumbnail")
        (self.report / "source_figure_map.json").write_text(json.dumps({"assets": [{
            "ref": reference, "path": "assets/source_image_01.png", "sha256": subject.digest(image), "page_idx": 0,
        }]}))
        (self.report / "figure_manifest.json").write_text(json.dumps([{
            "token": "[[PORTAL_IMAGE_001]]", "relative_path": "fig001.jpg", "source_path": "/private/SECRET.png",
        }]))
        (self.report / "source_mineru.md").write_text(f'![Chart]({reference})\n<img src="{reference}">\n![Missing](/private/SECRET.png)\n![Remote](https://private.invalid/SECRET)\n![Ref][raw]\n[raw]: {reference}\n![Absent][private]\n[private]: /private/SECRET.png')
        (self.report / "translated.md").write_text("译文\n[[PORTAL_IMAGE_001]]")
        files = {name: body for name, _kind, _language, body in subject.content_files(self.report)}
        self.assertEqual(files["source_mineru.md"].decode(), "![Chart](source_image_01.png)\n![](source_image_01.png)\nMissing\nRemote\n![Ref](source_image_01.png)\nAbsent\n")
        self.assertEqual(files["translated.md"].decode(), "译文\n![](fig001.jpg)")
        self.assertNotIn(b"SECRET", b"".join(files.values()))
        self.assertIn("fig001.jpg", files)

    def test_figure_metadata_recursively_projects_typed_text_and_geometry(self):
        (self.report / "source_figure_map.json").write_text(json.dumps({"provider": {"secret": "SECRET"}, "metadata": {
            "records": [{"index": 1, "page_idx": 0, "kind": "table", "body_bbox": [1, 2, 3, 4],
                         "caption": {"secret": "SECRET"}, "text": ["SECRET"], "body_text": "Public table",
                         "captions": [{"text": "Public caption", "bbox": [1, 2, 3, 4], "provider": {"secret": "SECRET"}},
                                      {"text": {"secret": "SECRET"}, "bbox": [1, 2, 3, 4]}],
                         "footnotes": ["Public note", {"nested": "SECRET"}], "provider_session": "SECRET"}],
            "pages": [{"page_idx": 0, "provider_size": [600, 800], "path": "/private/SECRET", "text_blocks": [
                {"index": 1, "kind": "text", "text": "Public text", "bbox": [0, 0, 10, 10], "secret": "SECRET"}]}],
        }, "assets": []}))
        files = {name: body for name, _kind, _language, body in subject.content_files(self.report)}
        projected = json.loads(files["figure-metadata.json"])
        self.assertNotIn(b"SECRET", files["figure-metadata.json"])
        self.assertEqual(projected["records"][0]["captions"], [{"text": "Public caption", "bbox": [1, 2, 3, 4]}])
        self.assertEqual(projected["pages"][0]["page_size"], [600, 800])
        self.assertEqual(projected["pages"][0]["text_blocks"][0]["text"], "Public text")

    def test_image_alias_requires_matching_content_hash_and_unambiguous_filename(self):
        for folder in ("assets", "images"):
            (self.report / folder).mkdir()
            (self.report / folder / "fig001.jpg").write_bytes(folder.encode())
        with self.assertRaisesRegex(ValueError, "ambiguous_artifact_filename"):
            subject.content_files(self.report)
        (self.report / "images" / "fig001.jpg").unlink()
        (self.report / "source_figure_map.json").write_text(json.dumps({"assets": [
            {"path": "assets/fig001.jpg", "ref": "images/hash.jpg", "sha256": "0" * 64}]}))
        with self.assertRaisesRegex(ValueError, "image_binding_mismatch"):
            subject.content_files(self.report)

    def test_english_pdf_is_explicitly_bound_and_metadata_keeps_its_language(self):
        (self.report / "translated_en.md").write_text("English translated text")
        name = "portal_translated_report_en_01.pdf"
        (self.report / name).write_bytes(b"%PDF-1.7\nsynthetic PDF\n%%EOF\n")
        (self.report / "translation_status_en.json").write_text(json.dumps({
            "source_title": "Energy outlook", "target_language": "en", "translated_markdown": "translated_en.md", "pdf": name,
            "translation_notice": {"provider_session": "SECRET"}, "untranslated_unit_count": {"secret": "SECRET"},
        }))
        self.publish()
        rows = self.manifest()["artifacts"]
        self.assertEqual(next(row for row in rows if row["filename"] == name)["language"], "en")
        metadata = next(row for row in rows if row["filename"] == "translation-metadata.json")
        value = json.loads(self.client.rows[metadata["object_key"]][0])
        self.assertEqual(value["translation_language"], "en")
        self.assertEqual(value["translation_languages"], ["en"])
        self.assertNotIn("SECRET", json.dumps(value))

    def test_pdf_without_status_binding_or_complete_header_trailer_is_not_published(self):
        name = "portal_translated_report_01.pdf"
        (self.report / name).write_bytes(b"%PDF-1.7\ntruncated")
        self.assertFalse(any(row[1] == "pdf" for row in subject.content_files(self.report)))
        (self.report / "translated.md").write_text("Chinese translation fixture")
        (self.report / "translation_status.json").write_text(json.dumps({"pdf": name}))
        with self.assertRaisesRegex(ValueError, "invalid_translation_pdf"):
            subject.content_files(self.report)
        (self.report / "translation_status.json").write_text(json.dumps({"pdf": "../private.pdf"}))
        with self.assertRaisesRegex(ValueError, "invalid_translation_pdf_binding"):
            subject.content_files(self.report)

    def test_cas_readback_requires_expected_hash_and_metadata_not_merely_an_object(self):
        def replace_manifest(key):
            if key.endswith("manifest.json"):
                value = json.loads(self.client.rows[key][0])
                value["artifacts"][0]["sha256"] = "0" * 64
                self.client.rows[key] = (subject.encoded(value), '"replaced"')
        self.client.after_put = replace_manifest
        with self.assertRaisesRegex(ValueError, "publish_readback_failed"):
            self.publish()
        self.assertNotIn(f"{subject.PREFIX}/index.json", self.client.rows)

    def test_cas_readback_accepts_concurrent_addition_but_not_removal(self):
        def append_manifest(key):
            if key.endswith("manifest.json"):
                value = json.loads(self.client.rows[key][0])
                extra = dict(value["artifacts"][0], id="f" * 64, filename="concurrent.md")
                value["artifacts"].append(extra)
                self.client.rows[key] = (subject.encoded(value), '"concurrent"')
        self.client.after_put = append_manifest
        self.publish()
        self.assertEqual(len(self.manifest()["artifacts"]), 3)
        self.client.after_put = lambda _key: None
        expected = self.manifest()
        removed = dict(expected, artifacts=expected["artifacts"][:-1])
        with self.assertRaisesRegex(ValueError, "publish_readback_failed"):
            subject.verify_collection(expected, removed, "artifacts")

    def test_blob_readback_requires_declared_mime_and_digest_metadata_before_manifest(self):
        def alter_header(key):
            if "/blobs/" in key:
                self.client.headers[key]["ContentType"] = "application/octet-stream"
        self.client.after_put = alter_header
        with self.assertRaisesRegex(ValueError, "artifact_readback_failed"):
            self.publish()
        self.assertFalse(any(key.endswith("manifest.json") for key in self.client.rows))


def tar_bytes(entries):
    output = io.BytesIO()
    with tarfile.open(fileobj=output, mode="w:gz") as archive:
        for entry in entries:
            if isinstance(entry, tuple):
                name, body = entry
                info = tarfile.TarInfo(name)
                info.size = len(body)
                archive.addfile(info, io.BytesIO(body))
            else:
                archive.addfile(entry)
    return output.getvalue()


class ArchiveTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.client = MemoryR2()
        self.key = "_private-workflow-handoff/xhs/123/261012/shard_0.tar.gz"

    def seed(self, raw):
        self.client.put_object(Bucket="bucket", Key=self.key, Body=raw, Metadata={"sha256": subject.digest(raw)})

    def extract(self, entries):
        self.seed(tar_bytes(entries))
        return subject.download_bounded(self.client, "bucket", self.key, self.root / "source")

    def test_normal_handoff_is_checked_and_published_offline(self):
        self.seed(tar_bytes([("report/source_mineru.md", b"# Synthetic report\nText."),
                             ("report/status.json", b'{"source_pdf":"/private/Synthetic report.pdf"}')]))
        result = subject.publish_run(self.client, "bucket", "123", [], "2026-10-12")
        self.assertEqual(result, {"handoffs": 1, "unique_reports": 1, "report_publications": 1, "artifact_publications": 2})
        self.assertTrue(any(key.endswith("manifest.json") for key in self.client.rows))

    def test_archive_path_traversal_duplicate_links_sparse_and_special_members_are_rejected(self):
        candidates = [[("../outside", b"private")], [("/outside", b"private")], [("folder\\outside", b"private")],
                      [("same", b"1"), ("./same", b"2")]]
        for kind in (tarfile.SYMTYPE, tarfile.LNKTYPE, tarfile.CHRTYPE, tarfile.FIFOTYPE, tarfile.GNUTYPE_SPARSE):
            info = tarfile.TarInfo("bad"); info.type = kind; info.linkname = "../outside"
            candidates.append([info])
        for entries in candidates:
            with self.subTest(entries=repr(entries)[:80]):
                with self.assertRaises((ValueError, tarfile.TarError)):
                    self.extract(entries)
                self.assertFalse((self.root / "source").exists())
                self.assertFalse((self.root / "outside").exists())

    def test_inflated_total_member_size_and_member_count_are_independently_bounded(self):
        for field, value, entries in [("MAX_EXTRACTED", 1024, [("large", b"0" * 2048)]),
                                      ("MAX_MEMBER", 10, [("large", b"0" * 11)]),
                                      ("MAX_MEMBERS", 1, [("one", b"1"), ("two", b"2")])]:
            with self.subTest(field=field), patch.object(subject, field, value):
                with self.assertRaises(ValueError):
                    self.extract(entries)
                self.assertFalse((self.root / "source").exists())

    def test_extended_header_bound_precedes_tar_metadata_allocation(self):
        header = tarfile.TarInfo("pax"); header.type = tarfile.XHDTYPE; header.size = 64 * 1024 + 1
        self.seed(gzip.compress(header.tobuf() + b"\0" * 1024))
        with self.assertRaisesRegex(ValueError, "invalid_handoff_member"):
            subject.download_bounded(self.client, "bucket", self.key, self.root / "source")
        self.assertFalse((self.root / "source").exists())

    def test_checksum_size_and_decompressed_trailing_crc_are_verified(self):
        raw = tar_bytes([("valid", b"content")])
        for change in ({"Metadata": {}}, {"Metadata": {"sha256": "0" * 64}}, {"ContentLength": len(raw) - 1},
                       {"ContentLength": subject.MAX_COMPRESSED + 1}):
            self.seed(raw); self.client.headers[self.key].update(change)
            with self.subTest(change=change), self.assertRaises(ValueError):
                subject.download_bounded(self.client, "bucket", self.key, self.root / "source")
            self.assertFalse((self.root / "source").exists())
        damaged = bytearray(raw); damaged[-8] ^= 1
        self.seed(bytes(damaged))
        with self.assertRaises((OSError, ValueError, tarfile.TarError)):
            subject.download_bounded(self.client, "bucket", self.key, self.root / "source")
        self.assertFalse((self.root / "source").exists())

    def test_compressed_actual_bytes_are_bounded_even_when_inventory_understates_size(self):
        raw = tar_bytes([("valid", b"content")]); self.seed(raw)
        with patch.object(subject, "MAX_COMPRESSED", len(raw) - 1), self.assertRaises(ValueError):
            subject.download_bounded(self.client, "bucket", self.key, self.root / "source")
        self.assertFalse((self.root / "source").exists())

    def test_source_and_translation_handoffs_count_one_unique_report(self):
        self.seed(tar_bytes([("report/source_mineru.md", b"# Synthetic report\nText.")]))
        key = self.key.replace("shard_0", "translated_0")
        raw = tar_bytes([("report/translated.md", b"Translated text."),
                         ("report/translation_status.json", b'{"source_title":"Synthetic report"}')])
        self.client.put_object(Bucket="bucket", Key=key, Body=raw, Metadata={"sha256": subject.digest(raw)})
        result = subject.publish_run(self.client, "bucket", "123", [])
        self.assertEqual(result, {"handoffs": 2, "unique_reports": 1, "report_publications": 2, "artifact_publications": 4})

    def test_current_catalog_validation_rejects_empty_or_invalid_id_inventory(self):
        path = self.root / "catalog.json"
        for value in ({}, {"items": []}, {"items": [{"id": "../private"}]}, {"items": [{"id": "a" * 24}] * 2}):
            path.write_text(json.dumps(value))
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, "invalid_current_catalog"):
                subject.load_catalog(path)
        path.write_text(json.dumps({"items": [{"id": "a" * 24, "title": "Synthetic"}]}))
        self.assertEqual(subject.load_catalog(path)[0]["title"], "Synthetic")

    def test_workflow_fetches_current_catalog_before_secret_publication_and_binds_workflow_identity(self):
        workflow = (Path(__file__).resolve().parents[1] / ".github/workflows/customer-content-publish.yml").read_text()
        self.assertIn("github.ref == 'refs/heads/main'", workflow)
        self.assertIn(".github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml", workflow)
        self.assertIn("Number.isSafeInteger(Number(runId))", workflow)
        self.assertIn("--max-time 180 --max-total-time 420", workflow)
        self.assertIn('--catalog "$RUNNER_TEMP/customer-current-catalog.json"', workflow)
        self.assertIn("load_catalog(Path(sys.argv[1]))", workflow)
        self.assertLess(workflow.index("Fetch and validate current public report catalog"), workflow.index("R2_SECRET_ACCESS_KEY:"))


if __name__ == "__main__":
    unittest.main()
