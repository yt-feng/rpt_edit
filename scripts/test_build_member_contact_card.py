#!/usr/bin/env python3

from __future__ import annotations

import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import qrcode
import zxingcpp
from PIL import Image

import build_member_contact_card as builder


def qr_image(payload: bytes, *, box_size: int = 10) -> Image.Image:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=4,
    )
    qr.add_data(payload, optimize=0)
    qr.make(fit=True)
    return qr.make_image(fill_color="black", back_color="white").convert("RGB")


def write_source(path: Path, payloads: tuple[bytes, ...]) -> None:
    if not payloads:
        Image.new("RGB", (900, 700), "#d923d9").save(path, format="JPEG", quality=96)
        return
    codes = [qr_image(payload, box_size=8 if len(payloads) > 1 else 12) for payload in payloads]
    width = max(900, sum(code.width for code in codes) + 80 * (len(codes) + 1))
    height = max(700, max(code.height for code in codes) + 160)
    source = Image.new("RGB", (width, height), "#d923d9")
    left = 80
    for code in codes:
        source.paste(code, (left, 80))
        left += code.width + 80
    source.save(path, format="JPEG", quality=96, subsampling=0)


class MemberContactCardBuilderTests(unittest.TestCase):
    def test_rebuilds_new_kc_pixels_and_preserves_exact_payload_without_logging_it(self) -> None:
        payload = b"https://example.invalid/private-member-contact?fixture=do-not-log"
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "legacy.jpg"
            output = root / "member-contact-card.jpg"
            write_source(source, (payload,))

            stdout = io.StringIO()
            stderr = io.StringIO()
            with mock.patch.object(
                sys,
                "argv",
                ["build_member_contact_card.py", "--source", str(source), "--output", str(output)],
            ), contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                self.assertEqual(builder.main(), 0)

            self.assertTrue(output.is_file())
            self.assertNotIn(payload.decode("ascii"), stdout.getvalue())
            self.assertNotIn(payload.decode("ascii"), stderr.getvalue())
            self.assertEqual(builder.BRAND_WORD, "".join(("KC", "Desk")))
            self.assertEqual(builder.BRAND_MONOGRAM, "KC")
            rebuilt = builder.decode_single_qr_payload(output, zxingcpp)
            self.assertEqual(rebuilt, payload)
            with Image.open(output) as card:
                self.assertEqual(card.format, "JPEG")
                self.assertEqual(card.size, builder.OUTPUT_SIZE)
                colors = card.convert("RGB").getdata()
                self.assertFalse(
                    any(red > 200 and blue > 150 and green < 100 for red, green, blue in colors),
                    "legacy magenta source pixels must not be copied into the rebuilt card",
                )

    def test_rejects_missing_and_invalid_jpeg_sources(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            output = root / "member-contact-card.jpg"
            with self.assertRaisesRegex(ValueError, "real JPEG"):
                builder.build_member_contact_card(root / "missing.jpg", output)
            invalid = root / "invalid.jpg"
            invalid.write_bytes(b"\xff\xd8\xffnot-a-jpeg")
            with self.assertRaisesRegex(ValueError, "valid JPEG"):
                builder.build_member_contact_card(invalid, output)
            self.assertFalse(output.exists())

    def test_rejects_zero_or_multiple_qr_codes(self) -> None:
        payloads = (
            b"https://example.invalid/private-contact-a",
            b"https://example.invalid/private-contact-b",
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            blank = root / "blank.jpg"
            multiple = root / "multiple.jpg"
            output = root / "member-contact-card.jpg"
            write_source(blank, ())
            write_source(multiple, payloads)
            with self.assertRaisesRegex(ValueError, "exactly one QR"):
                builder.build_member_contact_card(blank, output)
            with self.assertRaisesRegex(ValueError, "exactly one QR"):
                builder.build_member_contact_card(multiple, output)
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
