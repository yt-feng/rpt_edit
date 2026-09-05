from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import preflight_deepl_locale_repair as preflight


class DeepLCanaryTests(unittest.TestCase):
    def test_nine_samples_in_three_batches_without_deepseek_or_site_writes(self):
        native = {"ko": "금융 연구", "ja": "金融リサーチ", "ar": "بحث مالي"}
        repair = mock.Mock()
        repair.translate_many.side_effect = lambda locale, sources: [
            native[locale] + (" __KC_PH_000__" if "__KC_PH_000__" in source else "") for source in sources
        ]
        repair.snapshot.return_value = {"provider_requests": 3, "billed_characters": 228, "remaining_character_budget": 499000}
        with tempfile.TemporaryDirectory() as directory:
            report = preflight.run_preflight(Path(directory)/"diag.json", repair=repair)
            self.assertEqual(len(list(Path(directory).iterdir())), 1)
        self.assertEqual(report["status"], "passed")
        self.assertEqual(repair.translate_many.call_count, 3)
        self.assertEqual(len(report["samples"]), 9)
        self.assertTrue(all(call.args[1] == list(preflight.SOURCES) for call in repair.translate_many.call_args_list))
        repair.translate.assert_not_called()
        self.assertEqual(report["max_provider_requests"], 6)

    def test_error_stops_without_echoing_exception_secret(self):
        repair = mock.Mock()
        repair.translate_many.side_effect = RuntimeError("sensitive-provider-content")
        repair.snapshot.return_value = {"provider_requests": 1}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/"diag.json"
            report = preflight.run_preflight(path, repair=repair)
            self.assertNotIn("sensitive-provider-content", path.read_text())
        self.assertEqual(report["status"], "failed")
        repair.translate_many.assert_called_once()


if __name__ == "__main__":
    unittest.main()
