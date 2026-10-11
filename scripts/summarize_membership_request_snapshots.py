#!/usr/bin/env python3
"""Read retained membership snapshots in cloud memory and emit aggregate counts only.

The requested Beijing start/end dates are inclusive. This is a snapshot inventory,
not a submission ledger, a people count, a conversion funnel or a delivery audit.
Only ListObjectsV2 and GetObject are used; no provider is contacted or R2 modified.
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import date, datetime, time, timedelta, timezone
import json
import os
from pathlib import Path
import re
import sys
from typing import Any


PREFIX = "_membership-requests/v1/items/"
OBJECT_PATTERN = re.compile(re.escape(PREFIX) + r"[a-f0-9]{64}\.json\Z")
MAX_RECORD_BYTES = 128_000
MAX_OBJECTS = 50_000
KINDS = ("membership", "access", "support", "privacy", "refund")
STATUSES = ("pending", "sent", "failed")
WINDOWS = ("created_window", "latest_attempt_window", "retained_sent_window")
SHANGHAI = timezone(timedelta(hours=8))
ISSUES = (
    "invalid_objects", "duplicate_objects", "invalid_records", "read_failures",
    "listing_failures", "pagination_failures",
)
NOTES = (
    "Counts describe currently retained deduplicated snapshots, not people, sessions, submissions or a conversion funnel.",
    "A retry overwrites the same snapshot: created_at is retained; attempted_at, sent_at and the latest status can change.",
    "Created-window counts cover first creation of retained snapshots; latest-attempt counts do not recover every historical attempt.",
    "Retained-sent counts require the current status sent and current sent_at in the window; overwritten earlier notifications are unavailable.",
    "Sent means provider acceptance only, not inbox delivery, owner processing, membership activation or payment.",
    "Validation rejections, rate limits, honeypot responses and deduplicated responses do not create distinct snapshots.",
    "Storage lifecycle, earlier deletions and identity changes cannot be reconstructed from these snapshots.",
    "The three windows overlap. Membership and access are separate; support, privacy and refund are not membership conversions.",
    "Listing and reads are not an atomic historical snapshot; concurrent updates can affect the inventory.",
    "Any incomplete listing, invalid record or read failure makes every primary count null; diagnostic counts describe only scan coverage.",
)
PRIVACY = {
    "individual_records_included": False,
    "identifiers_included": False,
    "contact_details_included": False,
    "source_record_text_included": False,
}


class SafeError(RuntimeError):
    """Only fixed, non-identifying messages may be used."""


class InvalidRecord(SafeError):
    pass


class ReadFailure(SafeError):
    pass


def parse_day(value: str) -> date:
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise SafeError("Dates must use YYYY-MM-DD.")
    try:
        return date.fromisoformat(value)
    except ValueError:
        raise SafeError("A requested date is invalid.") from None


def interval(start_date: str, end_date: str) -> tuple[datetime, datetime]:
    start, end = parse_day(start_date), parse_day(end_date)
    if start > end:
        raise SafeError("The start date must not follow the end date.")
    try:
        end_exclusive = end + timedelta(days=1)
    except OverflowError:
        raise SafeError("The end date cannot be represented.") from None
    return (
        datetime.combine(start, time.min, SHANGHAI).astimezone(timezone.utc),
        datetime.combine(end_exclusive, time.min, SHANGHAI).astimezone(timezone.utc),
    )


def timestamp(value: Any) -> datetime:
    if not isinstance(value, str) or len(value) > 64:
        raise InvalidRecord("A snapshot timestamp is invalid.")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            raise ValueError
        return parsed.astimezone(timezone.utc)
    except (ValueError, TypeError, OverflowError):
        raise InvalidRecord("A snapshot timestamp is invalid.") from None


def utc_text(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def read_projection(client: Any, bucket: str, object_name: str) -> tuple:
    """Drop source bytes and the decoded record before returning controlled fields."""
    body = None
    try:
        try:
            response = client.get_object(Bucket=bucket, Key=object_name)
            body = response["Body"]
            declared = response.get("ContentLength")
            if "ContentLength" in response:
                if type(declared) is not int or declared < 0:
                    raise ReadFailure("A snapshot read has invalid length metadata.")
                if declared > MAX_RECORD_BYTES:
                    raise InvalidRecord("A snapshot is too large.")
            raw = body.read(MAX_RECORD_BYTES + 1)
            if "ContentLength" in response and len(raw) != declared:
                raise ReadFailure("A snapshot read did not match its declared length.")
        except (InvalidRecord, ReadFailure):
            raise
        except Exception:
            raise ReadFailure("A snapshot could not be read.") from None
        try:
            if not isinstance(raw, bytes) or len(raw) > MAX_RECORD_BYTES:
                raise ValueError
            record = json.loads(raw)
            if not isinstance(record, dict) or type(record.get("version")) is not int or record["version"] != 1:
                raise ValueError
            kind, status = record.get("request_kind"), record.get("status")
            if kind not in KINDS or status not in STATUSES:
                raise ValueError
            created, attempted = timestamp(record.get("created_at")), timestamp(record.get("attempted_at"))
            raw_sent = record.get("sent_at")
            if not isinstance(raw_sent, str):
                raise ValueError
            sent = timestamp(raw_sent) if raw_sent else None
            if created > attempted or (sent is not None and sent < attempted):
                raise ValueError
            if (status == "sent") != (sent is not None):
                raise ValueError
            return kind, status, created, attempted, sent
        except Exception:
            raise InvalidRecord("A snapshot has invalid structure or controlled fields.") from None
    finally:
        if body is not None and callable(getattr(body, "close", None)):
            try:
                body.close()
            except Exception:
                pass


def empty_metric() -> dict[str, Any]:
    return {"snapshot_count": 0, "by_request_kind": dict.fromkeys(KINDS, 0),
            "by_latest_status": dict.fromkeys(STATUSES, 0)}


def summarize(client: Any, bucket: str, start_date: str, end_date: str,
              max_objects: int = 5000) -> dict[str, Any]:
    start, end = interval(start_date, end_date)
    if not isinstance(bucket, str) or not bucket.strip():
        raise SafeError("The private bucket is not configured.")
    if type(max_objects) is not int or not 1 <= max_objects <= MAX_OBJECTS:
        raise SafeError("The object limit must be between 1 and 50000.")
    metrics = {name: empty_metric() for name in WINDOWS}
    counts: Counter = Counter()
    seen_objects: set[str] = set()
    seen_tokens: set[str] = set()
    token = ""
    exhausted = limit_reached = False
    while True:
        remaining = max_objects - counts["objects_listed"]
        if remaining <= 0:
            limit_reached = True
            break
        options = {"Bucket": bucket, "Prefix": PREFIX, "MaxKeys": min(1000, remaining)}
        if token:
            options["ContinuationToken"] = token
        try:
            response = client.list_objects_v2(**options)
        except Exception:
            counts["listing_failures"] += 1
            break
        entries = response.get("Contents", []) if isinstance(response, dict) else None
        truncated = response.get("IsTruncated") if isinstance(response, dict) else None
        if (not isinstance(entries, list) or len(entries) > options["MaxKeys"]
                or type(truncated) is not bool):
            counts["pagination_failures"] += 1
            break
        counts["objects_listed"] += len(entries)
        for entry in entries:
            object_name = entry.get("Key") if isinstance(entry, dict) else None
            if not isinstance(object_name, str) or not OBJECT_PATTERN.fullmatch(object_name):
                counts["invalid_objects"] += 1
                continue
            if object_name in seen_objects:
                counts["duplicate_objects"] += 1
                continue
            seen_objects.add(object_name)
            try:
                kind, status, created, attempted, sent = read_projection(client, bucket, object_name)
            except ReadFailure:
                counts["read_failures"] += 1
                continue
            except InvalidRecord:
                counts["invalid_records"] += 1
                continue
            counts["valid_records"] += 1
            matched = False
            for name, when in zip(WINDOWS, (created, attempted, sent)):
                if when is not None and start <= when < end:
                    metrics[name]["snapshot_count"] += 1
                    metrics[name]["by_request_kind"][kind] += 1
                    metrics[name]["by_latest_status"][status] += 1
                    matched = True
            counts["outside_all_windows"] += int(not matched)
        if not truncated:
            exhausted = True
            break
        next_token = response.get("NextContinuationToken")
        if not isinstance(next_token, str) or not next_token or next_token in seen_tokens or not entries:
            counts["pagination_failures"] += 1
            break
        seen_tokens.add(next_token)
        token = next_token
    complete = exhausted and not limit_reached and not any(counts[name] for name in ISSUES)
    if not complete:
        for metric in metrics.values():
            metric["snapshot_count"] = None
            metric["by_request_kind"] = dict.fromkeys(KINDS, None)
            metric["by_latest_status"] = dict.fromkeys(STATUSES, None)
    report = {
        "schema": "membership-request-snapshots-v1",
        "generated_at": utc_text(datetime.now(timezone.utc)),
        "window": {"start_date_inclusive": start_date, "end_date_inclusive": end_date,
                   "timezone": "Asia/Shanghai", "start_utc_inclusive": utc_text(start),
                   "end_utc_exclusive": utc_text(end)},
        "count_basis": "currently_retained_deduplicated_request_snapshots",
        "coverage": "complete" if complete else "partial",
        "complete": complete,
        "scan": {"max_objects": max_objects, "max_record_bytes": MAX_RECORD_BYTES,
                 "objects_listed": counts["objects_listed"], "valid_records": counts["valid_records"],
                 "outside_all_windows": counts["outside_all_windows"],
                 "prefix_exhausted": exhausted, "object_limit_reached": limit_reached,
                 **{name: counts[name] for name in ISSUES}},
        "windows": metrics,
        "privacy": dict(PRIVACY),
        "notes": list(NOTES),
    }
    assert_aggregate_privacy(report)
    return report


def assert_aggregate_privacy(report: Any) -> None:
    """Recursively allow only a fixed aggregate schema and controlled strings."""
    def fail():
        raise SafeError("Aggregate output failed the privacy or structure check.")

    def exact(value, names):
        if not isinstance(value, dict) or set(value) != set(names):
            fail()

    def count(value, nullable=False):
        if nullable and value is None:
            return
        if type(value) is not int or not 0 <= value <= MAX_OBJECTS:
            fail()

    exact(report, ("schema", "generated_at", "window", "count_basis", "coverage", "complete",
                   "scan", "windows", "privacy", "notes"))
    if (report["schema"] != "membership-request-snapshots-v1"
            or report["count_basis"] != "currently_retained_deduplicated_request_snapshots"
            or type(report["complete"]) is not bool
            or report["coverage"] != ("complete" if report["complete"] else "partial")
            or report["privacy"] != PRIVACY or report["notes"] != list(NOTES)):
        fail()
    try:
        if utc_text(timestamp(report["generated_at"])) != report["generated_at"]:
            fail()
        w = report["window"]
        exact(w, ("start_date_inclusive", "end_date_inclusive", "timezone", "start_utc_inclusive", "end_utc_exclusive"))
        start, end = interval(w["start_date_inclusive"], w["end_date_inclusive"])
        if w["timezone"] != "Asia/Shanghai" or w["start_utc_inclusive"] != utc_text(start) or w["end_utc_exclusive"] != utc_text(end):
            fail()
    except (SafeError, ValueError, TypeError):
        fail()
    scan = report["scan"]
    exact(scan, ("max_objects", "max_record_bytes", "objects_listed", "valid_records", "outside_all_windows",
                 "prefix_exhausted", "object_limit_reached", *ISSUES))
    if scan["max_record_bytes"] != MAX_RECORD_BYTES:
        fail()
    for name, value in scan.items():
        if name in ("prefix_exhausted", "object_limit_reached"):
            if type(value) is not bool:
                fail()
        elif name != "max_record_bytes":
            count(value)
    if not 1 <= scan["max_objects"] <= MAX_OBJECTS or scan["objects_listed"] > scan["max_objects"]:
        fail()
    expected_complete = scan["prefix_exhausted"] and not scan["object_limit_reached"] and not any(scan[name] for name in ISSUES)
    if report["complete"] != expected_complete:
        fail()
    exact(report["windows"], WINDOWS)
    for metric in report["windows"].values():
        exact(metric, ("snapshot_count", "by_request_kind", "by_latest_status"))
        exact(metric["by_request_kind"], KINDS)
        exact(metric["by_latest_status"], STATUSES)
        values = [metric["snapshot_count"], *metric["by_request_kind"].values(), *metric["by_latest_status"].values()]
        if report["complete"]:
            for value in values:
                count(value)
            if any(sum(metric[name].values()) != metric["snapshot_count"] for name in ("by_request_kind", "by_latest_status")):
                fail()
            if metric["snapshot_count"] > scan["valid_records"]:
                fail()
        elif any(value is not None for value in values):
            fail()


def render_markdown(report: dict[str, Any]) -> str:
    assert_aggregate_privacy(report)
    w = report["window"]
    def show(value):
        return str(value) if value is not None else "不可用（partial）"
    lines = ["# 会员申请业务快照核对", "",
             f"北京日期：{w['start_date_inclusive']} 至 {w['end_date_inclusive']}（含两端）。",
             f"扫描覆盖：{report['coverage']}。统计的是当前保留的去重快照，不是用户数、每次提交的完整流水或转化漏斗。", "",
             "| 时间口径 | 现存快照数量 |", "| --- | ---: |"]
    labels = {"created_window": "首次保存日在窗口内", "latest_attempt_window": "最近尝试日在窗口内",
              "retained_sent_window": "当前仍为 sent，且保留的发送日在窗口内"}
    for name in WINDOWS:
        lines.append(f"| {labels[name]} | {show(report['windows'][name]['snapshot_count'])} |")
    for name in WINDOWS:
        metric = report["windows"][name]
        lines += ["", f"## {labels[name]}", "", "| 申请类型 | 数量 |", "| --- | ---: |"]
        lines += [f"| {kind} | {show(metric['by_request_kind'][kind])} |" for kind in KINDS]
        lines += ["", "| 最新状态 | 数量 |", "| --- | ---: |"]
        lines += [f"| {status} | {show(metric['by_latest_status'][status])} |" for status in STATUSES]
    lines += ["", "## 覆盖诊断", "", "| 项目 | 值 |", "| --- | ---: |"]
    lines += [f"| {name} | {str(value).lower() if isinstance(value, bool) else value} |" for name, value in report["scan"].items()]
    lines += ["", "## 解释边界", "",
              "- 三个时间窗口可重叠；会员与访问权限分别列示，支持、隐私和退款不计会员转化。",
              "- 重试覆盖原快照，保留首次创建日期，但替换最近尝试、发送时间和状态；无法恢复被覆盖的历史尝试或通知。",
              "- sent 仅表示邮件服务接受发送（provider acceptance），不证明收件箱送达、人工处理、会员开通或付费。",
              "- 去重响应、字段拒绝、限流、蜜罐响应及保存前失败不形成独立新快照；对象删除、保留策略、身份变化和并发更新也限制历史完整性。",
              "- 任一列表/读取失败、无效记录或数量截断都会将全部主指标置为 null；覆盖诊断计数不代表申请量。",
              "- 输出只有汇总，无逐条记录、身份标识、联系方式、备注或错误正文。", ""]
    return "\n".join(lines)


def require_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value or value == "unconfigured":
        raise SafeError("Required private R2 configuration is missing.")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start-date", required=True)
    parser.add_argument("--end-date", required=True)
    parser.add_argument("--max-objects", type=int, default=5000)
    parser.add_argument("--output", required=True)
    parser.add_argument("--markdown-output", required=True)
    args = parser.parse_args()
    try:
        interval(args.start_date, args.end_date)
        if type(args.max_objects) is not int or not 1 <= args.max_objects <= MAX_OBJECTS:
            raise SafeError("The object limit must be between 1 and 50000.")
        import boto3
        from botocore.config import Config
        client = boto3.client(
            "s3", endpoint_url=f"https://{require_env('R2_ACCOUNT_ID')}.r2.cloudflarestorage.com",
            aws_access_key_id=require_env("R2_ACCESS_KEY_ID"),
            aws_secret_access_key=require_env("R2_SECRET_ACCESS_KEY"), region_name="auto",
            config=Config(retries={"max_attempts": 0}, connect_timeout=15, read_timeout=25),
        )
        report = summarize(client, require_env("R2_BUCKET"), args.start_date, args.end_date, args.max_objects)
        markdown = render_markdown(report)
        for target, content in ((args.output, json.dumps(report, ensure_ascii=False, indent=2) + "\n"),
                                (args.markdown_output, markdown)):
            Path(target).parent.mkdir(parents=True, exist_ok=True)
            Path(target).write_text(content, encoding="utf-8")
        return 0 if report["complete"] else 2
    except SafeError as error:
        print(str(error), file=sys.stderr)
        return 1
    except Exception:
        print("Snapshot aggregation failed; private diagnostic details were withheld.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
