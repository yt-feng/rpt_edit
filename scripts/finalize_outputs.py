#!/usr/bin/env python3
"""Finalize generated report outputs.

Responsibilities:
1. Sanitize investment-bank brand names in generated text outputs.
2. Generate Xianyu listing copy.
3. Generate Zhihu-style article copy.
4. Normalize WeChat endings.
5. Run sensitive-content guard on public-facing notes.
"""
from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Any

import requests

from deepseek_http import deepseek_api_keys_from_env, request_with_key_fallback

try:
    from sensitive_content_guard import (
        build_arg_parser as build_sensitive_arg_parser,
        run_sensitive_guard,
        sanitize_wechat_stock_language,
    )
except Exception:
    run_sensitive_guard = None
    build_sensitive_arg_parser = None
    def sanitize_wechat_stock_language(text: str) -> tuple[str, list[str]]:
        return text, []

TEXT_SUFFIXES = {".md", ".txt", ".json", ".srt", ".vtt"}
ZSXQ_IMAGE_MD = "![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)"
DISCLAIMER_TEXT = (
    "For informational purposes only. Portions may be generated, translated, summarized, or edited with "
    "AI assistance based on source materials and may contain omissions or errors. Please verify independently. "
    "This is not investment, legal, tax, accounting, or other professional advice."
)
GRAY_DISCLAIMER = f'<p style="color:#999999;font-size:12px;">{DISCLAIMER_TEXT}</p>'
XIANYU_MAX_CHARS = 1499
EMOJI_RE = re.compile(
    "["
    "\U0001F000-\U0001FAFF"
    "\U00002700-\U000027BF"
    "\U00002600-\U000026FF"
    "\U0001F1E6-\U0001F1FF"
    "\U0001F3FB-\U0001F3FF"
    "\U0000FE0F"
    "\U0000200D"
    "]+",
    flags=re.UNICODE,
)

BRAND_PATTERNS: list[tuple[str, str]] = [
    (r"Goldman\s+Sachs\s+Research", "GS"), (r"Goldman\s+Sachs", "GS"), (r"高盛研究", "GS"), (r"高盛", "GS"),
    (r"J\.\s*P\.\s*Morgan\s+Research", "JPM"), (r"J\.\s*P\.\s*Morgan", "JPM"), (r"JP\s*Morgan", "JPM"), (r"JPMorgan\s+Chase", "JPM"), (r"JPMorgan", "JPM"), (r"摩根大通研究", "JPM"), (r"摩根大通", "JPM"),
    (r"Morgan\s+Stanley\s+Research", "MS"), (r"Morgan\s+Stanley", "MS"), (r"摩根士丹利研究", "MS"), (r"摩根士丹利", "MS"), (r"大摩", "MS"),
    (r"Bank\s+of\s+America\s+Merrill\s+Lynch", "BofA"), (r"BofA\s+Merrill\s+Lynch", "BofA"), (r"BofA\s+Securities", "BofA"), (r"Bank\s+of\s+America", "BofA"), (r"Merrill\s+Lynch", "BofA"), (r"美银美林", "BofA"), (r"美国银行证券", "BofA"), (r"美银证券", "BofA"), (r"美林证券", "BofA"), (r"美银", "BofA"),
    (r"Citigroup\s+Research", "Citi"), (r"Citi\s+Research", "Citi"), (r"Citigroup", "Citi"), (r"花旗研究", "Citi"), (r"花旗银行", "Citi"), (r"花旗", "Citi"),
    (r"UBS\s+Securities", "UBS"), (r"UBS\s+Research", "UBS"), (r"瑞银证券", "UBS"), (r"瑞银", "UBS"),
    (r"Deutsche\s+Bank\s+Research", "DB"), (r"Deutsche\s+Bank", "DB"), (r"德意志银行研究", "DB"), (r"德意志银行", "DB"), (r"德银", "DB"),
    (r"HSBC\s+Global\s+Research", "HSBC"), (r"HSBC\s+Research", "HSBC"), (r"汇丰环球研究", "HSBC"), (r"汇丰研究", "HSBC"), (r"汇丰", "HSBC"),
    (r"Barclays\s+Research", "BARC"), (r"Barclays", "BARC"), (r"巴克莱研究", "BARC"), (r"巴克莱", "BARC"),
    (r"BNP\s+Paribas\s+Exane", "BNPP"), (r"BNP\s+Paribas", "BNPP"), (r"法国巴黎银行", "BNPP"), (r"法巴", "BNPP"),
    (r"Societe\s+Generale", "SG"), (r"Société\s+Générale", "SG"), (r"法兴银行", "SG"), (r"法兴", "SG"),
    (r"Credit\s+Suisse\s+Research", "CS"), (r"Credit\s+Suisse", "CS"), (r"瑞士信贷", "CS"), (r"瑞信", "CS"),
    (r"Nomura\s+Research", "NOM"), (r"Nomura", "NOM"), (r"野村证券", "NOM"), (r"野村", "NOM"),
    (r"Daiwa\s+Securities", "Daiwa"), (r"大和证券", "Daiwa"), (r"大和", "Daiwa"),
    (r"Mizuho\s+Securities", "Mizuho"), (r"瑞穗证券", "Mizuho"), (r"瑞穗", "Mizuho"),
    (r"Macquarie\s+Research", "MQ"), (r"Macquarie", "MQ"), (r"麦格理研究", "MQ"), (r"麦格理", "MQ"),
    (r"CLSA", "CLSA"), (r"里昂证券", "CLSA"), (r"里昂", "CLSA"),
    (r"CICC", "CICC"), (r"中金公司", "CICC"), (r"中金", "CICC"),
    (r"CITIC\s+Securities", "CITIC"), (r"中信证券", "CITIC"), (r"中信建投证券", "CSC"),
    (r"China\s+Merchants\s+Securities", "CMS"), (r"招商证券", "CMS"),
    (r"Haitong\s+Securities", "Haitong"), (r"海通证券", "Haitong"),
    (r"Huatai\s+Securities", "HTSC"), (r"华泰证券", "HTSC"),
    (r"Guotai\s+Junan", "GTJA"), (r"国泰君安", "GTJA"),
    (r"Jefferies\s+Research", "JEF"), (r"Jefferies", "JEF"), (r"杰富瑞", "JEF"),
    (r"Bernstein\s+Research", "Bernstein"), (r"Sanford\s+C\.\s+Bernstein", "Bernstein"), (r"伯恩斯坦", "Bernstein"),
    (r"Evercore\s+ISI", "Evercore"), (r"Evercore", "Evercore"),
    (r"Guggenheim\s+Securities", "Guggenheim"), (r"Guggenheim", "Guggenheim"),
    (r"Piper\s+Sandler", "Piper"), (r"Raymond\s+James", "RJ"),
    (r"RBC\s+Capital\s+Markets", "RBC"), (r"加拿大皇家银行", "RBC"),
]

