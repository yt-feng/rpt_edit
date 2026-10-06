"""Bind synthesized editions to their complete attempted source inventory."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re

RECEIPT_NAME = "ocr_synthesis_receipt.json"
SHA256 = re.compile(r"[a-f0-9]{64}")
NORMAL_KINDS = {"xhs", "native-pdf", "mineru-recovery", "legacy-daily"}


def _require(condition, category):
    if not condition:
        raise ValueError(category)


def source_inventory_sha256(reports):
    """Hash every attempted original, including explicitly skipped reports."""
    _require(isinstance(reports, list) and reports, "empty_source_inventory")
    inventory = []
    for row in reports:
        _require(isinstance(row, dict), "invalid_source_inventory")
        name, digest = row.get("source_pdf"), row.get("content_sha256")
        _require(isinstance(name, str) and name.strip() and isinstance(digest, str)
                 and SHA256.fullmatch(digest), "invalid_source_inventory")
        inventory.append((name, digest))
    _require(len({name for name, _ in inventory}) == len(inventory), "duplicate_source_inventory")
    raw = json.dumps(sorted(inventory), ensure_ascii=False, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def validate_ocr_synthesis_receipt(root, *, date_folder, expected_reports, source_run_id, execution_sha):
    """Validate exact handoff identity, per-report outcomes and all output bytes.

    Complete means every selected original was attempted, with at least one
    actual summary. Skipped inputs remain in the inventory and PDF disclosure.
    """
    from upload_market_view_to_r2 import parse_issue_date
    root = Path(root)
    raw = (root / RECEIPT_NAME).read_bytes()
    value = json.loads(raw)
    date = parse_issue_date(str(date_folder))[1]
    _require(isinstance(value, dict) and type(value.get("schema_version")) is int and value["schema_version"] == 1
             and value.get("source_kind") == "ocr-synthesis" and value.get("complete") is True,
             "invalid_ocr_synthesis_receipt")
    _require(value.get("date_folder") == date
             and value.get("source_run_id") == str(source_run_id)
             and value.get("execution_sha") == execution_sha
             and re.fullmatch(r"[a-f0-9]{40}", str(execution_sha))
             and re.fullmatch(r"[1-9][0-9]*", str(source_run_id)), "ocr_producer_identity_mismatch")
    expected = value.get("expected_reports")
    summarized, skipped = value.get("summarized_reports"), value.get("skipped_reports")
    _require(type(expected_reports) is int and expected_reports > 0
             and type(expected) is int and expected == expected_reports
             and type(value.get("attempted_reports")) is int and value["attempted_reports"] == expected
             and type(summarized) is int and summarized > 0
             and type(skipped) is int and skipped >= 0 and summarized + skipped == expected
             and type(value.get("report_count")) is int and value["report_count"] == summarized,
             "incomplete_attempted_source_coverage")
    _require(SHA256.fullmatch(str(value.get("selected_manifest_sha256", ""))), "invalid_selected_manifest_hash")
    rows = value.get("reports")
    inventory_sha = source_inventory_sha256(rows)
    _require(len(rows) == expected, "source_inventory_count_mismatch")
    from extract_native_market_sources import read_manifest
    manifest_raw, manifest_rows = read_manifest(root / "selected_to_process_manifest.json", expected)
    _require(hashlib.sha256(manifest_raw).hexdigest() == value["selected_manifest_sha256"]
             and source_inventory_sha256(manifest_rows) == inventory_sha, "selected_manifest_identity_mismatch")
    successful = [row for row in rows if row.get("status") == "summarized"]
    failed = [row for row in rows if row.get("status") == "skipped"]
    _require(len(successful) == summarized and len(failed) == skipped, "source_outcome_count_mismatch")
    for row in successful:
        pages, chunks = row.get("page_count"), row.get("chunk_count")
        _require(type(pages) is int and pages > 0
                 and row.get("pages_covered") == list(range(1, pages + 1))
                 and type(chunks) is int and chunks > 0
                 and type(row.get("chunks_completed")) is int and row["chunks_completed"] == chunks,
                 "incomplete_summarized_report")
    for row in failed:
        _require(isinstance(row.get("reason"), str) and re.fullmatch(r"[a-z][a-z0-9_]{0,79}", row["reason"]),
                 "missing_skipped_report_reason")
    files = value.get("files")
    _require(isinstance(files, list) and files, "missing_synthesis_files")
    checked = {}
    for item in files:
        _require(isinstance(item, dict) and isinstance(item.get("path"), str), "invalid_synthesis_file")
        relative = Path(item["path"])
        _require(not relative.is_absolute() and ".." not in relative.parts and relative.parts
                 and item["path"] not in checked, "invalid_synthesis_path")
        path = root / relative
        _require(path.resolve().is_relative_to(root.resolve()) and not path.is_symlink()
                 and path.is_file(), "missing_synthesis_file")
        data = path.read_bytes()
        _require(type(item.get("bytes")) is int and item["bytes"] > 0 and len(data) == item["bytes"]
                 and hashlib.sha256(data).hexdigest() == item.get("sha256"), "synthesis_file_hash_mismatch")
        checked[item["path"]] = data
    required = {"report_inputs.json", "figure_candidates.json", "market_views_structured.json"}
    for row in successful:
        required.update(f"ocr_sources/{row.get('id')}/{name}.json" for name in ("pages", "chunks", "summaries"))
    _require(required.issubset(checked), "missing_synthesis_document")
    inputs = json.loads(checked["report_inputs.json"])
    figures = json.loads(checked["figure_candidates.json"])
    summary = json.loads(checked["market_views_structured.json"])
    successful_ids = {row.get("id") for row in successful}
    _require(len(successful_ids) == summarized and all(isinstance(rid, str) and rid for rid in successful_ids),
             "invalid_summarized_report_identity")
    _require(isinstance(inputs, list) and len(inputs) == summarized
             and {row.get("id") for row in inputs if isinstance(row, dict)} == successful_ids
             and all(isinstance(row.get("digest"), str) and row["digest"].strip() for row in inputs),
             "missing_summarized_report_content")
    _require(isinstance(figures, list) and figures and all(
        isinstance(figure, dict) and figure.get("report_id") in successful_ids
        and figure.get("latex_path") in checked for figure in figures), "missing_synthesis_chart_content")
    _require(isinstance(summary, dict) and isinstance(summary.get("bank_roundup"), dict)
             and isinstance(summary["bank_roundup"].get("sections"), list)
             and summary["bank_roundup"]["sections"],
             "missing_synthesized_sections")
    sections = summary["bank_roundup"]["sections"]
    if summary.get("synthesis_mode") == "cross-report-v1":
        _require(len(sections) <= 10 and all(isinstance(section, dict) for section in sections),
                 "invalid_cross_report_module_count")
        references = [rid for section in sections for rid in section.get("references", [])]
        _require(len(references) == len(successful_ids) and set(references) == successful_ids,
                 "incomplete_cross_report_source_coverage")
        limits = summary.get("publication_limits") or {}
        _require(limits.get("max_modules") == 10 and limits.get("max_pages") == 70,
                 "missing_cross_report_publication_limits")
        _require("cross_report_evidence.json" in checked, "missing_cross_report_evidence")
        page_counts = {row["id"]: row["page_count"] for row in successful}
        figure_ids = {figure.get("figure_id") for figure in figures}
        figure_sources = {figure.get("figure_id"): figure.get("report_id") for figure in figures}
        for section in sections:
            refs = set(section["references"])
            selected = section.get("figure_ids") or []
            _require(len(selected) <= 3 and set(selected).issubset(figure_ids)
                     and all(figure_sources[fid] in refs for fid in selected), "invalid_cross_report_figures")
            views = section.get("bank_views") or []
            _require(isinstance(views, list) and 1 <= len(views) <= 4, "missing_cross_report_views")
            covered = set()
            for view in views:
                _require(isinstance(view, dict) and isinstance(view.get("view"), str) and view["view"].strip()
                         and isinstance(view.get("report_ids"), list) and view["report_ids"]
                         and len(set(view["report_ids"])) == len(view["report_ids"])
                         and set(view["report_ids"]).issubset(refs),
                         "invalid_cross_report_view_source")
                sources = view.get("sources") or []
                _require(isinstance(sources, list) and sources, "missing_cross_report_view_evidence")
                for source in sources:
                    _require(isinstance(source, dict) and source.get("report_id") in refs,
                             "invalid_cross_report_evidence_source")
                    _require(isinstance(source.get("pages"), list) and source["pages"]
                             and all(type(page) is int and 1 <= page <= page_counts[source["report_id"]]
                                 for page in source.get("pages") or []), "invalid_cross_report_evidence_page")
                _require({source["report_id"] for source in sources} == set(view["report_ids"]),
                         "cross_report_attribution_mismatch")
                covered.update(view["report_ids"])
            _require(covered == refs, "incomplete_cross_report_content_coverage")
    else:
        _require(len(sections) == summarized, "missing_synthesized_sections")
    # An explicit disclosure is required even though a skipped report is allowed.
    if failed:
        serialized = json.dumps(summary, ensure_ascii=False)
        _require(all(row["source_pdf"] in serialized for row in failed), "missing_skipped_report_disclosure")
    return {**value, "source_inventory_sha256": inventory_sha,
            "source_receipt_sha256": hashlib.sha256(raw).hexdigest()}


def publication_plan(pdf_path, date_value, *, source_kind, force_rebuild=False,
                     acceptance_only=False, source_inventory=None, client=None, bucket=None):
    """Only reuse a readable matching edition; lower editions are rebuilt."""
    from market_views_source_preview import readable_pdf, degraded_pdf
    from upload_market_view_to_r2 import private_publication_complete
    _require(source_kind in NORMAL_KINDS | {"ocr-synthesis"}, "unsupported_publication_source_kind")
    edition = "ocr-synthesis" if source_kind == "ocr-synthesis" else "standard"
    if force_rebuild or acceptance_only:
        return {"should_build": True, "edition": edition, "reason": "explicit_rebuild"}
    path = Path(pdf_path)
    if not readable_pdf(path) or degraded_pdf(path):
        return {"should_build": True, "edition": edition, "reason": "missing_or_source_pages_pdf"}
    if edition == "ocr-synthesis" and not source_inventory:
        return {"should_build": True, "edition": edition, "reason": "unbound_source_inventory"}
    complete = private_publication_complete(
        date_value, expected_edition=edition, allow_edition_upgrade=True,
        expected_source_inventory_sha256=source_inventory, client=client, bucket=bucket)
    return {"should_build": not complete, "edition": edition,
            "reason": "verified_existing_edition" if complete else "edition_or_source_upgrade"}
