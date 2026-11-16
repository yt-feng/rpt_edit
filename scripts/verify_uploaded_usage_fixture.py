"""Verify the same-job upload by immutable ID without listing artifacts."""
from __future__ import annotations

import hashlib
import io
import os
from pathlib import Path
import re
import sys
import time
import zipfile

import requests
from urllib3.exceptions import HTTPError as StreamError, ProtocolError, ReadTimeoutError, SSLError as StreamSSLError

MAX_ARCHIVE = 1024 * 1024
MEMBER = 'fixture/path-check.json'
READ_BUDGET_SECONDS = 45
RETRY_DELAYS = (1, 2, 4, 8)


class RetryableRead(RuntimeError):
    pass


def download(repository: str, artifact: str, token: str) -> bytes:
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository) or not re.fullmatch(r'[1-9][0-9]*', artifact):
        raise ValueError('Uploaded fixture identity invalid')
    url = f'https://api.github.com/repos/{repository}/actions/artifacts/{artifact}/zip'
    headers = {'Authorization': 'Bearer '+token,
               'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28'}
    deadline = time.monotonic() + READ_BUDGET_SECONDS
    # Only the exact ID returned by this job's upload is retried. Even that
    # immutable lookup can return 404 briefly before GitHub serves the archive.
    with requests.Session() as session:
        session.max_redirects = 3
        for attempt in range(len(RETRY_DELAYS) + 1):
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise RuntimeError('Uploaded fixture read exceeded elapsed budget')
            try:
                # Budget the possible redirect legs too. requests removes the
                # GitHub authorization header when following a cross-host URL.
                with session.get(url, headers=headers, stream=True,
                                 timeout=(min(3, remaining / 8), min(5, remaining / 8))) as response:
                    status = response.status_code
                    if status in {404, 408, 429} or 500 <= status <= 599:
                        raise RetryableRead(f'HTTP {status}')
                    if status != 200:
                        raise ValueError(f'Uploaded fixture read rejected: HTTP {status}')
                    declared = response.headers.get('Content-Length')
                    if declared is not None and (not declared.isdecimal() or int(declared) > MAX_ARCHIVE):
                        raise ValueError('Uploaded fixture archive exceeds bound or has invalid length')
                    chunks, size = [], 0
                    while True:
                        if time.monotonic() >= deadline:
                            raise RuntimeError('Uploaded fixture read exceeded elapsed budget')
                        # read1 returns currently available bytes, allowing the
                        # elapsed guard to run even when a server dribbles data.
                        read1 = getattr(response.raw, 'read1', None)
                        # Older requests-compatible urllib3 releases lack
                        # read1; a one-byte read preserves the same deadline.
                        chunk = (read1(65536, decode_content=True) if read1 is not None
                                 else response.raw.read(1, decode_content=True))
                        if time.monotonic() >= deadline:
                            raise RuntimeError('Uploaded fixture read exceeded elapsed budget')
                        if not chunk:
                            return b''.join(chunks)
                        size += len(chunk)
                        if size > MAX_ARCHIVE:
                            raise ValueError('Uploaded fixture archive exceeds bound')
                        chunks.append(chunk)
            except (requests.exceptions.SSLError, StreamSSLError):
                raise ValueError('Uploaded fixture TLS verification failed') from None
            except (RetryableRead, requests.exceptions.ConnectionError, requests.exceptions.Timeout,
                    requests.exceptions.ChunkedEncodingError, ProtocolError, ReadTimeoutError) as error:
                reason = str(error) if isinstance(error, RetryableRead) else type(error).__name__
            except (requests.exceptions.RequestException, StreamError):
                raise ValueError('Uploaded fixture request failed permanently') from None
            if attempt == len(RETRY_DELAYS):
                raise RuntimeError(f'Uploaded fixture read failed after {attempt + 1} attempts: {reason}') from None
            delay = RETRY_DELAYS[attempt]
            if time.monotonic() + delay >= deadline:
                raise RuntimeError('Uploaded fixture read exceeded elapsed budget') from None
            print(f'Uploaded fixture read retry attempt={attempt + 2} reason={reason}', file=sys.stderr, flush=True)
            time.sleep(delay)


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
    expected = (Path(os.environ['DEEPSEEK_USAGE_DIR'])/MEMBER).read_bytes()
    checksum = os.environ['UPLOADED_ARTIFACT_SHA256']
    if not re.fullmatch(r'[a-f0-9]{64}', checksum):
        raise ValueError('Uploaded fixture checksum invalid')
    payload = download(repository, artifact, os.environ['GH_TOKEN'])
    verify(payload, checksum, expected)
    print('Exact uploaded artifact checksum, fixture layout and contents verified')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
