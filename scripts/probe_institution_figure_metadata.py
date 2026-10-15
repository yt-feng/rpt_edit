"""Read exact failed Institution results, including existing physical segments."""
from __future__ import annotations
import argparse
import copy
from contextlib import ExitStack
import json
import os
from pathlib import Path
import tempfile

from mineru_task_ledger import digest, encoded, exact_json
from mineru_completed_child_reuse import read_completed_batch, result_lineage
from mineru_page_segments import read_segment_plan, merge_segments, SegmentArchive
from institution_dependency_backlog import cli_ledger
from institution_original_cache import OriginalCache, validate_binding, OPTIONS
from mineru_result_cache import ResultCache, identity, validate_zip
from mineru_task_ledger import DONE
from consume_legacy_mineru import download_once
from probe_mineru_figure_binding import ReadOnlyR2Client, ReadOnlyStore, ReadOnlyProvider, require, ProbeError
from probe_mineru_figure_binding import compare_cached_pdf, _difference
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


def cached_payload(ledger, cache, binding, *, download=None, budget=lambda: None, downloads=None):
    claim, _ = ledger.store.get('sources/' + binding['id'])
    require(isinstance(claim, dict) and exact_json(claim.get('binding'), binding), 'source_claim_missing')
    root, _ = ledger._read_batch(claim['batch_key'])
    require(any(exact_json(item, binding) for item in root['files']), 'source_root_mismatch')
    rows, counts = read_completed_batch(ledger, root)
    require(counts['all_succeeded'], 'source_root_incomplete')
    row = rows[binding['id']]
    payload = cache.get(binding, row['_recovery_lineage'])
    if payload is None:
        require(download is not None, 'source_result_cache_missing')
        require(str(row.get('state', '')).lower() in DONE, 'source_result_incomplete')
        lineage = result_lineage(ledger, binding, root, row)
        audit = {'source_binding_sha256': binding['id'], 'cache_identity_sha256': identity(binding, lineage),
                 'status': 'attempted'}
        budget()
        if downloads is not None:
            downloads.append(audit)
        payload = download(row.get('full_zip_url'))
        budget(); validate_zip(payload); budget()
        audit.update(status='validated', bytes=len(payload), result_zip_sha256=digest(payload))
    return payload


def embedded_pdf(payload):
    import mineru_figure_sources as figures
    from consume_legacy_mineru import safe_unzip
    with tempfile.TemporaryDirectory(prefix='institution-embedded-diagnostic-') as directory:
        root = Path(directory) / 'raw'; safe_unzip(payload, root)
        found = figures._metadata_files(root)
        require(found is not None, 'provider_metadata_missing')
        pdfs = [path for path in found[2] if path.is_file() and path.suffix.lower() == '.pdf']
        require(len(pdfs) == 1, 'embedded_pdf_ambiguous')
        return figures._regular(pdfs[0], root, 512 * 1024 * 1024)


def segment_pixel_diagnostics(original, merged, plan, payloads, binding, archive, page_index, budget):
    """Compare one actually selected failing page at all immutable boundaries."""
    import fitz
    import mineru_figure_sources as figures
    require(type(page_index) is int and page_index >= 0, 'diagnostic_page_invalid')
    matches = [(segment, payload) for segment, payload in zip(plan['segments'], payloads)
               if segment['page_start'] <= page_index + 1 <= segment['page_end']]
    require(len(matches) == 1, 'diagnostic_segment_ambiguous')
    segment, payload = matches[0]
    physical = archive.get(binding, segment['binding'])
    require(physical is not None, 'segment_archive_missing')
    local_index = page_index + 1 - segment['page_start']
    inputs = [('original', original, page_index), ('physical_segment', physical, local_index),
              ('provider_segment', embedded_pdf(payload), local_index),
              ('merged_provider', embedded_pdf(merged), page_index)]
    result = {'diagnostic_only': True, 'production_acceptance': False,
              'page_index': page_index, 'segment_page_index': local_index,
              'page_start': segment['page_start'], 'page_end': segment['page_end'],
              'documents': {}, 'boundaries': {}}
    with ExitStack() as stack:
        stack.enter_context(figures._silent_mupdf())
        images, geometries = {}, {}
        for name, raw, index in inputs:
            budget()
            document = stack.enter_context(fitz.open(stream=raw, filetype='pdf'))
            require(not document.is_encrypted and index < len(document), 'diagnostic_page_count')
            result['documents'][name] = {'sha256': digest(raw), 'pages': len(document),
                'catalog': {key: document.xref_get_key(document.pdf_catalog(), key)[0]
                            for key in ('OCProperties', 'OutputIntents')}}
            geometries[name] = figures._geometry(document[index])
            images[name] = figures._render(document[index]); stack.callback(images[name].close)
        for left, right in (('original', 'physical_segment'), ('physical_segment', 'provider_segment'),
                            ('provider_segment', 'merged_provider')):
            budget()
            result['boundaries'][left + '_to_' + right] = {
                'geometry_equal': exact_json(geometries[left], geometries[right]),
                'pixels': _difference(images[left], images[right])}
    return result


