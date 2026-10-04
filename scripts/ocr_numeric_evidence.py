#!/usr/bin/env python3
"""Verify OCR numeric fields against repeated, positioned reads of source pixels.

The first OCR transcript is retained in the private receipt. Numbers admitted to
the summary transcript require agreement from a higher-resolution page read and
two differently segmented reads of isolated source crops. Visible decimal and
minus marks are checked separately from OCR confidence. A disagreeing field is
explicitly marked; the surrounding report, tables and original pages remain.

This is corroboration, not a claim that a single OCR engine is infallible. Every
decision records its source position and inputs so acceptance can be measured
against ground-truth scans and inspected without trusting an engine score.
"""
from __future__ import annotations

import base64
import binascii
import csv
import difflib
import hashlib
import io
import json
import math
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unicodedata
from typing import Any, Iterable

import fitz
from PIL import Image


SCHEMA = 1
SOURCE_DPI = 300
SECOND_DPI = 450
CROP_DPI = 600
CROP_BATCH = 48
OCR_CROP_POLICY = "isolated-numeric-crop-v1"
OVERFLOW_RECOVERY_POLICY = "isolated-overflow-crop-v1"
ISOLATED_PADDING = 24
MAX_RECOVERY_PNG_BYTES = 16_000_000
MAX_FIELDS = 2500
MAX_IMAGE_PIXELS = 80_000_000
NUMERIC = re.compile(
    r"(?<![0-9.,])(?:[+\-−–]\s*)?(?:\(\s*)?(?:[$€£¥]\s*)?"
    r"(?:[0-9]{1,3}(?:,[0-9]{3})+|[0-9]+)(?:[.,][0-9]+)?"
    r"(?:\s*\))?(?:\s*%|\s*(?:bps?|x)\b)?(?:\s*\))?",
    re.I,
)


GEOMETRY_FLAGS = (
    "policy_matches", "dpi_matches", "clip_valid", "clip_matches", "size_valid", "size_matches",
    "field_count_valid", "input_hash_valid",
)


def safe_numeric_geometry_diagnostics(value: Any) -> dict[str, Any] | None:
    """Project crop failures without copying source words or engine output."""
    if not isinstance(value, dict) or type(value.get("schema")) is not int or value["schema"] != 1:
        return None
    output: dict[str, Any] = {"schema": 1}
    if isinstance(value.get("record_id"), str) and re.fullmatch(r"n[0-9]{4}", value["record_id"]):
        output["record_id"] = value["record_id"]
    if type(value.get("psm")) is int and value["psm"] in {6, 11}:
        output["psm"] = value["psm"]
    for key in GEOMETRY_FLAGS:
        if type(value.get(key)) is bool:
            output[key] = value[key]
    for key in ("field_bbox", "page_bounds", "expected_clip_bbox", "actual_clip_bbox"):
        box = value.get(key)
        if (isinstance(box, list) and len(box) == 4
                and all(type(item) in (int, float) and math.isfinite(item) and 0 <= item <= 100_000 for item in box)
                and box[2] > box[0] and box[3] > box[1]):
            output[key] = list(box)
    for key in ("expected_pixel_size", "actual_pixel_size"):
        size = value.get(key)
        if isinstance(size, list) and len(size) == 2 and all(type(item) is int and 0 <= item <= 100_000 for item in size):
            output[key] = list(size)
    for key in ("dpi", "field_count"):
        if type(value.get(key)) is int and 0 <= value[key] <= 2500:
            output[key] = value[key]
    if isinstance(value.get("field_count_kind"), str) and value["field_count_kind"] in {"missing", "null", "boolean", "integer", "other"}:
        output["field_count_kind"] = value["field_count_kind"]
    if type(value.get("field_count_above_bound")) is bool:
        output["field_count_above_bound"] = value["field_count_above_bound"]
    if type(value.get("field_count_capped_count")) is int and 0 <= value["field_count_capped_count"] <= MAX_FIELDS:
        output["field_count_capped_count"] = value["field_count_capped_count"]
    version = value.get("pymupdf_version")
    if isinstance(version, str) and len(version) <= 32 and re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version):
        output["pymupdf_version"] = version
    return output


class NumericEvidenceError(ValueError):
    """Numeric source evidence is incomplete, inconsistent or unavailable."""

    def __init__(self, message: str, *, diagnostics: dict[str, Any] | None = None):
        super().__init__(message)
        self.diagnostics = safe_numeric_geometry_diagnostics(diagnostics)


def safe_geometry_diagnostics(error_or_value: Any) -> dict[str, Any] | None:
    """Reproject module errors or a forwarded public-safe geometry object."""
    if isinstance(error_or_value, NumericEvidenceError):
        error_or_value = error_or_value.diagnostics
    elif isinstance(error_or_value, BaseException):
        error_or_value = getattr(error_or_value, "geometry_diagnostics", None)
    return safe_numeric_geometry_diagnostics(error_or_value)


def _sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def normalize_number(literal: str) -> str:
    value = unicodedata.normalize("NFKC", literal).replace("−", "-").replace("–", "-")
    value = re.sub(r"\s+", "", value)
    if value.startswith("(") and ")" in value:
        value = "-" + value[1:].replace(")", "")
    # Thousands separators are harmless spelling variants; decimal commas are
    # deliberately retained because their locale cannot be inferred from OCR.
    value = re.sub(r"(?<=\d),(?=\d{3}(?:\D|$))", "", value)
    return value.lower()


def numeric_mentions(text: str) -> list[dict[str, Any]]:
    return [{"begin": match.start(), "end": match.end(), "literal": match.group(),
             "normalized": normalize_number(match.group())} for match in NUMERIC.finditer(text)]


def _image(pixmap: fitz.Pixmap) -> Image.Image:
    if pixmap.n != 3 or pixmap.alpha:
        raise NumericEvidenceError("Numeric audit requires RGB source rendering")
    if pixmap.width * pixmap.height > MAX_IMAGE_PIXELS:
        raise NumericEvidenceError("Numeric audit source image exceeds the pixel bound")
    return Image.frombytes("RGB", (pixmap.width, pixmap.height), pixmap.samples)


