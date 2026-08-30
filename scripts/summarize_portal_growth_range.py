#!/usr/bin/env python3
"""Build a privacy-preserving portal growth review from private R2 analytics.

The report is intentionally aggregate-only. Raw visitor/session identifiers, IP
hashes, email addresses, full referrer URLs, user agents, and search text never
leave the process. Product metrics exclude known bots and administrative events.
"""

from __future__ import annotations

import argparse
import json
import os
import re
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlsplit


PRIMARY_PREFIX = "_analytics/events"
BACKUP_PREFIX = "_analytics_backup/events"
BJT = timezone(timedelta(hours=8))
BOT_HINTS = {"verified_bot", "likely_bot", "user_agent_bot"}
BOT_RE = re.compile(
    r"(?:bot|spider|crawler|headless|lighthouse|python|curl|wget|scrapy|httpclient|preview|monitor)",
    re.IGNORECASE,
)
ADMIN_EVENT_TYPES = {
    "admin_hot_report_upload",
    "admin_text_only_pdf_upload",
    "admin_user_update",
    "daily_file_download",
    "delivery_link_generate",
}
ENGAGEMENT_EVENT_TYPES = {
    "search",
    "report_open",
    "report_text_view",
    "download_attempt",
    "download_success",
    "report_request",
    "report_chat_interaction",
    "newsfeed_interaction",
    "course_material_request",
}
AI_HOST_RE = re.compile(r"(?:^|\.)(?:chatgpt|perplexity|claude|gemini|copilot)\.", re.IGNORECASE)
SEARCH_HOST_RE = re.compile(
    r"(?:^|\.)(?:google|bing|baidu|yandex|yahoo|duckduckgo|naver|seznam|sogou|so|sm|brave|mojeek|qwant)\.",
    re.IGNORECASE,
)
SOCIAL_HOST_RE = re.compile(
    r"(?:^|\.)(?:weixin|wechat|linkedin|facebook|instagram|reddit|twitter|x|zhihu|xiaohongshu|t)\.",
    re.IGNORECASE,
)
EXTERNAL_CHANNELS = {"organic_search", "ai_referral", "referral", "social", "email", "campaign"}


def clean_text(value: Any, limit: int = 240) -> str:
    return re.sub(r"[\x00-\x1f\x7f]+", "", str(value or "")).strip()[:limit]


def parse_date(value: Any) -> date | None:
    text = clean_text(value, 40)
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", text):
        return None
    try:
        return date.fromisoformat(text)
    except ValueError:
        return None


def parse_instant(value: Any) -> datetime | None:
    text = clean_text(value, 64)
    if not text:
        return None
    try:
        parsed = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed


def bjt_date(value: Any, fallback: Any = "") -> date | None:
    parsed = parse_instant(value)
    if parsed:
        return parsed.astimezone(BJT).date()
    return parse_date(fallback)


def date_range(start: date, end: date) -> list[date]:
    if end < start:
        raise ValueError("end date must not precede start date")
    return [start + timedelta(days=offset) for offset in range((end - start).days + 1)]


def normalize_path(value: Any) -> str:
    text = clean_text(value, 1000)
    if not text:
        return "/"
    try:
        parsed = urlsplit(text)
        path = parsed.path or "/"
    except ValueError:
        path = text.split("?", 1)[0].split("#", 1)[0] or "/"
    if not path.startswith("/"):
        path = f"/{path}"
    return re.sub(r"/{2,}", "/", path)[:300]


def normalize_host(value: Any) -> str:
    text = clean_text(value, 500).lower().rstrip(".")
    if not text or text in {"direct", "(direct)", "invalid"}:
        return ""
    try:
        host = (urlsplit(text).hostname or "").lower().rstrip(".")
    except ValueError:
        host = ""
    if not host and re.fullmatch(r"[a-z0-9.-]+", text):
        host = text
    return host[4:] if host.startswith("www.") else host


def is_bot_event(event: dict[str, Any]) -> bool:
    hint = clean_text(event.get("bot_hint"), 40).lower()
    device = clean_text(event.get("device_type"), 40).lower()
    return bool(
        event.get("verified_bot")
        or hint in BOT_HINTS
        or device == "bot"
        or BOT_RE.search(clean_text(event.get("user_agent"), 1000))
    )


def visitor_key(event: dict[str, Any]) -> str:
    visitor = clean_text(event.get("visitor_id"), 160)
    if visitor:
        return f"visitor:{visitor}"
    ip_hash = clean_text(event.get("ip_hash"), 160)
    return f"ip:{ip_hash}" if ip_hash else ""


def event_date(event: dict[str, Any]) -> date | None:
    return bjt_date(event.get("ts"), event.get("date"))


