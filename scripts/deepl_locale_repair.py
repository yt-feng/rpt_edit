#!/usr/bin/env python3
"""Quota-bounded DeepL repairs; never retranslates the successful locale cache."""
from __future__ import annotations

from collections import Counter
import html
import os
import re
import threading
from typing import Any
import xml.etree.ElementTree as ET

import requests


API_ROOT = "https://api-free.deepl.com/v2"
PLACEHOLDER_RE = re.compile(r"__KC_PH_\d+__")
TARGET_LANGUAGES = {"ko": "KO", "ja": "JA", "ar": "AR"}
QUOTA_RESERVE_CHARACTERS = 1000
DEFAULT_MAX_REQUESTS = 2500


class DeepLRepairError(Exception):
    """A safe, provider-body-free repair failure."""


class DeepLQuotaExhausted(DeepLRepairError):
    """The bounded repair allowance is exhausted."""


def _nonnegative_integer(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


def _protect_source(source: str) -> tuple[str, dict[str, str]]:
    if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f\ud800-\udfff\ufffe\uffff]", source):
        raise DeepLRepairError("DeepL repair source contains invalid XML characters")
    placeholders: dict[str, str] = {}
    pieces = ["<t>"]
    cursor = 0
    for index, match in enumerate(PLACEHOLDER_RE.finditer(source)):
        pieces.append(html.escape(source[cursor:match.start()], quote=False))
        key = str(index)
        placeholders[key] = match.group(0)
        pieces.append(f'<x id="{key}">{match.group(0)}</x>')
        cursor = match.end()
    pieces.append(html.escape(source[cursor:], quote=False))
    pieces.append("</t>")
    return "".join(pieces), placeholders


def _restore_translation(text: str, placeholders: dict[str, str]) -> str:
    # ElementTree silently ignores some declarations/comments. Reject them first.
    if not isinstance(text, str) or re.search(r"<!|<\?", text):
        raise DeepLRepairError("DeepL returned invalid repair XML")
    try:
        root = ET.fromstring(text)
    except (ET.ParseError, ValueError):
        raise DeepLRepairError("DeepL returned invalid repair XML") from None
    if root.tag != "t" or root.attrib:
        raise DeepLRepairError("DeepL changed the repair XML structure")
    parts = [root.text or ""]
    seen: set[str] = set()
    for child in root:
        key = child.attrib.get("id", "")
        if (
            child.tag != "x"
            or set(child.attrib) != {"id"}
            or key not in placeholders
            or key in seen
            or len(child)
            or child.text != placeholders[key]
        ):
            raise DeepLRepairError("DeepL changed a protected repair placeholder")
        seen.add(key)
        parts.extend((placeholders[key], child.tail or ""))
    plain = "".join(parts)
    if seen != set(placeholders) or Counter(PLACEHOLDER_RE.findall(plain)) != Counter(placeholders.values()):
        raise DeepLRepairError("DeepL changed the protected repair placeholders")
    if not plain.strip():
        raise DeepLRepairError("DeepL returned an empty repair")
    return plain


