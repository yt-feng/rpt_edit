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
    "zhihu_article.md",
    "xianyu_note.md",
    "podcast_script_zh.md",
    "podcast_script_en.md",
    "podcast_zh.md",
    "podcast_en.md",
}
SKIP_NAMES = {
    "source_mineru.md",
    "prompt_for_xianyu.md",
    "prompt_for_zhihu.md",
    "prompt_for_market_views.md",
}

SAFE_XHS_TAGS = ["#学习笔记", "#研究笔记", "#学习研究", "#研报解读"]
DISALLOWED_XHS_TAGS_RE = re.compile(r"#(?:投资学习|财经|金融|股票|基金|理财|小红书笔记|笔记分享|干货分享)\b")
SAFE_XIANYU_TAGS = ["#学习资料", "#研究笔记", "#学习笔记", "#行业研究", "#研报资料", "#资料整理", "#报告学习", "#案例研究"]
DISALLOWED_XIANYU_TAGS_RE = re.compile(r"#(?:财经|投资|股票|基金|理财|暴富|内幕|买入|卖出|稳赚|保本)\b")
WECHAT_STOCK_ARTICLE_FILENAMES = {"wechat_article.md", "wechat_article_en.md"}
EN_RATING_PATTERN = (
    r"(?<![A-Za-z])(?:strong\s+buy|buy|sell|overweight|underweight|outperform|underperform|"
    r"equal-?weight|market\s+perform|neutral|hold)(?![A-Za-z])"
)
EN_PRICE_TOKEN_PATTERN = r"(?<![A-Za-z])(?:PT|TP|PO)(?![A-Za-z])"
WECHAT_STOCK_TARGET_CLAUSE_RE = re.compile(
    r"(?:(?:上调|下调|维持|重申|给予|首予|首次覆盖|恢复|raise|raised|lower|lowered|maintain|"
    r"maintained|initiate|initiated|resume|resumed)\s*)?"
    r"[^，。；;\n]{0,24}"
    r"(?:目标价|目标价格|价格目标|目标估值|target\s+price|price\s+target|price\s+objective)"
    r"[^，。；;\n]{0,70}"
    rf"|(?:(?:new|raise|raised|lower|lowered|maintain|maintained)\s+)?{EN_PRICE_TOKEN_PATTERN}"
    r"[^，。；;\n]{0,45}",
    re.I,
)
WECHAT_STOCK_PAREN_RE = re.compile(
    r"[（(][^()（）\n]{0,90}(?:目标价|目标价格|target\s+price|price\s+target|"
    rf"{EN_PRICE_TOKEN_PATTERN}|买入|卖出|增持|减持|强烈推荐|推荐|荐股|"
    rf"{EN_RATING_PATTERN})[^()（）\n]{{0,90}}[）)]",
    re.I,
)
WECHAT_STOCK_CONTEXT_RE = re.compile(
    r"(?:评级|目标价|目标价格|价格目标|荐股|股票|股价|个股|券商|报告|研究覆盖|"
    rf"target\s+price|price\s+target|{EN_PRICE_TOKEN_PATTERN}|{EN_RATING_PATTERN})",
    re.I,
)
WECHAT_STOCK_FORBIDDEN_RE = re.compile(
    r"(?:目标价|目标价格|价格目标|目标估值|target\s+price|price\s+target|price\s+objective|"
    r"买入评级|卖出评级|增持评级|减持评级|强烈买入|推荐买入|建议买入|建议卖出|"
    r"强烈推荐|荐股|投资建议|操作建议|买卖建议|推荐|"
    rf"{EN_RATING_PATTERN})",
    re.I,
)

