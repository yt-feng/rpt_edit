#!/usr/bin/env python3
"""Real CJK cover rendering remains available when optional APT fonts fail."""
from __future__ import annotations

from unittest.mock import patch, sentinel
import unittest

from PIL import Image, ImageDraw, ImageFont

import pdf_to_xhs_batch as batch


class CoverFontTests(unittest.TestCase):
    def test_missing_system_fonts_render_distinct_chinese_glyphs(self):
        for bold in (False, True):
            with self.subTest(bold=bold), patch.object(batch.Path, "exists", return_value=False):
                font = batch.load_font(32, bold=bold)
            self.assertIsInstance(font, ImageFont.FreeTypeFont)
            glyphs = [bytes(font.getmask(text)) for text in ("中", "文", "国")]
            missing = bytes(font.getmask("\U0010ffff"))
            self.assertEqual(len(set(glyphs)), 3)
            self.assertTrue(all(glyph != missing and any(glyph) for glyph in glyphs))
            image = Image.new("L", (200, 60), 0)
            ImageDraw.Draw(image).text((0, 0), "中文研究报告", font=font, fill=255)
            self.assertIsNotNone(image.getbbox())

    def test_missing_kai_font_uses_the_same_cjk_fallback(self):
        with patch.object(batch.Path, "exists", return_value=False):
            font = batch.load_kai_font(24)
        self.assertNotEqual(bytes(font.getmask("中")), bytes(font.getmask("\U0010ffff")))

    def test_installed_noto_still_takes_precedence(self):
        with patch.object(batch.Path, "exists", return_value=True), \
             patch.object(batch.ImageFont, "truetype", return_value=sentinel.font) as truetype, \
             patch.object(batch.fitz, "Font") as bundled:
            self.assertIs(batch.load_font(24, bold=True), sentinel.font)
        truetype.assert_called_once_with("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc", 24)
        bundled.assert_not_called()


if __name__ == "__main__":
    unittest.main(verbosity=2)
