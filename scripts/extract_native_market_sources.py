#!/usr/bin/env python3
"""Extract a complete, manifest-bound Market Views source batch from local PDFs.

This fallback prefers readable native text, then uses local Tesseract OCR via
PyMuPDF. It makes no provider submission, network request or model call. Every
original and page remains bound to the complete manifest, including duplicate
file aliases and provably white pages. Transferred receipts need no originals.
"""
from __future__ import annotations

import argparse
from collections import Counter
import copy
from datetime import datetime
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from typing import Any, Callable

import fitz


SCHEMA = 2
MANIFEST_NAME = "selected_to_process_manifest.json"
RECEIPT_NAME = "source_receipt.json"
MARKDOWN_NAME = "source_native_pdf.md"
MIN_PAGE_CHARACTERS = 40
MIN_TABLE_CHARACTERS = 24
MIN_SPARSE_OCR_CHARACTERS = 12
MIN_REPORT_CHARACTERS = 600
PAGE_DPI = 300
OCR_LANGUAGES = "eng+chi_sim"
READABILITY_POLICY = "lexical-and-table-v2"
SPARSE_OCR_SUBTYPE = "sparse-structural-ocr-v1"
OCR_TEXT_LAYOUT_POLICY = "same-textpage-source-flow-v1"
OCR_RECOGNITION_POLICY = "full-page-cli-psm11-after-unreadable-v1"
OCR_ROTATED_AXIS_POLICY = "rotated-axis-regions-v1"
OCR_ROTATED_AXIS_ENGINE = "tesseract-cli-rotated-axis"
MAX_ALTERNATE_WORDS = 20_000
MAX_ALTERNATE_TEXT_BYTES = 1_000_000
LATIN_WORD = re.compile(r"[A-Za-z]+(?:['’][A-Za-z]+)*")
LONG_ASCII_RUN = re.compile(r"[A-Za-z0-9]{25,}")
NUMBER_TOKEN = re.compile(r"(?<![A-Za-z0-9])[-+]?\d+(?:[.,]\d+)*(?:%|bps)?(?![A-Za-z0-9])")
PENDING_NUMERIC_MARKER = re.compile(r"\[(?:漏识)?数值待核对:[ns]\d+\]")
CAPTION_INDEX = r"(?:\d+|\[(?:漏识)?数值待核对:[ns]\d{4}\])[A-Za-z]?"
EXHIBIT_CAPTION = re.compile(
    rf"^\s*((?:Figure|Fig\.?|Chart|Table|Exhibit)\s+{CAPTION_INDEX}"
    rf"[\s:：.\-–—]+\S.{{2,}}|(?:图表|图|表)\s*{CAPTION_INDEX}[\s:：.\-–—]*\S.{{2,}})\s*$",
    re.I,
)


class SourceValidationError(ValueError):
    """The complete source contract is not satisfied."""

    def __init__(self, message: str, *, category: str | None = None, geometry_diagnostics=None,
                 rotated_axis_diagnostics=None):
        super().__init__(message)
        self.category = category
        self.geometry_diagnostics = geometry_diagnostics
        self.rotated_axis_diagnostics = rotated_axis_diagnostics


# Only these exact engine messages may become public diagnostic categories.
# Unknown exception text can contain source text, paths or signed URLs.
NUMERIC_FAILURE_MESSAGES = {
    "Numeric audit requires RGB source rendering": "numeric_rgb_required",
    "Numeric audit source image exceeds the pixel bound": "numeric_source_pixel_bound",
    "OCR word is missing its source position": "numeric_word_position_missing",
    "OCR word position is invalid": "numeric_word_position_invalid",
    "OCR word position or text is invalid": "numeric_word_text_invalid",
    "Numeric OCR image exceeds the pixel bound": "numeric_ocr_pixel_bound",
    "Numeric verification OCR did not complete": "numeric_ocr_incomplete",
    "Numeric verification OCR failed": "numeric_ocr_failed",
    "Numeric verification OCR returned invalid coordinates": "numeric_ocr_coordinates_invalid",
    "Numeric verification OCR returned invalid TSV": "numeric_ocr_tsv_invalid",
    "Numeric crop geometry is invalid": "numeric_crop_geometry_invalid",
    "Numeric crop is outside the source page": "numeric_crop_outside_page",
    "Numeric audit text or language is invalid": "numeric_text_language_invalid",
    "Numeric source page exceeds the field bound": "numeric_field_bound",
    "Tesseract CLI is required for numeric verification": "numeric_tesseract_cli_missing",
    "Numeric evidence schema is invalid": "numeric_schema_invalid",
    "Numeric evidence digest mismatch": "numeric_digest_mismatch",
    "Numeric evidence original transcript mismatch": "numeric_original_transcript_mismatch",
    "Numeric evidence rotated source proof mismatch": "numeric_rotated_source_proof_mismatch",
    "Numeric evidence is not bound to the source page": "numeric_source_binding_mismatch",
    "Numeric evidence summary transcript mismatch": "numeric_summary_transcript_mismatch",
    "Numeric evidence omitted source fields": "numeric_source_fields_missing",
    "Numeric evidence original image is unavailable": "numeric_original_image_missing",
    "Numeric evidence original pixels mismatch": "numeric_original_pixels_mismatch",
    "Numeric evidence original image size mismatch": "numeric_original_image_size_mismatch",
    "Numeric evidence source position is invalid": "numeric_source_position_invalid",
    "Numeric evidence field pixels are invalid": "numeric_field_pixels_invalid",
    "Numeric evidence source punctuation mismatch": "numeric_punctuation_mismatch",
    "Numeric crop evidence has insufficient positioned reads": "numeric_crop_reads_insufficient",
    "Numeric crop geometry differs from its positioned source field": "numeric_crop_geometry_mismatch",
    "Numeric crop borrowed multiple source fields": "numeric_crop_multiple_fields",
    "Numeric crop reads differ from their common source pixels": "numeric_crop_pixels_mismatch",
    "Numeric evidence field mapping mismatch": "numeric_field_mapping_mismatch",
    "Numeric evidence field decision is invalid": "numeric_field_decision_invalid",
    "An unverified numeric field entered the summary": "numeric_unverified_summary_field",
    "Numeric evidence has insufficient positioned reads": "numeric_reads_insufficient",
    "Numeric evidence read is invalid": "numeric_read_invalid",
    "Numeric evidence admitted a conflicting field": "numeric_conflicting_field",
    "Numeric evidence correction classification mismatch": "numeric_correction_mismatch",
    "Numeric evidence borrowed another table field": "numeric_borrowed_table_field",
    "Numeric evidence field totals mismatch": "numeric_field_totals_mismatch",
    "Numeric evidence secondary inventory mismatch": "numeric_secondary_inventory_mismatch",
    "Numeric evidence secondary field is invalid": "numeric_secondary_field_invalid",
    "Numeric evidence secondary position is invalid": "numeric_secondary_position_invalid",
    "Numeric evidence omitted secondary-only fields": "numeric_secondary_fields_missing",
    "Numeric evidence secondary decision is invalid": "numeric_secondary_decision_invalid",
    "Numeric evidence cannot reproduce the summary transcript": "numeric_summary_reconstruction_mismatch",
}
NUMERIC_FAILURE_CATEGORIES = frozenset(NUMERIC_FAILURE_MESSAGES.values()) | {"numeric_evidence_invalid"}
ROTATED_AXIS_FAILURE_CATEGORIES = frozenset({
    "rotated_axis_proof_invalid", "rotated_axis_not_eligible", "rotated_axis_time_budget_exhausted",
})


def _numeric_failure_category(error: Exception) -> str:
    category = getattr(error, "category", None)
    if isinstance(category, str) and category in NUMERIC_FAILURE_CATEGORIES:
        return category
    return NUMERIC_FAILURE_MESSAGES.get(str(error), "numeric_evidence_invalid")


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def read_manifest(path: Path, expected_reports: int) -> tuple[bytes, list[dict[str, str]]]:
    if type(expected_reports) is not int or expected_reports <= 0:
        raise SourceValidationError("expected_reports must be a positive integer")
    if path.is_symlink() or not path.is_file():
        raise SourceValidationError("The selected manifest must be a regular file")
    raw = path.read_bytes()
    try:
        rows = json.loads(raw)
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise SourceValidationError("The selected manifest is invalid JSON") from exc
    if not isinstance(rows, list) or len(rows) != expected_reports:
        raise SourceValidationError(f"Manifest must contain exactly {expected_reports} report entries")
    bindings = []
    for row in rows:
        if not isinstance(row, dict):
            raise SourceValidationError("Manifest report entry must be an object")
        local_path = row.get("process_local_path")
        digest = row.get("content_sha256")
        if not isinstance(local_path, str) or not local_path.strip() or "\\" in local_path:
            raise SourceValidationError("Manifest is missing an exact process_local_path")
        name = Path(local_path).name
        if not name or Path(name).suffix.lower() != ".pdf":
            raise SourceValidationError("Manifest process_local_path must name a PDF")
        if not isinstance(digest, str) or not re.fullmatch(r"[a-f0-9]{64}", digest):
            raise SourceValidationError("Manifest is missing a verified PDF content_sha256")
        bindings.append({"source_pdf": name, "content_sha256": digest})
    if len({row["source_pdf"] for row in bindings}) != len(bindings):
        raise SourceValidationError("Manifest contains duplicate PDF basenames")
    return raw, bindings


def meaningful_characters(text: str) -> int:
    return sum(character.isalnum() for character in text)


def _is_han(character: str) -> bool:
    number = ord(character)
    return (0x3400 <= number <= 0x4DBF or 0x4E00 <= number <= 0x9FFF
            or 0xF900 <= number <= 0xFAFF or 0x20000 <= number <= 0x3134F)


