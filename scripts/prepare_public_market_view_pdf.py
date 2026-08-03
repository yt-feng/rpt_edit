#!/usr/bin/env python3
"""Create the public Market Views copy without its private ending page."""

from __future__ import annotations

import argparse
import os
import tempfile
from pathlib import Path
from typing import Any

from pypdf import PdfReader, PdfWriter

from check_public_identity import confusable_skeleton, private_markers


ENDING_PAGE_MARKER = "portal.example.invalid"
MIN_PDF_BYTES = 1024


def _contains_private_identity(value: str) -> bool:
    skeleton = confusable_skeleton(value)
    return any(confusable_skeleton(marker) in skeleton for marker in private_markers())


def _annotation_uris(page: Any) -> list[str]:
    uris: list[str] = []
    for reference in page.get("/Annots") or []:
        annotation = reference.get_object()
        action = annotation.get("/A") or {}
        uri = action.get("/URI")
        if uri:
            uris.append(str(uri))
    return uris


def prepare_public_copy(source: Path | str, output: Path | str) -> dict[str, int]:
    source_path = Path(source).expanduser().resolve()
    output_path = Path(output).expanduser().resolve()
    if not source_path.is_file():
        raise FileNotFoundError(f"Market Views source PDF does not exist: {source_path}")
    if source_path.stat().st_size <= MIN_PDF_BYTES:
        raise ValueError(f"Market Views source PDF is too small: {source_path}")
    if source_path == output_path:
        raise ValueError("Source and output paths must differ")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    temp_path: Path | None = None
    try:
        reader = PdfReader(source_path)
        if len(reader.pages) < 2:
            raise ValueError("Market Views PDF must contain a separate private ending page")
        ending_text = "".join((reader.pages[-1].extract_text() or "").split())
        if ENDING_PAGE_MARKER not in ending_text:
            raise ValueError("The final PDF page is not the expected private ending page")

        searchable_parts = [str(value or "") for value in (reader.metadata or {}).values()]
        for page in reader.pages[:-1]:
            searchable_parts.append(page.extract_text() or "")
            searchable_parts.extend(_annotation_uris(page))
        if _contains_private_identity("\n".join(searchable_parts)):
            raise ValueError("Private identity remains in the public Market Views PDF")

        writer = PdfWriter()
        for page in reader.pages[:-1]:
            writer.add_page(page)
        title = str((reader.metadata or {}).get("/Title") or "Market Views")
        writer.add_metadata(
            {
                "/Title": title,
                "/Author": "",
                "/Creator": "Neutral Market Views export",
                "/Keywords": "",
                "/Producer": "pypdf",
                "/Subject": "Public archive copy",
            }
        )
        expected_pages = len(reader.pages) - 1
        with tempfile.NamedTemporaryFile(
            prefix=f".{output_path.name}.",
            suffix=".tmp",
            dir=output_path.parent,
            delete=False,
        ) as handle:
            temp_path = Path(handle.name)
            writer.write(handle)

        if temp_path.stat().st_size <= MIN_PDF_BYTES:
            raise ValueError("Public Market Views PDF is too small after sanitization")
        public_document = PdfReader(temp_path)
        if len(public_document.pages) != expected_pages:
            raise ValueError("Public Market Views PDF page-count verification failed")
        public_text = "\n".join(page.extract_text() or "" for page in public_document.pages)
        public_uris = [uri for page in public_document.pages for uri in _annotation_uris(page)]
        if ENDING_PAGE_MARKER in public_text or ENDING_PAGE_MARKER in "\n".join(public_uris):
            raise ValueError("Private ending-page marker remains in public PDF")
        if _contains_private_identity("\n".join((public_text, *public_uris))):
            raise ValueError("Private identity remains in verified public PDF text or links")

        os.replace(temp_path, output_path)
        temp_path = None
        return {"page_count": expected_pages, "size_bytes": output_path.stat().st_size}
    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Remove the dedicated private ending page from a Market Views PDF."
    )
    parser.add_argument("--source", required=True, help="Original private Market Views PDF.")
    parser.add_argument("--output", required=True, help="Public-safe PDF output path.")
    args = parser.parse_args()

    result = prepare_public_copy(args.source, args.output)
    print(
        f"Prepared public Market Views PDF: {args.output} "
        f"({result['page_count']} pages, {result['size_bytes']} bytes)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
