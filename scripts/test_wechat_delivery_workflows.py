#!/usr/bin/env python3
"""Exercise delivery failure propagation and production receipt wiring."""

import os
from pathlib import Path
import subprocess
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[1]
DAILY = "dropbox-latest-pdf-to-xhs-sharded.yml"
PRODUCERS = {
    DAILY: ("push-xhs-notes-wechat-drafts", "push-portal-translated-wechat-drafts"),
    "institution-latest-pdf-to-wechat.yml": ("upload-wechat-drafts",),
    "consulting-latest-pdf-to-wechat.yml": ("upload-wechat-drafts",),
    "ark-invest-feed-to-wechat.yml": ("upload-wechat-drafts",),
}


def workflow(name):
    return yaml.safe_load((ROOT / ".github/workflows" / name).read_text())


class DeliveryWorkflowTests(unittest.TestCase):
    def test_every_restore_consumer_binds_history_to_actual_mutation_steps_and_immutable_archive(self):
        consumers = 0
        for path in (ROOT / '.github/workflows').glob('*.yml'):
            for jobid, job in (yaml.safe_load(path.read_text()) or {}).get('jobs', {}).items():
                steps = job.get('steps', [])
                for restore in steps:
                    if restore.get('uses') != './.github/actions/restore-wechat-diagnostics':
                        continue
                    consumers += 1
                    values = restore['with']
                    names = values.get('submission-step-names', 'Build and upload WeChat drafts').splitlines()
                    actual = [step.get('name') for step in steps]
                    for name in filter(None, map(str.strip, names)):
                        self.assertEqual(actual.count(name), 1, (path.name, jobid, name))
                    self.assertNotIn('-attempt-', values['name'])
                    if path.name == 'wechat-draft-readback.yml':
                        mutation = next(step for step in steps if step.get('name') == names[0])
                        self.assertIn('outputs.found', mutation['env']['REQUIRE_CHECKPOINT'])
                    else:
                        self.assertTrue(values.get('checkpoint-path'), (path.name, jobid))
                    archives = [step for step in steps if 'artifact' in step.get('uses', '')
                                and step.get('with', {}).get('name', '').startswith(values['name'])]
                    self.assertTrue(archives, (path.name, jobid))
                    for archive in archives:
                        self.assertIn('-attempt-${{ github.run_attempt }}', archive['with']['name'])
                        self.assertNotIn('overwrite', archive['with'])
        self.assertGreaterEqual(consumers, 10)

    def test_private_recovery_requires_exact_complete_live_delivery_and_keeps_all_queued_handoffs(self):
        recovery = workflow('recover-private-wechat-handoff.yml')
        steps = recovery['jobs']['recover']['steps']
        delivery = next(step for step in steps if step.get('id') == 'delivery')
        self.assertIn('institution_wechat_delivery_receipt.py', delivery['run'])
        self.assertIn('--expected-count "$EXPECTED_COUNT"', delivery['run'])
        self.assertIn('--source-dir "portal_translated_reports/$SCOPE/$DATE_FOLDER"', delivery['run'])
        self.assertLess(steps.index(delivery), next(i for i, step in enumerate(steps)
                                                   if step.get('name') == 'Update public Blog archive'))
        archive = next(step for step in steps if step.get('name') == 'Archive WeChat draft diagnostics')
        self.assertEqual(archive['with']['required'], 'true')
        for filename in ('institution-latest-pdf-to-wechat.yml', 'consulting-latest-pdf-to-wechat.yml',
                         'recover-private-wechat-handoff.yml'):
            concurrency = workflow(filename)['concurrency']
            self.assertEqual(concurrency['queue'], 'max')
            self.assertFalse(concurrency['cancel-in-progress'])

    def test_every_production_upload_requires_live_acceptance_and_durable_checkpoint(self):
        for filename, jobs in PRODUCERS.items():
            for jobid in jobs:
                with self.subTest(workflow=filename, job=jobid):
                    job = workflow(filename)["jobs"][jobid]
                    steps = job["steps"]
                    gate = next(i for i, step in enumerate(steps) if step.get("id") == "delivery")
                    archive = next(i for i, step in enumerate(steps) if step.get("id") == "archive_wechat_receipts")
                    blog = next(i for i, step in enumerate(steps) if step.get("name") == "Update public Blog archive")
                    self.assertLess(gate, archive)
                    self.assertLess(archive, blog)
                    self.assertIn("institution_wechat_delivery_receipt.py", steps[gate]["run"])
                    self.assertIn("--source-dir", steps[gate]["run"])
                    self.assertIn("--expected-count \"${{ needs.", steps[gate]["run"])
                    self.assertIn("publish", steps[gate]["if"])
                    self.assertEqual("${{ steps.delivery.outputs.delivery_complete }}", job["outputs"]["delivery_complete"])
                    receipt = steps[archive]["with"]
                    self.assertEqual("true", receipt["required"])
                    self.assertEqual("error", receipt["if-no-files-found"])
                    self.assertGreaterEqual(receipt["retention-days"], 14)
                    self.assertIn("checkpoint-path", receipt)
                    restore = next(step for step in steps if step.get("uses") == "./.github/actions/restore-wechat-diagnostics")
                    self.assertEqual(receipt["checkpoint-path"], restore["with"]["checkpoint-path"])
                    self.assertTrue(receipt["name"].endswith("-attempt-${{ github.run_attempt }}"))
                    self.assertIn("always()", steps[archive]["if"])

    def test_missing_institution_or_consulting_handoff_cannot_exit_success(self):
        for name in ("institution-latest-pdf-to-wechat.yml", "consulting-latest-pdf-to-wechat.yml"):
            upload = next(step for step in workflow(name)["jobs"]["upload-wechat-drafts"]["steps"] if step.get("id") == "upload")
            missing = upload["run"].split('if [ ! -d "$TRANSLATED_DIR" ]; then', 1)[1].split("fi", 1)[0]
            with self.subTest(workflow=name):
                self.assertIn("exit 1", missing)
                self.assertNotIn("exit 0", missing)
                cleanup = workflow(name)["jobs"]["cleanup-private-handoff"]["if"]
                self.assertIn("outputs.delivery_complete == 'true'", cleanup)

    def test_daily_success_requires_verified_delivery_output(self):
        script = workflow(DAILY)["jobs"]["validate-report-delivery"]["steps"][0]["run"]
        base = dict(SELECTION_RESULT="success", SOURCE_STATUS="success", SELECTED_COUNT="15", NO_WORK="false",
                    PRIMARY_READY="true", RECOVERED_DELIVERY="skipped", WECHAT_ENABLED="true", WECHAT_SOURCE="xhs_notes",
                    WECHAT_RESULT="success", WECHAT_DELIVERY_COMPLETE="true", TRANSLATED_DELIVERY_COMPLETE="true",
                    WECHAT_PUBLISH="false", TRANSLATION_COUNT="0", TRANSLATION_RESULT="skipped", TRANSLATED_WECHAT_RESULT="success")
        cases = [({}, True), ({"WECHAT_DELIVERY_COMPLETE": ""}, False), ({"WECHAT_DELIVERY_COMPLETE": "false"}, False),
                 ({"WECHAT_SOURCE": "portal_translated", "TRANSLATED_DELIVERY_COMPLETE": ""}, False),
                 ({"WECHAT_SOURCE": "portal_translated"}, True),
                 ({"SELECTED_COUNT": "0", "NO_WORK": "true", "WECHAT_DELIVERY_COMPLETE": ""}, True),
                 ({"SELECTED_COUNT": "0", "NO_WORK": "false"}, False)]
        for changes, success in cases:
            with self.subTest(changes=changes):
                result = subprocess.run(["bash", "-e", "-o", "pipefail", "-c", script],
                                        env={**os.environ, **base, **changes}, text=True, capture_output=True)
                self.assertEqual(result.returncode == 0, success, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
