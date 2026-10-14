#!/usr/bin/env python3
"""Daily delivery accepts healthy siblings without claiming absent sources."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import tempfile
import unittest

import market_views_partial_sources as partial
from private_workflow_handoff import create_archive, extract_archive
from run_pdf_to_xhs_in_batches import unique_batch_name, slug


class PartialSourcesTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.manifest = self.root / "selected.json"
        self.originals = self.root / "originals"
        self.originals.mkdir()
        self.rows = []
        for index in range(1, 5):
            name = f"{index:02d}-Report-{index}.pdf"
            raw = f"%PDF original {index}".encode()
            (self.originals / name).write_bytes(raw)
            self.rows.append({"process_local_path": f"_selected_macro_pdfs/{name}",
                              "content_sha256": hashlib.sha256(raw).hexdigest()})
        self.manifest.write_text(json.dumps(self.rows))
        self.identity = dict(date_folder="261014", source_run_id="123456", source_execution_sha="a" * 40)
        self.downloads = self.root / "downloads"
        self.downloads.mkdir()

    def tearDown(self):
        self.temporary.cleanup()

    def _report(self, shard_index=0, ordinal=1, *, error=False, state="done", name_override=None):
        row = self.rows[shard_index * 2 + ordinal - 1]
        staged_name = unique_batch_name(Path(row["process_local_path"]), ordinal)
        shard = self.root / f"producer_{shard_index}"
        directory = shard / slug(staged_name)
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "assets").mkdir()
        (directory / "source_mineru.md").write_text("# Research\n" + "Evidence for the exact original source and market outlook. " * 12)
        (directory / "wechat_article.md").write_text("Accepted generated article. " * 15)
        (directory / "assets/source_image_01.png").write_bytes(b"bound original figure pixels")
        status = {"source_pdf": f"/tmp/batch/{name_override or staged_name}", "mineru_state": state,
                  "wechat_article": "wechat_article.md"}
        if error:
            status["error"] = "Report generation failed after parsing"
        (directory / "status.json").write_text(json.dumps(status))
        return shard, directory

    def _prepare(self, shard_index=0, *, originals=True, checkpoint=None):
        return partial.prepare_shard(self.manifest, self.root / f"producer_{shard_index}",
            self.downloads / f"shard_{shard_index}", shard_index=shard_index, reports_per_shard=2,
            originals_dir=self.originals if originals else None, checkpoint_identity=checkpoint, **self.identity)

    def _assemble(self):
        return partial.assemble_sources(self.manifest, self.downloads, self.root / "delivery",
                                         reports_per_shard=2, **self.identity)

    def test_healthy_report_survives_failed_sibling_and_missing_shard(self):
        self._report()
        prepared = self._prepare()
        self.assertEqual((4, 1, 3), tuple(prepared[key] for key in ("expected_reports", "included_reports", "skipped_reports")))
        receipt = self._assemble()
        self.assertEqual(1, receipt["included_reports"])
        self.assertFalse(receipt["complete_source_inventory"])
        self.assertEqual(3, len([row for row in receipt["reports"] if row["status"] == "skipped"]))
        partial.verify_delivery(self.root / "delivery", manifest=self.manifest, **self.identity)

    def test_generation_failure_retains_raw_source_and_chart_excludes_article(self):
        self._report(error=True)
        receipt = self._prepare()
        files = {row["path"] for row in receipt["files"]}
        self.assertTrue(any(name.endswith("source_mineru.md") for name in files))
        self.assertTrue(any(name.endswith("source_image_01.png") for name in files))
        self.assertFalse(any(name.endswith("wechat_article.md") for name in files))

    def test_pending_report_never_admitted(self):
        self._report(state="pending")
        self.assertEqual(0, self._prepare()["included_reports"])
        with self.assertRaisesRegex(ValueError, "no_usable_reports"):
            self._assemble()

    def test_unaccepted_generated_article_is_not_admitted_with_raw_source(self):
        _shard, directory = self._report()
        status = json.loads((directory / "status.json").read_text())
        status.pop("wechat_article")
        (directory / "status.json").write_text(json.dumps(status))
        receipt = self._prepare()
        self.assertEqual(1, receipt["included_reports"])
        self.assertFalse(any(row["path"].endswith("wechat_article.md") for row in receipt["files"]))

    def test_exact_batch_name_required_even_when_source_hash_matches(self):
        self._report(name_override="0001-99-Unrelated.pdf")
        self.assertEqual(0, self._prepare()["included_reports"])

    def test_changed_original_is_omitted(self):
        self._report()
        (self.originals / Path(self.rows[0]["process_local_path"]).name).write_bytes(b"changed bytes")
        self.assertEqual(0, self._prepare()["included_reports"])

    def test_source_hash_contradiction_is_omitted(self):
        _shard, directory = self._report()
        status = json.loads((directory / "status.json").read_text())
        status["original_pdf_sha256"] = "b" * 64
        (directory / "status.json").write_text(json.dumps(status))
        self.assertEqual(0, self._prepare()["included_reports"])

    def test_missing_originals_require_exact_checkpoint_identity(self):
        shard, _directory = self._report()
        (shard / "_generation_checkpoint.json").write_text(json.dumps({"version": 1, "identity": "c" * 64, "complete": False}))
        self.assertEqual(0, self._prepare(originals=False, checkpoint="d" * 64)["included_reports"])
        self.assertEqual(1, self._prepare(originals=False, checkpoint="c" * 64)["included_reports"])

    def test_unbound_status_hash_is_not_accepted_as_checkpoint(self):
        _shard, directory = self._report()
        status = json.loads((directory / "status.json").read_text())
        status["original_pdf_sha256"] = self.rows[0]["content_sha256"]
        (directory / "status.json").write_text(json.dumps(status))
        self.assertEqual(0, self._prepare(originals=False)["included_reports"])

    def test_corrupt_shard_does_not_block_healthy_other_shard(self):
        self._report(0)
        self._report(1)
        self._prepare(0)
        self._prepare(1)
        path = next((self.downloads / "shard_0").glob("*/source_mineru.md"))
        path.write_text("tampered")
        receipt = self._assemble()
        self.assertEqual(1, receipt["included_reports"])
        self.assertEqual(Path(self.rows[2]["process_local_path"]).name,
                         next(row["source_pdf"] for row in receipt["reports"] if row["status"] == "included"))

    def test_healthy_report_survives_corrupt_sibling_figure_proof(self):
        self._report(0, 1)
        _shard, broken = self._report(0, 2)
        (broken / "source_figure_map.json").write_text('{"invalid_proof": true}')
        prepared = self._prepare(0)
        self.assertEqual(1, prepared["included_reports"])
        self.assertEqual("included", prepared["reports"][0]["status"])
        self.assertEqual("skipped", prepared["reports"][1]["status"])
        self.assertEqual(1, self._assemble()["included_reports"])

    def test_cross_run_or_date_receipt_is_rejected(self):
        self._report()
        self._prepare()
        for identity in ({**self.identity, "source_run_id": "999"}, {**self.identity, "date_folder": "261013"},
                         {**self.identity, "source_execution_sha": "b" * 40}):
            with self.assertRaisesRegex(ValueError, "identity_mismatch"):
                partial.verify_delivery(self.downloads / "shard_0", **identity)

    def test_hash_inventory_rejects_extra_files_and_modified_assets(self):
        self._report()
        self._prepare()
        self._assemble()
        root = self.root / "delivery"
        (root / "extra.md").write_text("unbound material")
        with self.assertRaisesRegex(ValueError, "file_inventory_mismatch"):
            partial.verify_delivery(root, **self.identity)
        (root / "extra.md").unlink()
        path = next(root.glob("*/assets/source_image_01.png"))
        path.write_bytes(b"different chart")
        with self.assertRaisesRegex(ValueError, "file_hash_mismatch"):
            partial.verify_delivery(root, **self.identity)

    def test_symlinked_original_or_report_never_enters_receipt(self):
        _shard, directory = self._report()
        source = directory / "source_mineru.md"
        outside = self.root / "outside.md"
        source.rename(outside)
        source.symlink_to(outside)
        self.assertEqual(0, self._prepare()["included_reports"])

    def test_successful_full_inventory_does_not_include_raw_pdfs(self):
        for shard in (0, 1):
            for ordinal in (1, 2):
                _root, directory = self._report(shard, ordinal)
                (directory / "raw.pdf").write_bytes(b"private original")
                (directory / "mineru_raw").mkdir()
                (directory / "mineru_raw/source.md").write_text("raw private output")
            self._prepare(shard)
        receipt = self._assemble()
        self.assertTrue(receipt["complete_source_inventory"])
        self.assertEqual((4, 0), (receipt["included_reports"], receipt["skipped_reports"]))
        self.assertFalse(any(row["path"].endswith(".pdf") or "mineru_raw" in row["path"] for row in receipt["files"]))

    def test_legacy_requires_byte_identical_manifest_and_explicit_trusted_caller(self):
        shard, _directory = self._report()
        import shutil
        shutil.copytree(shard, self.downloads / "shard_0")
        legacy = self.downloads / "shard_0"
        (legacy / partial.MANIFEST_NAME).write_bytes(self.manifest.read_bytes())
        candidates, _ = partial.collect_candidates(self.manifest, self.downloads, reports_per_shard=2, **self.identity)
        self.assertFalse(candidates)
        candidates, _ = partial.collect_candidates(self.manifest, self.downloads, reports_per_shard=2,
                                                    allow_legacy=True, **self.identity)
        self.assertEqual(1, len(candidates))
        (legacy / partial.MANIFEST_NAME).write_text(json.dumps(self.rows, indent=2))
        candidates, _ = partial.collect_candidates(self.manifest, self.downloads, reports_per_shard=2,
                                                    allow_legacy=True, **self.identity)
        self.assertFalse(candidates)

    def test_fallback_candidate_merges_with_ready_mineru_report(self):
        self._report()
        self._prepare()
        candidates, reasons = partial.collect_candidates(self.manifest, self.downloads, reports_per_shard=2,
                                                          **self.identity)
        fallback = self.root / "fallback"
        fallback.mkdir()
        (fallback / "source_native_pdf.md").write_text("# Exact PDF excerpt\n" + "Substantive original evidence. " * 15)
        (fallback / "source_excerpt_evidence.json").write_text(json.dumps({
            "source_pdf": Path(self.rows[1]["process_local_path"]).name,
            "content_sha256": self.rows[1]["content_sha256"], "pages": [1]}))
        (fallback / "status.json").write_text(json.dumps({"original_pdf_sha256": self.rows[1]["content_sha256"]}))
        candidates[Path(self.rows[1]["process_local_path"]).name] = {
            "directory": fallback, "content_sha256": self.rows[1]["content_sha256"],
            "source_method": "source-digest", "files": ["source_native_pdf.md", "status.json", "source_excerpt_evidence.json"]}
        receipt = partial.write_delivery_receipt(self.manifest, self.root / "merged", candidates,
                                                 omission_reasons=reasons, **self.identity)
        self.assertEqual((2, 2), (receipt["included_reports"], receipt["skipped_reports"]))
        self.assertEqual(["mineru", "source-digest"], [row["source_method"] for row in receipt["reports"] if row["status"] == "included"])

    def test_new_receipts_self_describe_custom_shard_size(self):
        self._report(1)
        receipt = self._prepare(1)
        self.assertEqual((1, 2), (receipt["shard_index"], receipt["reports_per_shard"]))
        candidates, _ = partial.collect_candidates(self.manifest, self.downloads, **self.identity)
        self.assertEqual({Path(self.rows[2]["process_local_path"]).name}, set(candidates))
        candidates, _ = partial.collect_candidates(self.manifest, self.downloads, reports_per_shard=5, **self.identity)
        self.assertFalse(candidates)

    def test_legacy_unknown_shard_size_is_not_guessed(self):
        shard, _directory = self._report()
        import shutil
        shutil.copytree(shard, self.downloads / "shard_0")
        (self.downloads / "shard_0" / partial.MANIFEST_NAME).write_bytes(self.manifest.read_bytes())
        candidates, _ = partial.collect_candidates(self.manifest, self.downloads, allow_legacy=True, **self.identity)
        self.assertFalse(candidates)

    def test_unavailable_originals_remain_explicit_outside_hashed_inventory(self):
        for shard in (0, 1):
            for ordinal in (1, 2):
                self._report(shard, ordinal)
            self._prepare(shard)
        candidates, reasons = partial.collect_candidates(self.manifest, self.downloads, **self.identity)
        receipt = partial.write_delivery_receipt(self.manifest, self.root / "missing-original", candidates,
            unavailable_originals=[{"source_pdf": "Download-failed.pdf", "reason": "original_download_failed"}],
            omission_reasons=reasons, **self.identity)
        self.assertEqual((4, 5), (receipt["expected_reports"], receipt["expected_source_reports"]))
        self.assertEqual(0, receipt["skipped_reports"])
        self.assertFalse(receipt["complete_source_inventory"])
        for unavailable in ([{"source_pdf": "Download-failed.pdf", "reason": "Bad reason"}],
                            [{"source_pdf": Path(self.rows[0]["process_local_path"]).name, "reason": "failed"}]):
            with self.assertRaisesRegex(ValueError, "unavailable_source_invalid"):
                partial.write_delivery_receipt(self.manifest, self.root / "invalid", candidates,
                                                 unavailable_originals=unavailable, **self.identity)

    def test_real_archive_roundtrip_preserves_receipt_and_original_chart_bytes(self):
        self._report()
        self._prepare()
        self._assemble()
        archive = self.root / "payload.tar.gz"
        create_archive(self.root / "delivery", archive)
        extract_archive(archive, self.root / "restored")
        receipt = partial.verify_delivery(self.root / "restored", manifest=self.manifest, **self.identity)
        self.assertEqual(1, receipt["included_reports"])
        self.assertEqual(b"bound original figure pixels", next((self.root / "restored").glob("*/assets/source_image_01.png")).read_bytes())

    def test_manifest_change_is_not_same_selection(self):
        self._report()
        self._prepare()
        altered = self.root / "altered.json"
        rows = [dict(row) for row in self.rows]
        rows[-1]["content_sha256"] = "f" * 64
        altered.write_text(json.dumps(rows))
        with self.assertRaisesRegex(ValueError, "original_manifest_mismatch"):
            partial.verify_delivery(self.downloads / "shard_0", manifest=altered, **self.identity)

    def test_original_figure_proof_and_image_map_survive_canonical_directory_copy(self):
        from test_mineru_figure_sources import Fixture, digest
        from build_market_views_pdf import extract_exhibit_figures
        import shutil
        fixture = Fixture(self.root / "figure-fixture")
        markdown = fixture.report / "source_mineru.md"
        markdown.write_text(markdown.read_text() + "\n\n" + "Economic growth and earnings evidence from the verified original source. " * 10)
        fixture.md_sha = digest(markdown.read_bytes())
        selection = fixture.create()
        fixture.status()
        (fixture.report / "source_image_map.json").write_text(json.dumps({"version": 1,
            "source_sha256": fixture.md_sha, "images": selection["reference_images"]}))
        row = self.rows[0]
        row["content_sha256"] = fixture.original_sha
        self.manifest.write_text(json.dumps(self.rows))
        name = Path(row["process_local_path"]).name
        (self.originals / name).write_bytes(fixture.original.read_bytes())
        staged = unique_batch_name(Path(row["process_local_path"]), 1)
        status = json.loads((fixture.report / "status.json").read_text())
        status.update(source_pdf=staged, mineru_state="done")
        (fixture.report / "status.json").write_text(json.dumps(status))
        producer = self.root / "producer_0"
        shutil.copytree(fixture.report, producer / slug(staged))
        self._prepare()
        receipt = self._assemble()
        report = self.root / "delivery" / receipt["reports"][0]["report_id"]
        figures = extract_exhibit_figures(report, "R001", "Original research", 2)
        self.assertEqual(1, len(figures))
        self.assertEqual("mineru_source_figure", figures[0]["selection_source"])
        self.assertEqual((fixture.report / selection["images"][0]).read_bytes(), Path(figures[0]["source_path"]).read_bytes())


class PartialSourceWorkflowTests(unittest.TestCase):
    def test_snapshot_runs_after_failed_generation_without_changing_normal_gate(self):
        from test_market_views_workflow_contract import UPSTREAM, gate
        workflow = UPSTREAM.read_text()
        step_name = "- name: Snapshot individually ready Market Views sources"
        step = workflow.split(step_name, 1)[1].split("\n      - name:", 1)[0]
        self.assertTrue(gate(step, {}, prior_steps_success=False,
                             steps={"generation_checkpoint": "success"}))
        self.assertFalse(gate(step, {}, prior_steps_success=False,
                              steps={"generation_checkpoint": "failure"}))
        self.assertIn("continue-on-error: true", step)
        self.assertIn("timeout-minutes: 5", step)
        self.assertLess(workflow.index("- name: Save private generation checkpoint including partial progress"),
                        workflow.index(step_name))
        self.assertLess(workflow.index(step_name), workflow.index("- name: Upload shard to private R2 handoff"))
        self.assertIn('if [ ! -f _selected_macro_manifest/selected_to_process_manifest.json ] || [ ! -d "$OUTPUT_DIR" ]', step)
        self.assertIn('scripts/market_views_partial_sources.py prepare', step)
        self.assertIn('--source-run-id "$GITHUB_RUN_ID" --source-execution-sha "$GITHUB_SHA"', step)
        self.assertIn('--shard-index "${{ matrix.shard_index }}"', step)
        self.assertIn('--reports-per-shard "${{ needs.resolve-inputs.outputs.reports_per_shard }}"', step)
        self.assertIn('_private-workflow-handoff/market-views-available/$GITHUB_RUN_ID/', step)
        normal = workflow.split("- name: Upload shard to private R2 handoff", 1)[1].split("\n      - name:", 1)[0]
        self.assertIn("if: ${{ steps.gate.outputs.run == 'true' }}", normal)
        self.assertNotIn("always()", normal)


if __name__ == "__main__":
    unittest.main()
