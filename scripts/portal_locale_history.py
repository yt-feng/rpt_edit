"""Pure daily release planning for a fixed historical publication window.

Pass only the ledger of the active production release as ``previous``. A draft,
translation cache, or failed CI artifact must never advance the publication day.
New content (on/after launch) is outside this historical quota and is handled by
the caller's normal publication policy.

The ``released`` list advertises only currently present, in-window candidates.
Removed sources are pruned rather than retained as ghost pages; if they return,
they are eligible for a later daily batch. Pruning never opens a same-day batch.
"""
from __future__ import annotations

from collections import deque
from datetime import date
import re
from typing import Any
from urllib.parse import unquote, urlsplit


SCHEMA_VERSION = 1
_DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}\Z")


def _date(value: Any, label: str) -> date:
    if not isinstance(value, str) or not _DATE_RE.fullmatch(value):
        raise ValueError(f"{label} must be an ISO calendar date (YYYY-MM-DD)")
    try:
        return date.fromisoformat(value)
    except ValueError:
        raise ValueError(f"{label} must be a valid calendar date") from None


def _canonical(value: Any) -> str:
    # Origin authorization belongs to the caller. This helper accepts either a
    # root-relative path or an absolute HTTP(S) canonical, never a relative URL.
    if (
        not isinstance(value, str)
        or not value
        or any(character.isspace() or ord(character) < 32 for character in value)
        or "\\" in value
    ):
        raise ValueError("historical canonical must be a nonempty canonical URL or absolute path")
    try:
        parsed = urlsplit(value)
        valid_origin = (
            parsed.scheme in {"http", "https"}
            and bool(parsed.hostname)
            and parsed.username is None
            and parsed.password is None
        )
        if parsed.netloc:
            parsed.port  # Validate malformed/non-numeric ports without using them.
    except ValueError:
        raise ValueError("historical canonical is malformed") from None
    absolute_path = value.startswith("/") and not value.startswith("//") and not parsed.scheme and not parsed.netloc
    if (
        not (absolute_path or valid_origin)
        or parsed.query
        or parsed.fragment
        or any(unquote(segment) in {".", ".."} for segment in parsed.path.split("/"))
    ):
        raise ValueError("historical canonical must be an absolute path or HTTP(S) URL without query, fragment, or traversal")
    return value


def _nonnegative_integer(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


def _canonical_list(value: Any, label: str) -> set[str]:
    if not isinstance(value, list):
        raise ValueError(f"previous {label} must be a canonical list")
    validated = [_canonical(item) for item in value]
    if len(set(validated)) != len(validated):
        raise ValueError(f"previous {label} contains duplicate canonicals")
    return set(validated)


def _kind(canonical: str) -> str:
    path = urlsplit(canonical).path
    if path.startswith("/blog/"):
        return "blog"
    if path.startswith("/reports/"):
        return "report"
    return "other"


def plan_history_release(
    candidates: dict[str, str],
    *,
    history_start_date: str,
    launch_date: str,
    today: str,
    previous: dict | None,
    daily_limit: int = 100,
    paused: bool = False,
) -> dict:
    """Select at most one balanced, latest-first batch for a calendar day.

    The fixed window is ``history_start_date <= publication < launch_date``.
    A same-day rerun preserves its surviving selection; missed days never accrue
    extra allowance. Before launch, a valid plan contains no released pages.
    The returned state must become active in production before it can be used
    as the next ``previous`` ledger. Within each blog/report/other cohort, newest
    publication wins (canonical breaks ties); the three cohorts take turns so
    report metadata cannot crowd all substantive blog pages out of a batch.
    Pausing retains surviving released pages without opening a new release day.
    """
    start = _date(history_start_date, "history_start_date")
    launch = _date(launch_date, "launch_date")
    current = _date(today, "today")
    if start >= launch:
        raise ValueError("history_start_date must precede launch_date")
    if not _nonnegative_integer(daily_limit) or daily_limit == 0:
        raise ValueError("daily_limit must be a positive integer")
    if not isinstance(paused, bool):
        raise ValueError("paused must be a boolean")
    if not isinstance(candidates, dict):
        raise ValueError("candidates must map canonical URLs to publication dates")

    eligible: dict[str, date] = {}
    for canonical, published in candidates.items():
        key = _canonical(canonical)
        publication = _date(published, "candidate publication date")
        if start <= publication < launch:
            eligible[key] = publication

    released: set[str] = set()
    selected: set[str] = set()
    last_release: date | None = None
    if previous is not None:
        if not isinstance(previous, dict):
            raise ValueError("previous must be an active production ledger object")
        if type(previous.get("schema_version")) is not int or previous["schema_version"] != SCHEMA_VERSION:
            raise ValueError("previous historical ledger schema is unsupported")
        for key, expected in (
            ("history_start_date", history_start_date),
            ("launch_date", launch_date),
            ("daily_limit", daily_limit),
        ):
            if type(previous.get(key)) is not type(expected) or previous[key] != expected:
                raise ValueError(f"previous historical ledger configuration differs: {key}")
        for key in ("pending_count", "out_of_scope_count"):
            if not _nonnegative_integer(previous.get(key)):
                raise ValueError(f"previous {key} must be a nonnegative integer")
        previous_released = _canonical_list(previous.get("released"), "released")
        previous_selected = _canonical_list(previous.get("selected_today"), "selected_today")
        if not previous_selected <= previous_released or len(previous_selected) > daily_limit:
            raise ValueError("previous daily selection is inconsistent with its released ledger")
        if "last_release_date" not in previous:
            raise ValueError("previous historical ledger has no last_release_date")
        last_value = previous["last_release_date"]
        if last_value is None:
            if previous_released or previous_selected:
                raise ValueError("previous released pages require a last_release_date")
        else:
            last_release = _date(last_value, "previous last_release_date")
            if last_release < launch:
                raise ValueError("previous historical release predates launch")
            if last_release > current:
                raise ValueError("previous historical release is in the future; clock moved backwards")
        released = previous_released & eligible.keys()
        if last_release == current:
            selected = previous_selected & released

    if not paused and current >= launch and last_release != current:
        cohorts = {kind: deque() for kind in ("blog", "report", "other")}
        for canonical in sorted(
            eligible.keys() - released,
            key=lambda canonical: (-eligible[canonical].toordinal(), canonical),
        ):
            cohorts[_kind(canonical)].append(canonical)
        batch: list[str] = []
        while len(batch) < daily_limit and any(cohorts.values()):
            for cohort in cohorts.values():
                if cohort and len(batch) < daily_limit:
                    batch.append(cohort.popleft())
        selected = set(batch)
        released.update(selected)
        # Record the attempted production day's allocation even for an empty
        # batch, preventing a later rerun from opening another same-day batch.
        last_release = current

    return {
        "schema_version": SCHEMA_VERSION,
        "history_start_date": history_start_date,
        "launch_date": launch_date,
        "last_release_date": last_release.isoformat() if last_release is not None else None,
        "released": sorted(released),
        "selected_today": sorted(selected),
        "pending_count": len(eligible) - len(released),
        "out_of_scope_count": len(candidates) - len(eligible),
        "daily_limit": daily_limit,
        "paused": paused,
        "selected_counts": {
            kind: sum(_kind(canonical) == kind for canonical in selected)
            for kind in ("blog", "report", "other")
        },
    }
