#!/usr/bin/env python3
"""Select test PDFs with at least N pages from a downloaded Dropbox folder."""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
from pathlib import Path
from typing import Any

import fitz


def log(message: str) -> None:
    print(message, flush=True)


def write_github_output(key: str, value: str) -> None:
    output_path = os.getenv("GITHUB_OUTPUT")
    if not output_path:
        return
    with open(output_path, "a", encoding="utf-8") as f:
        f.write(f"{key}={str(value).replace(chr(10), ' ')}\n")


def slug(value: str) -> str:
    value = Path(value).name
    value = re.sub(r"\.pdf$", "", value, flags=re.IGNORECASE)
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-._")
    return value[:120] or "report"


def page_count(pdf_path: Path) -> int:
    doc = fitz.open(pdf_path)
    try:
        return len(doc)
    finally:
        doc.close()


def load_manifest(input_dir: Path) -> dict[str, Any]:
    path = input_dir / "dropbox_manifest.json"
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def ordered_input_pdfs(input_dir: Path) -> list[Path]:
    selection_path = input_dir / "selected_to_process_manifest.json"
    if selection_path.exists():
        try:
            rows = json.loads(selection_path.read_text(encoding="utf-8"))
        except Exception:
            rows = []
        ordered: list[Path] = []
        if isinstance(rows, list):
            for row in rows:
                if not isinstance(row, dict):
                    continue
                raw_path = row.get("process_local_path")
                if not raw_path:
                    continue
                path = Path(str(raw_path))
                if not path.is_absolute():
                    path = input_dir / path
                if path.exists() and path.suffix.lower() == ".pdf":
                    ordered.append(path)
        if ordered:
            return ordered
    return sorted((p for p in input_dir.rglob("*.pdf") if p.is_file()), key=lambda p: (p.stat().st_mtime, p.name), reverse=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--min-pages", type=int, default=5)
    parser.add_argument("--max-pdfs", type=int, default=1)
    args = parser.parse_args()

    input_dir = Path(args.input_dir).resolve()
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest(input_dir)

    pdfs = ordered_input_pdfs(input_dir)
    candidates: list[dict[str, Any]] = []
    for pdf in pdfs:
        try:
            pages = page_count(pdf)
        except Exception as exc:
            log(f"Skip unreadable PDF {pdf}: {exc}")
            continue
        log(f"PDF candidate: pages={pages} path={pdf}")
        if pages >= args.min_pages:
            candidates.append({"path": pdf, "pages": pages})

    if not candidates:
        raise RuntimeError(f"No PDF with at least {args.min_pages} pages found under {input_dir}")

    selected = candidates[: max(1, args.max_pdfs)]
    selected_rows: list[dict[str, Any]] = []
    for index, row in enumerate(selected, 1):
        src: Path = row["path"]
        dst = output_dir / f"{index:04d}-{slug(src.name)}.pdf"
        shutil.copy2(src, dst)
        selected_rows.append({"selected_pdf": str(src), "selected_copy": str(dst), "page_count": row["pages"]})
        log(f"Selected test PDF {index}: {dst} ({row['pages']} pages)")

    summary = {
        "selected_pdfs": selected_rows,
        "selected_count": len(selected_rows),
        "min_pages": args.min_pages,
        "max_pdfs": args.max_pdfs,
        "latest_folder": manifest.get("latest_folder", ""),
        "candidate_count": len(candidates),
    }
    (output_dir / "selected_test_pdf.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    first = selected_rows[0]
    write_github_output("selected_pdf", first["selected_copy"])
    write_github_output("page_count", str(first["page_count"]))
    write_github_output("selected_count", str(len(selected_rows)))
    write_github_output("selected_name", Path(first["selected_pdf"]).name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
