#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import hashlib
import json
import sys
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "publish_course_materials",
    ROOT / "scripts" / "publish_course_materials.py",
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load course material publisher")
publisher = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = publisher
SPEC.loader.exec_module(publisher)


def fixture_manifest() -> dict:
    rows = []
    for index in range(1, 21):
        rows.append({
            "id": f"maifu-{index:02d}",
            "source_filename": f"material-{index:02d}.pdf",
            "title": f"Material {index:02d}",
            "topic": "Strategy",
            "summary": f"Course material summary {index:02d}",
            "pages": 37 if index < 20 else 43,
            "bytes": 1_000_000 if index < 20 else 2_902_439,
            "sha256": f"{index:064x}",
            "cover": f"assets/course-covers/maifu-{index:02d}.webp",
            "featured": index <= 6,
            "entities": [],
        })
    return {
        "schema_version": 1,
        "course": {
            "id": "str-01",
            "category": "战略咨询",
            "title": "麦府学堂｜战略与商业分析方法论",
        },
        "items": rows,
    }


class FakeNotFound(Exception):
    response = {
        "Error": {"Code": "NoSuchKey"},
        "ResponseMetadata": {"HTTPStatusCode": 404},
    }


class FakeR2:
    def __init__(self) -> None:
        self.objects: dict[str, dict] = {}
        self.calls: list[tuple[str, str]] = []

    def head_object(self, *, Bucket: str, Key: str) -> dict:
        self.calls.append(("head", Key))
        if Key not in self.objects:
            raise FakeNotFound()
        return self.objects[Key]

    def put_object(self, *, Bucket: str, Key: str, Body, ContentType: str, CacheControl: str, Metadata: dict) -> None:
        self.calls.append(("put", Key))
        body = Body.read() if hasattr(Body, "read") else bytes(Body)
        self.objects[Key] = {
            "ContentLength": len(body),
            "ContentType": ContentType,
            "CacheControl": CacheControl,
            "Metadata": dict(Metadata),
            "Body": body,
        }


