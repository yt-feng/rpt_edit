#!/usr/bin/env python3

from __future__ import annotations

import base64
import json
import os
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

from check_public_brand import PublicBrandError, check_public_brand, main


def write(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8")


def write_brand_mark(root: Path, label: str = "KC桌面") -> None:
    write(root / "assets/app-mark.svg", f'<svg role="img" aria-label="{label}"></svg>')


class PublicBrandCheckTests(unittest.TestCase):
    def test_clean_materialized_site_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            write(root / "index.html", "<title>KC桌面</title>")
            write_brand_mark(root)
            write(root / "assets/app.js", "const source = 'external';")
            write(root / "data/catalog.json", '{"items": []}')
            self.assertEqual(check_public_brand(root)["files"], 4)
            self.assertEqual(main([str(root)]), 0)

    def test_every_legacy_name_and_source_domain_is_rejected(self) -> None:
        samples = (
            "Reportify",
            "Report_ify",
            "reportify",
            "NashAI",
            "Nash AI",
            "MacroGate",
            "Macro Gate",
            "Macro-Gate",
            "Portal Suite",
            "Portal_Suite",
            "Portal Alternate",
            "Portal 娱乐",
            " ".join(("KC", "Desk", "Notes")),
            "-".join(("KC", "Desk", "Notes")),
            "Support Contact",
            "Support.Contact",
            "Twotigers",
            "Two Tigers",
            "麦府学堂",
            "麦府课堂",
            "慧博",
            "https://api.reportify.cn/reports",
            "https://www.nash-ai.cn/reports",
            "https://www.hibor.com.cn/data",
        )
        for sample in samples:
            with self.subTest(sample=sample), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                write(root / "index.html", f"KC桌面 {sample}")
                write_brand_mark(root)
                with self.assertRaisesRegex(PublicBrandError, "Public brand check failed"):
                    check_public_brand(root)

    def test_nfkc_and_zero_width_obfuscation_do_not_bypass_the_gate(self) -> None:
        samples = (
            "Ｒｅｐｏｒｔｉｆｙ",
            "Nash\u200bAI",
            "Portal\u00a0Suite",
            "Report&#105;fy",
            r'<script>document.body.textContent="\u0052eportify"</script>',
            "<span>Report</span><span>ify</span>",
            '<p>Report<span title=">">ify</span></p>',
            '<p>Report<span title="&quot;>">ify</span></p>',
            '<p>Report<span title="%22>">ify</span></p>',
            "Report<script>0</script>ify",
            "Report<style>.x{}</style>ify",
            "Report<template>not rendered</template>ify",
            "Report<!-- > -->ify",
            "Portal<div></div>Suite",
            r'<style>.legacy::after { content: "R\65portify"; }</style>',
            "https://report%69fy.cn/reports",
            '<script>document.body.textContent = "Report" + "ify";</script>',
            '<script>document.body.textContent = "Report" /* source */ + "ify";</script>',
            '<script>document.body.textContent = "Report" // source\n + "ify";</script>',
            '<div class="account-twotigersnalytics"></div>',
        )
        for sample in samples:
            with self.subTest(sample=sample), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                write(root / "index.html", f"KC桌面 {sample}")
                write_brand_mark(root)
                with self.assertRaises(PublicBrandError):
                    check_public_brand(root)

    def test_common_nested_encodings_do_not_bypass_the_gate(self) -> None:
        samples = (
            "https://report%2569fy.cn/reports",
            "https://report%252569fy.cn/reports",
            "Report&amp;#105;fy",
            "Report&amp;amp;#105;fy",
            "Report%26%23105%3Bfy",
            r"%5Cu0052eportify",
            r'<style>.legacy::after { content: "%5C000052eportify"; }</style>',
            "Report%3Cspan%3E%3C%2Fspan%3Eify",
        )
        for sample in samples:
            with self.subTest(sample=sample), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                write(root / "index.html", f"KC桌面 {sample}")
                write_brand_mark(root)
                with self.assertRaises(PublicBrandError):
                    check_public_brand(root)

    def test_legitimate_financial_term_and_person_name_are_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            write(root / "index.html", "KC桌面 tracks HIBOR. Nash authored the note.")
            write_brand_mark(root)
            write(root / "assets/app.js", "root.PortalSuiteContact = root.PortalSuiteAnalytics;")
            check_public_brand(root)

    def test_selected_private_profile_values_are_forbidden_even_inside_identifiers(self) -> None:
        profile = base64.b64encode(json.dumps({
            "version": 1,
            "replacements": [
                {"public": "admin-a", "private": "owner-handle"},
            ],
            "files": [],
        }).encode("utf-8")).decode("ascii")
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            write(root / "index.html", "KC桌面")
            write_brand_mark(root)
            write(root / "assets/app.js", 'const name = "account-owner-handlenalytics";')
            with patch.dict(os.environ, {"PORTAL_PRIVATE_CONFIG_B64": profile}):
                self.assertEqual(
                    main([str(root), "--forbid-profile-private-for", "admin-a"]),
                    1,
                )

            write(root / "assets/app.js", 'const name = "account-ops-analytics";')
            with patch.dict(os.environ, {"PORTAL_PRIVATE_CONFIG_B64": profile}):
                self.assertEqual(
                    main([str(root), "--forbid-profile-private-for", "admin-a"]),
                    0,
                )

    def test_required_public_brand_must_be_present(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            write(root / "index.html", "中文金融研报检索")
            write_brand_mark(root)
            write(root / "assets/app.js", "const brand = 'KC桌面';")
            with self.assertRaisesRegex(PublicBrandError, "missing required brand"):
                check_public_brand(root)
            self.assertEqual(main([str(root)]), 1)

    def test_paths_and_symlinks_are_checked(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            write(root / "index.html", "KC桌面")
            write_brand_mark(root)
            write(root / "Reportify" / "index.html", "legacy path")
            with self.assertRaisesRegex(PublicBrandError, "Reportify"):
                check_public_brand(root)

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            write(root / "index.html", "KC桌面")
            write_brand_mark(root)
            write(root / "assets/contact-card.jpg", "binary placeholder")
            with self.assertRaisesRegex(PublicBrandError, "contact-card asset"):
                check_public_brand(root)

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            write(root / "index.html", "KC桌面")
            write_brand_mark(root)
            (root / "linked.html").symlink_to(root / "index.html")
            with self.assertRaisesRegex(PublicBrandError, "symbolic links"):
                check_public_brand(root)

    def test_brand_mark_is_required_and_must_identify_kc(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            write(root / "index.html", "KC桌面")
            with self.assertRaisesRegex(PublicBrandError, "missing required KC brand mark"):
                check_public_brand(root)

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            write(root / "index.html", "KC桌面")
            write_brand_mark(root, "PS")
            with self.assertRaisesRegex(PublicBrandError, "aria-label must be KC"):
                check_public_brand(root)

        invalid_marks = (
            '<svg data-aria-label="KC"></svg>',
            '<svg><!-- aria-label="KC" --></svg>',
            '<svg><g aria-label="KC"></g></svg>',
            '<html aria-label="KC"></html>',
            '<svg aria-label="KC">',
        )
        for source in invalid_marks:
            with self.subTest(source=source), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                write(root / "index.html", "KC桌面")
                write(root / "assets/app-mark.svg", source)
                with self.assertRaisesRegex(PublicBrandError, "aria-label must be KC"):
                    check_public_brand(root)


if __name__ == "__main__":
    unittest.main(verbosity=2)
