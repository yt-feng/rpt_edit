#!/usr/bin/env python3
"""Publish one video through the official YouTube Data API.

The adapter is intentionally small and dependency-free so it can run on a
GitHub-hosted runner.  It refreshes an OAuth access token, starts a resumable
``videos.insert`` upload, streams a local media file to the returned session
URL, and polls ``videos.list`` until YouTube has finished processing it.

Credentials are read only from ``env``:

* ``YOUTUBE_CLIENT_ID``
* ``YOUTUBE_CLIENT_SECRET``
* ``YOUTUBE_REFRESH_TOKEN`` (``YOUTUBE_OAUTH_REFRESH_TOKEN`` is accepted too)

Provider URLs can all be replaced for testing or a controlled proxy:

* ``YOUTUBE_TOKEN_URL``
* ``YOUTUBE_VIDEOS_INSERT_URL`` (or ``YOUTUBE_UPLOAD_URL``)
* ``YOUTUBE_VIDEOS_LIST_URL`` (or ``YOUTUBE_API_BASE_URL``)
* ``YOUTUBE_WATCH_URL_TEMPLATE``

No provider response body, access token, refresh token, or client secret is
included in a receipt, exception message, or CLI output.
"""

from __future__ import annotations

import argparse
import inspect
import json
import mimetypes
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping


DEFAULT_TOKEN_URL = "https://oauth2.googleapis.com/token"
DEFAULT_VIDEOS_INSERT_URL = "https://www.googleapis.com/upload/youtube/v3/videos"
DEFAULT_VIDEOS_LIST_URL = "https://www.googleapis.com/youtube/v3/videos"
DEFAULT_WATCH_URL_TEMPLATE = "https://www.youtube.com/watch?v={video_id}"

MAX_RESPONSE_BYTES = 256 * 1024
MEDIA_CHUNK_BYTES = 1024 * 1024
VIDEO_ID_RE = re.compile(r"^[A-Za-z0-9_-]{1,128}$")


class YouTubePublishError(RuntimeError):
    """Base error with a stable, provider-body-free code."""

    def __init__(
        self,
        code: str,
        message: str,
        *,
        http_status: int | None = None,
    ) -> None:
        super().__init__(message)
        self.code = code
        self.http_status = http_status

    def as_dict(self) -> dict[str, Any]:
        result: dict[str, Any] = {
            "state": "failed",
            "code": self.code,
            "message": str(self),
        }
        if self.http_status is not None:
            result["http_status"] = self.http_status
        return result


class YouTubeConfigurationError(YouTubePublishError):
    """Local configuration or media input is incomplete."""


class YouTubeAuthenticationError(YouTubePublishError):
    """OAuth credentials are absent, invalid, expired, or revoked."""


class YouTubePermissionError(YouTubePublishError):
    """The authorized account cannot perform the requested operation."""


class YouTubeQuotaError(YouTubePublishError):
    """A YouTube project, channel, or rate quota stopped the request."""


class YouTubeAuditBlockerError(YouTubePublishError):
    """An unverified API project kept a requested public upload private."""


class YouTubeTransientError(YouTubePublishError):
    """A retryable provider or transport failure exhausted its retry budget."""


class YouTubeProtocolError(YouTubePublishError):
    """The provider returned a successful but unusable response."""


class YouTubeProcessingError(YouTubePublishError):
    """YouTube rejected, failed, or did not finish processing the upload."""


@dataclass(frozen=True)
class _PublishInput:
    media_path: Path
    title: str
    description: str
    category_id: str
    privacy_status: str
    publish_at: str | None
    made_for_kids: bool
    contains_synthetic_media: bool
    notify_subscribers: bool
    tags: tuple[str, ...]

    def metadata(self) -> dict[str, Any]:
        status: dict[str, Any] = {
            "privacyStatus": self.privacy_status,
            "selfDeclaredMadeForKids": self.made_for_kids,
            "containsSyntheticMedia": self.contains_synthetic_media,
        }
        if self.publish_at is not None:
            status["publishAt"] = self.publish_at
        snippet: dict[str, Any] = {
            "title": self.title,
            "description": self.description,
            "categoryId": self.category_id,
        }
        if self.tags:
            snippet["tags"] = list(self.tags)
        return {"snippet": snippet, "status": status}


@dataclass(frozen=True)
class _Endpoints:
    token_url: str
    insert_url: str
    list_url: str
    watch_url_template: str


@dataclass(frozen=True)
class _RetryPolicy:
    max_attempts: int
    base_delay_seconds: float
    max_delay_seconds: float
    timeout_seconds: float


@dataclass(frozen=True)
class _Response:
    status: int | None
    headers: Mapping[str, str] = field(repr=False)
    body: bytes = field(repr=False)
    transport_failed: bool = False
    body_unavailable: bool = False


class _MediaBody(Iterable[bytes]):
    """Re-openable file slice so an upload chunk can be retried safely."""

    def __init__(
        self,
        path: Path,
        *,
        offset: int = 0,
        length: int | None = None,
        chunk_size: int = MEDIA_CHUNK_BYTES,
    ) -> None:
        self._path = path
        self._offset = offset
        self._length = length
        self._chunk_size = chunk_size

    def __iter__(self) -> Iterable[bytes]:
        with self._path.open("rb") as handle:
            handle.seek(self._offset)
            remaining = self._length
            while True:
                if remaining is not None and remaining <= 0:
                    return
                read_size = self._chunk_size
                if remaining is not None:
                    read_size = min(read_size, remaining)
                chunk = handle.read(read_size)
                if not chunk:
                    return
                yield chunk
                if remaining is not None:
                    remaining -= len(chunk)


