"""Narrow non-linguistic values that translation must preserve verbatim."""
from __future__ import annotations

import re


_ASSET_REFERENCE = re.compile(
    r"(?:\.{1,2}/|/)?(?:[A-Za-z0-9_@.+~%-]+/)*"
    r"[A-Za-z0-9_@.+~%-]+\."
    r"(?:jpe?g|png|webp|gif|svg|avif|bmp|ico|pdf|csv|xlsx?|docx?|pptx?|zip)"
    r"(?:[?#][A-Za-z0-9_@.+~%&=/?#:-]*)?",
    re.IGNORECASE,
)

_LATIN_NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9 .&'’+()/,\-]*")
_NAME_CONNECTORS = frozenset({"of", "the", "and", "de", "del", "la", "du", "da", "di", "van", "von"})
_LEGAL_SUFFIXES = frozenset({"inc", "incorporated", "ltd", "limited", "corp", "corporation", "co", "company", "llc", "llp", "plc", "ag", "sa", "se", "nv", "gmbh"})
# This is an identity-literal check, not a language-quality classifier. Common
# sentence openings/verbs keep an English sentence containing a name in scope.
_PROSE_WORDS = frozenset({"we", "you", "they", "it", "this", "that", "these", "those", "is", "are", "was", "were", "will", "should", "could", "buy", "sell", "expect", "expects", "expected", "grow", "grows", "grew", "increased", "decreased", "improve", "improves", "improved", "continue", "continues", "remain", "remains", "because", "covers"})
_SHORT_SOURCE_LABEL = re.compile(r"[A-Za-z0-9&\u3400-\u9fff]{1,12}")
_SHORT_LATIN_LABEL = re.compile(r"[A-Za-z0-9][A-Za-z0-9.&+\-]{0,15}")
_ACRONYM_PAIR = re.compile(r"[A-Z0-9][A-Z0-9.&+\-]* [A-Z0-9][A-Z0-9.&+\-]*")
# A prose fragment can carry a list delimiter immediately before a short
# proper name, e.g. `、台积电`. Strip only this list delimiter while checking
# the label; sentence punctuation remains ineligible.
_SHORT_LABEL_EDGE_PUNCTUATION = "、"
_SHARED_JAPANESE_KEYWORD = re.compile(r"[A-Z0-9&+./\-\u3400-\u9fff]{1,12}")
# Removing a protected index number leaves a separator, e.g. S&P 500指数
# becomes S&P 指数. Permit that complete index-label form, not arbitrary
# spaces in mixed-script keywords or any structural placeholder token.
_SHARED_JAPANESE_INDEX_KEYWORD = re.compile(r"[A-Z0-9&+./\-]{1,9} 指数")
# These modifiers are also Japanese words. Combining them with a known metric
# does not make a label Chinese prose; e.g. a styled paragraph can expose just
# `国内RevPar` before its next <span>. Keep both vocabularies closed so arbitrary
# mixed-script copy such as `国内AI增长` never acquires an identity exemption.
_JAPANESE_FINANCIAL_LABEL = re.compile(
    r"(?:国内|海外|連結|単体|全社|通期|上期|下期|調整後)\s*"
    r"(?:RevPAR|ADR|EBITDA|EBIT|EPS|PER|PBR|ROE|ROA|ROIC|FCF|NAV|AUM|GDP|CPI|PPI)",
    re.IGNORECASE,
)
# HTMLParser preserves entities separately, so `三井E&amp;S` can expose the
# native company-name fragment `三井E`. Neither spelling needs a new Japanese
# rendering. Do not extend this to arbitrary Kanji + Latin company-like text.
_JAPANESE_ENTITY_LITERALS = frozenset({"三井E", "三井E&S"})
# Chart metric names can consist entirely of international abbreviations and
# measurement units. Keep the vocabulary and complete-string grammar closed;
# generic uppercase words or a sentence containing a metric are still prose.
_CHART_METRIC_IDENTITY = re.compile(
    r"(?:GRM \(US\$/bbl\)|[+-]?[1-9][0-9]{0,3}(?:\.[0-9]{1,2})?mm SOI ASP"
    r"|AST(?:2600|2700) ASP \(US\$\)|JPM PT LC)"
)
# Preserve geography codes exactly as supplied by chart metadata. These are
# observed source codes, not inferred country names or a general uppercase
# exemption. Require a complete, bounded slash-separated list in its own field.
_CHART_GEOGRAPHY_CODE = r"(?:AU|CA|EU|JN|SZ|UK)"
_CHART_GEOGRAPHY_IDENTITY = re.compile(
    rf"{_CHART_GEOGRAPHY_CODE}(?:[ \t]*/[ \t]*{_CHART_GEOGRAPHY_CODE}){{1,7}}"
)


