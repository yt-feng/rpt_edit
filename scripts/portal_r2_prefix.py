#!/usr/bin/env python3
"""Validate the public catalog's Cloudflare R2 object prefix.

This module is deliberately dependency-free so catalog builds and Worker
deployment workflows use the exact same validation rule before they touch R2
or render a wrangler configuration.
"""

from __future__ import annotations

import argparse
import re
import sys


DEFAULT_R2_PREFIX = "reports"
R2_PREFIX_SEGMENT_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
PROTECTED_R2_ROOTS = frozenset({
    "_catalog-pdf-overrides",
    "_hot-reports",
    "_market-views",
    "reportify",
    "reportify-status",
    "thinktank",
})


def validated_catalog_r2_prefix(prefix: object) -> str:
    """Return a normalized prefix that cannot overlap Worker-owned data."""
    clean_prefix = str(prefix or "").strip("/")
    segments = clean_prefix.split("/") if clean_prefix else []
    if not segments or any(not R2_PREFIX_SEGMENT_RE.fullmatch(segment) for segment in segments):
        raise ValueError(f"Unsafe catalog R2 prefix: {prefix!r}")
    root = segments[0].lower()
    if root.startswith("_") or root in PROTECTED_R2_ROOTS:
        raise ValueError(f"Catalog R2 prefix is reserved: {prefix!r}")
    return "/".join(segments)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate and print a normalized Portal Suite catalog R2 prefix.",
    )
    parser.add_argument("prefix", help="R2 prefix to validate")
    args = parser.parse_args(argv)
    try:
        print(validated_catalog_r2_prefix(args.prefix))
        return 0
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
