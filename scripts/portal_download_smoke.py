#!/usr/bin/env python3
"""Download one fixed catalog PDF once through the normal production password API.

This is a real download, not a read-only probe: the existing Worker may copy the
PDF into its Hot report archive and update its download count/public index. It
does not prove other account/membership paths, browser saving, PDF rendering, or
completion of that asynchronous archive. Completeness means the declared HTTP
response body, not PDF structure or bytes outside its Content-Length framing. No PDF, password, response headers,
filename, URL, hash, or response error body is logged or stored.

The Ubuntu Actions runner uses SIGALRM for a whole-operation deadline, including
DNS, TLS, headers and a slowly arriving body. HTTPSConnection neither redirects
nor retries; only one explicit POST is made, with no account or cookie headers.
"""
from __future__ import annotations

from contextlib import contextmanager, suppress
import http.client
import json
import os
from pathlib import Path
import signal
import ssl
import time

HOST = "kcdesk.com"
PATH = "/api/download"
REPORT_ID = "aabc619d832a0cf0fbb1b510"
CONNECT_TIMEOUT = 20
TOTAL_DEADLINE = 90
MAX_BYTES = 10 * 1024 * 1024
CHUNK_BYTES = 64 * 1024
ERRORS = frozenset({
    "missing_password", "http_status", "content_type", "content_encoding",
    "content_length", "body_too_large", "pdf_magic", "body_length",
    "deadline", "timeout", "tls", "transport", "local_failure", "summary_failure",
})
SCOPE = (
    "One observed catalog report through normal password delivery only; not all "
    "account or membership paths, browser saving, PDF rendering, or archive completion."
)
SIDE_EFFECTS = "Normal successful download may update the Hot report archive, count, and public index."


class SmokeFailure(Exception):
    """Carry only an enumerated diagnostic and a numeric HTTP status."""

    def __init__(self, category, status=None):
        self.category = category if category in ERRORS else "local_failure"
        self.status = status if type(status) is int and 100 <= status <= 599 else None
        super().__init__(self.category)


class _DeadlineExpired(Exception):
    pass


@contextmanager
def total_deadline(seconds):
    """Interrupt blocking system calls as well as repeated short body reads."""
    previous = signal.getsignal(signal.SIGALRM)

    def expired(_signum, _frame):
        raise _DeadlineExpired()

    signal.signal(signal.SIGALRM, expired)
    try:
        signal.setitimer(signal.ITIMER_REAL, seconds)
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous)


def download_smoke(password, *, connection_factory=None, clock=time.monotonic):
    if not isinstance(password, str) or not password:
        raise SmokeFailure("missing_password")
    factory = connection_factory or http.client.HTTPSConnection
    connection = response = None
    status = None
    expires = clock() + TOTAL_DEADLINE

    def remaining():
        seconds = expires - clock()
        if seconds <= 0:
            raise _DeadlineExpired()
        return seconds

    try:
        with total_deadline(TOTAL_DEADLINE):
            remaining()
            connection = factory(HOST, timeout=CONNECT_TIMEOUT, context=ssl.create_default_context())
            connection.connect()
            connection.sock.settimeout(remaining())
            # Never trim/normalize the existing secret, put it in a URL, or use
            # PASSWORD_SECRET to generate an alternative report credential.
            body = json.dumps({"id": REPORT_ID, "password": password}).encode("utf-8")
            connection.request("POST", PATH, body=body, headers={
                "Content-Type": "application/json",
                "Accept": "application/pdf",
                "Accept-Encoding": "identity",
            })
            response = connection.getresponse()
            status = response.status
            if status != 200:
                # In particular, never inspect Location or replay a 3xx/5xx POST.
                raise SmokeFailure("http_status", status)
            headers = response.getheaders()

            def values(name):
                return [value.strip() for key, value in headers if key.lower() == name]

            types = values("content-type")
            if len(types) != 1 or types[0].split(";", 1)[0].strip().lower() != "application/pdf":
                raise SmokeFailure("content_type", status)
            encodings = values("content-encoding")
            if encodings and encodings != ["identity"]:
                raise SmokeFailure("content_encoding", status)
            lengths = values("content-length")
            if (len(lengths) != 1 or not lengths[0].isascii() or not lengths[0].isdecimal()
                    or len(lengths[0]) > 10 or values("transfer-encoding")):
                raise SmokeFailure("content_length", status)
            expected = int(lengths[0])
            if expected <= 0:
                raise SmokeFailure("content_length", status)
            if expected > MAX_BYTES:
                raise SmokeFailure("body_too_large", status)

            size = 0
            prefix = b""
            while True:
                remaining()
                chunk = response.read(min(CHUNK_BYTES, MAX_BYTES - size + 1))
                remaining()
                if not chunk:
                    break
                size += len(chunk)
                if size > MAX_BYTES:
                    raise SmokeFailure("body_too_large", status)
                if size > expected:
                    raise SmokeFailure("body_length", status)
                prefix += chunk[:max(0, 5 - len(prefix))]
                if len(prefix) == 5 and prefix != b"%PDF-":
                    raise SmokeFailure("pdf_magic", status)
            if size != expected:
                raise SmokeFailure("body_length", status)
            if prefix != b"%PDF-":
                raise SmokeFailure("pdf_magic", status)
            return {"http_status": status, "pdf_magic_ok": True, "bytes_read": size}
    except SmokeFailure:
        raise
    except _DeadlineExpired:
        raise SmokeFailure("deadline", status) from None
    except ssl.SSLError:
        raise SmokeFailure("tls", status) from None
    except TimeoutError:
        raise SmokeFailure("timeout", status) from None
    except (OSError, http.client.HTTPException):
        raise SmokeFailure("transport", status) from None
    except Exception:
        raise SmokeFailure("local_failure", status) from None
    finally:
        if response is not None:
            with suppress(Exception):
                response.close()
        if connection is not None:
            with suppress(Exception):
                connection.close()


def main():
    try:
        result = download_smoke(os.environ.get("PORTAL_DOWNLOAD_PASSWORD", ""))
        code = 0
    except SmokeFailure as error:
        result = {"http_status": error.status, "error": error.category}
        code = 1
    except Exception:
        result = {"http_status": None, "error": "local_failure"}
        code = 1
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY", "")
    if summary_path:
        try:
            summary = {"result": result, "scope": SCOPE, "normal_side_effects": SIDE_EFFECTS}
            with Path(summary_path).open("a", encoding="utf-8") as output:
                output.write("```json\n" + json.dumps(summary, ensure_ascii=True, sort_keys=True) + "\n```\n")
        except Exception:
            result = {"http_status": result["http_status"], "error": "summary_failure"}
            code = 1
    print(json.dumps(result, sort_keys=True), flush=True)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
