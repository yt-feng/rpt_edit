#!/usr/bin/env python3
"""Read one exact saved article failure; emit only allowlisted diagnostics."""
from __future__ import annotations

import argparse
from contextlib import redirect_stderr, redirect_stdout
import json
import os
from pathlib import Path
import re
import tempfile

from inspect_market_views_r2_cache import (ReadOnlyClient, build_client, validate_ocr_producer)
from ocr_page_sources import decode, digest
from private_workflow_handoff import download_directory, require_env
from recover_ocr_cache_sources import exact_head

WORKFLOW = '.github/workflows/recovered-article-generation-inspect.yml'
SOURCE_RUN_ID = '37695511597'
HANDOFF_RUN_ID = '38053057754'
GENERATION_JOB_ID = 114216146082
SOURCE_JOB_ID = 114215930086
DATE_FOLDER = '261007'
EXPECTED_REPORTS = 44
MANIFEST_SHA256 = 'd16c57d614166f46f244b4a9ae65ffecce774be8cb1a52f52cdf968574e4a961'
KEY = f'_private-workflow-handoff/xhs-recovery/{SOURCE_RUN_ID}/{DATE_FOLDER}/{MANIFEST_SHA256}/generation.tar.gz'
MAX_LOG_BYTES = 2 * 1024 * 1024
MAX_JSON_BYTES = 16 * 1024 * 1024
CATEGORIES = {'article_generation_failed', 'article_source_validation_failed', 'generated_article_unbound',
    'checkpoint_source_mismatch', 'checkpoint_inventory', 'unbound_output_directory', 'overlapping_source_output',
    'ocr_page_evidence', 'source_count', 'article_binding', 'article_source_inventory',
    'article_directory_inventory', 'invalid_tree_file', 'tree_file_count', 'tree_symlink', 'invalid_json_file'}
TYPES = {'ReadTimeout', 'ConnectTimeout', 'ConnectionError', 'Timeout', 'SSLError', 'HTTPError', 'ChunkedEncodingError', 'ProxyError',
         'JSONDecodeError', 'KeyError', 'TypeError', 'ValueError', 'RuntimeError', 'FileNotFoundError', 'ArticleRecoveryError'}
HTTP_CODES = {400, 401, 402, 403, 404, 408, 409, 413, 422, 425, 429, 500, 502, 503, 504}
SAFE_SITES = {
    ('pdf_to_xhs_batch.py', 'call_deepseek'), ('pdf_to_xhs_batch.py', 'safe_generate_text'),
    ('pdf_to_xhs_batch.py', 'parse_json_response'), ('pdf_to_xhs_batch.py', 'generate_wechat_article'),
    ('pdf_to_xhs_batch.py', 'wechat_title_from_filename'), ('deepseek_http.py', 'request_with_retry'),
    ('deepseek_http.py', 'request_with_key_fallback'), ('wechat_editorial_binding.py', '_fingerprints'),
    ('wechat_editorial_binding.py', 'bind_generated_article'), ('recover_report_articles.py', 'generation_contract'),
    ('recover_report_articles.py', 'load_sources'), ('recover_report_articles.py', 'recover_articles'),
    ('recover_report_articles.py', 'validate_articles'),
}

PUBLIC_FAILURE_CODES = {
    'inspection_article_binding_mismatch',
    'inspection_article_directory_unbound',
    'inspection_article_page_binding_mismatch',
    'inspection_article_policy_mismatch',
    'inspection_article_status_invalid',
    'inspection_article_symlink',
    'inspection_articles_missing',
    'inspection_context_mismatch',
    'inspection_generation_gate_invalid',
    'inspection_generation_gate_order_invalid',
    'inspection_generation_job_invalid',
    'inspection_generation_job_missing',
    'inspection_generation_steps_invalid',
    'inspection_handoff_identity_invalid',
    'inspection_main_identity_invalid',
    'inspection_pending_inventory_oversized',
    'inspection_source_files_invalid',
    'inspection_source_inventory_mismatch',
    'inspection_source_job_mismatch',
    'inspection_source_provenance_mismatch',
    'inspection_source_receipt_invalid',
    'inspection_source_report_invalid',
    'inspection_verification_failed',
    'invalid_private_file',
}


