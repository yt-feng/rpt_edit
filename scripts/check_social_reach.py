#!/usr/bin/env python3
"""Read-only reach checks for successful social publishing receipts.

The monitor reads schema-v1 receipts from ``social_publish/receipts`` and
queries only provider read endpoints.  It intentionally separates an explicit
zero metric from unsupported, missing, malformed, and temporarily unavailable
metrics: only a confirmed zero at the 24-hour checkpoint sets
``should_alert``.  The 1-hour checkpoint is report-only.

Provider URLs are configurable for deterministic network mocking:

* ``YOUTUBE_VIDEOS_URL`` (or ``YOUTUBE_API_BASE_URL`` + ``/videos``)
* ``YOUTUBE_TOKEN_URL`` for an optional refresh-token exchange
* ``X_TWEET_LOOKUP_URL_TEMPLATE`` (or ``X_API_BASE_URL``)
* ``LINKEDIN_ANALYTICS_URL_TEMPLATE`` / ``LINKEDIN_ANALYTICS_ENDPOINT``

YouTube accepts ``YOUTUBE_API_KEY``, an explicit ``YOUTUBE_ACCESS_TOKEN``, or
the publisher's existing ``YOUTUBE_CLIENT_ID`` / ``YOUTUBE_CLIENT_SECRET`` /
``YOUTUBE_REFRESH_TOKEN`` set.  X reads the existing ``X_API_KEY``,
``X_API_SECRET``, ``X_ACCESS_TOKEN``, and ``X_ACCESS_TOKEN_SECRET`` via OAuth
1.0a.  LinkedIn additionally requires ``LINKEDIN_ANALYTICS_PERMISSION`` (or
``LINKEDIN_ANALYTICS_PERMISSION_GRANTED=true``), an endpoint, and
``LINKEDIN_ACCESS_TOKEN``.  A nonstandard LinkedIn response can expose its
integer count through ``LINKEDIN_ANALYTICS_METRIC_PATH``.

LinkedIn is queried only when an analytics endpoint, an explicit analytics
permission declaration, and an access token are all configured.  Otherwise it
is reported as ``unsupported`` and can never be mistaken for zero reach.

Outputs contain only fixed status/reason values, allow-listed counters,
timestamps, HTTP status codes, and a one-way receipt reference.  Provider
tokens, account IDs, post/video IDs, request URLs, and raw response bodies are
never rendered to JSON, email, stdout, or ``GITHUB_OUTPUT``.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import hmac
import json
import os
import secrets
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence


SCHEMA_VERSION = 1
DEFAULT_RECEIPTS_DIR = Path("social_publish/receipts")
DEFAULT_YOUTUBE_API_BASE_URL = "https://www.googleapis.com/youtube/v3"
DEFAULT_YOUTUBE_TOKEN_URL = "https://oauth2.googleapis.com/token"
DEFAULT_X_API_BASE_URL = "https://api.x.com"
MAX_RECEIPT_BYTES = 256 * 1024
MAX_RESPONSE_BYTES = 256 * 1024
DEFAULT_TIMEOUT = 20.0
DEFAULT_PAUSE_AFTER_CONSECUTIVE = 2
DEFAULT_MAX_RECEIPTS = 50
CHECKPOINT_WINDOW_END_HOURS = {1: 24, 24: 48}

PLATFORM_ALIASES = {
    "youtube": "youtube",
    "x": "x",
    "twitter": "x",
    "linkedin": "linkedin",
}
SUCCESS_STATUSES = frozenset({"success", "succeeded", "published", "complete", "completed"})
RESULT_STATUSES = frozenset({"checked", "unsupported", "unavailable", "not_found"})

REASON_TEXT = {
    "metric_observed": "已读取平台公开或已授权的触达指标",
    "zero_views_after_24h": "发布满 24 小时后，平台明确返回 0 次观看",
    "zero_impressions_after_24h": "发布满 24 小时后，平台明确返回 0 次曝光",
    "missing_configuration": "缺少该只读检查所需的 GitHub Secret",
    "invalid_provider_url": "只读 provider endpoint 配置无效",
    "credential_invalid": "平台拒绝了当前只读凭证",
    "permission_denied": "当前凭证没有读取该指标的权限",
    "provider_unavailable": "平台或网络暂时无法完成只读检查",
    "provider_response_invalid": "平台响应中没有可确认的指标结构",
    "content_not_found": "平台没有返回对应内容",
    "metric_unavailable": "平台响应未提供可确认的观看或曝光指标",
    "youtube_not_public": "YouTube status 显示该视频当前不是公开分发状态",
    "youtube_processing_incomplete": "YouTube status 显示该视频仍未完成处理",
    "youtube_status_unavailable": "YouTube 未返回可确认的公开和处理状态",
    "linkedin_analytics_not_configured": "LinkedIn analytics 权限或 endpoint 未配置，未执行请求",
}


@dataclass(frozen=True)
class Receipt:
    platform: str
    provider_id: str
    published_at: datetime
    receipt_ref: str


@dataclass(frozen=True)
class ReceiptLoad:
    receipts: tuple[Receipt, ...]
    seen_count: int
    invalid_count: int
    duplicate_count: int


@dataclass(frozen=True)
class HttpJsonResult:
    status: int | None
    payload: Any
    transport_error: bool = False


@dataclass(frozen=True)
class ProbeResult:
    status: str
    reason: str
    metric_name: str = ""
    metric_value: int | None = None
    metrics: Mapping[str, int] | None = None
    http_status: int | None = None
    content_status: Mapping[str, str] | None = None

    def __post_init__(self) -> None:
        if self.status not in RESULT_STATUSES:
            raise ValueError("unsupported normalized result status")


@dataclass(frozen=True)
class ReachResult:
    receipt_ref: str
    platform: str
    published_at: str
    age_hours: float
    status: str
    reason: str
    metric_name: str
    metric_value: int | None
    metrics: Mapping[str, int]
    http_status: int | None
    content_status: Mapping[str, str]
    should_alert: bool


@dataclass(frozen=True)
class ReachReport:
    schema_version: int
    checked_at: str
    checkpoint_hours: int
    checkpoint_window_end_hours: int
    max_receipts: int
    receipts_seen: int
    receipts_accepted: int
    receipts_invalid: int
    receipts_duplicate: int
    window_match_count: int
    truncated_count: int
    due_count: int
    checked_count: int
    unsupported_count: int
    unavailable_count: int
    zero_reach_count: int
    should_alert: bool
    pause_after_consecutive: int
    consecutive_zero_by_platform: Mapping[str, int]
    max_consecutive_zero: int
    pause_signal: bool
    subject: str
    alert_key: str
    results: tuple[ReachResult, ...]


def _iso_utc(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def parse_timestamp(value: str) -> datetime:
    normalized = value.strip()
    if normalized.endswith("Z"):
        normalized = f"{normalized[:-1]}+00:00"
    parsed = datetime.fromisoformat(normalized)
    if parsed.tzinfo is None:
        raise ValueError("timestamp must include a timezone")
    return parsed.astimezone(timezone.utc)


def _first_env(env: Mapping[str, str], names: Sequence[str]) -> str:
    for name in names:
        value = (env.get(name) or "").strip()
        if value:
            return value
    return ""


def _normalized_platform(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    return PLATFORM_ALIASES.get(value.strip().casefold(), "")


def _valid_provider_id(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    normalized = value.strip()
    if not normalized or len(normalized) > 512:
        return ""
    if any(character.isspace() or ord(character) < 32 for character in normalized):
        return ""
    return normalized


def _receipt_is_successful(payload: Mapping[str, Any]) -> bool:
    """Accept explicit success, or a minimal receipt with no status marker."""

    if "success" in payload and payload.get("success") is not True:
        return False
    if "status" in payload:
        status = payload.get("status")
        if not isinstance(status, str) or status.strip().casefold() not in SUCCESS_STATUSES:
            return False
    if "state" in payload:
        state = payload.get("state")
        if not isinstance(state, str) or state.strip().casefold() not in SUCCESS_STATUSES:
            return False
    return True


def _build_receipt(
    platform_value: Any,
    provider_id_value: Any,
    published_at_value: Any,
) -> Receipt | None:
    platform = _normalized_platform(platform_value)
    provider_id = _valid_provider_id(provider_id_value)
    if not platform or not provider_id or not isinstance(published_at_value, str):
        return None
    try:
        published_at = parse_timestamp(published_at_value)
    except (ValueError, OverflowError):
        return None
    digest = hashlib.sha256(
        f"{platform}\0{provider_id}".encode("utf-8")
    ).hexdigest()[:16]
    return Receipt(
        platform=platform,
        provider_id=provider_id,
        published_at=published_at,
        receipt_ref=f"receipt-{digest}",
    )


def parse_receipts(payload: Any) -> tuple[Receipt, ...]:
    """Parse the unified multi-provider receipt, plus the legacy flat shape."""

    if not isinstance(payload, dict):
        return ()
    schema_version = payload.get("schema_version")
    if type(schema_version) is not int or schema_version != SCHEMA_VERSION:
        return ()

    results = payload.get("results")
    if isinstance(results, dict):
        top_state = payload.get("state")
        completed_at = payload.get("completed_at")
        if top_state not in {"published", "partial"} or not isinstance(completed_at, str):
            return ()
        parsed: list[Receipt] = []
        for provider_name in ("youtube", "linkedin", "x"):
            provider_result = results.get(provider_name)
            if not isinstance(provider_result, dict) or provider_result.get("state") != "published":
                continue
            id_field = "video_id" if provider_name == "youtube" else "post_id"
            published_at = provider_result.get("published_at") or completed_at
            if provider_name == "youtube" and provider_result.get("publish_at"):
                published_at = provider_result.get("publish_at")
            receipt = _build_receipt(
                provider_name,
                provider_result.get(id_field),
                published_at,
            )
            if receipt is not None:
                parsed.append(receipt)
        return tuple(parsed)

    if not _receipt_is_successful(payload):
        return ()

    platform = _normalized_platform(payload.get("platform"))
    if not platform:
        return ()
    id_field = "video_id" if platform == "youtube" else "post_id"
    receipt = _build_receipt(
        platform,
        payload.get(id_field),
        payload.get("published_at"),
    )
    return (receipt,) if receipt is not None else ()


def parse_receipt(payload: Any) -> Receipt | None:
    """Return the first parsed receipt for callers handling a flat payload."""

    receipts = parse_receipts(payload)
    return receipts[0] if receipts else None


def load_receipts(receipts_dir: Path) -> ReceiptLoad:
    if not receipts_dir.is_dir():
        return ReceiptLoad((), 0, 0, 0)

    seen_count = 0
    invalid_count = 0
    duplicate_count = 0
    accepted: dict[tuple[str, str], Receipt] = {}
    for path in sorted(receipts_dir.glob("*.json")):
        seen_count += 1
        try:
            if path.is_symlink() or path.stat().st_size > MAX_RECEIPT_BYTES:
                raise ValueError("invalid receipt file")
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
            invalid_count += 1
            continue
        parsed_receipts = parse_receipts(payload)
        if not parsed_receipts:
            invalid_count += 1
            continue
        for receipt in parsed_receipts:
            key = (receipt.platform, receipt.provider_id)
            previous = accepted.get(key)
            if previous is not None:
                duplicate_count += 1
                if receipt.published_at < previous.published_at:
                    accepted[key] = receipt
                continue
            accepted[key] = receipt

    receipts = tuple(
        sorted(
            accepted.values(),
            key=lambda row: (row.published_at, row.platform, row.receipt_ref),
            reverse=True,
        )
    )
    return ReceiptLoad(receipts, seen_count, invalid_count, duplicate_count)


def _validated_http_url(value: str) -> str | None:
    try:
        parsed = urllib.parse.urlsplit(value)
    except ValueError:
        return None
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return None
    if parsed.username or parsed.password or parsed.fragment:
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
    method: str = "GET",
    headers: Mapping[str, str],
    body: bytes | None = None,
    timeout: float,
    opener: Callable[..., Any] | None = None,
) -> HttpJsonResult:
    """Fetch bounded JSON while discarding provider prose and exception text."""

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
        except Exception:  # noqa: BLE001 - raw error details are deliberately discarded.
            payload = None
        return HttpJsonResult(int(error.code), payload)
    except (urllib.error.URLError, TimeoutError, OSError, ValueError):
        return HttpJsonResult(None, None, True)


def _http_issue(result: HttpJsonResult) -> ProbeResult | None:
    if result.transport_error or result.status is None:
        return ProbeResult("unavailable", "provider_unavailable")
    if result.status == 401:
        return ProbeResult("unavailable", "credential_invalid", http_status=401)
    if result.status == 403:
        return ProbeResult("unavailable", "permission_denied", http_status=403)
    if result.status == 404:
        return ProbeResult("not_found", "content_not_found", http_status=404)
    if result.status == 429 or result.status >= 500:
        return ProbeResult(
            "unavailable",
            "provider_unavailable",
            http_status=result.status,
        )
    if not 200 <= result.status < 300:
        return ProbeResult(
            "unavailable",
            "provider_response_invalid",
            http_status=result.status,
        )
    if not isinstance(result.payload, dict):
        return ProbeResult(
            "unavailable",
            "provider_response_invalid",
            http_status=result.status,
        )
    return None


def _safe_nonnegative_int(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        parsed = value
    elif isinstance(value, str) and value.strip().isdigit():
        parsed = int(value.strip())
    else:
        return None
    if parsed < 0 or parsed > 10**18:
        return None
    return parsed


def _append_query(url: str, values: Mapping[str, str]) -> str:
    parts = urllib.parse.urlsplit(url)
    query = urllib.parse.parse_qsl(parts.query, keep_blank_values=True)
    query.extend(values.items())
    return urllib.parse.urlunsplit(
        (parts.scheme, parts.netloc, parts.path, urllib.parse.urlencode(query), "")
    )


def _youtube_videos_url(env: Mapping[str, str]) -> str:
    direct = _first_env(env, ("YOUTUBE_VIDEOS_URL", "YOUTUBE_VIDEOS_LIST_URL"))
    if direct:
        return direct
    base = (env.get("YOUTUBE_API_BASE_URL") or DEFAULT_YOUTUBE_API_BASE_URL).strip()
    return f"{base.rstrip('/')}/videos"


def _youtube_bearer_token(
    env: Mapping[str, str],
    *,
    timeout: float,
    opener: Callable[..., Any] | None,
) -> tuple[str, ProbeResult | None]:
    access_token = _first_env(env, ("YOUTUBE_ACCESS_TOKEN", "YOUTUBE_OAUTH_ACCESS_TOKEN"))
    if access_token:
        return access_token, None
    client_id = _first_env(env, ("YOUTUBE_CLIENT_ID", "YOUTUBE_OAUTH_CLIENT_ID"))
    client_secret = _first_env(
        env,
        ("YOUTUBE_CLIENT_SECRET", "YOUTUBE_OAUTH_CLIENT_SECRET"),
    )
    refresh_token = _first_env(
        env,
        ("YOUTUBE_REFRESH_TOKEN", "YOUTUBE_OAUTH_REFRESH_TOKEN"),
    )
    if not any((client_id, client_secret, refresh_token)):
        return "", None
    if not all((client_id, client_secret, refresh_token)):
        return "", ProbeResult("unavailable", "missing_configuration")
    token_url = (env.get("YOUTUBE_TOKEN_URL") or DEFAULT_YOUTUBE_TOKEN_URL).strip()
    if not _validated_http_url(token_url):
        return "", ProbeResult("unavailable", "invalid_provider_url")
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
            "User-Agent": "portal-suite-social-reach-monitor/1.0",
        },
        body=body,
        timeout=timeout,
        opener=opener,
    )
    if refreshed.status == 400 and isinstance(refreshed.payload, dict):
        oauth_error = refreshed.payload.get("error")
        if oauth_error in {"invalid_client", "invalid_grant", "unauthorized_client"}:
            return "", ProbeResult(
                "unavailable",
                "credential_invalid",
                http_status=refreshed.status,
            )
    issue = _http_issue(refreshed)
    if issue is not None:
        return "", issue
    token = refreshed.payload.get("access_token")
    if not isinstance(token, str) or not token:
        return "", ProbeResult(
            "unavailable",
            "provider_response_invalid",
            http_status=refreshed.status,
        )
    return token, None


def probe_youtube(
    receipt: Receipt,
    env: Mapping[str, str],
    *,
    timeout: float = DEFAULT_TIMEOUT,
    opener: Callable[..., Any] | None = None,
    provider_cache: dict[str, Any] | None = None,
) -> ProbeResult:
    endpoint = _youtube_videos_url(env)
    if not _validated_http_url(endpoint):
        return ProbeResult("unavailable", "invalid_provider_url")
    access_token = _first_env(env, ("YOUTUBE_ACCESS_TOKEN", "YOUTUBE_OAUTH_ACCESS_TOKEN"))
    api_key = _first_env(env, ("YOUTUBE_API_KEY", "GOOGLE_API_KEY"))
    if not api_key and not access_token:
        cache_key = "youtube_bearer"
        cached = provider_cache.get(cache_key) if provider_cache is not None else None
        if isinstance(cached, tuple) and len(cached) == 2:
            access_token, token_issue = cached
        else:
            access_token, token_issue = _youtube_bearer_token(
                env,
                timeout=timeout,
                opener=opener,
            )
            if provider_cache is not None:
                provider_cache[cache_key] = (access_token, token_issue)
        if token_issue is not None:
            return token_issue
    if not api_key and not access_token:
        return ProbeResult("unavailable", "missing_configuration")

    query = {
        "part": "statistics,status",
        "id": receipt.provider_id,
    }
    if api_key and not access_token:
        query["key"] = api_key
    headers = {
        "Accept": "application/json",
        "User-Agent": "portal-suite-social-reach-monitor/1.0",
    }
    if access_token:
        headers["Authorization"] = f"Bearer {access_token}"
    response = request_json(
        _append_query(endpoint, query),
        headers=headers,
        timeout=timeout,
        opener=opener,
    )
    issue = _http_issue(response)
    if issue is not None:
        return issue
    items = response.payload.get("items")
    if not isinstance(items, list):
        return ProbeResult(
            "unavailable",
            "provider_response_invalid",
            http_status=response.status,
        )
    if not items:
        return ProbeResult("not_found", "content_not_found", http_status=response.status)
    item = items[0]
    if not isinstance(item, dict):
        return ProbeResult(
            "unavailable",
            "provider_response_invalid",
            http_status=response.status,
        )
    statistics = item.get("statistics")
    view_count = (
        _safe_nonnegative_int(statistics.get("viewCount"))
        if isinstance(statistics, dict)
        else None
    )
    status = item.get("status")
    content_status: dict[str, str] = {}
    if isinstance(status, dict):
        upload_status = status.get("uploadStatus")
        privacy_status = status.get("privacyStatus")
        if upload_status in {"deleted", "failed", "processed", "rejected", "uploaded"}:
            content_status["upload_status"] = upload_status
        if privacy_status in {"private", "public", "unlisted"}:
            content_status["privacy_status"] = privacy_status
    if view_count is None:
        return ProbeResult(
            "unsupported",
            "metric_unavailable",
            http_status=response.status,
            content_status=content_status,
        )
    if view_count == 0:
        privacy = content_status.get("privacy_status")
        upload = content_status.get("upload_status")
        if privacy and privacy != "public":
            return ProbeResult(
                "unsupported",
                "youtube_not_public",
                metric_name="views",
                metric_value=0,
                metrics={"views": 0},
                http_status=response.status,
                content_status=content_status,
            )
        if upload and upload != "processed":
            return ProbeResult(
                "unavailable",
                "youtube_processing_incomplete",
                metric_name="views",
                metric_value=0,
                metrics={"views": 0},
                http_status=response.status,
                content_status=content_status,
            )
        if privacy != "public" or upload != "processed":
            return ProbeResult(
                "unsupported",
                "youtube_status_unavailable",
                metric_name="views",
                metric_value=0,
                metrics={"views": 0},
                http_status=response.status,
                content_status=content_status,
            )
    return ProbeResult(
        "checked",
        "metric_observed",
        metric_name="views",
        metric_value=view_count,
        metrics={"views": view_count},
        http_status=response.status,
        content_status=content_status,
    )


def _oauth_encode(value: Any) -> str:
    return urllib.parse.quote(str(value), safe="~-._")


def build_oauth1_header(
    method: str,
    url: str,
    *,
    consumer_key: str,
    consumer_secret: str,
    access_token: str,
    access_token_secret: str,
    nonce: str | None = None,
    timestamp: int | None = None,
) -> str:
    oauth_parameters = {
        "oauth_consumer_key": consumer_key,
        "oauth_nonce": nonce or secrets.token_hex(16),
        "oauth_signature_method": "HMAC-SHA1",
        "oauth_timestamp": str(int(time.time()) if timestamp is None else int(timestamp)),
        "oauth_token": access_token,
        "oauth_version": "1.0",
    }
    parsed = urllib.parse.urlsplit(url)
    base_url = urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path, "", ""))
    signature_parameters = list(urllib.parse.parse_qsl(parsed.query, keep_blank_values=True))
    signature_parameters.extend(oauth_parameters.items())
    encoded_parameters = sorted(
        (_oauth_encode(key), _oauth_encode(value))
        for key, value in signature_parameters
    )
    parameter_string = "&".join(f"{key}={value}" for key, value in encoded_parameters)
    signature_base = "&".join(
        (
            method.upper(),
            _oauth_encode(base_url),
            _oauth_encode(parameter_string),
        )
    )
    signing_key = f"{_oauth_encode(consumer_secret)}&{_oauth_encode(access_token_secret)}"
    signature = base64.b64encode(
        hmac.new(
            signing_key.encode("ascii"),
            signature_base.encode("ascii"),
            hashlib.sha1,
        ).digest()
    ).decode("ascii")
    oauth_parameters["oauth_signature"] = signature
    rendered = ", ".join(
        f'{_oauth_encode(key)}="{_oauth_encode(value)}"'
        for key, value in sorted(oauth_parameters.items())
    )
    return f"OAuth {rendered}"


def _x_lookup_url(receipt: Receipt, env: Mapping[str, str]) -> str:
    template = _first_env(
        env,
        ("X_TWEET_LOOKUP_URL_TEMPLATE", "X_TWEET_LOOKUP_URL"),
    )
    encoded_id = urllib.parse.quote(receipt.provider_id, safe="")
    if template:
        endpoint = template.replace("{post_id}", encoded_id).replace("{tweet_id}", encoded_id)
    else:
        base = (env.get("X_API_BASE_URL") or DEFAULT_X_API_BASE_URL).strip()
        endpoint = f"{base.rstrip('/')}/2/tweets/{encoded_id}"
    return _append_query(endpoint, {"tweet.fields": "public_metrics"})


def _x_metrics(payload: Mapping[str, Any]) -> tuple[int | None, dict[str, int]]:
    data = payload.get("data")
    if not isinstance(data, dict):
        return None, {}
    blocks = [
        data.get("public_metrics"),
        data.get("organic_metrics"),
        data.get("non_public_metrics"),
    ]
    safe_metrics: dict[str, int] = {}
    aliases = {
        "impression_count": "impressions",
        "view_count": "impressions",
        "like_count": "likes",
        "reply_count": "replies",
        "retweet_count": "reposts",
        "repost_count": "reposts",
        "quote_count": "quotes",
        "bookmark_count": "bookmarks",
    }
    impression_count: int | None = None
    for block in blocks:
        if not isinstance(block, dict):
            continue
        for provider_name, safe_name in aliases.items():
            parsed = _safe_nonnegative_int(block.get(provider_name))
            if parsed is None:
                continue
            safe_metrics[safe_name] = max(safe_metrics.get(safe_name, 0), parsed)
            if safe_name == "impressions":
                impression_count = max(impression_count or 0, parsed)
    return impression_count, safe_metrics


def probe_x(
    receipt: Receipt,
    env: Mapping[str, str],
    *,
    timeout: float = DEFAULT_TIMEOUT,
    opener: Callable[..., Any] | None = None,
    nonce: str | None = None,
    timestamp: int | None = None,
) -> ProbeResult:
    credentials = {
        "consumer_key": _first_env(env, ("X_API_KEY", "X_CONSUMER_KEY", "TWITTER_API_KEY")),
        "consumer_secret": _first_env(
            env,
            ("X_API_SECRET", "X_API_KEY_SECRET", "X_CONSUMER_SECRET", "TWITTER_API_SECRET"),
        ),
        "access_token": _first_env(env, ("X_ACCESS_TOKEN", "TWITTER_ACCESS_TOKEN")),
        "access_token_secret": _first_env(
            env,
            ("X_ACCESS_TOKEN_SECRET", "TWITTER_ACCESS_TOKEN_SECRET"),
        ),
    }
    if not all(credentials.values()):
        return ProbeResult("unavailable", "missing_configuration")
    url = _x_lookup_url(receipt, env)
    if not _validated_http_url(url):
        return ProbeResult("unavailable", "invalid_provider_url")
    authorization = build_oauth1_header(
        "GET",
        url,
        nonce=nonce,
        timestamp=timestamp,
        **credentials,
    )
    response = request_json(
        url,
        headers={
            "Accept": "application/json",
            "Authorization": authorization,
            "User-Agent": "portal-suite-social-reach-monitor/1.0",
        },
        timeout=timeout,
        opener=opener,
    )
    issue = _http_issue(response)
    if issue is not None:
        return issue
    impression_count, public_metrics = _x_metrics(response.payload)
    if impression_count is None:
        return ProbeResult(
            "unsupported",
            "metric_unavailable",
            metrics=public_metrics,
            http_status=response.status,
        )
    return ProbeResult(
        "checked",
        "metric_observed",
        metric_name="impressions",
        metric_value=impression_count,
        metrics=public_metrics,
        http_status=response.status,
    )


def _truthy(value: str) -> bool:
    return value.strip().casefold() in {"1", "true", "yes", "on", "granted"}


def _linkedin_permission_configured(env: Mapping[str, str]) -> bool:
    explicit = (env.get("LINKEDIN_ANALYTICS_PERMISSION_GRANTED") or "").strip()
    if explicit:
        return _truthy(explicit)
    permission = _first_env(
        env,
        (
            "LINKEDIN_ANALYTICS_PERMISSION",
            "LINKEDIN_ANALYTICS_PERMISSIONS",
            "LINKEDIN_ANALYTICS_SCOPE",
        ),
    )
    return bool(permission) and permission.casefold() not in {"0", "false", "no", "off", "denied"}


def _linkedin_endpoint(receipt: Receipt, env: Mapping[str, str]) -> str:
    template = _first_env(
        env,
        (
            "LINKEDIN_ANALYTICS_URL_TEMPLATE",
            "LINKEDIN_ANALYTICS_ENDPOINT",
            "LINKEDIN_ANALYTICS_URL",
        ),
    )
    encoded_id = urllib.parse.quote(receipt.provider_id, safe="")
    return template.replace("{post_id}", encoded_id).replace("{encoded_post_id}", encoded_id)


def _path_value(payload: Any, path: str) -> Any:
    value = payload
    for part in path.split("."):
        if isinstance(value, dict):
            if part not in value:
                return None
            value = value[part]
        elif isinstance(value, list) and part.isdigit():
            index = int(part)
            if index >= len(value):
                return None
            value = value[index]
        else:
            return None
    return value


def _linkedin_impressions(payload: Mapping[str, Any], metric_path: str) -> int | None:
    if metric_path:
        return _safe_nonnegative_int(_path_value(payload, metric_path))
    top_level_candidates = (
        "impression_count",
        "impressionCount",
        "impressions",
        "data.impression_count",
        "data.impressionCount",
        "data.impressions",
    )
    for path in top_level_candidates:
        parsed = _safe_nonnegative_int(_path_value(payload, path))
        if parsed is not None:
            return parsed
    elements = payload.get("elements")
    if isinstance(elements, list) and elements:
        element_paths = (
            "impressionCount",
            "impressions",
            "totalShareStatistics.impressionCount",
            "value",
            "value.fixedDecimal",
        )
        for path in element_paths:
            values = [_safe_nonnegative_int(_path_value(element, path)) for element in elements]
            # A partial series is not coerced to zero.  Sum only a complete,
            # homogeneous series so one positive bucket cannot be hidden by a
            # zero first element.
            if all(value is not None for value in values):
                total = sum(value for value in values if value is not None)
                return total if total <= 10**18 else None
    return None


def probe_linkedin(
    receipt: Receipt,
    env: Mapping[str, str],
    *,
    timeout: float = DEFAULT_TIMEOUT,
    opener: Callable[..., Any] | None = None,
) -> ProbeResult:
    endpoint_configured = bool(
        _first_env(
            env,
            (
                "LINKEDIN_ANALYTICS_URL_TEMPLATE",
                "LINKEDIN_ANALYTICS_ENDPOINT",
                "LINKEDIN_ANALYTICS_URL",
            ),
        )
    )
    if not endpoint_configured or not _linkedin_permission_configured(env):
        return ProbeResult("unsupported", "linkedin_analytics_not_configured")
    access_token = _first_env(
        env,
        ("LINKEDIN_ACCESS_TOKEN", "LINKEDIN_OAUTH_ACCESS_TOKEN"),
    )
    if not access_token:
        return ProbeResult("unavailable", "missing_configuration")
    endpoint = _linkedin_endpoint(receipt, env)
    if not _validated_http_url(endpoint):
        return ProbeResult("unavailable", "invalid_provider_url")
    linkedin_version = _first_env(
        env,
        ("LINKEDIN_API_VERSION", "LINKEDIN_VERSION"),
    ) or "202608"
    if not (len(linkedin_version) == 6 and linkedin_version.isdigit()):
        linkedin_version = "202608"
    response = request_json(
        endpoint,
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {access_token}",
            "LinkedIn-Version": linkedin_version,
            "X-Restli-Protocol-Version": "2.0.0",
            "User-Agent": "portal-suite-social-reach-monitor/1.0",
        },
        timeout=timeout,
        opener=opener,
    )
    issue = _http_issue(response)
    if issue is not None:
        return issue
    metric_path = (env.get("LINKEDIN_ANALYTICS_METRIC_PATH") or "").strip()
    impression_count = _linkedin_impressions(response.payload, metric_path)
    if impression_count is None:
        return ProbeResult(
            "unsupported",
            "metric_unavailable",
            http_status=response.status,
        )
    return ProbeResult(
        "checked",
        "metric_observed",
        metric_name="impressions",
        metric_value=impression_count,
        metrics={"impressions": impression_count},
        http_status=response.status,
    )


def probe_receipt(
    receipt: Receipt,
    env: Mapping[str, str],
    *,
    timeout: float,
    opener: Callable[..., Any] | None,
    provider_cache: dict[str, Any] | None = None,
) -> ProbeResult:
    if receipt.platform == "youtube":
        return probe_youtube(
            receipt,
            env,
            timeout=timeout,
            opener=opener,
            provider_cache=provider_cache,
        )
    if receipt.platform == "x":
        return probe_x(receipt, env, timeout=timeout, opener=opener)
    if receipt.platform == "linkedin":
        return probe_linkedin(receipt, env, timeout=timeout, opener=opener)
    return ProbeResult("unsupported", "metric_unavailable")


def _reach_result(
    receipt: Receipt,
    probe: ProbeResult,
    *,
    now: datetime,
    checkpoint_hours: int,
) -> ReachResult:
    metric_value = probe.metric_value
    should_alert = (
        checkpoint_hours == 24
        and probe.status == "checked"
        and metric_value == 0
        and probe.metric_name in {"views", "impressions"}
    )
    reason = probe.reason
    if should_alert:
        reason = (
            "zero_views_after_24h"
            if probe.metric_name == "views"
            else "zero_impressions_after_24h"
        )
    age = max(0.0, (now - receipt.published_at).total_seconds() / 3600)
    return ReachResult(
        receipt_ref=receipt.receipt_ref,
        platform=receipt.platform,
        published_at=_iso_utc(receipt.published_at),
        age_hours=round(age, 2),
        status=probe.status,
        reason=reason,
        metric_name=probe.metric_name,
        metric_value=metric_value,
        metrics=dict(probe.metrics or {}),
        http_status=probe.http_status,
        content_status=dict(probe.content_status or {}),
        should_alert=should_alert,
    )


def _consecutive_zero_counts(results: Sequence[ReachResult]) -> dict[str, int]:
    counts = {platform: 0 for platform in ("youtube", "x", "linkedin")}
    for platform in counts:
        platform_results = [row for row in results if row.platform == platform]
        for row in platform_results:
            if row.should_alert:
                counts[platform] += 1
            else:
                break
    return counts


def _subject(checkpoint_hours: int, zero_count: int, pause_signal: bool) -> str:
    if zero_count:
        suffix = "；建议暂停自动发布" if pause_signal else ""
        return f"[Portal Operations] {checkpoint_hours}h 社媒触达：{zero_count} 条为 0{suffix}"
    return f"[Portal Operations] {checkpoint_hours}h 社媒触达检查完成"


def _alert_key(
    checkpoint_hours: int,
    results: Sequence[ReachResult],
    pause_signal: bool,
) -> str:
    affected = [row.receipt_ref for row in results if row.should_alert]
    material = "|".join(
        [str(checkpoint_hours), str(pause_signal).lower(), *sorted(affected)]
    )
    digest = hashlib.sha256(material.encode("ascii")).hexdigest()[:16]
    return f"social-reach:{checkpoint_hours}h:{digest}"


def run_monitor(
    receipts_dir: Path,
    env: Mapping[str, str],
    *,
    checkpoint_hours: int,
    now: datetime | None = None,
    timeout: float = DEFAULT_TIMEOUT,
    pause_after_consecutive: int = DEFAULT_PAUSE_AFTER_CONSECUTIVE,
    max_receipts: int = DEFAULT_MAX_RECEIPTS,
    opener: Callable[..., Any] | None = None,
) -> ReachReport:
    if checkpoint_hours not in {1, 24}:
        raise ValueError("checkpoint_hours must be 1 or 24")
    if pause_after_consecutive < 2:
        raise ValueError("pause_after_consecutive must be at least 2")
    if max_receipts < 1:
        raise ValueError("max_receipts must be at least 1")
    checked_at = now or datetime.now(timezone.utc)
    if checked_at.tzinfo is None:
        checked_at = checked_at.replace(tzinfo=timezone.utc)
    checked_at = checked_at.astimezone(timezone.utc)

    loaded = load_receipts(receipts_dir)
    window_end_hours = CHECKPOINT_WINDOW_END_HOURS[checkpoint_hours]
    window_receipts = tuple(
        receipt
        for receipt in loaded.receipts
        if checkpoint_hours * 3600
        <= (checked_at - receipt.published_at).total_seconds()
        < window_end_hours * 3600
    )
    # When a newly deployed monitor encounters a backlog, prioritize receipts
    # closest to aging out of the checkpoint window.  Results are then restored
    # to newest-first order for the consecutive-zero calculation.
    selected_receipts = tuple(
        sorted(window_receipts, key=lambda row: row.published_at)[:max_receipts]
    )
    due_receipts = tuple(
        sorted(
            selected_receipts,
            key=lambda row: (row.published_at, row.platform, row.receipt_ref),
            reverse=True,
        )
    )
    provider_cache: dict[str, Any] = {}
    results = tuple(
        _reach_result(
            receipt,
            probe_receipt(
                receipt,
                env,
                timeout=timeout,
                opener=opener,
                provider_cache=provider_cache,
            ),
            now=checked_at,
            checkpoint_hours=checkpoint_hours,
        )
        for receipt in due_receipts
    )
    consecutive = _consecutive_zero_counts(results) if checkpoint_hours == 24 else {
        platform: 0 for platform in ("youtube", "x", "linkedin")
    }
    max_consecutive = max(consecutive.values(), default=0)
    zero_reach_count = sum(
        row.status == "checked"
        and row.metric_name in {"views", "impressions"}
        and row.metric_value == 0
        for row in results
    )
    should_alert = checkpoint_hours == 24 and bool(zero_reach_count)
    pause_signal = should_alert and max_consecutive >= pause_after_consecutive
    checked_count = sum(row.status == "checked" for row in results)
    unsupported_count = sum(row.status == "unsupported" for row in results)
    unavailable_count = sum(row.status in {"unavailable", "not_found"} for row in results)
    subject = _subject(checkpoint_hours, zero_reach_count, pause_signal)
    return ReachReport(
        schema_version=SCHEMA_VERSION,
        checked_at=_iso_utc(checked_at),
        checkpoint_hours=checkpoint_hours,
        checkpoint_window_end_hours=window_end_hours,
        max_receipts=max_receipts,
        receipts_seen=loaded.seen_count,
        receipts_accepted=len(loaded.receipts),
        receipts_invalid=loaded.invalid_count,
        receipts_duplicate=loaded.duplicate_count,
        window_match_count=len(window_receipts),
        truncated_count=max(0, len(window_receipts) - len(due_receipts)),
        due_count=len(due_receipts),
        checked_count=checked_count,
        unsupported_count=unsupported_count,
        unavailable_count=unavailable_count,
        zero_reach_count=zero_reach_count,
        should_alert=should_alert,
        pause_after_consecutive=pause_after_consecutive,
        consecutive_zero_by_platform=consecutive,
        max_consecutive_zero=max_consecutive,
        pause_signal=pause_signal,
        subject=subject,
        alert_key=_alert_key(checkpoint_hours, results, pause_signal),
        results=results,
    )


def report_payload(report: ReachReport) -> dict[str, Any]:
    payload = asdict(report)
    payload["results"] = [asdict(row) for row in report.results]
    return payload


def render_email(report: ReachReport, env: Mapping[str, str]) -> str:
    lines = [
        (
            "社媒发布触达检查结果如下。邮件不包含 token、API key、账号 ID、"
            "post/video ID、provider URL 或原始响应。"
        ),
        "",
        f"检查时间：{report.checked_at}",
        (
            "检查窗口：发布后 "
            f"[{report.checkpoint_hours}, {report.checkpoint_window_end_hours}) 小时"
        ),
        f"有效 receipt：{report.receipts_accepted}",
        f"窗口内 receipt：{report.window_match_count}",
        f"本次到期检查：{report.due_count}",
        f"受单次上限延后：{report.truncated_count}",
        f"明确零触达：{report.zero_reach_count}",
        f"需要提醒：{'是' if report.should_alert else '否'}",
        f"暂停信号：{'是' if report.pause_signal else '否'}",
        "",
        "检查结果：",
    ]
    if not report.results:
        lines.append("- 没有达到本次时间节点的有效 receipt。")
    for row in report.results:
        metric = "指标不可用"
        if row.metric_name and row.metric_value is not None:
            metric = f"{row.metric_name}={row.metric_value}"
        lines.extend(
            [
                f"- {row.platform} / {row.receipt_ref} / {row.status} / {metric}",
                f"  发布时间：{row.published_at}",
                f"  说明：{REASON_TEXT.get(row.reason, '需要查看本次 GitHub Actions 运行')}",
            ]
        )
    lines.extend(
        [
            "",
            "判定规则：",
            "1. 1 小时检查只报告，不发送零触达提醒。",
            "2. 24 小时检查只有在平台明确返回 views/impressions=0 时才提醒。",
            "3. unsupported、权限缺失、网络异常或响应缺指标都不会被当成 0。",
            (
                f"4. 同一平台最近连续 {report.pause_after_consecutive} 条 24 小时"
                "零触达时输出暂停信号。"
            ),
        ]
    )
    server = (env.get("GITHUB_SERVER_URL") or "").rstrip("/")
    repository = (env.get("GITHUB_REPOSITORY") or "").strip("/")
    run_id = (env.get("GITHUB_RUN_ID") or "").strip()
    if server and repository and run_id:
        lines.extend(["", f"本次运行：{server}/{repository}/actions/runs/{run_id}"])
    return "\n".join(lines).strip() + "\n"


def write_github_output(
    path: Path | None,
    report: ReachReport,
    email_path: Path,
    json_path: Path,
) -> None:
    if path is None:
        return
    pause_platforms = ",".join(
        platform
        for platform, count in report.consecutive_zero_by_platform.items()
        if count >= report.pause_after_consecutive
    )
    values = {
        "should_alert": str(report.should_alert).lower(),
        "pause_signal": str(report.pause_signal).lower(),
        "pause_platforms": pause_platforms,
        "max_consecutive_zero": str(report.max_consecutive_zero),
        "zero_reach_count": str(report.zero_reach_count),
        "due_count": str(report.due_count),
        "truncated_count": str(report.truncated_count),
        "unsupported_count": str(report.unsupported_count),
        "unavailable_count": str(report.unavailable_count),
        "subject": report.subject,
        "alert_key": report.alert_key,
        "email_file": str(email_path),
        "json_file": str(json_path),
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        for key, value in values.items():
            if "\n" in value or "\r" in value:
                raise ValueError("GitHub output values must be one line")
            handle.write(f"{key}={value}\n")


def _pause_threshold(value: str) -> int:
    parsed = int(value)
    if parsed < 2:
        raise argparse.ArgumentTypeError("must be at least 2")
    return parsed


def _positive_int(value: str) -> int:
    parsed = int(value)
    if parsed < 1:
        raise argparse.ArgumentTypeError("must be at least 1")
    return parsed


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    default_pause = os.environ.get(
        "SOCIAL_REACH_PAUSE_AFTER_CONSECUTIVE",
        str(DEFAULT_PAUSE_AFTER_CONSECUTIVE),
    )
    default_max_receipts = os.environ.get(
        "SOCIAL_REACH_MAX_RECEIPTS",
        str(DEFAULT_MAX_RECEIPTS),
    )
    parser = argparse.ArgumentParser(
        description="Check social reach from successful schema-v1 receipts without publishing"
    )
    parser.add_argument(
        "--receipts-dir",
        type=Path,
        default=DEFAULT_RECEIPTS_DIR,
    )
    parser.add_argument("--age-hours", type=int, choices=(1, 24), required=True)
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT)
    parser.add_argument(
        "--pause-after-consecutive",
        type=_pause_threshold,
        default=_pause_threshold(default_pause),
    )
    parser.add_argument(
        "--max-receipts",
        type=_positive_int,
        default=_positive_int(default_max_receipts),
    )
    parser.add_argument("--now", help=argparse.SUPPRESS)
    parser.add_argument("--json-output", type=Path, required=True)
    parser.add_argument("--email-output", type=Path, required=True)
    parser.add_argument(
        "--github-output",
        type=Path,
        default=Path(os.environ["GITHUB_OUTPUT"]) if os.environ.get("GITHUB_OUTPUT") else None,
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    now = parse_timestamp(args.now) if args.now else None
    report = run_monitor(
        args.receipts_dir,
        os.environ,
        checkpoint_hours=args.age_hours,
        now=now,
        timeout=args.timeout,
        pause_after_consecutive=args.pause_after_consecutive,
        max_receipts=args.max_receipts,
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
        "Social reach monitor complete: "
        f"checkpoint={report.checkpoint_hours}h, due={report.due_count}, "
        f"zero={report.zero_reach_count}, alert={str(report.should_alert).lower()}, "
        f"pause={str(report.pause_signal).lower()}"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001 - never render provider or credential detail.
        print(f"Social reach monitor failed: {type(exc).__name__}", file=sys.stderr)
        raise SystemExit(1)
