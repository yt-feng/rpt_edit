#!/usr/bin/env python3
"""Prove catalog-only updates retain published translations without inference."""
import base64
import copy
import hashlib
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import publish_static_slot as publisher
import retain_published_core_locales as retention
from test_audit_portal_shadow_preview import manifest_fixture
from test_publish_static_slot import FakeR2, write

ORIGIN = "https://portal.example.invalid"


def html(path: str, *, locale: str = "zh-Hans", content: str = "old content", noindex: bool = False) -> str:
    canonical = ORIGIN + "/" + (path[:-10] if path.endswith("index.html") else path)
    alternates = "" if locale != "zh-Hans" else (
        f'<link rel="alternate" hreflang="zh-Hans" href="{canonical}">'
        f'<link rel="alternate" hreflang="x-default" href="{canonical}">')
    return (f'<html lang="{locale}"><head><link rel="canonical" href="{canonical}">{alternates}'
            + ('<meta name="robots" content="noindex,follow">' if noindex else "")
            + f'</head><body>{content}</body></html>')


class RetentionTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.folder = Path(temporary.name)
        self.old, self.root = self.folder / "old", self.folder / "fresh"
        self.old.mkdir()
        self.root.mkdir()
        self.locale, bodies = manifest_fixture()
        self.locale.update(html_page_count=2, translation_scope="incremental",
                           index_policy={"mode": "incremental-publication-cutoff", "index_start_date": "2026-10-01",
                                         "default": "new-content-and-core-hubs", "allowlist_count": 0,
                                         "history_release_count": 0, "translation_mode": "new-content-only"})
        for path, body in bodies.items():
            target = self.old / path.lstrip("/")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(body)
        for locale in retention.LOCALES:
            write(self.old / locale / "index.html", html(locale + "/index.html", locale=locale))
            write(self.old / locale / "reports/old.html", html(locale + "/reports/old.html", locale=locale))
            write(self.old / locale / "assets/newsfeed-app.js", f"export const lang='{locale}';")
            write(self.old / f"sitemap-{locale}.xml", "<urlset/>")
        for path in retention.SHARED_ASSETS:
            write(self.old / path, "published " + path)
        write(self.old / "assets/newsfeed-app.js", "export const value='old';")
        self.locale["lazy_javascript_assets"] = {"zh-Hans": {
            "path": "assets/newsfeed-app.js", "byte_size": (self.old / "assets/newsfeed-app.js").stat().st_size,
            "sha256": hashlib.sha256((self.old / "assets/newsfeed-app.js").read_bytes()).hexdigest()}}
        write(self.old / retention.MANIFEST, json.dumps(self.locale))
        write(self.old / "data/catalog.json", '{"old":true}')
        write(self.old / "en/index.html", "English is handled by its existing publisher")
        self.client = FakeR2()
        paths, files, tree, total = publisher.build_inventory(self.old)
        self.state = {"schema_version": 1, "slot": "a", "release_id": "a" * 32, "tree_sha256": tree}
        self.manifest = {**self.state, "file_count": len(files), "files": files, "total_bytes": total}
        for relative, path in paths.items():
            self.client.upload_file(str(path), "bucket", publisher.slot_prefix("a") + relative,
                                    ExtraArgs=publisher.upload_extra_args(files[relative]))
        publisher.put_json(self.client, "bucket", "edge-static/slot-manifests/a.json", self.manifest)
        self.client.operations.clear()
        write(self.root / "index.html", html("index.html", content="fresh homepage"))
        write(self.root / "reports/old.html", html("reports/old.html", content="fresh old report"))
        write(self.root / "reports/new.html", html("reports/new.html", content="brand new report"))
        write(self.root / "assets/newsfeed-app.js", "export const value='new Chinese module';")
        write(self.root / "data/catalog.json", '{"old":true,"new":true}')
        write(self.root / "sitemap.xml", '<sitemapindex><sitemap><loc>' + ORIGIN + '/sitemap-pages.xml</loc></sitemap></sitemapindex>')
        write(self.root / "robots.txt", "User-agent: *\nAllow: /\n")
        self.active_path = self.folder / "active.json"
        self.active_path.write_text(json.dumps(self.manifest))
        self.receipt_path = self.folder / "receipt.json"

    def run_retention(self):
        receipt = retention.retain(client=self.client, bucket="bucket", active_state=self.state,
                                   active_manifest=self.manifest, root=self.root, site_url=ORIGIN)
        self.receipt_path.write_text(json.dumps(receipt))
        return receipt

    def test_catalog_changes_preserve_all_old_translations_without_remote_writes(self):
        chinese = (self.root / "data/catalog.json").read_bytes()
        new_page = (self.root / "reports/new.html").read_bytes()
        receipt = self.run_retention()
        self.assertEqual(receipt["provider_requests"], 0)
        self.assertEqual((self.root / "data/catalog.json").read_bytes(), chinese)
        self.assertEqual((self.root / "reports/new.html").read_bytes(), new_page)
        for path in retention.selected_paths(self.manifest["files"]) - {retention.MANIFEST}:
            self.assertEqual((self.root / path).read_bytes(), (self.old / path).read_bytes(), path)
        self.assertFalse((self.root / "en").exists())
        self.assertIn('hreflang="ko"', (self.root / "index.html").read_text())
        self.assertNotIn('hreflang="ko"', new_page.decode())
        result = retention.validate_retention(self.root, self.receipt_path, self.active_path)
        self.assertEqual(result["translation_scope"], "incremental")
        self.assertEqual(set(op for op, _ in self.client.operations), {"get", "head"})

    def test_only_current_chinese_lazy_asset_binding_changes(self):
        self.run_retention()
        actual = json.loads((self.root / retention.MANIFEST).read_bytes())
        expected = copy.deepcopy(self.locale)
        actual_lazy = actual["lazy_javascript_assets"].pop("zh-Hans")
        expected["lazy_javascript_assets"].pop("zh-Hans")
        self.assertEqual(actual, expected)
        self.assertEqual(actual_lazy["sha256"], hashlib.sha256((self.root / "assets/newsfeed-app.js").read_bytes()).hexdigest())

    def test_sharded_source_fallback_provenance_survives_retention_and_revalidation(self):
        import portal_locale_manifest as codec
        from test_verify_portal_locale_manifest_bundle import sharded_fixture

        self.locale, shards = sharded_fixture(self.locale)
        source_body = codec._json_bytes(self.locale)
        (self.old / retention.MANIFEST).write_bytes(source_body)
        for relative, body in shards.items():
            target = self.old / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(body)
        paths, files, tree, total = publisher.build_inventory(self.old)
        self.state["tree_sha256"] = tree
        self.manifest = {**self.state, "file_count": len(files), "files": files, "total_bytes": total}
        for relative, path in paths.items():
            self.client.upload_file(str(path), "bucket", publisher.slot_prefix("a") + relative,
                                    ExtraArgs=publisher.upload_extra_args(files[relative]))
        publisher.put_json(self.client, "bucket", publisher.manifest_key("a"), self.manifest)
        self.active_path.write_text(json.dumps(self.manifest))
        self.client.operations.clear()

        original = codec.load_locale_manifest(self.old / retention.MANIFEST)
        receipt = self.run_retention()
        result = retention.validate_retention(self.root, self.receipt_path, self.active_path)
        self.assertEqual(result["retained_files"], len(retention.selected_paths(files)))
        self.assertEqual(base64.b64decode(receipt["source_manifest_b64"], validate=True), source_body)
        retained = codec.load_locale_manifest(self.root / retention.MANIFEST)
        self.assertEqual(retained["source_fallbacks"]["schema_version"], 5)
        self.assertEqual(retained["source_fallbacks"], original["source_fallbacks"])
        expected = copy.deepcopy(self.locale)
        expected["lazy_javascript_assets"]["zh-Hans"] = retained["lazy_javascript_assets"]["zh-Hans"]
        self.assertEqual(retained, expected)
        codec.validate_translation_resolution(retained, retention.LOCALES)
        self.assertEqual(retained._verified_counts, original._verified_counts)
        self.assertEqual(retained._verified_fingerprint, hashlib.sha256(codec._json_bytes(retained)).digest())
        # The fresh Chinese binding changes root metadata and therefore must
        # receive its own verified fingerprint after reading all bound shards.
        self.assertNotEqual(retained._verified_fingerprint, original._verified_fingerprint)
        for relative, body in shards.items():
            self.assertEqual((self.root / relative).read_bytes(), body)
            self.assertEqual(self.client.operations.count(("get", publisher.slot_prefix("a") + relative)), 1)
        self.assertEqual(set(operation for operation, _key in self.client.operations), {"get", "head"})

        with self.assertRaisesRegex(codec.LocaleManifestError, "shards have not been verified"):
            codec.validate_translation_resolution(dict(retained), retention.LOCALES)
        retained["coverage"]["ko"] = 1.0
        with self.assertRaisesRegex(codec.LocaleManifestError, "root metadata changed"):
            codec.validate_translation_resolution(retained, retention.LOCALES)
        relative, body = next(iter(shards.items()))
        (self.root / relative).write_bytes(b"x" * len(body))
        with self.assertRaisesRegex(retention.RetentionError, "published file changed"):
            retention.validate_retention(self.root, self.receipt_path, self.active_path)

    def test_retention_proof_bounds_fit_recovery_without_expanding_embedded_source(self):
        import resume_portal_locale_candidate as resume
        self.assertEqual(resume.DIAGNOSTIC_MAX_BYTES["locale-retention.json"], retention.MAX_RECEIPT_BYTES)
        self.assertEqual(resume.DIAGNOSTIC_MAX_BYTES["locale-retention-active-manifest.json"],
                         retention.MAX_COMMITTED_MANIFEST_BYTES)
        # Base64 contains only the bounded wire root, not expanded shard rows
        # or an earlier receipt. Leave room for the fixed identity/count fields.
        encoded_root_limit = 4 * ((retention.MAX_LOCALE_MANIFEST_BYTES + 2) // 3)
        self.assertLess(encoded_root_limit + 1024 * 1024, retention.MAX_RECEIPT_BYTES)
        self.assertLessEqual(sum(resume.DIAGNOSTIC_MAX_BYTES[name] for name in resume.RETENTION_DIAGNOSTICS),
                             resume.MAX_DIAGNOSTICS_EXPANDED_BYTES)

    def test_corrupt_remote_file_never_promotes_a_partial_locale_tree(self):
        self.client.objects[publisher.slot_prefix("a") + "ko/index.html"]["body"] = b"corrupt"
        with self.assertRaisesRegex(RuntimeError, "differs from manifest"):
            self.run_retention()
        self.assertFalse((self.root / "ko").exists())
        self.assertFalse((self.root / retention.MANIFEST).exists())

    def test_remote_release_change_before_completion_prevents_promotion(self):
        changed = {**self.manifest, "release_id": "b" * 32}
        with patch.object(retention, "read_json_object", return_value=changed), self.assertRaises(retention.RetentionError):
            self.run_retention()
        self.assertFalse((self.root / "ko").exists())

    def test_forged_tree_stops_before_download(self):
        self.manifest["files"]["ko/index.html"]["sha256"] = "f" * 64
        with self.assertRaisesRegex(retention.RetentionError, "tree is invalid"):
            self.run_retention()
        self.assertEqual(self.client.operations, [])

    def test_modified_or_extra_published_translation_is_rejected_before_upload(self):
        self.run_retention()
        write(self.root / "ko/index.html", "changed")
        with self.assertRaisesRegex(retention.RetentionError, "published file changed"):
            retention.validate_retention(self.root, self.receipt_path, self.active_path)
        write(self.root / "ko/extra.html", "unverified")
        with self.assertRaisesRegex(retention.RetentionError, "inventory changed"):
            retention.validate_retention(self.root, self.receipt_path, self.active_path)

    def test_manifest_coverage_cannot_be_relabelled_as_new_translation(self):
        self.run_retention()
        changed = json.loads((self.root / retention.MANIFEST).read_bytes())
        changed["html_page_count"] += 1
        (self.root / retention.MANIFEST).write_text(json.dumps(changed))
        with self.assertRaisesRegex(retention.RetentionError, "metadata changed"):
            retention.validate_retention(self.root, self.receipt_path, self.active_path)

    def test_receipt_source_manifest_must_match_active_bytes(self):
        receipt = self.run_retention()
        receipt["source_manifest_b64"] = base64.b64encode(b"{}").decode()
        self.receipt_path.write_text(json.dumps(receipt))
        with self.assertRaisesRegex(retention.RetentionError, "proof differs"):
            retention.validate_retention(self.root, self.receipt_path, self.active_path)

    def test_noindex_translation_is_not_advertised_from_chinese(self):
        # Build a correctly committed old noindex variant, not a corrupt object.
        path = "ar/index.html"
        body = html(path, locale="ar", noindex=True).encode()
        self.client.objects[publisher.slot_prefix("a") + path]["body"] = body
        self.manifest["files"][path].update(size=len(body), sha256=hashlib.sha256(body).hexdigest())
        tree = retention.static_tree_sha256(self.manifest["files"])
        self.manifest["tree_sha256"] = self.state["tree_sha256"] = tree
        publisher.put_json(self.client, "bucket", "edge-static/slot-manifests/a.json", self.manifest)
        self.run_retention()
        self.assertNotIn('hreflang="ko"', (self.root / "index.html").read_text())

    def test_locale_followup_uses_newly_published_chinese_instead_of_queued_old_source(self):
        import restore_published_chinese_source as source
        self.run_retention()
        write(self.root / "assets/app.js", "current Chinese application")
        paths, files, tree, total = publisher.build_inventory(self.root)
        current_state = {"schema_version": 1, "slot": "b", "release_id": "b" * 32, "tree_sha256": tree}
        current_manifest = {**current_state, "file_count": len(files), "files": files, "total_bytes": total}
        for relative, path in paths.items():
            self.client.upload_file(str(path), "bucket", publisher.slot_prefix("b") + relative,
                                    ExtraArgs=publisher.upload_extra_args(files[relative]))
        publisher.put_json(self.client, "bucket", "edge-static/slot-manifests/b.json", current_manifest)
        before = Path.cwd()
        try:
            os.chdir(self.folder)
            restored = self.folder / "_neutral_site"
            receipt = source.restore(client=self.client, bucket="bucket", active_state=current_state,
                                     active_manifest=current_manifest, root=restored, site_url=ORIGIN)
        finally:
            os.chdir(before)
        self.assertEqual(receipt["source_state"], current_state)
        self.assertEqual((restored / "data/catalog.json").read_bytes(), (self.root / "data/catalog.json").read_bytes())
        self.assertEqual((restored / "reports/new.html").read_bytes(), (self.root / "reports/new.html").read_bytes())
        self.assertEqual((restored / "assets/app.js").read_text(), "current Chinese application")
        self.assertNotEqual((restored / "data/catalog.json").read_bytes(), (self.old / "data/catalog.json").read_bytes())
        self.assertNotIn('hreflang="ko"', (restored / "index.html").read_text())


if __name__ == "__main__":
    unittest.main()
