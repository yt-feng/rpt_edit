import json
from pathlib import Path
import unittest
from unittest.mock import Mock
import mineru_figure_sources as figures
from probe_adb_figure_metadata import numbers, structural_failure, probe, failed_table_pair
from restore_completed_institution_sources import selection

class MetadataTests(unittest.TestCase):
    def test_failure_has_only_bounded_structural_data(self):
        secret = 'secret-title-and-url'
        try:
            figures._bbox([0, -1, 50, 100], 200, 300)
        except figures.FigureSourceError as error:
            rows = structural_failure(error)
        self.assertEqual(rows[0]['value_coordinates'], [0, -1, 50, 100])
        self.assertEqual(rows[0]['width'], 200)
        self.assertNotIn(secret, json.dumps(rows))
        self.assertEqual(len(rows), 2)

    def test_only_exact_failed_table_pair_can_be_encrypted(self):
        box = [10, 20, 50, 100]
        content = [{'type': 'table', 'page_idx': 0, 'bbox': [100, 100, 500, 500],
                    'img_path': 'images/a.jpg', 'table_body': '<table>private-content</table>'}]
        middle = {'_backend': 'hybrid', '_version_name': '3.4.4', '_ocr_enable': True, '_effort': 'medium',
            'pdf_info': [{'page_idx': 0, 'page_size': [100, 200], 'para_blocks': [
                {'type': 'table', 'bbox': box, 'blocks': [{'type': 'table_body', 'bbox': box,
                    'lines': [{'spans': [{'type': 'table', 'bbox': box, 'image_path': 'a.jpg',
                        'html': '<table>private-middle</table>'}]}]}]}]}]}
        try: figures._normalise(content, middle)
        except figures.FigureSourceError as error:
            pair = failed_table_pair(error); public = structural_failure(error)
        self.assertEqual(pair['content_html'], content[0]['table_body'])
        self.assertEqual(pair['middle_html'], '<table>private-middle</table>')
        self.assertEqual(pair['page_idx'], 0)
        self.assertNotIn('private', json.dumps(public))
        try: figures._bbox([0, -1, 1, 1], 2, 2)
        except figures.FigureSourceError as error: self.assertIsNone(failed_table_pair(error))

    def test_nonnumeric_values_never_export(self):
        for value in ['private', ['private'], [float('inf')], [True], list(range(5))]:
            self.assertIsNone(numbers(value))
        try: figures._text('private\x00text')
        except figures.FigureSourceError as error: rows = structural_failure(error)
        self.assertNotIn('private', json.dumps(rows))
        self.assertEqual(rows[0]['value_type'], 'str')

    def test_visual_coverage_failure_discloses_counts_without_source_text(self):
        box = [10, 20, 50, 100]
        middle = {'_backend': 'hybrid', '_version_name': '3.4.4', '_ocr_enable': True, '_effort': 'medium',
            'pdf_info': [{'page_idx': 0, 'page_size': [100, 200], 'para_blocks': [
                {'type': 'table', 'bbox': box, 'blocks': [{'type': 'table_body', 'bbox': box,
                    'lines': [{'spans': [{'type': 'table', 'bbox': box, 'image_path': 'private.jpg',
                        'html': '<table>private-content</table>'}]}]}]}]}]}
        try:
            figures._normalise([], middle)
        except figures.FigureSourceError as error:
            rows = structural_failure(error)
        self.assertEqual(rows[0]['records_count'], 0)
        self.assertEqual(rows[0]['parents_count'], 1)
        self.assertEqual(rows[0]['used_count'], 0)
        self.assertNotIn('private', json.dumps(rows))

    def test_writing_ledger_rejected_before_any_reads(self):
        ledger = Mock(scope='institution', forbid_new_submissions=False)
        with self.assertRaisesRegex(ValueError, 'read_only_scope'): probe(ledger, Mock(), 'bucket', Path('unused'))
        ledger.store.get.assert_not_called()

    def test_original_manifest_order_is_not_the_production_batch_order(self):
        value, _ = selection('adb-261013')
        selected = sorted(value['sources'], key=lambda row: row['local_filename'])[5]
        self.assertEqual(selected['local_filename'], 'ADB_Understanding-Emission-Trends-in-Mongolia-Insights-from-Envi_368670f7.pdf')
        self.assertNotEqual(selected, value['sources'][5])

    def test_only_fixed_selection_and_readonly_wrappers(self):
        script = Path('scripts/probe_adb_figure_metadata.py').read_text()
        self.assertIn("selection('adb-261013')", script)
        self.assertIn("sorted(value['sources'], key=lambda source: source['local_filename'])[5]", script)
        for wrapper in ('ReadOnlyR2Client(client)', 'ReadOnlyStore(ledger.store)', 'ReadOnlyProvider(ledger.provider'):
            self.assertIn(wrapper, script)

if __name__ == '__main__': unittest.main()