def _word_mentions(words: Iterable[Any]) -> list[dict[str, Any]]:
    """Keep numerical positions, including signs split into separate OCR words."""
    lines: dict[tuple[int, int, int], list[dict[str, Any]]] = {}
    for item in words:
        if isinstance(item, dict):
            word = item
        else:
            if len(item) < 5:
                raise NumericEvidenceError("OCR word is missing its source position")
            word = {"bbox": [float(v) for v in item[:4]], "text": str(item[4]),
                    "block": int(item[5]) if len(item) > 5 else 0,
                    "paragraph": 0,
                    "line": int(item[6]) if len(item) > 6 else 0}
        box = word.get("bbox")
        if not isinstance(box, list) or len(box) != 4 or not all(isinstance(v, (int, float)) and math.isfinite(v) for v in box):
            raise NumericEvidenceError("OCR word position is invalid")
        if box[2] <= box[0] or box[3] <= box[1] or not isinstance(word.get("text"), str):
            raise NumericEvidenceError("OCR word position or text is invalid")
        lines.setdefault((int(word.get("block", 0)), int(word.get("paragraph", 0)),
                          int(word.get("line", 0))), []).append(word)
    mentions = []
    # PyMuPDF's sorted text and words share this geometric order. The occurrence
    # alignment below still refuses many-to-one changes rather than guessing.
    for line_words in sorted(lines.values(), key=lambda row: (min(w["bbox"][1] for w in row), min(w["bbox"][0] for w in row))):
        line_words.sort(key=lambda word: word["bbox"][0])
        spans = []
        text = ""
        for word in line_words:
            if text:
                text += " "
            begin = len(text)
            text += word["text"]
            spans.append((begin, len(text), word))
        for mention in numeric_mentions(text):
            relevant = [w for begin, end, w in spans if begin < mention["end"] and end > mention["begin"]]
            boxes = [w["bbox"] for w in relevant]
            # Restrict a numerical substring embedded in an identifier/word to
            # its proportional region. Pure numerical words retain exact boxes.
            if len(relevant) == 1:
                begin, end, word = next((a, b, w) for a, b, w in spans if w is relevant[0])
                box = list(word["bbox"])
                fraction_start = (mention["begin"] - begin) / max(1, end - begin)
                fraction_end = (mention["end"] - begin) / max(1, end - begin)
                width = box[2] - box[0]
                box[2] = box[0] + fraction_end * width
                box[0] += fraction_start * width
            else:
                box = [min(v[0] for v in boxes), min(v[1] for v in boxes),
                       max(v[2] for v in boxes), max(v[3] for v in boxes)]
            mentions.append({**mention, "bbox": [round(v, 4) for v in box]})
    return mentions


def _align_mentions(primary: list[dict[str, Any]], positioned: list[dict[str, Any]]) -> dict[int, dict[str, Any]]:
    matcher = difflib.SequenceMatcher(a=[row["normalized"] for row in primary],
                                     b=[row["normalized"] for row in positioned], autojunk=False)
    result = {}
    for operation, a0, a1, b0, b1 in matcher.get_opcodes():
        if operation == "equal":
            result.update({a0 + offset: positioned[b0 + offset] for offset in range(a1 - a0)})
        elif operation == "replace" and a1 - a0 == b1 - b0 == 1:
            result[a0] = positioned[b0]
    return result


def _read_tesseract(image: Image.Image, *, language: str, tessdata: str | None,
                    command: str, psm: int, dpi: int) -> list[dict[str, Any]]:
    if image.width * image.height > MAX_IMAGE_PIXELS:
        raise NumericEvidenceError("Numeric OCR image exceeds the pixel bound")
    with tempfile.TemporaryDirectory(prefix="numeric-ocr-") as directory:
        source = Path(directory) / "source.png"
        image.save(source, dpi=(dpi, dpi))
        args = [command, str(source), "stdout", "-l", language, "--psm", str(psm), "--dpi", str(dpi)]
        if tessdata:
            args += ["--tessdata-dir", tessdata]
        args += ["tsv"]
        try:
            result = subprocess.run(args, check=False, capture_output=True, timeout=120)
        except (OSError, subprocess.SubprocessError) as exc:
            raise NumericEvidenceError("Numeric verification OCR did not complete") from exc
        if result.returncode or len(result.stdout) > 16_000_000:
            raise NumericEvidenceError("Numeric verification OCR failed")
    try:
        rows = list(csv.DictReader(io.StringIO(result.stdout.decode("utf-8")), delimiter="\t"))
        words = []
        for row in rows:
            if row.get("level") != "5" or not row.get("text", "").strip():
                continue
            left, top, width, height = (int(row[key]) for key in ("left", "top", "width", "height"))
            if width <= 0 or height <= 0 or min(left, top) < 0 or left + width > image.width or top + height > image.height:
                raise NumericEvidenceError("Numeric verification OCR returned invalid coordinates")
            words.append({"bbox": [left, top, left + width, top + height], "text": row["text"],
                          "block": int(row["block_num"]), "paragraph": int(row["par_num"]),
                          "line": int(row["line_num"])})
        return words
    except (UnicodeError, KeyError, TypeError, ValueError) as exc:
        raise NumericEvidenceError("Numeric verification OCR returned invalid TSV") from exc


def _overlap(a: list[float], b: list[float]) -> float:
    width = max(0.0, min(a[2], b[2]) - max(a[0], b[0]))
    height = max(0.0, min(a[3], b[3]) - max(a[1], b[1]))
    return width * height / max(0.01, min((a[2] - a[0]) * (a[3] - a[1]), (b[2] - b[0]) * (b[3] - b[1])))


def _at_position(box: list[float], candidates: list[dict[str, Any]]) -> dict[str, Any] | None:
    hits = [row for row in candidates if _overlap(box, row["bbox"]) >= 0.55]
    # A duplicate value in another table column is never accepted as a read of
    # this field; a merged pair of source fields is also unresolved.
    return hits[0] if len(hits) == 1 else None


