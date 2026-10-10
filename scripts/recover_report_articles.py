#!/usr/bin/env python3
"""Resume complete WeChat articles from authenticated recovered extraction bytes.

This stage has no MinerU submission or result-download path. Its output directory
is the resumable private checkpoint and becomes deliverable only after validation.
"""
from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
import traceback

import pdf_to_xhs_batch as producer
from wechat_editorial_binding import FIELD, read_bound_article
from wechat_article_quality import audit_wechat_article_markdown

RECEIPT = "article_recovery_receipt.json"
PROVENANCE = "source_provenance.json"
POLICY = "verified-source-article-recovery-v1"
KINDS = {"mineru-recovery", "ocr-synthesis", "ocr-pages"}
SHA = re.compile(r"[a-f0-9]{64}")
MAX_FILE_BYTES = 128 * 1024 * 1024
MAX_FILES = 30000


class ArticleRecoveryError(ValueError):
    def __init__(self, category, source_ordinal=None):
        self.category, self.source_ordinal = category, source_ordinal
        super().__init__(category)


def require(condition, category):
    if not condition:
        raise ArticleRecoveryError(category)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def encoded(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=True, separators=(",", ":")).encode()


def read_json(path):
    require(path.is_file() and not path.is_symlink() and path.stat().st_size <= MAX_FILE_BYTES,
            "invalid_json_file")
    return json.loads(path.read_bytes())


def write_json(path, value):
    require(not path.is_symlink(), "output_symlink")
    temporary = path.with_name("." + path.name + ".tmp")
    require(not temporary.is_symlink(), "output_symlink")
    temporary.write_bytes(encoded(value) + b"\n")
    temporary.replace(path)


def inventory(root, *, exclude=()):
    require(root.is_dir() and not root.is_symlink(), "invalid_directory")
    rows = []
    for path in sorted(root.rglob("*")):
        require(not path.is_symlink(), "tree_symlink")
        if path.is_dir():
            continue
        relative = path.relative_to(root).as_posix()
        require(path.is_file() and path.stat().st_size <= MAX_FILE_BYTES, "invalid_tree_file")
        if relative in exclude:
            continue
        data = path.read_bytes()
        rows.append({"path": relative, "bytes": len(data), "sha256": digest(data)})
        require(len(rows) <= MAX_FILES, "tree_file_count")
    return rows


def checked_context(expected_reports, date_folder):
    require(type(expected_reports) is int and 1 <= expected_reports <= 1000, "invalid_expected_reports")
    require(isinstance(date_folder, str) and re.fullmatch(r"(?:[0-9]{6}|[0-9]{8})", date_folder), "invalid_date")
    datetime.strptime(date_folder, "%y%m%d" if len(date_folder) == 6 else "%Y%m%d")


def _ocr_source(pages, page_count):
    from report_extraction_source import ocr_markdown_from_pages
    try:
        return ocr_markdown_from_pages(pages, page_count)
    except ValueError:
        raise ArticleRecoveryError("ocr_page_evidence") from None


