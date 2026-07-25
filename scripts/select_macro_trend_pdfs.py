#!/usr/bin/env python3
"""Select PDFs from a downloaded Dropbox manifest.

Input: a folder produced by download_dropbox_latest_pdfs.py that contains
`dropbox_manifest.json` and downloaded PDF files.

Output:
- selected_macro_candidates.json: up to --candidate-count selected candidates.
- selected_to_process_manifest.json: the first --process-count candidates copied for processing.
- selected PDFs copied into --output-dir.

Classification is primarily done by DeepSeek from filenames/titles, and can be
used either as metadata for all reports or as a legacy macro/trend filter. If
DeepSeek fails or returns invalid JSON, a conservative filename heuristic is used.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from pathlib import Path
from typing import Any

import requests

from deepseek_http import deepseek_api_keys_from_env, request_with_key_fallback

MACRO_HINTS = [
    "macro", "strategy", "outlook", "market", "markets", "economy", "economic", "global", "regional",
    "sector", "industry", "theme", "themes", "trend", "trends", "supply chain", "oil price", "energy",
    "semiconductor", "ai supply", "hardware", "housing", "property", "rates", "inflation", "policy",
    "china", "asia", "apac", "europe", "us", "tariff", "trade", "commodity", "commodities",
    "fx", "credit", "fund flows", "pmi", "cpi", "gdp", "fed", "central bank", "asset allocation",
    "cross asset", "weekly kickstart", "markets daily",
]
MACRO_PRIORITY_HINTS = [
    "macro", "economy", "economic", "economics", "global", "regional", "strategy", "markets daily",
    "weekly kickstart", "rates", "inflation", "policy", "fed", "central bank", "fx", "credit",
    "commodity", "commodities", "oil", "copper", "pmi", "cpi", "gdp", "tariff", "trade",
    "fund flows", "asset allocation", "cross asset",
]
COMPANY_HINTS = [
    " inc", " corp", " corporation", " ltd", " limited", " co.", " plc", "adr", "nasdaq", "nyse",
    ".us", ".hk", ".ss", ".sz", ".ks", ".t", "initiate", "initiation", "target price",
    "price target", "upgrade", "downgrade", "overweight", "underweight", "earnings review",
    "conference call", "ndr", "roadshow", "results review", "estimate change", "valuation",
]
TICKER_RE = re.compile(
    r"(?:\([A-Z0-9]{1,8}(?:\.[A-Z]{1,4})\)|\b\d{4,6}\.(?:HK|SZ|SS|TW|T|KS)\b|\b[A-Z]{1,6}\.(?:US|HK|AS|MI)\b)",
    re.I,
)
RATING_ACTION_RE = re.compile(
    r"\b(?:overweight|underweight|upgrade|downgrade|initiat(?:e|ion)|target price|price target)\b",
    re.I,
)


def log(message: str) -> None:
    print(message, flush=True)


def write_github_output(key: str, value: str) -> None:
    output_path = os.getenv("GITHUB_OUTPUT")
    if not output_path:
        return
    with open(output_path, "a", encoding="utf-8") as f:
        f.write(f"{key}={str(value).replace(chr(10), ' ')}\n")


def sanitize_filename(name: str, fallback: str) -> str:
    name = Path(name).name.strip() or Path(fallback).name.strip() or "report.pdf"
    name = re.sub(r"[\\/:*?\"<>|]+", "-", name)
    name = re.sub(r"\s+", " ", name).strip()

    # Reserve room for the extension before truncating. Truncating the complete
    # name used to turn long PDFs into a trailing `.p`, so downstream *.pdf
    # discovery silently omitted the report.
    stem = name[:-4] if name.lower().endswith(".pdf") else name
    stem = stem.rstrip(" .-") or Path(fallback).stem.rstrip(" .-") or "report"
    max_stem_bytes = 180 - len(".pdf")
    encoded = stem.encode("utf-8")
    if len(encoded) > max_stem_bytes:
        stem = encoded[:max_stem_bytes].decode("utf-8", errors="ignore").rstrip(" .-")
    return f"{stem or 'report'}.pdf"


def load_manifest(input_dir: Path) -> list[dict[str, Any]]:
    manifest_path = input_dir / "dropbox_manifest.json"
    if not manifest_path.exists():
        raise RuntimeError(f"Missing manifest: {manifest_path}")
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    files = data.get("files", [])
    pdfs = []
    for idx, row in enumerate(files):
        raw_local_path = Path(row.get("local_path", ""))
        path_candidates = [raw_local_path] if raw_local_path.is_absolute() else [Path.cwd() / raw_local_path, input_dir / raw_local_path]
        if not raw_local_path.is_absolute() and raw_local_path.parts and raw_local_path.parts[0] == input_dir.name:
            path_candidates.append(input_dir / Path(*raw_local_path.parts[1:]))
        local_path = next((path for path in path_candidates if path.exists()), path_candidates[0])
        if local_path.exists() and local_path.suffix.lower() == ".pdf":
            pdfs.append({
                "id": idx,
                "name": row.get("name") or local_path.name,
                "dropbox_path": row.get("dropbox_path", ""),
                "local_path": str(local_path),
            })
    if not pdfs:
        # Fallback: scan local folder.
        for idx, path in enumerate(sorted(input_dir.rglob("*.pdf"))):
            pdfs.append({"id": idx, "name": path.name, "dropbox_path": "", "local_path": str(path)})
    if not pdfs:
        raise RuntimeError(f"No PDFs found in {input_dir}")
    return pdfs


def extract_json(text: str) -> Any:
    text = text.strip()
    try:
        return json.loads(text)
    except Exception:
        pass
    match = re.search(r"(\[.*\]|\{.*\})", text, flags=re.S)
    if not match:
        raise ValueError("No JSON found in DeepSeek response")
    return json.loads(match.group(1))


def call_deepseek(prompt: str, model: str, base_url: str) -> str:
    api_keys = deepseek_api_keys_from_env()
    if not api_keys:
        raise RuntimeError("Missing DEEPSEEK_API_KEY")
    response = request_with_key_fallback(
        base_url.rstrip("/") + "/chat/completions",
        headers={"Content-Type": "application/json"},
        payload={
            "model": model,
            "temperature": 0.15,
            "messages": [
                {"role": "system", "content": "你是严谨的研报标题分类器，只输出 JSON。"},
                {"role": "user", "content": prompt},
            ],
        },
        label="report classification",
        api_keys=api_keys,
        timeout=180,
    )
    if response.status_code >= 400:
        raise RuntimeError(f"DeepSeek classification failed: HTTP {response.status_code}, {response.text[:500]}")
    data = response.json()
    return data["choices"][0]["message"]["content"]


def classify_with_deepseek(pdfs: list[dict[str, Any]], args: argparse.Namespace) -> list[dict[str, Any]]:
    payload = [{"id": p["id"], "title": p["name"], "path": p.get("dropbox_path", "")} for p in pdfs]
    prompt = f"""