def _first_env(env: Mapping[str, str], names: tuple[str, ...]) -> str | None:
    for name in names:
        value = env.get(name)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return None


def _parse_int_env(
    env: Mapping[str, str],
    name: str,
    default: int,
    *,
    minimum: int,
    maximum: int,
) -> int:
    raw = env.get(name)
    if raw is None or not str(raw).strip():
        return default
    try:
        value = int(str(raw).strip())
    except (TypeError, ValueError):
        value = minimum - 1
    if not minimum <= value <= maximum:
        raise YouTubeConfigurationError(
            "configuration_invalid",
            "A YouTube numeric setting is outside its supported range.",
        )
    return value


def _parse_float_env(
    env: Mapping[str, str],
    name: str,
    default: float,
    *,
    minimum: float,
    maximum: float,
) -> float:
    raw = env.get(name)
    if raw is None or not str(raw).strip():
        return default
    try:
        value = float(str(raw).strip())
    except (TypeError, ValueError):
        value = minimum - 1.0
    if not minimum <= value <= maximum:
        raise YouTubeConfigurationError(
            "configuration_invalid",
            "A YouTube numeric setting is outside its supported range.",
        )
    return value


def _validate_url(value: str) -> str:
    try:
        parsed = urllib.parse.urlsplit(value)
    except (TypeError, ValueError):
        parsed = urllib.parse.SplitResult("", "", "", "", "")
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise YouTubeConfigurationError(
            "configuration_invalid",
            "A YouTube endpoint URL is invalid.",
        )
    return value


def _load_endpoints(env: Mapping[str, str]) -> _Endpoints:
    token_url = _first_env(env, ("YOUTUBE_TOKEN_URL", "YOUTUBE_OAUTH_TOKEN_URL"))
    insert_url = _first_env(
        env,
        ("YOUTUBE_VIDEOS_INSERT_URL", "YOUTUBE_UPLOAD_URL"),
    )
    list_url = _first_env(
        env,
        ("YOUTUBE_VIDEOS_LIST_URL", "YOUTUBE_API_VIDEOS_URL"),
    )

    api_base = _first_env(env, ("YOUTUBE_API_BASE_URL",))
    if list_url is None and api_base is not None:
        list_url = api_base.rstrip("/") + "/videos"

    upload_base = _first_env(env, ("YOUTUBE_UPLOAD_BASE_URL",))
    if insert_url is None and upload_base is not None:
        insert_url = upload_base.rstrip("/") + "/videos"

    watch_template = _first_env(env, ("YOUTUBE_WATCH_URL_TEMPLATE",))
    watch_base = _first_env(env, ("YOUTUBE_WATCH_BASE_URL",))
    if watch_template is None and watch_base is not None:
        watch_template = watch_base.rstrip("/") + "/{video_id}"

    token_url = _validate_url(token_url or DEFAULT_TOKEN_URL)
    insert_url = _validate_url(insert_url or DEFAULT_VIDEOS_INSERT_URL)
    list_url = _validate_url(list_url or DEFAULT_VIDEOS_LIST_URL)
    watch_template = watch_template or DEFAULT_WATCH_URL_TEMPLATE
    if "{video_id}" not in watch_template:
        raise YouTubeConfigurationError(
            "configuration_invalid",
            "The YouTube watch URL template must contain the video ID placeholder.",
        )
    # Validate with a harmless placeholder rather than provider-supplied data.
    _validate_url(watch_template.replace("{video_id}", "video"))
    return _Endpoints(token_url, insert_url, list_url, watch_template)


def _load_retry_policy(env: Mapping[str, str]) -> _RetryPolicy:
    return _RetryPolicy(
        max_attempts=_parse_int_env(
            env,
            "YOUTUBE_HTTP_MAX_ATTEMPTS",
            4,
            minimum=1,
            maximum=10,
        ),
        base_delay_seconds=_parse_float_env(
            env,
            "YOUTUBE_HTTP_RETRY_BASE_SECONDS",
            1.0,
            minimum=0.0,
            maximum=60.0,
        ),
        max_delay_seconds=_parse_float_env(
            env,
            "YOUTUBE_HTTP_RETRY_MAX_SECONDS",
            16.0,
            minimum=0.0,
            maximum=300.0,
        ),
        timeout_seconds=_parse_float_env(
            env,
            "YOUTUBE_HTTP_TIMEOUT_SECONDS",
            60.0,
            minimum=1.0,
            maximum=600.0,
        ),
    )


def _config_value(
    config: Mapping[str, Any],
    names: tuple[str, ...],
    *,
    required: bool = True,
    default: Any = None,
) -> Any:
    for name in names:
        if name in config:
            return config[name]
    if required:
        raise YouTubeConfigurationError(
            "configuration_missing",
            "The YouTube publish configuration is incomplete.",
        )
    return default