GENERIC_BANK_PHRASES: list[tuple[str, str]] = [
    (r"某(?:全球|国际|外资)?(?:投行|券商|证券公司)研报", "投行研报"),
    (r"(?:全球|国际|外资)(?:投行|券商|证券公司)研报", "投行研报"),
]

CHINESE_DISCLAIMER_PATTERNS = [
    r"\*?本文仅作学习交流[，,]不构成任何投资建议。?\*?",
    r"\*?本文仅供学习交流[，,]不构成任何投资建议。?\*?",
    r"\*?不构成任何投资建议。?\*?",
]


def log(message: str) -> None:
    print(message, flush=True)


def sanitize_text(text: str) -> str:
    text = str(text or "")
    for pattern, replacement in BRAND_PATTERNS:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    for pattern, replacement in GENERIC_BANK_PHRASES:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    text = re.sub(r"GS\s*\((?:Goldman\s+Sachs|高盛)\)", "GS", text, flags=re.IGNORECASE)
    text = re.sub(r"JPM\s*\((?:J\.?P\.?\s*Morgan|摩根大通)\)", "JPM", text, flags=re.IGNORECASE)
    text = re.sub(r"MS\s*\((?:Morgan\s+Stanley|摩根士丹利|大摩)\)", "MS", text, flags=re.IGNORECASE)
    text = re.sub(r"BofA\s*\((?:Bank\s+of\s+America|美银|美银证券)\)", "BofA", text, flags=re.IGNORECASE)
    return text


def remove_emoji(text: str) -> str:
    return EMOJI_RE.sub("", text or "")


def split_xianyu_hashtag_line(text: str) -> tuple[str, str]:
    lines = text.rstrip().splitlines()
    for index in range(len(lines) - 1, -1, -1):
        if re.match(r"\s*(?:Hashtag|hashtag|标签)\s*[:：]", lines[index].strip()):
            body = "\n".join(lines[:index]).rstrip()
            hashtag = lines[index].strip()
            return body, hashtag
    return text.rstrip(), ""


def truncate_xianyu_note(text: str, max_chars: int = XIANYU_MAX_CHARS) -> str:
    text = re.sub(r"\n{3,}", "\n\n", text.strip())
    if len(text) <= max_chars:
        return text

    body, hashtag = split_xianyu_hashtag_line(text)
    suffix = f"\n\n{hashtag}" if hashtag else ""
    budget = max_chars - len(suffix)
    if budget <= 80:
        return text[:max_chars].rstrip()

    truncated = body[:budget].rstrip()
    cut = max(truncated.rfind("\n"), truncated.rfind("。"), truncated.rfind("；"), truncated.rfind(";"))
    if cut >= int(budget * 0.72):
        truncated = truncated[: cut + 1].rstrip()
    return (truncated + suffix).strip()


