import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import audit_portal_locale_javascript_cache as auditor
import build_portal_locales as builder
from test_build_portal_locales import RecordingTranslator


class CachedJavascriptAuditTests(unittest.TestCase):
    def test_cached_audit_never_calls_provider_or_changes_cache(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            assets = root / "assets"
            assets.mkdir()
            source = 'const label = "查看报告";'
            for name in builder.LOCALIZED_JS_ASSETS:
                (assets / name).write_text(source)
            units = {}
            builder.collect_javascript_units(source, "app.js", units)
            cache = builder.empty_cache()
            for locale in builder.LOCALES:
                translated = RecordingTranslator()(locale, list(units.values()))
                for unit in units.values():
                    cache["locales"][locale][unit.key] = builder._translation_cache_row(unit, translated[unit.key])
            path = root / "cache.json.gz"
            builder.write_cache(path, cache)
            before = path.read_bytes()
            with mock.patch.object(builder, "translate_missing_units", side_effect=AssertionError("No paid requests")):
                report = auditor.audit(assets, path, root / "out")
            self.assertEqual(report["status"], "passed")
            self.assertEqual(report["provider_requests"], 0)
            self.assertEqual(len(report["assets"]), 21)
            self.assertEqual(path.read_bytes(), before)
            self.assertTrue((root / "out" / "ko" / "app.js").is_file())
            self.assertEqual(json.loads((root / "out" / "audit.json").read_text())["status"], "passed")

    def test_missing_cache_rows_are_reported_without_provider_repair(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            assets = root / "assets"
            assets.mkdir()
            for name in builder.LOCALIZED_JS_ASSETS:
                (assets / name).write_text('const label = "查看报告";')
            path = root / "cache.json.gz"
            builder.write_cache(path, builder.empty_cache())
            with mock.patch.object(builder, "translate_missing_units", side_effect=AssertionError("No paid requests")):
                report = auditor.audit(assets, path, root / "out")
            self.assertEqual(report["status"], "failed")
            self.assertEqual(report["provider_requests"], 0)
            self.assertEqual(len(report["assets"]), 21)
            self.assertTrue(all(row["status"] == "failed" for row in report["assets"]))


if __name__ == "__main__":
    unittest.main()
