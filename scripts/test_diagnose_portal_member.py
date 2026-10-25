import contextlib
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import types
import unittest
from unittest.mock import patch
from datetime import datetime, timezone

spec = importlib.util.spec_from_file_location("diagnostic", Path(__file__).with_name("diagnose_portal_member.py"))
diagnostic = importlib.util.module_from_spec(spec)
spec.loader.exec_module(diagnostic)


class DiagnosticTest(unittest.TestCase):
    def test_database_selection_is_bounded_and_does_not_require_password_columns(self):
        selected = {"username": "Example", "id": "selected", "email": "private"}
        with patch.object(diagnostic, "database_rows", return_value=[selected, {"username": "other"}]) as request:
            self.assertEqual(diagnostic.selected_database_users(hashlib.sha256(b"example").hexdigest()), [selected])
            self.assertEqual(request.call_args[0][1]["select"], "id,username,email")

    def test_only_selected_outcomes_leave_the_read_only_client(self):
        now = datetime.now(timezone.utc).isoformat()
        day = datetime.now(timezone.utc).date().isoformat()
        rows = {
            "_account/users/username/example": {"id": "private-id", "email": "private@email.invalid", "password_hash": "private-secret"},
            "_account/access/private%40email.invalid": {"status": "active", "access_mode": "all", "admin_email": "private-admin"},
            "_account/entitlements/private%40email.invalid": {},
            "_account/user-state/email/private%40email.invalid": {"disabled": False},
            "_account/user-state/id/private-id": {"disabled": False},
            f"_analytics/events/{day}/{now.replace(':', '-').replace('.', '-')}-a.json": {
                "user": {"id": "private-id"}, "type": "download_error", "status": "503", "error": "private message", "report_id": "a" * 24,
            },
            f"_analytics/events/{day}/{now.replace(':', '-').replace('.', '-')}-b.json": {
                "user": {"id": "someone-else"}, "type": "private-other-user",
            },
        }
        reads = []
        class Client:
            def get_paginator(self, name):
                self.assert_name = name
                return self
            def paginate(self, **kwargs):
                yield {"Contents": [{"Key": key} for key in rows if key.startswith(kwargs["Prefix"])]}
            def get_object(self, **kwargs):
                reads.append(kwargs["Key"])
                return {"Body": io.BytesIO(json.dumps(rows[kwargs["Key"]]).encode())}
        fake = Client()
        modules = {"boto3": types.SimpleNamespace(client=lambda *a, **k: fake),
                   "botocore": types.ModuleType("botocore"), "botocore.config": types.SimpleNamespace(Config=lambda **k: k)}
        environment = {"MEMBER_USERNAME_SHA256": hashlib.sha256(b"example").hexdigest(),
                       "R2_ACCOUNT_ID": "example", "R2_ACCESS_KEY_ID": "private", "R2_SECRET_ACCESS_KEY": "private", "R2_BUCKET": "private"}
        with tempfile.TemporaryDirectory() as directory, patch.dict(sys.modules, modules), patch.dict(os.environ, environment):
            previous = os.getcwd()
            try:
                os.chdir(directory)
                with contextlib.redirect_stdout(io.StringIO()) as stdout:
                    diagnostic.main()
                report = json.loads(Path("member-diagnostic.json").read_text())
                self.assertEqual(report["matched_account_count"], 1)
                self.assertEqual(report["access"], {"status": "active", "access_mode": "all"})
                self.assertNotIn("private", stdout.getvalue())
                self.assertEqual(len(report["observed_events"]), 1)
            finally:
                os.chdir(previous)


if __name__ == "__main__":
    unittest.main()
