#!/usr/bin/env python3
"""Select macro/industry-trend PDFs from a downloaded Dropbox manifest.

Input: a folder produced by download_dropbox_latest_pdfs.py that contains
`dropbox_manifest.json` and downloaded PDF files.

Output:
- selected_macro_candidates.json: up to --candidate-count macro/trend candidates.
- selected_to_process_manifest.json: the first --process-count candidates copied for processing.
- selected PDFs copied into --output-dir.

Classification is primarily done by DeepSeek from filenames/titles. If DeepSeek
fails or returns invalid JSON, a conservative filename heuristic is used.
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

MACRO_HINTS = [
    "macro", "strategy", "outlook", "market", "markets", "economy", "economic", "global", "regional",
    "sector", "industry", "theme", "themes", "trend", "trends", "supply chain", "oil price", "energy",
    "semiconductor", "ai supply", "hardware", "housing", "property", "rates", "inflation", "policy",
    "china", "asia", "apac", "europe", "us", "tariff", "trade", "commodity", "commodities",
]
COMPANY_HINTS = [
    " inc", " corp", " corporation", " ltd", " limited", " group", " co.", " plc", "adr", "nasdaq", "nyse",
    ".us", ".hk", ".ss", ".sz", ".ks", ".t", "earnings", "initiate", "initiation", "rating", "target price",
]


def log(message: str) -> None:
    print(message, flush=True)


def write_github_output(key: str, value: str) -> None:
    output_path = os.getenv("GITHUB_OUTPUT")
    if not output_path:
        return
    with open(output_path, "a", encoding="utf-8") as f:
        f.write(f"{key}={str(value).replace(chr(10), ' ')}\n")


def sanitize_filename(name: str, fallback: str) -> str:
    name = Path(name).name.strip() or fallback
    name = re.sub(r"[\\/:*?\"<>|]+", "-", name)
    name = re.sub(r"\s+", " ", name).strip()
    if not name.lower().endswith(".pdf"):
        name += ".pdf"
    return name[:180]


def load_manifest(input_dir: Path) -> list[dict[str, Any]]:
    manifest_path = input_dir / "dropbox_manifest.json"
    if not manifest_path.exists():
        raise RuntimeError(f"Missing manifest: {manifest_path}")
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    files = data.get("files", [])
    pdfs = []
    for idx, row in enumerate(files):
        local_path = Path(row.get("local_path", ""))
        if not local_path.is_absolute():
            local_path = input_dir / local_path
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
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise RuntimeError("Missing DEEPSEEK_API_KEY")
    response = requests.post(
        base_url.rstrip("/") + "/chat/completions",
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
        json={
            "model": model,
            "temperature": 0.15,
            "messages": [
                {"role": "system", "content": "你是严谨的研报标题分类器，只输出 JSON。"},
                {"role": "user", "content": prompt},
            ],
        },
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
- macro_trend：宏观、行业趋势、产业链、主题策略、区域/国家市场、商品/利率/政策/周期/资产配置/行业供需趋势。
- company_stock：单一上市公司、个股评级、目标价、单公司财报/估值/首次覆盖。
- other：不确定、资料说明、非研报。

注意：
- 只根据标题判断，不要编造。
- 如果标题明显是单一公司，即使涉及行业，也归为 company_stock。
- 如果标题是行业/产业链/市场整体，不针对单一公司，归为 macro_trend。
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


def classify_with_heuristic(pdfs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows = []
    for p in pdfs:
        title = str(p["name"]).lower()
        macro_score = sum(1 for h in MACRO_HINTS if h in title)
        company_score = sum(1 for h in COMPANY_HINTS if h in title)
        if macro_score > company_score and macro_score > 0:
            category = "macro_trend"
            score = min(0.85, 0.45 + macro_score * 0.1)
            reason = "文件名包含宏观/行业/趋势关键词"
        elif company_score > 0:
            category = "company_stock"
            score = min(0.85, 0.45 + company_score * 0.1)
            reason = "文件名包含公司/个股关键词"
        else:
            category = "other"
            score = 0.3
            reason = "启发式规则无法确认"
        rows.append({**p, "category": category, "score": score, "reason": reason, "classifier": "heuristic"})
    return rows


def select_candidates(classified: list[dict[str, Any]], candidate_count: int) -> list[dict[str, Any]]:
    macro = [r for r in classified if str(r.get("category")) == "macro_trend"]
    macro.sort(key=lambda r: float(r.get("score", 0)), reverse=True)
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
    parser.add_argument("--model", default=os.getenv("DEEPSEEK_MODEL", "deepseek-chat"))
    parser.add_argument("--deepseek-base-url", default=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    args = parser.parse_args()

    input_dir = Path(args.input_dir).resolve()
    output_dir = Path(args.output_dir).resolve()
    try:
        pdfs = load_manifest(input_dir)
        log(f"Loaded {len(pdfs)} PDFs for macro classification.")
        try:
            classified = classify_with_deepseek(pdfs, args)
            log("DeepSeek classification completed.")
        except Exception as exc:
            log(f"DeepSeek classification failed, using heuristic fallback: {exc}")
            classified = classify_with_heuristic(pdfs)

        candidates = select_candidates(classified, max(1, args.candidate_count))
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
        log(f"Selected {len(candidates)} macro candidates; copied {len(copied)} PDFs for processing to {output_dir}")
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
