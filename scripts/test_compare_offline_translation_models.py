"""Comparison coverage, immutability and inference boundary without loading models."""
import os
import re
import unittest
from unittest.mock import patch
import compare_offline_translation_models as comparison


class ComparisonTests(unittest.TestCase):
    def test_models_use_immutable_revisions_and_individual_licenses(self):
        for model in comparison.MANIFEST.values():
            self.assertRegex(model["revision"], r"^[a-f0-9]{40}$")
        self.assertEqual(comparison.MANIFEST["opus-en-zh"]["license"], "apache-2.0")
        self.assertEqual(comparison.MANIFEST["opus-zh-en"]["license"], "cc-by-4.0")
        self.assertEqual(comparison.MANIFEST["opus-en-zh"]["source_prefix"], ">>cmn_Hans<< ")

    def test_every_bilingual_model_gets_all_three_regressions_and_paragraph(self):
        for name in ("opus-en-zh", "opus-zh-en"):
            samples = comparison.selected_samples(comparison.MANIFEST[name])
            self.assertEqual(len(samples), 5)
            self.assertTrue(any(row["id"].endswith("paragraph") for row in samples))
            self.assertTrue(all(row.get("review_notes") for row in samples))
        self.assertEqual(len(comparison.selected_samples(comparison.MANIFEST["m2m100-418m"])), 16)

    def test_clause_split_preserves_every_source_character(self):
        text = "收入增长12.5%，营业利润率为8%。"
        self.assertEqual("".join(comparison.split_clauses(text, "zh")), text)
        english = "Cash reserves were USD 120 million on September 15, 2026."
        self.assertEqual(comparison.split_clauses(english, "en"), [english])

    def test_real_models_are_actions_only(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(RuntimeError, "GitHub Actions"):
                comparison.require_actions()


if __name__ == "__main__":
    unittest.main()
