#!/usr/bin/env python3

from __future__ import annotations

import hashlib
import importlib.util
import json
import struct
import sys
import tempfile
import unittest
from io import BytesIO
from pathlib import Path


SCRIPT = Path(__file__).with_name("build_report_research_index.py")
sys.path.insert(0, str(SCRIPT.parent))
SPEC = importlib.util.spec_from_file_location("build_report_research_index", SCRIPT)
assert SPEC and SPEC.loader
indexer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(indexer)


class MissingObject(Exception):
    response = {"Error": {"Code": "NoSuchKey"}}


class FakeR2:
    def __init__(self, fail_key_suffix: str = "") -> None:
        self.objects: dict[str, bytes] = {}
        self.metadata: dict[str, dict[str, str]] = {}
        self.operations: list[tuple[str, str]] = []
        self.fail_key_suffix = fail_key_suffix

    def head_object(self, *, Bucket: str, Key: str):
        del Bucket
        self.operations.append(("head", Key))
        if Key not in self.objects:
            raise MissingObject()
        return {
            "ContentLength": len(self.objects[Key]),
            "Metadata": self.metadata.get(Key, {}),
        }

    def put_object(self, *, Bucket: str, Key: str, Body: bytes, Metadata=None, **kwargs):
        del Bucket, kwargs
        self.operations.append(("put", Key))
        if self.fail_key_suffix and Key.endswith(self.fail_key_suffix):
            raise RuntimeError("injected upload failure")
        body = bytes(Body)
        self.objects[Key] = body
        self.metadata[Key] = dict(Metadata or {"sha256": hashlib.sha256(body).hexdigest()})

    def get_object(self, *, Bucket: str, Key: str):
        del Bucket
        self.operations.append(("get", Key))
        if Key not in self.objects:
            raise MissingObject()
        return {"Body": BytesIO(self.objects[Key])}


def lookup(output: Path, descriptor: dict, key: str):
    bucket = indexer._bucket_index(key, descriptor["bucket_count"])
    table_path = output / Path(descriptor["table_key"]).name
    data_path = output / Path(descriptor["data_key"]).name
    with table_path.open("rb") as table:
        table.seek(bucket * descriptor["slot_size"])
        offset, length = struct.unpack(">QI", table.read(descriptor["slot_size"]))
    if not length:
        return None
    with data_path.open("rb") as data:
        data.seek(offset)
        entries = json.loads(data.read(length))
    return next((value for exact, value in entries if exact == key), None)


