#!/usr/bin/env python3
"""Materialize individually completed, exactly bound sources for daily delivery.

A failed shard is not a failed report. These receipts preserve the entire frozen
selection while admitting only checked report contents. An empty shard receipt
is useful progress; an empty daily delivery is never accepted.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import tempfile
from typing import Any

RECEIPT_NAME = "daily_delivery_receipt.json"
MANIFEST_NAME = "selected_to_process_manifest.json"
SHA256 = re.compile(r"[a-f0-9]{64}")
SOURCE_MARKERS = ("source_mineru.md", "source_native_pdf.md")
GENERATED_MARKERS = ("wechat_article.md", "note.md", "zhihu_article.md")
DONE_STATES = {"done", "success", "completed", "segmented_complete"}


def _require(condition: bool, reason: str) -> None:
    if not condition:
        raise ValueError(reason)


def _digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _regular(path: Path, root: Path) -> bool:
    if not path.is_file() or path.is_symlink():
        return False
    try:
        relative = path.relative_to(root)
    except ValueError:
        return False
    return not root.is_symlink() and all(not (root / Path(*relative.parts[:n])).is_symlink()
                                         for n in range(1, len(relative.parts)))


def _read(path: Path, root: Path | None = None) -> bytes:
    _require(_regular(path, root or path.parent), "daily_delivery_file_not_regular")
    return path.read_bytes()


def _json(path: Path, root: Path | None = None) -> Any:
    return json.loads(_read(path, root))


def _identity(date_folder: str, source_run_id: str, source_execution_sha: str) -> None:
    from datetime import datetime
    _require(isinstance(date_folder, str) and bool(re.fullmatch(r"[0-9]{6}", date_folder)),
             "daily_delivery_date_invalid")
    datetime.strptime(date_folder, "%y%m%d")
    _require(isinstance(source_run_id, str) and bool(re.fullmatch(r"[1-9][0-9]{0,19}", source_run_id)),
             "daily_delivery_run_invalid")
    _require(isinstance(source_execution_sha, str)
             and bool(re.fullmatch(r"[a-f0-9]{40}", source_execution_sha)), "daily_delivery_sha_invalid")


def read_selection(manifest: Path) -> tuple[bytes, list[dict[str, Any]]]:
    raw = _read(Path(manifest))
    value = json.loads(raw)
    _require(isinstance(value, list) and bool(value) and all(isinstance(row, dict) for row in value),
             "daily_delivery_manifest_invalid")
    rows = []
    for row in sorted(value, key=lambda item: str(item.get("process_local_path") or "")):
        source = row.get("process_local_path")
        digest = row.get("content_sha256")
        _require(isinstance(source, str) and bool(source) and "\\" not in source
                 and Path(source).suffix.lower() == ".pdf"
                 and isinstance(digest, str) and bool(SHA256.fullmatch(digest)),
                 "daily_delivery_manifest_source_invalid")
        rows.append({**row, "source_pdf": Path(source).name})
    _require(len({row["source_pdf"] for row in rows}) == len(rows), "daily_delivery_duplicate_source")
    return raw, rows


def _inventory_digest(rows: list[dict[str, Any]]) -> str:
    raw = json.dumps(sorted((row["source_pdf"], row["content_sha256"]) for row in rows),
                     ensure_ascii=False, separators=(",", ":")).encode()
    return _digest(raw)


def _unavailable(rows: list[dict[str, Any]], unavailable: Any) -> list[dict[str, str]]:
    _require(isinstance(unavailable, list), "daily_delivery_unavailable_inventory_invalid")
    seen = {row["source_pdf"] for row in rows}
    result = []
    for row in unavailable:
        _require(isinstance(row, dict) and set(row) == {"source_pdf", "reason"},
                 "daily_delivery_unavailable_source_invalid")
        name, reason = row["source_pdf"], row["reason"]
        _require(isinstance(name, str) and name and Path(name).name == name and "\\" not in name
                 and Path(name).suffix.lower() == ".pdf" and name not in seen
                 and isinstance(reason, str) and bool(re.fullmatch(r"[a-z][a-z0-9_]{0,79}", reason)),
                 "daily_delivery_unavailable_source_invalid")
        seen.add(name)
        result.append({"source_pdf": name, "reason": reason})
    return result


def _substantive(path: Path, root: Path) -> bool:
    try:
        value = _read(path, root).decode("utf-8")
    except (OSError, ValueError, UnicodeError):
        return False
    return sum(character.isalnum() for character in value) >= 120


def _allowed(path: str) -> bool:
    return (path in {*SOURCE_MARKERS, *GENERATED_MARKERS, "status.json", "source_figure_map.json", "source_image_map.json",
                     "source_excerpt_evidence.json"}
            or bool(re.fullmatch(r"assets/source_image_[A-Za-z0-9_.-]+\.(?:png|jpg|jpeg|webp|gif|bmp|tiff?)", path,
                                 re.IGNORECASE))
            or bool(re.fullmatch(r"figure_source_evidence/(?:pages/page_[0-9]{4,}\.png|"
                                 r"provider_images/[a-f0-9]{64}\.(?:png|jpg|jpeg|webp|gif|bmp|tiff?))", path)))


def _candidate_files(directory: Path, *, status: dict[str, Any]) -> list[str]:
    for name in ("source_image_map.json", "source_figure_map.json", "figure_source_evidence", "assets"):
        _require(not (directory / name).is_symlink(), "daily_delivery_figure_contract_invalid")
    names = [*SOURCE_MARKERS, "status.json", "source_figure_map.json", "source_image_map.json"]
    if not status.get("error"):
        if status.get("wechat_article") == "wechat_article.md":
            names.append("wechat_article.md")
        if status.get("xhs_generation_enabled") is True:
            names.append("note.md")
    names.extend(path.relative_to(directory).as_posix() for path in sorted(directory.glob("assets/source_image_*"))
                 if _allowed(path.relative_to(directory).as_posix()))
    names.extend(path.relative_to(directory).as_posix() for path in sorted((directory / "figure_source_evidence").rglob("*"))
                 if _allowed(path.relative_to(directory).as_posix()))
    return sorted(name for name in set(names) if _regular(directory / name, directory)
                  and (directory / name).stat().st_size > 0)


def _verify_candidate(candidate: dict[str, Any], binding: dict[str, Any]) -> tuple[Path, list[str]]:
    _require(isinstance(candidate, dict) and candidate.get("content_sha256") == binding["content_sha256"],
             "daily_delivery_candidate_source_mismatch")
    directory = Path(candidate["directory"])
    files = candidate.get("files")
    method = candidate.get("source_method")
    _require(isinstance(method, str) and bool(re.fullmatch(r"[a-z][a-z0-9_-]{0,39}", method)),
             "daily_delivery_source_method_invalid")
    _require(isinstance(files, list) and bool(files) and all(isinstance(name, str) and _allowed(name) for name in files)
             and len(files) == len(set(files)) and "status.json" in files,
             "daily_delivery_candidate_files_invalid")
    for name in files:
        _require(bool(_read(directory / name, directory)), "daily_delivery_empty_candidate_file")
    status = _json(directory / "status.json", directory)
    _require(isinstance(status, dict) and status.get("original_pdf_sha256") == binding["content_sha256"],
             "daily_delivery_candidate_hash_unbound")
    _require(any(name in files and _substantive(directory / name, directory) for name in SOURCE_MARKERS),
             "daily_delivery_candidate_content_missing")
    if status.get("error"):
        _require(not set(files).intersection(GENERATED_MARKERS), "daily_delivery_failed_article_included")
    if ("source_image_map.json" in files or "source_figure_map.json" in files
            or "source_figure_map" in status or "source_figure_map_sha256" in status
            or any(name.startswith("figure_source_evidence/") for name in files)):
        # These validators replay existing maps/pixel evidence only: no OCR,
        # provider requests, PDF parsing or model calls occur during admission.
        from build_market_views_pdf import source_image_mapping
        markdown = directory / "source_mineru.md"
        try:
            mapping = source_image_mapping(markdown)
            if ("source_figure_map.json" in files or "source_figure_map" in status
                    or "source_figure_map_sha256" in status
                    or any(name.startswith("figure_source_evidence/") for name in files)):
                from mineru_figure_sources import validate_figure_sources
                validated = validate_figure_sources(directory,
                    expected_original_sha256=binding["content_sha256"],
                    expected_markdown_sha256=_digest(_read(markdown, directory)), expected_images=status.get("images"))
                _require(validated is not None and mapping is not None
                         and set(validated.values()) == set(mapping.values())
                         and all(mapping.get(ref) == target for ref, target in validated.items()),
                         "daily_delivery_figure_contract_invalid")
        except (OSError, ValueError, RuntimeError, TypeError, KeyError) as error:
            raise ValueError("daily_delivery_figure_contract_invalid") from error
    if method == "source-digest":
        _require("source_excerpt_evidence.json" in files, "daily_delivery_source_evidence_missing")
        evidence = _json(directory / "source_excerpt_evidence.json", directory)
        _require(isinstance(evidence, dict) and evidence.get("source_pdf") == binding["source_pdf"]
                 and evidence.get("content_sha256") == binding["content_sha256"],
                 "daily_delivery_source_evidence_mismatch")
    return directory, files


def write_delivery_receipt(manifest: Path, destination: Path, candidates: dict[str, dict[str, Any]], *,
                           date_folder: str, source_run_id: str, source_execution_sha: str,
                           omission_reasons: dict[str, str] | None = None,
                           allow_empty: bool = False, unavailable_originals: list[dict[str, str]] | None = None,
                           shard_index: int | None = None, reports_per_shard: int | None = None) -> dict[str, Any]:
    """Copy an authenticated candidate map and issue a complete coverage ledger.

    Callers adding fallback candidates must verify their original PDF bytes first;
    the candidate status binds those bytes via ``original_pdf_sha256``. Candidate
    files are re-read here and every byte is checked again by ``verify_delivery``.
    """
    _identity(date_folder, source_run_id, source_execution_sha)
    raw, rows = read_selection(manifest)
    unavailable = _unavailable(rows, [] if unavailable_originals is None else unavailable_originals)
    _require(isinstance(candidates, dict) and set(candidates).issubset({row["source_pdf"] for row in rows}),
             "daily_delivery_unselected_candidate")
    _require(bool(candidates) or allow_empty, "daily_delivery_no_usable_reports")
    destination = Path(destination)
    _require(not destination.is_symlink(), "daily_delivery_destination_symlink")
    destination.parent.mkdir(parents=True, exist_ok=True)
    omissions = omission_reasons or {}
    with tempfile.TemporaryDirectory(prefix="daily-delivery-", dir=destination.parent) as temporary:
        stage = Path(temporary) / "bundle"
        stage.mkdir()
        (stage / MANIFEST_NAME).write_bytes(raw)
        reports = []
        for index, row in enumerate(rows, 1):
            name = row["source_pdf"]
            record = {"source_pdf": name, "content_sha256": row["content_sha256"], "status": "skipped",
                      "reason": omissions.get(name, "source_not_ready"), "report_id": "", "source_method": ""}
            if name in candidates:
                candidate = candidates[name]
                directory, files = _verify_candidate(candidate, row)
                report_id = f"report_{index:04d}_{row['content_sha256'][:12]}"
                target = stage / report_id
                target.mkdir()
                for relative in files:
                    path = target / relative
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_bytes(_read(directory / relative, directory))
                record.update(status="included", reason="", report_id=report_id,
                              source_method=candidate["source_method"])
            _require(isinstance(record["reason"], str)
                     and (not record["reason"] or re.fullmatch(r"[a-z][a-z0-9_]{0,79}", record["reason"])),
                     "daily_delivery_omission_reason_invalid")
            reports.append(record)
        files = []
        for path in sorted(stage.rglob("*")):
            if path.is_file():
                data = _read(path, stage)
                files.append({"path": path.relative_to(stage).as_posix(), "bytes": len(data), "sha256": _digest(data)})
        included = len(candidates)
        receipt = {"schema_version": 1, "source_kind": "daily-digest", "date_folder": date_folder,
                   "source_run_id": source_run_id, "source_execution_sha": source_execution_sha,
                   "expected_reports": len(rows), "included_reports": included,
                   "skipped_reports": len(rows) - included, "manifest_sha256": _digest(raw),
                   "expected_source_reports": len(rows) + len(unavailable), "unavailable_originals": unavailable,
                   "source_inventory_sha256": _inventory_digest(rows),
                   "complete_source_inventory": included == len(rows) and not unavailable, "reports": reports, "files": files}
        if shard_index is not None or reports_per_shard is not None:
            receipt.update(shard_index=shard_index, reports_per_shard=reports_per_shard)
        (stage / RECEIPT_NAME).write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        verify_delivery(stage, date_folder=date_folder, source_run_id=source_run_id,
                        source_execution_sha=source_execution_sha, manifest=manifest, allow_empty=allow_empty)
        if destination.exists():
            _require(destination.is_dir() and destination.resolve() not in {Path("/"), Path.cwd().resolve()},
                     "daily_delivery_destination_invalid")
            shutil.rmtree(destination)
        shutil.move(str(stage), destination)
    return receipt


def verify_delivery(directory: Path, *, date_folder: str, source_run_id: str,
                    source_execution_sha: str, manifest: Path | None = None,
                    allow_empty: bool = False) -> dict[str, Any]:
    directory = Path(directory)
    _identity(date_folder, source_run_id, source_execution_sha)
    receipt = _json(directory / RECEIPT_NAME, directory)
    _require(isinstance(receipt, dict) and type(receipt.get("schema_version")) is int
             and receipt["schema_version"] == 1 and receipt.get("source_kind") == "daily-digest",
             "daily_delivery_receipt_invalid")
    _require(receipt.get("date_folder") == date_folder and receipt.get("source_run_id") == source_run_id
             and receipt.get("source_execution_sha") == source_execution_sha, "daily_delivery_identity_mismatch")
    raw, rows = read_selection(directory / MANIFEST_NAME)
    _require(receipt.get("manifest_sha256") == _digest(raw)
             and receipt.get("source_inventory_sha256") == _inventory_digest(rows), "daily_delivery_manifest_mismatch")
    if manifest is not None:
        _require(_read(Path(manifest)) == raw, "daily_delivery_original_manifest_mismatch")
    expected, included, skipped = (receipt.get(key) for key in ("expected_reports", "included_reports", "skipped_reports"))
    _require(all(type(value) is int for value in (expected, included, skipped)) and expected == len(rows)
             and included >= 0 and skipped >= 0 and included + skipped == expected,
             "daily_delivery_counts_invalid")
    _require(included > 0 or allow_empty, "daily_delivery_no_usable_reports")
    unavailable = _unavailable(rows, receipt.get("unavailable_originals", []))
    _require(type(receipt.get("expected_source_reports", expected)) is int
             and receipt.get("expected_source_reports", expected) == expected + len(unavailable),
             "daily_delivery_unavailable_count_mismatch")
    _require(receipt.get("complete_source_inventory") is (skipped == 0 and not unavailable), "daily_delivery_completion_invalid")
    reports = receipt.get("reports")
    _require(isinstance(reports, list) and len(reports) == expected, "daily_delivery_coverage_incomplete")
    checked: dict[str, bytes] = {}
    inventory = receipt.get("files")
    _require(isinstance(inventory, list) and bool(inventory), "daily_delivery_file_inventory_missing")
    for record in inventory:
        _require(isinstance(record, dict) and isinstance(record.get("path"), str), "daily_delivery_file_invalid")
        relative = PurePosixPath(record["path"])
        _require(relative.parts and not relative.is_absolute() and ".." not in relative.parts
                 and "\\" not in record["path"] and relative.as_posix() == record["path"]
                 and record["path"] not in checked and record["path"] != RECEIPT_NAME,
                 "daily_delivery_file_path_invalid")
        data = _read(directory / relative, directory)
        _require(type(record.get("bytes")) is int and record["bytes"] > 0 and len(data) == record["bytes"]
                 and _digest(data) == record.get("sha256"), "daily_delivery_file_hash_mismatch")
        checked[record["path"]] = data
    actual = set()
    for path in directory.rglob("*"):
        _require(not path.is_symlink(), "daily_delivery_symlink")
        if path.is_file() and path != directory / RECEIPT_NAME:
            actual.add(path.relative_to(directory).as_posix())
    _require(set(checked) == actual and checked.get(MANIFEST_NAME) == raw, "daily_delivery_file_inventory_mismatch")
    included_count = 0
    admitted_files = {MANIFEST_NAME}
    for index, (record, row) in enumerate(zip(reports, rows), 1):
        _require(isinstance(record, dict) and record.get("source_pdf") == row["source_pdf"]
                 and record.get("content_sha256") == row["content_sha256"], "daily_delivery_report_identity_mismatch")
        if record.get("status") == "included":
            included_count += 1
            report_id = f"report_{index:04d}_{row['content_sha256'][:12]}"
            _require(record.get("report_id") == report_id and record.get("reason") == "",
                     "daily_delivery_report_directory_invalid")
            files = [name[len(report_id) + 1:] for name in checked if name.startswith(report_id + "/")]
            candidate = {"directory": directory / report_id, "content_sha256": row["content_sha256"],
                         "source_method": record.get("source_method"), "files": files}
            _verify_candidate(candidate, row)
            admitted_files.update(report_id + "/" + name for name in files)
        else:
            _require(record.get("status") == "skipped" and record.get("report_id") == ""
                     and record.get("source_method") == "" and isinstance(record.get("reason"), str)
                     and bool(re.fullmatch(r"[a-z][a-z0-9_]{0,79}", record["reason"])),
                     "daily_delivery_skipped_report_invalid")
    _require(included_count == included and admitted_files == set(checked), "daily_delivery_report_inventory_mismatch")
    if "shard_index" in receipt or "reports_per_shard" in receipt:
        index, size = receipt.get("shard_index"), receipt.get("reports_per_shard")
        _require(type(index) is int and index >= 0 and type(size) is int and size > 0,
                 "daily_delivery_shard_invalid")
        selected = {row["source_pdf"] for row in rows[index * size:(index + 1) * size]}
        _require(bool(selected) and all(row["source_pdf"] in selected for row in reports if row["status"] == "included"),
                 "daily_delivery_wrong_shard_source")
    return receipt


def _checkpoint_trusted(directory: Path, identity: str | None) -> bool:
    if not identity or not SHA256.fullmatch(identity):
        return False
    try:
        metadata = _json(directory / "_generation_checkpoint.json", directory)
        return isinstance(metadata, dict) and metadata.get("version") == 1 and metadata.get("identity") == identity
    except (OSError, ValueError):
        return False


def _source_candidates(manifest: Path, directory: Path, stage: Path, *, shard_index: int,
                       reports_per_shard: int, originals_dir: Path | None = None,
                       checkpoint_identity: str | None = None, trusted_legacy: bool = False
                       ) -> tuple[dict[str, dict[str, Any]], dict[str, str]]:
    from run_pdf_to_xhs_in_batches import unique_batch_name, slug
    _raw, rows = read_selection(manifest)
    _require(not directory.is_symlink(), "daily_delivery_shard_symlink")
    _require(type(shard_index) is int and shard_index >= 0 and type(reports_per_shard) is int
             and reports_per_shard > 0, "daily_delivery_shard_invalid")
    selected = rows[shard_index * reports_per_shard:(shard_index + 1) * reports_per_shard]
    _require(bool(selected), "daily_delivery_empty_selection_shard")
    checkpoint = _checkpoint_trusted(directory, checkpoint_identity)
    candidates: dict[str, dict[str, Any]] = {}
    reasons = {}
    for ordinal, row in enumerate(selected, 1):
        name = row["source_pdf"]
        reasons[name] = "source_not_ready"
        expected_name = unique_batch_name(Path(row["process_local_path"]), ordinal)
        report = directory / slug(expected_name)
        try:
            status = _json(report / "status.json", report)
            _require(isinstance(status, dict) and Path(str(status.get("source_pdf") or "")).name == expected_name,
                     "source_identity_mismatch")
            _require(str(status.get("mineru_state") or "").lower() in DONE_STATES,
                     "source_extraction_not_completed")
            _require(_substantive(report / "source_mineru.md", report), "source_content_not_ready")
            if originals_dir is not None:
                original = Path(originals_dir) / name
                _require(_digest(_read(original, Path(originals_dir))) == row["content_sha256"],
                         "original_source_hash_mismatch")
            else:
                _require(checkpoint or trusted_legacy, "source_checkpoint_not_verified")
            if status.get("original_pdf_sha256"):
                _require(status["original_pdf_sha256"] == row["content_sha256"], "source_identity_mismatch")
            target = stage / name.removesuffix(".pdf")
            target.mkdir(parents=True, exist_ok=True)
            files = _candidate_files(report, status=status)
            for relative in files:
                path = target / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(_read(report / relative, report))
            status["original_pdf_sha256"] = row["content_sha256"]
            (target / "status.json").write_text(json.dumps(status, ensure_ascii=False) + "\n", encoding="utf-8")
            candidate = {"directory": target, "content_sha256": row["content_sha256"],
                         "source_method": "mineru", "files": files}
            _verify_candidate(candidate, row)
            candidates[name] = candidate
            reasons.pop(name)
        except (OSError, ValueError, KeyError):
            reasons[name] = "source_not_verified"
    return candidates, reasons


def prepare_shard(manifest: Path, directory: Path, destination: Path, *, date_folder: str,
                  source_run_id: str, source_execution_sha: str, shard_index: int,
                  reports_per_shard: int, originals_dir: Path | None = None,
                  checkpoint_identity: str | None = None) -> dict[str, Any]:
    """Admit a shard after exact checkpoint restore, including failed generation."""
    with tempfile.TemporaryDirectory(prefix="daily-source-candidates-") as temporary:
        candidates, reasons = _source_candidates(manifest, directory, Path(temporary), shard_index=shard_index,
            reports_per_shard=reports_per_shard, originals_dir=originals_dir, checkpoint_identity=checkpoint_identity)
        return write_delivery_receipt(manifest, destination, candidates, date_folder=date_folder,
            source_run_id=source_run_id, source_execution_sha=source_execution_sha,
            omission_reasons=reasons, allow_empty=True, shard_index=shard_index, reports_per_shard=reports_per_shard)


def collect_candidates(manifest: Path, directory: Path, *, date_folder: str, source_run_id: str,
                       source_execution_sha: str, reports_per_shard: int | None = None,
                       allow_legacy: bool = False, candidate_staging: Path | None = None
                       ) -> tuple[dict[str, dict[str, Any]], dict[str, str]]:
    """Merge valid shard receipts; missing or failed shards become omissions.

    ``allow_legacy`` is only for a caller that authenticated the exact main-run
    producer and downloaded its run-scoped xhs handoffs. Every legacy shard must
    also carry the byte-identical selected manifest; names alone never admit it.
    """
    _identity(date_folder, source_run_id, source_execution_sha)
    _require(reports_per_shard is None or type(reports_per_shard) is int and reports_per_shard > 0,
             "daily_delivery_shard_size_invalid")
    raw, rows = read_selection(manifest)
    candidates: dict[str, dict[str, Any]] = {}
    reasons = {row["source_pdf"]: "shard_unavailable" for row in rows}
    directory = Path(directory)
    stage = Path(candidate_staging) if candidate_staging else directory / "_daily_candidate_staging"
    for shard in sorted(directory.glob("shard_*")):
        match = re.fullmatch(r"shard_([0-9]+)", shard.name)
        if not match or shard.is_symlink() or not shard.is_dir():
            continue
        index = int(match.group(1))
        expected_names = set()
        try:
            if (shard / RECEIPT_NAME).exists():
                receipt = verify_delivery(shard, date_folder=date_folder, source_run_id=source_run_id,
                    source_execution_sha=source_execution_sha, manifest=manifest, allow_empty=True)
                size = receipt.get("reports_per_shard")
                _require(receipt.get("shard_index") == index and type(size) is int and size > 0
                         and (reports_per_shard is None or reports_per_shard == size),
                         "daily_delivery_shard_identity_mismatch")
                expected_names = {row["source_pdf"] for row in rows[index * size:(index + 1) * size]}
                for row in receipt["reports"]:
                    if row["status"] != "included":
                        continue
                    _require(row["source_pdf"] in expected_names, "daily_delivery_wrong_shard_source")
                    _require(row["source_pdf"] not in candidates, "daily_delivery_duplicate_shard_source")
                    report_id = row["report_id"]
                    candidates[row["source_pdf"]] = {
                        "directory": shard / report_id, "content_sha256": row["content_sha256"],
                        "source_method": row["source_method"],
                        "files": [item["path"][len(report_id) + 1:] for item in receipt["files"]
                                  if item["path"].startswith(report_id + "/")]}
                    reasons.pop(row["source_pdf"], None)
            elif allow_legacy and reports_per_shard is not None:
                expected_names = {row["source_pdf"] for row in rows[index * reports_per_shard:(index + 1) * reports_per_shard]}
                if not expected_names:
                    continue
                _require(_read(shard / MANIFEST_NAME, shard) == raw, "daily_delivery_legacy_manifest_mismatch")
                found, skipped = _source_candidates(manifest, shard, stage / shard.name, shard_index=index,
                    reports_per_shard=reports_per_shard, trusted_legacy=True)
                candidates.update(found)
                reasons.update(skipped)
                for name in found:
                    reasons.pop(name, None)
        except (OSError, ValueError, KeyError):
            # Do not admit even an early row from a shard that later failed.
            for name in expected_names:
                candidates.pop(name, None)
                reasons[name] = "shard_not_verified"
    return candidates, reasons


def assemble_sources(manifest: Path, directory: Path, destination: Path, *, date_folder: str,
                     source_run_id: str, source_execution_sha: str, reports_per_shard: int | None = None,
                     allow_legacy: bool = False) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="daily-assembly-candidates-") as temporary:
        candidates, reasons = collect_candidates(manifest, directory, date_folder=date_folder,
            source_run_id=source_run_id, source_execution_sha=source_execution_sha,
            reports_per_shard=reports_per_shard, allow_legacy=allow_legacy, candidate_staging=Path(temporary))
        return write_delivery_receipt(manifest, destination, candidates, date_folder=date_folder,
            source_run_id=source_run_id, source_execution_sha=source_execution_sha, omission_reasons=reasons)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("prepare", "assemble", "verify"))
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--directory", required=True, type=Path)
    parser.add_argument("--destination", type=Path)
    parser.add_argument("--date-folder", required=True)
    parser.add_argument("--source-run-id", "--run-id", dest="source_run_id", required=True)
    parser.add_argument("--source-execution-sha", "--execution-sha", dest="source_execution_sha", required=True)
    parser.add_argument("--shard-index", type=int, default=0)
    parser.add_argument("--reports-per-shard", type=int)
    parser.add_argument("--originals-dir", type=Path)
    parser.add_argument("--checkpoint-identity")
    parser.add_argument("--allow-legacy", action="store_true")
    parser.add_argument("--allow-empty", action="store_true")
    args = parser.parse_args()
    common = dict(date_folder=args.date_folder, source_run_id=args.source_run_id,
                  source_execution_sha=args.source_execution_sha)
    if args.command == "verify":
        receipt = verify_delivery(args.directory, manifest=args.manifest, allow_empty=args.allow_empty, **common)
    else:
        if args.manifest is None or args.destination is None:
            parser.error("prepare/assemble require --manifest and --destination")
        if args.command == "prepare":
            size = args.reports_per_shard or 5
            identity = args.checkpoint_identity
            if identity is None and args.originals_dir is None:
                from private_generation_checkpoint import input_identity
                options = json.loads(os.environ.get("GENERATION_OPTIONS_JSON", "{}"))
                identity = input_identity(args.manifest, args.shard_index, size,
                                          options, Path(__file__).resolve().parent.parent)
            receipt = prepare_shard(args.manifest, args.directory, args.destination,
                shard_index=args.shard_index, reports_per_shard=size,
                originals_dir=args.originals_dir, checkpoint_identity=identity, **common)
        else:
            receipt = assemble_sources(args.manifest, args.directory, args.destination,
                reports_per_shard=args.reports_per_shard, allow_legacy=args.allow_legacy, **common)
    print(json.dumps({key: receipt[key] for key in ("expected_reports", "included_reports", "skipped_reports",
                                                  "manifest_sha256", "source_inventory_sha256")}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