def event_fingerprint(event: dict[str, Any]) -> str:
    event_id = clean_text(event.get("id"), 200)
    if event_id:
        return f"id:{event_id}"
    fields = (
        event.get("ts"),
        event.get("type"),
        event.get("session_id"),
        event.get("visitor_id"),
        event.get("path"),
        event.get("report_id"),
        event.get("query"),
        event.get("institution"),
        event.get("placement"),
        event.get("target"),
        event.get("action"),
        event.get("status"),
        event.get("outcome"),
    )
    return "fallback:" + "\u001f".join(clean_text(value, 240) for value in fields)


def deduplicate_events(events: Iterable[dict[str, Any]]) -> tuple[list[dict[str, Any]], int]:
    unique: dict[str, dict[str, Any]] = {}
    duplicates = 0
    for event in events:
        if not isinstance(event, dict):
            continue
        key = event_fingerprint(event)
        if key in unique:
            duplicates += 1
            continue
        unique[key] = event
    rows = list(unique.values())
    rows.sort(key=lambda item: clean_text(item.get("ts"), 64))
    return rows, duplicates


def page_family(path: str) -> str:
    if path in {"/", "/index.html"}:
        return "home"
    if path in {"/reports", "/reports/"}:
        return "report_index"
    if path.startswith("/reports/institutions/"):
        return "institution_hub"
    if re.fullmatch(r"/reports/[a-z0-9_-]+\.html", path, re.IGNORECASE):
        return "public_report"
    if path == "/report.html":
        return "dynamic_report"
    if path in {"/blog", "/blog/"}:
        return "blog_index"
    if path.startswith("/blog/"):
        return "blog_article"
    if path in {"/charts", "/charts.html"}:
        return "charts"
    if path in {"/courses", "/courses.html"}:
        return "courses"
    if path.startswith("/newsfeed"):
        return "newsfeed"
    return "other"


def channel_for_session(session: "Session", site_hosts: set[str]) -> str:
    source = clean_text(session.utm_source, 120).lower()
    medium = clean_text(session.utm_medium, 120).lower()
    host = normalize_host(session.referrer_host)
    if medium in {"email", "newsletter"}:
        return "email"
    if source:
        if re.search(r"(?:chatgpt|perplexity|claude|gemini|copilot)", source):
            return "ai_referral"
        if re.search(r"(?:google|bing|baidu|yandex|duckduckgo|naver|sogou|brave)", source):
            return "organic_search"
        if re.search(r"(?:wechat|weixin|linkedin|facebook|reddit|twitter|xiaohongshu|zhihu)", source):
            return "social"
        return "campaign"
    if not host or host in site_hosts:
        return "direct"
    if AI_HOST_RE.search(host):
        return "ai_referral"
    if SEARCH_HOST_RE.search(host):
        return "organic_search"
    if SOCIAL_HOST_RE.search(host):
        return "social"
    return "referral"


def safe_rate(numerator: int | float, denominator: int | float) -> float | None:
    if not denominator:
        return None
    return round(float(numerator) / float(denominator), 4)


def percent_change(before: int | float, after: int | float) -> float | None:
    if not before:
        return None
    return round((float(after) - float(before)) / float(before), 4)


@dataclass
class Session:
    key: str
    visitor: str
    date: date
    landing_path: str
    referrer_host: str = ""
    utm_source: str = ""
    utm_medium: str = ""
    events: list[dict[str, Any]] = field(default_factory=list)
    landing_institutions: set[str] = field(default_factory=set)
    landing_report_ids: set[str] = field(default_factory=set)

    def event_types(self) -> Counter[str]:
        return Counter(clean_text(event.get("type"), 80).lower() for event in self.events)

    def is_engaged(self) -> bool:
        types = self.event_types()
        return types.get("page_view", 0) >= 2 or any(types.get(name, 0) for name in ENGAGEMENT_EVENT_TYPES)

    def has(self, event_type: str) -> bool:
        return any(clean_text(event.get("type"), 80).lower() == event_type for event in self.events)

    def successful_registration(self) -> bool:
        return any(
            clean_text(event.get("type"), 80).lower() == "account_auth"
            and clean_text(event.get("action"), 80).lower() == "register"
            and clean_text(event.get("status"), 80).lower() in {"success", "ok", "completed"}
            for event in self.events
        )


def session_key(event: dict[str, Any], fallback_index: int) -> str:
    session = clean_text(event.get("session_id"), 160)
    if session:
        return f"session:{session}"
    identity = visitor_key(event)
    day = event_date(event)
    landing = normalize_path(event.get("landing_path") or event.get("path"))
    started = parse_instant(event.get("session_started_at"))
    if identity and started:
        return f"fallback:{identity}:{started.isoformat()}"
    if identity and day:
        return f"fallback:{identity}:{day.isoformat()}:{landing}"
    return f"anonymous:{fallback_index}:{event_fingerprint(event)}"