class DeepLRepair:
    """One shared, thread-safe allowance with no hidden retry or key fallback."""

    def __init__(self, max_requests: int | None = None, *, transport: Any = None):
        maximum = DEFAULT_MAX_REQUESTS if max_requests is None else max_requests
        if not _nonnegative_integer(maximum):
            raise ValueError("max_requests must be a nonnegative integer")
        self._max_requests = maximum
        self._transport = requests if transport is None else transport
        self._api_key = os.getenv("DEEPL_API_KEY", "").strip()
        self._lock = threading.RLock()
        self._balance_checked = False
        self._limit: int | None = None
        self._initial_count: int | None = None
        self._balance_requests = 0
        self._provider_requests = 0
        self._billed = 0
        self._reserved = 0
        self._unobserved = 0
        self._stop_reason = ""
        self._stop_exception: type[DeepLRepairError] = DeepLRepairError

    def _stop(self, reason: str, error: type[DeepLRepairError] = DeepLRepairError) -> None:
        if not self._stop_reason:
            self._stop_reason = reason
            self._stop_exception = error

    def _raise_if_stopped(self) -> None:
        if self._stop_reason:
            raise self._stop_exception(self._stop_reason) from None

    def _headers(self) -> dict[str, str]:
        return {"Authorization": "DeepL-Auth-Key " + self._api_key}

    def _ensure_balance(self) -> None:
        # Called with the lock held: concurrent repairs issue only one usage GET.
        if self._balance_checked:
            self._raise_if_stopped()
            return
        self._balance_checked = True
        if not self._api_key:
            self._stop("DeepL repair key is not configured")
            self._raise_if_stopped()
        self._balance_requests += 1
        try:
            response = self._transport.get(
                API_ROOT + "/usage", headers=self._headers(), timeout=30,
                allow_redirects=False,
            )
        except requests.RequestException:
            self._stop("DeepL usage request failed; no automatic retry")
            self._raise_if_stopped()
        if response.status_code != 200:
            self._stop("DeepL usage HTTP " + str(int(response.status_code)))
            self._raise_if_stopped()
        try:
            payload = response.json()
        except (ValueError, requests.RequestException):
            payload = None
        if (
            not isinstance(payload, dict)
            or not _nonnegative_integer(payload.get("character_count"))
            or not _nonnegative_integer(payload.get("character_limit"))
        ):
            self._stop("DeepL usage response has no valid character allowance")
            self._raise_if_stopped()
        self._initial_count = payload["character_count"]
        self._limit = payload["character_limit"]

    def snapshot(self) -> dict[str, Any]:
        """Only allowlisted counters; credentials and provider bodies never leave."""
        with self._lock:
            remaining = None if self._limit is None else max(
                0, self._limit - (self._initial_count or 0) - self._billed - self._reserved
            )
            return {
                "balance_requests": self._balance_requests,
                "provider_requests": self._provider_requests,
                "max_requests": self._max_requests,
                "billed_characters": self._billed,
                "reserved_characters": self._reserved,
                "remaining_character_budget": remaining,
                "quota_reserve_characters": QUOTA_RESERVE_CHARACTERS,
                "unobserved_requests": self._unobserved,
                "stop_reason": self._stop_reason,
            }

    def translate(self, locale: str, source: str) -> str:
        if locale not in TARGET_LANGUAGES or not isinstance(source, str) or not source.strip():
            raise DeepLRepairError("DeepL repair needs a supported locale and nonempty source")
        protected, placeholders = _protect_source(source)
        reservation = max(len(source), len(source.encode("utf-8")))
        with self._lock:
            self._raise_if_stopped()
            if self._provider_requests >= self._max_requests:
                self._stop("DeepL repair request allowance exhausted", DeepLQuotaExhausted)
                self._raise_if_stopped()
            self._ensure_balance()
            available = (self._limit or 0) - (self._initial_count or 0) - self._billed - self._reserved
            if reservation + QUOTA_RESERVE_CHARACTERS > available:
                self._stop("DeepL repair character allowance exhausted", DeepLQuotaExhausted)
                self._raise_if_stopped()
            self._reserved += reservation
            self._provider_requests += 1
        try:
            response = self._transport.post(
                API_ROOT + "/translate", headers=self._headers(),
                json={
                    "text": [protected], "target_lang": TARGET_LANGUAGES[locale],
                    "tag_handling": "xml", "ignore_tags": ["x"],
                    "show_billed_characters": True,
                },
                timeout=30, allow_redirects=False,
            )
        except requests.RequestException:
            with self._lock:
                self._unobserved += 1
                self._stop("DeepL repair request failed; allowance retained without retry")
            raise DeepLRepairError("DeepL repair request failed; allowance retained without retry") from None
        if response.status_code != 200:
            error = DeepLQuotaExhausted if response.status_code == 456 else DeepLRepairError
            message = "DeepL repair HTTP " + str(int(response.status_code)) + "; no automatic retry"
            with self._lock:
                self._unobserved += 1
                self._stop(message, error)
            raise error(message)
        try:
            payload = response.json()
        except (ValueError, requests.RequestException):
            payload = None
        rows = payload.get("translations") if isinstance(payload, dict) else None
        row = rows[0] if isinstance(rows, list) and len(rows) == 1 and isinstance(rows[0], dict) else None
        billed = row.get("billed_characters") if row is not None else None
        with self._lock:
            if _nonnegative_integer(billed) and billed <= reservation:
                self._reserved -= reservation
                self._billed += billed
            else:
                self._unobserved += 1
                self._stop("DeepL billed usage is unverified; retained allowance and stopped new repairs")
        if row is None or not isinstance(row.get("text"), str):
            raise DeepLRepairError("DeepL returned no valid repair result")
        return _restore_translation(row["text"], placeholders)
