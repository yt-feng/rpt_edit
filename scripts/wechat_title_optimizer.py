#!/usr/bin/env python3
"""Shared WeChat title and keyword helpers.

DeepSeek is good at proposing angles, but the final public-account title needs
hard gates: no broker tickers, no file slugs, one colon at most, and enough
searchable nouns for WeChat 搜一搜. This module keeps those gates deterministic.
"""
from __future__ import annotations

import json
import re
from typing import Any

from sensitive_content_guard import sanitize_wechat_stock_language


INSTITUTION_TITLE_ALIASES: list[tuple[str, list[str]]] = [
    ("高盛", ["GS", "Goldman Sachs"]),
    ("摩根大通", ["JPM", "J.P. Morgan", "JP Morgan", "JPMorgan"]),
    ("摩根士丹利", ["MS", "Morgan Stanley", "摩根斯坦利", "大摩"]),
    ("美银", ["BofA", "Bank of America", "美国银行", "美银证券"]),
    ("花旗", ["Citi", "Citigroup"]),
    ("瑞银", ["UBS"]),
    ("汇丰", ["HSBC"]),
    ("巴克莱", ["BARC", "Barclays"]),
    ("伯恩斯坦", ["Bernstein", "Sanford C. Bernstein", "Sanford Bernstein"]),
    ("杰富瑞", ["JEF", "Jefferies"]),
    ("德意志银行", ["DB", "Deutsche Bank", "德银"]),
    ("野村", ["NOM", "Nomura"]),
    ("美联储", ["Fed", "Federal Reserve"]),
]
TITLE_ALIAS_SEPARATOR_RE = r"(?:[：:，,、;；\-—]\s*)?"
TITLE_BROKER_TICKER_RE = re.compile(
    r"(?<![A-Za-z])(?:GS|JPM|JEF|NOM|BARC|MS|DB|BofA)(?=(?:Q[1-4]|\d|[^A-Za-z]|$))|"
    r"(?<![A-Za-z])(?:Citi|Citigroup|Goldman|JPMorgan|Jefferies|Nomura|Barclays)(?![A-Za-z])",
    re.I,
)
TITLE_NOISE_RE = re.compile(
    r"(?:核心观点|关键要点|研报速览|报告解读|Shared|Update|Quick Note|DeepSeek|"
    r"一文看懂|震惊|爆了|彻底反转|一夜变天)",
    re.I,
)
TITLE_ABSTRACT_RE = re.compile(r"(?:结构性变量|二阶影响|再定价框架|核心框架|底层逻辑|长期主义)")

