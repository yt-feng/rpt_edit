#!/usr/bin/env python3
"""Compliance-oriented sensitive-content guard for generated notes.

This script is designed for generated marketing/publication materials only. It:
1. Applies local compliance-safe replacements for risky finance/marketing wording.
2. Checks text with the free-api sensitive-word endpoint when enabled.
3. If the endpoint flags content, asks DeepSeek to rewrite it into safer wording.

The goal is not to bypass platform moderation, but to reduce overclaiming,
financial-advice language, direct engagement bait, and sensitive phrasing before
publishing public-facing notes.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import time
from pathlib import Path
from typing import Any

import requests

TARGET_FILENAMES = {
    "note.md",
    "wechat_article.md",
    "wechat_article_en.md",
    "xianyu_note.md",
    "podcast_script_zh.md",
    "podcast_script_en.md",
    "podcast_zh.md",
    "podcast_en.md",
}
SKIP_NAMES = {
    "source_mineru.md",
    "prompt_for_xianyu.md",
    "prompt_for_market_views.md",
}

SAFE_XHS_TAGS = ["#学习笔记", "#研究笔记", "#学习研究", "#研报解读"]
DISALLOWED_XHS_TAGS_RE = re.compile(r"#(?:投资学习|财经|金融|股票|基金|理财|小红书笔记|笔记分享|干货分享)\b")

LOCAL_REPLACEMENTS: list[tuple[str, str]] = [
    # Financial-advice / trading intent
    (r"不构成任何投资建议", "仅为个人阅读分享"),
    (r"投资建议", "研究交流"),
    (r"投资参考", "研究参考"),
    (r"投资价值", "研究价值"),
    (r"投资机会", "研究线索"),
    (r"投资逻辑", "研究逻辑"),
    (r"投资者", "读者"),
    (r"适合投资", "适合研究"),
    (r"买入评级", "报告评级"),
    (r"卖出评级", "报告评级"),
    (r"强烈买入", "报告较为积极"),
    (r"推荐买入", "报告观点偏积极"),
    (r"马上上车", "可以继续跟踪"),
    (r"抄底", "底部观察"),
    (r"必涨", "存在上行假设"),
    (r"稳赚", "确定性仍需验证"),
    (r"翻倍", "弹性较高"),
    (r"暴涨", "明显走强"),
    (r"暴跌", "明显回落"),
    (r"收益率", "回报表现"),
    (r"保证收益", "不承诺结果"),
    (r"保本", "风险自担"),
    (r"内幕", "资料"),
    (r"内部资料", "资料"),
    (r"独家", "整理版"),
    (r"原版", "电子版"),
    (r"无水印", "清晰版"),
    (r"全网最低", "价格友好"),
    # Direct engagement bait / platform-sensitive CTA
    (r"关注点赞收藏", "欢迎交流收藏"),
    (r"点赞收藏关注", "欢迎交流收藏"),
    (r"关注\s*[、,，和]*\s*点赞", "欢迎交流"),
    (r"点赞\s*[、,，和]*\s*关注", "欢迎交流"),
    (r"点个关注", "欢迎交流"),
    (r"求关注", "欢迎交流"),
    (r"求点赞", "欢迎交流"),
    (r"点赞", "收藏"),
    (r"评论区见", "欢迎讨论"),
    (r"评论区留言", "可以一起讨论"),
    # Extreme marketing terms
    (r"必看", "值得看看"),
    (r"必读", "值得读"),
    (r"爆款", "吸引人的"),
    (r"震惊", "值得注意"),
    (r"全网首发", "整理分享"),
    (r"唯一", "相对少见"),
    (r"顶级", "高质量"),
    (r"最全", "较完整"),
    (r"最强", "较强"),
    (r"绝对", "相对"),
]

# Standalone use of “投资” is broad. Replace in public-facing text, but preserve
# common research terms that are less promotional.
PROTECTED_TERMS = {
    "投研": "__PROTECT_TOUYAN__",
    "投行": "__PROTECT_TOUHANG__",
    "投顾": "__PROTECT_TOUGU__",
    "投资银行": "__PROTECT_IBANK__",
}


def log(message: str) -> None:
    print(message, flush=True)


def apply_local_guard(text: str) -> tuple[str, list[str]]:
    changes: list[str] = []
    protected = text
    for key, token in PROTECTED_TERMS.items():
        protected = protected.replace(key, token)
    for pattern, repl in LOCAL_REPLACEMENTS:
        new_text, n = re.subn(pattern, repl, protected, flags=re.IGNORECASE)
        if n:
            changes.append(f"{pattern}->{repl} x{n}")
        protected = new_text
    new_text, n = re.subn(r"投资", "研究", protected)
    if n:
        changes.append(f"投资->研究 x{n}")
    for key, token in PROTECTED_TERMS.items():
        protected = protected.replace(token, key)
    protected = re.sub(r"\n{4,}", "\n\n\n", protected)
    return protected, changes


def normalize_xhs_note_tags(text: str) -> tuple[str, list[str]]:
    """Keep only approved XHS hashtags and append a stable safe tag set."""
    changes: list[str] = []
    original = text
    text = DISALLOWED_XHS_TAGS_RE.sub("", text)
    # Drop any trailing hashtag-only block. Then append our allowed set.
    text = re.sub(r"(?:^|\n)\s*(?:#[^\n#\s]+\s*)+\s*$", "", text, flags=re.MULTILINE).strip()
    text = text + "\n\n" + " ".join(SAFE_XHS_TAGS) + "\n"
    text = re.sub(r"\n{3,}", "\n\n", text)
    if text != original:
        changes.append("normalize_xhs_note_tags")
    return text, changes


def chunks(text: str, max_chars: int = 650) -> list[str]:
    paras = re.split(r"(\n\n+)", text)
    out: list[str] = []
    buf = ""
    for part in paras:
        if len(buf) + len(part) <= max_chars:
            buf += part
        else:
            if buf.strip():
                out.append(buf.strip())
            if len(part) > max_chars:
                for i in range(0, len(part), max_chars):
                    piece = part[i:i + max_chars].strip()
                    if piece:
                        out.append(piece)
                buf = ""
            else:
                buf = part
    if buf.strip():
        out.append(buf.strip())
    return out


def free_api_check(text: str, api_url: str, max_chunks: int = 20) -> dict[str, Any]:
    hits: list[dict[str, Any]] = []
    errors: list[str] = []
    for idx, chunk in enumerate(chunks(text)[:max_chunks], 1):
        try:
            response = requests.get(api_url, params={"msg": chunk}, timeout=12)
            data = response.json()
            if str(data.get("num")) == "1":
                hits.append({"chunk_index": idx, "ci": data.get("ci", ""), "desc": data.get("desc", "存在敏感词")})
        except Exception as exc:
            errors.append(str(exc)[:200])
            break
        time.sleep(0.1)
    return {"hit": bool(hits), "hits": hits, "errors": errors}


def deepseek_rewrite(text: str, detected_hits: list[dict[str, Any]], model: str, base_url: str) -> str:
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise RuntimeError("Missing DEEPSEEK_API_KEY")
    prompt = f"""