def _required_bool(config: Mapping[str, Any], names: tuple[str, ...]) -> bool:
    value = _config_value(config, names)
    if type(value) is not bool:
        raise YouTubeConfigurationError(
            "configuration_invalid",
            "A YouTube content declaration must be a JSON boolean.",
        )
    return value


def _optional_bool(
    config: Mapping[str, Any],
    names: tuple[str, ...],
    default: bool,
) -> bool:
    value = _config_value(config, names, required=False, default=default)
    if type(value) is not bool:
        raise YouTubeConfigurationError(
            "configuration_invalid",
            "A YouTube publish option must be a JSON boolean.",
        )
    return value


def _normalize_publish_at(value: Any) -> str | None:
    if value is None or value == "":
        return None
    if isinstance(value, datetime):
        if value.tzinfo is None:
            raise YouTubeConfigurationError(
                "configuration_invalid",
                "The YouTube publish time must include a timezone.",
            )
        normalized = value.isoformat()
    elif isinstance(value, str):
        normalized = value.strip()
    else:
        normalized = ""

    if not normalized:
        raise YouTubeConfigurationError(
            "configuration_invalid",
            "The YouTube publish time is invalid.",
        )
    try:
        parsed = datetime.fromisoformat(normalized.replace("Z", "+00:00"))
    except ValueError:
        parsed = None
    if parsed is None or parsed.tzinfo is None:
        raise YouTubeConfigurationError(
            "configuration_invalid",
            "The YouTube publish time must be an ISO 8601 timestamp with timezone.",
        )
    return normalized


def _resolve_media_path(config: Mapping[str, Any], asset_root: Path) -> Path:
    raw_path = _config_value(config, ("media_path", "asset_path"))
    if not isinstance(raw_path, (str, os.PathLike)) or not str(raw_path).strip():
        raise YouTubeConfigurationError(
            "configuration_invalid",
            "The YouTube media path is invalid.",
        )
    try:
        root = Path(asset_root).expanduser().resolve(strict=True)
        supplied = Path(raw_path).expanduser()
        candidate = supplied.resolve(strict=True) if supplied.is_absolute() else (root / supplied).resolve(strict=True)
        candidate.relative_to(root)
    except (OSError, RuntimeError, ValueError):
        raise YouTubeConfigurationError(
            "media_unavailable",
            "The YouTube media file is missing or outside the allowed asset root.",
        ) from None
    if not candidate.is_file():
        raise YouTubeConfigurationError(
            "media_unavailable",
            "The YouTube media file is not a regular file.",
        )
    try:
        size = candidate.stat().st_size
    except OSError:
        size = 0
    if size <= 0:
        raise YouTubeConfigurationError(
            "media_unavailable",
            "The YouTube media file is empty or unavailable.",
        )
    return candidate


def _normalize_config(config: Mapping[str, Any], asset_root: Path) -> _PublishInput:
    if not isinstance(config, Mapping):
        raise YouTubeConfigurationError(
            "configuration_invalid",
            "The YouTube publish configuration must be a mapping.",
        )

    title = _config_value(config, ("title",))
    description = _config_value(config, ("description",))
    category = _config_value(config, ("category_id", "categoryId", "category"))
    privacy = _config_value(
        config,
        ("privacy_status", "privacyStatus"),
        required=False,
        default="private",
    )
    publish_at = _normalize_publish_at(
        _config_value(
            config,
            ("publish_at", "publishAt"),
            required=False,
            default=None,
        )
    )

    if not isinstance(title, str) or not title.strip() or len(title) > 100:
        raise YouTubeConfigurationError(
            "configuration_invalid",
            "The YouTube title is empty or too long.",
        )
    if not isinstance(description, str) or len(description.encode("utf-8")) > 5000:
        raise YouTubeConfigurationError(
            "configuration_invalid",
            "The YouTube description is invalid or too long.",
        )
    if isinstance(category, bool) or not str(category).strip().isdigit():
        raise YouTubeConfigurationError(
            "configuration_invalid",
            "The YouTube category ID is invalid.",
        )
    if not isinstance(privacy, str) or privacy not in {"private", "public", "unlisted"}:
        raise YouTubeConfigurationError(
            "configuration_invalid",
            "The YouTube privacy status is invalid.",
        )
    if publish_at is not None and privacy != "private":
        raise YouTubeConfigurationError(
            "configuration_invalid",
            "YouTube scheduled publishing requires private privacy status.",
        )

    raw_tags = _config_value(config, ("tags",), required=False, default=[])
    if not isinstance(raw_tags, list) or len(raw_tags) > 15:
        raise YouTubeConfigurationError(
            "configuration_invalid",
            "The YouTube tags configuration is invalid.",
        )
    tags: list[str] = []
    for raw_tag in raw_tags:
        if not isinstance(raw_tag, str) or not raw_tag.strip() or len(raw_tag.strip()) > 50:
            raise YouTubeConfigurationError(
                "configuration_invalid",
                "The YouTube tags configuration is invalid.",
            )
        tags.append(raw_tag.strip())

    return _PublishInput(
        media_path=_resolve_media_path(config, asset_root),
        title=title,
        description=description,
        category_id=str(category).strip(),
        privacy_status=privacy,
        publish_at=publish_at,
        made_for_kids=_required_bool(
            config,
            (
                "made_for_kids",
                "self_declared_made_for_kids",
                "selfDeclaredMadeForKids",
            ),
        ),
        contains_synthetic_media=_required_bool(
            config,
            ("contains_synthetic_media", "containsSyntheticMedia"),
        ),
        notify_subscribers=_optional_bool(
            config,
            ("notify_subscribers", "notifySubscribers"),
            True,
        ),
        tags=tuple(tags),
    )