BIG_NAME_TERMS = [
    "高盛",
    "摩根士丹利",
    "摩根斯坦利",
    "摩根大通",
    "美银",
    "花旗",
    "瑞银",
    "汇丰",
    "巴克莱",
    "伯恩斯坦",
    "杰富瑞",
    "野村",
    "美联储",
    "IMF",
    "世界银行",
    "国际清算银行",
    "麦肯锡",
    "波士顿咨询",
    "贝恩",
    "木头姐",
    "ARK",
    "洪灏",
    "邢自强",
    "辜朝明",
    "特朗普",
    "马斯克",
    "鲍威尔",
]
SEARCH_TERMS = [
    "中国",
    "A股",
    "港股",
    "人民币",
    "美元",
    "房地产",
    "房价",
    "楼市",
    "公积金",
    "消费",
    "美妆",
    "化妆品",
    "618",
    "外卖补贴",
    "电商",
    "汽车",
    "新能源车",
    "电池",
    "光伏",
    "储能",
    "半导体",
    "功率半导体",
    "AI",
    "软件",
    "机器人",
    "人形机器人",
    "Robotaxi",
    "自动驾驶",
    "数据中心",
    "服务器",
    "GPU",
    "ASIC",
    "HDD",
    "SSD",
    "MLCC",
    "SiC",
    "铜",
    "铝",
    "黄金",
    "原油",
    "通胀",
    "降息",
    "加息",
    "收益率",
    "美元指数",
    "就业",
    "GDP",
    "CPI",
    "PMI",
    "供应链",
    "资本开支",
    "现金流",
    "定价权",
    "利润率",
    "政策",
    "关税",
    "出口管制",
    "比特币",
    "加密货币",
    "DeFi",
    "生物科技",
    "医药",
    "全球经济",
]
CONTRARIAN_TERMS = [
    "低估",
    "高估",
    "误判",
    "反而",
    "不是",
    "而是",
    "真正",
    "悖论",
    "拐点",
    "分水岭",
    "触底",
    "回升",
    "修复",
    "再加速",
    "韧性",
    "超预期",
    "预期差",
    "为何",
]
GENERIC_KEYWORD_STOPWORDS = {
    "标题",
    "微信标题",
    "核心观点",
    "关键要点",
    "报告解读",
    "投资启示",
    "总结",
    "更多",
    "完整报告",
    "KC桌面",
    "外资精译",
    "Personal",
    "reading",
    "notes",
}
ENGLISH_SLUG_WORDS = {
    "china": "中国",
    "chinese": "中国",
    "autos": "汽车",
    "auto": "汽车",
    "automotive": "汽车",
    "ev": "电动车",
    "energy": "能源",
    "security": "安全",
    "semiconductor": "半导体",
    "semiconductors": "半导体",
    "hardware": "硬件",
    "software": "软件",
    "server": "服务器",
    "servers": "服务器",
    "property": "地产",
    "real": "房地产",
    "estate": "地产",
    "consumer": "消费",
    "consumption": "消费",
    "beauty": "美妆",
    "cosmetics": "美妆",
    "retail": "零售",
    "internet": "互联网",
    "robot": "机器人",
    "robots": "机器人",
    "robotics": "机器人",
    "power": "电力",
    "solar": "光伏",
    "battery": "电池",
    "batteries": "电池",
    "materials": "材料",
    "usd": "美元",
    "cny": "人民币",
    "rmb": "人民币",
    "fix": "中间价",
    "model": "模型",
    "market": "市场",
    "markets": "市场",
    "rates": "利率",
    "inflation": "通胀",
    "ai": "AI",
}
ENGLISH_SLUG_SKIP_WORDS = {
    "morgan",
    "stanley",
    "goldman",
    "sachs",
    "jpmorgan",
    "jpm",
    "nomura",
    "barclays",
    "jefferies",
    "bernstein",
    "citi",
    "shared",
    "update",
    "quick",
    "note",
    "report",
    "research",
}


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", str(text or "")).strip()


def strip_markdown_markup(text: str) -> str:
    text = re.sub(r"^\s*#{1,6}\s*", "", str(text or ""))
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"!\[[^\]]*\]\([^\)]+\)", "", text)
    return normalize_space(text)


def canonicalize_institution_title_name(title: str) -> str:
    normalized = normalize_space(title)
    normalized = normalized.replace("摩根斯坦利", "摩根士丹利")
    normalized = normalized.replace("美国银行", "美银")
    return normalized


def alias_pattern(alias: str) -> str:
    if alias.lower() == "bofa":
        return r"(?<![A-Za-z])BofA(?=(?:Q[1-4]|\d|[^A-Za-z]|$))"
    if re.fullmatch(r"[A-Z]{2,5}", alias):
        return rf"(?<![A-Za-z]){re.escape(alias)}(?=(?:Q[1-4]|\d|[^A-Za-z]|$))"
    if re.fullmatch(r"[A-Za-z. ]+", alias):
        return r"\b" + re.escape(alias).replace(r"\ ", r"[\s._-]+") + r"\b"
    return re.escape(alias)


def limit_title_colons(title: str) -> str:
    cleaned = normalize_space(title).replace(":", "：")
    if "：" not in cleaned:
        return cleaned
    head, tail = cleaned.split("：", 1)
    tail = re.sub(r"\s*：\s*", "，", tail).strip(" ，")
    return f"{head.strip()}：{tail}" if tail else head.strip()


def clean_leading_report_slug(title: str) -> str:
    cleaned = normalize_space(title)
    cleaned = re.sub(r"^([^：:]{1,18}[：:]\s*)(?:\d{4}[-_])?\d{1,4}[-_]\d{1,4}[-_]+", r"\1", cleaned)
    cleaned = re.sub(r"^(?:\d{4}[-_])?\d{1,4}[-_]\d{1,4}[-_]+", "", cleaned)
    cleaned = re.sub(r"^[#\s]*\d{1,4}[-_]\d{1,4}[-_]+", "", cleaned)

    def readable_slug_tail(value: str) -> str:
        if value.count("-") + value.count("_") < 3:
            return value
        value = value.replace("_", " ")
        value = re.sub(r"\s*-{2,}\s*", "，", value)
        value = re.sub(r"\s*-\s*", " ", value)
        return normalize_space(value)

    for sep in ("：", ":"):
        if sep in cleaned:
            head, tail = cleaned.split(sep, 1)
            return f"{head.strip()}：{readable_slug_tail(tail.strip())}".strip("： ")
    return readable_slug_tail(cleaned).strip(" -_")


