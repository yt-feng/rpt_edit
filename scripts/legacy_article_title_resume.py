"""Admit one retained title-only failure from its independently pinned archive."""
from __future__ import annotations
import json
from pathlib import Path

from ocr_page_sources import decode, digest

ARCHIVE_SHA = '5c94fdc2352fb0620f6fd60c208ea724874eeda23b9272cd39b2572d2e817a09'
ARCHIVE_BYTES = 2072910
CONTEXT_SHA = 'd43d1c72c35edfb3cc0e771d446ea8580cebc4d53c5db9a97442b835f11c7f8f'
OLD_CONTRACT = '38322b7597e2f8ba740ea8a902eddd23f6f489027fa48d0f5b74875952b6055e'
BODY_SHA = '39ab8a0b90489d9454b54f8ba2f4606f95c793ba0510ff6e72cca901a17deab7'
BODY_BYTES = 4763
PROMPT_SHA = 'a2ca6fa50bb4bf26e5cf49a4312a634b31504a31f3f3d4d9282a1538425b2d78'
SOURCE_SHA = 'dda8bf2a62c853e835a7a22f53bd79cadfa249debe1d44aee71238c1923e6d6c'
PROOF = 'legacy_title_resume.json'


def require(condition, code):
    if not condition: raise ValueError(code)


def encode(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=True, separators=(',', ':')).encode()


def incident(context):
    return digest(encode(context)) == CONTEXT_SHA


def authorize(checkpoint, context, archive_head):
    """Called only after the HEAD-pinned read-only adapter verified the archive."""
    if not incident(context): return
    metadata = decode((checkpoint/'articles/source_provenance.json').read_bytes())
    directory = metadata['sources'][27]['directory']
    # Later resumptions use their durable staged receipt, not a new legacy admission.
    if (checkpoint/'generation-progress'/directory/'article_generation_progress.json').is_file(): return
    require(archive_head.get('ContentLength') == ARCHIVE_BYTES
            and archive_head.get('Metadata',{}).get('sha256') == ARCHIVE_SHA, 'legacy_title_archive_mismatch')
    from inspect_recovered_article_generation import inspect_checkpoint
    report = inspect_checkpoint(checkpoint,context['source_execution_sha'],context['handoff_execution_sha'])
    require(report['completed_article_count'] == 27 and report['failed_source_ordinal'] == 28
            and report['terminal_category'] == 'generated_article_unbound'
            and report['title_needs_repair'] is True and report['title_repair_attempted'] is True
            and report['title_repair_error_present'] is False and report['title_quality_issues_present'] is False,
            'legacy_title_diagnosis_mismatch')
    root = checkpoint/'articles'/directory
    status_raw = (root/'status.json').read_bytes(); status = decode(status_raw)
    body_raw = (root/'wechat_article.md').read_bytes()
    source = metadata['sources'][27]
    receipt = decode(metadata['source_receipt_json'].encode())
    pages_raw = (root/'source_ocr_pages.json').read_bytes()
    from recover_report_articles import _ocr_source, POLICY
    require(status.get('article_recovery') == {'policy':POLICY,'generation_contract_sha256':OLD_CONTRACT}
            and status.get('wechat_source_provenance') == source['provenance']
            and status.get('wechat_article') == 'wechat_article.md'
            and status.get('wechat_editorial_model') == 'deepseek-flash'
            and 'wechat_editorial_binding' not in status and not status.get('error')
            and digest(pages_raw) == source['provenance']['source_pages_sha256'], 'legacy_title_state_mismatch')
    text = _ocr_source(decode(pages_raw), receipt['reports'][27]['page_count'])
    require((root/'source_ocr.md').read_bytes() == text and digest(text) == source['source_markdown_sha256'] == SOURCE_SHA,
            'legacy_title_source_mismatch')
    from wechat_article_quality import audit_wechat_article_markdown
    require(len(body_raw) == BODY_BYTES and digest(body_raw) == BODY_SHA
            and digest((root/'prompt_for_wechat.md').read_bytes()) == PROMPT_SHA and not {'forbidden_meta_section','model_cta'} & set(audit_wechat_article_markdown(body_raw.decode())),
            'legacy_title_body_invalid')
    value = {'schema_version':1,'archive_sha256':ARCHIVE_SHA,'archive_size_bytes':ARCHIVE_BYTES,
        'context_sha256':CONTEXT_SHA,'ordinal':28,'directory':directory,'body_sha256':digest(body_raw),
        'status_sha256':digest(status_raw),'source_markdown_sha256':digest(text),
        'source_provenance_sha256':digest(encode(source['provenance'])),
        'prompt_sha256':digest((root/'prompt_for_wechat.md').read_bytes()),'generation_contract_sha256':OLD_CONTRACT,
        'prior_title_decision':status['wechat_title_decision']}
    (checkpoint/PROOF).write_bytes(encode(value))


def seed(progress, output, directory, plan, context):
    """Migrate only the exact authenticated legacy body, never arbitrary unbound files."""
    path = output.parent/PROOF
    if not path.is_file(): return None
    proof = decode(path.read_bytes())
    if directory.name != proof.get('directory'): return None
    require(incident(context) and proof.get('schema_version') == 1
            and proof.get('archive_sha256') == ARCHIVE_SHA and proof.get('archive_size_bytes') == ARCHIVE_BYTES
            and proof.get('context_sha256') == CONTEXT_SHA and proof.get('ordinal') == 28
            and proof.get('generation_contract_sha256') == OLD_CONTRACT
            and proof.get('source_markdown_sha256') == digest(plan['source_bytes'])
            and proof.get('source_provenance_sha256') == digest(encode(plan['provenance'])), 'legacy_title_proof_mismatch')
    saved = progress.saved_body()
    if saved is not None:
        require(digest(saved.encode()) == proof.get('body_sha256'), 'legacy_title_bytes_changed')
        progress.seed_body(saved,proof=proof)
        return proof['prior_title_decision']
    status_raw = (directory/'status.json').read_bytes(); body = (directory/'wechat_article.md').read_bytes()
    status = decode(status_raw)
    require(digest(status_raw) == proof.get('status_sha256') and digest(body) == proof.get('body_sha256')
            and digest((directory/'prompt_for_wechat.md').read_bytes()) == proof.get('prompt_sha256'), 'legacy_title_bytes_changed')
    decision = status['wechat_title_decision']
    candidates = decision.get('raw_candidates')
    require(isinstance(candidates,list) and len(candidates) <= 100
            and all(isinstance(item,str) and len(item) <= 1000 for item in candidates), 'legacy_title_candidates_invalid')
    progress.seed_body(body.decode(),proof=proof)
    return decision
