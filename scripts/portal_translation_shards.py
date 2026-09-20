#!/usr/bin/env python3
"""Plan bounded private report translation shards and verify their exact union."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import shutil


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def create_plan(date_dir: Path, max_reports: str = "all", reports_per_shard: int = 5) -> dict:
    from build_portal_translated_reports import find_report_dirs, parse_selection_limit

    if not 1 <= reports_per_shard <= 8:
        raise ValueError("Translation shards must contain between 1 and 8 reports")
    available = find_report_dirs(date_dir)
    limit = parse_selection_limit(max_reports, "--max-reports")
    selected = available if limit is None else available[:limit]
    if not selected:
        raise ValueError("No reports available for the translation plan")
    records = []
    for index, directory in enumerate(selected, 1):
        relative = directory.relative_to(date_dir).as_posix()
        if not re.fullmatch(r"shard_\d+/[^/]+", relative):
            raise ValueError("Dropbox translation plans require shard_<index>/<report> inputs")
        records.append({"global_index": index, "relative_dir": relative,
                        "source_sha256": digest(directory / "source_mineru.md")})
    plan = {
        "schema_version": 1, "date_folder": date_dir.name, "source_count": len(available),
        "max_reports": "all" if limit is None else limit, "selected_count": len(selected),
        "reports_per_shard": reports_per_shard, "shard_count": math.ceil(len(selected) / reports_per_shard),
        "reports": records,
    }
    plan["plan_sha256"] = hashlib.sha256(json.dumps(plan, sort_keys=True).encode()).hexdigest()
    return plan


def load_plan(path: Path) -> dict:
    plan = json.loads(path.read_text(encoding="utf-8"))
    stored_digest = plan.get("plan_sha256")
    actual = hashlib.sha256(json.dumps({key: value for key, value in plan.items() if key != "plan_sha256"}, sort_keys=True).encode()).hexdigest()
    if stored_digest != actual or plan.get("schema_version") != 1:
        raise ValueError("Translation plan checksum or schema mismatch")
    reports = plan["reports"]
    if not reports or len(reports) != plan["selected_count"]:
        raise ValueError("Translation plan has missing report records")
    if [item["global_index"] for item in reports] != list(range(1, len(reports) + 1)):
        raise ValueError("Translation plan has missing or duplicate global indices")
    if len({item["relative_dir"] for item in reports}) != len(reports):
        raise ValueError("Translation plan repeats a source report")
    for item in reports:
        relative = PurePosixPath(item["relative_dir"])
        if len(relative.parts) != 2 or ".." in relative.parts or not re.fullmatch(r"shard_\d+", relative.parts[0]):
            raise ValueError("Unsafe source report path in translation plan")
    per_shard = plan["reports_per_shard"]
    if not 1 <= per_shard <= 8 or plan["shard_count"] != math.ceil(len(reports) / per_shard):
        raise ValueError("Translation plan shard dimensions are inconsistent")
    return plan


def shard_records(plan: dict, shard_index: int) -> list[dict]:
    if not 0 <= shard_index < plan["shard_count"]:
        raise ValueError("Translation shard index is outside the plan")
    first = shard_index * plan["reports_per_shard"]
    return plan["reports"][first:first + plan["reports_per_shard"]]


def selected_reports(plan: dict, shard_index: int, date_dir: Path) -> list[tuple[int, Path]]:
    if date_dir.name != plan["date_folder"]:
        raise ValueError("Translation plan date does not match the source directory")
    selected = []
    for record in shard_records(plan, shard_index):
        directory = date_dir / record["relative_dir"]
        if not directory.resolve().is_relative_to(date_dir.resolve()):
            raise ValueError("Source report escapes the planned date directory")
        if digest(directory / "source_mineru.md") != record["source_sha256"]:
            raise ValueError(f"Source changed after planning: global index {record['global_index']}")
        selected.append((record["global_index"], directory))
    return selected


def checkpoint_scope(plan: dict, shard_index: int) -> str:
    shard_records(plan, shard_index)
    # No run ID: reruns of the same date and dimensions reuse successful
    # content-addressed segments, without workers overwriting one another.
    return f"dropbox-p{plan['reports_per_shard']}-n{plan['shard_count']}-i{shard_index}"


def materialize(plan: dict, shard_index: int, prefix: str, date_dir: Path) -> None:
    from private_workflow_handoff import download_directory, validate_prefix

    prefix = validate_prefix(prefix)
    source_shards = sorted({PurePosixPath(record["relative_dir"]).parts[0] for record in shard_records(plan, shard_index)})
    for source_shard in source_shards:
        download_directory(f"{prefix}{source_shard}.tar.gz", date_dir / source_shard)
    selected_reports(plan, shard_index, date_dir)


def download_results(plan: dict, prefix: str, destination: Path) -> None:
    from private_workflow_handoff import download_directory, validate_prefix

    prefix = validate_prefix(prefix)
    for index in range(plan["shard_count"]):
        # Do not name these shard_<n>.tar.gz: existing raw-shard consumers
        # recursively list that suffix under the same private run prefix.
        download_directory(f"{prefix}translated_{index}.tar.gz", destination / f"shard_{index}")


def merge_shards(plan: dict, shard_root: Path, output_root: Path) -> dict:
    date = plan["date_folder"]
    expected = {record["global_index"]: record for record in plan["reports"]}
    merged = []
    seen = set()
    copies = []
    logs = []
    for shard_index in range(plan["shard_count"]):
        source_root = shard_root / f"shard_{shard_index}"
        date_root = source_root / "portal_translated_reports" / date
        summary_path = date_root / f"translation_shard_{shard_index}.json"
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
        records = shard_records(plan, shard_index)
        indices = {item["global_index"] for item in records}
        if (summary.get("plan_sha256") != plan["plan_sha256"] or summary.get("failures")
                or summary.get("successful_count") != len(records)
                or {item.get("global_index") for item in summary.get("reports", [])} != indices):
            raise ValueError(f"Translation shard {shard_index} is incomplete or mismatches the plan")
        for report in summary["reports"]:
            index = report["global_index"]
            if index in seen:
                raise ValueError(f"Duplicate translated report index: {index}")
            seen.add(index)
            name = Path(report["output_dir"]).name
            if not re.match(rf"^{index:02d}-", name):
                raise ValueError(f"Output directory does not use global index {index}")
            directory = date_root / name
            expected_source = expected[index]["relative_dir"]
            status = json.loads((directory / "translation_status.json").read_text(encoding="utf-8"))
            if status.get("global_index") != index or not str(status.get("source_report_dir", "")).endswith("/" + expected_source):
                raise ValueError(f"Translation status points at a different source: {index}")
            pdf_name = f"portal_translated_report_{index:02d}.pdf"
            if (status.get("pdf") != pdf_name or not (directory / "translated.md").is_file()
                    or not (directory / pdf_name).is_file() or (directory / pdf_name).stat().st_size <= 1024):
                raise ValueError(f"Missing completed translation/PDF for global report {index}")
            destination = output_root / "portal_translated_reports" / date / name
            copies.append((directory, destination))
            merged.append({**report, "output_dir": f"portal_translated_reports/{date}/{name}",
                           "pdf_path": f"portal_translated_reports/{date}/{name}/{pdf_name}"})
        logs.append((source_root / "translation_shard_logs" / f"shard_{shard_index}.log", shard_index))
    if seen != set(expected):
        raise ValueError("Translated shard union does not contain every selected report")
    # Validate all shards first. Never publish an apparently successful subset.
    date_root = output_root / "portal_translated_reports" / date
    if date_root.exists():
        shutil.rmtree(date_root)
    for source, destination in copies:
        shutil.copytree(source, destination)
    merged.sort(key=lambda report: report["global_index"])
    summary = {
        "date_folder": date, "max_reports": plan["max_reports"],
        "selected_count": plan["selected_count"], "successful_count": len(merged),
        "title_neutralized_count": sum(bool((item.get("wechat_title_decision") or {}).get("neutralization_changes")) for item in merged),
        "sensitive_skipped_count": 0, "sensitive_skipped": [], "failures": [], "reports": merged,
        "plan_sha256": plan["plan_sha256"], "shard_count": plan["shard_count"],
    }
    write_json(date_root / "translation_summary.json", summary)
    with (output_root / "portal_translated_reports_progress.log").open("w", encoding="utf-8") as combined:
        for source, index in logs:
            combined.write(f"\n--- Translation shard {index} ---\n")
            if source.exists():
                combined.write(source.read_text(encoding="utf-8", errors="replace"))
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    plan_cmd = subparsers.add_parser("plan")
    plan_cmd.add_argument("--date-dir", type=Path, required=True)
    plan_cmd.add_argument("--max-reports", default="all")
    plan_cmd.add_argument("--reports-per-shard", type=int, default=5)
    plan_cmd.add_argument("--output", type=Path, required=True)
    worker = subparsers.add_parser("materialize")
    worker.add_argument("--plan", type=Path, required=True)
    worker.add_argument("--shard-index", type=int, required=True)
    worker.add_argument("--prefix", required=True)
    worker.add_argument("--date-dir", type=Path, required=True)
    merge = subparsers.add_parser("merge")
    merge.add_argument("--plan", type=Path, required=True)
    merge.add_argument("--shard-root", type=Path, required=True)
    merge.add_argument("--output-root", type=Path, required=True)
    download = subparsers.add_parser("download-results")
    download.add_argument("--plan", type=Path, required=True)
    download.add_argument("--prefix", required=True)
    download.add_argument("--destination", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "plan":
        plan = create_plan(args.date_dir, args.max_reports, args.reports_per_shard)
        write_json(args.output, plan)
        if os.environ.get("GITHUB_OUTPUT"):
            with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as output:
                output.write(f"shard_indices={json.dumps(list(range(plan['shard_count'])))}\n")
                output.write(f"shard_count={plan['shard_count']}\nselected_count={plan['selected_count']}\n")
        print(f"Selected {plan['selected_count']} reports in {plan['shard_count']} translation shards")
    elif args.command == "materialize":
        plan = load_plan(args.plan)
        materialize(plan, args.shard_index, args.prefix, args.date_dir)
        if os.environ.get("GITHUB_ENV"):
            with open(os.environ["GITHUB_ENV"], "a", encoding="utf-8") as output:
                output.write(f"TRANSLATION_CHECKPOINT_SCOPE={checkpoint_scope(plan, args.shard_index)}\n")
    elif args.command == "download-results":
        download_results(load_plan(args.plan), args.prefix, args.destination)
    else:
        summary = merge_shards(load_plan(args.plan), args.shard_root, args.output_root)
        print(f"Verified and merged all {summary['successful_count']} translated reports")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
