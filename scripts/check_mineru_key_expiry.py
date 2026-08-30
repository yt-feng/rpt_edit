#!/usr/bin/env python3
"""Check the configured MinerU key pool without creating a parsing task.

The monitor deliberately probes a synthetic, nonexistent batch with GET.  MinerU
can therefore authenticate the key and return an application-level "task not
found" response without allocating upload space or starting a billable parse.

Only slot names and normalized status fields are written to logs and artifacts;
raw credentials and response bodies never leave this process.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import math
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path
from typing import Any, Callable, Mapping
from zoneinfo import ZoneInfo


DEFAULT_MINERU_BASE_URL = "https://mineru.net"
PROBE_BATCH_ID = "00000000-0000-4000-8000-000000000000"
SLOT_NAMES = ("MINER_U", "MINER_U_2", "MINER_U_3", "MINER_U_4")
SHANGHAI = ZoneInfo("Asia/Shanghai")

EXPIRED_CODE = "A0211"
INVALID_CODE = "A0202"

THREE_DAYS = timedelta(days=3)
FOURTEEN_DAYS = timedelta(days=14)

STAGE_PRIORITY = {
    "healthy": 0,
    "healthy_forced": 1,
    "expiry_unknown": 20,
    "probe_unknown": 30,
    "expiring_14d": 40,
    "expiring_3d": 70,
    "invalid": 90,
    "expired": 100,
    "no_keys": 110,
}

STAGE_SEVERITY = {
    "healthy": "info",
    "healthy_forced": "info",
    "expiry_unknown": "warning",
    "probe_unknown": "warning",
    "expiring_14d": "warning",
    "expiring_3d": "critical",
    "invalid": "critical",
    "expired": "critical",
    "no_keys": "critical",
}


@dataclass(frozen=True)
class ConfiguredSlot:
    env_name: str
    display_name: str
    token: str
    explicit_expiry: str


@dataclass(frozen=True)
class ProbeResult:
    state: str
    code: str
    http_status: int | None


@dataclass(frozen=True)
class SlotResult:
    env_name: str
    display_name: str
    stage: str
    severity: str
    probe_state: str
    probe_code: str
    probe_http_status: int | None
    expiry_state: str
    expires_at: str
    expiry_source: str
    days_remaining: int | None


@dataclass(frozen=True)
class MonitorReport:
    checked_at: str
    configured_count: int
    issue_count: int
    should_alert: bool
    alert_stage: str
    severity: str
    subject: str
    dedupe_key: str
    slots: tuple[SlotResult, ...]


def slot_display_name(env_name: str) -> str:
    if env_name == "MINER_U":
        return "Key 1"
    return f"Key {env_name.rsplit('_', 1)[1]}"


def collect_configured_slots(env: Mapping[str, str]) -> list[ConfiguredSlot]:
    slots: list[ConfiguredSlot] = []
    for env_name in SLOT_NAMES:
        token = (env.get(env_name) or "").strip()
        if not token:
            continue
        slots.append(
            ConfiguredSlot(
                env_name=env_name,
                display_name=slot_display_name(env_name),
                token=token,
                explicit_expiry=(env.get(f"{env_name}_EXPIRES_AT") or "").strip(),
            )
        )
    return slots


def _decode_base64url_json(value: str) -> dict[str, Any] | None:
    try:
        padded = value + "=" * (-len(value) % 4)
        decoded = base64.urlsafe_b64decode(padded.encode("ascii"))
        payload = json.loads(decoded.decode("utf-8"))
    except (ValueError, UnicodeError, json.JSONDecodeError):
        return None
    return payload if isinstance(payload, dict) else None


def jwt_expiry(token: str) -> datetime | None:
    """Return a JWT ``exp`` timestamp, or None for opaque/malformed tokens."""

    parts = token.split(".")
    if len(parts) != 3:
        return None
    payload = _decode_base64url_json(parts[1])
    if not payload:
        return None
    exp = payload.get("exp")
    if isinstance(exp, bool) or not isinstance(exp, (int, float)):
        return None
    try:
        return datetime.fromtimestamp(float(exp), tz=timezone.utc)
    except (OverflowError, OSError, ValueError):
        return None


def parse_explicit_expiry(value: str) -> datetime:
    """Parse an ISO date/time; a date-only value means end-of-day in Beijing."""

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


def resolve_expiry(slot: ConfiguredSlot) -> tuple[datetime | None, str, bool]:
    """Return expiry, source, and whether an explicit variable was malformed."""

    if slot.explicit_expiry:
        try:
            return parse_explicit_expiry(slot.explicit_expiry), "GitHub Variable（预计值）", False
        except ValueError:
            return None, "GitHub Variable（预计值，格式无效）", True
    expiry = jwt_expiry(slot.token)
    if expiry:
        return expiry, "JWT exp", False
    return None, "未识别", False


def _response_code(body: bytes) -> str:
    try:
        payload = json.loads(body.decode("utf-8"))
    except (UnicodeError, json.JSONDecodeError):
        return ""
    if not isinstance(payload, dict):
        return ""
    # The documentation shows ``code`` while the live gateway also uses
    # ``msgCode`` for authentication failures. Accept both without retaining
    # the rest of the provider response.
    code = payload.get("code")
    if code is None:
        code = payload.get("msgCode")
    if code is None:
        code = payload.get("msg_code")
    if code is None:
        return ""
    return str(code).strip().upper()


def classify_probe_response(http_status: int, code: str) -> ProbeResult:
    """Classify only documented auth codes; transient/ambiguous replies stay unknown."""

    normalized_code = (code or "").strip().upper()
    if http_status == 429 or http_status >= 500:
        return ProbeResult("unknown", normalized_code, http_status)
    if normalized_code == EXPIRED_CODE:
        return ProbeResult("expired", normalized_code, http_status)
    if normalized_code == INVALID_CODE:
        return ProbeResult("invalid", normalized_code, http_status)
    if http_status in {401, 403}:
        return ProbeResult("unknown", normalized_code, http_status)
    # Any other application code from the synthetic task lookup means the
    # request passed token authentication and failed later in task lookup.
    if normalized_code:
        return ProbeResult("valid", normalized_code, http_status)
    if 200 <= http_status < 300:
        return ProbeResult("valid", "", http_status)
    return ProbeResult("unknown", "", http_status)


def probe_token(
    token: str,
    *,
    api_base_url: str = DEFAULT_MINERU_BASE_URL,
    timeout: float = 20,
    opener: Callable[..., Any] | None = None,
) -> ProbeResult:
    parsed = urllib.parse.urlparse(api_base_url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return ProbeResult("unknown", "", None)
    url = f"{api_base_url.rstrip('/')}/api/v4/extract-results/batch/{PROBE_BATCH_ID}"
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "portal-suite-mineru-key-monitor/1.0",
        },
        method="GET",
    )
    open_request = opener or urllib.request.urlopen
    try:
        with open_request(request, timeout=timeout) as response:
            status = int(response.getcode())
            body = response.read(64 * 1024)
        return classify_probe_response(status, _response_code(body))
    except urllib.error.HTTPError as error:
        try:
            body = error.read(64 * 1024)
        except Exception:  # noqa: BLE001 - status alone still gives a safe result.
            body = b""
        return classify_probe_response(int(error.code), _response_code(body))
    except (urllib.error.URLError, TimeoutError, OSError):
        return ProbeResult("unknown", "", None)


def expiry_evaluation(
    expiry: datetime | None,
    *,
    now: datetime,
    malformed: bool = False,
) -> tuple[str, str, int | None]:
    if malformed or expiry is None:
        return "unknown", "expiry_unknown", None
    remaining = expiry.astimezone(timezone.utc) - now.astimezone(timezone.utc)
    seconds = remaining.total_seconds()
    days_remaining = math.ceil(seconds / 86400)
    if seconds <= 0:
        return "expired", "expired", days_remaining
    if remaining <= THREE_DAYS:
        return "expiring", "expiring_3d", days_remaining
    if remaining <= FOURTEEN_DAYS:
        return "expiring", "expiring_14d", days_remaining
    return "healthy", "healthy", days_remaining


def choose_slot_stage(probe: ProbeResult, expiry_stage: str) -> str:
    candidates = [expiry_stage]
    if probe.state == "expired":
        candidates.append("expired")
    elif probe.state == "invalid":
        candidates.append("invalid")
    elif probe.state == "unknown":
        candidates.append("probe_unknown")
    return max(candidates, key=lambda stage: STAGE_PRIORITY[stage])


def _iso_utc(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def _stage_fingerprint(stage: str, slots: list[SlotResult]) -> str:
    affected = [
        f"{row.env_name}:{row.stage}:{row.expires_at or 'unknown'}"
        for row in slots
        if row.stage != "healthy"
    ]
    material = "|".join(affected) or "healthy"
    digest = hashlib.sha256(material.encode("utf-8")).hexdigest()[:12]
    return f"mineru-key-monitor:{stage}:{digest}"


def _subject(stage: str, issue_count: int, configured_count: int, force_email: bool) -> str:
    if stage == "no_keys":
        return "[Portal Operations] 未检测到 MinerU API Key"
    if issue_count:
        return f"[Portal Operations] MinerU API Key 检查：{issue_count} 枚需要处理"
    if force_email:
        return f"[Portal Operations 测试] MinerU API Key 检查正常（{configured_count} 枚）"
    return f"[Portal Operations] MinerU API Key 检查正常（{configured_count} 枚）"


def run_monitor(
    env: Mapping[str, str],
    *,
    now: datetime | None = None,
    force_email: bool = False,
    api_base_url: str = DEFAULT_MINERU_BASE_URL,
    timeout: float = 20,
    probe_func: Callable[..., ProbeResult] = probe_token,
) -> MonitorReport:
    checked_at = now or datetime.now(timezone.utc)
    if checked_at.tzinfo is None:
        checked_at = checked_at.replace(tzinfo=timezone.utc)
    configured = collect_configured_slots(env)
    rows: list[SlotResult] = []
    for slot in configured:
        probe = probe_func(slot.token, api_base_url=api_base_url, timeout=timeout)
        expiry, source, malformed = resolve_expiry(slot)
        expiry_state, expiry_stage, days_remaining = expiry_evaluation(
            expiry,
            now=checked_at,
            malformed=malformed,
        )
        stage = choose_slot_stage(probe, expiry_stage)
        rows.append(
            SlotResult(
                env_name=slot.env_name,
                display_name=slot.display_name,
                stage=stage,
                severity=STAGE_SEVERITY[stage],
                probe_state=probe.state,
                probe_code=probe.code,
                probe_http_status=probe.http_status,
                expiry_state=expiry_state,
                expires_at=_iso_utc(expiry) if expiry else "",
                expiry_source=source,
                days_remaining=days_remaining,
            )
        )

    if not rows:
        alert_stage = "no_keys"
        issue_count = 1
    else:
        alert_stage = max((row.stage for row in rows), key=lambda stage: STAGE_PRIORITY[stage])
        issue_count = sum(row.stage != "healthy" for row in rows)
        if not issue_count and force_email:
            alert_stage = "healthy_forced"
    should_alert = bool(issue_count or force_email)
    severity = STAGE_SEVERITY[alert_stage]
    return MonitorReport(
        checked_at=_iso_utc(checked_at),
        configured_count=len(rows),
        issue_count=issue_count,
        should_alert=should_alert,
        alert_stage=alert_stage,
        severity=severity,
        subject=_subject(alert_stage, issue_count, len(rows), force_email),
        dedupe_key=_stage_fingerprint(alert_stage, rows),
        slots=tuple(rows),
    )


PROBE_TEXT = {
    "valid": "鉴权有效",
    "expired": "API 已确认过期",
    "invalid": "API 已确认无效",
    "unknown": "暂时无法确认（服务或网络响应不确定）",
}

STAGE_TEXT = {
    "healthy": "正常",
    "expiry_unknown": "无法确定到期时间",
    "probe_unknown": "API 状态暂时无法确认",
    "expiring_14d": "14 天内到期",
    "expiring_3d": "3 天内到期",
    "invalid": "Key 无效，需要更换",
    "expired": "已到期，需要更换",
}


def _expiry_text(row: SlotResult) -> str:
    if not row.expires_at:
        if "格式无效" in row.expiry_source:
            return "到期变量格式无效"
        return "未找到明确到期时间"
    local_expiry = datetime.fromisoformat(row.expires_at.replace("Z", "+00:00")).astimezone(SHANGHAI)
    rendered = local_expiry.strftime("%Y-%m-%d %H:%M %Z")
    if row.days_remaining is None:
        return rendered
    if row.days_remaining <= 0:
        return f"{rendered}（已到期）"
    return f"{rendered}（约 {row.days_remaining} 天后）"


def render_email(report: MonitorReport, env: Mapping[str, str]) -> str:
    lines = [
        "MinerU API Key 定期检查结果如下。邮件只显示 Key 槽位，不包含任何凭证内容。",
        "",
        f"检查时间：{report.checked_at}",
        f"已配置 Key：{report.configured_count} 枚",
        f"需要处理：{report.issue_count} 枚",
        f"提醒阶段：{report.alert_stage}",
        "",
        "检查结果：",
    ]
    if not report.slots:
        lines.append("- 未检测到 MINER_U、MINER_U_2、MINER_U_3、MINER_U_4 中任何非空 Secret。")
    for row in report.slots:
        code = f"，代码 {row.probe_code}" if row.probe_code else ""
        lines.extend(
            [
                f"- {row.display_name}（{row.env_name}）：{STAGE_TEXT[row.stage]}",
                f"  API 验证：{PROBE_TEXT[row.probe_state]}{code}",
                f"  到期时间：{_expiry_text(row)}；来源：{row.expiry_source}",
            ]
        )

    lines.extend(
        [
            "",
            "需要更换时：",
            "1. 打开 GitHub 仓库 Settings → Secrets and variables → Actions。",
            "2. 在 Secrets 中替换邮件列出的 MINER_U 槽位。",
            "3. 在 Variables 中同步更新同名的 *_EXPIRES_AT，建议使用带时区的 ISO 时间，例如 2026-12-31T23:59:59+08:00。",
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
    payload["slots"] = [asdict(row) for row in report.slots]
    return payload


def write_github_output(path: Path | None, report: MonitorReport, email_path: Path, json_path: Path) -> None:
    if path is None:
        return
    values = {
        "should_alert": str(report.should_alert).lower(),
        "alert_stage": report.alert_stage,
        "severity": report.severity,
        "subject": report.subject,
        "dedupe_key": report.dedupe_key,
        "configured_count": str(report.configured_count),
        "issue_count": str(report.issue_count),
        "email_file": str(email_path),
        "json_file": str(json_path),
    }
    with path.open("a", encoding="utf-8") as handle:
        for key, value in values.items():
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
    parser = argparse.ArgumentParser(description="Check MinerU key validity and expiry")
    parser.add_argument("--api-base-url", default=os.environ.get("MINERU_BASE_URL", DEFAULT_MINERU_BASE_URL))
    parser.add_argument("--timeout", type=float, default=20)
    parser.add_argument("--force-email", action="store_true")
    parser.add_argument("--now", help=argparse.SUPPRESS)
    parser.add_argument("--json-output", type=Path, required=True)
    parser.add_argument("--email-output", type=Path, required=True)
    parser.add_argument("--github-output", type=Path, default=Path(os.environ["GITHUB_OUTPUT"]) if os.environ.get("GITHUB_OUTPUT") else None)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    now = parse_now(args.now) if args.now else None
    report = run_monitor(
        os.environ,
        now=now,
        force_email=args.force_email,
        api_base_url=args.api_base_url,
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
        "MinerU key monitor complete: "
        f"configured={report.configured_count}, issues={report.issue_count}, "
        f"stage={report.alert_stage}, alert={str(report.should_alert).lower()}"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001 - keep Actions failure concise and credential-free.
        print(f"MinerU key monitor failed: {type(exc).__name__}", file=sys.stderr)
        raise SystemExit(1)
