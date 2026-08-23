#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from unittest.mock import Mock, patch
from pathlib import Path
from types import SimpleNamespace

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, relative: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    if spec is None or spec.loader is None:
        raise RuntimeError(relative)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


chart = load_module("build_chart_search_index", "scripts/build_chart_search_index.py")
merge = load_module("merge_chart_search_index", "scripts/merge_chart_search_index.py")
r2 = load_module("chart_search_r2", "scripts/chart_search_r2.py")


def write_image(path: Path, color: str = "white") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    image = Image.new("RGB", (640, 360), color)
    draw = ImageDraw.Draw(image)
    draw.line((20, 300, 180, 220, 340, 240, 600, 80), fill="blue", width=8)
    draw.text((30, 25), "MLCC shipments 2024-2026", fill="black")
    image.save(path)


def write_report(root: Path, name: str, title: str, color: str = "white") -> Path:
    report = root / "shard_0" / name
    image = report / "assets" / "source_image_01.png"
    write_image(image, color)
    (report / "status.json").write_text(
        json.dumps({"source_pdf": f"/private/input/{title.replace(' ', '_')}.pdf"}),
        encoding="utf-8",
    )
    return report


def sample_analysis(is_chart: bool = True) -> dict:
    return {
        "is_chart": is_chart,
        "content_kind": "chart" if is_chart else "invalid",
        "quality_score": 92 if is_chart else 10,
        "has_data_evidence": is_chart,
        "invalid_reason": "none" if is_chart else "decorative",
        "title": "MLCC 出货量",
        "chart_type": "line",
        "description": "图中展示 2024 至 2026 年 MLCC 出货量上升。",
        "trend_summary": "总体上升",
        "metrics": ["shipments"],
        "entities": ["MLCC"],
        "periods": ["2024", "2026"],
        "geographies": [],
        "units": ["million units"],
        "keywords": ["MLCC", "出货量"],
    }