def page_readability(text: str, *, allow_sparse_ocr: bool = False) -> dict[str, Any]:
    """Check language and table structure, rather than counting opaque glyphs.

    This is an extraction routing gate, not an assertion of OCR accuracy.
    Chinese does not need spaces; English prose needs several plausible word
    tokens, and financial tables may instead supply short labels and numbers.
    A long ASCII identifier cannot stand in for a page of source prose.
    """
    # An audit annotation is not recognized source language. In particular,
    # repeated Chinese pending markers must not make an unreadable page pass.
    text = PENDING_NUMERIC_MARKER.sub("", text)
    count = meaningful_characters(text)
    bad = sum(character == "\ufffd" or unicodedata.category(character) in {"Co", "Cs", "Cn"}
              or (unicodedata.category(character) == "Cc" and character not in "\n\r\t")
              for character in text)
    folded = "".join(character for character in unicodedata.normalize("NFKD", text)
                     if not unicodedata.combining(character))
    latin_count = sum(character.isascii() and character.isalpha() for character in folded)
    han_count = sum(_is_han(character) for character in text)
    words = [word for word in LATIN_WORD.findall(folded)
             if 2 <= len(word.replace("'", "").replace("’", "")) <= 24
             and (re.search(r"[aeiouy]", word, re.I) or word.isupper() and len(word) <= 8)
             and len(set(word.lower())) >= 2
             and not re.search(r"(.)\1{5,}", word, re.I)]
    word_characters = sum(len(word) for word in words)
    distinct_words = len({word.lower() for word in words})
    long_ascii = sum(len(match.group()) for match in LONG_ASCII_RUN.finditer(text))
    numbers = len(NUMBER_TOKEN.findall(text))
    chinese = han_count >= 8 and han_count / max(1, han_count + latin_count) >= 0.2
    english = (len(words) >= 4 and distinct_words >= 3 and word_characters >= 16
               and word_characters / max(1, latin_count) >= 0.6)
    table = (numbers >= 8 and
             ((len(words) >= 3 and distinct_words >= 3 and word_characters >= 9
               and word_characters / max(1, latin_count) >= 0.6)
              or han_count >= 4 and han_count / max(1, han_count + latin_count) >= 0.2))
    minimum = MIN_TABLE_CHARACTERS if table else MIN_PAGE_CHARACTERS
    reason = ("insufficient_characters" if count < minimum else
              "invalid_unicode" if bad / max(1, len(text)) > 0.02 else
              "opaque_ascii_runs" if long_ascii / max(1, count) > 0.25 else
              "missing_language_or_table_structure" if not (chinese or english or table) else "readable")
    assessment = {"policy": READABILITY_POLICY, "accepted": reason == "readable", "reason": reason,
            "characters": count, "minimum_characters": minimum, "invalid_unicode_characters": bad,
            "han_characters": han_count, "latin_characters": latin_count,
            "plausible_words": len(words), "distinct_plausible_words": distinct_words,
            "plausible_word_characters": word_characters, "long_ascii_characters": long_ascii,
            "numeric_tokens": numbers, "structure": "chinese" if chinese else "english" if english else "table" if table else None}
    # Short section/divider pages still require complete OCR first. This branch
    # never relaxes the native gate, replaces regular evidence, or counts audit
    # annotations as source language. Preserve the original page and numeric
    # evidence even when its only prose is a heading, speaker and page footer.
    sparse_english = (distinct_words >= 3 and word_characters >= 12
                      and word_characters / max(1, latin_count) >= 0.75)
    han_frequencies: dict[str, int] = {}
    for character in text:
        if _is_han(character):
            han_frequencies[character] = han_frequencies.get(character, 0) + 1
    sparse_chinese = (han_count >= 4 and len(han_frequencies) >= 3
                      and max(han_frequencies.values(), default=0) / max(1, han_count) <= 0.6
                      and han_count / max(1, han_count + latin_count) >= 0.6)
    if (allow_sparse_ocr and reason == "insufficient_characters"
            and count >= MIN_SPARSE_OCR_CHARACTERS and bad == 0 and long_ascii == 0
            and (sparse_english or sparse_chinese)):
        assessment.update(accepted=True, reason="readable_sparse_structural_ocr",
                          minimum_characters=MIN_SPARSE_OCR_CHARACTERS,
                          subtype=SPARSE_OCR_SUBTYPE,
                          structure="sparse_ocr_chinese" if sparse_chinese else "sparse_ocr_english")
    return assessment


def require_readable_page(text: str, source_name: str, page_number: int, *,
                          allow_sparse_ocr: bool = False) -> int:
    assessment = page_readability(text, allow_sparse_ocr=allow_sparse_ocr)
    count = assessment["characters"]
    if assessment["reason"] == "insufficient_characters":
        raise SourceValidationError(
            f"{source_name} page {page_number} has insufficient readable page text ({count} characters)"
        )
    if not assessment["accepted"]:
        raise SourceValidationError(
            f"{source_name} page {page_number} has unreadable extracted text ({assessment['reason']})"
        )
    return meaningful_characters(text)


def _ocr_primary_text(ocr: Any) -> str:
    if not isinstance(ocr, dict) or not isinstance(ocr.get("numeric_evidence"), dict):
        raise SourceValidationError("OCR page is missing its recognized source transcript")
    primary = ocr["numeric_evidence"].get("primary_text")
    if not isinstance(primary, str):
        raise SourceValidationError("OCR page is missing its recognized source transcript")
    return primary


def _same_recognized_glyphs(first: str, second: str) -> bool:
    # Preserve punctuation, signs, case and every repeated character. Only
    # whitespace and order may differ between reads of one OCR TextPage.
    return (Counter(character for character in first if not character.isspace())
            == Counter(character for character in second if not character.isspace()))


def _text_layout_record(sorted_text: str, source_flow_text: str) -> dict[str, Any]:
    return {"schema": 1, "policy": OCR_TEXT_LAYOUT_POLICY, "selection": "source-flow",
            "sorted_text": sorted_text,
            "sorted_text_sha256": sha256_bytes(sorted_text.encode("utf-8")),
            "sorted_readability": page_readability(sorted_text, allow_sparse_ocr=True),
            "selected_text_sha256": sha256_bytes(source_flow_text.encode("utf-8")),
            "selected_readability": page_readability(source_flow_text, allow_sparse_ocr=True)}


def _ocr_layout_candidates(page: fitz.Page, textpage: fitz.TextPage, sorted_text: str,
                           number: int) -> tuple[str | None, bool, dict[str, Any] | None, dict[str, Any]]:
    sorted_readability = page_readability(sorted_text, allow_sparse_ocr=True)
    candidates = {"selection": "geometric-sorted", "sorted_readability": sorted_readability}
    if sorted_readability["accepted"]:
        return sorted_text, True, None, candidates
    try:
        source_flow_text = page.get_text("text", textpage=textpage, sort=False).strip()
    except Exception as exc:
        raise SourceValidationError(f"Runner OCR text layout failed at page {number}: ocr_engine_failed",
                                    category="ocr_engine_failed") from exc
    same_glyphs = _same_recognized_glyphs(sorted_text, source_flow_text)
    flow_readability = page_readability(source_flow_text, allow_sparse_ocr=True)
    candidates.update(selection="rejected", source_flow_text=source_flow_text,
                      source_flow_readability=flow_readability, source_flow_same_glyphs=same_glyphs)
    if same_glyphs and flow_readability["accepted"]:
        candidates["selection"] = "source-flow"
        return source_flow_text, False, _text_layout_record(sorted_text, source_flow_text), candidates
    return None, True, None, candidates


def _select_ocr_text_layout(page: fitz.Page, textpage: fitz.TextPage, sorted_text: str,
                            source_name: str, number: int) -> tuple[str, bool, dict[str, Any] | None]:
    selected, selected_sort, record, _ = _ocr_layout_candidates(page, textpage, sorted_text, number)
    if selected is not None:
        return selected, selected_sort, record
    # Neither a changed recognition nor a still-unreadable source-flow read
    # can replace the failed default. Keep the original rejection reason.
    require_readable_page(sorted_text, source_name, number, allow_sparse_ocr=True)
    raise AssertionError("Unreadable OCR layout unexpectedly passed")


def _alternate_words(words: Any, image_size: list[int], page_size: list[float]) -> tuple[str, list[dict[str, Any]]]:
    """Rebuild TSV language and numeric positions with one common line order."""
    if (not isinstance(image_size, list) or len(image_size) != 2
            or any(type(value) is not int or value <= 0 for value in image_size)
            or not isinstance(page_size, list) or len(page_size) != 2
            or any(type(value) not in (int, float) or not math.isfinite(value) or value <= 0 for value in page_size)
            or not isinstance(words, list) or len(words) > MAX_ALTERNATE_WORDS):
        raise SourceValidationError("Alternate OCR words have invalid source geometry")
    lines: dict[tuple[int, int, int], list[dict[str, Any]]] = {}
    positioned = []
    for word in words:
        if (not isinstance(word, dict) or set(word) != {"bbox", "text", "block", "paragraph", "line"}
                or not isinstance(word["bbox"], list) or len(word["bbox"]) != 4
                or any(type(value) is not int for value in word["bbox"])
                or not (0 <= word["bbox"][0] < word["bbox"][2] <= image_size[0]
                        and 0 <= word["bbox"][1] < word["bbox"][3] <= image_size[1])
                or any(type(word[key]) is not int or not 0 <= word[key] <= 10_000_000
                       for key in ("block", "paragraph", "line"))
                or not isinstance(word["text"], str) or not word["text"]
                or any(character.isspace() for character in word["text"])
                or len(word["text"].encode("utf-8")) > MAX_ALTERNATE_TEXT_BYTES):
            raise SourceValidationError("Alternate OCR words have invalid source geometry")
        lines.setdefault((word["block"], word["paragraph"], word["line"]), []).append(word)
        # Invert the actual raster dimensions, including rounded edge pixels.
        positioned.append({**word, "bbox": [value * page_size[index % 2] / image_size[index % 2]
                                              for index, value in enumerate(word["bbox"])]})
    ordered = sorted(lines.values(), key=lambda row: (min(word["bbox"][1] for word in row),
                                                     min(word["bbox"][0] for word in row)))
    text = "\n".join(" ".join(word["text"] for word in sorted(row, key=lambda word: word["bbox"][0]))
                     for row in ordered)
    if len(text.encode("utf-8")) > MAX_ALTERNATE_TEXT_BYTES:
        raise SourceValidationError("Alternate OCR words exceed the transcript bound")
    return text, positioned