def is_product_event(event: dict[str, Any]) -> bool:
    event_type = clean_text(event.get("type"), 80).lower()
    return bool(
        not is_bot_event(event)
        and event_type not in ADMIN_EVENT_TYPES
        and not event_type.startswith("admin_")
    )


def has_session_identity(event: dict[str, Any]) -> bool:
    return bool(clean_text(event.get("session_id"), 160) or visitor_key(event))


def build_sessions(
    events: Iterable[dict[str, Any]],
    start: date,
    end: date,
) -> tuple[dict[str, Session], dict[str, Any]]:
    sessions: dict[str, Session] = {}
    bot_events = 0
    admin_events = 0
    missing_identity_events = 0
    for index, event in enumerate(events):
        day = event_date(event)
        if not day or not start <= day <= end:
            continue
        if is_bot_event(event):
            bot_events += 1
            continue
        event_type = clean_text(event.get("type"), 80).lower()
        if event_type in ADMIN_EVENT_TYPES or event_type.startswith("admin_"):
            admin_events += 1
            continue
        identity = visitor_key(event)
        if not has_session_identity(event):
            missing_identity_events += 1
            continue
        key = session_key(event, index)
        started = bjt_date(event.get("session_started_at"), day.isoformat()) or day
        if not start <= started <= end:
            continue
        landing = normalize_path(event.get("landing_path") or event.get("path"))
        session = sessions.get(key)
        if session is None:
            session = Session(
                key=key,
                visitor=identity,
                date=started,
                landing_path=landing,
                referrer_host=clean_text(event.get("referrer_host"), 200)
                or normalize_host(event.get("referrer")),
                utm_source=clean_text(event.get("utm_source"), 160),
                utm_medium=clean_text(event.get("utm_medium"), 160),
            )
            sessions[key] = session
        session.events.append(event)
        if event_type == "page_view" and normalize_path(event.get("path")) == session.landing_path:
            institution = clean_text(event.get("institution"), 160).lower()
            if institution:
                session.landing_institutions.add(institution)
            report_id = clean_text(event.get("report_id"), 160).lower()
            if report_id:
                session.landing_report_ids.add(report_id)
    return sessions, {
        "known_bot_events_excluded": bot_events,
        "administrative_events_excluded": admin_events,
        "non_bot_events_without_session_identity_excluded": missing_identity_events,
    }


def session_metrics(sessions: Iterable[Session], site_hosts: set[str]) -> dict[str, int]:
    rows = list(sessions)
    visitors = {session.visitor for session in rows if session.visitor}
    return {
        "visitors": len(visitors),
        "sessions": len(rows),
        "engaged_sessions": sum(session.is_engaged() for session in rows),
        "organic_search_sessions": sum(channel_for_session(session, site_hosts) == "organic_search" for session in rows),
        "ai_referral_sessions": sum(channel_for_session(session, site_hosts) == "ai_referral" for session in rows),
        "report_open_sessions": sum(session.has("report_open") for session in rows),
        "download_attempt_sessions": sum(session.has("download_attempt") for session in rows),
        "download_success_sessions": sum(session.has("download_success") for session in rows),
        "report_request_sessions": sum(session.has("report_request") for session in rows),
        "registration_sessions": sum(session.successful_registration() for session in rows),
    }


def public_channel_rows(sessions: Iterable[Session], site_hosts: set[str]) -> list[dict[str, Any]]:
    grouped: dict[str, list[Session]] = defaultdict(list)
    for session in sessions:
        grouped[channel_for_session(session, site_hosts)].append(session)
    result = []
    total = sum(len(rows) for rows in grouped.values())
    for channel, rows in sorted(grouped.items(), key=lambda item: (-len(item[1]), item[0])):
        metrics = session_metrics(rows, site_hosts)
        result.append({
            "channel": channel,
            **metrics,
            "session_share": safe_rate(metrics["sessions"], total),
            "engagement_rate": safe_rate(metrics["engaged_sessions"], metrics["sessions"]),
            "download_success_rate": safe_rate(metrics["download_success_sessions"], metrics["sessions"]),
        })
    return result


def public_landing_rows(
    sessions: Iterable[Session],
    site_hosts: set[str],
    min_count: int,
    limit: int = 30,
) -> list[dict[str, Any]]:
    grouped: dict[str, list[Session]] = defaultdict(list)
    for session in sessions:
        grouped[session.landing_path].append(session)
    rows = []
    for path, path_sessions in grouped.items():
        if len(path_sessions) < min_count:
            continue
        channels = Counter(channel_for_session(session, site_hosts) for session in path_sessions)
        metrics = session_metrics(path_sessions, site_hosts)
        rows.append({
            "path": path,
            "family": page_family(path),
            **metrics,
            "channels": [
                {"channel": channel, "sessions": count}
                for channel, count in channels.most_common(6)
            ],
        })
    rows.sort(key=lambda row: (-row["sessions"], row["path"]))
    return rows[:limit]


