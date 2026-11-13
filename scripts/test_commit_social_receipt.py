#!/usr/bin/env python3

import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


SCRIPT = Path(__file__).with_name("commit_social_receipt.sh")


def git(cwd: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=cwd,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def receipt(content_id: str, state: str) -> dict:
    payload = {
        "schema_version": 1,
        "content_id": content_id,
        "manifest_sha256": "a" * 64,
        "state": state,
        "run_id": "9001",
        "code_sha": "b" * 40,
        "results": {},
    }
    if state != "reserved":
        payload["completed_at"] = "2026-09-01T00:00:00Z"
    return payload


class ExactReceiptCommitTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.remote = self.root / "remote.git"
        self.seed = self.root / "seed"
        git(self.root, "init", "--bare", "--initial-branch=main", str(self.remote))
        git(self.root, "clone", str(self.remote), str(self.seed))
        git(self.seed, "config", "user.name", "test")
        git(self.seed, "config", "user.email", "test@example.invalid")
        (self.seed / "social_publish" / "receipts").mkdir(parents=True)
        (self.seed / "social_publish" / "receipts" / ".gitkeep").write_text("\n")
        git(self.seed, "add", ".")
        git(self.seed, "commit", "-m", "seed")
        git(self.seed, "push", "origin", "main")
        self.env = {
            **os.environ,
            "SOCIAL_GIT_TOKEN": "test-token-not-used-by-file-remote",
            "RUNNER_TEMP": str(self.root),
        }

    def tearDown(self):
        self.temporary.cleanup()

    def run_helper(self, cwd: Path, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["bash", str(SCRIPT), *args],
            cwd=cwd,
            env=self.env,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

    def test_reserve_then_finalize_keeps_concurrent_unrelated_receipt(self):
        content_id = "2026-09-01-exact-receipt"
        public = self.seed / "social_publish" / "receipts" / f"{content_id}.json"
        encrypted = Path(f"{public}.enc")
        public.write_text(json.dumps(receipt(content_id, "reserved")) + "\n")
        reserved = self.run_helper(
            self.seed,
            "reserve",
            public.relative_to(self.seed).as_posix(),
            "",
            "reserve",
            "2",
        )
        self.assertEqual(reserved.returncode, 0, reserved.stderr)

        other = self.root / "other"
        git(self.root, "clone", str(self.remote), str(other))
        git(other, "config", "user.name", "other")
        git(other, "config", "user.email", "other@example.invalid")
        unrelated = other / "social_publish" / "receipts" / "2026-09-01-unrelated.json"
        unrelated.write_text(json.dumps(receipt("2026-09-01-unrelated", "published")) + "\n")
        git(other, "add", unrelated.relative_to(other).as_posix())
        git(other, "commit", "-m", "unrelated receipt")
        git(other, "push", "origin", "main")

        public.write_text(json.dumps(receipt(content_id, "published")) + "\n")
        encrypted.write_text('{"format":"opaque-test-envelope"}\n')
        finalized = self.run_helper(
            self.seed,
            "finalize",
            public.relative_to(self.seed).as_posix(),
            encrypted.relative_to(self.seed).as_posix(),
            "finalize",
            "2",
        )
        self.assertEqual(finalized.returncode, 0, finalized.stderr)

        audit = self.root / "audit"
        git(self.root, "clone", str(self.remote), str(audit))
        self.assertTrue((audit / unrelated.relative_to(other)).is_file())
        self.assertEqual(
            json.loads((audit / public.relative_to(self.seed)).read_text())["state"],
            "published",
        )
        self.assertTrue((audit / encrypted.relative_to(self.seed)).is_file())

    def test_reserve_refuses_different_existing_content_id_receipt(self):
        content_id = "2026-09-01-conflict-receipt"
        public = self.seed / "social_publish" / "receipts" / f"{content_id}.json"
        public.write_text(json.dumps(receipt(content_id, "reserved")) + "\n")
        git(self.seed, "add", public.relative_to(self.seed).as_posix())
        git(self.seed, "commit", "-m", "existing")
        git(self.seed, "push", "origin", "main")
        payload = receipt(content_id, "reserved")
        payload["run_id"] = "9002"
        public.write_text(json.dumps(payload) + "\n")
        rejected = self.run_helper(
            self.seed,
            "reserve",
            public.relative_to(self.seed).as_posix(),
            "",
            "reserve",
            "1",
        )
        self.assertEqual(rejected.returncode, 4)
        self.assertIn("different receipt", rejected.stderr)


if __name__ == "__main__":
    unittest.main()
