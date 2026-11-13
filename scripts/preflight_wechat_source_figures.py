"""Read-only replay of one exact Daily's primary and original-PDF backup figures."""
from contextlib import redirect_stderr, redirect_stdout
import json
import os
from pathlib import Path
import re
import sys
import tempfile

from recovered_article_delivery import api, DAILY, MANUAL
from inspect_market_views_r2_cache import ReadOnlyClient, build_client, bounded_size, InvalidObject
from private_workflow_handoff import download_directory, r2_bucket
from ocr_page_sources import RECEIPT, validate_pages_receipt
from original_pdf_figures import SIDECAR, digest, encode, extract, validate, write
from report_extraction_source import ocr_markdown_from_pages
from wechat_image_quality import source_chart_images

WORKFLOW = '.github/workflows/wechat-source-figure-preflight.yml'
MAX_ARCHIVE_BYTES = 2 * 1024 ** 3
MAX_EXPANDED_BYTES = 4 * 1024 ** 3


class FigurePreflightError(ValueError):
    def __init__(self, ordinal, category):
        self.ordinal = ordinal
        self.category = category
        super().__init__(category)


def require(condition):
    if not condition:
        raise ValueError('source_figure_preflight_invalid')


def producer(run, run_id, repository, workflow):
    require(str(run.get('id')) == run_id and run.get('path') == workflow
            and run.get('head_branch') == 'main' and run.get('status') == 'completed'
            and run.get('event') in {'schedule', 'workflow_dispatch'}
            and run.get('repository', {}).get('full_name') == repository
            and run.get('head_repository', {}).get('full_name') == repository
            and re.fullmatch(r'[a-f0-9]{40}', run.get('head_sha', '')))
    return run['head_sha']


def source_archive_head(client, bucket, key):
    head = client.head_object(Bucket=bucket, Key=key)
    bounded_size(head, MAX_ARCHIVE_BYTES)
    require(re.fullmatch(r'[a-f0-9]{64}', str((head.get('Metadata') or {}).get('sha256', ''))))
    return head


def replay_primary(pdf, directory, selected):
    """Re-render the actual original, beyond merely replaying carried PNGs."""
    import fitz
    import mineru_figure_sources as figures
    if (directory / SIDECAR).is_file():
        proof = json.loads((directory / SIDECAR).read_bytes())
        with fitz.open(stream=pdf, filetype='pdf') as document:
            pages = [{'page': index + 1, 'text': page.get_text('text')} for index, page in enumerate(document)]
        validate(proof, lambda name: (directory / name).read_bytes(), original_pdf_sha256=digest(pdf),
                 source_sha256=digest((directory / 'source_mineru.md').read_bytes()), pdf=pdf, pages=pages)
        return len(selected[:3])
    proof = json.loads((directory / 'source_figure_map.json').read_bytes())
    require(proof['original_pdf_sha256'] == digest(pdf))
    assets = {row['path']: row for row in proof['assets']}
    count = 0
    with figures._silent_mupdf(), fitz.open(stream=pdf, filetype='pdf') as document:
        for path in selected[:3]:
            asset = assets[path.relative_to(directory).as_posix()]
            require(asset['mode'] == 'authenticated_original_crop')
            page = document[asset['page_idx']]
            expected = next(row['geometry'] for row in proof['pages'] if row['page_idx'] == asset['page_idx'])
            require(figures._geometry(page) == expected)
            with figures._render(page) as original:
                with original.crop(asset['crop']['pixel_box']) as cropped:
                    require(digest(cropped.tobytes()) == asset['rgb_sha256'])
            count += 1
    return count


