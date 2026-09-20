#!/usr/bin/env python3
"""Run public financial samples through installed models without API access."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import time
from unittest import mock

from offline_translation import OfflineTranslator, PROVIDER
import build_portal_locales as locales


REVIEWED_FINANCIAL_SAMPLES = {
    ("Operating cash flow rose by 15% in 2026.", "ko"): "2026년 영업 현금 흐름은 15% 증가했습니다.",
    ("Operating cash flow rose by 15% in 2026.", "ja"): "2026年、営業キャッシュフローは15%増加しました。",
    ("Operating cash flow rose by 15% in 2026.", "ar"): "ارتفع التدفق النقدي التشغيلي بنسبة 15% في عام 2026.",
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--diagnostics-out', type=Path, required=True)
    args = parser.parse_args()
    report = {'provider': PROVIDER, 'provider_requests': 0, 'api_cost_cny': 0,
              'status': 'running', 'semantic_review': 'required', 'samples': [], 'errors': []}
    translator = OfflineTranslator()
    started = time.monotonic()
    # Model downloads belong to the separate installer. Translation is offline.
    with mock.patch('urllib.request.urlopen', side_effect=AssertionError('Translation attempted network access')), \
         mock.patch('requests.sessions.Session.request', side_effect=AssertionError('Translation attempted HTTP')):
        for source in ('今年公司收入增长12.5%，营业利润率为8%。',
                       'Operating cash flow rose by 15% in 2026.',
                       '阅读完整报告并查看图表数据。'):
            protected, unit = locales.unit_for_text(source, 'html:text:p')
            for locale in locales.LOCALES:
                row = {'source': source, 'locale': locale}
                try:
                    row['translation'] = translator.translate(unit.source, locale)
                    locales.validate_translation_quality(locale, unit, row['translation'])
                    row['translation'] = protected.restore(row['translation'])
                    expected = REVIEWED_FINANCIAL_SAMPLES.get((source, locale))
                    if expected is not None and row['translation'] != expected:
                        raise ValueError("Reviewed financial sample does not preserve the approved cash-flow meaning")
                    row['status'] = 'passed'
                except Exception as error:
                    row['status'] = 'failed'
                    row['error'] = str(error)
                    report['errors'].append(f'{locale}: {error}')
                report['samples'].append(row)
        # These sentences are not covered by reviewed phrase overrides. Keep
        # both sides in the artifact for actual financial semantic review.
        for source_language, target, source in (
            ('en', 'zh', 'Revenue fell by 8.2% year on year in the first half of 2026.'),
            ('en', 'zh', 'The operating margin increased by 2.5 percentage points to 18.5%.'),
            ('en', 'zh', 'Cash reserves were USD 120 million on September 15, 2026.'),
            ('zh', 'en', '2026年上半年，公司收入同比下降8.2%。'),
            ('zh', 'en', '营业利润率上升2.5个百分点，达到18.5%。'),
            ('zh', 'en', '截至2026年9月15日，现金储备为1.2亿美元。'),
        ):
            row = {'source': source, 'source_language': source_language, 'locale': target,
                   'semantic_review': 'pending-human-review', 'reviewed_override': False}
            try:
                row['translation'] = translator.translate(source, target, source_language)
                if target == 'zh' and not locales.CJK_RE.search(row['translation']):
                    raise ValueError('English-to-Chinese sample contains no Chinese translation')
                if target == 'en' and locales.CJK_RE.search(row['translation']):
                    raise ValueError('Chinese-to-English sample retains Chinese prose')
                row['status'] = 'passed-structural-checks'
            except Exception as error:
                row['status'] = 'failed'
                row['error'] = str(error)
                report['errors'].append(f'{source_language}->{target}: {error}')
            report['samples'].append(row)
        source = '# Financial outlook\n\nRevenue increased by 12.5% in 2026.\n\n| Metric | Value |\n| --- | --- |\n| Revenue | USD 120 million |\n\n![Chart](https://example.org/figure.png)\n'
        try:
            text = translator.translate_markdown(source, target='zh', source='en')
            for marker in ('12.5%', '2026', '120', 'https://example.org/figure.png', '| --- | --- |'):
                if marker not in text:
                    raise ValueError(f'Markdown lost {marker}')
            if not locales.CJK_RE.search(text):
                raise ValueError('Report translation has no Chinese text')
            report['report_sample'] = {'source': source, 'translation': text}
        except Exception as error:
            report['errors'].append(f'report: {error}')
    report['seconds'] = round(time.monotonic() - started, 2)
    report['status'] = 'failed' if report['errors'] else 'passed'
    args.diagnostics_out.parent.mkdir(parents=True, exist_ok=True)
    args.diagnostics_out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return int(bool(report['errors']))


if __name__ == '__main__':
    raise SystemExit(main())
