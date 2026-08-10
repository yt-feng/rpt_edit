#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "build_member_course_directory",
    ROOT / "scripts" / "build_member_course_directory.py",
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load course directory builder")
builder_module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = builder_module
SPEC.loader.exec_module(builder_module)


def private_config() -> dict:
    return {
        "catalog_version": "fixture-v1",
        "root_prefix": "private/root",
        "hmac_secret": "fixture-secret-with-more-than-24-bytes",
        "courses": [
            {"id": "fin-01", "title": "Financial Modeling", "category": "Finance"},
            {"id": "law-02", "title": "Transaction Practice", "category": "Legal"},
        ],
        "privacy": {
            "redact_terms": ["SourceBrand", "TrainingHub", "SpeakerName", "PlatformLMS"],
            "redact_patterns": [r"member\s*group\s*\d+"],
        },
        "prefix_rules": [
            {"prefix": "SourceBrand", "course_ids": ["law-02"], "strip_components": 1},
            {
                "prefix": "SourceBrand/ModelPack",
                "course_ids": ["fin-01"],
                "strip_components": 2,
                "priority": 10,
            },
            {"prefix": "TrainingHub", "course_ids": ["law-02"], "strip_components": 1},
        ],
        "keyword_rules": [
            {
                "keywords": ["valuation"],
                "course_ids": ["law-02"],
                "when_course_ids": ["fin-01"],
            }
        ],
        "notable_entities": [
            {"name": "Prestige Bank", "type": "investment_bank", "aliases": ["PB Capital"]},
            {"name": "Alpha Law Firm", "type": "law_firm", "aliases": ["ALF"]},
            {"name": "Market Authority", "type": "regulator", "aliases": ["MA Board"]},
        ],
    }


def index_line(path: str, size: str = "13.5MB", date: str = "2026-08-10") -> str:
    return f"- `{path}` — {size} — {date}\n"


