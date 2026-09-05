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
_SHORT_SOURCE_LABEL = re.compile(r"[A-Za-z0-9\u3400-\u9fff]{1,12}")
_SHORT_LATIN_LABEL = re.compile(r"[A-Za-z0-9][A-Za-z0-9.&+\-]{0,15}")


def is_short_latin_label_translation(source: object, translated: object) -> bool:
    """A short label may translate to a Latin brand/acronym in every locale.

    This is not an entity exemption: both complete strings must remain short,
    with no source sentence punctuation or output word/sentence separators.
    """
    if not isinstance(source, str) or not isinstance(translated, str):
        return False
    source, translated = source.strip(), translated.strip()
    return bool(
        _SHORT_SOURCE_LABEL.fullmatch(source)
        and re.search(r"[\u3400-\u9fff]", source)
        and _SHORT_LATIN_LABEL.fullmatch(translated)
        and re.search(r"[A-Za-z]", translated)
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
    name_case = all(
        word.casefold() in _NAME_CONNECTORS or word[0].isdigit()
        or any(character.isupper() for character in word)
        for word in words
    )
    if not name_case:
        return False
    if words[-1].casefold() in _LEGAL_SUFFIXES:
        # IT and Will can themselves be part of a legal company name. A suffix
        # gives stronger identity evidence than a keyword's capitalization.
        return not any(word.casefold() in _PROSE_WORDS - {"it", "will"} for word in words)
    return (context == "chart:keywords" and len(words) <= 6
            and not value.endswith((".", ","))
            and not any(word.casefold() in _PROSE_WORDS for word in words))


def is_machine_asset_reference(value: object) -> bool:
    """Match an entire ASCII asset filename/path, never surrounding prose."""
    return isinstance(value, str) and bool(_ASSET_REFERENCE.fullmatch(value.strip()))