def load_sources(source_dir, source_kind, expected_reports, date_folder, *, source_run_id=None,
                 source_execution_sha=None, source_handoff_run_id=None, source_handoff_execution_sha=None):
    """Validate the entire source batch before any paid generation occurs."""
    checked_context(expected_reports, date_folder)
    require(source_kind in KINDS, "invalid_source_kind")
    root = Path(source_dir)
    inventory(root)
    manifest_path = root / "selected_to_process_manifest.json"
    plans = []
    if source_kind == "mineru-recovery":
        from recover_durable_mineru_sources import RECEIPT as SOURCE_RECEIPT, validate_sources
        receipt = validate_sources(root, expected_reports, date_folder,
            expected_recovery_run_id=source_handoff_run_id, expected_execution_sha=source_handoff_execution_sha)
        require(source_run_id is None or receipt["source_run_id"] == source_run_id, "source_original_run")
        require(source_execution_sha is None or receipt["source_execution_sha"] == source_execution_sha, "source_original_sha")
        source_run_id, source_execution_sha = receipt["source_run_id"], receipt["source_execution_sha"]
        source_handoff_run_id, source_handoff_execution_sha = receipt["recovery_run_id"], receipt["recovery_execution_sha"]
        raw = (root / SOURCE_RECEIPT).read_bytes()
        for ordinal, report in enumerate(receipt["reports"], 1):
            binding = report["binding"]
            directory = root / report["directory"]
            plans.append({"directory": report["directory"], "source_pdf": binding["source_pdf"],
                "original_filename": binding["original_filename"], "content_sha256": binding["content_sha256"],
                "source_report_id": report["source_id"], "source_markdown": "source_mineru.md",
                "source_bytes": (directory / "source_mineru.md").read_bytes(),
                "status": read_json(directory / "status.json"), "copy_root": directory,
                "source_status_json": (directory / "status.json").read_text()})
    else:
        from market_views_publication import RECEIPT_NAME as SOURCE_RECEIPT, validate_ocr_synthesis_receipt
        validator = validate_ocr_synthesis_receipt
        if source_kind == 'ocr-pages':
            from ocr_page_sources import RECEIPT as SOURCE_RECEIPT, validate_pages_receipt
            validator = validate_pages_receipt
        initial = read_json(root / SOURCE_RECEIPT)
        require(isinstance(initial, dict), "invalid_ocr_receipt")
        source_run_id = source_run_id or initial.get("source_run_id")
        source_execution_sha = source_execution_sha or initial.get("execution_sha")
        receipt = validator(root, date_folder=date_folder, expected_reports=expected_reports,
            source_run_id=source_run_id, execution_sha=source_execution_sha,
            recovery_run_id=source_handoff_run_id, recovery_execution_sha=source_handoff_execution_sha)
        source_handoff_run_id = source_handoff_run_id or source_run_id
        source_handoff_execution_sha = source_handoff_execution_sha or source_execution_sha
        if source_kind == 'ocr-synthesis':
            require(receipt["skipped_reports"] == 0 and receipt["summarized_reports"] == expected_reports,
                    "ocr_article_sources_incomplete")
        raw = (root / SOURCE_RECEIPT).read_bytes()
        from extract_native_market_sources import read_manifest
        _, bindings = read_manifest(manifest_path, expected_reports)
        reports = {row["source_pdf"]: row for row in receipt["reports"]}
        files = {row["path"] for row in receipt["files"]}
        figures = read_json(root / "figure_candidates.json") if source_kind == 'ocr-synthesis' else []
        for ordinal, binding in enumerate(bindings, 1):
            report = reports[binding["source_pdf"]]
            rid = report["id"]
            require(isinstance(rid, str) and re.fullmatch(r"R[0-9]{3,4}", rid), "ocr_report_id")
            relative = f"ocr_sources/{rid}/pages.json"
            require(relative in files, "ocr_unbound_page_text")
            pages_path = root / relative
            source = _ocr_source(read_json(pages_path), report["page_count"])
            own_figures = [row for row in figures if row["report_id"] == rid]
            plans.append({"directory": f"report_{ordinal:04d}_{binding['content_sha256'][:12]}",
                "source_pdf": binding["source_pdf"], "original_filename": binding.get("original_filename", binding["source_pdf"]),
                "content_sha256": binding["content_sha256"], "source_report_id": rid,
                "source_markdown": "source_ocr.md", "source_bytes": source, "status": {},
                "source_pages_sha256": digest(pages_path.read_bytes()), "pages_path": pages_path,
                "figures": [(root / row["latex_path"], row) for row in own_figures]})
    require(len(plans) == expected_reports and len({row["directory"] for row in plans}) == expected_reports
            and len({row["source_pdf"] for row in plans}) == expected_reports, "source_count")
    source_hash = digest(raw)
    for plan in plans:
        plan["provenance"] = {"source_kind": source_kind, "source_pdf": plan["source_pdf"],
            "content_sha256": plan["content_sha256"], "source_receipt_sha256": source_hash,
            "source_report_id": plan["source_report_id"]}
        if source_kind in {"ocr-synthesis", "ocr-pages"}:
            plan["provenance"]["source_pages_sha256"] = plan["source_pages_sha256"]
    from market_views_publication import source_inventory_sha256
    metadata = {"schema_version": 1, "source_kind": source_kind, "date_folder": date_folder,
        "expected_reports": expected_reports, "source_run_id": source_run_id,
        "source_execution_sha": source_execution_sha, "source_receipt_sha256": source_hash,
        "source_handoff_run_id": source_handoff_run_id, "source_handoff_execution_sha": source_handoff_execution_sha,
        "source_inventory_sha256": source_inventory_sha256(plans),
        "source_receipt_json": raw.decode("utf-8"), "manifest_sha256": digest(manifest_path.read_bytes()),
        "sources": [{"directory": row["directory"], "source_markdown": row["source_markdown"],
            "source_markdown_sha256": digest(row["source_bytes"]), "provenance": row["provenance"],
            **({"source_status_json": row["source_status_json"]} if "source_status_json" in row else {})} for row in plans]}
    if source_kind == "ocr-synthesis":
        metadata["source_figures_json"] = (root / "figure_candidates.json").read_text()
    return metadata, plans


