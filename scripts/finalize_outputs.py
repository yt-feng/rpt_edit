#!/usr/bin/env python3
"""Finalize generated report outputs.

Responsibilities:
1. Sanitize investment-bank brand names in all generated text outputs.
2. Generate Xianyu listing copy from sanitized MinerU markdown.

Rule:
- Known banks are replaced with canonical abbreviations such as GS, JPM, MS, BofA.
- Unknown or generic bank references can remain as 投行 / 外资投行.
"""
from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Any

import requests

TEXT_SUFFIXES = {".md", ".txt", ".json", ".srt", ".vtt"}

# Centralized brand-abbreviation table.
# Keep longer / more specific aliases before shorter aliases.
# This intentionally targets final text outputs only. Original source images may still contain visible logos.
BRAND_PATTERNS: list[tuple[str, str]] = [
    # Bulge bracket / global banks
    (r"Goldman\s+Sachs\s+Research", "GS"),
    (r"Goldman\s+Sachs", "GS"),
    (r"高盛研究", "GS"),
    (r"高盛", "GS"),
    (r"J\.\s*P\.\s*Morgan\s+Research", "JPM"),
    (r"J\.\s*P\.\s*Morgan", "JPM"),
    (r"JP\s*Morgan", "JPM"),
    (r"JPMorgan\s+Chase", "JPM"),
    (r"JPMorgan", "JPM"),
    (r"摩根大通研究", "JPM"),
    (r"摩根大通", "JPM"),
    (r"Morgan\s+Stanley\s+Research", "MS"),
    (r"Morgan\s+Stanley", "MS"),
    (r"摩根士丹利研究", "MS"),
    (r"摩根士丹利", "MS"),
    (r"大摩", "MS"),
    (r"Bank\s+of\s+America\s+Merrill\s+Lynch", "BofA"),
    (r"BofA\s+Merrill\s+Lynch", "BofA"),
    (r"BofA\s+Securities", "BofA"),
    (r"Bank\s+of\s+America", "BofA"),
    (r"Merrill\s+Lynch", "BofA"),
    (r"美银美林", "BofA"),
    (r"美国银行证券", "BofA"),
    (r"美银证券", "BofA"),
    (r"美林证券", "BofA"),
    (r"美银", "BofA"),
    (r"Citigroup\s+Research", "Citi"),
    (r"Citi\s+Research", "Citi"),
    (r"Citigroup", "Citi"),
    (r"Citi", "Citi"),
    (r"花旗研究", "Citi"),
    (r"花旗银行", "Citi"),
    (r"花旗", "Citi"),
    (r"UBS\s+Securities", "UBS"),
    (r"UBS\s+Research", "UBS"),
    (r"UBS", "UBS"),
    (r"瑞银证券", "UBS"),
    (r"瑞银", "UBS"),
    (r"Deutsche\s+Bank\s+Research", "DB"),
    (r"Deutsche\s+Bank", "DB"),
    (r"德意志银行研究", "DB"),
    (r"德意志银行", "DB"),
    (r"德银", "DB"),
    (r"HSBC\s+Global\s+Research", "HSBC"),
    (r"HSBC\s+Research", "HSBC"),
    (r"HSBC", "HSBC"),
    (r"汇丰环球研究", "HSBC"),
    (r"汇丰研究", "HSBC"),
    (r"汇丰", "HSBC"),
    (r"Barclays\s+Research", "BARC"),
    (r"Barclays", "BARC"),
    (r"巴克莱研究", "BARC"),
    (r"巴克莱", "BARC"),
    (r"BNP\s+Paribas\s+Exane", "BNPP"),
    (r"BNP\s+Paribas", "BNPP"),
    (r"巴黎银行研究", "BNPP"),
    (r"法国巴黎银行", "BNPP"),
    (r"法巴", "BNPP"),
    (r"Societe\s+Generale", "SG"),
    (r"Société\s+Générale", "SG"),
    (r"SG\s+Research", "SG"),
    (r"法兴银行", "SG"),
    (r"法兴", "SG"),
    (r"Credit\s+Suisse\s+Research", "CS"),
    (r"Credit\s+Suisse", "CS"),
    (r"瑞信研究", "CS"),
    (r"瑞士信贷", "CS"),
    (r"瑞信", "CS"),

    # Japan / Asia-Pacific / regional banks and brokers
    (r"Nomura\s+Research", "NOM"),
    (r"Nomura", "NOM"),
    (r"野村证券", "NOM"),
    (r"野村", "NOM"),
    (r"Daiwa\s+Securities", "Daiwa"),
    (r"Daiwa", "Daiwa"),
    (r"大和证券", "Daiwa"),
    (r"大和", "Daiwa"),
    (r"Mizuho\s+Securities", "Mizuho"),
    (r"Mizuho", "Mizuho"),
    (r"瑞穗证券", "Mizuho"),
    (r"瑞穗", "Mizuho"),
    (r"SMBC\s+Nikko", "SMBC"),
    (r"SMBC", "SMBC"),
    (r"三井住友", "SMBC"),
    (r"Macquarie\s+Research", "MQ"),
    (r"Macquarie", "MQ"),
    (r"麦格理研究", "MQ"),
    (r"麦格理", "MQ"),
    (r"CLSA", "CLSA"),
    (r"里昂证券", "CLSA"),
    (r"里昂", "CLSA"),
    (r"CICC", "CICC"),
    (r"中金公司", "CICC"),
    (r"中金", "CICC"),
    (r"CITIC\s+Securities", "CITIC"),
    (r"中信证券", "CITIC"),
    (r"中信建投证券", "CSC"),
    (r"China\s+Merchants\s+Securities", "CMS"),
    (r"招商证券", "CMS"),
    (r"Haitong\s+Securities", "Haitong"),
    (r"海通证券", "Haitong"),
    (r"Huatai\s+Securities", "HTSC"),
    (r"华泰证券", "HTSC"),
    (r"Guotai\s+Junan", "GTJA"),
    (r"国泰君安", "GTJA"),
    (r"Essence\s+Securities", "Essence"),
    (r"安信证券", "Essence"),
    (r"GF\s+Securities", "GF"),
    (r"广发证券", "GF"),
    (r"Orient\s+Securities", "Orient"),
    (r"东方证券", "Orient"),
    (r"Industrial\s+Securities", "Industrial"),
    (r"兴业证券", "Industrial"),

    # Independent / boutique / sector research brokers
    (r"Jefferies\s+Research", "JEF"),
    (r"Jefferies", "JEF"),
    (r"杰富瑞研究", "JEF"),
    (r"杰富瑞", "JEF"),
    (r"Bernstein\s+Research", "Bernstein"),
    (r"Sanford\s+C\.\s+Bernstein", "Bernstein"),
    (r"Bernstein", "Bernstein"),
    (r"伯恩斯坦", "Bernstein"),
    (r"Evercore\s+ISI", "Evercore"),
    (r"Evercore", "Evercore"),
    (r"Guggenheim\s+Securities", "Guggenheim"),
    (r"Guggenheim", "Guggenheim"),
    (r"Piper\s+Sandler", "Piper"),
    (r"Piper\s+Jaffray", "Piper"),
    (r"Raymond\s+James", "RJ"),
    (r"RBC\s+Capital\s+Markets", "RBC"),
    (r"RBC", "RBC"),
    (r"加拿大皇家银行", "RBC"),
    (r"TD\s+Cowen", "TD Cowen"),
    (r"Cowen", "Cowen"),
    (r"Stifel", "Stifel"),
    (r"William\s+Blair", "William Blair"),
    (r"Wolfe\s+Research", "Wolfe"),
    (r"Needham", "Needham"),
    (r"Oppenheimer", "Oppenheimer"),
    (r"KeyBanc", "KeyBanc"),
    (r"Melius\s+Research", "Melius"),
    (r"Redburn\s+Atlantic", "Redburn"),
    (r"Arete\s+Research", "Arete"),
    (r"Morningstar", "Morningstar"),
    (r"晨星", "Morningstar"),
]

