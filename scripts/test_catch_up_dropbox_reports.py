import copy
import hashlib
import json
import unittest
from unittest.mock import patch

import catch_up_dropbox_reports as catchup


class GitHub:
    repository = "example/reports"

    def __init__(self, active=False, recent=None):
        self.active, self.recent = active, recent or []

    def api(self, path):
        rows = ([{"head_branch": "main", "status": "in_progress"}]
                if self.active and "status=in_progress" in path
                else [] if "&status=" in path else self.recent)
        return {"total_count": len(rows), "workflow_runs": rows}


class CatchUpTests(unittest.TestCase):
    def setUp(self):
        self.a, self.b = "a" * 24, "b" * 24
        self.catalog = {"items": [{"id": self.a, "date_folder": "261101", "date_folders": ["261101"]}]}
        self.source = {(self.a, "261101"), (self.b, "261102")}
        self.sent = []

    def run_catchup(self, github=None, source=None):
        return catchup.catch_up(github or GitHub(), read_source=lambda: self.source if source is None else source,
                               read_catalog=lambda: copy.deepcopy(self.catalog),
                               dispatch=lambda github, generation: self.sent.append(generation) or True)

    def test_late_yesterday_batch_requests_incremental_without_today_requirement(self):
        self.assertEqual(self.run_catchup(), {"state": "requested", "missing_reports": 1})
        self.assertEqual(self.sent, [catchup.generation_for({(self.b, "261102")})])

    def test_existing_active_release_is_preserved_and_source_not_read(self):
        result = catchup.catch_up(GitHub(active=True), read_source=lambda: self.fail("source read while active"),
                                  read_catalog=lambda: self.fail("catalog read while active"))
        self.assertEqual(result, {"state": "refresh_active"})

    def test_same_folder_append_and_new_date_for_existing_content_are_detected(self):
        for source in ({(self.b, "261101")}, {(self.a, "261102")}):
            with self.subTest(source=source):
                self.assertEqual(self.run_catchup(source=source)["state"], "requested")

    def test_unchanged_and_empty_sources_do_not_dispatch(self):
        self.assertEqual(self.run_catchup(source={(self.a, "261101")})["state"], "up_to_date")
        self.assertEqual(self.run_catchup(source=set())["state"], "source_not_ready")
        self.assertEqual(self.sent, [])

    def test_failed_or_finished_same_generation_is_not_repeated_every_hour(self):
        generation = catchup.generation_for({(self.b, "261102")})
        run = {"head_branch": "main", "display_title": f"Neutral edge Dropbox refresh ({generation})",
               "status": "completed", "conclusion": "failure"}
        self.assertEqual(self.run_catchup(GitHub(recent=[run]))["state"], "already_requested")
        self.assertEqual(self.sent, [])

    def test_race_with_new_refresh_is_checked_before_dispatch(self):
        with patch.object(catchup, "active_refresh", side_effect=[False, True]):
            self.assertEqual(self.run_catchup()["state"], "refresh_active")
        self.assertEqual(self.sent, [])

    def test_pdf_metadata_uses_same_content_identity_as_catalog(self):
        paths = []
        def reader(token, path, recursive=False):
            paths.append((path, recursive))
            if path == "/zip_backup":
                return [{".tag": "folder", "name": "261102", "path_lower": "/zip_backup/261102"},
                        {".tag": "folder", "name": "not-a-date"}]
            return [{".tag": "file", "name": "sample.pdf", "path_lower": path + "/sample.pdf", "content_hash": "ABC"},
                    {".tag": "file", "name": "ignore.txt", "path_lower": path + "/ignore.txt"}]
        expected = hashlib.sha256(b"dropbox-content:abc").hexdigest()[:24]
        self.assertEqual(catchup.source_reports("token", reader=reader), {(expected, "261102")})
        self.assertEqual(paths, [("/zip_backup", False), ("/zip_backup/261102", True)])

    def test_invalid_catalog_or_github_inventory_cannot_dispatch(self):
        self.catalog = {"items": []}
        with self.assertRaises(ValueError):
            self.run_catchup()
        with patch.object(GitHub, "api", return_value={"total_count": 101, "workflow_runs": []}):
            with self.assertRaises(ValueError):
                catchup.active_refresh(GitHub())
        self.assertEqual(self.sent, [])

    def test_dispatch_has_one_attempt_and_no_shell_interpolation(self):
        with patch.object(catchup.subprocess, "run") as run:
            run.return_value.returncode = 1
            self.assertFalse(catchup.dispatch_once(GitHub(), "a" * 64))
            self.assertEqual(run.call_count, 1)
            args, kwargs = run.call_args
            self.assertIsInstance(args[0], list)
            self.assertEqual(json.loads(kwargs["input"])["event_type"], catchup.EVENT)
            self.assertFalse(kwargs.get("shell", False))

    def test_temporary_provider_error_is_deferred_without_details(self):
        with patch.dict(catchup.os.environ, {"GITHUB_REPOSITORY": "example/reports", "GITHUB_STEP_SUMMARY": ""}), \
             patch.object(catchup, "catch_up", side_effect=RuntimeError("private provider body")), \
             patch("builtins.print") as output:
            self.assertEqual(catchup.main(), 0)
            self.assertEqual(json.loads(output.call_args.args[0]), {"state": "deferred"})


if __name__ == "__main__":
    unittest.main()