def generation_contract(args):
    files = ("pdf_to_xhs_batch.py", "wechat_editorial_binding.py", "wechat_article_quality.py",
             "wechat_title_optimizer.py", "sensitive_content_guard.py", "institution_names.py")
    value = {"files": {name: digest((Path(__file__).parent / name).read_bytes()) for name in files},
        "prompt_sha256": digest(Path(args.wechat_prompt_template).read_bytes()),
        "options": {key: getattr(args, key) for key in
                    ("model", "deepseek_base_url", "wechat_length", "wechat_prompt_chars", "community_cta", "wechat_title_refine")}}
    return digest(encoded(value))


def sources_equivalent(previous, current):
    """New recovery bookkeeping cannot invalidate identical accepted source bytes.

    Keep the first complete package/receipt unchanged. Different provider lineage,
    segment evidence, originals, text or figure files never qualify for this reuse.
    """
    try:
        if previous == current:
            return True
        keys = ("source_kind", "date_folder", "expected_reports", "source_run_id", "source_execution_sha",
                "source_inventory_sha256", "manifest_sha256")
        if any(previous[key] != current[key] for key in keys) or current["source_kind"] != "mineru-recovery":
            return False
        receipts = []
        for value in (previous, current):
            raw = value["source_receipt_json"]
            if digest(raw.encode()) != value["source_receipt_sha256"]:
                return False
            receipt = json.loads(raw)
            receipts.append({key: item for key, item in receipt.items()
                             if key not in {"recovery_run_id", "recovery_execution_sha", "provider_posts"}})
        return receipts[0] == receipts[1]
    except (KeyError, TypeError, ValueError):
        return False


def usable_article(directory):
    bound = read_bound_article(directory)
    if bound is None:
        return None
    body = re.sub(r"(?m)^#{1,6}\s+.*$", "", bound.article)
    body = re.sub(r"!\[[^\]]*\]\([^)]*\)|<[^>]*>", "", body).strip()
    if (not body or re.search(r"(?:请复制.{0,80}prompt|DeepSeek.{0,100}(?:失败|failed)|Missing\s+DEEPSEEK_API_KEY)", body, re.I)
            or {"forbidden_meta_section", "model_cta"} & set(audit_wechat_article_markdown(bound.article))):
        return None
    return bound


def _stage_source(plan, directory):
    directory.mkdir(parents=True, exist_ok=True)
    if plan.get("copy_root"):
        for path in plan["copy_root"].rglob("*"):
            if path.is_file() and path.name != "status.json":
                target = directory / path.relative_to(plan["copy_root"])
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(path, target)
    (directory / plan["source_markdown"]).write_bytes(plan["source_bytes"])
    status = dict(plan["status"])
    if "pages_path" in plan:
        shutil.copyfile(plan["pages_path"], directory / "source_ocr_pages.json")
        images, provenance = [], []
        for number, (path, row) in enumerate(plan["figures"], 1):
            require(path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}, "ocr_figure_format")
            relative = f"assets/ocr_reconstructed_{number:02d}{path.suffix.lower()}"
            target = directory / relative
            target.parent.mkdir(exist_ok=True)
            shutil.copyfile(path, target)
            images.append(relative)
            provenance.append({"path": relative, "kind": "ocr_reconstructed_chart", "source_pages": row.get("source_pages", []),
                               "sha256": digest(target.read_bytes()), "source_figure_id": row.get("figure_id"),
                               "source_figure_path": row["latex_path"]})
        status.update(images=images, image_source_kind=("ocr_pages_text_only"
            if plan['provenance']['source_kind'] == 'ocr-pages' else "ocr_reconstructed_chart"), ocr_figures=provenance)
    status.update(source_pdf=plan["source_pdf"], original_filename=plan["original_filename"],
        original_pdf_sha256=plan["content_sha256"], source_markdown=plan["source_markdown"],
        source_method="ocr" if "pages_path" in plan else "mineru",
        wechat_source_provenance=plan["provenance"])
    return status