def _with_query(url: str, values: Mapping[str, str]) -> str:
    parsed = urllib.parse.urlsplit(url)
    pairs = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    replacement_keys = set(values)
    pairs = [(key, value) for key, value in pairs if key not in replacement_keys]
    pairs.extend(values.items())
    return urllib.parse.urlunsplit(
        (
            parsed.scheme,
            parsed.netloc,
            parsed.path,
            urllib.parse.urlencode(pairs),
            parsed.fragment,
        )
    )


def _header_map(response: Any) -> dict[str, str]:
    try:
        source = response.headers
        items = source.items()
    except Exception:
        return {}
    result: dict[str, str] = {}
    try:
        for key, value in items:
            result[str(key).lower()] = str(value)
    except Exception:
        return {}
    return result


def _read_response(response: Any, *, status_override: int | None = None) -> _Response:
    try:
        status_value = status_override
        if status_value is None:
            status_value = getattr(response, "status", None)
        if status_value is None and hasattr(response, "getcode"):
            status_value = response.getcode()
        status = int(status_value) if status_value is not None else None
    except Exception:
        status = status_override

    headers = _header_map(response)
    body_unavailable = False
    try:
        reader = response.read
        try:
            body = reader(MAX_RESPONSE_BYTES + 1)
        except TypeError:
            # Lightweight test doubles often implement ``read()`` without the
            # optional size argument.  The hard size check below still applies.
            body = reader()
        if not isinstance(body, bytes):
            body = bytes(body or b"")
    except Exception:
        body = b""
        body_unavailable = True
    finally:
        try:
            response.close()
        except Exception:
            pass

    if len(body) > MAX_RESPONSE_BYTES:
        body = b""
        body_unavailable = True
    return _Response(
        status=status,
        headers=headers,
        body=body,
        body_unavailable=body_unavailable,
    )


def _open_once(
    opener: Callable[..., Any],
    request: urllib.request.Request,
    timeout_seconds: float,
) -> _Response:
    response: Any = None
    http_error: urllib.error.HTTPError | None = None
    transport_failed = False
    try:
        try:
            signature = inspect.signature(opener)
        except (TypeError, ValueError):
            supports_timeout = True
        else:
            parameters = signature.parameters.values()
            supports_timeout = "timeout" in signature.parameters or any(
                parameter.kind == inspect.Parameter.VAR_KEYWORD
                for parameter in parameters
            )
        if supports_timeout:
            response = opener(request, timeout=timeout_seconds)
        else:
            response = opener(request)
    except urllib.error.HTTPError as exc:
        http_error = exc
    except Exception:
        transport_failed = True

    # Process provider material only after leaving the exception handler so a
    # sanitized exception raised later has no displayed provider exception.
    if transport_failed:
        return _Response(None, {}, b"", transport_failed=True)
    if http_error is not None:
        return _read_response(http_error, status_override=http_error.code)
    if response is None:
        return _Response(None, {}, b"", transport_failed=True)
    return _read_response(response)


def _decode_json(body: bytes) -> Any:
    decoded: Any = None
    valid = True
    try:
        decoded = json.loads(body.decode("utf-8"))
    except Exception:
        valid = False
    if not valid:
        raise YouTubeProtocolError(
            "provider_response_invalid",
            "YouTube returned an unreadable response.",
        ) from None
    return decoded


def _provider_error_reason(body: bytes) -> str:
    """Return only a normalized internal classifier, never the provider text."""

    try:
        payload = json.loads(body.decode("utf-8"))
    except Exception:
        return ""
    if not isinstance(payload, Mapping):
        return ""
    error = payload.get("error")
    if isinstance(error, str):
        return error.lower()
    if not isinstance(error, Mapping):
        return ""
    details = error.get("errors")
    if isinstance(details, list):
        for item in details:
            if isinstance(item, Mapping) and isinstance(item.get("reason"), str):
                return item["reason"].lower()
    status = error.get("status")
    if isinstance(status, str):
        return status.lower()
    return ""


