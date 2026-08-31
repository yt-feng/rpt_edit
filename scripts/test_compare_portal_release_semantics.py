#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import compare_portal_release_semantics as compare


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_catalog(path: Path, *, title: str = "Report", seen: str = "2026-08-30") -> None:
    write_json(path, {
        "schema_version": 1,
        "updated_at_bjt": seen,
        "item_count": 1,
        "items": [{
            "id": "a" * 16,
            "title": title,
            "last_seen_at_bjt": seen,
            "available": True,
        }],
    })


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
    def legacy_fixture(self, directory: str) -> tuple[Path, Path, Path, Path]:
        root = Path(directory)
        paths = tuple(root / name for name in ("old.json", "new.json", "old.xml", "new.xml"))
        write_catalog(paths[0])
        write_catalog(paths[1])
        write_sitemap(paths[2])
        write_sitemap(paths[3])
        return paths  # type: ignore[return-value]

    def release_fixture(self, directory: str) -> dict[str, object]:
        root = Path(directory)
        public = root / "public"
        site = root / "site"
        blog = root / "blog"
        contract = [root / "builder.py", root / "edge.js"]
        write_catalog(public / "data/catalog.json")
        write_json(public / "data/search_index.json", {
            "schema_version": 1,
            "updated_at_bjt": "2026-08-30",
            "item_count": 1,
            "items": [{"id": "a" * 16, "text": "alpha"}],
        })
        write_json(public / "data/chart_search_index.json", {
            "schema_version": 1,
            "updated_at_bjt": "2026-08-30",
            "reports": [{"report_id": "a" * 16, "search_text": "chart"}],
        })
        write_json(public / "data/password_rules.json", {"schema_version": 1, "default_group": "default"})
        write_json(public / "data/config.json", {"worker_base_url": "https://worker.example.com"})
        write_sitemap(public / "sitemap-baidu.xml")
        (public / "index.html").write_text("home", encoding="utf-8")
        write_json(blog / "20260830/article.json", {
            "title": "Article",
            "body": "Body",
            "updated_at_bjt": "2026-08-30",
        })
        (site / "assets").mkdir(parents=True)
        (site / "index.html").write_text("source home", encoding="utf-8")
        (site / "assets/app.js").write_text("console.log('app')", encoding="utf-8")
        for path, value in zip(contract, ("# builder", "export default {}"), strict=True):
            path.write_text(value, encoding="utf-8")
        return {
            "catalog": public / "data/catalog.json",
            "sitemap": public / "sitemap-baidu.xml",
            "search_index": public / "data/search_index.json",
            "chart_search_index": public / "data/chart_search_index.json",
            "password_rules": public / "data/password_rules.json",
            "runtime_config": public / "data/config.json",
            "blog_archive_root": blog,
            "site_source_root": site,
            "build_contract_paths": contract,
            "public_root": public,
        }

    def test_volatile_catalog_timestamps_are_a_noop(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            old_catalog, new_catalog, old_sitemap, new_sitemap = self.legacy_fixture(directory)
            write_catalog(new_catalog, seen="2026-08-31")
            result = compare.compare(old_catalog, new_catalog, old_sitemap, new_sitemap)
            self.assertFalse(result["changed"])
            self.assertFalse(result["catalog_changed"])

    def test_meaningful_catalog_change_requires_release(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            old_catalog, new_catalog, old_sitemap, new_sitemap = self.legacy_fixture(directory)
            write_catalog(new_catalog, title="Changed report")
            result = compare.compare(old_catalog, new_catalog, old_sitemap, new_sitemap)
            self.assertTrue(result["changed"])
            self.assertTrue(result["catalog_changed"])

    def test_manifest_ignores_volatile_json_and_sitemap_lastmod(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = self.release_fixture(directory)
            previous = compare.build_manifest(**fixture)
            write_catalog(fixture["catalog"], seen="2026-08-31")  # type: ignore[arg-type]
            search = fixture["search_index"]  # type: ignore[assignment]
            payload = json.loads(search.read_text(encoding="utf-8"))
            payload["updated_at_bjt"] = "2026-08-31"
            payload["text_storage_size_bytes"] = 999
            write_json(search, payload)
            write_sitemap(fixture["sitemap"], lastmod="2026-08-31")  # type: ignore[arg-type]
            current = compare.build_manifest(**fixture)
            result = compare.compare_manifests(previous, current)
            self.assertFalse(result["changed"])
            self.assertEqual(result["changed_components"], [])

    def test_manifest_covers_every_release_surface(self) -> None:
        cases = {
            "catalog": lambda f: write_catalog(f["catalog"], title="Changed"),
            "search_index": lambda f: write_json(f["search_index"], {"items": [{"id": "x", "text": "changed"}]}),
            "chart_search_index": lambda f: write_json(f["chart_search_index"], {"reports": [{"search_text": "changed"}]}),
            "password_rules": lambda f: write_json(f["password_rules"], {"default_group": "changed"}),
            "runtime_config": lambda f: write_json(f["runtime_config"], {"worker_base_url": "https://changed.example"}),
            "blog_archive": lambda f: write_json(f["blog_archive_root"] / "20260830/article.json", {"body": "changed"}),
            "materialized_site_source": lambda f: (f["site_source_root"] / "index.html").write_text("changed", encoding="utf-8"),
            "build_contract": lambda f: f["build_contract_paths"][0].write_text("changed", encoding="utf-8"),
            "public_paths": lambda f: (f["public_root"] / "new.html").write_text("new", encoding="utf-8"),
            "canonical_urls": lambda f: write_sitemap(f["sitemap"], extra=True),
        }
        for expected, mutate in cases.items():
            with self.subTest(component=expected), tempfile.TemporaryDirectory() as directory:
                fixture = self.release_fixture(directory)
                previous = compare.build_manifest(**fixture)
                mutate(fixture)
                current = compare.build_manifest(**fixture)
                result = compare.compare_manifests(previous, current)
                self.assertTrue(result["changed"])
                self.assertIn(expected, result["changed_components"])

    def test_manifest_self_file_does_not_change_public_paths(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            fixture = self.release_fixture(directory)
            previous = compare.build_manifest(**fixture)
            write_json(fixture["public_root"] / "data/release-semantics.json", previous)  # type: ignore[operator]
            current = compare.build_manifest(**fixture)
            self.assertFalse(compare.compare_manifests(previous, current)["changed"])

    def test_invalid_manifest_fails_closed(self) -> None:
        with self.assertRaisesRegex(ValueError, "digest"):
            compare.validate_manifest({
                "schema_version": 1,
                "normalizer_version": 1,
                "components": {key: "0" * 64 for key in compare.COMPONENT_KEYS},
                "semantic_sha256": "f" * 64,
            }, source="test")

    def test_duplicate_sitemap_url_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sitemap.xml"
            path.write_text(
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
                '<url><loc>https://example.com/</loc></url>'
                '<url><loc>https://example.com/</loc></url>'
                '</urlset>',
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "duplicate"):
                compare.sitemap_projection(path, include_lastmod=False)


if __name__ == "__main__":
    unittest.main(verbosity=2)