def enforce_xianyu_constraints(text: str) -> str:
    text = remove_emoji(text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return truncate_xianyu_note(text, XIANYU_MAX_CHARS)


def enforce_xianyu_constraints_in_dir(output_dir: Path) -> int:
    changed = 0
    for path in output_dir.rglob("xianyu_note.md"):
        original = path.read_text(encoding="utf-8", errors="ignore")
        constrained = enforce_xianyu_constraints(original)
        if constrained != original:
            path.write_text(sanitize_text(constrained), encoding="utf-8")
            changed += 1
    return changed


def normalize_wechat_ending(text: str, include_zsxq: bool) -> str:
    text = sanitize_text(text).strip()
    text, _stock_changes = sanitize_wechat_stock_language(text)
    for pattern in CHINESE_DISCLAIMER_PATTERNS:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE).strip()
    text = re.sub(
        r'<p\s+style="color:#999999;font-size:12px;">[^<]*(?:not investment advice|investment, legal, tax, accounting)[^<]*</p>',
        "",
        text,
        flags=re.IGNORECASE,
    ).strip()
    text = text.replace(ZSXQ_IMAGE_MD, "").strip()
    parts = [text]
    if include_zsxq:
        parts.append(ZSXQ_IMAGE_MD)
    parts.append(GRAY_DISCLAIMER)
    return "\n\n".join(part for part in parts if part).strip() + "\n"


def normalize_wechat_articles(output_dir: Path) -> int:
    count = 0
    for path in output_dir.rglob("wechat_article.md"):
        try:
            path.write_text(normalize_wechat_ending(path.read_text(encoding="utf-8", errors="ignore"), include_zsxq=True), encoding="utf-8")
            count += 1
        except Exception as exc:
            log(f"Could not normalize {path}: {exc}")
    for path in output_dir.rglob("wechat_article_en.md"):
        try:
            path.write_text(normalize_wechat_ending(path.read_text(encoding="utf-8", errors="ignore"), include_zsxq=False), encoding="utf-8")
            count += 1
        except Exception as exc:
            log(f"Could not normalize {path}: {exc}")
    return count


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


