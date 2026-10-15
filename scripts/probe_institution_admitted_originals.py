"""Read-only canary: restore the exact three still-pending IMF originals."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import tempfile

from institution_admitted_originals import AdmittedOriginalError, AdmittedOriginals, _cache
from institution_original_cache import OriginalCache
from institution_pending_intake import PendingIntake
from institution_verified_originals import VerifiedOriginals, pdf_pages
from mineru_task_ledger import digest, exact_json

ROOT = Path(__file__).resolve().parents[1]
SELECTION = ROOT/'institution_feeds/reviewed_originals/imf-20261015-reviewed.json'
SELECTION_SHA256 = 'c880842e7f022145eaca780dd52017934444ab7c7f1be7208a9cc7f74b81196b'


class ReadOnlyR2:
    def __init__(self, client):
        self.client = client
        self.gets = self.lists = 0
    def get_object(self, **kwargs):
        self.gets += 1
        return self.client.get_object(**kwargs)
    def list_objects_v2(self, **kwargs):
        self.lists += 1
        return self.client.list_objects_v2(**kwargs)


def run_probe(rows, pending, seen, adapter):
    result = {'schema': 1, 'diagnostic_only': True, 'production_acceptance': False,
              'remote_writes': 0, 'provider_posts': 0, 'source_http_requests': 0,
              'model_calls': 0, 'seen_writes': 0, 'sources': []}
    before = pending.path.read_bytes()
    with tempfile.TemporaryDirectory(prefix='institution-admitted-probe-') as directory:
        for ordinal, row in enumerate(rows, 1):
            source = {'ordinal': ordinal, 'expected_sha256': row['sha256'], 'expected_pages': row['pages']}
            try:
                binding = row['binding']; destination = Path(directory)/binding['source']
                restored = adapter.restore(row['item'], binding['source'], pending, destination,
                                           64*1024*1024, force=False, seen=seen)
                if restored is None:
                    raise AdmittedOriginalError('canary_original_not_resumable')
                if not exact_json(restored['admitted_original_resume']['binding'], binding):
                    raise AdmittedOriginalError('canary_original_binding_changed')
                payload = destination.read_bytes()
                if digest(payload) != row['sha256'] or len(payload) != row['size'] or pdf_pages(payload) != row['pages']:
                    raise AdmittedOriginalError('canary_original_bytes_changed')
                source.update(status='verified', sha256=digest(payload), bytes=len(payload), pages=row['pages'],
                              registry_sha256=restored['admitted_original_resume']['registry_sha256'])
            except AdmittedOriginalError as exc:
                source.update(status='rejected', category=str(exc))
            except Exception:
                source.update(status='rejected', category='canary_unexpected_failure')
            result['sources'].append(source)
    if pending.path.read_bytes() != before:
        raise AdmittedOriginalError('canary_pending_changed')
    result['registry'] = dict(adapter.audit)
    result['verified_count'] = sum(row['status'] == 'verified' for row in result['sources'])
    result['status'] = 'success' if result['verified_count'] == len(rows) else 'failure'
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if digest(SELECTION.read_bytes()) != SELECTION_SHA256:
        raise AdmittedOriginalError('canary_selection_changed')
    selection = VerifiedOriginals(SELECTION)
    if len(selection.records) != 3:
        raise AdmittedOriginalError('canary_selection_count')
    seen = json.loads((ROOT/'institution_feeds/seen_state.json').read_text())['items']
    pending = PendingIntake(ROOT/'institution_feeds/pending_intake/imf.json', seen, now=datetime.now(timezone.utc))
    base = _cache(); reader = ReadOnlyR2(base.client)
    adapter = AdmittedOriginals(cache_factory=lambda: OriginalCache.single_attempt(reader, base.bucket))
    result = run_probe(list(selection.records.values()), pending, seen, adapter)
    result.update(selection_sha256=SELECTION_SHA256, r2_get_requests=reader.gets, r2_list_requests=reader.lists)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in ('status', 'verified_count', 'registry')}))
    return 0 if result['status'] == 'success' else 1


if __name__ == '__main__':
    raise SystemExit(main())
