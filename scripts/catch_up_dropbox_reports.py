#!/usr/bin/env python3
"""Compare Dropbox metadata with live reports; request one incremental catch-up.

No PDF bodies, R2 uploads, translations, or source writes occur here. A missing
calendar-day folder is normal: batch dates need not equal the upload date.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
from urllib.parse import urlsplit

import requests

from build_bank_report_catalog import dropbox_access_token, list_folder
from download_dropbox_latest_pdfs import dated_folders
from portal_suite_catalog import report_id_for_entry
from recover_neutral_runner_loss import GitHub

WORKFLOW = "neutral-edge-cutover.yml"
EVENT = "portal-dropbox-report-refresh"
ACTIVE = ("in_progress", "queued", "pending", "waiting", "requested")


def source_reports(token, root="/zip_backup", *, reader=list_folder):
    folders = dated_folders(reader(token, root, recursive=False))[:3]
    rows = set()
    for _, folder in folders:
        path = folder.get("path_display") or folder.get("path_lower") or root + "/" + folder["name"]
        for entry in reader(token, path, recursive=True):
            if (entry.get(".tag") == "file" and str(entry.get("name", "")).lower().endswith(".pdf")
                    and (entry.get("path_display") or entry.get("path_lower"))):
                rows.add((report_id_for_entry(entry), str(folder["name"])))
    return rows


def missing_reports(source, catalog):
    items = catalog.get("items")
    if not isinstance(items, list) or not items:
        raise ValueError("invalid_live_catalog")
    published = set()
    for item in items:
        if not isinstance(item, dict) or not re.fullmatch(r"[a-f0-9]{24}", str(item.get("id", ""))):
            raise ValueError("invalid_live_report")
        dates = set(item.get("date_folders") or []) | {item.get("date_folder")}
        published.update((item["id"], str(day)) for day in dates if day)
    return source - published


def generation_for(missing):
    return hashlib.sha256(json.dumps(sorted(missing), separators=(",", ":")).encode()).hexdigest()


def workflow_runs(github, *, status=None):
    query = "branch=main&per_page=100" + ("&status=" + status if status else "")
    payload = github.api(f"actions/workflows/{WORKFLOW}/runs?{query}")
    rows = payload.get("workflow_runs")
    if not isinstance(rows, list) or not isinstance(payload.get("total_count"), int):
        raise ValueError("invalid_run_inventory")
    if status and payload["total_count"] > len(rows):
        raise ValueError("incomplete_active_inventory")
    return [row for row in rows if row.get("head_branch") == "main"]


def active_refresh(github):
    # Status-specific queries also find a long-running release even when many
    # newer workflow_run events have replaced its pending successor.
    return any(workflow_runs(github, status=status) for status in ACTIVE)


def dispatch_once(github, generation):
    payload = {"event_type": EVENT, "client_payload": {"source_generation": generation}}
    # No mutation retry: a transport timeout may follow an accepted request.
    result = subprocess.run(
        ["gh", "api", f"repos/{github.repository}/dispatches", "--method", "POST", "--input", "-"],
        input=json.dumps(payload), capture_output=True, text=True, timeout=35, check=False,
    )
    return result.returncode == 0


def catch_up(github, *, read_source, read_catalog, dispatch=dispatch_once):
    if active_refresh(github):
        return {"state": "refresh_active"}
    source = read_source()
    if not source:
        return {"state": "source_not_ready"}
    missing = missing_reports(source, read_catalog())
    if not missing:
        return {"state": "up_to_date", "source_reports": len(source)}
    generation = generation_for(missing)
    title = f"Neutral edge Dropbox refresh ({generation})"
    if any(run.get("display_title") == title and run.get("conclusion") != "cancelled"
           for run in workflow_runs(github)):
        # The same missing set gets at most one automatic request. A program
        # failure is investigated, rather than retried every hour indefinitely.
        return {"state": "already_requested", "missing_reports": len(missing)}
    # GitHub can replace an unstarted pending run with a different production
    # release. That cancelled queue entry must not consume this source batch.
    if active_refresh(github):
        return {"state": "refresh_active"}
    accepted = dispatch(github, generation)
    return {"state": "requested" if accepted else "dispatch_unconfirmed", "missing_reports": len(missing)}


def read_live_catalog(origin):
    parsed = urlsplit(origin)
    if (parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password
            or parsed.port or parsed.path not in ("", "/") or parsed.query or parsed.fragment):
        raise ValueError("invalid_site_origin")
    response = requests.get(origin.rstrip("/") + "/data/catalog.json", timeout=(10, 60),
                            headers={"Cache-Control": "no-cache", "User-Agent": "portal-source-catchup"})
    response.raise_for_status()
    if len(response.content) > 64 * 1024 * 1024:
        raise ValueError("catalog_oversized")
    return response.json()


def main():
    try:
        github = GitHub(os.environ["GITHUB_REPOSITORY"])
        result = catch_up(github, read_source=lambda: source_reports(dropbox_access_token()),
                          read_catalog=lambda: read_live_catalog(os.environ["PORTAL_SITE_URL"]))
    except Exception:
        # Source/API delays are deferred; they never turn the production
        # refresh red or expose credentials, paths, filenames or provider text.
        result = {"state": "deferred"}
    print(json.dumps(result, sort_keys=True))
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as output:
            output.write("Dropbox report catch-up: `" + result["state"] + "`\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
