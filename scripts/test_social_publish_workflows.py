#!/usr/bin/env python3

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"


def read(name: str) -> str:
    return (WORKFLOWS / name).read_text(encoding="utf-8")


class HostedRunnerContractTests(unittest.TestCase):
    def test_all_social_jobs_are_github_hosted_and_browser_free(self):
        for name in (
            "social-publish-control.yml",
            "social-credential-monitor.yml",
            "social-reach-monitor.yml",
        ):
            text = read(name)
            self.assertIn("runs-on: ubuntu-latest", text, name)
            self.assertNotIn("self-hosted", text.casefold(), name)
            self.assertNotRegex(text.casefold(), r"\b(playwright|selenium|puppeteer|chromium)\b")
            self.assertNotIn("continue-on-error", text)

    def test_publish_and_reach_share_one_repository_wide_lock(self):
        for name in ("social-publish-control.yml", "social-reach-monitor.yml"):
            text = read(name)
            self.assertIn("group: social-publishing-control-plane", text)
            self.assertIn("cancel-in-progress: false", text)
        publish = read("social-publish-control.yml")
        self.assertNotIn("group: social-publish-${{", publish)


class PublishWorkflowContractTests(unittest.TestCase):
    def setUp(self):
        self.text = read("social-publish-control.yml")

    def test_prepare_is_secret_free_and_defaults_to_validation(self):
        prepare = self.text.split("  prepare:", 1)[1].split("\n  publish:", 1)[0]
        self.assertNotIn("secrets.", prepare)
        self.assertIn("default: validate", self.text)
        self.assertIn("vars.SOCIAL_AUTO_PUBLISH_ENABLED == 'true'", prepare)

    def test_production_publish_is_fail_closed(self):
        required = (
            "environment: social-production",
            "github.run_attempt != 1",
            "refs/heads/main",
            "confirm_content_id",
            "EXPECTED_MANIFEST_SHA256",
            "Load latest ledger without changing approved code",
            "git restore --source=FETCH_HEAD --staged --worktree -- social_publish/receipts",
            "Reserve content ID before any provider write",
            "Commit reservation to the durable ledger",
            "Publish once through official APIs",
            "SOCIAL_PUBLISH_ENABLED == 'true'",
            "persist-credentials: false",
            "commit_social_receipt.sh reserve",
            "commit_social_receipt.sh finalize",
        )
        for marker in required:
            self.assertIn(marker, self.text)
        self.assertLess(
            self.text.index("Commit reservation to the durable ledger"),
            self.text.index("Publish once through official APIs"),
        )

    def test_private_locators_must_be_encrypted_before_final_commit(self):
        self.assertIn("--private-receipt-output", self.text)
        self.assertIn("social_receipt_crypto.mjs check-key", self.text)
        self.assertIn("social_receipt_crypto.mjs seal", self.text)
        self.assertIn("steps.seal_receipt.outcome == 'success'", self.text)
        upload = self.text.split("- name: Upload sanitized publish receipt", 1)[1].split(
            "- name: Materialize private email runtime values", 1
        )[0]
        self.assertNotIn("social-private-receipt", upload)
        self.assertIn(".json.enc", upload)
        self.assertNotIn("runner.temp }}/social-private", upload)

    def test_no_automatic_post_retry_or_engagement_path(self):
        lowered = self.text.casefold()
        self.assertNotRegex(lowered, r"\b(auto[_-]?(like|reply|follow|repost)|reply_to)\b")
        self.assertIn("没有执行自动补发", self.text)

    def test_enabled_platforms_get_separate_identity_preflights(self):
        for platform, expected_identity in (
            ("youtube", "YOUTUBE_CHANNEL_ID"),
            ("linkedin", "LINKEDIN_AUTHOR_URN"),
            ("x", "X_USER_ID"),
        ):
            self.assertIn(f"--platform {platform}", self.text)
            self.assertIn(expected_identity, self.text)
        provider_block = self.text.split("- name: Publish once through official APIs", 1)[1].split(
            "- name: Encrypt private provider locators", 1
        )[0]
        self.assertNotIn("secrets.", provider_block)

    def test_final_commit_stages_only_the_public_and_encrypted_companion(self):
        final_block = self.text.split("- name: Commit final or partial receipt", 1)[1].split(
            "- name: Upload sanitized publish receipt", 1
        )[0]
        self.assertIn("commit_social_receipt.sh finalize", final_block)
        self.assertIn('"$PUBLIC_RECEIPT"', final_block)
        self.assertIn('"$PUBLIC_RECEIPT.enc"', final_block)
        self.assertNotIn("commit_output_dir.sh", final_block)


class MonitorWorkflowContractTests(unittest.TestCase):
    def test_credential_monitor_uses_read_only_probe_then_direct_email(self):
        text = read("social-credential-monitor.yml")
        test_block = text.split("- name: Test monitor without provider credentials", 1)[1].split(
            "- name: Run read-only credential", 1
        )[0]
        self.assertNotIn("secrets.", test_block)
        self.assertIn("vars.SOCIAL_CREDENTIAL_MONITOR_ENABLED == 'true'", text)
        self.assertIn("github.ref == 'refs/heads/main'", text)
        self.assertIn("environment: social-monitor", text)
        self.assertIn("ref: main", text)
        self.assertIn("persist-credentials: false", text)
        self.assertIn("scripts/check_social_credentials.py", text)
        self.assertIn("scripts/send_portal_ops_alert.py", text)
        self.assertNotIn("portal-ops-alert.yml", text)
        self.assertIn("--dedupe-hours \"$DEDUPE_HOURS\"", text)

    def test_reach_monitor_never_uploads_decrypted_locator(self):
        text = read("social-reach-monitor.yml")
        self.assertIn("vars.SOCIAL_REACH_MONITOR_ENABLED == 'true'", text)
        self.assertIn("github.ref == 'refs/heads/main'", text)
        self.assertIn("environment: social-monitor", text)
        self.assertIn("ref: main", text)
        self.assertIn("social_receipt_crypto.mjs open", text)
        self.assertIn("--receipts-dir \"$RUNNER_TEMP/social-private-receipts\"", text)
        upload = text.split("- name: Upload sanitized reach report", 1)[1].split(
            "- name: Write durable automatic-publishing pause", 1
        )[0]
        self.assertNotIn("social-private-receipts", upload)
        self.assertNotIn(".json.enc", upload)
        self.assertIn("social_publish/PAUSED.json", text)
        self.assertIn("steps.reach.outputs.should_alert == 'true'", text)

    def test_only_normalized_outputs_enter_summaries_and_emails(self):
        for name in ("social-credential-monitor.yml", "social-reach-monitor.yml"):
            text = read(name)
            self.assertNotRegex(text, re.compile(r"echo .*\$\{\{ secrets\.", re.IGNORECASE))
            self.assertIn("send_portal_ops_alert.py", text)


if __name__ == "__main__":
    unittest.main()
