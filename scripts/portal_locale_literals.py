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
_PROSE_WORDS = frozenset({"we", "you", "they", "it", "this", "that", "these", "those", "is", "are", "was", "were", "will", "should", "could", "buy", "sell", "expect", "expects", "expected", "grow", "grows", "grew", "increased", "decreased", "improved", "because", "covers"})


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
    if not words or len(words) > 16 or any(word.casefold() in _PROSE_WORDS for word in words):
        return False
    name_case = all(
        word.casefold() in _NAME_CONNECTORS or word[0].isdigit()
        or any(character.isupper() for character in word)
        for word in words
    )
    if not name_case:
        return False
    if words[-1].casefold() in _LEGAL_SUFFIXES:
        return True
    return context == "chart:keywords" and len(words) <= 6


def is_machine_asset_reference(value: object) -> bool:
    """Match an entire ASCII asset filename/path, never surrounding prose."""
    return isinstance(value, str) and bool(_ASSET_REFERENCE.fullmatch(value.strip()))