class ChartSearchIndexTests(unittest.TestCase):
    def test_deduplicates_model_calls_and_never_exports_paths(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            reports = workspace / "260809"
            write_report(reports, "report_a", "Alpha MLCC Outlook")
            write_report(reports, "report_b", "Beta MLCC Outlook")
            catalog = workspace / "catalog.json"
            catalog.write_text(json.dumps({"items": [
                {"id": "report-alpha", "title": "Alpha MLCC Outlook"},
                {"id": "report-beta", "title": "Beta MLCC Outlook"},
            ]}), encoding="utf-8")
            candidates = chart.discover_candidates(
                reports,
                chart.load_catalog_lookup(catalog),
                date_folder="260809",
                max_per_report=8,
            )
            calls = []

            def analyze(path: Path) -> dict:
                calls.append(path)
                return sample_analysis()

            state_path = workspace / "state.json"
            state = {"schema_version": 1, "items": {}}
            index, summary = chart.build_index(
                candidates,
                state=state,
                previous_index={"schema_version": 1, "reports": []},
                state_path=state_path,
                asset_output_dir=workspace / "assets",
                analyze=analyze,
                max_model_calls=20,
            )
            self.assertEqual(len(calls), 1)
            self.assertEqual(summary["cache_hits"], 1)
            self.assertEqual(index["report_count"], 2)
            self.assertEqual(index["item_count"], 2)
            self.assertEqual({item["report_id"] for item in index["reports"]}, {"report-alpha", "report-beta"})
            serialized = json.dumps(index)
            self.assertNotIn("/private/input", serialized)
            self.assertNotIn(str(workspace), serialized)
            self.assertEqual(len(list((workspace / "assets").glob("*.jpg"))), 1)

    def test_checkpoint_skips_api_on_rerun(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            reports = workspace / "260809"
            write_report(reports, "report_a", "Alpha MLCC Outlook")
            candidates = chart.discover_candidates(reports, {}, date_folder="260809")
            state_path = workspace / "state.json"
            first_state = {"schema_version": 1, "items": {}}
            first, _summary = chart.build_index(
                candidates,
                state=first_state,
                previous_index={"schema_version": 1, "reports": []},
                state_path=state_path,
                asset_output_dir=workspace / "assets",
                analyze=lambda _path: sample_analysis(),
                max_model_calls=20,
            )

            def should_not_run(_path: Path) -> dict:
                raise AssertionError("checkpoint was ignored")

            second, summary = chart.build_index(
                candidates,
                state=json.loads(state_path.read_text(encoding="utf-8")),
                previous_index=first,
                state_path=state_path,
                asset_output_dir=workspace / "assets-second",
                analyze=should_not_run,
                max_model_calls=20,
            )
            self.assertEqual(summary["model_calls"], 0)
            self.assertEqual(summary["cache_hits"], 1)
            self.assertEqual(second["item_count"], 1)

    def test_legacy_ok_checkpoints_remain_unprocessed_until_every_batch_is_reclassified(self) -> None:
        """A version migration must not publish after only the first 20 calls."""
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            candidate_count = 358
            candidates = [
                chart.ChartCandidate(
                    image_path=workspace / f"source_image_{ordinal:03d}.png",
                    image_sha256=f"{ordinal:064x}",
                    report_ref=f"report-{ordinal:03d}",
                    report_id=f"report-{ordinal:03d}",
                    report_title=f"Report {ordinal:03d}",
                    date_folder="260811",
                    ordinal=ordinal,
                )
                for ordinal in range(1, candidate_count + 1)
            ]
            legacy_analysis = sample_analysis(False)
            state = {
                "schema_version": 1,
                "analysis_version": "chart-search-v1",
                "items": {
                    candidate.image_sha256: {
                        "status": "ok",
                        "analysis_version": "chart-search-v1",
                        "attempts": 1,
                        "last_attempt_run_id": "older-workflow",
                        "analysis": legacy_analysis,
                    }
                    for candidate in candidates
                },
            }
            previous = {"schema_version": 1, "reports": []}
            calls = 0

            def classify_as_non_chart(_path: Path) -> dict:
                nonlocal calls
                calls += 1
                return sample_analysis(False)

            summaries = []
            for _batch in range(20):
                previous, summary = chart.build_index(
                    candidates,
                    state=state,
                    previous_index=previous,
                    state_path=workspace / "state.json",
                    asset_output_dir=workspace / "assets",
                    analyze=classify_as_non_chart,
                    max_model_calls=20,
                    attempt_run_id="migration-workflow",
                )
                summaries.append(summary)
                if summary["unprocessed_count"] == 0:
                    break

            self.assertEqual(summaries[0]["model_calls"], 20)
            self.assertEqual(summaries[0]["deferred"], 338)
            self.assertEqual(summaries[0]["unprocessed_count"], 338)
            self.assertEqual(len(summaries), 18)
            self.assertEqual(calls, candidate_count)
            self.assertEqual(summaries[-1]["model_calls"], 18)
            self.assertEqual(summaries[-1]["unprocessed_count"], 0)
            self.assertTrue(all(chart.state_is_reusable(row) for row in state["items"].values()))

    def test_non_chart_is_checkpointed_but_not_indexed(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            reports = workspace / "260809"
            write_report(reports, "report_a", "Decorative Image")
            candidates = chart.discover_candidates(reports, {}, date_folder="260809")
            index, summary = chart.build_index(
                candidates,
                state={"schema_version": 1, "items": {}},
                previous_index={"schema_version": 1, "reports": []},
                state_path=workspace / "state.json",
                asset_output_dir=workspace / "assets",
                analyze=lambda _path: sample_analysis(False),
                max_model_calls=20,
            )
            self.assertEqual(summary["model_calls"], 1)
            self.assertEqual(index["item_count"], 0)

    def test_author_disclaimer_toc_and_pure_text_are_never_publishable(self) -> None:
        fixtures = (
            ("author", "分析师简介", "作者介绍与联系方式"),
            ("disclaimer", "Important Disclosures", "Legal notice and disclaimer"),
            ("toc", "目录", "Table of contents"),
            ("pure_text", "研究说明", "只有正文段落，没有数据关系"),
        )
        for reason, title, description in fixtures:
            payload = sample_analysis()
            payload.update({
                "content_kind": "invalid",
                "quality_score": 95,
                "has_data_evidence": False,
                "invalid_reason": reason,
                "title": title,
                "description": description,
            })
            with self.subTest(reason=reason):
                self.assertFalse(chart.is_publishable_chart(chart.normalize_analysis(payload)))

    def test_valid_table_and_flow_require_structured_evidence(self) -> None:
        table = sample_analysis()
        table.update({"content_kind": "table", "chart_type": "table", "metrics": ["Revenue"]})
        self.assertTrue(chart.is_publishable_chart(chart.normalize_analysis(table)))
        table["metrics"] = []
        table["entities"] = []
        table["periods"] = []
        table["geographies"] = []
        table["units"] = []
        self.assertFalse(chart.is_publishable_chart(chart.normalize_analysis(table)))

    def test_public_chart_record_is_explicitly_v2(self) -> None:
        candidate = SimpleNamespace(
            report_ref="report-ref",
            image_sha256="d" * 64,
            ordinal=7,
        )
        record = chart.chart_record(candidate, chart.normalize_analysis(sample_analysis()))
        self.assertEqual(record["analysis_version"], "chart-search-v2")

    def test_reclassification_removes_prior_false_positive_from_index(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            reports = workspace / "260809"
            write_report(reports, "report_a", "Important Disclosures")
            candidate = chart.discover_candidates(reports, {}, date_folder="260809")[0]
            chart_id = chart.chart_record(candidate, chart.normalize_analysis(sample_analysis()))["id"]
            previous = {
                "schema_version": 1,
                "reports": [{
                    "report_ref": candidate.report_ref,
                    "report_id": "",
                    "title": candidate.report_title,
                    "date_folder": "260809",
                    "charts": [{
                        **chart.chart_record(candidate, chart.normalize_analysis(sample_analysis())),
                        "id": chart_id,
                    }],
                }],
            }
            rejected = sample_analysis()
            rejected.update({
                "is_chart": False,
                "content_kind": "invalid",
                "quality_score": 0,
                "has_data_evidence": False,
                "invalid_reason": "disclaimer",
            })
            index, _summary = chart.build_index(
                [candidate],
                state={"schema_version": 1, "items": {}},
                previous_index=previous,
                state_path=workspace / "state.json",
                asset_output_dir=workspace / "assets",
                analyze=lambda _path: rejected,
                max_model_calls=20,
            )
            self.assertEqual(index["item_count"], 0)
            self.assertEqual(index["report_count"], 0)

    def test_repeatedly_bad_image_is_quarantined_without_blocking_the_index(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            reports = workspace / "260809"
            write_report(reports, "report_a", "Unreadable Chart")
            candidates = chart.discover_candidates(reports, {}, date_folder="260809")
            state = {"schema_version": 1, "items": {}}
            previous = {"schema_version": 1, "reports": []}

            def fail(_path: Path) -> dict:
                raise chart.StableImageError("fixture image cannot be decoded")

            for attempt_run_id in ("run-1", "run-2", "run-3"):
                previous, summary = chart.build_index(
                    candidates,
                    state=state,
                    previous_index=previous,
                    state_path=workspace / "state.json",
                    asset_output_dir=workspace / "assets",
                    analyze=fail,
                    max_model_calls=20,
                    retry_errors_now=True,
                    attempt_run_id=attempt_run_id,
                )
            self.assertEqual(summary["quarantined_count"], 1)
            self.assertEqual(summary["retryable_count"], 0)
            self.assertEqual(next(iter(state["items"].values()))["status"], "quarantined")
            self.assertEqual(next(iter(state["items"].values()))["stable_attempt_runs"], 3)

            def must_not_retry(_path: Path) -> dict:
                raise AssertionError("quarantined image was retried")

            _index, skipped = chart.build_index(
                candidates,
                state=state,
                previous_index=previous,
                state_path=workspace / "state.json",
                asset_output_dir=workspace / "assets",
                analyze=must_not_retry,
                max_model_calls=20,
            )
            self.assertEqual(skipped["model_calls"], 0)
            self.assertEqual(skipped["quarantined_count"], 1)

    def test_stable_image_failure_counts_only_once_per_workflow_run(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            reports = workspace / "260809"
            write_report(reports, "report_a", "Unreadable Chart")
            candidates = chart.discover_candidates(reports, {}, date_folder="260809")
            state = {"schema_version": 1, "items": {}}

            def fail(_path: Path) -> dict:
                raise chart.StableImageError("fixture image cannot be decoded")

            for _batch in range(5):
                _index, summary = chart.build_index(
                    candidates,
                    state=state,
                    previous_index={"schema_version": 1, "reports": []},
                    state_path=workspace / "state.json",
                    asset_output_dir=workspace / "assets",
                    analyze=fail,
                    max_model_calls=20,
                    retry_errors_now=True,
                    attempt_run_id="same-run",
                )
            record = next(iter(state["items"].values()))
            self.assertEqual(record["status"], "error")
            self.assertEqual(record["stable_attempt_runs"], 1)
            self.assertEqual(summary["model_calls"], 0)

    def test_distinct_recovery_attempt_retries_transient_checkpoint(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            reports = workspace / "260809"
            write_report(reports, "report_a", "Recoverable Chart")
            candidates = chart.discover_candidates(reports, {}, date_folder="260809")
            state = {"schema_version": 1, "items": {}}
            previous = {"schema_version": 1, "reports": []}
            calls = 0

            def transient_then_success(_path: Path) -> dict:
                nonlocal calls
                calls += 1
                if calls == 1:
                    raise chart.RetryableVisionError(
                        "fixture malformed model output",
                        reason="model_json",
                    )
                return sample_analysis()

            previous, first = chart.build_index(
                candidates,
                state=state,
                previous_index=previous,
                state_path=workspace / "state.json",
                asset_output_dir=workspace / "assets",
                analyze=transient_then_success,
                max_model_calls=1,
                attempt_run_id="run:1",
            )
            self.assertEqual(first["retryable_count"], 1)
            self.assertEqual(first["retryable_reasons"], {"model_json": 1})

            previous, suppressed = chart.build_index(
                candidates,
                state=state,
                previous_index=previous,
                state_path=workspace / "state.json",
                asset_output_dir=workspace / "assets",
                analyze=transient_then_success,
                max_model_calls=1,
                retry_errors_now=True,
                attempt_run_id="run:1",
            )
            self.assertEqual(suppressed["model_calls"], 0)
            self.assertEqual(suppressed["retryable_count"], 1)

            recovered_index, recovered = chart.build_index(
                candidates,
                state=state,
                previous_index=previous,
                state_path=workspace / "state.json",
                asset_output_dir=workspace / "assets",
                analyze=transient_then_success,
                max_model_calls=1,
                retry_errors_now=True,
                attempt_run_id="run:1:recovery-1",
            )
            self.assertEqual(calls, 2)
            self.assertEqual(recovered["model_calls"], 1)
            self.assertEqual(recovered["retryable_count"], 0)
            self.assertEqual(recovered_index["item_count"], 1)

    def test_global_transient_failures_open_circuit_without_quarantine(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            reports = workspace / "260809"
            write_report(reports, "report_a", "Alpha", "white")
            write_report(reports, "report_b", "Beta", "gray")
            write_report(reports, "report_c", "Gamma", "yellow")
            write_report(reports, "report_d", "Delta", "pink")
            candidates = chart.discover_candidates(reports, {}, date_folder="260809")
            state = {"schema_version": 1, "items": {}}
            state_path = workspace / "state.json"

            def unavailable(_path: Path) -> dict:
                raise chart.RetryableVisionError("fixture service outage")

            with self.assertRaises(chart.VisionCircuitOpen):
                chart.build_index(
                    candidates,
                    state=state,
                    previous_index={"schema_version": 1, "reports": []},
                    state_path=state_path,
                    asset_output_dir=workspace / "assets",
                    analyze=unavailable,
                    max_model_calls=20,
                    attempt_run_id="outage-run",
                    circuit_breaker_threshold=3,
                )
            persisted = json.loads(state_path.read_text(encoding="utf-8"))
            records = list(persisted["items"].values())
            self.assertEqual(len(records), 3)
            self.assertTrue(all(record["status"] == "error" for record in records))
            self.assertTrue(all(record["failure_class"] == "transient" for record in records))
            self.assertEqual(persisted["circuit_breaker"]["consecutive_transient_failures"], 3)

    def test_transient_failures_never_quarantine_across_runs(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            reports = workspace / "260809"
            write_report(reports, "report_a", "Retry Later")
            candidates = chart.discover_candidates(reports, {}, date_folder="260809")
            state = {"schema_version": 1, "items": {}}
            private_sentinel = "https://private.invalid response-body fake-key"

            def unavailable(_path: Path) -> dict:
                raise chart.RetryableVisionError(private_sentinel)

            for run_id in ("run-1", "run-2", "run-3", "run-4"):
                _index, summary = chart.build_index(
                    candidates,
                    state=state,
                    previous_index={"schema_version": 1, "reports": []},
                    state_path=workspace / "state.json",
                    asset_output_dir=workspace / "assets",
                    analyze=unavailable,
                    max_model_calls=20,
                    retry_errors_now=True,
                    attempt_run_id=run_id,
                    circuit_breaker_threshold=3,
                )
            record = next(iter(state["items"].values()))
            self.assertEqual(record["status"], "error")
            self.assertEqual(record["failure_class"], "transient")
            self.assertEqual(record["failure_reason"], "other")
            self.assertEqual(summary["retryable_count"], 1)
            self.assertEqual(summary["retryable_reasons"], {"other": 1})
            self.assertNotIn(
                private_sentinel,
                json.dumps({"state": state, "summary": summary}, ensure_ascii=False),
            )

    def test_retryable_reason_codes_are_provider_neutral(self) -> None:
        fixtures = {
            "transport",
            "http_transient",
            "http_unexpected",
            "response_json",
            "no_choices",
            "model_json",
            "other",
        }
        for reason in fixtures:
            with self.subTest(reason=reason):
                self.assertEqual(
                    chart.retryable_reason_code(
                        chart.RetryableVisionError("private detail", reason=reason)
                    ),
                    reason,
                )
        invalid = chart.RetryableVisionError("private detail", reason="https://private.invalid")
        self.assertEqual(chart.retryable_reason_code(invalid), "other")
        self.assertEqual(chart.retryable_reason_code(ValueError("private detail")), "other")

    def test_replacement_date_removes_only_stale_same_date_reports(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            reports = workspace / "260809"
            write_report(reports, "report_a", "Replacement Report")
            candidates = chart.discover_candidates(reports, {}, date_folder="260809")
            canonical_ref = candidates[0].report_ref
            previous = {
                "schema_version": 1,
                "reports": [
                    {
                        "report_ref": "stale-same-date",
                        "title": "Stale",
                        "date_folder": "260809",
                        "charts": [],
                    },
                    {
                        "report_ref": "older-date",
                        "title": "Older",
                        "date_folder": "260808",
                        "charts": [{"id": "older-chart", "ordinal": 1, **sample_analysis()}],
                    },
                ],
            }
            index, summary = chart.build_index(
                candidates,
                state={"schema_version": 1, "items": {}},
                previous_index=previous,
                state_path=workspace / "state.json",
                asset_output_dir=workspace / "assets",
                analyze=lambda _path: sample_analysis(),
                max_model_calls=20,
                replace_date_folder="260809",
            )
            refs = {report["report_ref"] for report in index["reports"]}
            self.assertEqual(refs, {"older-date", canonical_ref})
            self.assertEqual(summary["replaced_report_count"], 1)

    def test_replacement_date_requires_candidates(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            workspace = Path(temp)
            with self.assertRaisesRegex(RuntimeError, "has no chart candidates"):
                chart.build_index(
                    [],
                    state={"schema_version": 1, "items": {}},
                    previous_index={"schema_version": 1, "reports": []},
                    state_path=workspace / "state.json",
                    asset_output_dir=workspace / "assets",
                    analyze=lambda _path: sample_analysis(),
                    max_model_calls=20,
                    replace_date_folder="260809",
                )

    def test_authentication_error_fails_immediately_without_retry(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            image_path = Path(temp) / "image.png"
            write_image(image_path)
            response = Mock()
            response.status_code = 401
            response.headers = {}
            response.json.return_value = {"error": {"message": "unauthorized"}}
            client = chart.VisionClient(
                api_base="https://vision.example.invalid/v1",
                api_key="fixture",
                model="fixture-model",
                timeout=5,
                retries=4,
                retry_backoff=0.1,
                min_interval=0,
            )
            client.session = Mock()
            client.session.post.return_value = response
            with self.assertRaises(chart.VisionConfigurationError):
                client.analyze(image_path)
            self.assertEqual(client.session.post.call_count, 1)

    def test_server_invalid_json_and_throttling_are_retryable(self) -> None:
        invalid = Mock()
        invalid.status_code = 200
        invalid.headers = {}
        invalid.json.side_effect = ValueError("invalid JSON")
        throttled = Mock()
        throttled.status_code = 429
        throttled.headers = {}
        throttled.json.return_value = {"error": {"message": "busy"}}
        throttled_error = chart.classify_http_error(throttled)
        self.assertIsInstance(throttled_error, chart.RetryableVisionError)
        self.assertEqual(chart.retryable_reason_code(throttled_error), "http_transient")

        with tempfile.TemporaryDirectory() as temp:
            image_path = Path(temp) / "image.png"
            write_image(image_path)
            client = chart.VisionClient(
                api_base="https://vision.example.invalid/v1",
                api_key="fixture",
                model="fixture-model",
                timeout=5,
                retries=1,
                retry_backoff=0.1,
                min_interval=0,
            )
            client.session = Mock()
            client.session.post.return_value = invalid
            with self.assertRaises(chart.RetryableVisionError) as caught:
                client.analyze(image_path)
            self.assertEqual(chart.retryable_reason_code(caught.exception), "response_json")

    def test_structured_output_request_has_no_truncating_token_cap(self) -> None:
        response = Mock()
        response.status_code = 200
        response.headers = {}
        response.json.return_value = {
            "choices": [{"message": {"content": json.dumps(sample_analysis())}}]
        }
        with tempfile.TemporaryDirectory() as temp:
            image_path = Path(temp) / "image.png"
            write_image(image_path)
            client = chart.VisionClient(
                api_base="https://vision.example.invalid/v1",
                api_key="fixture",
                model="fixture-model",
                timeout=5,
                retries=1,
                retry_backoff=0.1,
                min_interval=0,
            )
            client.session = Mock()
            client.session.post.return_value = response

            analysis = client.analyze(image_path)

        request_payload = client.session.post.call_args.kwargs["json"]
        self.assertEqual(request_payload["response_format"], {"type": "json_object"})
        self.assertTrue(
            {"max_tokens", "max_completion_tokens"}.isdisjoint(request_payload)
        )
        self.assertTrue(analysis["is_chart"])

    def test_malformed_choice_is_retried_as_model_json(self) -> None:
        malformed = Mock()
        malformed.status_code = 200
        malformed.headers = {}
        malformed.json.return_value = {"choices": ["private model output"]}
        with tempfile.TemporaryDirectory() as temp:
            image_path = Path(temp) / "image.png"
            write_image(image_path)
            client = chart.VisionClient(
                api_base="https://vision.example.invalid/v1",
                api_key="fixture",
                model="fixture-model",
                timeout=5,
                retries=2,
                retry_backoff=0.001,
                min_interval=0,
            )
            client.session = Mock()
            client.session.post.return_value = malformed
            with patch.object(chart.time, "sleep") as sleep:
                with self.assertRaises(chart.RetryableVisionError) as caught:
                    client.analyze(image_path)
            self.assertEqual(client.session.post.call_count, 2)
            self.assertEqual(sleep.call_count, 1)
            self.assertEqual(chart.retryable_reason_code(caught.exception), "model_json")

    def test_private_state_checkpoint_can_publish_without_public_index(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            state_path = Path(temp) / "state.json"
            state_path.write_text(json.dumps({
                "schema_version": 1,
                "analysis_version": "chart-search-v1",
                "items": {"a" * 64: {"status": "error"}},
            }), encoding="utf-8")

            class FakeClient:
                def __init__(self) -> None:
                    self.calls = []

                def put_object(self, **kwargs) -> None:
                    self.calls.append(kwargs)

            client = FakeClient()
            args = SimpleNamespace(prefix="_chart-search/v1", state=str(state_path))
            with patch.object(r2, "client_and_bucket", return_value=(client, "private-bucket")):
                self.assertEqual(r2.command_publish_state(args), 0)
            self.assertEqual(len(client.calls), 1)
            self.assertEqual(client.calls[0]["Key"], "_chart-search/v1/state.json")
            self.assertEqual(client.calls[0]["CacheControl"], "private, no-store")

    def test_chart_storage_budget_evicts_unreferenced_then_oldest(self) -> None:
        old_id = "a" * 64
        new_id = "b" * 64
        orphan_id = "c" * 64
        index = {
            "schema_version": 1,
            "reports": [
                {
                    "report_ref": "old",
                    "report_id": "old-report",
                    "title": "Old report",
                    "date_folder": "260801",
                    "chart_count": 1,
                    "charts": [{**chart.chart_record(
                        SimpleNamespace(
                            report_ref="old", image_sha256=old_id, ordinal=1,
                        ),
                        chart.normalize_analysis(sample_analysis()),
                    )}],
                },
                {
                    "report_ref": "new",
                    "report_id": "new-report",
                    "title": "New report",
                    "date_folder": "260803",
                    "chart_count": 1,
                    "charts": [{**chart.chart_record(
                        SimpleNamespace(
                            report_ref="new", image_sha256=new_id, ordinal=1,
                        ),
                        chart.normalize_analysis(sample_analysis()),
                    )}],
                },
            ],
        }
        index["report_count"] = 2
        index["item_count"] = 2

        class FakeClient:
            def __init__(self) -> None:
                timestamp = datetime(2026, 8, 1, tzinfo=timezone.utc)
                self.rows = [
                    {"Key": "_chart-search/v1/state.json", "Size": 5, "LastModified": timestamp},
                    {"Key": "_chart-search/v1/index.json", "Size": 999, "LastModified": timestamp},
                    {"Key": f"_chart-search/v1/images/{old_id}.jpg", "Size": 10, "LastModified": timestamp},
                    {"Key": f"_chart-search/v1/images/{new_id}.jpg", "Size": 10, "LastModified": timestamp},
                    {"Key": f"_chart-search/v1/images/{orphan_id}.jpg", "Size": 4, "LastModified": timestamp},
                ]
                self.deleted: list[str] = []

            def list_objects_v2(self, **_kwargs):
                return {"Contents": list(self.rows), "IsTruncated": False}

            def delete_objects(self, **kwargs):
                keys = [row["Key"] for row in kwargs["Delete"]["Objects"]]
                self.deleted.extend(keys)
                self.rows = [row for row in self.rows if row["Key"] not in keys]

        client = FakeClient()
        r2.filter_index_images(index, {old_id, new_id})
        budget = r2.pretty_json_size(index) + 5 + 10
        result = r2.enforce_storage_budget(
            client,
            "private-bucket",
            "_chart-search/v1",
            index,
            budget_bytes=budget,
        )
        self.assertEqual(result["images_retained"], 1)
        self.assertEqual(result["images_evicted"], 2)
        self.assertEqual(index["item_count"], 1)
        self.assertEqual(index["reports"][0]["report_id"], "new-report")
        self.assertIn(f"_chart-search/v1/images/{old_id}.jpg", client.deleted)
        self.assertIn(f"_chart-search/v1/images/{orphan_id}.jpg", client.deleted)
        self.assertNotIn(f"_chart-search/v1/images/{new_id}.jpg", client.deleted)

    def test_publish_filter_drops_every_legacy_v1_chart(self) -> None:
        v1_id = "e" * 64
        v2_id = "f" * 64
        index = {
            "schema_version": 1,
            "reports": [{
                "report_ref": "mixed",
                "report_id": "mixed-report",
                "title": "Mixed report",
                "date_folder": "260811",
                "chart_count": 2,
                "charts": [
                    {
                        **chart.chart_record(
                            SimpleNamespace(report_ref="mixed", image_sha256=v1_id, ordinal=1),
                            chart.normalize_analysis(sample_analysis()),
                        ),
                        "analysis_version": "chart-search-v1",
                    },
                    chart.chart_record(
                        SimpleNamespace(report_ref="mixed", image_sha256=v2_id, ordinal=2),
                        chart.normalize_analysis(sample_analysis()),
                    ),
                ],
            }],
        }
        removed = r2.filter_index_images(index, {v1_id, v2_id})
        self.assertEqual(removed, 1)
        self.assertEqual(index["item_count"], 1)
        self.assertEqual(index["reports"][0]["charts"][0]["analysis_version"], "chart-search-v2")

    def test_merge_adds_chart_terms_idempotently(self) -> None:
        search = {
            "schema_version": 1,
            "items": [{"id": "report-alpha", "text": "existing report words"}],
            "sources": {},
        }
        charts = {
            "schema_version": 1,
            "reports": [{
                "report_id": "report-alpha",
                "chart_count": 2,
                "search_text": "MLCC shipments 2026 上升",
            }],
        }
        first = merge.merge_indexes(search, charts)
        merge.merge_indexes(search, charts)
        self.assertEqual(first["chart_matched"], 1)
        self.assertEqual(search["items"][0]["text"].count(merge.MARKER.strip()), 1)
        self.assertIn("MLCC shipments", search["items"][0]["text"])

    def test_merge_reconciles_missing_report_id_from_fresh_catalog(self) -> None:
        charts = {
            "schema_version": 1,
            "reports": [{"report_id": "", "title": "Alpha MLCC Outlook", "charts": []}],
        }
        catalog = {"items": [{
            "id": "report-alpha",
            "title": "Alpha-MLCC_Outlook.pdf",
            "bank_name": "Bernstein",
            "available": False,
            "pdf_archived": True,
            "size_bytes": 1234,
            "page_count": 27,
        }]}
        self.assertEqual(merge.reconcile_report_ids(charts, catalog), 1)
        self.assertEqual(charts["reports"][0]["report_id"], "report-alpha")
        self.assertEqual(charts["reports"][0]["bank_name"], "Bernstein")
        self.assertIs(charts["reports"][0]["available"], False)
        self.assertIs(charts["reports"][0]["pdf_archived"], True)
        self.assertEqual(charts["reports"][0]["page_count"], 27)

    def test_merge_only_publishes_pdf_state_grounded_in_the_current_catalog(self) -> None:
        charts = {
            "schema_version": 1,
            "reports": [
                {"report_id": "known", "title": "Known", "available": True, "charts": []},
                {"report_id": "missing", "title": "Missing", "available": True, "pdf_archived": False, "charts": []},
            ],
        }
        catalog = {"items": [{"id": "known", "title": "Known", "available": False}]}
        self.assertEqual(merge.reconcile_report_ids(charts, catalog), 0)
        self.assertIs(charts["reports"][0]["available"], False)
        self.assertNotIn("pdf_archived", charts["reports"][0])
        self.assertNotIn("available", charts["reports"][1])
        self.assertNotIn("pdf_archived", charts["reports"][1])

    def test_merge_command_publishes_reconciled_chart_ids(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            search_path = root / "search.json"
            chart_path = root / "charts.json"
            catalog_path = root / "catalog.json"
            output_path = root / "published.json"
            search_path.write_text(json.dumps({"items": [{"id": "report-alpha", "text": "base"}]}), encoding="utf-8")
            chart_path.write_text(json.dumps({
                "schema_version": 1,
                "reports": [{
                    "report_id": "",
                    "title": "Alpha MLCC Outlook",
                    "chart_count": 1,
                    "search_text": "MLCC shipments",
                    "charts": [],
                }],
            }), encoding="utf-8")
            catalog_path.write_text(json.dumps({
                "items": [{
                    "id": "report-alpha",
                    "title": "Alpha-MLCC_Outlook.pdf",
                    "available": False,
                    "page_count": 18,
                }],
            }), encoding="utf-8")
            argv = [
                "merge_chart_search_index.py",
                "--search-index", str(search_path),
                "--chart-index", str(chart_path),
                "--catalog", str(catalog_path),
                "--chart-output", str(output_path),
            ]
            with patch.object(sys, "argv", argv):
                self.assertEqual(merge.main(), 0)
            published = json.loads(output_path.read_text(encoding="utf-8"))
            self.assertEqual(published["reports"][0]["report_id"], "report-alpha")
            self.assertIs(published["reports"][0]["available"], False)
            self.assertEqual(published["reports"][0]["page_count"], 18)

    def test_title_matching_tolerates_sequence_bank_alias_and_trailing_date(self) -> None:
        catalog = {"items": [{
            "id": "report-alpha",
            "title": "GS India Financials Metrics that matter",
        }]}
        lookup_path = None
        with tempfile.TemporaryDirectory() as temp:
            lookup_path = Path(temp) / "catalog.json"
            lookup_path.write_text(json.dumps(catalog), encoding="utf-8")
            lookup = chart.load_catalog_lookup(lookup_path)
            report_id, _title = chart.match_catalog_report(
                "0001-06-Goldman Sachs India Financials Metrics that matter 260808.pdf",
                lookup,
            )
        self.assertEqual(report_id, "report-alpha")

    def test_api_and_r2_paths_reject_unsafe_configuration(self) -> None:
        self.assertEqual(
            chart.validate_api_base("https://vision.example.invalid/v1"),
            "https://vision.example.invalid/v1/chat/completions",
        )
        with self.assertRaises(RuntimeError):
            chart.validate_api_base("http://vision.example.invalid/v1")
        with self.assertRaises(RuntimeError):
            chart.validate_api_base("https://user:secret@vision.example.invalid/v1")
        with self.assertRaises(RuntimeError):
            r2.validate_prefix("../chart")

    def test_workflow_has_bounded_same_job_transient_recovery(self) -> None:
        workflow = (ROOT / ".github/workflows/portal-chart-search-index.yml").read_text(
            encoding="utf-8"
        )
        recovery = workflow.index("Retrying $CALL_LIMIT transient chart checkpoint(s)")
        strict_gate = workflow.index('if [ "$RETRYABLE" != "0" ]')
        public_publish = workflow.index("- name: Publish checkpoint and searchable index")

        self.assertIn(
            "VISION_INDEX_TRANSIENT_RECOVERY_ROUNDS || '1'",
            workflow,
        )
        self.assertIn(
            '"${GITHUB_RUN_ID}:${GITHUB_RUN_ATTEMPT}:recovery-${RECOVERY_ROUND}"',
            workflow,
        )
        self.assertIn('[ "$STABLE_ERRORS" = "0" ]', workflow)
        self.assertIn(
            'if [ "$STABLE_ERRORS" != "0" ] || [ "$UNPROCESSED" != "0" ]; then break; fi',
            workflow,
        )
        self.assertLess(recovery, strict_gate)
        self.assertLess(strict_gate, public_publish)


if __name__ == "__main__":
    unittest.main()
