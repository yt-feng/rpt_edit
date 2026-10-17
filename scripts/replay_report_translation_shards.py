#!/usr/bin/env python3
"""Replay failed PDF matrix members against the original immutable private plan."""
from __future__ import annotations

import argparse
from datetime import datetime
import json
import os
from pathlib import Path
import re
import tempfile

import portal_translation_shards as shards
from private_workflow_handoff import build_r2_client, download_directory, list_keys, r2_bucket, upload_directory
from recover_private_wechat_handoff import fetch_source_metadata

SOURCE_WORKFLOW = ".github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml"
MATRIX_NAME = re.compile(r"translate-report-shard \(([0-9]+)\)")


def coordinates(run_id: str, date: str, requested: str) -> tuple[str, list[int]]:
    if not re.fullmatch(r"[1-9][0-9]*", run_id) or not re.fullmatch(r"(?:[0-9]{6}|[0-9]{8})", date):
        raise ValueError("Replay requires an exact numeric run ID and date folder")
    datetime.strptime(date, "%y%m%d" if len(date) == 6 else "%Y%m%d")
    if not re.fullmatch(r"[0-9]+(?:,[0-9]+)*", requested):
        raise ValueError("Failed shard indices must be a comma-separated numeric list")
    indices = [int(value) for value in requested.split(",")]
    if len(indices) != len(set(indices)):
        raise ValueError("Failed shard indices must not repeat")
    return f"_private-workflow-handoff/xhs/{run_id}/{date}", sorted(indices)


def validate_source(run: dict, jobs: dict, repository: str, run_id: str, requested: list[int]) -> dict[int, dict]:
    if (str(run.get("id")) != run_id or run.get("path") != SOURCE_WORKFLOW
            or run.get("head_branch") != "main" or run.get("run_attempt") != 1
            or (run.get("head_repository") or {}).get("full_name") != repository):
        raise ValueError("Replay source must be the specified main-branch daily workflow's first attempt")
    records = jobs.get("jobs", [])
    if jobs.get("total_count", len(records)) != len(records):
        raise ValueError("Source job inventory is incomplete")
    planners = [job for job in records if job.get("name") == "plan-portal-translated-reports"]
    if len(planners) != 1 or planners[0].get("conclusion") != "success":
        raise ValueError("Original translation plan did not complete successfully")
    matrix = {}
    for job in records:
        match = MATRIX_NAME.fullmatch(str(job.get("name", "")))
        if match:
            index = int(match.group(1))
            if index in matrix:
                raise ValueError("Source job inventory repeats a translation shard")
            matrix[index] = job
    if not matrix or any(job.get("status") != "completed" for job in matrix.values()):
        raise ValueError("Wait until every original translation matrix job has completed")
    if not set(requested).issubset(matrix):
        raise ValueError("Requested shard is absent from the original translation matrix")
    for index, job in matrix.items():
        expected = "failure" if index in requested else "success"
        if job.get("conclusion") != expected:
            raise ValueError("Request exactly the failed shards; active, successful or cancelled shards cannot be replayed")
    return matrix


def validate_plan(plan: dict, date: str, matrix: dict[int, dict], expected_hash: str = "") -> None:
    if plan["date_folder"] != date or set(matrix) != set(range(plan["shard_count"])):
        raise ValueError("Original plan date or shard inventory differs from source workflow")
    if expected_hash and plan["plan_sha256"] != expected_hash:
        raise ValueError("Private translation plan changed after recovery preparation")


def recovery_completed(jobs: dict) -> bool:
    names = {f"deliver-recovered-report-articles / {stage}" for stage in ("generate", "deliver", "publish")}
    records = [job for job in jobs["jobs"] if job.get("name") in names]
    if not records or all(job.get("conclusion") == "skipped" for job in records):
        return False
    if (len(records) != len(names) or {job["name"] for job in records} != names
            or any(job.get("status") != "completed" or job.get("conclusion") != "success" for job in records)):
        raise ValueError("Original recovered article delivery is not completely verified")
    return True


