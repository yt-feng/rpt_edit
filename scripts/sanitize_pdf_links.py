#!/usr/bin/env python3
"""Remove clickable link annotations from a PDF and rewrite it in place."""

from __future__ import annotations

import argparse
from pathlib import Path


def sanitize_pdf_links(path: Path) -> bool:
    from pypdf import PdfReader, PdfWriter

    reader = PdfReader(str(path))
    writer = PdfWriter()
    changed = False

    for page in reader.pages:
        if "/Annots" in page:
            del page["/Annots"]
            changed = True
        writer.add_page(page)

    if reader.metadata:
      writer.add_metadata({str(key): str(value) for key, value in reader.metadata.items() if value})

    if not changed:
      return False

    tmp = path.with_suffix(path.suffix + ".sanitized")
    with tmp.open("wb") as handle:
      writer.write(handle)
    tmp.replace(path)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Remove PDF link annotations.")
    parser.add_argument("pdf", type=Path)
    args = parser.parse_args()
    changed = sanitize_pdf_links(args.pdf)
    print(f"{'Sanitized' if changed else 'No link annotations found'}: {args.pdf}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
