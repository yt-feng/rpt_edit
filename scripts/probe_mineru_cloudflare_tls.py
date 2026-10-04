#!/usr/bin/env python3
"""One strict-HTTPS CDN HEAD from a temporary Cloudflare Worker, then cleanup.

Cloudflare API references:
https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/
https://developers.cloudflare.com/api/resources/workers/subresources/subdomains/
https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/subdomain/
https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-526/

This is a connectivity diagnostic, not a result download or an R2 mirror.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import secrets
from typing import Any

import requests
from requests.adapters import HTTPAdapter

ROOT = Path(__file__).resolve().parents[1]
WORKER_SOURCE = ROOT / "workers/mineru-result-tls-probe/src/index.js"
API_ROOT = "https://api.cloudflare.com/client/v4"
PROBE_CATEGORIES = frozenset({
    "tls_invalid_certificate", "tls_handshake_failed", "https_redirect_received",
    "https_response_received", "fetch_failed", "fetch_timeout",
    "upstream_http_error",
})
MAX_RESPONSE_BYTES = 262144


class ProbeFailure(Exception):
    def __init__(self, stage: str, category: str, status: int | None = None,
                 codes: list[int] | None = None):
        super().__init__(category)
        self.stage, self.category, self.status = stage, category, status
        self.codes = codes or []


def _object(response: Any, stage: str) -> dict:
    chunks, size = [], 0
    try:
        for chunk in response.iter_content(chunk_size=16384):
            size += len(chunk)
            if size > MAX_RESPONSE_BYTES:
                raise ProbeFailure(stage, "response_too_large", response.status_code)
            chunks.append(chunk)
        payload = json.loads(b"".join(chunks))
    except ProbeFailure:
        raise
    except (ValueError, UnicodeError, requests.RequestException):
        raise ProbeFailure(stage, "invalid_response", response.status_code) from None
    if not isinstance(payload, dict):
        raise ProbeFailure(stage, "invalid_response", response.status_code)
    return payload


def _codes(payload: dict) -> list[int]:
    errors = payload.get("errors", [])
    if not isinstance(errors, list):
        return []
    return [row["code"] for row in errors[:8] if isinstance(row, dict)
            and type(row.get("code")) is int and 0 <= row["code"] <= 1000000]


def _validate_probe(payload: dict) -> dict:
    expected = {"schema_version": 1, "provider_host": "cdn-mineru.openxlab.org.cn",
                "request_method": "HEAD", "request_count": 1,
                "redirects_followed": 0, "zip_downloads": 0, "provider_posts": 0}
    if any(payload.get(key) != value or type(payload.get(key)) is not type(value)
           for key, value in expected.items()):
        raise ProbeFailure("worker_probe", "invalid_probe_summary")
    category, status = payload.get("category"), payload.get("upstream_http_status")
    if category not in PROBE_CATEGORIES or (status is not None and
                                           (type(status) is not int or not 100 <= status <= 599)):
        raise ProbeFailure("worker_probe", "invalid_probe_summary")
    expected_category = ("tls_invalid_certificate" if status == 526 else
                         "tls_handshake_failed" if status == 525 else
                         "upstream_http_error" if status is not None and status >= 500 else
                         "https_redirect_received" if status is not None and 300 <= status < 400 else
                         "https_response_received" if status is not None else None)
    if ((expected_category is not None and category != expected_category)
            or (expected_category is None and category not in {"fetch_failed", "fetch_timeout"})):
        raise ProbeFailure("worker_probe", "invalid_probe_summary")
    colo = payload.get("colo")
    elapsed = payload.get("elapsed_ms")
    if not isinstance(colo, str) or not re.fullmatch(r"[A-Z]{3}|unknown", colo):
        raise ProbeFailure("worker_probe", "invalid_probe_summary")
    if type(elapsed) is not int or not 0 <= elapsed <= 60000:
        raise ProbeFailure("worker_probe", "invalid_probe_summary")
    return {**expected, "category": category, "upstream_http_status": status,
            "colo": colo, "elapsed_ms": elapsed}


def _configuration(env: dict[str, str]) -> tuple[str, str, str, str, str]:
    repository = env.get("GITHUB_REPOSITORY", "")
    workflow_ref = repository + "/.github/workflows/mineru-cloudflare-tls-probe.yml@refs/heads/main"
    if (env.get("GITHUB_ACTIONS") != "true" or env.get("GITHUB_EVENT_NAME") != "workflow_dispatch"
            or env.get("GITHUB_REF") != "refs/heads/main"
            or not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository)
            or env.get("GITHUB_WORKFLOW_REF") != workflow_ref):
        raise ProbeFailure("configuration", "main_manual_action_required")
    account, token = env.get("CLOUDFLARE_ACCOUNT_ID", ""), env.get("CLOUDFLARE_API_TOKEN", "")
    run_id, attempt, sha = env.get("GITHUB_RUN_ID", ""), env.get("GITHUB_RUN_ATTEMPT", ""), env.get("GITHUB_SHA", "")
    if (not re.fullmatch(r"[a-f0-9]{32}", account) or not token.strip() or len(token) > 1024
            or not re.fullmatch(r"[0-9]{1,20}", run_id) or not re.fullmatch(r"[0-9]{1,5}", attempt)
            or not re.fullmatch(r"[a-f0-9]{40}", sha)):
        raise ProbeFailure("configuration", "invalid_action_configuration")
    return account, token, run_id, attempt, sha


def run_probe(env: dict[str, str], session: Any = None) -> dict:
    summary = {
        "schema_version": 1, "category": "not_started", "stage": "configuration",
        "provider_host": "cdn-mineru.openxlab.org.cn", "strict_https": True,
        "provider_posts": 0, "zip_downloads": 0, "r2_writes": 0,
        "worker_created": False, "worker_deleted": False,
        "cloudflare_api_calls": 0, "worker_calls": 0,
        "cloudflare_api_methods": {"GET": 0, "PUT": 0, "POST": 0, "DELETE": 0},
        "cleanup_category": "not_needed",
    }
    worker_name = None
    creation_attempted = False
    created = False
    own_session = session is None
    account = token = None
    try:
        account, token, run_id, attempt, sha = _configuration(env)
        summary["execution_sha"] = sha
        summary["run_id"] = run_id
        summary["run_attempt"] = attempt
        source = WORKER_SOURCE.read_bytes()
        summary["worker_source_sha256"] = hashlib.sha256(source).hexdigest()
        worker_name = f"mineru-result-tls-probe-{run_id}-{attempt}-{secrets.token_hex(4)}"
        probe_token = secrets.token_hex(32)
        if session is None:
            session = requests.Session()
            session.mount("https://", HTTPAdapter(max_retries=0))

        def request(method: str, url: str, stage: str, *, api: bool = True, **kwargs):
            summary["stage"] = stage
            if api:
                summary["cloudflare_api_calls"] += 1
                summary["cloudflare_api_methods"][method] += 1
                headers = {"Authorization": f"Bearer {token}"}
            else:
                summary["worker_calls"] += 1
                headers = {"Authorization": f"Bearer {probe_token}"}
            try:
                return session.request(method, url, headers=headers, timeout=(5, 20),
                                       allow_redirects=False, verify=True, stream=True, **kwargs)
            except requests.exceptions.SSLError:
                raise ProbeFailure(stage, "tls_verification_failed") from None
            except requests.exceptions.Timeout:
                raise ProbeFailure(stage, "request_timeout") from None
            except requests.RequestException:
                raise ProbeFailure(stage, "request_failed") from None

        def api(method: str, path: str, stage: str, **kwargs) -> Any:
            response = request(method, API_ROOT + path, stage, **kwargs)
            try:
                payload = _object(response, stage)
                if not 200 <= response.status_code < 300 or payload.get("success") is not True:
                    raise ProbeFailure(stage, "cloudflare_api_rejected", response.status_code, _codes(payload))
                return payload.get("result")
            finally:
                response.close()

        account_path = f"/accounts/{account}/workers"
        result = api("GET", account_path + "/subdomain", "existing_subdomain")
        subdomain = result.get("subdomain") if isinstance(result, dict) else None
        if not isinstance(subdomain, str) or not re.fullmatch(r"[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?", subdomain):
            raise ProbeFailure("existing_subdomain", "existing_subdomain_required")
        script_path = account_path + "/scripts/" + worker_name
        response = request("GET", API_ROOT + script_path, "new_worker_absence")
        try:
            if response.status_code != 404:
                raise ProbeFailure("new_worker_absence", "new_worker_absence_unconfirmed", response.status_code)
            payload = _object(response, "new_worker_absence")
            if payload.get("success") is not False or 10007 not in _codes(payload):
                raise ProbeFailure("new_worker_absence", "new_worker_absence_unconfirmed", 404)
        finally:
            response.close()
        metadata = {
            "main_module": "index.js", "compatibility_date": "2026-10-04",
            "compatibility_flags": ["global_fetch_strictly_public", "no_cots_on_external_fetch"],
            "bindings": [{"type": "secret_text", "name": "PROBE_TOKEN", "text": probe_token}],
            "logpush": False,
            "observability": {"enabled": False},
        }
        creation_attempted = True
        api("PUT", script_path, "create_temporary_worker", files={
            "metadata": (None, json.dumps(metadata), "application/json"),
            "index.js": ("index.js", source, "application/javascript+module"),
        })
        created = True
        summary["worker_created"] = True
        api("POST", script_path + "/subdomain", "enable_temporary_worker", json={
            "enabled": True, "previews_enabled": False,
        })
        response = request("GET", f"https://{worker_name}.{subdomain}.workers.dev/probe",
                           "worker_probe", api=False)
        try:
            if response.status_code != 200:
                raise ProbeFailure("worker_probe", "worker_http_rejected", response.status_code)
            summary["probe"] = _validate_probe(_object(response, "worker_probe"))
        finally:
            response.close()
        summary["category"] = summary["probe"]["category"]
        summary["stage"] = "complete"
    except ProbeFailure as error:
        summary.update(category=error.category, stage=error.stage)
        if error.status is not None:
            summary["http_status"] = error.status
        if error.codes:
            summary["cloudflare_error_codes"] = error.codes
    except (OSError, ValueError):
        summary.update(category="invalid_local_configuration", stage="configuration")
    finally:
        if created:
            # Delete only the unique script whose successful creation this run observed.
            original_stage = summary["stage"]
            try:
                api("DELETE", f"/accounts/{account}/workers/scripts/{worker_name}", "cleanup")
                summary["worker_deleted"] = True
                summary["cleanup_category"] = "deleted"
            except ProbeFailure as error:
                summary["cleanup_category"] = error.category
                if error.status is not None:
                    summary["cleanup_http_status"] = error.status
            summary["stage"] = original_stage
        elif creation_attempted:
            summary["cleanup_category"] = "creation_not_acknowledged"
        if creation_attempted and not summary["worker_deleted"]:
            summary["preserved_worker_name_sha256"] = hashlib.sha256(worker_name.encode()).hexdigest()
        if own_session and session is not None:
            session.close()
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--summary-path", type=Path,
                        default=ROOT / "artifacts/mineru-cloudflare-tls-probe.json")
    args = parser.parse_args()
    summary = run_probe(dict(os.environ))
    args.summary_path.parent.mkdir(parents=True, exist_ok=True)
    args.summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, sort_keys=True))
    return 0 if (summary["category"] in {"https_response_received", "https_redirect_received"}
                 and summary["worker_deleted"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
