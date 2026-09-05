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


def is_machine_asset_reference(value: object) -> bool:
    """Match an entire ASCII asset filename/path, never surrounding prose."""
    return isinstance(value, str) and bool(_ASSET_REFERENCE.fullmatch(value.strip()))
