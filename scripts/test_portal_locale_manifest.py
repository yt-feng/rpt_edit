"""No-network tests for source-preserving locale release accounting."""

from __future__ import annotations

import copy
import hashlib
import unittest

from portal_locale_manifest import LocaleManifestError, validate_translation_resolution


LOCALES = ("ko", "ja", "ar")


def with_source_fallback(manifest: dict) -> dict:
    # Real selected source from the failed 35574073283 preflight diagnostics.
    # Its protected data must remain exact when a translation cannot be accepted.
    source = "BofA-Global Emerging Markets Weekly:Don’t hyperventilate about hyperscalers-__KC_PH_000__"
    prompt_version = "portal-public-locales-v4"
    key = hashlib.sha256(f"{prompt_version}\0copy\0{source}".encode()).hexdigest()
    manifest.update({
        "prompt_version": prompt_version,
        "source_unit_count": 10,
        "translation_entry_count": {"ko": 9, "ja": 10, "ar": 10},
        "coverage": {"ko": 0.9, "ja": 1.0, "ar": 1.0},
        "resolved_entry_count": {locale: 10 for locale in LOCALES},
        "resolved_coverage": {locale: 1.0 for locale in LOCALES},
        "source_fallbacks": {
            "schema_version": 1,
            "counts": {"ko": 1, "ja": 0, "ar": 0},
            "units": {
                "ko": {key: {
                    "source": source,
                    "source_sha256": hashlib.sha256(source.encode()).hexdigest(),
                    "context": "html:meta:keyword",
                    "translation_class": "copy",
                    "reason": "financial_quantity_changed_missing_or_added",
                }},
                "ja": {}, "ar": {},
            },
        },
    })
    return manifest


class LocaleManifestTests(unittest.TestCase):
    def test_accepts_strict_legacy_and_explicit_source_resolution(self):
        validate_translation_resolution({"coverage": dict.fromkeys(LOCALES, 1.0)}, LOCALES)
        manifest = with_source_fallback({})
        validate_translation_resolution(manifest, LOCALES)
        row = next(iter(manifest["source_fallbacks"]["units"]["ko"].values()))
        row["reason"] = "translation_time_budget"
        validate_translation_resolution(manifest, LOCALES)

    def test_cannot_claim_partial_translation_is_full_without_provenance(self):
        for coverage in (0.9, True, float("nan")):
            with self.subTest(coverage=coverage), self.assertRaises(LocaleManifestError):
                validate_translation_resolution({"coverage": {"ko": coverage, "ja": 1, "ar": 1}}, LOCALES)

    def test_rejects_changed_source_hash_key_and_missing_provenance(self):
        fixture = with_source_fallback({})
        key = next(iter(fixture["source_fallbacks"]["units"]["ko"]))
        for field, value in (("source", "altered 45%"), ("source_sha256", "0" * 64),
                             ("context", ""), ("reason", ""), ("translation_class", "unknown")):
            manifest = copy.deepcopy(fixture)
            manifest["source_fallbacks"]["units"]["ko"][key][field] = value
            with self.subTest(field=field), self.assertRaises(LocaleManifestError):
                validate_translation_resolution(manifest, LOCALES)
        manifest = copy.deepcopy(fixture)
        rows = manifest["source_fallbacks"]["units"]["ko"]
        rows["0" * 64] = rows.pop(key)
        with self.assertRaisesRegex(LocaleManifestError, "identity differs"):
            validate_translation_resolution(manifest, LOCALES)

    def test_rejects_false_counts_coverage_and_unaccounted_units(self):
        mutations = (
            lambda m: m["source_fallbacks"]["counts"].update(ko=2),
            lambda m: m["source_fallbacks"]["counts"].update(ko=True),
            lambda m: m["translation_entry_count"].update(ko=10),
            lambda m: m["resolved_entry_count"].update(ko=9),
            lambda m: m["coverage"].update(ko=1.0),
            lambda m: m["resolved_coverage"].update(ko=0.9),
            lambda m: m["source_fallbacks"]["units"].pop("ar"),
            lambda m: m.update(source_unit_count=11),
        )
        for index, mutate in enumerate(mutations):
            manifest = with_source_fallback({})
            mutate(manifest)
            with self.subTest(case=index), self.assertRaises(LocaleManifestError):
                validate_translation_resolution(manifest, LOCALES)


if __name__ == "__main__":
    unittest.main()