class InspectionError(ValueError):
    """Messages are fixed codes; exceptions themselves are never published."""


def require(condition, category):
    if not condition: raise InspectionError(category)


def read(path, maximum):
    require(path.is_file() and not path.is_symlink() and 0 < path.stat().st_size <= maximum, 'invalid_private_file')
    return path.read_bytes()


def runtime_identity(env):
    repository = env.get('GITHUB_REPOSITORY', '')
    require(env.get('GITHUB_ACTIONS') == 'true' and env.get('GITHUB_REF') == 'refs/heads/main'
            and env.get('GITHUB_EVENT_NAME') == 'workflow_dispatch'
            and re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository)
            and env.get('GITHUB_WORKFLOW_REF') == f'{repository}/{WORKFLOW}@refs/heads/main',
            'inspection_main_identity_invalid')
    return repository


def authenticate(original, handoff, jobs, repository):
    from market_views_source_readiness import require_source_readiness
    request = {'source_run_id': SOURCE_RUN_ID, 'date_folder': DATE_FOLDER,
               'expected_reports': EXPECTED_REPORTS, 'manifest_sha256': MANIFEST_SHA256}
    original_sha = validate_ocr_producer(original, request, repository)
    require(isinstance(handoff, dict) and str(handoff.get('id')) == HANDOFF_RUN_ID
            and handoff.get('path') == '.github/workflows/recover-ocr-cache-sources.yml'
            and handoff.get('status') == 'completed' and handoff.get('conclusion') == 'failure'
            and handoff.get('repository', {}).get('full_name') == repository
            and handoff.get('head_repository', {}).get('full_name') == repository,
            'inspection_handoff_identity_invalid')
    ready = require_source_readiness(handoff, jobs, source_kind='ocr-pages')
    require(ready['source_job_id'] == SOURCE_JOB_ID, 'inspection_source_job_mismatch')
    matches = [row for row in jobs['jobs'] if row.get('id') == GENERATION_JOB_ID]
    require(len(matches) == 1, 'inspection_generation_job_missing')
    job = matches[0]
    require(job.get('run_id') == int(HANDOFF_RUN_ID) and job.get('head_sha') == handoff['head_sha']
            and job.get('name') == 'deliver / generate' and job.get('status') == 'completed'
            and job.get('conclusion') == 'failure', 'inspection_generation_job_invalid')
    steps = job.get('steps')
    require(isinstance(steps, list) and all(isinstance(row, dict) for row in steps), 'inspection_generation_steps_invalid')
    checked = []
    for name, outcome in (
        ('Authenticate original upload and restore exact recovery sources', 'success'),
        ('Generate only missing bound report articles', 'failure'),
        ('Save generation progress even after interruption', 'success'),
    ):
        rows = [row for row in steps if row.get('name') == name]
        require(len(rows) == 1 and rows[0].get('status') == 'completed'
                and rows[0].get('conclusion') == outcome and type(rows[0].get('number')) is int,
                'inspection_generation_gate_invalid')
        checked.append(rows[0]['number'])
    require(checked == sorted(set(checked)) and all(n > 0 for n in checked), 'inspection_generation_gate_order_invalid')
    return original_sha, handoff['head_sha']


