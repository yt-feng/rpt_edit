"""Offline verification of the producer steps admitting native PDF sources.

Inputs are captured GitHub run metadata and one complete `filter=latest` jobs
page. This module performs no network requests and reads no source contents.
"""
from __future__ import annotations

import re

MAX_JOBS = 100
SOURCE_GATES = {
    '.github/workflows/market-views-native-recovery.yml': (
        'recover',
        ('Extract and verify the complete original source batch',
         'Archive verified native sources in private R2',
         'Audit complete cloud OCR numeric evidence'),
    ),
    '.github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml': (
        'recover-market-sources',
        ('Extract and verify every original report for Market Views',
         'Audit complete cloud OCR backup evidence',
         'Save complete native sources to private R2'),
    ),
}


class SourceReadinessError(ValueError):
    """Fixed error categories avoid reflecting untrusted job/step metadata."""


def _require(condition, category):
    if not condition:
        raise SourceReadinessError(category)


def require_source_readiness(producer, jobs_page):
    """Admit only exact, successfully completed source gates for this run/SHA.

    The enclosing producer may still be waiting for this PDF consumer, or may
    have failed after all source gates. Its overall conclusion is intentionally
    not an admission condition, so the manual generate-and-wait step cannot
    create a circular dependency.
    """
    _require(isinstance(producer, dict), 'invalid_producer_metadata')
    run_id, sha, workflow = producer.get('id'), producer.get('head_sha'), producer.get('path')
    _require(type(run_id) is int and run_id > 0 and producer.get('head_branch') == 'main'
             and isinstance(sha, str) and re.fullmatch(r'[a-f0-9]{40}', sha) is not None
             and isinstance(workflow, str) and workflow in SOURCE_GATES, 'invalid_source_producer')
    _require(isinstance(jobs_page, dict), 'invalid_jobs_response')
    count, jobs = jobs_page.get('total_count'), jobs_page.get('jobs')
    _require(type(count) is int and 0 <= count <= MAX_JOBS and isinstance(jobs, list)
             and len(jobs) == count, 'incomplete_or_oversized_jobs_response')
    job_ids = []
    for item in jobs:
        _require(isinstance(item, dict) and type(item.get('id')) is int and item['id'] > 0,
                 'invalid_job_metadata')
        job_ids.append(item['id'])
    _require(len(job_ids) == len(set(job_ids)), 'ambiguous_jobs_response')
    job_name, step_names = SOURCE_GATES[workflow]
    matches = [item for item in jobs if item.get('name') == job_name]
    _require(len(matches) == 1, 'missing_or_ambiguous_source_job')
    source_job = matches[0]
    _require(type(source_job.get('run_id')) is int and source_job['run_id'] == run_id
             and source_job.get('head_sha') == sha, 'source_job_run_or_sha_mismatch')
    _require(source_job.get('status') in {'in_progress', 'completed'}, 'source_job_not_started')
    steps = source_job.get('steps')
    _require(isinstance(steps, list) and all(isinstance(step, dict) for step in steps), 'invalid_source_steps')
    numbers = [step.get('number') for step in steps]
    _require(all(type(number) is int and number > 0 for number in numbers)
             and len(numbers) == len(set(numbers)), 'ambiguous_source_steps')
    admitted = []
    for name in step_names:
        matches = [step for step in steps if step.get('name') == name]
        _require(len(matches) == 1, 'missing_or_ambiguous_source_gate')
        step = matches[0]
        _require(step.get('status') == 'completed' and step.get('conclusion') == 'success',
                 'source_gate_not_successful')
        admitted.append(step)
    _require([step['number'] for step in admitted] == sorted(step['number'] for step in admitted),
             'source_gate_order_mismatch')
    return {'ready': True, 'producer_run_id': run_id, 'execution_sha': sha,
            'source_job_id': source_job['id'], 'source_job_name': job_name,
            'completed_source_gates': list(step_names)}
