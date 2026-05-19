#!/usr/bin/env python3
"""Select one test PDF with at least N pages from a downloaded Dropbox folder."""
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--min-pages", type=int, default=5)
    args = parser.parse_args()

    input_dir = Path(args.input_dir).resolve()
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest(input_dir)

    pdfs = sorted((p for p in input_dir.rglob("*.pdf") if p.is_file()), key=lambda p: (p.stat().st_mtime, p.name), reverse=True)
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

    selected = candidates[0]
    src: Path = selected["path"]
    dst = output_dir / f"0001-{slug(src.name)}.pdf"
    shutil.copy2(src, dst)

    summary = {
        "selected_pdf": str(src),
        "selected_copy": str(dst),
        "page_count": selected["pages"],
        "min_pages": args.min_pages,
        "latest_folder": manifest.get("latest_folder", ""),
        "candidate_count": len(candidates),
    }
    (output_dir / "selected_test_pdf.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    write_github_output("selected_pdf", str(dst))
    write_github_output("page_count", str(selected["pages"]))
    write_github_output("selected_name", src.name)
    log(f"Selected test PDF: {dst} ({selected['pages']} pages)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
