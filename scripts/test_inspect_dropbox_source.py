import unittest
from inspect_dropbox_source import inspect


class DropboxSourceMetadataTests(unittest.TestCase):
    def test_new_files_in_old_folder_do_not_change_source_date(self):
        calls = []
        def reader(token, path, recursive=False):
            calls.append((path, recursive))
            if not recursive:
                return [{'.tag': 'folder', 'name': '261001', 'path_lower': '/zip_backup/261001'}]
            return [{'.tag': 'file', 'name': 'private-report.pdf', 'size': 123,
                     'server_modified': '2026-10-03T20:00:00Z'}]
        result = inspect('private-token', '/zip_backup', '261004', reader=reader)
        self.assertEqual(result['freshness'], 'blocked_source_date')
        self.assertEqual(result['latest_folders'][0]['newest_server_modified'], '2026-10-03T20:00:00Z')
        self.assertEqual(result['report_body_downloads'], 0)
        self.assertNotIn('private-report', str(result))
        self.assertEqual(calls, [('/zip_backup', False), ('/zip_backup/261001', True)])

    def test_new_root_archive_is_reported_without_admitting_an_old_folder(self):
        def reader(token, path, recursive=False):
            if not recursive:
                return [{'.tag': 'folder', 'name': '261001'},
                        {'.tag': 'file', 'name': '261003.zip', 'size': 100,
                         'server_modified': '2026-10-03T20:00:00Z'},
                        {'.tag': 'file', 'name': 'private-note.txt', 'size': 10,
                         'server_modified': '2026-10-02T10:00:00Z'}]
            return []
        result = inspect('token', '/zip_backup', '261004', reader=reader)
        self.assertEqual(result['freshness'], 'blocked_source_date')
        self.assertEqual(result['root_file_count'], 2)
        self.assertEqual(result['root_date_archives'][0]['date'], '2026-10-03')
        self.assertNotIn('private-note', str(result))
        self.assertEqual(result['report_body_downloads'], 0)

    def test_new_date_folder_is_admitted_at_existing_one_day_lag(self):
        def reader(token, path, recursive=False):
            if not recursive:
                return [{'.tag': 'folder', 'name': '261003'}, {'.tag': 'folder', 'name': '261001'}]
            return []
        result = inspect('token', '/zip_backup', '261004', reader=reader)
        self.assertEqual(result['freshness'], 'passed')
        self.assertEqual(result['selected_date_folder'], '261003')


if __name__ == '__main__':
    unittest.main()
