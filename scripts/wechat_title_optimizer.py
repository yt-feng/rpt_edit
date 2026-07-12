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
INLINE_BROKER_ALIAS_PATTERN = (
    r"(?<![A-Za-z])(?:GS|JPM|JEF|NOM|BARC|DB|BofA|UBS|Citi|Citigroup|Goldman|"
    r"JPMorgan|Jefferies|Nomura|Barclays)(?![A-Za-z])"
)
INLINE_BROKER_ALIAS_RE = re.compile(INLINE_BROKER_ALIAS_PATTERN, re.I)
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
    "回报表现",
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
    "全球宏观",
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
    "观察提示",
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

FILENAME_DATE_SUFFIX_RE = re.compile(
    r"(?:[-_\s]+(?:19|20)?\d{6,8}|[-_\s]+(?:19|20)\d{2}[-_.]\d{1,2}[-_.]\d{1,2})$",
    re.I,
)
FILENAME_SERIAL_PREFIX_RE = re.compile(r"^(?:(?:\d{1,4})[-_]){2,5}")
FILENAME_INSTITUTION_EXTRA_ALIASES: dict[str, list[str]] = {
    "IMF": ["IMF", "International Monetary Fund"],
    "世界银行": ["World Bank", "WorldBank"],
    "国际清算银行": ["BIS", "Bank for International Settlements"],
    "经合组织": ["OECD"],
    "亚洲开发银行": ["ADB", "Asian Development Bank"],
    "世界经济论坛": ["WEF", "World Economic Forum"],
    "联合国贸发会议": ["UNCTAD"],
    "世界贸易组织": ["WTO", "World Trade Organization"],
    "麦肯锡": ["McKinsey", "McKinsey & Company"],
    "波士顿咨询": ["BCG", "Boston Consulting Group"],
    "贝恩": ["Bain", "Bain & Company"],
    "木头姐ARK": ["ARK", "ARK Invest"],
}
FILENAME_PHRASE_TRANSLATIONS: list[tuple[str, str]] = [
    ("market strategy japan", "日本市场策略"),
    ("corporate caution", "公司谨慎"),
    ("inflationary pressure", "通胀压力"),
    ("market strategy", "市场策略"),
    ("artificial intelligence", "人工智能"),
    ("supply chain", "供应链"),
    ("capital expenditure", "资本开支"),
    ("interest rates", "利率"),
    ("real estate", "房地产"),
]
FILENAME_WORD_TRANSLATIONS = {
    "and": "和",
    "japan": "日本",
    "china": "中国",
    "global": "全球",
    "market": "市场",
    "strategy": "策略",
    "corporate": "公司",
    "caution": "谨慎",
    "inflation": "通胀",
    "inflationary": "通胀",
    "pressure": "压力",
    "outlook": "展望",
    "update": "更新",
    "energy": "能源",
    "security": "安全",
    "consumer": "消费",
    "technology": "科技",
    "software": "软件",
    "hardware": "硬件",
    "semiconductor": "半导体",
    "semiconductors": "半导体",
    "automotive": "汽车",
    "autos": "汽车",
    "property": "地产",
    "rates": "利率",
    "trade": "贸易",
    "policy": "政策",
    "growth": "增长",
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


INSTITUTION_GENERIC_TITLE_PREFIX_RE = (
    r"(?:报告认为|报告指出|报告显示|报告称|报告|研报|研究|会议|观点|展望|"
    r"分析|简报|文章|数据显示|数据|指出|认为|称|表示)"
)
INSTITUTION_NAME_SUFFIX_RE = re.compile(r"(?:会议|报告|研究所|学会|公司|银行|咨询|组织|基金|论坛|委员会|集团|署|局|会)$")


def institution_title_stems(name: str) -> list[str]:
    base = canonicalize_institution_title_name(name).strip()
    if not base:
        return []
    candidates = [base]
    stem = INSTITUTION_NAME_SUFFIX_RE.sub("", base)
    if 2 <= len(stem) < len(base):
        candidates.append(stem)
    return sorted(dict.fromkeys(candidates), key=len, reverse=True)


def remove_redundant_institution_report_prefix(title: str) -> str:
    cleaned = normalize_space(title).replace(":", "：")
    if "：" not in cleaned:
        return cleaned
    head, tail = cleaned.split("：", 1)
    head = head.strip()
    tail = tail.strip()
    if not head or not tail:
        return cleaned
    for stem in institution_title_stems(head):
        escaped = re.escape(stem)
        patterns = [
            rf"^(?:{escaped})\s*(?:{INSTITUTION_GENERIC_TITLE_PREFIX_RE})\s*[：:，,、;；\-—]\s*",
            rf"^(?:{escaped})\s*[：:，,、;；\-—]\s*",
        ]
        for pattern in patterns:
            replaced = re.sub(pattern, "", tail, count=1, flags=re.I).strip(" ，,。；;：:、-—")
            if replaced != tail:
                tail = replaced
                break
    return f"{head}：{tail}" if tail else head


def remove_redundant_title_aliases(title: str) -> str:
    cleaned = clean_leading_report_slug(canonicalize_institution_title_name(title))
    cleaned = remove_redundant_institution_report_prefix(cleaned)
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
    cleaned = remove_redundant_institution_report_prefix(cleaned)
    cleaned = remove_inline_broker_aliases(cleaned)
    cleaned = re.sub(r"\s*[：:]\s*", "：", cleaned)
    cleaned = re.sub(r"：{2,}", "：", cleaned)
    return limit_title_colons(cleaned).strip("：: -—")


def remove_inline_broker_aliases(title: str) -> str:
    cleaned = normalize_space(title)
    if not INLINE_BROKER_ALIAS_RE.search(cleaned):
        return cleaned
    action_words = r"(?:称|表示|认为|预计|拆解|发现|观察|调升|下调|重申|警告|指出|提到)"
    cleaned = re.sub(
        rf"{INLINE_BROKER_ALIAS_PATTERN}\s*(?={action_words})",
        "报告",
        cleaned,
        flags=re.I,
    )
    cleaned = re.sub(
        rf"([：:，,、;；\-—])\s*{INLINE_BROKER_ALIAS_PATTERN}\s*([：:，,、;；\-—])?",
        r"\1",
        cleaned,
        flags=re.I,
    )
    cleaned = re.sub(INLINE_BROKER_ALIAS_PATTERN, "报告", cleaned, flags=re.I)
    cleaned = re.sub(r"报告报告", "报告", cleaned)
    cleaned = re.sub(r"[，,、]{2,}", "，", cleaned)
    cleaned = re.sub(r"：[,，、]+", "：", cleaned)
    return cleaned.strip(" ，,。；;：:、-—")


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
    min_chars = min(18, max(8, max_chars // 2))
    candidates: list[str] = []
    for match in re.finditer(r"[，,；;。！？!?]", text):
        candidate = text[: match.start()].strip("，,；;：: ")
        if min_chars <= len(candidate) <= max_chars:
            candidates.append(candidate)
    if candidates:
        return candidates[-1]

    cut = text[:max_chars].rstrip("，,；;：: ")
    next_char = text[max_chars : max_chars + 1]
    if next_char and re.search(r"[A-Za-z]", next_char):
        cut = re.sub(r"[A-Za-z]{1,8}$", "", cut).rstrip("，,；;：: ")
    cut = re.sub(
        r"(?:以及|或者|因为|如果|但是|只是|而是|正在|成为|显示|指出|包括|对于|通过|"
        r"需要|不是|还是|可以|已经|将|的|和|与|及|在|对|为|从|向|到|但|而|早期)$",
        "",
        cut,
    )
    return cut.strip("，,；;：: ")


def clean_wechat_title(
    title: str,
    institution_name: str = "",
    max_chars: int = 64,
    strict_wording: bool = True,
) -> str:
    cleaned = strip_markdown_markup(title)
    cleaned, _stock_changes = sanitize_wechat_stock_language(cleaned, strict_wording=strict_wording)
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


def strip_source_filename_noise(source_filename: str) -> str:
    """Return the semantic filename stem without archive numbering or dates."""
    cleaned = re.split(r"[/\\]", normalize_space(source_filename))[-1]
    cleaned = re.sub(r"\.(?:pdf|docx?|pptx?|xlsx?)$", "", cleaned, flags=re.I)
    cleaned = FILENAME_SERIAL_PREFIX_RE.sub("", cleaned)
    cleaned = re.sub(r"^(?:19|20)?\d{6,8}[-_]+", "", cleaned)
    for _ in range(2):
        cleaned = FILENAME_DATE_SUFFIX_RE.sub("", cleaned).strip(" -_")
    cleaned = re.sub(r"(?i)(?:^|[-_\s])shared(?=$|[-_\s])", "-", cleaned)
    cleaned = re.sub(r"[-_]{4,}", "---", cleaned)
    return cleaned.strip(" -_")


def filename_institution_aliases(institution_name: str) -> list[str]:
    expected = canonicalize_institution_title_name(institution_name)
    aliases: list[str] = [expected] if expected else []
    for cn_name, known_aliases in INSTITUTION_TITLE_ALIASES:
        if canonicalize_institution_title_name(cn_name) == expected:
            aliases.extend([cn_name, *known_aliases])
    aliases.extend(FILENAME_INSTITUTION_EXTRA_ALIASES.get(expected, []))
    return list(dict.fromkeys(alias for alias in aliases if alias))


def strip_filename_institution_prefix(source_filename: str, institution_name: str) -> str:
    cleaned = strip_source_filename_noise(source_filename)
    aliases = filename_institution_aliases(institution_name)
    if not aliases:
        return cleaned
    alias_group = "|".join(alias_pattern(alias) for alias in sorted(aliases, key=len, reverse=True))
    return re.sub(
        rf"^(?:{alias_group})\s*(?:[：:，,、;；\-—_/]+\s*)?",
        "",
        cleaned,
        count=1,
        flags=re.I,
    ).strip(" -_：:")


def translate_filename_terms_fallback(value: str) -> str:
    """Conservative phrase translation used only when DeepSeek is unavailable."""
    segment_token = "␞"
    translated = value
    translated = translated.replace("：", f" {segment_token} ").replace(":", f" {segment_token} ")
    translated = re.sub(r"-{2,}", f" {segment_token} ", translated)
    translated = re.sub(r"(?<=[A-Za-z0-9])[-_](?=[A-Za-z0-9])", " ", translated)
    translated = translated.replace("_", " ")
    for phrase, chinese in FILENAME_PHRASE_TRANSLATIONS:
        translated = re.sub(rf"\b{re.escape(phrase)}\b", chinese, translated, flags=re.I)
    for word, chinese in FILENAME_WORD_TRANSLATIONS.items():
        translated = re.sub(rf"\b{re.escape(word)}\b", chinese, translated, flags=re.I)
    translated = re.sub(rf"\s*{re.escape(segment_token)}\s*", "-", translated)
    translated = re.sub(r"\s*-\s*", "-", translated)
    translated = re.sub(r"(?<=[\u4e00-\u9fff])\s+|\s+(?=[\u4e00-\u9fff])", "", translated)
    translated = normalize_space(translated).replace(" -", "-").replace("- ", "-")
    return translated.strip(" -_：:")


def fit_filename_title(text: str, max_chars: int) -> str:
    cleaned = normalize_space(text)
    if len(cleaned) <= max_chars:
        return cleaned
    boundaries: list[str] = []
    for match in re.finditer(r"[-，,；;。！？!?]", cleaned):
        candidate = cleaned[: match.start()].strip(" -，,；;。！？!?")
        if 10 <= len(candidate) <= max_chars:
            boundaries.append(candidate)
    if boundaries:
        return boundaries[-1]
    return truncate_chars(cleaned, max_chars)


def clean_filename_wechat_title(title: str, institution_name: str = "", max_chars: int = 35) -> str:
    """Apply structural gates without reinterpreting the filename's meaning."""
    cleaned = strip_source_filename_noise(strip_markdown_markup(title))
    cleaned, _stock_changes = sanitize_wechat_stock_language(cleaned, strict_wording=False)
    cleaned = re.sub(r"^(?:标题|微信标题|公众号标题)\s*[：:]\s*", "", cleaned)
    cleaned = re.sub(r"[《》#>*]+", "", cleaned)
    cleaned = cleaned.replace("摩根斯坦利", "摩根士丹利").replace("美国银行", "美银")
    cleaned = remove_redundant_title_aliases(cleaned)
    if institution_name:
        cleaned = strip_unexpected_leading_institution_prefix(cleaned, institution_name)
        cleaned = ensure_title_has_institution_local(cleaned, institution_name)
    cleaned = remove_redundant_title_aliases(cleaned)
    cleaned = re.sub(r"\s*[：:]\s*", "：", cleaned)
    if "：" in cleaned:
        head, tail = cleaned.split("：", 1)
        tail = re.sub(r"[：:]", "-", tail)
        cleaned = f"{head}：{tail}"
    cleaned = re.sub(r"\s*-\s*", "-", cleaned)
    cleaned = re.sub(r"\s+", "", cleaned)
    cleaned = limit_title_colons(cleaned).strip("：: -—")
    return fit_filename_title(cleaned, max_chars).strip("：: -—")


def filename_title_fallback(source_filename: str, institution_name: str = "", max_chars: int = 35) -> str:
    body = strip_filename_institution_prefix(source_filename, institution_name)
    body = translate_filename_terms_fallback(body)
    if not body:
        body = "报告更新"
    title = ensure_title_has_institution_local(body, institution_name) if institution_name else body
    return clean_filename_wechat_title(title, institution_name, max_chars=max_chars)


def finalize_filename_wechat_title(
    translated_title: str,
    source_filename: str,
    institution_name: str = "",
    max_chars: int = 35,
) -> str:
    fallback = filename_title_fallback(source_filename, institution_name, max_chars=max_chars)
    candidate = clean_filename_wechat_title(translated_title, institution_name, max_chars=max_chars)
    candidate_body = candidate.split("：", 1)[-1] if candidate else ""
    if len(candidate_body) < 4:
        return fallback
    return candidate


def _title_semantic_body(title: str) -> str:
    body = clean_filename_wechat_title(title, "", max_chars=80)
    if "：" in body:
        body = body.split("：", 1)[1]
    body = re.sub(r"(?:报告|研究|更新|观点|展望)$", "", body)
    return re.sub(r"[^A-Za-z0-9\u4e00-\u9fff]+", "", body).lower()


def _character_ngrams(value: str, size: int = 2) -> set[str]:
    compact = _title_semantic_body(value)
    if len(compact) < size:
        return set(compact)
    return {compact[index : index + size] for index in range(len(compact) - size + 1)}


def filename_anchor_coverage(candidate: str, anchor: str) -> float:
    anchor_grams = _character_ngrams(anchor)
    if not anchor_grams:
        return 0.0
    return len(anchor_grams & _character_ngrams(candidate)) / len(anchor_grams)


def _numeric_title_tokens(value: str) -> set[str]:
    return set(re.findall(r"(?<![A-Za-z0-9])\d+(?:\.\d+)?", value or ""))


def filename_title_additions_are_supported(
    candidate: str,
    anchor: str,
    source_filename: str,
    evidence_text: str,
) -> bool:
    evidence = f"{strip_source_filename_noise(source_filename)}\n{evidence_text}"
    added_numbers = _numeric_title_tokens(candidate) - _numeric_title_tokens(anchor)
    if not added_numbers.issubset(_numeric_title_tokens(evidence)):
        return False
    added_names = [term for term in BIG_NAME_TERMS if term in candidate and term not in anchor]
    return all(term.lower() in evidence.lower() for term in added_names)


def choose_filename_anchored_title(
    candidates: list[str],
    source_filename: str,
    institution_name: str = "",
    max_chars: int = 35,
    evidence_text: str = "",
) -> str:
    """Let hooks improve a title only when filename semantics remain dominant."""
    fallback = filename_title_fallback(source_filename, institution_name, max_chars=max_chars)
    faithful_raw = candidates[0] if candidates else fallback
    anchor = finalize_filename_wechat_title(
        faithful_raw,
        source_filename,
        institution_name,
        max_chars=max_chars,
    )
    pool: list[str] = []
    for raw in [anchor, *candidates[1:], fallback]:
        cleaned = finalize_filename_wechat_title(raw, source_filename, institution_name, max_chars=max_chars)
        if cleaned and cleaned not in pool:
            pool.append(cleaned)
    if not pool:
        return fallback

    anchor_segments = [
        segment
        for segment in re.split(r"[-，,；;。！？!?]", anchor.split("：", 1)[-1])
        if len(_title_semantic_body(segment)) >= 4
    ]

    def preserves_each_segment(candidate: str) -> bool:
        return all(filename_anchor_coverage(candidate, segment) >= 0.30 for segment in anchor_segments)

    eligible = [
        candidate
        for candidate in pool
        if filename_anchor_coverage(candidate, anchor) >= 0.72
        and preserves_each_segment(candidate)
        and filename_title_additions_are_supported(
            candidate,
            anchor,
            source_filename,
            evidence_text,
        )
    ] or [anchor]

    def anchored_score(candidate: str) -> tuple[float, int]:
        coverage = filename_anchor_coverage(candidate, anchor)
        hook_hits = sum(1 for term in CONTRARIAN_TERMS if term in candidate)
        added_big_names = sum(1 for term in BIG_NAME_TERMS if term in candidate and term not in anchor)
        data_bonus = 3 if re.search(r"(?:\d+(?:\.\d+)?%?|20\d{2}|Q[1-4])", candidate) else 0
        length_bonus = 4 if 18 <= len(candidate) <= 35 else 1
        score = (
            coverage * 80
            + min(hook_hits, 2) * 6
            + min(added_big_names, 2) * 5
            + data_bonus
            + length_bonus
        )
        return score, -pool.index(candidate)

    return max(eligible, key=anchored_score)


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


def build_filename_title_translation_prompt(
    source_filename: str,
    institution_name: str,
    article_excerpt: str = "",
) -> str:
    cleaned_filename = strip_source_filename_noise(source_filename)
    filename_body = strip_filename_institution_prefix(cleaned_filename, institution_name)
    return f"""
你是微信公众号标题编辑。原始 PDF 文件名标题是最高权重的语义底稿；正文摘录只能用于补充文件名已经指向的数据节点、反常识差异或人物钩子，不能重新概括一篇与文件名不同的标题。

硬性规则：
1. 只返回 JSON：{{"titles":["忠实底稿","数据增强版","反常识增强版"]}}，固定三个候选，不要解释。
2. 删除文件扩展名、开头归档编号和末尾发布日期；不要删除文件名中的主题、地区、公司、数据或判断。
3. 已识别机构必须写中文名，并放在唯一的中文冒号前。不要保留英文机构简称。
4. 第一个候选是忠实中文底稿：按原文件名顺序翻译，允许为自然中文调整词序，但不能另选角度。
5. 第二个候选优先补充正文摘录中明确出现的数据节点；第三个候选优先补充明确的反常识差异、大机构或知名人物。没有可靠钩子时，直接重复忠实底稿，严禁编造。
6. 两个增强版仍必须保留底稿中的地区/对象、主题和核心判断；钩子只能补充或锐化，不能替换文件名命题。
7. 原文件名如果包含“主标题：副标题”或明显的双层结构，中文标题使用“主标题-副标题”；不要生成第二个冒号。
8. 尽量控制在 20-35 个字符。过长时只能压缩“报告、更新、研究”等文体词或使用更短的直译，不能截断句子，不能另选角度。
9. 常用专有名词和缩写可保留，例如 AI、GDP、CPI、GPU；其余普通英文应译成简体中文。
10. 不要输出“报告指出、报告认为、核心观点、关键要点、研报速览”等正文概括措辞。

已识别机构：{institution_name or "未知"}
原始文件名：{source_filename}
去除编号和日期后的文件名：{cleaned_filename}
待翻译的文件名正文：{filename_body or cleaned_filename}

正文第一段摘录（只用于验证数据或反常识钩子，不能替代文件名命题）：
{article_excerpt[:1800] or "无"}
""".strip()


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
8. 不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；用“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
9. 涉及中国、国内、内地、大陆、人民币、A股、港股时，必须使用中性客观表达，不写负面判断。
10. 不要夸大原文证据。

已识别机构：{institution_name or "未知"}
原报告标题：{source_title}
可用长尾关键词：{keywords or "从正文自行提取"}

文章摘录：
{article_excerpt[:2200]}
""".strip()
