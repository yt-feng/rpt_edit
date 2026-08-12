#!/usr/bin/env python3
from __future__ import annotations

import stat
import struct
import tempfile
import unittest
import zipfile
import zlib
from pathlib import Path
from unittest.mock import patch

import materialize_shard_artifacts as materializer
from materialize_shard_artifacts import materialize


class MaterializeShardArtifactsTests(unittest.TestCase):
    def write_publish_ready_zip(self, path: Path, members: dict[str, bytes | str]) -> None:
        with zipfile.ZipFile(
            path,
            "w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=6,
        ) as archive:
            for name, value in members.items():
                archive.writestr(name, value)

    def test_materializes_and_validates_downloaded_shards(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            artifacts = root / "artifacts"
            (artifacts / "unrelated-directory").mkdir(parents=True)
            for shard in range(2):
                for report in range(2):
                    report_dir = artifacts / f"final-dropbox-macro-shard-260801-{shard}" / f"report-{shard}-{report}"
                    report_dir.mkdir(parents=True)
                    (report_dir / "wechat_article.md").write_text("article", encoding="utf-8")

            destination = root / "xhs_notes" / "dropbox" / "260801"
            shard_count, report_count = materialize(artifacts, destination, 2, 4)

            self.assertEqual(2, shard_count)
            self.assertEqual(4, report_count)
            self.assertTrue((destination / "shard_0" / "report-0-0" / "wechat_article.md").exists())
            self.assertTrue((destination / "shard_1" / "report-1-1" / "wechat_article.md").exists())

    def test_rejects_unexpected_report_count(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            report_dir = root / "artifacts" / "shard-0" / "report"
            report_dir.mkdir(parents=True)
            (report_dir / "note.md").write_text("note", encoding="utf-8")
            with self.assertRaisesRegex(RuntimeError, "Expected 2 reports"):
                materialize(root / "artifacts", root / "destination", 1, 2)

    def test_merges_split_publish_ready_zips_by_report_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            artifact = root / "artifacts" / "publish-ready-260811-31558231750"
            artifact.mkdir(parents=True)
            part_one = artifact / "publish_ready_260811_part001.zip"
            self.write_publish_ready_zip(part_one, {
                "260811/shard_0/Morgan Stanley AI/note.txt": "# AI report",
                "260811/shard_0/Morgan Stanley AI/assets/source_image_001.png": b"\x89PNG\r\n\x1a\nfirst",
                "260811/shard_1/JPMorgan Power/wechat_article.txt": "# Power",
            })
            part_two = artifact / "publish_ready_260811_part002.zip"
            self.write_publish_ready_zip(part_two, {
                "260811/shard_0/Morgan Stanley AI/assets/source_image_002.jpg": b"\xff\xd8\xffsecond",
                "260811/shard_1/JPMorgan Power/assets/source_image_003.webp": b"RIFF\x08\x00\x00\x00WEBPthird",
            })

            destination = root / "xhs_notes" / "dropbox" / "260811"
            shard_count, report_count = materialize(
                root / "artifacts",
                destination,
                2,
                2,
                expected_date="260811",
                require_images=True,
            )

            self.assertEqual((2, 2), (shard_count, report_count))
            self.assertTrue((destination / "shard_0/Morgan Stanley AI/note.md").is_file())
            self.assertTrue(
                (destination / "shard_0/Morgan Stanley AI/assets/source_image_001.png").is_file()
            )
            self.assertTrue(
                (destination / "shard_0/Morgan Stanley AI/assets/source_image_002.jpg").is_file()
            )
            self.assertTrue(
                (destination / "shard_1/JPMorgan Power/wechat_article.md").is_file()
            )
            self.assertTrue(
                (destination / "shard_1/JPMorgan Power/assets/source_image_003.webp").is_file()
            )

    def test_rejects_publish_ready_zip_traversal_without_writing_outside_destination(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            artifact = root / "artifacts"
            artifact.mkdir()
            with zipfile.ZipFile(artifact / "publish_ready_260811.zip", "w") as archive:
                archive.writestr("../../escaped.txt", "escape")

            with self.assertRaisesRegex(RuntimeError, "Unsafe ZIP member path"):
                materialize(
                    artifact,
                    root / "output" / "260811",
                    expected_date="260811",
                    require_images=True,
                )
            self.assertFalse((root / "escaped.txt").exists())

    def test_rejects_publish_ready_zip_symlink(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            artifact = root / "artifacts"
            artifact.mkdir()
            link = zipfile.ZipInfo("260811/shard_0/report/assets/source_image_001.png")
            link.create_system = 3
            link.external_attr = (stat.S_IFLNK | 0o777) << 16
            with zipfile.ZipFile(artifact / "publish_ready_260811.zip", "w") as archive:
                archive.writestr(link, "../../outside")

            with self.assertRaisesRegex(RuntimeError, "Unsupported ZIP member type"):
                materialize(
                    artifact,
                    root / "output" / "260811",
                    expected_date="260811",
                    require_images=True,
                )

    def test_rejects_publish_ready_zip_from_another_date(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            artifact = root / "artifacts"
            artifact.mkdir()
            with zipfile.ZipFile(artifact / "publish_ready_260810.zip", "w") as archive:
                archive.writestr("260810/shard_0/report/note.txt", "note")
                archive.writestr(
                    "260810/shard_0/report/assets/source_image_001.png",
                    b"\x89PNG\r\n\x1a\nimage",
                )
            with self.assertRaisesRegex(RuntimeError, "does not match expected date"):
                materialize(
                    artifact,
                    root / "output" / "260811",
                    expected_date="260811",
                    require_images=True,
                )

    def test_rejects_duplicate_gap_and_mixed_publish_ready_parts(self) -> None:
        scenarios = {
            "duplicate": ["a/publish_ready_260811_part001.zip", "b/publish_ready_260811_part001.zip"],
            "gap": ["publish_ready_260811_part001.zip", "publish_ready_260811_part003.zip"],
            "mixed": ["publish_ready_260811.zip", "publish_ready_260811_part001.zip"],
            "not-padded": ["publish_ready_260811_part1.zip"],
        }
        for label, relative_paths in scenarios.items():
            with self.subTest(label=label), tempfile.TemporaryDirectory() as temp_dir:
                root = Path(temp_dir)
                artifact = root / "artifacts"
                for ordinal, relative_path in enumerate(relative_paths):
                    path = artifact / relative_path
                    path.parent.mkdir(parents=True, exist_ok=True)
                    self.write_publish_ready_zip(path, {
                        f"260811/shard_0/report-{ordinal}/note.txt": "note",
                        f"260811/shard_0/report-{ordinal}/assets/source_image_001.png": b"\x89PNG\r\n\x1a\nimage",
                    })
                with self.assertRaisesRegex(RuntimeError, "publish-ready ZIP|Publish-ready ZIP"):
                    materialize(
                        artifact,
                        root / "output" / "260811",
                        expected_date="260811",
                        require_images=True,
                    )

    def test_accepts_report_with_restored_zhihu_marker(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            artifact = root / "artifacts"
            artifact.mkdir()
            self.write_publish_ready_zip(artifact / "publish_ready_260811.zip", {
                "260811/shard_0/report/zhihu_article.txt": "article",
                "260811/shard_0/report/assets/source_image_001.png": b"\x89PNG\r\n\x1a\nimage",
            })
            self.assertEqual(
                (1, 1),
                materialize(
                    artifact,
                    root / "output" / "260811",
                    1,
                    1,
                    expected_date="260811",
                    require_images=True,
                ),
            )
            self.assertTrue((root / "output/260811/shard_0/report/zhihu_article.md").is_file())

    def test_rejects_non_deflate_and_unsafe_compression_ratio(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            artifact = root / "artifacts"
            artifact.mkdir()
            with zipfile.ZipFile(
                artifact / "publish_ready_260811.zip",
                "w",
                compression=zipfile.ZIP_BZIP2,
            ) as archive:
                archive.writestr("260811/shard_0/report/note.txt", "note")
            with self.assertRaisesRegex(RuntimeError, "Unsupported ZIP compression method"):
                materialize(artifact, root / "output/260811", expected_date="260811")

        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            artifact = root / "artifacts"
            artifact.mkdir()
            image = b"\x89PNG\r\n\x1a\n" + b"\0" * (10 * 1024 * 1024 - 8)
            self.write_publish_ready_zip(artifact / "publish_ready_260811.zip", {
                "260811/shard_0/report/note.txt": "note",
                "260811/shard_0/report/assets/source_image_001.png": image,
            })
            with self.assertRaisesRegex(RuntimeError, "unsafe compression ratio"):
                materialize(
                    artifact,
                    root / "output/260811",
                    expected_date="260811",
                    require_images=True,
                )

    def test_rejects_forged_central_size_before_decompression(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            artifact = root / "artifacts"
            artifact.mkdir()
            archive_path = artifact / "publish_ready_260811.zip"
            image_name = b"260811/shard_0/report/assets/source_image_001.png"
            self.write_publish_ready_zip(archive_path, {
                "260811/shard_0/report/note.txt": "note",
                image_name.decode(): b"\x89PNG\r\n\x1a\n" + b"A" * (1024 * 1024),
            })
            payload = bytearray(archive_path.read_bytes())
            forged_size = 12
            forged_crc = zlib.crc32(b"\x89PNG\r\n\x1a\n" + b"A" * 4)
            with zipfile.ZipFile(archive_path, "r") as archive:
                image_info = next(info for info in archive.infolist() if info.filename == image_name.decode())
                local_offset = image_info.header_offset
            struct.pack_into("<I", payload, local_offset + 14, forged_crc)
            struct.pack_into("<I", payload, local_offset + 22, forged_size)
            offset = 0
            patched = False
            while True:
                offset = payload.find(b"PK\x01\x02", offset)
                if offset < 0:
                    break
                filename_size = struct.unpack_from("<H", payload, offset + 28)[0]
                filename = bytes(payload[offset + 46 : offset + 46 + filename_size])
                if filename == image_name:
                    struct.pack_into("<I", payload, offset + 16, forged_crc)
                    struct.pack_into("<I", payload, offset + 24, forged_size)
                    patched = True
                    break
                offset += 4
            self.assertTrue(patched)
            archive_path.write_bytes(payload)

            with self.assertRaisesRegex(RuntimeError, "decompressed size exceeds"):
                materialize(
                    artifact,
                    root / "output/260811",
                    expected_date="260811",
                    require_images=True,
                )

    def test_directory_entries_count_toward_archive_limit(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            artifact = root / "artifacts"
            artifact.mkdir()
            self.write_publish_ready_zip(artifact / "publish_ready_260811.zip", {
                "260811/shard_0/report/": b"",
                "260811/shard_0/report/note.txt": "note",
            })
            with patch.object(materializer, "MAX_ZIP_ENTRIES", 1):
                with self.assertRaisesRegex(RuntimeError, "exceeds safe extraction limits"):
                    materialize(artifact, root / "output/260811", expected_date="260811")


if __name__ == "__main__":
    unittest.main()
