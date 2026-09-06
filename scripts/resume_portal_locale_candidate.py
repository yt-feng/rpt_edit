#!/usr/bin/env python3
"""Restore an already uploaded inactive locale candidate without remote writes."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import gzip
import hashlib
import io
import json
import os
from pathlib import Path
import re
import sys
from typing import Any, Callable
from urllib.error import HTTPError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener
import zipfile

import publish_static_slot as publisher
from edge_route_cutover import request_status
import verify_portal_chinese_parity as parity
from verify_prepared_static_slot import static_tree_sha256


LOCALES = ("ko", "ja", "ar")
WORKFLOW_PATH = ".github/workflows/neutral-edge-cutover.yml"
AUDIT_STEP = "Verify isolated multilingual shadow worker"
REQUIRED_STEPS = (
    "Validate complete static release",
    "Verify protected Chinese release after locale build",
    "Upload inactive static slot and immutable runtime",
)
DIAGNOSTICS = (
    "locale-preflight-diagnostics.json", "locale-full-diagnostics.json",
    "chinese-parity.json", "chinese-performance.json",
)
PUBLIC_PATHS = frozenset((
    "index.html", "feed.xml", "assets/app.js", "assets/styles.css", "assets/locale.css",
    "assets/locale-runtime.js", "data/catalog.json", "data/catalog_preview.json",
    "data/release-semantics.json", "data/i18n/manifest.json", "sitemap-baidu.xml",
    *(f"sitemap-{locale}.xml" for locale in LOCALES),
))
SHA40 = re.compile(r"[0-9a-f]{40}\Z")
MAX_API_BYTES = 64 * 1024 * 1024


class ResumeError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ResumeError(message)


def decode_json(data: bytes, label: str) -> dict[str, Any]:
    try:
        payload = json.loads(data)
    except (UnicodeDecodeError, ValueError) as error:
        raise ResumeError(f"{label} is invalid JSON") from error
    require(isinstance(payload, dict), f"{label} must be an object")
    return payload


class GitHubRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, newurl):
        require(urlsplit(newurl).scheme == "https", "GitHub download redirected outside HTTPS")
        redirected = super().redirect_request(request, fp, code, msg, headers, newurl)
        if redirected and urlsplit(request.full_url).netloc != urlsplit(newurl).netloc:
            redirected.remove_header("Authorization")
        return redirected


def phase(name: str) -> None:
    print(f"Locale resume phase={name}", flush=True)


class GitHubClient:
    def __init__(self, token: str):
        require(bool(token), "GH_TOKEN is required")
        self.token = token
        self.opener = build_opener(GitHubRedirect())

    def bytes(self, path: str) -> bytes:
        require(path.startswith("/repos/"), "Unexpected GitHub API route")
        request = Request("https://api.github.com" + path, headers={
            "Authorization": "Bearer " + self.token,
            "Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "Portal-Locale-Resume/1.0",
        })
        try:
            with self.opener.open(request, timeout=60) as response:
                body = response.read(MAX_API_BYTES + 1)
        except HTTPError as error:
            # Report the requested API route, never a redirected signed URL or
            # response headers. GitHub's bounded JSON message explains token
            # permission failures that would otherwise appear as bare HTTP 403.
            message = ""
            try:
                payload = json.loads(error.read(8192))
                value = payload.get("message") if isinstance(payload, dict) else None
                if isinstance(value, str):
                    value = value.replace(self.token, "[redacted]")
                    value = re.sub(r"https?://[^\s<>\"']+", "[URL omitted]", value)
                    value = re.sub(r"\b(?:gh[pousr]_[A-Za-z0-9_]+|github_pat_[A-Za-z0-9_]+)", "[redacted]", value)
                    message = " message=" + " ".join(value.split())[:500]
            except (OSError, UnicodeDecodeError, ValueError):
                pass
            finally:
                error.close()
            raise ResumeError(f"GitHub API request failed: route={urlsplit(path).path} status={error.code}{message}") from None
        require(len(body) <= MAX_API_BYTES, "GitHub response is oversized")
        return body

    def json(self, path: str) -> dict[str, Any]:
        return decode_json(self.bytes(path), "GitHub response")


def live_state(origin: str) -> dict[str, Any]:
    parsed = urlsplit(origin)
    require(parsed.scheme == "https" and bool(parsed.netloc) and not parsed.username
            and not parsed.password and parsed.path in {"", "/"} and not parsed.query
            and not parsed.fragment, "LIVE_ORIGIN must be a bare HTTPS origin")
    status, headers, body = request_status(
        origin.rstrip("/") + "/.well-known/edge-state", method="GET", headers={"Cache-Control": "no-cache"},
    )
    require(status == 200, f"Live identity request failed: route=/.well-known/edge-state status={status}")
    # request_status reads at most 64 KiB. Reject a full buffer because it may
    # have been truncated; the Edge identity document is only a few hundred bytes.
    require(len(body) < 65536, "Live identity response is oversized or truncated")
    content_length = headers.get("content-length")
    require(content_length is None or (content_length.isdigit() and int(content_length) <= 65536),
            "Live identity response content length is invalid or oversized")
    return decode_json(body, "Live identity")


def paged_rows(github: Any, path: str, field: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for page in range(1, 101):
        payload = github.json(f"{path}?per_page=100&page={page}")
        batch = payload.get(field)
        require(isinstance(batch, list) and all(isinstance(row, dict) for row in batch), f"GitHub {field} list is invalid")
        rows.extend(batch)
        if len(batch) < 100:
            return rows
    raise ResumeError(f"GitHub {field} pagination exceeded its bound")


def verify_source_run(github: Any, repository: str, run_id: int, attempt: int, commit: str) -> tuple[dict[str, Any], str, str]:
    require(bool(re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository)), "GITHUB_REPOSITORY is invalid")
    require(run_id > 0 and attempt > 0, "Source run and attempt must be positive")
    require(bool(SHA40.fullmatch(commit)), "Candidate commit must be a full lowercase SHA")
    base = f"/repos/{repository}/actions/runs/{run_id}"
    phase("source_attempt")
    run = github.json(f"{base}/attempts/{attempt}")
    require(run.get("id") == run_id and run.get("run_attempt") == attempt, "Source run attempt does not match")
    require(run.get("status") == "completed" and run.get("conclusion") == "failure", "Source attempt must be a completed failed run")
    require(run.get("path") == WORKFLOW_PATH and run.get("head_branch") == "main", "Source must be the main neutral-edge-cutover workflow")
    require((run.get("repository") or {}).get("full_name") == repository
            and (run.get("head_repository") or {}).get("full_name") == repository,
            "Source run must belong to this repository, including its head repository")
    require(run.get("head_sha") == commit, "Candidate commit does not match the source run")
    phase("source_jobs")
    jobs = paged_rows(github, f"{base}/attempts/{attempt}/jobs", "jobs")
    selected = [job for job in jobs if job.get("name") == "prepare_release"]
    require(len(selected) == 1, "Source must have one prepare_release job")
    job = selected[0]
    require(job.get("status") == "completed" and job.get("conclusion") == "failure", "Source preparation must have failed after upload")
    require(all(other is job or other.get("conclusion") in {"skipped", "success"} for other in jobs), "Another source job failed")
    require(not any(other is not job and other.get("conclusion") == "success" and "cutover" in str(other.get("name", "")) for other in jobs), "Source run already completed a cutover")
    steps = job.get("steps")
    require(isinstance(steps, list), "Source job has no step evidence")
    by_name = {step.get("name"): step for step in steps}
    audit = by_name.get(AUDIT_STEP, {})
    require(audit.get("conclusion") == "failure", "Source did not fail at the shadow HTTP audit")
    audit_number = audit.get("number")
    require(isinstance(audit_number, int), "Source audit step number is invalid")
    for name in REQUIRED_STEPS:
        step = by_name.get(name, {})
        require(step.get("conclusion") == "success" and isinstance(step.get("number"), int)
                and step["number"] < audit_number, f"Source prerequisite did not succeed: {name}")
    require(all(step.get("conclusion") not in {"failure", "cancelled", "timed_out"}
                or int(step.get("number", 0)) >= audit_number for step in steps),
            "Source failed before shadow audit")
    phase("source_logs")
    logs = github.bytes(f"/repos/{repository}/actions/jobs/{int(job['id'])}/logs").decode("utf-8")
    upload_started = by_name[REQUIRED_STEPS[2]].get("started_at", "")
    require(bool(re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d+)?Z", upload_started)), "Source upload step has no trusted timestamp")
    identity_logs = "\n".join(line for line in logs.splitlines()
                              if re.match(r"\d{4}-\d\d-\d\dT", line) and line[:19] >= upload_started[:19])
    # Remove only runner decoration; source commands containing shell variables
    # cannot satisfy the literal identity assignments below.
    logs = re.sub(r"\x1b\[[0-9;]*m", "", logs)
    logs = re.sub(r"(?m)^\d{4}-\d\d-\d\dT[^ ]+ +", "", logs)
    return run, logs, identity_logs


def log_values(logs: str, names: tuple[str, ...], pattern: str) -> set[str]:
    names_pattern = "|".join(re.escape(name) for name in names)
    return set(re.findall(rf"(?m)(?<![A-Za-z0-9_])(?:{names_pattern})\s*[:=]\s*[\"']?({pattern})(?=[\"'\s]|$)", logs))


def verify_logged_identity(logs: str, *, slot: str, release: str, tree: str, commit: str, previous: dict[str, Any]) -> None:
    require(log_values(logs, ("NEUTRAL_OPERATION",), "[a-z][a-z-]*") == {"migrate"},
            "Only a prepared migrate candidate can be resumed")
    for label, names, pattern, expected in (
        ("slot", ("static_slot", "SHADOW_STATIC_SLOT"), "[ab]", slot),
        ("release", ("STATIC_RELEASE", "release_id"), "[0-9a-f]{32}", release),
        ("tree", ("STATIC_TREE_SHA256", "SHADOW_STATIC_TREE", "CANDIDATE_STATIC_TREE"), "[0-9a-f]{64}", tree),
        ("commit", ("CANDIDATE_COMMIT_SHA",), "[0-9a-f]{40}", commit),
        ("previous slot", ("previous_slot", "ACTIVE_STATIC_SLOT"), "[ab]", previous["slot"]),
        ("previous release", ("PREVIOUS_STATIC_RELEASE", "previous_release"), "[0-9a-f]{32}", previous["release_id"]),
    ):
        require(log_values(logs, names, pattern) == {expected}, f"Source log {label} identity is missing or inconsistent")
    previous_trees = log_values(logs, ("PREVIOUS_STATIC_TREE", "previous_tree"), "[0-9a-f]{64}")
    require(not previous_trees or previous_trees == {previous["tree_sha256"]}, "Source log previous tree does not match")


def download_diagnostics(github: Any, repository: str, run_id: int, attempt: int, destination: Path) -> None:
    name = f"neutral-translation-diagnostics-{run_id}-{attempt}"
    phase("diagnostic_artifact_metadata")
    artifacts = paged_rows(github, f"/repos/{repository}/actions/runs/{run_id}/artifacts", "artifacts")
    matches = [artifact for artifact in artifacts if artifact.get("name") == name and not artifact.get("expired")]
    require(len(matches) == 1, "Source diagnostics artifact is missing, expired, or ambiguous")
    artifact = matches[0]
    workflow_run = artifact.get("workflow_run") or {}
    require(not workflow_run or workflow_run.get("id") == run_id, "Diagnostics artifact belongs to another run")
    phase("diagnostic_artifact_download")
    data = github.bytes(f"/repos/{repository}/actions/artifacts/{int(artifact['id'])}/zip")
    required: dict[str, bytes] = {}
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            for item in archive.infolist():
                publisher.safe_relative_path(item.filename.rstrip("/"))
                require(not ((item.external_attr >> 16) & 0o170000) == 0o120000, "Diagnostic archive contains a symbolic link")
                if item.is_dir():
                    continue
                name = Path(item.filename).name
                if name not in DIAGNOSTICS:
                    continue
                require(name not in required and 0 < item.file_size <= 16 * 1024 * 1024, "Diagnostic archive entry is duplicate or oversized")
                required[name] = archive.read(item)
    except (zipfile.BadZipFile, ValueError) as error:
        raise ResumeError("Source diagnostics archive is invalid") from error
    require(set(required) == set(DIAGNOSTICS), "Source diagnostics artifact is incomplete")
    for name, body in required.items():
        write_local(destination, name, body)


def write_local(root: Path, relative: str, body: bytes) -> None:
    relative = publisher.safe_relative_path(relative)
    root = root.resolve()
    target = root / relative
    require(target.resolve().is_relative_to(root) and not target.is_symlink(), "Local output contains a symbolic or escaping path")
    current = target.parent
    while current != root:
        require(not current.is_symlink(), "Local output parent is a symbolic link")
        current = current.parent
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(body)


def assert_no_incomplete(client: Any, bucket: str, slot: str) -> None:
    try:
        client.head_object(Bucket=bucket, Key=publisher.incomplete_key(slot))
    except Exception as error:
        if publisher.upload_error_code(error) in {"404", "nosuchkey", "notfound"} or isinstance(error, KeyError):
            return
        raise
    raise ResumeError("Candidate slot has an incomplete marker")


def validate_remote_slot(client: Any, bucket: str, slot: str, release: str, tree: str, *, workers: int = 16) -> dict[str, Any]:
    assert_no_incomplete(client, bucket, slot)
    manifest = publisher.valid_manifest(publisher.read_json_object(client, bucket, publisher.manifest_key(slot)), slot)
    require(manifest is not None and manifest["release_id"] == release and manifest["tree_sha256"] == tree, "Candidate slot manifest identity does not match")
    files = manifest["files"]
    require(bool(files) and static_tree_sha256(files) == tree, "Candidate manifest tree digest does not match its descriptors")
    require(manifest.get("total_bytes") == sum(int(row["size"]) for row in files.values()), "Candidate manifest byte count does not match")
    prefix = publisher.slot_prefix(slot)
    listed = publisher.list_objects(client, bucket, prefix)
    require(listed == {prefix + relative: int(row["size"]) for relative, row in files.items()}, "Candidate object tree differs from its committed manifest")
    progress = publisher._PublishProgress("resume_verify_metadata", objects=len(files), workers=workers)
    with ThreadPoolExecutor(max_workers=workers) as pool:
        checks = {pool.submit(publisher.remote_object_matches_descriptor, client, bucket, prefix + relative, descriptor): relative
                  for relative, descriptor in files.items()}
        for count, future in enumerate(as_completed(checks), 1):
            require(future.result(), f"Candidate object metadata does not match: {checks[future]}")
            progress.update(count)
    progress.finish(verified=len(files))
    runtime = publisher.valid_runtime_manifest(publisher.read_json_object(client, bucket, publisher.runtime_manifest_key(release)), release)
    require(runtime is not None, "Candidate immutable runtime manifest is invalid")
    reference = {key: runtime[key] for key in ("schema_version", "release_id", "prefix", "tree_sha256")}
    require(manifest.get("runtime_data") == reference, "Candidate runtime reference differs from its immutable manifest")
    require(set(runtime["files"]) == {Path(path).name for path in publisher.DEFAULT_RUNTIME_PATHS},
            "Candidate immutable runtime file inventory is unexpected")
    for path in publisher.DEFAULT_RUNTIME_PATHS:
        require(all(runtime["files"][Path(path).name][field] == (files.get(path) or {}).get(field) for field in ("sha256", "size")),
                "Candidate immutable runtime content differs from the static candidate")
    for filename, descriptor in runtime["files"].items():
        metadata = client.head_object(Bucket=bucket, Key=runtime["prefix"] + filename)
        require(publisher.runtime_object_matches(metadata, descriptor, release), "Candidate immutable runtime object does not match")
    return manifest


def download_candidate_files(client: Any, bucket: str, manifest: dict[str, Any], site_dir: Path, *, workers: int = 16) -> set[str]:
    files = manifest["files"]
    prefix = publisher.slot_prefix(manifest["slot"])
    downloaded: set[str] = set()
    def fetch_one(relative: str) -> str:
        require(relative in files, f"Candidate audit file is absent from manifest: {relative}")
        descriptor = files[relative]
        body = publisher.body_bytes(client.get_object(Bucket=bucket, Key=prefix + relative)["Body"])
        require(len(body) == descriptor["size"] and hashlib.sha256(body).hexdigest() == descriptor["sha256"],
                f"Candidate downloaded file differs from manifest: {relative}")
        write_local(site_dir, relative, body)
        return relative
    downloaded.add(fetch_one("data/i18n/manifest.json"))
    locale_manifest = decode_json((site_dir / "data/i18n/manifest.json").read_bytes(), "Locale manifest")
    require(locale_manifest.get("quality_gate_version") == 3 and set(locale_manifest.get("locales", [])) == set(LOCALES)
            and all((locale_manifest.get("coverage") or {}).get(locale) == 1 for locale in LOCALES), "Candidate locale coverage is incomplete")
    require(locale_manifest.get("translation_scope") == "incremental" and
            (locale_manifest.get("index_policy") or {}).get("mode") == "incremental-publication-cutoff",
            "Candidate is not an incremental locale release")
    wanted = set(PUBLIC_PATHS)
    paths = locale_manifest.get("required_paths")
    require(isinstance(paths, list) and all(isinstance(path, str) for path in paths), "Locale required paths are invalid")
    wanted.update(publisher.safe_relative_path(path) for path in paths)
    expected_count = locale_manifest.get("html_page_count")
    require(isinstance(expected_count, int) and expected_count > 0, "Locale HTML count is invalid")
    for locale in LOCALES:
        locale_pages = {relative for relative in files if relative.startswith(locale + "/") and relative.endswith(".html")}
        require(len(locale_pages) == expected_count, f"Locale HTML inventory differs from manifest: {locale}")
        wanted.update(locale_pages)
        wanted.update(relative[len(locale) + 1:] for relative in locale_pages)
    require(wanted.issubset(files), "Candidate is missing an audit or public artifact file")
    with ThreadPoolExecutor(max_workers=workers) as pool:
        downloaded.update(pool.map(fetch_one, sorted(wanted - downloaded)))
    return downloaded


def validate_diagnostics(directory: Path, site_dir: Path, logs: str, origin: str) -> dict[str, Any]:
    values = {name: decode_json((directory / name).read_bytes(), name) for name in DIAGNOSTICS}
    preflight = values["locale-preflight-diagnostics.json"]
    full = values["locale-full-diagnostics.json"]
    require(preflight.get("status") == "passed" and preflight.get("preflight_only") is True, "Source locale preflight did not pass")
    require(full.get("status") == "passed" and full.get("ready") is True and not full.get("preflight_only")
            and not full.get("stop_reason") and full.get("pending_repair_count", 0) == 0, "Source locale build is not ready")
    report = values["chinese-parity.json"]
    require(report.get("schema_version") == 1 and report.get("kind") == parity.VERIFY_KIND
            and report.get("site_origin") == origin.rstrip("/"), "Source Chinese parity identity is invalid")
    parity._verify_digest(report, label="Source Chinese parity report")
    require(bool(publisher.SHA256_PATTERN.fullmatch(str(report.get("snapshot_digest", ""))))
            and bool(publisher.SHA256_PATTERN.fullmatch(str(report.get("verified_tree_digest", "")))), "Source Chinese parity digests are invalid")
    require(report["digest"] in logs and report["verified_tree_digest"] in logs, "Source log does not attest the downloaded parity report")
    performance = values["chinese-performance.json"]
    app = (site_dir / "assets/app.js").read_bytes()
    gzipped = gzip.compress(app, compresslevel=9, mtime=0)
    require(performance.get("schema_version") == 1 and performance.get("candidate_bytes") == len(app)
            and performance.get("candidate_gzip_bytes") == len(gzipped)
            and performance.get("candidate_sha256") == hashlib.sha256(app).hexdigest(), "Chinese performance report does not match uploaded app")
    require(len(app) <= 700_000 and len(gzipped) <= 150_000, "Chinese app exceeds its loading budget")
    require(performance.get("active_compared") is True and performance.get("raw_delta_bytes", 25000) <= 24000
            and performance.get("gzip_delta_bytes", 7000) <= 6000, "Chinese performance comparison did not pass")
    require(performance["candidate_sha256"] in logs, "Source log does not attest Chinese performance")
    return {"chinese_parity_sha256": hashlib.sha256((directory / "chinese-parity.json").read_bytes()).hexdigest(),
            "preflight_passed": True, "locale_ready": True, "performance_passed": True}


def resume_candidate(*, github: Any, client: Any, bucket: str, repository: str, run_id: int, run_attempt: int,
                     site_dir: Path, diagnostics_dir: Path, work_dir: Path, origin: str,
                     expected_slot: str, expected_release: str, expected_tree: str, expected_commit: str,
                     expected_previous_release: str, expected_previous_tree: str,
                     fetch_live: Callable[[str], dict[str, Any]] = live_state, workers: int = 16) -> dict[str, Any]:
    require(1 <= workers <= 32, "Resume metadata workers must be between 1 and 32")
    slot, release = publisher.validate_slot(expected_slot), publisher.validate_release(expected_release)
    require(bool(publisher.SHA256_PATTERN.fullmatch(expected_tree)), "Candidate tree is invalid")
    require(not site_dir.is_symlink() and (not site_dir.exists() or not any(site_dir.iterdir())), "Resume site directory must be empty")
    previous = decode_json((work_dir / "previous-edge-state.json").read_bytes(), "Captured previous Edge state")
    require(previous.get("schema_version") == 1 and previous.get("slot") in publisher.SLOTS
            and previous.get("release_id") == publisher.validate_release(expected_previous_release)
            and previous.get("tree_sha256") == expected_previous_tree
            and bool(publisher.SHA256_PATTERN.fullmatch(expected_previous_tree)), "Current captured state differs from the expected previous identity")
    require(slot != previous["slot"], "Cannot resume the active slot")
    run, logs, identity_logs = verify_source_run(github, repository, run_id, run_attempt, expected_commit)
    verify_logged_identity(identity_logs, slot=slot, release=release, tree=expected_tree, commit=expected_commit, previous=previous)
    phase("live_baseline")
    require(fetch_live(origin) == previous, "Live Edge state changed since baseline capture")
    phase("remote_slot_verification")
    manifest = validate_remote_slot(client, bucket, slot, release, expected_tree, workers=workers)
    download_diagnostics(github, repository, run_id, run_attempt, diagnostics_dir)
    phase("candidate_file_download")
    downloaded = download_candidate_files(client, bucket, manifest, site_dir, workers=workers)
    phase("diagnostic_validation")
    diagnostics = validate_diagnostics(diagnostics_dir, site_dir, logs, origin)
    phase("final_identity_recheck")
    require(fetch_live(origin) == previous, "Live Edge state changed during candidate restore")
    assert_no_incomplete(client, bucket, slot)
    final_manifest = publisher.valid_manifest(publisher.read_json_object(client, bucket, publisher.manifest_key(slot)), slot)
    require(final_manifest == manifest, "Candidate slot manifest changed during restore")
    for name in DIAGNOSTICS:
        write_local(work_dir, name, (diagnostics_dir / name).read_bytes())
    result = {
        "schema_version": 1, "source_run_id": run_id, "source_run_attempt": run_attempt,
        "source_workflow": WORKFLOW_PATH, "repository": repository,
        "commit_sha": run["head_sha"], "static_release": release, "static_slot": slot,
        "static_prefix": publisher.slot_prefix(slot), "tree_sha256": expected_tree,
        "previous_slot": previous["slot"], "previous_release": previous["release_id"], "previous_tree": previous["tree_sha256"],
        "verified_remote_objects": manifest["file_count"], "downloaded_objects": len(downloaded),
        "remote_mutations": 0, **diagnostics,
    }
    write_local(work_dir, "locale-resume-identity.json", publisher.json_bytes(result))
    phase("complete")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-id", type=int, required=True)
    parser.add_argument("--run-attempt", type=int, default=1)
    parser.add_argument("--site-dir", type=Path, default=Path("_neutral_site"))
    parser.add_argument("--diagnostics-dir", type=Path, required=True)
    parser.add_argument("--work-dir", type=Path, required=True)
    for field in ("slot", "release", "tree", "commit", "previous-release", "previous-tree"):
        parser.add_argument("--expected-" + field, required=True)
    parser.add_argument("--workers", type=int, default=16)
    args = parser.parse_args()
    try:
        phase("initialize_clients")
        github = GitHubClient(publisher.require_env("GH_TOKEN"))
        client, _transfer = publisher.build_r2_client()
        result = resume_candidate(
            github=github, client=client, bucket=publisher.require_env("R2_BUCKET"),
            repository=publisher.require_env("GITHUB_REPOSITORY"), origin=publisher.require_env("LIVE_ORIGIN"),
            **vars(args),
        )
        outputs = {key: result[key] for key in ("static_slot", "static_prefix", "tree_sha256", "static_release", "commit_sha", "chinese_parity_sha256")}
        publisher.append_github_values(os.getenv("GITHUB_OUTPUT", ""), outputs)
        publisher.append_github_values(os.getenv("GITHUB_ENV", ""), {
            "STATIC_SLOT": result["static_slot"], "STATIC_PREFIX": result["static_prefix"],
            "STATIC_RELEASE": result["static_release"], "STATIC_TREE_SHA256": result["tree_sha256"],
        })
        print(f"Prepared candidate restored: objects_verified={result['verified_remote_objects']} objects_downloaded={result['downloaded_objects']} remote_mutations=0")
        return 0
    except Exception as error:
        print(f"Locale candidate resume failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