def is_chart_geography_identity_label(source: object, translated: object, context: str) -> bool:
    """Accept unchanged lists of observed codes only in chart geographies."""
    if context != "chart:geographies" or not isinstance(source, str) or not isinstance(translated, str):
        return False
    source = source.strip()
    return bool(source == translated.strip() and _CHART_GEOGRAPHY_IDENTITY.fullmatch(source))


def is_chart_metric_identity_label(source: object, translated: object, context: str) -> bool:
    """Accept unchanged bounded metric/unit labels only in chart metrics."""
    if context != "chart:metrics" or not isinstance(source, str) or not isinstance(translated, str):
        return False
    source = source.strip()
    return bool(source == translated.strip() and _CHART_METRIC_IDENTITY.fullmatch(source))


def is_japanese_identity_label(source: object, translated: object) -> bool:
    """Recognize complete Japanese entity/metric labels, never surrounding copy.

    This check is context independent: inline markup can leave a standalone
    label inside a paragraph, heading, or metadata field. The caller must check
    structural placeholders first and invoke it only for Japanese output.
    """
    if not isinstance(source, str) or not isinstance(translated, str):
        return False
    source = source.strip()
    return bool(
        source == translated.strip()
        and (source in _JAPANESE_ENTITY_LITERALS or _JAPANESE_FINANCIAL_LABEL.fullmatch(source))
    )


def is_shared_japanese_keyword(source: object, translated: object, context: str) -> bool:
    """Short Kanji/acronym index names may be identical in Japanese metadata."""
    if context not in {"chart:keywords", "ja:shared-keyword"}:
        return False
    if not isinstance(source, str) or not isinstance(translated, str):
        return False
    source = source.strip()
    return bool(
        source == translated.strip()
        and (_SHARED_JAPANESE_KEYWORD.fullmatch(source) or _SHARED_JAPANESE_INDEX_KEYWORD.fullmatch(source))
        and re.search(r"[A-Z]", source)
        and 1 <= len(re.findall(r"[\u3400-\u9fff]", source)) <= 4
    )


def is_short_latin_label_translation(source: object, translated: object) -> bool:
    """A short label may translate to a Latin brand/acronym in every locale.

    This is not an entity exemption: both complete strings must remain short,
    with no source sentence punctuation or output word/sentence separators.
    """
    if not isinstance(source, str) or not isinstance(translated, str):
        return False
    source, translated = source.strip(), translated.strip()
    source_core = source.strip(_SHORT_LABEL_EDGE_PUNCTUATION)
    translated_core = translated.strip(_SHORT_LABEL_EDGE_PUNCTUATION)
    edge_delimited = source_core != source or translated_core != translated
    return bool(
        _SHORT_SOURCE_LABEL.fullmatch(source_core)
        and re.search(r"[\u3400-\u9fff]", source_core)
        and (not edge_delimited or len(source_core) <= 4)
        and (_SHORT_LATIN_LABEL.fullmatch(translated_core)
             or (len(translated_core) <= 16 and _ACRONYM_PAIR.fullmatch(translated_core)))
        and re.search(r"[A-Za-z]", translated_core)
    )


def is_latin_name_literal(value: object, context: str = "") -> bool:
    """Recognize a whole short company name, never a sentence around a name.

    Legal company names can occur in any field. A looser title-cased identity
    is allowed only in name-like chart keywords, not article titles or prose.
    """
    if not isinstance(value, str):
        return False
    value = value.strip()
    if len(value) > 160 or not _LATIN_NAME.fullmatch(value):
        return False
    words = re.findall(r"[A-Za-z0-9]+(?:['’][A-Za-z]+)?", value)
    if not words or len(words) > 16:
        return False
    has_legal_suffix = words[-1].casefold() in _LEGAL_SUFFIXES
    has_named_token = any(
        word.casefold() not in _LEGAL_SUFFIXES | _NAME_CONNECTORS
        and (word[0].isdigit() or any(character.isupper() for character in word))
        for word in words
    )
    name_case = all(
        word.casefold() in _NAME_CONNECTORS or word[0].isdigit()
        # Legal forms such as plc and co are routinely lowercase. They may
        # relax casing only alongside a name and a terminal legal suffix.
        or (has_legal_suffix and has_named_token and word.casefold() in _LEGAL_SUFFIXES)
        or any(character.isupper() for character in word)
        for word in words
    )
    if not name_case:
        return False
    if has_legal_suffix:
        # IT and Will can themselves be part of a legal company name. A suffix
        # gives stronger identity evidence than a keyword's capitalization.
        return not any(word.casefold() in _PROSE_WORDS - {"it", "will"} for word in words)
    return (context == "chart:keywords" and len(words) <= 6
            and not value.endswith((".", ","))
            and not any(word.casefold() in _PROSE_WORDS for word in words))


def is_machine_asset_reference(value: object) -> bool:
    """Match an entire ASCII asset filename/path, never surrounding prose."""
    return isinstance(value, str) and bool(_ASSET_REFERENCE.fullmatch(value.strip()))
