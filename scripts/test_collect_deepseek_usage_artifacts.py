import io
import json
from pathlib import Path
import tempfile
import unittest
import zipfile
from datetime import date
from zoneinfo import ZoneInfo
from collect_deepseek_usage_artifacts import artifact_overlaps_day, extract_events


class CollectionTests(unittest.TestCase):
    def test_shanghai_boundary_includes_late_upload(self):
        day = date(2026, 9, 20)
        zone = ZoneInfo('Asia/Shanghai')
        self.assertFalse(artifact_overlaps_day({'created_at': '2026-09-19T15:59:59Z'}, day, zone))
        self.assertTrue(artifact_overlaps_day({'created_at': '2026-09-19T16:00:00Z'}, day, zone))
        self.assertTrue(artifact_overlaps_day({'created_at': '2026-09-21T03:00:00Z'}, day, zone))
        self.assertFalse(artifact_overlaps_day({'created_at': '2026-09-21T16:00:00Z'}, day, zone))

    def test_extracts_only_event_objects_without_zip_path_traversal(self):
        payload = io.BytesIO()
        with zipfile.ZipFile(payload, 'w') as z:
            z.writestr('../../outside.json', json.dumps({'event_id': 'abc', 'total_tokens': 10}))
            z.writestr('summary.json', '{}')
            z.writestr('raw.txt', 'ignored')
            z.writestr('broken.json', '{')
            z.writestr('oversized.json', ' ' * 65_000)
        with tempfile.TemporaryDirectory() as directory:
            dest = Path(directory) / 'events'
            dest.mkdir()
            self.assertEqual(extract_events(payload.getvalue(), dest), 1)
            self.assertEqual([p.name for p in dest.iterdir()], ['event-00000000.json'])
            self.assertEqual(len(list(Path(directory).rglob('*.json'))), 1)


if __name__ == '__main__':
    unittest.main()
