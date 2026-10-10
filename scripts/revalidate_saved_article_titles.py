#!/usr/bin/env python3
"""Revalidate one pinned title failure using retained responses, without model calls."""
from __future__ import annotations

import argparse
from contextlib import redirect_stderr, redirect_stdout
import copy
import json
import os
from pathlib import Path
import re
import shutil
import tempfile

import article_generation_progress as progress
import inspect_recovered_article_generation as inspection
import recover_report_articles as articles
import recovered_article_delivery as delivery
import wechat_title_optimizer as titles
from saved_article_title_diagnostics import observe_saved_title_gates, title_excerpt
from inspect_market_views_r2_cache import ReadOnlyClient, build_client
from private_workflow_handoff import download_directory, require_env
from recover_ocr_cache_sources import exact_head
from sensitive_content_guard import sanitize_wechat_stock_language
from wechat_article_quality import audit_wechat_article_markdown
from wechat_editorial_binding import bind_generated_article

WORKFLOW = '.github/workflows/revalidate-saved-article-titles.yml'
POLICY = 'saved-title-whitespace-revalidation-v1'
GENERATION_RUN_ID = '38056186143'
GENERATION_JOB_ID = 114225092309
ORDINAL = 38
ARCHIVE_SHA = '4e645b5f6ed6bb0536b9fe8f2a6a99ab3b8dab851dba0297981a5e9755f89ab7'
ARCHIVE_BYTES = 3102115
CONTEXT_SHA = 'd43d1c72c35edfb3cc0e771d446ea8580cebc4d53c5db9a97442b835f11c7f8f'
OLD_CONTRACT = '2c28f8ede8c08c4ba466888a4650a2196e83a7a29b74097586933882856f553c'
PROGRESS_SHA = '3734b356e03bb26f60b19f18cf9c709b8cf39c949ee647e704d622e0d7911fca'
FILE_PINS = {
    'wechat_article.md': (4373, 'b6e5fe04c94400f12cd5e102ad9fd8a7e03b352334e96f124703a47608c55fe1'),
    'prompt_for_wechat.md': (40471, '6192acb8534198c5a1c112393e2fbb8add99c40ad0ed9919af7fa446cb3aa432'),
    'source_ocr.md': (48042, 'a6e1faa77a08920806fb6b950688b7937e96f9107e51f9f720621eedc6188a5a'),
}
PUBLIC_CODES = {'revalidation_runtime_invalid', 'revalidation_mode_invalid', 'revalidation_archive_changed',
    'revalidation_context_invalid', 'revalidation_incident_invalid', 'revalidation_file_mismatch',
    'revalidation_progress_invalid', 'revalidation_progress_pending', 'revalidation_identity_mismatch',
    'revalidation_candidates_invalid', 'revalidation_title_unready', 'revalidation_title_guard_failed',
    'revalidation_body_invalid', 'revalidation_binding_failed', 'revalidation_unexpected_changes',
    'revalidation_complete_invalid', 'revalidation_write_scope_invalid', 'revalidation_failed'}


class RevalidationError(ValueError):
    pass


def require(condition, category):
    if not condition:
        raise RevalidationError(category)


def snapshot(root):
    return {row['path']: (row['bytes'], row['sha256']) for row in articles.inventory(root)}


def validator_identity():
    files = ('revalidate_saved_article_titles.py', 'saved_article_title_diagnostics.py', 'wechat_title_optimizer.py', 'sensitive_content_guard.py',
             'wechat_article_quality.py', 'wechat_editorial_binding.py')
    return {name: articles.digest((Path(__file__).parent / name).read_bytes()) for name in files}


def runtime_identity(env):
    repo = env.get('GITHUB_REPOSITORY', '')
    require(env.get('GITHUB_ACTIONS') == 'true' and env.get('GITHUB_REF') == 'refs/heads/main'
        and env.get('GITHUB_EVENT_NAME') == 'workflow_dispatch'
        and re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repo)
        and env.get('GITHUB_WORKFLOW_REF') == f'{repo}/{WORKFLOW}@refs/heads/main', 'revalidation_runtime_invalid')
    return repo


def pinned_head(head):
    require(head.get('ContentLength') == ARCHIVE_BYTES and head.get('Metadata', {}).get('sha256') == ARCHIVE_SHA,
            'revalidation_archive_changed')


