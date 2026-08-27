#!/usr/bin/env python3
from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/portal-email-routing-config.yml"
IDENTITY_GUARD = ROOT / "scripts/check_public_identity.py"


class EmailRoutingWorkflowContractTests(unittest.TestCase):
    def workflow(self) -> str:
        return WORKFLOW.read_text(encoding="utf-8")

    def test_workflow_is_manual_and_defaults_to_audit(self) -> None:
        workflow = self.workflow()
        self.assertIn("workflow_dispatch:", workflow)
        self.assertNotRegex(workflow, r"(?m)^\s+(?:schedule|push|pull_request):")
        self.assertRegex(workflow, r"mode:[\s\S]*?default:\s*audit")
        self.assertRegex(workflow, r"options:[\s\S]*?- audit[\s\S]*?- apply")

    def test_destination_is_only_loaded_from_the_dedicated_secret(self) -> None:
        workflow = self.workflow()
        occurrences = re.findall(
            r"(?m)^\s+PORTAL_FORWARD_DESTINATION_EMAIL:\s*[^\n]+",
            workflow,
        )
        self.assertEqual(
            [occurrence.strip() for occurrence in occurrences],
            ["PORTAL_FORWARD_DESTINATION_EMAIL: ${{ secrets.PORTAL_FORWARD_DESTINATION_EMAIL }}"],
        )
        self.assertNotIn("vars.PORTAL_FORWARD_DESTINATION_EMAIL", workflow)
        self.assertNotRegex(workflow, r"(?i)[a-z0-9._%+-]+@gmail\.com")

    def test_dedicated_token_is_preferred_and_runtime_values_are_masked(self) -> None:
        workflow = self.workflow()
        self.assertIn(
            "secrets.CLOUDFLARE_EMAIL_ROUTING_API_TOKEN || secrets.CLOUDFLARE_API_TOKEN",
            workflow,
        )
        self.assertIn("--github-add-mask", workflow)
        self.assertIn('--mode "$PORTAL_EMAIL_ROUTING_MODE"', workflow)
        self.assertIn("python3 -B scripts/test_configure_portal_email_routing.py", workflow)
        self.assertIn("python3 -B scripts/test_portal_email_routing_workflow.py", workflow)

    def test_public_identity_guard_accepts_the_new_sources(self) -> None:
        self.assertTrue(IDENTITY_GUARD.is_file())
        workflow = self.workflow().casefold()
        script = (ROOT / "scripts/configure_portal_email_routing.py").read_text(encoding="utf-8").casefold()
        blocked = "".join(("kc", "desk"))
        self.assertNotIn(blocked, workflow)
        self.assertNotIn(blocked, script)


if __name__ == "__main__":
    unittest.main(verbosity=2)