def call_deepseek(prompt: str, args: argparse.Namespace, label: str, temperature: float = 0.62) -> str:
    api_keys = deepseek_api_keys_from_env()
    if not api_keys:
        return f"未检测到 DEEPSEEK_API_KEY。请复制对应 prompt 文件手动生成：{label}\n"
    response = request_with_key_fallback(
        args.deepseek_base_url.rstrip("/") + "/chat/completions",
        headers={"Content-Type": "application/json"},
        payload={
            "model": args.model,
            "temperature": temperature,
            "messages": [
                {"role": "system", "content": "你是资料类内容编辑。最终输出必须对投行品牌脱敏，并避免收益承诺、金融操作建议、极限词和直接互动诱导。"},
                {"role": "user", "content": prompt},
            ],
        },
        label=label,
        api_keys=api_keys,
        timeout=240,
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


def generate_from_template(item_dir: Path, args: argparse.Namespace, source_path: Path, template_path: Path, output_name: str, prompt_name: str, label: str, prompt_chars: int, target_length: int | None = None) -> dict[str, str]:
    status: dict[str, str] = {}
    if not source_path.exists():
        status[f"{output_name}_error"] = "source_mineru.md not found"
        return status
    if not template_path.exists():
        status[f"{output_name}_error"] = f"prompt template not found: {template_path}"
        return status
    source_text = trim_source_text(source_path.read_text(encoding="utf-8", errors="ignore"), prompt_chars)
    template = template_path.read_text(encoding="utf-8")
    format_args = {"source_text": source_text}
    if target_length is not None:
        format_args["target_length"] = target_length
    prompt = sanitize_text(template.format(**format_args))
    (item_dir / prompt_name).write_text(prompt, encoding="utf-8")
    try:
        text = call_deepseek(prompt, args, label)
    except Exception as exc:
        text = f"DeepSeek 生成 {label} 失败：{exc}\n\n请复制 {prompt_name} 手动生成。\n"
        status[f"{output_name}_error"] = str(exc)
    (item_dir / output_name).write_text(sanitize_text(text), encoding="utf-8")
    status[output_name] = output_name
    status[prompt_name] = prompt_name
    return status


def generate_xianyu_for_item(item_dir: Path, args: argparse.Namespace) -> dict[str, str]:
    status = generate_from_template(
        item_dir=item_dir,
        args=args,
        source_path=item_dir / "source_mineru.md",
        template_path=Path(args.xianyu_prompt_template),
        output_name="xianyu_note.md",
        prompt_name="prompt_for_xianyu.md",
        label="Xianyu listing note",
        prompt_chars=args.xianyu_prompt_chars,
    )
    note_path = item_dir / "xianyu_note.md"
    if note_path.exists():
        original = note_path.read_text(encoding="utf-8", errors="ignore")
        constrained = enforce_xianyu_constraints(original)
        note_path.write_text(sanitize_text(constrained), encoding="utf-8")
        status["xianyu_note_chars"] = str(len(constrained))
        status["xianyu_note_no_emoji"] = str(not EMOJI_RE.search(constrained)).lower()
        status["xianyu_note_max_chars"] = str(XIANYU_MAX_CHARS)
    return status


def generate_zhihu_for_item(item_dir: Path, args: argparse.Namespace) -> dict[str, str]:
    return generate_from_template(
        item_dir=item_dir,
        args=args,
        source_path=item_dir / "source_mineru.md",
        template_path=Path(args.zhihu_prompt_template),
        output_name="zhihu_article.md",
        prompt_name="prompt_for_zhihu.md",
        label="Zhihu article",
        prompt_chars=args.zhihu_prompt_chars,
        target_length=args.zhihu_length,
    )


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


def run_guard_if_enabled(output_dir: Path, args: argparse.Namespace) -> None:
    if str(args.sensitive_guard).lower() not in {"1", "true", "yes", "y", "on"}:
        log("Sensitive content guard disabled.")
        return
    if run_sensitive_guard is None or build_sensitive_arg_parser is None:
        log("Sensitive content guard import failed; skipping.")
        return
    guard_parser = build_sensitive_arg_parser()
    guard_args = guard_parser.parse_args([
        "--output-dir", str(output_dir),
        "--model", args.model,
        "--deepseek-base-url", args.deepseek_base_url,
        "--sensitive-api-url", args.sensitive_api_url,
        "--use-free-api", args.use_free_api,
        "--max-check-chunks", str(args.max_check_chunks),
    ])
    run_sensitive_guard(output_dir, guard_args)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="xhs_notes")
    parser.add_argument("--model", default=os.getenv("DEEPSEEK_MODEL", "deepseek-chat"))
    parser.add_argument("--deepseek-base-url", default=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    parser.add_argument("--generate-xianyu", default="true")
    parser.add_argument("--xianyu-prompt-template", default="prompts/xianyu_report_listing_prompt.md")
    parser.add_argument("--xianyu-prompt-chars", type=int, default=22000)
    parser.add_argument("--generate-zhihu", default="true")
    parser.add_argument("--zhihu-prompt-template", default="prompts/zhihu_report_article_prompt.md")
    parser.add_argument("--zhihu-prompt-chars", type=int, default=26000)
    parser.add_argument("--zhihu-length", type=int, default=2200)
    parser.add_argument("--sensitive-guard", default="true")
    parser.add_argument("--sensitive-api-url", default=os.getenv("SENSITIVE_API_URL", "https://v.api.aa1.cn/api/api-mgc/index.php"))
    parser.add_argument("--use-free-api", default="true")
    parser.add_argument("--max-check-chunks", type=int, default=20)
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    sanitized_before = sanitize_output_dir(output_dir)
    log(f"Sanitized {sanitized_before} generated text files before finalization.")

    summary: list[dict[str, Any]] = []
    for item_dir in sorted(p for p in output_dir.iterdir() if p.is_dir()):
        update: dict[str, Any] = {}
        if str(args.generate_xianyu).lower() in {"1", "true", "yes", "y", "on"}:
            log(f"Generating Xianyu note for {item_dir.name}")
            update.update(generate_xianyu_for_item(item_dir, args))
        if str(args.generate_zhihu).lower() in {"1", "true", "yes", "y", "on"}:
            log(f"Generating Zhihu article for {item_dir.name}")
            update.update(generate_zhihu_for_item(item_dir, args))
        if update:
            update_item_status(item_dir, update)
            summary.append({"item": item_dir.name, **update})

    normalized = normalize_wechat_articles(output_dir)
    log(f"Normalized {normalized} WeChat article endings.")
    run_guard_if_enabled(output_dir, args)
    constrained_xianyu = enforce_xianyu_constraints_in_dir(output_dir)
    log(f"Enforced Xianyu hard constraints on {constrained_xianyu} files.")
    sanitized_after = sanitize_output_dir(output_dir)
    log(f"Sanitized {sanitized_after} generated text files after finalization.")
    (output_dir / "finalize_summary.json").write_text(sanitize_text(json.dumps(summary, ensure_ascii=False, indent=2)), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
