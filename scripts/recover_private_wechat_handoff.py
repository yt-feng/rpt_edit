#!/usr/bin/env python3
"""Validate a blocked producer and resume its private WeChat handoff without regeneration."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import runpy
import tempfile
from datetime import datetime
from pathlib import Path
from urllib.request import urlopen

from private_workflow_handoff import build_r2_client, download_directory, r2_bucket, upload_directory
from wechat_attempt_history import GitHubHistory, never_submitted

SOURCES = {
    "institution": ("institutions", ".github/workflows/institution-latest-pdf-to-wechat.yml"),
    "consulting": ("consulting", ".github/workflows/consulting-latest-pdf-to-wechat.yml"),
}


def fetch_source_metadata(repository: str, run_id: str, token: str) -> tuple[dict, dict]:
    reader = GitHubHistory(repository, run_id, token, request=urlopen)
    run = reader.get()
    attempt = run.get('run_attempt')
    if type(attempt) is not int or not 1 <= attempt <= 100:
        raise ValueError('Source attempt history is unknown or exceeds the bounded audit')
    history = [{'attempt': number, 'jobs': reader.jobs(number)} for number in range(1, attempt + 1)]
    return run, {'jobs': history[-1]['jobs'], 'attempts': history}


def coordinates(source: str, run_id: str, date: str) -> tuple[str, str]:
    if source not in SOURCES or not re.fullmatch(r"[1-9][0-9]*", run_id):
        raise ValueError("Choose a supported source and a numeric source run ID")
    if not re.fullmatch(r"[0-9]{6}", date):
        raise ValueError("date_folder must be a six-digit date")
    datetime.strptime(date, "%y%m%d")
    scope = SOURCES[source][0]
    return scope, f"_private-workflow-handoff/{scope}/{run_id}/{date}"


def validate_run(run: dict, jobs: dict, *, source: str, run_id: str, repository: str) -> None:
    attempt = run.get('run_attempt')
    if type(attempt) is not int or not 1 <= attempt <= 100:
        raise ValueError('Source attempt history is unknown or exceeds the bounded audit')
    if (str(run.get("id")) != run_id or run.get("path") != SOURCES[source][1]
            or run.get("head_branch") != "main"
            or (run.get("head_repository") or {}).get("full_name") != repository
            or run.get("status") != "completed" or run.get("conclusion") != "failure"):
        raise ValueError("Source must be the specified failed main-branch producer in this repository")
    history = jobs.get('attempts')
    if history is None and attempt == 1:
        history = [{'attempt': 1, 'jobs': jobs.get('jobs')}]
    if (not isinstance(history, list) or [row.get('attempt') for row in history if isinstance(row, dict)]
            != list(range(1, attempt + 1))):
        raise ValueError('Every source attempt must have complete independent job history')
    latest, observed_uploader = {}, False
    for row in history:
        records = row.get('jobs')
        never_submitted(records, 'upload-wechat-drafts', ['Build and upload WeChat drafts'])
        observed_uploader = observed_uploader or any(job.get('name') == 'upload-wechat-drafts' for job in records)
        for job in records:
            if job.get('name') == 'fetch-and-build':
                if sum(other.get('name') == 'fetch-and-build' for other in records) != 1:
                    raise ValueError('Original producer job identity is ambiguous')
                latest['fetch-and-build'] = job
    records = list(latest.values())
    if not observed_uploader:
        raise ValueError('Original uploader job identity was never observed')
    producer = [job for job in records if job.get("name") == "fetch-and-build"]
    if len(producer) != 1:
        raise ValueError('Recovery requires a completed original producer')
    steps = {step.get("name"): step.get("conclusion") for step in producer[0].get("steps", [])}
    for step in ("Build Portal translated report PDFs", "Upload translated reports to private R2 handoff"):
        if steps.get(step) != "success":
            raise ValueError(f"Original producer did not complete {step}")


def validate_translations(root: Path, scope: str, date: str, expected: int) -> None:
    summary = json.loads((root / "translation_summary.json").read_text(encoding="utf-8"))
    articles = sorted(root.glob("*/translated.md"))
    reports = summary.get("reports", [])
    if (expected < 1 or summary.get("date_folder") != date
            or summary.get("successful_count") != expected or len(articles) != expected
            or len(reports) != expected or summary.get("failures")):
        raise ValueError("Restored translation date/count does not match the requested complete handoff")
    output_names = {Path(str(report.get("output_dir", ""))).name for report in reports}
    if output_names != {article.parent.name for article in articles}:
        raise ValueError("Restored article directories differ from the translation manifest")
    for article in articles:
        status = json.loads((article.parent / "translation_status.json").read_text(encoding="utf-8"))
        source_parts = Path(str(status.get("source_report_dir", ""))).parts
        if (not article.read_text(encoding="utf-8").strip()
                or status.get("translated_markdown") != "translated.md"
                or len(source_parts) < 4 or source_parts[-4:-1] != ("xhs_notes", scope, date)):
            raise ValueError("Restored article is empty or belongs to another source/date")


def merge_receipts(destination: Path, restored: Path) -> None:
    """Keep every accepted draft from diagnostics and R2 without filename collisions."""
    accepted = {}
    groups = {}
    metadata = {}
    submissions = {}
    validator = runpy.run_path(str(Path(__file__).resolve().parents[1] /
        '.github/actions/resilient-diagnostic-artifact/validate_wechat_checkpoint.py'))['valid_submission']
    for directory in (restored, destination):
        for path in directory.glob('draft_submission_*.json'):
            if path.is_symlink() or not path.is_file():
                raise ValueError('Private submission checkpoint is not a regular file')
            receipt = json.loads(path.read_bytes())
            if not validator(receipt, path.name):
                raise ValueError('Private submission checkpoint is invalid')
            previous = submissions.get(path.name)
            if previous:
                if any(previous.get(key) != receipt.get(key) for key in
                       ('group_key', 'account_fingerprint', 'article_count', 'titles')):
                    raise ValueError('Conflicting submission checkpoint identity')
                if previous['status'] == receipt['status'] == 'accepted' and previous['media_id'] != receipt['media_id']:
                    raise ValueError('Conflicting accepted submission IDs')
                rank = {'rejected': 0, 'add_in_flight': 1, 'add_outcome_unknown': 2, 'accepted': 3}
                if rank[previous['status']] > rank[receipt['status']]:
                    continue
            submissions[path.name] = receipt
        summary_path = directory / "wechat_draft_summary.json"
        if not summary_path.is_file():
            continue
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
        if summary.get("dry_run"):
            raise ValueError("Recovery receipts must contain actual accepted drafts")
        metadata.update(summary)
        for draft in summary.get("drafts", []):
            media_id = str(draft.get("media_id") or "")
            group_key = str(draft.get("group_key") or "")
            payload_name = Path(str(draft.get("payload") or "")).name
            if not media_id or not group_key or not re.fullmatch(r"draft_payload_[A-Za-z0-9_-]+\.json", payload_name):
                raise ValueError("Recovery receipt has no complete media/group/payload identity")
            payload = json.loads((directory / payload_name).read_text(encoding="utf-8"))
            articles = payload.get("articles")
            if not isinstance(articles, list) or not articles or len(articles) != draft.get("article_count"):
                raise ValueError("Recovery receipt payload does not match its accepted article count")
            if group_key in groups and groups[group_key] != media_id:
                raise ValueError("Conflicting accepted media IDs for the same draft group; review receipts")
            if media_id in accepted:
                previous, previous_payload = accepted[media_id]
                if previous["group_key"] != group_key or previous_payload.get("articles") != articles:
                    raise ValueError("Conflicting payload identities for the same accepted draft; review receipts")
            groups[group_key] = media_id
            accepted[media_id] = (dict(draft), payload)
    if not accepted and not submissions:
        raise ValueError("Private receipt checkpoint contains no accepted drafts")
    destination.mkdir(parents=True, exist_ok=True)
    for filename, receipt in submissions.items():
        temporary = destination / (filename + '.tmp')
        temporary.write_text(json.dumps(receipt), encoding='utf-8')
        temporary.replace(destination / filename)
    if not accepted:
        return  # Preserve uncertain writes for API readback; never invent success.
    merged = []
    for media_id, (draft, payload) in accepted.items():
        # Distinct attempts both start at draft_payload_01.json. Preserve each
        # payload under its media identity before writing the union summary.
        filename = f"draft_payload_receipt_{hashlib.sha256(media_id.encode()).hexdigest()[:24]}.json"
        (destination / filename).write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        draft["payload"] = filename
        merged.append(draft)
    metadata.update(dry_run=False, draft_count=len(merged), drafts=merged)
    pending = destination / ".recovered_draft_summary.json"
    pending.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
    pending.replace(destination / "wechat_draft_summary.json")


def restore_receipts(prefix: str, destination: Path, *, client=None, bucket=None) -> bool:
    client = client or build_r2_client()
    bucket = bucket or r2_bucket()
    key = prefix + "/recovery-receipts.tar.gz"
    try:
        client.head_object(Bucket=bucket, Key=key)
    except Exception as exc:
        # Only absence is optional: authorization/service failures must stop replay.
        code = str(getattr(exc, "response", {}).get("Error", {}).get("Code", ""))
        if code in {"404", "NoSuchKey", "NotFound"}:
            print("No previous recovery receipt checkpoint")
            return False
        raise
    with tempfile.TemporaryDirectory(prefix="wechat-recovery-receipts-") as temporary:
        restored = Path(temporary) / "receipts"
        download_directory(key, restored, client=client, bucket=bucket)
        merge_receipts(destination, restored)
    return True


def save_receipts(prefix: str, receipts: Path) -> bool:
    summary_path = receipts / "wechat_draft_summary.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8")) if summary_path.is_file() else {}
    if summary.get("dry_run"):
        raise ValueError("Cannot persist dry-run recovery receipts")
    pending = list(receipts.glob('draft_submission_*.json'))
    if not pending and not any(isinstance(draft, dict) and draft.get("media_id") for draft in summary.get("drafts", [])):
        print("No accepted drafts to checkpoint; preserving any existing private receipts")
        return False
    if pending:
        validator = runpy.run_path(str(Path(__file__).resolve().parents[1] /
            '.github/actions/resilient-diagnostic-artifact/validate_wechat_checkpoint.py'))['valid_submission']
        for path in pending:
            if path.is_symlink() or not validator(json.loads(path.read_bytes()), path.name):
                raise ValueError('Private submission checkpoint is invalid')
    upload_directory(receipts, prefix + "/recovery-receipts.tar.gz")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("validate-run", "restore", "save-receipts"))
    parser.add_argument("--source", required=True, choices=tuple(SOURCES))
    parser.add_argument("--source-run-id", required=True)
    parser.add_argument("--date-folder", required=True)
    parser.add_argument("--expected-count", required=True, type=int)
    parser.add_argument("--run-json", type=Path)
    parser.add_argument("--jobs-json", type=Path)
    args = parser.parse_args()
    scope, prefix = coordinates(args.source, args.source_run_id, args.date_folder)
    translated = Path("portal_translated_reports") / scope / args.date_folder
    receipts = Path("wechat_drafts") / scope / args.date_folder
    if args.command == "validate-run":
        repository = os.environ["GITHUB_REPOSITORY"]
        if args.run_json is not None and args.jobs_json is not None:
            run, jobs = json.loads(args.run_json.read_text()), json.loads(args.jobs_json.read_text())
        elif args.run_json is not None or args.jobs_json is not None:
            raise ValueError("Provide both --run-json and --jobs-json, or neither")
        else:
            run, jobs = fetch_source_metadata(repository, args.source_run_id, os.environ.get("GH_TOKEN", ""))
        validate_run(run, jobs, source=args.source, run_id=args.source_run_id, repository=repository)
        if args.expected_count < 1:
            raise ValueError("expected_count must be positive")
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as output:
            output.write(f"scope={scope}\n")
    elif args.command == "restore":
        download_directory(prefix + "/translated.tar.gz", translated)
        validate_translations(translated, scope, args.date_folder, args.expected_count)
        restore_receipts(prefix, receipts)
    else:
        save_receipts(prefix, receipts)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
