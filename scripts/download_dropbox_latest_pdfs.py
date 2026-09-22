#!/usr/bin/env python3
"""Download PDFs from a date-named folder under a Dropbox root.

Expected Dropbox layout:
/zip_backup/
  260512/
    a.pdf
    nested/b.pdf
  260513/
    c.pdf

The script orders YYMMDD / YYYYMMDD folders by calendar date. Explicit dates never
fall back to a different batch. Scheduled callers can allow a bounded calendar-day
lag between the report batch and the run date; the default remains strict (zero).
All PDFs inside the selected folder are downloaded recursively into --output-dir.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from datetime import date
from pathlib import Path
from typing import Any

import requests

DROPBOX_API = "https://api.dropboxapi.com/2"
DROPBOX_CONTENT = "https://content.dropboxapi.com/2"
DATE_FOLDER_RE = re.compile(r"^(?:[0-9]{6}|[0-9]{8})$")
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


def parse_date_folder(name: str) -> date:
    """Parse a real calendar date; short years explicitly mean 2000-2099."""
    if not DATE_FOLDER_RE.fullmatch(name):
        raise RuntimeError(
            f"Dropbox date folder must contain 6 to 8 digits in YYMMDD or YYYYMMDD format: {name!r}"
        )
    expanded = "20" + name if len(name) == 6 else name
    try:
        return date(int(expanded[:4]), int(expanded[4:6]), int(expanded[6:]))
    except ValueError as exc:
        raise RuntimeError(f"Invalid Dropbox calendar date: {name!r}") from exc


def dated_folders(entries: list[dict[str, Any]]) -> list[tuple[date, dict[str, Any]]]:
    folders = []
    for entry in entries:
        if entry.get(".tag") != "folder":
            continue
        try:
            parsed = parse_date_folder(str(entry.get("name", "")))
        except RuntimeError:
            continue
        folders.append((parsed, entry))
    return sorted(folders, key=lambda item: (item[0], str(item[1]["name"])), reverse=True)


def recent_date_folder_names(entries: list[dict[str, Any]]) -> list[str]:
    """Only expose bounded, validated date names, never arbitrary file names."""
    return [str(entry["name"]) for _, entry in dated_folders(entries)[:20]]


def latest_date_folder(entries: list[dict[str, Any]]) -> dict[str, Any]:
    folders = dated_folders(entries)
    if not folders:
        raise RuntimeError("No valid date-named child folders found (YYMMDD or YYYYMMDD).")
    newest_date = folders[0][0]
    matches = [entry for parsed, entry in folders if parsed == newest_date]
    if len(matches) != 1:
        names = ", ".join(str(entry["name"]) for entry in matches[:20])
        raise RuntimeError(
            f"Multiple Dropbox folders represent latest batch {newest_date}: {names}. "
            "Specify --date-folder with the exact folder name; no automatic choice was made."
        )
    return matches[0]


def select_date_folder(entries: list[dict[str, Any]], requested: str = "") -> dict[str, Any]:
    """Select the requested batch, allowing only an equivalent date-format alias."""
    requested = requested.strip()
    if not requested:
        return latest_date_folder(entries)
    requested_date = parse_date_folder(requested)
    for entry in entries:
        if entry.get(".tag") == "folder" and str(entry.get("name", "")) == requested:
            return entry
    matches = [entry for parsed, entry in dated_folders(entries) if parsed == requested_date]
    if len(matches) == 1:
        return matches[0]
    available = ", ".join(recent_date_folder_names(entries)) or "<none>"
    raise RuntimeError(
        f"Requested Dropbox date folder was not found: {requested}. "
        f"Available date folders (newest first): {available}. "
        "No fallback to a different report batch was performed. "
        "Check the batch date, root path and the Dropbox account/namespace used by this workflow."
    )


def validate_expected_date_folder(
    selected: dict[str, Any], expected: str = "", max_age_days: int = 0
) -> dict[str, Any]:
    """Require source date in [expected - max_age_days, expected], inclusive."""
    if max_age_days < 0:
        raise RuntimeError("--max-folder-age-days must be non-negative")
    expected = expected.strip()
    if not expected:
        return selected
    expected_date = parse_date_folder(expected)
    selected_name = str(selected.get("name", ""))
    selected_date = parse_date_folder(selected_name)
    age = (expected_date - selected_date).days
    if not 0 <= age <= max_age_days:
        raise RuntimeError(
            "Fresh Dropbox date folder was not available: "
            f"expected {expected}, selected latest folder {selected_name or '<unknown>'}. "
            f"Source age is {age} calendar days; allowed age is 0..{max_age_days}. "
            "Stopped before processing stale or future-dated reports. "
            "For an intentional historical backfill, specify --date-folder without --expected-date-folder."
        )
    return selected


def write_input_summary(diagnostics: dict[str, Any]) -> None:
    summary_path = os.getenv("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    try:
        with open(summary_path, "a", encoding="utf-8") as stream:
            stream.write("## Dropbox input selection\n\n")
            stream.write("```json\n" + json.dumps(diagnostics, ensure_ascii=True, indent=2) + "\n```\n")
            stream.write("Input download status is not article generation or publication status.\n\n")
    except OSError:
        log("WARNING: Could not write Dropbox input summary; primary result is unchanged.")


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
    parser.add_argument(
        "--date-folder",
        default="",
        help="YYMMDD or YYYYMMDD report batch; empty selects the latest calendar date",
    )
    parser.add_argument(
        "--expected-date-folder",
        default="",
        help="Latest allowed source date, normally the Beijing run date; used with --max-folder-age-days",
    )
    parser.add_argument(
        "--max-folder-age-days",
        type=int,
        default=0,
        help="Maximum calendar-day batch lag from --expected-date-folder; 0 is strict, 1 permits overnight batches",
    )
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    diagnostics: dict[str, Any] = {
        "status": "failed",
        "requested_date_folder": args.date_folder.strip(),
        "expected_date_folder": args.expected_date_folder.strip(),
        "max_folder_age_days": args.max_folder_age_days,
        "available_date_folders": [],
        "selected_date_folder": None,
        "pdf_count": 0,
        "downloaded_pdf_count": 0,
    }

    try:
        # Reject malformed policy inputs before accessing credentials or Dropbox.
        if args.max_folder_age_days < 0:
            raise RuntimeError("--max-folder-age-days must be non-negative")
        for value in (args.date_folder.strip(), args.expected_date_folder.strip()):
            if value:
                parse_date_folder(value)
        token = dropbox_access_token()
        root = args.dropbox_root.rstrip("/") or ""
        output_dir = Path(args.output_dir).resolve()
        log(f"Listing Dropbox root: {root}")
        root_entries = list_folder(token, root, recursive=False)
        diagnostics["available_date_folders"] = recent_date_folder_names(root_entries)
        log("Available Dropbox date folders (newest first): " +
            (", ".join(diagnostics["available_date_folders"]) or "<none>"))
        latest = select_date_folder(root_entries, args.date_folder)
        diagnostics["selected_date_folder"] = str(latest["name"])
        diagnostics["source_date"] = parse_date_folder(str(latest["name"])).isoformat()
        diagnostics["folder_age_days"] = (
            (parse_date_folder(args.expected_date_folder.strip()) - parse_date_folder(str(latest["name"]))).days
            if args.expected_date_folder.strip() else None
        )
        validate_expected_date_folder(latest, args.expected_date_folder, args.max_folder_age_days)
        latest_name = latest["name"]
        latest_path = latest.get("path_lower") or latest.get("path_display") or f"{root}/{latest_name}"
        selection_label = "Requested" if args.date_folder else "Latest"
        log(f"{selection_label} Dropbox date folder: {latest_path}")
        if args.expected_date_folder.strip():
            log(f"Source batch date={diagnostics['source_date']}; "
                f"reference date={args.expected_date_folder.strip()}; "
                f"age={diagnostics['folder_age_days']} day(s), allowed=0..{args.max_folder_age_days}.")

        entries = list_folder(token, latest_path, recursive=True)
        pdfs = [e for e in entries if e.get(".tag") == "file" and str(e.get("name", "")).lower().endswith(".pdf")]
        diagnostics["pdf_count"] = len(pdfs)
        if not pdfs:
            raise RuntimeError(f"No PDFs found under latest Dropbox folder: {latest_path}")

        output_dir.mkdir(parents=True, exist_ok=True)
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
            diagnostics["downloaded_pdf_count"] = len(manifest)

        if not manifest:
            raise RuntimeError(f"No PDFs were downloaded from latest Dropbox folder: {latest_path}")

        manifest_path = output_dir / "dropbox_manifest.json"
        manifest_path.write_text(json.dumps({
            "latest_folder": latest_name, "latest_path": latest_path,
            "source_date": diagnostics["source_date"],
            "expected_date_folder": args.expected_date_folder.strip(),
            "max_folder_age_days": args.max_folder_age_days,
            "folder_age_days": diagnostics["folder_age_days"],
            "pdf_count": len(manifest), "files": manifest,
        }, ensure_ascii=False, indent=2), encoding="utf-8")

        write_github_output("latest_folder", latest_name)
        write_github_output("latest_path", str(latest_path))
        write_github_output("pdf_count", str(len(manifest)))
        write_github_output("input_dir", str(output_dir))
        log(f"Downloaded {len(manifest)} PDFs from {latest_name} to {output_dir}")
        diagnostics["status"] = "downloaded"
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    finally:
        write_input_summary(diagnostics)


if __name__ == "__main__":
    raise SystemExit(main())