LOCAL_REPLACEMENTS: list[tuple[str, str]] = [
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

WECHAT_STOCK_REPLACEMENTS: list[tuple[str, str]] = [
    (r"(?:投资建议|操作建议|买卖建议)", "研究交流"),
    (r"(?:荐股|推荐标的|推荐个股)", "公司研究"),
    (r"(?:强烈推荐|推荐买入|建议买入|建议卖出)", "报告观点"),
    (r"(?:维持|重申|给予|首予|首次覆盖|恢复|上调|下调)\s*(?:买入|卖出|增持|减持|持有|中性|跑赢大市|跑输大市|优于大市|弱于大市)\s*(?:评级|建议|观点)?", "更新公司观点"),
    (rf"(?:维持|重申|给予|首予|首次覆盖|恢复|上调|下调)\s*{EN_RATING_PATTERN}\s*(?:rating|rated|recommendation)?", "公司观点更新"),
    (r"(?:买入|卖出|增持|减持|持有|中性|跑赢大市|跑输大市|优于大市|弱于大市)\s*(?:评级|建议)", "公司观点"),
    (r"评级\s*(?:上调|下调|维持|重申|恢复)?\s*(?:至|为)?\s*(?:买入|卖出|增持|减持|持有|中性|跑赢大市|跑输大市|优于大市|弱于大市)", "公司观点更新"),
    (rf"{EN_RATING_PATTERN}\s*(?:rating|rated|recommendation)?", "报告观点"),
    (r"(?:上调|下调|维持|重申|恢复)\s*评级", "更新公司观点"),
    (r"推荐", "提到"),
]

WECHAT_STRICT_WORD_REPLACEMENTS: list[tuple[str, str]] = [
    (r"世界经济论坛", "WEF"),
    (r"中国经济", "中国宏观环境"),
    (r"国内经济", "国内宏观环境"),
    (r"全球经济", "全球宏观环境"),
    (r"世界经济", "全球宏观环境"),
    (r"经济体", "地区"),
    (r"经济", "宏观环境"),
    (r"投资银行", "国际机构"),
    (r"投行", "国际机构"),
    (r"投研", "研究"),
    (r"投资者", "读者"),
    (r"投资人", "参与者"),
    (r"投资组合", "组合观察"),
    (r"投资回报", "回报表现"),
    (r"投资收益", "回报表现"),
    (r"投资周期", "研究周期"),
    (r"投资启示", "观察提示"),
    (r"投资", "研究"),
    (r"财经", "研究"),
    (r"金融机构", "机构"),
    (r"金融市场", "市场"),
    (r"金融条件", "资金条件"),
    (r"金融", "资金"),
    (r"A股|港股", "相关市场"),
    (r"股票市场|股市", "市场"),
    (r"股票|个股", "公司"),
    (r"股价", "报价"),
    (r"证券", "标的"),
    (r"券商", "机构"),
    (r"基金经理", "组合负责人"),
    (r"基金", "产品"),
    (r"理财", "资金规划"),
    (r"收益率", "回报表现"),
    (r"资产定价", "市场定价"),
    (r"风险", "不确定性"),
    (r"危机", "扰动"),
    (r"不好|不行", "需要继续观察"),
    (r"疲弱|乏力|低迷", "仍在调整"),
    (r"恶化", "出现变化"),
    (r"衰退|萎缩|收缩", "调整"),
    (r"通缩", "价格变化"),
    (r"崩盘|崩溃|暴跌", "明显波动"),
    (r"下行|放缓", "节奏变化"),
    (r"压力", "不确定性"),
    (r"拖累", "影响"),
    (r"负面", "谨慎"),
    (r"唱衰", "谨慎讨论"),
]

WECHAT_CHINA_NEUTRAL_REPLACEMENTS: list[tuple[str, str]] = [
    (
        r"((?:中国|国内|内地|大陆|人民币|A股|港股)[^。；;\n]{0,16})"
        r"(?:不好|不行|疲弱|乏力|低迷|恶化|危机|衰退|萎缩|收缩|通缩|崩盘|崩溃|"
        r"暴跌|下行|放缓|压力|拖累|负面|唱衰)",
        r"\1仍在调整",
    ),
    (r"中国不好|中国不行|唱衰中国", "相关表述需要中性处理"),
]

WECHAT_DIRECT_FORBIDDEN_RE = re.compile(
    r"(?:经济|投资|投行|投研|财经|金融|股票|个股|股价|股市|A股|港股|炒股|理财|证券|券商|基金|收益率|资产定价|风险)"
)
WECHAT_CHINA_NEGATIVE_CONTEXT_RE = re.compile(
    r"(?:中国|国内|内地|大陆|人民币|A股|港股)[^。；;\n]{0,20}"
    r"(?:不好|不行|疲弱|乏力|低迷|恶化|危机|衰退|萎缩|收缩|通缩|崩盘|崩溃|"
    r"暴跌|下行|放缓|压力|拖累|负面|唱衰)"
)

WECHAT_BLOCKED_TITLE_RULES: list[tuple[str, re.Pattern[str]]] = [
    (
        "military_or_defense",
        re.compile(
            r"(?:军用|军事|军队|国防|防务|战备|军工|武器|导弹|弹药|作战|战场|战争|"
            r"空军|海军|陆军|核武|航母)"
            r"|\b(?:defen[cs]e|military|armed\s+forces?|weapons?|missiles?|munitions?|"
            r"combat|warfare|battlefield|army|navy|air\s+force|nuclear\s+weapons?)\b"
            r"|\b(?:defen[cs]e|military|combat)\b.{0,40}\breadiness\b"
            r"|\breadiness\b.{0,40}\b(?:defen[cs]e|military|combat)\b",
            re.I,
        ),
    ),
    (
        "politically_sensitive",
        re.compile(
            r"(?:政治|政党|选举|议会|政变|地缘政治|制裁|主权争端|领土争端|台海|"
            r"台湾问题|台独|新疆|疆独|西藏|藏独|港独|人权指控|颜色革命)"
            r"|\b(?:geopolitic(?:s|al)?|political\s+part(?:y|ies)|elections?|parliament|"
            r"coup|sanctions?|sovereignty\s+disputes?|territorial\s+disputes?|"
            r"Taiwan\s+Strait|Xinjiang|Tibet|human\s+rights\s+allegations?)\b",
            re.I,
        ),
    ),
]

PROTECTED_TERMS = {
    "投研": "__PROTECT_TOUYAN__",
    "投行": "__PROTECT_TOUHANG__",
    "投顾": "__PROTECT_TOUGU__",
    "投资银行": "__PROTECT_IBANK__",
}


def log(message: str) -> None:
    print(message, flush=True)


def blocked_wechat_title_reason(title: str) -> str | None:
    """Return a deterministic block reason for a public-account title."""
    normalized = re.sub(r"\s+", " ", title or "").strip()
    if not normalized:
        return None
    for reason, pattern in WECHAT_BLOCKED_TITLE_RULES:
        if pattern.search(normalized):
            return reason
    return None


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


def sanitize_wechat_strict_wording(text: str) -> tuple[str, list[str]]:
    """Neutralize public-account wording that is too direct for finance-adjacent posts."""
    changes: list[str] = []
    cleaned = text or ""
    for pattern, repl in WECHAT_CHINA_NEUTRAL_REPLACEMENTS + WECHAT_STRICT_WORD_REPLACEMENTS:
        cleaned, n = re.subn(pattern, repl, cleaned, flags=re.I)
        if n:
            changes.append(f"{pattern}->{repl} x{n}")
    cleanup_pairs = [
        (r"宏观环境环境", "宏观环境"),
        (r"资金资金", "资金"),
        (r"研究研究", "研究"),
        (r"产品产品", "产品"),
        (r"市场市场", "市场"),
        (r"公司公司", "公司"),
        (r"(仍在调整){2,}", "仍在调整"),
        (r"((?:中国|国内|内地|大陆)宏观环境)不确定性仍在调整", r"\1仍在调整"),
        (r"仍在调整影响", "仍在调整，并影响"),
        (r"仍在调整相关市场", "仍在调整，相关市场"),
        (r"不确定性自担", "请自行判断"),
        (r"不确定性提示", "观察提示"),
        (r"研究建议", "观察提示"),
        (r"操作提示", "观察提示"),
    ]
    for pattern, repl in cleanup_pairs:
        cleaned, n = re.subn(pattern, repl, cleaned, flags=re.I)
        if n:
            changes.append(f"{pattern}->{repl} x{n}")
    return cleaned, changes


def sanitize_wechat_stock_language(
    text: str,
    strict_wording: bool = True,
    strict_h1_wording: bool | None = None,
) -> tuple[str, list[str]]:
    """Remove broker calls; optionally neutralize broader finance-adjacent wording."""
    changes: list[str] = []
    out_lines: list[str] = []
    for raw in (text or "").splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if stripped.startswith("![") or re.fullmatch(r"\[\[KC_IMAGE_\d{3}\]\]", stripped):
            out_lines.append(line)
            continue

        original_line = line
        heading_prefix = ""
        marker = re.match(r"^(\s*#{1,6}\s+)(.*)$", line)
        if marker:
            heading_prefix = marker.group(1)
            line = marker.group(2)
        is_heading = bool(heading_prefix)
        target_repl = "公司情况更新" if is_heading else ""
        line, n = WECHAT_STOCK_PAREN_RE.subn("", line)
        if n:
            changes.append(f"remove_stock_parenthetical x{n}")
        line, n = WECHAT_STOCK_TARGET_CLAUSE_RE.subn(target_repl, line)
        if n:
            changes.append(f"remove_target_price_clause x{n}")

        stock_context = bool(WECHAT_STOCK_CONTEXT_RE.search(original_line))
        for pattern, repl in WECHAT_STOCK_REPLACEMENTS:
            if pattern == "推荐" or stock_context or re.search(pattern, line, flags=re.I):
                line, n = re.subn(pattern, repl, line, flags=re.I)
                if n:
                    changes.append(f"{pattern}->{repl} x{n}")

        if stock_context:
            for word, repl in [("买入", "观点偏积极"), ("卖出", "观点偏谨慎"), ("增持", "观点偏积极"), ("减持", "观点偏谨慎")]:
                line, n = re.subn(word, repl, line)
                if n:
                    changes.append(f"{word}->{repl} x{n}")

        line = re.sub(r"\s{2,}", " ", line)
        line = re.sub(r"\s*([，。；;,:：])\s*", r"\1", line)
        line = re.sub(r"[，,；;]\s*(?:并)?(?:报告观点|公司观点|更新公司观点|公司观点更新)\s*(?:该股|该公司)?", "", line)
        line = re.sub(r"(?:[，,；;]\s*){2,}", "，", line)
        line = re.sub(r"[，,；;：:]\s*(?=$)", "", line)
        line = re.sub(r"(公司情况更新){2,}", "公司情况更新", line)
        line_strict_wording = strict_wording
        if marker and len(marker.group(1).strip()) == 1 and strict_h1_wording is not None:
            line_strict_wording = strict_h1_wording
        if line_strict_wording:
            line, strict_changes = sanitize_wechat_strict_wording(line)
            changes.extend(strict_changes)
        line = re.sub(r"\s*([，。；;,:：])\s*", r"\1", line)
        line = re.sub(r"[，,]+([。；;])", r"\1", line)
        line = re.sub(r"(?:[，,；;]\s*){2,}", "，", line)
        line = re.sub(r"[，,；;：:]\s*(?=$)", "", line)
        if re.fullmatch(r"[\s，,。；;]*(?:并)?(?:报告观点|公司观点|公司观点更新|更新公司观点|观点偏积极|观点偏谨慎|该股|该公司)+[。.]?", line):
            line = ""
        if is_heading:
            heading = line.strip(" ：:，,；;")
            heading = re.sub(r"[，,]?(?:更新公司观点|公司观点更新|公司观点|报告观点)$", "", heading).strip(" ：:，,；;")
            if not heading:
                heading = "公司情况更新"
            elif len(heading) < 6:
                heading = (heading + "：公司情况更新").strip("：")
            line = heading_prefix + heading
        if line != original_line:
            changes.append("sanitize_wechat_stock_line")
        out_lines.append(line)
    cleaned = "\n".join(out_lines)
    cleaned = re.sub(r"(仍在调整){2,}", "仍在调整", cleaned)
    cleaned = re.sub(r"\n{4,}", "\n\n\n", cleaned)
    return cleaned, changes


def contains_wechat_stock_forbidden_language(text: str) -> bool:
    return bool(WECHAT_STOCK_FORBIDDEN_RE.search(text or ""))


def contains_wechat_strict_forbidden_language(text: str) -> bool:
    return bool(WECHAT_DIRECT_FORBIDDEN_RE.search(text or "") or WECHAT_CHINA_NEGATIVE_CONTEXT_RE.search(text or ""))


def normalize_xhs_note_tags(text: str) -> tuple[str, list[str]]:
    changes: list[str] = []
    original = text
    text = DISALLOWED_XHS_TAGS_RE.sub("", text)
    text = re.sub(r"(?:^|\n)\s*(?:#[^\n#\s]+\s*)+\s*$", "", text, flags=re.MULTILINE).strip()
    text = text + "\n\n" + " ".join(SAFE_XHS_TAGS) + "\n"
    text = re.sub(r"\n{3,}", "\n\n", text)
    if text != original:
        changes.append("normalize_xhs_note_tags")
    return text, changes


def normalize_xianyu_note(text: str) -> tuple[str, list[str]]:
    changes: list[str] = []
    original = text
    hashtag_candidates: list[str] = []
    kept_lines: list[str] = []
    for raw in text.splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if re.match(r"^(?:建议价格|价格建议|参考价格)\s*[:：]", stripped):
            changes.append("remove_xianyu_price_line")
            continue
        keyword_match = re.match(r"^(?:搜索关键词|搜索词|关键词)\s*[:：]\s*(.*)$", stripped)
        if keyword_match:
            keyword_text = keyword_match.group(1)
            parts = [p.strip(" #，,、/|;；") for p in re.split(r"[\s，,、/|;；]+", keyword_text) if p.strip(" #，,、/|;；")]
            for part in parts:
                if not re.search(r"财经|投资|股票|基金|理财|暴富|内幕|买入|卖出|稳赚|保本", part):
                    hashtag_candidates.append("#" + part.lstrip("#"))
            changes.append("convert_search_keywords_to_hashtag")
            continue
        hashtag_match = re.match(r"^(?:Hashtag|hashtag|标签)\s*[:：]\s*(.*)$", stripped)
        if hashtag_match:
            tag_text = DISALLOWED_XIANYU_TAGS_RE.sub("", hashtag_match.group(1))
            hashtag_candidates.extend(re.findall(r"#[^\s#，,、/|;；]+", tag_text))
            changes.append("normalize_existing_xianyu_hashtag_line")
            continue
        kept_lines.append(line)
    tags: list[str] = []
    for tag in hashtag_candidates + SAFE_XIANYU_TAGS:
        tag = tag.strip()
        if not tag.startswith("#"):
            tag = "#" + tag
        if DISALLOWED_XIANYU_TAGS_RE.search(tag):
            continue
        if tag not in tags:
            tags.append(tag)
        if len(tags) >= 10:
            break
    text = "\n".join(kept_lines).strip()
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = text + "\n\nHashtag：" + " ".join(tags) + "\n"
    if text != original:
        changes.append("normalize_xianyu_note")
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
4. 微信文章里不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；改成“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
5. 不要新增事实、页数、价格、承诺、联系方式。
6. 小红书 note.md 的标签只能使用 #学习笔记 #研究笔记 #学习研究 #研报解读。
7. 闲鱼 xianyu_note.md 不要输出“建议价格”或“搜索关键词”，如需关键词请改成 Hashtag。
8. 涉及中国、国内、内地、大陆、人民币、A股、港股时，必须使用中性客观表达，不写“不好、不行、疲弱、低迷、恶化、危机、衰退、崩盘、放缓、压力、拖累、唱衰”等负面判断。
9. 知乎 zhihu_article.md 保持理性长文风格，不要写关注点赞或操作建议。
10. 只输出改写后的正文，不要解释。

检测命中：
{json.dumps(detected_hits, ensure_ascii=False)}

原文：
{text}
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
    if path.suffix.lower() == ".md" and not path.name.startswith("prompt_") and "source" not in path.name.lower():
        return True
    return False


def guard_file(path: Path, args: argparse.Namespace) -> dict[str, Any]:
    original = path.read_text(encoding="utf-8", errors="ignore")
    local_text, local_changes = apply_local_guard(original)
    if path.name in WECHAT_STOCK_ARTICLE_FILENAMES:
        local_text, stock_changes = sanitize_wechat_stock_language(local_text)
        local_changes.extend(stock_changes)
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
    if path.name == "xianyu_note.md":
        final_text, xianyu_changes = normalize_xianyu_note(final_text)
        local_changes.extend(xianyu_changes)
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
