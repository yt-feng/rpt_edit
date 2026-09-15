#!/usr/bin/env python3
"""Replay workflow gates for the ZIP timeout that suppressed the daily PDF."""

import re
import unittest
from pathlib import Path


WORKFLOWS = Path(__file__).resolve().parents[1] / ".github/workflows"
UPSTREAM = WORKFLOWS / "dropbox-latest-pdf-to-xhs-sharded.yml"
MARKET = WORKFLOWS / "market-views-latex-pdf.yml"


def job(path, name):
    text = path.read_text(encoding="utf-8")
    return re.search(
        rf"(?ms)^  {re.escape(name)}:\n(.*?)(?=^  [\w-]+:\n|\Z)", text
    ).group(1)


def gate(block, results, *, selected="64", cancelled=False):
    expression = re.search(r"(?s)\bif:.*?\$\{\{(.*?)\}\}", block).group(1)
    expression = expression.replace("needs.*.result", repr(list(results.values())))
    expression = re.sub(
        r"needs\.([\w-]+)\.result", lambda m: repr(results[m[1]]), expression
    )
    expression = expression.replace(
        "needs.select-macro-reports.outputs.selected_count", repr(selected)
    )
    expression = expression.replace("always()", "True")
    expression = expression.replace("cancelled()", repr(cancelled))
    expression = expression.replace("&&", " and ").replace("||", " or ")
    expression = re.sub(r"!(?!=)", " not ", expression)
    return eval(" ".join(expression.split()), {"__builtins__": {}}, {
        "contains": lambda values, value: value in values,
    })


class MarketViewsWorkflowContractTests(unittest.TestCase):
    def test_zip_timeout_cannot_suppress_complete_shards(self):
        trigger = job(UPSTREAM, "trigger-market-views")
        needs = re.search(r"needs: \[(.*?)\]", trigger).group(1).split(", ")
        self.assertIn("process-shard", needs)
        self.assertNotIn("package-publish-ready", needs)
        for package in ("success", "failure", "cancelled", "skipped"):
            with self.subTest(package=package):
                self.assertTrue(gate(trigger, {
                    "process-shard": "success", "package-publish-ready": package,
                }))
        for shards in ("failure", "cancelled", "skipped"):
            self.assertFalse(gate(trigger, {"process-shard": shards}))
        self.assertFalse(gate(trigger, {"process-shard": "success"}, selected="0"))
        self.assertFalse(gate(trigger, {"process-shard": "success"}, cancelled=True))

    def test_r2_consumer_validates_producer_shard_count(self):
        trigger = job(UPSTREAM, "trigger-market-views")
        self.assertIn("EXPECTED_SHARDS: ${{ needs.select-macro-reports.outputs.effective_shard_count }}", trigger)
        self.assertIn('-f expected_shards="$EXPECTED_SHARDS"', trigger)
        market = MARKET.read_text(encoding="utf-8")
        download = market.split("- name: Download bank inputs from private R2", 1)[1].split("\n      - name:", 1)[0]
        self.assertIn('--expected-count "${{ github.event.inputs.expected_shards || \'0\' }}"', download)
        self.assertIn('gh run watch "$MARKET_RUN_ID"', trigger)

    def test_cleanup_retains_inputs_for_failed_or_cancelled_consumers(self):
        cleanup = job(UPSTREAM, "cleanup-private-handoff")
        results = {name: "success" for name in (
            "package-publish-ready", "trigger-market-views", "trigger-chart-search-index",
            "push-xhs-notes-wechat-drafts", "build-portal-translated-reports",
            "push-portal-translated-wechat-drafts",
        )}
        self.assertTrue(gate(cleanup, results))
        for name in results:
            for status in ("failure", "cancelled"):
                with self.subTest(name=name, status=status):
                    self.assertFalse(gate(cleanup, {**results, name: status}))
        self.assertFalse(gate(cleanup, {**results, "trigger-market-views": "skipped"}))
        for name in ("push-xhs-notes-wechat-drafts", "build-portal-translated-reports", "push-portal-translated-wechat-drafts"):
            results[name] = "skipped"
        self.assertTrue(gate(cleanup, results))

    def test_timeout_cancellation_reaches_existing_alert_policy(self):
        for workflow in (UPSTREAM, MARKET):
            notify = job(workflow, "notify-failure")
            for status in ("failure", "cancelled"):
                self.assertTrue(gate(notify, {"job": status}, cancelled=status == "cancelled"))
            for status in ("success", "skipped"):
                self.assertFalse(gate(notify, {"job": status}))


if __name__ == "__main__":
    unittest.main(verbosity=2)
