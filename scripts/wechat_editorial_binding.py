"""Bind one successful upstream article/title to its exact extraction bytes.

Only the producer creates a binding. Known subsequent transformations can carry
forward an already verified binding; a legacy or externally modified article
never acquires provenance just because another processing stage touched it.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re
from typing import Any

FIELD = "wechat_editorial_binding"
VERSION = 1


@dataclass(frozen=True)
class BoundArticle:
    article: str
    title: str
    decision: dict[str, Any]
    binding: dict[str, Any]
    model: str


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _title_metadata(status: dict[str, Any], article: str) -> dict[str, Any] | None:
    title, decision = status.get("wechat_title"), status.get("wechat_title_decision")
    heading = re.search(r"(?m)^#\s+(.+?)\s*$", article)
    if (status.get("error") or status.get("wechat_article") != "wechat_article.md"
            or status.get("wechat_title_source") != "source_filename_weighted_finetune"
            or not isinstance(title, str) or not title.strip()
            or not isinstance(decision, dict) or decision.get("needs_model_repair")
            or decision.get("repair_error") or decision.get("selected_quality_issues")
            or decision.get("final_title_after_wording_guard") != title
            or not heading or heading.group(1) != title):
        return None
    return {"title": title, "decision": decision, "source_pdf": status.get("source_pdf"),
            "title_source": status["wechat_title_source"], "model": status.get("wechat_editorial_model", "unknown")}


def _fingerprints(directory: Path, status: dict[str, Any]) -> tuple[dict[str, Any], str] | None:
    provenance = status.get("wechat_source_provenance")
    extra = {}
    source_name = "source_mineru.md"
    if provenance is not None:
        if not isinstance(provenance, dict):
            return None
        kind = provenance.get("source_kind")
        keys = {"source_kind", "source_pdf", "content_sha256", "source_receipt_sha256", "source_report_id"}
        if kind == "ocr-synthesis":
            keys.add("source_pages_sha256")
            source_name = "source_ocr.md"
        if (kind not in {"mineru-recovery", "ocr-synthesis"} or set(provenance) != keys
                or provenance.get("source_pdf") != status.get("source_pdf")
                or status.get("source_method") != ("ocr" if kind == "ocr-synthesis" else "mineru")
                or status.get("source_markdown") != source_name
                or not isinstance(provenance.get("source_report_id"), str)
                or not re.fullmatch(r"[A-Za-z0-9_-]{1,160}", provenance["source_report_id"])
                or any(not isinstance(provenance.get(key), str)
                       or not re.fullmatch(r"[a-f0-9]{64}", provenance[key])
                       for key in keys if key.endswith("sha256"))):
            return None
        extra = {"source_kind": kind, "source_markdown": source_name,
                 "source_provenance_sha256": digest(json.dumps(provenance, sort_keys=True, ensure_ascii=True).encode())}
    source, article = directory / source_name, directory / "wechat_article.md"
    if source.is_symlink() or article.is_symlink():
        return None
    source_bytes, article_bytes = source.read_bytes(), article.read_bytes()
    if provenance is not None:
        other = directory / ("source_mineru.md" if source_name == "source_ocr.md" else "source_ocr.md")
        if other.exists() or other.is_symlink():
            return None
        if provenance["source_kind"] == "ocr-synthesis":
            from report_extraction_source import ocr_markdown_from_pages
            pages_path = directory / "source_ocr_pages.json"
            if pages_path.is_symlink() or not pages_path.is_file():
                return None
            raw_pages = pages_path.read_bytes()
            if digest(raw_pages) != provenance["source_pages_sha256"]:
                return None
            pages = json.loads(raw_pages)
            if not isinstance(pages, list) or ocr_markdown_from_pages(pages, len(pages)) != source_bytes:
                return None
    body = article_bytes.decode("utf-8")
    metadata = _title_metadata(status, body)
    if not source_bytes or not body.strip() or metadata is None:
        return None
    return {"version": 2 if extra else VERSION, **extra, "source_sha256": digest(source_bytes),
            "article_sha256": digest(article_bytes),
            "title_metadata_sha256": digest(json.dumps(metadata, sort_keys=True, ensure_ascii=True).encode())}, body


def bind_generated_article(directory: Path, status: dict[str, Any]) -> bool:
    """Called only after a newly generated body/title has passed producer guards."""
    fingerprints = _fingerprints(directory, status)
    if fingerprints is None:
        status.pop(FIELD, None)
        return False
    status[FIELD] = fingerprints[0]
    return True


def read_bound_article(directory: Path) -> BoundArticle | None:
    try:
        status = json.loads((directory / "status.json").read_text(encoding="utf-8"))
        if not isinstance(status, dict) or not isinstance(status.get(FIELD), dict):
            return None
        current = _fingerprints(directory, status)
        if current is None or status[FIELD] != current[0]:
            return None
        return BoundArticle(current[1], status["wechat_title"], status["wechat_title_decision"], current[0],
                            str(status.get("wechat_editorial_model", "unknown")))
    except (OSError, ValueError, TypeError, KeyError):
        return None


def advance_binding(directory: Path, before: BoundArticle | None, *, status: dict[str, Any] | None = None) -> bool:
    """Carry forward exact verified source/title provenance after a known edit.

When status is supplied, update it in memory for the caller's existing write.
Otherwise update the on-disk status. Never accept source or title changes here.
"""
    if before is None:
        return False
    try:
        supplied = status is not None
        if status is None:
            status = json.loads((directory / "status.json").read_text(encoding="utf-8"))
        if not isinstance(status, dict) or status.get(FIELD) != before.binding:
            return False
        current = _fingerprints(directory, status)
        if current is None or {key: value for key, value in current[0].items() if key != "article_sha256"} != {
                key: value for key, value in before.binding.items() if key != "article_sha256"}:
            return False
        status[FIELD] = current[0]
        if not supplied:
            (directory / "status.json").write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
        return True
    except (OSError, ValueError, TypeError, KeyError):
        return False
