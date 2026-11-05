#!/usr/bin/env python3
"""Resume chart indexing by reconciling exact GitHub child executions."""
from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time
from urllib.parse import urlencode

WORKFLOW = "portal-chart-search-index.yml"
WORKFLOW_PATH = ".github/workflows/" + WORKFLOW
SOURCE_PATH = ".github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml"
MAX_EXECUTIONS = 3
MAX_DISCOVERY_PAGES = 4
ACTIVE = {"queued", "in_progress", "waiting", "pending", "requested"}


class RecoveryError(RuntimeError):
    pass


def require(condition, message):
    if not condition:
        raise RecoveryError(message)


def request_from_environment(env):
    repository = env.get("GITHUB_REPOSITORY", "")
    require(re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository), "Invalid chart repository")
    date = env.get("DATE_FOLDER", "")
    source = env.get("SOURCE_RUN_ID", "")
    require(re.fullmatch(r"[0-9]{6,8}", date), "Invalid chart date")
    require(re.fullmatch(r"[1-9][0-9]{0,19}", source), "Invalid chart source run")
    require(not env.get("ARTIFACT_RUN_ID"), "Durable daily requests require private handoffs")
    require(env.get("SOURCE_ARTIFACT_PATTERN", "publish-ready-*") == "publish-ready-*", "Unexpected daily artifact selector")
    require(env.get("ALLOW_INDEX_REMOVAL_MIGRATION", "false") == "false", "Durable chart requests cannot remove index records")
    manifest = env.get("HANDOFF_MANIFEST_SHA256", "")
    shards, articles = env.get("EXPECTED_SHARDS", "0"), env.get("EXPECTED_ARTICLES", "0")
    if env.get("RECOVERED_RESULT") == "success":
        manifest, shards, articles = env.get("RECOVERED_MANIFEST", ""), "1", env.get("SELECTED_COUNT", "")
    maximum = env.get("MAX_IMAGES", "0")
    require(all(re.fullmatch(r"[0-9]+", value) for value in (shards, articles, maximum)), "Invalid chart limits")
    if manifest:
        require(re.fullmatch(r"[a-f0-9]{64}", manifest) and int(shards) == 1 and 0 < int(articles) <= 1000,
                "Invalid recovered chart binding")
    else:
        require(int(articles) == 0, "Unexpected chart article count")
    return {"schema": 1, "repository": repository, "workflow": WORKFLOW_PATH,
        "date_folder": date, "source_handoff_run_id": source,
        "source_handoff_manifest_sha256": manifest, "expected_shards": str(int(shards)),
        "expected_articles": str(int(articles)), "max_images": str(int(maximum)),
        "source_artifact_run_id": "", "source_artifact_pattern": "publish-ready-*",
        "allow_index_removal_migration": "false"}