# Extra generic direct-brand fallback for long institution descriptions that are not in the table.
GENERIC_BANK_PHRASES: list[tuple[str, str]] = [
    (r"某(?:全球|国际|外资)?(?:投行|券商|证券公司)研报", "投行研报"),
    (r"(?:全球|国际|外资)(?:投行|券商|证券公司)研报", "投行研报"),
]


def log(message: str) -> None:
    print(message, flush=True)


def sanitize_text(text: str) -> str:
    for pattern, replacement in BRAND_PATTERNS:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    for pattern, replacement in GENERIC_BANK_PHRASES:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    # Normalize common over-explicit phrasing after replacement.
    text = re.sub(r"GS\s*\((?:Goldman\s+Sachs|高盛)\)", "GS", text, flags=re.IGNORECASE)
    text = re.sub(r"JPM\s*\((?:J\.?P\.?\s*Morgan|摩根大通)\)", "JPM", text, flags=re.IGNORECASE)
    text = re.sub(r"MS\s*\((?:Morgan\s+Stanley|摩根士丹利|大摩)\)", "MS", text, flags=re.IGNORECASE)
    text = re.sub(r"BofA\s*\((?:Bank\s+of\s+America|美银|美银证券)\)", "BofA", text, flags=re.IGNORECASE)
    return text


def sanitize_file(path: Path) -> bool:
    try:
        original = path.read_text(encoding="utf-8", errors="ignore")
    except Exception as exc:
        log(f"Skip unreadable text file {path}: {exc}")
        return False
    sanitized = sanitize_text(original)
    if sanitized != original:
        path.write_text(sanitized, encoding="utf-8")
        return True
    return False


def sanitize_output_dir(output_dir: Path) -> int:
    count = 0
    if not output_dir.exists():
        return count
    for path in output_dir.rglob("*"):
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            if sanitize_file(path):
                count += 1
    return count