def retained_progress(root, metadata, source):
    directory = root / 'generation-progress' / source['directory']
    raw = inspection.read(directory / progress.RECEIPT, progress.MAX_STATE_BYTES)
    require(articles.digest(raw) == PROGRESS_SHA, 'revalidation_progress_invalid')
    expected = {key: metadata[key] for key in ('source_run_id', 'source_execution_sha', 'source_handoff_run_id',
        'source_handoff_execution_sha', 'source_kind', 'manifest_sha256', 'source_receipt_sha256')}
    expected.update(directory=source['directory'], source_sha256=source['source_markdown_sha256'],
        provenance_sha256=articles.digest(articles.encoded(source['provenance'])), generation_contract_sha256=OLD_CONTRACT)
    # _load validates identity, response bytes/hashes, inventory and MAX_TITLES.
    # Do not initialize Progress: even its lock file would mutate the snapshot.
    observer = object.__new__(progress.Progress)
    observer.directory, observer.path, observer.identity = directory, directory / progress.RECEIPT, expected
    state = observer._load()
    require(state['identity'] == expected, 'revalidation_identity_mismatch')
    entries = state['requests']
    require(entries and all(entry['state'] == 'complete' for entry in entries), 'revalidation_progress_pending')
    require(entries[0]['kind'] == 'body' and entries[0]['origin'] == 'request'
        and 1 <= len(entries[1:]) <= progress.MAX_TITLES
        and all(entry['kind'] == 'title' and entry['origin'] == 'request' for entry in entries[1:]),
        'revalidation_progress_invalid')
    batches = [titles.extract_title_candidates(observer._response(entry)) for entry in entries[1:]]
    require(all(isinstance(batch, list) and len(batch) <= 12 and all(isinstance(item, str)
        and 0 < len(item) <= 1000 for item in batch) for batch in batches), 'revalidation_candidates_invalid')
    return state, batches


def replace_h1(raw, title=None):
    matches = list(re.finditer(rb'(?m)^#[ \t]+[^\r\n]+', raw))
    require(len(matches) == 1, 'revalidation_body_invalid')
    match = matches[0]
    replacement = b'# <retained-title>' if title is None else b'# ' + title.encode('utf-8')
    return raw[:match.start()] + replacement + raw[match.end():]


def select_title(status, body, batches):
    source, institution = status.get('original_filename'), status.get('institution_name', '')
    require(isinstance(source, str) and 0 < len(source) <= 2048 and isinstance(institution, str)
        and len(institution) <= 200, 'revalidation_incident_invalid')
    excerpt = title_excerpt(body)
    # Match production repair precedence: newest response first, initial last.
    candidates = [value for batch in reversed(batches) for value in batch]
    # The selector also considers filename/evidence fallbacks. Only genuine
    # retained candidates may authorize this special revalidation. Do not use
    # finalize_filename_wechat_title here: short input becomes a filename fallback.
    generated = set()
    for raw in candidates:
        cleaned = titles.clean_filename_wechat_title(raw, institution)
        if len(cleaned.split('：', 1)[-1]) >= 4 and not titles.title_quality_issues(cleaned, institution, source):
            generated.add(cleaned)
    chosen, decision = titles.decide_filename_anchored_title(candidates, source, institution, evidence_text=excerpt)
    if chosen not in generated or decision.get('needs_model_repair') or decision.get('selected_quality_issues'):
        return None, decision
    initial, initial_decision = titles.decide_filename_anchored_title(batches[0], source, institution, evidence_text=excerpt)
    decision.update(repair_attempted=len(batches) > 1,
        repair_candidates=[value for batch in reversed(batches[1:]) for value in batch],
        initial_selection={'title': initial, 'reason': initial_decision.get('selection_reason'),
                           'quality_issues': initial_decision.get('selected_quality_issues', [])})
    chosen, _ = sanitize_wechat_stock_language(chosen, strict_wording=False)
    before = chosen
    chosen, changes = titles.ensure_publishable_neutral_title(chosen, institution, source, evidence_text=body)
    # A retained response must pass; a new deterministic fallback is not model evidence.
    require(not any(change.startswith('quality_') for change in changes)
        and not titles.title_quality_issues(chosen, institution, source)
        and not titles.missing_required_filename_terms(chosen, titles.required_filename_terms(source, institution))
        and titles.filename_title_additions_are_supported(chosen, before, source, body), 'revalidation_title_guard_failed')
    if changes:
        decision.update(pre_neutralization_title=before,
            pre_neutralization_selection_reason=decision.get('selection_reason'),
            selection_reason='deterministic_neutralization', neutralization_changes=changes, selected_title=chosen)
    decision['final_title_after_wording_guard'] = chosen
    return chosen, decision