def _recognition_record(sorted_text: str, flow_text: str, selected_text: str, words: list[dict[str, Any]],
                        *, pixels: dict[str, Any], page_size: list[float], version: str,
                        models: list[dict[str, str]]) -> dict[str, Any]:
    return {"schema": 1, "policy": OCR_RECOGNITION_POLICY, "selection": "full-page-psm11",
            "default_sorted_text": sorted_text, "default_sorted_text_sha256": sha256_bytes(sorted_text.encode("utf-8")),
            "default_sorted_readability": page_readability(sorted_text, allow_sparse_ocr=True),
            "default_source_flow_text": flow_text, "default_source_flow_text_sha256": sha256_bytes(flow_text.encode("utf-8")),
            "default_source_flow_readability": page_readability(flow_text, allow_sparse_ocr=True),
            "default_same_glyphs": _same_recognized_glyphs(sorted_text, flow_text),
            "engine": "tesseract-cli", "tesseract_version": version, "languages": OCR_LANGUAGES,
            "dpi": PAGE_DPI, "psm": 11, "oem": "default", "output": "tsv", "full_page": True,
            "input_pixel_sha256": pixels["pixel_sha256"], "image_size": [pixels["width"], pixels["height"]],
            "page_size_points": page_size, "traineddata": models, "primary_words": words,
            "selected_text_sha256": sha256_bytes(selected_text.encode("utf-8")),
            "selected_readability": page_readability(selected_text, allow_sparse_ocr=True)}


def _validate_ocr_recognition(page: dict[str, Any], recognized_text: str) -> dict[str, Any] | None:
    ocr = page.get("ocr")
    record = ocr.get("recognition") if isinstance(ocr, dict) else None
    indicator_present = "recognition_selection" in page
    record_present = isinstance(ocr, dict) and "recognition" in ocr
    if not indicator_present and not record_present:
        if isinstance(ocr, dict) and ocr.get("engine") == "tesseract-cli":
            raise SourceValidationError("Alternate OCR recognition is missing its source proof")
        return None  # Existing immutable schema-2 receipts retain their engine.
    image = page.get("original_page")
    try:
        if (page.get("extraction_method") != "ocr" or not isinstance(ocr, dict)
                or ocr.get("engine") != "tesseract-cli" or "text_layout" in ocr
                or "text_layout_selection" in page or not isinstance(record, dict)
                or type(record.get("schema")) is not int or not isinstance(image, dict)
                or not isinstance(record.get("tesseract_version"), str)
                or not re.fullmatch(r"[0-9][0-9A-Za-z.+_-]{0,63}", record["tesseract_version"])):
            raise ValueError("recognition")
        sorted_text, flow_text = record["default_sorted_text"], record["default_source_flow_text"]
        if any(not isinstance(value, str) or len(value.encode("utf-8")) > MAX_ALTERNATE_TEXT_BYTES
               for value in (sorted_text, flow_text)):
            raise ValueError("defaults")
        evidence = ocr["numeric_evidence"]
        if (not isinstance(ocr.get("traineddata"), list)
                or any(not isinstance(model, dict) or set(model) != {"language", "filename", "sha256"}
                       or any(not isinstance(value, str) for value in model.values()) for model in ocr["traineddata"])):
            raise ValueError("models")
        selected, positioned = _alternate_words(record["primary_words"], record["image_size"], record["page_size_points"])
        expected = _recognition_record(sorted_text, flow_text, selected, record["primary_words"],
                                       pixels=image, page_size=evidence["page_size_points"],
                                       version=record["tesseract_version"], models=ocr["traineddata"])
        binding = {"policy": OCR_RECOGNITION_POLICY, "selection": "full-page-psm11",
                   "recognition_sha256": sha256_bytes(canonical_bytes(record))}
        if (canonical_bytes(record) != canonical_bytes(expected)
                or canonical_bytes(page.get("recognition_selection")) != canonical_bytes(binding)
                or selected != recognized_text or record["default_sorted_readability"]["accepted"]
                or record["default_source_flow_readability"]["accepted"]
                or not record["selected_readability"]["accepted"]
                or evidence["input_pixel_sha256"] != image["pixel_sha256"]
                or canonical_bytes(evidence["source_image_size"]) != canonical_bytes(record["image_size"])):
            raise ValueError("binding")
        # A transcript hash alone cannot prove which repeated table value was
        # positioned. Replay the exact producer alignment from transferred TSV.
        from ocr_numeric_evidence import _align_mentions, _word_mentions, numeric_mentions
        aligned = _align_mentions(numeric_mentions(selected), _word_mentions(positioned))
        for index, numerical in enumerate(evidence["records"]):
            expected_box = aligned[index]["bbox"] if index in aligned else None
            if canonical_bytes(numerical["bbox"]) != canonical_bytes(expected_box):
                raise ValueError("word-position")
    except (ImportError, KeyError, TypeError, ValueError, OverflowError) as exc:
        raise SourceValidationError("Alternate OCR recognition differs from its complete source proof") from exc
    return {"page": page["page"], **binding}


def _validate_ocr_text_layout(page: dict[str, Any], recognized_text: str) -> dict[str, Any] | None:
    ocr = page.get("ocr")
    layout = ocr.get("text_layout") if isinstance(ocr, dict) else None
    indicator_present = "text_layout_selection" in page
    layout_present = isinstance(ocr, dict) and "text_layout" in ocr
    if not indicator_present and not layout_present:
        return None  # Existing immutable schema-2 receipts used sorted text.
    sorted_text = layout.get("sorted_text") if isinstance(layout, dict) else None
    expected = _text_layout_record(sorted_text, recognized_text) if isinstance(sorted_text, str) else None
    binding = {"policy": OCR_TEXT_LAYOUT_POLICY, "selection": "source-flow",
               "text_layout_sha256": sha256_bytes(canonical_bytes(layout))} if isinstance(layout, dict) else None
    if (page.get("extraction_method") != "ocr" or not isinstance(layout, dict)
            or type(layout.get("schema")) is not int
            or canonical_bytes(layout) != canonical_bytes(expected)
            or page.get("text_layout_selection") != binding
            or layout["sorted_readability"]["accepted"]
            or not layout["selected_readability"]["accepted"]
            or not _same_recognized_glyphs(sorted_text, recognized_text)):
        raise SourceValidationError("OCR text layout selection differs from its recognized source transcript")
    return {"page": page["page"], **binding}


def _validate_ocr_rotated_axis(page: dict[str, Any], recognized_text: str, *,
                              image_path: Path | None = None) -> dict[str, Any] | None:
    ocr = page.get("ocr")
    present = isinstance(ocr, dict) and "rotated_axis" in ocr
    indicator_present = "rotated_axis_selection" in page
    if not present and not indicator_present:
        if isinstance(ocr, dict) and ocr.get("engine") == OCR_ROTATED_AXIS_ENGINE:
            raise SourceValidationError("Rotated OCR recognition is missing its source proof")
        return None
    try:
        from ocr_rotated_axis_evidence import replay_rotated_axis_proof
        proof, image = ocr["rotated_axis"], page["original_page"]
        evidence = ocr["numeric_evidence"]
        if (page.get("extraction_method") != "ocr" or ocr.get("engine") != OCR_ROTATED_AXIS_ENGINE
                or not isinstance(proof, dict) or type(proof.get("schema")) is not int
                or proof.get("policy") != OCR_ROTATED_AXIS_POLICY
                or "recognition" in ocr or "recognition_selection" in page
                or "text_layout" in ocr or "text_layout_selection" in page
                or not isinstance(image, dict) or not isinstance(evidence, dict) or image_path is None):
            raise ValueError("rotated-proof")
        binding = {"policy": OCR_ROTATED_AXIS_POLICY, "selection": "rotated-axis",
                   "rotated_axis_sha256": sha256_bytes(canonical_bytes(proof))}
        if (canonical_bytes(page.get("rotated_axis_selection")) != canonical_bytes(binding)
                or evidence.get("rotated_axis_sha256") != binding["rotated_axis_sha256"]):
            raise ValueError("rotated-binding")
        replay_rotated_axis_proof(proof, recognized_text,
            input_pixel_sha256=image["pixel_sha256"], page_size_points=evidence["page_size_points"],
            image_path=image_path, language=ocr["languages"], traineddata=ocr["traineddata"])
    except (ImportError, KeyError, TypeError, ValueError, OverflowError) as exc:
        raise SourceValidationError("Rotated OCR recognition differs from its complete source proof") from exc
    return {"page": page["page"], **binding}


def _source_context(value: Any) -> dict[str, str]:
    required = {"date_folder", "producer_run_id", "execution_sha", "original_source_run_id"}
    if not isinstance(value, dict) or set(value) != required or any(not isinstance(item, str) for item in value.values()):
        raise SourceValidationError("Source execution context must contain the exact date and producer binding")
    if not re.fullmatch(r"\d{6}", value["date_folder"]):
        raise SourceValidationError("Source execution context has an invalid date folder")
    try:
        datetime.strptime(value["date_folder"], "%y%m%d")
    except ValueError as exc:
        raise SourceValidationError("Source execution context has an invalid date folder") from exc
    if (not re.fullmatch(r"[1-9]\d*", value["producer_run_id"])
            or not re.fullmatch(r"[a-f0-9]{40}", value["execution_sha"])
            or (value["original_source_run_id"] and not re.fullmatch(r"[1-9]\d*", value["original_source_run_id"]))):
        raise SourceValidationError("Source execution context has an invalid GitHub run or commit binding")
    return dict(value)