def _field_padding(box: list[float]) -> float:
    # OCR word boxes can omit the very sign/decimal/percent glyph we need to
    # verify. Include the adjoining fraction of one character without reaching
    # a separate table column.
    return min(8.0, max(1.5, (box[3] - box[1]) * 0.65))


def _pixel_box(box: list[float], image: Image.Image, page_size: list[float], *, padding: float | None = None) -> list[int]:
    padding = _field_padding(box) if padding is None else padding
    sx, sy = image.width / page_size[0], image.height / page_size[1]
    return [max(0, math.floor((box[0] - padding) * sx)), max(0, math.floor((box[1] - padding) * sy)),
            min(image.width, math.ceil((box[2] + padding) * sx)), min(image.height, math.ceil((box[3] + padding) * sy))]


def _ocr_crop_clip(box: list[float], page_size: list[float]) -> list[float]:
    """Isolate a positioned field for OCR without copying adjoining prose.

    The wider 300dpi punctuation witness is deliberately separate: it still
    detects a sign or percent mark omitted from the positioned word. Such a
    field must remain unresolved if this tight read cannot reproduce the mark.
    """
    if (not isinstance(box, list) or len(box) != 4
            or not isinstance(page_size, list) or len(page_size) != 2
            or any(type(value) not in (int, float) or not math.isfinite(value) for value in box + page_size)
            or box[2] <= box[0] or box[3] <= box[1] or min(page_size) <= 0):
        raise NumericEvidenceError("Numeric crop geometry is invalid")
    height = box[3] - box[1]
    horizontal = min(1.5, max(0.75, height * 0.12))
    vertical = min(1.0, max(0.5, height * 0.06))
    clip = [max(0.0, box[0] - horizontal), max(0.0, box[1] - vertical),
            min(page_size[0], box[2] + horizontal), min(page_size[1], box[3] + vertical)]
    if clip[2] <= clip[0] or clip[3] <= clip[1]:
        raise NumericEvidenceError("Numeric crop is outside the source page")
    return [round(value, 4) for value in clip]


def _ocr_crop_pixel_size(clip: list[float]) -> list[int]:
    bounds = (fitz.Rect(clip) * fitz.Matrix(CROP_DPI / 72, CROP_DPI / 72)).irect
    return [bounds.width, bounds.height]