def diagnostic(log, status):
    """Classify fixed code sites and typed markers, never return captured text."""
    matches = list(re.finditer(r'^Report article recovery stopped: ([a-z_]{1,80})(?: source_ordinal=([0-9]{1,4}))?$', log, re.M))
    terminal = matches[-1] if matches else None
    category = terminal[1] if terminal and terminal[1] in CATEGORIES else 'unknown'
    ordinal = int(terminal[2]) if terminal and terminal[2] else None
    if ordinal is not None and not 1 <= ordinal <= EXPECTED_REPORTS: ordinal = None
    # Earlier reports' recoverable title errors are not the failing report.
    successes = list(re.finditer(r'^RECOVERED_ARTICLE ordinal=[0-9]+ reused=(?:true|false)$', log, re.M))
    tail = log[successes[-1].end():] if successes else log
    if terminal: tail = tail[:max(0, terminal.end() - (successes[-1].end() if successes else 0))]
    decision = status.get('wechat_title_decision', {})
    if not isinstance(decision, dict): decision = {}
    repair_error = decision.get('repair_error', '')
    if not isinstance(repair_error, str): repair_error = ''
    evidence = tail + '\n' + repair_error[:65536]
    types = sorted(set(re.findall(r'^(?:requests\.exceptions\.|urllib3\.exceptions\.)?([A-Za-z][A-Za-z0-9_]{0,60}):', evidence, re.M)) & TYPES)
    sites = sorted({(Path(path).name, function) for path, function in
        re.findall(r'^\s*File "([^"\n]{1,2048})", line [0-9]+, in ([A-Za-z_][A-Za-z0-9_]{0,80})$', tail, re.M)
        if (Path(path).name, function) in SAFE_SITES})
    http = sorted({int(code) for code in re.findall(r'\bHTTP ([0-9]{3})\b', evidence) if int(code) in HTTP_CODES})
    causes = set()
    if 'Missing DEEPSEEK_API_KEY for ' in evidence: causes.add('missing_model_credential')
    if set(types) & {'ReadTimeout', 'ConnectTimeout', 'Timeout'} or re.search(r'\bread timed out\b', evidence, re.I): causes.add('model_timeout')
    if set(types) & {'ConnectionError', 'SSLError', 'ChunkedEncodingError', 'ProxyError'}: causes.add('model_transport_failure')
    if 'Unexpected DeepSeek response:' in evidence or 'non-json response:' in evidence: causes.add('model_response_invalid')
    if http:
        causes.update('model_http_'+str(code) for code in http)
    if 'WeChat article failed deterministic editorial guard:' in evidence: causes.add('editorial_guard_failed')
    if decision.get('needs_model_repair') is True or bool(decision.get('selected_quality_issues')): causes.add('title_quality_rejected')
    if repair_error: causes.add('title_repair_failed')
    if 'FileNotFoundError' in types: causes.add('generation_file_missing')
    if category == 'generated_article_unbound': causes.add('editorial_binding_missing')
    if category.startswith('checkpoint_'): causes.add('checkpoint_binding_failed')
    if 'DeepSeek generation failed for WeChat article:' in evidence: phase = 'body_generation'
    elif repair_error or 'title_quality_rejected' in causes: phase = 'title_generation'
    elif 'editorial_guard_failed' in causes: phase = 'editorial_guard'
    elif category == 'generated_article_unbound': phase = 'editorial_binding'
    elif category == 'article_source_validation_failed' or category.startswith('checkpoint_'): phase = 'source_validation'
    elif ('recover_report_articles.py', 'generation_contract') in sites: phase = 'generation_contract'
    else: phase = 'unknown'
    return {'terminal_category': category, 'failed_source_ordinal': ordinal, 'phase': phase,
        'typed_causes': sorted(causes) or ['unknown'], 'exception_types': types,
        'code_sites': [{'file': file, 'function': function} for file, function in sites], 'http_statuses': http,
        'title_repair_attempted': decision.get('repair_attempted') is True,
        'title_repair_error_present': bool(repair_error), 'title_needs_repair': decision.get('needs_model_repair') is True,
        'title_quality_issues_present': bool(decision.get('selected_quality_issues'))}


