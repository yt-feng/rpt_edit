import copy
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

import preflight_wechat_source_figures as preflight
from test_mineru_figure_sources import Fixture
from wechat_image_quality import source_chart_images


class PreflightTests(unittest.TestCase):
    def test_missing_backup_figures_are_reported_for_the_entire_batch_and_never_pass(self):
        from original_pdf_figures import digest, encode
        from ocr_page_sources import RECEIPT
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            fixture = Fixture(root / 'mineru'); fixture.create(); fixture.status()
            original = root / 'originals'; original.mkdir()
            (original / RECEIPT).write_bytes(b'{}')
            (original / 'original.pdf').write_bytes(fixture.original.read_bytes())
            text = 'Original report discussion.'
            pages = [{'page': 1, 'text': text, 'text_sha256': digest(text.encode()),
                      'empty_text': False, 'method': 'native'}]
            reports, retained = [], []
            for number in range(1, 4):
                rid = f'R{number:03d}'; source = f'report-{number}.pdf'
                directory = original / 'ocr_sources' / rid; directory.mkdir(parents=True)
                (directory / 'pages.json').write_bytes(encode(pages))
                reports.append({'id': rid, 'source_pdf': source, 'content_sha256': fixture.original_sha,
                                'original_pdf_path': 'original.pdf', 'page_count': 1})
                retained.append({'binding': {'source_pdf': source, 'content_sha256': fixture.original_sha},
                                 'directory': fixture.report.relative_to(root).as_posix()})
            with patch('market_views_source_digest._chart_regions', return_value=[]):
                result = preflight.audit(original, root, root / 'audit', {'reports': reports}, {'reports': retained})
            self.assertEqual(result['status'], 'incomplete')
            self.assertEqual(result['category'], 'native_backup_missing_figures')
            self.assertEqual(result['report_count'], 3)
            self.assertEqual(result['missing_backup_source_ordinals'], [1, 2, 3])
            self.assertEqual(result['primary_original_crops_replayed'], 3)

    def test_complete_chart_archive_has_an_explicit_profile_above_old_incident_limit(self):
        from inspect_market_views_r2_cache import bounded_size, InvalidObject
        head = {'ContentLength': 1018234618, 'Metadata': {'sha256': 'a' * 64}}
        client = Mock(); client.head_object.return_value = head
        with self.assertRaisesRegex(InvalidObject, 'object_size_limit'):
            bounded_size(head)
        self.assertEqual(preflight.source_archive_head(client, 'private', 'exact.tar.gz'), head)
        head['ContentLength'] = preflight.MAX_ARCHIVE_BYTES + 1
        with self.assertRaisesRegex(InvalidObject, 'object_size_limit'):
            preflight.source_archive_head(client, 'private', 'exact.tar.gz')
        head['ContentLength'] = 1018234618; head['Metadata'] = {}
        with self.assertRaises(ValueError):
            preflight.source_archive_head(client, 'private', 'exact.tar.gz')

    def test_explicit_archive_profile_keeps_hash_head_and_expansion_checks(self):
        from inspect_market_views_r2_cache import ReadOnlyClient, InvalidObject
        from test_inspect_market_views_r2_cache import FakeR2, archive_bytes
        payload = archive_bytes({'figure.png': b'x' * 2048})
        client = FakeR2(); client.add('exact.tar.gz', payload)
        head = client.head_object(Key='exact.tar.gz')
        with tempfile.TemporaryDirectory() as temporary:
            target = str(Path(temporary) / 'source.tar.gz')
            reader = ReadOnlyClient(client, head, archive_limit=len(payload), expanded_limit=4096)
            reader.download_file('private', 'exact.tar.gz', target)
            self.assertEqual(Path(target).read_bytes(), payload)
            reader = ReadOnlyClient(client, head, archive_limit=len(payload), expanded_limit=1024)
            with self.assertRaisesRegex(InvalidObject, 'archive_expansion_limit'):
                reader.download_file('private', 'exact.tar.gz', target)
            client.objects['exact.tar.gz']['Body'] = payload[:-1] + bytes([payload[-1] ^ 1])
            with self.assertRaisesRegex(InvalidObject, 'archive_hash_mismatch'):
                reader.download_file('private', 'exact.tar.gz', target)
            client.objects['exact.tar.gz']['ContentLength'] += 1
            with self.assertRaisesRegex(InvalidObject, 'archive_changed'):
                reader.download_file('private', 'exact.tar.gz', target)

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
