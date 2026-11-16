import hashlib
from io import BytesIO
import json
import unittest
from unittest.mock import patch

import inspect_portal_publication_handoffs as inspection


class HandoffInspectionTests(unittest.TestCase):
    def fixture(self, kind="extended"):
        batch = {"generation": "a" * 64}
        batch.update({"candidates": {"uk": "b" * 64, "my": "c" * 64}} if kind == "extended" else {"candidate_id": "b" * 64})
        raw = json.dumps({"schema_version": 1, "batch": batch, "private_content": "MUST NOT APPEAR"}).encode()
        return raw, hashlib.sha256(raw).hexdigest()

    def test_exact_replay_inputs_and_no_private_fields(self):
        raw, receipt = self.fixture()
        result = inspection.checked_projection(raw, receipt, "extended")
        self.assertEqual(result["inputs"], {"operation": "migrate", "translation_scope": "incremental",
            "extended_locales": "my,uk", "extended_source_generation": "a" * 64,
            "extended_candidate_ids": "my=" + "c" * 64 + ",uk=" + "b" * 64, "extended_handoff": receipt})
        self.assertNotIn("MUST NOT APPEAR", json.dumps(result))
        self.assertNotIn("private_content", json.dumps(result))

    def test_english_requires_only_known_handoff(self):
        raw, receipt = self.fixture("english")
        self.assertEqual(inspection.checked_projection(raw, receipt, "english")["inputs"],
            {"operation": "migrate", "translation_scope": "incremental", "english_handoff": receipt})

    def test_invalid_digest_or_source_or_locale_fails(self):
        raw, receipt = self.fixture()
        with self.assertRaises(ValueError):
            inspection.checked_projection(raw + b" ", receipt, "extended")
        for batch in ({"generation": "https://secret", "candidates": {"uk": "b" * 64}},
                      {"generation": "a" * 64, "candidates": {"https://secret": "b" * 64}},
                      {"generation": "a" * 64, "candidates": {"uk": "https://secret"}}):
            raw = json.dumps({"schema_version": 1, "batch": batch}).encode()
            with self.assertRaises(ValueError):
                inspection.checked_projection(raw, hashlib.sha256(raw).hexdigest(), "extended")

    def test_only_exact_get_and_body_closed(self):
        raw, receipt = self.fixture()
        body = BytesIO(raw)
        calls = []
        class Client:
            def get_object(self, **kwargs):
                calls.append(kwargs)
                return {"Body": body}
        with patch.object(inspection, "KNOWN_RECEIPTS", {receipt: "extended"}):
            result = inspection.inspect(Client(), "fixture", [receipt])
        self.assertTrue(body.closed)
        self.assertTrue(result["read_only"])
        self.assertEqual(calls, [{"Bucket": "fixture", "Key": f"_extended-locales/v1/publication-handoffs/{receipt}/receipt.json"}])

    def test_unknown_or_duplicate_inputs_never_issue_request(self):
        class NoRequests:
            def get_object(self, **kwargs):
                raise AssertionError("Unexpected read")
        known = next(iter(inspection.KNOWN_RECEIPTS))
        for inputs in ([], ["d" * 64], [known, known], ["../../anything"]):
            with self.assertRaises(ValueError):
                inspection.inspect(NoRequests(), "fixture", inputs)


if __name__ == "__main__":
    unittest.main()
