#!/usr/bin/env python3
"""Regressions for stale, incomplete and altered served chart indexes."""
import copy
import json
from pathlib import Path
import tempfile
import unittest

from compare_portal_release_semantics import COMPONENT_KEYS, digest, stable_value
import verify_public_chart_index as gate


class ChartAcceptanceTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.index = {"schema_version": 1, "updated_at_bjt": "2026-09-29",
                      "report_count": 1, "item_count": 2, "reports": [
                          {"report_id": "example", "chart_count": 2, "charts": [
                              {"image_id": "a" * 64, "description": "new description"},
                              {"image_id": "b" * 64, "description": "retained description"}]}]}
        self.index_path = self.write("candidate.json", self.index)
        components = dict.fromkeys(COMPONENT_KEYS, "0" * 64)
        components["chart_search_index"] = digest(stable_value(self.index))
        self.semantics = self.write("semantics.json", {
            "schema_version": 1, "normalizer_version": 1, "components": components,
            "semantic_sha256": digest(components)})
        self.expected = self.root / "expected.json"
        self.output = self.root / "report.json"

    def write(self, name, value):
        path = self.root / name
        path.write_text(json.dumps(value), encoding="utf-8")
        return path

    def prepare(self):
        return gate.main(["prepare", "--index", str(self.index_path), "--semantics",
                          str(self.semantics), "--output", str(self.expected)])

    def verify(self, public=None, release=None):
        return gate.main(["verify", "--expected", str(self.expected), "--semantics",
                          str(self.semantics), "--public-index", str(public or self.index_path),
                          "--release-index", str(release or self.index_path),
                          "--output", str(self.output)])

    def test_exact_prepared_content_passes_both_served_routes(self):
        self.assertEqual(self.prepare(), 0)
        self.assertEqual(self.verify(), 0)
        report = json.loads(self.output.read_text())
        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["public"], report["release"])
        self.assertEqual(report["public"]["item_count"], 2)
        self.assertNotIn("description", self.output.read_text())
        self.assertNotIn(str(self.root), self.output.read_text())

    def test_same_count_stale_description_or_image_is_rejected_on_either_route(self):
        self.assertEqual(self.prepare(), 0)
        for field, value in (("description", "yesterday"), ("image_id", "c" * 64)):
            changed = copy.deepcopy(self.index)
            changed["reports"][0]["charts"][0][field] = value
            path = self.write("changed.json", changed)
            for route in ("public", "release"):
                with self.subTest(field=field, route=route):
                    self.assertEqual(self.verify(**{route: path}), 1)
                    self.assertEqual(json.loads(self.output.read_text())["status"], "failed")

    def test_actual_array_counts_must_match_all_declared_counts(self):
        mutations = [lambda x: x.update(report_count=2), lambda x: x.update(item_count=3),
                     lambda x: x.update(item_count=True),
                     lambda x: x["reports"][0].update(chart_count=3),
                     lambda x: x["reports"][0]["charts"].pop(),
                     lambda x: x["reports"][0]["charts"].append(None)]
        for mutate in mutations:
            value = copy.deepcopy(self.index)
            mutate(value)
            with self.subTest(index=value), self.assertRaises(ValueError):
                gate.index_receipt(self.write("bad.json", value))

    def test_empty_valid_index_and_duplicate_image_occurrences_are_counted(self):
        empty = {"schema_version": 1, "report_count": 0, "item_count": 0, "reports": []}
        self.assertEqual(gate.index_receipt(self.write("empty.json", empty))["item_count"], 0)
        value = copy.deepcopy(self.index)
        value["reports"][0]["charts"][1]["image_id"] = "a" * 64
        self.assertEqual(gate.index_receipt(self.write("reused.json", value))["item_count"], 2)

    def test_semantic_component_must_match_prepared_candidate(self):
        self.index["reports"][0]["charts"][0]["description"] = "different"
        self.write("candidate.json", self.index)
        self.assertEqual(self.prepare(), 1)
        self.assertFalse(self.expected.exists())

    def test_receipt_tampering_and_invalid_manifest_fail_closed(self):
        self.assertEqual(self.prepare(), 0)
        original = json.loads(self.expected.read_text())
        for field, value in (("item_count", True), ("file_sha256", "bad"),
                             ("source_text", "must not appear in report")):
            self.write("expected.json", {**original, field: value})
            self.assertEqual(self.verify(), 1)
            self.assertNotIn("must not appear", self.output.read_text())
        self.write("expected.json", original)
        self.write("semantics.json", {"schema_version": 1})
        self.assertEqual(self.verify(), 1)

    def test_timestamp_only_change_retains_semantics_but_fails_exact_release_bytes(self):
        self.assertEqual(self.prepare(), 0)
        changed = {**self.index, "updated_at_bjt": "2026-09-30"}
        path = self.write("changed.json", changed)
        self.assertEqual(gate.index_receipt(path)["semantic_sha256"],
                         gate.index_receipt(self.index_path)["semantic_sha256"])
        self.assertEqual(self.verify(public=path), 1)

    def test_invalid_json_missing_or_oversized_body_replaces_prior_success(self):
        self.assertEqual(self.prepare(), 0)
        self.assertEqual(self.verify(), 0)
        for body in ("", "{truncated", "[]", "null"):
            path = self.root / "bad.json"
            path.write_text(body)
            self.assertEqual(self.verify(public=path), 1)
            self.assertEqual(json.loads(self.output.read_text())["status"], "failed")
        self.assertEqual(self.verify(public=self.root / "missing.json"), 1)
        from unittest.mock import patch
        with patch.object(gate, "MAX_INDEX_BYTES", 5), self.assertRaises(ValueError):
            gate.index_receipt(self.index_path)


if __name__ == "__main__":
    unittest.main()