def remove_redundant_title_aliases(title: str) -> str:
    cleaned = clean_leading_report_slug(canonicalize_institution_title_name(title))
    for cn_name, aliases in INSTITUTION_TITLE_ALIASES:
        alias_group = "|".join(alias_pattern(alias) for alias in aliases)
        cleaned = re.sub(
            rf"^({re.escape(cn_name)})\s*(?:{alias_group})\s*{TITLE_ALIAS_SEPARATOR_RE}",
            rf"\1：",
            cleaned,
            flags=re.I,
        )
        cleaned = re.sub(
            rf"^({re.escape(cn_name)})[：:]\s*(?:{alias_group})\s*{TITLE_ALIAS_SEPARATOR_RE}",
            rf"\1：",
            cleaned,
            flags=re.I,
        )
        cleaned = re.sub(
            rf"^(?:{alias_group})\s*[：:]\s*({re.escape(cn_name)})\s*{TITLE_ALIAS_SEPARATOR_RE}",
            rf"\1：",
            cleaned,
            flags=re.I,
        )
        cleaned = re.sub(
            rf"^({re.escape(cn_name)})\s*(?:\(|（)\s*(?:{alias_group})\s*(?:\)|）)\s*{TITLE_ALIAS_SEPARATOR_RE}",
            rf"\1：",
            cleaned,
            flags=re.I,
        )
    cleaned = re.sub(r"\s*[：:]\s*", "：", cleaned)
    cleaned = re.sub(r"：{2,}", "：", cleaned)
    return limit_title_colons(cleaned).strip("：: -—")


def repair_english_slug_tail(title: str) -> str:
    if "：" not in title:
        return re.sub(r"\b(?:Shared|Update|Quick Note|Report|Research)\b", "", title, flags=re.I).strip(" ，,")
    head, tail = title.split("：", 1)
    if not re.search(r"[A-Za-z]", tail):
        return title
    readable_tail = re.sub(r"\b(?:Shared|Update|Quick Note|Report|Research)\b", "", tail, flags=re.I)
    readable_tail = re.sub(r"[-_/]+", " ", readable_tail)
    words = re.findall(r"AI|USD|CNY|RMB|[A-Z]+(?=[A-Z][a-z]|$)|[A-Z]?[a-z]+|\d+", readable_tail)
    mapped: list[str] = []
    for word in words:
        key = word.lower()
        if key in ENGLISH_SLUG_SKIP_WORDS or key.isdigit():
            continue
        value = ENGLISH_SLUG_WORDS.get(key)
        if value and value not in mapped:
            mapped.append(value)
    chinese_chars = len(re.findall(r"[\u4e00-\u9fff]", tail))
    latin_chars = len(re.findall(r"[A-Za-z]", tail))
    if mapped and latin_chars > max(chinese_chars * 2, 6):
        return f"{head}：{''.join(mapped[:6])}"
    tail = normalize_space(readable_tail).strip(" ，,")
    return f"{head}：{tail}" if tail else head


def ensure_title_has_institution_local(title: str, institution_name: str) -> str:
    institution = canonicalize_institution_title_name(institution_name)
    title = normalize_space(title)
    if not institution or title.startswith(f"{institution}：") or title == institution:
        return title
    return f"{institution}：{title}".strip("： ")


def strip_unexpected_leading_institution_prefix(title: str, institution_name: str) -> str:
    expected = canonicalize_institution_title_name(institution_name)
    cleaned = remove_redundant_title_aliases(title)
    for _ in range(3):
        for cn_name, aliases in INSTITUTION_TITLE_ALIASES:
            if canonicalize_institution_title_name(cn_name) == expected:
                continue
            prefix_group = "|".join([re.escape(cn_name), *(alias_pattern(alias) for alias in aliases)])
            replaced = re.sub(rf"^(?:{prefix_group})\s*[：:，,、;；\-—]\s*", "", cleaned, flags=re.I).strip()
            if replaced != cleaned:
                cleaned = replaced
                break
        else:
            break
    return cleaned


