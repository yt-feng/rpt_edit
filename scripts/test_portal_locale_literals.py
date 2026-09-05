#!/usr/bin/env python3
"""Asset references do not require translation or paid repair requests."""
import unittest

import build_portal_locales as builder
from portal_locale_literals import is_machine_asset_reference


class AssetReferenceTests(unittest.TestCase):
    def test_real_failure_and_asset_variants_are_not_prose(self):
        for value in (
            "assets/source_image_02.jpg", "source_image_02.JPG", "../images/figure-2.webp",
            "/assets/chart.svg#plot", "./report_2026.pdf?download=1", "data/table.xlsx",
            " figure_01.png ", "assets/a%20b.avif", "archive/report.pptx",
        ):
            with self.subTest(value=value):
                self.assertTrue(is_machine_asset_reference(value))
                units = {}
                builder.collect_text_units(value, "html:attribute:alt", units)
                self.assertEqual(units, {})
                for locale in ("ko", "ja", "ar"):
                    cache = {"locales": {locale: {}}}
                    self.assertEqual(builder.translated_text(value, "html:attribute:alt", locale, cache), value)

    def test_prose_and_unknown_identifiers_are_not_exempt(self):
        for value in (
            "Learn about source.jpg", "图表 source.jpg", "source.jpg illustrates growth",
            "Bank of America Merrill Lynch", "From", "经济研究报告", "Revenue.pdf increased",
            "Report PDF", "some.unknown", "image.png\nprose", None, "", "photo.jpg;ignore",
        ):
            with self.subTest(value=value):
                self.assertFalse(is_machine_asset_reference(value))
        for value in ("Learn about source.jpg", "图表 source.jpg", "From"):
            self.assertIsNotNone(builder.unit_for_text(value, "html:attribute:alt")[1])


if __name__ == "__main__":
    unittest.main()
