#!/usr/bin/env python3
"""Provision an immutable official GGUF on Actions; never download during inference."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import urllib.request

from compare_hymt_translation import file_sha256, require_actions, verify_model

MANIFEST_PATH = Path(__file__).with_name('hymt_translation_model_manifest.json')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model-dir', type=Path, required=True)
    parser.add_argument('--server-bin', type=Path, required=True)
    parser.add_argument('--audit-out', type=Path, required=True)
    args = parser.parse_args()
    require_actions()
    manifest = json.loads(MANIFEST_PATH.read_text())
    model = manifest['model']
    args.model_dir.mkdir(parents=True, exist_ok=True)
    destination = args.model_dir / model['filename']
    if not destination.exists():
        temporary = destination.with_suffix('.download')
        url = f"https://huggingface.co/{model['repository']}/resolve/{model['revision']}/{model['filename']}"
        try:
            with urllib.request.urlopen(url, timeout=180) as response, temporary.open('wb') as stream:
                while block := response.read(4 * 1024 * 1024):
                    stream.write(block)
            verify_model(temporary, manifest)
            temporary.replace(destination)
        finally:
            temporary.unlink(missing_ok=True)
    verify_model(destination, manifest)
    if not args.server_bin.is_file():
        raise RuntimeError('Missing pinned llama-server runtime')
    # Preserve license alongside cached public model files.
    license_path = args.model_dir / 'LICENSE.txt'
    if not license_path.exists():
        url = f"https://huggingface.co/{model['repository']}/resolve/{model['revision']}/LICENSE.txt"
        with urllib.request.urlopen(url, timeout=60) as response:
            license_path.write_bytes(response.read())
    receipt = {'provider': 'hymt', 'model': model, 'model_sha256': model['sha256'],
               'runtime_revision': manifest['runtime']['revision'], 'runtime': manifest['runtime'],
               'server_sha256': file_sha256(args.server_bin),
               'manifest_sha256': hashlib.sha256(MANIFEST_PATH.read_bytes()).hexdigest(),
               'created_at': datetime.now(timezone.utc).isoformat(),
               'github_run_id': os.environ.get('GITHUB_RUN_ID'), 'paid_provider_requests': 0}
    for path in (args.audit_out, args.model_dir / 'hymt-model-provenance.json'):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
