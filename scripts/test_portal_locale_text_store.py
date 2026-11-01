#!/usr/bin/env python3
"""Bounded HTML retention and unchanged locale publication behavior."""
from __future__ import annotations

from contextlib import ExitStack
import gc
import gzip
import json
from pathlib import Path
import tempfile
import tracemalloc
import unittest
from unittest import mock

import build_portal_locales as builder
from portal_locale_text_store import FileTextMapping, StagedTextMapping
import test_build_portal_locales as fixtures
import test_portal_locale_incremental as incremental_fixtures


class TextStoreTests(unittest.TestCase):
    def test_archive_bodies_are_not_retained_during_read_transform_and_staging(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            paths = [root / f"{index}.html" for index in range(48)]
            # A 24 MiB archive must not consume another archive-sized heap for
            # either the source mapping or its pending Chinese updates.
            body = "<html><body>" + "x" * (512 * 1024) + "</body></html>"
            for path in paths:
                path.write_text(body, encoding="utf-8")
            del body
            gc.collect()
            tracemalloc.start()
            try:
                sources = FileTextMapping(paths)
                staged = StagedTextMapping(root / "staged")
                for path, source in sources.items():
                    staged[path] = source.replace("<html>", '<html lang="zh-Hans">')
                del source
                gc.collect()
                retained, peak = tracemalloc.get_traced_memory()
            finally:
                tracemalloc.stop()
            self.assertLess(retained, 1024 * 1024)
            self.assertLess(peak, 4 * 1024 * 1024)
            self.assertEqual(list(staged), paths)
            self.assertTrue(staged[paths[-1]].startswith('<html lang="zh-Hans">'))
            self.assertTrue(paths[-1].read_text().startswith("<html>"))

    def test_staging_replacement_order_and_failed_write_preserve_accepted_stage(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            first, second = root / "first.html", root / "second.html"
            staged = StagedTextMapping(root / "staged")
            staged[first] = "第一版\n"
            staged[second] = "الثانية\n"
            staged[first] = "修订版\n"
            self.assertEqual(list(staged), [first, second])
            self.assertEqual(staged[first], "修订版\n")
            with mock.patch.object(Path, "replace", side_effect=OSError("disk write failed")):
                with self.assertRaisesRegex(OSError, "disk write failed"):
                    staged[first] = "incomplete replacement"
            self.assertEqual(staged[first], "修订版\n")
            self.assertFalse(first.exists())
            del staged[first]
            self.assertEqual(list(staged), [second])

    def test_disk_staged_discovery_rolls_back_exact_originals_on_commit_failure(self):
        fixture = fixtures.PortalLocaleBuildTests()
        fixture.setUp()
        try:
            page = fixture.site / "index.html"
            original = page.read_bytes().replace(b"\n", b"\r\n")
            page.write_bytes(original)
            robots = fixture.site / "robots.txt"
            robots.unlink()
            sitemap = (fixture.site / "sitemap.xml").read_bytes()
            staged = StagedTextMapping(fixture.temporary_root / "staged-discovery")
            staged[page] = "pending transformed page"

            def interrupt_after_write(root, site_url):
                (root / "robots.txt").write_text("partial mutation")
                raise KeyboardInterrupt()

            with mock.patch.object(builder, "update_robots", side_effect=interrupt_after_write):
                with self.assertRaises(KeyboardInterrupt):
                    builder.commit_chinese_discovery(fixture.site, staged, fixtures.SITE_URL, "2026-09-30")
            self.assertEqual(page.read_bytes(), original)
            self.assertEqual((fixture.site / "sitemap.xml").read_bytes(), sitemap)
            self.assertFalse(robots.exists())
        finally:
            fixture.tearDown()


class LocaleStorageEquivalenceTests(unittest.TestCase):
    def _build(self, scope, *, eager):
        fixture = incremental_fixtures.IncrementalBuildTests()
        fixture.setUp()
        try:
            kwargs = {"translation_scope": scope, "workers": 1}
            if scope == "incremental":
                kwargs["index_start_date"] = "2026-09-05"
            elif scope == "month":
                kwargs.update(index_start_date="2026-09-05", history_start_date="2026-08-05",
                              history_release_date="2026-09-05", history_daily_limit=1)
            with ExitStack() as stack:
                if eager:
                    stack.enter_context(mock.patch.object(
                        builder, "FileTextMapping", side_effect=lambda paths: {
                            path: path.read_text(encoding="utf-8") for path in paths
                        },
                    ))
                    stack.enter_context(mock.patch.object(builder, "StagedTextMapping", side_effect=lambda _: {}))
                fixture.fixture._build(fixtures.RecordingTranslator(), **kwargs)
            tree = {path.relative_to(fixture.site).as_posix(): path.read_bytes()
                    for path in fixture.site.rglob("*") if path.is_file()}
            with gzip.open(fixture.fixture.cache, "rt") as handle:
                cache = json.load(handle)
            return tree, cache
        finally:
            fixture.tearDown()

    def test_release_month_and_incremental_outputs_match_eager_storage_exactly(self):
        for scope in ("release", "month", "incremental"):
            with self.subTest(scope=scope):
                self.assertEqual(self._build(scope, eager=False), self._build(scope, eager=True))

    def test_temporary_html_workspace_is_removed_after_failure(self):
        fixture = fixtures.PortalLocaleBuildTests()
        fixture.setUp()
        workspace = []
        original = builder._build_localized_release

        def record_workspace(**kwargs):
            workspace.append(kwargs["html_workspace"])
            return original(**kwargs)

        try:
            before = {path: path.read_bytes() for path in fixture.site.rglob("*.html")}
            with mock.patch.object(builder, "_build_localized_release", side_effect=record_workspace), \
                    mock.patch.object(builder, "write_locale_manifest", side_effect=OSError("manifest failed")):
                with self.assertRaisesRegex(OSError, "manifest failed"):
                    fixture._build(fixtures.RecordingTranslator())
            self.assertEqual(len(workspace), 1)
            self.assertFalse(workspace[0].exists())
            self.assertEqual(before, {path: path.read_bytes() for path in before})
        finally:
            fixture.tearDown()


if __name__ == "__main__":
    unittest.main()