def truncate_chars(text: str, max_chars: int) -> str:
    text = normalize_space(text)
    if len(text) <= max_chars:
        return text
    return text[: max(0, max_chars - 1)].rstrip("，,；;：: ") + "…"


def clean_wechat_title(title: str, institution_name: str = "", max_chars: int = 64) -> str:
    cleaned = strip_markdown_markup(title)
    cleaned, _stock_changes = sanitize_wechat_stock_language(cleaned)
    cleaned = re.sub(r"^(?:标题|微信标题|公众号标题)\s*[：:]\s*", "", cleaned)
    cleaned = re.sub(r"[《》#>*]+", "", cleaned)
    cleaned = remove_redundant_title_aliases(cleaned)
    cleaned = repair_english_slug_tail(cleaned)
    cleaned = re.sub(r"\s*(?:--+|—+)\s*", "，", cleaned)
    cleaned = re.sub(r"\s+", "", cleaned)
    cleaned = re.sub(r"(真正的){2,}", "真正的", cleaned)
    cleaned = cleaned.replace("摩根斯坦利", "摩根士丹利").replace("美国银行", "美银")
    if institution_name:
        cleaned = strip_unexpected_leading_institution_prefix(cleaned, institution_name)
        cleaned = ensure_title_has_institution_local(cleaned, institution_name)
        if cleaned.strip("：:，, ") == canonicalize_institution_title_name(institution_name):
            cleaned = f"{canonicalize_institution_title_name(institution_name)}：公司情况更新"
    cleaned = remove_redundant_title_aliases(cleaned)
    cleaned = limit_title_colons(cleaned)
    return truncate_chars(cleaned, max_chars).strip("：: -—")


def parse_title_candidates(raw: str) -> list[str]:
    text = (raw or "").strip()
    candidates: list[str] = []

    def add(value: Any) -> None:
        title = normalize_space(str(value or ""))
        title = re.sub(r"^\d+[\).、]\s*", "", title)
        title = title.strip("\"'“”‘’")
        if title and title not in candidates:
            candidates.append(title)

    json_match = re.search(r"\{.*\}", text, re.S)
    if json_match:
        try:
            payload = json.loads(json_match.group(0))
            values = payload.get("titles") if isinstance(payload, dict) else None
            if isinstance(values, list):
                for item in values:
                    add(item)
        except Exception:
            pass
    if not candidates:
        for raw_line in text.splitlines():
            line = raw_line.strip()
            if not line or line.startswith("```"):
                continue
            line = re.sub(r"^(?:[-*]|\d+[\).、])\s*", "", line)
            if len(line) <= 80:
                add(line)
    return candidates[:12]


extract_title_candidates = parse_title_candidates


def title_score(title: str, institution_name: str = "", source_keywords: list[str] | None = None) -> int:
    source_keywords = source_keywords or []
    cleaned = clean_wechat_title(title, institution_name, max_chars=80)
    score = 0
    if 20 <= len(cleaned) <= 35:
        score += 5
    elif 16 <= len(cleaned) <= 40:
        score += 2
    else:
        score -= 4
    if len(cleaned) > 48:
        score -= 5
    if cleaned.count("：") > 1:
        score -= 8
    if TITLE_BROKER_TICKER_RE.search(cleaned):
        score -= 10
    if TITLE_NOISE_RE.search(cleaned):
        score -= 5
    if TITLE_ABSTRACT_RE.search(cleaned):
        score -= 2
    first_window = cleaned[:16]
    if any(term in first_window for term in BIG_NAME_TERMS):
        score += 3
    if any(term in cleaned for term in BIG_NAME_TERMS):
        score += 2
    search_hits = [term for term in SEARCH_TERMS if term.lower() in cleaned.lower()]
    score += min(len(search_hits), 4) * 2
    contrarian_hits = [term for term in CONTRARIAN_TERMS if term in cleaned]
    score += min(len(contrarian_hits), 3) * 3
    if re.search(r"(?:\d+(?:\.\d+)?%?|\bQ[1-4]\b|20\d{2}|[A-Za-z]{2,}\d+)", cleaned):
        score += 2
    for keyword in source_keywords[:10]:
        if keyword and keyword.lower() in cleaned.lower():
            score += 1
    if institution_name and cleaned.startswith(canonicalize_institution_title_name(institution_name)):
        score += 1
    if re.search(r"[A-Za-z]{4,}", cleaned) and not any(term in cleaned for term in ["Robotaxi", "DeFi", "ARK", "AI"]):
        score -= 2
    return score