def audit(original_root, primary_root, workspace, original_receipt, primary_receipt, progress=lambda _: None):
    from push_xhs_notes_to_wechat_drafts import extra_asset_images
    from build_portal_translated_reports import prepare_clean_markdown
    by_source = {row['binding']['source_pdf']: row for row in primary_receipt['reports']}
    require(len(by_source) == len(original_receipt['reports']))
    source_receipt_sha = digest((original_root / RECEIPT).read_bytes())
    rows = []
    for ordinal, report in enumerate(original_receipt['reports'], 1):
        primary = by_source[report['source_pdf']]
        require(primary['binding']['content_sha256'] == report['content_sha256'])
        pdf = (original_root / report['original_pdf_path']).read_bytes()
        require(digest(pdf) == report['content_sha256'])
        primary_directory = primary_root / primary['directory']
        try:
            selected = source_chart_images(primary_directory, require_verified=True)
            replayed = replay_primary(pdf, primary_directory, selected) if selected else 0
        except Exception:
            raise FigurePreflightError(ordinal, 'primary_figure_replay_failed') from None
        pages_raw = (original_root / 'ocr_sources' / report['id'] / 'pages.json').read_bytes()
        pages = json.loads(pages_raw)
        markdown = ocr_markdown_from_pages(pages, report['page_count'])
        proof, files = extract(pdf, pages, source_sha256=digest(markdown))
        validate(proof, files.__getitem__, original_pdf_sha256=report['content_sha256'],
                 source_sha256=digest(markdown), pdf=pdf, pages=pages)
        directory = workspace / 'native-backup' / report['id']
        write(directory, proof, files)
        (directory / 'source_ocr.md').write_bytes(markdown)
        (directory / 'source_ocr_pages.json').write_bytes(pages_raw)
        status = {'source_method': 'ocr', 'source_markdown': 'source_ocr.md', 'source_pdf': report['source_pdf'],
            'original_pdf_sha256': report['content_sha256'], 'original_figures_sha256': digest(encode(proof)),
            'images': list(files), 'chart_source_image_count': len(files), 'image_source_kind': 'ocr_original_figures',
            'wechat_source_provenance': {'source_kind': 'ocr-pages', 'source_pdf': report['source_pdf'],
                'content_sha256': report['content_sha256'], 'source_receipt_sha256': source_receipt_sha,
                'source_report_id': report['id'], 'source_pages_sha256': digest(pages_raw)}}
        (directory / 'status.json').write_bytes(encode(status))
        admitted = extra_asset_images(directory, set())
        _, translated = prepare_clean_markdown(directory, workspace / 'translation' / report['id'], 3, strict_chart_images=True)
        require(len(admitted) == len(translated) == len(files))
        row = {'ordinal': ordinal, 'primary_retained_figures': len(selected), 'primary_original_crops_replayed': replayed,
               'native_backup_figures': len(admitted), 'native_candidate_count': proof['candidate_count']}
        if selected and not admitted:
            raise FigurePreflightError(ordinal, 'native_backup_missing_figures')
        rows.append(row)
        if ordinal % 5 == 0 or ordinal == len(original_receipt['reports']):
            progress({'event': 'source_figure_preflight_progress', 'checked_reports': ordinal})
    return {'status': 'verified', 'report_count': len(rows), 'primary_reports_with_figures': sum(bool(r['primary_retained_figures']) for r in rows),
            'primary_retained_figures': sum(r['primary_retained_figures'] for r in rows),
            'primary_original_crops_replayed': sum(r['primary_original_crops_replayed'] for r in rows),
            'native_backup_reports_with_figures': sum(bool(r['native_backup_figures']) for r in rows),
            'native_backup_figures': sum(r['native_backup_figures'] for r in rows),
            'reports': rows, 'diagnostic_only': True, 'provider_posts': 0, 'model_calls': 0, 'wechat_writes': 0,
            'r2_writes': 0, 'production_draft_delivery': False}