def validate_source_evidence(root, metadata):
    """Bind copied text and figures back to the authenticated producer receipt."""
    raw = metadata.get("source_receipt_json")
    require(isinstance(raw, str) and digest(raw.encode()) == metadata["source_receipt_sha256"],
            "source_receipt_bytes")
    receipt = json.loads(raw)
    source_files = {row["path"]: row for row in receipt["files"]}
    originals = receipt["reports"]
    sources = metadata["sources"]
    require(len(sources) == len(originals) == metadata["expected_reports"], "source_receipt_count")
    if metadata["source_kind"] == "mineru-recovery":
        require(receipt["date_folder"] == metadata["date_folder"] and receipt["source_run_id"] == metadata["source_run_id"]
                and receipt["source_execution_sha"] == metadata["source_execution_sha"]
                and receipt["recovery_run_id"] == metadata["source_handoff_run_id"]
                and receipt["recovery_execution_sha"] == metadata["source_handoff_execution_sha"], "source_receipt_identity")
        for source, original in zip(sources, originals):
            name = source["directory"]
            require(name == original["directory"] and re.fullmatch(r"report_[0-9]{4}_[a-f0-9]{12}", name),
                    "source_directory_binding")
            expected = {"source_kind": "mineru-recovery", "source_pdf": original["binding"]["source_pdf"],
                "content_sha256": original["binding"]["content_sha256"],
                "source_receipt_sha256": metadata["source_receipt_sha256"], "source_report_id": original["source_id"]}
            require(source["provenance"] == expected and source["source_markdown"] == "source_mineru.md"
                    and source["source_markdown_sha256"] == original["source_markdown_sha256"], "source_text_binding")
            original_status = source.get("source_status_json", "")
            require(digest(original_status.encode()) == source_files[name + "/status.json"]["sha256"], "source_status_binding")
            status = read_json(root / name / "status.json")
            require(status.get("images") == json.loads(original_status)["images"], "source_images_binding")
            for path, item in source_files.items():
                if path.startswith(name + "/") and path != name + "/status.json":
                    target = root / path
                    require(target.is_file() and target.stat().st_size == item["bytes"]
                            and digest(target.read_bytes()) == item["sha256"], "source_evidence_hash")
    else:
        pages_only = metadata['source_kind'] == 'ocr-pages'
        require(receipt.get('source_kind') == metadata['source_kind'] and receipt.get('complete') is True
                and receipt["date_folder"] == metadata["date_folder"] and receipt["source_run_id"] == metadata["source_run_id"]
                and receipt["execution_sha"] == metadata["source_execution_sha"]
                and receipt["selected_manifest_sha256"] == metadata["manifest_sha256"], "source_receipt_identity")
        if pages_only:
            from ocr_page_sources import POLICY as PAGES_POLICY, EXTRACTION, validate_pages_lineage
            require(receipt.get('policy') == PAGES_POLICY and receipt.get('extraction') == EXTRACTION
                    and receipt.get('expected_reports') == receipt.get('report_count') == metadata['expected_reports']
                    and 'source_figures_json' not in metadata,
                    'ocr_pages_article_contract_invalid')
            validate_pages_lineage(receipt, source_run_id=metadata['source_run_id'],
                source_execution_sha=metadata['source_execution_sha'], recovery_run_id=metadata['source_handoff_run_id'],
                recovery_execution_sha=metadata['source_handoff_execution_sha'], manifest_sha256=metadata['manifest_sha256'])
        else:
            require(receipt['skipped_reports'] == 0, 'source_receipt_identity')
        if not pages_only and ("cache_recovery" in receipt or metadata["source_run_id"] != metadata["source_handoff_run_id"]):
            from market_views_publication import validate_ocr_cache_recovery_lineage
            validate_ocr_cache_recovery_lineage(receipt, source_run_id=metadata["source_run_id"],
                source_execution_sha=metadata["source_execution_sha"], recovery_run_id=metadata["source_handoff_run_id"],
                recovery_execution_sha=metadata["source_handoff_execution_sha"], manifest_sha256=metadata["manifest_sha256"])
        elif not pages_only:
            require(metadata["source_execution_sha"] == metadata["source_handoff_execution_sha"],
                    "source_receipt_identity")
        figures = []
        if not pages_only:
            figure_raw = metadata.get("source_figures_json", "")
            require(digest(figure_raw.encode()) == source_files["figure_candidates.json"]["sha256"], "source_figures_binding")
            figures = json.loads(figure_raw)
        by_id = {row["id"]: row for row in originals}
        for source in sources:
            provenance = source["provenance"]
            rid = provenance["source_report_id"]
            original = by_id[rid]
            require(provenance == {"source_kind": metadata['source_kind'], "source_pdf": original["source_pdf"],
                "content_sha256": original["content_sha256"], "source_receipt_sha256": metadata["source_receipt_sha256"],
                "source_report_id": rid, "source_pages_sha256": source_files[f"ocr_sources/{rid}/pages.json"]["sha256"]},
                "ocr_source_binding")
            directory = root / source["directory"]
            pages = directory / "source_ocr_pages.json"
            require(digest(pages.read_bytes()) == provenance["source_pages_sha256"], "ocr_page_binding")
            text = _ocr_source(read_json(pages), original["page_count"])
            require(source["source_markdown"] == "source_ocr.md" and digest(text) == source["source_markdown_sha256"]
                    and (directory / "source_ocr.md").read_bytes() == text, "ocr_source_text_binding")
            status = read_json(directory / "status.json")
            expected_images, expected_proofs = [], []
            for number, figure in enumerate((row for row in figures if row["report_id"] == rid), 1):
                path = f"assets/ocr_reconstructed_{number:02d}{Path(figure['latex_path']).suffix.lower()}"
                data = (directory / path).read_bytes()
                require(digest(data) == source_files[figure["latex_path"]]["sha256"], "ocr_figure_hash")
                expected_images.append(path)
                expected_proofs.append({"path": path, "kind": "ocr_reconstructed_chart", "source_pages": figure.get("source_pages", []),
                    "sha256": digest(data), "source_figure_id": figure.get("figure_id"), "source_figure_path": figure["latex_path"]})
            require(status.get("images") == expected_images and status.get("ocr_figures") == expected_proofs
                    and status.get("image_source_kind") == ("ocr_pages_text_only" if pages_only else "ocr_reconstructed_chart"),
                    "ocr_figure_binding")


