"""Reject changed financial quantities without breaking translation context.

This is a deterministic structural check, not a semantic translation judge.
Amounts are compared at their underlying scale and rates remain distinct from
percentage-point changes. Unsupported written-out quantities fail closed when
their numeric counterpart disappears.
"""
from __future__ import annotations

from collections import Counter
from datetime import date
from decimal import Decimal
import re
import unicodedata


# Keep a complete decimal indivisible. Otherwise a failed suffix match can
# backtrack USD1.2bn into USD1 plus a stray 2, hiding a changed magnitude.
NUMBER = r"(?>[+\-−]?\d+(?:[,٬]\d{3})*(?:[.٫,]\d+)?)"
SCALES = {
    "thousand": 10**3, "million": 10**6, "billion": 10**9, "trillion": 10**12,
    "k": 10**3, "m": 10**6, "b": 10**9, "t": 10**12,
    "mn": 10**6, "mln": 10**6, "mm": 10**6,
    "bn": 10**9, "bln": 10**9, "tn": 10**12, "trn": 10**12,
    "万": 10**4, "万元": 10**4, "十万": 10**5, "百万": 10**6,
    "千万": 10**7, "亿": 10**8, "亿元": 10**8, "十亿": 10**9,
    "百亿": 10**10, "千亿": 10**11, "万亿": 10**12,
    "만": 10**4, "천만": 10**7, "백만": 10**6, "억": 10**8,
    "십억": 10**9, "조": 10**12, "مليون": 10**6, "مليار": 10**9, "ألف": 10**3,
}
SCALE = "(?:" + "|".join(re.escape(value) for value in sorted(SCALES, key=len, reverse=True)) + ")"
CURRENCIES = {
    "USD": ("USD", "US$", "$", "US dollars", "U.S. dollars", "US dollar", "U.S. dollar", "dollars", "dollar", "美元", "美金", "달러", "دولار أمريكي", "دولار"),
    "CNY": ("CNY", "RMB", "人民币", "元人民币", "元", "yuan", "renminbi", "Chinese yuan", "Chinese renminbi", "人民币元", "위안"),
    "EUR": ("EUR", "€", "euros", "euro", "欧元", "유로"),
    "GBP": ("GBP", "£", "pounds", "pound", "英镑"),
    "JPY": ("JPY", "日元", "円", "yen"),
    "HKD": ("HKD", "HK$", "港元", "港币"),
}
ALIASES = {alias.casefold(): code for code, aliases in CURRENCIES.items() for alias in aliases}
CURRENCY = "(?:" + "|".join(re.escape(s) for s in sorted(ALIASES, key=len, reverse=True)) + ")"
MONTH_NAMES = "January February March April May June July August September October November December".split()
MONTHS = {name.casefold(): i for i, name in enumerate(MONTH_NAMES, 1)}
MONTHS.update({name[:3].casefold(): i for i, name in enumerate(MONTH_NAMES, 1)})
MONTH = "(?:" + "|".join(sorted(MONTHS, key=len, reverse=True)) + r")\.?"


def _normalized(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).replace("−", "-").replace("٬", ",").replace("٫", ".")
    text = "".join(str(unicodedata.decimal(c)) if c.isdecimal() else c for c in text)
    return re.sub(r"__(?:KC_PH|HYMTPH)_\d+__", " ", text)


def _decimal(value: str) -> Decimal:
    value = value.replace("−", "-")
    if "," in value:
        # A sole non-thousands comma is a decimal separator; never use floats.
        if "." not in value and value.count(",") == 1 and len(value.rsplit(",", 1)[1]) != 3:
            value = value.replace(",", ".")
        else:
            value = value.replace(",", "")
    return Decimal(value)


