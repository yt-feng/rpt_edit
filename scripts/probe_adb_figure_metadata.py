"""Read the pinned sixth ADB original/result and disclose structural diagnostics only."""
from __future__ import annotations
import argparse
import copy
import json
import math
import os
from pathlib import Path
import tempfile

from mineru_task_ledger import digest, encoded
from mineru_completed_child_reuse import read_completed_batch
from institution_dependency_backlog import Backlog, cli_ledger
from institution_original_cache import OriginalCache
from mineru_result_cache import ResultCache
from restore_completed_institution_sources import selection, restore
from probe_mineru_figure_binding import ReadOnlyProvider, ReadOnlyR2Client, ReadOnlyStore, require

WORKFLOW = '.github/workflows/adb-figure-metadata-probe.yml'


def numbers(value):
    return value if isinstance(value, list) and len(value) <= 4 and all(type(v) in (int, float) and math.isfinite(v) for v in value) else None


def structural_failure(error):
    """No repr(error), raw text, references, HTML, URLs or arbitrary frame locals."""
    frames = []
    trace = error.__traceback__
    while trace:
        frame = trace.tb_frame
        if Path(frame.f_code.co_filename).name == 'mineru_figure_sources.py':
            local = frame.f_locals
            row = {'function': frame.f_code.co_name, 'line': trace.tb_lineno}
            for key in ('ordinal', 'bi', 'pi', 'index', 'width', 'height', 'w', 'h', 'low', 'high'):
                value = local.get(key)
                if type(value) in (int, float) and math.isfinite(value): row[key] = value
            for key in ('value', 'size', 'box', 'body'):
                if key in local:
                    row[key+'_type'] = type(local[key]).__name__
                    if numbers(local[key]) is not None: row[key+'_coordinates'] = local[key]
            for key in ('block', 'child', 'item', 'span'):
                value = local.get(key)
                if isinstance(value, dict):
                    kind = value.get('type')
                    row[key+'_type_hash'] = digest(encoded(kind))
                    if kind in ('text', 'title', 'table', 'chart', 'image', 'table_body', 'image_body', 'chart_body', 'table_caption', 'table_footnote', 'image_caption', 'image_footnote'):
                        row[key+'_type'] = kind
                    if numbers(value.get('bbox')) is not None: row[key+'_bbox'] = value['bbox']
            frames.append(row)
        trace = trace.tb_next
    return frames[-8:]


def failed_table_pair(error):
    trace = error.__traceback__
    while trace:
        frame = trace.tb_frame
        if Path(frame.f_code.co_filename).name == 'mineru_figure_sources.py' and frame.f_code.co_name == '_normalise':
            local = frame.f_locals; parent = local.get('parent'); item = local.get('item')
            if (isinstance(parent, dict) and parent.get('kind') == 'table'
                    and isinstance(item, dict) and item.get('type') == 'table'
                    and isinstance(parent.get('refs'), list) and len(parent['refs']) == 1
                    and isinstance(local.get('body_text'), str)
                    and isinstance(parent['refs'][0].get('html'), str)):
                return {'content_html': local['body_text'], 'middle_html': parent['refs'][0]['html'],
                    'content_index': local['index'], 'page_idx': local['pi']}
        trace = trace.tb_next
    return None


def inspect_payload(payload, export=None, context=None):
    import mineru_figure_sources as figures
    from consume_legacy_mineru import safe_unzip
    with tempfile.TemporaryDirectory(prefix='adb-metadata-') as directory:
        root = Path(directory)/'raw'; safe_unzip(payload, root)
        try:
            found = figures._metadata_files(root)
            require(found is not None, 'metadata_missing')
            (_, content), (_, middle), _ = found
            result = figures._normalise(content, middle)
            return {'status': 'valid', 'pages': len(result['pages']), 'visuals': len(result['records'])}
        except figures.FigureSourceError as error:
            result = {'status': 'rejected', 'category': error.category, 'frames': structural_failure(error)}
            pair = failed_table_pair(error)
            if export is not None:
                require(pair is not None, 'failed_table_pair_missing')
                from export_market_views_original_page_qa import encrypt_payload
                recipient, certificate, target = export
                plaintext = encoded({'schema': 1, 'context': context, 'table_pair': pair})
                require(len(plaintext) <= 256*1024, 'table_pair_size_bound')
                ciphertext = encrypt_payload(plaintext, recipient)
                with open(target, 'xb') as output:
                    os.chmod(target, 0o600); output.write(ciphertext)
                result['encrypted_table'] = {'ciphertext_sha256': digest(ciphertext),
                    'ciphertext_bytes': len(ciphertext), 'plaintext_sha256': digest(plaintext), **certificate}
            return result


