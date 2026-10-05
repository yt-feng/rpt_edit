#!/usr/bin/env python3
"""Offline source-admission regressions, including failed archived OCR sources."""
import copy
import re
import unittest
from pathlib import Path

from market_views_source_readiness import SOURCE_GATES, SourceReadinessError, require_source_readiness

WORKFLOWS = Path(__file__).resolve().parents[1] / '.github/workflows'
MANUAL = '.github/workflows/market-views-native-recovery.yml'
DAILY = '.github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml'
LEGACY = '.github/workflows/market-views-legacy-recovery.yml'
SHA = 'c' * 40


def evidence(workflow=MANUAL, *, status='in_progress', conclusion=None):
    producer = {'id': 12345, 'head_branch': 'main', 'head_sha': SHA, 'path': workflow,
                'status': status, 'conclusion': conclusion, 'event': 'workflow_dispatch'}
    job_name, gates = SOURCE_GATES[workflow]
    steps = [{'name': name, 'number': number, 'status': 'completed', 'conclusion': 'success'}
             for number, name in enumerate(gates, start=3)]
    if workflow == MANUAL:
        steps.append({'name': 'Generate and wait for the exact Market Views PDF',
                      'number': 6, 'status': status, 'conclusion': conclusion})
    job = {'id': 67890, 'run_id': producer['id'], 'head_sha': SHA, 'name': job_name,
           'status': status, 'conclusion': conclusion, 'steps': steps}
    return producer, {'total_count': 1, 'jobs': [job]}


