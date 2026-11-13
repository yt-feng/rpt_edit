import copy
from pathlib import Path
import tempfile
import unittest

import preflight_wechat_source_figures as preflight
from test_mineru_figure_sources import Fixture
from wechat_image_quality import source_chart_images


class PreflightTests(unittest.TestCase):
    def test_actual_original_pdf_crops_are_replayed_and_wrong_original_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            fixture = Fixture(Path(temporary))
            fixture.create(); fixture.status()
            selected = source_chart_images(fixture.report, require_verified=True)
            self.assertEqual(preflight.replay_primary(fixture.original.read_bytes(), fixture.report, selected), 1)
            with self.assertRaises(ValueError):
                preflight.replay_primary(fixture.original.read_bytes() + b'changed', fixture.report, selected)

    def test_unrelated_producer_is_rejected_before_any_archive_access(self):
        run = {'id': 123, 'path': preflight.DAILY, 'head_branch': 'main', 'status': 'completed',
               'event': 'workflow_dispatch', 'repository': {'full_name': 'owner/repo'},
               'head_repository': {'full_name': 'owner/repo'}, 'head_sha': 'a' * 40}
        self.assertEqual(preflight.producer(run, '123', 'owner/repo', preflight.DAILY), 'a' * 40)
        for key, value in [('head_branch', 'other'), ('path', 'other.yml'), ('status', 'in_progress'),
                           ('head_repository', {'full_name': 'other/repo'})]:
            changed = copy.deepcopy(run); changed[key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                preflight.producer(changed, '123', 'owner/repo', preflight.DAILY)


if __name__ == '__main__':
    unittest.main()