请根据研报 PDF 文件名/路径判断它更像哪类报告，并选出宏观趋势类候选。

分类口径：
- macro_trend：优先选择宏观、策略、区域/国家市场、利率/汇率/信用/商品、政策、周期、资产配置、行业供需趋势、产业链主题。
- company_stock：单一上市公司、个股评级、目标价、单公司财报/估值/首次覆盖、公司路演/电话会/业绩点评。
- other：不确定、资料说明、非研报。

注意：
- 只根据标题判断，不要编造。
- 严格规避个股：如果标题明显是单一公司、含股票代码、评级动作、目标价、财报/业绩点评，即使涉及行业，也归为 company_stock。
- 如果标题是行业/产业链/市场整体，不针对单一公司，归为 macro_trend。
- 宏观/跨资产/政策/利率/汇率/商品/区域市场报告优先给更高 score。
- 返回 JSON 数组，不要解释。
- 每项格式：{{"id": 0, "category": "macro_trend", "score": 0.95, "reason": "简短中文原因"}}
- score 表示你对该分类的置信度，0-1。

PDF 列表：
{json.dumps(payload, ensure_ascii=False, indent=2)}
""".strip()
    raw = call_deepseek(prompt, args.model, args.deepseek_base_url)
    data = extract_json(raw)
    if isinstance(data, dict):
        data = data.get("items", []) or data.get("results", [])
    if not isinstance(data, list):
        raise ValueError("DeepSeek classification JSON is not a list")
    by_id = {int(item.get("id")): item for item in data if isinstance(item, dict) and str(item.get("id", "")).isdigit()}
    rows = []
    for p in pdfs:
        item = by_id.get(int(p["id"]), {})
        rows.append({
            **p,
            "category": item.get("category", "other"),
            "score": float(item.get("score", 0) or 0),
            "reason": item.get("reason", ""),
            "classifier": "deepseek",
        })
    return rows


def title_blob(row: dict[str, Any]) -> str:
    return f"{row.get('name', '')} {row.get('dropbox_path', '')}".lower().replace("_", " ").replace("-", " ")


def score_hints(text: str, hints: list[str]) -> int:
    return sum(1 for hint in hints if hint in text)


def company_guard_reasons(text: str) -> list[str]:
    reasons: list[str] = []
    if TICKER_RE.search(text):
        reasons.append("contains_ticker")
    if RATING_ACTION_RE.search(text):
        reasons.append("contains_rating_or_target_price")
    company_score = score_hints(text, COMPANY_HINTS)
    macro_priority_score = score_hints(text, MACRO_PRIORITY_HINTS)
    if company_score >= 2 or (company_score and not macro_priority_score):
        reasons.append(f"company_hint_score={company_score}")
    return reasons


def apply_macro_preference_guard(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    guarded = []
    for row in rows:
        text = title_blob(row)
        company_reasons = company_guard_reasons(text)
        macro_priority_score = score_hints(text, MACRO_PRIORITY_HINTS)
        macro_score = score_hints(text, MACRO_HINTS)
        updated = dict(row)
        updated["macro_hint_score"] = macro_score
        updated["macro_priority_score"] = macro_priority_score
        updated["company_guard_reasons"] = company_reasons
        if company_reasons:
            updated["category"] = "company_stock"
            updated["score"] = max(float(updated.get("score", 0) or 0), 0.9)
            base_reason = str(updated.get("reason") or "").strip()
            guard_reason = "本地规则排除个股/评级/目标价/财报信号：" + ",".join(company_reasons)
            updated["reason"] = f"{base_reason}；{guard_reason}" if base_reason else guard_reason
            updated["classifier"] = f"{updated.get('classifier', 'unknown')}+local_guard"
        elif str(updated.get("category")) == "macro_trend" and macro_priority_score:
            updated["score"] = min(0.99, float(updated.get("score", 0) or 0) + macro_priority_score * 0.03)
            updated["reason"] = (str(updated.get("reason") or "").strip() + "；宏观优先信号加权").strip("；")
            updated["classifier"] = f"{updated.get('classifier', 'unknown')}+macro_priority"
        guarded.append(updated)
    return guarded


def classify_with_heuristic(pdfs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows = []
    for p in pdfs:
        title = title_blob(p)
        macro_score = score_hints(title, MACRO_HINTS)
        macro_priority_score = score_hints(title, MACRO_PRIORITY_HINTS)
        company_reasons = company_guard_reasons(title)
        if company_reasons:
            category = "company_stock"
            score = 0.9
            reason = "文件名包含公司/个股/评级/目标价/财报信号：" + ",".join(company_reasons)
        elif macro_score > 0:
            category = "macro_trend"
            score = min(0.9, 0.45 + macro_score * 0.08 + macro_priority_score * 0.05)
            reason = "文件名包含宏观/行业/趋势关键词"
        else:
            category = "other"
            score = 0.3
            reason = "启发式规则无法确认"
        rows.append({
            **p,
            "category": category,
            "score": score,
            "reason": reason,
            "classifier": "heuristic",
            "macro_hint_score": macro_score,
            "macro_priority_score": macro_priority_score,
            "company_guard_reasons": company_reasons,
        })
    return rows


def select_candidates(classified: list[dict[str, Any]], candidate_count: int, selection_mode: str) -> list[dict[str, Any]]:
    if selection_mode == "all":
        return classified[:candidate_count]

    macro = [r for r in classified if str(r.get("category")) == "macro_trend"]
    macro.sort(
        key=lambda r: (
            int(r.get("macro_priority_score", 0) or 0),
            int(r.get("macro_hint_score", 0) or 0),
            float(r.get("score", 0) or 0),
        ),
        reverse=True,
    )
    return macro[:candidate_count]


def copy_selected(selected: list[dict[str, Any]], output_dir: Path, process_count: int) -> list[dict[str, Any]]:
    output_dir.mkdir(parents=True, exist_ok=True)
    to_process = selected[:process_count]
    copied = []
    for idx, row in enumerate(to_process, 1):
        source = Path(row["local_path"])
        target = output_dir / f"{idx:02d}-{sanitize_filename(row['name'], f'report-{idx}.pdf')}"
        shutil.copy2(source, target)
        copied.append({**row, "process_rank": idx, "process_local_path": str(target)})
    return copied


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--candidate-count", type=int, default=10)
    parser.add_argument("--process-count", type=int, default=5)
    parser.add_argument(
        "--selection-mode",
        choices=["all", "macro"],
        default=os.getenv("REPORT_SELECTION_MODE", "all"),
        help="all keeps every downloaded PDF; macro keeps only macro/trend reports.",
    )
    parser.add_argument("--model", default=os.getenv("DEEPSEEK_MODEL", "deepseek-v4-flash"))
    parser.add_argument("--deepseek-base-url", default=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    args = parser.parse_args()

    input_dir = Path(args.input_dir).resolve()
    output_dir = Path(args.output_dir).resolve()
    try:
        pdfs = load_manifest(input_dir)
        log(f"Loaded {len(pdfs)} PDFs for classification.")
        try:
            classified = classify_with_deepseek(pdfs, args)
            classified = apply_macro_preference_guard(classified)
            log("DeepSeek classification completed.")
        except Exception as exc:
            log(f"DeepSeek classification failed, using heuristic fallback: {exc}")
            classified = classify_with_heuristic(pdfs)

        candidates = select_candidates(classified, max(1, args.candidate_count), args.selection_mode)
        copied = copy_selected(candidates, output_dir, max(1, args.process_count))

        classification_path = output_dir / "macro_classification_all.json"
        candidates_path = output_dir / "selected_macro_candidates.json"
        process_path = output_dir / "selected_to_process_manifest.json"
        classification_path.write_text(json.dumps(classified, ensure_ascii=False, indent=2), encoding="utf-8")
        candidates_path.write_text(json.dumps(candidates, ensure_ascii=False, indent=2), encoding="utf-8")
        process_path.write_text(json.dumps(copied, ensure_ascii=False, indent=2), encoding="utf-8")

        write_github_output("candidate_count", str(len(candidates)))
        write_github_output("process_count", str(len(copied)))
        write_github_output("selected_input_dir", str(output_dir))
        label = "all report candidates" if args.selection_mode == "all" else "macro candidates"
        log(f"Selection mode={args.selection_mode}; selected {len(candidates)} {label}; copied {len(copied)} PDFs for processing to {output_dir}")
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
