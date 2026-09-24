#!/usr/bin/env python3
"""Bounded real-model contract canary; no deployment or translation artifacts.

A passing sample validates structure, not general linguistic quality. The engine
runs only on a verified public Linux Actions runner with its pinned CPU model.
"""
from __future__ import annotations
import argparse
import json
import os
from compare_hymt_translation import require_actions
from offline_translation import MODEL_ID, OfflineTranslator
from build_portal_extended_locales import validate_text
from portal_extended_locales import ExpansionError, digest, select_locales

SAMPLES = (
    ('public-reading', 'zh', '这份报告介绍市场变化，请核对原始资料。'),
    ('financial-quantity', 'en', 'Revenue grew by 12.5% in 2026.'),
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--locales', default='en,fr,hi,zh-Hant')
    args = parser.parse_args()
    locales = select_locales(args.locales)
    require_actions()
    if os.environ.get('KC_PUBLIC_REPOSITORY') != 'true':
        raise ExpansionError('Real-model canary requires a verified public repository')
    translator = OfflineTranslator()
    outcomes = []
    for locale in locales:
        for identity, language, source in SAMPLES:
            try:
                result = translator.translate(source, target=locale, source=language, markdown=False)
                validate_text(source, result, locale, language)
                row = {'locale': locale, 'sample': identity, 'status': 'passed',
                       'translation_sha256': digest(result.encode())}
            except Exception as error:
                # Public logs retain only bounded error categories, never source
                # documents, model responses, credentials, or provider payloads.
                row = {'locale': locale, 'sample': identity, 'status': 'failed',
                       'error_type': type(error).__name__}
            outcomes.append(row)
            print(json.dumps(row, ensure_ascii=False), flush=True)
    print(json.dumps({'model': MODEL_ID, 'samples': len(outcomes),
                      'paid_provider_requests': 0, 'semantic_review': 'not-performed',
                      'deployment_performed': False}))
    return 0 if all(row['status'] == 'passed' for row in outcomes) else 1


if __name__ == '__main__':
    raise SystemExit(main())