def main():
    result = {'status': 'incomplete', 'category': 'source_figure_preflight_not_verified'}
    stage = 'producer_metadata'
    try:
        env = os.environ; repository = env.get('GITHUB_REPOSITORY', '')
        require(env.get('GITHUB_ACTIONS') == 'true' and env.get('GITHUB_REF') == 'refs/heads/main'
                and env.get('GITHUB_WORKFLOW_REF') == f'{repository}/{WORKFLOW}@refs/heads/main')
        run_id, recovery_id, date, manifest = [env.get(k, '') for k in ('SOURCE_RUN_ID', 'MINERU_RECOVERY_RUN_ID', 'DATE_FOLDER', 'MANIFEST_SHA256')]
        count = env.get('EXPECTED_ARTICLES', '')
        require(re.fullmatch(r'[1-9][0-9]{0,19}', run_id) and re.fullmatch(r'[1-9][0-9]{0,19}', recovery_id)
                and re.fullmatch(r'[0-9]{6}', date) and re.fullmatch(r'[a-f0-9]{64}', manifest)
                and re.fullmatch(r'[1-9][0-9]{0,3}', count) and int(count) <= 1000)
        original_sha = producer(api(repository, run_id), run_id, repository, DAILY)
        recovery_sha = producer(api(repository, recovery_id), recovery_id, repository, MANUAL)
        with tempfile.TemporaryDirectory() as temporary, open(os.devnull, 'w') as private:
            root = Path(temporary)
            output = sys.stdout
            def progress(value): print(json.dumps(value), file=output, flush=True)
            with redirect_stdout(private), redirect_stderr(private):
                client, bucket = build_client(), r2_bucket()
                for prefix, identity, destination in (('market-ocr-pages-daily', run_id, 'originals'),
                                                       ('mineru-market-sources', recovery_id, 'primary')):
                    key = f'_private-workflow-handoff/{prefix}/{identity}/{date}/shard_0.tar.gz'
                    stage = destination + '_archive'
                    head = source_archive_head(client, bucket, key)
                    reader = ReadOnlyClient(client, head, archive_limit=MAX_ARCHIVE_BYTES, expanded_limit=MAX_EXPANDED_BYTES)
                    download_directory(key, root / destination, client=reader, bucket=bucket)
                    progress({'event': 'source_archive_verified', 'source_kind': destination,
                              'archive_bytes': head['ContentLength']})
                stage = 'source_receipts'
                original = validate_pages_receipt(root / 'originals', date_folder=date, expected_reports=int(count),
                    source_run_id=run_id, execution_sha=original_sha, recovery_run_id=run_id, recovery_execution_sha=original_sha)
                from recover_durable_mineru_sources import validate_sources
                primary = validate_sources(root / 'primary', int(count), date,
                    expected_recovery_run_id=recovery_id, expected_execution_sha=recovery_sha)
                require(original['selected_manifest_sha256'] == primary['manifest_sha256'] == manifest
                        and primary['source_run_id'] == run_id and primary['source_execution_sha'] == original_sha)
                stage = 'figure_replay'
                result = audit(root / 'originals', root / 'primary', root, original, primary, progress)
        print(json.dumps({key: value for key, value in result.items() if key != 'reports'}, sort_keys=True))
    except Exception as error:
        result['error_type'] = type(error).__name__
        result['stage'] = stage
        if isinstance(error, InvalidObject) and str(error) in {'object_size_limit', 'archive_changed',
                'archive_hash_mismatch', 'archive_expansion_limit', 'archive_member_limit', 'archive_format',
                'archive_path', 'archive_duplicate_member', 'object_size_mismatch', 'object_body', 'archive_limit_invalid'}:
            result['category'] = str(error)
        if isinstance(error, FigurePreflightError):
            result.update(category=error.category, source_ordinal=error.ordinal)
        print(json.dumps(result, sort_keys=True))
    Path(os.environ['RUNNER_TEMP'], 'wechat-source-figure-preflight.json').write_bytes(encode(result))
    return 0 if result.get('status') == 'verified' else 2


if __name__ == '__main__':
    raise SystemExit(main())
