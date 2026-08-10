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

from sensitive_content_guard import (
    neutralize_wechat_title,
    sanitize_wechat_stock_language,
    wechat_title_neutrality_issues,
)


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
    ("麦格理", ["Macquarie"]),
    ("法兴", ["SocGen", "Societe Generale"]),
    ("法国巴黎银行", ["BNP", "BNP Paribas"]),
    ("瑞穗", ["Mizuho"]),
    ("大和", ["Daiwa"]),
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
    r"一文看懂|一图胜千言|赋能.{0,10}(?:观点|行业)|支持我们的观点|"
    r"震惊|爆了|彻底反转|一夜变天)",
    re.I,
)
TITLE_ABSTRACT_RE = re.compile(r"(?:结构性变量|二阶影响|再定价框架|核心框架|底层逻辑|长期主义)")
GENERIC_FILENAME_TITLE_LABELS = (
    "研究笔记",
    "行业观察",
    "研究观察",
    "报告观察",
    "观察笔记",
    "专题观察",
    "公司观察",
    "研报解读",
    "报告解读",
)
GENERIC_FILENAME_TITLE_LABEL_RE = re.compile(
    rf"^(?:(?:{'|'.join(map(re.escape, GENERIC_FILENAME_TITLE_LABELS))}|观察)"
    r"\s*[：:，,、;；\-—]+\s*)+"
)
SOURCE_DOCUMENT_TYPE_RE = re.compile(
    r"(?<![A-Za-z])(?:research|quick|flash|company|industry|sector)\s+"
    r"(?:note|update|view|watch|observation|insights?)(?![A-Za-z])",
    re.I,
)
REQUIRED_ACRONYM_EXCLUSIONS = {
    "BOFA",
    "BARC",
    "CITI",
    "CORP",
    "DAILY",
    "DB",
    "FLASH",
    "GS",
    "HSBC",
    "INC",
    "JEF",
    "JPM",
    "LTD",
    "MS",
    "NOM",
    "NOTE",
    "PDF",
    "PLC",
    "PREVIEW",
    "QUICK",
    "REPORT",
    "RESEARCH",
    "REVIEW",
    "SHARED",
    "UBS",
    "UPDATE",
    "WEEKLY",
}

# Only topic-defining technical acronyms are literal requirements. Exchange
# suffixes (HK/US/TT/UN), document metadata (CIO/IT), and finance shorthand
# (EPS/ROIC/FX/USD) may be translated or omitted when natural Chinese keeps the
# same meaning. Treating every capitalized token as mandatory was the root
# cause of readable Chinese candidates losing to filename fragments.
REQUIRED_TECHNICAL_ACRONYMS = {
    "ADAS",
    "AGI",
    "AI",
    "API",
    "ASIC",
    "CCL",
    "CPI",
    "CPO",
    "CPU",
    "CSRD",
    "DRAM",
    "GDP",
    "GPU",
    "HBM",
    "HDD",
    "HDI",
    "IGBT",
    "LIDAR",
    "LLM",
    "MLCC",
    "NAND",
    "NPU",
    "PCB",
    "PFY",
    "PP",
    "PVC",
    "SAAS",
    "SSD",
    "TPU",
}

