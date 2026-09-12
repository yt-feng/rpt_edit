#!/usr/bin/env python3
"""Download and convert the pinned M2M100 checkpoint inside GitHub Actions.

This is the only step that may contact Hugging Face. Translation itself reads
the converted local directory and is tested with network calls blocked. The
guard prevents an accidental multi-gigabyte model download on a developer
machine that may be running other projects.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import shutil
import tempfile

from m2m100_offline_translation import MANIFEST as M2M100_MANIFEST, MODEL as M2M100_MODEL_ID, REVISION as M2M100_REVISION, MODEL_ID as M2M100_RUNTIME_ID, OfflineTranslationError, atomic_json, model_directory as m2m100_model_directory


SOURCE_PATTERNS = [
    "README.md", "config.json", "generation_config.json", "pytorch_model.bin",
    "sentencepiece.bpe.model", "special_tokens_map.json", "tokenizer_config.json", "vocab.json",
]
RUNTIME_COPY = [name for name in SOURCE_PATTERNS if name != "pytorch_model.bin"]


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as stream:
        while block := stream.read(1024 * 1024):
            hasher.update(block)
    return hasher.hexdigest()


def file_receipt(root: Path, *, relative_paths: list[str]) -> dict[str, str]:
    return {relative: digest(root / relative) for relative in relative_paths if (root / relative).is_file()}


def ensure_actions_only() -> None:
    if os.environ.get("GITHUB_ACTIONS") != "true":
        raise OfflineTranslationError("M2M100 model provisioning is restricted to GitHub Actions")


def already_installed(destination: Path) -> bool:
    receipt_path = destination / "m2m100-model-provenance.json"
    runtime_dir = destination / "ct2-int8"
    if not receipt_path.is_file() or not runtime_dir.is_dir():
        return False
    try:
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        return (
            receipt.get("model_id") == M2M100_MODEL_ID
            and receipt.get("revision") == M2M100_REVISION
            and receipt.get("quantization") == "int8"
            and receipt.get("license") == "MIT"
            and bool(receipt.get("source_files"))
            and bool(receipt.get("runtime_files"))
            and all(
                isinstance(relative, str)
                and isinstance(expected, str)
                and (destination / relative).is_file()
                and digest(destination / relative) == expected
                for relative, expected in receipt.get("runtime_files", {}).items()
            )
        )
    except (OSError, ValueError):
        return False


def install(destination: Path) -> dict:
    ensure_actions_only()
    if already_installed(destination):
        receipt = json.loads((destination / "m2m100-model-provenance.json").read_text(encoding="utf-8"))
        print(f"Using cached M2M100 model: {destination}", flush=True)
        return receipt
    try:
        import torch
        from huggingface_hub import snapshot_download
        from ctranslate2.converters import TransformersConverter
    except ImportError as exc:
        raise OfflineTranslationError(
            "Install the M2M100 provisioning runtime before model setup"
        ) from exc

    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="m2m100-install-", dir=destination.parent) as work:
        work_dir = Path(work)
        source_dir = Path(snapshot_download(
            M2M100_MODEL_ID,
            revision=M2M100_REVISION,
            cache_dir=work_dir / "hf-cache",
            allow_patterns=SOURCE_PATTERNS,
            max_workers=2,
        ))
        card_path = source_dir / "README.md"
        card = card_path.read_text(encoding="utf-8")
        if "license: mit" not in card.lower():
            raise OfflineTranslationError("Pinned M2M100 model card no longer declares the expected MIT license")
        missing = [name for name in SOURCE_PATTERNS if not (source_dir / name).is_file()]
        if missing:
            raise OfflineTranslationError(f"Pinned M2M100 snapshot is missing: {', '.join(missing)}")

        converted = work_dir / "ct2-int8"
        try:
            converter = TransformersConverter(str(source_dir), low_cpu_mem_usage=True)
        except TypeError:
            # Older CTranslate2 releases do not accept low_cpu_mem_usage in the
            # converter constructor; the pinned Action runtime does, but this
            # keeps the installer error explicit if the environment drifts.
            converter = TransformersConverter(str(source_dir))
        try:
            converter.convert(str(converted), quantization="int8", force=True)
        except TypeError:
            converter.convert(str(converted), quantization="int8")
        if not (converted / "model.bin").is_file():
            raise OfflineTranslationError("CTranslate2 conversion produced no model.bin")

        staged = work_dir / "staged"
        staged.mkdir()
        for name in RUNTIME_COPY:
            shutil.copy2(source_dir / name, staged / name)
        shutil.move(str(converted), staged / "ct2-int8")
        runtime_files = [str(path.relative_to(staged)) for path in staged.rglob("*") if path.is_file()]
        receipt = {
            "schema": 1,
            "provider": "m2m100-offline",
            "model_id": M2M100_MODEL_ID,
            "revision": M2M100_REVISION,
            "model_runtime_id": M2M100_RUNTIME_ID,
            "license": "MIT",
            "license_evidence": "README.md at the pinned official Hugging Face revision declares license: mit",
            "quantization": "int8",
            "conversion": {"converter": "ctranslate2.converters.TransformersConverter", "source_framework": "PyTorch"},
            "runtime": {
                "ctranslate2": importlib.metadata.version("ctranslate2"),
                "sentencepiece": importlib.metadata.version("sentencepiece"),
                "transformers": importlib.metadata.version("transformers"),
                "torch": importlib.metadata.version("torch"),
            },
            "source_files": file_receipt(source_dir, relative_paths=SOURCE_PATTERNS),
            "runtime_files": file_receipt(staged, relative_paths=runtime_files),
            "routes": sorted([list(route) for route in M2M100_MANIFEST.get("routes", [])]),
            "integrity_policy": "Refuse a cached directory unless the pinned revision, license evidence, quantization, and file receipts match.",
        }
        atomic_json(staged / "m2m100-model-provenance.json", receipt)
        if destination.exists():
            shutil.rmtree(destination)
        shutil.move(str(staged), destination)
    return receipt


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model-dir", type=Path, default=m2m100_model_directory())
    parser.add_argument("--audit-out", type=Path)
    args = parser.parse_args()
    receipt = install(args.model_dir)
    if args.audit_out:
        atomic_json(args.audit_out, receipt)
    print(json.dumps(receipt, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