def inspect_checkpoint(root, original_sha, handoff_sha):
    context_raw = read(root/'context.json', MAX_JSON_BYTES)
    context = decode(context_raw)
    expected = {'schema_version': 1, 'source_run_id': SOURCE_RUN_ID, 'source_handoff_run_id': HANDOFF_RUN_ID,
        'source_kind': 'ocr-pages', 'date_folder': DATE_FOLDER, 'expected_articles': EXPECTED_REPORTS,
        'source_execution_sha': original_sha, 'handoff_execution_sha': handoff_sha, 'manifest_sha256': MANIFEST_SHA256}
    require(isinstance(context, dict) and set(context) == set(expected) | {'source_receipt_sha256'}
            and all(context.get(key) == value for key, value in expected.items())
            and type(context['schema_version']) is int and type(context['expected_articles']) is int
            and isinstance(context['source_receipt_sha256'], str) and re.fullmatch(r'[a-f0-9]{64}', context['source_receipt_sha256']),
            'inspection_context_mismatch')
    article_root = root/'articles'
    require(article_root.is_dir() and not article_root.is_symlink(), 'inspection_articles_missing')
    log_path = root/'private-diagnostics/private-generation.log'
    log = read(log_path, MAX_LOG_BYTES).decode('utf-8', errors='replace')
    metadata_path = article_root/'source_provenance.json'
    metadata, sources = None, []
    if metadata_path.exists():
        from ocr_page_sources import EXTRACTION, POLICY, validate_pages_lineage, extraction_key
        from market_views_publication import source_inventory_sha256
        metadata = decode(read(metadata_path, MAX_JSON_BYTES))
        bound = {'schema_version':1,'source_kind':'ocr-pages','date_folder':DATE_FOLDER,'expected_reports':EXPECTED_REPORTS,
            'source_run_id':SOURCE_RUN_ID,'source_handoff_run_id':HANDOFF_RUN_ID,'source_execution_sha':original_sha,
            'source_handoff_execution_sha':handoff_sha,'manifest_sha256':MANIFEST_SHA256,
            'source_receipt_sha256':context['source_receipt_sha256']}
        require(isinstance(metadata, dict) and set(metadata) == set(bound) | {'sources','source_inventory_sha256','source_receipt_json'}
                and all(metadata.get(key) == value for key,value in bound.items())
                and type(metadata['schema_version']) is int and type(metadata['expected_reports']) is int
                and isinstance(metadata.get('source_receipt_json'), str)
                and digest(metadata['source_receipt_json'].encode()) == context['source_receipt_sha256'], 'inspection_source_provenance_mismatch')
        receipt = decode(metadata['source_receipt_json'].encode())
        receipt_keys = {'schema_version','policy','source_kind','complete','date_folder','source_run_id','execution_sha',
            'expected_reports','report_count','total_pages','reports','selected_manifest_sha256',
            'source_inventory_sha256','extraction','files','cache_recovery'}
        require(isinstance(receipt,dict) and set(receipt) == receipt_keys
                and type(receipt['schema_version']) is int and receipt['schema_version'] == 1
                and receipt['policy'] == POLICY and receipt['source_kind'] == 'ocr-pages'
                and receipt['complete'] is True and receipt['extraction'] == EXTRACTION
                and type(receipt['expected_reports']) is int and type(receipt['report_count']) is int
                and receipt['expected_reports'] == receipt['report_count'] == EXPECTED_REPORTS
                and receipt['date_folder'] == DATE_FOLDER and receipt['source_run_id'] == SOURCE_RUN_ID
                and receipt['execution_sha'] == original_sha and receipt['selected_manifest_sha256'] == MANIFEST_SHA256,
                'inspection_source_receipt_invalid')
        validate_pages_lineage(receipt, source_run_id=SOURCE_RUN_ID, source_execution_sha=original_sha,
            recovery_run_id=HANDOFF_RUN_ID, recovery_execution_sha=handoff_sha, manifest_sha256=MANIFEST_SHA256)
        sources = metadata.get('sources')
        require(isinstance(sources, list) and len(sources) == EXPECTED_REPORTS
                and isinstance(receipt.get('reports'), list) and len(receipt['reports']) == EXPECTED_REPORTS,
                'inspection_source_inventory_mismatch')
        files = receipt['files']
        require(isinstance(files,list) and len(files) == EXPECTED_REPORTS * 3 + 1, 'inspection_source_files_invalid')
        source_files = {}
        for row in files:
            require(isinstance(row,dict) and set(row) == {'path','bytes','sha256'}
                    and isinstance(row['path'],str) and row['path'] not in source_files
                    and type(row['bytes']) is int and 0 < row['bytes'] <= 128 * 1024 * 1024
                    and isinstance(row['sha256'],str) and re.fullmatch(r'[a-f0-9]{64}',row['sha256']),
                    'inspection_source_files_invalid')
            source_files[row['path']] = row
        allowed_files = {'selected_to_process_manifest.json'}
        total_pages = 0
        for ordinal, (source, report) in enumerate(zip(sources, receipt['reports']), 1):
            rid = f'R{ordinal:03d}'
            report_keys = {'id','source_pdf','content_sha256','page_count','pages_covered','original_pdf_path','extraction_key','page_cache_sha256'}
            require(isinstance(report,dict) and set(report) == report_keys and report['id'] == rid
                    and isinstance(report['source_pdf'],str) and report['source_pdf'].strip()
                    and isinstance(report['content_sha256'],str) and re.fullmatch(r'[a-f0-9]{64}',report['content_sha256'])
                    and type(report['page_count']) is int and 0 < report['page_count'] <= 1000
                    and report['pages_covered'] == list(range(1,report['page_count']+1))
                    and report['original_pdf_path'] == f'originals/{rid}.pdf'
                    and report['extraction_key'] == extraction_key(report['content_sha256']),
                    'inspection_source_report_invalid')
            paths = (f'originals/{rid}.pdf',f'ocr_sources/{rid}/pages.json',f'ocr_sources/{rid}/page_cache.json')
            require(all(path in source_files for path in paths)
                    and source_files[paths[0]]['sha256'] == report['content_sha256']
                    and source_files[paths[2]]['sha256'] == report['page_cache_sha256'], 'inspection_source_files_invalid')
            allowed_files.update(paths)
            total_pages += report['page_count']
            provenance = {'source_kind':'ocr-pages','source_pdf':report['source_pdf'],
                'content_sha256':report['content_sha256'],'source_receipt_sha256':context['source_receipt_sha256'],
                'source_report_id':rid,'source_pages_sha256':source_files[paths[1]]['sha256']}
            require(isinstance(source, dict) and set(source) == {'directory','source_markdown','source_markdown_sha256','provenance'}
                    and source['directory'] == f'report_{ordinal:04d}_{report["content_sha256"][:12]}'
                    and source['source_markdown'] == 'source_ocr.md' and source['provenance'] == provenance
                    and isinstance(source['source_markdown_sha256'],str) and re.fullmatch(r'[a-f0-9]{64}',source['source_markdown_sha256']),
                    'inspection_source_inventory_mismatch')
        require(set(source_files) == allowed_files and source_files['selected_to_process_manifest.json']['sha256'] == MANIFEST_SHA256
                and sum(row['bytes'] for row in files) <= 512 * 1024 * 1024,
                'inspection_source_files_invalid')
        require(type(receipt['total_pages']) is int and receipt['total_pages'] == total_pages
                and receipt['source_inventory_sha256'] == metadata['source_inventory_sha256'] == source_inventory_sha256(receipt['reports']),
                'inspection_source_inventory_mismatch')
    summary = diagnostic(log, {})
    ordinal = summary['failed_source_ordinal']
    completed, statuses = 0, {}
    from recover_report_articles import POLICY as ARTICLE_POLICY, _ocr_source, usable_article
    expected_dirs = {row['directory'] for row in sources}
    for directory in article_root.iterdir():
        require(not directory.is_symlink(), 'inspection_article_symlink')
        if directory.is_dir(): require(directory.name in expected_dirs, 'inspection_article_directory_unbound')
    for number, source in enumerate(sources, 1):
        directory = article_root/source['directory']
        status_path = directory/'status.json'
        status = decode(read(status_path, MAX_JSON_BYTES)) if status_path.exists() else {}
        require(isinstance(status, dict), 'inspection_article_status_invalid')
        statuses[number] = status
        article = usable_article(directory) if directory.exists() else None
        if article is not None:
            raw_pages = read(directory/'source_ocr_pages.json', MAX_JSON_BYTES)
            file_row = source_files[f'ocr_sources/R{number:03d}/pages.json']
            require(len(raw_pages) == file_row['bytes'] and digest(raw_pages) == file_row['sha256'],
                    'inspection_article_page_binding_mismatch')
            text = _ocr_source(decode(raw_pages),receipt['reports'][number-1]['page_count'])
            require(read(directory/'source_ocr.md', MAX_JSON_BYTES) == text
                    and digest(text) == source['source_markdown_sha256'], 'inspection_article_binding_mismatch')
            require(status.get('article_recovery',{}).get('policy') == ARTICLE_POLICY
                    and status.get('images') == [] and status.get('ocr_figures') == []
                    and status.get('image_source_kind') == 'ocr_pages_text_only', 'inspection_article_policy_mismatch')
            require(status.get('wechat_source_provenance') == source['provenance']
                    and article.binding['source_sha256'] == source['source_markdown_sha256'], 'inspection_article_binding_mismatch')
            completed += 1
    summary = diagnostic(log, statuses.get(ordinal, {}))
    pending = list(article_root.rglob('*.pending.json'))
    require(len(pending) <= 1000, 'inspection_pending_inventory_oversized')
    return {'schema_version':1,'diagnostics_only':True,'source_run_id':SOURCE_RUN_ID,'handoff_run_id':HANDOFF_RUN_ID,
        'generation_job_id':GENERATION_JOB_ID,'date_folder':DATE_FOLDER,'expected_articles':EXPECTED_REPORTS,
        'context_sha256':digest(context_raw),'source_provenance_present':metadata is not None,
        'private_log_sha256':digest(log_path.read_bytes()),'completed_article_count':completed,
        'complete_article_receipt_present':(article_root/'article_recovery_receipt.json').is_file(),
        'pending_marker_count':len(pending),'prior_provider_request_count':'unknown','provider_outcome_resolved':False,
        'inspection_provider_posts':0,'object_writes':0,'object_deletions':0,**summary}


