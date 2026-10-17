#!/usr/bin/env python3
"""Send one signed operations alert through the Portal Suite Newsfeed mail worker."""

from __future__ import annotations

import argparse
import hashlib
import hmac
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


DEFAULT_WORKER_BASE_URL = "https://portal.example.invalid/api"
ALERT_PATH = "/ops/alerts/email"
DEFAULT_DEDUPE_HOURS = 24
MIN_DEDUPE_HOURS = 1
MAX_DEDUPE_HOURS = 720


def workflow_alert_text(workflow: str, source_results: str, env: dict[str, str]) -> str:
    """Describe observed consumer outcomes without guessing provider failures."""
    results = {}
    for item in source_results.split(","):
        key, separator, value = item.partition("=")
        if separator:
            results[key.strip()] = value.strip()
    lines = ["自动任务有未完成的环节，请按下列交付状态检查对应步骤。", ""]
    if workflow == "Daily report articles and translations":
        no_work = results.get("no_work") == "true" and results.get("selected_count") == "0"
        if no_work:
            wechat = "本次无新增来源，未声称新增草稿"
        elif results.get("wechat_enabled") == "false":
            wechat = "本次未启用"
        elif results.get("wechat_source") == "portal_translated":
            wechat = "已完成草稿投递与回读验证" if results.get("translated_wechat") == "success" else "尚未完成草稿交付"
        elif results.get("wechat") == "success":
            wechat = "已完成草稿投递与回读验证"
        elif (results.get("wechat_enabled") == "true" and results.get("wechat_source") == "xhs_notes"
              and results.get("recovered_articles") == "success"):
            wechat = "已通过恢复链路完成草稿投递与回读验证"
        else:
            wechat = "尚未确认完成草稿交付"
        lines.append(f"微信文章：{wechat}。")
        market = ("本次无新增来源" if no_work else
                  "已验证交付" if results.get("delivery_gate") == "success" else "尚未确认交付")
        lines.append(f"Market Views：{market}。")
        if no_work:
            translated = "本次无新增来源"
        elif results.get("translation_requested") == "0":
            translated = "本次未启用"
        elif results.get("translated") == "success":
            translated = "已完成"
        elif results.get("translation_shards") in {"failure", "cancelled"}:
            translated = "分片未全部完成，合并交付尚未完成；请查看失败分片日志和 runner 注释"
        else:
            translated = "尚未确认完成"
        lines.append(f"报告全文翻译：{translated}。")
        source_kind = results.get("recovery_source_kind")
        if results.get("market_source_recovery") == "success" and source_kind == "mineru-recovery":
            lines.append("来源恢复：MinerU 结果已恢复；本次恢复未使用 OCR。")
        elif (results.get("market_source_recovery") == "success" and source_kind == "ocr-synthesis") or results.get("ocr_page_source_recovery") == "success":
            lines.append("来源恢复：OCR 来源已就绪；微信交付结果以上述独立状态为准。")
        lines.append("")
    failed = [key for key, value in results.items() if value in {"failure", "cancelled"}]
    if failed:
        lines.append("未完成的步骤：" + "、".join(failed))
    lines += [f"Workflow：{workflow}", f"Job 结果：{source_results}",
              f"触发方式：{env.get('GITHUB_EVENT_NAME', '')}",
              f"分支：{env.get('GITHUB_REF_NAME', '')}",
              "运行地址：" + env.get("GITHUB_SERVER_URL", "https://github.com") + "/" + env.get("GITHUB_REPOSITORY", "") + "/actions/runs/" + env.get("GITHUB_RUN_ID", ""), "",
              "整体任务失败不代表所有文章均未交付。以上仅根据已记录的步骤结果判断；具体原因请查看首次失败步骤的错误及 runner 注释。未获得明确 API 错误时，不将原因归为余额、Token 或服务故障。已验证草稿和完成的分片会保留，恢复时复用。"]
    return "\n".join(lines)


def normalize_worker_url(value: str) -> str:
    base = (value or "").strip() or DEFAULT_WORKER_BASE_URL
    if base.startswith("/"):
        base = f"https://portal.example.invalid{base}"
    parsed = urllib.parse.urlparse(base)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("Portal Suite Worker URL must be an absolute HTTP(S) URL or a /api path")
    return f"{base.rstrip('/')}{ALERT_PATH}"


def dedupe_hours_value(value: int | str) -> int:
    hours = int(value)
    if not MIN_DEDUPE_HOURS <= hours <= MAX_DEDUPE_HOURS:
        raise ValueError(
            f"dedupe hours must be between {MIN_DEDUPE_HOURS} and {MAX_DEDUPE_HOURS}"
        )
    return hours


