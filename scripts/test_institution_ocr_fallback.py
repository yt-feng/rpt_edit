"""Provider-only OCR continuation retains exact source/page and handoff identities."""
from __future__ import annotations

import copy
import json
import os
from pathlib import Path
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
import fitz
from unittest.mock import patch

import institution_dependency_backlog as backlog
import institution_ocr_fallback as ocr
import pdf_to_xhs_batch as producer
from report_extraction_source import digest, ocr_markdown_from_pages, resolve_extraction_source
import run_pdf_to_xhs_in_batches as wrapper


def pages(_pdf=None, **_kwargs):
    text = "Revenue was 10 million. Three companies reported shorter delivery times."
    return [{"page": 1, "method": "ocr", "text": text,
             "text_sha256": digest(text.encode()), "empty_text": False}]


class InstitutionOcrTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.inputs = self.root / "pdfs"
        self.inputs.mkdir()
        self.output = self.root / "out"
        self.output.mkdir()
        self.bindings = {}
        for number in range(1, 4):
            path = self.inputs / f"{number:04d}-WorldBank-report-{number}.pdf"
            with fitz.open() as document:
                page = document.new_page()
                page.insert_text((40, 60), f'Original research report {number}, text only.')
                document.save(path)
            self.bindings[path.name] = {"source": f"WorldBank-report-{number}.pdf",
                "sha256": digest(path.read_bytes()), "size": path.stat().st_size}
        self.inventory = {"schema": 1, "sources": list(self.bindings.values()), "deferred_sources": 0}

    def run_worker(self, command, **kwargs):
        self.assertLessEqual(kwargs["timeout"], 600)
        request = json.loads(Path(command[-1]).read_bytes())
        ocr.extract_source(Path(request["pdf"]), Path(request["output"]), request["binding"], reader=pages)
        return SimpleNamespace(returncode=0)

    def recover(self, inventory=None, runner=None):
        return ocr.recover_batch(inventory or self.inventory, self.bindings,
                                 self.inputs, self.output, runner=runner or self.run_worker)

    def test_pages_and_provenance_continue_to_discovery_and_exact_translated_handoff(self):
        result = self.recover()
        self.assertEqual((result["ocr_reports"], result["failed_reports"]), (3, 0))
        self.assertEqual(wrapper.count_generated_report_dirs(self.output, chart_source_only=True), 3)
        import build_portal_translated_reports as builder
        directories = builder.find_report_dirs(self.output)
        self.assertEqual(len(directories), 3)
        translated = self.root / "translated"
        translated.mkdir()
        rows = []
        for number, directory in enumerate(directories):
            source = resolve_extraction_source(directory)
            self.assertEqual(source.method, "ocr")
            self.assertFalse((directory / "source_mineru.md").exists())
            output = translated / str(number)
            output.mkdir()
            pdf = output / "translated.pdf"
            pdf.write_bytes(b"%PDF-fixture")
            rows.append({"source_report_dir": str(directory), "output_dir": str(output),
                         "pdf_path": str(pdf), **source.identity()})
        summary = {"failures": 0, "selected_count": 3, "successful_count": 3, "reports": rows}
        path = translated / "translation_summary.json"
        path.write_text(json.dumps(summary))
        self.assertEqual(backlog.verify_handoff(self.output, translated), 3)
        rows[0]["source_method"] = "mineru"
        path.write_text(json.dumps(summary))
        with self.assertRaisesRegex(Exception, "OCR provenance mismatch"):
            backlog.verify_handoff(self.output, translated)

    def test_healthy_mineru_source_reused_and_held_source_never_ocrd(self):
        name, binding = next(iter(self.bindings.items()))
        directory = self.output / wrapper.slug(name)
        directory.mkdir()
        (directory / "source_mineru.md").write_text("Original MinerU text is retained.")
        (directory / "status.json").write_text(json.dumps({"source_pdf": name,
            "original_pdf_sha256": binding["sha256"], "chart_source_only": True}))
        inventory = {"schema": 1, "sources": list(self.bindings.values())[:2], "deferred_sources": 1}
        with patch.object(ocr.subprocess, "run", side_effect=self.run_worker) as calls:
            result = self.recover(inventory, runner=calls)
        self.assertEqual((result["ocr_reports"], result["reused_reports"], result["deferred_sources"]), (1, 1, 1))
        self.assertEqual(calls.call_count, 1)
        self.assertEqual((directory / "source_mineru.md").read_text(), "Original MinerU text is retained.")
        self.assertFalse((directory / "source_ocr.md").exists())
        self.assertFalse((self.output / wrapper.slug(list(self.bindings)[2])).exists())

    def test_original_vector_chart_survives_institution_ocr_continuation(self):
        from test_original_pdf_figures import chart_pdf
        from wechat_image_quality import source_chart_images
        name, _ = next(iter(self.bindings.items()))
        pdf, _ = chart_pdf(1); path = self.inputs / name; path.write_bytes(pdf)
        binding = {'source': 'WorldBank-report-1.pdf', 'size': len(pdf), 'sha256': digest(pdf)}
        directory = self.output / 'with-original-chart'
        ocr.extract_source(path, directory, binding, reader=pages)
        self.assertTrue(ocr.existing_source(directory, name, binding))
        self.assertEqual(resolve_extraction_source(directory).method, 'ocr')
        self.assertEqual(len(source_chart_images(directory, require_verified=True)), 1)
        import build_portal_translated_reports as translation
        clean, images = translation.prepare_clean_markdown(directory, self.root / 'translation', max_images=3)
        self.assertEqual(len(images), 1)
        self.assertEqual(images[0]['source_kind'], 'ocr_original')
        self.assertIn('[[PORTAL_IMAGE_001]]', clean)

    def rejected_source(self):
        name, binding = next(iter(self.bindings.items()))
        directory = self.output / wrapper.slug(name)
        directory.mkdir()
        (directory / "source_mineru.md").write_text("Premature rejected MinerU marker.")
        (directory / "mineru_raw").mkdir()
        (directory / "mineru_raw" / "middle.json").write_text("rejected metadata")
        (directory / "assets").mkdir()
        (directory / "assets" / "source_image_01.png").write_bytes(b"rejected image")
        (directory / "status.json").write_text(json.dumps({"source_pdf": name,
            "original_pdf_sha256": binding["sha256"], "error": "figure_metadata_invalid",
            "mineru_figure_failure_category": "figure_metadata_invalid"}))
        return directory, name, binding

    def test_rejected_metadata_uses_independent_ocr_and_discards_premature_mineru_assets(self):
        directory, name, binding = self.rejected_source()
        with self.assertRaisesRegex(ValueError, "existing_source_mismatch"):
            ocr.existing_source(directory, name, binding)
        result = self.recover()
        self.assertEqual((result["ocr_reports"], result["reused_reports"], result["failed_reports"]), (3, 0, 0))
        self.assertEqual(resolve_extraction_source(directory).method, "ocr")
        self.assertTrue(ocr.existing_source(directory, name, binding))
        self.assertEqual({path.name for path in directory.iterdir()},
                         {"source_ocr.md", "source_ocr_pages.json", "status.json", ocr.RECEIPT,
                          "source_original_figures.json", "source_image_map.json"})

    def test_failed_ocr_keeps_rejected_source_closed_and_never_exposes_partial_ocr(self):
        directory, name, binding = self.rejected_source()
        original_status = (directory / "status.json").read_bytes()
        def timeout(command, **kwargs):
            request = json.loads(Path(command[-1]).read_bytes())
            stage = Path(request["output"])
            stage.mkdir()
            (stage / "source_ocr.md").write_text("Incomplete OCR must remain isolated.")
            raise subprocess.TimeoutExpired(command, kwargs["timeout"])
        result = self.recover(runner=timeout)
        self.assertEqual(result["failed_reports"], 3)
        self.assertEqual((directory / "status.json").read_bytes(), original_status)
        self.assertFalse(list(self.output.rglob("source_ocr.md")))
        with self.assertRaisesRegex(ValueError, "existing_source_mismatch"):
            ocr.existing_source(directory, name, binding)

    def test_metadata_fallback_rejects_changed_binding_integrity_failure_and_mixed_markers(self):
        directory, name, binding = self.rejected_source()
        baseline = json.loads((directory / "status.json").read_bytes())
        for change in ({"source_pdf": "different.pdf"}, {"original_pdf_sha256": "a" * 64},
                       {"mineru_figure_failure_category": "figure_source_binding_mismatch"}):
            (directory / "status.json").write_text(json.dumps(dict(baseline, **change)))
            with self.subTest(change=change), patch.object(ocr.subprocess, "run") as worker:
                with self.assertRaises(ValueError):
                    self.recover(runner=worker)
                worker.assert_not_called()
        (directory / "status.json").write_text(json.dumps(baseline))
        (directory / "source_ocr.md").write_text("A stale mixed source must stop recovery.")
        with patch.object(ocr.subprocess, "run") as worker, self.assertRaises(ValueError):
            self.recover(runner=worker)
        worker.assert_not_called()

    def test_changed_page_evidence_cannot_keep_the_original_receipt(self):
        self.recover()
        name, binding = next(iter(self.bindings.items()))
        directory = self.output / wrapper.slug(name)
        changed = pages()
        changed[0]["text"] = "Changed content."
        changed[0]["text_sha256"] = digest(changed[0]["text"].encode())
        raw = ocr.encoded(changed)
        (directory / "source_ocr_pages.json").write_bytes(raw)
        (directory / "source_ocr.md").write_bytes(ocr_markdown_from_pages(changed, 1))
        status_path = directory / "status.json"
        status = json.loads(status_path.read_bytes())
        status["wechat_source_provenance"]["source_pages_sha256"] = digest(raw)
        status_path.write_text(json.dumps(status))
        with self.assertRaisesRegex(ValueError, "receipt_mismatch"):
            ocr.existing_source(directory, name, binding)

    def test_private_handoff_preserves_page_receipts_without_original_pdfs(self):
        from private_workflow_handoff import create_archive, extract_archive
        self.recover()
        (self.output / "original.pdf").write_bytes(b"%PDF-not-an-output")
        archive = self.root / "extracted-sources.tar.gz"
        count, _size, _digest = create_archive(self.output, archive)
        self.assertEqual(count, 18)
        restored = self.root / "restored"
        extract_archive(archive, restored)
        for name, binding in self.bindings.items():
            self.assertTrue(ocr.existing_source(restored / wrapper.slug(name), name, binding))
        self.assertFalse((restored / "original.pdf").exists())

    def test_invalid_selection_or_changed_original_stops_before_any_worker(self):
        for mode in ("duplicate", "changed_hash", "missing_held", "unexpected_source"):
            value = copy.deepcopy(self.inventory)
            if mode == "duplicate":
                value["sources"][1] = value["sources"][0]
            elif mode == "changed_hash":
                value["sources"][0]["sha256"] = "a" * 64
            elif mode == "missing_held":
                value["sources"].pop()
            else:
                value["sources"][0]["source"] = "another-report.pdf"
            with self.subTest(mode=mode), patch.object(ocr.subprocess, "run") as worker:
                with self.assertRaises(ValueError):
                    self.recover(value, runner=worker)
                worker.assert_not_called()
        next(self.inputs.iterdir()).write_bytes(b"%PDF-changed")
        with patch.object(ocr.subprocess, "run") as worker, self.assertRaisesRegex(ValueError, "original_changed"):
            self.recover(runner=worker)
        worker.assert_not_called()

    def test_timeout_does_not_block_independent_sources_and_remains_a_failure(self):
        calls = []
        def worker(command, **kwargs):
            calls.append(command)
            if len(calls) == 1:
                raise subprocess.TimeoutExpired(command, kwargs["timeout"])
            return self.run_worker(command, **kwargs)
        result = self.recover(runner=worker)
        self.assertEqual((result["ocr_reports"], result["failed_reports"]), (2, 1))
        self.assertEqual(result["failures"][0]["category"], "ocr_timeout")

    def test_existing_ocr_is_reused_and_shared_budget_stops_new_work(self):
        with patch.object(ocr.subprocess, "run") as worker:
            result = ocr.recover_batch(self.inventory, self.bindings, self.inputs, self.output,
                                       runner=worker, deadline=0)
        worker.assert_not_called()
        self.assertEqual(result["failed_reports"], 3)
        self.assertEqual({failure["category"] for failure in result["failures"]}, {"ocr_time_budget_exhausted"})
        self.recover()
        with patch.object(ocr.subprocess, "run") as worker:
            result = self.recover(runner=worker)
        worker.assert_not_called()
        self.assertEqual(result["reused_reports"], 3)

    def test_wrapper_needs_opt_in_current_provider_marker_and_exact_inventory(self):
        args = producer.build_arg_parser().parse_args(["--chart-source-only"])
        args.input_dir, args.output_dir = str(self.inputs), str(self.output)
        args.institution_ocr_fallback = True
        for mode in ("disabled", "code_failure", "missing_inventory", "provider_failure"):
            args.institution_ocr_fallback = mode != "disabled"
            def child(command, outcome_path, **kwargs):
                inventory_path = (Path(command[command.index("--ocr-fallback-inventory-path") + 1])
                                  if "--ocr-fallback-inventory-path" in command else None)
                source_map = json.loads(Path(command[command.index("--mineru-source-map") + 1]).read_bytes())
                if mode != "code_failure":
                    outcome_path.write_text(json.dumps({"schema": 1, "category": "mineru_unavailable"}))
                if mode != "missing_inventory" and inventory_path:
                    inventory_path.write_text(json.dumps({"schema": 1,
                        "sources": list(source_map["files"].values()), "deferred_sources": 0}))
                return SimpleNamespace(returncode=2), 1
            with self.subTest(mode=mode), patch.object(wrapper, "run_pending_task_attempts", side_effect=child), \
                    patch.object(ocr, "recover_batch", return_value={"ocr_reports": 1, "reused_reports": 0,
                        "deferred_sources": 0, "failed_reports": 0, "failures": []}) as recover:
                result = wrapper.run_batch(1, [(1, next(self.inputs.iterdir()))], args)
            self.assertEqual(result["returncode"], 0 if mode == "provider_failure" else 2)
            self.assertEqual(recover.call_count, int(mode == "provider_failure"))

    def test_completed_pending_attempt_keeps_ocr_permission_when_next_poll_has_no_budget(self):
        args = producer.build_arg_parser().parse_args(["--chart-source-only"])
        args.input_dir, args.output_dir = str(self.inputs), str(self.output)
        args.institution_ocr_fallback = True
        args.pending_task_attempts, args.pending_task_retry_delay = 3, 2
        args._extraction_deadline = 10
        clock = [0]
        def child(command, **kwargs):
            self.assertEqual(kwargs["timeout"], 10)
            outcome = Path(command[command.index("--provider-outcome-path") + 1])
            inventory = Path(command[command.index("--ocr-fallback-inventory-path") + 1])
            source_map = json.loads(Path(command[command.index("--mineru-source-map") + 1]).read_bytes())
            outcome.write_text(json.dumps({"schema": 1, "category": "mineru_unavailable"}))
            inventory.write_text(json.dumps({"schema": 1, "sources": list(source_map["files"].values()),
                                              "deferred_sources": 0}))
            clock[0] = 10
            return SimpleNamespace(returncode=75)
        with patch.object(wrapper.subprocess, "run", side_effect=child) as calls, \
                patch.object(wrapper.time, "monotonic", side_effect=lambda: clock[0]), \
                patch.object(wrapper.time, "sleep"), \
                patch.object(ocr, "recover_batch", return_value={"ocr_reports": 1, "reused_reports": 0,
                    "deferred_sources": 0, "failed_reports": 0, "failures": []}) as recover:
            result = wrapper.run_batch(1, [(1, next(self.inputs.iterdir()))], args)
        self.assertEqual(calls.call_count, 1)
        recover.assert_called_once()
        self.assertEqual(result["returncode"], 0)
        self.assertEqual(result["mineru_returncode"], 75)
        self.assertEqual(result["pending_task_attempts"], 1)
        self.assertEqual(result["provider_failure_category"], "mineru_unavailable")

    def test_no_budget_at_invocation_start_cannot_reuse_stale_provider_permission(self):
        outcome = self.root / "stale-outcome.json"
        outcome.write_text(json.dumps({"schema": 1, "category": "mineru_unavailable"}))
        with patch.object(wrapper.subprocess, "run") as child, \
                patch.object(wrapper.time, "monotonic", return_value=10):
            result, attempts = wrapper.run_pending_task_attempts(
                ["new-source-command"], outcome, attempts=3, deadline=10)
        child.assert_not_called()
        self.assertEqual((result.returncode, attempts), (75, 0))
        self.assertFalse(outcome.exists())

    @unittest.skipUnless(os.environ.get("REQUIRE_MARKET_VIEWS_OCR_TESTS") == "1", "real OCR runs in cloud CI")
    def test_real_native_and_scanned_pages_feed_verified_institution_source(self):
        import fitz
        import build_portal_translated_reports as builder
        pdf = self.inputs / "0004-WorldBank-OCR.pdf"
        with fitz.open() as scan, fitz.open() as document:
            original = scan.new_page(width=600, height=400)
            original.insert_text((40, 100), "Revenue was 10 million in 2026.", fontsize=24)
            image = original.get_pixmap(dpi=180).tobytes("png")
            native = document.new_page(width=600, height=400)
            native.insert_textbox((40, 40, 550, 350), "The World Bank reports that delivery times decreased. " * 4, fontsize=16)
            scanned = document.new_page(width=600, height=400)
            scanned.insert_image(scanned.rect, stream=image)
            document.save(pdf)
        binding = {"source": "WorldBank-OCR.pdf", "sha256": digest(pdf.read_bytes()), "size": pdf.stat().st_size}
        directory = self.output / wrapper.slug(pdf.name)
        ocr.extract_source(pdf, directory, binding)
        source = resolve_extraction_source(directory)
        evidence = json.loads((directory / "source_ocr_pages.json").read_bytes())
        self.assertEqual([page["method"] for page in evidence], ["native", "ocr"])
        self.assertIn("Revenue", evidence[1]["text"])
        self.assertEqual(source.method, "ocr")
        self.assertEqual(builder.find_report_dirs(self.output), [directory])
        clean, _figures = builder.prepare_clean_markdown(directory, self.root / "clean", 0)
        self.assertIn("10 million", clean)


if __name__ == "__main__":
    unittest.main()
