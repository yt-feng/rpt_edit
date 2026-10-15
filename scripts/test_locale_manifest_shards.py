"""Bounded provenance partitions and complete release accounting, without networking."""

from __future__ import annotations

import base64
import copy
import hashlib
import json
import os
from pathlib import Path
import tempfile
import unittest
import weakref
import zlib
from unittest.mock import patch

import portal_locale_manifest as codec

LOCALES = ("ar", "ja", "ko")


def fixture(count=48, *, source_size=80):
    prompt = "portal-public-locales-v4"
    rows = {}
    for index in range(count):
        source = f"Source report {index}: " + ("Financial source text 25% remains exact. " * (source_size // 40 + 1))
        key = hashlib.sha256(f"{prompt}\0copy\0{source}".encode()).hexdigest()
        rows[key] = {"source": source, "source_sha256": hashlib.sha256(source.encode()).hexdigest(),
                     "context": "html:text:p", "reason": "translation_time_budget", "translation_class": "copy"}
    units = {locale: dict(rows) for locale in LOCALES}
    return {"schema_version": 1, "prompt_version": prompt, "source_unit_count": count + 2,
            "translation_entry_count": dict.fromkeys(LOCALES, 2),
            "resolved_entry_count": dict.fromkeys(LOCALES, count + 2),
            "coverage": dict.fromkeys(LOCALES, 2 / (count + 2)),
            "resolved_coverage": dict.fromkeys(LOCALES, 1.0),
            "source_fallbacks": {"schema_version": 1, "units": units, "counts": dict.fromkeys(LOCALES, count)},
            "required_paths": ["ko/index.html", "ja/index.html", "ar/index.html"],
            "index_policy": {"start_date": "2026-09-05", "scope": "incremental"}}


def encoded_bundle(manifest):
    bodies = {}
    root = codec._encode_locale_manifest_bundle(manifest, lambda descriptor, body: bodies.__setitem__(descriptor["path"], body))
    return json.loads(root), bodies


def replace_shard(root, bodies, index, shard):
    body = codec._json_bytes(shard)
    old = root["source_fallbacks"]["shards"][index]
    digest = hashlib.sha256(body).hexdigest()
    descriptor = dict(old, sha256=digest, byte_size=len(body),
                      path=f"{codec.FALLBACK_SHARD_DIRECTORY}/{old['prefix']}-{digest}.json")
    root["source_fallbacks"]["shards"][index] = descriptor
    bodies[descriptor["path"]] = body


class ShardTests(unittest.TestCase):
    def test_lossless_source_rows_and_metadata_with_small_root(self):
        original = fixture()
        root, bodies = encoded_bundle(original)
        seen = dict.fromkeys(LOCALES, 0)

        def resolve(descriptor):
            body = bodies[descriptor["path"]]
            decoded = codec._decode_fallback_shard(body, descriptor, original["prompt_version"], set(LOCALES))
            for locale in LOCALES:
                expected = {key: row for key, row in original["source_fallbacks"]["units"][locale].items()
                            if key.startswith(descriptor["prefix"])}
                self.assertEqual(decoded["units"][locale], expected)
                seen[locale] += len(expected)
            return body

        parsed = codec.parse_locale_manifest(codec._json_bytes(root), shard_resolver=resolve)
        codec.validate_translation_resolution(parsed, LOCALES)
        self.assertEqual(seen, original["source_fallbacks"]["counts"])
        self.assertEqual({key: value for key, value in parsed.items() if key != "source_fallbacks"},
                         {key: value for key, value in original.items() if key != "source_fallbacks"})
        self.assertNotIn("units", parsed["source_fallbacks"])
        self.assertLessEqual(len(bodies), 16)
        self.assertEqual(parsed["required_paths"], original["required_paths"])

    def test_small_empty_and_legacy_manifests_stay_readable(self):
        original = fixture(0)
        root, bodies = encoded_bundle(original)
        self.assertEqual(bodies, {})
        self.assertEqual(codec.parse_locale_manifest(codec._json_bytes(root)), original)
        for schema in (1, 2, 3, 4):
            from test_locale_manifest_compaction import CompactionTests
            tests = CompactionTests()
            source, packed = tests.packed()
            value = source if schema == 1 else json.loads(packed)
            if schema >= 3:
                value["source_fallbacks"] = codec._compress_fallback_records(value["source_fallbacks"], schema_version=schema)
            self.assertEqual(codec.parse_locale_manifest(codec._json_bytes(value)), source)

    def test_adaptive_split_preserves_original_per_leaf_limits(self):
        original = fixture(64)
        with patch.object(codec, "MAX_FALLBACK_REFERENCES", 6):
            root, bodies = encoded_bundle(original)
            self.assertGreater(len(bodies), 16)
            self.assertTrue(any(len(item["prefix"]) > 1 for item in root["source_fallbacks"]["shards"]))
            parsed = codec.parse_locale_manifest(codec._json_bytes(root), shard_resolver=lambda descriptor: bodies[descriptor["path"]])
            codec.validate_translation_resolution(parsed, LOCALES)
            for descriptor in root["source_fallbacks"]["shards"]:
                decoded = codec._decode_fallback_shard(bodies[descriptor["path"]], descriptor,
                                                       original["prompt_version"], set(LOCALES))
                self.assertLessEqual(sum(decoded["counts"].values()), 6)

    def test_retained_byte_limit_also_splits_without_raising_the_cap(self):
        original = fixture(64, source_size=640)
        with patch.object(codec, "MAX_EXPANDED_FALLBACK_BYTES", 3000):
            root, bodies = encoded_bundle(original)
            self.assertGreater(len(bodies), 16)
            parsed = codec.parse_locale_manifest(codec._json_bytes(root), shard_resolver=lambda descriptor: bodies[descriptor["path"]])
            codec.validate_translation_resolution(parsed, LOCALES)

    def test_split_does_not_keep_over_budget_encoder_traceback_alive(self):
        class EncoderAllocation:
            pass
        previous = []
        original_encode = codec._encode_fallback_shard

        def encode(*args):
            if not previous:
                allocation = EncoderAllocation()
                previous.append(weakref.ref(allocation))
                raise codec._ShardBudgetExceeded("valid leaf must split")
            self.assertIsNone(previous[0](), "recursive split retained the failed encoder frame")
            return original_encode(*args)

        with patch.object(codec, "_encode_fallback_shard", side_effect=encode):
            root, bodies = encoded_bundle(fixture())
        parsed = codec.parse_locale_manifest(codec._json_bytes(root), shard_resolver=lambda descriptor: bodies[descriptor["path"]])
        codec.validate_translation_resolution(parsed, LOCALES)

    def test_invalid_provenance_is_not_treated_as_a_capacity_split(self):
        original = fixture()
        next(iter(original["source_fallbacks"]["units"]["ko"].values()))["source"] = "Changed protected source"
        with patch.object(codec, "_iter_encoded_fallback_shards") as encode:
            with self.assertRaisesRegex(codec.LocaleManifestError, "hash differs"):
                codec.validate_locale_manifest_capacity(original)
            encode.assert_not_called()

    def test_missing_resolver_and_plain_json_summary_cannot_claim_acceptance(self):
        root, bodies = encoded_bundle(fixture())
        with self.assertRaisesRegex(codec.LocaleManifestError, "resolver"):
            codec.parse_locale_manifest(codec._json_bytes(root))
        with self.assertRaisesRegex(codec.LocaleManifestError, "not been verified"):
            codec.validate_translation_resolution(root, LOCALES)
        parsed = codec.parse_locale_manifest(codec._json_bytes(root), shard_resolver=lambda descriptor: bodies[descriptor["path"]])
        for field, value in (("prompt_version", "changed"), ("source_unit_count", 5), ("required_paths", [])):
            altered = copy.copy(parsed)
            altered[field] = value
            with self.assertRaisesRegex(codec.LocaleManifestError, "metadata changed"):
                codec.validate_translation_resolution(altered, LOCALES)

    def test_index_paths_counts_prefixes_and_leaf_budget_are_strict(self):
        original, bodies = encoded_bundle(fixture())
        changes = (
            lambda root: root["source_fallbacks"]["shards"][0].update(path="../secret"),
            lambda root: root["source_fallbacks"]["shards"][0].update(byte_size=True),
            lambda root: root["source_fallbacks"]["shards"].reverse(),
            lambda root: root["source_fallbacks"]["shards"].insert(0, root["source_fallbacks"]["shards"][0]),
            lambda root: root["source_fallbacks"]["counts"].update(ko=True),
        )
        for mutate in changes:
            root = copy.deepcopy(original)
            mutate(root)
            with self.subTest(mutate=mutate), self.assertRaises(codec.LocaleManifestError):
                codec.parse_locale_manifest(codec._json_bytes(root), shard_resolver=lambda descriptor: self.fail("invalid index reached resolver"))
        root = copy.deepcopy(original)
        first = root["source_fallbacks"]["shards"][0]
        child = dict(first, prefix=first["prefix"] + "0")
        child["path"] = f"{codec.FALLBACK_SHARD_DIRECTORY}/{child['prefix']}-{child['sha256']}.json"
        root["source_fallbacks"]["shards"].insert(1, child)
        with self.assertRaisesRegex(codec.LocaleManifestError, "overlapping"):
            codec.locale_manifest_shard_descriptors(root)
        with patch.object(codec, "MAX_FALLBACK_SHARDS", 1), self.assertRaisesRegex(codec.LocaleManifestError, "leaf budget"):
            codec.validate_locale_manifest_capacity(fixture())

    def test_missing_corrupt_and_mismatched_shard_is_rejected(self):
        root, bodies = encoded_bundle(fixture())
        for body in (b"", b"{}", b"corrupted"):
            with self.subTest(body=body), self.assertRaisesRegex(codec.LocaleManifestError, "size or hash"):
                codec.parse_locale_manifest(codec._json_bytes(root), shard_resolver=lambda descriptor: body)
        for field, value in (("prompt_version", "other"), ("prefix", "ff")):
            changed = copy.deepcopy(root)
            shard = json.loads(bodies[changed["source_fallbacks"]["shards"][0]["path"]])
            shard[field] = value
            replace_shard(changed, bodies, 0, shard)
            with self.assertRaisesRegex(codec.LocaleManifestError, "schema or identity"):
                codec.parse_locale_manifest(codec._json_bytes(changed), shard_resolver=lambda descriptor: bodies[descriptor["path"]])

    def test_rehashed_bad_source_wrong_partition_and_false_counts_are_rejected(self):
        original, original_bodies = encoded_bundle(fixture())
        for mutation in ("source", "partition", "count"):
            root, bodies = copy.deepcopy(original), dict(original_bodies)
            descriptor = root["source_fallbacks"]["shards"][0]
            shard = json.loads(bodies[descriptor["path"]])
            packed = shard["source_fallbacks"]
            table = json.loads(zlib.decompress(base64.b64decode(packed["data"])))
            if mutation == "source":
                table["records"][0]["source"] = "Changed source but recomputed all file hashes"
            elif mutation == "partition":
                table["keys"][0] = ("f" if descriptor["prefix"][0] != "f" else "0") + table["keys"][0][1:]
            else:
                table["counts"]["ko"] += 1
            table_body = codec._json_bytes(table)
            packed.update(byte_size=len(table_body), sha256=hashlib.sha256(table_body).hexdigest(),
                          data=base64.b64encode(zlib.compress(table_body)).decode())
            replace_shard(root, bodies, 0, shard)
            with self.subTest(mutation=mutation), self.assertRaises(codec.LocaleManifestError):
                codec.parse_locale_manifest(codec._json_bytes(root), shard_resolver=lambda descriptor: bodies[descriptor["path"]])
        root, bodies = copy.deepcopy(original), dict(original_bodies)
        root["source_fallbacks"]["counts"]["ko"] -= 1
        with self.assertRaisesRegex(codec.LocaleManifestError, "verified shard counts differ"):
            codec.parse_locale_manifest(codec._json_bytes(root), shard_resolver=lambda descriptor: bodies[descriptor["path"]])

    def test_parser_releases_previous_leaf_before_resolving_next(self):
        root, bodies = encoded_bundle(fixture())
        original_decode = codec._decode_fallback_shard
        previous = []

        def decode(*args, **kwargs):
            value = original_decode(*args, **kwargs)
            previous[:] = [weakref.ref(next(iter(value["units"]["ko"].values())))]
            return value

        def resolve(descriptor):
            if previous:
                self.assertIsNone(previous[0](), "a prior leaf's decoded records survived")
            return bodies[descriptor["path"]]

        with patch.object(codec, "_decode_fallback_shard", side_effect=decode):
            parsed = codec.parse_locale_manifest(codec._json_bytes(root), shard_resolver=resolve)
        self.assertIsNone(previous[0]())
        codec.validate_translation_resolution(parsed, LOCALES)

    def test_writer_does_not_try_monolithic_encoding_and_copy_includes_all_leaves(self):
        with tempfile.TemporaryDirectory() as temporary:
            source = Path(temporary) / "site/data/i18n/manifest.json"
            destination = Path(temporary) / "artifact/candidate/data/i18n/manifest.json"
            with patch.object(codec, "encode_locale_manifest", side_effect=AssertionError("global encoding attempted")):
                codec.write_locale_manifest_bundle(source, fixture())
            parsed = codec.load_locale_manifest(source)
            codec.copy_locale_manifest_bundle(source, destination)
            self.assertEqual(codec.load_locale_manifest(destination), parsed)
            for item in codec.locale_manifest_shard_descriptors(parsed):
                self.assertEqual((Path(temporary) / "site" / item["path"]).read_bytes(),
                                 (Path(temporary) / "artifact/candidate" / item["path"]).read_bytes())
            shard = codec._local_shard_path(source, codec.locale_manifest_shard_descriptors(parsed)[0])
            saved = shard.read_bytes()
            shard.unlink()
            with self.assertRaisesRegex(codec.LocaleManifestError, "missing"):
                codec.load_locale_manifest(source)
            elsewhere = Path(temporary) / "elsewhere.json"
            elsewhere.write_bytes(saved)
            shard.symlink_to(elsewhere)
            with self.assertRaisesRegex(codec.LocaleManifestError, "symlink"):
                codec.load_locale_manifest(source)

    def test_copy_writes_the_exact_root_that_was_verified(self):
        with tempfile.TemporaryDirectory() as temporary:
            source = Path(temporary) / "site/data/i18n/manifest.json"
            destination = Path(temporary) / "artifact/data/i18n/manifest.json"
            codec.write_locale_manifest_bundle(source, fixture())
            expected = source.read_bytes()
            reader = codec._read_local_shard

            def switch_root(*args):
                source.write_text('{"schema_version":1,"unverified":"different root"}')
                return reader(*args)

            with patch.object(codec, "_read_local_shard", side_effect=switch_root):
                codec.copy_locale_manifest_bundle(source, destination)
            self.assertEqual(destination.read_bytes(), expected)
            codec.validate_translation_resolution(codec.load_locale_manifest(destination), LOCALES)

    def test_rewrite_removes_only_obsolete_generated_leaves(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "data/i18n/manifest.json"
            codec.write_locale_manifest_bundle(path, fixture())
            directory = path.parent / "source-fallbacks"
            old = set(directory.iterdir())
            unrelated = directory / "notes.txt"
            unrelated.write_text("outside generated leaf naming contract")
            codec.write_locale_manifest_bundle(path, fixture(1))
            parsed = codec.load_locale_manifest(path)
            expected = {codec._local_shard_path(path, item) for item in codec.locale_manifest_shard_descriptors(parsed)}
            self.assertEqual(set(directory.iterdir()), expected | {unrelated})
            self.assertTrue(old - expected)
            codec.write_locale_manifest_bundle(path, fixture(0))
            self.assertEqual(list(directory.iterdir()), [unrelated])


class CloudShardTests(unittest.TestCase):
    @unittest.skipUnless(os.environ.get("LOCALE_MANIFEST_SHARD_SCALE"), "Large source inventory runs only in Actions")
    def test_inventory_crosses_original_global_reference_and_retained_bounds(self):
        self.assertEqual(os.environ.get("GITHUB_ACTIONS"), "true", "large scale fixture is cloud-only")
        count = int(os.environ["LOCALE_MANIFEST_SHARD_SCALE"])
        self.assertEqual(count, 110000)
        original = fixture(count, source_size=640)
        rows = original["source_fallbacks"]["units"]["ko"]
        retained = sum(len(codec._json_bytes(row)) for row in rows.values()) + count * 3 * 72
        self.assertGreater(count * 3, codec.MAX_FALLBACK_REFERENCES)
        self.assertGreater(retained, codec.MAX_EXPANDED_FALLBACK_BYTES)
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "data/i18n/manifest.json"
            with patch.object(codec, "encode_locale_manifest", side_effect=AssertionError("global encoding attempted")):
                codec.write_locale_manifest_bundle(path, original)
            parsed = codec.load_locale_manifest(path)
            codec.validate_translation_resolution(parsed, LOCALES)
            self.assertEqual(parsed["source_fallbacks"]["counts"], original["source_fallbacks"]["counts"])
            descriptors = codec.locale_manifest_shard_descriptors(parsed)
            self.assertEqual(len(descriptors), 16)
            maxima = {"references": 0, "retained_bytes": 0, "decoded_bytes": 0}
            for descriptor in descriptors:
                fallback = json.loads(codec._read_local_shard(path, descriptor))["source_fallbacks"]
                packed = codec._decompress_fallback_records(fallback)
                references = sum(len(rows) for rows in packed["units"].values())
                retained_bytes = sum(len(codec._json_bytes(row)) for row in packed["records"]) + references * 72
                self.assertLessEqual(references, codec.MAX_FALLBACK_REFERENCES)
                self.assertLessEqual(retained_bytes, codec.MAX_EXPANDED_FALLBACK_BYTES)
                self.assertLessEqual(fallback["byte_size"], codec.MAX_EXPANDED_FALLBACK_BYTES)
                maxima["references"] = max(maxima["references"], references)
                maxima["retained_bytes"] = max(maxima["retained_bytes"], retained_bytes)
                maxima["decoded_bytes"] = max(maxima["decoded_bytes"], fallback["byte_size"])
                del packed, fallback
            print(json.dumps({"cloud_shard_sources": count, "global_references": count * 3,
                              "global_retained_bytes": retained, "shards": len(descriptors),
                              "max_shard_wire_bytes": max(row["byte_size"] for row in descriptors),
                              "max_shard_accounting": maxima,
                              "root_wire_bytes": path.stat().st_size}, sort_keys=True))

    @unittest.skipUnless(os.environ.get("LOCALE_MANIFEST_FULL"), "Exact complete manifest was not requested")
    def test_complete_production_manifest_keeps_all_rows_and_metadata(self):
        self.assertEqual(os.environ.get("GITHUB_ACTIONS"), "true", "complete input comparison is cloud-only")
        original_path = Path(os.environ["LOCALE_MANIFEST_FULL"])
        original = codec.load_locale_manifest(original_path)
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "data/i18n/manifest.json"
            if original["source_fallbacks"]["schema_version"] == 5:
                # Future completed runs already carry the new format. Verify
                # and copy every bound leaf without reconstructing a global map.
                codec.copy_locale_manifest_bundle(original_path, path)
                self.assertEqual(path.read_bytes(), original_path.read_bytes())
                self.assertEqual(codec.load_locale_manifest(path), original)
                for descriptor in codec.locale_manifest_shard_descriptors(original):
                    self.assertEqual(codec._read_local_shard(original_path, descriptor),
                                     codec._read_local_shard(path, descriptor))
                print(json.dumps({"production_shard_sources": original["source_unit_count"],
                                  "complete_references": sum(original["source_fallbacks"]["counts"].values()),
                                  "root_wire_bytes": path.stat().st_size,
                                  "shards": len(codec.locale_manifest_shard_descriptors(original))}, sort_keys=True))
                return
            self.assertEqual(original["source_fallbacks"]["schema_version"], 1)
            codec.write_locale_manifest_bundle(path, original)
            parsed = codec.load_locale_manifest(path)
            codec.validate_translation_resolution(parsed, LOCALES)
            self.assertEqual({key: value for key, value in parsed.items() if key != "source_fallbacks"},
                             {key: value for key, value in original.items() if key != "source_fallbacks"})
            matched = dict.fromkeys(LOCALES, 0)
            for descriptor in codec.locale_manifest_shard_descriptors(parsed):
                body = codec._read_local_shard(path, descriptor)
                part = codec._decode_fallback_shard(body, descriptor, original["prompt_version"], set(LOCALES))
                for locale in LOCALES:
                    expected = {key: row for key, row in original["source_fallbacks"]["units"][locale].items()
                                if key.startswith(descriptor["prefix"])}
                    self.assertEqual(part["units"][locale], expected)
                    matched[locale] += len(expected)
            self.assertEqual(matched, original["source_fallbacks"]["counts"])
            descriptors = codec.locale_manifest_shard_descriptors(parsed)
            print(json.dumps({"production_shard_sources": original["source_unit_count"],
                              "complete_references": sum(matched.values()), "root_wire_bytes": path.stat().st_size,
                              "shards": len(descriptors),
                              "total_shard_wire_bytes": sum(row["byte_size"] for row in descriptors),
                              "max_shard_wire_bytes": max(row["byte_size"] for row in descriptors)}, sort_keys=True))


if __name__ == "__main__":
    unittest.main()