class ReadinessTests(unittest.TestCase):
    def test_legacy_sources_require_all_complete_materialization_archive_and_readback_gates(self):
        producer, jobs = evidence(LEGACY)
        self.assertTrue(require_source_readiness(producer, jobs)['ready'])
        for index in range(3):
            for conclusion in ('failure', 'skipped', 'cancelled'):
                changed = copy.deepcopy(jobs); changed['jobs'][0]['steps'][index]['conclusion'] = conclusion
                with self.subTest(index=index, conclusion=conclusion), self.assertRaises(SourceReadinessError):
                    require_source_readiness(producer, changed)

    def test_legacy_producer_must_be_exact_manual_main_and_can_wait_for_consumer(self):
        producer, jobs = evidence(LEGACY)
        for event in ('schedule', 'pull_request', 'workflow_run', None):
            with self.subTest(event=event), self.assertRaisesRegex(SourceReadinessError, '^invalid_legacy_source_producer$'):
                require_source_readiness({**producer, 'event': event}, jobs)
        self.assertTrue(require_source_readiness(producer, jobs)['ready'])
        producer['status'] = 'completed'; producer['conclusion'] = 'failure'
        self.assertTrue(require_source_readiness(producer, jobs)['ready'])

    def test_legacy_readback_gate_must_bind_exact_producer_sha_and_order(self):
        producer, jobs = evidence(LEGACY)
        jobs['jobs'][0]['head_sha'] = 'e' * 40
        with self.assertRaises(SourceReadinessError): require_source_readiness(producer, jobs)
        jobs['jobs'][0]['head_sha'] = SHA
        jobs['jobs'][0]['steps'][-1]['number'] = 1
        with self.assertRaises(SourceReadinessError): require_source_readiness(producer, jobs)

    def test_manual_producer_waiting_for_this_consumer_does_not_circularly_wait(self):
        producer, jobs = evidence()
        report = require_source_readiness(producer, jobs)
        self.assertTrue(report['ready'])
        self.assertEqual(report['execution_sha'], SHA)
        self.assertEqual(report['source_job_name'], 'recover')
        self.assertEqual(len(report['completed_source_gates']), 3)

    def test_completed_later_pdf_failure_keeps_successful_source_gates_admissible(self):
        for workflow in (MANUAL, DAILY):
            with self.subTest(workflow=workflow):
                producer, jobs = evidence(workflow, status='completed', conclusion='failure')
                self.assertTrue(require_source_readiness(producer, jobs)['ready'])

    def test_failed_skipped_or_pending_gold_audit_cannot_use_previously_archived_r2(self):
        for workflow in (MANUAL, DAILY):
            producer, baseline = evidence(workflow)
            for status, conclusion in (('completed', 'failure'), ('completed', 'skipped'),
                                       ('completed', 'cancelled'), ('completed', 'timed_out'),
                                       ('in_progress', None), ('queued', None), ('completed', None)):
                with self.subTest(workflow=workflow, status=status, conclusion=conclusion):
                    jobs = copy.deepcopy(baseline)
                    audit = next(step for step in jobs['jobs'][0]['steps'] if step['name'].startswith('Audit complete'))
                    audit.update(status=status, conclusion=conclusion)
                    with self.assertRaisesRegex(SourceReadinessError, '^source_gate_not_successful$'):
                        require_source_readiness(producer, jobs)

    def test_all_three_source_gates_are_required_not_only_the_audit(self):
        producer, baseline = evidence()
        for index in range(3):
            with self.subTest(index=index):
                jobs = copy.deepcopy(baseline)
                jobs['jobs'][0]['steps'][index]['conclusion'] = 'failure'
                with self.assertRaisesRegex(SourceReadinessError, '^source_gate_not_successful$'):
                    require_source_readiness(producer, jobs)

    def test_exact_job_and_step_names_reject_missing_or_ambiguous_evidence(self):
        producer, baseline = evidence()
        changes = []
        missing_job = copy.deepcopy(baseline)
        missing_job['jobs'][0]['name'] = 'recover-other'
        changes.append(missing_job)
        duplicate_job = copy.deepcopy(baseline)
        duplicate_job['jobs'].append({**copy.deepcopy(duplicate_job['jobs'][0]), 'id': 67891})
        duplicate_job['total_count'] = 2
        changes.append(duplicate_job)
        missing_step = copy.deepcopy(baseline)
        missing_step['jobs'][0]['steps'][2]['name'] += ' (similar)'
        changes.append(missing_step)
        duplicate_step = copy.deepcopy(baseline)
        duplicate_step['jobs'][0]['steps'].append({**duplicate_step['jobs'][0]['steps'][2], 'number': 7})
        changes.append(duplicate_step)
        for jobs in changes:
            with self.subTest(jobs=jobs):
                with self.assertRaises(SourceReadinessError):
                    require_source_readiness(producer, jobs)

    def test_source_job_must_bind_this_exact_producer_run_and_execution_sha(self):
        producer, baseline = evidence()
        for key, value in (('run_id', 12346), ('run_id', '12345'), ('head_sha', 'd' * 40)):
            with self.subTest(key=key, value=value):
                jobs = copy.deepcopy(baseline)
                jobs['jobs'][0][key] = value
                with self.assertRaisesRegex(SourceReadinessError, '^source_job_run_or_sha_mismatch$'):
                    require_source_readiness(producer, jobs)

    def test_producer_branch_workflow_sha_and_identity_are_validated(self):
        producer, jobs = evidence()
        for key, value in (('head_branch', 'feature'), ('path', '.github/workflows/other.yml'),
                           ('head_sha', 'not-a-sha'), ('id', True), ('id', '12345')):
            with self.subTest(key=key):
                with self.assertRaisesRegex(SourceReadinessError, '^invalid_source_producer$'):
                    require_source_readiness({**producer, key: value}, jobs)

    def test_complete_latest_page_is_required_and_large_runs_fail_closed(self):
        producer, jobs = evidence()
        for count in (2, 101, -1, True, '1', None):
            with self.subTest(count=count):
                with self.assertRaisesRegex(SourceReadinessError, '^incomplete_or_oversized_jobs_response$'):
                    require_source_readiness(producer, {**jobs, 'total_count': count})
        full = copy.deepcopy(jobs)
        full['jobs'].extend({'id': 80000 + index, 'name': 'unrelated ' + str(index)} for index in range(99))
        full['total_count'] = 100
        self.assertTrue(require_source_readiness(producer, full)['ready'])
        full['jobs'].append({'id': 90000, 'name': 'unrelated extra'})
        full['total_count'] = 101
        with self.assertRaises(SourceReadinessError):
            require_source_readiness(producer, full)

    def test_duplicate_job_ids_invalid_steps_and_unstarted_jobs_are_rejected(self):
        producer, baseline = evidence()
        changes = []
        duplicated = copy.deepcopy(baseline)
        duplicated['jobs'].append({**duplicated['jobs'][0], 'name': 'unrelated'})
        duplicated['total_count'] = 2
        changes.append(duplicated)
        for field, value in (('status', 'queued'), ('steps', None), ('steps', ['PRIVATE malformed'])):
            changed = copy.deepcopy(baseline)
            changed['jobs'][0][field] = value
            changes.append(changed)
        duplicated_steps = copy.deepcopy(baseline)
        duplicated_steps['jobs'][0]['steps'][1]['number'] = 3
        changes.append(duplicated_steps)
        for jobs in changes:
            with self.assertRaises(SourceReadinessError) as failure:
                require_source_readiness(producer, jobs)
            self.assertNotIn('PRIVATE', str(failure.exception))

    def test_gate_order_must_match_each_actual_producer_sequence(self):
        for workflow in (MANUAL, DAILY):
            producer, jobs = evidence(workflow)
            steps = jobs['jobs'][0]['steps']
            steps[0]['number'], steps[1]['number'] = steps[1]['number'], steps[0]['number']
            with self.assertRaisesRegex(SourceReadinessError, '^source_gate_order_mismatch$'):
                require_source_readiness(producer, jobs)

    def test_declared_gate_titles_match_current_producer_workflows_and_order(self):
        for workflow, (name, gates) in SOURCE_GATES.items():
            text = (WORKFLOWS / Path(workflow).name).read_text()
            block = re.search(rf'(?ms)^  {re.escape(name)}:\n(.*?)(?=^  [\w-]+:\n|\Z)', text).group(1)
            positions = []
            for gate in gates:
                self.assertEqual(block.count('- name: ' + gate + '\n'), 1)
                positions.append(block.index('- name: ' + gate + '\n'))
            self.assertEqual(positions, sorted(positions))

    def test_consumer_checks_latest_source_gates_before_receipt_and_paid_generation(self):
        workflow = (WORKFLOWS / 'market-views-latex-pdf.yml').read_text()
        start = workflow.index('- name: Verify complete native PDF source receipt')
        resolve = workflow.index('- name: Resolve and validate primary bank source')
        build = workflow.index('- name: Build market views data and LaTeX source')
        block = workflow[start:resolve]
        self.assertIn('/jobs?filter=latest&per_page=100', block)
        self.assertNotIn('--paginate', block)
        self.assertIn('require_source_readiness(producer, source_jobs)', block)
        self.assertIn('source_jobs = json.loads(jobs_result.stdout)', block)
        self.assertLess(block.index('require_source_readiness(producer, source_jobs)'),
                        block.index("'scripts/extract_native_market_sources.py', 'validate'"))
        self.assertLess(resolve, build)
        self.assertNotIn('scripts/test_market_views_source_readiness.py', block)
        ci = (WORKFLOWS / 'public-identity-guard.yml').read_text()
        self.assertLess(ci.index('python3 -B scripts/test_market_views_source_readiness.py'),
                        ci.index('python3 -B scripts/test_market_views_workflow_contract.py'))
        self.assertIn("raw_fixture = os.environ.get('NATIVE_QUALITY_FIXTURE_JSON', '')", block)
        self.assertIn("fixture_args = ['--fixtures', str(fixture_path)]", block)
        self.assertIn("'scripts/audit_market_views_ocr_receipt.py'", block)
        self.assertIn("'--execution-sha', producer['head_sha']", block)
        self.assertNotIn('continue-on-error:', block)
        artifact = workflow.split('- name: Preserve sanitized native source numeric audit', 1)[1].split('\n      - name:', 1)[0]
        self.assertIn("if: ${{ always() && inputs.source_handoff_kind == 'native-pdf' && inputs.acceptance_only != true }}", artifact)
        self.assertIn('path: ${{ runner.temp }}/market-views-native-source-audit.json', artifact)
        self.assertIn('retention-days: 7', artifact)


if __name__ == '__main__':
    unittest.main()