class ReportResearchIndexTests(unittest.TestCase):
    def catalog(self) -> dict:
        return {
            "schema_version": 1,
            "items": [
                {
                    "id": "a" * 24,
                    "title": "JPMorgan advanced materials outlook 260828",
                    "title_zh": "摩根大通：先进材料展望-260828",
                    "filename": "private-a.pdf",
                    "date_folder": "260828",
                    "bank_code": "JPM",
                    "bank_name": "摩根大通",
                    "page_count": 18,
                    "available": True,
                    "r2_key": "reports/private-a.pdf",
                    "source_path": "/private/mineru/source-a.md",
                },
                {
                    "id": "b" * 24,
                    "title": "Energy storage demand 260827",
                    "title_zh": "储能需求研究-260827",
                    "filename": "private-b.pdf",
                    "date_folder": "260827",
                    "bank_code": "ABC",
                    "bank_name": "研究机构",
                    "page_count": 12,
                    "r2_synced": True,
                },
                {
                    "id": "c" * 24,
                    "title": "Catalog title without extracted body 260826",
                    "filename": "private-c.pdf",
                    "date_folder": "260826",
                    "available": True,
                    "r2_key": "reports/private-c.pdf",
                },
            ],
        }

    def search_index(self) -> dict:
        return {
            "schema_version": 1,
            "items": [
                {
                    "id": "a" * 24,
                    "text": (
                        "This report reviews advanced materials and manufacturing economics. "
                        "The central full-text finding is that perovskite tandem conversion efficiency "
                        "improved materially while pilot-line yield remained the binding constraint. "
                        "Capacity assumptions, unit costs, sensitivity analysis, and adoption scenarios "
                        "are compared across suppliers. The evidence section records a 27 percent test "
                        "result and separates laboratory performance from commercial shipments. "
                    ) * 3,
                },
                {
                    "id": "b" * 24,
                    "text": (
                        "储能系统需求研究比较了多个机构的数据口径。报告正文指出长时储能招标量增长，"
                        "但并网确认与招标储备之间仍有时间差。研究进一步核对容量补偿、电芯成本、"
                        "利用小时和项目回报，并将实际并网数据与规划数据分开呈现。"
                    ) * 5,
                },
                {"id": "c" * 24, "text": "catalog title without extracted body 260826"},
                {"id": "not-a-catalog-id", "text": "must be ignored"},
            ],
        }

    def build_payload(
        self,
        root: Path,
        catalog_payload: dict,
        search_payload: dict,
        previous_corpus: dict | None = None,
    ) -> tuple[Path, dict]:
        catalog = root / "catalog.json"
        search = root / "search.json"
        output = root / "output"
        catalog.write_text(json.dumps(catalog_payload, ensure_ascii=False), encoding="utf-8")
        search.write_text(json.dumps(search_payload, ensure_ascii=False), encoding="utf-8")
        manifest = indexer.build_index(
            catalog,
            search,
            output,
            token_bucket_count=32,
            item_bucket_count=8,
            evidence_bucket_count=32,
            chunk_chars=180,
            chunk_overlap=24,
            min_text_chars=80,
            previous_corpus=previous_corpus,
        )
        return output, manifest

    def build(self, root: Path) -> tuple[Path, dict]:
        return self.build_payload(root, self.catalog(), self.search_index())

    def test_full_text_term_points_to_relevant_bounded_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output, manifest = self.build(Path(temporary))
            self.assertEqual(manifest["schema_version"], 1)
            self.assertEqual(manifest["item_count"], 2)
            self.assertGreater(manifest["chunk_count"], 2)
            postings = lookup(output, manifest["token_table"], "perovskite")
            self.assertEqual(postings[0]["id"], "a" * 24)
            self.assertLessEqual(len(postings[0]["chunks"]), 2)
            evidence_key = f"{'a' * 24}:{postings[0]['chunks'][0]}"
            evidence = lookup(output, manifest["evidence_table"], evidence_key)
            self.assertIn("perovskite", evidence["text"].lower())
            self.assertLessEqual(len(evidence["text"]), 180)

            chinese = lookup(output, manifest["token_table"], "长时储能")
            self.assertEqual(chinese[0]["id"], "b" * 24)

    def test_items_and_evidence_expose_only_public_source_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output, manifest = self.build(Path(temporary))
            item = lookup(output, manifest["item_table"], "a" * 24)
            self.assertEqual(item["public_url"], f"/report.html?id={'a' * 24}")
            self.assertNotIn("filename", item)
            self.assertNotIn("r2_key", item)
            self.assertNotIn("source_path", item)
            evidence = lookup(output, manifest["evidence_table"], f"{'a' * 24}:c000000")
            self.assertEqual(evidence["source"], {
                "report_id": "a" * 24,
                "public_url": f"/report.html?id={'a' * 24}",
            })

            persisted = b"".join(path.read_bytes() for path in sorted(output.iterdir()))
            self.assertNotIn(b"reports/private", persisted)
            self.assertNotIn(b"/private/mineru", persisted)
            self.assertNotIn(b"private-a.pdf", persisted)
            corpus = indexer.read_corpus(output / indexer.CORPUS_FILENAME)
            self.assertEqual(set(corpus), {"a" * 24, "b" * 24})
            for row in corpus.values():
                self.assertEqual(set(row), {"id", "item", "text"})
                self.assertEqual(set(row["item"]), indexer.CORPUS_ITEM_FIELDS)
                self.assertNotIn("filename", row["item"])
                self.assertNotIn("r2_key", row["item"])
                self.assertNotIn("source_path", row["item"])

    def test_reports_without_full_text_are_skipped(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output, manifest = self.build(Path(temporary))
            self.assertIsNone(lookup(output, manifest["item_table"], "c" * 24))
            self.assertNotIn("c" * 24, indexer.read_corpus(output / indexer.CORPUS_FILENAME))

    def test_fixed_slot_buckets_stay_within_range_read_limit(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output, manifest = self.build(Path(temporary))
            for name in ("token_table", "item_table", "evidence_table"):
                descriptor = manifest[name]
                table = output / Path(descriptor["table_key"]).name
                self.assertEqual(table.stat().st_size, descriptor["bucket_count"] * 12)
                self.assertEqual(descriptor["slot_size"], 12)
                self.assertLessEqual(descriptor["max_bucket_bytes"], 128 * 1024)

    def test_release_and_all_index_bytes_are_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            first_output, first_manifest = self.build(Path(first))
            second_output, second_manifest = self.build(Path(second))
            self.assertEqual(first_manifest, second_manifest)
            for filename in (
                "manifest.json",
                "tokens.tbl", "tokens.dat",
                "items.tbl", "items.dat",
                "evidence.tbl", "evidence.dat",
                indexer.CORPUS_FILENAME,
            ):
                self.assertEqual((first_output / filename).read_bytes(), (second_output / filename).read_bytes())

    def test_operational_metadata_does_not_duplicate_an_unchanged_release(self) -> None:
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            first_output, first_manifest = self.build(Path(first))
            catalog = self.catalog()
            catalog["updated_at_bjt"] = "2099-01-01 00:00:00 +0800"
            catalog["items"][0]["source_path"] = "/different/private/source.md"
            catalog["items"][0]["r2_key"] = "different-private-object-key"
            catalog["items"].append({
                "id": "d" * 24,
                "title": "New title-only catalog row",
                "filename": "private-d.pdf",
                "available": True,
            })
            search = self.search_index()
            search["updated_at_bjt"] = "2099-01-01 00:00:00 +0800"
            search["items"].append({"id": "d" * 24, "text": "new title-only catalog row"})
            second_output, second_manifest = self.build_payload(Path(second), catalog, search)
            self.assertEqual(first_manifest, second_manifest)
            for filename in (
                "manifest.json",
                "tokens.tbl", "tokens.dat",
                "items.tbl", "items.dat",
                "evidence.tbl", "evidence.dat",
                indexer.CORPUS_FILENAME,
            ):
                self.assertEqual((first_output / filename).read_bytes(), (second_output / filename).read_bytes())

    def test_previous_corpus_survives_a_partial_public_search_window(self) -> None:
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            first_output, _first_manifest = self.build(Path(first))
            previous = indexer.read_corpus(first_output / indexer.CORPUS_FILENAME)
            partial = self.search_index()
            refreshed_a = (
                "A refreshed full report now emphasizes solidstatefresh manufacturing economics, "
                "pilot-line throughput, conversion efficiency, supplier capacity, and commercial adoption. "
            ) * 4
            partial["items"] = [
                {"id": "a" * 24, "text": refreshed_a},
                {"id": "c" * 24, "text": "catalog title without extracted body 260826"},
            ]
            second_output, second_manifest = self.build_payload(
                Path(second),
                self.catalog(),
                partial,
                previous_corpus=previous,
            )
            merged = indexer.read_corpus(second_output / indexer.CORPUS_FILENAME)
            self.assertEqual(set(merged), {"a" * 24, "b" * 24})
            self.assertEqual(merged["a" * 24]["text"], indexer.body_text(refreshed_a))
            self.assertEqual(merged["b" * 24]["text"], previous["b" * 24]["text"])
            self.assertEqual(second_manifest["item_count"], 2)
            self.assertEqual(lookup(second_output, second_manifest["token_table"], "solidstatefresh")[0]["id"], "a" * 24)
            self.assertEqual(lookup(second_output, second_manifest["token_table"], "长时储能")[0]["id"], "b" * 24)

    def test_pruning_an_unchanged_body_does_not_change_the_release(self) -> None:
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            first_output, first_manifest = self.build(Path(first))
            previous = indexer.read_corpus(first_output / indexer.CORPUS_FILENAME)
            partial = self.search_index()
            partial["items"] = [partial["items"][0], partial["items"][2]]
            second_output, second_manifest = self.build_payload(
                Path(second),
                self.catalog(),
                partial,
                previous_corpus=previous,
            )
            self.assertEqual(first_manifest, second_manifest)
            for filename in (
                "manifest.json",
                "tokens.tbl", "tokens.dat",
                "items.tbl", "items.dat",
                "evidence.tbl", "evidence.dat",
                indexer.CORPUS_FILENAME,
            ):
                self.assertEqual((first_output / filename).read_bytes(), (second_output / filename).read_bytes())

    def test_manifest_is_committed_last_after_all_immutable_objects(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output, manifest = self.build(Path(temporary))
            client = FakeR2()
            indexer.publish_index(client, "private-bucket", output)
            manifest_key = "_report-research/v1/manifest.json"
            puts = [key for operation, key in client.operations if operation == "put"]
            self.assertEqual(puts[-1], manifest_key)
            self.assertIn(manifest["corpus"]["key"], puts[:-1])
            self.assertEqual(json.loads(client.objects[manifest_key]), manifest)

            client.operations.clear()
            indexer.publish_index(client, "private-bucket", output)
            immutable_puts = [key for operation, key in client.operations if operation == "put" and key != manifest_key]
            self.assertEqual(immutable_puts, [])

    def test_failed_immutable_upload_never_commits_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output, _manifest = self.build(Path(temporary))
            client = FakeR2(fail_key_suffix="evidence.dat")
            with self.assertRaisesRegex(RuntimeError, "injected"):
                indexer.publish_index(client, "private-bucket", output)
            self.assertNotIn("_report-research/v1/manifest.json", client.objects)

    def test_failed_corpus_upload_never_commits_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output, _manifest = self.build(Path(temporary))
            client = FakeR2(fail_key_suffix=indexer.CORPUS_FILENAME)
            with self.assertRaisesRegex(RuntimeError, "injected"):
                indexer.publish_index(client, "private-bucket", output)
            self.assertNotIn("_report-research/v1/manifest.json", client.objects)

    def test_missing_stable_manifest_is_a_clean_first_build(self) -> None:
        client = FakeR2()
        self.assertEqual(indexer.load_stable_corpus(client, "private-bucket"), {})
        self.assertFalse(any(operation == "put" for operation, _key in client.operations))

    def test_damaged_stable_corpus_fails_closed_and_keeps_old_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output, manifest = self.build(Path(temporary))
            client = FakeR2()
            indexer.publish_index(client, "private-bucket", output)
            manifest_key = "_report-research/v1/manifest.json"
            committed_manifest = client.objects[manifest_key]
            corpus_key = manifest["corpus"]["key"]
            client.objects[corpus_key] = b"damaged-gzip-payload"
            client.operations.clear()
            with self.assertRaisesRegex(indexer.CorpusError, "integrity verification"):
                indexer.load_stable_corpus(client, "private-bucket")
            self.assertEqual(client.objects[manifest_key], committed_manifest)
            self.assertFalse(any(operation == "put" for operation, _key in client.operations))

    def test_neutral_edge_transaction_does_not_publish_the_shared_manifest(self) -> None:
        workflow = SCRIPT.parent.parent.joinpath(".github/workflows/neutral-edge-cutover.yml").read_text(encoding="utf-8")
        self.assertNotIn("scripts/build_report_research_index.py", workflow)
        self.assertNotIn("_report-research/v1/manifest.json", workflow)


if __name__ == "__main__":
    unittest.main()
