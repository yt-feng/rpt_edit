#!/usr/bin/env python3
import hashlib
from pathlib import Path
import re
import tempfile
import unittest
from urllib.parse import parse_qs, urljoin, urlsplit

import build_portal_locales as locales
from build_portal_suite_site import version_assets
from portal_lazy_assets import fingerprint_newsfeed_loader

SOURCE_ASSETS = Path(__file__).resolve().parents[1] / "portal_suite/site_src/assets"


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

    def test_missing_module_fails_before_publication(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "assets").mkdir()
            (root / "assets/app.js").write_text('const NEWSFEED_APP_ASSET = "assets/newsfeed-app.js?v=missing";')
            with self.assertRaisesRegex(ValueError, "present together"):
                fingerprint_newsfeed_loader(root)


if __name__ == "__main__":
    unittest.main()
