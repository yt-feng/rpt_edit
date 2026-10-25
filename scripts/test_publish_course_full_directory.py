import copy
import io
import json
import unittest

from publish_course_full_directory import KEY, publish, validate


def payload():
    return {"schema_version": 1, "variant": "original_names", "complete": True, "item_count": 1,
            "generated_at": "2026-10-25T00:00:00Z", "items": [{"id": "original_12345678", "name": "Example original name.pdf",
            "folders": ["Example course"], "extension": "pdf", "size_label": "2.3 MB", "date": "2026-10-24"}]}


class Tests(unittest.TestCase):
    def test_original_names_are_preserved_without_storage_locators(self):
        p = payload()
        self.assertEqual(json.loads(validate(p)), p)
        for key in ["path", "fsid", "download_url", "root"]:
            p = payload(); p["items"][0][key] = "private"
            with self.assertRaises(ValueError): validate(p)
        p = payload(); p["root"] = "private"
        with self.assertRaises(ValueError): validate(p)

    def test_partial_or_mismatched_inventory_cannot_publish(self):
        for change in [{"complete": False}, {"item_count": 2}, {"items": []}, {"variant": "sanitized"}, {"item_count": True}, {"schema_version": True}]:
            with self.subTest(change=change), self.assertRaises(ValueError): validate({**payload(), **change})
        p = payload(); p["items"] *= 2; p["item_count"] = 2
        with self.assertRaises(ValueError): validate(p)

    def test_bounds_and_plain_field_contract(self):
        for change in [{"name": "../../private"}, {"name": "text\nheader"}, {"folders": ["course"] * 33}, {"extension": "pdf?token"},
                       {"id": 12345678}, {"extension": 0}, {"size_label": None}, {"date": 0}, {"size_label": "٣ MB"}, {"date": "٢٠٢٦-١٠-٢٥"}]:
            p = payload(); p["items"][0].update(change)
            with self.subTest(change=change), self.assertRaises(ValueError): validate(p)

    def test_stable_pointer_is_conditional_and_every_write_is_read_back(self):
        class Client:
            def __init__(self): self.objects = {}; self.calls = []
            def head_object(self, **_): return {"ETag": "previous"}
            def put_object(self, **kwargs):
                self.calls.append(kwargs); self.objects[kwargs["Key"]] = kwargs["Body"]
            def get_object(self, **kwargs): return {"Body": io.BytesIO(self.objects[kwargs["Key"]])}
        client = Client(); result = publish(client, "fixture", validate(payload()))
        self.assertTrue(result["ok"])
        self.assertEqual(client.calls[-1]["Key"], KEY)
        self.assertEqual(client.calls[-1]["IfMatch"], "previous")
        self.assertTrue(all(row["CacheControl"] == "private, no-store" for row in client.calls))

    def test_failed_revision_verification_never_replaces_stable_pointer(self):
        class Client:
            calls = []
            def head_object(self, **_): return {"ETag": "previous"}
            def put_object(self, **kwargs): self.calls.append(kwargs["Key"])
            def get_object(self, **_): return {"Body": io.BytesIO(b"wrong")}
        client = Client()
        with self.assertRaises(ValueError): publish(client, "fixture", validate(payload()))
        self.assertNotIn(KEY, client.calls)


if __name__ == "__main__": unittest.main()