def parse_json_response(response: requests.Response, label: str) -> dict[str, Any]:
    try:
        data = response.json()
    except Exception as exc:
        raise RuntimeError(f"{label}: HTTP {response.status_code}, non-json response: {response.text[:500]}") from exc
    code = data.get("code")
    if response.status_code >= 400 or code not in (None, 0, "0"):
        raise RuntimeError(f"{label}: HTTP {response.status_code}, response={json.dumps(data, ensure_ascii=False)[:1000]}")
    return data


def call_deepseek(prompt: str, args: argparse.Namespace, label: str) -> str:
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        return f"未检测到 DEEPSEEK_API_KEY。请复制 prompt_for_xianyu.md 手动生成：{label}\n"
    url = args.deepseek_base_url.rstrip("/") + "/chat/completions"
    payload = {
        "model": args.model,
        "temperature": 0.68,
        "messages": [
            {"role": "system", "content": "你是资料类商品文案编辑。最终输出必须对投行品牌脱敏：常见投行使用 GS、JPM、MS、BofA、Citi、UBS、DB 等缩写；不确定时用投行或外资投行泛称。"},
            {"role": "user", "content": prompt},
        ],
    }
    response = requests.post(
        url,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
        json=payload,
        timeout=180,
    )
    data = parse_json_response(response, f"DeepSeek generate {label}")
    return sanitize_text(data["choices"][0]["message"]["content"].strip() + "\n")


def trim_source_text(source_text: str, max_chars: int) -> str:
    source_text = sanitize_text(re.sub(r"\n{3,}", "\n\n", source_text).strip())
    if len(source_text) > max_chars:
        head_len = int(max_chars * 0.72)
        tail_len = int(max_chars * 0.22)
        source_text = source_text[:head_len] + "\n\n[中间内容因长度限制已省略]\n\n" + source_text[-tail_len:]
    return source_text


def generate_xianyu_for_item(item_dir: Path, args: argparse.Namespace) -> dict[str, str]:
    source_path = item_dir / "source_mineru.md"
    prompt_template_path = Path(args.xianyu_prompt_template)
    status: dict[str, str] = {}
    if not source_path.exists():
        status["xianyu_error"] = "source_mineru.md not found"
        return status
    if not prompt_template_path.exists():
        status["xianyu_error"] = f"prompt template not found: {prompt_template_path}"
        return status

    source_text = trim_source_text(source_path.read_text(encoding="utf-8", errors="ignore"), args.xianyu_prompt_chars)
    prompt = prompt_template_path.read_text(encoding="utf-8").format(source_text=source_text)
    prompt = sanitize_text(prompt)
    (item_dir / "prompt_for_xianyu.md").write_text(prompt, encoding="utf-8")
    try:
        note = call_deepseek(prompt, args, "Xianyu listing note")
    except Exception as exc:
        note = f"DeepSeek 生成闲鱼文案失败：{exc}\n\n请复制 prompt_for_xianyu.md 手动生成。\n"
        status["xianyu_error"] = str(exc)
    (item_dir / "xianyu_note.md").write_text(sanitize_text(note), encoding="utf-8")
    status["xianyu_note"] = "xianyu_note.md"
    status["prompt_for_xianyu"] = "prompt_for_xianyu.md"
    return status


def update_item_status(item_dir: Path, update: dict[str, Any]) -> None:
    status_path = item_dir / "status.json"
    status: dict[str, Any] = {}
    if status_path.exists():
        try:
            status = json.loads(status_path.read_text(encoding="utf-8", errors="ignore"))
        except Exception:
            status = {}
    status.update(update)
    status_path.write_text(sanitize_text(json.dumps(status, ensure_ascii=False, indent=2)), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="xhs_notes")
    parser.add_argument("--model", default=os.getenv("DEEPSEEK_MODEL", "deepseek-chat"))
    parser.add_argument("--deepseek-base-url", default=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    parser.add_argument("--generate-xianyu", default="true")
    parser.add_argument("--xianyu-prompt-template", default="prompts/xianyu_report_listing_prompt.md")
    parser.add_argument("--xianyu-prompt-chars", type=int, default=22000)
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    sanitized_before = sanitize_output_dir(output_dir)
    log(f"Sanitized {sanitized_before} generated text files before finalization.")

    summary: list[dict[str, Any]] = []
    if str(args.generate_xianyu).lower() in {"1", "true", "yes", "y", "on"}:
        for item_dir in sorted(p for p in output_dir.iterdir() if p.is_dir()):
            log(f"Generating Xianyu note for {item_dir.name}")
            update = generate_xianyu_for_item(item_dir, args)
            update_item_status(item_dir, update)
            summary.append({"item": item_dir.name, **update})

    sanitized_after = sanitize_output_dir(output_dir)
    log(f"Sanitized {sanitized_after} generated text files after finalization.")
    (output_dir / "finalize_summary.json").write_text(sanitize_text(json.dumps(summary, ensure_ascii=False, indent=2)), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
