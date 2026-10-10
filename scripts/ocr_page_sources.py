"""Verified original OCR pages, independent of Market Views model synthesis."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import re

KIND = 'ocr-pages'
POLICY = 'verified-ocr-pages-v1'
RECEIPT = 'ocr_pages_receipt.json'
PREFIX = '_private-workflow-handoff/market-ocr-pages-cache-recovery'
EXTRACTION = {'prompt_version': 'complete-ocr-synthesis-v1', 'languages': 'eng+chi_sim',
              'dpi': 220, 'ocr_all_pages': True}
MAX_FILE_BYTES = 128 * 1024 * 1024
MAX_TOTAL_BYTES = 512 * 1024 * 1024


class OCRPagesError(ValueError):
    """Only fixed public failure categories."""


def require(condition, code):
    if not condition: raise OCRPagesError(code)


def digest(raw): return hashlib.sha256(raw).hexdigest()


def encode(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=True, separators=(',', ':')).encode() + b'\n'


def decode(raw):
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, 'ocr_pages_duplicate_json_key')
            result[key] = value
        return result
    try:
        return json.loads(raw, object_pairs_hook=pairs, parse_constant=lambda _: require(False, 'ocr_pages_nonfinite_json'))
    except (UnicodeError, json.JSONDecodeError):
        raise OCRPagesError('ocr_pages_json_invalid') from None


def read(path):
    require(path.is_file() and not path.is_symlink() and 0 < path.stat().st_size <= MAX_FILE_BYTES,
            'ocr_pages_file_missing_or_invalid')
    return path.read_bytes()


def extraction_key(pdf_sha):
    return digest(json.dumps([EXTRACTION['prompt_version'], pdf_sha, EXTRACTION['languages'],
                              EXTRACTION['dpi'], EXTRACTION['ocr_all_pages']]).encode())


def pdf_pages(raw):
    import fitz
    try:
        with fitz.open(stream=raw, filetype='pdf') as document:
            require(not document.needs_pass and 0 < document.page_count <= 1000,
                    'ocr_pages_original_pdf_invalid')
            return document.page_count
    except OCRPagesError: raise
    except Exception: raise OCRPagesError('ocr_pages_original_pdf_invalid') from None


def checked_pages(raw, count):
    from report_extraction_source import ocr_markdown_from_pages
    value = decode(raw)
    require(isinstance(value, dict) and set(value) == {'pages'}, 'ocr_pages_cache_schema_invalid')
    try: ocr_markdown_from_pages(value['pages'], count)
    except ValueError: raise OCRPagesError('ocr_pages_evidence_invalid') from None
    return value['pages']


def inventory(root):
    require(root.is_dir() and not root.is_symlink(), 'ocr_pages_root_invalid')
    files = []
    total = 0
    for path in sorted(root.rglob('*')):
        require(not path.is_symlink(), 'ocr_pages_symlink')
        if path.is_dir(): continue
        if path.name == RECEIPT and path.parent == root: continue
        raw = read(path); total += len(raw)
        require(total <= MAX_TOTAL_BYTES and len(files) < 4001, 'ocr_pages_inventory_oversized')
        files.append({'path': path.relative_to(root).as_posix(), 'bytes': len(raw), 'sha256': digest(raw)})
    return files


def build_pages(input_dir, manifest, cache, output, *, expected_reports, date_folder,
                source_run_id, execution_sha, recovery):
    """Validate every original/cache unit before creating any handoff file.

    Does not invoke or inspect synthesis, model caches, pending submissions or
    OCR executables. Original PDFs are included for independent consumer checks.
    """
    from recover_durable_mineru_sources import frozen_inputs
    from market_views_publication import source_inventory_sha256
    raw, bindings, pairs = frozen_inputs(input_dir, manifest, expected_reports, date_folder)
    require(not output.exists() and not output.is_symlink(), 'ocr_pages_output_not_fresh')
    require(cache.is_dir() and not cache.is_symlink() and not (cache/'pages').is_symlink(), 'ocr_pages_cache_invalid')
    prepared, reports = {}, []
    total = len(raw)
    for ordinal, ((path, _), binding) in enumerate(zip(pairs, bindings), 1):
        rid = f'R{ordinal:03d}'
        pdf = read(path)
        require(digest(pdf) == binding['content_sha256'], 'ocr_pages_original_pdf_changed')
        count = pdf_pages(pdf)
        key = extraction_key(binding['content_sha256'])
        cached = read(cache/'pages'/(key+'.json'))
        pages = checked_pages(cached, count)
        originals_path = f'originals/{rid}.pdf'
        prepared[originals_path] = pdf
        prepared[f'ocr_sources/{rid}/page_cache.json'] = cached
        prepared[f'ocr_sources/{rid}/pages.json'] = encode(pages)
        total += len(pdf) + len(cached) + len(encode(pages))
        require(total <= MAX_TOTAL_BYTES, 'ocr_pages_inventory_oversized')
        reports.append({'id': rid, 'source_pdf': binding['source_pdf'], 'content_sha256': binding['content_sha256'],
            'page_count': count, 'pages_covered': list(range(1,count+1)), 'original_pdf_path': originals_path,
            'extraction_key': key, 'page_cache_sha256': digest(cached)})
    require(len(reports) == expected_reports, 'ocr_pages_report_count_invalid')
    prepared['selected_to_process_manifest.json'] = raw
    receipt = {'schema_version': 1, 'policy': POLICY, 'source_kind': KIND, 'complete': True,
        'date_folder': date_folder, 'source_run_id': source_run_id, 'execution_sha': execution_sha,
        'expected_reports': expected_reports, 'report_count': len(reports),
        'total_pages': sum(row['page_count'] for row in reports), 'reports': reports,
        'selected_manifest_sha256': digest(raw), 'source_inventory_sha256': source_inventory_sha256(reports),
        'extraction': dict(EXTRACTION), 'cache_recovery': recovery,
        'files': [{'path': name, 'bytes': len(data), 'sha256': digest(data)} for name,data in sorted(prepared.items())]}
    require(total + len(encode(receipt)) <= MAX_TOTAL_BYTES, 'ocr_pages_inventory_oversized')
    # Validate identity before committing the already validated page files.
    from market_views_publication import validate_ocr_cache_recovery_lineage
    validate_ocr_cache_recovery_lineage(receipt, source_run_id=source_run_id, source_execution_sha=execution_sha,
        recovery_run_id=recovery['recovery_run_id'], recovery_execution_sha=recovery['recovery_execution_sha'],
        manifest_sha256=digest(raw))
    output.mkdir(parents=True)
    for name, data in prepared.items():
        target = output/name; target.parent.mkdir(parents=True, exist_ok=True); target.write_bytes(data)
    (output/RECEIPT).write_bytes(encode(receipt))
    validate_pages_receipt(output, date_folder=date_folder, expected_reports=expected_reports,
        source_run_id=source_run_id, execution_sha=execution_sha,
        recovery_run_id=recovery['recovery_run_id'], recovery_execution_sha=recovery['recovery_execution_sha'])
    return receipt


def validate_pages_receipt(root, *, date_folder, expected_reports, source_run_id, execution_sha,
                           recovery_run_id, recovery_execution_sha):
    from extract_native_market_sources import read_manifest
    from market_views_publication import source_inventory_sha256, validate_ocr_cache_recovery_lineage
    root = Path(root)
    value = decode(read(root/RECEIPT))
    keys = {'schema_version','policy','source_kind','complete','date_folder','source_run_id','execution_sha',
        'expected_reports','report_count','total_pages','reports','selected_manifest_sha256',
        'source_inventory_sha256','extraction','cache_recovery','files'}
    require(isinstance(value,dict) and set(value) == keys and type(value['schema_version']) is int
            and value['schema_version'] == 1 and value['policy'] == POLICY and value['source_kind'] == KIND
            and value['complete'] is True and value['extraction'] == EXTRACTION,
            'ocr_pages_receipt_contract_invalid')
    require(type(expected_reports) is int and 1 <= expected_reports <= 1000
            and value['expected_reports'] == value['report_count'] == expected_reports
            and type(value['expected_reports']) is int and type(value['report_count']) is int
            and value['date_folder'] == date_folder and value['source_run_id'] == source_run_id
            and value['execution_sha'] == execution_sha, 'ocr_pages_source_identity_invalid')
    files = inventory(root)
    require(value['files'] == files, 'ocr_pages_file_inventory_changed')
    manifest_raw, bindings = read_manifest(root/'selected_to_process_manifest.json',expected_reports)
    require(digest(manifest_raw) == value['selected_manifest_sha256'], 'ocr_pages_manifest_changed')
    validate_ocr_cache_recovery_lineage(value, source_run_id=source_run_id, source_execution_sha=execution_sha,
        recovery_run_id=recovery_run_id, recovery_execution_sha=recovery_execution_sha,
        manifest_sha256=digest(manifest_raw), source_dir=root)
    rows = value['reports']
    require(isinstance(rows,list) and len(rows) == expected_reports, 'ocr_pages_report_count_invalid')
    allowed_files = {'selected_to_process_manifest.json'}
    total_pages = 0
    for ordinal,(row,binding) in enumerate(zip(rows,bindings),1):
        rid=f'R{ordinal:03d}'; original=f'originals/{rid}.pdf'
        row_keys={'id','source_pdf','content_sha256','page_count','pages_covered','original_pdf_path','extraction_key','page_cache_sha256'}
        require(isinstance(row,dict) and set(row)==row_keys and row['id']==rid
                and row['source_pdf']==binding['source_pdf'] and row['content_sha256']==binding['content_sha256']
                and row['original_pdf_path']==original and row['extraction_key']==extraction_key(binding['content_sha256']),
                'ocr_pages_report_binding_invalid')
        pdf=read(root/original)
        require(digest(pdf)==binding['content_sha256'], 'ocr_pages_original_pdf_changed')
        count=pdf_pages(pdf); total_pages+=count
        require(type(row['page_count']) is int and row['page_count']==count and row['pages_covered']==list(range(1,count+1)),
                'ocr_pages_page_count_invalid')
        cache_name=f'ocr_sources/{rid}/page_cache.json'; pages_name=f'ocr_sources/{rid}/pages.json'
        cached=read(root/cache_name)
        require(digest(cached)==row['page_cache_sha256'], 'ocr_pages_cache_binding_invalid')
        pages=checked_pages(cached,count)
        require(read(root/pages_name)==encode(pages), 'ocr_pages_extracted_text_changed')
        allowed_files.update((original,cache_name,pages_name))
    require({row['path'] for row in files}==allowed_files, 'ocr_pages_unexpected_files')
    require(type(value['total_pages']) is int and value['total_pages']==total_pages
            and value['source_inventory_sha256']==source_inventory_sha256(rows)==source_inventory_sha256(bindings),
            'ocr_pages_inventory_binding_invalid')
    return value
