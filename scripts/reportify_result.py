"""Shared validation for the grabber's public-safe result sidecar."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re

from reportify_pdf_grabber import MESSAGES, validate_pdf


def read_result(path: Path, report_id: str) -> dict:
    if path.stat().st_size > 64 * 1024:
        raise ValueError("Report result is too large")
    result = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(result, dict) or result.get("id") != report_id or result.get("version") != 1:
        raise ValueError("Report result identity mismatch")
    return result


def ready_metadata(result: dict, data: bytes | None = None) -> dict[str, str]:
    pages, expected = result.get("page_count"), result.get("expected_page_count")
    if (result.get("status") != "ready" or result.get("validated") is not True
            or type(pages) is not int or type(expected) is not int or pages <= 0 or pages != expected
            or not isinstance(result.get("sha256"), str) or not re.fullmatch(r"[0-9a-f]{64}", result["sha256"])):
        raise ValueError("Report result is not a verified full PDF")
    if data is not None:
        if hashlib.sha256(data).hexdigest() != result["sha256"]:
            raise ValueError("Report PDF changed after validation")
        validate_pdf(data, expected)
    return {"source": "reportify", "validated": "true", "page_count": str(pages),
            "expected_page_count": str(expected)}


def status_fields(status: str, result: dict | None) -> dict:
    if status == "ready":
        ready_metadata(result or {})
        return {"validated": True, "page_count": result["page_count"],
                "expected_page_count": result["expected_page_count"], "reason": "", "error_code": ""}
    if status != "failed":
        return {}
    reason = result.get("reason") if isinstance(result, dict) and result.get("status") == "failed" else None
    if reason not in MESSAGES:
        reason = "upstream_unavailable"
    fields = {"validated": False, "reason": reason, "error_code": reason, "message": MESSAGES[reason]}
    if isinstance(result, dict):
        for key in ("page_count", "expected_page_count"):
            if type(result.get(key)) is int and result[key] >= 0:
                fields[key] = result[key]
        # Restrict diagnostics to identifiers, never arbitrary upstream messages.
        detail = result.get("detail_code")
        if isinstance(detail, str) and re.fullmatch(r"[a-z0-9_]{1,80}", detail):
            fields["detail_code"] = detail
    return fields