def complete_receipt(root, metadata):
    rows = []
    for source in metadata['sources']:
        bound = articles.usable_article(root / source['directory'])
        require(bound is not None, 'revalidation_complete_invalid')
        rows.append({'directory': source['directory'], 'source_pdf': source['provenance']['source_pdf'],
            'content_sha256': source['provenance']['content_sha256'], 'source_markdown': source['source_markdown'],
            'source_markdown_sha256': source['source_markdown_sha256'], 'article_sha256': bound.binding['article_sha256'],
            'editorial_binding': bound.binding})
    receipt = {key: metadata[key] for key in ('source_kind', 'date_folder', 'expected_reports', 'source_run_id',
        'source_execution_sha', 'source_handoff_run_id', 'source_handoff_execution_sha', 'source_receipt_sha256',
        'source_inventory_sha256')}
    receipt.update(schema_version=1, policy=articles.POLICY, complete=True, report_count=len(rows), reports=rows,
                   files=articles.inventory(root, exclude=(articles.RECEIPT,)))
    articles.write_json(root / articles.RECEIPT, receipt)
    return articles.validate_articles(root, inspection.EXPECTED_REPORTS, inspection.DATE_FOLDER,
        source_kind='ocr-pages', source_receipt_sha256=metadata['source_receipt_sha256'])


