#!/usr/bin/env python3
"""Actions-only production adapter exercise; full outputs require human review."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import time
import build_portal_locales as locales
from offline_translation import MODEL_ID, PROVIDER, OfflineTranslator


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--diagnostics-out', type=Path, required=True)
    args = parser.parse_args()
    translator = OfflineTranslator()
    report = {'provider': PROVIDER, 'model': MODEL_ID, 'paid_provider_requests': 0,
              'api_cost_cny': 0, 'semantic_review': 'pending-human-review', 'samples': [], 'errors': []}
    started = time.monotonic()
    def record(row, operation):
        sample_started = time.monotonic()
        try:
            row['translation'] = operation()
            row['status'] = 'structural-checks-passed'
        except Exception as error:
            row['status'] = 'failed'
            row['error'] = str(error)
            report['errors'].append(f"{row['id']}: {error}")
        row['seconds'] = round(time.monotonic() - sample_started, 3)
        row['semantic_review'] = 'pending-human-review'
        report['samples'].append(row)
        args.diagnostics_out.parent.mkdir(parents=True, exist_ok=True)
        args.diagnostics_out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    # Read shared fixtures without changing them or the independent model runs.
    samples = json.loads(Path(__file__).with_name('translation_quality_samples.json').read_text())
    for sample in samples:
        if sample['source_language'] in {'en', 'zh'} and sample['target_language'] in {'en', 'zh'}:
            record({**sample, 'mode': 'production-adapter'},
                   lambda s=sample: translator.translate(s['text'], s['target_language'], s['source_language']))
    for source in ('今年公司收入增长12.5%，营业利润率为8%。',
                   '公司的毛利率为23%，收入同比下降4.7%。'):
        protected, unit = locales.unit_for_text(source, 'html:text:p')
        for language in locales.LOCALES:
            row = {'id': f'locale-{language}-{len(report["samples"])}', 'text': source,
                   'model_input': unit.source, 'target_language': language,
                   'mode': 'actual-masked-locale'}
            def translate_locale(language=language, unit=unit, protected=protected):
                value = translator.translate(unit.source, language)
                locales.validate_translation_quality(language, unit, value)
                return protected.restore(value)
            record(row, translate_locale)
    markdown = ('# Financial outlook\n\nRevenue fell by 8.2% year on year in the first half of 2026. '
                'The operating margin increased by 2.5 percentage points to 18.5%.\n\n'
                'See [the report](https://example.org/report.pdf) for **cash reserves**.\n\n'
                '| Metric | Value |\n| --- | --- |\n| Cash reserves | USD 120 million |\n\n'
                '![Chart](https://example.org/figure.png)\n\n```python\nrevenue = 120\n```\n')
    def translate_report():
        value = translator.translate_markdown(markdown, 'zh', 'en')
        for token in ('https://example.org/report.pdf', 'https://example.org/figure.png', '| --- | --- |', '```python\nrevenue = 120\n```'):
            if token not in value:
                raise ValueError(f'Markdown lost protected content: {token}')
        return value
    record({'id': 'report-markdown', 'text': markdown, 'mode': 'production-markdown'}, translate_report)
    report['seconds'] = round(time.monotonic() - started, 3)
    report['cache_stats'] = translator.stats
    report['status'] = 'failed' if report['errors'] else 'structural-checks-passed'
    args.diagnostics_out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    lines = ['# Hy-MT2 production adapter samples', '', 'Semantic review: pending human review.', '',
             f"Runtime: {report['seconds']} seconds; paid API calls: 0.", '']
    for row in report['samples']:
        lines += [f"## {row['id']}", '', row['text'], '', row.get('translation', '(rejected)'), '',
                  f"Status: {row['status']}; seconds: {row['seconds']}.", '']
        if row.get('error'): lines += [row['error'], '']
    args.diagnostics_out.with_suffix('.md').write_text('\n'.join(lines))
    return 1 if report['errors'] else 0

if __name__ == '__main__':
    raise SystemExit(main())
