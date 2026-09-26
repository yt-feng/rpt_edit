#!/usr/bin/env python3
"""Offline checks for the read-only final candidate identity guard."""

from __future__ import annotations

import copy
import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import publish_static_slot as publisher
import verify_prepared_static_slot as guard
from test_publish_static_slot import FakeR2, release, write
from test_verify_portal_locale_routes import ORIGIN, describe, fixture as locale_fixture


class PreparedStaticSlotTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.client = FakeR2()
        self.slot = "b"
        self.release = release(17)

    def prepare(self, *, multilingual: bool = True, omit: str = "", extra_files: dict | None = None) -> dict:
        paths = set(guard.REQUIRED_STATIC_PATHS) | set(publisher.DEFAULT_RUNTIME_PATHS)
        if multilingual:
            paths.update(guard.REQUIRED_LOCALE_PATHS)
        # Path sorting differs from string sorting for these two siblings.
        paths.update(("alpha.txt", "alpha/z.txt"))
        for relative in sorted(paths - {omit}):
            write(self.root / relative, "fixture: " + relative)
        for relative, body in (extra_files or {}).items():
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(body)
        paths_by_relative, files, tree, total = publisher.build_inventory(self.root)
        for relative, path in paths_by_relative.items():
            self.client.upload_file(
                str(path), "bucket", publisher.slot_prefix(self.slot) + relative,
                ExtraArgs=publisher.upload_extra_args(files[relative]),
            )
        _runtime_paths, runtime_files, runtime_tree = publisher.runtime_inventory(self.root)
        runtime = {
            "schema_version": publisher.RUNTIME_SCHEMA_VERSION,
            "release_id": self.release,
            "prefix": publisher.runtime_release_prefix(self.release),
            "tree_sha256": runtime_tree,
            "file_count": len(runtime_files),
            "files": runtime_files,
        }
        for filename, descriptor in runtime_files.items():
            self.client.put_object(
                Bucket="bucket", Key=runtime["prefix"] + filename,
                Body=(self.root / "data" / filename).read_bytes(),
                Metadata={"sha256": descriptor["sha256"], "release-id": self.release},
                ContentType=descriptor["content_type"], CacheControl=descriptor["cache_control"],
            )
        publisher.put_json(self.client, "bucket", publisher.runtime_manifest_key(self.release), runtime)
        self.manifest = {
            "schema_version": publisher.SCHEMA_VERSION,
            "slot": self.slot,
            "release_id": self.release,
            "tree_sha256": tree,
            "file_count": len(files),
            "total_bytes": total,
            "files": files,
            "runtime_data": {key: runtime[key] for key in ("schema_version", "release_id", "prefix", "tree_sha256")},
        }
        publisher.put_json(self.client, "bucket", publisher.manifest_key(self.slot), self.manifest)
        self.client.operations.clear()
        return self.manifest

    def verify(self, **overrides):
        return guard.verify_prepared_static_slot(
            self.client, "bucket", **{
                "slot": self.slot, "release": self.release, "tree": self.manifest["tree_sha256"],
                **overrides,
            },
        )

    def replace_manifest(self, changes: dict) -> None:
        payload = {**self.manifest, **changes}
        publisher.put_json(self.client, "bucket", publisher.manifest_key(self.slot), payload)

    def locale_files(self) -> tuple[dict, dict]:
        manifest, responses = locale_fixture()
        manifest["coverage"] = dict.fromkeys(guard.locale_routes.LOCALES, 1.0)
        manifest["lazy_javascript_assets"] = {}
        for locale, prefix in [("zh-Hans", ""), *((locale, f"{locale}/") for locale in guard.locale_routes.LOCALES)]:
            path = prefix + "assets/newsfeed-app.js"
            body = f"export function initNewsfeedApp() {{ /* {locale} */ }}".encode()
            manifest["lazy_javascript_assets"][locale] = describe(path, body)
            responses[ORIGIN + "/" + path] = (200, {}, body)
        path = guard.locale_routes.DETAIL_PATH
        body = b"/* detail recovery module */"
        manifest["detail_asset"] = describe(path, body)
        responses[ORIGIN + "/" + path] = (200, {}, body)
        files = {url.removeprefix(ORIGIN + "/"): response[2] for url, response in responses.items()}
        return manifest, files

    def prepare_locales(self, manifest: dict, files: dict) -> None:
        self.prepare(extra_files={**files, "data/i18n/manifest.json": json.dumps(manifest, ensure_ascii=False).encode()})

    def test_declared_locale_shells_and_assets_use_only_committed_r2_objects(self) -> None:
        manifest, files = self.locale_files()
        self.prepare_locales(manifest, files)
        with patch("verify_portal_locale_routes.release_fetch.subprocess.run", side_effect=AssertionError("No live HTTP allowed")):
            result = self.verify(locale_origin=ORIGIN)
        self.assertEqual(result["locale_routes_status"], "passed")
        self.assertEqual(result["locale_objects_verified"], 24)
        self.assertTrue(all(operation in {"head", "get"} for operation, _key in self.client.operations))
        for path in files:
            self.assertIn(("get", publisher.slot_prefix(self.slot) + path), self.client.operations)

    def test_three_megabyte_source_fallback_manifest_passes_the_same_route_contract(self) -> None:
        manifest, files = self.locale_files()
        rows = {}
        for index in range(2000):
            source = f"Report {index}: " + "original source text " * 18
            key = hashlib.sha256(f"portal-public-locales-v4\0copy\0{source}".encode()).hexdigest()
            rows[key] = {"source": source, "source_sha256": hashlib.sha256(source.encode()).hexdigest(),
                         "context": "html:text:p", "translation_class": "copy", "reason": "translation_time_budget"}
        locales = guard.locale_routes.LOCALES
        manifest.update(prompt_version="portal-public-locales-v4", source_unit_count=len(rows),
                        coverage=dict.fromkeys(locales, 0), translation_entry_count=dict.fromkeys(locales, 0),
                        resolved_entry_count=dict.fromkeys(locales, len(rows)), resolved_coverage=dict.fromkeys(locales, 1.0),
                        source_fallbacks={"schema_version": 1, "counts": dict.fromkeys(locales, len(rows)),
                                          "units": {locale: rows for locale in locales}})
        self.assertGreater(len(json.dumps(manifest).encode()), 3 * 1024 * 1024)
        self.prepare_locales(manifest, files)
        self.assertEqual(self.verify(locale_origin=ORIGIN)["locale_objects_verified"], 24)

    def test_oversized_locale_manifest_is_rejected_before_its_r2_body_is_read(self) -> None:
        manifest, files = self.locale_files()
        self.prepare_locales(manifest, files)
        descriptor = self.manifest["files"]["data/i18n/manifest.json"]
        descriptor["size"] = guard.MAX_LOCALE_MANIFEST_BYTES + 1
        self.manifest["tree_sha256"] = guard.static_tree_sha256(self.manifest["files"])
        self.manifest["total_bytes"] = sum(row["size"] for row in self.manifest["files"].values())
        self.replace_manifest({})
        self.client.operations.clear()
        with self.assertRaisesRegex(RuntimeError, "byte size exceeds its bound"):
            self.verify(locale_origin=ORIGIN)
        self.assertNotIn(("get", publisher.slot_prefix(self.slot) + "data/i18n/manifest.json"), self.client.operations)

    def test_semantically_wrong_shell_fails_even_when_all_committed_hashes_match(self) -> None:
        manifest, files = self.locale_files()
        path = "ja/report.html"
        files[path] = files[path].replace(b'data-page="report"', b'data-page="404"')
        manifest["application_routes"]["ja"]["report.html"] = describe(path, files[path])
        self.prepare_locales(manifest, files)
        with self.assertRaisesRegex(RuntimeError, "wrong page identity"):
            self.verify(locale_origin=ORIGIN)

    def test_locale_descriptor_must_match_the_committed_slot_before_reading_routes(self) -> None:
        manifest, files = self.locale_files()
        manifest["application_routes"]["ja"]["report.html"]["sha256"] = "0" * 64
        self.prepare_locales(manifest, files)
        with self.assertRaisesRegex(RuntimeError, "descriptor differs from the committed"):
            self.verify(locale_origin=ORIGIN)
        self.assertNotIn(("get", publisher.slot_prefix(self.slot) + "ja/report.html"), self.client.operations)

    def test_arbitrary_route_url_cannot_escape_the_slot(self) -> None:
        manifest, files = self.locale_files()
        manifest["application_routes"]["ja"]["report.html"]["path"] = "https://other.invalid/report.html"
        self.prepare_locales(manifest, files)
        with self.assertRaises(guard.locale_routes.RouteVerificationError):
            self.verify(locale_origin=ORIGIN)
        self.assertFalse(any("other.invalid" in key for _operation, key in self.client.operations))

    def test_r2_streams_close_on_success_and_oversized_route_failure(self) -> None:
        manifest, files = self.locale_files()
        self.prepare_locales(manifest, files)
        original_get = self.client.get_object
        streams = []
        corrupt = False

        def tracked_get(*, Bucket, Key):
            response = original_get(Bucket=Bucket, Key=Key)
            if corrupt and Key.endswith("/ja/report.html"):
                response["Body"].close()
                response["Body"] = io.BytesIO(files["ja/report.html"] + b"x")
            streams.append(response["Body"])
            return response

        self.client.get_object = tracked_get
        self.verify(locale_origin=ORIGIN)
        self.assertTrue(streams and all(stream.closed for stream in streams))
        streams.clear()
        corrupt = True
        with self.assertRaisesRegex(RuntimeError, "byte size bound"):
            self.verify(locale_origin=ORIGIN)
        self.assertTrue(streams and all(stream.closed for stream in streams))

    def test_locale_origin_requires_a_locale_manifest_and_valid_origin(self) -> None:
        self.prepare(multilingual=False)
        with self.assertRaisesRegex(RuntimeError, "locale manifest is required"):
            self.verify(locale_origin=ORIGIN)
        self.client.operations.clear()
        with self.assertRaises(guard.locale_routes.RouteVerificationError):
            self.verify(locale_origin="https://other.invalid/ar/")
        self.assertEqual(self.client.operations, [])

    def test_cli_locale_origin_enables_the_r2_route_gate(self) -> None:
        manifest, files = self.locale_files()
        self.prepare_locales(manifest, files)
        argv = ["verify_prepared_static_slot.py", "--slot", self.slot, "--release", self.release,
                "--tree", self.manifest["tree_sha256"], "--locale-origin", ORIGIN]
        output = io.StringIO()
        with patch("sys.argv", argv), patch.object(guard, "build_r2_client", return_value=(self.client, None)), \
                patch.object(guard, "require_env", return_value="bucket"), patch("sys.stdout", output):
            self.assertEqual(guard.main(), 0)
        self.assertEqual(json.loads(output.getvalue())["locale_objects_verified"], 24)

    def test_multilingual_candidate_passes_without_writes_or_full_inventory_reads(self) -> None:
        manifest = self.prepare()
        result = self.verify()
        self.assertTrue(result["verified"])
        self.assertEqual(result["static_objects_verified"], len(guard.REQUIRED_STATIC_PATHS) + len(guard.REQUIRED_LOCALE_PATHS))
        self.assertEqual(result["runtime_objects_verified"], 3)
        self.assertEqual(guard.static_tree_sha256(manifest["files"]), manifest["tree_sha256"])
        self.assertNotEqual(publisher.runtime_tree_sha256(manifest["files"]), manifest["tree_sha256"])
        self.assertTrue(all(operation in {"head", "get"} for operation, _key in self.client.operations))
        self.assertFalse(any(key.endswith("alpha/z.txt") for _operation, key in self.client.operations))

    def test_plain_chinese_candidate_does_not_require_locale_objects(self) -> None:
        self.prepare(multilingual=False)
        result = self.verify()
        self.assertTrue(result["verified"])
        self.assertEqual(result["static_objects_verified"], len(guard.REQUIRED_STATIC_PATHS))

    def test_multilingual_manifest_requires_all_three_locale_homes(self) -> None:
        self.prepare(omit="ar/index.html")
        with self.assertRaisesRegex(RuntimeError, "required object: ar/index.html"):
            self.verify()

    def test_requested_identity_cannot_follow_a_reused_slot(self) -> None:
        self.prepare()
        self.replace_manifest({"release_id": release(18)})
        with self.assertRaisesRegex(RuntimeError, "requested candidate"):
            self.verify()

    def test_manifest_tree_is_recomputed_instead_of_trusting_its_header(self) -> None:
        self.prepare()
        changed = copy.deepcopy(self.manifest["files"])
        changed["alpha.txt"]["sha256"] = "0" * 64
        self.replace_manifest({"files": changed})
        with self.assertRaisesRegex(RuntimeError, "file tree"):
            self.verify()

    def test_incomplete_marker_is_rejected_even_when_not_a_json_object(self) -> None:
        self.prepare()
        self.client.put_object(Bucket="bucket", Key=publisher.incomplete_key(self.slot), Body=b"[]")
        with self.assertRaisesRegex(RuntimeError, "incomplete publication marker"):
            self.verify()

    def test_same_length_corruption_is_rejected_even_with_unchanged_digest_metadata(self) -> None:
        self.prepare()
        key = publisher.slot_prefix(self.slot) + "index.html"
        self.client.objects[key]["body"] = b"x" * len(self.client.objects[key]["body"])
        with self.assertRaisesRegex(RuntimeError, "content differs"):
            self.verify()

    def test_wrong_metadata_is_rejected_even_with_correct_object_bytes(self) -> None:
        self.prepare()
        key = publisher.slot_prefix(self.slot) + "index.html"
        self.client.objects[key]["metadata"]["sha256"] = "0" * 64
        with self.assertRaisesRegex(RuntimeError, "metadata differs"):
            self.verify()

    def test_runtime_binding_and_release_metadata_are_both_checked(self) -> None:
        self.prepare()
        self.replace_manifest({"runtime_data": {**self.manifest["runtime_data"], "tree_sha256": "0" * 64}})
        with self.assertRaisesRegex(RuntimeError, "runtime manifest identities differ"):
            self.verify()
        self.replace_manifest({})
        key = publisher.runtime_release_prefix(self.release) + "catalog.json"
        self.client.objects[key]["metadata"]["release-id"] = release(18)
        with self.assertRaisesRegex(RuntimeError, "runtime metadata differs"):
            self.verify()

    def test_runtime_bytes_and_static_source_must_match(self) -> None:
        self.prepare()
        key = publisher.runtime_release_prefix(self.release) + "catalog.json"
        self.client.objects[key]["body"] = b"x" * len(self.client.objects[key]["body"])
        with self.assertRaisesRegex(RuntimeError, "content differs"):
            self.verify()

    def test_publication_started_during_checks_is_detected_before_return(self) -> None:
        self.prepare()
        get_object = self.client.get_object
        def begin_new_publication(*, Bucket, Key):
            if Key.endswith("/password_rules.json"):
                self.client.put_object(Bucket=Bucket, Key=publisher.incomplete_key(self.slot), Body=b"{}")
            return get_object(Bucket=Bucket, Key=Key)
        self.client.get_object = begin_new_publication
        with self.assertRaisesRegex(RuntimeError, "incomplete publication marker"):
            self.verify()

    def test_manifest_replaced_during_checks_is_detected_before_return(self) -> None:
        self.prepare()
        get_object = self.client.get_object
        def replace_on_runtime_read(*, Bucket, Key):
            if Key.endswith("/password_rules.json"):
                self.replace_manifest({"release_id": release(18)})
            return get_object(Bucket=Bucket, Key=Key)
        self.client.get_object = replace_on_runtime_read
        with self.assertRaisesRegex(RuntimeError, "requested candidate"):
            self.verify()

    def test_publication_started_during_final_manifest_read_is_detected(self) -> None:
        self.prepare()
        get_object = self.client.get_object
        reads = 0
        def begin_on_second_manifest_read(*, Bucket, Key):
            nonlocal reads
            if Key == publisher.manifest_key(self.slot):
                reads += 1
                if reads == 2:
                    self.client.put_object(Bucket=Bucket, Key=publisher.incomplete_key(self.slot), Body=b"{}")
            return get_object(Bucket=Bucket, Key=Key)
        self.client.get_object = begin_on_second_manifest_read
        with self.assertRaisesRegex(RuntimeError, "incomplete publication marker"):
            self.verify()


if __name__ == "__main__":
    unittest.main()
