"""Private memo restoration must distinguish cold cache from failed storage access."""
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import private_translation_checkpoint as checkpoint


class StorageError(RuntimeError):
    def __init__(self, code):
        self.response = {"Error": {"Code": code}}


class PrivateTranslationCheckpointTests(unittest.TestCase):
    def test_cache_miss_is_cold_start_but_auth_or_transport_failure_is_not(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary) / "memo"
            with patch.object(checkpoint, "download_directory", side_effect=StorageError("NoSuchKey")):
                self.assertFalse(checkpoint.restore(directory, "test.tar.gz"))
                self.assertTrue(directory.is_dir())
            for failure in (StorageError("AccessDenied"), TimeoutError("timeout")):
                with patch.object(checkpoint, "download_directory", side_effect=failure):
                    with self.assertRaises(type(failure)):
                        checkpoint.restore(directory, "test.tar.gz")

    def test_only_nonempty_completed_json_memo_is_uploaded(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary) / "memo"
            with patch.object(checkpoint, "upload_directory") as upload:
                self.assertFalse(checkpoint.save(directory, "test.tar.gz"))
                directory.mkdir()
                (directory / "incomplete.tmp").write_text("unfinished")
                self.assertFalse(checkpoint.save(directory, "test.tar.gz"))
                (directory / "accepted.json").write_text('{"translation":"done"}')
                self.assertTrue(checkpoint.save(directory, "test.tar.gz"))
                upload.assert_called_once_with(directory, "test.tar.gz")

    def test_keys_have_fixed_private_prefix_and_safe_scope_date(self):
        self.assertEqual(checkpoint.checkpoint_key("institution", "260920"),
                         "_workflow-cache/report-translation/v1/institution/260920.tar.gz")
        self.assertEqual(checkpoint.checkpoint_key("dropbox-p5-n16-i0", "20260920"),
                         "_workflow-cache/report-translation/v1/dropbox-p5-n16-i0/20260920.tar.gz")
        for scope, date in (("../public", "260920"), ("institution", "latest"), ("", "260920")):
            with self.assertRaises(ValueError):
                checkpoint.checkpoint_key(scope, date)


if __name__ == "__main__":
    unittest.main()
