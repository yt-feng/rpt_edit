#!/usr/bin/env python3
"""Explicitly provision pinned Argos model archives; inference never downloads.

The upstream index has no published archive digests. Exact URL/version pins plus
a recorded SHA-256 receipt provide repeat-run integrity, not upstream signatures.
Model licenses are captured from the archive; absent license text is reported as
unverified rather than inferred from the Argos Python library's license.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import tempfile
import urllib.request
import zipfile

from offline_translation import MANIFEST, MODEL_ID, OfflineTranslationError, atomic_json, model_directory, normalize_language


def selected_models(targets: str) -> list[dict]:
    requested = {normalize_language(code.strip()) for code in targets.split(",") if code.strip()}
    if not requested:
        raise OfflineTranslationError("At least one target language is required")
    # Every non-English locale can receive English or Chinese source content.
    routes = {("zh", "en")}
    routes.update(("en", target) for target in requested if target != "en")
    return [model for model in MANIFEST["models"] if (model["source"], model["target"]) in routes]


def inspect_archive(path: Path, model: dict) -> tuple[dict, str]:
    with zipfile.ZipFile(path) as archive:
        for member in archive.infolist():
            parts = PurePosixPath(member.filename).parts
            if member.filename.startswith("/") or ".." in parts or "\\" in member.filename:
                raise OfflineTranslationError(f"Invalid model archive path: {member.filename}")
            if (member.external_attr >> 16) & 0o170000 == 0o120000:
                raise OfflineTranslationError("Model archive must not contain symlinks")
        metadata_paths = [name for name in archive.namelist() if name.count("/") == 1 and name.endswith("/metadata.json")]
        if len(metadata_paths) != 1:
            raise OfflineTranslationError("Expected exactly one top-level model metadata.json")
        metadata = json.loads(archive.read(metadata_paths[0]))
        actual = (metadata.get("from_code"), metadata.get("to_code"), str(metadata.get("package_version")))
        expected = (model["source"], model["target"], model["version"])
        if actual != expected:
            raise OfflineTranslationError(f"Model metadata mismatch: expected {expected}, got {actual}")
        root = metadata_paths[0].split("/")[0]
        if not any(name.startswith(root + "/model/") for name in archive.namelist()):
            raise OfflineTranslationError("Argos model directory is missing")
        evidence = {}
        for name in archive.namelist():
            if re.search(r"(?:^|/)(?:license|licence|copying|readme)(?:[._-][^/]*)?$", name, re.I):
                info = archive.getinfo(name)
                if not info.is_dir() and info.file_size <= 1024 * 1024:
                    evidence[name] = archive.read(name).decode("utf-8", errors="replace")
        licenses = [name for name in evidence if re.search(r"(?:^|/)(?:license|licence|copying)", name, re.I)]
        return {"metadata": metadata, "license_status": "bundled_license_text_available" if licenses else "unverified_no_bundled_license_file", "license_and_readme_files": evidence}, root


def install_one(model: dict, packages_dir: Path, previous: dict | None) -> dict:
    if previous and model.get("sha256") and previous.get("sha256") != model["sha256"]:
        raise OfflineTranslationError(f"Cached archive SHA-256 does not match the pinned manifest for {model['source']}->{model['target']}; use a fresh ARGOS_PACKAGES_DIR")
    if previous and previous.get("url") == model["url"] and previous.get("version") == model["version"]:
        installed = packages_dir / previous.get("package_directory", "__missing__") / "metadata.json"
        if installed.is_file():
            metadata = json.loads(installed.read_text(encoding="utf-8"))
            if (metadata.get("from_code"), metadata.get("to_code"), str(metadata.get("package_version"))) == (model["source"], model["target"], model["version"]):
                print(f"Cached {model['source']}->{model['target']} v{model['version']}", flush=True)
                return previous
    with tempfile.TemporaryDirectory(prefix="argos-install-", dir=packages_dir) as directory:
        archive_path = Path(directory) / "model.argosmodel"
        digest = hashlib.sha256()
        print(f"Downloading {model['source']}->{model['target']} v{model['version']}", flush=True)
        request = urllib.request.Request(model["url"], headers={"User-Agent": "Portal-offline-model-installer/1"})
        # Use normal TLS verification. Failure is surfaced without proxy/DNS/TLS
        # changes and without falling back to a remote translation service.
        with urllib.request.urlopen(request, timeout=120) as response, archive_path.open("wb") as output:
            while block := response.read(1024 * 1024):
                digest.update(block)
                output.write(block)
        sha256 = digest.hexdigest()
        expected_digest = model.get("sha256") or (previous or {}).get("sha256")
        if expected_digest and sha256 != expected_digest:
            raise OfflineTranslationError(f"Archive SHA-256 changed for {model['source']}->{model['target']}")
        evidence, root = inspect_archive(archive_path, model)
        # Do not call Argos' install_from_path: it imports the high-level
        # translator/sentence splitters as a side effect. Validated extraction
        # preserves the same official package directory layout.
        with zipfile.ZipFile(archive_path) as archive:
            archive.extractall(Path(directory) / "extracted")
        destination = packages_dir / root
        if destination.exists():
            raise OfflineTranslationError(f"Unreceipted package already exists: {destination}; use a fresh ARGOS_PACKAGES_DIR")
        shutil.move(str(Path(directory) / "extracted" / root), destination)
        return {**model, "sha256": sha256, "checksum_basis": "recorded_download" if not model.get("sha256") else "pinned_manifest", "archive_bytes": archive_path.stat().st_size, "package_directory": root, **evidence}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--targets", default="zh,en,ko,ja,ar", help="Comma-separated target language codes")
    parser.add_argument("--audit-out", type=Path, help="Copy the model provenance/license report to this path")
    args = parser.parse_args()
    packages_dir = model_directory()
    packages_dir.mkdir(parents=True, exist_ok=True)
    receipt_path = packages_dir / "offline-model-provenance.json"
    previous = json.loads(receipt_path.read_text(encoding="utf-8")) if receipt_path.exists() else {}
    installed = {(model["source"], model["target"]): model for model in previous.get("models", [])}
    for model in selected_models(args.targets):
        pair = (model["source"], model["target"])
        installed[pair] = install_one(model, packages_dir, installed.get(pair))
        receipt = {"schema": 1, "model_id": MODEL_ID, "runtime": MANIFEST["runtime"], "upstream_index": MANIFEST["index_source"], "integrity_policy": MANIFEST["integrity_policy"], "license_policy": MANIFEST["license_policy"], "models": [installed[key] for key in sorted(installed)]}
        atomic_json(receipt_path, receipt)
        if args.audit_out:
            atomic_json(args.audit_out, receipt)
    print(f"Offline model provenance: {receipt_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