def search_intent_count(events: Iterable[dict[str, Any]]) -> int:
    intents: set[str] = set()
    for event in events:
        if clean_text(event.get("type"), 80).lower() != "search":
            continue
        if is_bot_event(event):
            continue
        session = clean_text(event.get("session_id"), 160) or visitor_key(event)
        query = re.sub(r"\s+", " ", clean_text(event.get("query"), 240).lower())
        instant = parse_instant(event.get("ts"))
        bucket = int(instant.timestamp() // 60) if instant else clean_text(event.get("ts"), 16)
        intents.add(f"{session}\u001f{query}\u001f{bucket}")
    return len(intents)


def daily_rows(
    sessions: Iterable[Session],
    events: Iterable[dict[str, Any]],
    start: date,
    end: date,
    site_hosts: set[str],
) -> list[dict[str, Any]]:
    by_day_sessions: dict[date, list[Session]] = defaultdict(list)
    by_day_events: dict[date, list[dict[str, Any]]] = defaultdict(list)
    for session in sessions:
        by_day_sessions[session.date].append(session)
    for event in events:
        day = event_date(event)
        if day and start <= day <= end and is_product_event(event) and has_session_identity(event):
            by_day_events[day].append(event)
    result = []
    for day in date_range(start, end):
        day_sessions = by_day_sessions.get(day, [])
        metrics = session_metrics(day_sessions, site_hosts)
        result.append({
            "date": day.isoformat(),
            **metrics,
            "page_views": sum(
                clean_text(event.get("type"), 80).lower() == "page_view"
                for event in by_day_events.get(day, [])
            ),
            "search_intents": search_intent_count(by_day_events.get(day, [])),
        })
    return result


def retention_rows(sessions: Iterable[Session], start: date, end: date) -> list[dict[str, Any]]:
    active_days: dict[str, set[date]] = defaultdict(set)
    new_visitors: set[str] = set()
    for session in sessions:
        if not session.visitor:
            continue
        active_days[session.visitor].add(session.date)
        if any(event.get("is_returning") is False for event in session.events):
            new_visitors.add(session.visitor)
    rows = []
    for offset in (1, 7):
        eligible = 0
        retained = 0
        for visitor in new_visitors:
            first = min(active_days[visitor])
            if first + timedelta(days=offset) > end:
                continue
            eligible += 1
            if first + timedelta(days=offset) in active_days[visitor]:
                retained += 1
        rows.append({
            "metric": f"d{offset}",
            "eligible_new_visitors": eligible,
            "retained_visitors": retained,
            "retention_rate": safe_rate(retained, eligible),
        })
    return rows


def session_catalog_institutions(
    session: Session,
    catalog_institutions: dict[str, set[str]],
) -> set[str]:
    values = set(session.landing_institutions)
    for report_id in session.landing_report_ids:
        values.update(catalog_institutions.get(report_id, set()))
    return values


def action_matches(
    session: Session,
    action: dict[str, Any],
    catalog_institutions: dict[str, set[str]],
) -> bool:
    prefixes = [normalize_path(value) for value in action.get("landing_path_prefixes", []) if value]
    institutions = {clean_text(value, 160).lower() for value in action.get("institutions", []) if value}
    return bool(
        any(session.landing_path.startswith(prefix) for prefix in prefixes)
        or (institutions and session_catalog_institutions(session, catalog_institutions).intersection(institutions))
    )


def action_window(action: dict[str, Any]) -> dict[str, date] | None:
    deployed = parse_instant(action.get("effective_at"))
    if not deployed:
        return None
    action_day = deployed.astimezone(BJT).date()
    pre_days = max(1, int(action.get("pre_days") or 7))
    post_days = max(1, int(action.get("post_days") or 7))
    washout_days = max(0, int(action.get("washout_days") or 0))
    pre_start = action_day - timedelta(days=pre_days)
    pre_end = action_day - timedelta(days=1)
    washout_start = action_day
    washout_end = action_day + timedelta(days=washout_days)
    post_start = washout_end + timedelta(days=1)
    post_end = post_start + timedelta(days=post_days - 1)
    return {
        "action_day": action_day,
        "pre_start": pre_start,
        "pre_end": pre_end,
        "washout_start": washout_start,
        "washout_end": washout_end,
        "post_start": post_start,
        "post_end": post_end,
    }


def resolve_review_window(
    start_text: str,
    end_text: str,
    actions: Iterable[dict[str, Any]],
    *,
    auto_days: int = 14,
    today: date | None = None,
) -> tuple[date, date]:
    start = parse_date(start_text)
    end = parse_date(end_text)
    if bool(start_text) != bool(end_text):
        raise ValueError("--start-date and --end-date must be provided together")
    if start_text and (not start or not end):
        raise ValueError("dates must use YYYY-MM-DD")
    if start and end:
        if end < start:
            raise ValueError("end date must not precede start date")
        return start, end
    if not 1 <= auto_days <= 62:
        raise ValueError("--auto-days must be between 1 and 62")
    last_complete_day = (today or datetime.now(tz=BJT).date()) - timedelta(days=1)
    start = last_complete_day - timedelta(days=auto_days - 1)
    end = last_complete_day
    for action in actions:
        window = action_window(action)
        if not window:
            continue
        action_start = window["pre_start"]
        action_end = window["post_end"]
        if action_start <= end and action_end >= start:
            start = min(start, action_start)
    if (end - start).days > 62:
        raise ValueError("resolved review range must contain at most 63 days")
    return start, end


def is_external_session(session: Session, site_hosts: set[str]) -> bool:
    return channel_for_session(session, site_hosts) in EXTERNAL_CHANNELS


def date_set(start: date, end: date) -> set[date]:
    return set(date_range(start, end))


def action_impact_rows(
    sessions: Iterable[Session],
    actions: Iterable[dict[str, Any]],
    report_start: date,
    report_end: date,
    site_hosts: set[str],
    catalog_institutions: dict[str, set[str]],
    covered_dates: set[date] | None = None,
) -> list[dict[str, Any]]:
    all_sessions = list(sessions)
    rows = []
    for action in actions:
        deployed = parse_instant(action.get("effective_at"))
        window = action_window(action)
        if not deployed or not window:
            continue
        pre_start = window["pre_start"]
        pre_end = window["pre_end"]
        washout_start = window["washout_start"]
        washout_end = window["washout_end"]
        post_start = window["post_start"]
        post_end = window["post_end"]
        required_dates = date_set(pre_start, pre_end) | date_set(post_start, post_end)
        complete = pre_start >= report_start and post_end <= report_end
        if covered_dates is not None:
            complete = complete and required_dates.issubset(covered_dates)
        pre_sessions = [session for session in all_sessions if pre_start <= session.date <= pre_end]
        post_sessions = [session for session in all_sessions if post_start <= session.date <= post_end]
        pre_metrics = session_metrics(pre_sessions, site_hosts)
        post_metrics = session_metrics(post_sessions, site_hosts)
        pre_external = [session for session in pre_sessions if is_external_session(session, site_hosts)]
        post_external = [session for session in post_sessions if is_external_session(session, site_hosts)]
        pre_target = [
            session for session in pre_external
            if action_matches(session, action, catalog_institutions)
        ]
        post_target = [
            session for session in post_external
            if action_matches(session, action, catalog_institutions)
        ]
        control_families = {
            clean_text(value, 80) for value in action.get("control_page_families", ["public_report"]) if value
        }
        pre_control = [
            session for session in pre_external
            if page_family(session.landing_path) in control_families
            and not action_matches(session, action, catalog_institutions)
        ]
        post_control = [
            session for session in post_external
            if page_family(session.landing_path) in control_families
            and not action_matches(session, action, catalog_institutions)
        ]
        target_total = len(pre_target) + len(post_target)
        pre_share = safe_rate(len(pre_target), len(pre_target) + len(pre_control))
        post_share = safe_rate(len(post_target), len(post_target) + len(post_control))
        target_change = percent_change(len(pre_target), len(post_target))
        control_change = percent_change(len(pre_control), len(post_control))
        relative_did = (
            round(target_change - control_change, 4)
            if target_change is not None and control_change is not None
            else None
        )
        share_point_change = (
            round(post_share - pre_share, 4)
            if pre_share is not None and post_share is not None
            else None
        )
        if not complete:
            signal = "incomplete_window"
        elif target_total < int(action.get("minimum_target_sessions") or 5):
            signal = "insufficient_target_sample"
        elif not pre_control or not post_control:
            signal = "insufficient_control_sample"
        elif share_point_change is not None and share_point_change > 0:
            signal = "positive_directional_signal"
        elif share_point_change is not None and share_point_change < 0:
            signal = "negative_directional_signal"
        else:
            signal = "flat_directional_signal"
        rows.append({
            "id": clean_text(action.get("id"), 100),
            "name": clean_text(action.get("name"), 240),
            "effective_at": deployed.isoformat(),
            "hypothesis": clean_text(action.get("hypothesis"), 500),
            "status": signal,
            "complete_window": complete,
            "pre_window": {"start": pre_start.isoformat(), "end": pre_end.isoformat()},
            "washout_window": {"start": washout_start.isoformat(), "end": washout_end.isoformat()},
            "post_window": {"start": post_start.isoformat(), "end": post_end.isoformat()},
            "pre": {
                **pre_metrics,
                "external_sessions": len(pre_external),
                "target_external_landing_sessions": len(pre_target),
                "control_external_report_landing_sessions": len(pre_control),
                "target_share_of_treatment_and_control": pre_share,
            },
            "post": {
                **post_metrics,
                "external_sessions": len(post_external),
                "target_external_landing_sessions": len(post_target),
                "control_external_report_landing_sessions": len(post_control),
                "target_share_of_treatment_and_control": post_share,
            },
            "change": {
                "sessions": percent_change(pre_metrics["sessions"], post_metrics["sessions"]),
                "organic_search_sessions": percent_change(
                    pre_metrics["organic_search_sessions"], post_metrics["organic_search_sessions"]
                ),
                "ai_referral_sessions": percent_change(
                    pre_metrics["ai_referral_sessions"], post_metrics["ai_referral_sessions"]
                ),
                "target_external_landing_sessions": target_change,
                "control_external_report_landing_sessions": control_change,
                "difference_in_relative_changes": relative_did,
                "target_share_point_change": share_point_change,
            },
            "interpretation": "Observational difference-in-differences signal only; concurrent releases and acquisition mix may confound causality.",
        })
    return rows


def build_growth_review(
    events: Iterable[dict[str, Any]],
    start_date: str,
    end_date: str,
    actions: Iterable[dict[str, Any]] = (),
    *,
    site_host: str = "portal.example.invalid",
    min_count: int = 2,
    expected_dates: Iterable[str] = (),
    covered_dates: Iterable[str] | None = None,
    catalog_institutions: dict[str, set[str]] | None = None,
) -> dict[str, Any]:
    start = parse_date(start_date)
    end = parse_date(end_date)
    if not start or not end:
        raise ValueError("start_date and end_date must use YYYY-MM-DD")
    rows, duplicate_count = deduplicate_events(events)
    sessions, exclusions = build_sessions(rows, start, end)
    session_rows = list(sessions.values())
    normalized_site_host = normalize_host(site_host)
    site_hosts = {normalized_site_host, f"www.{normalized_site_host}"} if normalized_site_host else set()
    totals = session_metrics(session_rows, site_hosts)
    included_events = [
        event
        for event in rows
        if (day := event_date(event)) and start <= day <= end
        and is_product_event(event)
        and has_session_identity(event)
    ]
    totals.update({
        "page_views": sum(clean_text(event.get("type"), 80).lower() == "page_view" for event in included_events),
        "search_intents": search_intent_count(included_events),
    })
    channels = public_channel_rows(session_rows, site_hosts)
    review = {
        "schema": "portal-growth-review-v1",
        "start_date": start.isoformat(),
        "end_date": end.isoformat(),
        "generated_at": datetime.now(tz=BJT).isoformat(timespec="seconds"),
        "totals": totals,
        "funnel": [
            {"step": "landing_sessions", "sessions": totals["sessions"], "rate_from_landing": 1.0},
            {"step": "engaged_sessions", "sessions": totals["engaged_sessions"], "rate_from_landing": safe_rate(totals["engaged_sessions"], totals["sessions"])},
            {"step": "report_open_sessions", "sessions": totals["report_open_sessions"], "rate_from_landing": safe_rate(totals["report_open_sessions"], totals["sessions"])},
            {"step": "download_attempt_sessions", "sessions": totals["download_attempt_sessions"], "rate_from_landing": safe_rate(totals["download_attempt_sessions"], totals["sessions"])},
            {"step": "download_success_sessions", "sessions": totals["download_success_sessions"], "rate_from_landing": safe_rate(totals["download_success_sessions"], totals["sessions"])},
            {"step": "report_request_sessions", "sessions": totals["report_request_sessions"], "rate_from_landing": safe_rate(totals["report_request_sessions"], totals["sessions"])},
            {"step": "registration_sessions", "sessions": totals["registration_sessions"], "rate_from_landing": safe_rate(totals["registration_sessions"], totals["sessions"])},
        ],
        "acquisition_channels": channels,
        "top_landing_pages": public_landing_rows(session_rows, site_hosts, min_count),
        "daily": daily_rows(session_rows, rows, start, end, site_hosts),
        "retention": retention_rows(session_rows, start, end),
        "action_impacts": action_impact_rows(
            session_rows,
            actions,
            start,
            end,
            site_hosts,
            catalog_institutions or {},
            (
                {day for value in covered_dates or [] if (day := parse_date(value))}
                if covered_dates is not None
                else None
            ),
        ),
        "data_quality": {
            "input_events": len(rows) + duplicate_count,
            "deduplicated_events": len(rows),
            "duplicate_events_removed": duplicate_count,
            **exclusions,
            "expected_dates": list(expected_dates),
            "event_date_coverage": sorted({day.isoformat() for event in rows if (day := event_date(event))}),
            "notes": [
                "Known bots and administrative events are excluded from product growth metrics.",
                "Search intents are deduplicated by session, normalized query, and one-minute time bucket.",
                "External search keywords and AI prompts are not available in site analytics.",
                "No purchase or revenue event exists, so this report cannot attribute revenue.",
            ],
        },
        "privacy": {
            "visitor_ids_included": False,
            "session_ids_included": False,
            "ip_hashes_included": False,
            "email_addresses_included": False,
            "search_queries_included": False,
            "full_referrer_urls_included": False,
            "raw_user_agents_included": False,
        },
    }
    return review


def markdown_summary(review: dict[str, Any]) -> str:
    totals = review["totals"]
    lines = [
        f"# KC桌面增长复盘：{review['start_date']} 至 {review['end_date']}",
        "",
        f"- 去除已识别机器人和后台操作后：{totals['visitors']} 位访客，{totals['sessions']} 个会话。",
        f"- 自然搜索会话：{totals['organic_search_sessions']}；AI 来源会话：{totals['ai_referral_sessions']}。",
        f"- 参与会话：{totals['engaged_sessions']}；打开报告：{totals['report_open_sessions']}；下载成功：{totals['download_success_sessions']}；报告申请：{totals['report_request_sessions']}。",
        f"- 已排除机器人事件：{review['data_quality']['known_bot_events_excluded']}；已排除后台事件：{review['data_quality']['administrative_events_excluded']}。",
        "",
        "## 获客渠道",
        "",
        "| 渠道 | 会话 | 参与 | 报告打开 | 下载成功 |",
        "|---|---:|---:|---:|---:|",
    ]
    for row in review.get("acquisition_channels", []):
        lines.append(
            f"| {row['channel']} | {row['sessions']} | {row['engaged_sessions']} | "
            f"{row['report_open_sessions']} | {row['download_success_sessions']} |"
        )
    lines.extend(["", "## 发布动作复盘", ""])
    impacts = review.get("action_impacts", [])
    if not impacts:
        lines.append("本区间没有可评估的发布动作。")
    for impact in impacts:
        pre = impact["pre"]
        post = impact["post"]
        lines.extend([
            f"### {impact['name']}",
            "",
            f"- 状态：{impact['status']}。",
            f"- 前窗 {impact['pre_window']['start']} 至 {impact['pre_window']['end']}："
            f"自然搜索 {pre['organic_search_sessions']}，目标外部落地 {pre['target_external_landing_sessions']}。",
            f"- 洗脱窗 {impact['washout_window']['start']} 至 {impact['washout_window']['end']} 不进入前后比较。",
            f"- 后窗 {impact['post_window']['start']} 至 {impact['post_window']['end']}："
            f"自然搜索 {post['organic_search_sessions']}，目标外部落地 {post['target_external_landing_sessions']}。",
            f"- 目标落地占处理组与对照组的份额变化：{impact['change']['target_share_point_change']}。",
            "- 说明：这是方向性观察，不把同期发布、渠道结构变化误写成单一动作的因果证明。",
            "",
        ])
    lines.extend([
        "## 口径",
        "",
        "报告只包含聚合数据，不包含访客、会话、IP、邮箱、搜索词、完整来源 URL 或原始 UA。",
        "",
    ])
    return "\n".join(lines)


def load_action_ledger(path: Path | None) -> list[dict[str, Any]]:
    if not path:
        return []
    payload = json.loads(path.read_text(encoding="utf-8"))
    actions = payload.get("actions", []) if isinstance(payload, dict) else []
    return [action for action in actions if isinstance(action, dict)]


def load_catalog_institutions(path: Path | None) -> dict[str, set[str]]:
    if not path:
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    items = payload.get("items", []) if isinstance(payload, dict) else payload
    result: dict[str, set[str]] = defaultdict(set)
    for item in items if isinstance(items, list) else []:
        if not isinstance(item, dict):
            continue
        report_id = clean_text(item.get("id"), 160).lower()
        if not report_id:
            continue
        for field_name in ("institution", "bank_code", "bank_name"):
            value = clean_text(item.get(field_name), 160).lower()
            if value:
                result[report_id].add(value)
    return dict(result)


def r2_client() -> Any:
    try:
        import boto3
        from botocore.config import Config
    except ImportError as error:  # pragma: no cover - installed in Actions.
        raise RuntimeError("boto3 is required to read the private analytics archive") from error
    account_id = clean_text(os.environ.get("R2_ACCOUNT_ID"), 200)
    access_key = clean_text(os.environ.get("R2_ACCESS_KEY_ID"), 300)
    secret_key = clean_text(os.environ.get("R2_SECRET_ACCESS_KEY"), 500)
    if not all([account_id, access_key, secret_key]):
        raise RuntimeError("Missing private R2 configuration")
    return boto3.client(
        "s3",
        endpoint_url=f"https://{account_id}.r2.cloudflarestorage.com",
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="auto",
        config=Config(signature_version="s3v4", retries={"max_attempts": 8, "mode": "adaptive"}),
    )


def list_keys(client: Any, bucket: str, prefix: str) -> list[str]:
    keys: list[str] = []
    continuation = ""
    while True:
        kwargs: dict[str, Any] = {"Bucket": bucket, "Prefix": prefix, "MaxKeys": 1000}
        if continuation:
            kwargs["ContinuationToken"] = continuation
        response = client.list_objects_v2(**kwargs)
        keys.extend(str(item["Key"]) for item in response.get("Contents", []) if item.get("Key"))
        if not response.get("IsTruncated"):
            return keys
        continuation = clean_text(response.get("NextContinuationToken"), 4000)
        if not continuation:
            raise RuntimeError("R2 listing was truncated without a continuation token")


def read_event(client: Any, bucket: str, keys: list[str]) -> dict[str, Any] | None:
    for key in keys:
        try:
            response = client.get_object(Bucket=bucket, Key=key)
            payload = json.loads(response["Body"].read().decode("utf-8"))
            if isinstance(payload, dict):
                return payload
        except Exception:  # Try the mirrored copy before omitting a damaged event.
            continue
    return None


def load_r2_range_events(start: date, end: date) -> tuple[list[dict[str, Any]], list[str]]:
    client = r2_client()
    bucket = clean_text(os.environ.get("R2_BUCKET"), 240)
    if not bucket:
        raise RuntimeError("Missing R2_BUCKET")
    candidates: dict[str, list[str]] = {}
    for day in date_range(start, end):
        day_text = day.isoformat()
        for root in (PRIMARY_PREFIX, BACKUP_PREFIX):
            prefix = f"{root}/{day_text}/"
            for key in list_keys(client, bucket, prefix):
                suffix = key[len(prefix):]
                if suffix:
                    candidates.setdefault(f"{day_text}/{suffix}", []).append(key)
    if not candidates:
        raise RuntimeError(f"No analytics events found from {start.isoformat()} through {end.isoformat()}")
    with ThreadPoolExecutor(max_workers=24) as pool:
        rows = list(pool.map(lambda keys: read_event(client, bucket, keys), candidates.values()))
    loaded = [row for row in rows if row is not None]
    if not loaded:
        raise RuntimeError(f"No readable analytics events found from {start.isoformat()} through {end.isoformat()}")
    covered = sorted({
        day.isoformat()
        for row in loaded
        if (day := event_date(row)) and start <= day <= end
    })
    return loaded, covered


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-date", default="")
    parser.add_argument("--end-date", default="")
    parser.add_argument("--auto-days", type=int, default=14)
    parser.add_argument("--actions", type=Path)
    parser.add_argument("--catalog", type=Path)
    parser.add_argument("--site-host", default="portal.example.invalid")
    parser.add_argument("--min-count", type=int, default=2)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--markdown-output", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    actions = load_action_ledger(args.actions)
    try:
        start, end = resolve_review_window(
            args.start_date,
            args.end_date,
            actions,
            auto_days=args.auto_days,
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    if (end - start).days > 62:
        raise SystemExit("date range must contain 1-63 days")
    if not 1 <= args.min_count <= 100:
        raise SystemExit("--min-count must be between 1 and 100")
    events, covered = load_r2_range_events(start, end)
    review = build_growth_review(
        events,
        start.isoformat(),
        end.isoformat(),
        actions,
        site_host=args.site_host,
        min_count=args.min_count,
        expected_dates=[day.isoformat() for day in date_range(start, end)],
        covered_dates=covered,
        catalog_institutions=load_catalog_institutions(args.catalog),
    )
    review["data_quality"]["r2_dates_with_events"] = covered
    review["data_quality"]["r2_dates_without_events"] = [
        day for day in review["data_quality"]["expected_dates"] if day not in set(covered)
    ]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(review, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.markdown_output:
        args.markdown_output.parent.mkdir(parents=True, exist_ok=True)
        args.markdown_output.write_text(markdown_summary(review), encoding="utf-8")
    print("Private aggregate growth review generated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
