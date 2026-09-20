#!/usr/bin/env python3
"""Persist report translation/editorial memo files in the existing private R2 bucket."""
from __future__ import annotations

import argparse
from pathlib import Path
import re

from private_workflow_handoff import download_directory, upload_directory


def checkpoint_key(scope: str, date_folder: str) -> str:
    if not re.fullmatch(r"[a-z][a-z0-9-]{0,63}", scope):
        raise ValueError("Invalid translation checkpoint scope")
    if not re.fullmatch(r"\d{6}", date_folder):
        raise ValueError("Translation checkpoint date must be YYMMDD")
    return f"_workflow-cache/report-translation/v1/{scope}/{date_folder}.tar.gz"


def restore(directory: Path, key: str) -> bool:
    try:
        download_directory(key, directory)
    except Exception as error:
        code = str(getattr(error, "response", {}).get("Error", {}).get("Code", ""))
        if code not in {"NoSuchKey", "404", "NotFound"}:
            raise
        print("No previous private translation checkpoint; starting with an empty memo.")
        directory.mkdir(parents=True, exist_ok=True)
        return False
    return True


def save(directory: Path, key: str) -> bool:
    if not directory.is_dir() or not any(directory.rglob("*.json")):
        print("No completed translation/editorial rows to checkpoint.")
        return False
    upload_directory(directory, key)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("restore", "save"))
    parser.add_argument("--scope", required=True)
    parser.add_argument("--date-folder", required=True)
    parser.add_argument("--directory", type=Path, required=True)
    args = parser.parse_args()
    action = restore if args.command == "restore" else save
    action(args.directory, checkpoint_key(args.scope, args.date_folder))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