def revalidate_checkpoint(root, candidate_workspace, original_sha, handoff_sha):
    original_inventory = snapshot(root)
    context_raw = inspection.read(root / 'context.json', inspection.MAX_JSON_BYTES)
    require(articles.digest(context_raw) == CONTEXT_SHA, 'revalidation_context_invalid')
    diagnosis = inspection.inspect_checkpoint(root, original_sha, handoff_sha)
    require(diagnosis['completed_article_count'] == inspection.EXPECTED_REPORTS - 1
        and diagnosis['failed_source_ordinal'] == ORDINAL and diagnosis['terminal_category'] == 'generated_article_unbound'
        and not diagnosis['complete_article_receipt_present'] and diagnosis['pending_marker_count'] == 0
        and [row['source_ordinal'] for row in diagnosis['incomplete_articles']] == [ORDINAL], 'revalidation_incident_invalid')
    require(all(row['pending'] == 0 and row['body_complete'] == 1
        and 0 <= row['title_complete'] <= progress.MAX_TITLES for row in diagnosis['retained_progress_observations']),
        'revalidation_progress_pending')
    article_root = root / 'articles'
    metadata = articles.read_json(article_root / articles.PROVENANCE)
    articles.validate_source_evidence(article_root, metadata)
    source = metadata['sources'][ORDINAL - 1]
    directory = article_root / source['directory']
    status = articles.read_json(directory / 'status.json')
    require(status.get('article_recovery') == {'policy': articles.POLICY, 'generation_contract_sha256': OLD_CONTRACT}
        and status.get('wechat_source_provenance') == source['provenance']
        and status.get('wechat_article') == 'wechat_article.md' and not status.get('error')
        and articles.FIELD not in status, 'revalidation_incident_invalid')
    pinned_files = {}
    for name, (size, sha) in FILE_PINS.items():
        raw = inspection.read(directory / name, articles.MAX_FILE_BYTES)
        require(len(raw) == size and articles.digest(raw) == sha, 'revalidation_file_mismatch')
        pinned_files[name] = raw
    state, batches = retained_progress(root, metadata, source)
    body = inspection.read(directory / 'wechat_article.md', articles.MAX_FILE_BYTES)
    require(not {'forbidden_meta_section', 'model_cta'} & set(audit_wechat_article_markdown(body.decode('utf-8'))),
        'revalidation_body_invalid')
    title, decision = select_title(status, body.decode('utf-8'), batches)
    result = {'schema_version': 1, 'policy': POLICY, 'source_ordinal': ORDINAL, 'expected_articles': inspection.EXPECTED_REPORTS,
        'completed_article_count_before': inspection.EXPECTED_REPORTS - 1, 'revalidation_ready': title is not None,
        'retained_body_count': 1, 'retained_title_response_count': len(batches), 'pending_request_count': 0,
        'provider_posts': 0, 'object_writes': 0, 'object_deletions': 0, 'archive_sha256': ARCHIVE_SHA,
        'context_sha256': CONTEXT_SHA, 'progress_sha256': PROGRESS_SHA,
        'new_validator_sha256': articles.digest(articles.encoded(validator_identity())),
        'title_diagnosis': inspection.title_selection_diagnostic(decision),
        'saved_candidate_evidence_diagnosis': observe_saved_title_gates(status, body.decode('utf-8'),
            pinned_files['source_ocr.md'].decode('utf-8'), batches, decision)}
    if title is None:
        require(snapshot(root) == original_inventory, 'revalidation_unexpected_changes')
        return result
    checkpoint = candidate_workspace / 'checkpoint'
    require(not checkpoint.exists(), 'revalidation_unexpected_changes')
    shutil.copytree(root, checkpoint)
    changed = checkpoint / 'articles' / source['directory']
    after_body = replace_h1(body, title)
    require(replace_h1(after_body) == replace_h1(body)
        and not {'forbidden_meta_section', 'model_cta'} & set(audit_wechat_article_markdown(after_body.decode('utf-8'))),
        'revalidation_body_invalid')
    new_status = copy.deepcopy(status)
    new_status.update(wechat_title=title, wechat_title_decision=decision)
    for key in ('wechat_title_stock_language_sanitized', 'wechat_title_neutralization_changes'):
        new_status.pop(key, None)
    (changed / 'wechat_article.md').write_bytes(after_body)
    require(bind_generated_article(changed, new_status), 'revalidation_binding_failed')
    articles.write_json(changed / 'status.json', new_status)
    modified = snapshot(checkpoint)
    allowed = {f'articles/{source["directory"]}/{name}' for name in ('status.json', 'wechat_article.md')}
    require(set(modified) == set(original_inventory)
        and all(modified[name] == value for name, value in original_inventory.items() if name not in allowed),
        'revalidation_unexpected_changes')
    receipt = complete_receipt(checkpoint / 'articles', metadata)
    proof = {'schema_version': 1, 'policy': POLICY, 'source_ordinal': ORDINAL,
        'original_archive_sha256': ARCHIVE_SHA, 'original_archive_size_bytes': ARCHIVE_BYTES,
        'context_sha256': CONTEXT_SHA, 'old_generation_contract_sha256': OLD_CONTRACT,
        'source_provenance_sha256': articles.digest(articles.encoded(source['provenance'])),
        'source_markdown_sha256': source['source_markdown_sha256'], 'old_progress_sha256': PROGRESS_SHA,
        'requests': [{key: entry[key] for key in ('id', 'kind', 'origin', 'prompt_sha256', 'options_sha256',
            'response_path', 'response_sha256', 'response_bytes')} for entry in state['requests']],
        'validator_files': validator_identity(), 'new_validator_sha256': result['new_validator_sha256'],
        'before_article_sha256': articles.digest(body), 'after_article_sha256': articles.digest(after_body),
        'body_except_h1_sha256': articles.digest(replace_h1(body)),
        'before_status_sha256': articles.digest((directory / 'status.json').read_bytes()),
        'after_status_sha256': articles.digest((changed / 'status.json').read_bytes()),
        'article_receipt_sha256': articles.digest((checkpoint / 'articles' / articles.RECEIPT).read_bytes()),
        'unchanged_article_count': inspection.EXPECTED_REPORTS - 1, 'provider_posts': 0}
    audit = checkpoint / 'private-diagnostics' / 'title-revalidation'
    audit.mkdir(parents=True, exist_ok=True)
    articles.write_json(audit / f'ordinal_{ORDINAL:04d}.json', proof)
    (candidate_workspace / 'context.json').write_bytes(context_raw)
    require(snapshot(root) == original_inventory, 'revalidation_unexpected_changes')
    result.update(completed_article_count_after=receipt['report_count'], unchanged_article_count=inspection.EXPECTED_REPORTS - 1,
        body_except_h1_sha256=proof['body_except_h1_sha256'], article_receipt_sha256=proof['article_receipt_sha256'],
        proof_sha256=articles.digest((audit / f'ordinal_{ORDINAL:04d}.json').read_bytes()))
    return result