GENERIC_SERIES_SOURCE_RE = re.compile(
    r"^(?:(?:fx|macro|market|asia|china|global)\s*)?"
    r"(?:insights?|notes?|viewpoint|observations?|watch|overview)"
    r"(?:\s*[-:：]\s*(?:thoughts?|views?|notes?)\s+on\s+[^-:：]+)?$",
    re.I,
)
GENERIC_SERIES_TITLE_RE = re.compile(
    r"^(?:(?:FX|宏观|市场|行业|公司|全球|亚洲|中国|日本)?"
    r"(?:洞察|观察|观点|笔记|思考|简报|周报|月报|概览|综述|总览)"
    r"(?:[-，]?(?:对)?[^，。；;]{1,10}(?:的)?(?:思考|观察|观点))?"
    r"|宏观观察笔记)$",
    re.I,
)
VAGUE_OBSERVATION_TEMPLATE_RE = re.compile(
    r"^(?:研究主题与(?:行业|相关)变化观察|研究主题与相关数据观察|"
    r"[^，。；;：:]{2,18}业务与(?:近期|季度)数据观察|"
    r"[^，。；;：:]{2,18}数据与主题变化观察|"
    r"(?:行业规则|资金结构|资金工具|货币市场|统计方法|城市与住房数据|跨境贸易)"
    r"[^，。；;]{0,12}观察)$",
    re.I,
)
CONCRETE_TITLE_SIGNAL_RE = re.compile(
    r"(?:增长|下降|回落|回升|走弱|改善|加速|放缓|分化|挤出|转向|"
    r"拐点|触底|超预期|低于预期|高于预期|未到|决定|创(?:新高|纪录)|"
    r"压力|韧性|关键变量|分水岭|变化|数据|指标|框架|技术|流程|治理|运营|"
    r"应用|方法|规则|结构|组织|AI|同比|环比|\d)",
    re.I,
)
TITLE_DANGLING_SUFFIX_RE = re.compile(
    r"(?:[-—，,：:]\s*(?:关键|核心|以及|和|与|但|而|而是|不是|的|为|是)|"
    r"(?:以及|因为|如果|但是|而是|不是|显示|指出|包括|对于|通过|需要|"
    r"正在|成为))$"
)
LISTING_SUFFIX_RE = re.compile(r"(?:[A-Z]{1,8}|\d{3,6})\.[A-Z]{1,3}(?![A-Za-z])", re.I)
LONG_UNTRANSLATED_ENGLISH_RE = re.compile(r"[A-Za-z]{10,}")
TITLE_FORBIDDEN_PUBLIC_WORDING_RE = re.compile(
    r"(?:目标价|目标价格|买入|卖出|增持|减持|荐股|推荐|股票|个股|股价|股市|"
    r"投资|经济|财经|金融|理财|证券|券商|收益率|资产定价)",
    re.I,
)
MALFORMED_NUMERIC_TITLE_RE = re.compile(r"(?:\d+\.\d+\d+\.\d+|\d{7,})")
TITLE_REPAIR_PHRASES: list[tuple[str, str]] = [
    (r"(?:关键|核心)?股票(?:观点|思路|想法|选择)", "核心公司线索"),
    (r"(?:关键|核心)?个股(?:观点|思路|想法|选择)", "核心公司线索"),
    (r"\bkey\s+stock\s+ideas?\b", "核心公司线索"),
    (r"存储周期辩论", "存储周期讨论"),
    (r"\bASML\s+Holding\b", "ASML"),
    (r"(?:GS)?(?:OIL|EQUITY|CREDIT|MACRO)\s+ANALYST", ""),
    (r"(?:报告)?上调([\u4e00-\u9fffA-Za-z0-9.-]{2,16}?)(?:至|为)?买入", r"\1"),
]
TITLE_DIRECT_WORD_REPLACEMENTS: list[tuple[str, str]] = [
    (r"中国经济学", "中国宏观研究"),
    (r"国内经济学", "国内宏观研究"),
    (r"全球经济学|世界经济学", "全球宏观研究"),
    (r"中国经济", "中国宏观环境"),
    (r"国内经济", "国内宏观环境"),
    (r"全球经济|世界经济", "全球宏观环境"),
    (r"经济学", "宏观研究"),
    (r"经济", "宏观环境"),
    (r"投资银行|投行", "国际机构"),
    (r"投资者|投资人", "参与者"),
    (r"投资", "研究"),
    (r"财经", "研究"),
    (r"金融", "资金"),
    (r"股票市场|股市", "市场"),
    (r"股票|个股", "公司"),
    (r"股价", "报价"),
    (r"理财", "资金规划"),
    (r"证券|券商", "机构"),
    (r"收益率", "回报表现"),
    (r"资产定价", "市场定价"),
]

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
    "Portal Suite",
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
    for chinese_name, aliases in INSTITUTION_TITLE_ALIASES:
        if normalized.casefold() in {chinese_name.casefold(), *(alias.casefold() for alias in aliases)}:
            return chinese_name
    for chinese_name, aliases in FILENAME_INSTITUTION_EXTRA_ALIASES.items():
        if normalized.casefold() in {chinese_name.casefold(), *(alias.casefold() for alias in aliases)}:
            return chinese_name
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
        chinese_chars = len(re.findall(r"[\u4e00-\u9fff]", value))
        latin_chars = len(re.findall(r"[A-Za-z]", value))
        if chinese_chars >= 6 and "_" not in value and latin_chars <= chinese_chars * 2:
            return value
        numeric_range_token = "␟"
        value = re.sub(r"(?<=\d)-(?=\d)", numeric_range_token, value)
        value = value.replace("_", " ")
        value = re.sub(r"\s*-{2,}\s*", "，", value)
        value = re.sub(r"\s*-\s*", " ", value)
        return normalize_space(value).replace(numeric_range_token, "-")

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
    noise_clean_tail = re.sub(r"\b(?:Shared|Update|Quick Note|Report|Research)\b", "", tail, flags=re.I)
    slug_words = re.sub(r"[-_/]+", " ", noise_clean_tail)
    words = re.findall(r"AI|USD|CNY|RMB|[A-Z]+(?=[A-Z][a-z]|$)|[A-Z]?[a-z]+|\d+", slug_words)
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
    # In a mixed Chinese title, hyphens can be semantic: 9.8-14.8,
    # PayPal-Stripe, IL-23. Only the English-heavy slug branch above may
    # reinterpret them as filename separators.
    tail = normalize_space(noise_clean_tail).strip(" ，,")
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
    cleaned = remove_generic_filename_title_labels(cleaned)
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