def probe(ledger, client, bucket, output, export=None):
    require(ledger.scope == 'institution' and ledger.forbid_new_submissions, 'read_only_scope')
    ledger = copy.copy(ledger); ledger.store = copy.copy(ledger.store)
    client = ReadOnlyR2Client(client); ledger.store.client = client
    ledger.store = ReadOnlyStore(ledger.store)
    ledger.provider = ReadOnlyProvider(ledger.provider, ledger.clock, ledger.clock()+480)
    value, checksum = selection('adb-261013')
    with tempfile.TemporaryDirectory(prefix='adb-pinned-originals-') as directory:
        path = Path(directory)/'originals'
        manifest = restore(ledger, OriginalCache(client, bucket), Backlog(client, bucket), value, path)
        row = sorted(value['sources'], key=lambda source: source['local_filename'])[5]
        require(row['local_filename'] == 'ADB_Understanding-Emission-Trends-in-Mongolia-Insights-from-Envi_368670f7.pdf', 'selected_source_mismatch')
        binding = ledger.bind(path/row['local_filename'], row['local_filename'])
        claim, _ = ledger.store.get('sources/'+binding['id'])
        root, _ = ledger._read_batch(claim['batch_key'])
        rows, counts = read_completed_batch(ledger, root)
        require(counts['all_succeeded'], 'original_root_incomplete')
        payload = ResultCache(client, bucket).get(binding, rows[binding['id']]['_recovery_lineage'])
        require(payload is not None, 'selected_cached_result_missing')
        result = {'schema': 1, 'diagnostic_only': True, 'selection_sha256': checksum,
            'source_ordinal': 6, 'source_binding_sha256': binding['id'],
            'original_pdf_sha256': binding['sha256'], 'result_zip_sha256': digest(payload),
            'provider_posts': 0, 'provider_uploads': 0, 'cache_writes': 0, 'ledger_writes': 0,
            'fresh_feed_requests': 0, 'model_calls': 0, 'publication_writes': 0,
            'original_members': manifest['recovery']['original_members'],
            'metadata': inspect_payload(payload, export, {'source_binding': binding,
                'selection_sha256': checksum, 'result_zip_sha256': digest(payload),
                'source_run_id': value['source_run_id']})}
    ledger.store.verify()
    output.write_bytes(encoded(result))
    print(json.dumps(result, sort_keys=True))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    repo = os.environ.get('GITHUB_REPOSITORY', '')
    require(os.environ.get('GITHUB_EVENT_NAME') == 'workflow_dispatch'
        and os.environ.get('GITHUB_REF') == 'refs/heads/main'
        and os.environ.get('GITHUB_WORKFLOW_REF') == repo+'/'+WORKFLOW+'@refs/heads/main', 'reviewed_main_only')
    try:
        export = None
        certificate = os.environ.get('RECIPIENT_CERT_PEM', '')
        if certificate:
            from export_market_views_original_page_qa import checked_recipient
            recipient, metadata = checked_recipient(certificate)
            target = args.output.with_suffix('.cms')
            require(not target.exists() and not target.is_symlink(), 'encrypted_output_exists')
            export = recipient, metadata, target
        ledger = cli_ledger(args.output.parent)
        probe(ledger, ledger.store.client, ledger.store.bucket, args.output, export)
    except Exception as error:
        args.output.write_bytes(encoded({'schema': 1, 'diagnostic_only': True,
            'status': 'stopped', 'error_type': type(error).__name__}))
        raise SystemExit('Pinned ADB diagnostic stopped; no source data logged.') from None


if __name__ == '__main__': main()
