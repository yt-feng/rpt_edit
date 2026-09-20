#!/usr/bin/env python3
"""Exercise private checkpoint transport using only built-in synthetic fixtures.

Run save, verify and cleanup in separate processes. Each phase creates fresh local
directories; only private R2 objects connect save to verify. Never accepts an
arbitrary object key or prefix. Public diagnostics contain counts and hashes only.
"""
from __future__ import annotations

import argparse
from contextlib import redirect_stderr, redirect_stdout
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile
from typing import Any

from check_completed_shard import completed_shard_reason
import private_generation_checkpoint as generation
import private_translation_checkpoint as translation
import private_workflow_handoff as handoff

NAMESPACE = "_workflow-smoke/private-checkpoints/v1"
REPO = Path(__file__).resolve().parent.parent
SYNTHETIC_PDF = b"%PDF-1.4\nPublic synthetic checkpoint fixture; no source report.\n%%EOF\n"
PHASES = ("save", "verify", "cleanup")


def object_keys(run_id: str, run_attempt: str) -> dict[str, str]:
    if not all(re.fullmatch(r"[1-9][0-9]{0,19}", value) for value in (run_id, run_attempt)):
        raise ValueError("Expected numeric GitHub run identity")
    return {name: f"{NAMESPACE}/{run_id}/{run_attempt}/{name}.tar.gz"
            for name in ("translation", "generation", "handoff")}


def json_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=True, sort_keys=True) + "\n").encode()


def fixtures(root: Path) -> tuple[Path, str, dict[str, bytes], dict[str, bytes]]:
    manifest = root / "selected.json"
    manifest.write_bytes(json_bytes([{
        "process_rank": 1, "process_local_path": "selected/01-public-synthetic.pdf",
        "content_sha256": hashlib.sha256(SYNTHETIC_PDF).hexdigest(),
    }]))
    identity = generation.input_identity(manifest, 0, 1, {"model": "synthetic-no-model"}, REPO)
    report = "0001-public-synthetic"
    article = b"# Public synthetic fixture\nThis is a storage transport check.\n"
    generated = {
        f"{report}/source_mineru.md": b"Public synthetic source: revenue was USD 120 million.\n",
        f"{report}/wechat_article.md": article,
        f"{report}/zhihu_article.md": article,
        f"{report}/zhihu_article.md.generation.json": json_bytes({"input_sha256": hashlib.sha256(article).hexdigest()}),
        f"{report}/status.json": json_bytes({"source_pdf": "01-public-synthetic.pdf", "wechat_article": "wechat_article.md"}),
        "shard_run_summary.md": b"- Selected PDFs available to shards: 1\n- Shard index: 0\n- Reports per shard: 1\n- Report directories generated: 1\n",
        "finalize_summary.json": json_bytes([{"item": report, "zhihu_article.md": "zhihu_article.md"}]),
        "sensitive_content_guard_summary.json": json_bytes([{"api_errors": [], "rewrite_error": ""}]),
        "sensitive_content_guard_cache.json": json_bytes({hashlib.sha256(b"synthetic-path").hexdigest(): hashlib.sha256(article).hexdigest()}),
        generation.CHECKPOINT_FILE: json_bytes({"version": generation.VERSION, "identity": identity, "complete": True}),
    }
    memo = {
        f"{hashlib.sha256(b'public-synthetic-body').hexdigest()}.json": json_bytes({"article": article.decode(), "provider": "synthetic-no-model"}),
        f"titles/{hashlib.sha256(b'public-synthetic-title').hexdigest()}.json": json_bytes({"title": "Public synthetic fixture", "decision": {"needs_model_repair": False}}),
    }
    return manifest, identity, generated, memo


def write_tree(directory: Path, files: dict[str, bytes]) -> None:
    for relative, data in files.items():
        target = directory / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)


def tree_hash(files: dict[str, bytes]) -> str:
    return hashlib.sha256(json_bytes({name: hashlib.sha256(data).hexdigest()
                                     for name, data in sorted(files.items())})).hexdigest()


def verify_tree(directory: Path, expected: dict[str, bytes]) -> None:
    actual = {path.relative_to(directory).as_posix(): path.read_bytes()
              for path in directory.rglob("*") if path.is_file()}
    if actual != expected:
        raise RuntimeError("Synthetic checkpoint content mismatch")


