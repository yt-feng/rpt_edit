"""Pinned, local-only Simplified-to-Traditional script conversion.

Script conversion is not a generative paraphrase. URLs, code and placeholders
are protected by the caller; no network or language-model request is made here.
"""
from functools import lru_cache
from importlib.metadata import version

OPENCC_DISTRIBUTION = "opencc-python-reimplemented"
OPENCC_VERSION = "0.1.7"

@lru_cache(maxsize=1)
def _converter():
    if version(OPENCC_DISTRIBUTION) != OPENCC_VERSION:
        raise RuntimeError("Install the pinned local OpenCC dependency before Traditional Chinese builds")
    from opencc import OpenCC
    return OpenCC("s2t")

def to_traditional(text: str) -> str:
    return _converter().convert(text)
