#!/usr/bin/env python3
"""Rebuild the authenticated member contact card from a legacy QR payload.

The source image is used only as input to the QR decoder.  No source pixels,
metadata, text, or layout are copied into the generated KC branded card.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import sys
import tempfile
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont


MAX_SOURCE_BYTES = 1024 * 1024
MAX_OUTPUT_BYTES = 1024 * 1024
OUTPUT_SIZE = (1080, 1320)
BRAND_WORD = "".join(("KC", "Desk"))
BRAND_MONOGRAM = "".join(("K", "C"))


def _load_image_module(name: str) -> Any:
    try:
        if name == "qrcode":
            import qrcode

            return qrcode
        if name == "zxingcpp":
            import zxingcpp

            return zxingcpp
    except ImportError as error:
        raise RuntimeError(f"Required member-card image dependency is unavailable: {name}") from error
    raise ValueError("Unsupported member-card image dependency")


def validate_jpeg(path: Path, *, maximum_bytes: int) -> tuple[int, tuple[int, int]]:
    if path.is_symlink() or not path.is_file():
        raise ValueError("Member contact source must be a real JPEG file")
    size = path.stat().st_size
    if size <= 0 or size > maximum_bytes:
        raise ValueError("Member contact JPEG size is outside the allowed range")
    with path.open("rb") as handle:
        if handle.read(3) != b"\xff\xd8\xff":
            raise ValueError("Member contact source is not a JPEG")
    try:
        with Image.open(path) as image:
            if image.format != "JPEG":
                raise ValueError("Member contact source is not a JPEG")
            dimensions = image.size
            image.verify()
    except (OSError, SyntaxError) as error:
        raise ValueError("Member contact source is not a valid JPEG") from error
    if not all(128 <= int(value) <= 4096 for value in dimensions):
        raise ValueError("Member contact JPEG dimensions are outside the allowed range")
    return size, dimensions


def decode_single_qr_payload(path: Path, zxing_module: Any | None = None) -> bytes:
    validate_jpeg(path, maximum_bytes=MAX_SOURCE_BYTES)
    zxing = zxing_module or _load_image_module("zxingcpp")
    with Image.open(path) as source:
        source.load()
        decoder_input = source.convert("RGB")
    results = zxing.read_barcodes(
        decoder_input,
        formats=zxing.BarcodeFormat.QRCode,
    )
    if len(results) != 1:
        raise ValueError("Member contact source must contain exactly one QR code")
    payload = bytes(results[0].bytes)
    if not payload:
        raise ValueError("Member contact QR payload is empty")
    return payload


def _font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    return ImageFont.load_default(size=size)


def render_member_contact_card(payload: bytes, qrcode_module: Any | None = None) -> Image.Image:
    if not payload:
        raise ValueError("Member contact QR payload is empty")
    qrcode = qrcode_module or _load_image_module("qrcode")
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=1,
        border=4,
    )
    qr.add_data(payload, optimize=0)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="#07161b", back_color="#ffffff").convert("RGB")
    scale = max(4, 740 // qr_image.width)
    qr_image = qr_image.resize(
        (qr_image.width * scale, qr_image.height * scale),
        Image.Resampling.NEAREST,
    )

    card = Image.new("RGB", OUTPUT_SIZE, "#07161b")
    draw = ImageDraw.Draw(card)
    draw.rounded_rectangle((72, 64, 1008, 1256), radius=44, fill="#0d252c", outline="#2e6570", width=3)
    draw.rounded_rectangle((102, 92, 234, 224), radius=28, fill="#113b46", outline="#66e0d1", width=3)
    draw.text((168, 158), BRAND_MONOGRAM, font=_font(64), fill="#f4fbfc", anchor="mm")
    draw.text((272, 105), BRAND_WORD, font=_font(72), fill="#f4fbfc")
    draw.text((276, 182), "MEMBER CONTACT", font=_font(30), fill="#86a9b1")

    tile_padding = 46
    tile_width = qr_image.width + tile_padding * 2
    tile_left = (OUTPUT_SIZE[0] - tile_width) // 2
    tile_top = 302
    tile_bottom = tile_top + qr_image.height + tile_padding * 2
    draw.rounded_rectangle(
        (tile_left, tile_top, tile_left + tile_width, tile_bottom),
        radius=32,
        fill="#ffffff",
    )
    card.paste(qr_image, (tile_left + tile_padding, tile_top + tile_padding))
    draw.text(
        (OUTPUT_SIZE[0] // 2, 1194),
        "PRIVATE MEMBER ACCESS",
        font=_font(28),
        fill="#86a9b1",
        anchor="mm",
    )
    return card


def build_member_contact_card(
    source_path: Path,
    output_path: Path,
    *,
    zxing_module: Any | None = None,
    qrcode_module: Any | None = None,
) -> dict[str, object]:
    source = Path(source_path)
    output = Path(output_path)
    if output.is_symlink():
        raise ValueError("Member contact output must not be a symbolic link")
    if source.resolve(strict=False) == output.resolve(strict=False):
        raise ValueError("Member contact output must differ from the legacy source")

    zxing = zxing_module or _load_image_module("zxingcpp")
    payload = decode_single_qr_payload(source, zxing)
    card = render_member_contact_card(payload, qrcode_module)
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            dir=output.parent,
            prefix=".member-contact-card-",
            suffix=".jpg",
            delete=False,
        ) as handle:
            temporary_path = Path(handle.name)
        card.save(
            temporary_path,
            format="JPEG",
            quality=96,
            subsampling=0,
            optimize=True,
        )
        os.chmod(temporary_path, 0o600)
        size, dimensions = validate_jpeg(temporary_path, maximum_bytes=MAX_OUTPUT_BYTES)
        rebuilt_payload = decode_single_qr_payload(temporary_path, zxing)
        if rebuilt_payload != payload:
            raise ValueError("Rebuilt member contact QR payload does not match the source")
        output_digest = hashlib.sha256(temporary_path.read_bytes()).hexdigest()
        os.replace(temporary_path, output)
        temporary_path = None
        return {
            "output_sha256": output_digest,
            "output_size": size,
            "output_width": dimensions[0],
            "output_height": dimensions[1],
        }
    finally:
        card.close()
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output)
    try:
        result = build_member_contact_card(Path(args.source), output)
        print(
            " ".join(
                f"{key}={result[key]}"
                for key in ("output_size", "output_width", "output_height", "output_sha256")
            )
        )
        return 0
    except Exception as error:
        output.unlink(missing_ok=True)
        print(f"Member contact card build failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