def remove_source_document_type_noise(value: str) -> str:
    """Drop filename labels that describe the document, not its subject."""
    cleaned = SOURCE_DOCUMENT_TYPE_RE.sub(" ", value or "")
    cleaned = re.sub(r"\s*([：:，,、;；\-—])\s*(?=[：:，,、;；\-—])", r"\1", cleaned)
    cleaned = re.sub(r"(?:^|\s)[：:，,、;；\-—]+\s*", "-", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned.strip(" -_：:，,、;；—")


def remove_generic_filename_title_labels(title: str) -> str:
    """Remove vacuous translated labels while preserving the actual subject."""
    cleaned = normalize_space(title).replace(":", "：")
    prefix = ""
    body = cleaned
    if "：" in cleaned:
        head, tail = cleaned.split("：", 1)
        if len(head) <= 14:
            prefix = f"{head.strip()}："
            body = tail.strip()
    original_body = body
    body = GENERIC_FILENAME_TITLE_LABEL_RE.sub("", body).strip(" ，,、;；：:—-")
    body = re.sub(r"(?:的)?(?:观察笔记|研究笔记)$", "", body).strip(" ，,、;；：:—-")
    if len(re.sub(r"\s+", "", body)) < 4:
        body = original_body
    return f"{prefix}{body}".strip("：: -—")


def filename_institution_aliases(institution_name: str) -> list[str]:
    expected = canonicalize_institution_title_name(institution_name)
    aliases: list[str] = [expected] if expected else []
    for cn_name, known_aliases in INSTITUTION_TITLE_ALIASES:
        if canonicalize_institution_title_name(cn_name) == expected:
            aliases.extend([cn_name, *known_aliases])
    aliases.extend(FILENAME_INSTITUTION_EXTRA_ALIASES.get(expected, []))
    return list(dict.fromkeys(alias for alias in aliases if alias))


def normalize_title_institution_prefix(title: str, institution_name: str) -> str:
    """Replace an expected English prefix with one canonical Chinese prefix."""
    expected = canonicalize_institution_title_name(institution_name)
    cleaned = normalize_space(title).replace(":", "：")
    if not expected:
        return cleaned

    if "：" in cleaned:
        head, tail = cleaned.split("：", 1)
        if canonicalize_institution_title_name(head) == expected:
            cleaned = tail.strip()

    for alias in sorted(filename_institution_aliases(expected), key=len, reverse=True):
        if canonicalize_institution_title_name(alias) != expected:
            continue
        separator_pattern = rf"^(?:{alias_pattern(alias)})\s*[：:，,、;；\-—_/]+\s*"
        replaced = re.sub(separator_pattern, "", cleaned, count=1, flags=re.I).strip()
        if replaced != cleaned:
            cleaned = replaced
            break
        if re.fullmatch(r"[A-Z]{2,6}", alias):
            # DeepSeek sometimes concatenates the broker alias and the topic,
            # e.g. NOMFX. Strip NOM while preserving the topic-defining FX.
            replaced = re.sub(rf"^{re.escape(alias)}(?=[A-Z]{{2,}})", "", cleaned, count=1, flags=re.I)
            if replaced != cleaned:
                cleaned = replaced.strip()
                break
    return f"{expected}：{cleaned}".strip("： ") if cleaned else expected


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
    for pattern, replacement in TITLE_REPAIR_PHRASES:
        cleaned = re.sub(pattern, replacement, cleaned, flags=re.I)
    cleaned = LISTING_SUFFIX_RE.sub("", cleaned)
    cleaned, _stock_changes = sanitize_wechat_stock_language(cleaned, strict_wording=False)
    cleaned = re.sub(r"^(?:标题|微信标题|公众号标题)\s*[：:]\s*", "", cleaned)
    cleaned = re.sub(r"[《》#>*]+", "", cleaned)
    cleaned = cleaned.replace("摩根斯坦利", "摩根士丹利").replace("美国银行", "美银")
    cleaned = remove_redundant_title_aliases(cleaned)
    if institution_name:
        cleaned = strip_unexpected_leading_institution_prefix(cleaned, institution_name)
        cleaned = normalize_title_institution_prefix(cleaned, institution_name)
    cleaned = remove_redundant_title_aliases(cleaned)
    prefix = ""
    body = cleaned
    if "：" in cleaned:
        head, body = cleaned.split("：", 1)
        prefix = f"{head}："
    for pattern, replacement in TITLE_DIRECT_WORD_REPLACEMENTS:
        body = re.sub(pattern, replacement, body, flags=re.I)
    without_report = re.sub(
        r"^报告(?:指出|显示|认为|称|拆解|提示)?\s*[：:，,、;；\-—]*\s*",
        "",
        body,
    ).strip()
    if len(re.findall(r"[A-Za-z0-9\u4e00-\u9fff]", without_report)) >= 8:
        body = without_report
    cleaned = f"{prefix}{body}".strip("：: -—")
    cleaned = remove_generic_filename_title_labels(cleaned)
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
    body = remove_source_document_type_noise(body)
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


def required_filename_terms(source_filename: str, institution_name: str = "") -> list[str]:
    """Return technical acronyms that the Chinese title must keep verbatim."""
    body = strip_filename_institution_prefix(source_filename, institution_name)
    terms: list[str] = []
    for token in re.findall(r"(?<![A-Za-z0-9])([A-Z]{2,8})(?![A-Za-z0-9])", body):
        upper = token.upper()
        if (
            upper in REQUIRED_ACRONYM_EXCLUSIONS
            or upper not in REQUIRED_TECHNICAL_ACRONYMS
            or upper in terms
        ):
            continue
        terms.append(upper)
    return terms[:6]


def missing_required_filename_terms(candidate: str, required_terms: list[str]) -> list[str]:
    haystack = (candidate or "").upper()
    return [term for term in required_terms if term.upper() not in haystack]


def source_uses_generic_series_title(source_filename: str, institution_name: str = "") -> bool:
    """Return True when the filename names a series but not a readable thesis."""
    body = strip_filename_institution_prefix(source_filename, institution_name)
    body = re.sub(r"\s+", " ", body).strip(" -_：:")
    if GENERIC_SERIES_SOURCE_RE.fullmatch(body):
        return True
    last_segment = re.split(r"\s*[-:：]\s*", body)[-1]
    if re.fullmatch(
        r"(?:[A-Za-z0-9& ]+\s+)?(?:overview|insights?|notes?|viewpoint|observations?|watch)",
        last_segment,
        flags=re.I,
    ):
        return True
    compact = re.sub(r"[\s_\-：:]+", "", body)
    return bool(
        re.fullmatch(
            r"(?:宏观|市场|行业|公司|全球|亚洲|中国|日本)?(?:洞察|观察|观点|笔记|思考|简报|周报|月报|概览|综述|总览)",
            compact,
        )
    )


def title_is_generic_series(title: str) -> bool:
    body = normalize_space(title).replace(":", "：")
    if "：" in body:
        body = body.split("：", 1)[1]
    body = re.sub(r"^(?:MS|NOM|JPM|JEF|BARC|BofA|UBS|Citi)(?=[A-Z])", "", body, flags=re.I)
    compact = re.sub(r"[\s_]+", "", body).strip(" ，,。；;：:、-—")
    if GENERIC_SERIES_TITLE_RE.fullmatch(compact):
        return True
    has_generic_label = bool(re.search(r"(?:洞察|观察|观点|笔记|思考|简报|周报|月报|概览|综述|总览)", compact))
    return has_generic_label and not CONCRETE_TITLE_SIGNAL_RE.search(compact) and len(compact) <= 18


def title_quality_issues(
    title: str,
    institution_name: str = "",
    source_filename: str = "",
) -> list[str]:
    """Find defects that must never reach a WeChat draft title."""
    cleaned = normalize_space(title).replace(":", "：").strip(" ，,。；;：:、-—")
    body = cleaned.split("：", 1)[1] if "：" in cleaned else cleaned
    body = body.strip(" ，,。；;：:、-—")
    issues: list[str] = []
    semantic_chars = re.findall(r"[A-Za-z0-9\u4e00-\u9fff]", body)
    if len(semantic_chars) < 8:
        issues.append("body_too_short")
    if title_is_generic_series(cleaned):
        issues.append("generic_series_title")
    if VAGUE_OBSERVATION_TEMPLATE_RE.fullmatch(body):
        issues.append("vague_observation_template")
    if TITLE_NOISE_RE.search(body):
        issues.append("promotional_or_template_noise")
    if body.endswith("主题进展与关键变化"):
        issues.append("generic_emergency_title")
    if TITLE_DANGLING_SUFFIX_RE.search(body):
        issues.append("dangling_suffix")
    segments = [item.strip(" ，,。；;：:、-—") for item in re.split(r"[-—]", body) if item.strip()]
    if len(segments) >= 2:
        tail = segments[-1]
        if len(re.findall(r"[A-Za-z0-9\u4e00-\u9fff]", tail)) < 4 or tail in {
            "关键",
            "核心",
            "观点",
            "观察",
            "更新",
            "讨论",
            "研究",
            "报告",
            "笔记",
            "分析",
            "展望",
            "思考",
        }:
            issues.append("incomplete_last_segment")
    if LISTING_SUFFIX_RE.search(body):
        issues.append("listing_suffix")
    if LONG_UNTRANSLATED_ENGLISH_RE.search(body):
        issues.append("long_untranslated_english")
    latin_chars = len(re.findall(r"[A-Za-z]", body))
    chinese_chars = len(re.findall(r"[\u4e00-\u9fff]", body))
    if latin_chars >= 12 and latin_chars > max(10, chinese_chars * 2):
        issues.append("english_heavy_fragment")
    if TITLE_FORBIDDEN_PUBLIC_WORDING_RE.search(body):
        issues.append("forbidden_public_wording")
    if MALFORMED_NUMERIC_TITLE_RE.search(body):
        issues.append("malformed_numeric_range")
    if re.search(r"(?:至|达|为|约|上调至|下调至)\d+(?:\.\d+)?$", body):
        issues.append("bare_trailing_number")
    if source_filename and source_uses_generic_series_title(source_filename, institution_name):
        if not CONCRETE_TITLE_SIGNAL_RE.search(body):
            issues.append("series_missing_body_thesis")
    return list(dict.fromkeys(issues))


def ensure_publishable_neutral_title(
    title: str,
    institution_name: str = "",
    source_filename: str = "",
    max_chars: int = 35,
    evidence_text: str = "",
) -> tuple[str, list[str]]:
    """Return a complete neutral title; title defects must never drop an article."""
    cleaned = clean_filename_wechat_title(title, institution_name, max_chars=max_chars)
    neutralized, changes = neutralize_wechat_title(cleaned, institution_name)
    neutralized = clean_filename_wechat_title(
        neutralized,
        institution_name,
        max_chars=max_chars,
    )
    issues = title_quality_issues(neutralized, institution_name, source_filename)
    if not issues:
        return neutralized, changes

    source_fallback = filename_title_fallback(source_filename, institution_name, max_chars=max_chars)
    source_fallback, source_changes = neutralize_wechat_title(source_fallback, institution_name)
    source_fallback = clean_filename_wechat_title(
        source_fallback,
        institution_name,
        max_chars=max_chars,
    )
    source_issues = title_quality_issues(source_fallback, institution_name, source_filename)
    if not source_issues:
        return source_fallback, list(dict.fromkeys([*changes, *source_changes, "quality_source_fallback"]))

    if evidence_text:
        evidence_fallback = evidence_title_fallback(
            evidence_text,
            source_filename,
            institution_name,
            max_chars=max_chars,
        )
        evidence_fallback, evidence_changes = neutralize_wechat_title(evidence_fallback, institution_name)
        evidence_fallback = clean_filename_wechat_title(
            evidence_fallback,
            institution_name,
            max_chars=max_chars,
        )
        evidence_issues = title_quality_issues(evidence_fallback, institution_name, source_filename)
        if not evidence_issues:
            return evidence_fallback, list(dict.fromkeys([
                *changes,
                *evidence_changes,
                "quality_evidence_fallback",
            ]))

    required_terms = required_filename_terms(source_filename, institution_name)
    term_block = "、".join(required_terms[:3])
    safe_body = f"{term_block}技术与相关数据观察" if term_block else "研究主题与相关数据观察"
    fallback = clean_filename_wechat_title(safe_body, institution_name, max_chars=max_chars)
    fallback, fallback_neutralization = neutralize_wechat_title(fallback, institution_name)
    fallback = clean_filename_wechat_title(fallback, institution_name, max_chars=max_chars)
    fallback_issues = title_quality_issues(fallback, institution_name, source_filename)
    if fallback_issues:
        fallback = clean_filename_wechat_title(
            "行业技术与相关数据观察",
            institution_name,
            max_chars=max_chars,
        )
    quality_change = f"quality_fallback:{','.join(issues)}"
    return fallback, list(dict.fromkeys([*changes, *fallback_neutralization, quality_change]))


def ensure_required_filename_terms(
    candidate: str,
    required_terms: list[str],
    institution_name: str = "",
    max_chars: int = 35,
) -> str:
    """Repair a fallback deterministically when truncation omitted an acronym."""
    if not missing_required_filename_terms(candidate, required_terms):
        return candidate
    prefix = ""
    body = candidate
    if "：" in candidate:
        head, body = candidate.split("：", 1)
        prefix = f"{head}："
    for term in required_terms:
        body = re.sub(re.escape(term), "", body, flags=re.I)
    term_block = "与".join(required_terms)
    tail_budget = max(0, max_chars - len(prefix) - len(term_block))
    tail = fit_filename_title(body.strip(" ，,、;；：:—-"), tail_budget) if tail_budget else ""
    rebuilt = f"{prefix}{term_block}{tail}"
    return clean_filename_wechat_title(rebuilt, institution_name, max_chars=max_chars)


def evidence_title_fallback(
    evidence_text: str,
    source_filename: str,
    institution_name: str = "",
    max_chars: int = 35,
) -> str:
    """Choose a complete body sentence when every generated title is malformed."""
    required_terms = required_filename_terms(source_filename, institution_name)
    candidates: list[tuple[int, str]] = []
    for index, raw in enumerate(re.split(r"[\n。！？!?；;]+", evidence_text or "")):
        clause = normalize_space(raw).strip(" ，,。；;：:、-—")
        if not clause or re.search(r"(?:(?:编辑|KC)评论|免责声明|仅供|公众号|星标|扫码|更新信息)", clause, re.I):
            continue
        candidate = clean_filename_wechat_title(clause, institution_name, max_chars=max_chars)
        if missing_required_filename_terms(candidate, required_terms):
            continue
        if title_quality_issues(candidate, institution_name, source_filename):
            continue
        score = 0
        score += min(len(_numeric_title_tokens(candidate)), 2) * 8
        score += 6 if CONCRETE_TITLE_SIGNAL_RE.search(candidate) else 0
        score += 4 if 16 <= len(candidate) <= max_chars else 0
        score -= min(index, 8)
        candidates.append((score, candidate))
    if candidates:
        return max(candidates, key=lambda item: item[0])[1]

    fallback = filename_title_fallback(source_filename, institution_name, max_chars=max_chars)
    if not title_quality_issues(fallback, institution_name, source_filename):
        return fallback
    institution = canonicalize_institution_title_name(institution_name)
    term_block = "与".join(required_terms)
    safe_body = f"{term_block}技术与相关数据观察" if term_block else "研究主题与相关数据观察"
    return clean_filename_wechat_title(safe_body, institution, max_chars=max_chars)


def _contrarian_additions_supported(candidate: str, anchor: str, evidence: str) -> bool:
    added = [term for term in CONTRARIAN_TERMS if term in candidate and term not in anchor]
    for term in added:
        if term in evidence:
            continue
        if term == "反而" and re.search(r"(?:但|却|然而|不升反降|不降反升)", evidence):
            continue
        if term in {"不是", "而是"} and re.search(r"不是.{1,30}而是", evidence):
            continue
        return False
    return True


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
    if not all(term.lower() in evidence.lower() for term in added_names):
        return False
    return _contrarian_additions_supported(candidate, anchor, evidence)


def _title_hook_signals(candidate: str, anchor: str) -> dict[str, list[str]]:
    return {
        "added_numbers": sorted(_numeric_title_tokens(candidate) - _numeric_title_tokens(anchor)),
        "added_contrarian_terms": [
            term for term in CONTRARIAN_TERMS if term in candidate and term not in anchor
        ],
        "added_big_names": [term for term in BIG_NAME_TERMS if term in candidate and term not in anchor],
    }


def decide_filename_anchored_title(
    candidates: list[str],
    source_filename: str,
    institution_name: str = "",
    max_chars: int = 35,
    evidence_text: str = "",
) -> tuple[str, dict[str, Any]]:
    """Select a title and return an auditable record of every deterministic gate."""
    institution_name = canonicalize_institution_title_name(institution_name)
    required_terms = required_filename_terms(source_filename, institution_name)
    fallback = filename_title_fallback(source_filename, institution_name, max_chars=max_chars)
    fallback = ensure_required_filename_terms(
        fallback,
        required_terms,
        institution_name,
        max_chars=max_chars,
    )
    faithful_raw = candidates[0] if candidates else fallback
    faithful = finalize_filename_wechat_title(
        faithful_raw,
        source_filename,
        institution_name,
        max_chars=max_chars,
    )
    faithful_missing = missing_required_filename_terms(faithful, required_terms)
    generic_source = source_uses_generic_series_title(source_filename, institution_name)
    generated_pool: list[str] = []
    for raw in candidates:
        cleaned = finalize_filename_wechat_title(raw, source_filename, institution_name, max_chars=max_chars)
        if cleaned and cleaned not in generated_pool:
            generated_pool.append(cleaned)
    pool = list(generated_pool)
    if fallback and fallback not in pool:
        pool.append(fallback)

    def base_reasons(candidate: str) -> list[str]:
        reasons: list[str] = []
        missing_terms = missing_required_filename_terms(candidate, required_terms)
        if missing_terms:
            reasons.append("missing_required_terms=" + ",".join(missing_terms))
        reasons.extend(title_quality_issues(candidate, institution_name, source_filename))
        return reasons

    valid_generated = [candidate for candidate in generated_pool if not base_reasons(candidate)]
    if generic_source:
        concrete_generated = [
            candidate
            for candidate in valid_generated
            if not title_is_generic_series(candidate) and CONCRETE_TITLE_SIGNAL_RE.search(candidate)
        ]
        anchor = concrete_generated[0] if concrete_generated else (valid_generated[0] if valid_generated else "")
    else:
        anchor = valid_generated[0] if valid_generated else ""

    fallback_valid = not base_reasons(fallback)
    emergency = evidence_title_fallback(
        evidence_text,
        source_filename,
        institution_name,
        max_chars=max_chars,
    )
    if not anchor:
        anchor = fallback if fallback_valid else emergency
    for item in [anchor, emergency]:
        if item and item not in pool:
            pool.append(item)
    if not pool:
        pool = [emergency]

    anchor_segments = [
        segment
        for segment in re.split(r"[-，,；;。！？!?]", anchor.split("：", 1)[-1])
        if len(_title_semantic_body(segment)) >= 4
    ]

    def preserves_each_segment(candidate: str) -> bool:
        return all(filename_anchor_coverage(candidate, segment) >= 0.30 for segment in anchor_segments)

    coverage_threshold = 0.62 if required_terms else 0.72
    eligible: list[str] = []
    rejected: list[dict[str, Any]] = []
    for candidate in pool:
        reasons = base_reasons(candidate)
        coverage = filename_anchor_coverage(candidate, anchor)
        if generic_source:
            if title_is_generic_series(candidate) or not CONCRETE_TITLE_SIGNAL_RE.search(candidate):
                reasons.append("series_title_without_concrete_thesis")
        else:
            if coverage < coverage_threshold:
                reasons.append(f"anchor_coverage={coverage:.2f}")
            if not preserves_each_segment(candidate):
                reasons.append("missing_anchor_segment")
        if not filename_title_additions_are_supported(candidate, faithful, source_filename, evidence_text):
            reasons.append("unsupported_hook_addition")
        if reasons:
            rejected.append({"title": candidate, "reasons": reasons})
        else:
            eligible.append(candidate)
    if not eligible:
        eligible = [emergency]

    def anchored_score(candidate: str) -> tuple[float, int]:
        coverage = filename_anchor_coverage(candidate, anchor)
        signals = _title_hook_signals(candidate, faithful)
        data_bonus = min(len(signals["added_numbers"]), 2) * 12
        # Unsupported additions were rejected above. A source-backed contrast
        # is useful information, so reward it modestly instead of suppressing it.
        contrast_bonus = min(len(signals["added_contrarian_terms"]), 2) * 6
        name_bonus = min(len(signals["added_big_names"]), 2) * 5
        existing_data_bonus = 3 if re.search(r"(?:\d+(?:\.\d+)?%?|20\d{2}|Q[1-4])", candidate) else 0
        concrete_bonus = 10 if generic_source and CONCRETE_TITLE_SIGNAL_RE.search(candidate) else 0
        length_bonus = 4 if 18 <= len(candidate) <= 35 else 1
        score = coverage * 55 + data_bonus + contrast_bonus + name_bonus + existing_data_bonus + concrete_bonus + length_bonus
        return score, -pool.index(candidate)

    selected = max(eligible, key=anchored_score)
    signals = _title_hook_signals(selected, faithful)
    selected_issues = title_quality_issues(selected, institution_name, source_filename)
    if selected == emergency and selected not in valid_generated and not fallback_valid:
        selection_reason = "evidence_or_emergency_fallback"
    elif generic_source:
        selection_reason = "series_body_thesis"
    elif selected != faithful and any(signals.values()):
        selection_reason = "supported_hook"
    elif faithful_missing and selected == fallback:
        selection_reason = "fallback_missing_required_terms"
    elif candidates:
        selection_reason = "faithful_filename_anchor"
    else:
        selection_reason = "deterministic_fallback"
    decision = {
        "source_filename": source_filename,
        "cleaned_source_title": strip_source_filename_noise(source_filename),
        "institution_name": institution_name,
        "required_terms": required_terms,
        "deterministic_fallback": fallback,
        "raw_candidates": candidates,
        "cleaned_candidates": pool,
        "faithful_candidate_missing_terms": faithful_missing,
        "faithful_candidate_quality_issues": title_quality_issues(
            faithful,
            institution_name,
            source_filename,
        ),
        "generic_series_source": generic_source,
        "rejected_candidates": rejected,
        "selected_title": selected,
        "selection_reason": selection_reason,
        "selected_quality_issues": selected_issues,
        "needs_model_repair": bool(selected_issues) or selection_reason == "evidence_or_emergency_fallback",
        "hook_signals": signals,
        "removed_generic_labels": [
            label
            for label in GENERIC_FILENAME_TITLE_LABELS
            if any(label in raw for raw in candidates) and label not in selected
        ],
    }
    return selected, decision


def choose_filename_anchored_title(
    candidates: list[str],
    source_filename: str,
    institution_name: str = "",
    max_chars: int = 35,
    evidence_text: str = "",
) -> str:
    """Let hooks improve a title only when filename semantics remain dominant."""
    selected, _decision = decide_filename_anchored_title(
        candidates,
        source_filename,
        institution_name,
        max_chars=max_chars,
        evidence_text=evidence_text,
    )
    return selected


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
    score += min(len(contrarian_hits), 2) * 2
    score -= len(wechat_title_neutrality_issues(cleaned)) * 12
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
    institution_name = canonicalize_institution_title_name(institution_name)
    cleaned_filename = strip_source_filename_noise(source_filename)
    filename_body = strip_filename_institution_prefix(cleaned_filename, institution_name)
    required_terms = required_filename_terms(source_filename, institution_name)
    generic_series_source = source_uses_generic_series_title(source_filename, institution_name)
    hook_snippets = []
    for clause in re.split(r"[。！？!?；;\n]+", normalize_space(article_excerpt)):
        clause = clause.strip(" ，,")
        if not clause:
            continue
        has_data = re.search(r"(?:\d+(?:\.\d+)?%?|20\d{2}|Q[1-4]|同比|环比)", clause)
        has_concrete_topic = re.search(r"(?:AI|半导体|汽车|软件|能源|供应链|消费|零售|企业|市场)", clause, re.I)
        if has_data or has_concrete_topic:
            hook_snippets.append(clause[:90])
        if len(hook_snippets) >= 5:
            break
    return f"""
你是微信公众号标题编辑。原始 PDF 文件名标题是最高权重的语义底稿；正文摘录只能用于补充文件名已经指向的数据节点、时间范围、技术或行业事实，不能重新概括一篇与文件名不同的标题。

硬性规则：
1. 只返回 JSON：{{"titles":["忠实底稿","数据增强版","主题增强版"]}}，固定三个候选，不要解释。
2. 删除文件扩展名、开头归档编号和末尾发布日期；保留文件名中的主题、地区、公司和数据。原题中的好坏评价或敏感标签必须中性化，不要求逐字保留。
3. 已识别机构必须写中文名，并放在唯一的中文冒号前。不要保留英文机构简称。
4. 第一个候选通常是忠实中文底稿：按原文件名顺序完整翻译，允许为自然中文和中性表达调整词序，但不能另选角度。若文件名只是 Insights、Notes、Viewpoint、Thoughts on 等系列名，三个候选都必须结合正文写出本期实际对象和事实主题，不能直译成“宏观观察笔记”“洞察”“对某事的思考”。
5. 第二个候选优先补充正文摘录中明确出现的日期或数据节点；第三个候选优先补充对象、技术、行业或研究范围。允许使用原文明确支持的增长、下降、创纪录、超预期、指引变化、拐点、对比以及“为什么/如何”等事实型钩子；不使用煽动、攻击、输赢、荐股或无证据的好坏判断。没有可靠事实时可以重复忠实底稿，严禁编造。
6. 两个增强版仍必须保留底稿中的地区/对象和研究主题；钩子只能补充事实，不能加入好坏判断，也不能把标题写成争辩或结论宣判。
7. 原文件名如果包含“主标题：副标题”或明显的双层结构，中文标题使用“主标题-副标题”；不要生成第二个冒号。
8. 尽量控制在 20-35 个字符。过长时只能压缩“报告、更新、研究”等文体词或使用更短的直译，不能截断句子，不能另选角度。
9. 下方“必须原样保留的技术词”只包含定义主题的技术缩写，每一个都必须出现在三个候选中。例如原名是“PCB CCL update”，不得写成只有“CCL更新”，必须同时保留 PCB 和 CCL。交易所后缀 HK/US/TT/UN，以及 EPS、ROIC、FX、USD、CIO、IT 等可自然译成中文，不要求机械保留英文。
10. Research note、quick note、industry update、sector view 只是文档类型，不是读者关心的主题。不要翻成“研究笔记、行业观察、研究观察、观察笔记”；直接从真正的对象和结论开始。
11. 常用专有名词和技术缩写可保留，例如 AI、GDP、CPI、GPU；其余普通英文必须译成简体中文。删除 1880.HK、MSFT.US 等上市代码，不得出现 TourismGroupDutyFree、WhereAreWe 这类英文文件名残片。
12. Key Stock Ideas 必须按语义写成“核心公司线索”或具体公司变化，不得写“股票观点、推荐、买入”等措辞。
13. 标题要陈述“谁、什么主题、哪组数据、哪个时间范围”。禁止危机、骗局、崩盘、恐慌、失败、赢家、输家、高估、低估、抄底、稳赚、必涨、震惊、唯一真相等煽动、对立或行动建议；但原文支持的增长、下降、压力、盈利、创纪录、超预期、改善、回升、指引上调/下调等研究事实可以保留。
14. 涉及中国宏观、人民币汇率、信贷、债务、权益、房地产、就业、财政或监管时，仍要保留原报告的具体公司、城市、数据、时间和研究对象；只中性化确有必要的立场化词语，不能一律改成“近期数据、资金结构、市场主题”等空泛概括。
15. 原报告涉及军事、国防、战争、选举、政党、制裁、地缘政治等议题时，标题不要出现这些词；只写报告中可公开表达的行业、技术、运营、数据或区域研究主题，例如“航空运维与AI技术应用观察”。不要因此放弃生成标题。
16. 不要直接写“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”；使用“宏观环境、研究、资金、公司、报价、市场、回报表现、市场定价”等中性表述。
17. 不要输出“报告指出、报告认为、核心观点、关键要点、研报速览”等正文概括措辞。
18. 禁止使用“研究主题与行业变化观察”“某公司业务与近期数据观察”“某行业数据与主题变化观察”等占位标题。除非原文件名本身没有任何主题且正文也没有证据，否则标题必须出现具体公司、产品、技术、地区或数据中的至少两项。
19. 输出前逐条自检：冒号或短横线后的每个分句都必须完整；不得以“关键、核心、以及、和、与、但、而是、的、为”结尾；标题正文不能只有 AI、更新、观察等一个词。读者必须能直接看懂研究对象和事实主题，且不能感到标题在要求其认同某种立场。

合格结构示例（只学习结构，不复制事实）：
- 高盛：药明康德2Q26收入增47.7%，全年指引再上调
- 德意志银行：AI巨头占四成30年期新发行，指数集中度上升
- 花旗：铜价中长期逻辑-2027年供需缺口约40万吨

已识别机构：{institution_name or "未知"}
原始文件名：{source_filename}
去除编号和日期后的文件名：{cleaned_filename}
待翻译的文件名正文：{filename_body or cleaned_filename}
必须原样保留的技术词：{"、".join(required_terms) or "无"}
文件名是否只是系列名：{"是，必须从正文补足本期对象和事实主题" if generic_series_source else "否，以文件名命题为最高权重"}

可用事实型钩子证据（只可从这里选，不得改数字或扩大含义）：
{chr(10).join(f"- {item}" for item in hook_snippets) or "无"}

正文第一段摘录（只用于验证日期、数据、技术或行业事实，不能替代文件名命题）：
{article_excerpt[:1800] or "无"}
""".strip()


def build_filename_title_repair_prompt(
    source_filename: str,
    institution_name: str,
    article_excerpt: str,
    previous_candidates: list[str],
    quality_issues: list[str],
) -> str:
    """Build a second-pass prompt used only after deterministic gates fail."""
    institution_name = canonicalize_institution_title_name(institution_name)
    required_terms = required_filename_terms(source_filename, institution_name)
    generic_series = source_uses_generic_series_title(source_filename, institution_name)
    return f"""
你是微信公众号标题纠错编辑。上一轮标题未通过程序硬校验，请重新生成三个完整中文标题。只返回 JSON：{{"titles":["标题1","标题2","标题3"]}}，不要解释。

必须做到：
1. 机构只写“{institution_name or '已识别机构'}”，放在唯一的中文冒号前。
2. 普通英文全部译成简体中文；删除 HK/US/TT/UN 上市后缀和代码；只保留下方指定的技术缩写。
3. 每个标题正文必须说明清楚对象、主题和变化，不能只写 AI、更新、观察、关键、核心，也不能以连接词或“关键/核心”收尾。
4. 任何短横线或逗号后的分句都必须完整，控制在 20-35 个字符，宁可重写短句，绝不从中间截断。
5. 不要写研究笔记、行业观察、宏观观察笔记、报告解读、核心观点、关键要点。
6. Key Stock Ideas 写成“核心公司线索”或具体公司变化，不写股票观点、推荐、买入、卖出、目标价。
7. 原文件名若只是系列名称，必须依据正文摘录写本期实际对象和事实主题，不能翻译系列名充数。
8. 不直接写经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价，改用中性表述。
9. 只写研究对象、时间、数据或主题，不制造攻击和情绪对立。禁止危机、骗局、崩盘、恐慌、失败、赢家、输家、高估、低估、抄底、稳赚、必涨、震惊、唯一真相及“不是……而是……”句式；原文明确支持的增长、下降、压力、盈利、创纪录、超预期、改善、回升和指引变化可以保留。
10. 涉及中国宏观、人民币汇率、信贷、债务、权益、房地产、就业、财政或监管时，保留具体公司、城市、数据、时间和研究对象，只中性化确有必要的立场词，不能退化成“近期数据、资金结构、市场主题”等空泛标题。
11. 涉及军事、国防、战争、选举、政党、制裁、地缘政治等议题时，公开标题只写可公开表达的行业、技术、运营、数据或区域主题，不出现敏感标签，也不能放弃生成。
12. 不得编造正文没有的数据、人物或判断。
13. 禁止“研究主题与行业变化观察”“某公司业务与近期数据观察”“某行业数据与主题变化观察”等占位标题；必须优先保留原文件名的公司、产品、技术和主题，并用正文证据补足一个事实钩子。

原始文件名：{source_filename}
必须保留的技术缩写：{"、".join(required_terms) or "无"}
是否为系列名称：{"是" if generic_series else "否"}
上一轮候选：{json.dumps(previous_candidates, ensure_ascii=False)}
未通过原因：{"、".join(quality_issues) or "候选均被语义或完整性校验拒绝"}
正文摘录：
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
你是 Portal Suite 的微信公众号标题编辑。请只基于给定报告和文章内容，生成 6 个更适合微信搜一搜和转发的中文标题候选。

硬性规则：
1. 只返回 JSON：{{"titles":["标题1","标题2"]}}，不要解释。
2. 每个标题优先 18-34 个中文字符，最长 42 个字符。
3. 最多一个中文冒号。
4. 如果有机构名，只保留中文机构名，不要写 GS、JPM、JEF、NOM、BARC、MS、DB、Citi 等英文简称。
5. 标题要包含一个清晰、可核验的事实钩子：大机构/大人物、具体公司、可搜索主题词、数据节点、时间范围、技术或行业对象，至少命中其中两个。允许原文支持的反常识事实、增长/下降、创纪录、超预期、指引变化、对比以及“为什么/如何”；不要使用煽动、攻击、输赢、荐股或无证据宣判。
6. 不要用“核心观点”“关键要点”“研报速览”“一文看懂”“震惊”“爆了”等机械或廉价词。
7. 单一公司/个股报告的标题只能写公司情况、行业变化、业务进展或竞争格局；禁止写目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO。
8. 不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；用“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
9. 标题不得煽动情绪或评价谁输谁赢。禁止危机、骗局、崩盘、恐慌、失败、赢家、输家、高估、低估、抄底、稳赚、必涨、震惊、唯一真相，以及“不是……而是……”等对立式表达；原文明确支持的增长、下降、压力、盈利、创纪录、超预期、改善、回升和指引变化可以保留。
10. 涉及中国宏观、人民币汇率、信贷、债务、权益、房地产、就业、财政或监管时，保留具体公司、城市、数据、时间和研究对象，只中性化确有必要的立场词，不能退化成空泛的“近期数据、资金结构、市场主题”。
11. 涉及军事、国防、战争、选举、政党、制裁、地缘政治等议题时，公开标题只写行业、技术、运营、数据或区域研究主题，不出现敏感标签，但仍需生成可发布标题。
12. 不要夸大原文证据。
13. 禁止“研究主题与行业变化观察”“某公司业务与近期数据观察”“某行业数据与主题变化观察”等占位标题。标题必须出现具体公司、产品、技术、地区或数据中的至少两项。

已识别机构：{institution_name or "未知"}
原报告标题：{source_title}
可用长尾关键词：{keywords or "从正文自行提取"}

文章摘录：
{article_excerpt[:2200]}
""".strip()