def save_objects(keys: dict[str, str]) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="private-checkpoint-save-") as temporary:
        root = Path(temporary)
        _manifest, identity, generated, memo = fixtures(root)
        directory = root / "generation"
        # Production save must create its own completion metadata.
        write_tree(directory, {name: data for name, data in generated.items() if name != generation.CHECKPOINT_FILE})
        write_tree(directory, {"raw.pdf": SYNTHETIC_PDF, "unused.mp4": b"synthetic excluded media",
                               "mineru_raw/raw.json": b"{}"})
        if not generation.save(directory, keys["generation"], identity, complete=True):
            raise RuntimeError("Synthetic generation checkpoint was not saved")
        cache = root / "translation"
        write_tree(cache, memo)
        if not translation.save(cache, keys["translation"]):
            raise RuntimeError("Synthetic translation checkpoint was not saved")
        return {"objects_uploaded": 2, "fixture_sha256": tree_hash({**generated, **memo})}


def verify_objects(keys: dict[str, str]) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="private-checkpoint-verify-") as temporary:
        root = Path(temporary)
        manifest, identity, generated, memo = fixtures(root)
        directory, cache, downstream = root / "generation", root / "translation", root / "downstream"
        # No saved local tree or cache exists in this process.
        if any(path.exists() for path in (directory, cache, downstream)):
            raise RuntimeError("Expected an empty restore destination")
        if not generation.restore(directory, keys["generation"], identity):
            raise RuntimeError("Expected the generation checkpoint to exist")
        if not translation.restore(cache, keys["translation"]):
            raise RuntimeError("Expected the translation checkpoint to exist")
        verify_tree(directory, generated)
        verify_tree(cache, memo)
        if not completed_shard_reason(directory, manifest, 0, 1, 1)[0]:
            raise RuntimeError("Restored generation did not pass the production reuse gate")
        # A reused generation must still produce a complete current-run handoff.
        handoff.upload_directory(directory, keys["handoff"])
        handoff.download_directory(keys["handoff"], downstream)
        verify_tree(downstream, generated)
        return {"objects_restored": 3, "objects_uploaded": 1, "reuse_checks_passed": 1,
                "files_verified": 2 * len(generated) + len(memo),
                "fixture_sha256": tree_hash({**generated, **memo})}


def cleanup_objects(keys: dict[str, str]) -> dict[str, Any]:
    client, bucket = handoff.build_r2_client(), handoff.r2_bucket()
    removed = 0
    # Exact three object names, never list/delete-prefix. Missing uploads are OK.
    for key in keys.values():
        try:
            client.delete_object(Bucket=bucket, Key=key)
            try:
                client.head_object(Bucket=bucket, Key=key)
            except Exception as error:
                code = str(getattr(error, "response", {}).get("Error", {}).get("Code", ""))
                if code in {"NoSuchKey", "404", "NotFound"}:
                    removed += 1
        except Exception:
            # Attempt every exact object even if one delete fails.
            continue
    return {"success": removed == len(keys), "objects_verified_absent": removed}


def run_phase(phase: str, diagnostics: Path) -> bool:
    result: dict[str, Any] = {"schema_version": 1, "phase": phase, "success": False}
    # Helpers normally print keys; SDK errors may include bucket/endpoint data.
    # Neither goes to public Actions logs or artifacts, even on failure.
    with open(os.devnull, "w") as sink, redirect_stdout(sink), redirect_stderr(sink):
        try:
            keys = object_keys(os.environ.get("GITHUB_RUN_ID", ""), os.environ.get("GITHUB_RUN_ATTEMPT", ""))
            action = {"save": save_objects, "verify": verify_objects, "cleanup": cleanup_objects}[phase]
            result.update(action(keys))
            if phase != "cleanup":
                result["success"] = True
        except Exception:
            pass
    diagnostics.mkdir(parents=True, exist_ok=True)
    (diagnostics / f"{phase}.json").write_bytes(json_bytes(result))
    print(f"Private checkpoint {phase}: success={str(result['success']).lower()}")
    return result["success"]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase", choices=PHASES)
    parser.add_argument("--diagnostics-out", type=Path, required=True)
    args = parser.parse_args(argv)
    return 0 if run_phase(args.phase, args.diagnostics_out) else 1


if __name__ == "__main__":
    raise SystemExit(main())