class CourseMaterialPublisherTests(unittest.TestCase):
    def write_manifest(self, value: dict) -> Path:
        handle = tempfile.NamedTemporaryFile("w", suffix=".json", encoding="utf-8", delete=False)
        with handle:
            json.dump(value, handle, ensure_ascii=False)
        self.addCleanup(Path(handle.name).unlink, missing_ok=True)
        return Path(handle.name)

    def test_manifest_accepts_exact_twenty_item_release(self) -> None:
        course, rows = publisher.load_manifest(self.write_manifest(fixture_manifest()))
        self.assertEqual(course["id"], "str-01")
        self.assertEqual(len(rows), 20)
        self.assertEqual(sum(row.pages for row in rows), 746)
        self.assertEqual(sum(row.size for row in rows), 21_902_439)
        self.assertEqual(sum(row.featured for row in rows), 6)

    def test_manifest_fails_closed_on_missing_or_extra_fields_and_wrong_totals(self) -> None:
        cases = []
        missing = fixture_manifest()
        missing["items"][0].pop("summary")
        cases.append(missing)
        extra = fixture_manifest()
        extra["items"][0]["object_key"] = "private/key.pdf"
        cases.append(extra)
        wrong_total = fixture_manifest()
        wrong_total["items"][0]["pages"] += 1
        cases.append(wrong_total)
        wrong_order = fixture_manifest()
        wrong_order["items"][0]["id"] = "maifu-20"
        cases.append(wrong_order)
        for value in cases:
            with self.subTest(value=value["items"][0]):
                with self.assertRaises(publisher.PublishError):
                    publisher.load_manifest(self.write_manifest(value))

    def test_webdav_url_encodes_every_private_path_segment(self) -> None:
        url = publisher._webdav_url(
            "https://dav.example.invalid/root",
            "/Fund/Jade Ocean/E02 投资&战略 KM/麦府学堂/",
            "【麦肯锡系列】测试.pdf",
        )
        self.assertEqual(
            url,
            "https://dav.example.invalid/root/Fund/Jade%20Ocean/"
            "E02%20%E6%8A%95%E8%B5%84%26%E6%88%98%E7%95%A5%20KM/"
            "%E9%BA%A6%E5%BA%9C%E5%AD%A6%E5%A0%82/"
            "%E3%80%90%E9%BA%A6%E8%82%AF%E9%94%A1%E7%B3%BB%E5%88%97%E3%80%91%E6%B5%8B%E8%AF%95.pdf",
        )
        with self.assertRaises(publisher.PublishError):
            publisher._webdav_url("http://dav.example.invalid", "/private", "x.pdf")
        with self.assertRaises(publisher.PublishError):
            publisher._webdav_url("https://dav.example.invalid", "/private/../other", "x.pdf")

    def test_publish_is_idempotent_and_never_lists_or_deletes(self) -> None:
        material = publisher.Material(
            id="maifu-01",
            source_filename="one.pdf",
            title="One",
            topic="Strategy",
            summary="Summary",
            pages=1,
            size=8,
            sha256="1" * 64,
            cover="assets/course-covers/maifu-01.webp",
            featured=True,
            entities=(),
        )
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "one.pdf"
            path.write_bytes(b"12345678")
            client = FakeR2()
            self.assertTrue(publisher.publish_material(client, "bucket", path, material, "release"))
            self.assertFalse(publisher.publish_material(client, "bucket", path, material, "release"))
        self.assertEqual([call[0] for call in client.calls].count("put"), 1)
        self.assertFalse(hasattr(client, "delete_object"))
        self.assertFalse(hasattr(client, "list_objects_v2"))

    def test_private_manifest_omits_source_names_and_object_keys(self) -> None:
        course, rows = publisher.load_manifest(self.write_manifest(fixture_manifest()))
        payload = publisher.private_manifest(course, rows)
        text = payload.decode("utf-8")
        self.assertNotIn("source_filename", text)
        self.assertNotIn("object_key", text)
        parsed = json.loads(text)
        self.assertEqual(parsed["item_count"], 20)
        self.assertEqual(parsed["total_pages"], 746)
        self.assertEqual(parsed["total_bytes"], 21_902_439)

    def test_all_sources_are_verified_before_the_first_r2_write(self) -> None:
        materials = tuple(
            publisher.Material(
                id=f"maifu-{index:02d}",
                source_filename=f"material-{index:02d}.pdf",
                title=f"Material {index:02d}",
                topic="Strategy",
                summary="Summary",
                pages=1,
                size=8,
                sha256="",
                cover=f"assets/course-covers/maifu-{index:02d}.webp",
                featured=index == 1,
                entities=(),
            )
            for index in range(1, 3)
        )
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            finalized = []
            for material in materials:
                data = material.id.encode("ascii")[:8].ljust(8, b"0")
                (root / material.source_filename).write_bytes(data)
                finalized.append(publisher.Material(
                    **{**material.__dict__, "sha256": hashlib.sha256(data).hexdigest()}
                ))
            with (
                patch.object(publisher, "load_manifest", return_value=({"id": "str-01"}, tuple(finalized))),
                patch.object(publisher, "build_r2_client", return_value=FakeR2()),
                patch.object(
                    publisher,
                    "verify_pdf",
                    side_effect=[None, publisher.PublishError("second PDF invalid")],
                ),
                patch.object(publisher, "publish_material") as publish,
                patch.dict(publisher.os.environ, {"R2_BUCKET": "bucket"}),
            ):
                with self.assertRaises(publisher.PublishError):
                    publisher.run(Namespace(manifest="ignored", source_dir=str(root), dry_run=False))
            publish.assert_not_called()

    def test_private_manifest_head_verifies_release_and_digest(self) -> None:
        client = FakeR2()
        body = b'{"schema_version":1}\n'
        release = "a" * 64
        client.put_object(
            Bucket="bucket",
            Key=publisher.MANIFEST_OBJECT_KEY,
            Body=body,
            ContentType="application/json; charset=utf-8",
            CacheControl="private, no-store",
            Metadata={"release": release, "sha256": hashlib.sha256(body).hexdigest()},
        )
        self.assertTrue(publisher.matching_private_manifest_head(client, "bucket", body, release))
        client.objects[publisher.MANIFEST_OBJECT_KEY]["Metadata"]["release"] = "wrong"
        self.assertFalse(publisher.matching_private_manifest_head(client, "bucket", body, release))

    def test_workflow_keeps_source_path_secret_and_runs_local_contract_tests(self) -> None:
        workflow = (ROOT / ".github" / "workflows" / "course-materials-private-publish.yml").read_text(
            encoding="utf-8"
        )
        self.assertIn("secrets.COURSE_MAIFU_WEBDAV_PATH", workflow)
        self.assertIn("scripts/test_publish_course_materials.py", workflow)
        self.assertIn("scripts/publish_course_materials.py", workflow)
        self.assertIn("portal_suite/site_src/data/course-materials.json", workflow)
        self.assertNotIn("Jade Ocean", workflow)
        self.assertNotIn("delete_object", workflow)


if __name__ == "__main__":
    unittest.main()
