#!/usr/bin/env python3
import hashlib
from pathlib import Path
import re
import tempfile
import unittest
from urllib.parse import parse_qs, urljoin, urlsplit

import build_portal_locales as locales
from build_portal_suite_site import version_assets
from portal_lazy_assets import fingerprint_newsfeed_loader, fingerprint_reader_loaders

SOURCE_ASSETS = Path(__file__).resolve().parents[1] / "portal_suite/site_src/assets"
READER_ASSETS = {
    "app.js": ("report-discussion.js", "report-discussion.css", "download-invitation.js", "download-invitation.css"),
    "site-runtime.js": ("site-feedback.js", "site-feedback.css"),
}


class LazyAssetTests(unittest.TestCase):
    def test_module_only_change_updates_loader_and_its_hash(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "assets").mkdir()
            app, module = root / "assets/app.js", root / "assets/newsfeed-app.js"
            app.write_text('const NEWSFEED_APP_ASSET = "assets/newsfeed-app.js?v=__NEWSFEED_APP_SHA__";')
            versions = []
            for content in ("first module", "updated module"):
                module.write_text(content)
                fingerprint_newsfeed_loader(root)
                self.assertIn(hashlib.sha256(content.encode()).hexdigest()[:12], app.read_text())
                versions.append(app.read_bytes())
                fingerprint_newsfeed_loader(root)
                self.assertEqual(app.read_bytes(), versions[-1])
            self.assertNotEqual(*versions)

    def test_real_version_assets_updates_html_when_only_newsfeed_module_changes(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "assets").mkdir()
            app = root / "assets/app.js"
            module = root / "assets/newsfeed-app.js"
            page = root / "newsfeed.html"
            app.write_bytes((SOURCE_ASSETS / "app.js").read_bytes())
            for asset in READER_ASSETS["app.js"]:
                (root / "assets" / asset).write_bytes((SOURCE_ASSETS / asset).read_bytes())
            module.write_bytes((SOURCE_ASSETS / "newsfeed-app.js").read_bytes())
            page.write_text('<html><body><script src="assets/app.js?v=old"></script></body></html>')
            versions = []
            for revision in ("", "\n// Module-only revision\n"):
                # Keep app.js and HTML from the preceding build. Only child
                # content changes; the production entrypoint owns both hashes.
                if revision:
                    module.write_text(module.read_text() + revision)
                version_assets(root)
                child_digest = hashlib.sha256(module.read_bytes()).hexdigest()[:12]
                self.assertIn(f'assets/newsfeed-app.js?v={child_digest}";', app.read_text())
                app_digest = hashlib.sha1(app.read_bytes()).hexdigest()[:8]
                self.assertIn(f'src="assets/app.js?v={app_digest}"', page.read_text())
                self.assertNotIn("__NEWSFEED_APP_SHA__", app.read_text())
                versions.append((app.read_bytes(), page.read_bytes()))
                version_assets(root)
                self.assertEqual((app.read_bytes(), page.read_bytes()), versions[-1])
            self.assertNotEqual(versions[0][0], versions[1][0])
            self.assertNotEqual(versions[0][1], versions[1][1])

    def test_locale_module_gets_its_own_digest(self):
        # Use the real loader and entire child through the actual locale JS
        # renderer, then check the loader -> app -> HTML fingerprint chain.
        original_app = (SOURCE_ASSETS / "app.js").read_text()
        loader_start = original_app.index("  const NEWSFEED_APP_ASSET =")
        loader_end = original_app.index("  async function initDelivery(", loader_start)
        sources = {
            "app.js": original_app[loader_start:loader_end],
            "newsfeed-app.js": (SOURCE_ASSETS / "newsfeed-app.js").read_text(),
        }
        units = {}
        for asset, source in sources.items():
            locales.collect_javascript_units(source, asset, units)
        cache = locales.empty_cache()
        for locale, copy in {"ko": "금융 뉴스", "ja": "金融ニュース", "ar": "الأخبار المالية"}.items():
            for unit in units.values():
                translated = " ".join([copy, *locales.PLACEHOLDER_RE.findall(unit.source)])
                cache["locales"][locale][unit.key] = locales._translation_cache_row(unit, translated)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            outputs = []
            child_versions = []
            for locale in ("ko", "ja", "ar"):
                local = root / locale
                (local / "assets").mkdir(parents=True)
                for asset, source in sources.items():
                    (local / "assets" / asset).write_text(locales.render_localized_javascript(source, asset, locale, cache))
                fingerprint_newsfeed_loader(local)
                app = (local / "assets/app.js").read_text()
                module = local / "assets/newsfeed-app.js"
                child_digest = hashlib.sha256(module.read_bytes()).hexdigest()[:12]
                child_url = re.search(r'const NEWSFEED_APP_ASSET = "([^"]+)";', app).group(1)
                self.assertEqual(child_url, f"assets/newsfeed-app.js?v={child_digest}")
                self.assertEqual(urlsplit(urljoin(f"https://portal.example.invalid/{locale}/newsfeed.html", child_url)).path,
                                 f"/{locale}/assets/newsfeed-app.js")
                app_digest = hashlib.sha256((local / "assets/app.js").read_bytes()).hexdigest()[:12]
                html = locales.render_localized_html(
                    '<html><body><script src="assets/app.js?v=root-version"></script></body></html>',
                    locale=locale, cache=cache, site_url="https://portal.example.invalid", discovery_markup="",
                    script_asset_digests={"app.js": app_digest},
                )
                script_url = re.search(r'<script src="([^"]+)"', html).group(1)
                self.assertEqual(urlsplit(urljoin(f"https://portal.example.invalid/{locale}/newsfeed.html", script_url)).path,
                                 f"/{locale}/assets/app.js")
                self.assertEqual(parse_qs(urlsplit(script_url).query), {"v": [app_digest]})
                outputs.append(app_digest)
                child_versions.append(child_digest)
            self.assertEqual(len(set(outputs)), 3)
            self.assertEqual(len(set(child_versions)), 3)

    def test_reader_javascript_and_css_changes_invalidate_loader_and_html(self):
        # Exercise every lazy dependency through the production fingerprint
        # chain. CSS-only changes must invalidate the loader just like JS.
        for loader_name, assets in READER_ASSETS.items():
            for changed_asset in assets:
                with self.subTest(loader=loader_name, changed=changed_asset), tempfile.TemporaryDirectory() as temporary:
                    root = Path(temporary)
                    (root / "assets").mkdir()
                    loader = root / "assets" / loader_name
                    loader.write_text("\n".join(f'load("/assets/{name}?v=old");' for name in assets))
                    page = root / "report.html"
                    page.write_text(f'<script src="assets/{loader_name}?v=old"></script>')
                    for name in assets:
                        (root / "assets" / name).write_text(f"Initial content for {name}")
                    version_assets(root)
                    original_loader, original_page = loader.read_bytes(), page.read_bytes()
                    unchanged_hashes = {name: hashlib.sha256((root / "assets" / name).read_bytes()).hexdigest()[:12] for name in assets}
                    child = root / "assets" / changed_asset
                    child.write_text(child.read_text() + "\n/* Child-only revision */\n")
                    version_assets(root)
                    child_digest = hashlib.sha256(child.read_bytes()).hexdigest()[:12]
                    self.assertIn(f"{changed_asset}?v={child_digest}", loader.read_text())
                    self.assertNotEqual(original_loader, loader.read_bytes())
                    self.assertNotEqual(original_page, page.read_bytes())
                    loader_digest = hashlib.sha1(loader.read_bytes()).hexdigest()[:8]
                    self.assertIn(f'assets/{loader_name}?v={loader_digest}', page.read_text())
                    for name in assets:
                        if name != changed_asset:
                            self.assertIn(f"{name}?v={unchanged_hashes[name]}", loader.read_text())
                    completed = loader.read_bytes(), page.read_bytes()
                    version_assets(root)
                    self.assertEqual(completed, (loader.read_bytes(), page.read_bytes()))

    def test_each_referenced_reader_dependency_is_required(self):
        for loader_name, assets in READER_ASSETS.items():
            for missing in assets:
                with self.subTest(loader=loader_name, missing=missing), tempfile.TemporaryDirectory() as temporary:
                    root = Path(temporary)
                    (root / "assets").mkdir()
                    (root / "assets" / loader_name).write_text("\n".join(f'load("/assets/{name}?v=old");' for name in assets))
                    for name in assets:
                        if name != missing:
                            (root / "assets" / name).write_text("Available dependency")
                    with self.assertRaisesRegex(ValueError, re.escape(f"Reader asset is missing: {missing}")):
                        fingerprint_reader_loaders(root)

    def test_legacy_pages_without_reader_loaders_need_no_reader_assets(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            # A page without assets and an older ordinary app both stay valid.
            fingerprint_reader_loaders(root)
            (root / "assets").mkdir()
            app = root / "assets/app.js"
            app.write_text('const legacyApplication = "no lazy reader modules";')
            runtime = root / "assets/site-runtime.js"
            runtime.write_text('const clockOnlyRuntime = true;')
            originals = app.read_bytes(), runtime.read_bytes()
            page = root / "index.html"
            page.write_text('<script src="assets/app.js"></script><script src="assets/site-runtime.js"></script>')
            version_assets(root)
            self.assertEqual(originals, (app.read_bytes(), runtime.read_bytes()))
            for loader in (app, runtime):
                digest = hashlib.sha1(loader.read_bytes()).hexdigest()[:8]
                self.assertIn(f'assets/{loader.name}?v={digest}', page.read_text())

    def test_missing_module_fails_before_publication(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "assets").mkdir()
            (root / "assets/app.js").write_text('const NEWSFEED_APP_ASSET = "assets/newsfeed-app.js?v=missing";')
            with self.assertRaisesRegex(ValueError, "present together"):
                fingerprint_newsfeed_loader(root)


if __name__ == "__main__":
    unittest.main()