class CourseDirectoryBuilderTests(unittest.TestCase):
    def build_fixture(self) -> dict:
        with tempfile.TemporaryDirectory() as temp:
            index = Path(temp) / "index.md"
            index.write_text(
                "# Private fixture\n\n"
                + index_line(
                    "private/root/SourceBrand/ModelPack/TrainingHub/Prestige Bank Valuation/"
                    "PlatformLMS DCF Valuation.pdf"
                )
                + index_line(
                    "private/root/TrainingHub/Legal/SpeakerName-Alpha Law Firm MA Board Merger.mp4",
                    "2.0GB",
                )
                + index_line(
                    "private/root/TrainingHub/Legal/member group 42/Contact user@example.com 1.mp3",
                    "800KB",
                ),
                encoding="utf-8",
            )
            builder = builder_module.CourseDirectoryBuilder(private_config())
            return builder.build(builder.parse_index(index))

    def test_builds_hmac_tree_and_preserves_only_allowed_entities(self) -> None:
        payload = self.build_fixture()
        self.assertEqual(set(payload), {"schema_version", "generated_at", "items"})
        self.assertEqual(len(payload["items"]), 4)
        self.assertTrue(all(node["id"].startswith("f_") for node in payload["items"]))
        self.assertTrue(all(set(node) == {
            "id", "course_id", "name", "folders", "extension", "size_label", "date", "entities",
        } for node in payload["items"]))
        self.assertTrue(all(
            isinstance(entity, str)
            for node in payload["items"]
            for entity in node["entities"]
        ))
        self.assertTrue(all(
            isinstance(entity, str)
            for node in payload["items"]
            for entity in node["entities"]
        ))

        serialized = json.dumps(payload, ensure_ascii=False)
        for private_value in ("SourceBrand", "TrainingHub", "SpeakerName", "PlatformLMS", "private/root"):
            self.assertNotIn(private_value.casefold(), serialized.casefold())
        self.assertNotIn("user@example.com", serialized)
        self.assertNotIn("member group 42", serialized.casefold())
        self.assertIn("Prestige Bank", serialized)
        self.assertIn("Alpha Law Firm", serialized)
        self.assertIn("Market Authority", serialized)

    def test_longest_prefix_is_primary_and_keyword_adds_secondary_course(self) -> None:
        payload = self.build_fixture()
        valuation_nodes = [node for node in payload["items"] if "Valuation" in node["name"]]
        self.assertEqual({node["course_id"] for node in valuation_nodes}, {"fin-01", "law-02"})
        self.assertEqual(sum(node["course_id"] == "fin-01" for node in payload["items"]), 1)
        self.assertEqual(sum(node["course_id"] == "law-02" for node in payload["items"]), 3)

    def test_generic_file_title_uses_safe_parent_context(self) -> None:
        payload = self.build_fixture()
        audio = next(node for node in payload["items"] if node["extension"] == "mp3")
        self.assertNotEqual(audio["name"], "1")
        self.assertIn("Legal", audio["folders"])
        self.assertEqual(audio["size_label"], "800KB")

    def test_hmac_ids_are_deterministic_but_change_with_secret(self) -> None:
        first = self.build_fixture()
        second = self.build_fixture()
        self.assertEqual(
            [node["id"] for node in first["items"]],
            [node["id"] for node in second["items"]],
        )
        changed = private_config()
        changed["hmac_secret"] = "a-different-fixture-secret-over-24-bytes"
        with tempfile.TemporaryDirectory() as temp:
            index = Path(temp) / "index.md"
            index.write_text(
                index_line("private/root/TrainingHub/Legal/Agreement.pdf"),
                encoding="utf-8",
            )
            builder = builder_module.CourseDirectoryBuilder(changed)
            payload = builder.build(builder.parse_index(index))
        self.assertNotEqual(first["items"][0]["id"], payload["items"][0]["id"])

    def test_unmapped_source_fails_without_echoing_private_path(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            index = Path(temp) / "index.md"
            private_path = "private/root/UnknownProvider/SecretFolder/Document.pdf"
            index.write_text(index_line(private_path), encoding="utf-8")
            builder = builder_module.CourseDirectoryBuilder(private_config())
            with self.assertRaises(builder_module.BuildError) as context:
                builder.build(builder.parse_index(index))
        self.assertNotIn(private_path, str(context.exception))
        self.assertIn("no prefix mapping", str(context.exception))

    def test_config_rejects_allowed_entity_that_conflicts_with_redaction(self) -> None:
        config = private_config()
        config["notable_entities"].append({
            "name": "SourceBrand Research",
            "type": "provider",
            "aliases": [],
        })
        with self.assertRaises(builder_module.BuildError):
            builder_module.CourseDirectoryBuilder(config)

    def test_config_rejects_course_id_outside_worker_catalog(self) -> None:
        config = private_config()
        config["courses"][0]["id"] = "unknown-01"
        with self.assertRaises(builder_module.BuildError) as context:
            builder_module.CourseDirectoryBuilder(config)
        self.assertIn("unsupported course ID", str(context.exception))

    def test_course_id_allowlist_matches_publisher_and_worker_catalog(self) -> None:
        workflow = (ROOT / ".github" / "workflows" / "course-directory-private-publish.yml").read_text(
            encoding="utf-8"
        )
        workflow_block = workflow.split("COURSE_IDS = {", 1)[1].split("}", 1)[0]
        workflow_ids = set(re.findall(r'"([a-z]+-\d{2})"', workflow_block))

        worker = (ROOT / "workers" / "portal-suite-worker" / "src" / "index.js").read_text(
            encoding="utf-8"
        )
        catalog_block = worker.split("const COURSE_CATALOG = Object.freeze([", 1)[1].split(
            "].map((course)", 1
        )[0]
        worker_ids = set(re.findall(r'id:\s*"([a-z]+-\d{2})"', catalog_block))

        self.assertEqual(len(builder_module.ALLOWED_COURSE_IDS), 43)
        self.assertEqual(builder_module.ALLOWED_COURSE_IDS, workflow_ids)
        self.assertEqual(builder_module.ALLOWED_COURSE_IDS, worker_ids)

    def test_capacity_contract_matches_encryptor_publisher_and_worker(self) -> None:
        def constant_value(path: Path, name: str) -> int:
            text = path.read_text(encoding="utf-8")
            match = re.search(rf"\b{name}\s*=\s*([0-9_* ]+)", text)
            self.assertIsNotNone(match, f"missing {name} in {path.name}")
            factors = [int(value.replace("_", "")) for value in re.findall(r"\d[\d_]*", match.group(1))]
            result = 1
            for factor in factors:
                result *= factor
            return result

        expected_bytes = 16 * 1024 * 1024
        expected_items = 45_000
        encryptor = ROOT / "scripts" / "encrypt_member_course_directory.mjs"
        workflow = ROOT / ".github" / "workflows" / "course-directory-private-publish.yml"
        worker = ROOT / "workers" / "portal-suite-worker" / "src" / "index.js"

        self.assertEqual(builder_module.MAX_COMPACT_JSON_BYTES, expected_bytes)
        self.assertEqual(builder_module.MAX_DIRECTORY_ITEMS, expected_items)
        self.assertEqual(constant_value(encryptor, "MAX_PLAINTEXT_BYTES"), expected_bytes)
        self.assertEqual(constant_value(encryptor, "MAX_ITEMS"), expected_items)
        self.assertEqual(constant_value(workflow, "MAX_PLAINTEXT_BYTES"), expected_bytes)
        self.assertEqual(constant_value(workflow, "MAX_ITEMS"), expected_items)
        self.assertEqual(constant_value(worker, "COURSE_DIRECTORY_MAX_BYTES"), expected_bytes)
        self.assertEqual(constant_value(worker, "COURSE_DIRECTORY_MAX_ITEMS"), expected_items)

    def test_output_caps_fail_before_writing(self) -> None:
        builder = builder_module.CourseDirectoryBuilder(private_config())
        minimal_item = {
            "id": "f_12345678",
            "course_id": "fin-01",
            "name": "Document",
            "folders": [],
            "extension": "pdf",
            "size_label": "1KB",
            "date": "2026-08-10",
            "entities": [],
        }
        payload = {
            "schema_version": 1,
            "generated_at": "2026-08-10T00:00:00+00:00",
            "items": [minimal_item],
        }
        with patch.object(builder_module, "MAX_DIRECTORY_ITEMS", 0):
            with self.assertRaises(builder_module.BuildError) as item_context:
                builder.validate_output(payload)
        self.assertIn("item count", str(item_context.exception))

        with patch.object(builder_module, "MAX_COMPACT_JSON_BYTES", 64):
            with self.assertRaises(builder_module.BuildError) as byte_context:
                builder.validate_output(payload)
        self.assertIn("UTF-8 output", str(byte_context.exception))

    def test_short_entity_alias_requires_ascii_word_boundaries(self) -> None:
        config = private_config()
        config["notable_entities"].append({
            "name": "Alpha Bureau",
            "type": "regulator",
            "aliases": ["AB"],
        })
        with tempfile.TemporaryDirectory() as temp:
            index = Path(temp) / "index.md"
            index.write_text(
                index_line("private/root/TrainingHub/Legal/Table Review.pdf")
                + index_line("private/root/TrainingHub/Legal/AB Review.pdf"),
                encoding="utf-8",
            )
            builder = builder_module.CourseDirectoryBuilder(config)
            payload = builder.build(builder.parse_index(index))
        by_name = {item["name"]: item for item in payload["items"]}
        self.assertNotIn("Alpha Bureau", by_name["Table Review"]["entities"])
        self.assertIn("Alpha Bureau", by_name["AB Review"]["entities"])

    def test_flat_folders_keep_the_nearest_eight_levels(self) -> None:
        levels = [f"Folder {number}" for number in range(1, 11)]
        with tempfile.TemporaryDirectory() as temp:
            index = Path(temp) / "index.md"
            index.write_text(
                index_line("/".join(["private/root/TrainingHub", *levels, "Document.pdf"])),
                encoding="utf-8",
            )
            builder = builder_module.CourseDirectoryBuilder(private_config())
            payload = builder.build(builder.parse_index(index))
        self.assertEqual(payload["items"][0]["folders"], levels[-8:])

    def test_domain_marker_touching_chinese_text_is_removed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            index = Path(temp) / "index.md"
            index.write_text(
                index_line("private/root/TrainingHub/Legal/课程www.example.com资料.pdf")
                + index_line("private/root/TrainingHub/Legal/联系abc@example.com资料.pdf")
                + index_line("private/root/TrainingHub/Legal/网址private.example.edu资料.pdf"),
                encoding="utf-8",
            )
            builder = builder_module.CourseDirectoryBuilder(private_config())
            payload = builder.build(builder.parse_index(index))
        serialized = json.dumps(payload, ensure_ascii=False).casefold()
        self.assertNotIn("www.", serialized)
        self.assertNotIn("example.com", serialized)
        self.assertNotIn("abc@", serialized)
        self.assertNotIn("example.edu", serialized)


if __name__ == "__main__":
    unittest.main()
