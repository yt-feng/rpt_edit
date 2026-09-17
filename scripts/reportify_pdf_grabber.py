#!/usr/bin/env python3
"""Fetch only an explicitly authorized full PDF from the report detail API.

The cloud workflow reads the short-lived session from R2. Preview images, guessed
CDN paths and browser printouts are never considered deliverable report PDFs.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
from io import BytesIO
import json
import math
import os
from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

API_ORIGIN = "https://api.reportify.cn"
ASSET_HOSTS = {"api.reportify.cn", "s.reportify.cn", "reportify.cn", "www.reportify.cn"}
SESSION_KEY = "reportify-auth/session.json"
SESSION_MAX_AGE_SECONDS = 12 * 60 * 60
MAX_PDF_BYTES = 100 * 1024 * 1024
MESSAGES = {
    "upstream_login_required": "The upstream report requires a current authorized session.",
    "upstream_access_required": "The current upstream account cannot access the full report.",
    "upstream_unavailable": "The upstream full report is currently unavailable.",
    "invalid_pdf": "The returned file did not match the complete report.",
}


class ReportifyUnavailable(Exception):
    def __init__(self, reason: str, detail_code: str, **metrics):
        self.reason, self.detail_code, self.metrics = reason, detail_code, metrics
        super().__init__(MESSAGES[reason])


def report_id_from_url(url: str) -> str:
    parsed = urlsplit(url)
    match = re.fullmatch(r"/reports/([0-9]{6,25})/?", parsed.path)
    if (parsed.scheme != "https" or parsed.hostname not in {"reportify.cn", "www.reportify.cn"}
            or parsed.username or parsed.password or parsed.port not in (None, 443) or not match):
        raise ValueError("Use an HTTPS report URL with a numeric report ID")
    return match[1]


def stored_session_token(client, bucket: str, *, now: datetime | None = None) -> str:
    """Read the same 12-hour session used by the Worker; never expose its body."""
    try:
        obj = client.get_object(Bucket=bucket, Key=SESSION_KEY)
        body = obj["Body"]
        try:
            raw = body.read(64 * 1024 + 1)
        finally:
            body.close()
    except Exception as exc:
        code = str(getattr(exc, "response", {}).get("Error", {}).get("Code", ""))
        if code in {"NoSuchKey", "404", "NotFound"}:
            return ""
        raise ReportifyUnavailable("upstream_unavailable", "credential_store_unavailable") from None
    try:
        if len(raw) > 64 * 1024:
            return ""
        data = json.loads(raw)
        token = data.get("token")
        updated = datetime.fromisoformat(str(data.get("updated_at", "")).replace("Z", "+00:00"))
        age = ((now or datetime.now(timezone.utc)) - updated).total_seconds()
        if not isinstance(token, str) or not token.strip() or not 0 <= age <= SESSION_MAX_AGE_SECONDS:
            return ""
        if any(ord(char) < 32 for char in token):
            return ""
        return token.strip()
    except (ValueError, TypeError, AttributeError):
        return ""


def runtime_r2_client():
    from mark_reportify_pdf_status import build_r2_client
    try:
        return build_r2_client()
    except SystemExit:
        raise ReportifyUnavailable("upstream_unavailable", "credential_store_unconfigured") from None


def allowed_asset_url(value: str) -> bool:
    try:
        parsed = urlsplit(value)
        return bool(parsed.scheme == "https" and parsed.hostname in ASSET_HOSTS
                    and not parsed.username and not parsed.password and parsed.port in (None, 443)
                    and not any(char.isspace() or ord(char) < 32 for char in value))
    except ValueError:
        return False


class _NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def fetch_bytes(url: str, *, token: str = "", cookie: str = "", maximum: int, accept: str) -> bytes:
    """Follow bounded allowed HTTPS redirects; API credentials never reach a CDN."""
    opener = build_opener(_NoRedirect())
    for _ in range(4):
        if not allowed_asset_url(url):
            raise ReportifyUnavailable("upstream_unavailable", "invalid_asset_url")
        headers = {"Accept": accept, "User-Agent": "Mozilla/5.0", "Referer": "https://reportify.cn/"}
        if urlsplit(url).hostname == "api.reportify.cn":
            if token:
                headers["Authorization"] = f"Bearer {token}"
            if cookie:
                headers["Cookie"] = cookie
        try:
            with opener.open(Request(url, headers=headers), timeout=90) as response:
                body = response.read(maximum + 1)
                if len(body) > maximum:
                    raise ReportifyUnavailable("upstream_unavailable", "response_too_large")
                return body
        except HTTPError as exc:
            if exc.code in {301, 302, 303, 307, 308} and exc.headers.get("Location"):
                url = urljoin(url, exc.headers["Location"])
                exc.close()
                continue
            status = exc.code
            exc.close()
            reason = ("upstream_login_required" if status == 401 else
                      "upstream_access_required" if status == 403 and (token or cookie) else
                      "upstream_login_required" if status == 403 else "upstream_unavailable")
            raise ReportifyUnavailable(reason, f"http_{status}") from None
        except (URLError, TimeoutError, OSError, ValueError):
            raise ReportifyUnavailable("upstream_unavailable", "request_failed") from None
    raise ReportifyUnavailable("upstream_unavailable", "too_many_redirects")


def _positive_integer(value) -> int:
    if isinstance(value, bool):
        return 0
    try:
        parsed = int(value)
        exact = value == parsed if type(value) in (int, float) else str(value).strip() == str(parsed)
        return parsed if exact and 0 < parsed <= 2**53 - 1 else 0
    except (ValueError, TypeError, OverflowError):
        return 0


def expected_page_count(detail: dict) -> int:
    if not isinstance(detail, dict) or not isinstance(detail.get("main"), dict):
        raise ReportifyUnavailable("upstream_unavailable", "invalid_detail")
    main = detail["main"]
    meta = main.get("meta_data") if isinstance(main.get("meta_data"), dict) else {}
    return _positive_integer(meta.get("document_total_page") or main.get("document_total_page")
                             or main.get("page_count") or main.get("pages"))


def authorized_pdf(detail: dict, *, authenticated: bool) -> tuple[str, int]:
    """Explicit API permission is required; top-level flags outrank legacy main."""
    expected = expected_page_count(detail)
    main = detail["main"]
    permissions = detail if "readable" in detail or "resource_limit" in detail else main
    readable = permissions.get("readable")
    # resource_limit may describe a separate quota. It cannot override an
    # explicit readable=true with an actual full-PDF URL, nor grant access.
    if "resource_limit" in permissions:
        limit = permissions["resource_limit"]
        if type(limit) not in (int, float) or not math.isfinite(limit) or limit < 0:
            raise ReportifyUnavailable("upstream_unavailable", "invalid_resource_limit", expected_page_count=expected)
    if readable is False:
        raise ReportifyUnavailable("upstream_access_required" if authenticated else "upstream_login_required",
                                   "full_report_not_authorized", expected_page_count=expected)
    if readable is not True:
        raise ReportifyUnavailable("upstream_unavailable", "read_permission_unknown", expected_page_count=expected)
    url = main.get("url_pdf")
    if not isinstance(url, str) or not url.strip():
        raise ReportifyUnavailable("upstream_unavailable", "full_pdf_not_exposed", expected_page_count=expected)
    if not allowed_asset_url(url.strip()):
        raise ReportifyUnavailable("upstream_unavailable", "invalid_asset_url", expected_page_count=expected)
    if not expected:
        raise ReportifyUnavailable("upstream_unavailable", "expected_page_count_missing")
    return url.strip(), expected


def validate_pdf(data: bytes, expected_pages: int) -> int:
    if not data.startswith(b"%PDF-"):
        raise ReportifyUnavailable("invalid_pdf", "not_pdf", expected_page_count=expected_pages)
    from pypdf import PdfReader
    try:
        reader = PdfReader(BytesIO(data), strict=True)
        if reader.is_encrypted:
            raise ValueError("encrypted")
        pages = len(reader.pages)
    except Exception:
        raise ReportifyUnavailable("invalid_pdf", "unreadable_pdf", expected_page_count=expected_pages) from None
    if not expected_pages or pages != expected_pages:
        raise ReportifyUnavailable("invalid_pdf", "page_count_mismatch", page_count=pages,
                                   expected_page_count=expected_pages)
    return pages


def cached_pdf(client, bucket: str, report_id: str, expected: int) -> bytes | None:
    """Validate an already stored PDF, without fetching any gated upstream file."""
    try:
        obj = client.get_object(Bucket=bucket, Key=f"reportify/{report_id}.pdf")
        body = obj["Body"]
        try:
            data = body.read(MAX_PDF_BYTES + 1)
        finally:
            body.close()
    except Exception as exc:
        code = str(getattr(exc, "response", {}).get("Error", {}).get("Code", ""))
        if code in {"NoSuchKey", "404", "NotFound"}:
            return None
        raise ReportifyUnavailable("upstream_unavailable", "cache_store_unavailable") from None
    if len(data) > MAX_PDF_BYTES:
        raise ReportifyUnavailable("invalid_pdf", "cached_pdf_too_large", expected_page_count=expected)
    validate_pdf(data, expected)
    return data


def grab_report(report_id: str, output: Path, *, token: str = "", cookie: str = "", fetch=fetch_bytes,
                cache_client=None, bucket: str = "portal-suite-pdfs") -> dict:
    detail_bytes = fetch(f"{API_ORIGIN}/reports/{report_id}", token=token, cookie=cookie,
                         maximum=2 * 1024 * 1024, accept="application/json")
    try:
        detail = json.loads(detail_bytes)
    except (ValueError, UnicodeError):
        raise ReportifyUnavailable("upstream_unavailable", "invalid_detail") from None
    expected = expected_page_count(detail)
    data, cache_error = None, None
    if cache_client is not None and expected:
        try:
            data = cached_pdf(cache_client, bucket, report_id, expected)
        except ReportifyUnavailable as exc:
            if exc.reason != "invalid_pdf":
                raise
            cache_error = exc
    cached = data is not None
    if data is None:
        try:
            url, expected = authorized_pdf(detail, authenticated=bool(token or cookie))
        except ReportifyUnavailable:
            if cache_error is not None:
                raise cache_error
            raise
        data = fetch(url, token=token, cookie=cookie, maximum=MAX_PDF_BYTES, accept="application/pdf")
    pages = validate_pdf(data, expected)
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_name(output.name + ".download")
    temporary.write_bytes(data)
    temporary.replace(output)
    return {"version": 1, "id": report_id, "status": "ready", "validated": True, "cached": cached,
            "page_count": pages, "expected_page_count": expected, "sha256": hashlib.sha256(data).hexdigest(),
            "size_bytes": len(data), "reason": "", "error_code": "", "message": "Complete report PDF verified."}


def write_result(path: Path, result: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    temporary.replace(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--result-json", help="Machine-readable result (default: output path + .result.json)")
    parser.add_argument("--session-from-r2", action="store_true", help="Read the current server-side R2 session")
    parser.add_argument("--headless", action="store_true", help="Compatibility flag; the API path uses no browser")
    parser.add_argument("--auth-token", default=os.getenv("REPORTIFY_AUTH_TOKEN", ""), help="Prefer runtime secret env or R2")
    parser.add_argument("--cookie-header", default=os.getenv("REPORTIFY_COOKIE_HEADER") or os.getenv("REPORTIFY_COOKIE", ""))
    args = parser.parse_args()
    report_id = report_id_from_url(args.url)
    output = Path(args.output).expanduser().resolve()
    result_path = Path(args.result_json) if args.result_json else output.with_name(output.name + ".result.json")
    try:
        client = runtime_r2_client() if args.session_from_r2 else None
        bucket = os.getenv("R2_BUCKET", "").strip() or "portal-suite-pdfs"
        token = stored_session_token(client, bucket) if client else args.auth_token.strip()
        result = grab_report(report_id, output, token=token, cookie=args.cookie_header, cache_client=client, bucket=bucket)
    except ReportifyUnavailable as exc:
        result = {"version": 1, "id": report_id, "status": "failed", "validated": False,
                  "reason": exc.reason, "error_code": exc.reason, "detail_code": exc.detail_code,
                  "message": MESSAGES[exc.reason], **exc.metrics}
    write_result(result_path, result)
    # No signed URLs, token values, API bodies or raw transport exceptions.
    print(json.dumps({key: result[key] for key in ("id", "status", "reason", "detail_code", "page_count", "expected_page_count") if key in result}))
    return 0 if result["status"] == "ready" else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        raise SystemExit(130)
    except Exception:
        print("Report preparation failed before a verified result was available.", file=sys.stderr)
        raise SystemExit(1)
