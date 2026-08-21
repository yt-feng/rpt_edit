#!/usr/bin/env python3
"""Build per-bank TXT catalogs for the latest Dropbox report folders.

The script reads Dropbox /zip_backup date folders without downloading PDFs,
selects the latest N date-named folders, groups PDF filenames by sanitized
investment-bank short code, and writes one TXT file per bank.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any

import requests

DROPBOX_API = "https://api.dropboxapi.com/2"
DATE_FOLDER_RE = re.compile(r"^\d{6,8}$")
DROPBOX_REQUEST_MAX_ATTEMPTS = 5
DROPBOX_RETRY_BASE_SECONDS = 5.0
DROPBOX_RETRY_MAX_SECONDS = 40.0
DROPBOX_RETRY_AFTER_MAX_SECONDS = 300.0
DROPBOX_RETRYABLE_STATUSES = {408, 425, 429, 500, 502, 503, 504}
TRANSIENT_DROPBOX_ERRORS = (
    requests.exceptions.ConnectionError,
    requests.exceptions.Timeout,
    requests.exceptions.ChunkedEncodingError,
)

BANK_PATTERNS: list[tuple[str, str, str]] = [
    ("GS", "高盛", r"\b(?:goldman\s*sachs|gs)\b|高盛"),
    ("JPM", "摩根大通", r"\b(?:j\.?\s*p\.?\s*morgan|jpmorgan|jpm)\b|摩根大通"),
    ("MS", "摩根士丹利", r"\b(?:morgan\s*stanley|ms)\b|摩根士丹利|大摩"),
    ("BofA", "美银", r"\b(?:bank\s*of\s*america|bofa|merrill\s*lynch)\b|美银|美林"),
    ("Citi", "花旗", r"\b(?:citigroup|citi)\b|花旗"),
    ("UBS", "瑞银", r"\bubs\b|瑞银"),
    ("DB", "德银", r"\b(?:deutsche\s*bank|db)\b|德银|德意志银行"),
    ("HSBC", "汇丰", r"\bhsbc\b|汇丰"),
    ("BARC", "巴克莱", r"\bbarclays\b|巴克莱"),
    ("BNPP", "法巴", r"\b(?:bnp\s*paribas|bnpp|exane)\b|法巴|法国巴黎银行"),
    ("SG", "法兴", r"\b(?:societe\s*generale|soci[eé]t[eé]\s*g[eé]n[eé]rale|sg)\b|法兴|法兴银行"),
    ("CS", "瑞信", r"\b(?:credit\s*suisse|cs)\b|瑞信|瑞士信贷"),
    ("NOM", "野村", r"\b(?:nomura|nom)\b|野村"),
    ("Daiwa", "大和", r"\bdaiwa\b|大和"),
    ("Mizuho", "瑞穗", r"\bmizuho\b|瑞穗"),
    ("MQ", "麦格理", r"\bmacquarie\b|麦格理"),
    ("CLSA", "里昂", r"\bclsa\b|里昂"),
    ("CICC", "中金", r"\bcicc\b|中金"),
    ("CITIC", "中信证券", r"\b(?:citic\s*securities|citic)\b|中信证券"),
    ("CSC", "中信建投", r"中信建投|\bchina\s*securities\b"),
    ("CMS", "招商证券", r"\bchina\s*merchants\s*securities\b|招商证券"),
    ("Haitong", "海通证券", r"\bhaitong\b|海通证券"),
    ("HTSC", "华泰证券", r"\b(?:huatai|htsc)\b|华泰证券"),
    ("GTJA", "国泰君安", r"\b(?:guotai\s*junan|gtja)\b|国泰君安"),
    ("JEF", "杰富瑞", r"\bjefferies\b|杰富瑞"),
    ("Bernstein", "伯恩斯坦", r"\b(?:bernstein|sanford\s*c\.?\s*bernstein)\b|伯恩斯坦"),
    ("Evercore", "Evercore", r"\bevercore\b"),
    ("Guggenheim", "Guggenheim", r"\bguggenheim\b"),
    ("Piper", "Piper Sandler", r"\bpiper\s*sandler\b"),
    ("RJ", "Raymond James", r"\braymond\s*james\b"),
    ("RBC", "RBC", r"\brbc\b|加拿大皇家银行"),
    ("WellsFargo", "富国银行", r"\bwells\s*fargo\b|富国银行"),
    ("TD", "TD", r"\btd\s*(?:cowen|securities)?\b"),
    ("Cowen", "Cowen", r"\bcowen\b"),
    ("Oppenheimer", "Oppenheimer", r"\boppenheimer\b"),
    ("Wedbush", "Wedbush", r"\bwedbush\b"),
    ("Melius", "Melius", r"\bmelius\b"),
    ("Arete", "Arete", r"\barete\b"),
]


def log(message: str) -> None:
    print(message, flush=True)


def write_github_output(key: str, value: str) -> None:
    output_path = os.getenv("GITHUB_OUTPUT")
    if not output_path:
        return
    with open(output_path, "a", encoding="utf-8") as f:
        f.write(f"{key}={str(value).replace(chr(10), ' ')}\n")


def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def dropbox_error_payload(response: requests.Response) -> dict[str, Any]:
    try:
        payload = response.json()
    except (TypeError, ValueError):
        return {}
    if not isinstance(payload, dict):
        return {}
    return payload


def dropbox_error_tag(response: requests.Response) -> str:
    payload = dropbox_error_payload(response)
    error = payload.get("error")
    if not isinstance(error, dict):
        return ""
    return str(error.get(".tag") or "").strip().lower()


def dropbox_retry_delay(attempt: int, response: requests.Response | None = None) -> float:
    delay = min(
        DROPBOX_RETRY_MAX_SECONDS,
        DROPBOX_RETRY_BASE_SECONDS * (2 ** max(0, attempt - 1)),
    )
    if response is not None:
        retry_after = str(response.headers.get("Retry-After") or "").strip()
        try:
            delay = max(
                delay,
                min(DROPBOX_RETRY_AFTER_MAX_SECONDS, max(0.0, float(retry_after))),
            )
        except ValueError:
            pass
    return delay


def dropbox_response_is_retryable(response: requests.Response) -> bool:
    status = int(response.status_code)
    if status in DROPBOX_RETRYABLE_STATUSES:
        return True
    if status != 403 or dropbox_error_tag(response) != "other":
        return False

    # Dropbox can report an internal service-to-service Envoy denial as a
    # typed 403 even though the caller token and path are unchanged. Keep this
    # narrow so normal permission failures still stop immediately.
    payload = dropbox_error_payload(response)
    user_message = payload.get("user_message")
    message = user_message.get("text") if isinstance(user_message, dict) else ""
    diagnostic = f"{message}\n{response.text}".lower()
    return "spiffe://" in diagnostic and "/service/envoy-edge" in diagnostic


def dropbox_post_with_retry(label: str, url: str, **kwargs: Any) -> requests.Response:
    for attempt in range(1, DROPBOX_REQUEST_MAX_ATTEMPTS + 1):
        try:
            response = requests.post(url, **kwargs)
        except TRANSIENT_DROPBOX_ERRORS as exc:
            if attempt >= DROPBOX_REQUEST_MAX_ATTEMPTS:
                raise RuntimeError(
                    f"{label} failed after {attempt} attempts: {type(exc).__name__}: {exc}"
                ) from exc
            delay = dropbox_retry_delay(attempt)
            log(
                f"{label} transient {type(exc).__name__} on attempt "
                f"{attempt}/{DROPBOX_REQUEST_MAX_ATTEMPTS}; retrying in {delay:g}s"
            )
            time.sleep(delay)
            continue

        if response.status_code < 400:
            return response

        request_id = str(response.headers.get("X-Dropbox-Request-Id") or "missing")
        error_tag = dropbox_error_tag(response) or "unknown"
        if dropbox_response_is_retryable(response) and attempt < DROPBOX_REQUEST_MAX_ATTEMPTS:
            delay = dropbox_retry_delay(attempt, response)
            log(
                f"{label} transient HTTP {response.status_code} tag={error_tag} "
                f"request_id={request_id} on attempt {attempt}/{DROPBOX_REQUEST_MAX_ATTEMPTS}; "
                f"retrying in {delay:g}s"
            )
            response.close()
            time.sleep(delay)
            continue

        status = response.status_code
        body = response.text[:800]
        suffix = f" after {attempt} attempts" if attempt > 1 else ""
        response.close()
        raise RuntimeError(
            f"{label} failed{suffix}: HTTP {status}, "
            f"request_id={request_id}, {body}"
        )

    raise AssertionError("Dropbox retry loop exhausted without a result")


def dropbox_access_token() -> str:
    response = dropbox_post_with_retry(
        "Dropbox token refresh",
        "https://api.dropboxapi.com/oauth2/token",
        data={"grant_type": "refresh_token", "refresh_token": require_env("DROPBOX_REFRESH_TOKEN")},
        auth=(require_env("DROPBOX_APP_KEY"), require_env("DROPBOX_APP_SECRET")),
        timeout=60,
    )
    try:
        token = response.json().get("access_token")
    finally:
        response.close()
    if not token:
        raise RuntimeError("Dropbox token refresh response did not include access_token")
    return str(token)


def api_post(token: str, endpoint: str, payload: dict[str, Any]) -> dict[str, Any]:
    response = dropbox_post_with_retry(
        f"Dropbox API {endpoint}",
        f"{DROPBOX_API}{endpoint}",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        json=payload,
        timeout=90,
    )
    try:
        data = response.json()
    finally:
        response.close()
    if not isinstance(data, dict):
        raise RuntimeError(f"Dropbox API {endpoint} returned a non-object response")
    return data


def list_folder(token: str, path: str, recursive: bool = False) -> list[dict[str, Any]]:
    data = api_post(token, "/files/list_folder", {"path": path, "recursive": recursive, "include_deleted": False})
    entries = list(data.get("entries", []))
    while data.get("has_more"):
        data = api_post(token, "/files/list_folder/continue", {"cursor": data["cursor"]})
        entries.extend(data.get("entries", []))
    return entries


def latest_date_folders(entries: list[dict[str, Any]], days: int) -> list[dict[str, Any]]:
    folders = [e for e in entries if e.get(".tag") == "folder" and DATE_FOLDER_RE.match(str(e.get("name", "")))]
    if not folders:
        names = ", ".join(str(e.get("name")) for e in entries[:20])
        raise RuntimeError(f"No date-named child folders found. First entries: {names}")
    return sorted(folders, key=lambda e: int(e["name"]), reverse=True)[:days]


def detect_bank(text: str) -> tuple[str, str]:
    haystack = text.replace("_", " ").replace("-", " ").replace(".", " ")
    for code, cn_name, pattern in BANK_PATTERNS:
        if re.search(pattern, haystack, flags=re.IGNORECASE):
            return code, cn_name
    return "Other_IB", "其他投行"


def sanitize_report_name(name: str) -> str:
    stem = re.sub(r"\.pdf$", "", name, flags=re.IGNORECASE)
    text = stem
    for code, _cn_name, pattern in BANK_PATTERNS:
        text = re.sub(pattern, code, text, flags=re.IGNORECASE)
    text = re.sub(r"\s+", " ", text).strip(" -_\t\r\n")
    return text or stem


def safe_filename(code: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", code).strip("_") or "Other_IB"


def bank_display_name(code: str, cn_name: str) -> str:
    return f"{code}（{cn_name or code}）"


def render_sales_intro(code: str, cn_name: str) -> list[str]:
    display_name = bank_display_name(code, cn_name)
    return [
        f"{display_name}研报：单篇6.66，周报告合集29。",
        "需要单篇请发报告名，需要周报告合集的私聊咨询。",
        "拍下留邮箱或者云盘链接发送。",
        "",
        "商品描述：",
    ]


def collect_reports(token: str, root: str, folders: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    grouped: dict[str, dict[str, Any]] = defaultdict(lambda: {"cn_name": "", "dates": defaultdict(list)})
    for folder in folders:
        date_name = str(folder["name"])
        folder_path = str(folder.get("path_lower") or folder.get("path_display") or f"{root.rstrip('/')}/{date_name}")
        log(f"Listing PDFs under {folder_path}")
        entries = list_folder(token, folder_path, recursive=True)
        pdfs = [e for e in entries if e.get(".tag") == "file" and str(e.get("name", "")).lower().endswith(".pdf")]
        log(f"  {date_name}: {len(pdfs)} PDFs")
        for entry in sorted(pdfs, key=lambda e: str(e.get("name", "")).lower()):
            name = str(entry.get("name", "report.pdf"))
            path_display = str(entry.get("path_display") or entry.get("path_lower") or "")
            code, cn_name = detect_bank(f"{name} {path_display}")
            grouped[code]["cn_name"] = cn_name
            grouped[code]["dates"][date_name].append({
                "name": sanitize_report_name(name),
                "dropbox_path": path_display,
            })
    return grouped


def render_bank_txt(code: str, cn_name: str, dates: dict[str, list[dict[str, str]]], date_order: list[str], root: str, generated_at: str) -> str:
    lines: list[str] = []
    lines.extend(render_sales_intro(code, cn_name))
    lines.append("")
    for date_name in date_order:
        items = dates.get(date_name, [])
        if not items:
            continue
        lines.append(date_name)
        for item in items:
            lines.append(f"【{item['name']}】")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dropbox-root", default="/zip_backup")
    parser.add_argument("--days", type=int, default=5)
    parser.add_argument("--output-root", default="bank_report_catalogs")
    parser.add_argument("--output-date", default="")
    args = parser.parse_args()

    try:
        root = args.dropbox_root.rstrip("/") or ""
        token = dropbox_access_token()
        root_entries = list_folder(token, root, recursive=False)
        folders = latest_date_folders(root_entries, args.days)
        date_order = [str(f["name"]) for f in folders]
        generated_at = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
        output_date = args.output_date.strip() or date_order[0]
        output_dir = Path(args.output_root) / output_date
        output_dir.mkdir(parents=True, exist_ok=True)

        grouped = collect_reports(token, root, folders)
        summary: dict[str, Any] = {
            "generated_at_bjt": generated_at,
            "dropbox_root": root,
            "days": args.days,
            "date_order": date_order,
            "output_dir": str(output_dir),
            "banks": {},
        }

        for stale in output_dir.glob("*.txt"):
            stale.unlink()

        for code in sorted(grouped.keys(), key=lambda x: (x == "Other_IB", x.lower())):
            data = grouped[code]
            dates = data["dates"]
            count = sum(len(items) for items in dates.values())
            if count == 0:
                continue
            txt = render_bank_txt(code, data.get("cn_name") or code, dates, date_order, root, generated_at)
            path = output_dir / f"{safe_filename(code)}.txt"
            path.write_text(txt, encoding="utf-8")
            summary["banks"][code] = {
                "cn_name": data.get("cn_name") or code,
                "report_count": count,
                "file": str(path),
            }
            log(f"Wrote {path}: {count} reports")

        summary_path = output_dir / "summary.json"
        summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
        write_github_output("output_dir", str(output_dir))
        write_github_output("latest_folder", date_order[0])
        write_github_output("bank_count", str(len(summary["banks"])))
        log(f"Done. Output directory: {output_dir}")
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
