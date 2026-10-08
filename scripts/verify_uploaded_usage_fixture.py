"""Verify the same-job upload by immutable ID without listing artifacts."""
from __future__ import annotations

import hashlib
import io
import os
from pathlib import Path
import re
import zipfile

import requests

MAX_ARCHIVE = 1024 * 1024
MEMBER = 'fixture/path-check.json'


def verify(payload: bytes, checksum: str, expected: bytes) -> None:
    if not re.fullmatch(r'[a-f0-9]{64}', checksum) or hashlib.sha256(payload).hexdigest() != checksum:
        raise ValueError('Uploaded fixture checksum mismatch')
    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        entries = archive.infolist()
        matches = [entry for entry in entries if entry.filename == MEMBER]
        if (len(entries) > 1000 or len(matches) != 1 or matches[0].is_dir()
                or matches[0].file_size > 64000 or matches[0].flag_bits & 1):
            raise ValueError('Uploaded fixture member invalid')
        # Read only the known fixture; archive paths are never extracted.
        actual = archive.read(matches[0])
        if actual != expected:
            raise ValueError('Uploaded fixture contents changed')


def main() -> int:
    repository, artifact = os.environ['GITHUB_REPOSITORY'], os.environ['UPLOADED_ARTIFACT_ID']
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository) or not re.fullmatch(r'[1-9][0-9]*', artifact):
        raise ValueError('Uploaded fixture identity invalid')
    url = f'https://api.github.com/repos/{repository}/actions/artifacts/{artifact}/zip'
    headers = {'Authorization': 'Bearer '+os.environ['GH_TOKEN'],
               'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28'}
    # A direct artifact lookup does not depend on the just-written name index.
    # requests strips authorization on the cross-host archive redirect.
    chunks, size = [], 0
    with requests.get(url, headers=headers, stream=True, timeout=(10, 30)) as response:
        response.raise_for_status()
        for chunk in response.iter_content(65536):
            size += len(chunk)
            if size > MAX_ARCHIVE:
                raise ValueError('Uploaded fixture archive exceeds bound')
            chunks.append(chunk)
    expected = (Path(os.environ['DEEPSEEK_USAGE_DIR'])/MEMBER).read_bytes()
    verify(b''.join(chunks), os.environ['UPLOADED_ARTIFACT_SHA256'], expected)
    print('Exact uploaded artifact checksum, fixture layout and contents verified')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
