"""Deterministic, source-bounded helpers for public discovery.

No model calls, network access, publication claims, or archive identity changes.
All institution definitions are supplied by the caller's existing entity registry.
"""
from __future__ import annotations

from collections import defaultdict
from functools import lru_cache
from html import unescape
from html.parser import HTMLParser
import re
import unicodedata
from typing import Any, Iterable


def compact(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


@lru_cache(maxsize=4)
def _institution_prefix_rules(registry: tuple) -> tuple:
    return tuple((re.compile(r"^\s*" + re.escape(alias).replace(r"\ ", r"[\s.]+")
                             + r"(?:研报|研究报告)?(?=$|[\s:：·|｜_\-–—])", re.I), index)
                 for index, (_slug, aliases) in enumerate(registry) for alias in aliases)


@lru_cache(maxsize=65536)
def _institution_prefix_match(value: str, registry: tuple) -> tuple[int | None, int]:
    best_end, best_index = 0, None
    for pattern, index in _institution_prefix_rules(registry):
        match = pattern.match(value)
        if match and match.end() > best_end:
            best_end, best_index = match.end(), index
    return best_index, best_end


def institution_prefix(value: str, definitions: Iterable[dict]) -> tuple[dict | None, int]:
    """Recognize only a leading, delimited source label, never a body mention."""
    definitions = tuple(definitions)
    registry = tuple((row["slug"], tuple(row["aliases"])) for row in definitions)
    index, end = _institution_prefix_match(str(value or ""), registry)
    return (definitions[index] if index is not None else None), end


def repair_institution_prefix(source: str, translated: str, definitions: Iterable[dict]) -> str:
    """Correct a contradictory translated source prefix; preserve all other text."""
    source_bank, _ = institution_prefix(source, definitions)
    translated_bank, end = institution_prefix(translated, definitions)
    if source_bank and translated_bank and source_bank["slug"] != translated_bank["slug"]:
        return str(source_bank["name_zh"]) + translated[end:]
    return translated


def protect_institution_prefix(value: str, identifiers: dict[str, str], definitions: Iterable[dict]) -> str:
    definition, end = institution_prefix(value, definitions)
    if not definition:
        return value
    index = len(identifiers)
    token = f"__KC_PH_{index:04d}__"
    while token in value or token in identifiers:
        index += 1
        token = f"__KC_PH_{index:04d}__"
    identifiers[token] = str(definition["name_zh"])
    return token + value[end:]


def sentence_excerpt(value: str, limit: int = 300) -> str:
    """Keep full short text, or only complete sentences fitting the budget.

    An over-budget single sentence returns empty; callers can use a truthful
    metadata fallback. Never manufacture punctuation after cutting characters.
    """
    text = compact(value)
    if len(text) <= max(0, limit):
        return text
    ends = [match.end() for match in re.finditer(r"[。！？!?][\"'”’）)]*|\.(?=\s|$)", text)]
    candidates = [end for end in ends if end <= limit]
    return text[:max(candidates)].strip() if candidates else ""


class TextBlocks(HTMLParser):
    """Preserve paragraph boundaries while ignoring non-content HTML."""
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.hidden = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "template"}:
            self.hidden += 1
        if tag in {"p", "div", "section", "li", "br", "h1", "h2", "h3", "figcaption"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "template"} and self.hidden:
            self.hidden -= 1
        if tag in {"p", "div", "section", "li", "h1", "h2", "h3", "figcaption"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self.hidden:
            self.parts.append(data)


def original_report_names(article: dict[str, Any]) -> list[str]:
    explicit = compact(article.get("source_report_name"))
    parser = TextBlocks()
    parser.feed(str(article.get("content") or ""))
    lines = "".join(parser.parts).splitlines()
    values = [explicit] if explicit else []
    # Explicit metadata is the original basename; the footer is a sanitized
    # presentation alias and must not override that provenance.
    for line in ([] if explicit else lines):
        match = re.search(r"(?:Original\s+report|原始报告|原报告)\s*[：:]\s*(.+)", line, re.I)
        if match:
            value = re.split(r"更新信息参见|查看原文|阅读原文", match.group(1), maxsplit=1)[0]
            values.append(compact(value))
    # Only names, not arbitrary links, private object locators or path traversal.
    return list(dict.fromkeys(value for value in values if value and len(value) <= 600
                             and not re.search(r"(?:https?://|s3://|r2://|\.\./|\\|^[~/])", value, re.I)))


def document_name_key(value: str) -> str:
    text = unicodedata.normalize("NFKC", unescape(str(value or ""))).casefold().strip()
    text = re.sub(r"\.pdf\s*$", "", text)
    # The ingestion pipeline adds a numeric processing prefix. Remove it only
    # when followed by a known institution token; all report dates and financial
    # numbers elsewhere remain part of the exact identity. Collisions still fail
    # closed in ReportSourceIndex.
    text = re.sub(r"^\d{1,4}[-_ ]+(?=(?:gs|jpm|ms|ubs|citi|bofa|db|barc|jef|nom|hsbc|bernstein)(?:[-_ :]|$))", "", text)
    return re.sub(r"[\W_]+", " ", text).strip()


class ReportSourceIndex:
    """Exact normalized source-name or validated-ID matching, built once.

    Dates/numbers are retained. Multiple matching reports stay ambiguous: an
    article's publication date is not evidence of a report's publication date.
    """
    def __init__(self, items: list[dict[str, Any]]) -> None:
        self.by_id: dict[str, dict[str, Any]] = {}
        self.by_name: dict[str, set[str]] = defaultdict(set)
        self.duplicate_ids: set[str] = set()
        for item in items:
            report_id = str(item.get("id") or "")
            if not report_id:
                continue
            if report_id in self.by_id and item != self.by_id[report_id]:
                self.duplicate_ids.add(report_id)
            self.by_id[report_id] = item
            for field in ("filename", "title"):
                key = document_name_key(str(item.get(field) or ""))
                if key:
                    self.by_name[key].add(report_id)

    def resolve(self, article: dict[str, Any]) -> tuple[str, dict[str, Any] | None]:
        names = original_report_names(article)
        explicit_id = str(article.get("source_report_id") or "")
        if len(names) > 1 and len({document_name_key(name) for name in names}) > 1:
            return "ambiguous", None
        candidates = set().union(*(self.by_name.get(document_name_key(name), set()) for name in names))
        if explicit_id:
            if explicit_id in self.duplicate_ids:
                return "ambiguous", None
            if explicit_id not in self.by_id:
                return "unmatched", None
            if names and explicit_id not in candidates:
                return "conflict", None
            return "matched", self.by_id[explicit_id]
        if candidates & self.duplicate_ids or len(candidates) > 1:
            return "ambiguous", None
        if len(candidates) == 1:
            return "matched", self.by_id[next(iter(candidates))]
        return ("unmatched" if names else "not_provided"), None


def title_quality_flags(value: str) -> list[str]:
    title = compact(value)
    flags = []
    if not title:
        flags.append("empty_title")
    if len(title) > 110:
        flags.append("long_title_review")
    if re.search(r"[：:,，、;；\-—]$|(?:以及|分别为|主要包括|如下)$", title):
        flags.append("unfinished_title")
    if re.search(r"(?:此前按|粗略折算|原始输出|作为AI|待补充)", title):
        flags.append("editorial_fragment")
    return flags


# Company and fine-topic labels are controlled retrieval keys, not new page or
# authorship claims. Short ticker symbols require explicit ticker punctuation.
COMPANY_ALIASES: dict[str, tuple[str, ...]] = {
    "micron": ("Micron", "美光"), "nvidia": ("Nvidia", "英伟达"),
    "tsmc": ("TSMC", "Taiwan Semiconductor", "台积电"),
    "smic": ("SMIC", "中芯国际"), "sk-hynix": ("SK Hynix", "海力士"),
    "samsung": ("Samsung", "三星电子"), "microsoft": ("Microsoft", "微软"),
    "amazon": ("Amazon", "亚马逊"), "alphabet": ("Alphabet", "Google", "谷歌"),
    "amd": ("AMD", "超威半导体"), "broadcom": ("Broadcom", "博通"),
    "marvell": ("Marvell", "迈威尔"), "tesla": ("Tesla", "特斯拉"),
    "fedex-freight": ("FedEx Freight", "联邦快递货运"),
    "alibaba": ("Alibaba", "阿里巴巴"), "tencent": ("Tencent", "腾讯"),
    "apple": ("Apple", "苹果公司"), "asml": ("ASML", "阿斯麦"),
}
TICKERS = {"micron": "MU", "nvidia": "NVDA", "tsmc": "TSM", "smic": "0981.HK",
           "microsoft": "MSFT", "amazon": "AMZN", "alphabet": "GOOGL", "amd": "AMD",
           "broadcom": "AVGO", "marvell": "MRVL", "tesla": "TSLA", "fedex-freight": "FDXF"}
FINE_TOPICS = {
    "memory": r"\b(?:memory|dram|nand|hbm)\b|存储器|存储芯片|内存",
    "hbm": r"\bhbm\b|高带宽存储", "dram": r"\bdram\b|动态随机存储",
    "nand": r"\bnand\b|闪存", "cpo": r"\bcpo\b|共封装光学|光电共封装",
    "foundry": r"\bfoundr(?:y|ies)\b|晶圆代工|先进制程",
    "semi-equipment": r"\b(?:lithography|wafer fab equipment)\b|半导体设备|光刻",
    "data-center": r"\b(?:data\s*cent(?:er|re)s?|datacenters?)\b|数据中心|算力中心",
    "robotics": r"\brobot(?:s|ics)?\b|机器人",
    "lng": r"\blng\b|液化天然气", "inflation": r"\b(?:inflation|cpi)\b|通胀|消费者价格",
    "freight": r"\b(?:freight|shipping|logistics)\b|货运|航运|物流",
}


@lru_cache(maxsize=8192)
def research_entities(text: str) -> tuple[frozenset[str], frozenset[str]]:
    companies = set()
    for key, aliases in COMPANY_ALIASES.items():
        for alias in aliases:
            pattern = (r"(?<![A-Za-z0-9])" + re.escape(alias) + r"(?![A-Za-z0-9])") if alias.isascii() else re.escape(alias)
            if re.search(pattern, text, re.I):
                companies.add(key)
                break
        ticker = TICKERS.get(key)
        if ticker and re.search(r"(?:[($（]|\bTicker\s*[:：]\s*)" + re.escape(ticker)
                                + r"(?=[)）\s.]|$)", text):
            companies.add(key)
    fine = {key for key, pattern in FINE_TOPICS.items() if re.search(pattern, text, re.I)}
    return frozenset(companies), frozenset(fine)


def editorial_topic_labels(title: str, digest: str, rules: list) -> list[str]:
    """A title match outranks incidental prose; use digest only as fallback."""
    title_scores, digest_scores = [], []
    for order, (label, pattern) in enumerate(rules):
        title_hits = {match.group(0).casefold() for match in pattern.finditer(title)}
        digest_hits = {match.group(0).casefold() for match in pattern.finditer(digest)}
        if title_hits:
            title_scores.append((len(title_hits), len(digest_hits), -order, label))
        if digest_hits:
            digest_scores.append((len(digest_hits), 0, -order, label))
    scores = sorted(title_scores or digest_scores, reverse=True)
    if not scores:
        return []
    return [row[3] for row in scores[:2] if row[0] >= max(1, scores[0][0] / 2)]


def report_source_metadata(status: Any) -> dict[str, str]:
    """Extract only an original basename from trusted ingestion status.

    Never serialize directories, storage URLs, tokens, or an inferred report ID.
    This sidecar is persisted with the public template, not sent to WeChat.
    """
    if not isinstance(status, dict):
        return {}
    for field in ("source_report_original_name", "original_report_name", "source_pdf"):
        raw = str(status.get(field) or "").strip()
        if not raw or re.search(r"[a-z][a-z0-9+.-]*://|[?\x00-\x1f]", raw, re.I):
            continue
        name = re.split(r"[/\\]", raw)[-1]
        if (name and len(name) <= 600 and name not in {".", ".."}
                and not re.search(r"[<>]", name)):
            return {"source_report_name": name}
    return {}
