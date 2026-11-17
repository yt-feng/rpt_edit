"""Admit exact source-bound recovered article shards for chart indexing."""
from __future__ import annotations

import argparse
from datetime import datetime
import json
import os
from pathlib import Path
import re


def selection(env) -> dict:
    values = {key: env.get(key, '') for key in ('DATE_FOLDER', 'HANDOFF_RUN_ID',
              'ARTIFACT_RUN_ID', 'HANDOFF_MANIFEST_SHA256', 'EXPECTED_SHARDS', 'EXPECTED_ARTICLES', 'HANDOFF_KIND')}
    if (not re.fullmatch(r'[1-9][0-9]{0,19}', values['HANDOFF_RUN_ID'])
            or values['ARTIFACT_RUN_ID']
            or not re.fullmatch(r'[a-f0-9]{64}', values['HANDOFF_MANIFEST_SHA256'])
            or not re.fullmatch(r'(?:[0-9]{6}|[0-9]{8})', values['DATE_FOLDER'])
            or values['EXPECTED_SHARDS'] != '1'
            or not re.fullmatch(r'[1-9][0-9]{0,3}', values['EXPECTED_ARTICLES'])
            or values['HANDOFF_KIND'] not in {'', 'complete-primary'}):
        raise ValueError('invalid_recovered_chart_selection')
    datetime.strptime(values['DATE_FOLDER'], '%y%m%d' if len(values['DATE_FOLDER']) == 6 else '%Y%m%d')
    values['EXPECTED_ARTICLES'] = int(values['EXPECTED_ARTICLES'])
    if values['EXPECTED_ARTICLES'] > 1000:
        raise ValueError('invalid_recovered_chart_count')
    family = 'xhs-complete' if values['HANDOFF_KIND'] else 'xhs-recovery'
    values['prefix'] = ('_private-workflow-handoff/' + family + '/' + values['HANDOFF_RUN_ID'] + '/'
                        + values['DATE_FOLDER'] + '/' + values['HANDOFF_MANIFEST_SHA256'] + '/articles')
    return values


def validate_handoff(root: Path, config: dict) -> dict:
    if config.get('HANDOFF_KIND') == 'complete-primary':
        from reuse_completed_progressive_sources import validate_complete_handoff
        from report_extraction_source import resolve_extraction_source
        from build_chart_search_index import discover_candidates

        validate_complete_handoff(root, config['HANDOFF_RUN_ID'], config['DATE_FOLDER'],
                                  config['HANDOFF_MANIFEST_SHA256'], config['EXPECTED_ARTICLES'])
        # Keep the original-image chart index separate from reconstructed OCR.
        reports = sorted(path.parent for path in root.glob('*/status.json'))
        if (len(reports) != config['EXPECTED_ARTICLES']
                or any(resolve_extraction_source(path).method != 'mineru' for path in reports)):
            raise ValueError('unsupported_complete_primary_chart_source_kind')
        candidates = discover_candidates(root, {}, date_folder=config['DATE_FOLDER'])
        if not candidates:
            raise ValueError('complete_primary_chart_original_images_missing')
        return {'complete': True, 'reports': config['EXPECTED_ARTICLES'], 'source_kind': 'complete-primary',
                'original_image_count': len(candidates)}
    from recover_report_articles import validate_articles, read_json, PROVENANCE, RECEIPT

    if read_json(root / RECEIPT).get('source_kind') != 'mineru-recovery':
        raise ValueError('unsupported_recovered_chart_source_kind')
    receipt = validate_articles(root, config['EXPECTED_ARTICLES'], config['DATE_FOLDER'], source_kind='mineru-recovery')
    provenance = read_json(root / PROVENANCE)
    if (receipt['source_run_id'] != config['HANDOFF_RUN_ID']
            or provenance.get('manifest_sha256') != config['HANDOFF_MANIFEST_SHA256']):
        raise ValueError('recovered_chart_source_identity_mismatch')
    from build_chart_search_index import discover_candidates
    candidates = discover_candidates(root, {}, date_folder=config['DATE_FOLDER'])
    if not candidates:
        raise ValueError('recovered_chart_original_images_missing')
    # OCR reconstructions never enter the original-image index. The existing
    # source-image names, bytes and authenticated provenance stay intact.
    return {'complete': True, 'reports': receipt['report_count'], 'source_kind': receipt['source_kind'],
            'original_image_count': len(candidates)}


def materialize(destination: Path, config: dict) -> dict:
    from private_workflow_handoff import download_directory

    root = destination / config['DATE_FOLDER'] / 'shard_0'
    if root.exists():
        raise ValueError('recovered_chart_destination_not_empty')
    download_directory(config['prefix'] + '/shard_0.tar.gz', root)
    return validate_handoff(root, config)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--destination', type=Path, required=True)
    args = parser.parse_args()
    config = selection(os.environ)
    print(json.dumps(materialize(args.destination, config), sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
