"""Cache-first adapter; the cache probe cannot construct an inference engine."""
from __future__ import annotations
import json

from offline_translation import OfflineTranslator, OfflineTranslationError
from hymt_offline_translation import split_sentences, normalize_language, _detect_source
from build_portal_extended_locales import validate_text


class CacheMiss(OfflineTranslationError):
    pass


def forbidden_engine(*args):
    raise CacheMiss('quality_repair_cache_miss')


class CacheFirstTranslator:
    def __init__(self, translator=None):
        self.fresh = translator or OfflineTranslator(validation_attempts=1, quantity_policy='advisory')
        self.cached = OfflineTranslator(cache_dir=self.fresh.cache_dir, model_dir=self.fresh.model_dir,
                                       engine_factory=forbidden_engine, validation_attempts=1,
                                       quantity_policy='advisory')

    def __getattr__(self, name): return getattr(self.fresh, name)

    def set_deadline(self, deadline):
        self.fresh.set_deadline(deadline)
        self.cached.set_deadline(deadline)

    def cached_translation(self, text, target, source, *, markdown):
        # Distinguish absent files from unreadable/corrupted ones before the
        # adapter's intentionally broad cache fallback can hide an I/O failure.
        target, source = normalize_language(target), normalize_language(source)
        for piece in split_sentences(text):
            identity, path = self.cached._memo_identity(piece.strip(), target,
                source or _detect_source(piece.strip()), markdown=markdown)
            try:
                with path.open('rb') as file: raw = file.read(1024*1024+1)
            except FileNotFoundError: continue
            if len(raw) > 1024*1024:
                raise OfflineTranslationError('quality_repair_cache_too_large')
            value = json.loads(raw)
            if not isinstance(value, dict) or any(value.get(k) != v for k, v in identity.items()) or not isinstance(value.get('translation'), str):
                raise OfflineTranslationError('quality_repair_cache_identity_invalid')
            try:
                self.cached.translate(piece, target, source, markdown=markdown)
            except CacheMiss:
                # An existing but structurally rejected cache is not an absent
                # response. Do not turn its hidden adapter fallback into a POST.
                raise OfflineTranslationError('quality_repair_existing_cache_rejected') from None
        try:
            value = self.cached.translate(text, target, source, markdown=markdown)
        except CacheMiss:
            return None
        if self.cached.stats['batch_requests'] or self.cached.stats['translated_fragments']:
            raise OfflineTranslationError('quality_repair_cache_probe_used_inference')
        validate_text(text, value, target, source)
        return value
