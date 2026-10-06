#!/usr/bin/env python3
"""Bounded local publication-only screening of already selected source visuals.

This never changes source images or their proofs and never submits remote OCR.
The runner-local cache stores successful OCR only; failures are soft per image.
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
from typing import Any, Callable


OCR_SCHEMA = 1
OCR_TIMEOUT_SECONDS = 15
OCR_WORKERS = 4
OCR_MAX_TEXT = 100_000
OCR_MAX_IMAGE_BYTES = 32 * 1024 * 1024
OCR_MAX_IMAGE_PIXELS = 40_000_000


def all_candidates_are_publication_only(audit: Any) -> bool:
    """Narrow exception to the zero-figure gate, never to a rendering failure."""
    if not isinstance(audit, dict) or audit.get("schema_version") != 1:
        return False
    count, entries = audit.get("candidates"), audit.get("entries")
    allowed = {"exclude_research_staff_roster", "exclude_broker_rating_history",
               "exclude_analyst_coverage_table", "exclude_publication_disclosure"}
    return (type(count) is int and count > 0 and audit.get("excluded") == count
            and audit.get("retained") == 0 and isinstance(entries, list) and len(entries) == count
            and all(isinstance(entry, dict) and entry.get("candidate_index") == index
                    and entry.get("ocr_status") in {"ok", "cache_hit"}
                    and entry.get("decision") in allowed
                    for index, entry in enumerate(entries)))


def _ocr_one(path: Path, cache_dir: Path, executable: str | None) -> dict[str, Any]:
    try:
        if path.stat().st_size > OCR_MAX_IMAGE_BYTES:
            return {"status": "image_limit", "text": ""}
        image_sha = hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return {"status": "image_unreadable", "text": ""}
    identity = {"schema": OCR_SCHEMA, "engine": "tesseract-cli", "image_sha256": image_sha, "language": "eng", "psm": 11}
    key = hashlib.sha256(json.dumps(identity, sort_keys=True).encode()).hexdigest()
    cache_file = cache_dir / f"{key}.json"
    try:
        cached = json.loads(cache_file.read_text(encoding="utf-8"))
        if cached.get("identity") == identity and isinstance(cached.get("text"), str) and len(cached["text"]) <= OCR_MAX_TEXT:
            return {"status": "cache_hit", "image_sha256": image_sha, "text": cached["text"]}
    except (OSError, ValueError, TypeError, AttributeError):
        pass
    result = {"status": "unavailable", "image_sha256": image_sha, "text": ""}
    if not executable:
        return result
    try:
        from PIL import Image
        with Image.open(path) as image:
            if image.width * image.height > OCR_MAX_IMAGE_PIXELS:
                return {**result, "status": "image_limit"}
    except Exception:
        return {**result, "status": "image_unreadable"}
    try:
        process = subprocess.run(
            [executable, str(path.resolve()), "stdout", "-l", "eng", "--psm", "11"],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
            timeout=OCR_TIMEOUT_SECONDS, check=False,
            env={**os.environ, "OMP_THREAD_LIMIT": "1"},
        )
    except subprocess.TimeoutExpired:
        return {**result, "status": "timeout"}
    except OSError:
        return {**result, "status": "execution_error"}
    if process.returncode:
        return {**result, "status": "ocr_error"}
    if len(process.stdout) > OCR_MAX_TEXT:
        return {**result, "status": "text_limit"}
    result.update(status="ok", text=process.stdout)
    temporary = None
    try:
        cache_dir.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=cache_dir, suffix=".tmp", delete=False) as handle:
            handle.write(json.dumps({"identity": identity, "text": process.stdout}))
            temporary = Path(handle.name)
        temporary.replace(cache_file)
    except OSError:
        # Cache writes are optional; the current OCR result remains usable.
        pass
    finally:
        if temporary is not None:
            try:
                temporary.unlink(missing_ok=True)
            except OSError:
                pass
    return result


def filter_publication_figures(
    figures: list[dict[str, Any]], cache_dir: Path,
    classifier: Callable[[dict[str, Any]], str | None], *,
    log_fn: Callable[[str], None] = print,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Keep original ordering and objects; screen each unique image once.

    Caller must apply its per-report candidate cap before this function and use
    only this returned list for section selection and automatic figure filling.
    No raw OCR, filenames, author names or provider text enters log/audit output.
    """
    executable = shutil.which("tesseract")
    paths = list(dict.fromkeys(str(Path(fig["source_path"]).resolve()) for fig in figures))
    with ThreadPoolExecutor(max_workers=OCR_WORKERS) as executor:
        results = list(executor.map(lambda p: _ocr_one(Path(p), cache_dir, executable), paths))
    by_path = dict(zip(paths, results))
    kept, entries = [], []
    for index, fig in enumerate(figures):
        result = by_path[str(Path(fig["source_path"]).resolve())]
        # Pixel OCR has no trusted element type; permit the same explicit table
        # patterns as metadata, whose semantic guards also require table rows.
        reason = classifier({"kind": "table", "body_text": result["text"]}) if result["text"].strip() else None
        entry = {"candidate_index": index, "report_id": fig.get("report_id"),
                 "image_sha256": result.get("image_sha256"), "ocr_status": result["status"],
                 "decision": reason or "retain"}
        entries.append(entry)
        if reason:
            log_fn(f"Publication OCR candidate={index} status={result['status']} decision={reason}")
        else:
            kept.append(fig)
            if result["status"] not in {"ok", "cache_hit"}:
                log_fn(f"Publication OCR candidate={index} status={result['status']} decision=retain")
    statuses = {status: sum(x["ocr_status"] == status for x in entries)
                for status in sorted({x["ocr_status"] for x in entries})}
    audit = {"schema_version": 1, "engine": "tesseract-eng-psm11", "candidates": len(figures),
             "unique_images": len(paths), "retained": len(kept), "excluded": len(figures) - len(kept),
             "max_workers": OCR_WORKERS, "timeout_seconds": OCR_TIMEOUT_SECONDS,
             "statuses": statuses, "entries": entries}
    log_fn(f"Publication OCR candidates={len(figures)} retained={len(kept)} excluded={audit['excluded']} statuses={json.dumps(statuses, sort_keys=True)}")
    return kept, audit