def choose_best_wechat_title(
    candidates: list[str],
    fallback: str,
    institution_name: str = "",
    source_keywords: list[str] | None = None,
    max_chars: int = 64,
) -> str:
    pool: list[str] = []
    for item in [*candidates, fallback]:
        cleaned = clean_wechat_title(item, institution_name, max_chars=max_chars)
        if cleaned and cleaned not in pool:
            pool.append(cleaned)
    if not pool:
        return clean_wechat_title(fallback or "研报精译", institution_name, max_chars=max_chars)
    ranked = sorted(
        pool,
        key=lambda item: (
            title_score(item, institution_name, source_keywords),
            -abs(len(item) - 28),
            -pool.index(item),
        ),
        reverse=True,
    )
    return clean_wechat_title(ranked[0], institution_name, max_chars=max_chars)


def extract_wechat_keywords(title: str, body: str = "", max_keywords: int = 8) -> list[str]:
    haystack = normalize_space(f"{title}\n{body}")
    keywords: list[str] = []

    def add(term: str) -> None:
        cleaned = normalize_space(term).strip("，,。；;：:（）()[]【】<>《》\"'")
        if not cleaned or cleaned in GENERIC_KEYWORD_STOPWORDS:
            return
        if TITLE_BROKER_TICKER_RE.fullmatch(cleaned):
            return
        if cleaned not in keywords:
            keywords.append(cleaned)

    for term in [*BIG_NAME_TERMS, *SEARCH_TERMS, *CONTRARIAN_TERMS]:
        if term.lower() in haystack.lower():
            add(term)
        if len(keywords) >= max_keywords:
            return keywords
    for part in re.split(r"[：:，,、；;|/()\[\]（）【】\s]+", strip_markdown_markup(title)):
        if 2 <= len(part) <= 14 and not TITLE_NOISE_RE.search(part):
            add(part)
        if len(keywords) >= max_keywords:
            return keywords
    pattern = re.compile(
        r"(?:中国[\u4e00-\u9fffA-Za-z0-9]{1,10}|"
        r"[\u4e00-\u9fffA-Za-z0-9]{1,10}(?:行业|市场|板块|周期|拐点|分水岭|定价权|供应链|资本开支|现金流|利润率|补贴|政策)|"
        r"(?:AI|GPU|ASIC|HDD|SSD|MLCC|SiC|DeFi|Robotaxi|Bitcoin|SpaceX|Tesla|Nvidia)[A-Za-z0-9-]*)"
    )
    for match in pattern.finditer(haystack):
        add(match.group(0))
        if len(keywords) >= max_keywords:
            break
    return keywords[:max_keywords]


def build_wechat_title_refinement_prompt(
    source_title: str,
    institution_name: str,
    article_excerpt: str,
    source_keywords: list[str] | None = None,
) -> str:
    keywords = "、".join(source_keywords or [])
    return f"""
你是 KC桌面 的微信公众号标题编辑。请只基于给定报告和文章内容，生成 6 个更适合微信搜一搜和转发的中文标题候选。

硬性规则：
1. 只返回 JSON：{{"titles":["标题1","标题2"]}}，不要解释。
2. 每个标题优先 18-34 个中文字符，最长 42 个字符。
3. 最多一个中文冒号。
4. 如果有机构名，只保留中文机构名，不要写 GS、JPM、JEF、NOM、BARC、MS、DB、Citi 等英文简称。
5. 标题要包含一个清晰钩子：大机构/大人物、可搜索主题词、反常识判断、市场误判、数据节点、政策/行业变量，至少命中其中两个。
6. 不要用“核心观点”“关键要点”“研报速览”“一文看懂”“震惊”“爆了”等机械或廉价词。
7. 单一公司/个股报告的标题只能写公司情况、行业变化、业务进展或竞争格局；禁止写目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO。
8. 不要夸大原文证据。

已识别机构：{institution_name or "未知"}
原报告标题：{source_title}
可用长尾关键词：{keywords or "从正文自行提取"}

文章摘录：
{article_excerpt[:2200]}
""".strip()
