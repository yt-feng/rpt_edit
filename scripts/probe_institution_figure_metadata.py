"""Read exact failed Institution results, including existing physical segments."""
from __future__ import annotations
import argparse
import copy
import json
import os
from pathlib import Path
import tempfile

from mineru_task_ledger import digest, encoded, exact_json
from mineru_completed_child_reuse import read_completed_batch
from mineru_page_segments import read_segment_plan, merge_segments
from institution_dependency_backlog import cli_ledger
from institution_original_cache import OriginalCache, validate_binding, OPTIONS
from mineru_result_cache import ResultCache
from probe_mineru_figure_binding import ReadOnlyR2Client, ReadOnlyStore, ReadOnlyProvider, require, ProbeError
from probe_adb_figure_metadata import inspect_payload, structural_failure
from probe_consulting_mineru_figure_binding import verify_production_figures

WORKFLOW = '.github/workflows/institution-figure-metadata-probe.yml'
SELECTION = Path(__file__).parent / 'fixtures/institution_sources/figure_metadata_20261015.json'


def selection():
    raw = SELECTION.read_bytes()
    require(digest(raw) == '44c930b219243cba9a82185015faa00adad38e443f13954786b0486adaef8ae2', 'reviewed_inventory_changed')
    value = json.loads(raw)
    require(value['source_run_id'] == '38658714099' and len(value['sources']) == 4,
            'reviewed_inventory_invalid')
    return value


def binding_for(row):
    value = {'source': row['local_filename'], 'sha256': row['sha256'], 'size': row['bytes'],
             'scope': 'institution', 'endpoint': 'https://mineru.net', 'options': OPTIONS}
    value['id'] = digest(encoded(value))
    validate_binding(value)
    return value


def cached_payload(ledger, cache, binding):
    claim, _ = ledger.store.get('sources/' + binding['id'])
    require(isinstance(claim, dict) and exact_json(claim.get('binding'), binding), 'source_claim_missing')
    root, _ = ledger._read_batch(claim['batch_key'])
    require(any(exact_json(item, binding) for item in root['files']), 'source_root_mismatch')
    rows, counts = read_completed_batch(ledger, root)
    require(counts['all_succeeded'], 'source_root_incomplete')
    payload = cache.get(binding, rows[binding['id']]['_recovery_lineage'])
    require(payload is not None, 'source_result_cache_missing')
    return payload


def inspect_source(ledger, client, bucket, binding):
    import mineru_figure_sources as figures
    deadline = ledger.clock() + 480
    def budget():
        require(ledger.clock() < deadline, 'probe_deadline')
    original = OriginalCache(client, bucket).get(binding)
    require(original is not None, 'original_cache_missing')
    plan = read_segment_plan(ledger, binding)
    cache = ResultCache(client, bucket)
    result = {'source_binding_sha256': binding['id'], 'original_pdf_sha256': digest(original),
              'segmented': plan is not None}
    if plan is None:
        payload = cached_payload(ledger, cache, binding)
    else:
        payloads, reports = [], []
        for segment in plan['segments']:
            payload = cached_payload(ledger, cache, segment['binding'])
            payloads.append(payload)
            reports.append({'page_start': segment['page_start'], 'page_end': segment['page_end'],
                'result_zip_sha256': digest(payload), 'metadata': inspect_payload(payload)})
        result['segments'] = reports
        with tempfile.TemporaryDirectory(prefix='institution-figure-diagnostic-') as directory:
            path = Path(directory) / 'original.pdf'; path.write_bytes(original)
            try:
                payload = merge_segments(plan, payloads, path)
            except figures.FigureSourceError as error:
                result['merge'] = {'status': 'rejected', 'category': error.category,
                                   'frames': structural_failure(error)}
                return result
        result['merge'] = {'status': 'valid'}
    result.update(result_zip_sha256=digest(payload), metadata=inspect_payload(payload))
    if result['metadata']['status'] == 'valid':
        # Reuse the real source-only image producer, exact original crops and
        # consumer replay after raw MinerU data is removed. All files remain in
        # disposable private directories; this is not a completed publication.
        with tempfile.TemporaryDirectory(prefix='institution-figure-acceptance-') as directory:
            path = Path(directory) / 'original.pdf'; path.write_bytes(original)
            result['production_figure_consumer'] = verify_production_figures(
                path, payload, binding['sha256'], budget)
    return result


def probe(ledger, client, bucket):
    require(ledger.scope == 'institution' and ledger.forbid_new_submissions, 'read_only_scope')
    reader = copy.copy(ledger); reader.store = copy.copy(ledger.store)
    client = ReadOnlyR2Client(client); reader.store.client = client
    reader.store = ReadOnlyStore(reader.store)
    results = []
    for ordinal, row in enumerate(selection()['sources'], 1):
        reader.provider = ReadOnlyProvider(ledger.provider, ledger.clock, ledger.clock() + 480)
        result = {'ordinal': ordinal}
        try:
            result.update(inspect_source(reader, client, bucket, binding_for(row)))
        except Exception as error:
            result.update(status='stopped', category=str(error) if isinstance(error, ProbeError)
                          else type(error).__name__)
        results.append(result)
    reader.store.verify()
    return {'schema': 1, 'diagnostic_only': True, 'production_acceptance': False,
        'source_run_id': '38658714099', 'sources': results,
        'provider_posts': 0, 'provider_uploads': 0, 'cache_writes': 0, 'ledger_writes': 0,
        'fresh_feed_requests': 0, 'model_calls': 0, 'publication_writes': 0}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    repo = os.environ.get('GITHUB_REPOSITORY', '')
    require(os.environ.get('GITHUB_EVENT_NAME') == 'workflow_dispatch'
        and os.environ.get('GITHUB_REF') == 'refs/heads/main'
        and os.environ.get('GITHUB_WORKFLOW_REF') == repo + '/' + WORKFLOW + '@refs/heads/main',
        'reviewed_main_only')
    ledger = cli_ledger(args.output.parent)
    result = probe(ledger, ledger.store.client, ledger.store.bucket)
    args.output.write_bytes(encoded(result))
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__': main()
