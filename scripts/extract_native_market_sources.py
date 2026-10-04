#!/usr/bin/env python3
"""Extract a complete, manifest-bound Market Views source batch from local PDFs.

This fallback uses the original PDF text layer and original exhibit pages only.
It performs no OCR, provider submission, network request or article generation.
Every page must have readable native text; one unsupported report rejects the
whole batch. The consumer can validate the transferred receipt without PDFs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys
import tempfile
import unicodedata
from typing import Any

import fitz


SCHEMA = 1
MANIFEST_NAME = "selected_to_process_manifest.json"
RECEIPT_NAME = "source_receipt.json"
MARKDOWN_NAME = "source_native_pdf.md"
MIN_PAGE_CHARACTERS = 40
MIN_REPORT_CHARACTERS = 600
EXHIBIT_CAPTION = re.compile(
    r"^\s*((?:Figure|Fig\.?|Chart|Table|Exhibit)\s+\d+[A-Za-z]?\b"
    r"[\s:：.\-–—]+\S.{2,}|(?:图表|图|表)\s*\d+[\s:：.\-–—]*\S.{2,})\s*$",
    re.I,
)


class SourceValidationError(ValueError):
    """The complete source contract is not satisfied."""


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
    if len({row["content_sha256"] for row in bindings}) != len(bindings):
        raise SourceValidationError("Manifest contains duplicate PDF contents")
    return raw, bindings


def meaningful_characters(text: str) -> int:
    return sum(character.isalnum() for character in text)


def require_readable_page(text: str, source_name: str, page_number: int) -> int:
    count = meaningful_characters(text)
    if count < MIN_PAGE_CHARACTERS:
        raise SourceValidationError(
            f"{source_name} page {page_number} has insufficient native text ({count} characters); "
            "scanned or textless pages require extraction outside this fallback"
        )
    bad = sum(character == "\ufffd" or unicodedata.category(character) in {"Co", "Cs", "Cn"}
              or (unicodedata.category(character) == "Cc" and character not in "\n\r\t")
              for character in text)
    if bad / max(1, len(text)) > 0.02:
        raise SourceValidationError(f"{source_name} page {page_number} has an unreadable PDF text layer")
    return count


def file_record(path: Path, root: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    return {"path": path.relative_to(root).as_posix(), "sha256": sha256_bytes(raw), "size_bytes": len(raw)}


def _extract_report(pdf: Path, binding: dict[str, str], root: Path, index: int) -> dict[str, Any]:
    raw = pdf.read_bytes()
    if sha256_bytes(raw) != binding["content_sha256"]:
        raise SourceValidationError(f"Original PDF hash mismatch: {pdf.name}")
    if not raw.startswith(b"%PDF-"):
        raise SourceValidationError(f"Original file is not a PDF: {pdf.name}")
    directory = root / f"report_{index:04d}_{binding['content_sha256'][:12]}"
    directory.mkdir()
    markdown = (f"# {Path(binding['source_pdf']).stem}\n\n"
                "原文来源：原始 PDF 的可读文本层。以下逐页保留原文；图像为原报告页面。\n\n")
    assets: list[dict[str, Any]] = []
    page_records: list[dict[str, Any]] = []
    total_characters = 0
    try:
        with fitz.open(stream=raw, filetype="pdf") as document:
            if document.is_encrypted or document.needs_pass:
                raise SourceValidationError(f"Encrypted PDF is unsupported: {pdf.name}")
            if document.is_repaired or document.page_count <= 0:
                raise SourceValidationError(f"Damaged or empty PDF is unsupported: {pdf.name}")
            for page_index in range(document.page_count):
                page = document.load_page(page_index)
                page_number = page_index + 1
                text = page.get_text("text", sort=True).strip()
                characters = require_readable_page(text, pdf.name, page_number)
                total_characters += characters
                captions = [match.group(1).strip() for line in text.splitlines()
                            if (match := EXHIBIT_CAPTION.fullmatch(line))]
                markdown += f"## 原报告第 {page_number} 页\n\n"
                text_begin = len(markdown.encode("utf-8"))
                markdown += text
                text_end = len(markdown.encode("utf-8"))
                markdown += "\n\n"
                page_record: dict[str, Any] = {
                    "page": page_number, "native_text_characters": characters,
                    "native_text_sha256": sha256_bytes(text.encode("utf-8")),
                    "markdown_text_begin": text_begin, "markdown_text_end": text_end,
                }
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
    if total_characters < MIN_REPORT_CHARACTERS:
        raise SourceValidationError(f"{pdf.name} has insufficient text for a report summary ({total_characters} characters)")
    if pdf.read_bytes() != raw:
        raise SourceValidationError(f"Original PDF changed during extraction: {pdf.name}")
    markdown_path = directory / MARKDOWN_NAME
    markdown_path.write_text(markdown, encoding="utf-8")
    status = {
        "source_method": "native-pdf", **binding, "source_markdown": MARKDOWN_NAME,
        "page_count": len(page_records), "pages_covered": list(range(1, len(page_records) + 1)),
        "native_text_characters": total_characters,
        "images": [str(PurePosixPath(asset["path"]).relative_to(directory.name)) for asset in assets],
    }
    write_json(directory / "status.json", status)
    return {
        **binding, "directory": directory.name, "source_method": "native-pdf",
        "page_count": len(page_records), "pages_covered": status["pages_covered"],
        "native_text_characters": total_characters, "pages": page_records,
        "markdown": file_record(markdown_path, root),
        "status": file_record(directory / "status.json", root), "assets": assets,
    }


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


def extract_sources(input_dir: Path, manifest: Path, output_dir: Path, expected_reports: int) -> dict[str, Any]:
    input_dir, manifest, output_dir = Path(input_dir), Path(manifest), Path(output_dir)
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
        reports = [_extract_report(originals[binding["source_pdf"]], binding, staging, index)
                   for index, binding in enumerate(bindings, 1)]
        final_originals = _original_inventory(input_dir)
        if set(final_originals) != wanted or manifest.read_bytes() != raw_manifest:
            raise SourceValidationError("Original batch inventory or manifest changed during extraction")
        if any(sha256_bytes(final_originals[row["source_pdf"]].read_bytes()) != row["content_sha256"]
               for row in bindings):
            raise SourceValidationError("Original batch bytes changed during extraction")
        (staging / MANIFEST_NAME).write_bytes(raw_manifest)
        receipt = {
            "schema": SCHEMA, "source_method": "native-pdf", "complete": True,
            "expected_reports": expected_reports, "report_count": len(reports),
            "manifest_sha256": sha256_bytes(canonical_bytes(bindings)),
            "manifest_file": file_record(staging / MANIFEST_NAME, staging), "reports": reports,
        }
        write_json(staging / RECEIPT_NAME, receipt)
        validate_sources(staging, manifest, expected_reports)
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


def validate_sources(output_dir: Path, manifest: Path, expected_reports: int) -> dict[str, Any]:
    """Validate the complete transferred batch against its selected source manifest."""
    output_dir = Path(output_dir)
    if output_dir.is_symlink() or not output_dir.is_dir():
        raise SourceValidationError("Source output must be a regular directory")
    _, bindings = read_manifest(Path(manifest), expected_reports)
    receipt_path = output_dir / RECEIPT_NAME
    if receipt_path.is_symlink() or not receipt_path.is_file():
        raise SourceValidationError("Complete source receipt is missing")
    try:
        receipt = json.loads(receipt_path.read_bytes())
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise SourceValidationError("Complete source receipt is invalid JSON") from exc
    if not isinstance(receipt, dict) or type(receipt.get("schema")) is not int or receipt.get("schema") != SCHEMA:
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", nargs="?", choices=("extract", "validate"), default="extract")
    parser.add_argument("--input-dir", type=Path)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--expected-reports", type=int, required=True)
    args = parser.parse_args()
    if args.command == "extract" and args.input_dir is None:
        parser.error("--input-dir is required for extraction")
    try:
        receipt = (validate_sources(args.output_dir, args.manifest, args.expected_reports)
                   if args.command == "validate" else
                   extract_sources(args.input_dir, args.manifest, args.output_dir, args.expected_reports))
    except (OSError, SourceValidationError) as exc:
        print(f"Native Market Views source rejected: {exc}", file=sys.stderr)
        return 2
    print(f"Native Market Views source {args.command} complete: reports={receipt['report_count']}, "
          f"pages={sum(report['page_count'] for report in receipt['reports'])}, "
          f"exhibit_pages={sum(len(report['assets']) for report in receipt['reports'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