def file_record(path: Path, root: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    return {"path": path.relative_to(root).as_posix(), "sha256": sha256_bytes(raw), "size_bytes": len(raw)}


def _pixel_record(pixmap: fitz.Pixmap) -> dict[str, Any]:
    samples = pixmap.samples
    return {"width": pixmap.width, "height": pixmap.height, "channels": pixmap.n,
            "alpha": bool(pixmap.alpha), "pixel_sha256": sha256_bytes(samples),
            "sample_count": len(samples), "white_sample_count": samples.count(255)}


def _tesseract_version(command: str, number: int) -> str:
    try:
        result = subprocess.run([command, "--version"], check=False, capture_output=True, timeout=10)
        first = result.stdout.decode("utf-8").splitlines()[0] if result.stdout else ""
        match = re.fullmatch(r"tesseract ([0-9][0-9A-Za-z.+_-]{0,63})", first.strip())
        if result.returncode or len(result.stdout) > 8192 or not match:
            raise ValueError("version")
        return match.group(1)
    except (OSError, subprocess.SubprocessError, UnicodeError, ValueError, IndexError) as exc:
        raise SourceValidationError(f"Runner OCR failed at page {number}: ocr_engine_failed",
                                    category="ocr_engine_failed") from exc


def _recognize_ocr_page(page: fitz.Page, source_name: str, number: int, *,
                        allow_rejected: bool = False) -> tuple[str, list[Any], str, dict[str, Any], dict[str, Any]]:
    """Choose one primary recognition; numeric failures never retry this stage."""
    try:
        tessdata = Path(fitz.get_tessdata())
        models = []
        for language in OCR_LANGUAGES.split("+"):
            model = tessdata / f"{language}.traineddata"
            if not model.is_file():
                raise FileNotFoundError(model.name)
            models.append({"language": language, "filename": model.name,
                           "sha256": sha256_bytes(model.read_bytes())})
    except Exception as exc:
        raise SourceValidationError(
            f"Runner OCR dependencies unavailable at page {number}: ocr_language_data_unavailable",
            category="ocr_language_data_unavailable",
        ) from exc
    try:
        textpage = page.get_textpage_ocr(language=OCR_LANGUAGES, dpi=PAGE_DPI,
                                       full=True, tessdata=str(tessdata))
        text = page.get_text("text", textpage=textpage, sort=True).strip()
    except Exception as exc:
        raise SourceValidationError(f"Runner OCR failed at page {number}: ocr_engine_failed",
                                    category="ocr_engine_failed") from exc
    sorted_text = text
    text, selected_sort, text_layout, candidates = _ocr_layout_candidates(page, textpage, sorted_text, number)
    diagnostic = {key: value for key, value in candidates.items() if key != "source_flow_text"}
    provenance = {"engine": "tesseract-via-pymupdf", "pymupdf_version": fitz.VersionBind,
                  "languages": OCR_LANGUAGES, "dpi": PAGE_DPI, "full_page": True, "traineddata": models}
    if text is None and not candidates["source_flow_readability"]["accepted"]:
        # Both complete default-language candidates failed. This is a fresh
        # recognition of the same whole page, not a same-glyph ordering choice.
        try:
            from ocr_numeric_evidence import _image, _read_tesseract
            command = shutil.which("tesseract")
            if not command:
                raise FileNotFoundError("tesseract")
            version = _tesseract_version(command, number)
            pixmap = page.get_pixmap(dpi=PAGE_DPI, colorspace=fitz.csRGB, alpha=False)
            pixels = _pixel_record(pixmap)
            words = _read_tesseract(_image(pixmap), language=OCR_LANGUAGES, tessdata=str(tessdata),
                                    command=command, psm=11, dpi=PAGE_DPI)
            page_size = [float(page.rect.width), float(page.rect.height)]
            text, primary_words = _alternate_words(words, [pixmap.width, pixmap.height], page_size)
            if any(len(value.encode("utf-8")) > MAX_ALTERNATE_TEXT_BYTES
                   for value in (sorted_text, candidates["source_flow_text"])):
                raise ValueError("default transcript bound")
            recognition = _recognition_record(sorted_text, candidates["source_flow_text"], text, words,
                                              pixels=pixels, page_size=page_size, version=version, models=models)
        except SourceValidationError as exc:
            if exc.category == "ocr_engine_failed":
                raise
            raise SourceValidationError(f"Runner OCR failed at page {number}: ocr_engine_failed",
                                        category="ocr_engine_failed") from exc
        except Exception as exc:
            raise SourceValidationError(f"Runner OCR failed at page {number}: ocr_engine_failed",
                                        category="ocr_engine_failed") from exc
        provenance.update(engine="tesseract-cli", recognition=recognition)
        diagnostic.update(recognition_attempted=True, alternate_readability=recognition["selected_readability"],
                          selection="full-page-psm11" if recognition["selected_readability"]["accepted"] else "rejected")
        # Axis recovery cannot replace a healthy recognition, a different
        # rejection class, or a numeric-audit failure. All three complete-page
        # candidates must first fail the unchanged opaque-glyph gate.
        assessments = (candidates["sorted_readability"], candidates["source_flow_readability"],
                       recognition["selected_readability"])
        if all(value.get("accepted") is False and value.get("reason") == "opaque_ascii_runs"
               for value in assessments):
            try:
                from ocr_rotated_axis_evidence import RotatedAxisError, recover_rotated_axes
                axis_diagnostics = {}
                try:
                    rotated = recover_rotated_axes(page, {
                        "geometric-sorted": {"text": sorted_text,
                            "words": page.get_text("words", textpage=textpage, sort=True)},
                        "source-flow": {"text": candidates["source_flow_text"],
                            "words": page.get_text("words", textpage=textpage, sort=False)},
                        "full-page-psm11": {"text": text, "words": primary_words},
                    }, language=OCR_LANGUAGES, tessdata=str(tessdata), tesseract_command=command,
                       tesseract_version=version, traineddata=models, reader=_read_tesseract,
                       diagnostics=axis_diagnostics)
                except RotatedAxisError as exc:
                    category = str(exc) if str(exc) in ROTATED_AXIS_FAILURE_CATEGORIES else "rotated_axis_proof_invalid"
                    raise SourceValidationError(f"Runner OCR axis recovery rejected at page {number}: {category}",
                                                category=category) from exc
                if rotated is not None:
                    text, primary_words = rotated["primary_text"], rotated["primary_words"]
                    require_readable_page(text, source_name, number, allow_sparse_ocr=True)
                    provenance.pop("recognition")
                    provenance.update(engine=OCR_ROTATED_AXIS_ENGINE, rotated_axis=rotated["proof"])
                    diagnostic.update(selection="rotated-axis", rotated_axis_attempted=True,
                                      rotated_axis_readability=page_readability(text, allow_sparse_ocr=True))
                else:
                    diagnostic["rotated_axis_attempted"] = True
                    if axis_diagnostics:
                        diagnostic["rotated_axis_diagnostics"] = axis_diagnostics
            except SourceValidationError:
                raise
            except Exception as exc:
                raise SourceValidationError(f"Runner OCR axis recovery failed at page {number}: ocr_engine_failed",
                                            category="ocr_engine_failed") from exc
    else:
        if text is None:
            # A changed-glyph source-flow result may not authorize another
            # recognition when its own language gate already passed.
            text, selected_sort = sorted_text, True
        try:
            primary_words = page.get_text("words", textpage=textpage, sort=selected_sort)
        except Exception as exc:
            raise SourceValidationError(f"Runner OCR failed at page {number}: ocr_engine_failed",
                                        category="ocr_engine_failed") from exc
        if text_layout is not None:
            provenance["text_layout"] = text_layout
    if not allow_rejected:
        try:
            require_readable_page(text, source_name, number, allow_sparse_ocr=True)
        except SourceValidationError as exc:
            exc.rotated_axis_diagnostics = diagnostic.get("rotated_axis_diagnostics")
            raise
    return text, primary_words, str(tessdata), provenance, diagnostic


def _ocr_page(page: fitz.Page, source_name: str, number: int) -> tuple[str, dict[str, Any]]:
    """Retain the selected raw recognition and all independent numeric evidence."""
    text, primary_words, tessdata, provenance, _ = _recognize_ocr_page(page, source_name, number)
    try:
        from ocr_numeric_evidence import NumericEvidenceError, audit_numeric_evidence, safe_geometry_diagnostics
    except ImportError as exc:
        raise SourceValidationError(f"Runner OCR support unavailable at page {number}: ocr_numeric_support_missing",
                                    category="ocr_numeric_support_missing") from exc
    try:
        axis_arguments = ({"rotated_axis_proof": provenance["rotated_axis"]}
                          if "rotated_axis" in provenance else {})
        audit = audit_numeric_evidence(
            page, text, language=OCR_LANGUAGES, tessdata=tessdata, primary_words=primary_words,
            **axis_arguments,
        )
        text = audit["safe_text"]
    except NumericEvidenceError as exc:
        category = _numeric_failure_category(exc)
        raise SourceValidationError(f"Runner OCR numeric evidence rejected at page {number}: {category}",
                                    category=category, geometry_diagnostics=safe_geometry_diagnostics(exc)) from exc
    except SourceValidationError:
        # A readable-language/source-contract rejection is not a missing model
        # or engine failure. Preserve its actual cause for bounded recovery.
        raise
    except Exception as exc:
        raise SourceValidationError(f"Runner OCR numeric audit failed at page {number}: numeric_audit_failed",
                                    category="numeric_audit_failed") from exc
    provenance["numeric_evidence"] = audit["evidence"]
    return text, provenance


def _extract_report(pdf: Path, binding: dict[str, str], root: Path, index: int,
                    *, enable_ocr: bool = False) -> dict[str, Any]:
    raw = pdf.read_bytes()
    if sha256_bytes(raw) != binding["content_sha256"]:
        raise SourceValidationError(f"Original PDF hash mismatch: {pdf.name}")
    if not raw.startswith(b"%PDF-"):
        raise SourceValidationError(f"Original file is not a PDF: {pdf.name}")
    directory = root / f"report_{index:04d}_{binding['content_sha256'][:12]}"
    directory.mkdir()
    markdown = (f"# {Path(binding['source_pdf']).stem}\n\n"
                "原始 PDF 逐页来源。优先使用可读文本层；图片页使用运行环境中的 Tesseract OCR，"
                "并保留原页图以核对识别文字。确认为全白的页明确记录，不补写原文。\n\n")
    assets: list[dict[str, Any]] = []
    page_records: list[dict[str, Any]] = []
    total_characters = native_total = recognized_total = 0
    try:
        with fitz.open(stream=raw, filetype="pdf") as document:
            if document.is_encrypted or document.needs_pass:
                raise SourceValidationError(f"Encrypted PDF is unsupported: {pdf.name}")
            if document.is_repaired or document.page_count <= 0:
                raise SourceValidationError(f"Damaged or empty PDF is unsupported: {pdf.name}")
            for page_index in range(document.page_count):
                page = document.load_page(page_index)
                page_number = page_index + 1
                native_text = page.get_text("text", sort=True).strip()
                native_characters = meaningful_characters(native_text)
                native_total += native_characters
                text, recognized_text, method, pixmap, ocr = native_text, native_text, "native", None, None
                try:
                    characters = require_readable_page(native_text, pdf.name, page_number)
                except SourceValidationError:
                    pixmap = page.get_pixmap(dpi=PAGE_DPI, colorspace=fitz.csRGB, alpha=False)
                    pixels = _pixel_record(pixmap)
                    if not native_text and pixels["white_sample_count"] == pixels["sample_count"]:
                        text, characters, method = "", 0, "blank"
                        recognized_text = ""
                    else:
                        if not enable_ocr:
                            raise SourceValidationError(
                                f"OCR is disabled for unreadable source page: {pdf.name} page {page_number}"
                            )
                        text, ocr = _ocr_page(page, pdf.name, page_number)
                        recognized_text = _ocr_primary_text(ocr)
                        # Readability is a property of recognized source
                        # language, before uncertain values are annotated.
                        # Numeric evidence separately rebuilds safe text and
                        # checks source positions and pixels in the consumer.
                        require_readable_page(recognized_text, pdf.name, page_number, allow_sparse_ocr=True)
                        characters = meaningful_characters(text)
                        method = "ocr"
                total_characters += characters
                recognized_readability = page_readability(recognized_text, allow_sparse_ocr=method == "ocr")
                recognized_characters = recognized_readability["characters"]
                recognized_total += recognized_characters
                captions = [match.group(1).strip() for line in text.splitlines()
                            if (match := EXHIBIT_CAPTION.fullmatch(line))]
                markdown += f"## 原报告第 {page_number} 页\n\n"
                markdown += {"native": "提取方式：原 PDF 可读文本层。\n\n",
                             "ocr": "提取方式：运行环境中的整页 Tesseract OCR。未确认数值明确标记为待核对；请以原页图核对识别文字。\n\n",
                             "blank": "原页在 300dpi RGB 白底渲染中全部像素为白色，且原文本层为空；本页无原文。\n\n"}[method]
                text_begin = len(markdown.encode("utf-8"))
                markdown += text
                text_end = len(markdown.encode("utf-8"))
                markdown += "\n\n"
                page_record: dict[str, Any] = {
                    "page": page_number, "extraction_method": method,
                    "source_pdf_sha256": binding["content_sha256"],
                    "native_text": native_text, "native_text_characters": native_characters,
                    "native_text_sha256": sha256_bytes(native_text.encode("utf-8")),
                    "native_readability": page_readability(native_text),
                    "text_characters": characters, "text_sha256": sha256_bytes(text.encode("utf-8")),
                    "text_readability": page_readability(text),
                    "recognized_text_characters": recognized_characters,
                    "recognized_readability": recognized_readability,
                    "markdown_text_begin": text_begin, "markdown_text_end": text_end,
                }
                if method != "native" or captions:
                    if pixmap is None:
                        pixmap = page.get_pixmap(dpi=PAGE_DPI, colorspace=fitz.csRGB, alpha=False)
                    page_image = directory / "pages" / f"source_page_{page_number:04d}.png"
                    page_image.parent.mkdir(exist_ok=True)
                    pixmap.save(str(page_image))
                    page_record["original_page"] = {
                        **file_record(page_image, root), **_pixel_record(pixmap),
                        "source_pdf_sha256": binding["content_sha256"], "source_page": page_number,
                        "dpi": PAGE_DPI, "pymupdf_version": fitz.VersionBind,
                    }
                    if method != "native":
                        markdown += f"![原报告第 {page_number} 页核对原图](pages/{page_image.name})\n\n"
                if method == "ocr":
                    page_record["ocr"] = {**ocr, "input_pixel_sha256": page_record["original_page"]["pixel_sha256"]}
                    if "text_layout" in ocr:
                        page_record["text_layout_selection"] = {
                            "policy": OCR_TEXT_LAYOUT_POLICY, "selection": "source-flow",
                            "text_layout_sha256": sha256_bytes(canonical_bytes(ocr["text_layout"])),
                        }
                    if "recognition" in ocr:
                        page_record["recognition_selection"] = {
                            "policy": OCR_RECOGNITION_POLICY, "selection": "full-page-psm11",
                            "recognition_sha256": sha256_bytes(canonical_bytes(ocr["recognition"])),
                        }
                    if "rotated_axis" in ocr:
                        page_record["rotated_axis_selection"] = {
                            "policy": OCR_ROTATED_AXIS_POLICY, "selection": "rotated-axis",
                            "rotated_axis_sha256": sha256_bytes(canonical_bytes(ocr["rotated_axis"])),
                        }
                elif method == "blank":
                    page_record["blank_proof"] = {"criterion": "all-rgb-samples-255",
                                                 "ocr_attempted": False}
                # Caption lines identify an exhibit page. The pixels are always
                # the actual full original page; no inferred chart is redrawn.
                if captions:
                    asset_path = directory / "assets" / f"source_image_{len(assets) + 1}.png"
                    asset_path.parent.mkdir(exist_ok=True)
                    scale = min(2.0, 1800 / max(page.rect.width, page.rect.height))
                    page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False).save(str(asset_path))
                    asset = {**file_record(asset_path, root), "source_page": page_number,
                             "description": " / ".join(captions)}
                    assets.append(asset)
                    page_record["asset_path"] = asset["path"]
                    relative_asset = asset_path.relative_to(directory).as_posix()
                    markdown += (f"原报告第 {page_number} 页图表原页：{' / '.join(captions)}\n\n"
                                 f"![原报告第 {page_number} 页]({relative_asset})\n\n")
                page_records.append(page_record)
    except SourceValidationError:
        raise
    except Exception as exc:
        raise SourceValidationError(f"Cannot read original PDF {pdf.name}: {type(exc).__name__}") from exc
    if recognized_total < MIN_REPORT_CHARACTERS:
        raise SourceValidationError(f"{pdf.name} has insufficient text for a report summary ({recognized_total} characters)")
    if pdf.read_bytes() != raw:
        raise SourceValidationError(f"Original PDF changed during extraction: {pdf.name}")
    markdown_path = directory / MARKDOWN_NAME
    markdown_path.write_text(markdown, encoding="utf-8")
    status = {
        "source_method": "original-pdf", "receipt_schema": SCHEMA, **binding,
        "extraction_policy": "native-then-local-ocr", "duplicate_of": None,
        "source_markdown": MARKDOWN_NAME,
        "page_count": len(page_records), "pages_covered": list(range(1, len(page_records) + 1)),
        "text_characters": total_characters, "native_text_characters": native_total,
        "recognized_text_characters": recognized_total,
        "ocr_page_count": sum(page["extraction_method"] == "ocr" for page in page_records),
        "blank_page_count": sum(page["extraction_method"] == "blank" for page in page_records),
        "images": [str(PurePosixPath(asset["path"]).relative_to(directory.name)) for asset in assets],
    }
    layout_bindings, recognition_bindings, rotated_axis_bindings = [], [], []
    for page_record in page_records:
        primary = _ocr_primary_text(page_record["ocr"]) if page_record["extraction_method"] == "ocr" else ""
        layout_binding = _validate_ocr_text_layout(page_record, primary)
        if layout_binding is not None:
            layout_bindings.append(layout_binding)
        recognition_binding = _validate_ocr_recognition(page_record, primary)
        if recognition_binding is not None:
            recognition_bindings.append(recognition_binding)
        rotated_axis_binding = _validate_ocr_rotated_axis(page_record, primary,
            image_path=root / page_record["original_page"]["path"] if "original_page" in page_record else None)
        if rotated_axis_binding is not None:
            rotated_axis_bindings.append(rotated_axis_binding)
    if layout_bindings:
        # This immutable file's receipt hash also binds the optional page
        # metadata: deleting both layout fields cannot pose as an old receipt.
        status["ocr_text_layout_bindings"] = layout_bindings
    if recognition_bindings:
        status["ocr_recognition_bindings"] = recognition_bindings
    if rotated_axis_bindings:
        status["ocr_rotated_axis_bindings"] = rotated_axis_bindings
    write_json(directory / "status.json", status)
    return {
        **binding, "directory": directory.name, "source_method": "original-pdf", "duplicate_of": None,
        "page_count": len(page_records), "pages_covered": status["pages_covered"],
        "text_characters": total_characters, "native_text_characters": native_total,
        "recognized_text_characters": recognized_total,
        "ocr_page_count": status["ocr_page_count"], "blank_page_count": status["blank_page_count"],
        "pages": page_records,
        "markdown": file_record(markdown_path, root),
        "status": file_record(directory / "status.json", root), "assets": assets,
    }