def _classified_error(stage: str, response: _Response) -> YouTubePublishError:
    status = response.status
    reason = _provider_error_reason(response.body)

    if stage == "oauth":
        if reason == "invalid_grant":
            return YouTubeAuthenticationError(
                "oauth_refresh_invalid",
                "YouTube OAuth authorization must be renewed.",
                http_status=status,
            )
        if reason in {"invalid_client", "deleted_client"}:
            return YouTubeAuthenticationError(
                "oauth_client_invalid",
                "The YouTube OAuth client configuration is invalid.",
                http_status=status,
            )
        if status == 429:
            return YouTubeQuotaError(
                "rate_limited",
                "YouTube temporarily rate-limited the OAuth request.",
                http_status=status,
            )
        if status is not None and status >= 500:
            return YouTubeTransientError(
                "provider_unavailable",
                "YouTube OAuth is temporarily unavailable after bounded retries.",
                http_status=status,
            )
        return YouTubeAuthenticationError(
            "oauth_refresh_failed",
            "YouTube OAuth did not accept the refresh request.",
            http_status=status,
        )

    if reason in {
        "quotaexceeded",
        "dailylimitexceeded",
        "uploadlimitexceeded",
        "userratelimitexceeded",
    }:
        code = "upload_limit_exceeded" if reason == "uploadlimitexceeded" else "quota_exceeded"
        return YouTubeQuotaError(
            code,
            "A YouTube project or channel quota blocked the upload.",
            http_status=status,
        )
    if status == 429:
        return YouTubeQuotaError(
            "rate_limited",
            "YouTube rate-limited the request after bounded retries.",
            http_status=status,
        )
    if status == 401:
        return YouTubeAuthenticationError(
            "access_token_rejected",
            "YouTube rejected the refreshed access token.",
            http_status=status,
        )
    if status == 403:
        return YouTubePermissionError(
            "permission_denied",
            "The authorized YouTube account cannot perform this operation.",
            http_status=status,
        )
    if status is not None and status >= 500:
        return YouTubeTransientError(
            "provider_unavailable",
            "YouTube is temporarily unavailable after bounded retries.",
            http_status=status,
        )
    return YouTubePublishError(
        "request_rejected",
        "YouTube rejected the publish request.",
        http_status=status,
    )


def _retry_delay(policy: _RetryPolicy, attempt_index: int, headers: Mapping[str, str]) -> float:
    delay = min(
        policy.max_delay_seconds,
        policy.base_delay_seconds * (2**attempt_index),
    )
    retry_after = headers.get("retry-after")
    if retry_after:
        try:
            delay = min(policy.max_delay_seconds, max(delay, float(retry_after)))
        except ValueError:
            pass
    return max(0.0, delay)


def _request_with_retry(
    request_factory: Callable[[], urllib.request.Request],
    *,
    opener: Callable[..., Any],
    sleep_func: Callable[[float], None],
    policy: _RetryPolicy,
    stage: str,
    expected_statuses: frozenset[int],
) -> _Response:
    last_response = _Response(None, {}, b"", transport_failed=True)
    for attempt in range(policy.max_attempts):
        request = request_factory()
        response = _open_once(opener, request, policy.timeout_seconds)
        last_response = response
        if response.status in expected_statuses and not response.transport_failed:
            if response.body_unavailable:
                raise YouTubeProtocolError(
                    "provider_response_invalid",
                    "YouTube returned an unreadable response.",
                    http_status=response.status,
                )
            return response

        retryable = response.transport_failed or response.status == 429 or (
            response.status is not None and response.status >= 500
        )
        if retryable and attempt + 1 < policy.max_attempts:
            sleep_func(_retry_delay(policy, attempt, response.headers))
            continue
        break

    if last_response.transport_failed:
        raise YouTubeTransientError(
            "transport_unavailable",
            "The YouTube request failed after bounded transport retries.",
        ) from None
    raise _classified_error(stage, last_response) from None


def _refresh_access_token(
    *,
    client_id: str,
    client_secret: str,
    refresh_token: str,
    endpoint: str,
    opener: Callable[..., Any],
    sleep_func: Callable[[float], None],
    policy: _RetryPolicy,
) -> str:
    form_body = urllib.parse.urlencode(
        {
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh_token,
            "grant_type": "refresh_token",
        }
    ).encode("ascii")

    def request_factory() -> urllib.request.Request:
        return urllib.request.Request(
            endpoint,
            data=form_body,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            method="POST",
        )

    response = _request_with_retry(
        request_factory,
        opener=opener,
        sleep_func=sleep_func,
        policy=policy,
        stage="oauth",
        expected_statuses=frozenset({200}),
    )
    payload = _decode_json(response.body)
    access_token = payload.get("access_token") if isinstance(payload, Mapping) else None
    if not isinstance(access_token, str) or not access_token:
        raise YouTubeProtocolError(
            "oauth_response_invalid",
            "YouTube OAuth did not return a usable access token.",
            http_status=response.status,
        )
    return access_token


