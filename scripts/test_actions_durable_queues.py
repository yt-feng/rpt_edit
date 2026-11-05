"""Require every owner of a shared writer lock to preserve pending requests.

GitHub applies the incoming run/job's queue policy. One cross-workflow owner
left on the default single slot can still displace a precise recovery request.
"""
from pathlib import Path
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[1]
GROUP_MARKERS = (
    'portal-production-release',
    'extended-locales-r2-pipeline',
    'extended-locales-source-admission',
    'extended-locale-${{ matrix.locale }}',
)
EXPECTED_OWNERS = {
    ('neutral-edge-cutover.yml', 'workflow'),
    ('neutral-locale-resume.yml', 'workflow'),
    ('manual-edge-canonical-redirect-hotfix.yml', 'workflow'),
    ('manual-cloudflare-url-cache-purge.yml', 'workflow'),
    ('portal-ui-hotfix.yml', 'workflow'),
    ('portal-worker-emergency-deploy.yml', 'workflow'),
    ('portal-research-index-refresh.yml', 'job:refresh'),
    ('portal-extended-locales-r2.yml', 'workflow'),
    ('portal-extended-locales-r2.yml', 'job:locale'),
    ('portal-extended-locales-source.yml', 'job:source_snapshot'),
}


class DurableQueuePolicyTests(unittest.TestCase):
    def test_all_shared_writer_lock_owners_keep_multiple_pending_requests(self):
        found = set()
        for path in sorted((ROOT / '.github/workflows').glob('*.yml')):
            workflow = yaml.safe_load(path.read_text())
            owners = [('workflow', workflow)] + [
                ('job:' + name, job) for name, job in workflow.get('jobs', {}).items()
            ]
            for scope, owner in owners:
                concurrency = owner.get('concurrency', {})
                if not isinstance(concurrency, dict):
                    continue
                group = str(concurrency.get('group', ''))
                if not any(marker in group for marker in GROUP_MARKERS):
                    continue
                found.add((path.name, scope))
                with self.subTest(workflow=path.name, scope=scope):
                    self.assertIs(concurrency.get('cancel-in-progress'), False)
                    self.assertEqual(concurrency.get('queue'), 'max',
                        'A default single pending slot can cancel exact recovery before any job starts')
        self.assertEqual(found, EXPECTED_OWNERS)


if __name__ == '__main__':
    unittest.main()