def _clone_report(pdf: Path, binding: dict[str, str], root: Path, index: int, canonical: dict[str, Any]) -> dict[str, Any]:
    """Retain each exact alias binding while reusing extraction of identical bytes."""
    if sha256_bytes(pdf.read_bytes()) != binding["content_sha256"]:
        raise SourceValidationError(f"Original PDF hash mismatch: {pdf.name}")
    directory = f"report_{index:04d}_{binding['content_sha256'][:12]}"
    shutil.copytree(root / canonical["directory"], root / directory)
    report = copy.deepcopy(canonical)
    report.update(binding)
    report["directory"], report["duplicate_of"] = directory, canonical["directory"]
    for record in [report["markdown"], report["status"], *report["assets"],
                   *(page["original_page"] for page in report["pages"] if page.get("original_page"))]:
        record["path"] = directory + record["path"][len(canonical["directory"]):]
    for page in report["pages"]:
        if page.get("asset_path"):
            page["asset_path"] = directory + page["asset_path"][len(canonical["directory"]):]
    status_path = root / report["status"]["path"]
    status = json.loads(status_path.read_bytes())
    status.update(binding)
    status["duplicate_of"] = canonical["directory"]
    write_json(status_path, status)
    report["status"] = file_record(status_path, root)
    return report


def _original_inventory(input_dir: Path) -> dict[str, Path]:
    if input_dir.is_symlink() or not input_dir.is_dir():
        raise SourceValidationError("input_dir must be a regular directory of original PDFs")
    originals: dict[str, Path] = {}
    for path in sorted(input_dir.rglob("*")):
        if path.suffix.lower() != ".pdf":
            continue
        if path.is_symlink() or not path.is_file() or input_dir.resolve() not in path.resolve().parents:
            raise SourceValidationError("Original PDFs must be regular files inside input_dir")
        if path.name in originals:
            raise SourceValidationError(f"Duplicate original PDF basename: {path.name}")
        originals[path.name] = path
    return originals


