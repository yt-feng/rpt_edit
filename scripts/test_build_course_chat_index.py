#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import hashlib
import json
import struct
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
        self.assertIn(
            'const COURSE_CHAT_LOOKUP_MANIFEST_R2_KEY = "_course-directory/v2/chat-lookup/manifest.json";',
            worker,
        )
        self.assertIn("const CHAT_LOOKUP_SCHEMA_VERSION = 2;", worker)
        self.assertIn("const CHAT_LOOKUP_MAX_QUERY_TOKENS = 8;", worker)
        self.assertEqual(builder.LOOKUP_SCHEMA_VERSION, 2)
        self.assertEqual(builder.MAX_QUERY_TOKENS, 8)
        self.assertEqual(builder.MAX_CHAT_INDEX_BYTES, 2 * 1024 * 1024)
        self.assertEqual(builder.MAX_CHAT_INDEX_ITEMS, 5000)

    def test_real_json_encoding_is_compact(self) -> None:
        result = builder.build_course_chat_index(payload(1))
        encoded = builder.serialize_course_chat_index(result)
        self.assertEqual(encoded, json.dumps(result, ensure_ascii=False, separators=(",", ":")).encode())

    def test_v2_direct_indexes_are_deterministic_and_exact_under_collisions(self) -> None:
        entries = {f"key-{number}": {"number": number} for number in range(180)}
        index = builder.build_direct_index(entries)

        self.assertEqual(len(index.table), index.bucket_count * 12)
        self.assertEqual(index.table, builder.build_direct_index(entries).table)
        self.assertEqual(index.data, builder.build_direct_index(entries).data)
        self.assertTrue(any(
            struct.unpack_from(">I", index.table, slot * 12 + 8)[0] > 0
            for slot in range(index.bucket_count)
        ))
        for key, value in entries.items():
            self.assertEqual(builder.direct_index_lookup(index, key), value)
        self.assertIsNone(builder.direct_index_lookup(index, "not-present"))

    def test_v2_hash_contract_uses_sha256_first_u64_big_endian(self) -> None:
        key = "摩根大通"
        expected = int.from_bytes(hashlib.sha256(key.encode("utf-8")).digest()[:8], "big") % 257
        self.assertEqual(builder.direct_bucket_number(key, 257), expected)

    def test_v2_lookup_preserves_big_names_all_courses_and_private_allow_list(self) -> None:
        source = payload(2)
        source["items"][0]["name"] = "摩根大通并购模型与估值案例"
        source["items"][0]["entities"] = ["摩根大通"]
        source["items"][1]["name"] = "高盛数据中心建模案例"
        source["items"][1]["entities"] = ["高盛"]

        lookup = builder.build_course_chat_lookup(source)
        manifest = lookup.manifest

        self.assertEqual(manifest["schema_version"], 2)
        self.assertEqual(manifest["format"], "course-chat-direct-bucket-v2")
        self.assertEqual(manifest["course_count"], 43)
        self.assertEqual(manifest["max_query_tokens"], 8)
        self.assertEqual(manifest["max_candidates"], 12)
        self.assertLessEqual(len(manifest["default_items"]), 12)
        self.assertIn("摩根大通", manifest["default_items"][0]["name"])
        self.assertTrue(all(set(item) == builder.ROW_FIELDS for item in manifest["default_items"]))

        token_descriptor = manifest["token_index"]
        item_descriptor = manifest["item_index"]
        self.assertEqual(token_descriptor["slot_size"], 12)
        self.assertEqual(item_descriptor["slot_size"], 12)
        self.assertEqual(set(lookup.objects), {
            token_descriptor["table_key"], token_descriptor["data_key"],
            item_descriptor["table_key"], item_descriptor["data_key"],
        })
        self.assertTrue(all(f"/{lookup.revision}/" in key for key in lookup.objects))

    def test_v2_query_tokens_retrieve_only_exact_postings_and_items(self) -> None:
        source = payload(1)
        source["items"][0]["name"] = "摩根大通并购模型与估值案例"
        source["items"][0]["entities"] = ["摩根大通"]
        lookup = builder.build_course_chat_lookup(source)
        selected = builder.build_course_chat_index(source)["items"]
        item_id = source["items"][0]["id"]

        token_index = builder.DirectIndex(
            table=lookup.objects[lookup.manifest["token_index"]["table_key"]],
            data=lookup.objects[lookup.manifest["token_index"]["data_key"]],
            bucket_count=lookup.manifest["token_index"]["bucket_count"],
            key_count=lookup.manifest["token_count"],
        )
        item_index = builder.DirectIndex(
            table=lookup.objects[lookup.manifest["item_index"]["table_key"]],
            data=lookup.objects[lookup.manifest["item_index"]["data_key"]],
            bucket_count=lookup.manifest["item_index"]["bucket_count"],
            key_count=lookup.manifest["item_count"],
        )
        query_tokens = builder.normalize_course_chat_tokens("推荐摩根大通并购资料", query=True)
        self.assertLessEqual(len(query_tokens), 8)
        self.assertIn(item_id, builder.direct_index_lookup(token_index, "摩根大通"))
        self.assertIn(item_id, builder.direct_index_lookup(token_index, "并购"))
        self.assertEqual(
            builder.direct_index_lookup(item_index, item_id),
            next(item for item in selected if item["id"] == item_id),
        )
        self.assertIsNone(builder.direct_index_lookup(token_index, "不存在词"))

    def test_v2_manifest_is_small_and_references_verified_content_hashes(self) -> None:
        lookup = builder.build_course_chat_lookup(payload(4))
        encoded = builder.serialize_course_chat_lookup_manifest(lookup)
        self.assertLessEqual(len(encoded), 32 * 1024)
        self.assertNotIn(b"source_path", encoded)
        for descriptor_name in ("token_index", "item_index"):
            descriptor = lookup.manifest[descriptor_name]
            self.assertEqual(descriptor["max_bucket_bytes"], 64 * 1024)
            self.assertEqual(
                hashlib.sha256(lookup.objects[descriptor["table_key"]]).hexdigest(),
                descriptor["table_sha256"],
            )
            self.assertEqual(
                hashlib.sha256(lookup.objects[descriptor["data_key"]]).hexdigest(),
                descriptor["data_sha256"],
            )
        with patch.object(builder, "MAX_LOOKUP_MANIFEST_BYTES", 64):
            with self.assertRaisesRegex(builder.CourseChatIndexError, "manifest exceeds"):
                builder.serialize_course_chat_lookup_manifest(lookup)


if __name__ == "__main__":
    unittest.main()