def inspect(client, bucket, original, handoff, jobs, repository, workspace):
    original_sha, handoff_sha = authenticate(original, handoff, jobs, repository)
    head = exact_head(client, bucket, KEY)
    # Only the adapter is passed to download_directory: it has no mutation API.
    download_directory(KEY, workspace/'checkpoint', client=ReadOnlyClient(client, head), bucket=bucket)
    result = inspect_checkpoint(workspace/'checkpoint', original_sha, handoff_sha)
    return {**result, 'archive_sha256':head['Metadata']['sha256'],'archive_size_bytes':head['ContentLength']}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args(argv)
    try:
        repository = runtime_identity(os.environ)
        from recovered_article_delivery import api, jobs
        original, handoff = api(repository,SOURCE_RUN_ID), api(repository,HANDOFF_RUN_ID)
        job_page = jobs(repository,HANDOFF_RUN_ID)
        with tempfile.TemporaryDirectory(prefix='generation-inspection-') as temp:
            with (Path(temp)/'private-inspection.log').open('w') as private, redirect_stdout(private), redirect_stderr(private):
                result = inspect(build_client(),require_env('R2_BUCKET'),original,handoff,job_page,repository,Path(temp))
        result = {'success':True,**result}
    except Exception as error:
        # No arbitrary exception strings/classes, URLs or provider messages.
        result = {'success':False,'category':str(error) if isinstance(error,InspectionError) and str(error) in PUBLIC_FAILURE_CODES else 'inspection_verification_failed',
                  'inspection_provider_posts':0,'object_writes':0,'object_deletions':0}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps(result,sort_keys=True))
    return 0 if result['success'] else 1


if __name__=='__main__':raise SystemExit(main())
