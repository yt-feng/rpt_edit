"""Resolve an explicit report extraction without relabelling OCR as MinerU."""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


@dataclass(frozen=True)
class ExtractionSource:
    path: Path
    method: str
    sha256: str
    provenance_sha256: str | None

    def identity(self) -> dict:
        return {"source_method": self.method, "source_markdown": self.path.name,
                "source_sha256": self.sha256,
                "source_provenance_sha256": self.provenance_sha256}

    def cache_namespace(self) -> str:
        # Preserve existing MinerU memo paths. OCR never consumes those memos,
        # even when its extracted text happens to equal a MinerU result.
        if self.method == "mineru":
            return ""
        return "ocr-" + digest(json.dumps(self.identity(), sort_keys=True).encode())


def has_extraction_source(directory: Path) -> bool:
    return any((directory / name).exists() or (directory / name).is_symlink()
               for name in ("source_mineru.md", "source_ocr.md"))


def ocr_markdown_from_pages(pages, page_count: int) -> bytes:
    if not (isinstance(pages, list) and type(page_count) is int
            and 0 < page_count <= 1000 and len(pages) == page_count):
        raise ValueError("Invalid OCR page inventory")
    texts = []
    for number, page in enumerate(pages, 1):
        if not (isinstance(page, dict) and type(page.get("page")) is int
                and page["page"] == number and isinstance(page.get("text"), str)):
            raise ValueError("Invalid OCR page order")
        text = page["text"]
        if not (page.get("text_sha256") == digest(text.encode())
                and type(page.get("empty_text")) is bool
                and page["empty_text"] == (not bool(text.strip()))
                and page.get("method") in {"native", "ocr", "native+ocr"}):
            raise ValueError("Invalid OCR page evidence")
        texts.append(f"## Original page {number}\n\n{text}\n")
    if not any(page["text"].strip() for page in pages):
        raise ValueError("Empty OCR source")
    return ("# Original report page text (native extraction / OCR)\n\n" + "\n".join(texts)).encode()


def resolve_extraction_source(directory: Path) -> ExtractionSource:
    if directory.is_symlink():
        raise ValueError("Report extraction directory must not be a symlink")
    status_path = directory / "status.json"
    if status_path.is_symlink():
        raise ValueError("Report extraction status must not be a symlink")
    status = json.loads(status_path.read_text(encoding="utf-8")) if status_path.exists() else {}
    if not isinstance(status, dict):
        raise ValueError("Invalid report extraction status")
    present = [name for name in ("source_mineru.md", "source_ocr.md")
               if (directory / name).exists() or (directory / name).is_symlink()]
    if len(present) != 1:
        raise ValueError("Report extraction is missing or has conflicting sources")
    method = status.get("source_method", "mineru")
    if method not in {"mineru", "ocr"}:
        raise ValueError("Unknown report extraction method")
    name = "source_mineru.md" if method == "mineru" else "source_ocr.md"
    if status.get("source_markdown", name) != name or present != [name]:
        raise ValueError("Report extraction method and Markdown path disagree")
    source = directory / name
    if source.is_symlink() or not source.is_file():
        raise ValueError("Report extraction must be a regular Markdown file")
    content = source.read_bytes()
    if not content.strip():
        raise ValueError("Report extraction is empty")
    source_sha256 = digest(content)
    provenance = status.get("wechat_source_provenance")
    provenance_sha256 = None
    if method == "ocr" and (provenance is None or status.get("source_markdown") != name):
        raise ValueError("OCR extraction requires explicit source provenance")
    if provenance is not None:
        fields = {"source_kind", "source_pdf", "content_sha256", "source_receipt_sha256", "source_report_id"}
        if method == "ocr":
            fields.add("source_pages_sha256")
        if (not isinstance(provenance, dict) or set(provenance) != fields
                or provenance.get("source_kind") != {"mineru": "mineru-recovery", "ocr": "ocr-synthesis"}[method]
                or not isinstance(status.get("source_pdf"), str) or not status["source_pdf"]
                or provenance.get("source_pdf") != status["source_pdf"]
                or not isinstance(provenance.get("source_report_id"), str)
                or not re.fullmatch(r"[A-Za-z0-9_-]{1,160}", provenance["source_report_id"])
                or any(not isinstance(provenance.get(key), str)
                       or not re.fullmatch(r"[a-f0-9]{64}", provenance[key])
                       for key in fields if key.endswith("sha256"))):
            raise ValueError("Invalid report extraction provenance")
        provenance_sha256 = digest(json.dumps(provenance, sort_keys=True, ensure_ascii=True).encode())
    if method == "ocr":
        pages_path = directory / "source_ocr_pages.json"
        if pages_path.is_symlink() or not pages_path.is_file():
            raise ValueError("OCR source requires regular page evidence")
        raw_pages = pages_path.read_bytes()
        if digest(raw_pages) != provenance["source_pages_sha256"]:
            raise ValueError("OCR page evidence hash mismatch")
        pages = json.loads(raw_pages)
        if not isinstance(pages, list) or ocr_markdown_from_pages(pages, len(pages)) != content:
            raise ValueError("OCR Markdown does not match its page evidence")
    return ExtractionSource(source, method, source_sha256, provenance_sha256)
