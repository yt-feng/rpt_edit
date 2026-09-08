#!/usr/bin/env python3
import io
import json
from pathlib import Path
import tempfile
import unittest
from download_report_research_inputs import clean_origin, download_inputs


class InputDownloadTests(unittest.TestCase):
    def test_only_clean_https_origins(self):
        self.assertEqual(clean_origin("https://example.invalid/"), "https://example.invalid")
        for value in ("http://example.invalid", "https://a:b@example.invalid", "https://example.invalid:443", "https://example.invalid/path", "https://example.invalid?q=secret", ""):
            with self.subTest(value=value), self.assertRaises(ValueError):
                clean_origin(value)

    def test_both_inputs_are_validated_before_writing(self):
        class Opener:
            def __init__(self, valid):
                self.valid = valid
                self.paths = []
            def open(self, request, timeout):
                self.paths.append(request.full_url)
                return io.BytesIO(json.dumps({"items": [{"id": "a" * 24}]} if self.valid or len(self.paths) == 1 else {"error": "missing"}).encode())
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "input"
            with self.assertRaises(ValueError):
                download_inputs("https://example.invalid", path, opener=Opener(False))
            self.assertFalse(path.exists())
            opener = Opener(True)
            self.assertEqual(download_inputs("https://example.invalid", path, opener=opener), {"catalog.json": 1, "search_index.json": 1})
            self.assertEqual(opener.paths, ["https://example.invalid/data/catalog.json", "https://example.invalid/data/search_index.json"])
            self.assertEqual((path / "catalog.json").stat().st_mode & 0o777, 0o600)


if __name__ == "__main__":
    unittest.main()
