#!/usr/bin/env python3
"""Infer Chinese institution names from report filenames and metadata."""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any


INSTITUTION_PATTERNS: tuple[tuple[re.Pattern[str], str], ...] = (
    (re.compile(r"\bGoldman(?:\s+Sachs)?\b|\bGS\b", re.I), "高盛"),
    (re.compile(r"\bMorgan\s+Stanley\b|\bMS\b", re.I), "摩根斯坦利"),
    (re.compile(r"\bJ\.?\s*P\.?\s*[-_\s]*Morgan\b|\bJPMorgan\b|\bJPM\b", re.I), "摩根大通"),
    (re.compile(r"\bHSBC\b|Hongkong\s+and\s+Shanghai\s+Banking", re.I), "汇丰"),
    (re.compile(r"\bUBS\b", re.I), "瑞银"),
    (re.compile(r"\bCiti(?:group)?\b", re.I), "花旗"),
    (re.compile(r"\bBofA\b|Bank\s+of\s+America", re.I), "美国银行"),
    (re.compile(r"\bBarclays\b", re.I), "巴克莱"),
    (re.compile(r"\bDeutsche\s+Bank\b", re.I), "德意志银行"),
    (re.compile(r"\bNomura\b", re.I), "野村"),
    (re.compile(r"\bBernstein\b", re.I), "伯恩斯坦"),
    (re.compile(r"\bJefferies\b", re.I), "杰富瑞"),
    (re.compile(r"\bMacquarie\b", re.I), "麦格理"),
    (re.compile(r"\bSociete\s+Generale\b|\bSocGen\b", re.I), "法兴"),
    (re.compile(r"\bBNP\s+Paribas\b", re.I), "法国巴黎银行"),
    (re.compile(r"\bCredit\s+Suisse\b", re.I), "瑞信"),
    (re.compile(r"\bMizuho\b", re.I), "瑞穗"),
    (re.compile(r"\bDaiwa\b", re.I), "大和"),
    # Public economic / policy institutions (see scripts/fetch_institution_latest_pdfs.py).
    (re.compile(r"\bWorld\s*Bank\b|\bWorldBank\b", re.I), "世界银行"),
    (re.compile(r"\bIMF\b|International\s+Monetary\s+Fund", re.I), "IMF"),
    (re.compile(r"\bBIS\b|Bank\s+for\s+International\s+Settlements", re.I), "国际清算银行"),
    (re.compile(r"\bRAND\b", re.I), "兰德公司"),
    (re.compile(r"\bBrookings\b", re.I), "布鲁金斯学会"),
    (re.compile(r"\bARK\s+Invest\b|\bARKInvest\b|\bARKK\b|Cathie\s+Wood", re.I), "木头姐ARK"),
    # MBB strategy consultancies.
    (re.compile(r"\bMcKinsey\b", re.I), "麦肯锡"),
    (re.compile(r"\bBain\b", re.I), "贝恩"),
    (re.compile(r"\bBCG\b|Boston\s+Consulting", re.I), "波士顿咨询"),
)


def stringify_metadata(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, Path):
        return value.name
    if isinstance(value, (list, tuple, set)):
        return " ".join(stringify_metadata(item) for item in value)
    if isinstance(value, dict):
        return " ".join(f"{key} {stringify_metadata(item)}" for key, item in value.items())
    return str(value)


def infer_institution_name(*values: Any) -> str:
    haystack = "\n".join(stringify_metadata(value) for value in values if value is not None)
    if not haystack:
        return ""
    searchable = re.sub(r"[_/]+", " ", haystack)
    for pattern, chinese_name in INSTITUTION_PATTERNS:
        if pattern.search(searchable):
            return chinese_name
    return ""


def ensure_title_has_institution(title: str, institution: str) -> str:
    title = re.sub(r"\s+", " ", title or "").strip()
    institution = (institution or "").strip()
    if not title or not institution:
        return title
    if institution in title[: max(8, len(institution) + 3)]:
        return title
    return f"{institution}：{title}"
