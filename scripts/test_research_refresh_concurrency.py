#!/usr/bin/env python3
"""Regression contract for eligibility-scoped production serialization."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ResearchRefreshConcurrencyTests(unittest.TestCase):
    def setUp(self):
        self.workflow = (ROOT / '.github/workflows/portal-research-index-refresh.yml').read_text()

    def test_lock_is_job_scoped_not_workflow_scoped(self):
        self.assertNotRegex(self.workflow, re.compile(r'^concurrency:', re.M))
        self.assertIn('    concurrency:\n      group: portal-production-release\n      cancel-in-progress: false', self.workflow)
        self.assertEqual(self.workflow.count('group: portal-production-release'), 1)

    def test_upstream_and_repository_eligibility_are_preserved(self):
        gate = self.workflow.split('    if: >-', 1)[1].split('    concurrency:', 1)[0]
        for required in (
            "github.ref == 'refs/heads/main'",
            "github.event_name == 'workflow_dispatch'",
            "vars.PORTAL_RESEARCH_REFRESH_ENABLED == 'true'",
            "github.event.workflow_run.conclusion == 'success'",
            'github.event.workflow_run.head_branch == github.event.repository.default_branch',
            'github.event.workflow_run.head_repository.full_name == github.repository',
        ):
            self.assertIn(required, gate)
        self.assertIn('types: [completed]', self.workflow)
        self.assertNotIn('always()', gate)

    def test_real_publishers_still_share_a_non_cancelling_lock(self):
        release = (ROOT / '.github/workflows/neutral-edge-cutover.yml').read_text()
        concurrency = re.search(r'^concurrency:\n(.*?)(?=^jobs:\n)', release, re.M | re.S).group(1)
        group = re.search(r'^  group: >-\n(.*?)^  cancel-in-progress: false$',
                          concurrency, re.M | re.S)
        self.assertIsNotNone(group, 'The root release lock must remain non-cancelling')
        preparation = release.split('\n  prepare_release:\n', 1)[1]
        admission = preparation.split('    if: >-\n', 1)[1].split('    runs-on:', 1)[0].strip()
        self.assertTrue(admission.startswith('${{') and admission.endswith('}}'))
        expected = ("${{ ( " + ' '.join(admission[3:-2].split()) +
                    " ) && 'portal-production-release' || "
                    "format('portal-release-ineligible-{0}-{1}', github.run_id, github.run_attempt) }}")
        self.assertEqual(' '.join(group.group(1).split()), expected)
        self.assertIn('default: false', self.workflow)
        self.assertIn('contents: read', self.workflow)
        self.assertIn('scripts/test_research_refresh_concurrency.py', self.workflow)
        self.assertNotIn('cancel-in-progress: true', self.workflow)


if __name__ == '__main__':
    unittest.main()
