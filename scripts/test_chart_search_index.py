#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
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

            def unavailable(_path: Path) -> dict:
                raise chart.RetryableVisionError("fixture service outage")

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
            self.assertEqual(summary["retryable_count"], 1)

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
        self.assertIsInstance(chart.classify_http_error(throttled), chart.RetryableVisionError)

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
            with self.assertRaises(chart.RetryableVisionError):
                client.analyze(image_path)

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
        catalog = {"items": [{"id": "report-alpha", "title": "Alpha-MLCC_Outlook.pdf"}]}
        self.assertEqual(merge.reconcile_report_ids(charts, catalog), 1)
        self.assertEqual(charts["reports"][0]["report_id"], "report-alpha")

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
                "items": [{"id": "report-alpha", "title": "Alpha-MLCC_Outlook.pdf"}],
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


if __name__ == "__main__":
    unittest.main()