def quantities(text: str) -> Counter:
    text = _normalized(text)
    found = Counter()

    def take(pattern: str, key) -> None:
        nonlocal text
        def consume(match):
            found[key(match)] += 1
            return " " * len(match.group())
        text = re.sub(pattern, consume, text, flags=re.IGNORECASE)

    def day_key(year, month, day):
        try:
            return ("date", date(int(year), int(month), int(day)).isoformat())
        except ValueError:
            return ("invalid_date", str((year, month, day)))

    take(r"(?<!\d)(\d{4})\s*(?:[-/]\s*|年\s*|년\s*)(\d{1,2})\s*(?:[-/]\s*|月\s*|월\s*)(\d{1,2})\s*(?:日|일)?(?!\d)",
         lambda m: day_key(m[1], m[2], m[3]))
    take(rf"\b({MONTH})\s+(\d{{1,2}})(?:st|nd|rd|th)?\s*,?\s*(\d{{4}})\b",
         lambda m: day_key(m[3], MONTHS[m[1].rstrip('.').casefold()], m[2]))
    take(rf"\b(\d{{1,2}})\s+({MONTH})\s*,?\s*(\d{{4}})\b",
         lambda m: day_key(m[3], MONTHS[m[2].rstrip('.').casefold()], m[1]))
    take(rf"\b({MONTH})\s+(\d{{4}})\b",
         lambda m: ("month", int(m[2]), MONTHS[m[1].rstrip('.').casefold()]))
    take(r"(?<!\d)(\d{4})[-/](\d{1,2})(?![\d/-])",
         lambda m: ("month", int(m[1]), int(m[2])))
    take(r"(?<!\d)(\d{4})\s*(?:年|년)\s*(\d{1,2})\s*(?:月|월)",
         lambda m: ("month", int(m[1]), int(m[2])))
    # Period labels commonly appear in financial titles; recognizing them
    # avoids rejecting a correct Chinese ordinal as a missing Arabic digit.
    ordinals = {'一': 1, '二': 2, '三': 3, '四': 4, 'first': 1, 'second': 2, 'third': 3, 'fourth': 4}
    take(r"(?<!\d)(\d{4})\s*年\s*第?([一二三四1-4])季度",
         lambda m: ("quarter", int(m[1]), ordinals.get(m[2], int(m[2]) if m[2].isdigit() else 0)))
    take(r"\bQ([1-4])\s*[,-]?\s*(\d{4})\b", lambda m: ("quarter", int(m[2]), int(m[1])))
    take(r"\b(\d{4})\s*Q([1-4])\b", lambda m: ("quarter", int(m[1]), int(m[2])))
    take(r"\b([1-4])Q\s*(\d{4})\b", lambda m: ("quarter", int(m[2]), int(m[1])))
    take(r"\b(first|second|third|fourth)\s+quarter(?:\s+of)?\s+(\d{4})\b",
         lambda m: ("quarter", int(m[2]), ordinals[m[1].casefold()]))
    take(r"\bH([12])\s*(\d{4})\b", lambda m: ("half", int(m[2]), int(m[1])))
    take(r"\b(\d{4})\s*H([12])\b", lambda m: ("half", int(m[1]), int(m[2])))
    take(r"\b([12])H\s*(\d{4})\b", lambda m: ("half", int(m[2]), int(m[1])))
    take(r"\b(first|second)\s+half(?:\s+of)?\s+(\d{4})\b",
         lambda m: ("half", int(m[2]), ordinals[m[1].casefold()]))
    take(r"(?<!\d)(\d{4})\s*年\s*([上下])半年", lambda m: ("half", int(m[1]), 1 if m[2] == '上' else 2))

    # Currency recognition comes before scaled plain numbers. Keep the unit
    # separate so USD120m can never match an unqualified 120 or CNY120m.
    def money(m):
        scale = (m['scale'] or '').casefold()
        return ("currency", ALIASES[m['currency'].casefold()], _decimal(m['number']) * SCALES.get(scale, 1))
    # Alphabetic boundaries avoid interpreting the suffix of e.g. "dollars".
    take(rf"(?<![A-Za-z])(?P<currency>{CURRENCY})\s*(?P<number>{NUMBER})\s*(?P<scale>{SCALE})?(?![\dA-Za-z])", money)
    take(rf"(?<![\dA-Za-z])(?P<number>{NUMBER})\s*(?P<scale>{SCALE})?\s*(?P<currency>{CURRENCY})(?![A-Za-z])", money)
    take(rf"({NUMBER})\s*(?:basis\s+points?|bps\b|基点|基點)",
         lambda m: ("percentage_points", _decimal(m[1]) / 100))
    take(rf"(?P<number>{NUMBER})\s*(?:percentage\s+points?|percent(?:age)?\s+points?|个百分点|個百分點|パーセントポイント|퍼센트포인트|نقطة\s+مئوية|نقاط\s+مئوية)",
         lambda m: ("percentage_points", _decimal(m['number'])))
    take(rf"(?P<number>{NUMBER})\s*(?:%|٪|percent(?:age)?(?![a-z])|per\s+cent(?![a-z])|パーセント|퍼센트|في\s+المائة|في\s+المئة)",
         lambda m: ("percent", _decimal(m['number'])))
    take(rf"百分之\s*({NUMBER})", lambda m: ("percent", _decimal(m[1])))
    take(rf"(?<![\dA-Za-z])({NUMBER})\s*({SCALE})(?![A-Za-z])",
         lambda m: ("number", _decimal(m[1]) * SCALES[m[2].casefold()]))
    take(NUMBER, lambda m: ("number", _decimal(m[0])))
    return found


def quantity_issues(source: str, translated: str, source_language: str = "", target_language: str = "") -> list[str]:
    before, after = quantities(source), quantities(translated)
    issues = []
    if any(key[0] == 'invalid_date' for key in before.keys() | after.keys()):
        issues.append("invalid_calendar_date")
    if before != after:
        issues.append("financial_quantity_changed_missing_or_added")
    return issues
