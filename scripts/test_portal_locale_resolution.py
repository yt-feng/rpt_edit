#!/usr/bin/env python3
"""Coverage checks must retain exact semantics and linear inventory work."""

import os
import unittest

import build_portal_locales as builder


class CountedSet(set):
    def __init__(self, values, operations):
        super().__init__(values)
        self.operations = operations

    def __or__(self, other):
        self.operations["unions"] += 1
        return CountedSet(super().__or__(other), self.operations)

    def __contains__(self, key):
        self.operations["lookups"] += 1
        return super().__contains__(key)


class SourceResolutionTests(unittest.TestCase):
    def units(self, keys):
        return [builder.TranslationUnit(key, "html:text:p", key) for key in keys]

    def assert_linear_inventory_work(self, size):
        keys = [str(index) for index in range(size)]
        operations = {"unions": 0, "lookups": 0}
        translated = CountedSet(keys[::2], operations)
        retained = set(keys[1::2])
        count = builder._checked_resolved_source_count(
            self.units(keys), translated, retained, "ko")
        self.assertEqual(count, size)
        self.assertEqual(operations, {"unions": 1, "lookups": size})
        self.assertEqual(translated, set(keys[::2]))
        self.assertEqual(retained, set(keys[1::2]))

    def test_coverage_scan_does_one_union_and_one_lookup_per_source(self):
        for size in (256, 1024):
            with self.subTest(size=size):
                self.assert_linear_inventory_work(size)

    def test_overlapping_resolution_sets_count_each_identity_once(self):
        count = builder._checked_resolved_source_count(
            self.units(["translated", "retained", "both"]),
            {"translated", "both"}, {"retained", "both"}, "ja")
        self.assertEqual(count, 3)

    def test_missing_sources_preserve_locale_and_exact_failure_count(self):
        with self.assertRaisesRegex(
                builder.TranslationError, "^ar translation coverage is incomplete: 2 units$"):
            builder._checked_resolved_source_count(
                self.units(["translated", "retained", "missing-a", "missing-b"]),
                {"translated"}, {"retained"}, "ar")

    def test_empty_inventory_is_fully_accounted(self):
        self.assertEqual(builder._checked_resolved_source_count([], set(), set(), "ko"), 0)

    @unittest.skipUnless(os.environ.get("LOCALE_RESOLUTION_SCALE"), "Cloud inventory-scale regression")
    def test_current_production_inventory_scale(self):
        size = int(os.environ["LOCALE_RESOLUTION_SCALE"])
        self.assertGreater(size, 0)
        self.assertLessEqual(size, 300_000)
        self.assert_linear_inventory_work(size)
        print(f"locale_resolution_scale={size} union_operations=1 membership_checks={size}")


if __name__ == "__main__":
    unittest.main()
