#!/usr/bin/env python3
"""Guarded, manifest-driven social publishing for GitHub Actions.

The control plane deliberately supports only top-level publishing through the
official YouTube, LinkedIn, and X APIs.  It has no browser, Cookie, reply,
comment, like, follow, repost, or engagement-automation path.

Publishing is split into reserve and publish phases.  The reservation is
committed before the first provider write.  An interrupted run therefore stays
``reserved`` and requires inspection instead of silently sending a duplicate.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import hmac
import json
import os
import re
import secrets
import sys
import tempfile
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping


SCHEMA_VERSION = 1
CONTENT_ID_RE = re.compile(r"^[a-z0-9][a-z0-9._-]{7,79}$")
HASHTAG_RE = re.compile(r"(?<!\w)#[\w\u3400-\u9fff]+", re.UNICODE)
MENTION_RE = re.compile(r"(?<![\w@])@[A-Za-z0-9_]{1,30}")
URL_RE = re.compile(r"https?://[^\s<>()]+", re.IGNORECASE)
PLACEHOLDER_RE = re.compile(r"\{\{([A-Z0-9_]+)\}\}")

PLATFORMS = ("youtube", "linkedin", "x")
SHORTENER_HOSTS = {
    "bit.ly",
    "buff.ly",
    "cutt.ly",
    "goo.gl",
    "is.gd",
    "ow.ly",
    "rebrand.ly",
    "shorturl.at",
    "tiny.cc",
    "tinyurl.com",
}

TOP_LEVEL_KEYS = {
    "schema_version",
    "content_id",
    "approved",
    "not_before",
    "source_url",
    "source",
    "platforms",
}
SOURCE_KEYS = {"run_id", "artifact_name"}
YOUTUBE_KEYS = {
    "enabled",
    "media_path",
    "media_sha256",
    "title",
    "description",
    "category_id",
    "privacy_status",
    "publish_at",
    "made_for_kids",
    "contains_synthetic_media",
    "notify_subscribers",
    "tags",
}
LINKEDIN_KEYS = {"enabled", "text"}
X_KEYS = {"enabled", "text"}

DEFAULT_LINKEDIN_POSTS_URL = "https://api.linkedin.com/rest/posts"
DEFAULT_X_POSTS_URL = "https://api.x.com/2/tweets"
DEFAULT_LINKEDIN_VERSION = "202608"
DEFAULT_MIN_INTERVAL_HOURS = 20
MIN_INTERVAL_FLOOR_HOURS = 4
NEAR_DUPLICATE_HAMMING_DISTANCE = 3


class ManifestError(ValueError):
    """The public manifest does not satisfy the publishing contract."""


class ProviderError(RuntimeError):
    """A sanitized provider failure suitable for a receipt and workflow log."""

    def __init__(self, platform: str, code: str, message: str):
        self.platform = platform
        self.code = code
        super().__init__(message)


@dataclass(frozen=True)
class ManifestPlan:
    path: Path
    manifest: dict[str, Any]
    digest: str
    content_id: str
    approved: bool
    not_before: datetime | None
    platforms: tuple[str, ...]
    fingerprints: dict[str, str]
    simhashes: dict[str, str]


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def iso_utc(value: datetime) -> str:
    return value.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_datetime(value: str, *, field: str) -> datetime:
    normalized = (value or "").strip()
    if not normalized:
        raise ManifestError(f"{field} must be a non-empty ISO 8601 timestamp")
    if normalized.endswith("Z"):
        normalized = f"{normalized[:-1]}+00:00"
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise ManifestError(f"{field} must be an ISO 8601 timestamp") from exc
    if parsed.tzinfo is None:
        raise ManifestError(f"{field} must include a timezone")
    return parsed.astimezone(timezone.utc)


def _require_mapping(value: Any, field: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ManifestError(f"{field} must be an object")
    return value


def _reject_unknown_keys(value: Mapping[str, Any], allowed: set[str], field: str) -> None:
    unknown = sorted(set(value) - allowed)
    if unknown:
        raise ManifestError(f"{field} contains unsupported fields: {', '.join(unknown)}")


def _require_bool(value: Any, field: str) -> bool:
    if not isinstance(value, bool):
        raise ManifestError(f"{field} must be true or false")
    return value


def _require_text(value: Any, field: str, *, minimum: int, maximum: int) -> str:
    if not isinstance(value, str):
        raise ManifestError(f"{field} must be text")
    text = value.strip()
    if not minimum <= len(text) <= maximum:
        raise ManifestError(f"{field} must contain {minimum}-{maximum} characters")
    return text


def normalize_text(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value).casefold()
    normalized = URL_RE.sub(" <url> ", normalized)
    return " ".join(normalized.split())


def content_fingerprint(value: str) -> str:
    return hashlib.sha256(normalize_text(value).encode("utf-8")).hexdigest()


def _simhash_tokens(value: str) -> list[str]:
    normalized = normalize_text(value)
    words = re.findall(r"[a-z0-9_]+|[\u3400-\u9fff]", normalized)
    tokens = list(words)
    cjk = "".join(token for token in words if len(token) == 1 and "\u3400" <= token <= "\u9fff")
    tokens.extend(cjk[index : index + 2] for index in range(max(0, len(cjk) - 1)))
    return tokens or [normalized]


def simhash64(value: str) -> str:
    vector = [0] * 64
    for token in _simhash_tokens(value):
        digest = hashlib.blake2b(token.encode("utf-8"), digest_size=8).digest()
        number = int.from_bytes(digest, "big")
        for bit in range(64):
            vector[bit] += 1 if number & (1 << bit) else -1
    result = 0
    for bit, score in enumerate(vector):
        if score >= 0:
            result |= 1 << bit
    return f"{result:016x}"


def hamming_distance(left: str, right: str) -> int:
    return (int(left, 16) ^ int(right, 16)).bit_count()


def canonical_manifest_bytes(manifest: Mapping[str, Any]) -> bytes:
    return json.dumps(
        manifest,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def validate_https_url(value: str, field: str) -> str:
    try:
        parsed = urllib.parse.urlparse(value)
    except ValueError as exc:
        raise ManifestError(f"{field} must be an HTTPS URL") from exc
    if parsed.scheme != "https" or not parsed.netloc or parsed.username or parsed.password:
        raise ManifestError(f"{field} must be an HTTPS URL without embedded credentials")
    host = (parsed.hostname or "").casefold()
    if host in SHORTENER_HOSTS or any(host.endswith(f".{item}") for item in SHORTENER_HOSTS):
        raise ManifestError(f"{field} must use the final destination URL, not a URL shortener")
    return value


def validate_text_urls(text: str, field: str) -> None:
    for index, value in enumerate(URL_RE.findall(text), start=1):
        validate_https_url(value.rstrip(".,;:!?)]}"), f"{field} URL {index}")


def validate_placeholders(text: str, field: str, *, youtube_enabled: bool) -> None:
    allowed = {"SOURCE_URL"}
    if youtube_enabled:
        allowed.add("YOUTUBE_URL")
    found = set(PLACEHOLDER_RE.findall(text))
    unknown = sorted(found - allowed)
    if unknown:
        raise ManifestError(f"{field} contains unsupported placeholders: {', '.join(unknown)}")
    if "YOUTUBE_URL" in found and not youtube_enabled:
        raise ManifestError(f"{field} uses YOUTUBE_URL but YouTube publishing is disabled")


def safe_asset_path(asset_root: Path, relative_path: str, *, must_exist: bool) -> Path:
    if not isinstance(relative_path, str) or not relative_path.strip():
        raise ManifestError("platforms.youtube.media_path must be a non-empty relative path")
    candidate_value = Path(relative_path)
    if candidate_value.is_absolute() or ".." in candidate_value.parts:
        raise ManifestError("platforms.youtube.media_path must stay inside the selected artifact")
    root = asset_root.resolve()
    candidate = (root / candidate_value).resolve()
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise ManifestError("platforms.youtube.media_path must stay inside the selected artifact") from exc
    if must_exist and (not candidate.is_file() or candidate.stat().st_size <= 0):
        raise ManifestError("the selected YouTube media file is missing or empty")
    return candidate


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _validate_youtube(
    config: Mapping[str, Any],
    *,
    asset_root: Path,
    require_media: bool,
) -> tuple[str, dict[str, Any]]:
    _reject_unknown_keys(config, YOUTUBE_KEYS, "platforms.youtube")
    title = _require_text(config.get("title"), "platforms.youtube.title", minimum=12, maximum=100)
    description = _require_text(
        config.get("description"),
        "platforms.youtube.description",
        minimum=100,
        maximum=5000,
    )
    validate_text_urls(description, "platforms.youtube.description")
    media_path = safe_asset_path(asset_root, config.get("media_path"), must_exist=require_media)
    media_sha256 = config.get("media_sha256")
    if not isinstance(media_sha256, str) or not re.fullmatch(r"[0-9a-f]{64}", media_sha256):
        raise ManifestError("platforms.youtube.media_sha256 must be a lowercase SHA-256")
    if require_media and file_sha256(media_path) != media_sha256:
        raise ManifestError("the selected YouTube media file does not match media_sha256")
    category_id = str(config.get("category_id", "")).strip()
    if not category_id.isdigit():
        raise ManifestError("platforms.youtube.category_id must contain digits")
    privacy = config.get("privacy_status")
    if privacy not in {"private", "unlisted", "public"}:
        raise ManifestError("platforms.youtube.privacy_status must be private, unlisted, or public")
    publish_at = config.get("publish_at")
    if publish_at is not None:
        if privacy != "private":
            raise ManifestError("scheduled YouTube publishing requires privacy_status=private")
        parse_datetime(publish_at, field="platforms.youtube.publish_at")
    _require_bool(config.get("made_for_kids"), "platforms.youtube.made_for_kids")
    _require_bool(
        config.get("contains_synthetic_media"),
        "platforms.youtube.contains_synthetic_media",
    )
    _require_bool(config.get("notify_subscribers"), "platforms.youtube.notify_subscribers")
    tags = config.get("tags", [])
    if not isinstance(tags, list) or len(tags) > 15 or any(
        not isinstance(tag, str) or not tag.strip() or len(tag.strip()) > 50 for tag in tags
    ):
        raise ManifestError("platforms.youtube.tags must contain at most 15 non-empty tags")
    combined = f"{title}\n{description}"
    return combined, {"title_length": len(title), "description_length": len(description)}


def _validate_linkedin(config: Mapping[str, Any], *, youtube_enabled: bool) -> tuple[str, dict[str, Any]]:
    _reject_unknown_keys(config, LINKEDIN_KEYS, "platforms.linkedin")
    text = _require_text(config.get("text"), "platforms.linkedin.text", minimum=120, maximum=3000)
    validate_text_urls(text, "platforms.linkedin.text")
    validate_placeholders(text, "platforms.linkedin.text", youtube_enabled=youtube_enabled)
    if len(HASHTAG_RE.findall(text)) > 3:
        raise ManifestError("platforms.linkedin.text may contain at most 3 hashtags")
    if MENTION_RE.search(text) or "urn:li:" in text.casefold():
        raise ManifestError("automated LinkedIn mentions are not supported")
    return text, {"text_length": len(text), "hashtag_count": len(HASHTAG_RE.findall(text))}


def _validate_x(config: Mapping[str, Any], *, youtube_enabled: bool) -> tuple[str, dict[str, Any]]:
    _reject_unknown_keys(config, X_KEYS, "platforms.x")
    text = _require_text(config.get("text"), "platforms.x.text", minimum=40, maximum=280)
    validate_text_urls(text, "platforms.x.text")
    validate_placeholders(text, "platforms.x.text", youtube_enabled=youtube_enabled)
    if len(HASHTAG_RE.findall(text)) > 2:
        raise ManifestError("platforms.x.text may contain at most 2 hashtags")
    if MENTION_RE.search(text):
        raise ManifestError("automated X mentions and replies are not supported")
    cashtags = re.findall(r"(?<!\w)\$[A-Za-z]{1,8}\b", text)
    if len(cashtags) > 1:
        raise ManifestError("platforms.x.text may contain at most 1 cashtag")
    return text, {"text_length": len(text), "hashtag_count": len(HASHTAG_RE.findall(text))}


def load_manifest(
    path: Path,
    *,
    asset_root: Path | None = None,
    require_media: bool = False,
) -> ManifestPlan:
    try:
        raw = path.read_bytes()
        manifest = json.loads(raw.decode("utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ManifestError("manifest must be a readable UTF-8 JSON file") from exc
    manifest = _require_mapping(manifest, "manifest")
    _reject_unknown_keys(manifest, TOP_LEVEL_KEYS, "manifest")
    if manifest.get("schema_version") != SCHEMA_VERSION:
        raise ManifestError(f"manifest.schema_version must be {SCHEMA_VERSION}")
    content_id = manifest.get("content_id")
    if not isinstance(content_id, str) or not CONTENT_ID_RE.fullmatch(content_id):
        raise ManifestError("manifest.content_id must be 8-80 lowercase letters, digits, dots, dashes, or underscores")
    approved = _require_bool(manifest.get("approved"), "manifest.approved")
    not_before_value = manifest.get("not_before")
    not_before = (
        parse_datetime(not_before_value, field="manifest.not_before")
        if not_before_value is not None
        else None
    )
    source_url = manifest.get("source_url")
    if source_url is not None:
        if not isinstance(source_url, str):
            raise ManifestError("manifest.source_url must be an HTTPS URL")
        validate_https_url(source_url, "manifest.source_url")
    source = _require_mapping(manifest.get("source", {}), "manifest.source")
    _reject_unknown_keys(source, SOURCE_KEYS, "manifest.source")
    run_id = source.get("run_id")
    artifact_name = source.get("artifact_name")
    if bool(run_id) != bool(artifact_name):
        raise ManifestError("manifest.source.run_id and artifact_name must be set together")
    if run_id is not None and (not isinstance(run_id, str) or not run_id.isdigit()):
        raise ManifestError("manifest.source.run_id must contain digits")
    if artifact_name is not None and (
        not isinstance(artifact_name, str)
        or not artifact_name.strip()
        or any(char in artifact_name for char in "\r\n/")
    ):
        raise ManifestError("manifest.source.artifact_name is invalid")

    platform_configs = _require_mapping(manifest.get("platforms"), "manifest.platforms")
    _reject_unknown_keys(platform_configs, set(PLATFORMS), "manifest.platforms")
    enabled: list[str] = []
    for platform in PLATFORMS:
        if platform not in platform_configs:
            continue
        config = _require_mapping(platform_configs[platform], f"platforms.{platform}")
        is_enabled = _require_bool(config.get("enabled"), f"platforms.{platform}.enabled")
        if is_enabled:
            enabled.append(platform)
    if not enabled:
        raise ManifestError("manifest.platforms must enable at least one platform")
    if "youtube" in enabled and not run_id:
        raise ManifestError("YouTube publishing requires an exact source run and artifact")

    root = asset_root or path.parent
    fingerprints: dict[str, str] = {}
    simhashes: dict[str, str] = {}
    platform_summaries: dict[str, dict[str, Any]] = {}
    youtube_enabled = "youtube" in enabled
    for platform in enabled:
        config = platform_configs[platform]
        if platform == "youtube":
            fingerprint_text, summary = _validate_youtube(
                config,
                asset_root=root,
                require_media=require_media,
            )
        elif platform == "linkedin":
            fingerprint_text, summary = _validate_linkedin(config, youtube_enabled=youtube_enabled)
        else:
            fingerprint_text, summary = _validate_x(config, youtube_enabled=youtube_enabled)
        fingerprints[platform] = content_fingerprint(fingerprint_text)
        simhashes[platform] = simhash64(fingerprint_text)
        platform_summaries[platform] = summary

    if "linkedin" in enabled and "x" in enabled:
        linkedin_text = normalize_text(platform_configs["linkedin"]["text"])
        x_text = normalize_text(platform_configs["x"]["text"])
        if linkedin_text == x_text:
            raise ManifestError("LinkedIn and X must use platform-specific copy")

    # The digest is over the parsed, canonical form rather than whitespace in
    # the JSON file, so formatting-only commits do not create a new identity.
    digest = hashlib.sha256(canonical_manifest_bytes(manifest)).hexdigest()
    return ManifestPlan(
        path=path,
        manifest=manifest,
        digest=digest,
        content_id=content_id,
        approved=approved,
        not_before=not_before,
        platforms=tuple(enabled),
        fingerprints=fingerprints,
        simhashes=simhashes,
    )


def sanitized_preview(plan: ManifestPlan) -> dict[str, Any]:
    configs = plan.manifest["platforms"]
    platforms: list[dict[str, Any]] = []
    for platform in plan.platforms:
        config = configs[platform]
        if platform == "youtube":
            fields = {
                "title_length": len(config["title"].strip()),
                "description_length": len(config["description"].strip()),
                "media_sha256": config["media_sha256"],
                "privacy_status": config["privacy_status"],
                "scheduled": bool(config.get("publish_at")),
                "contains_synthetic_media": config["contains_synthetic_media"],
                "notify_subscribers": config["notify_subscribers"],
            }
        else:
            fields = {
                "text_length": len(config["text"].strip()),
                "hashtag_count": len(HASHTAG_RE.findall(config["text"])),
            }
        platforms.append(
            {
                "platform": platform,
                "fingerprint": plan.fingerprints[platform],
                "simhash": plan.simhashes[platform],
                **fields,
            }
        )
    return {
        "schema_version": SCHEMA_VERSION,
        "content_id": plan.content_id,
        "manifest_sha256": plan.digest,
        "approved": plan.approved,
        "not_before": iso_utc(plan.not_before) if plan.not_before else "",
        "platforms": platforms,
        "source_artifact_configured": bool(plan.manifest.get("source")),
    }


def resolve_template(text: str, *, source_url: str, youtube_url: str) -> str:
    replacements = {
        "SOURCE_URL": source_url,
        "YOUTUBE_URL": youtube_url,
    }

    def replace(match: re.Match[str]) -> str:
        key = match.group(1)
        value = replacements.get(key, "")
        if not value:
            raise ManifestError(f"placeholder {key} has no resolved URL")
        return value

    return PLACEHOLDER_RE.sub(replace, text)


def receipt_file(ledger_dir: Path, content_id: str) -> Path:
    return ledger_dir / f"{content_id}.json"


def pause_file(ledger_dir: Path) -> Path:
    return ledger_dir.parent / "PAUSED.json"


def atomic_write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(handle, "w", encoding="utf-8") as stream:
            json.dump(payload, stream, ensure_ascii=False, indent=2, sort_keys=True)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary_name, path)
    except Exception:
        try:
            os.unlink(temporary_name)
        except OSError:
            pass
        raise


def read_receipts(ledger_dir: Path) -> list[dict[str, Any]]:
    receipts: list[dict[str, Any]] = []
    if not ledger_dir.is_dir():
        return receipts
    for path in sorted(ledger_dir.glob("*.json")):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError):
            raise ManifestError(f"receipt ledger contains an unreadable record: {path.name}")
        if not isinstance(payload, dict) or payload.get("schema_version") != SCHEMA_VERSION:
            raise ManifestError(f"receipt ledger contains an unsupported record: {path.name}")
        receipts.append(payload)
    return receipts


def min_interval_hours(env: Mapping[str, str]) -> int:
    raw = (env.get("SOCIAL_MIN_INTERVAL_HOURS") or str(DEFAULT_MIN_INTERVAL_HOURS)).strip()
    try:
        value = int(raw)
    except ValueError as exc:
        raise ManifestError("SOCIAL_MIN_INTERVAL_HOURS must be an integer") from exc
    if not MIN_INTERVAL_FLOOR_HOURS <= value <= 168:
        raise ManifestError(
            f"SOCIAL_MIN_INTERVAL_HOURS must be between {MIN_INTERVAL_FLOOR_HOURS} and 168"
        )
    return value


def _published_platforms(receipt: Mapping[str, Any]) -> Iterable[str]:
    results = receipt.get("results")
    if not isinstance(results, dict):
        return ()
    return tuple(
        platform
        for platform, result in results.items()
        if isinstance(result, dict) and result.get("state") == "published"
    )


def receipt_is_resolved_without_publish(receipt: Mapping[str, Any]) -> bool:
    if receipt.get("state") != "resolved_not_published":
        return False
    resolution = receipt.get("resolution")
    if not isinstance(resolution, dict):
        return False
    if resolution.get("decision") != "confirmed_no_provider_write":
        return False
    reviewed_by = resolution.get("reviewed_by")
    reviewed_at = resolution.get("reviewed_at")
    if (
        not isinstance(reviewed_by, str)
        or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,78}", reviewed_by)
        or not isinstance(reviewed_at, str)
    ):
        return False
    try:
        parse_datetime(reviewed_at, field="receipt.resolution.reviewed_at")
    except ManifestError:
        return False
    return True


def enforce_ledger_guards(
    plan: ManifestPlan,
    *,
    ledger_dir: Path,
    now: datetime,
    env: Mapping[str, str],
) -> None:
    if pause_file(ledger_dir).exists():
        raise ManifestError(
            "social publishing is paused by the reach monitor; inspect and remove PAUSED.json before publishing"
        )
    interval = timedelta(hours=min_interval_hours(env))
    for receipt in read_receipts(ledger_dir):
        state = receipt.get("state")
        if state == "resolved_not_published":
            if not receipt_is_resolved_without_publish(receipt):
                raise ManifestError("receipt has an invalid reviewed resolution")
            continue
        if state != "published":
            raise ManifestError(
                "publishing is paused by an unresolved receipt; review the provider page before any new publication"
            )
        if receipt.get("content_id") == plan.content_id:
            raise ManifestError("content_id already has a receipt; inspect it before any retry")
        prior_fingerprints = receipt.get("fingerprints", {})
        prior_simhashes = receipt.get("simhashes", {})
        for platform in plan.platforms:
            if isinstance(prior_fingerprints, dict) and prior_fingerprints.get(platform) == plan.fingerprints[platform]:
                raise ManifestError(f"{platform} copy exactly duplicates an earlier publication")
            prior_simhash = prior_simhashes.get(platform) if isinstance(prior_simhashes, dict) else None
            if isinstance(prior_simhash, str) and re.fullmatch(r"[0-9a-f]{16}", prior_simhash):
                if hamming_distance(prior_simhash, plan.simhashes[platform]) <= NEAR_DUPLICATE_HAMMING_DISTANCE:
                    raise ManifestError(f"{platform} copy is too similar to an earlier publication")
        completed = receipt.get("completed_at")
        if not isinstance(completed, str):
            continue
        try:
            completed_at = parse_datetime(completed, field="receipt.completed_at")
        except ManifestError:
            raise ManifestError("receipt ledger contains an invalid completion timestamp")
        for platform in set(plan.platforms).intersection(_published_platforms(receipt)):
            if now - completed_at < interval:
                raise ManifestError(
                    f"{platform} has not reached the configured minimum publication interval"
                )


def reserve(
    plan: ManifestPlan,
    *,
    ledger_dir: Path,
    run_id: str,
    run_url: str,
    now: datetime,
    env: Mapping[str, str],
    code_sha: str = "",
) -> tuple[Path, dict[str, Any]]:
    if not plan.approved:
        raise ManifestError("manifest.approved must be true before publishing")
    if plan.not_before and now < plan.not_before:
        raise ManifestError("manifest.not_before has not been reached")
    if not run_id.isdigit():
        raise ManifestError("run_id must contain digits")
    if code_sha and not re.fullmatch(r"[0-9a-f]{40}", code_sha):
        raise ManifestError("code_sha must be a lowercase 40-character Git SHA")
    validate_https_url(run_url, "run_url")
    enforce_ledger_guards(plan, ledger_dir=ledger_dir, now=now, env=env)
    payload = {
        "schema_version": SCHEMA_VERSION,
        "content_id": plan.content_id,
        "manifest_sha256": plan.digest,
        "state": "reserved",
        "reserved_at": iso_utc(now),
        "completed_at": "",
        "run_id": run_id,
        "run_url": run_url,
        "code_sha": code_sha,
        "platforms": list(plan.platforms),
        "fingerprints": plan.fingerprints,
        "simhashes": plan.simhashes,
        "results": {},
        "failure": None,
    }
    path = receipt_file(ledger_dir, plan.content_id)
    atomic_write_json(path, payload)
    return path, payload


def load_matching_reservation(
    plan: ManifestPlan,
    *,
    ledger_dir: Path,
    run_id: str,
) -> tuple[Path, dict[str, Any]]:
    path = receipt_file(ledger_dir, plan.content_id)
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ManifestError("a committed reservation is required before publishing") from exc
    if (
        not isinstance(payload, dict)
        or payload.get("schema_version") != SCHEMA_VERSION
        or payload.get("state") != "reserved"
        or payload.get("manifest_sha256") != plan.digest
        or payload.get("run_id") != run_id
    ):
        raise ManifestError("reservation does not match this manifest and workflow run")
    return path, payload


def _provider_code(http_status: int) -> str:
    if http_status == 401:
        return "invalid_credential"
    if http_status == 403:
        return "permission_denied"
    if http_status == 429:
        return "quota_or_rate_limit"
    if http_status >= 500:
        return "provider_transient"
    return "provider_rejected"


def _json_request(
    request: urllib.request.Request,
    *,
    platform: str,
    expected_statuses: set[int],
    timeout: float,
    opener: Callable[..., Any] | None = None,
) -> tuple[int, Mapping[str, Any], Mapping[str, str]]:
    open_request = opener or urllib.request.urlopen
    try:
        with open_request(request, timeout=timeout) as response:
            status = int(response.getcode())
            body = response.read(128 * 1024)
            headers = dict(response.headers.items()) if getattr(response, "headers", None) else {}
    except urllib.error.HTTPError as error:
        try:
            error.read(128 * 1024)
        except Exception:
            pass
        code = _provider_code(int(error.code))
        raise ProviderError(platform, code, f"{platform} API returned {code}") from None
    except (urllib.error.URLError, TimeoutError, OSError):
        raise ProviderError(platform, "network_transient", f"{platform} API was temporarily unavailable") from None
    if status not in expected_statuses:
        code = _provider_code(status)
        raise ProviderError(platform, code, f"{platform} API returned {code}")
    try:
        payload = json.loads(body.decode("utf-8")) if body else {}
    except (UnicodeError, json.JSONDecodeError):
        raise ProviderError(platform, "invalid_provider_response", f"{platform} API returned an invalid response") from None
    if not isinstance(payload, dict):
        raise ProviderError(platform, "invalid_provider_response", f"{platform} API returned an invalid response")
    return status, payload, headers


def publish_linkedin(
    text: str,
    *,
    env: Mapping[str, str],
    opener: Callable[..., Any] | None = None,
    timeout: float = 30,
) -> dict[str, Any]:
    token = (env.get("LINKEDIN_ACCESS_TOKEN") or "").strip()
    author = (env.get("LINKEDIN_AUTHOR_URN") or "").strip()
    if not token or not author:
        raise ProviderError("linkedin", "missing_credential", "LinkedIn publishing credentials are not configured")
    if not re.fullmatch(r"urn:li:(person|organization):[A-Za-z0-9_-]+", author):
        raise ProviderError("linkedin", "invalid_configuration", "LinkedIn author configuration is invalid")
    payload = {
        "author": author,
        "commentary": text,
        "visibility": "PUBLIC",
        "distribution": {
            "feedDistribution": "MAIN_FEED",
            "targetEntities": [],
            "thirdPartyDistributionChannels": [],
        },
        "lifecycleState": "PUBLISHED",
        "isReshareDisabledByAuthor": False,
    }
    version = (env.get("LINKEDIN_API_VERSION") or DEFAULT_LINKEDIN_VERSION).strip()
    if not re.fullmatch(r"20\d{4}", version):
        raise ProviderError("linkedin", "invalid_configuration", "LinkedIn API version is invalid")
    url = (env.get("LINKEDIN_POSTS_URL") or DEFAULT_LINKEDIN_POSTS_URL).strip()
    request = urllib.request.Request(
        url,
        data=json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8"),
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Linkedin-Version": version,
            "User-Agent": "portal-social-publisher/1.0",
            "X-Restli-Protocol-Version": "2.0.0",
        },
        method="POST",
    )
    _status, _body, headers = _json_request(
        request,
        platform="linkedin",
        expected_statuses={201},
        timeout=timeout,
        opener=opener,
    )
    post_id = next(
        (value for key, value in headers.items() if key.casefold() == "x-restli-id"),
        "",
    )
    if not isinstance(post_id, str) or not post_id.startswith("urn:li:"):
        raise ProviderError("linkedin", "missing_post_receipt", "LinkedIn did not return a post receipt")
    return {
        "state": "published",
        "post_id": post_id,
        "url": f"https://www.linkedin.com/feed/update/{post_id}/",
        "distribution": "MAIN_FEED",
    }


def percent_encode(value: str) -> str:
    return urllib.parse.quote(value, safe="~-._")


def oauth1_header(
    method: str,
    url: str,
    *,
    consumer_key: str,
    consumer_secret: str,
    access_token: str,
    access_token_secret: str,
    timestamp: int | None = None,
    nonce: str | None = None,
) -> str:
    oauth = {
        "oauth_consumer_key": consumer_key,
        "oauth_nonce": nonce or secrets.token_hex(16),
        "oauth_signature_method": "HMAC-SHA1",
        "oauth_timestamp": str(timestamp if timestamp is not None else int(time.time())),
        "oauth_token": access_token,
        "oauth_version": "1.0",
    }
    parsed = urllib.parse.urlparse(url)
    base_url = urllib.parse.urlunparse((parsed.scheme, parsed.netloc, parsed.path, "", "", ""))
    parameters: list[tuple[str, str]] = list(oauth.items())
    parameters.extend(urllib.parse.parse_qsl(parsed.query, keep_blank_values=True))
    normalized = "&".join(
        f"{percent_encode(str(key))}={percent_encode(str(value))}"
        for key, value in sorted(parameters, key=lambda item: (percent_encode(str(item[0])), percent_encode(str(item[1]))))
    )
    base_string = "&".join(
        (method.upper(), percent_encode(base_url), percent_encode(normalized))
    )
    signing_key = f"{percent_encode(consumer_secret)}&{percent_encode(access_token_secret)}"
    signature = base64.b64encode(
        hmac.new(signing_key.encode("utf-8"), base_string.encode("utf-8"), hashlib.sha1).digest()
    ).decode("ascii")
    oauth["oauth_signature"] = signature
    values = ", ".join(
        f'{percent_encode(key)}="{percent_encode(value)}"' for key, value in sorted(oauth.items())
    )
    return f"OAuth {values}"


def x_credentials(env: Mapping[str, str]) -> tuple[str, str, str, str]:
    values = (
        (env.get("X_API_KEY") or "").strip(),
        (env.get("X_API_SECRET") or "").strip(),
        (env.get("X_ACCESS_TOKEN") or "").strip(),
        (env.get("X_ACCESS_TOKEN_SECRET") or "").strip(),
    )
    if not all(values):
        raise ProviderError("x", "missing_credential", "X publishing credentials are not configured")
    return values


def publish_x(
    text: str,
    *,
    env: Mapping[str, str],
    opener: Callable[..., Any] | None = None,
    timeout: float = 30,
    timestamp: int | None = None,
    nonce: str | None = None,
) -> dict[str, Any]:
    api_key, api_secret, token, token_secret = x_credentials(env)
    url = (env.get("X_POSTS_URL") or DEFAULT_X_POSTS_URL).strip()
    request = urllib.request.Request(
        url,
        data=json.dumps({"text": text}, ensure_ascii=False, separators=(",", ":")).encode("utf-8"),
        headers={
            "Accept": "application/json",
            "Authorization": oauth1_header(
                "POST",
                url,
                consumer_key=api_key,
                consumer_secret=api_secret,
                access_token=token,
                access_token_secret=token_secret,
                timestamp=timestamp,
                nonce=nonce,
            ),
            "Content-Type": "application/json",
            "User-Agent": "portal-social-publisher/1.0",
        },
        method="POST",
    )
    _status, body, _headers = _json_request(
        request,
        platform="x",
        expected_statuses={201},
        timeout=timeout,
        opener=opener,
    )
    data = body.get("data")
    post_id = data.get("id") if isinstance(data, dict) else None
    if not isinstance(post_id, str) or not post_id.isdigit():
        raise ProviderError("x", "missing_post_receipt", "X did not return a post receipt")
    return {
        "state": "published",
        "post_id": post_id,
        "url": f"https://x.com/i/web/status/{post_id}",
    }


def _publish_youtube(
    config: Mapping[str, Any],
    *,
    asset_root: Path,
    env: Mapping[str, str],
    locator_callback: Callable[[Mapping[str, Any]], None] | None = None,
) -> dict[str, Any]:
    try:
        from social_publish_youtube import YouTubePublishError, publish_youtube
    except ImportError as exc:
        raise ProviderError("youtube", "publisher_unavailable", "YouTube publisher is unavailable") from exc
    try:
        result = publish_youtube(
            config,
            asset_root=asset_root,
            env=env,
            receipt_callback=locator_callback,
        )
    except YouTubePublishError as exc:
        code = getattr(exc, "code", "provider_rejected")
        raise ProviderError("youtube", code, f"YouTube API returned {code}") from None
    if not isinstance(result, dict) or result.get("state") != "published":
        raise ProviderError("youtube", "invalid_provider_response", "YouTube did not return a publish receipt")
    allowed = {
        "state",
        "video_id",
        "url",
        "privacy_status",
        "processing_status",
        "publish_at",
    }
    return {key: value for key, value in result.items() if key in allowed}


def publish_reserved(
    plan: ManifestPlan,
    *,
    asset_root: Path,
    ledger_dir: Path,
    run_id: str,
    env: Mapping[str, str],
    now: datetime,
    private_receipt_path: Path | None = None,
    clock: Callable[[], datetime] = utc_now,
) -> tuple[Path, dict[str, Any]]:
    path, receipt = load_matching_reservation(plan, ledger_dir=ledger_dir, run_id=run_id)
    configs = plan.manifest["platforms"]
    source_url = plan.manifest.get("source_url") or ""
    youtube_url = ""
    private_receipt: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "content_id": plan.content_id,
        "manifest_sha256": plan.digest,
        "state": "reserved",
        "completed_at": "",
        "results": {},
        "failure": None,
    }
    if private_receipt_path is not None:
        atomic_write_json(private_receipt_path, private_receipt)

    def persist_early_youtube_locator(locator: Mapping[str, Any]) -> None:
        video_id = locator.get("video_id")
        if not isinstance(video_id, str) or not video_id:
            raise ProviderError(
                "youtube",
                "missing_post_receipt",
                "YouTube did not return a publish receipt",
            )
        locator_time = clock()
        if locator_time.tzinfo is None:
            raise ManifestError("publisher clock must include a timezone")
        result: dict[str, Any] = {
            "state": "published",
            "video_id": video_id,
            "published_at": iso_utc(locator_time),
        }
        publish_at = locator.get("publish_at")
        if isinstance(publish_at, str) and publish_at:
            result["publish_at"] = publish_at
        private_receipt["results"]["youtube"] = result
        private_receipt["state"] = "partial"
        private_receipt["completed_at"] = result["published_at"]
        if private_receipt_path is not None:
            atomic_write_json(private_receipt_path, private_receipt)
    try:
        for platform in plan.platforms:
            if platform == "youtube":
                result = _publish_youtube(
                    configs[platform],
                    asset_root=asset_root,
                    env=env,
                    locator_callback=persist_early_youtube_locator,
                )
                youtube_url = str(result.get("url") or "")
            elif platform == "linkedin":
                text = resolve_template(
                    configs[platform]["text"],
                    source_url=source_url,
                    youtube_url=youtube_url,
                )
                result = publish_linkedin(text, env=env)
            else:
                text = resolve_template(
                    configs[platform]["text"],
                    source_url=source_url,
                    youtube_url=youtube_url,
                )
                result = publish_x(text, env=env)
            provider_completed_at = clock()
            if provider_completed_at.tzinfo is None:
                raise ManifestError("publisher clock must include a timezone")
            published_at = iso_utc(provider_completed_at)
            id_field = "video_id" if platform == "youtube" else "post_id"
            provider_id = result.get(id_field)
            if not isinstance(provider_id, str) or not provider_id:
                raise ProviderError(
                    platform,
                    "missing_post_receipt",
                    f"{platform} did not return a publish receipt",
                )
            private_result = {
                "state": "published",
                id_field: provider_id,
                "published_at": published_at,
            }
            public_result: dict[str, Any] = {
                "state": "published",
                "published_at": published_at,
            }
            if platform == "youtube":
                for key in ("privacy_status", "processing_status", "publish_at"):
                    if key in result:
                        public_result[key] = result[key]
                if "publish_at" in result:
                    private_result["publish_at"] = result["publish_at"]
            elif platform == "linkedin" and "distribution" in result:
                public_result["distribution"] = result["distribution"]

            # Provider IDs are required for later read-only reach checks, but
            # they must not enter this public repository, summaries, artifacts,
            # or email. The workflow encrypts this private locator before its
            # final durable commit.
            private_receipt["results"][platform] = private_result
            private_receipt["state"] = "partial"
            private_receipt["completed_at"] = published_at
            if private_receipt_path is not None:
                atomic_write_json(private_receipt_path, private_receipt)
            receipt["results"][platform] = public_result
            # Persist after each successful provider call.  The workflow commits
            # only the final file, but a later always() artifact still captures
            # partial progress if a subsequent platform fails.
            atomic_write_json(path, receipt)
    except (ProviderError, ManifestError) as exc:
        platform = getattr(exc, "platform", "control")
        code = getattr(exc, "code", "manifest_rejected")
        receipt["state"] = "partial" if receipt["results"] else "failed"
        failed_at = clock()
        if failed_at.tzinfo is None:
            failed_at = now
        receipt["completed_at"] = iso_utc(failed_at)
        receipt["failure"] = {"platform": platform, "code": code}
        private_receipt["state"] = "partial" if private_receipt["results"] else receipt["state"]
        private_receipt["completed_at"] = receipt["completed_at"]
        private_receipt["failure"] = receipt["failure"]
        if private_receipt_path is not None:
            atomic_write_json(private_receipt_path, private_receipt)
        atomic_write_json(path, receipt)
        raise
    completed_at = clock()
    if completed_at.tzinfo is None:
        raise ManifestError("publisher clock must include a timezone")
    receipt["state"] = "published"
    receipt["completed_at"] = iso_utc(completed_at)
    receipt["failure"] = None
    private_receipt["state"] = "published"
    private_receipt["completed_at"] = receipt["completed_at"]
    private_receipt["failure"] = None
    if private_receipt_path is not None:
        atomic_write_json(private_receipt_path, private_receipt)
    atomic_write_json(path, receipt)
    return path, receipt


def select_manifest(
    outbox_dir: Path,
    *,
    ledger_dir: Path,
    now: datetime,
) -> Path | None:
    if not outbox_dir.is_dir():
        return None
    if pause_file(ledger_dir).exists():
        raise ManifestError("automatic queue is paused by social_publish/PAUSED.json")
    unresolved = [
        receipt.get("content_id", "unknown")
        for receipt in read_receipts(ledger_dir)
        if receipt.get("state") != "published"
        and not receipt_is_resolved_without_publish(receipt)
    ]
    if unresolved:
        raise ManifestError(
            "automatic queue is paused by an unresolved publishing receipt"
        )
    candidates: list[tuple[datetime, str, Path]] = []
    for path in sorted(outbox_dir.glob("*.json")):
        try:
            plan = load_manifest(path, require_media=False)
        except ManifestError as exc:
            raise ManifestError(f"outbox manifest {path.name} is invalid: {exc}") from exc
        if not plan.approved or receipt_file(ledger_dir, plan.content_id).exists():
            continue
        due = plan.not_before or datetime(1970, 1, 1, tzinfo=timezone.utc)
        if due <= now:
            candidates.append((due, plan.content_id, path))
    if not candidates:
        return None
    return min(candidates)[2]


def write_json(path: Path | None, payload: Mapping[str, Any]) -> None:
    rendered = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


def append_github_output(path: Path | None, values: Mapping[str, Any]) -> None:
    if not path:
        return
    with path.open("a", encoding="utf-8") as stream:
        for key, value in values.items():
            normalized = str(value).replace("\r", "").replace("\n", " ")
            stream.write(f"{key}={normalized}\n")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    def common(subparser: argparse.ArgumentParser, *, needs_manifest: bool = True) -> None:
        if needs_manifest:
            subparser.add_argument("--manifest", type=Path, required=True)
        subparser.add_argument("--asset-root", type=Path, default=Path("."))
        subparser.add_argument("--json-output", type=Path)
        subparser.add_argument("--github-output", type=Path)

    validate_parser = subparsers.add_parser("validate")
    common(validate_parser)
    validate_parser.add_argument("--require-media", action="store_true")

    inspect_parser = subparsers.add_parser("inspect")
    common(inspect_parser)

    select_parser = subparsers.add_parser("select")
    common(select_parser, needs_manifest=False)
    select_parser.add_argument("--outbox-dir", type=Path, required=True)
    select_parser.add_argument("--ledger-dir", type=Path, required=True)

    reserve_parser = subparsers.add_parser("reserve")
    common(reserve_parser)
    reserve_parser.add_argument("--ledger-dir", type=Path, required=True)
    reserve_parser.add_argument("--run-id", required=True)
    reserve_parser.add_argument("--run-url", required=True)
    reserve_parser.add_argument("--code-sha", required=True)

    publish_parser = subparsers.add_parser("publish")
    common(publish_parser)
    publish_parser.add_argument("--ledger-dir", type=Path, required=True)
    publish_parser.add_argument("--run-id", required=True)
    publish_parser.add_argument("--private-receipt-output", type=Path, required=True)

    return parser.parse_args(argv)


def run(argv: list[str] | None = None, *, env: Mapping[str, str] | None = None) -> int:
    args = parse_args(argv)
    environment = env or os.environ
    now = utc_now()
    if args.command == "select":
        selected = select_manifest(args.outbox_dir, ledger_dir=args.ledger_dir, now=now)
        payload = {"selected": bool(selected), "manifest_path": selected.as_posix() if selected else ""}
        write_json(args.json_output, payload)
        append_github_output(
            args.github_output,
            {"selected": str(bool(selected)).lower(), "manifest_path": payload["manifest_path"]},
        )
        return 0

    plan = load_manifest(
        args.manifest,
        asset_root=args.asset_root,
        require_media=bool(getattr(args, "require_media", False) or args.command == "publish"),
    )
    if args.command in {"validate", "inspect"}:
        preview = sanitized_preview(plan)
        source = plan.manifest.get("source") or {}
        preview["source_run_id"] = source.get("run_id", "")
        preview["source_artifact_name"] = source.get("artifact_name", "")
        write_json(args.json_output, preview)
        append_github_output(
            args.github_output,
            {
                "content_id": plan.content_id,
                "manifest_sha256": plan.digest,
                "platforms": ",".join(plan.platforms),
                "approved": str(plan.approved).lower(),
                "source_run_id": source.get("run_id", ""),
                "source_artifact_name": source.get("artifact_name", ""),
            },
        )
        return 0
    if args.command == "reserve":
        path, payload = reserve(
            plan,
            ledger_dir=args.ledger_dir,
            run_id=args.run_id,
            run_url=args.run_url,
            now=now,
            env=environment,
            code_sha=args.code_sha,
        )
    else:
        path, payload = publish_reserved(
            plan,
            asset_root=args.asset_root,
            ledger_dir=args.ledger_dir,
            run_id=args.run_id,
            env=environment,
            now=now,
            private_receipt_path=args.private_receipt_output,
        )
    write_json(args.json_output, payload)
    append_github_output(
        args.github_output,
        {
            "content_id": plan.content_id,
            "manifest_sha256": plan.digest,
            "receipt_file": path.as_posix(),
            "receipt_state": payload["state"],
        },
    )
    return 0


def main() -> int:
    try:
        return run()
    except (ManifestError, ProviderError) as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
