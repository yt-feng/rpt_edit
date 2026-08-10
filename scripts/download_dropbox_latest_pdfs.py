#!/usr/bin/env python3
"""Download PDFs from the latest date-named folder under a Dropbox root.

Expected Dropbox layout:
/zip_backup/
  260512/
    a.pdf
    nested/b.pdf
  260513/
    c.pdf

The script selects the latest date-like child folder by numeric name and downloads all PDFs
inside it recursively into --output-dir.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any

import requests

DROPBOX_API = "https://api.dropboxapi.com/2"
DROPBOX_CONTENT = "https://content.dropboxapi.com/2"
DATE_FOLDER_RE = re.compile(r"^\d{6,8}$")
DOWNLOAD_MAX_ATTEMPTS = 3
DOWNLOAD_RETRY_BASE_SECONDS = 2.0
DOWNLOAD_RETRY_MAX_SECONDS = 15.0
DOWNLOAD_RETRY_AFTER_MAX_SECONDS = 300.0
RETRYABLE_DOWNLOAD_STATUSES = {408, 425, 429, 500, 502, 503, 504}
TRANSIENT_DOWNLOAD_ERRORS = (
    requests.exceptions.ConnectionError,
    requests.exceptions.Timeout,
    requests.exceptions.ChunkedEncodingError,
)


def log(message: str) -> None:
    print(message, flush=True)


def write_github_output(key: str, value: str) -> None:
    output_path = os.getenv("GITHUB_OUTPUT")
    if not output_path:
        return
    with open(output_path, "a", encoding="utf-8") as f:
        safe_value = str(value).replace("\n", " ")
        f.write(f"{key}={safe_value}\n")


def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def dropbox_access_token() -> str:
    app_key = require_env("DROPBOX_APP_KEY")
    app_secret = require_env("DROPBOX_APP_SECRET")
    refresh_token = require_env("DROPBOX_REFRESH_TOKEN")
    response = requests.post(
        "https://api.dropboxapi.com/oauth2/token",
        data={"grant_type": "refresh_token", "refresh_token": refresh_token},
        auth=(app_key, app_secret),
        timeout=60,
    )
    if response.status_code >= 400:
        raise RuntimeError(f"Dropbox token refresh failed: HTTP {response.status_code}, {response.text[:500]}")
    data = response.json()
    token = data.get("access_token")
    if not token:
        raise RuntimeError(f"Dropbox token refresh response did not include access_token: {data}")
    return token


def api_post(token: str, endpoint: str, payload: dict[str, Any]) -> dict[str, Any]:
    response = requests.post(
        f"{DROPBOX_API}{endpoint}",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        json=payload,
        timeout=90,
    )
    if response.status_code >= 400:
        raise RuntimeError(f"Dropbox API {endpoint} failed: HTTP {response.status_code}, {response.text[:800]}")
    return response.json()


def list_folder(token: str, path: str, recursive: bool = False) -> list[dict[str, Any]]:
    data = api_post(token, "/files/list_folder", {"path": path, "recursive": recursive, "include_deleted": False})
    entries = list(data.get("entries", []))
    while data.get("has_more"):
        data = api_post(token, "/files/list_folder/continue", {"cursor": data["cursor"]})
        entries.extend(data.get("entries", []))
    return entries


def latest_date_folder(entries: list[dict[str, Any]]) -> dict[str, Any]:
    folders = [
        e for e in entries
        if e.get(".tag") == "folder" and DATE_FOLDER_RE.match(str(e.get("name", "")))
    ]
    if not folders:
        names = ", ".join(str(e.get("name")) for e in entries[:20])
        raise RuntimeError(f"No date-named child folders found. First entries: {names}")
    return max(folders, key=lambda e: int(e["name"]))


def safe_local_relpath(dropbox_path: str, latest_path: str, fallback_name: str) -> str:
    """Create a safe local relative path while preserving readable filenames when possible."""
    rel = str(dropbox_path).replace(str(latest_path).rstrip("/") + "/", "", 1).lstrip("/")
    if not rel or rel == dropbox_path.lstrip("/"):
        rel = fallback_name
    parts = []
    for part in Path(rel).parts:
        cleaned = part.replace("/", "_").replace("\\", "_").strip()
        parts.append(cleaned or "file")
    return str(Path(*parts)) if parts else fallback_name


def download_retry_delay(attempt: int, response: requests.Response | None = None) -> float:
    """Return bounded backoff while honoring reasonable numeric Retry-After values."""
    delay = min(
        DOWNLOAD_RETRY_MAX_SECONDS,
        DOWNLOAD_RETRY_BASE_SECONDS * (2 ** max(0, attempt - 1)),
    )
    if response is not None:
        retry_after = response.headers.get("Retry-After", "").strip()
        try:
            retry_after_seconds = max(0.0, float(retry_after))
            delay = max(
                delay,
                min(DOWNLOAD_RETRY_AFTER_MAX_SECONDS, retry_after_seconds),
            )
        except (TypeError, ValueError):
            pass
    return delay


def download_file(token: str, dropbox_path: str, local_path: Path) -> None:
    local_path.parent.mkdir(parents=True, exist_ok=True)
    # HTTP headers must be latin-1 encodable. json.dumps default ensure_ascii=True
    # escapes non-ASCII characters such as Chinese punctuation in Dropbox paths.
    dropbox_api_arg = json.dumps({"path": dropbox_path})
    for attempt in range(1, DOWNLOAD_MAX_ATTEMPTS + 1):
        try:
            response = requests.post(
                f"{DROPBOX_CONTENT}/files/download",
                headers={
                    "Authorization": f"Bearer {token}",
                    "Dropbox-API-Arg": dropbox_api_arg,
                },
                timeout=300,
            )
        except TRANSIENT_DOWNLOAD_ERRORS as exc:
            if attempt >= DOWNLOAD_MAX_ATTEMPTS:
                raise RuntimeError(
                    f"Dropbox download failed for {dropbox_path} after {attempt} attempts: "
                    f"{type(exc).__name__}: {exc}"
                ) from exc
            delay = download_retry_delay(attempt)
            log(
                f"Dropbox download transient {type(exc).__name__} for {dropbox_path} "
                f"on attempt {attempt}/{DOWNLOAD_MAX_ATTEMPTS}; retrying in {delay:g}s."
            )
            time.sleep(delay)
            continue

        if response.status_code < 400:
            try:
                local_path.write_bytes(response.content)
            finally:
                response.close()
            return

        error_text = response.text[:500]
        retryable = response.status_code in RETRYABLE_DOWNLOAD_STATUSES
        if not retryable or attempt >= DOWNLOAD_MAX_ATTEMPTS:
            response.close()
            raise RuntimeError(
                f"Dropbox download failed for {dropbox_path}: "
                f"HTTP {response.status_code}, {error_text}"
            )

        delay = download_retry_delay(attempt, response)
        status_code = response.status_code
        response.close()
        log(
            f"Dropbox download retryable HTTP {status_code} for {dropbox_path} "
            f"on attempt {attempt}/{DOWNLOAD_MAX_ATTEMPTS}; retrying in {delay:g}s."
        )
        time.sleep(delay)

    raise RuntimeError(f"Dropbox download retry loop ended unexpectedly for {dropbox_path}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dropbox-root", default="/zip_backup")
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    try:
        token = dropbox_access_token()
        root = args.dropbox_root.rstrip("/") or ""
        output_dir = Path(args.output_dir).resolve()
        output_dir.mkdir(parents=True, exist_ok=True)

        log(f"Listing Dropbox root: {root}")
        root_entries = list_folder(token, root, recursive=False)
        latest = latest_date_folder(root_entries)
        latest_name = latest["name"]
        latest_path = latest.get("path_lower") or latest.get("path_display") or f"{root}/{latest_name}"
        log(f"Latest Dropbox date folder: {latest_path}")

        entries = list_folder(token, latest_path, recursive=True)
        pdfs = [e for e in entries if e.get(".tag") == "file" and str(e.get("name", "")).lower().endswith(".pdf")]
        if not pdfs:
            raise RuntimeError(f"No PDFs found under latest Dropbox folder: {latest_path}")

        manifest: list[dict[str, str]] = []
        for entry in pdfs:
            dropbox_path = entry.get("path_lower") or entry.get("path_display")
            if not dropbox_path:
                log(f"Skipping entry without path: {entry}")
                continue
            rel = safe_local_relpath(str(dropbox_path), str(latest_path), str(entry.get("name", "report.pdf")))
            local_path = output_dir / rel
            log(f"Downloading PDF: {dropbox_path} -> {local_path}")
            download_file(token, str(dropbox_path), local_path)
            manifest.append({"dropbox_path": str(dropbox_path), "local_path": str(local_path), "name": str(entry.get("name", ""))})

        if not manifest:
            raise RuntimeError(f"No PDFs were downloaded from latest Dropbox folder: {latest_path}")

        manifest_path = output_dir / "dropbox_manifest.json"
        manifest_path.write_text(json.dumps({"latest_folder": latest_name, "latest_path": latest_path, "pdf_count": len(manifest), "files": manifest}, ensure_ascii=False, indent=2), encoding="utf-8")

        write_github_output("latest_folder", latest_name)
        write_github_output("latest_path", str(latest_path))
        write_github_output("pdf_count", str(len(manifest)))
        write_github_output("input_dir", str(output_dir))
        log(f"Downloaded {len(manifest)} PDFs from {latest_name} to {output_dir}")
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