def resolve_source_prefix(plan: dict, original_prefix: str, run: dict, jobs: dict,
                          expected_prefix: str = "") -> str:
    """Older plans omitted the distinct recovered source location.

    Resolve only the original Daily's successful recovery, never a most-recent
    archive or an arbitrary fallback after a source hash mismatch.
    """
    recovered = recovery_completed(jobs)
    prefix = plan.get("source_prefix")
    if prefix is None:
        prefix = original_prefix
        if recovered:
            root = f"_private-workflow-handoff/xhs-recovery/{run['id']}/{plan['date_folder']}"
            pattern = re.compile(re.escape(root) + r"/[a-f0-9]{64}/articles/shard_0\.tar\.gz")
            candidates = [key.removesuffix("/shard_0.tar.gz") for key in list_keys(root) if pattern.fullmatch(key)]
            if len(candidates) != 1:
                raise ValueError("Original recovered translation source is missing or ambiguous")
            prefix = candidates[0]
    source_run, manifest = shards.source_prefix_identity(prefix, plan["date_folder"])
    if source_run != str(run["id"]) or bool(manifest) != recovered:
        raise ValueError("Translation source prefix differs from the original workflow outcome")
    if expected_prefix and prefix != expected_prefix:
        raise ValueError("Translation source prefix changed after recovery preparation")
    return prefix


def validate_recovered_sources(plan: dict, prefix: str, run: dict, date_root: Path) -> None:
    """Authenticate the original recovery receipt and every planned extraction."""
    _, manifest = shards.source_prefix_identity(prefix, plan["date_folder"])
    if manifest is None:
        return
    from recover_report_articles import PROVENANCE, validate_articles
    root = date_root / "shard_0"
    receipt = validate_articles(root, plan["source_count"], plan["date_folder"])
    provenance = json.loads((root / PROVENANCE).read_text(encoding="utf-8"))
    source_receipt = json.loads(provenance["source_receipt_json"])
    manifest_key = "manifest_sha256" if receipt["source_kind"] == "mineru-recovery" else "selected_manifest_sha256"
    if (receipt["source_run_id"] != str(run["id"]) or receipt["source_execution_sha"] != run["head_sha"]
            or receipt["source_handoff_run_id"] != str(run["id"])
            or receipt["source_handoff_execution_sha"] != run["head_sha"]
            or provenance.get("manifest_sha256") != manifest or source_receipt.get(manifest_key) != manifest):
        raise ValueError("Recovered translation source does not match the original Daily identity")
    for index in range(plan["shard_count"]):
        shards.selected_reports(plan, index, date_root)


def validate_result(plan: dict, index: int, root: Path) -> None:
    records = shards.shard_records(plan, index)
    date_root = root / "portal_translated_reports" / plan["date_folder"]
    summary = json.loads((date_root / f"translation_shard_{index}.json").read_text(encoding="utf-8"))
    expected = {record["global_index"]: record for record in records}
    reports = summary.get("reports", [])
    if (summary.get("plan_sha256") != plan["plan_sha256"] or summary.get("failures")
            or summary.get("successful_count") != len(records) or len(reports) != len(records)
            or {report.get("global_index") for report in reports} != set(expected)):
        raise ValueError("Recovered PDF shard is incomplete or differs from the original plan")
    for report in reports:
        global_index = report["global_index"]
        name = Path(report["output_dir"]).name
        if not name.startswith(f"{global_index:02d}-"):
            raise ValueError("Recovered report changed its global index")
        directory = date_root / name
        status = json.loads((directory / "translation_status.json").read_text(encoding="utf-8"))
        pdf_name = f"portal_translated_report_{global_index:02d}.pdf"
        if (status.get("global_index") != global_index
                or not str(status.get("source_report_dir", "")).endswith("/" + expected[global_index]["relative_dir"])
                or status.get("pdf") != pdf_name
                or not (directory / "translated.md").read_text(encoding="utf-8").strip()
                or (directory / pdf_name).stat().st_size <= 1024):
            raise ValueError("Recovered PDF or its source identity is incomplete")
        record = expected[global_index]
        if plan["schema_version"] >= 2 and any(status.get(key) != record.get(key) for key in
                ("source_method", "source_markdown", "source_sha256", "source_provenance_sha256")):
            raise ValueError("Recovered PDF extraction identity differs from the original plan")
        if plan["schema_version"] == 1 and (
                status.get("source_method", "mineru") != "mineru"
                or status.get("source_markdown", "source_mineru.md") != "source_mineru.md"
                or status.get("source_sha256", record["source_sha256"]) != record["source_sha256"]):
            raise ValueError("Legacy recovered PDF extraction identity changed")


