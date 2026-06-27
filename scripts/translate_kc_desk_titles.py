#!/usr/bin/env python3
"""Translate KC Desk Notes report titles to Simplified Chinese with DeepSeek."""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import re
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any

import requests


CJK_RE = re.compile(r"[\u3400-\u9fff]")


def log(message: str) -> None:
    print(message, flush=True)


def bjt_now() -> str:
    tz = timezone(timedelta(hours=8))
    return datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")


def load_json(path: Path, fallback: dict[str, Any]) -> dict[str, Any]:
    if not path.exists():
        return fallback
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def has_cjk(value: str) -> bool:
    return bool(CJK_RE.search(value or ""))


def normalize_translation(value: str) -> str:
    text = str(value or "").strip()
    text = re.sub(r"^```(?:json|text|markdown)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```$", "", text)
    text = re.sub(r"^\s*(?:中文标题|译名|翻译|title_zh|zh)\s*[:：]\s*", "", text, flags=re.IGNORECASE)
    text = text.strip().strip("\"'“”‘’`")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def parse_deepseek_response(response: requests.Response, label: str) -> str:
    try:
        data = response.json()
    except Exception as exc:
        raise RuntimeError(f"{label}: HTTP {response.status_code}, non-json response: {response.text[:500]}") from exc
    if response.status_code >= 400:
        raise RuntimeError(f"{label}: HTTP {response.status_code}, response={json.dumps(data, ensure_ascii=False)[:800]}")
    try:
        return str(data["choices"][0]["message"]["content"])
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError(f"{label}: unexpected DeepSeek response: {json.dumps(data, ensure_ascii=False)[:800]}") from exc


def translate_title(title: str, args: argparse.Namespace) -> str:
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise RuntimeError("Missing DEEPSEEK_API_KEY")

    payload: dict[str, Any] = {
        "model": args.model,
        "temperature": 0,
        "max_tokens": 220,
        "messages": [
            {
                "role": "system",
                "content": (
                    "你是金融研报标题翻译编辑。将英文研报标题翻译成简体中文，"
                    "保留机构名、公司名、股票代码、评级、日期、货币、数字和专有名词；"
                    "只输出标题本身，不解释，不加引号。"
                ),
            },
            {
                "role": "user",
                "content": f"请翻译这个金融研报标题：\n{title}",
            },
        ],
    }

    last_error: Exception | None = None
    for attempt in range(1, args.retries + 1):
        try:
            response = requests.post(
                args.deepseek_base_url.rstrip("/") + "/chat/completions",
                headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
                json=payload,
                timeout=args.timeout,
            )
            translated = normalize_translation(parse_deepseek_response(response, title[:80]))
            if not translated:
                raise RuntimeError("DeepSeek returned an empty translation")
            return translated
        except Exception as exc:  # noqa: BLE001 - retry transient HTTP/network/model errors.
            last_error = exc
            if attempt >= args.retries:
                break
            time.sleep(min(2 ** (attempt - 1), 8))
    raise RuntimeError(str(last_error) if last_error else "Unknown DeepSeek error")


def candidate_items(catalog: dict[str, Any], force: bool, limit: int) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for item in catalog.get("items", []):
        if not isinstance(item, dict):
            continue
        title = str(item.get("title") or "").strip()
        if not title:
            continue
        current = str(item.get("title_zh") or "").strip()
        if current and not force:
            continue
        rows.append(item)
        if limit > 0 and len(rows) >= limit:
            break
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog-path", default="kc_desk_notes/data/catalog.json")
    parser.add_argument("--model", default=os.getenv("DEEPSEEK_MODEL", "deepseek-chat"))
    parser.add_argument("--deepseek-base-url", default=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    parser.add_argument("--workers", type=int, default=int(os.getenv("DEEPSEEK_TITLE_WORKERS", "500")))
    parser.add_argument("--timeout", type=int, default=45)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--limit", type=int, default=0, help="Translate at most this many missing titles. 0 means all.")
    parser.add_argument("--force", action="store_true", help="Retranslate titles that already have title_zh.")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--fail-on-error", action="store_true")
    args = parser.parse_args()

    catalog_path = Path(args.catalog_path)
    catalog = load_json(catalog_path, {"schema_version": 1, "items": []})
    items = candidate_items(catalog, args.force, args.limit)
    if not items:
        log("No KC Desk Notes titles need translation.")
        return 0

    if not os.getenv("DEEPSEEK_API_KEY"):
        log("DEEPSEEK_API_KEY is missing; skipping title translation.")
        return 0

    log(f"Translating {len(items)} KC Desk Notes titles with DeepSeek model={args.model}, workers={args.workers}")
    translated = 0
    failed = 0

    def work(item: dict[str, Any]) -> tuple[dict[str, Any], str, str]:
        title = str(item.get("title") or "").strip()
        if has_cjk(title) and not args.force:
            return item, title, ""
        return item, translate_title(title, args), ""

    max_workers = max(1, args.workers)
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(work, item): item for item in items}
        for index, future in enumerate(concurrent.futures.as_completed(futures), start=1):
            item = futures[future]
            report_id = str(item.get("id") or "")
            try:
                target_item, title_zh, _ = future.result()
                target_item["title_zh"] = title_zh
                translated += 1
            except Exception as exc:  # noqa: BLE001 - retry next scheduled run.
                failed += 1
                log(f"  [failed] {report_id}: {exc}")
            if index == len(items) or index % 50 == 0:
                log(f"  progress {index}/{len(items)} translated={translated} failed={failed}")

    catalog["title_translation"] = {
        "provider": "deepseek",
        "model": args.model,
        "updated_at_bjt": bjt_now(),
        "translated_title_count": sum(1 for item in catalog.get("items", []) if str(item.get("title_zh") or "").strip()),
        "last_run_translated": translated,
        "last_run_failed": failed,
    }

    if args.dry_run:
        log("Dry run; catalog not written.")
    else:
        write_json(catalog_path, catalog)
        log(f"Wrote {catalog_path}: translated={translated}, failed={failed}")

    if failed and args.fail_on_error:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
