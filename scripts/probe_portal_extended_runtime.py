"""Read-only comparison probe for the first exact unfinished source unit.

Only the diagnostic process disables the Unicode sampler constraint. Its output
is never a candidate, never shares the translation cache, and never updates the
durable checkpoint. The ordinary builder is a separate, constrained process.
"""
import argparse
import json
import os
from pathlib import Path
import time

import hymt_offline_translation as hymt
from build_portal_extended_locales import Memo, TranslationUnitError, safe_failure_code, translate_document
from compare_hymt_translation import require_actions
from portal_extended_locales import digest, validate_corpus


class PendingUnit(Exception):
    pass


def first_pending(corpus, locale, checkpoint):
    class Capture:
        unit = None
        def translate(self, text, target, source=None, *, markdown=True):
            self.unit = (text, source, markdown)
            raise PendingUnit()

    capture = Capture()
    memo = Memo(checkpoint, locale, capture, time.monotonic()+60,
                source_generation=corpus['documents_sha256'], allow_source_fallback=True)
    for doc in validate_corpus(corpus):
        try:
            translate_document(doc, memo)
        except TranslationUnitError as error:
            if isinstance(error.error, PendingUnit):
                return capture.unit
            raise
    return None


def probe(corpus, locale, checkpoint, translator):
    unit = first_pending(corpus, locale, checkpoint)
    result = {'locale': locale, 'diagnostic_only': True, 'unicode_constraint': False,
              'checkpoint_writes': 0, 'publication_performed': False}
    if unit is None:
        return {**result, 'status': 'no-pending-unit'}
    text, source, markdown = unit
    result.update(unit_sha256=digest(text.encode()), unit_characters=len(text))
    grammar = hymt.UNICODE_TEXT_GRAMMAR
    try:
        hymt.UNICODE_TEXT_GRAMMAR = ''
        translator.translate(text, locale, source, markdown=markdown)
        result['status'] = 'unconstrained-unit-passed'
    except Exception as error:
        result.update(status='unconstrained-unit-failed', failure_code=safe_failure_code(error))
    finally:
        hymt.UNICODE_TEXT_GRAMMAR = grammar
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--corpus', type=Path, required=True)
    parser.add_argument('--checkpoint', type=Path, required=True)
    parser.add_argument('--locale', required=True)
    parser.add_argument('--cache', type=Path, required=True)
    args = parser.parse_args()
    require_actions()
    if os.environ.get('KC_PUBLIC_REPOSITORY') != 'true':
        raise RuntimeError('Requires a verified public Actions runner')
    translator = hymt.OfflineTranslator(cache_dir=args.cache, validation_attempts=1)
    translator.set_deadline(time.monotonic()+600)
    result = probe(json.loads(args.corpus.read_text()), args.locale, args.checkpoint, translator)
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
