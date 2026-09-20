#!/usr/bin/env python3
"""Resume source-matched paid report generation using a persistent private R2 memo.

The immutable input identity includes actual PDF bytes, shard membership, relevant
options, source code and prompts. Only exact identities are restored; a renamed,
changed or reordered source cannot make an old article pass skip-existing checks.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import tempfile
from typing import Any

from private_workflow_handoff import download_directory, upload_directory

CHECKPOINT_FILE = "_generation_checkpoint.json"
VERSION = 1
GENERATION_FILES = (
    "scripts/pdf_to_xhs_batch.py", "scripts/run_pdf_to_xhs_in_batches.py",
    "scripts/finalize_outputs.py", "scripts/postprocess_podcast.py",
    "scripts/sensitive_content_guard.py", "scripts/wechat_title_optimizer.py",
    "scripts/wechat_article_quality.py", "scripts/institution_names.py",
    "scripts/deepseek_http.py", "scripts/wechat_editorial_binding.py",
)
OPTION_NAMES = (
    "model", "deepseek_base_url", "mineru_model", "language", "ocr",
    "wechat_length", "community_cta", "reports_per_shard", "batch_size",
)


def input_identity(manifest: Path, shard_index: int, reports_per_shard: int,
                   options: dict[str, Any], repo_root: Path) -> str:
    if shard_index < 0 or reports_per_shard < 1:
        raise ValueError("Invalid generation shard parameters")
    rows = json.loads(manifest.read_text(encoding="utf-8"))
    if not isinstance(rows, list) or not all(isinstance(row, dict) for row in rows):
        raise ValueError("Expected a selected report manifest list")
    # Match run_pdf_to_xhs_in_batches.find_pdfs: copied input files are flat and
    # lexically sorted, including batches containing more than 99 reports.
    rows = sorted(rows, key=lambda row: str(row.get("process_local_path") or ""))
    selected = rows[shard_index * reports_per_shard:(shard_index + 1) * reports_per_shard]
    if not selected:
        raise ValueError("Cannot checkpoint an empty generation shard")
    sources = []
    for row in selected:
        digest = str(row.get("content_sha256") or "")
        source_name = Path(str(row.get("process_local_path") or "")).name
        if not re.fullmatch(r"[0-9a-f]{64}", digest) or not source_name:
            raise ValueError("Source manifest is missing its verified PDF content hash")
        sources.append({"filename": source_name, "content_sha256": digest})
    contract = {name: hashlib.sha256((repo_root / name).read_bytes()).hexdigest() for name in GENERATION_FILES}
    for path in sorted((repo_root / "prompts").glob("*.md")):
        contract[str(path.relative_to(repo_root))] = hashlib.sha256(path.read_bytes()).hexdigest()
    identity = {
        "version": VERSION, "shard_index": shard_index, "reports_per_shard": reports_per_shard,
        "sources": sources, "options": {name: options.get(name) for name in OPTION_NAMES},
        "contract": contract,
    }
    return hashlib.sha256(json.dumps(identity, sort_keys=True, ensure_ascii=True).encode()).hexdigest()


def checkpoint_key(date_folder: str, shard_index: int, identity: str) -> str:
    if not re.fullmatch(r"\d{6,8}", date_folder) or shard_index < 0:
        raise ValueError("Invalid generation checkpoint date or shard")
    if not re.fullmatch(r"[0-9a-f]{64}", identity):
        raise ValueError("Invalid generation checkpoint identity")
    return f"_workflow-cache/report-generation/v1/{date_folder}/shard_{shard_index}/{identity}.tar.gz"


def _clear_directory(directory: Path) -> None:
    if directory.resolve() in {Path.cwd().resolve(), Path('/')}:
        raise ValueError("Refusing to replace a generation root directory")
    if directory.is_symlink():
        directory.unlink()
    elif directory.exists():
        shutil.rmtree(directory)
    directory.mkdir(parents=True, exist_ok=True)


def _prune_incomplete_report_markers(directory: Path) -> None:
    # Failed intermediate files must not satisfy the batch runner's presence-only
    # skip-existing gate. Completed reports and their finalization caches survive.
    for item in directory.iterdir():
        if not item.is_dir() or not (item / "wechat_article.md").exists():
            continue
        try:
            status = json.loads((item / "status.json").read_text(encoding="utf-8"))
            complete = (isinstance(status, dict) and not status.get("error")
                        and status.get("wechat_article") == "wechat_article.md"
                        and (item / "source_mineru.md").stat().st_size > 0
                        and (item / "wechat_article.md").stat().st_size > 0)
        except (OSError, ValueError):
            complete = False
        if not complete:
            (item / "wechat_article.md").unlink()


def restore(directory: Path, key: str, identity: str, *, force: bool = False) -> bool:
    if force:
        _clear_directory(directory)
        print("Forced generation: private checkpoint reuse bypassed.")
        return False
    with tempfile.TemporaryDirectory(prefix="generation-checkpoint-") as temporary:
        candidate = Path(temporary) / "candidate"
        try:
            download_directory(key, candidate)
        except Exception as error:
            code = str(getattr(error, "response", {}).get("Error", {}).get("Code", ""))
            if code not in {"NoSuchKey", "404", "NotFound"}:
                raise
            _clear_directory(directory)
            print("No exact private generation checkpoint; processing current sources.")
            return False
        metadata = json.loads((candidate / CHECKPOINT_FILE).read_text(encoding="utf-8"))
        if metadata.get("version") != VERSION or metadata.get("identity") != identity:
            raise ValueError("Private generation checkpoint identity does not match current inputs")
        _prune_incomplete_report_markers(candidate)
        if metadata.get("complete") is not True:
            (candidate / "shard_run_summary.md").unlink(missing_ok=True)
        _clear_directory(directory)
        shutil.copytree(candidate, directory, dirs_exist_ok=True)
    print("Restored exact source-matched private generation checkpoint.")
    return True


def _finalization_succeeded(directory: Path) -> bool:
    try:
        finalized = json.loads((directory / "finalize_summary.json").read_text(encoding="utf-8"))
        guarded = json.loads((directory / "sensitive_content_guard_summary.json").read_text(encoding="utf-8"))
        if not isinstance(finalized, list) or not finalized or not isinstance(guarded, list) or not guarded:
            return False
        if any(not isinstance(row, dict) or any(value for key, value in row.items() if key.endswith("_error")) for row in finalized):
            return False
        if any(not isinstance(row, dict) or row.get("error") or row.get("rewrite_error") or row.get("api_errors") for row in guarded):
            return False
    except (OSError, ValueError):
        return False
    for item in directory.iterdir():
        if not item.is_dir() or not (item / "source_mineru.md").is_file():
            continue
        # This production contract includes Zhihu. A successful generation memo
        # exists only after generated_text_is_usable accepted the result.
        try:
            memo = json.loads((item / "zhihu_article.md.generation.json").read_text(encoding="utf-8"))
            if not re.fullmatch(r"[0-9a-f]{64}", str(memo.get("input_sha256") or "")):
                return False
            if (item / "zhihu_article.md").stat().st_size == 0:
                return False
        except (OSError, ValueError, AttributeError):
            return False
    return (directory / "shard_run_summary.md").is_file()


def save(directory: Path, key: str, identity: str, *, complete: bool = False) -> bool:
    if not directory.is_dir() or not any(directory.glob("*/source_mineru.md")):
        print("No generated report sources to checkpoint.")
        return False
    # Never label a partially failed finalizer complete merely because its CLI
    # returned success. The next run must retry only unfinished finalization.
    accepted_complete = complete and _finalization_succeeded(directory)
    metadata = {"version": VERSION, "identity": identity, "complete": accepted_complete}
    (directory / CHECKPOINT_FILE).write_text(json.dumps(metadata, sort_keys=True) + "\n", encoding="utf-8")
    upload_directory(directory, key)
    print(f"Saved private generation checkpoint; complete={str(accepted_complete).lower()}.")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("restore", "save"))
    parser.add_argument("--date-folder", required=True)
    parser.add_argument("--shard-index", type=int, required=True)
    parser.add_argument("--reports-per-shard", type=int, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--directory", type=Path, required=True)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--force-reprocess", default="false")
    parser.add_argument("--complete", default="false")
    args = parser.parse_args()
    options = json.loads(os.getenv("GENERATION_OPTIONS_JSON", "{}"))
    if not isinstance(options, dict):
        raise ValueError("GENERATION_OPTIONS_JSON must be an object")
    identity = input_identity(args.manifest, args.shard_index, args.reports_per_shard, options, args.repo_root)
    key = checkpoint_key(args.date_folder, args.shard_index, identity)
    if args.command == "restore":
        restore(args.directory, key, identity, force=args.force_reprocess.lower() == "true")
    else:
        save(args.directory, key, identity, complete=args.complete.lower() == "true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
