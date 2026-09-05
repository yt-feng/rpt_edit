#!/usr/bin/env python3
from __future__ import annotations

import gzip
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
import unittest
from unittest.mock import Mock

from run_portal_locale_backfill import run_backfill


def balance(amount: str = "500", *, available: bool = True) -> dict:
    return {
        "status": "passed", "mode": "balance", "provider_requests": 0, "balance_requests": 1,
        "is_available": available,
        "balance_infos": [{"currency": "CNY", "total_balance": amount,
                           "granted_balance": "0", "topped_up_balance": amount}],
    }


def cache(path: Path, count: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(gzip.compress(json.dumps({"locales": {"ko": {
        str(index): {"source": f"source-{index}", "translation": f"translated-{index}"}
        for index in range(count)
    }}}).encode()))


def translation_gap(*, rows: int = 4, **diagnostics) -> dict:
    return {
        "returncode": 1, "rows": rows,
        "diagnostics": {
            "status": "failed", "ready": False, "preflight_only": False,
            "stop_category": None, "stop_reason": "", "remaining_units_total": 1,
            "build_error": "Locale translation has 1 unresolved source units; completed rows saved",
            "usage_complete_responses": 2,
            "deepl_repair": {"provider_requests": 1, "billed_characters": 30,
                             "unobserved_requests": 0, "reserved_characters": 0, "stop_reason": ""},
            **diagnostics,
        },
    }


class PortalLocaleBackfillTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = TemporaryDirectory(prefix="locale-backfill-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.initial = self.root / "restored.json.gz"
        self.output = self.root / "candidate/data/i18n/cache-v1.json.gz"
        self.diagnostics = self.root / "locale-full-diagnostics.json"
        cache(self.initial, 2)
        self.commands: list[list[str]] = []

    def provider(self, outcomes: list[dict]) -> Mock:
        def execute(command: list[str], *, check: bool):
            self.assertFalse(check)
            self.commands.append(command)
            outcome = outcomes[len(self.commands) - 1]
            report = {
                "status": "checkpointed", "ready": False, "stop_category": "budget",
                "provider_requests": 2, "usage_unknown_responses": 0,
                "usage_partial_responses": 0, "unobserved_provider_requests": 0,
                "usage_totals": {"prompt_tokens": 10, "completion_tokens": 20, "total_tokens": 30},
                **outcome.get("diagnostics", {}),
            }
            if outcome.get("write_cache", True):
                cache(Path(command[command.index("--cache-out") + 1]), outcome.get("rows", 2 + len(self.commands)))
            if outcome.get("write_diagnostics", True):
                Path(command[command.index("--diagnostics-out") + 1]).write_text(json.dumps(report))
            return SimpleNamespace(returncode=outcome.get("returncode", 0))
        return Mock(side_effect=execute)

    def run_backfill(self, outcomes: list[dict], *, balances: list[dict] | None = None, args=None):
        reader = Mock(side_effect=balances or [balance()] * 3)
        provider = self.provider(outcomes)
        report = run_backfill(
            args or ["--root", str(self.root / "candidate"), "--workers", "500", "--attempts", "2"],
            cache_in=self.initial, cache_out=self.output, diagnostics_out=self.diagnostics,
            balance_reader=reader, runner=provider,
        )
        self.assertEqual(json.loads(self.diagnostics.read_text()), report)
        return report, reader, provider

    def test_budget_resume_reuses_checkpoint_and_refreshes_balance(self):
        report, reader, provider = self.run_backfill([
            {"rows": 4}, {"rows": 6, "diagnostics": {"status": "passed", "ready": True}},
        ], balances=[balance("500"), balance("257.20")])
        self.assertEqual(reader.call_count, 2)
        self.assertEqual(provider.call_count, 2)
        self.assertEqual(["400", "237.20"], [cmd[cmd.index("--max-provider-cost-cny") + 1] for cmd in self.commands])
        self.assertEqual(self.commands[0][self.commands[0].index("--cache-in") + 1], str(self.initial))
        self.assertEqual(self.commands[1][self.commands[1].index("--cache-in") + 1], str(self.output))
        for command in self.commands:
            self.assertIn("--checkpoint-on-budget", command)
            self.assertIn("--workers", command)
            self.assertEqual(command[command.index("--workers") + 1], "500")
        self.assertEqual(report["status"], "passed")
        self.assertTrue(report["ready"])
        self.assertEqual(report["provider_requests"], 4)
        self.assertEqual(report["usage_totals"]["total_tokens"], 60)
        self.assertEqual(len(list(self.root.glob("locale-full-diagnostics-round-*.json"))), 2)
        self.assertEqual(len(list(self.root.glob("locale-full-diagnostics-balance-*.json"))), 2)

    def test_residual_translation_gaps_resume_saved_growth_then_require_complete_build(self):
        report, reader, provider = self.run_backfill([
            translation_gap(rows=4), {"rows": 5, "diagnostics": {"status": "passed", "ready": True}},
        ], balances=[balance("500"), balance("80")])
        self.assertEqual((reader.call_count, provider.call_count), (2, 2))
        self.assertEqual(self.commands[1][self.commands[1].index("--cache-in") + 1], str(self.output))
        self.assertEqual([command[command.index("--max-provider-cost-cny") + 1] for command in self.commands], ["400", "60"])
        self.assertEqual(report["rounds"][0]["stop_category"], "translation_gaps")
        self.assertEqual(report["rounds"][0]["cache_rows_before"], 2)
        self.assertEqual(report["rounds"][0]["cache_rows_after"], 4)
        self.assertEqual(report["rounds"][0]["remaining_units_total"], 1)
        self.assertFalse(report["rounds"][0]["ready"])
        self.assertEqual(report["status"], "passed")
        self.assertTrue(report["ready"])

    def test_budget_checkpoint_with_unsettled_deepl_usage_never_resumes(self):
        for unobserved, reserved in ((1, 300), (0, 300), (1, 0)):
            with self.subTest(unobserved=unobserved, reserved=reserved):
                self.commands.clear()
                report, reader, provider = self.run_backfill([{
                    "rows": 4,
                    "diagnostics": {"stop_category": "budget", "deepl_repair": {
                        "provider_requests": 1, "billed_characters": 0, "stop_reason": "",
                        "unobserved_requests": unobserved, "reserved_characters": reserved,
                    }},
                }])
                self.assertEqual((reader.call_count, provider.call_count), (1, 1))
                self.assertEqual(report["status"], "failed")
                self.assertEqual(report["stop_category"], "incomplete_usage")
                self.assertFalse(report["ready"])

    def test_repair_limit_checkpoint_with_unsettled_deepl_usage_never_resumes(self):
        report, reader, provider = self.run_backfill([{
            "rows": 4,
            "diagnostics": {"stop_category": "repair_limit", "deepl_repair": {
                "provider_requests": 1, "billed_characters": 0, "stop_reason": "",
                "unobserved_requests": 1, "reserved_characters": 300,
            }},
        }])
        self.assertEqual((reader.call_count, provider.call_count), (1, 1))
        self.assertEqual(report["status"], "failed")
        self.assertEqual(report["stop_category"], "incomplete_usage")
        self.assertFalse(report["ready"])

    def test_residual_translation_gaps_without_cache_growth_never_resume(self):
        report, reader, provider = self.run_backfill([translation_gap(rows=2)])
        self.assertEqual((reader.call_count, provider.call_count), (1, 1))
        self.assertEqual(report["status"], "checkpointed")
        self.assertEqual(report["stop_category"], "no_progress")
        self.assertFalse(report["ready"])

    def test_residual_translation_gaps_keep_existing_three_round_limit(self):
        report, reader, provider = self.run_backfill([translation_gap(rows=rows) for rows in (3, 4, 5)])
        self.assertEqual((reader.call_count, provider.call_count), (3, 3))
        self.assertEqual(report["status"], "checkpointed")
        self.assertEqual(report["stop_category"], "round_limit")
        self.assertFalse(report["ready"])
        self.assertTrue(all(not row["ready"] for row in report["rounds"]))

    def test_residual_translation_retry_rejects_unknown_or_unobserved_usage(self):
        for change in (
            {"usage_unknown_responses": 1}, {"usage_partial_responses": 1},
            {"unobserved_provider_requests": 1}, {"usage_complete_responses": 1},
            {"usage_complete_responses": None},
            {"usage_totals": {"prompt_tokens": 10, "completion_tokens": 20, "total_tokens": 40}},
            {"deepl_repair": {"unobserved_requests": 1, "reserved_characters": 30, "stop_reason": ""}},
            {"deepl_repair": {"unobserved_requests": 0, "reserved_characters": 30, "stop_reason": ""}},
        ):
            with self.subTest(change=change):
                self.commands.clear()
                report, reader, provider = self.run_backfill([translation_gap(**change)])
                self.assertEqual((reader.call_count, provider.call_count), (1, 1))
                self.assertEqual(report["status"], "failed")
                self.assertFalse(report["ready"])

    def test_residual_translation_retry_never_accepts_terminal_preflight_or_render_errors(self):
        for change in (
            {"stop_reason": "provider transport failed"}, {"stop_category": "systemic"},
            {"stop_category": "deepl_quota"}, {"stop_category": "provider"},
            {"deepl_repair": {"unobserved_requests": 0, "reserved_characters": 0, "stop_reason": "quota"}},
            {"preflight_only": True}, {"remaining_units_total": 0},
            {"remaining_units_total": 2}, {"remaining_units_total": True},
            {"build_error": "Chinese HTML must contain exactly one locale bootstrap: about.html"},
            {"build_error": "ValueError"}, {"ready": True},
        ):
            with self.subTest(change=change):
                self.commands.clear()
                report, reader, provider = self.run_backfill([translation_gap(**change)])
                self.assertEqual((reader.call_count, provider.call_count), (1, 1))
                self.assertEqual(report["status"], "failed")
                self.assertFalse(report["ready"])

    def test_at_most_three_rounds_and_incomplete_candidate_never_ready(self):
        report, reader, provider = self.run_backfill([{}, {}, {}])
        self.assertEqual(reader.call_count, 3)
        self.assertEqual(provider.call_count, 3)
        self.assertEqual(report["status"], "checkpointed")
        self.assertEqual(report["stop_category"], "round_limit")
        self.assertFalse(report["ready"])

    def test_bounded_repair_checkpoint_can_resume_but_other_checkpoint_cannot(self):
        report, _, provider = self.run_backfill([
            {"diagnostics": {"stop_category": "repair_limit"}},
            {"diagnostics": {"status": "passed"}},
        ])
        self.assertTrue(report["ready"])
        self.assertEqual(provider.call_count, 2)
        for category in ("quality", "provider", "transport", "systemic"):
            with self.subTest(category=category):
                self.commands.clear()
                report, _, provider = self.run_backfill([{"diagnostics": {"stop_category": category}}])
                self.assertEqual(provider.call_count, 1)
                self.assertEqual(report["status"], "failed")
                self.assertFalse(report["ready"])

    def test_insufficient_or_unavailable_balance_never_calls_builder(self):
        for snapshot in [balance("20"), balance("2"), balance("-1"), balance("500", available=False)]:
            with self.subTest(snapshot=snapshot):
                report, reader, provider = self.run_backfill([], balances=[snapshot])
                self.assertEqual(reader.call_count, 1)
                provider.assert_not_called()
                self.assertEqual(report["status"], "checkpointed")
                self.assertFalse(report["ready"])
                self.assertEqual(report["provider_requests"], 0)
                self.assertTrue(self.initial.is_file())

    def test_second_round_insufficient_balance_preserves_first_progress(self):
        report, reader, provider = self.run_backfill([{"rows": 5}], balances=[balance(), balance("20")])
        self.assertEqual(provider.call_count, 1)
        self.assertEqual(reader.call_count, 2)
        self.assertEqual(report["status"], "checkpointed")
        self.assertFalse(report["ready"])
        with gzip.open(self.output, "rt") as handle:
            self.assertEqual(len(json.load(handle)["locales"]["ko"]), 5)

    def test_provider_failure_is_red_and_never_resumed(self):
        for returncode in (0, 1):
            with self.subTest(returncode=returncode):
                self.commands.clear()
                report, reader, provider = self.run_backfill([{
                    "returncode": returncode, "diagnostics": {"status": "failed", "stop_category": "provider"},
                }])
                self.assertEqual(provider.call_count, 1)
                self.assertEqual(reader.call_count, 1)
                self.assertEqual(report["status"], "failed")
                self.assertFalse(report["ready"])

    def test_nonzero_exit_even_with_passed_diagnostics_is_failure(self):
        report, _, provider = self.run_backfill([{"returncode": 1, "diagnostics": {"status": "passed"}}])
        self.assertEqual(provider.call_count, 1)
        self.assertEqual(report["status"], "failed")
        self.assertFalse(report["ready"])

    def test_unknown_partial_or_unobserved_usage_never_resumes(self):
        for field in ("usage_unknown_responses", "usage_partial_responses", "unobserved_provider_requests"):
            with self.subTest(field=field):
                self.commands.clear()
                report, reader, provider = self.run_backfill([{"diagnostics": {field: 1}}])
                self.assertEqual(provider.call_count, 1)
                self.assertEqual(reader.call_count, 1)
                self.assertEqual(report["status"], "failed")
                self.assertEqual(report["stop_category"], "incomplete_usage")
                self.assertFalse(report["ready"])

    def test_no_saved_progress_never_resumes(self):
        report, reader, provider = self.run_backfill([{"rows": 2}])
        self.assertEqual(provider.call_count, 1)
        self.assertEqual(reader.call_count, 1)
        self.assertEqual(report["status"], "checkpointed")
        self.assertEqual(report["stop_category"], "no_progress")
        self.assertFalse(report["ready"])

    def test_missing_checkpoint_or_diagnostics_is_failure(self):
        for field in ("write_cache", "write_diagnostics"):
            with self.subTest(field=field), TemporaryDirectory() as directory:
                self.commands.clear()
                self.output = Path(directory) / "cache.gz"
                self.diagnostics = Path(directory) / "diag.json"
                report, _, provider = self.run_backfill([{field: False}])
                self.assertEqual(provider.call_count, 1)
                self.assertEqual(report["status"], "failed")

    def test_balance_failure_or_missing_cny_is_not_silently_checkpointed(self):
        snapshots = [{"status": "failed", "balance_requests": 1},
                     {**balance(), "balance_infos": []},
                     {**balance(), "balance_infos": [{**balance()["balance_infos"][0], "currency": "USD"}]}]
        for snapshot in snapshots:
            with self.subTest(snapshot=snapshot):
                report, _, provider = self.run_backfill([], balances=[snapshot])
                provider.assert_not_called()
                self.assertEqual(report["status"], "failed")

    def test_diagnostics_whitelist_omits_untrusted_fields(self):
        secret = "DO-NOT-RETAIN-provider-secret"
        report, _, _ = self.run_backfill([{"diagnostics": {
            "status": "passed", "response": secret, "build_error": secret,
            "usage_totals": {"total_tokens": 3, "extra": secret},
        }}], balances=[{**balance(), "Authorization": secret, "body": secret}])
        self.assertNotIn(secret, json.dumps(report))
        self.assertNotIn(secret, self.root.joinpath("locale-full-diagnostics-balance-1.json").read_text())

    def test_budget_override_is_rejected_before_balance_or_translation(self):
        for option in ("--max-provider-cost-cny=900", "--max-provider-cost-cny", "--checkpoint-on-budget", "--preflight-only"):
            with self.subTest(option=option):
                report, reader, provider = self.run_backfill([], args=[option])
                reader.assert_not_called()
                provider.assert_not_called()
                self.assertEqual(report["status"], "failed")

    def test_success_does_not_need_another_balance_read(self):
        report, reader, provider = self.run_backfill([{"diagnostics": {"status": "passed"}}])
        self.assertEqual(provider.call_count, 1)
        self.assertEqual(reader.call_count, 1)
        self.assertTrue(report["ready"])

    def test_deepl_exhaustion_checkpoints_without_starting_another_paid_round(self):
        report, reader, provider = self.run_backfill([{"diagnostics": {
            "stop_category": "deepl_quota", "deepl_repair": {"provider_requests": 2, "billed_characters": 30, "stop_reason": "quota"},
        }}])
        self.assertEqual(provider.call_count, 1)
        self.assertEqual(reader.call_count, 1)
        self.assertEqual(report["status"], "checkpointed")
        self.assertEqual(report["stop_category"], "deepl_quota")
        self.assertFalse(report["ready"])
        self.assertEqual(report["rounds"][0]["deepl_repair"]["billed_characters"], 30)

    def test_unknown_deepl_usage_prevents_budget_continuation(self):
        report, reader, provider = self.run_backfill([{"diagnostics": {
            "stop_category": "budget", "deepl_repair": {"provider_requests": 1, "stop_reason": "usage unverified"},
        }}])
        self.assertEqual(provider.call_count, 1)
        self.assertEqual(reader.call_count, 1)
        self.assertEqual(report["status"], "checkpointed")
        self.assertEqual(report["stop_category"], "deepl_stopped")
        self.assertFalse(report["ready"])


if __name__ == "__main__":
    unittest.main()
