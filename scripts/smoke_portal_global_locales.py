#!/usr/bin/env python3
"""Actions-only language qualification using the pinned local CPU model.

This checks structure, protected source references, and complete numbers. It is
not a claim of native-speaker semantic review or production publication.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import time
from compare_hymt_translation import require_actions
from offline_translation import MODEL_ID, PROVIDER, OfflineTranslator, atomic_json
from portal_language_registry import selected_locales
import build_portal_locales as builder
from financial_quantity_integrity import quantity_issues

# Fixed public website-related samples: never private reports or credentials.
SAMPLES = (
    ('description', '这份报告分析半导体需求、市场风险和研究方法。', 'zh'),
    ('figures', '今年公司收入增长12.5%，营业利润率为8%。', 'zh'),
    ('citation', '阅读研究结论与来源：[报告](https://example.org/report.pdf)。', 'zh'),
)

def qualify(targets, output: Path, translator=None) -> dict:
    codes=selected_locales(targets)
    # Loading the adapter does not enable any remote paid provider.
    diagnostics=[]
    translator=translator or OfflineTranslator(diagnostic_callback=diagnostics.append)
    report={'schema_version':1,'provider':PROVIDER,'model':MODEL_ID,
            'targets':list(codes),'paid_provider_requests':0,'api_cost_cny':0,
            'semantic_review':'pending','production_ready':False,'samples':[],
            'qualified_locales':[],'blocked_locales':[]}
    for code in codes:
        passed=True
        for kind, source, source_language in SAMPLES:
            row={'locale':code,'kind':kind,'source':source,
                 'source_sha256':hashlib.sha256(source.encode()).hexdigest()}
            started=time.monotonic()
            diagnostics.clear()
            try:
                protected, unit=builder.unit_for_text(source,'html:text:p')
                translated=translator.translate(unit.source,code,source_language)
                builder.validate_translation_quality(code,unit,translated)
                row['translation']=protected.restore(translated)
                problems=quantity_issues(source,row['translation'],source_language,code)
                if problems: raise ValueError('Restored quantity check: '+'; '.join(problems))
                if kind=='citation' and (row['translation'].count('](') != 1 or
                                         row['translation'].count(')') != source.count(')') or
                                         '](https://example.org/report.pdf)' not in row['translation']):
                    raise ValueError('Source citation changed')
                row['status']='structural-checks-passed'
            except Exception as error:
                passed=False; row.update(status='blocked',error=str(error),diagnostics=list(diagnostics))
            row['seconds']=round(time.monotonic()-started,3)
            report['samples'].append(row)
            atomic_json(output,report)
        report['qualified_locales' if passed else 'blocked_locales'].append(code)
        atomic_json(output,report)
    report['status']='passed' if not report['blocked_locales'] else 'blocked'
    atomic_json(output,report)
    return report

def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--targets',default='all')
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    require_actions()
    result=qualify(args.targets,args.output)
    print(json.dumps({key:result[key] for key in ('status','qualified_locales','blocked_locales','paid_provider_requests')}))
    return 0 if result['status']=='passed' else 1

if __name__=='__main__': raise SystemExit(main())