def validate_articles(output_dir, expected_reports, date_folder, *, source_kind=None, source_receipt_sha256=None):
    checked_context(expected_reports, date_folder)
    root = Path(output_dir)
    receipt = read_json(root / RECEIPT)
    keys = {"schema_version", "policy", "complete", "source_kind", "date_folder", "expected_reports", "report_count",
            "source_run_id", "source_execution_sha", "source_handoff_run_id", "source_handoff_execution_sha",
            "source_receipt_sha256", "source_inventory_sha256", "reports", "files"}
    require(isinstance(receipt, dict) and set(receipt) == keys and type(receipt["schema_version"]) is int
            and receipt["schema_version"] == 1 and receipt["policy"] == POLICY and receipt["complete"] is True
            and receipt["source_kind"] in KINDS and (source_kind is None or receipt["source_kind"] == source_kind)
            and receipt["date_folder"] == date_folder and type(receipt["expected_reports"]) is int
            and receipt["expected_reports"] == expected_reports and type(receipt["report_count"]) is int
            and receipt["report_count"] == expected_reports, "article_receipt_contract")
    require(source_receipt_sha256 is None or receipt["source_receipt_sha256"] == source_receipt_sha256,
            "article_source_receipt_mismatch")
    require(receipt["files"] == inventory(root, exclude=(RECEIPT,)), "article_file_inventory")
    source = read_json(root / PROVENANCE)
    require(isinstance(source, dict) and isinstance(source.get("sources"), list)
            and len(source["sources"]) == expected_reports, "article_source_provenance")
    require(all(isinstance(row, dict) and re.fullmatch(r"report_[0-9]{4}_[a-f0-9]{12}", str(row.get("directory")))
                for row in source["sources"]), "article_source_directory")
    for key in ("source_kind", "date_folder", "expected_reports", "source_run_id", "source_execution_sha",
                "source_handoff_run_id", "source_handoff_execution_sha", "source_receipt_sha256", "source_inventory_sha256"):
        require(source.get(key) == receipt[key], "article_provenance_mismatch")
    validate_source_evidence(root, source)
    require(isinstance(receipt["source_run_id"], str) and re.fullmatch(r"[1-9][0-9]*", receipt["source_run_id"])
            and re.fullmatch(r"[a-f0-9]{40}", str(receipt["source_execution_sha"]))
            and isinstance(receipt["source_handoff_run_id"], str) and re.fullmatch(r"[1-9][0-9]*", receipt["source_handoff_run_id"])
            and re.fullmatch(r"[a-f0-9]{40}", str(receipt["source_handoff_execution_sha"]))
            and all(SHA.fullmatch(str(receipt[key])) for key in ("source_receipt_sha256", "source_inventory_sha256")),
            "article_producer_identity")
    reports = receipt["reports"]
    require(isinstance(reports, list) and len(reports) == expected_reports
            and isinstance(source.get("sources"), list) and len(source["sources"]) == expected_reports,
            "article_report_count")
    directories = set()
    for ordinal, (row, original) in enumerate(zip(reports, source["sources"]), 1):
        try:
            require(isinstance(row, dict) and set(row) == {"directory", "source_pdf", "content_sha256", "source_markdown",
                "source_markdown_sha256", "article_sha256", "editorial_binding"}, "article_report_contract")
            name = row["directory"]
            require(isinstance(name, str) and re.fullmatch(r"report_[0-9]{4}_[a-f0-9]{12}", name)
                    and name not in directories and name == original["directory"], "article_report_directory")
            directories.add(name)
            directory = root / name
            status = read_json(directory / "status.json")
            bound = usable_article(directory)
            require(bound is not None and status.get("wechat_source_provenance") == original["provenance"]
                    and row["editorial_binding"] == bound.binding and row["article_sha256"] == bound.binding["article_sha256"]
                    and row["source_markdown_sha256"] == original["source_markdown_sha256"] == bound.binding["source_sha256"]
                    and row["source_markdown"] == original["source_markdown"] == bound.binding["source_markdown"]
                    and row["source_pdf"] == original["provenance"]["source_pdf"]
                    and row["content_sha256"] == original["provenance"]["content_sha256"], "article_binding")
        except ArticleRecoveryError as error:
            error.source_ordinal = ordinal
            raise
    require({p.name for p in root.iterdir() if p.is_dir()} == directories, "article_directory_inventory")
    from market_views_publication import source_inventory_sha256 as inventory_hash
    require(inventory_hash(reports) == receipt["source_inventory_sha256"], "article_source_inventory")
    return receipt