class ScopedWriter:
    def __init__(self, client, bucket, keys):
        self.client, self.bucket, self.keys, self.attempts = client, bucket, set(keys), 0

    def upload_file(self, filename, bucket, key, **kwargs):
        require(bucket == self.bucket and key in self.keys, 'revalidation_write_scope_invalid')
        self.attempts += 1
        return self.client.upload_file(filename, bucket, key, **kwargs)

    def head_object(self, **kwargs):
        require(kwargs.get('Bucket') == self.bucket and kwargs.get('Key') in self.keys, 'revalidation_write_scope_invalid')
        return self.client.head_object(**kwargs)


def execute(client, bucket, original, handoff, source_jobs, recovery, recovery_jobs, repository, workspace, mode):
    require(mode in {'inspect', 'apply'}, 'revalidation_mode_invalid')
    original_sha, handoff_sha = inspection.authenticate(original, handoff, source_jobs, repository)
    job_id = inspection.authenticate_recovery(recovery, recovery_jobs, repository, GENERATION_RUN_ID)
    require(job_id == GENERATION_JOB_ID, 'revalidation_incident_invalid')
    head = exact_head(client, bucket, inspection.KEY)
    pinned_head(head)
    root = workspace / 'original-checkpoint'
    download_directory(inspection.KEY, root, client=ReadOnlyClient(client, head), bucket=bucket)
    candidate = workspace / 'candidate'
    result = revalidate_checkpoint(root, candidate, original_sha, handoff_sha)
    result.update(success=True, mode=mode, applied=False, generation_run_id=GENERATION_RUN_ID)
    if mode == 'apply':
        require(result['revalidation_ready'], 'revalidation_title_unready')
        # The global source concurrency group serializes this with normal recovery.
        # Recheck the exact old object immediately before any permitted write.
        pinned_head(exact_head(client, bucket, inspection.KEY))
        prefix = inspection.KEY.removesuffix('/generation.tar.gz')
        writer = ScopedWriter(client, bucket, (inspection.KEY, prefix + '/articles/shard_0.tar.gz'))
        try:
            completed = delivery.save_generation(candidate, writer, bucket, complete=True)
            require(completed['article_count'] == inspection.EXPECTED_REPORTS and writer.attempts == 2,
                    'revalidation_complete_invalid')
        except Exception:
            return {**result, 'success': False, 'category': 'revalidation_failed',
                'object_writes': None, 'object_write_attempts': writer.attempts}
        result.update(applied=True, object_writes=2, object_write_attempts=2)
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mode', choices=('inspect', 'apply'), default='inspect')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        repository = runtime_identity(os.environ)
        original, handoff = delivery.api(repository, inspection.SOURCE_RUN_ID), delivery.api(repository, inspection.HANDOFF_RUN_ID)
        source_jobs = delivery.jobs(repository, inspection.HANDOFF_RUN_ID)
        recovery, recovery_jobs = delivery.api(repository, GENERATION_RUN_ID), delivery.jobs(repository, GENERATION_RUN_ID)
        with tempfile.TemporaryDirectory(prefix='title-revalidation-') as temp:
            workspace = Path(temp)
            with (workspace / 'private.log').open('w') as private, redirect_stdout(private), redirect_stderr(private):
                result = execute(build_client(), require_env('R2_BUCKET'), original, handoff, source_jobs,
                    recovery, recovery_jobs, repository, workspace, args.mode)
    except Exception as error:
        result = {'success': False, 'category': str(error) if isinstance(error, RevalidationError)
            and str(error) in PUBLIC_CODES else 'revalidation_failed', 'provider_posts': 0,
            'object_writes': 0, 'object_deletions': 0}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + '\n')
    print(json.dumps(result, sort_keys=True))
    return 0 if result['success'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
