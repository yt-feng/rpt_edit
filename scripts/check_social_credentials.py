#!/usr/bin/env python3
"""Read-only health checks for social publishing credentials.

The primary checks introspect a direct LinkedIn token, signs a read-only direct
X OAuth 1.0a identity request, and refreshes a direct YouTube OAuth access token
before calling ``channels.list`` with ``mine=true``.  An optional Buffer check
verifies an account and its configured LinkedIn, X, and YouTube channels with
GraphQL queries.  It never creates, edits, schedules, or deletes social content.

Only fixed slot labels and normalized health fields are written to JSON,
email, stdout, or ``GITHUB_OUTPUT``.  API keys, OAuth credentials, account and
channel identifiers, and provider response bodies remain process-local.

Expected direct-provider secrets / variables:

* ``LINKEDIN_CLIENT_ID``, ``LINKEDIN_CLIENT_SECRET``, and
  ``LINKEDIN_ACCESS_TOKEN``; optional ``LINKEDIN_REQUIRED_SCOPES``
* ``X_API_KEY``, ``X_API_SECRET``, ``X_ACCESS_TOKEN``,
  ``X_ACCESS_TOKEN_SECRET``, and ``X_USER_ID``
* ``YOUTUBE_CLIENT_ID``, ``YOUTUBE_CLIENT_SECRET``,
  ``YOUTUBE_REFRESH_TOKEN``, and ``YOUTUBE_CHANNEL_ID``

Optional Buffer configuration (enabled when any Buffer value is present or
``BUFFER_MONITOR_ENABLED=true``):

* ``BUFFER_API_KEY`` and ``BUFFER_ACCOUNT_ID``
* ``BUFFER_LINKEDIN_CHANNEL_ID``
* ``BUFFER_X_CHANNEL_ID`` (``BUFFER_TWITTER_CHANNEL_ID`` is also accepted)
* ``BUFFER_YOUTUBE_CHANNEL_ID``

Each fixed slot accepts an optional ``*_CREDENTIAL_EXPIRES_AT`` ISO date or
timestamp and an optional non-sensitive ``*_CREDENTIAL_VERSION``.  Versions
are used only inside a one-way dedupe fingerprint so replacing a credential
can start a fresh alert window without hashing the credential itself.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import hmac
import json
import math
import os
import secrets
import sys
import time as time_module
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path
from typing import Any, Callable, Mapping
from zoneinfo import ZoneInfo


DEFAULT_BUFFER_API_URL = "https://api.buffer.com"
DEFAULT_LINKEDIN_INTROSPECTION_URL = "https://www.linkedin.com/oauth/v2/introspectToken"
DEFAULT_X_USERS_ME_URL = "https://api.x.com/2/users/me"
DEFAULT_YOUTUBE_TOKEN_URL = "https://oauth2.googleapis.com/token"
DEFAULT_YOUTUBE_API_BASE_URL = "https://www.googleapis.com/youtube/v3"
MAX_RESPONSE_BYTES = 128 * 1024
SHANGHAI = ZoneInfo("Asia/Shanghai")

THREE_DAYS = timedelta(days=3)
FOURTEEN_DAYS = timedelta(days=14)

VALID_STATUSES = frozenset(
    {
        "healthy",
        "expiring_14d",
        "expiring_3d",
        "invalid",
        "permission_denied",
        "transient",
        "missing",
    }
)

STATUS_PRIORITY = {
    "healthy": 0,
    "expiring_14d": 40,
    "transient": 55,
    "expiring_3d": 70,
    "permission_denied": 80,
    "invalid": 90,
    "missing": 100,
}

STATUS_SEVERITY = {
    "healthy": "info",
    "expiring_14d": "warning",
    "expiring_3d": "critical",
    "invalid": "critical",
    "permission_denied": "critical",
    "transient": "warning",
    "missing": "critical",
}

STATUS_TEXT = {
    "healthy": "正常",
    "expiring_14d": "14 天内到期",
    "expiring_3d": "3 天内到期",
    "invalid": "凭证或连接无效",
    "permission_denied": "权限或发布状态不满足要求",
    "transient": "暂时无法确认",
    "missing": "缺少配置",
}

REASON_TEXT = {
    "authenticated": "只读鉴权检查通过",
    "missing_configuration": "需要补充对应的 GitHub Secret 或 Variable",
    "credential_invalid": "API 已拒绝该凭证",
    "permission_denied": "API 已拒绝当前权限",
    "account_mismatch": "API key 对应的 Buffer account 与配置不一致",
    "channel_not_available": "配置的 Buffer channel 无法读取",
    "channel_disconnected": "Buffer channel 已断开连接，需要重新连接",
    "channel_locked": "Buffer channel 已锁定，当前不能发布",
    "queue_paused": "Buffer channel 队列已暂停",
    "service_mismatch": "Buffer channel 的 service 与目标平台不一致",
    "provider_response_invalid": "只读 API 返回了无法确认的结构",
    "transient_response": "服务、限流或网络响应暂时不确定",
    "oauth_refresh_invalid": "YouTube OAuth refresh 已失效，需要重新授权",
    "linkedin_token_inactive": "LinkedIn token 已失效或已撤销，需要重新授权",
    "scope_missing": "当前授权缺少发布所需 scope",
    "identity_mismatch": "只读 identity 与配置不一致",
    "youtube_channel_mismatch": "YouTube OAuth 对应的 channel 与配置不一致",
    "expiry_variable_invalid": "到期时间 Variable 格式无效",
    "credential_expired": "配置的凭证预计到期时间已过",
    "credential_expiring": "配置的凭证预计即将到期",
}

BUFFER_ACCOUNT_QUERY = """
query SocialCredentialAccount {
  account {
    id
  }
}
""".strip()

BUFFER_CHANNEL_QUERY = """
query SocialCredentialChannel($channelId: ChannelId!) {
  channel(input: {id: $channelId}) {
    id
    service
    isDisconnected
    isLocked
    isQueuePaused
  }
}
""".strip()


@dataclass(frozen=True)
class SlotSpec:
    slot: str
    display_name: str
    provider: str
    expiry_env_names: tuple[str, ...]
    version_env_names: tuple[str, ...]


@dataclass(frozen=True)
class BufferChannelSpec:
    slot: str
    display_name: str
    id_env_names: tuple[str, ...]
    expected_services: frozenset[str]


BUFFER_SLOT_SPECS = (
    SlotSpec(
        "BUFFER_ACCOUNT",
        "Buffer API / Account",
        "buffer",
        ("BUFFER_CREDENTIAL_EXPIRES_AT", "BUFFER_ACCOUNT_CREDENTIAL_EXPIRES_AT"),
        ("BUFFER_CREDENTIAL_VERSION", "BUFFER_ACCOUNT_CREDENTIAL_VERSION"),
    ),
    SlotSpec(
        "BUFFER_LINKEDIN",
        "Buffer LinkedIn Channel",
        "buffer",
        ("BUFFER_LINKEDIN_CREDENTIAL_EXPIRES_AT",),
        ("BUFFER_LINKEDIN_CREDENTIAL_VERSION",),
    ),
    SlotSpec(
        "BUFFER_X",
        "Buffer X Channel",
        "buffer",
        (
            "BUFFER_X_CREDENTIAL_EXPIRES_AT",
            "BUFFER_TWITTER_CREDENTIAL_EXPIRES_AT",
        ),
        (
            "BUFFER_X_CREDENTIAL_VERSION",
            "BUFFER_TWITTER_CREDENTIAL_VERSION",
        ),
    ),
    SlotSpec(
        "BUFFER_YOUTUBE",
        "Buffer YouTube Channel",
        "buffer",
        ("BUFFER_YOUTUBE_CREDENTIAL_EXPIRES_AT",),
        ("BUFFER_YOUTUBE_CREDENTIAL_VERSION",),
    ),
)

DIRECT_SLOT_SPECS = (
    SlotSpec(
        "LINKEDIN_DIRECT",
        "Direct LinkedIn OAuth",
        "linkedin",
        ("LINKEDIN_CREDENTIAL_EXPIRES_AT",),
        ("LINKEDIN_CREDENTIAL_VERSION",),
    ),
    SlotSpec(
        "X_DIRECT",
        "Direct X OAuth 1.0a",
        "x",
        ("X_CREDENTIAL_EXPIRES_AT", "TWITTER_CREDENTIAL_EXPIRES_AT"),
        ("X_CREDENTIAL_VERSION", "TWITTER_CREDENTIAL_VERSION"),
    ),
    SlotSpec(
        "YOUTUBE_DIRECT",
        "Direct YouTube OAuth",
        "youtube",
        ("YOUTUBE_CREDENTIAL_EXPIRES_AT", "YOUTUBE_OAUTH_CREDENTIAL_EXPIRES_AT"),
        ("YOUTUBE_CREDENTIAL_VERSION", "YOUTUBE_OAUTH_CREDENTIAL_VERSION"),
    ),
)

ALL_SLOT_SPECS = BUFFER_SLOT_SPECS + DIRECT_SLOT_SPECS
SLOT_SPEC_BY_NAME = {spec.slot: spec for spec in ALL_SLOT_SPECS}

BUFFER_CHANNEL_SPECS = (
    BufferChannelSpec(
        "BUFFER_LINKEDIN",
        "Buffer LinkedIn Channel",
        ("BUFFER_LINKEDIN_CHANNEL_ID",),
        frozenset({"linkedin"}),
    ),
    BufferChannelSpec(
        "BUFFER_X",
        "Buffer X Channel",
        ("BUFFER_X_CHANNEL_ID", "BUFFER_TWITTER_CHANNEL_ID"),
        frozenset({"x", "twitter"}),
    ),
    BufferChannelSpec(
        "BUFFER_YOUTUBE",
        "Buffer YouTube Channel",
        ("BUFFER_YOUTUBE_CHANNEL_ID",),
        frozenset({"youtube"}),
    ),
)


@dataclass(frozen=True)
class HttpJsonResult:
    status: int | None
    payload: Any
    transport_error: bool = False


@dataclass(frozen=True)
class ProbeResult:
    status: str
    reason: str
    http_status: int | None = None
    expires_at: datetime | None = None

    def __post_init__(self) -> None:
        if self.status not in VALID_STATUSES:
            raise ValueError(f"unsupported status: {self.status}")


@dataclass(frozen=True)
class CheckResult:
    slot: str
    display_name: str
    provider: str
    status: str
    severity: str
    reason: str
    http_status: int | None
    expires_at: str
    days_remaining: int | None


@dataclass(frozen=True)
class MonitorReport:
    checked_at: str
    check_count: int
    configured_count: int
    issue_count: int
    should_alert: bool
    alert_stage: str
    severity: str
    subject: str
    dedupe_key: str
    checks: tuple[CheckResult, ...]


def _first_env(env: Mapping[str, str], names: tuple[str, ...]) -> str:
    for name in names:
        value = (env.get(name) or "").strip()
        if value:
            return value
    return ""


def _validated_http_url(value: str) -> str | None:
    try:
        parsed = urllib.parse.urlparse(value)
    except ValueError:
        return None
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return None
    if parsed.username or parsed.password:
        return None
    return value


def _decode_json(body: bytes) -> Any:
    try:
        return json.loads(body.decode("utf-8"))
    except (UnicodeError, json.JSONDecodeError):
        return None


def request_json(
    url: str,
    *,
    method: str,
    headers: Mapping[str, str],
    body: bytes | None,
    timeout: float,
    opener: Callable[..., Any] | None = None,
) -> HttpJsonResult:
    """Return bounded JSON without retaining or reporting exception text."""

    if not _validated_http_url(url):
        return HttpJsonResult(None, None, True)
    request = urllib.request.Request(
        url,
        data=body,
        headers=dict(headers),
        method=method,
    )
    open_request = opener or urllib.request.urlopen
    try:
        with open_request(request, timeout=timeout) as response:
            status = int(response.getcode())
            payload = _decode_json(response.read(MAX_RESPONSE_BYTES))
        return HttpJsonResult(status, payload)
    except urllib.error.HTTPError as error:
        try:
            payload = _decode_json(error.read(MAX_RESPONSE_BYTES))
        except Exception:  # noqa: BLE001 - status is still safe to classify.
            payload = None
        return HttpJsonResult(int(error.code), payload)
    except (urllib.error.URLError, TimeoutError, OSError, ValueError):
        return HttpJsonResult(None, None, True)


def _error_tokens(payload: Any) -> set[str]:
    """Extract only normalized auth/error categories for in-process classification."""

    if not isinstance(payload, dict):
        return set()
    candidates: list[Any] = []
    errors = payload.get("errors")
    if isinstance(errors, list):
        candidates.extend(errors)
    elif errors is not None:
        candidates.append(errors)
    if payload.get("error") is not None:
        candidates.append(payload.get("error"))

    tokens: set[str] = set()
    for candidate in candidates:
        if isinstance(candidate, dict):
            extensions = candidate.get("extensions")
            values = [candidate.get("code"), candidate.get("error")]
            if isinstance(extensions, dict):
                values.extend((extensions.get("code"), extensions.get("error")))
        else:
            values = [candidate]
        for value in values:
            if value is None:
                continue
            normalized = "".join(ch for ch in str(value).casefold() if ch.isalnum() or ch == "_")
            if normalized:
                tokens.add(normalized)
    return tokens


def _classify_api_envelope(result: HttpJsonResult, *, not_found_is_invalid: bool = False) -> ProbeResult | None:
    if result.transport_error or result.status is None:
        return ProbeResult("transient", "transient_response", None)
    if result.status == 401:
        return ProbeResult("invalid", "credential_invalid", result.status)
    if result.status == 403:
        return ProbeResult("permission_denied", "permission_denied", result.status)
    if result.status == 429 or result.status >= 500:
        return ProbeResult("transient", "transient_response", result.status)
    if not 200 <= result.status < 300:
        return ProbeResult("transient", "provider_response_invalid", result.status)
    if not isinstance(result.payload, dict):
        return ProbeResult("transient", "provider_response_invalid", result.status)

    tokens = _error_tokens(result.payload)
    if tokens:
        if tokens & {
            "unauthorized",
            "unauthenticated",
            "authentication_error",
            "invalid_token",
            "invalid_api_key",
        }:
            return ProbeResult("invalid", "credential_invalid", result.status)
        if tokens & {
            "forbidden",
            "permission_denied",
            "access_denied",
            "insufficient_permissions",
        }:
            return ProbeResult("permission_denied", "permission_denied", result.status)
        if not_found_is_invalid and tokens & {"not_found", "channel_not_found"}:
            return ProbeResult("invalid", "channel_not_available", result.status)
        return ProbeResult("transient", "provider_response_invalid", result.status)
    return None


def _graphql_call(
    api_url: str,
    api_key: str,
    query: str,
    variables: Mapping[str, str] | None,
    *,
    timeout: float,
    opener: Callable[..., Any] | None,
) -> HttpJsonResult:
    body = json.dumps(
        {"query": query, "variables": dict(variables or {})},
        ensure_ascii=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return request_json(
        api_url,
        method="POST",
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
            "User-Agent": "portal-suite-social-credential-monitor/1.0",
        },
        body=body,
        timeout=timeout,
        opener=opener,
    )


def _normalized_service(value: Any) -> str:
    return "".join(ch for ch in str(value or "").casefold() if ch.isalnum())


def classify_buffer_channel(
    channel: Any,
    *,
    expected_id: str,
    expected_services: frozenset[str],
    http_status: int | None = 200,
) -> ProbeResult:
    if not isinstance(channel, dict):
        return ProbeResult("transient", "provider_response_invalid", http_status)
    if str(channel.get("id") or "") != expected_id:
        return ProbeResult("invalid", "channel_not_available", http_status)
    service = _normalized_service(channel.get("service"))
    if service not in {_normalized_service(value) for value in expected_services}:
        return ProbeResult("permission_denied", "service_mismatch", http_status)
    flag_names = ("isDisconnected", "isLocked", "isQueuePaused")
    if any(type(channel.get(name)) is not bool for name in flag_names):
        return ProbeResult("transient", "provider_response_invalid", http_status)
    if channel["isDisconnected"]:
        return ProbeResult("invalid", "channel_disconnected", http_status)
    if channel["isLocked"]:
        return ProbeResult("permission_denied", "channel_locked", http_status)
    if channel["isQueuePaused"]:
        return ProbeResult("permission_denied", "queue_paused", http_status)
    return ProbeResult("healthy", "authenticated", http_status)


def probe_buffer_credentials(
    env: Mapping[str, str],
    *,
    api_url: str = DEFAULT_BUFFER_API_URL,
    timeout: float = 20,
    opener: Callable[..., Any] | None = None,
) -> dict[str, ProbeResult]:
    """Query Buffer account/channel state without any GraphQL mutation."""

    results: dict[str, ProbeResult] = {}
    api_key = (env.get("BUFFER_API_KEY") or "").strip()
    expected_account_id = (env.get("BUFFER_ACCOUNT_ID") or "").strip()
    channel_ids = {
        spec.slot: _first_env(env, spec.id_env_names)
        for spec in BUFFER_CHANNEL_SPECS
    }

    for spec in BUFFER_CHANNEL_SPECS:
        if not channel_ids[spec.slot]:
            results[spec.slot] = ProbeResult("missing", "missing_configuration")

    if not api_key or not expected_account_id:
        account_result = ProbeResult("missing", "missing_configuration")
        results["BUFFER_ACCOUNT"] = account_result
        for spec in BUFFER_CHANNEL_SPECS:
            if channel_ids[spec.slot]:
                results[spec.slot] = account_result
        return results

    account_response = _graphql_call(
        api_url,
        api_key,
        BUFFER_ACCOUNT_QUERY,
        None,
        timeout=timeout,
        opener=opener,
    )
    account_issue = _classify_api_envelope(account_response)
    if account_issue is not None:
        account_result = account_issue
    else:
        data = account_response.payload.get("data")
        account = data.get("account") if isinstance(data, dict) else None
        account_id = account.get("id") if isinstance(account, dict) else None
        if not isinstance(account_id, str) or not account_id:
            account_result = ProbeResult(
                "transient",
                "provider_response_invalid",
                account_response.status,
            )
        elif account_id != expected_account_id:
            account_result = ProbeResult(
                "permission_denied",
                "account_mismatch",
                account_response.status,
            )
        else:
            account_result = ProbeResult("healthy", "authenticated", account_response.status)
    results["BUFFER_ACCOUNT"] = account_result

    if account_result.status != "healthy":
        for spec in BUFFER_CHANNEL_SPECS:
            if channel_ids[spec.slot]:
                results[spec.slot] = ProbeResult(
                    account_result.status,
                    account_result.reason,
                    account_result.http_status,
                )
        return results

    for spec in BUFFER_CHANNEL_SPECS:
        channel_id = channel_ids[spec.slot]
        if not channel_id:
            continue
        response = _graphql_call(
            api_url,
            api_key,
            BUFFER_CHANNEL_QUERY,
            {"channelId": channel_id},
            timeout=timeout,
            opener=opener,
        )
        issue = _classify_api_envelope(response, not_found_is_invalid=True)
        if issue is not None:
            results[spec.slot] = issue
            continue
        data = response.payload.get("data")
        channel = data.get("channel") if isinstance(data, dict) else None
        results[spec.slot] = classify_buffer_channel(
            channel,
            expected_id=channel_id,
            expected_services=spec.expected_services,
            http_status=response.status,
        )
    return results


def _scope_set(value: Any) -> set[str]:
    if isinstance(value, list):
        raw_values = [str(item) for item in value]
    else:
        raw_values = str(value or "").replace(",", " ").split()
    return {
        item.strip().casefold()
        for item in raw_values
        if item.strip()
    }


def _x_scope_set(value: Any) -> set[str]:
    scopes = _scope_set(value)
    compact = {scope.replace("-", "").replace("_", "") for scope in scopes}
    if compact & {"readwrite", "readandwrite"}:
        scopes.update({"read", "write"})
    return scopes


def probe_direct_linkedin(
    env: Mapping[str, str],
    *,
    introspection_url: str = DEFAULT_LINKEDIN_INTROSPECTION_URL,
    timeout: float = 20,
    opener: Callable[..., Any] | None = None,
) -> ProbeResult:
    """Introspect a LinkedIn token and verify its active state, TTL, and scopes."""

    client_id = (env.get("LINKEDIN_CLIENT_ID") or "").strip()
    client_secret = (env.get("LINKEDIN_CLIENT_SECRET") or "").strip()
    access_token = (env.get("LINKEDIN_ACCESS_TOKEN") or "").strip()
    if not all((client_id, client_secret, access_token)):
        return ProbeResult("missing", "missing_configuration")
    required_scopes = _scope_set(env.get("LINKEDIN_REQUIRED_SCOPES") or "w_member_social")
    body = urllib.parse.urlencode(
        {
            "client_id": client_id,
            "client_secret": client_secret,
            "token": access_token,
        }
    ).encode("utf-8")
    response = request_json(
        introspection_url,
        method="POST",
        headers={
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "portal-suite-social-credential-monitor/1.0",
        },
        body=body,
        timeout=timeout,
        opener=opener,
    )
    if response.transport_error or response.status is None:
        return ProbeResult("transient", "transient_response")
    if response.status in {400, 401}:
        return ProbeResult("invalid", "credential_invalid", response.status)
    if response.status == 403:
        return ProbeResult("permission_denied", "permission_denied", response.status)
    if response.status == 429 or response.status >= 500:
        return ProbeResult("transient", "transient_response", response.status)
    if not 200 <= response.status < 300 or not isinstance(response.payload, dict):
        return ProbeResult("transient", "provider_response_invalid", response.status)

    active = response.payload.get("active")
    token_status = str(response.payload.get("status") or "").strip().casefold()
    if type(active) is not bool:
        return ProbeResult("transient", "provider_response_invalid", response.status)
    if not active or token_status in {"revoked", "expired", "inactive"}:
        return ProbeResult("invalid", "linkedin_token_inactive", response.status)
    returned_client_id = response.payload.get("client_id")
    if returned_client_id is not None and str(returned_client_id) != client_id:
        return ProbeResult("invalid", "credential_invalid", response.status)
    granted_scopes = _scope_set(response.payload.get("scope"))
    if required_scopes and not required_scopes.issubset(granted_scopes):
        return ProbeResult("permission_denied", "scope_missing", response.status)

    expiry: datetime | None = None
    expires_at = response.payload.get("expires_at")
    if expires_at is not None:
        if isinstance(expires_at, bool) or not isinstance(expires_at, (int, float)):
            return ProbeResult("transient", "provider_response_invalid", response.status)
        try:
            expiry = datetime.fromtimestamp(float(expires_at), tz=timezone.utc)
        except (OverflowError, OSError, ValueError):
            return ProbeResult("transient", "provider_response_invalid", response.status)
    return ProbeResult("healthy", "authenticated", response.status, expiry)


def _oauth_quote(value: Any) -> str:
    return urllib.parse.quote(str(value), safe="~-._")


def oauth1_authorization_header(
    method: str,
    url: str,
    *,
    consumer_key: str,
    consumer_secret: str,
    access_token: str,
    access_token_secret: str,
    nonce: str,
    timestamp: int,
) -> str:
    """Create an RFC 5849 HMAC-SHA1 Authorization header."""

    parsed = urllib.parse.urlparse(url)
    base_url = urllib.parse.urlunparse((parsed.scheme, parsed.netloc, parsed.path, "", "", ""))
    oauth_params = {
        "oauth_consumer_key": consumer_key,
        "oauth_nonce": nonce,
        "oauth_signature_method": "HMAC-SHA1",
        "oauth_timestamp": str(int(timestamp)),
        "oauth_token": access_token,
        "oauth_version": "1.0",
    }
    signature_params: list[tuple[str, str]] = [
        (str(key), str(value))
        for key, value in urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    ]
    signature_params.extend(oauth_params.items())
    normalized = "&".join(
        f"{_oauth_quote(key)}={_oauth_quote(value)}"
        for key, value in sorted(
            signature_params,
            key=lambda row: (_oauth_quote(row[0]), _oauth_quote(row[1])),
        )
    )
    base_string = "&".join(
        (_oauth_quote(method.upper()), _oauth_quote(base_url), _oauth_quote(normalized))
    )
    signing_key = f"{_oauth_quote(consumer_secret)}&{_oauth_quote(access_token_secret)}"
    signature = base64.b64encode(
        hmac.new(
            signing_key.encode("utf-8"),
            base_string.encode("utf-8"),
            hashlib.sha1,
        ).digest()
    ).decode("ascii")
    oauth_params["oauth_signature"] = signature
    rendered = ", ".join(
        f'{_oauth_quote(key)}="{_oauth_quote(value)}"'
        for key, value in sorted(oauth_params.items())
    )
    return f"OAuth {rendered}"


def probe_direct_x(
    env: Mapping[str, str],
    *,
    users_me_url: str = DEFAULT_X_USERS_ME_URL,
    timeout: float = 20,
    opener: Callable[..., Any] | None = None,
    nonce_func: Callable[[], str] | None = None,
    timestamp_func: Callable[[], int] | None = None,
) -> ProbeResult:
    """Sign one read-only OAuth 1.0a ``GET /2/users/me`` identity request."""

    consumer_key = _first_env(env, ("X_API_KEY", "X_CONSUMER_KEY", "TWITTER_API_KEY"))
    consumer_secret = _first_env(
        env,
        ("X_API_SECRET", "X_API_KEY_SECRET", "X_CONSUMER_SECRET", "TWITTER_API_SECRET"),
    )
    access_token = _first_env(env, ("X_ACCESS_TOKEN", "TWITTER_ACCESS_TOKEN"))
    access_token_secret = _first_env(
        env,
        ("X_ACCESS_TOKEN_SECRET", "TWITTER_ACCESS_TOKEN_SECRET"),
    )
    expected_user_id = _first_env(env, ("X_USER_ID", "TWITTER_USER_ID"))
    if not all((consumer_key, consumer_secret, access_token, access_token_secret, expected_user_id)):
        return ProbeResult("missing", "missing_configuration")

    declared_scopes = _x_scope_set(
        _first_env(env, ("X_OAUTH1_SCOPES", "X_APP_PERMISSIONS", "TWITTER_APP_PERMISSIONS"))
    )
    required_scopes = _x_scope_set(env.get("X_REQUIRED_SCOPES") or "read write")
    if not declared_scopes:
        return ProbeResult("missing", "missing_configuration")
    if not required_scopes.issubset(declared_scopes):
        return ProbeResult("permission_denied", "scope_missing")

    nonce = (nonce_func or (lambda: secrets.token_urlsafe(18)))()
    timestamp = (timestamp_func or (lambda: int(time_module.time())))()
    authorization = oauth1_authorization_header(
        "GET",
        users_me_url,
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
        nonce=nonce,
        timestamp=timestamp,
    )
    response = request_json(
        users_me_url,
        method="GET",
        headers={
            "Accept": "application/json",
            "Authorization": authorization,
            "User-Agent": "portal-suite-social-credential-monitor/1.0",
        },
        body=None,
        timeout=timeout,
        opener=opener,
    )
    if response.transport_error or response.status is None:
        return ProbeResult("transient", "transient_response")
    if response.status == 401:
        return ProbeResult("invalid", "credential_invalid", response.status)
    if response.status == 403:
        return ProbeResult("permission_denied", "permission_denied", response.status)
    if response.status == 429 or response.status >= 500:
        return ProbeResult("transient", "transient_response", response.status)
    if not 200 <= response.status < 300 or not isinstance(response.payload, dict):
        return ProbeResult("transient", "provider_response_invalid", response.status)
    data = response.payload.get("data")
    returned_user_id = data.get("id") if isinstance(data, dict) else None
    if not isinstance(returned_user_id, str) or not returned_user_id:
        return ProbeResult("transient", "provider_response_invalid", response.status)
    if returned_user_id != expected_user_id:
        return ProbeResult("permission_denied", "identity_mismatch", response.status)
    return ProbeResult("healthy", "authenticated", response.status)


def _youtube_error_value(payload: Any) -> str:
    if not isinstance(payload, dict):
        return ""
    value = payload.get("error")
    if isinstance(value, dict):
        value = value.get("status") or value.get("code")
    return "".join(ch for ch in str(value or "").casefold() if ch.isalnum() or ch == "_")


def _classify_youtube_http(result: HttpJsonResult, *, refresh: bool) -> ProbeResult | None:
    if result.transport_error or result.status is None:
        return ProbeResult("transient", "transient_response", None)
    error_value = _youtube_error_value(result.payload)
    if result.status == 401:
        return ProbeResult("invalid", "credential_invalid", result.status)
    if result.status == 403:
        return ProbeResult("permission_denied", "permission_denied", result.status)
    if result.status == 429 or result.status >= 500:
        return ProbeResult("transient", "transient_response", result.status)
    if not 200 <= result.status < 300:
        if refresh and error_value in {
            "invalid_grant",
            "invalid_client",
            "unauthorized_client",
        }:
            return ProbeResult("invalid", "oauth_refresh_invalid", result.status)
        if error_value in {"access_denied", "insufficientpermissions", "permission_denied"}:
            return ProbeResult("permission_denied", "permission_denied", result.status)
        return ProbeResult("transient", "provider_response_invalid", result.status)
    if not isinstance(result.payload, dict):
        return ProbeResult("transient", "provider_response_invalid", result.status)
    return None


def probe_direct_youtube(
    env: Mapping[str, str],
    *,
    token_url: str = DEFAULT_YOUTUBE_TOKEN_URL,
    api_base_url: str = DEFAULT_YOUTUBE_API_BASE_URL,
    timeout: float = 20,
    opener: Callable[..., Any] | None = None,
) -> ProbeResult:
    """Refresh OAuth and call ``channels.list``; no upload or mutation occurs."""

    client_id = _first_env(env, ("YOUTUBE_CLIENT_ID", "YOUTUBE_OAUTH_CLIENT_ID"))
    client_secret = _first_env(env, ("YOUTUBE_CLIENT_SECRET", "YOUTUBE_OAUTH_CLIENT_SECRET"))
    refresh_token = _first_env(env, ("YOUTUBE_REFRESH_TOKEN", "YOUTUBE_OAUTH_REFRESH_TOKEN"))
    expected_channel_id = _first_env(env, ("YOUTUBE_CHANNEL_ID", "YOUTUBE_OAUTH_CHANNEL_ID"))
    if not all((client_id, client_secret, refresh_token, expected_channel_id)):
        return ProbeResult("missing", "missing_configuration")

    body = urllib.parse.urlencode(
        {
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh_token,
            "grant_type": "refresh_token",
        }
    ).encode("ascii")
    refreshed = request_json(
        token_url,
        method="POST",
        headers={
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "portal-suite-social-credential-monitor/1.0",
        },
        body=body,
        timeout=timeout,
        opener=opener,
    )
    issue = _classify_youtube_http(refreshed, refresh=True)
    if issue is not None:
        return issue
    access_token = refreshed.payload.get("access_token")
    if not isinstance(access_token, str) or not access_token:
        return ProbeResult("transient", "provider_response_invalid", refreshed.status)
    required_scopes = _scope_set(
        env.get("YOUTUBE_REQUIRED_SCOPES")
        or "https://www.googleapis.com/auth/youtube.upload"
    )
    granted_scopes = _scope_set(refreshed.payload.get("scope"))
    if not required_scopes.issubset(granted_scopes):
        return ProbeResult("permission_denied", "scope_missing", refreshed.status)

    query = urllib.parse.urlencode(
        {"part": "id", "mine": "true", "maxResults": "50"}
    )
    listed = request_json(
        f"{api_base_url.rstrip('/')}/channels?{query}",
        method="GET",
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {access_token}",
            "User-Agent": "portal-suite-social-credential-monitor/1.0",
        },
        body=None,
        timeout=timeout,
        opener=opener,
    )
    issue = _classify_youtube_http(listed, refresh=False)
    if issue is not None:
        return issue
    items = listed.payload.get("items")
    if not isinstance(items, list):
        return ProbeResult("transient", "provider_response_invalid", listed.status)
    returned_ids = {
        str(item.get("id"))
        for item in items
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }
    if expected_channel_id not in returned_ids:
        return ProbeResult("permission_denied", "youtube_channel_mismatch", listed.status)
    return ProbeResult("healthy", "authenticated", listed.status)


def parse_explicit_expiry(value: str) -> datetime:
    """Parse ISO date/time; a date-only value means end-of-day in Beijing."""

    normalized = value.strip()
    if not normalized:
        raise ValueError("empty expiry")
    try:
        if len(normalized) == 10:
            parsed_date = date.fromisoformat(normalized)
            return datetime.combine(parsed_date, time(23, 59, 59), tzinfo=SHANGHAI)
        if normalized.endswith("Z"):
            normalized = f"{normalized[:-1]}+00:00"
        parsed = datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise ValueError("expiry must be an ISO date or timestamp") from exc
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=SHANGHAI)
    return parsed


def evaluate_expiry(
    value: str,
    *,
    now: datetime,
) -> tuple[str | None, datetime | None, int | None, str | None]:
    if not value.strip():
        return None, None, None, None
    try:
        expiry = parse_explicit_expiry(value)
    except ValueError:
        return "invalid", None, None, "expiry_variable_invalid"
    remaining = expiry.astimezone(timezone.utc) - now.astimezone(timezone.utc)
    seconds = remaining.total_seconds()
    days_remaining = math.ceil(seconds / 86400)
    if seconds <= 0:
        return "invalid", expiry, days_remaining, "credential_expired"
    if remaining <= THREE_DAYS:
        return "expiring_3d", expiry, days_remaining, "credential_expiring"
    if remaining <= FOURTEEN_DAYS:
        return "expiring_14d", expiry, days_remaining, "credential_expiring"
    return "healthy", expiry, days_remaining, None


def _iso_utc(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def _slot_variable(env: Mapping[str, str], slot: str, kind: str) -> str:
    spec = SLOT_SPEC_BY_NAME[slot]
    names = spec.expiry_env_names if kind == "expiry" else spec.version_env_names
    return _first_env(env, names)


def combine_probe_and_expiry(
    spec: SlotSpec,
    probe: ProbeResult,
    env: Mapping[str, str],
    *,
    now: datetime,
) -> CheckResult:
    expiry_value = (
        probe.expires_at.isoformat()
        if probe.expires_at is not None
        else _slot_variable(env, spec.slot, "expiry")
    )
    expiry_status, expiry, days_remaining, expiry_reason = evaluate_expiry(expiry_value, now=now)
    candidates = [(probe.status, probe.reason)]
    if expiry_status and expiry_status != "healthy":
        candidates.append((expiry_status, expiry_reason or "credential_expiring"))
    status, reason = max(candidates, key=lambda row: STATUS_PRIORITY[row[0]])
    return CheckResult(
        slot=spec.slot,
        display_name=spec.display_name,
        provider=spec.provider,
        status=status,
        severity=STATUS_SEVERITY[status],
        reason=reason,
        http_status=probe.http_status,
        expires_at=_iso_utc(expiry) if expiry else "",
        days_remaining=days_remaining,
    )


def _dedupe_key(
    alert_stage: str,
    checks: tuple[CheckResult, ...],
    env: Mapping[str, str],
) -> str:
    affected = [row for row in checks if row.status != "healthy"] or list(checks)
    material = "|".join(
        f"{row.slot}:{row.status}:{row.reason}:"
        f"{_slot_variable(env, row.slot, 'version') or '0'}:"
        f"{row.expires_at or 'none'}"
        for row in affected
    )
    digest = hashlib.sha256(material.encode("utf-8")).hexdigest()[:16]
    return f"social-credential-monitor:{alert_stage}:{digest}"


def _subject(alert_stage: str, issue_count: int, check_count: int, force_email: bool) -> str:
    if issue_count:
        return f"[Portal Operations] 社媒发布凭证检查：{issue_count} 项需要处理"
    if force_email:
        return f"[Portal Operations 测试] 社媒发布凭证检查正常（{check_count} 项）"
    return f"[Portal Operations] 社媒发布凭证检查正常（{check_count} 项）"


def buffer_monitor_requested(env: Mapping[str, str]) -> bool:
    explicit = (env.get("BUFFER_MONITOR_ENABLED") or "").strip().casefold()
    if explicit:
        return explicit in {"1", "true", "yes", "on"}
    names = {
        "BUFFER_API_KEY",
        "BUFFER_ACCOUNT_ID",
        *(name for spec in BUFFER_CHANNEL_SPECS for name in spec.id_env_names),
    }
    return any((env.get(name) or "").strip() for name in names)


def run_monitor(
    env: Mapping[str, str],
    *,
    now: datetime | None = None,
    force_email: bool = False,
    buffer_api_url: str = DEFAULT_BUFFER_API_URL,
    linkedin_introspection_url: str = DEFAULT_LINKEDIN_INTROSPECTION_URL,
    x_users_me_url: str = DEFAULT_X_USERS_ME_URL,
    youtube_token_url: str = DEFAULT_YOUTUBE_TOKEN_URL,
    youtube_api_base_url: str = DEFAULT_YOUTUBE_API_BASE_URL,
    timeout: float = 20,
    buffer_probe_func: Callable[..., dict[str, ProbeResult]] | None = None,
    linkedin_probe_func: Callable[..., ProbeResult] | None = None,
    x_probe_func: Callable[..., ProbeResult] | None = None,
    youtube_probe_func: Callable[..., ProbeResult] | None = None,
) -> MonitorReport:
    checked_at = now or datetime.now(timezone.utc)
    if checked_at.tzinfo is None:
        checked_at = checked_at.replace(tzinfo=timezone.utc)
    buffer_probe = buffer_probe_func or probe_buffer_credentials
    linkedin_probe = linkedin_probe_func or probe_direct_linkedin
    x_probe = x_probe_func or probe_direct_x
    youtube_probe = youtube_probe_func or probe_direct_youtube
    probes: dict[str, ProbeResult] = {}
    active_specs: tuple[SlotSpec, ...] = DIRECT_SLOT_SPECS
    probes["LINKEDIN_DIRECT"] = linkedin_probe(
        env,
        introspection_url=linkedin_introspection_url,
        timeout=timeout,
    )
    probes["X_DIRECT"] = x_probe(
        env,
        users_me_url=x_users_me_url,
        timeout=timeout,
    )
    probes["YOUTUBE_DIRECT"] = youtube_probe(
        env,
        token_url=youtube_token_url,
        api_base_url=youtube_api_base_url,
        timeout=timeout,
    )
    if buffer_monitor_requested(env):
        active_specs = DIRECT_SLOT_SPECS + BUFFER_SLOT_SPECS
        probes.update(
            buffer_probe(
                env,
                api_url=buffer_api_url,
                timeout=timeout,
            )
        )
    checks = tuple(
        combine_probe_and_expiry(
            spec,
            probes.get(spec.slot, ProbeResult("transient", "provider_response_invalid")),
            env,
            now=checked_at,
        )
        for spec in active_specs
    )
    issue_count = sum(row.status != "healthy" for row in checks)
    configured_count = sum(row.status != "missing" for row in checks)
    alert_stage = max(
        (row.status for row in checks),
        key=lambda status: STATUS_PRIORITY[status],
    )
    should_alert = bool(issue_count or force_email)
    severity = STATUS_SEVERITY[alert_stage] if issue_count else "info"
    return MonitorReport(
        checked_at=_iso_utc(checked_at),
        check_count=len(checks),
        configured_count=configured_count,
        issue_count=issue_count,
        should_alert=should_alert,
        alert_stage=alert_stage,
        severity=severity,
        subject=_subject(alert_stage, issue_count, len(checks), force_email),
        dedupe_key=_dedupe_key(alert_stage, checks, env),
        checks=checks,
    )


def _expiry_text(row: CheckResult) -> str:
    if not row.expires_at:
        return "未配置预计到期时间"
    expiry = datetime.fromisoformat(row.expires_at.replace("Z", "+00:00")).astimezone(SHANGHAI)
    rendered = expiry.strftime("%Y-%m-%d %H:%M %Z")
    if row.days_remaining is None:
        return rendered
    if row.days_remaining <= 0:
        return f"{rendered}（已到期）"
    return f"{rendered}（约 {row.days_remaining} 天后）"


def render_email(report: MonitorReport, env: Mapping[str, str]) -> str:
    lines = [
        "社媒发布凭证定期检查结果如下。邮件不包含 token、API key、账号 ID、channel ID 或 provider 原始响应。",
        "",
        f"检查时间：{report.checked_at}",
        f"检查项：{report.check_count}",
        f"已完整配置：{report.configured_count}",
        f"需要处理：{report.issue_count}",
        f"提醒阶段：{report.alert_stage}",
        "",
        "检查结果：",
    ]
    for row in report.checks:
        lines.extend(
            [
                f"- {row.display_name}（{row.slot}）：{STATUS_TEXT[row.status]}",
                f"  说明：{REASON_TEXT.get(row.reason, '需要查看本次 GitHub Actions 运行')}",
                f"  到期时间：{_expiry_text(row)}",
            ]
        )
    lines.extend(
        [
            "",
            "处理方式：",
            "1. 打开 GitHub 仓库 Settings → Secrets and variables → Actions。",
            "2. Buffer 项异常时，在 Buffer 内重新连接对应平台，并同步更新对应 channel Secret。",
            "3. Direct LinkedIn 异常时，重新授权并确认发布 scope；Direct X 异常时确认 App 为 read/write 并替换 OAuth 1.0a credentials。",
            "4. Direct YouTube OAuth 异常时，重新授权并替换 Refresh Token。",
            "5. 更换凭证时同步更新 *_CREDENTIAL_EXPIRES_AT；如需开启新的提醒窗口，将 *_CREDENTIAL_VERSION 加 1。",
        ]
    )
    server = (env.get("GITHUB_SERVER_URL") or "").rstrip("/")
    repository = (env.get("GITHUB_REPOSITORY") or "").strip("/")
    run_id = (env.get("GITHUB_RUN_ID") or "").strip()
    if server and repository and run_id:
        lines.extend(["", f"本次运行：{server}/{repository}/actions/runs/{run_id}"])
    return "\n".join(lines).strip() + "\n"


def report_payload(report: MonitorReport) -> dict[str, Any]:
    payload = asdict(report)
    payload["checks"] = [asdict(row) for row in report.checks]
    return payload


def write_github_output(
    path: Path | None,
    report: MonitorReport,
    email_path: Path,
    json_path: Path,
) -> None:
    if path is None:
        return
    values = {
        "should_alert": str(report.should_alert).lower(),
        "alert_stage": report.alert_stage,
        "severity": report.severity,
        "subject": report.subject,
        "dedupe_key": report.dedupe_key,
        "check_count": str(report.check_count),
        "configured_count": str(report.configured_count),
        "issue_count": str(report.issue_count),
        "email_file": str(email_path),
        "json_file": str(json_path),
    }
    with path.open("a", encoding="utf-8") as handle:
        for key, value in values.items():
            if "\n" in value or "\r" in value:
                raise ValueError(f"GitHub output {key} must be one line")
            handle.write(f"{key}={value}\n")


def parse_now(value: str) -> datetime:
    normalized = value.strip()
    if normalized.endswith("Z"):
        normalized = f"{normalized[:-1]}+00:00"
    parsed = datetime.fromisoformat(normalized)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check direct LinkedIn, X, and YouTube credentials plus optional Buffer"
    )
    parser.add_argument(
        "--buffer-api-url",
        default=os.environ.get("BUFFER_GRAPHQL_URL", DEFAULT_BUFFER_API_URL),
    )
    parser.add_argument(
        "--linkedin-introspection-url",
        default=os.environ.get(
            "LINKEDIN_INTROSPECTION_URL",
            DEFAULT_LINKEDIN_INTROSPECTION_URL,
        ),
    )
    parser.add_argument(
        "--x-users-me-url",
        default=os.environ.get("X_USERS_ME_URL", DEFAULT_X_USERS_ME_URL),
    )
    parser.add_argument(
        "--youtube-token-url",
        default=os.environ.get("YOUTUBE_TOKEN_URL", DEFAULT_YOUTUBE_TOKEN_URL),
    )
    parser.add_argument(
        "--youtube-api-base-url",
        default=os.environ.get("YOUTUBE_API_BASE_URL", DEFAULT_YOUTUBE_API_BASE_URL),
    )
    parser.add_argument("--timeout", type=float, default=20)
    parser.add_argument("--force-email", action="store_true")
    parser.add_argument("--now", help=argparse.SUPPRESS)
    parser.add_argument("--json-output", type=Path, required=True)
    parser.add_argument("--email-output", type=Path, required=True)
    parser.add_argument(
        "--github-output",
        type=Path,
        default=Path(os.environ["GITHUB_OUTPUT"]) if os.environ.get("GITHUB_OUTPUT") else None,
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    now = parse_now(args.now) if args.now else None
    report = run_monitor(
        os.environ,
        now=now,
        force_email=args.force_email,
        buffer_api_url=args.buffer_api_url,
        linkedin_introspection_url=args.linkedin_introspection_url,
        x_users_me_url=args.x_users_me_url,
        youtube_token_url=args.youtube_token_url,
        youtube_api_base_url=args.youtube_api_base_url,
        timeout=args.timeout,
    )
    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.email_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(
        json.dumps(report_payload(report), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    args.email_output.write_text(render_email(report, os.environ), encoding="utf-8")
    write_github_output(args.github_output, report, args.email_output, args.json_output)
    print(
        "Social credential monitor complete: "
        f"configured={report.configured_count}, issues={report.issue_count}, "
        f"stage={report.alert_stage}, alert={str(report.should_alert).lower()}"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001 - never print provider/body/credential detail.
        print(f"Social credential monitor failed: {type(exc).__name__}", file=sys.stderr)
        raise SystemExit(1)
