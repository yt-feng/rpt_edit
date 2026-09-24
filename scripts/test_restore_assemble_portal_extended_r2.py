import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

from portal_extended_locales import ExpansionError
from restore_assemble_portal_extended_r2 import parse_candidate_specs, restore_and_assemble


class RestoreAssemblyTests(unittest.TestCase):
    def test_candidate_map_is_explicit_and_exact(self):
        candidate = 'a' * 64
        locales, mapping = parse_candidate_specs(f'en={candidate}', 'en')
        self.assertEqual(locales, ('en',))
        self.assertEqual(mapping, {'en': candidate})
        for value, approved in [('en=', 'en'), (f'en={candidate},fr={candidate}', 'en'), (f'fr={candidate}', 'en')]:
            with self.subTest(value=value):
                with self.assertRaises(ExpansionError):
                    parse_candidate_specs(value, approved)

    def test_restore_and_assembly_requires_all_r2_receipts(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / 'root'
            root.mkdir()
            evidence = Path(temporary) / 'evidence.json'
            fake = mock.Mock()
            fake.restore_source.side_effect = RuntimeError('R2 permission denied')
            with mock.patch('restore_assemble_portal_extended_r2.R2Store.from_env', return_value=fake):
                with self.assertRaisesRegex(RuntimeError, 'permission'):
                    restore_and_assemble(
                        root=root,
                        prefix='_extended-locales/v1',
                        source_generation='b' * 64,
                        approved_locales='en',
                        candidate_specs='en=' + 'a' * 64,
                        evidence_out=evidence,
                    )
            self.assertFalse(evidence.exists())


if __name__ == '__main__':
    unittest.main(verbosity=2)