def recover_articles(source_dir, source_kind, output_dir, expected_reports, date_folder, args, *,
                     source_run_id=None, source_execution_sha=None, source_handoff_run_id=None,
                     source_handoff_execution_sha=None):
    source_dir, output = Path(source_dir), Path(output_dir)
    require(not output.resolve().is_relative_to(source_dir.resolve())
            and not source_dir.resolve().is_relative_to(output.resolve()), "overlapping_source_output")
    metadata, plans = load_sources(source_dir, source_kind, expected_reports, date_folder,
        source_run_id=source_run_id, source_execution_sha=source_execution_sha,
        source_handoff_run_id=source_handoff_run_id, source_handoff_execution_sha=source_handoff_execution_sha)
    contract = generation_contract(args)
    output.mkdir(parents=True, exist_ok=True)
    inventory(output)
    if (output / PROVENANCE).exists():
        previous = read_json(output / PROVENANCE)
        require(sources_equivalent(previous, metadata), "checkpoint_source_mismatch")
        metadata = previous
        for plan, source in zip(plans, metadata["sources"]):
            plan["provenance"] = source["provenance"]
    else:
        require(not list(output.iterdir()), "unbound_output_directory")
        write_json(output / PROVENANCE, metadata)
    expected_dirs = {row["directory"] for row in plans}
    require(all(path.name in expected_dirs or path.name in {PROVENANCE, RECEIPT}
                for path in output.iterdir()), "checkpoint_inventory")
    if (output / RECEIPT).exists():
        return validate_articles(output, expected_reports, date_folder, source_kind=source_kind,
                                 source_receipt_sha256=metadata["source_receipt_sha256"])
    (output / RECEIPT).unlink(missing_ok=True)
    reports = []
    for ordinal, plan in enumerate(plans, 1):
        directory = output / plan["directory"]
        context = {"policy": POLICY, "generation_contract_sha256": contract}
        try:
            existing = read_json(directory / "status.json") if (directory / "status.json").exists() else {}
            bound = usable_article(directory)
            if (bound is not None and existing.get("wechat_source_provenance") == plan["provenance"]
                    and bound.binding["source_sha256"] == digest(plan["source_bytes"])
                    and existing.get("article_recovery", {}).get("policy") == POLICY):
                status = existing
                print(f"RECOVERED_ARTICLE ordinal={ordinal} reused=true", flush=True)
            else:
                status = _stage_source(plan, directory)
                status["article_recovery"] = context
                producer.generate_wechat_article(directory, plan["original_filename"],
                    plan["source_bytes"].decode("utf-8"), args, status)
                write_json(directory / "status.json", status)
                bound = usable_article(directory)
                require(bound is not None, "generated_article_unbound")
                print(f"RECOVERED_ARTICLE ordinal={ordinal} reused=false", flush=True)
            reports.append({"directory": plan["directory"], "source_pdf": plan["source_pdf"],
                "content_sha256": plan["content_sha256"], "source_markdown": plan["source_markdown"],
                "source_markdown_sha256": digest(plan["source_bytes"]), "article_sha256": bound.binding["article_sha256"],
                "editorial_binding": bound.binding})
        except Exception as error:
            if isinstance(error, ArticleRecoveryError):
                error.source_ordinal = ordinal
                raise
            raise ArticleRecoveryError("article_generation_failed", ordinal) from error
    receipt = {key: metadata[key] for key in ("source_kind", "date_folder", "expected_reports", "source_run_id",
               "source_execution_sha", "source_handoff_run_id", "source_handoff_execution_sha",
               "source_receipt_sha256", "source_inventory_sha256")}
    receipt.update(schema_version=1, policy=POLICY, complete=True, report_count=len(reports), reports=reports,
                   files=inventory(output, exclude=(RECEIPT,)))
    write_json(output / RECEIPT, receipt)
    try:
        return validate_articles(output, expected_reports, date_folder, source_kind=source_kind,
                                 source_receipt_sha256=metadata["source_receipt_sha256"])
    except Exception:
        (output / RECEIPT).unlink(missing_ok=True)
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", required=True, type=Path)
    parser.add_argument("--source-kind", required=True, choices=sorted(KINDS))
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--expected-reports", required=True, type=int)
    parser.add_argument("--date-folder", required=True)
    parser.add_argument("--source-run-id")
    parser.add_argument("--source-execution-sha")
    parser.add_argument("--source-handoff-run-id")
    parser.add_argument("--source-handoff-execution-sha")
    parser.add_argument("--model", default=producer.build_arg_parser().get_default("model"))
    parser.add_argument("--deepseek-base-url", default=producer.build_arg_parser().get_default("deepseek_base_url"))
    parser.add_argument("--private-diagnostics", action="store_true",
                        help="Write exception tracebacks to stderr; use only with private log storage")
    options = parser.parse_args()
    args = producer.build_arg_parser().parse_args([])
    args.model, args.deepseek_base_url = options.model, options.deepseek_base_url
    args.wechat_prompt_template = str(Path(__file__).resolve().parents[1] / args.wechat_prompt_template)
    try:
        receipt = recover_articles(options.source_dir, options.source_kind, options.output_dir,
            options.expected_reports, options.date_folder, args, source_run_id=options.source_run_id,
            source_execution_sha=options.source_execution_sha, source_handoff_run_id=options.source_handoff_run_id,
            source_handoff_execution_sha=options.source_handoff_execution_sha)
    except Exception as error:
        if options.private_diagnostics:
            traceback.print_exc(file=sys.stderr)
        category = error.category if isinstance(error, ArticleRecoveryError) else "article_source_validation_failed"
        ordinal = getattr(error, "source_ordinal", None)
        suffix = f" source_ordinal={ordinal}" if type(ordinal) is int else ""
        print(f"Report article recovery stopped: {category}{suffix}", file=sys.stderr)
        return 2
    print(json.dumps({"complete": True, "report_count": receipt["report_count"],
                      "source_kind": receipt["source_kind"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
