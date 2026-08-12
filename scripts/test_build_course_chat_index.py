#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "build_course_chat_index",
    ROOT / "scripts" / "build_course_chat_index.py",
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load Course Chat index builder")
builder = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = builder
SPEC.loader.exec_module(builder)


def row(course_id: str, number: int, entities: list[str] | None = None) -> dict:
    return {
        "id": f"file-{course_id}-{number:05d}",
        "course_id": course_id,
        "name": f"Resource {course_id} {number}",
        "folders": ["Topic"],
        "extension": "pdf",
        "size_label": "1MB",
        "date": "2026-08-12",
        "entities": list(entities or []),
    }


def payload(rows_per_course: int = 35) -> dict:
    rows = []
    for course_id in sorted(builder.ALLOWED_COURSE_IDS):
        rows.extend(row(course_id, number) for number in range(rows_per_course))
    return {
        "schema_version": 1,
        "generated_at": "2026-08-12T00:00:00Z",
        "items": rows,
    }


class CourseChatIndexTests(unittest.TestCase):
    def test_retains_all_entity_rows_and_thirty_neutral_rows_per_course(self) -> None:
        source = payload(40)
        source["items"][35]["entities"] = ["Public Institution"]
        source["items"][-1]["entities"] = ["Public Regulator"]

        result = builder.build_course_chat_index(source)

        selected_ids = {item["id"] for item in result["items"]}
        self.assertIn(source["items"][35]["id"], selected_ids)
        self.assertIn(source["items"][-1]["id"], selected_ids)
        for course_id in builder.ALLOWED_COURSE_IDS:
            neutral = [
                item for item in result["items"]
                if item["course_id"] == course_id and not item["entities"]
            ]
            self.assertEqual(len(neutral), 30)

    def test_output_is_an_original_order_allow_list_subset_and_deterministic(self) -> None:
        source = payload(32)
        result = builder.build_course_chat_index(source)
        again = builder.build_course_chat_index(source)

        source_by_id = {item["id"]: item for item in source["items"]}
        positions = {item["id"]: index for index, item in enumerate(source["items"])}
        selected_positions = [positions[item["id"]] for item in result["items"]]
        self.assertEqual(selected_positions, sorted(selected_positions))
        self.assertTrue(all(item == source_by_id[item["id"]] for item in result["items"]))
        self.assertEqual(
            builder.serialize_course_chat_index(result),
            builder.serialize_course_chat_index(again),
        )

    def test_rejects_private_extra_fields_and_incomplete_course_coverage(self) -> None:
        source = payload(1)
        source["items"][0]["source_path"] = "private/path"
        with self.assertRaisesRegex(builder.CourseChatIndexError, "allow-listed"):
            builder.build_course_chat_index(source)

        incomplete = payload(1)
        incomplete["items"] = [
            item for item in incomplete["items"] if item["course_id"] != "fin-01"
        ]
        with self.assertRaisesRegex(builder.CourseChatIndexError, "cover every course"):
            builder.build_course_chat_index(incomplete)

    def test_enforces_item_and_compact_utf8_byte_caps(self) -> None:
        source = payload(1)
        for item in source["items"]:
            item["entities"] = ["Public Institution"]
        with patch.object(builder, "MAX_CHAT_INDEX_ITEMS", 42):
            with self.assertRaisesRegex(builder.CourseChatIndexError, "item limit"):
                builder.build_course_chat_index(source)

        result = builder.build_course_chat_index(payload(1))
        with patch.object(builder, "MAX_CHAT_INDEX_BYTES", 64):
            with self.assertRaisesRegex(builder.CourseChatIndexError, "byte limit"):
                builder.serialize_course_chat_index(result)

    def test_declared_caps_and_course_count_match_the_worker_contract(self) -> None:
        worker = (ROOT / "workers" / "portal-suite-worker" / "src" / "index.js").read_text(
            encoding="utf-8"
        )
        self.assertEqual(len(builder.ALLOWED_COURSE_IDS), 43)
        self.assertIn("const COURSE_CHAT_DIRECTORY_MAX_BYTES = 2 * 1024 * 1024;", worker)
        self.assertIn("const COURSE_CHAT_DIRECTORY_MAX_ITEMS = 5000;", worker)
        self.assertEqual(builder.MAX_CHAT_INDEX_BYTES, 2 * 1024 * 1024)
        self.assertEqual(builder.MAX_CHAT_INDEX_ITEMS, 5000)

    def test_real_json_encoding_is_compact(self) -> None:
        result = builder.build_course_chat_index(payload(1))
        encoded = builder.serialize_course_chat_index(result)
        self.assertEqual(encoded, json.dumps(result, ensure_ascii=False, separators=(",", ":")).encode())


if __name__ == "__main__":
    unittest.main()
