#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import compare_portal_release_semantics as compare


def write_catalog(path: Path, *, title: str = "Report", seen: str = "2026-08-30") -> None:
    path.write_text(json.dumps({
        "schema_version": 1,
        "updated_at_bjt": seen,
        "item_count": 1,
        "items": [{
            "id": "a" * 16,
            "title": title,
            "last_seen_at_bjt": seen,
            "available": True,
        }],
    }), encoding="utf-8")


def write_sitemap(path: Path, *, lastmod: str = "2026-08-30", extra: bool = False) -> None:
    urls = [("https://example.com/", lastmod)]
    if extra:
        urls.append(("https://example.com/blog/new.html", lastmod))
    rows = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        *[f"<url><loc>{url}</loc><lastmod>{date}</lastmod></url>" for url, date in urls],
        "</urlset>",
    ]
    path.write_text("\n".join(rows), encoding="utf-8")


class PortalReleaseSemanticTests(unittest.TestCase):
    def fixture(self, directory: str) -> tuple[Path, Path, Path, Path]:
        root = Path(directory)
        paths = tuple(root / name for name in ("old.json", "new.json", "old.xml", "new.xml"))
        write_catalog(paths[0])
        write_catalog(paths[1])
        write_sitemap(paths[2])
        write_sitemap(paths[3])
        return paths  # type: ignore[return-value]

    def test_volatile_catalog_timestamps_are_a_noop(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            old_catalog, new_catalog, old_sitemap, new_sitemap = self.fixture(directory)
            write_catalog(new_catalog, seen="2026-08-31")
            result = compare.compare(old_catalog, new_catalog, old_sitemap, new_sitemap)
            self.assertFalse(result["changed"])
            self.assertFalse(result["catalog_changed"])

    def test_meaningful_catalog_change_requires_release(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            old_catalog, new_catalog, old_sitemap, new_sitemap = self.fixture(directory)
            write_catalog(new_catalog, title="Changed report")
            result = compare.compare(old_catalog, new_catalog, old_sitemap, new_sitemap)
            self.assertTrue(result["changed"])
            self.assertTrue(result["catalog_changed"])

    def test_new_or_updated_canonical_url_requires_release(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            old_catalog, new_catalog, old_sitemap, new_sitemap = self.fixture(directory)
            write_sitemap(new_sitemap, extra=True)
            result = compare.compare(old_catalog, new_catalog, old_sitemap, new_sitemap)
            self.assertTrue(result["changed"])
            self.assertTrue(result["sitemap_changed"])

    def test_duplicate_sitemap_url_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            old_catalog, new_catalog, old_sitemap, new_sitemap = self.fixture(directory)
            new_sitemap.write_text(
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
                '<url><loc>https://example.com/</loc></url>'
                '<url><loc>https://example.com/</loc></url>'
                '</urlset>',
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "duplicate"):
                compare.compare(old_catalog, new_catalog, old_sitemap, new_sitemap)


if __name__ == "__main__":
    unittest.main(verbosity=2)
