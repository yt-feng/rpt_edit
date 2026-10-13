import json
from pathlib import Path
import unittest
from unittest.mock import Mock
import mineru_figure_sources as figures
from probe_adb_figure_metadata import numbers, structural_failure, probe

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

    def test_nonnumeric_values_never_export(self):
        for value in ['private', ['private'], [float('inf')], [True], list(range(5))]:
            self.assertIsNone(numbers(value))
        try: figures._text('private\x00text')
        except figures.FigureSourceError as error: rows = structural_failure(error)
        self.assertNotIn('private', json.dumps(rows))
        self.assertEqual(rows[0]['value_type'], 'str')

    def test_writing_ledger_rejected_before_any_reads(self):
        ledger = Mock(scope='institution', forbid_new_submissions=False)
        with self.assertRaisesRegex(ValueError, 'read_only_scope'): probe(ledger, Mock(), 'bucket', Path('unused'))
        ledger.store.get.assert_not_called()

    def test_only_fixed_selection_and_readonly_wrappers(self):
        script = Path('scripts/probe_adb_figure_metadata.py').read_text()
        self.assertIn("selection('adb-261013')", script)
        self.assertIn("value['sources'][5]", script)
        for wrapper in ('ReadOnlyR2Client(client)', 'ReadOnlyStore(ledger.store)', 'ReadOnlyProvider(ledger.provider'):
            self.assertIn(wrapper, script)

if __name__ == '__main__': unittest.main()
