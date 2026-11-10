"""Check exact private-source binding before any public archive is materialized."""
import hashlib
from io import BytesIO
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

import restore_public_market_view_archive as recovery


class ArchiveTests(unittest.TestCase):
    def setUp(self):
        self.raw = b'%PDF-bound-private-source\n' + b'x' * 1500
        self.sha = hashlib.sha256(self.raw).hexdigest()
        self.item = {'sha256': self.sha, 'size_bytes': len(self.raw)}
        self.client = Mock()
        self.client.get_object.return_value = {'Body': BytesIO(self.raw)}

    def test_only_verified_source_reaches_existing_public_sanitizer(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / 'public.pdf'
            def sanitize(source, target):
                self.assertEqual(Path(source).read_bytes(), self.raw)
                Path(target).write_bytes(b'PUBLIC_SAFE_COPY')
                return {'page_count': 38, 'size_bytes': 16}
            with patch.object(recovery, 'validate_existing_private_pair', return_value=self.item), \
                    patch.object(recovery, 'prepare_public_copy', side_effect=sanitize):
                result = recovery.restore(self.client, 'bucket', '261109', self.sha, output)
            self.assertEqual(output.read_bytes(), b'PUBLIC_SAFE_COPY')
        self.assertEqual(result['private_pdf_sha256'], self.sha)
        self.assertEqual(result['model_calls'], 0)
        self.client.put_object.assert_not_called()
        self.client.delete_object.assert_not_called()

    def test_wrong_hash_changed_or_truncated_bytes_never_write_public_copy(self):
        cases = [('a' * 64, self.raw), (self.sha, self.raw[:-1]), (self.sha, b'y' * len(self.raw))]
        for expected, data in cases:
            with self.subTest(expected=expected), tempfile.TemporaryDirectory() as directory:
                output = Path(directory) / 'public.pdf'
                output.write_bytes(b'EXISTING_PUBLIC_COPY')
                self.client.get_object.return_value = {'Body': BytesIO(data)}
                with patch.object(recovery, 'validate_existing_private_pair', return_value=self.item), \
                        patch.object(recovery, 'prepare_public_copy') as sanitize, self.assertRaises(ValueError):
                    recovery.restore(self.client, 'bucket', '261109', expected, output)
                self.assertEqual(output.read_bytes(), b'EXISTING_PUBLIC_COPY')
                sanitize.assert_not_called()

    def test_invalid_request_and_unverified_pair_stop_before_source_materialization(self):
        for day, sha in [('20261109', self.sha), ('261109', 'invalid')]:
            with self.assertRaises(ValueError):
                recovery.restore(self.client, 'bucket', day, sha, Path('unused.pdf'))
        self.client.head_object.assert_not_called()
        with patch.object(recovery, 'validate_existing_private_pair', side_effect=RuntimeError('unavailable')), \
                self.assertRaises(RuntimeError):
            recovery.restore(self.client, 'bucket', '261109', self.sha, Path('unused.pdf'))
        self.client.get_object.assert_not_called()


if __name__ == '__main__':
    unittest.main()