def extract_sources(input_dir: Path, manifest: Path, output_dir: Path, expected_reports: int,
                    progress: Callable[[dict[str, Any]], None] | None = None, *,
                    enable_ocr: bool = False, source_context: dict[str, str] | None = None) -> dict[str, Any]:
    input_dir, manifest, output_dir = Path(input_dir), Path(manifest), Path(output_dir)
    if type(enable_ocr) is not bool:
        raise SourceValidationError("enable_ocr must be an explicit boolean")
    context = _source_context(source_context) if source_context is not None else None
    raw_manifest, bindings = read_manifest(manifest, expected_reports)
    originals = _original_inventory(input_dir)
    wanted = {row["source_pdf"] for row in bindings}
    if set(originals) != wanted:
        raise SourceValidationError(
            f"Original PDF inventory does not match manifest: missing={sorted(wanted - set(originals))}, "
            f"extra={sorted(set(originals) - wanted)}"
        )
    # Never replace an existing batch with a new partial extraction. A complete
    # existing batch can be validated and reused by the caller.
    if output_dir.exists() or output_dir.is_symlink():
        raise SourceValidationError("output_dir already exists; validate the existing batch or choose an empty destination")
    if input_dir.resolve() == output_dir.resolve() or input_dir.resolve() in output_dir.resolve().parents:
        raise SourceValidationError("output_dir must be outside the original PDF directory")
    output_dir.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=f".{output_dir.name}-native-", dir=output_dir.parent) as temporary:
        staging = Path(temporary) / "batch"
        staging.mkdir()
        reports, canonical = [], {}
        for index, binding in enumerate(bindings, 1):
            prior = canonical.get(binding["content_sha256"])
            report = (_clone_report(originals[binding["source_pdf"]], binding, staging, index, prior)
                      if prior else _extract_report(originals[binding["source_pdf"]], binding, staging, index,
                                                    enable_ocr=enable_ocr))
            reports.append(report)
            canonical.setdefault(binding["content_sha256"], report)
            if progress:
                progress(report)
        final_originals = _original_inventory(input_dir)
        if set(final_originals) != wanted or manifest.read_bytes() != raw_manifest:
            raise SourceValidationError("Original batch inventory or manifest changed during extraction")
        if any(sha256_bytes(final_originals[row["source_pdf"]].read_bytes()) != row["content_sha256"]
               for row in bindings):
            raise SourceValidationError("Original batch bytes changed during extraction")
        (staging / MANIFEST_NAME).write_bytes(raw_manifest)
        receipt = {
            "schema": SCHEMA, "source_method": "original-pdf", "complete": True,
            "extraction_policy": "native-then-local-ocr", "unique_content_count": len(canonical),
            "expected_reports": expected_reports, "report_count": len(reports),
            "manifest_sha256": sha256_bytes(canonical_bytes(bindings)),
            "manifest_file": file_record(staging / MANIFEST_NAME, staging), "reports": reports,
        }
        if context is not None:
            receipt["source_context"] = context
        write_json(staging / RECEIPT_NAME, receipt)
        validate_sources(staging, manifest, expected_reports, expected_source_context=context)
        if output_dir.exists() or output_dir.is_symlink():
            raise SourceValidationError("output_dir appeared during extraction; existing output is preserved")
        os.rename(staging, output_dir)
    return receipt


def _verified_file(root: Path, record: Any) -> Path:
    if not isinstance(record, dict) or not isinstance(record.get("path"), str):
        raise SourceValidationError("Receipt file record is malformed")
    relative = PurePosixPath(record["path"])
    if (relative.is_absolute() or not relative.parts or "\\" in record["path"]
            or any(part in {"..", "."} for part in relative.parts)
            or type(record.get("size_bytes")) is not int or record["size_bytes"] <= 0
            or not re.fullmatch(r"[a-f0-9]{64}", str(record.get("sha256") or ""))):
        raise SourceValidationError("Receipt contains an unsafe file path")
    path = root.joinpath(*relative.parts)
    if any(root.joinpath(*relative.parts[:index]).is_symlink() for index in range(1, len(relative.parts) + 1)):
        raise SourceValidationError("Receipt file path must not contain symbolic links")
    if not path.is_file() or root.resolve() not in path.resolve().parents:
        raise SourceValidationError(f"Receipt file is missing: {relative}")
    raw = path.read_bytes()
    if record.get("size_bytes") != len(raw) or record.get("sha256") != sha256_bytes(raw):
        raise SourceValidationError(f"Transferred source file checksum mismatch: {relative}")
    return path


def _validate_sources_v1(output_dir: Path, manifest: Path, expected_reports: int) -> dict[str, Any]:
    """Validate the complete transferred batch against its selected source manifest."""
    output_dir = Path(output_dir)
    if output_dir.is_symlink() or not output_dir.is_dir():
        raise SourceValidationError("Source output must be a regular directory")
    _, bindings = read_manifest(Path(manifest), expected_reports)
    if len({binding["content_sha256"] for binding in bindings}) != len(bindings):
        raise SourceValidationError("Schema 1 cannot represent duplicate PDF contents")
    receipt_path = output_dir / RECEIPT_NAME
    if receipt_path.is_symlink() or not receipt_path.is_file():
        raise SourceValidationError("Complete source receipt is missing")
    try:
        receipt = json.loads(receipt_path.read_bytes())
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise SourceValidationError("Complete source receipt is invalid JSON") from exc
    if not isinstance(receipt, dict) or type(receipt.get("schema")) is not int or receipt.get("schema") != 1:
        raise SourceValidationError("Source receipt schema is unsupported")
    if (receipt.get("source_method") != "native-pdf" or receipt.get("complete") is not True
            or type(receipt.get("expected_reports")) is not int or type(receipt.get("report_count")) is not int
            or receipt.get("expected_reports") != expected_reports or receipt.get("report_count") != expected_reports
            or receipt.get("manifest_sha256") != sha256_bytes(canonical_bytes(bindings))):
        raise SourceValidationError("Source receipt is incomplete or does not match the selected manifest")
    local_manifest = _verified_file(output_dir, receipt.get("manifest_file"))
    if local_manifest.name != MANIFEST_NAME or local_manifest.parent != output_dir:
        raise SourceValidationError("Receipt must bind the root selected manifest")
    _, local_bindings = read_manifest(local_manifest, expected_reports)
    if local_bindings != bindings:
        raise SourceValidationError("Transferred source manifest differs from the expected source manifest")
    reports = receipt.get("reports")
    if not isinstance(reports, list) or len(reports) != expected_reports:
        raise SourceValidationError("Receipt is missing expected report coverage")
    inventory = {RECEIPT_NAME, MANIFEST_NAME}
    directories = set()
    for report, binding in zip(reports, bindings):
        if not isinstance(report, dict) or any(report.get(key) != value for key, value in binding.items()):
            raise SourceValidationError("Receipt report is not bound to the exact selected original PDF")
        directory = report.get("directory")
        count = report.get("page_count")
        pages = report.get("pages")
        if (not isinstance(directory, str) or not re.fullmatch(r"report_\d{4}_[a-f0-9]{12}", directory)
                or directory in directories or report.get("source_method") != "native-pdf"
                or type(count) is not int or count <= 0
                or report.get("pages_covered") != list(range(1, count + 1))
                or not isinstance(pages, list) or len(pages) != count):
            raise SourceValidationError("Receipt has incomplete or duplicate original page coverage")
        directories.add(directory)
        total = 0
        for number, page in enumerate(pages, 1):
            if (not isinstance(page, dict) or type(page.get("page")) is not int or page.get("page") != number
                    or type(page.get("native_text_characters")) is not int
                    or page["native_text_characters"] < MIN_PAGE_CHARACTERS
                    or not re.fullmatch(r"[a-f0-9]{64}", str(page.get("native_text_sha256") or ""))):
                raise SourceValidationError("Receipt contains an unreadable or missing original page")
            total += page["native_text_characters"]
        if (total < MIN_REPORT_CHARACTERS or type(report.get("native_text_characters")) is not int
                or report.get("native_text_characters") != total):
            raise SourceValidationError("Receipt has insufficient original report text")
        assets = report.get("assets")
        if not isinstance(assets, list):
            raise SourceValidationError("Receipt assets must be a list")
        records = [report.get("markdown"), report.get("status"), *assets]
        for record in records:
            path = _verified_file(output_dir, record)
            relative = path.relative_to(output_dir).as_posix()
            if not relative.startswith(directory + "/") or relative in inventory:
                raise SourceValidationError("Receipt contains a duplicate or misplaced report file")
            inventory.add(relative)
        markdown_path = output_dir / report["markdown"]["path"]
        status_path = output_dir / report["status"]["path"]
        if markdown_path.name != MARKDOWN_NAME or status_path.name != "status.json":
            raise SourceValidationError("Receipt does not identify the native source files")
        markdown_text = markdown_path.read_text(encoding="utf-8")
        markdown_raw = markdown_path.read_bytes()
        expected_headings = [f"## 原报告第 {number} 页" for number in range(1, count + 1)]
        if any(heading not in markdown_text for heading in expected_headings):
            raise SourceValidationError("Native markdown is missing original page sections")
        previous_end = 0
        for page in pages:
            begin, end = page.get("markdown_text_begin"), page.get("markdown_text_end")
            if (type(begin) is not int or type(end) is not int
                    or not previous_end <= begin < end <= len(markdown_raw)):
                raise SourceValidationError("Receipt has invalid original page text bounds")
            page_raw = markdown_raw[begin:end]
            try:
                page_text = page_raw.decode("utf-8")
            except UnicodeError as exc:
                raise SourceValidationError("Receipt original page text is not readable UTF-8") from exc
            if (sha256_bytes(page_raw) != page["native_text_sha256"]
                    or require_readable_page(page_text, binding["source_pdf"], page["page"]) != page["native_text_characters"]):
                raise SourceValidationError("Receipt original page text differs from transferred markdown")
            previous_end = end
        try:
            status = json.loads(status_path.read_bytes())
        except (UnicodeError, json.JSONDecodeError) as exc:
            raise SourceValidationError("Native source status is invalid JSON") from exc
        if (not isinstance(status, dict) or status.get("source_method") != "native-pdf"
                or any(status.get(key) != value for key, value in binding.items())
                or status.get("page_count") != count or status.get("pages_covered") != report["pages_covered"]
                or status.get("source_markdown") != MARKDOWN_NAME or status.get("native_text_characters") != total):
            raise SourceValidationError("Native source status disagrees with source receipt")
        expected_assets = []
        asset_pages = set()
        for index, asset in enumerate(assets, 1):
            expected_path = f"{directory}/assets/source_image_{index}.png"
            page_number = asset.get("source_page")
            if (asset.get("path") != expected_path or type(page_number) is not int or not 1 <= page_number <= count
                    or page_number in asset_pages
                    or not isinstance(asset.get("description"), str) or not asset["description"].strip()
                    or pages[page_number - 1].get("asset_path") != expected_path):
                raise SourceValidationError("Native exhibit asset lacks an exact original page binding")
            asset_pages.add(page_number)
            expected_assets.append(f"assets/source_image_{index}.png")
            if f"]({expected_assets[-1]})" not in markdown_text:
                raise SourceValidationError("Native source markdown omits a bound original exhibit page")
        if status.get("images") != expected_assets:
            raise SourceValidationError("Native source image status differs from the source receipt")
        if {page["page"] for page in pages if page.get("asset_path")} != asset_pages:
            raise SourceValidationError("Receipt contains an unbound original exhibit page")
    actual_files = set()
    for path in output_dir.rglob("*"):
        if path.is_symlink():
            raise SourceValidationError("Transferred source directory contains symbolic links")
        if path.is_file():
            actual_files.add(path.relative_to(output_dir).as_posix())
    if actual_files != inventory:
        raise SourceValidationError("Transferred source inventory contains missing or unreceipted files")
    return receipt


