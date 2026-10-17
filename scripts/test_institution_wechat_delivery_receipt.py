import json
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import tempfile
import unittest

import institution_wechat_delivery_receipt as receipts


class OperationsAlertSparseCheckoutTests(unittest.TestCase):
    def test_notification_checkout_runs_its_actual_tests_with_only_stdlib(self):
        root = Path(__file__).resolve().parents[1]
        workflow = (root / ".github/workflows/portal-ops-alert.yml").read_text(encoding="utf-8")

        def literal_lines(text, marker):
            lines = text.splitlines()
            index = next(index for index, line in enumerate(lines) if line.strip() == marker)
            indentation = len(lines[index]) - len(lines[index].lstrip())
            block = []
            for line in lines[index + 1:]:
                if not line.strip():
                    break
                if len(line) - len(line.lstrip()) <= indentation:
                    break
                block.append(line.strip())
            return block

        files = literal_lines(workflow, "sparse-checkout: |")
        self.assertEqual(set(files), {
            "scripts/render_private_config.py", "scripts/check_portal_ops_alert_window.py",
            "scripts/send_portal_ops_alert.py", "scripts/test_check_portal_ops_alert_window.py",
            "scripts/test_send_portal_ops_alert.py",
        })
        test_step = workflow.split("- name: Test public operations alert client", 1)[1]
        commands = [shlex.split(line) for line in literal_lines(test_step, "run: |")]
        # This test is deliberately outside the notification checkout. Only its
        # two actual leaf test scripts run there, so this cannot recurse.
        self.assertEqual(commands, [
            ["python", "-B", "scripts/test_check_portal_ops_alert_window.py"],
            ["python", "-B", "scripts/test_send_portal_ops_alert.py"],
        ])
        with tempfile.TemporaryDirectory() as temporary:
            checkout = Path(temporary)
            for name in files:
                destination = checkout / name
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(root / name, destination)
            self.assertEqual(sorted(str(path.relative_to(checkout)) for path in checkout.rglob("*") if path.is_file()),
                             sorted(files))
            for command in commands:
                with self.subTest(script=command[-1]):
                    result = subprocess.run(
                        [sys.executable, "-E", "-s", "-S", *command[1:]],
                        cwd=checkout, text=True, capture_output=True, timeout=30, check=False,
                    )
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


class InstitutionDeliveryReceiptTests(unittest.TestCase):
    def setUp(self):
        from push_portal_translated_to_wechat_drafts import draft_group_key

        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.output = Path(self.temporary.name) / "20261017"
        self.output.mkdir()
        self.payload = {"articles": [{"title": "研究摘要", "author": "研究编辑", "content": "<p>经济增长保持稳定。</p>"}]}
        self.summary = {
            "date_folder": self.output.name, "dry_run": False, "status": "verified",
            "selected_count": 1, "draft_count": 1, "articles": [{"title": "研究摘要"}],
            "drafts": [{
                "media_id": "sample-media-id", "payload": "draft_payload_001.json", "article_count": 1,
                "group_key": draft_group_key(self.payload["articles"]), "status": "verified",
                "draft_get": {"ok": True, "article_count": 1, "expected_article_count": 1,
                              "matches_editorial_contract": True, "matches_expected_article_count": True,
                              "matches_expected_titles": True, "matches_media_contract": True},
            }],
        }
        self.save()

    def save(self):
        (self.output / "wechat_draft_summary.json").write_text(json.dumps(self.summary), encoding="utf-8")
        (self.output / "draft_payload_001.json").write_text(json.dumps(self.payload), encoding="utf-8")

    def assert_unconfirmed(self):
        self.assertEqual(receipts.institution_wechat_delivery_outputs(self.output),
                         {"wechat_verified": "false", "verified_article_count": "0", "verified_draft_count": "0"})

    def test_saved_complete_readback_produces_only_verified_counts(self):
        self.assertEqual(receipts.institution_wechat_delivery_outputs(self.output),
                         {"wechat_verified": "true", "verified_article_count": "1", "verified_draft_count": "1"})

    def test_unfinished_dry_run_and_wrong_date_receipts_are_not_delivery(self):
        for key, value in (("status", "in_progress"), ("dry_run", True), ("date_folder", "20261016"),
                           ("selected_count", 2), ("draft_count", 2)):
            with self.subTest(key=key):
                previous = self.summary[key]
                self.summary[key] = value
                self.save()
                self.assert_unconfirmed()
                self.summary[key] = previous

    def test_incomplete_readback_is_not_delivery(self):
        readback = self.summary["drafts"][0]["draft_get"]
        for key, value in list(readback.items()):
            with self.subTest(key=key):
                readback[key] = False if isinstance(value, bool) else 2
                self.save()
                self.assert_unconfirmed()
                readback[key] = value

    def test_receipt_cannot_be_reused_for_changed_payload(self):
        self.payload["articles"][0]["content"] = "<p>这是另一份报告。</p>"
        self.save()
        self.assert_unconfirmed()

    def test_missing_or_invalid_summary_and_payload_are_unconfirmed(self):
        for name in ("wechat_draft_summary.json", "draft_payload_001.json"):
            with self.subTest(name=name):
                path = self.output / name
                path.unlink()
                self.assert_unconfirmed()
                path.write_text("[]", encoding="utf-8")
                self.assert_unconfirmed()
                self.save()

    def test_duplicate_receipt_does_not_inflate_counts(self):
        self.summary["drafts"] *= 2
        self.summary.update(draft_count=2, selected_count=2, articles=self.summary["articles"] * 2)
        self.save()
        self.assert_unconfirmed()

    def test_payload_path_cannot_escape_receipt_directory(self):
        path = self.output / "draft_payload_001.json"
        outside = self.output.parent / "draft_payload_external.json"
        path.rename(outside)
        path.symlink_to(outside)
        self.assert_unconfirmed()


if __name__ == "__main__":
    unittest.main()