def _start_resumable_upload(
    publish_input: _PublishInput,
    *,
    access_token: str,
    endpoint: str,
    opener: Callable[..., Any],
    sleep_func: Callable[[float], None],
    policy: _RetryPolicy,
) -> str:
    upload_url = _with_query(
        endpoint,
        {
            "uploadType": "resumable",
            "part": "snippet,status",
            "notifySubscribers": "true" if publish_input.notify_subscribers else "false",
        },
    )
    metadata_body = json.dumps(
        publish_input.metadata(),
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    media_size = publish_input.media_path.stat().st_size
    media_type = mimetypes.guess_type(publish_input.media_path.name)[0] or "application/octet-stream"

    def request_factory() -> urllib.request.Request:
        return urllib.request.Request(
            upload_url,
            data=metadata_body,
            headers={
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json; charset=UTF-8",
                "X-Upload-Content-Length": str(media_size),
                "X-Upload-Content-Type": media_type,
            },
            method="POST",
        )

    # Session creation is a write without an idempotency key.  If its response
    # is lost, or YouTube answers with a retryable status, creating a second
    # session could later create a duplicate video.  Make exactly one attempt
    # and leave the reserved control-plane item for explicit inspection.
    del sleep_func
    response = _open_once(opener, request_factory(), policy.timeout_seconds)
    if response.transport_failed or response.status == 429 or (
        response.status is not None and response.status >= 500
    ):
        raise YouTubeTransientError(
            "upload_session_ambiguous",
            "YouTube resumable session creation could not be confirmed; publishing is paused to prevent a duplicate upload.",
            http_status=response.status,
        ) from None
    if response.status not in {200, 201}:
        raise _classified_error("api", response) from None
    session_url = response.headers.get("location")
    if not session_url:
        raise YouTubeProtocolError(
            "upload_session_missing",
            "YouTube did not return a resumable upload session.",
            http_status=response.status,
        )
    return _validate_url(session_url)


def _video_id_from_final_upload(response: _Response) -> str:
    payload = _decode_json(response.body)
    video_id = payload.get("id") if isinstance(payload, Mapping) else None
    if not isinstance(video_id, str) or not VIDEO_ID_RE.fullmatch(video_id):
        raise YouTubeProtocolError(
            "video_id_missing",
            "YouTube did not return a usable video ID.",
            http_status=response.status,
        )
    return video_id


def _acknowledged_upload_offset(response: _Response, media_size: int) -> int:
    """Parse the next byte offset from a resumable 308 response.

    YouTube omits ``Range`` when it has not persisted any bytes.  The returned
    value is therefore zero in that case.  No provider header value is copied
    into an exception.
    """

    acknowledged = response.headers.get("range", "").strip()
    if not acknowledged:
        return 0
    match = re.fullmatch(r"bytes=0-(\d+)", acknowledged, re.IGNORECASE)
    if match is None:
        raise YouTubeProtocolError(
            "upload_resume_invalid",
            "YouTube did not return a usable resumable upload offset.",
            http_status=response.status,
        )
    next_offset = int(match.group(1)) + 1
    if next_offset < 0 or next_offset > media_size:
        raise YouTubeProtocolError(
            "upload_resume_invalid",
            "YouTube returned an invalid resumable upload offset.",
            http_status=response.status,
        )
    return next_offset


def _query_resumable_upload(
    *,
    access_token: str,
    session_url: str,
    media_size: int,
    opener: Callable[..., Any],
    sleep_func: Callable[[float], None],
    policy: _RetryPolicy,
) -> _Response:
    """Safely query a session after an ambiguous chunk response."""

    def request_factory() -> urllib.request.Request:
        return urllib.request.Request(
            session_url,
            data=b"",
            headers={
                "Authorization": f"Bearer {access_token}",
                "Content-Length": "0",
                "Content-Range": f"bytes */{media_size}",
            },
            method="PUT",
        )

    # A status query carries no media bytes, so bounded retry is safe here.
    return _request_with_retry(
        request_factory,
        opener=opener,
        sleep_func=sleep_func,
        policy=policy,
        stage="api",
        expected_statuses=frozenset({200, 201, 308}),
    )


def _upload_media(
    publish_input: _PublishInput,
    *,
    access_token: str,
    session_url: str,
    env: Mapping[str, str],
    opener: Callable[..., Any],
    sleep_func: Callable[[float], None],
    policy: _RetryPolicy,
) -> str:
    media_size = publish_input.media_path.stat().st_size
    media_type = mimetypes.guess_type(publish_input.media_path.name)[0] or "application/octet-stream"
    # YouTube requires resumable chunks (except the final chunk) to be a
    # multiple of 256 KiB.  Eight MiB keeps runner memory low without creating
    # an excessive number of requests.
    upload_chunk_bytes = _parse_int_env(
        env,
        "YOUTUBE_UPLOAD_CHUNK_BYTES",
        8 * 1024 * 1024,
        minimum=256 * 1024,
        maximum=64 * 1024 * 1024,
    )
    if upload_chunk_bytes % (256 * 1024) != 0:
        raise YouTubeConfigurationError(
            "configuration_invalid",
            "The YouTube resumable upload chunk size must be a multiple of 256 KiB.",
        )
    offset = 0
    stalled_attempts = 0
    completion_checks = 0

    while True:
        # A 308 may acknowledge the final byte while the terminal resource
        # response is still unavailable.  Query until YouTube returns that
        # resource; never infer success from byte count alone.
        if offset == media_size:
            if completion_checks >= policy.max_attempts:
                raise YouTubeTransientError(
                    "upload_completion_ambiguous",
                    "YouTube acknowledged all media bytes but did not confirm the completed video.",
                )
            response = _query_resumable_upload(
                access_token=access_token,
                session_url=session_url,
                media_size=media_size,
                opener=opener,
                sleep_func=sleep_func,
                policy=policy,
            )
            if response.status in {200, 201}:
                return _video_id_from_final_upload(response)
            confirmed_offset = _acknowledged_upload_offset(response, media_size)
            if confirmed_offset != media_size:
                if confirmed_offset > offset:
                    raise YouTubeProtocolError(
                        "upload_resume_invalid",
                        "YouTube returned an invalid resumable upload offset.",
                        http_status=response.status,
                    )
                offset = confirmed_offset
                completion_checks = 0
                stalled_attempts = 0
                continue
            completion_checks += 1
            if completion_checks < policy.max_attempts:
                sleep_func(_retry_delay(policy, completion_checks - 1, response.headers))
            continue

        chunk_length = min(upload_chunk_bytes, media_size - offset)
        chunk_end = offset + chunk_length - 1

        def request_factory(
            start: int = offset,
            length: int = chunk_length,
            end: int = chunk_end,
        ) -> urllib.request.Request:
            return urllib.request.Request(
                session_url,
                data=_MediaBody(
                    publish_input.media_path,
                    offset=start,
                    length=length,
                ),
                headers={
                    "Authorization": f"Bearer {access_token}",
                    "Content-Length": str(length),
                    "Content-Range": f"bytes {start}-{end}/{media_size}",
                    "Content-Type": media_type,
                },
                method="PUT",
            )

        # A media PUT may have been partly or fully committed even when the
        # caller receives a transport error, 429, or 5xx.  Do not resend it
        # until the session URI reports its durable offset.
        response = _open_once(opener, request_factory(), policy.timeout_seconds)
        ambiguous_write = response.transport_failed or response.status == 429 or (
            response.status is not None and response.status >= 500
        )
        ambiguity_response = response
        if ambiguous_write:
            response = _query_resumable_upload(
                access_token=access_token,
                session_url=session_url,
                media_size=media_size,
                opener=opener,
                sleep_func=sleep_func,
                policy=policy,
            )

        if response.status in {200, 201}:
            if not ambiguous_write and chunk_end + 1 != media_size:
                raise YouTubeProtocolError(
                    "upload_response_invalid",
                    "YouTube completed a resumable upload before all media was sent.",
                    http_status=response.status,
                )
            return _video_id_from_final_upload(response)
        if response.status != 308:
            raise _classified_error("api", response) from None

        next_offset = _acknowledged_upload_offset(response, media_size)
        if next_offset < offset or next_offset > chunk_end + 1:
            raise YouTubeProtocolError(
                "upload_resume_invalid",
                "YouTube returned an invalid resumable upload offset.",
                http_status=response.status,
            )
        if next_offset == offset:
            stalled_attempts += 1
            if stalled_attempts >= policy.max_attempts:
                raise YouTubeTransientError(
                    "upload_state_ambiguous",
                    "YouTube did not confirm progress for the resumable media upload.",
                    http_status=ambiguity_response.status,
                )
            sleep_func(
                _retry_delay(
                    policy,
                    stalled_attempts - 1,
                    ambiguity_response.headers,
                )
            )
        else:
            stalled_attempts = 0
        offset = next_offset
        completion_checks = 0


def _poll_processing(
    video_id: str,
    requested_privacy: str,
    *,
    access_token: str,
    endpoint: str,
    env: Mapping[str, str],
    opener: Callable[..., Any],
    sleep_func: Callable[[float], None],
    policy: _RetryPolicy,
) -> tuple[str, str]:
    max_polls = _parse_int_env(
        env,
        "YOUTUBE_PROCESSING_MAX_POLLS",
        60,
        minimum=1,
        maximum=720,
    )
    poll_interval = _parse_float_env(
        env,
        "YOUTUBE_PROCESSING_POLL_SECONDS",
        10.0,
        minimum=0.0,
        maximum=300.0,
    )
    list_url = _with_query(
        endpoint,
        {
            "part": "status,processingDetails",
            "id": video_id,
        },
    )

    for poll_index in range(max_polls):
        def request_factory() -> urllib.request.Request:
            return urllib.request.Request(
                list_url,
                headers={"Authorization": f"Bearer {access_token}"},
                method="GET",
            )

        response = _request_with_retry(
            request_factory,
            opener=opener,
            sleep_func=sleep_func,
            policy=policy,
            stage="api",
            expected_statuses=frozenset({200}),
        )
        payload = _decode_json(response.body)
        items = payload.get("items") if isinstance(payload, Mapping) else None
        item = items[0] if isinstance(items, list) and items else None
        if not isinstance(item, Mapping):
            raise YouTubeProtocolError(
                "video_status_missing",
                "YouTube did not return the uploaded video's status.",
                http_status=response.status,
            )

        status_obj = item.get("status")
        processing_obj = item.get("processingDetails")
        status_obj = status_obj if isinstance(status_obj, Mapping) else {}
        processing_obj = processing_obj if isinstance(processing_obj, Mapping) else {}
        privacy_status = status_obj.get("privacyStatus")
        upload_status = status_obj.get("uploadStatus")
        processing_status = processing_obj.get("processingStatus")

        if (
            requested_privacy in {"public", "unlisted"}
            and privacy_status == "private"
        ):
            raise YouTubeAuditBlockerError(
                "youtube_api_audit_required",
                "YouTube kept the requested public or unlisted upload private; the API project must pass YouTube's compliance audit.",
                http_status=response.status,
            )
        if upload_status == "failed":
            raise YouTubeProcessingError(
                "upload_failed",
                "YouTube could not process the uploaded media.",
                http_status=response.status,
            )
        if upload_status == "rejected":
            raise YouTubeProcessingError(
                "upload_rejected",
                "YouTube rejected the uploaded media.",
                http_status=response.status,
            )
        if processing_status == "failed":
            raise YouTubeProcessingError(
                "processing_failed",
                "YouTube video processing failed.",
                http_status=response.status,
            )
        if processing_status == "terminated":
            raise YouTubeProcessingError(
                "processing_terminated",
                "YouTube video processing terminated.",
                http_status=response.status,
            )
        if processing_status == "succeeded":
            if privacy_status not in {"private", "public", "unlisted"}:
                raise YouTubeProtocolError(
                    "video_status_invalid",
                    "YouTube returned an invalid privacy status.",
                    http_status=response.status,
                )
            return processing_status, str(privacy_status)

        if poll_index + 1 < max_polls:
            sleep_func(poll_interval)

    raise YouTubeProcessingError(
        "processing_timeout",
        "YouTube video processing did not finish within the configured polling window.",
    )


def publish_youtube(
    config: Mapping[str, Any],
    *,
    asset_root: Path,
    env: Mapping[str, str],
    opener: Callable[..., Any] | None = None,
    sleep_func: Callable[[float], None] = time.sleep,
    now: Any = None,
    receipt_callback: Callable[[Mapping[str, Any]], None] | None = None,
) -> dict[str, Any]:
    """Publish a configured local asset and return a sanitized receipt.

    ``now`` is accepted for the shared control-plane adapter contract.  The
    YouTube API itself decides whether a supplied ``publishAt`` is valid, so
    this adapter intentionally does not rewrite or compare it with local time.
    """

    del now
    publish_input = _normalize_config(config, Path(asset_root))
    endpoints = _load_endpoints(env)
    retry_policy = _load_retry_policy(env)

    client_id = _first_env(env, ("YOUTUBE_CLIENT_ID",))
    client_secret = _first_env(env, ("YOUTUBE_CLIENT_SECRET",))
    refresh_token = _first_env(
        env,
        ("YOUTUBE_REFRESH_TOKEN", "YOUTUBE_OAUTH_REFRESH_TOKEN"),
    )
    if not all((client_id, client_secret, refresh_token)):
        raise YouTubeAuthenticationError(
            "oauth_configuration_missing",
            "YouTube OAuth credentials are incomplete.",
        )

    active_opener = opener or urllib.request.urlopen
    access_token = _refresh_access_token(
        client_id=str(client_id),
        client_secret=str(client_secret),
        refresh_token=str(refresh_token),
        endpoint=endpoints.token_url,
        opener=active_opener,
        sleep_func=sleep_func,
        policy=retry_policy,
    )
    session_url = _start_resumable_upload(
        publish_input,
        access_token=access_token,
        endpoint=endpoints.insert_url,
        opener=active_opener,
        sleep_func=sleep_func,
        policy=retry_policy,
    )
    video_id = _upload_media(
        publish_input,
        access_token=access_token,
        session_url=session_url,
        env=env,
        opener=active_opener,
        sleep_func=sleep_func,
        policy=retry_policy,
    )
    if receipt_callback is not None:
        # The video resource now exists. Persist its locator before processing
        # and visibility polling so an audit/status failure remains traceable
        # without attempting another upload.
        receipt_callback({
            "video_id": video_id,
            "publish_at": publish_input.publish_at,
        })
    processing_status, privacy_status = _poll_processing(
        video_id,
        publish_input.privacy_status,
        access_token=access_token,
        endpoint=endpoints.list_url,
        env=env,
        opener=active_opener,
        sleep_func=sleep_func,
        policy=retry_policy,
    )

    try:
        watch_url = endpoints.watch_url_template.format(video_id=video_id)
    except Exception:
        raise YouTubeConfigurationError(
            "configuration_invalid",
            "The YouTube watch URL template is invalid.",
        ) from None
    _validate_url(watch_url)

    # Deliberately keep the receipt schema small and stable.  It must never
    # contain provider payloads, credential material, or the upload session URL.
    return {
        "state": "published",
        "video_id": video_id,
        "url": watch_url,
        "privacy_status": privacy_status,
        "processing_status": processing_status,
        "publish_at": publish_input.publish_at,
    }


def _read_cli_config(path: Path) -> Mapping[str, Any]:
    try:
        raw = path.read_bytes()
    except OSError:
        raise YouTubeConfigurationError(
            "configuration_unavailable",
            "The YouTube publish configuration file cannot be read.",
        ) from None
    if len(raw) > 1024 * 1024:
        raise YouTubeConfigurationError(
            "configuration_invalid",
            "The YouTube publish configuration file is too large.",
        )
    payload = _decode_json(raw)
    if not isinstance(payload, Mapping):
        raise YouTubeConfigurationError(
            "configuration_invalid",
            "The YouTube publish configuration must be a JSON object.",
        )
    return payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True, help="Publish manifest JSON")
    parser.add_argument(
        "--asset-root",
        type=Path,
        default=Path.cwd(),
        help="Allowed root for the local media artifact",
    )
    args = parser.parse_args(argv)

    try:
        receipt = publish_youtube(
            _read_cli_config(args.config),
            asset_root=args.asset_root,
            env=os.environ,
        )
    except YouTubePublishError as exc:
        print(json.dumps(exc.as_dict(), ensure_ascii=False, sort_keys=True), file=sys.stderr)
        return 1
    print(json.dumps(receipt, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