def pixel_punctuation(image: Image.Image) -> dict[str, Any]:
    """Record connected ink marks, independently of recognized characters."""
    grayscale = image.convert("L")
    width, height = grayscale.size
    pixels = grayscale.tobytes()
    ink = {index for index, value in enumerate(pixels) if value < 160}
    components = []
    while ink:
        seed = ink.pop()
        queue, found = [seed], [seed]
        while queue:
            value = queue.pop()
            x, y = value % width, value // width
            for nx in range(max(0, x - 1), min(width, x + 2)):
                for ny in range(max(0, y - 1), min(height, y + 2)):
                    adjacent = ny * width + nx
                    if adjacent in ink:
                        ink.remove(adjacent)
                        queue.append(adjacent)
                        found.append(adjacent)
        xs, ys = [v % width for v in found], [v // width for v in found]
        if len(found) >= 2:
            components.append({"bbox": [min(xs), min(ys), max(xs) + 1, max(ys) + 1], "area": len(found)})
    components.sort(key=lambda row: (row["bbox"][0], row["bbox"][1]))
    tallest = max((c["bbox"][3] - c["bbox"][1] for c in components), default=0)
    tall = [c for c in components if c["bbox"][3] - c["bbox"][1] >= tallest * 0.65]
    decimal, minus, percent, parentheses = [], [], [], []
    for component in components:
        left, top, right, bottom = component["bbox"]
        cw, ch = right - left, bottom - top
        if tallest and ch <= tallest * 0.30 and cw <= tallest * 0.30:
            before = [c for c in tall if c["bbox"][2] <= left]
            after = [c for c in tall if c["bbox"][0] >= right]
            if before and after:
                neighbors = [max(before, key=lambda c: c["bbox"][2]), min(after, key=lambda c: c["bbox"][0])]
                baseline = sum(c["bbox"][3] for c in neighbors) / 2
                if baseline - tallest * 0.27 <= (top + bottom) / 2 <= baseline + tallest * 0.16:
                    decimal.append(component["bbox"])
        if tallest and cw >= ch * 2.2 and ch <= tallest * 0.30 and tall:
            first = min(tall, key=lambda c: c["bbox"][0])
            if right <= first["bbox"][0] and first["bbox"][1] + tallest * 0.18 <= (top + bottom) / 2 <= first["bbox"][3] - tallest * 0.18:
                minus.append(component["bbox"])
    # A printed percent glyph contains two small round components straddling
    # a thin diagonal. Use actual connected ink, not a '%' from OCR output.
    for slash in components:
        left, top, right, bottom = slash["bbox"]
        sw, sh = right - left, bottom - top
        if not tallest or sh < tallest * 0.60 or sw > sh * 0.80 or slash["area"] / max(1, sw * sh) >= 0.35:
            continue
        circles = []
        for candidate in components:
            if candidate is slash:
                continue
            x0, y0, x1, y1 = candidate["bbox"]
            cw, ch = x1 - x0, y1 - y0
            if tallest * 0.24 <= ch <= tallest * 0.61 and 0.65 <= cw / max(1, ch) <= 1.45 and 0.16 <= candidate["area"] / max(1, cw * ch) <= 0.85:
                circles.append(candidate)
        upper = [c for c in circles if c["bbox"][0] < left and c["bbox"][2] <= right and c["bbox"][1] <= top + sh * 0.30 and c["bbox"][3] < top + sh * 0.65]
        lower = [c for c in circles if c["bbox"][2] > right and c["bbox"][0] >= left and c["bbox"][1] > top + sh * 0.35 and c["bbox"][3] >= bottom - sh * 0.30]
        if upper and lower:
            a, b = max(upper, key=lambda c: c["bbox"][0]), min(lower, key=lambda c: c["bbox"][0])
            if left - a["bbox"][0] <= sh * 0.55 and b["bbox"][2] - right <= sh * 0.55:
                percent.append([a["bbox"][0], min(top, a["bbox"][1]), b["bbox"][2], max(bottom, b["bbox"][3])])
    narrow = [c for c in components if c["bbox"][3] - c["bbox"][1] >= tallest * 0.92
              and (c["bbox"][2] - c["bbox"][0]) / max(1, c["bbox"][3] - c["bbox"][1]) <= 0.28]
    for left in narrow:
        for right in narrow:
            if left is right or right["bbox"][0] <= left["bbox"][2]:
                continue
            enclosed = [c for c in components if c["bbox"][0] > left["bbox"][2] and c["bbox"][2] < right["bbox"][0]
                        and c["bbox"][3] - c["bbox"][1] >= tallest * 0.60]
            if enclosed and abs(left["bbox"][1] - right["bbox"][1]) <= tallest * 0.10 and abs(left["bbox"][3] - right["bbox"][3]) <= tallest * 0.10:
                parentheses.append([left["bbox"][0], left["bbox"][1], right["bbox"][2], right["bbox"][3]])
    return {"width": width, "height": height, "pixel_sha256": _sha(image.convert("RGB").tobytes()),
            "threshold": 160, "components": components, "decimal_marks": decimal, "minus_marks": minus,
            "percent_marks": percent, "parentheses_marks": parentheses}


def _punctuation_reason(literal: str, witness: dict[str, Any]) -> str | None:
    normalized = normalize_number(literal)
    decimal = bool(re.search(r"\d\.\d", normalized))
    # Commas may be decimal or grouping punctuation; no locale conversion is
    # performed. Both are preserved by OCR consensus and source crops.
    if decimal and not witness["decimal_marks"]:
        return "decimal_not_visible"
    if not decimal and len(witness["decimal_marks"]) > literal.count(","):
        return "visible_decimal_omitted"
    if witness["minus_marks"] and not normalized.startswith("-"):
        return "visible_minus_omitted"
    if witness["parentheses_marks"] and not normalized.startswith("-"):
        return "visible_negative_parentheses_omitted"
    if normalized.startswith("-") and "(" not in literal and not witness["minus_marks"]:
        return "minus_not_visible"
    if "(" in literal and not witness["parentheses_marks"]:
        return "negative_parentheses_not_visible"
    if "%" in normalized and not witness["percent_marks"]:
        return "percent_not_visible"
    if "%" not in normalized and witness["percent_marks"]:
        return "visible_percent_omitted"
    return None


def _source_crop_hits(numbers: list[dict[str, Any]], source_box: list[float]) -> tuple[list[dict[str, Any]], bool]:
    """Reject boxes spanning other mosaic rows; never truncate a crop count.

    The old minimum-area overlap can be 1 for a huge candidate containing a
    tiny crop. At least 95% of a candidate's own area must also lie inside its
    source crop. Count the old positional candidates up to the overflow trigger
    so pathological OCR still gets one bounded, isolated source-pixel read.
    """
    hits, candidate_count = [], 0
    for row in numbers:
        box = row["bbox"]
        if _overlap(source_box, box) < 0.95:
            continue
        candidate_count += 1
        if candidate_count > MAX_FIELDS:
            return [], True
        intersection = (max(0.0, min(source_box[2], box[2]) - max(source_box[0], box[0]))
                        * max(0.0, min(source_box[3], box[3]) - max(source_box[1], box[1])))
        candidate_area = max(0.01, (box[2] - box[0]) * (box[3] - box[1]))
        if intersection / candidate_area >= 0.95:
            hits.append(row)
    return hits, False


def _isolated_canvas(crop: Image.Image) -> Image.Image:
    if (crop.width + 2 * ISOLATED_PADDING) * (crop.height + 2 * ISOLATED_PADDING) > MAX_IMAGE_PIXELS:
        raise NumericEvidenceError("Numeric OCR image exceeds the pixel bound")
    canvas = Image.new("RGB", (crop.width + 2 * ISOLATED_PADDING, crop.height + 2 * ISOLATED_PADDING), "white")
    canvas.paste(crop, (ISOLATED_PADDING, ISOLATED_PADDING))
    return canvas


def _overflow_recovery_metadata(crop: Image.Image, canvas: Image.Image, psm: int) -> str:
    buffer = io.BytesIO()
    crop.save(buffer, format="PNG")
    raw = buffer.getvalue()
    if len(raw) > MAX_RECOVERY_PNG_BYTES:
        raise NumericEvidenceError("Numeric OCR image exceeds the pixel bound")
    value = {"schema": 1, "policy": OVERFLOW_RECOVERY_POLICY, "trigger": "mosaic-field-count-overflow",
             "mosaic_field_count_lower_bound": MAX_FIELDS + 1, "psm": psm,
             "padding_pixels": ISOLATED_PADDING,
             "crop_pixel_sha256": _sha(crop.tobytes()), "crop_png_base64": base64.b64encode(raw).decode("ascii"),
             "isolated_canvas_size": list(canvas.size), "isolated_canvas_pixel_sha256": _sha(canvas.tobytes()),
             "isolated_source_bbox": [ISOLATED_PADDING, ISOLATED_PADDING,
                                       ISOLATED_PADDING + crop.width, ISOLATED_PADDING + crop.height]}
    # Keep the raw canonical metadata available for strict duplicate-key
    # checking even when a legacy caller has already decoded the outer receipt.
    return _canonical(value).decode("utf-8")


def _validate_overflow_recovery(read: dict[str, Any], expected_size: list[int]) -> None:
    if "crop_read_recovery" not in read:
        return
    raw_metadata = read["crop_read_recovery"]
    def invalid():
        raise NumericEvidenceError("Numeric crop reads differ from their common source pixels")
    def unique_pairs(pairs):
        value = {}
        for key, item in pairs:
            if key in value:
                invalid()
            value[key] = item
        return value
    if (not isinstance(raw_metadata, str)
            or len(raw_metadata) > ((MAX_RECOVERY_PNG_BYTES + 2) // 3) * 4 + 4096):
        invalid()
    try:
        value = json.loads(raw_metadata, object_pairs_hook=unique_pairs,
                           parse_constant=lambda _: invalid())
        keys = {"schema", "policy", "trigger", "mosaic_field_count_lower_bound", "psm", "padding_pixels",
                "crop_pixel_sha256", "crop_png_base64", "isolated_canvas_size",
                "isolated_canvas_pixel_sha256", "isolated_source_bbox"}
        if not isinstance(value, dict) or set(value) != keys:
            invalid()
        encoded = value["crop_png_base64"]
        if not isinstance(encoded, str) or len(encoded) > ((MAX_RECOVERY_PNG_BYTES + 2) // 3) * 4:
            invalid()
        raw = base64.b64decode(encoded, validate=True)
        if (not 1 <= len(raw) <= MAX_RECOVERY_PNG_BYTES
                or base64.b64encode(raw).decode("ascii") != encoded
                or not raw.startswith(b"\x89PNG\r\n\x1a\n")):
            invalid()
        # Reject ancillary/covert chunks and trailing bytes. Bounds and format
        # are checked before Pillow expands any compressed source pixels.
        cursor, chunks = 8, []
        while cursor < len(raw):
            if cursor + 12 > len(raw):
                invalid()
            length = int.from_bytes(raw[cursor:cursor + 4], "big")
            end = cursor + 12 + length
            kind = raw[cursor + 4:cursor + 8]
            if (end > len(raw) or kind not in {b"IHDR", b"IDAT", b"IEND"}
                    or binascii.crc32(raw[cursor + 4:end - 4]) & 0xffffffff
                    != int.from_bytes(raw[end - 4:end], "big")):
                invalid()
            if kind == b"IHDR" and (length != 13 or raw[cursor + 16:cursor + 21] != b"\x08\x02\x00\x00\x00"):
                invalid()
            if kind == b"IEND" and length != 0:
                invalid()
            chunks.append(kind)
            cursor = end
        if (not chunks or chunks[0] != b"IHDR" or chunks[-1] != b"IEND"
                or chunks.count(b"IHDR") != 1 or chunks.count(b"IEND") != 1 or b"IDAT" not in chunks):
            invalid()
        header_size = [int.from_bytes(raw[16:20], "big"), int.from_bytes(raw[20:24], "big")]
        if header_size != expected_size or min(header_size) <= 0 or header_size[0] * header_size[1] > MAX_IMAGE_PIXELS:
            invalid()
        with Image.open(io.BytesIO(raw)) as image:
            if (image.format != "PNG" or image.mode != "RGB" or list(image.size) != expected_size
                    or image.width * image.height > MAX_IMAGE_PIXELS or image.info
                    or getattr(image, "n_frames", 1) != 1):
                invalid()
            image.load()
            crop = image.copy()
        canvas = _isolated_canvas(crop)
        if canvas.width * canvas.height > MAX_IMAGE_PIXELS:
            invalid()
        expected = {"schema": 1, "policy": OVERFLOW_RECOVERY_POLICY, "trigger": "mosaic-field-count-overflow",
                    "mosaic_field_count_lower_bound": MAX_FIELDS + 1,
                    "psm": 6 if read.get("method") == "source-crop-psm-6" else 11,
                    "padding_pixels": ISOLATED_PADDING,
                    "crop_pixel_sha256": _sha(crop.tobytes()), "crop_png_base64": encoded,
                    "isolated_canvas_size": list(canvas.size),
                    "isolated_canvas_pixel_sha256": _sha(canvas.tobytes()),
                    "isolated_source_bbox": [ISOLATED_PADDING, ISOLATED_PADDING,
                                              ISOLATED_PADDING + crop.width, ISOLATED_PADDING + crop.height]}
        if (_canonical(value).decode("utf-8") != raw_metadata or _canonical(value) != _canonical(expected)
                or value["crop_pixel_sha256"] != read.get("input_pixel_sha256")):
            invalid()
    except NumericEvidenceError:
        raise
    except (ValueError, TypeError, KeyError, OSError, OverflowError, Image.DecompressionBombError) as exc:
        raise NumericEvidenceError("Numeric crop reads differ from their common source pixels") from exc


def _crop_reads(page: fitz.Page, positioned: dict[int, dict[str, Any]], *, language: str,
                tessdata: str | None, command: str) -> dict[int, list[dict[str, Any]]]:
    result = {}
    items = list(positioned.items())
    for offset in range(0, len(items), CROP_BATCH):
        crops = []
        for index, row in items[offset:offset + CROP_BATCH]:
            clip = _ocr_crop_clip(row["bbox"], [float(page.rect.width), float(page.rect.height)])
            crop = _image(page.get_pixmap(dpi=CROP_DPI, clip=fitz.Rect(clip), colorspace=fitz.csRGB, alpha=False))
            crops.append((index, crop, clip))
        if not crops:
            continue
        # Isolated fields are placed on separate rows, retaining all source
        # symbols. This batches expensive engine startup without merging table
        # columns or changing their number-to-position correspondence.
        mosaic = Image.new("RGB", (max(crop.width for _, crop, _ in crops) + 48,
                                   sum(crop.height + 48 for _, crop, _ in crops) + 24), "white")
        locations = []
        top = 24
        for index, crop, clip in crops:
            mosaic.paste(crop, (24, top))
            locations.append((index, [24, top, 24 + crop.width, top + crop.height], crop, clip, _sha(crop.tobytes())))
            top += crop.height + 48
        for psm in (6, 11):
            words = _read_tesseract(mosaic, language=language, tessdata=tessdata, command=command,
                                    psm=psm, dpi=CROP_DPI)
            numbers = _word_mentions(words)
            for index, box, crop, clip, crop_hash in locations:
                hits, overflow = _source_crop_hits(numbers, box)
                recovery = None
                if overflow:
                    canvas = _isolated_canvas(crop)
                    isolated_words = _read_tesseract(canvas, language=language, tessdata=tessdata, command=command,
                                                     psm=psm, dpi=CROP_DPI)
                    isolated_box = [ISOLATED_PADDING, ISOLATED_PADDING,
                                    ISOLATED_PADDING + crop.width, ISOLATED_PADDING + crop.height]
                    hits, still_overflow = _source_crop_hits(_word_mentions(isolated_words), isolated_box)
                    if still_overflow:
                        raise NumericEvidenceError("Numeric source page exceeds the field bound")
                    recovery = _overflow_recovery_metadata(crop, canvas, psm)
                read = {"method": f"source-crop-psm-{psm}", "dpi": CROP_DPI,
                                                      "literal": hits[0]["literal"] if len(hits) == 1 else None,
                                                      "field_count": len(hits),
                                                      "input_pixel_sha256": crop_hash,
                                                      "crop_policy": OCR_CROP_POLICY,
                                                      "source_clip_bbox": clip,
                                                      "crop_pixel_size": [crop.width, crop.height]}
                if recovery is not None:
                    read["crop_read_recovery"] = recovery
                result.setdefault(index, []).append(read)
    return result


def _replacement(index: int) -> str:
    return f"[数值待核对:n{index + 1:04d}]"


def _apply(primary_text: str, records: list[dict[str, Any]]) -> str:
    chunks, previous = [], 0
    for record in records:
        chunks += [primary_text[previous:record["begin"]], record["safe_literal"]]
        previous = record["end"]
    chunks.append(primary_text[previous:])
    return "".join(chunks)


def _supplemental_markers(fields: list[dict[str, Any]]) -> str:
    if not fields:
        return ""
    return "\n\n整页复核发现第一轮漏识数值字段；其原页位置及识别候选保留在来源证据中，以下字段尚待核对：\n" + " ".join(field["safe_literal"] for field in fields)


def audit_numeric_evidence(page: fitz.Page, primary_text: str, *, primary_words: Iterable[Any] | None = None,
                           language: str = "eng+chi_sim", tessdata: str | Path | None = None,
                           tesseract_command: str | None = None) -> dict[str, Any]:
    if not isinstance(primary_text, str) or not isinstance(language, str) or not re.fullmatch(r"[a-z_]+(?:\+[a-z_]+)*", language):
        raise NumericEvidenceError("Numeric audit text or language is invalid")
    primary = numeric_mentions(primary_text)
    if len(primary) > MAX_FIELDS:
        raise NumericEvidenceError("Numeric source page exceeds the field bound")
    source_image = _image(page.get_pixmap(dpi=SOURCE_DPI, colorspace=fitz.csRGB, alpha=False))
    source_hash = _sha(source_image.tobytes())
    size = [float(page.rect.width), float(page.rect.height)]
    records, supplemental, second = [], [], []
    runtime = {"engine": "tesseract-cli", "language": language, "second_page_dpi": SECOND_DPI,
               "crop_dpi": CROP_DPI, "crop_psm": [6, 11], "confidence_used_for_acceptance": False}
    # Even a first transcript containing no numbers can have omitted an entire
    # financial table. Independently inspect every non-white source image.
    nonwhite_source = any(extreme != (255, 255) for extreme in source_image.getextrema())
    if primary or nonwhite_source:
        command = tesseract_command or shutil.which("tesseract")
        if not command:
            raise NumericEvidenceError("Tesseract CLI is required for numeric verification")
        directory = str(tessdata) if tessdata else None
        if primary_words is None and primary:
            words = _read_tesseract(source_image, language=language, tessdata=directory, command=command, psm=3, dpi=SOURCE_DPI)
            primary_words = [{**word, "bbox": [value * 72 / SOURCE_DPI for value in word["bbox"]]} for word in words]
        positioned = _align_mentions(primary, _word_mentions(primary_words or []))
        second_image = _image(page.get_pixmap(dpi=SECOND_DPI, colorspace=fitz.csRGB, alpha=False))
        second_words = _read_tesseract(second_image, language=language, tessdata=directory,
                                      command=command, psm=3, dpi=SECOND_DPI)
        second_pixel_hash = _sha(second_image.tobytes())
        second = _word_mentions([{**word, "bbox": [value * 72 / SECOND_DPI for value in word["bbox"]]} for word in second_words])
        crop_reads = _crop_reads(page, positioned, language=language, tessdata=directory, command=command)
        for index, mention in enumerate(primary):
            record = {"id": f"n{index + 1:04d}", **mention, "safe_literal": _replacement(index),
                      "status": "unresolved", "reason": "source_position_unresolved", "bbox": None,
                      "source_pixel_bbox": None, "pixel_punctuation": None, "reads": []}
            if index in positioned:
                box = positioned[index]["bbox"]
                pixel_box = _pixel_box(box, source_image, size)
                witness = pixel_punctuation(source_image.crop(tuple(pixel_box)))
                at = _at_position(box, second)
                reads = [{"method": "second-page-psm-3", "dpi": SECOND_DPI,
                          "literal": at["literal"] if at else None, "bbox": at["bbox"] if at else None,
                          "input_pixel_sha256": second_pixel_hash}] + crop_reads.get(index, [])
                record.update({"bbox": box, "source_pixel_bbox": pixel_box, "pixel_punctuation": witness, "reads": reads,
                               "reason": "positioned_reads_disagree"})
                values = [normalize_number(read["literal"]) for read in reads if read["literal"] is not None]
                if len(reads) == len(values) == 3 and len(set(values)) == 1:
                    literal = reads[1]["literal"]
                    reason = _punctuation_reason(literal, witness)
                    if reason:
                        record["reason"] = reason
                    else:
                        original_notation_valid = values[0] == mention["normalized"] and _punctuation_reason(mention["literal"], witness) is None
                        record.update({"safe_literal": mention["literal"] if original_notation_valid else literal,
                                       "status": "verified" if values[0] == mention["normalized"] else "corrected",
                                       "reason": "three_positioned_reads_and_source_marks"})
            records.append(record)
        # A first-pass transcript is not a complete numeric inventory. Detect
        # numbers found in the separate whole-page read which have no source
        # position in the first transcript; retain their candidates and pixels
        # explicitly instead of silently omitting them from the source receipt.
        for candidate in second:
            if any(_overlap(candidate["bbox"], value["bbox"]) >= 0.55 for value in positioned.values()):
                continue
            box = _pixel_box(candidate["bbox"], source_image, size)
            index = len(supplemental) + 1
            supplemental.append({"id": f"s{index:04d}", "literal": candidate["literal"],
                                 "normalized": candidate["normalized"], "bbox": candidate["bbox"],
                                 "safe_literal": f"[漏识数值待核对:s{index:04d}]", "status": "unresolved",
                                 "reason": "not_present_in_primary_transcript", "source_pixel_bbox": box,
                                 "pixel_punctuation": pixel_punctuation(source_image.crop(tuple(box)))})
    safe_text = _apply(primary_text, records) + _supplemental_markers(supplemental)
    evidence = {"schema": SCHEMA, "primary_text": primary_text, "primary_text_sha256": _sha(primary_text.encode()),
                "safe_text_sha256": _sha(safe_text.encode()), "input_pixel_sha256": source_hash,
                "page_size_points": size, "source_image_size": [source_image.width, source_image.height],
                "source_dpi": SOURCE_DPI, "runtime": runtime, "source_num_count": len(records),
                "verified_count": sum(record["status"] == "verified" for record in records),
                "corrected_count": sum(record["status"] == "corrected" for record in records),
                "unresolved_count": sum(record["status"] == "unresolved" for record in records), "records": records,
                "secondary_only_count": len(supplemental), "secondary_only_fields": supplemental,
                "observed_num_count": len(records) + len(supplemental),
                "second_page_fields": [{"literal": row["literal"], "normalized": row["normalized"], "bbox": row["bbox"]} for row in second]}
    evidence["evidence_sha256"] = _sha(_canonical(evidence))
    validate_numeric_evidence(safe_text, evidence, source_hash)
    return {"safe_text": safe_text, "evidence": evidence}


def validate_numeric_evidence(safe_text: str, evidence: dict[str, Any], image_pixel_sha256: str,
                              *, image_path: str | Path | None = None) -> None:
    """Rebuild the admitted transcript and, when present, its actual pixel marks."""
    if not isinstance(evidence, dict) or evidence.get("schema") != SCHEMA or evidence.get("source_dpi") != SOURCE_DPI:
        raise NumericEvidenceError("Numeric evidence schema is invalid")
    unsigned = {key: value for key, value in evidence.items() if key != "evidence_sha256"}
    if evidence.get("evidence_sha256") != _sha(_canonical(unsigned)):
        raise NumericEvidenceError("Numeric evidence digest mismatch")
    primary_text = evidence.get("primary_text")
    if not isinstance(primary_text, str) or evidence.get("primary_text_sha256") != _sha(primary_text.encode()):
        raise NumericEvidenceError("Numeric evidence original transcript mismatch")
    if evidence.get("input_pixel_sha256") != image_pixel_sha256 or not re.fullmatch(r"[a-f0-9]{64}", image_pixel_sha256):
        raise NumericEvidenceError("Numeric evidence is not bound to the source page")
    if evidence.get("safe_text_sha256") != _sha(safe_text.encode()):
        raise NumericEvidenceError("Numeric evidence summary transcript mismatch")
    records = evidence.get("records")
    mentions = numeric_mentions(primary_text)
    if not isinstance(records, list) or len(records) != len(mentions) or len(records) > MAX_FIELDS:
        raise NumericEvidenceError("Numeric evidence omitted source fields")
    source_image = None
    if image_path is not None:
        path = Path(image_path)
        if path.is_symlink() or not path.is_file():
            raise NumericEvidenceError("Numeric evidence original image is unavailable")
        with Image.open(path) as image:
            source_image = image.convert("RGB")
        if source_image.width * source_image.height > MAX_IMAGE_PIXELS or _sha(source_image.tobytes()) != image_pixel_sha256:
            raise NumericEvidenceError("Numeric evidence original pixels mismatch")
        if list(source_image.size) != evidence.get("source_image_size"):
            raise NumericEvidenceError("Numeric evidence original image size mismatch")
    def validate_crop(field):
        box, witness = field.get("source_pixel_bbox"), field.get("pixel_punctuation")
        point_box = field.get("bbox")
        if not isinstance(point_box, list) or len(point_box) != 4 or not all(isinstance(value, (int, float)) and math.isfinite(value) for value in point_box):
            raise NumericEvidenceError("Numeric evidence source position is invalid")
        if not isinstance(box, list) or len(box) != 4 or not all(type(value) is int for value in box) or box[2] <= box[0] or box[3] <= box[1]:
            raise NumericEvidenceError("Numeric evidence field pixels are invalid")
        if source_image is not None and (min(box) < 0 or box[2] > source_image.width or box[3] > source_image.height
                                         or box != _pixel_box(point_box, source_image, evidence["page_size_points"])
                                         or pixel_punctuation(source_image.crop(tuple(box))) != witness):
            raise NumericEvidenceError("Numeric evidence source punctuation mismatch")
    def validate_ocr_crop_reads(record):
        reads = record.get("reads")
        metadata = {"crop_policy", "source_clip_bbox", "crop_pixel_size"}
        if not isinstance(reads, list) or not any(isinstance(read, dict) and metadata.intersection(read) for read in reads):
            # Immutable old R2 receipts used the original wider crops and did
            # not record this geometry. Keep their existing acceptance gate.
            return
        if (len(reads) != 3 or any(not isinstance(read, dict) for read in reads)
                or [read.get("method") for read in reads] != ["second-page-psm-3", "source-crop-psm-6", "source-crop-psm-11"]):
            raise NumericEvidenceError("Numeric crop evidence has insufficient positioned reads")
        expected = _ocr_crop_clip(record.get("bbox"), evidence.get("page_size_points"))
        expected_size = _ocr_crop_pixel_size(expected)
        for read in reads[1:]:
            clip, size = read.get("source_clip_bbox"), read.get("crop_pixel_size")
            field_count = read.get("field_count")
            count_kind = ("missing" if "field_count" not in read else "null" if field_count is None else
                          "boolean" if type(field_count) is bool else "integer" if type(field_count) is int else "other")
            checks = {
                "policy_matches": read.get("crop_policy") == OCR_CROP_POLICY,
                "dpi_matches": type(read.get("dpi")) is int and read["dpi"] == CROP_DPI,
                "clip_valid": (isinstance(clip, list) and len(clip) == 4
                               and all(type(value) in (int, float) and math.isfinite(value) for value in clip)),
                "clip_matches": clip == expected,
                "size_valid": isinstance(size, list) and len(size) == 2 and all(type(value) is int for value in size),
                "size_matches": size == expected_size,
                "field_count_valid": type(read.get("field_count")) is int and 0 <= read["field_count"] <= MAX_FIELDS,
                "input_hash_valid": (isinstance(read.get("input_pixel_sha256"), str)
                                     and re.fullmatch(r"[a-f0-9]{64}", read["input_pixel_sha256"]) is not None),
            }
            if not all(checks.values()):
                raise NumericEvidenceError("Numeric crop geometry differs from its positioned source field", diagnostics={
                    "schema": 1, "record_id": record.get("id"),
                    "psm": 6 if read.get("method") == "source-crop-psm-6" else 11,
                    "field_bbox": record.get("bbox"), "page_bounds": [0, 0, *evidence["page_size_points"]],
                    "expected_clip_bbox": expected, "actual_clip_bbox": clip,
                    "expected_pixel_size": expected_size, "actual_pixel_size": size,
                    "dpi": read.get("dpi"), "field_count": read.get("field_count"),
                    "field_count_kind": count_kind,
                    "field_count_above_bound": type(field_count) is int and field_count > MAX_FIELDS,
                    "field_count_capped_count": max(0, min(MAX_FIELDS, field_count)) if type(field_count) is int else None,
                    "pymupdf_version": fitz.VersionBind, **checks,
                })
            _validate_overflow_recovery(read, expected_size)
            if record.get("status") in {"verified", "corrected"} and read["field_count"] != 1:
                raise NumericEvidenceError("Numeric crop borrowed multiple source fields")
        if reads[1]["input_pixel_sha256"] != reads[2]["input_pixel_sha256"]:
            raise NumericEvidenceError("Numeric crop reads differ from their common source pixels")
    counts = {"verified": 0, "corrected": 0, "unresolved": 0}
    for index, (record, mention) in enumerate(zip(records, mentions)):
        if not isinstance(record, dict) or any(record.get(key) != value for key, value in mention.items()) or record.get("id") != f"n{index + 1:04d}":
            raise NumericEvidenceError("Numeric evidence field mapping mismatch")
        status = record.get("status")
        if status not in counts or not isinstance(record.get("safe_literal"), str):
            raise NumericEvidenceError("Numeric evidence field decision is invalid")
        counts[status] += 1
        box, witness, reads = record.get("source_pixel_bbox"), record.get("pixel_punctuation"), record.get("reads")
        if record.get("bbox") is not None:
            validate_crop(record)
        validate_ocr_crop_reads(record)
        if status == "unresolved":
            if record["safe_literal"] != _replacement(index):
                raise NumericEvidenceError("An unverified numeric field entered the summary")
        else:
            if not isinstance(reads, list) or len(reads) != 3 or [read.get("method") for read in reads] != ["second-page-psm-3", "source-crop-psm-6", "source-crop-psm-11"]:
                raise NumericEvidenceError("Numeric evidence has insufficient positioned reads")
            if any(not isinstance(read.get("literal"), str) or not re.fullmatch(r"[a-f0-9]{64}", read.get("input_pixel_sha256", "")) for read in reads):
                raise NumericEvidenceError("Numeric evidence read is invalid")
            values = [normalize_number(read["literal"]) for read in reads]
            if len(set(values)) != 1 or normalize_number(record["safe_literal"]) != values[0] or witness is None or _punctuation_reason(record["safe_literal"], witness):
                raise NumericEvidenceError("Numeric evidence admitted a conflicting field")
            if (status == "verified") != (mention["normalized"] == values[0]) or record.get("reason") != "three_positioned_reads_and_source_marks":
                raise NumericEvidenceError("Numeric evidence correction classification mismatch")
            if record.get("bbox") is None or not isinstance(reads[0].get("bbox"), list) or _overlap(record["bbox"], reads[0]["bbox"]) < 0.55:
                raise NumericEvidenceError("Numeric evidence borrowed another table field")
    if evidence.get("source_num_count") != len(records) or any(evidence.get(f"{status}_count") != count for status, count in counts.items()):
        raise NumericEvidenceError("Numeric evidence field totals mismatch")
    supplemental, second_fields = evidence.get("secondary_only_fields"), evidence.get("second_page_fields")
    if not isinstance(supplemental, list) or not isinstance(second_fields, list) or evidence.get("secondary_only_count") != len(supplemental) or evidence.get("observed_num_count") != len(records) + len(supplemental):
        raise NumericEvidenceError("Numeric evidence secondary inventory mismatch")
    expected_extra = []
    for field in second_fields:
        if not isinstance(field, dict) or not isinstance(field.get("literal"), str) or field.get("normalized") != normalize_number(field["literal"]):
            raise NumericEvidenceError("Numeric evidence secondary field is invalid")
        box = field.get("bbox")
        if not isinstance(box, list) or len(box) != 4 or not all(isinstance(value, (int, float)) and math.isfinite(value) for value in box):
            raise NumericEvidenceError("Numeric evidence secondary position is invalid")
        if not any(record["bbox"] is not None and _overlap(box, record["bbox"]) >= 0.55 for record in records):
            expected_extra.append(field)
    if len(expected_extra) != len(supplemental):
        raise NumericEvidenceError("Numeric evidence omitted secondary-only fields")
    for index, (extra, field) in enumerate(zip(expected_extra, supplemental), start=1):
        if not isinstance(field, dict) or any(field.get(key) != extra[key] for key in ("literal", "normalized", "bbox")) or field.get("id") != f"s{index:04d}" or field.get("safe_literal") != f"[漏识数值待核对:s{index:04d}]" or field.get("status") != "unresolved" or field.get("reason") != "not_present_in_primary_transcript":
            raise NumericEvidenceError("Numeric evidence secondary decision is invalid")
        validate_crop(field)
    if _apply(primary_text, records) + _supplemental_markers(supplemental) != safe_text:
        raise NumericEvidenceError("Numeric evidence cannot reproduce the summary transcript")
