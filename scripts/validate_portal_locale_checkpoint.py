#!/usr/bin/env python3
"""Validate an optional CI translation checkpoint before reuse or persistence.

The release builder remains responsible for exact-source and quality checks.
This entrypoint uses its real cache loader, including supported model migrations,
and reports only aggregate counts. It never rewrites the checkpoint.
"""
from __future__ import annotations

import argparse
from contextlib import redirect_stdout
import json
from pathlib import Path
import sys
from typing import Any

from build_portal_locales import LOCALES, load_cache
from offline_translation import MODEL_ID


class CheckpointValidationError(ValueError):
    """A checkpoint cannot be supplied to the current locale builder."""


def validate_checkpoint(path: Path, *, kind: str = "locale") -> dict[str, Any]:
    if kind not in {"locale", "title"}:
        raise CheckpointValidationError("invalid_checkpoint_kind")
    try:
        if path.is_symlink() or not path.is_file() or path.stat().st_size == 0:
            raise CheckpointValidationError("missing_or_empty_checkpoint")
    except OSError as error:
        raise CheckpointValidationError("unreadable_checkpoint") from error
    try:
        # Namespace migrations can emit a generic message. Keep stdout reserved
        # for the machine-readable receipt and never print loader exceptions,
        # which may contain a private path or source-unit key.
        with redirect_stdout(sys.stderr):
            if kind == "title":
                from translate_portal_titles import load_title_cache
                cache = load_title_cache(path)
            else:
                cache = load_cache(path, MODEL_ID, provider="hymt")
    except (OSError, RuntimeError, ValueError, TypeError, AttributeError) as error:
        raise CheckpointValidationError("invalid_checkpoint") from error
    if kind == "title":
        return {"status": "valid", "entry_count": len(cache["entries"])}
    counts = {locale: len(cache["locales"][locale]) for locale in LOCALES}
    # A valid empty cache is possible after a bounded first run or model upgrade.
    # Source fallback rows are intentionally not persisted as translations.
    return {"status": "valid", "entry_count": sum(counts.values()), "entries_by_locale": counts}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kind", choices=("locale", "title"), default="locale")
    parser.add_argument("path", type=Path, help="Translation checkpoint to validate")
    args = parser.parse_args(argv)
    try:
        result = validate_checkpoint(args.path, kind=args.kind)
    except CheckpointValidationError as error:
        print(json.dumps({"status": "invalid", "reason": str(error)}, sort_keys=True))
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