def request_id(request):
    return hashlib.sha256(json.dumps(request, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def title(request):
    return "Chart request " + request_id(request)


def timestamp(value):
    try:
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
        require(result.tzinfo is not None, "Chart run timestamp has no timezone")
        return result
    except (AttributeError, TypeError, ValueError) as error:
        raise RecoveryError("Invalid chart run timestamp") from error


class GitHub:
    def __init__(self, repository, *, sleep=time.sleep):
        self.repository, self.sleep = repository, sleep

    def read(self, path):
        for attempt in range(3):
            try:
                result = subprocess.run(["gh", "api", path], capture_output=True, text=True, timeout=120)
                if result.returncode == 0:
                    return json.loads(result.stdout)
            except (subprocess.TimeoutExpired, json.JSONDecodeError):
                pass
            if attempt < 2:
                self.sleep(2 ** attempt)
        raise RecoveryError("GitHub chart inspection unavailable; source retained")

    def dispatch(self, request, retry):
        args = ["gh", "workflow", "run", WORKFLOW, "--repo", self.repository, "--ref", "main"]
        for key in ("date_folder", "source_handoff_run_id", "source_handoff_manifest_sha256",
                    "expected_shards", "expected_articles", "max_images"):
            args += ["-f", key + "=" + request[key]]
        args += ["-f", "dispatch_request_id=" + request_id(request), "-f", "retry_errors_now=" + str(retry).lower()]
        # A POST is never retried here. Its response can be lost after acceptance.
        try:
            subprocess.run(args, capture_output=True, text=True, timeout=120)
        except subprocess.TimeoutExpired:
            return
        # Even a successful response is reconciled through the authenticated run
        # inventory; stdout format and unknown HTTP outcomes cannot cause a POST retry.

    def watch(self, run_id, seconds):
        try:
            subprocess.run(["gh", "run", "watch", str(run_id), "--repo", self.repository,
                "--compact", "--exit-status", "--interval", "30"], stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL, timeout=seconds)
        except subprocess.TimeoutExpired:
            pass

    def summary(self, run_id, date):
        for attempt in range(3):
            # A failed extraction may leave a partial download; each read retry
            # gets a clean destination and cannot accidentally reuse it.
            with tempfile.TemporaryDirectory(prefix="chart-summary-") as directory:
                try:
                    result = subprocess.run(["gh", "run", "download", str(run_id), "--repo", self.repository,
                        "--name", f"chart-search-summary-{date}-{run_id}", "--dir", directory],
                        capture_output=True, text=True, timeout=120)
                    if result.returncode == 0:
                        return json.loads((Path(directory) / "summary.json").read_bytes())
                except (subprocess.TimeoutExpired, OSError, json.JSONDecodeError):
                    pass
            if attempt < 2:
                self.sleep(2 ** attempt)
        raise RecoveryError("Exact chart child summary unavailable; source retained")


def validate_run(row, request):
    repository = request["repository"]
    require(isinstance(row, dict) and type(row.get("id")) is int and row["id"] > 0
        and row.get("display_title") == title(request) and row.get("path") == WORKFLOW_PATH
        and row.get("head_branch") == "main" and row.get("event") == "workflow_dispatch"
        and re.fullmatch(r"[a-f0-9]{40}", str(row.get("head_sha", "")))
        and all((row.get(key) or {}).get("full_name") == repository for key in ("repository", "head_repository"))
        and (row.get("repository") or {}).get("private") is False
        and row.get("status") in ACTIVE | {"completed"}, "Chart request run identity mismatch")
    return row


def discover(github, request, created):
    found, seen = [], set()
    source_time = timestamp(created)
    for page in range(1, MAX_DISCOVERY_PAGES + 1):
        query = urlencode({"event": "workflow_dispatch", "branch": "main", "per_page": 100, "page": page})
        result = github.read(f"repos/{request['repository']}/actions/workflows/{WORKFLOW}/runs?{query}")
        rows = result.get("workflow_runs") if isinstance(result, dict) else None
        require(isinstance(rows, list) and type(result.get("total_count")) is int
            and result["total_count"] >= 0, "Incomplete chart workflow inventory")
        before_source = False
        for row in rows:
            require(isinstance(row, dict) and type(row.get("id")) is int and row["id"] not in seen, "Repeated chart workflow inventory")
            seen.add(row["id"])
            if timestamp(row.get("created_at")) < source_time:
                before_source = True
                continue
            if row.get("display_title") == title(request):
                found.append(validate_run(row, request))
        if before_source or len(seen) >= result["total_count"]:
            return sorted(found, key=lambda row: row["id"])
        require(len(rows) == 100, "Truncated chart workflow inventory")
    raise RecoveryError("Chart discovery bound reached; source retained")


def stable_only(summary):
    require(isinstance(summary, dict), "Invalid chart summary")
    values = [summary.get(key) for key in ("workflow_unprocessed_count", "workflow_retryable_count", "workflow_stable_error_count")]
    return (all(type(value) is int and value >= 0 for value in values)
        and values[0] == values[1] == 0 and values[2] > 0 and summary.get("request_limit_reached") is False)


def recover(request, github, *, sleep=time.sleep, clock=time.monotonic):
    source = github.read(f"repos/{request['repository']}/actions/runs/{request['source_handoff_run_id']}")
    require(source.get("id") == int(request["source_handoff_run_id"]) and source.get("path") == SOURCE_PATH
        and source.get("head_branch") == "main"
        and (source.get("repository") or {}).get("full_name") == request["repository"], "Chart source run identity mismatch")
    created, deadline = source.get("created_at"), clock() + 20700
    dispatched = False
    while True:
        require(clock() < deadline, "Chart parent wait budget exhausted; source retained")
        runs = discover(github, request, created)
        active = [row for row in runs if row["status"] in ACTIVE]
        require(len(active) <= 1, "Multiple active exact chart children; source retained")
        if active:
            selected = active[0]
        else:
            successes = [row for row in runs if row.get("conclusion") == "success"]
            if successes:
                selected = successes[-1]
                print(f"chart_dispatch complete child={selected['id']} request={request_id(request)} reused=true", flush=True)
                return selected["id"]
            require(len(runs) < MAX_EXECUTIONS, "Three exact chart executions exhausted; source retained")
            retry = bool(runs)
            if runs:
                selected = runs[-1]
                require(selected.get("conclusion") == "failure"
                    and stable_only(github.summary(selected["id"], request["date_folder"])),
                    "Chart child is not a confirmed stable-image-only failure; source retained")
            previous = {row["id"] for row in runs}
            github.dispatch(request, retry)
            # Reconcile an accepted or unknown POST before considering any later
            # mutation. An absent child stops this invocation; the next parent
            # rerun performs the same exact lookup before it can POST.
            for lookup in range(3):
                runs = discover(github, request, created)
                added = [row for row in runs if row["id"] not in previous]
                require(len(added) <= 1, "Ambiguous chart dispatch outcome; source retained")
                if added:
                    selected = added[0]
                    break
                if lookup < 2:
                    sleep(2 ** (lookup + 1))
            else:
                raise RecoveryError(f"Chart dispatch outcome unknown request={request_id(request)} source={request['source_handoff_run_id']}; no duplicate dispatch attempted")
            dispatched = True
        print(f"chart_dispatch attached child={selected['id']} request={request_id(request)}", flush=True)
        for watch_attempt in range(3):
            if selected["status"] == "completed":
                break
            github.watch(selected["id"], max(1, min(18000, int(deadline - clock()))))
            # gh watch can fail after the child succeeds, or lose its transport
            # while the child is still active. Only the independent run decides.
            selected = validate_run(github.read(f"repos/{request['repository']}/actions/runs/{selected['id']}"), request)
        require(selected["status"] == "completed", "Chart watch unavailable; exact active child retained")
        if selected.get("conclusion") == "success":
            print(f"chart_dispatch complete child={selected['id']} request={request_id(request)} reused={str(not dispatched).lower()}", flush=True)
            return selected["id"]
        # Re-read the complete inventory before another dispatch, preserving
        # the three-execution budget across all parent attempts and reruns.


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validate-request", action="store_true")
    args = parser.parse_args()
    request = request_from_environment(os.environ)
    if args.validate_request:
        require(os.environ.get("DISPATCH_REQUEST_ID") == request_id(request), "Chart dispatch request digest mismatch")
    else:
        recover(request, GitHub(request["repository"]))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RecoveryError as error:
        raise SystemExit(str(error)) from None
