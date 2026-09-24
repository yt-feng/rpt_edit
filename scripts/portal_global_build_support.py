"""Bounded in-memory acceleration for public candidate preparation only."""
from functools import lru_cache


def cache_metadata_normalization(builder):
    """Memoize pure short-string normalization; never retain full report bodies."""
    original = builder.normalize_search_text
    cached = lru_cache(maxsize=32768)(original)

    def normalize(value):
        text = str(value or "")
        return cached(text) if len(text) <= 1000 else original(text)

    builder.normalize_search_text = normalize
    return cached