def restore_completed_slot(plan: dict, index: int, prefix: str, destination: Path, *, client=None, bucket=None) -> bool:
    client, bucket = client or build_r2_client(), bucket or r2_bucket()
    key = f"{prefix}/translated_{index}.tar.gz"
    try:
        client.head_object(Bucket=bucket, Key=key)
    except Exception as exc:
        code = str(getattr(exc, "response", {}).get("Error", {}).get("Code", ""))
        if code in {"404", "NoSuchKey", "NotFound"}:
            return False
        raise
    download_directory(key, destination, client=client, bucket=bucket)
    validate_result(plan, index, destination)
    print(f"Preserving previously completed PDF shard {index}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("prepare", "materialize", "publish", "merge"))
    parser.add_argument("--source-run-id", required=True)
    parser.add_argument("--date-folder", required=True)
    parser.add_argument("--failed-shards", required=True)
    parser.add_argument("--plan-dir", required=True, type=Path)
    parser.add_argument("--plan-sha256", default="")
    parser.add_argument("--source-prefix", default="")
    parser.add_argument("--shard-index", type=int)
    parser.add_argument("--output-root", type=Path, required=True)
    args = parser.parse_args()
    prefix, requested = coordinates(args.source_run_id, args.date_folder, args.failed_shards)
    repository = os.environ["GITHUB_REPOSITORY"]
    run, jobs = fetch_source_metadata(repository, args.source_run_id, os.environ.get("GH_TOKEN", ""))
    matrix = validate_source(run, jobs, repository, args.source_run_id, requested)
    if args.command in {"materialize", "publish"} and args.shard_index not in requested:
        raise ValueError("Only an explicitly requested failed shard may be replayed")
    download_directory(prefix + "/translation-plan.tar.gz", args.plan_dir)
    plan = shards.load_plan(args.plan_dir / "plan.json")
    validate_plan(plan, args.date_folder, matrix, args.plan_sha256)
    if args.command == "prepare":
        source_prefix = resolve_source_prefix(plan, prefix, run, jobs, args.source_prefix)
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as output:
            output.write(f"shard_indices={json.dumps(requested)}\nplan_sha256={plan['plan_sha256']}\nselected_count={plan['selected_count']}\n")
            output.write(f"source_prefix={source_prefix}\n")
    elif args.command == "materialize":
        complete = restore_completed_slot(plan, args.shard_index, prefix, args.output_root)
        if not complete:
            source_prefix = resolve_source_prefix(plan, prefix, run, jobs, args.source_prefix)
            date_root = Path("xhs_notes/dropbox") / args.date_folder
            shards.materialize(plan, args.shard_index, source_prefix, date_root)
            validate_recovered_sources(plan, source_prefix, run, date_root)
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as output:
            output.write(f"complete={str(complete).lower()}\n")
        with open(os.environ["GITHUB_ENV"], "a", encoding="utf-8") as output:
            output.write(f"TRANSLATION_CHECKPOINT_SCOPE={shards.checkpoint_scope(plan, args.shard_index)}\n")
    elif args.command == "publish":
        validate_result(plan, args.shard_index, args.output_root)
        # Another attempt may already have completed this slot. Never replace it.
        with tempfile.TemporaryDirectory(prefix="verified-pdf-slot-") as temporary:
            if restore_completed_slot(plan, args.shard_index, prefix, Path(temporary)):
                return 0
        upload_directory(args.output_root, f"{prefix}/translated_{args.shard_index}.tar.gz", include_translated_pdfs=True)
    else:
        with tempfile.TemporaryDirectory(prefix="recovered-pdf-shards-") as temporary:
            shards.download_results(plan, prefix, Path(temporary))
            summary = shards.merge_shards(plan, Path(temporary), args.output_root)
        print(f"Verified all {summary['successful_count']} originally selected translated PDFs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