def inspect_source(ledger, client, bucket, binding, *, download=None, downloads=None):
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
        payload = cached_payload(ledger, cache, binding, download=download, budget=budget, downloads=downloads)
    else:
        payloads, reports = [], []
        for segment in plan['segments']:
            payload = cached_payload(ledger, cache, segment['binding'], download=download,
                                     budget=budget, downloads=downloads)
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
            if result['production_figure_consumer']['status'] == 'rejected' or plan is not None:
                # Diagnostics never change acceptance and use the same eight
                # production decisions, never the generic probe's 100 images.
                try:
                    comparison = compare_cached_pdf(path, payload, original_sha256=binding['sha256'],
                        clock=ledger.clock, deadline=deadline, max_images=8)
                    result['pixel_diagnostic'] = comparison
                    failed = next((page for page in comparison.get('pages', [])
                                   if page.get('default_rgb_equal') is False), None)
                    if plan is not None and failed is None:
                        import fitz
                        with fitz.open(stream=original, filetype='pdf') as document:
                            # The pinned source's prior exact cloud diagnostic
                            # failed at page 1; page 0 already matched. It remains
                            # eligible only if among the actual eight decisions.
                            checked = sorted(comparison.get('pages', []),
                                             key=lambda page: page['page_index'] != 1)
                            failed = next((page for page in checked
                                if document.xref_get_key(document.page_xref(page['page_index']), 'Group')[0]
                                != 'null'), None)
                    if plan is not None and failed is not None:
                        result['segment_pixel_diagnostic'] = segment_pixel_diagnostics(
                            original, payload, plan, payloads, binding,
                            SegmentArchive(client, bucket), failed['page_index'], budget)
                except Exception as error:
                    result['pixel_diagnostic_error'] = (str(error) if isinstance(error, ProbeError)
                                                        else type(error).__name__)
    return result


def probe(ledger, client, bucket, *, download=lambda url: download_once(url, timeout=20)):
    require(ledger.scope == 'institution' and ledger.forbid_new_submissions, 'read_only_scope')
    reader = copy.copy(ledger); reader.store = copy.copy(ledger.store)
    client = ReadOnlyR2Client(client); reader.store.client = client
    reader.store = ReadOnlyStore(reader.store)
    results = []
    for ordinal, row in enumerate(selection()['sources'], 1):
        reader.provider = ReadOnlyProvider(ledger.provider, ledger.clock, ledger.clock() + 480)
        downloads = []
        result = {'ordinal': ordinal, 'provider_zip_downloads': downloads}
        try:
            result.update(inspect_source(reader, client, bucket, binding_for(row),
                                         download=download, downloads=downloads))
        except Exception as error:
            result.update(status='stopped', category=str(error) if isinstance(error, ProbeError)
                          else type(error).__name__)
        result['provider_status_gets'] = reader.provider.gets
        results.append(result)
    reader.store.verify()
    return {'schema': 1, 'diagnostic_only': True, 'production_acceptance': False,
        'source_run_id': '38658714099', 'sources': results,
        'provider_posts': 0, 'provider_uploads': 0, 'cache_writes': 0, 'ledger_writes': 0,
        'provider_zip_download_attempts': sum(len(row['provider_zip_downloads']) for row in results),
        'provider_status_gets': sum(row['provider_status_gets'] for row in results),
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
