#!/usr/bin/env python3
"""Bounded, source-bound OCR continuation after a proved MinerU-only failure."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time

from report_extraction_source import digest, ocr_markdown_from_pages, resolve_extraction_source

RECEIPT = "ocr_extraction_receipt.json"


def encoded(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=True).encode()


def require(condition, category):
    if not condition:
        raise ValueError(category)


def verify_pdf(pdf: Path, binding):
    require(pdf.is_file() and not pdf.is_symlink(), "institution_ocr_original_missing")
    raw = pdf.read_bytes()
    require(raw.startswith(b"%PDF-") and len(raw) == binding["size"]
            and digest(raw) == binding["sha256"], "institution_ocr_original_changed")


def existing_source(directory: Path, filename: str, binding) -> bool:
    require(not directory.is_symlink(), "institution_ocr_output_symlink")
    if not any((directory / name).exists() or (directory / name).is_symlink()
               for name in ("source_mineru.md", "source_ocr.md")):
        return False
    source = resolve_extraction_source(directory)
    status = json.loads((directory / "status.json").read_bytes())
    require(not status.get("error") and status.get("source_pdf") == filename
            and status.get("original_pdf_sha256") == binding["sha256"],
            "institution_ocr_existing_source_mismatch")
    if source.method == "ocr":
        receipt = directory / RECEIPT
        require(receipt.is_file() and not receipt.is_symlink(), "institution_ocr_receipt_missing")
        raw = receipt.read_bytes()
        value = json.loads(raw)
        pages_raw = (directory / "source_ocr_pages.json").read_bytes()
        require(digest(raw) == status["wechat_source_provenance"]["source_receipt_sha256"]
                and value == {"schema": 1, "source": binding, "source_pdf": filename,
                    "fallback_category": "mineru_unavailable", "page_count": len(json.loads(pages_raw)),
                    "source_pages_sha256": digest(pages_raw), "source_markdown_sha256": source.sha256,
                    "languages": "eng+chi_sim", "dpi": 220}
                and status["wechat_source_provenance"]["content_sha256"] == binding["sha256"],
                "institution_ocr_receipt_mismatch")
    return True


def extract_source(pdf: Path, directory: Path, binding, *, reader=None):
    """Write page evidence and explicit OCR provenance, never source_mineru.md."""
    verify_pdf(pdf, binding)
    if existing_source(directory, pdf.name, binding):
        return
    if reader is None:
        from build_market_views_ocr_fallback import extract_pages
        reader = extract_pages
    pages = reader(pdf, languages="eng+chi_sim", dpi=220)
    markdown = ocr_markdown_from_pages(pages, len(pages))
    raw_pages = encoded(pages)
    verify_pdf(pdf, binding)
    receipt = encoded({"schema": 1, "source": binding, "source_pdf": pdf.name,
        "fallback_category": "mineru_unavailable", "page_count": len(pages),
        "source_pages_sha256": digest(raw_pages), "source_markdown_sha256": digest(markdown),
        "languages": "eng+chi_sim", "dpi": 220})
    status = {
        "source_pdf": pdf.name, "source_original_filename": binding["source"],
        "source_method": "ocr", "source_markdown": "source_ocr.md",
        "original_pdf_sha256": binding["sha256"], "chart_source_only": True,
        "chart_source_image_count": 0, "images": [],
        "ocr_fallback_reason": "mineru_unavailable", "ocr_page_count": len(pages),
        "wechat_source_provenance": {"source_kind": "ocr-pages", "source_pdf": pdf.name,
            "content_sha256": binding["sha256"], "source_receipt_sha256": digest(receipt),
            "source_report_id": "ocr-" + digest(encoded(binding)),
            "source_pages_sha256": digest(raw_pages)},
    }
    require(not directory.is_symlink(), "institution_ocr_output_symlink")
    directory.mkdir(parents=True, exist_ok=True)
    outputs = {"source_ocr_pages.json": raw_pages, RECEIPT: receipt,
               "status.json": encoded(status), "source_ocr.md": markdown}
    for name in outputs:
        require(not (directory / name).is_symlink(), "institution_ocr_output_symlink")
    # Validate in isolation before exposing source markers to downstream discovery.
    with tempfile.TemporaryDirectory(prefix=".institution-ocr-", dir=directory.parent) as temporary:
        stage = Path(temporary)
        for name, raw in outputs.items():
            (stage / name).write_bytes(raw)
        resolve_extraction_source(stage)
        for name in outputs:
            (stage / name).replace(directory / name)
    resolve_extraction_source(directory)


def recover_batch(inventory, bindings, tmp_input: Path, output: Path, *, runner=None, timeout=600, deadline=None):
    """Consume only the child's current eligible inventory; never infer eligibility."""
    require(isinstance(inventory, dict) and set(inventory) == {"schema", "sources", "deferred_sources"}
            and type(inventory["schema"]) is int and inventory["schema"] == 1
            and isinstance(inventory["sources"], list) and 0 < len(inventory["sources"]) <= 5
            and type(inventory["deferred_sources"]) is int
            and 0 <= inventory["deferred_sources"] <= len(bindings), "institution_ocr_inventory_invalid")
    from run_pdf_to_xhs_in_batches import slug
    plans, seen, destinations = [], set(), set()
    for binding in inventory["sources"]:
        require(isinstance(binding, dict) and set(binding) == {"source", "size", "sha256"}
                and isinstance(binding["source"], str) and type(binding["size"]) is int
                and binding["size"] > 0 and isinstance(binding["sha256"], str),
                "institution_ocr_binding_invalid")
        names = [name for name, expected in bindings.items() if expected == binding]
        require(len(names) == 1 and names[0] not in seen, "institution_ocr_inventory_mismatch")
        name = names[0]
        require(Path(name).name == name and name.endswith(".pdf"), "institution_ocr_filename_invalid")
        seen.add(name)
        directory = output / slug(name)
        require(directory not in destinations, "institution_ocr_output_collision")
        destinations.add(directory)
        pdf = tmp_input / name
        verify_pdf(pdf, binding)
        reused = existing_source(directory, name, binding)
        plans.append((pdf, directory, binding, reused))
    require(len(plans) + inventory["deferred_sources"] == len(bindings),
            "institution_ocr_selection_incomplete")
    completed, reused_count, failures = 0, 0, []
    runner = runner or subprocess.run
    for pdf, directory, binding, reused in plans:
        if reused:
            reused_count += 1
            continue
        remaining = timeout if deadline is None else min(timeout, deadline - time.monotonic())
        if remaining <= 0:
            failures.append({"source_sha256": binding["sha256"], "category": "ocr_time_budget_exhausted"})
            continue
        with tempfile.TemporaryDirectory(prefix="institution-ocr-request-") as temporary:
            request = Path(temporary) / "request.json"
            request.write_bytes(encoded({"pdf": str(pdf), "output": str(directory), "binding": binding}))
            try:
                result = runner([sys.executable, str(Path(__file__).resolve()), "--request", str(request)],
                                timeout=remaining, capture_output=True, text=True)
            except subprocess.TimeoutExpired:
                failures.append({"source_sha256": binding["sha256"], "category": "ocr_timeout"})
                continue
            if result.returncode != 0:
                failures.append({"source_sha256": binding["sha256"], "category": "ocr_extraction_failed"})
                continue
        if not existing_source(directory, pdf.name, binding):
            failures.append({"source_sha256": binding["sha256"], "category": "ocr_output_missing"})
            continue
        completed += 1
    return {"ocr_reports": completed, "reused_reports": reused_count,
            "deferred_sources": inventory["deferred_sources"], "failed_reports": len(failures),
            "failures": failures}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", type=Path, required=True)
    args = parser.parse_args()
    value = json.loads(args.request.read_bytes())
    extract_source(Path(value["pdf"]), Path(value["output"]), value["binding"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