def _validate_page_image(root: Path, record: dict[str, Any], binding: dict[str, str], number: int) -> Path:
    path = _verified_file(root, record)
    if (record.get("source_pdf_sha256") != binding["content_sha256"]
            or type(record.get("source_page")) is not int or record["source_page"] != number
            or type(record.get("dpi")) is not int or record["dpi"] != PAGE_DPI
            or not isinstance(record.get("pymupdf_version"), str) or not record["pymupdf_version"]):
        raise SourceValidationError("Original page image lacks source PDF and rendering provenance")
    try:
        pixmap = fitz.Pixmap(str(path))
        pixels = _pixel_record(pixmap)
    except Exception as exc:
        raise SourceValidationError("Original page image is not readable") from exc
    if (pixmap.n != 3 or pixmap.alpha or any(record.get(key) != value for key, value in pixels.items())
            or any(type(record.get(key)) is not int for key in ("width", "height", "channels", "sample_count", "white_sample_count"))
            or record.get("alpha") is not False):
        raise SourceValidationError("Original page pixels disagree with their provenance")
    return path


def _validate_sources_v2(output_dir: Path, manifest: Path, expected_reports: int) -> dict[str, Any]:
    root = Path(output_dir)
    if root.is_symlink() or not root.is_dir():
        raise SourceValidationError("Source output must be a regular directory")
    _, bindings = read_manifest(Path(manifest), expected_reports)
    receipt_path = root / RECEIPT_NAME
    if receipt_path.is_symlink() or not receipt_path.is_file():
        raise SourceValidationError("Complete source receipt is missing")
    receipt = json.loads(receipt_path.read_bytes())
    unique_count = len({binding["content_sha256"] for binding in bindings})
    if (receipt.get("schema") != 2 or receipt.get("source_method") != "original-pdf"
            or receipt.get("complete") is not True
            or receipt.get("extraction_policy") != "native-then-local-ocr"
            or any(type(receipt.get(key)) is not int for key in ("expected_reports", "report_count", "unique_content_count"))
            or receipt.get("expected_reports") != expected_reports or receipt.get("report_count") != expected_reports
            or receipt.get("unique_content_count") != unique_count
            or receipt.get("manifest_sha256") != sha256_bytes(canonical_bytes(bindings))):
        raise SourceValidationError("Source receipt is incomplete or does not match the selected manifest")
    local_manifest = _verified_file(root, receipt.get("manifest_file"))
    if local_manifest != root / MANIFEST_NAME or read_manifest(local_manifest, expected_reports)[1] != bindings:
        raise SourceValidationError("Transferred source manifest differs from the expected source manifest")
    reports = receipt.get("reports")
    if not isinstance(reports, list) or len(reports) != expected_reports:
        raise SourceValidationError("Receipt is missing expected report coverage")
    inventory, canonical = {RECEIPT_NAME, MANIFEST_NAME}, {}
    for index, (report, binding) in enumerate(zip(reports, bindings), 1):
        if not isinstance(report, dict) or any(report.get(key) != value for key, value in binding.items()):
            raise SourceValidationError("Receipt report is not bound to the exact selected original PDF")
        directory = f"report_{index:04d}_{binding['content_sha256'][:12]}"
        prior = canonical.get(binding["content_sha256"])
        expected_duplicate = prior["directory"] if prior else None
        count, pages, assets = report.get("page_count"), report.get("pages"), report.get("assets")
        if (report.get("directory") != directory or report.get("source_method") != "original-pdf"
                or "duplicate_of" not in report or report["duplicate_of"] != expected_duplicate
                or type(count) is not int or count <= 0
                or report.get("pages_covered") != list(range(1, count + 1))
                or not isinstance(pages, list) or len(pages) != count or not isinstance(assets, list)):
            raise SourceValidationError("Receipt has incomplete page coverage or invalid duplicate source binding")
        records = [report.get("markdown"), report.get("status"), *assets]
        for page in pages:
            if isinstance(page, dict) and page.get("original_page") is not None:
                records.append(page["original_page"])
        for record in records:
            path = _verified_file(root, record)
            relative = path.relative_to(root).as_posix()
            if not relative.startswith(directory + "/") or relative in inventory:
                raise SourceValidationError("Receipt contains a duplicate or misplaced report file")
            inventory.add(relative)
        if report["markdown"]["path"] != f"{directory}/{MARKDOWN_NAME}" or report["status"]["path"] != f"{directory}/status.json":
            raise SourceValidationError("Receipt does not identify the original source files")
        markdown_raw = (root / report["markdown"]["path"]).read_bytes()
        markdown_text = markdown_raw.decode("utf-8")
        previous_end = text_total = native_total = recognized_total = ocr_count = blank_count = 0
        page_texts, layout_bindings, recognition_bindings, rotated_axis_bindings = [], [], [], []
        for number, page in enumerate(pages, 1):
            if (not isinstance(page, dict) or type(page.get("page")) is not int or page["page"] != number
                    or page.get("source_pdf_sha256") != binding["content_sha256"]
                    or page.get("extraction_method") not in {"native", "ocr", "blank"}
                    or not isinstance(page.get("native_text"), str)
                    or type(page.get("native_text_characters")) is not int
                    or page["native_text_characters"] != meaningful_characters(page["native_text"])
                    or page.get("native_text_sha256") != sha256_bytes(page["native_text"].encode("utf-8"))
                    or type(page.get("text_characters")) is not int):
                raise SourceValidationError("Receipt contains an unreadable or missing original page")
            if f"## 原报告第 {number} 页" not in markdown_text:
                raise SourceValidationError("Original markdown is missing original page sections")
            begin, end = page.get("markdown_text_begin"), page.get("markdown_text_end")
            if (type(begin) is not int or type(end) is not int
                    or not previous_end <= begin <= end <= len(markdown_raw)):
                raise SourceValidationError("Receipt has invalid original page text bounds")
            page_raw = markdown_raw[begin:end]
            text = page_raw.decode("utf-8")
            if (sha256_bytes(page_raw) != page.get("text_sha256")
                    or meaningful_characters(text) != page["text_characters"]):
                raise SourceValidationError("Receipt original page text differs from transferred markdown")
            if (page.get("native_readability") != page_readability(page["native_text"])
                    or page.get("text_readability") != page_readability(text)):
                raise SourceValidationError("Receipt page readability evidence differs from bound source text")
            method, image = page["extraction_method"], page.get("original_page")
            image_path = None
            if image is not None:
                image_path = _validate_page_image(root, image, binding, number)
                if image_path != root / directory / "pages" / f"source_page_{number:04d}.png":
                    raise SourceValidationError("Original page image is misplaced")
            if method == "blank":
                recognized_text = ""
                if (text or page["native_text"] or image is None
                        or image["sample_count"] != image["white_sample_count"]
                        or page.get("blank_proof") != {"criterion": "all-rgb-samples-255", "ocr_attempted": False}
                        or page.get("ocr") is not None or page.get("asset_path")):
                    raise SourceValidationError("Blank page lacks a provably white original page")
                blank_count += 1
            else:
                recognized_text = _ocr_primary_text(page.get("ocr")) if method == "ocr" else text
                require_readable_page(recognized_text, binding["source_pdf"], number,
                                      allow_sparse_ocr=method == "ocr")
                if page.get("blank_proof") is not None:
                    raise SourceValidationError("Readable page cannot claim blank-page provenance")
                if method == "native":
                    if text != page["native_text"] or page.get("ocr") is not None:
                        raise SourceValidationError("Native page text or provenance is inconsistent")
                else:
                    ocr = page.get("ocr")
                    if (image is None or not isinstance(ocr, dict)
                            or ocr.get("engine") not in {"tesseract-via-pymupdf", "tesseract-cli", OCR_ROTATED_AXIS_ENGINE}
                            or not isinstance(ocr.get("pymupdf_version"), str) or not ocr["pymupdf_version"]
                            or ocr.get("languages") != OCR_LANGUAGES or ocr.get("full_page") is not True
                            or type(ocr.get("dpi")) is not int or ocr["dpi"] != PAGE_DPI
                            or ocr.get("input_pixel_sha256") != image["pixel_sha256"]):
                        raise SourceValidationError("OCR page lacks exact local OCR provenance")
                    models = ocr.get("traineddata")
                    if (not isinstance(models, list) or len(models) != len(OCR_LANGUAGES.split("+"))
                            or any(not isinstance(model, dict) or model.get("language") != language
                                   or model.get("filename") != f"{language}.traineddata"
                                   or not re.fullmatch(r"[a-f0-9]{64}", str(model.get("sha256") or ""))
                                   for model, language in zip(models, OCR_LANGUAGES.split("+")))):
                        raise SourceValidationError("OCR language data provenance is incomplete")
                    try:
                        from ocr_numeric_evidence import validate_numeric_evidence
                        axis_arguments = ({"rotated_axis_proof": ocr["rotated_axis"]}
                                          if "rotated_axis" in ocr else {})
                        validate_numeric_evidence(
                            text, ocr.get("numeric_evidence"), image["pixel_sha256"], image_path=image_path,
                            **axis_arguments,
                        )
                    except (ImportError, TypeError, ValueError, KeyError) as exc:
                        raise SourceValidationError("OCR numeric evidence is missing or differs from the original page") from exc
                    # OCR is authorized only when the native page fails the native gate.
                    try:
                        require_readable_page(page["native_text"], binding["source_pdf"], number)
                    except SourceValidationError:
                        pass
                    else:
                        raise SourceValidationError("OCR replaced a supported native text page")
                    ocr_count += 1
                if image is not None and image["sample_count"] == image["white_sample_count"]:
                    raise SourceValidationError("A fully white page cannot contain recognized report text")
            layout_binding = _validate_ocr_text_layout(page, recognized_text)
            if layout_binding is not None:
                layout_bindings.append(layout_binding)
            recognition_binding = _validate_ocr_recognition(page, recognized_text)
            if recognition_binding is not None:
                recognition_bindings.append(recognition_binding)
            rotated_axis_binding = _validate_ocr_rotated_axis(page, recognized_text, image_path=image_path)
            if rotated_axis_binding is not None:
                rotated_axis_bindings.append(rotated_axis_binding)
            recognized_readability = page_readability(recognized_text, allow_sparse_ocr=method == "ocr")
            recognized_characters = recognized_readability["characters"]
            if (page.get("recognized_text_characters") != recognized_characters
                    or type(page.get("recognized_text_characters")) is not int
                    or page.get("recognized_readability") != recognized_readability):
                raise SourceValidationError("Receipt recognized language evidence differs from the bound source transcript")
            if method != "native" and f"](pages/source_page_{number:04d}.png)" not in markdown_text:
                raise SourceValidationError("Markdown omits the OCR or blank original page image")
            page_texts.append(text)
            previous_end = end
            text_total += page["text_characters"]
            native_total += page["native_text_characters"]
            recognized_total += recognized_characters
        totals = {"text_characters": text_total, "native_text_characters": native_total,
                  "recognized_text_characters": recognized_total,
                  "ocr_page_count": ocr_count, "blank_page_count": blank_count}
        if recognized_total < MIN_REPORT_CHARACTERS or any(type(report.get(key)) is not int or report[key] != value for key, value in totals.items()):
            raise SourceValidationError("Receipt has insufficient original report text or incorrect extraction totals")
        status = json.loads((root / report["status"]["path"]).read_bytes())
        expected_status = {"source_method": "original-pdf", "receipt_schema": 2, **binding,
                           "source_markdown": MARKDOWN_NAME, "extraction_policy": "native-then-local-ocr",
                           "duplicate_of": expected_duplicate, "page_count": count,
                           "pages_covered": report["pages_covered"], **totals}
        if not isinstance(status, dict) or any(status.get(key) != value for key, value in expected_status.items()):
            raise SourceValidationError("Original source status disagrees with source receipt")
        if ((layout_bindings or "ocr_text_layout_bindings" in status)
                and canonical_bytes(status.get("ocr_text_layout_bindings")) != canonical_bytes(layout_bindings)):
            raise SourceValidationError("Original source status disagrees with OCR text layout bindings")
        if ((recognition_bindings or "ocr_recognition_bindings" in status)
                and canonical_bytes(status.get("ocr_recognition_bindings")) != canonical_bytes(recognition_bindings)):
            raise SourceValidationError("Original source status disagrees with OCR recognition bindings")
        if ((rotated_axis_bindings or "ocr_rotated_axis_bindings" in status)
                and canonical_bytes(status.get("ocr_rotated_axis_bindings")) != canonical_bytes(rotated_axis_bindings)):
            raise SourceValidationError("Original source status disagrees with rotated OCR recognition bindings")
        asset_pages, expected_assets = set(), []
        for asset_index, asset in enumerate(assets, 1):
            page_number = asset.get("source_page")
            path = f"{directory}/assets/source_image_{asset_index}.png"
            if (asset.get("path") != path or type(page_number) is not int or not 1 <= page_number <= count
                    or page_number in asset_pages or pages[page_number - 1].get("asset_path") != path
                    or pages[page_number - 1].get("original_page") is None):
                raise SourceValidationError("Original exhibit asset lacks an exact original page binding")
            captions = [match.group(1).strip() for line in page_texts[page_number - 1].splitlines()
                        if (match := EXHIBIT_CAPTION.fullmatch(line))]
            if not captions or asset.get("description") != " / ".join(captions):
                raise SourceValidationError("Original exhibit asset lacks a source caption")
            asset_pages.add(page_number)
            expected_assets.append(f"assets/source_image_{asset_index}.png")
            if f"]({expected_assets[-1]})" not in markdown_text:
                raise SourceValidationError("Original source markdown omits a bound exhibit page")
        if status.get("images") != expected_assets or {page["page"] for page in pages if page.get("asset_path")} != asset_pages:
            raise SourceValidationError("Original source images disagree with source receipt")
        if prior:
            fields = ("page_count", "pages_covered", "text_characters", "native_text_characters",
                      "recognized_text_characters", "ocr_page_count", "blank_page_count")
            if any(report[key] != prior[key] for key in fields):
                raise SourceValidationError("Duplicate source extraction differs from canonical content")
            def content_pages(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
                result = copy.deepcopy(rows)
                for page in result:
                    page.pop("asset_path", None)
                    if page.get("original_page"):
                        page["original_page"].pop("path", None)
                return result
            if content_pages(pages) != content_pages(prior["pages"]) or report["markdown"]["sha256"] != prior["markdown"]["sha256"]:
                raise SourceValidationError("Duplicate source page text or pixels differ from canonical content")
            alias_assets = [{key: value for key, value in asset.items() if key != "path"} for asset in assets]
            canonical_assets = [{key: value for key, value in asset.items() if key != "path"} for asset in prior["assets"]]
            if alias_assets != canonical_assets:
                raise SourceValidationError("Duplicate source exhibit pixels differ from canonical content")
        canonical.setdefault(binding["content_sha256"], report)
    actual_files = set()
    for path in root.rglob("*"):
        if path.is_symlink():
            raise SourceValidationError("Transferred source directory contains symbolic links")
        if path.is_file():
            actual_files.add(path.relative_to(root).as_posix())
    if actual_files != inventory:
        raise SourceValidationError("Transferred source inventory contains missing or unreceipted files")
    return receipt


def validate_sources(output_dir: Path, manifest: Path, expected_reports: int, *,
                     expected_source_context: dict[str, str] | None = None) -> dict[str, Any]:
    """Validate schema 1 native receipts or schema 2 native/local-OCR receipts."""
    path = Path(output_dir) / RECEIPT_NAME
    if path.is_symlink() or not path.is_file():
        raise SourceValidationError("Complete source receipt is missing")
    try:
        receipt = json.loads(path.read_bytes())
        if not isinstance(receipt, dict) or type(receipt.get("schema")) is not int:
            raise SourceValidationError("Source receipt schema is unsupported")
        if "source_context" in receipt:
            _source_context(receipt["source_context"])
        if expected_source_context is not None:
            expected = _source_context(expected_source_context)
            if receipt.get("schema") != 2 or receipt.get("source_context") != expected:
                raise SourceValidationError("Source receipt differs from the expected cloud execution context")
        if receipt["schema"] == 1:
            return _validate_sources_v1(output_dir, manifest, expected_reports)
        if receipt["schema"] == 2:
            return _validate_sources_v2(output_dir, manifest, expected_reports)
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise SourceValidationError("Complete source receipt or status is invalid JSON or UTF-8") from exc
    raise SourceValidationError("Source receipt schema is unsupported")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", nargs="?", choices=("extract", "validate"), default="extract")
    parser.add_argument("--input-dir", type=Path)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--expected-reports", type=int, required=True)
    parser.add_argument("--enable-ocr", action="store_true",
                        help="Permit the tested runner OCR fallback when native text is unreadable")
    parser.add_argument("--date-folder")
    parser.add_argument("--producer-run-id")
    parser.add_argument("--execution-sha")
    parser.add_argument("--original-source-run-id")
    args = parser.parse_args()
    if args.command == "extract" and args.input_dir is None:
        parser.error("--input-dir is required for extraction")
    context_values = {name: getattr(args, name) for name in
                      ("date_folder", "producer_run_id", "execution_sha", "original_source_run_id")}
    if any(value is not None for value in context_values.values()) and any(value is None for value in context_values.values()):
        parser.error("Cloud source context requires all four date, producer, execution and original-source arguments")
    context = context_values if context_values["date_folder"] is not None else None
    try:
        receipt = (validate_sources(args.output_dir, args.manifest, args.expected_reports,
                                    expected_source_context=context)
                   if args.command == "validate" else
                   extract_sources(args.input_dir, args.manifest, args.output_dir, args.expected_reports,
                                   enable_ocr=args.enable_ocr, source_context=context,
                                   progress=lambda report: print(
                                       f"Original PDF source materialized: {report['source_pdf']}; "
                                       f"pages={report['page_count']}, OCR={report['ocr_page_count']}, "
                                       f"blank={report['blank_page_count']}, duplicate_of={report['duplicate_of']}",
                                       flush=True)))
    except (OSError, SourceValidationError) as exc:
        print(f"Original PDF Market Views source rejected: {exc}", file=sys.stderr)
        return 2
    print(f"Original PDF Market Views source {args.command} complete: reports={receipt['report_count']}, "
          f"unique_contents={receipt.get('unique_content_count', receipt['report_count'])}, "
          f"pages={sum(report['page_count'] for report in receipt['reports'])}, "
          f"ocr_pages={sum(report.get('ocr_page_count', 0) for report in receipt['reports'])}, "
          f"blank_pages={sum(report.get('blank_page_count', 0) for report in receipt['reports'])}, "
          f"exhibit_pages={sum(len(report['assets']) for report in receipt['reports'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
