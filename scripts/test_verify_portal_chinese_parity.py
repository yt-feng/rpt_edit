#!/usr/bin/env python3
"""Regression tests for the Simplified-Chinese parity gate."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import verify_portal_chinese_parity as parity  # noqa: E402


ORIGIN = "https://portal.example.invalid"
ASSET_VERSION = "0123456789ab"
BOOTSTRAP = (
    '<script data-kc-locale-bootstrap>(function(){'
    'var n=navigator,l=String(n.language||n.languages&&n.languages[0]||"").toLowerCase();'
    'if(l==="zh"||/^zh-(?:cn|sg|hans)(?:-|$)/.test(l))return;'
    'var h=document.head,c=document.createElement("link"),s=document.createElement("script");'
    f'c.rel="stylesheet";c.href="/assets/locale.css?v={ASSET_VERSION}";'
    f's.src="/assets/locale-runtime.js?v={ASSET_VERSION}";s.defer=true;'
    'h.appendChild(c);h.appendChild(s)})()</script>'
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


class ChineseParityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.base = Path(self.temporary.name)
        self.site = self.base / "site"
        self.snapshot_path = self.base / "snapshot.json"
        self._write_pre_locale_site()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _write(self, relative: str, value: str | bytes) -> None:
        path = self.site / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(value, bytes):
            path.write_bytes(value)
        else:
            path.write_text(value, encoding="utf-8")

    def _html(self, *, path: str = "/", title: str = "中文首页") -> str:
        canonical = f"{ORIGIN}{path}"
        return f'''<!doctype html>
<html lang="zh-Hans">
  <head>
    <meta charset="utf-8">
    <meta name="robots" content="index,follow">
    <meta name="description" content="中文金融研究">
    <link rel="canonical" href="{canonical}">
    <link rel="alternate" hreflang="zh-Hans" href="{canonical}">
    <link rel="alternate" hreflang="x-default" href="{canonical}">
    <title>{title}</title>
    <script type="application/ld+json">{{"@context":"https://schema.org","name":"{title}"}}</script>
  </head>
  <body><main><h1>{title}</h1><p>稳定的中文内容。</p></main><script src="/assets/app.js"></script></body>
</html>
'''

    def _write_pre_locale_site(self) -> None:
        self.site.mkdir()
        self._write("index.html", self._html())
        self._write("reports/market/index.html", self._html(path="/reports/market/", title="市场报告"))
        self._write("baidu_verify_codeva-FzG1Vh5prB.html", "0123456789abcdef0123456789abcdef\n")
        self._write("assets/app.js", "console.log('zh root');\n")
        self._write("assets/styles.css", "body { color: #111; }\n")
        self._write("data/catalog.json", '{"items":[]}\n')
        self._write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {ORIGIN}/sitemap.xml\n")
        self._write(
            "sitemap.xml",
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f'  <sitemap><loc>{ORIGIN}/sitemap-pages.xml</loc></sitemap>\n'
            '</sitemapindex>\n',
        )
        protected = {
            "feed.xml": "<rss><channel><title>中文报告</title></channel></rss>\n",
            "llms.txt": "# 中文报告\n",
            "llms-full.txt": "# 中文完整报告\n",
            "sitemap-baidu.xml": "<urlset><url><loc>https://portal.example.invalid/</loc></url></urlset>\n",
            "sitemap-sogou.xml": "<urlset><url><loc>https://portal.example.invalid/</loc></url></urlset>\n",
            "sitemap-pages.xml": "<urlset><url><loc>https://portal.example.invalid/</loc></url></urlset>\n",
            "sitemap-reports-01.xml": "<urlset><url><loc>https://portal.example.invalid/reports/market/</loc></url></urlset>\n",
            "sitemap-blog-01.xml": "<urlset><url><loc>https://portal.example.invalid/blog/example/</loc></url></urlset>\n",
        }
        for relative, value in protected.items():
            self._write(relative, value)

    def _snapshot(self, *, active_manifest: Path | None = None) -> dict:
        value = parity.create_snapshot(
            root=self.site,
            site_origin=ORIGIN,
            active_manifest=active_manifest,
        )
        self.snapshot_path.write_text(json.dumps(value), encoding="utf-8")
        return value

    def _apply_locale_discovery(self) -> None:
        for path in sorted(self.site.rglob("*.html")):
            relative = path.relative_to(self.site).as_posix()
            if (
                path.relative_to(self.site).parts[0] in parity.LOCALE_DIRS
                or parity.is_site_verification_html(relative)
            ):
                continue
            source = path.read_text(encoding="utf-8")
            canonical = parity._head_links(source.encode(), relative=str(path)).canonicals[0]
            suffix = canonical.removeprefix(ORIGIN)
            localized_path = "/" if suffix == "/" else suffix
            links = "\n".join(
                [
                    f'<link rel="alternate" hreflang="ko" href="{ORIGIN}/ko{localized_path}">',
                    f'<link rel="alternate" hreflang="ja" href="{ORIGIN}/ja{localized_path}">',
                    f'<link rel="alternate" hreflang="ar" href="{ORIGIN}/ar{localized_path}">',
                ]
            )
            source = source.replace("  </head>", f"    {BOOTSTRAP}\n    {links}\n  </head>")
            path.write_text(source, encoding="utf-8")
        robots = (self.site / "robots.txt").read_text(encoding="utf-8").rstrip()
        robots += "\n" + "\n".join(
            f"Sitemap: {ORIGIN}/sitemap-{locale}.xml" for locale in parity.LOCALES
        ) + "\n"
        (self.site / "robots.txt").write_text(robots, encoding="utf-8")
        sitemap = (self.site / "sitemap.xml").read_text(encoding="utf-8")
        rows = "\n".join(
            f"  <sitemap><loc>{ORIGIN}/sitemap-{locale}.xml</loc><lastmod>2026-09-04</lastmod></sitemap>"
            for locale in parity.LOCALES
        )
        sitemap = sitemap.replace("</sitemapindex>", f"{rows}\n</sitemapindex>")
        (self.site / "sitemap.xml").write_text(sitemap, encoding="utf-8")
        for locale in parity.LOCALES:
            self._write(f"sitemap-{locale}.xml", f"<urlset><url><loc>{ORIGIN}/{locale}/</loc></url></urlset>\n")
            self._write(f"{locale}/index.html", f"<html lang=\"{locale}\"><body>{locale}</body></html>\n")
            self._write(f"{locale}/assets/locale.css", "/* locale */\n")
        self._write("assets/locale.css", "/* locale */\n")
        self._write("assets/locale-runtime.js", "console.log('locale');\n")
        self._write("data/i18n/manifest.json", '{"locales":["ko","ja","ar"]}\n')

    def _verified_site(self) -> None:
        self._snapshot()
        self._apply_locale_discovery()

    def _verify(self) -> dict:
        return parity.verify_snapshot(root=self.site, snapshot_path=self.snapshot_path)

    def test_correct_controlled_additions_pass_and_emit_auditable_digest(self) -> None:
        snapshot = self._snapshot()
        self.assertEqual(snapshot["schema_version"], 1)
        self.assertEqual(snapshot["counts"]["html"], 2)
        self.assertRegex(snapshot["digest"], r"^[0-9a-f]{64}$")
        self.assertIn("body_sha256", snapshot["files"]["index.html"])
        self.assertIn("head_neutralized_sha256", snapshot["files"]["index.html"])
        self.assertNotIn("body_sha256", snapshot["files"]["baidu_verify_codeva-FzG1Vh5prB.html"])
        self.assertIn("baidu_verify_codeva-FzG1Vh5prB.html", snapshot["protected_files"])
        self._apply_locale_discovery()
        result = self._verify()
        self.assertEqual(result["counts"]["hreflang_clusters"], 2)
        self.assertRegex(result["digest"], r"^[0-9a-f]{64}$")

    def test_active_manifest_checks_stable_protected_scope_and_skips_html(self) -> None:
        preliminary = parity.create_snapshot(root=self.site, site_origin=ORIGIN)
        manifest = self.base / "active.json"
        manifest.write_text(
            json.dumps({"files": {
                relative: {"size": row["size"], "sha256": row["sha256"]}
                for relative, row in preliminary["files"].items()
            }}),
            encoding="utf-8",
        )
        # A different active HTML hash is intentionally irrelevant to this
        # optional live-slot check; pre/post locale parity still protects HTML.
        active = json.loads(manifest.read_text(encoding="utf-8"))
        active["files"]["index.html"] = {"size": 1, "sha256": "0" * 64}
        manifest.write_text(json.dumps(active), encoding="utf-8")
        snapshot = self._snapshot(active_manifest=manifest)
        self.assertTrue(snapshot["active_manifest"]["checked"])
        self.assertIn("query hashes", snapshot["active_manifest"]["skipped_html_reason"])

    def test_active_manifest_rejects_protected_content_mismatch(self) -> None:
        preliminary = parity.create_snapshot(root=self.site, site_origin=ORIGIN)
        manifest = self.base / "active.json"
        rows = {
            relative: {"size": row["size"], "sha256": row["sha256"]}
            for relative, row in preliminary["files"].items()
        }
        rows["assets/styles.css"]["sha256"] = "f" * 64
        manifest.write_text(json.dumps({"files": rows}), encoding="utf-8")
        with self.assertRaisesRegex(parity.ParityError, "active manifest"):
            self._snapshot(active_manifest=manifest)

    def test_body_change_fails(self) -> None:
        self._verified_site()
        path = self.site / "index.html"
        path.write_text(path.read_text(encoding="utf-8").replace("稳定的中文内容", "被修改"), encoding="utf-8")
        with self.assertRaisesRegex(parity.ParityError, "body changed"):
            self._verify()

    def test_each_protected_head_field_change_fails(self) -> None:
        cases = {
            "canonical": (f'rel="canonical" href="{ORIGIN}/"', f'rel="canonical" href="{ORIGIN}/wrong/"'),
            "title": ("<title>中文首页</title>", "<title>错误标题</title>"),
            "robots": ('content="index,follow"', 'content="noindex,follow"'),
            "json_ld": ('"name":"中文首页"', '"name":"错误结构化数据"'),
            "zh_hans": (f'hreflang="zh-Hans" href="{ORIGIN}/"', f'hreflang="zh-Hans" href="{ORIGIN}/wrong/"'),
            "x_default": (f'hreflang="x-default" href="{ORIGIN}/"', f'hreflang="x-default" href="{ORIGIN}/wrong/"'),
        }
        for label, (before, after) in cases.items():
            with self.subTest(label=label):
                with tempfile.TemporaryDirectory() as temporary:
                    original_site = self.site
                    original_snapshot = self.snapshot_path
                    try:
                        self.site = Path(temporary) / "site"
                        shutil.copytree(original_site, self.site)
                        self.snapshot_path = Path(temporary) / "snapshot.json"
                        self._verified_site()
                        path = self.site / "index.html"
                        source = path.read_text(encoding="utf-8")
                        self.assertIn(before, source)
                        path.write_text(source.replace(before, after, 1), encoding="utf-8")
                        with self.assertRaisesRegex(parity.ParityError, "changed"):
                            self._verify()
                    finally:
                        self.site = original_site
                        self.snapshot_path = original_snapshot

    def test_chinese_sitemap_and_css_changes_fail(self) -> None:
        for relative in ("sitemap-baidu.xml", "assets/styles.css"):
            with self.subTest(relative=relative):
                with tempfile.TemporaryDirectory() as temporary:
                    site = Path(temporary) / "site"
                    shutil.copytree(self.site, site)
                    snapshot_path = Path(temporary) / "snapshot.json"
                    snapshot = parity.create_snapshot(root=site, site_origin=ORIGIN)
                    snapshot_path.write_text(json.dumps(snapshot), encoding="utf-8")
                    old_site, old_snapshot = self.site, self.snapshot_path
                    try:
                        self.site, self.snapshot_path = site, snapshot_path
                        self._apply_locale_discovery()
                        path = site / relative
                        path.write_bytes(path.read_bytes() + b"changed\n")
                        with self.assertRaisesRegex(parity.ParityError, "changed"):
                            self._verify()
                    finally:
                        self.site, self.snapshot_path = old_site, old_snapshot

    def test_site_verification_html_is_byte_protected_not_treated_as_a_page(self) -> None:
        self._verified_site()
        path = self.site / "baidu_verify_codeva-FzG1Vh5prB.html"
        path.write_text("f" * 32 + "\n", encoding="utf-8")
        with self.assertRaisesRegex(parity.ParityError, "token changed"):
            self._verify()

    def test_site_verification_filename_cannot_exempt_arbitrary_html(self) -> None:
        path = self.site / "baidu_verify_codeva-FzG1Vh5prB.html"
        path.write_text("<html><head></head><body>fake</body></html>", encoding="utf-8")
        with self.assertRaisesRegex(parity.ParityError, "token is invalid"):
            self._snapshot()

    def test_unrecognized_headless_html_still_fails_closed(self) -> None:
        self._write("unexpected-token.html", "not a supported verification file")
        with self.assertRaisesRegex(parity.ParityError, "head element"):
            self._snapshot()

    def test_nested_verification_filename_is_not_exempt(self) -> None:
        self._write("nested/baidu_verify_codeva-FzG1Vh5prB.html", "0" * 32 + "\n")
        with self.assertRaisesRegex(parity.ParityError, "head element"):
            self._snapshot()

    def test_root_path_set_change_fails(self) -> None:
        self._verified_site()
        self._write("unexpected.txt", "unexpected\n")
        with self.assertRaisesRegex(parity.ParityError, "path set changed"):
            self._verify()

    def test_wrong_locale_href_fails(self) -> None:
        self._verified_site()
        path = self.site / "index.html"
        source = path.read_text(encoding="utf-8")
        source = source.replace(f'hreflang="ja" href="{ORIGIN}/ja/"', f'hreflang="ja" href="{ORIGIN}/wrong/"')
        path.write_text(source, encoding="utf-8")
        with self.assertRaisesRegex(parity.ParityError, "incorrect ja hreflang"):
            self._verify()

    def test_direct_static_locale_asset_fails(self) -> None:
        self._verified_site()
        path = self.site / "index.html"
        source = path.read_text(encoding="utf-8").replace(
            "</head>", '<link rel="stylesheet" href="/assets/locale.css?v=bad"></head>'
        )
        path.write_text(source, encoding="utf-8")
        with self.assertRaisesRegex(parity.ParityError, "statically loads locale assets"):
            self._verify()

    def test_removed_simplified_chinese_guard_fails(self) -> None:
        self._verified_site()
        path = self.site / "index.html"
        source = path.read_text(encoding="utf-8").replace(
            'if(l==="zh"||/^zh-(?:cn|sg|hans)(?:-|$)/.test(l))return;',
            "",
        )
        path.write_text(source, encoding="utf-8")
        with self.assertRaisesRegex(parity.ParityError, "bootstrap guard"):
            self._verify()

    def test_robots_and_sitemap_allow_only_exact_locale_additions(self) -> None:
        for relative, before, after, message in (
            (
                "robots.txt",
                f"Sitemap: {ORIGIN}/sitemap-ar.xml",
                "Sitemap: https://wrong.example/sitemap-ar.xml",
                "robots.txt",
            ),
            (
                "sitemap.xml",
                f"{ORIGIN}/sitemap-ar.xml",
                "https://wrong.example/sitemap-ar.xml",
                "sitemap.xml",
            ),
        ):
            with self.subTest(relative=relative):
                with tempfile.TemporaryDirectory() as temporary:
                    site = Path(temporary) / "site"
                    shutil.copytree(self.site, site)
                    snapshot_path = Path(temporary) / "snapshot.json"
                    snapshot = parity.create_snapshot(root=site, site_origin=ORIGIN)
                    snapshot_path.write_text(json.dumps(snapshot), encoding="utf-8")
                    old_site, old_snapshot = self.site, self.snapshot_path
                    try:
                        self.site, self.snapshot_path = site, snapshot_path
                        self._apply_locale_discovery()
                        path = site / relative
                        path.write_text(path.read_text(encoding="utf-8").replace(before, after), encoding="utf-8")
                        with self.assertRaisesRegex(parity.ParityError, message):
                            self._verify()
                    finally:
                        self.site, self.snapshot_path = old_site, old_snapshot

    def test_snapshot_digest_tampering_fails_closed(self) -> None:
        self._verified_site()
        snapshot = json.loads(self.snapshot_path.read_text(encoding="utf-8"))
        snapshot["files"]["index.html"]["body_sha256"] = "0" * 64
        self.snapshot_path.write_text(json.dumps(snapshot), encoding="utf-8")
        with self.assertRaisesRegex(parity.ParityError, "digest"):
            self._verify()

    def test_symlink_in_static_tree_fails_closed(self) -> None:
        (self.site / "linked.txt").symlink_to(self.site / "robots.txt")
        with self.assertRaisesRegex(parity.ParityError, "symlink"):
            self._snapshot()


if __name__ == "__main__":
    unittest.main()
