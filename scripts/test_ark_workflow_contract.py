#!/usr/bin/env python3
"""Regression tests for the ARK workflow sparse-checkout contract."""

from __future__ import annotations

import re
import unittest
from pathlib import Path


WORKFLOW = Path(__file__).resolve().parents[1] / ".github/workflows/ark-invest-feed-to-wechat.yml"


class ArkWorkflowContractTests(unittest.TestCase):
    def workflow_text(self) -> str:
        return WORKFLOW.read_text(encoding="utf-8")

    def test_pull_step_keeps_blog_archive_in_sparse_checkout(self) -> None:
        workflow = self.workflow_text()
        match = re.search(
            r"git sparse-checkout set --no-cone \\\n(?P<paths>.*?)\n\s+git fetch",
            workflow,
            flags=re.DOTALL,
        )

        self.assertIsNotNone(match, "ARK workflow sparse-checkout command not found")
        self.assertIn("portal_suite/data/blog_archive", match.group("paths"))

    def test_upload_job_downloads_generated_articles_from_artifact(self) -> None:
        workflow = self.workflow_text()
        upload_job = workflow.split("  upload-wechat-drafts:", 1)[1].split(
            "  notify-failure:", 1
        )[0]

        download_step = "- name: Download generated ARK article artifact"
        build_step = "- name: Build and upload WeChat drafts"
        self.assertIn("uses: actions/download-artifact@v4", upload_job)
        self.assertIn(
            "name: ark-invest-feed-run-${{ needs.fetch-and-build.outputs.date_folder }}-${{ github.run_id }}",
            upload_job,
        )
        self.assertLess(upload_job.index(download_step), upload_job.index(build_step))
        self.assertNotIn("Commit generated ARK outputs", workflow)
        self.assertIn("Generated ARK artifact is missing $TRANSLATED_DIR", upload_job)
        self.assertNotIn("nothing to upload", upload_job)

    def test_dispatch_can_replay_an_artifact_from_a_prior_run(self) -> None:
        workflow = self.workflow_text()
        fetch_job = workflow.split("  fetch-and-build:", 1)[1].split(
            "  upload-wechat-drafts:", 1
        )[0]

        self.assertIn("replay_run_id:", workflow)
        self.assertIn("replay_date_folder:", workflow)
        self.assertRegex(workflow, r"(?m)^  actions: read$")
        self.assertIn("- name: Download prior ARK run artifact", fetch_job)
        self.assertIn("github-token: ${{ github.token }}", fetch_job)
        self.assertIn("repository: ${{ github.repository }}", fetch_job)
        self.assertIn("run-id: ${{ steps.replay.outputs.run_id }}", fetch_job)
        self.assertIn("Replayed ARK artifact has no translated articles", fetch_job)
        self.assertIn("SUMMARY_COUNT", fetch_job)
        self.assertIn(
            "article_count: ${{ steps.handoff.outputs.article_count }}",
            fetch_job,
        )
        self.assertIn(
            "name: ark-invest-feed-run-${{ steps.handoff.outputs.date_folder }}-${{ github.run_id }}",
            fetch_job,
        )
        self.assertIn("overwrite: true", fetch_job)


if __name__ == "__main__":
    unittest.main(verbosity=2)
