#!/usr/bin/env python3
"""Execute the real post-archive dispatch scripts against a local GitHub API mock."""
import json
from pathlib import Path
import re
import subprocess
import textwrap
import unittest


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml"
JOBS = {"push-xhs-notes-wechat-drafts": "upload_xhs_wechat", "push-portal-translated-wechat-drafts": "upload_portal_wechat"}
NODE_RUNNER = """
const input = JSON.parse(require('fs').readFileSync(0, 'utf8'));
const calls = [];
const github = {rest: {actions: {createWorkflowDispatch: async payload => {
  if (input.fail) throw new Error('dispatch unavailable');
  calls.push(payload);
}}}};
const AsyncFunction = Object.getPrototypeOf(async function(){}).constructor;
new AsyncFunction('github', 'context', 'core', 'process', input.script)(
  github, {repo: {owner: 'example', repo: 'repo'}}, {info: () => {}}, {env: input.env}
).then(() => process.stdout.write(JSON.stringify(calls))).catch(error => {
  process.stderr.write(error.message); process.exitCode = 1;
});
"""


def job_body(name):
    return re.search(rf"(?ms)^  {re.escape(name)}:\n(.*?)(?=^  [\w-]+:\n|\Z)", WORKFLOW.read_text()).group(1)


def dispatch_step(name):
    return job_body(name).split("      - name: Refresh public site after accepted Blog archive\n", 1)[1].split("      - name: ", 1)[0]


def execute_step(name, env, fail=False):
    script = textwrap.dedent(dispatch_step(name).split("script: |\n", 1)[1])
    return subprocess.run(["node", "-e", NODE_RUNNER], input=json.dumps({"script": script, "env": env, "fail": fail}),
                          text=True, capture_output=True, check=False)


class PostBlogRefreshTests(unittest.TestCase):
    def test_actual_scripts_dispatch_only_under_existing_auto_release_settings(self):
        cases = [
            ({}, False),
            ({"NEUTRAL_SCHEDULE_ENABLED": "false"}, False),
            ({"NEUTRAL_SCHEDULE_ENABLED": "true", "PORTAL_MULTILINGUAL_ENABLED": "false"}, True),
            ({"NEUTRAL_SCHEDULE_ENABLED": "true", "PORTAL_MULTILINGUAL_ENABLED": "true", "PORTAL_MULTILINGUAL_LIVE": "false"}, False),
            ({"NEUTRAL_SCHEDULE_ENABLED": "true", "PORTAL_MULTILINGUAL_ENABLED": "true", "PORTAL_MULTILINGUAL_LIVE": "true"}, True),
        ]
        expected = {"owner": "example", "repo": "repo", "workflow_id": "neutral-edge-cutover.yml", "ref": "main",
                    "inputs": {"operation": "migrate", "translation_scope": "incremental"}}
        for name in JOBS:
            for env, enabled in cases:
                with self.subTest(job=name, env=env):
                    result = execute_step(name, env)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertEqual(json.loads(result.stdout), [expected] if enabled else [])

    def test_dispatch_failure_is_visible_and_no_new_diff_is_not_required(self):
        for name in JOBS:
            with self.subTest(job=name):
                result = execute_step(name, {"NEUTRAL_SCHEDULE_ENABLED": "true"}, fail=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("dispatch unavailable", result.stderr)
                self.assertNotIn("continue-on-error", dispatch_step(name))
                self.assertNotIn("changed", dispatch_step(name))

    def test_dispatch_occurs_after_verified_upload_and_committed_archive_in_same_job(self):
        for name, upload_id in JOBS.items():
            with self.subTest(job=name):
                body = job_body(name)
                step = dispatch_step(name)
                self.assertIn(f"steps.{upload_id}.outcome == 'success'", step)
                self.assertIn("steps.commit_blog_archive.outcome == 'success'", step)
                self.assertLess(body.index(f"id: {upload_id}"), body.index("id: commit_blog_archive"))
                self.assertLess(body.index("bash scripts/push_main_with_rebase_retry.sh 5"), body.index("Refresh public site after accepted Blog archive"))
                self.assertIn("uses: actions/github-script@v7", step)
                self.assertNotIn("gh ", step)
                self.assertNotIn("needs.", step)
        # The immediate article branch must never wait for the PDF workers.
        body = job_body("push-xhs-notes-wechat-drafts")
        self.assertNotIn("translate-report-shard", body)
        self.assertNotIn("build-portal-translated-reports", body)
        neutral = (ROOT / ".github/workflows/neutral-edge-cutover.yml").read_text()
        self.assertIn("- Daily report articles and translations", neutral)
        self.assertIn("group: portal-production-release", neutral)


if __name__ == "__main__":
    unittest.main()