请把下面的中文营销/笔记文案改写为更稳妥的平台公开发布版本。

要求：
1. 保留原有信息结构、标题层级、Markdown 链接和图片链接。
2. 删除或替换金融操作建议、收益承诺、买卖暗示、极限词、夸张词、直接引导关注点赞等表达。
3. 不要用谐音、拆字、错别字或黑话绕过平台规则；要改成自然、合规、克制的表达。
4. “投资”相关词尽量改成“研究”“投研”“观察”“学习参考”等，视上下文自然处理。
5. 不要新增事实、页数、价格、承诺、联系方式。
6. 小红书 note.md 的标签只能使用 #学习笔记 #研究笔记 #学习研究 #研报解读。
7. 只输出改写后的正文，不要解释。

检测命中：
{json.dumps(detected_hits, ensure_ascii=False)}

原文：
"""
{text}
"""
""".strip()
    response = requests.post(
        base_url.rstrip("/") + "/chat/completions",
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
        json={
            "model": model,
            "temperature": 0.2,
            "messages": [
                {"role": "system", "content": "你是严谨的中文内容合规编辑，只做安全、自然、克制的改写。"},
                {"role": "user", "content": prompt},
            ],
        },
        timeout=240,
    )
    if response.status_code >= 400:
        raise RuntimeError(f"DeepSeek rewrite failed: HTTP {response.status_code}, {response.text[:500]}")
    data = response.json()
    return data["choices"][0]["message"]["content"].strip() + "\n"


def should_process(path: Path) -> bool:
    if path.name in SKIP_NAMES:
        return False
    if path.name in TARGET_FILENAMES:
        return True
    # Include additional generated markdown notes, but skip raw/source/prompt files.
    if path.suffix.lower() == ".md" and not path.name.startswith("prompt_") and "source" not in path.name.lower():
        return True
    return False


def guard_file(path: Path, args: argparse.Namespace) -> dict[str, Any]:
    original = path.read_text(encoding="utf-8", errors="ignore")
    local_text, local_changes = apply_local_guard(original)
    check = {"hit": False, "hits": [], "errors": []}
    final_text = local_text
    rewrite_error = ""
    if str(args.use_free_api).lower() in {"1", "true", "yes", "y", "on"}:
        check = free_api_check(local_text, args.sensitive_api_url, args.max_check_chunks)
    if check.get("hit"):
        try:
            rewritten = deepseek_rewrite(local_text, check.get("hits", []), args.model, args.deepseek_base_url)
            final_text, more_changes = apply_local_guard(rewritten)
            local_changes.extend(["after_deepseek:" + x for x in more_changes])
        except Exception as exc:
            rewrite_error = str(exc)
            log(f"DeepSeek sensitive rewrite failed for {path}: {exc}")
    if path.name == "note.md":
        final_text, tag_changes = normalize_xhs_note_tags(final_text)
        local_changes.extend(tag_changes)
    changed = final_text != original
    if changed:
        path.write_text(final_text, encoding="utf-8")
    return {
        "path": str(path),
        "changed": changed,
        "local_changes": local_changes[:80],
        "api_hit": bool(check.get("hit")),
        "api_hits": check.get("hits", []),
        "api_errors": check.get("errors", []),
        "rewrite_error": rewrite_error,
    }


def run_sensitive_guard(output_dir: Path, args: argparse.Namespace) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for path in sorted(output_dir.rglob("*")):
        if path.is_file() and should_process(path):
            try:
                results.append(guard_file(path, args))
            except Exception as exc:
                results.append({"path": str(path), "changed": False, "error": str(exc)})
    summary_path = output_dir / "sensitive_content_guard_summary.json"
    summary_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    changed = sum(1 for item in results if item.get("changed"))
    hits = sum(1 for item in results if item.get("api_hit"))
    log(f"Sensitive content guard processed {len(results)} files; changed={changed}, api_hits={hits}.")
    return results


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--model", default=os.getenv("DEEPSEEK_MODEL", "deepseek-chat"))
    parser.add_argument("--deepseek-base-url", default=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    parser.add_argument("--sensitive-api-url", default=os.getenv("SENSITIVE_API_URL", "https://v.api.aa1.cn/api/api-mgc/index.php"))
    parser.add_argument("--use-free-api", default="true")
    parser.add_argument("--max-check-chunks", type=int, default=20)
    return parser


def main() -> int:
    parser = build_arg_parser()
    args = parser.parse_args()
    run_sensitive_guard(Path(args.output_dir), args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