def payload_bytes(
    subject: str,
    text: str,
    dedupe_key: str,
    severity: str,
    dedupe_hours: int = DEFAULT_DEDUPE_HOURS,
) -> bytes:
    payload = {
        "subject": subject.strip(),
        "text": text.strip(),
        "dedupe_key": dedupe_key.strip(),
        "dedupe_window_hours": dedupe_hours_value(dedupe_hours),
        "severity": severity.strip().lower(),
    }
    if not payload["subject"] or not payload["text"] or not payload["dedupe_key"]:
        raise ValueError("subject, text, and dedupe_key are required")
    return json.dumps(
        payload,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def signed_headers(signing_key: str, body: bytes, timestamp: int) -> dict[str, str]:
    if not signing_key:
        raise ValueError("OPS_ALERT_SIGNING_KEY is not configured")
    timestamp_text = str(int(timestamp))
    message = timestamp_text.encode("ascii") + b"." + body
    signature = hmac.new(signing_key.encode("utf-8"), message, hashlib.sha256).hexdigest()
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "rpt-edit-ops-alert/1.0",
        "X-Portal-Timestamp": timestamp_text,
        "X-Portal-Signature": f"sha256={signature}",
    }


def send_alert(
    *,
    worker_base_url: str,
    signing_key: str,
    subject: str,
    text: str,
    dedupe_key: str,
    severity: str = "warning",
    dedupe_hours: int = DEFAULT_DEDUPE_HOURS,
    attempts: int = 3,
    timeout: float = 20,
) -> dict[str, Any]:
    url = normalize_worker_url(worker_base_url)
    body = payload_bytes(subject, text, dedupe_key, severity, dedupe_hours)
    last_error: Exception | None = None
    for attempt in range(1, max(1, attempts) + 1):
        request = urllib.request.Request(
            url,
            data=body,
            headers=signed_headers(signing_key, body, int(time.time())),
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                response_body = response.read().decode("utf-8", errors="replace")
                result = json.loads(response_body or "{}")
                if not result.get("sent"):
                    raise RuntimeError(result.get("detail") or "Portal Suite Worker did not confirm the alert")
                return result
        except urllib.error.HTTPError as error:
            detail = error.read().decode("utf-8", errors="replace")[:500]
            last_error = RuntimeError(f"Portal Suite Worker returned HTTP {error.code}: {detail}")
            if error.code not in {408, 425, 429} and error.code < 500:
                break
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, RuntimeError) as error:
            last_error = error
        if attempt < max(1, attempts):
            time.sleep(min(2 ** (attempt - 1), 4))
    raise RuntimeError(f"Could not send Portal Suite operations alert: {last_error}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--worker-base-url",
        default=os.environ.get("PORTAL_WORKER_URL", DEFAULT_WORKER_BASE_URL),
    )
    parser.add_argument("--subject", required=True)
    parser.add_argument("--text")
    parser.add_argument("--text-file", type=Path)
    parser.add_argument("--source-workflow")
    parser.add_argument("--workflow-results")
    parser.add_argument("--dedupe-key", required=True)
    parser.add_argument(
        "--dedupe-hours",
        type=dedupe_hours_value,
        default=DEFAULT_DEDUPE_HOURS,
        metavar="HOURS",
        help=(
            f"Suppress repeats for {MIN_DEDUPE_HOURS}-{MAX_DEDUPE_HOURS} hours "
            "(default: %(default)s)."
        ),
    )
    parser.add_argument("--severity", choices=("info", "warning", "critical"), default="warning")
    parser.add_argument("--attempts", type=int, default=3)
    parser.add_argument("--timeout", type=float, default=20)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    text = args.text or ""
    if args.text_file:
        text = args.text_file.read_text(encoding="utf-8")
    if args.source_workflow:
        text = workflow_alert_text(args.source_workflow, args.workflow_results or "", dict(os.environ))
    signing_key = os.environ.get("OPS_ALERT_SIGNING_KEY", "").strip()
    result = send_alert(
        worker_base_url=args.worker_base_url,
        signing_key=signing_key,
        subject=args.subject,
        text=text,
        dedupe_key=args.dedupe_key,
        severity=args.severity,
        dedupe_hours=args.dedupe_hours,
        attempts=args.attempts,
        timeout=args.timeout,
    )
    status = "deduplicated" if result.get("deduplicated") else "sent"
    print(f"Portal Suite operations alert {status} via {result.get('provider') or 'configured provider'}.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001 - keep workflow error concise.
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)
