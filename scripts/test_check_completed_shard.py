import json
import tempfile
import unittest
from pathlib import Path

from check_completed_shard import completed_shard_reason, normalized_source_name


class CompletedShardTests(unittest.TestCase):
    def build_fixture(self, root: Path) -> tuple[Path, Path]:
        manifest = []
        for rank in range(1, 7):
            manifest.append(
                {
                    "id": rank - 1,
                    "process_rank": rank,
                    "process_local_path": f"/tmp/{rank:02d}-Report-{rank}.pdf",
                }
            )
        manifest_path = root / "selected_to_process_manifest.json"
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

        output_dir = root / "shard_1"
        output_dir.mkdir()
        report_dir = output_dir / "0001-06-Report-6"
        report_dir.mkdir()
        (report_dir / "source_mineru.md").write_text("source", encoding="utf-8")
        (report_dir / "wechat_article.md").write_text("# article", encoding="utf-8")
        (report_dir / "status.json").write_text(
            json.dumps({"source_pdf": "/tmp/0001-06-Report-6.pdf"}),
            encoding="utf-8",
        )
        (output_dir / "shard_run_summary.md").write_text(
            "\n".join(
                [
                    "# Shard 1 summary",
                    "- Selected PDFs available to shards: 6",
                    "- Shard index: 1",
                    "- Reports per shard: 5",
                    "- Report directories generated: 1",
                ]
            ),
            encoding="utf-8",
        )
        return output_dir, manifest_path

    def test_reuses_matching_complete_shard(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output_dir, manifest_path = self.build_fixture(Path(tmp))
            complete, reason = completed_shard_reason(output_dir, manifest_path, 1, 6, 5)
        self.assertTrue(complete)
        self.assertIn("reusing 1", reason)

    def test_rejects_changed_source_selection(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output_dir, manifest_path = self.build_fixture(Path(tmp))
            payload = json.loads(manifest_path.read_text(encoding="utf-8"))
            payload[-1]["process_local_path"] = "/tmp/06-Different.pdf"
            manifest_path.write_text(json.dumps(payload), encoding="utf-8")
            complete, reason = completed_shard_reason(output_dir, manifest_path, 1, 6, 5)
        self.assertFalse(complete)
        self.assertIn("do not match", reason)

    def test_force_reprocess_disables_reuse(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output_dir, manifest_path = self.build_fixture(Path(tmp))
            complete, reason = completed_shard_reason(
                output_dir,
                manifest_path,
                1,
                6,
                5,
                force_reprocess=True,
            )
        self.assertFalse(complete)
        self.assertEqual("force_reprocess=true", reason)

    def test_source_name_comparison_ignores_batch_punctuation_rewrites(self) -> None:
        manifest_name = "01-BARC-A&T：Read~through（Q2）.pdf"
        staged_name = "0001-01-BARC-A-T-Read-through-Q2-.pdf"
        self.assertEqual(
            normalized_source_name(manifest_name),
            normalized_source_name(staged_name),
        )

    def test_source_name_comparison_normalizes_institution_prefixes(self) -> None:
        pairs = [
            ("GS-China outlook.pdf", "GoldmanSachs-China outlook.pdf"),
            ("MS-AI infrastructure.pdf", "MorganStanley-AI infrastructure.pdf"),
            ("JPM-Japan FX.pdf", "JPMorgan-Japan FX.pdf"),
            ("DB-Europe rates.pdf", "DeutscheBank-Europe rates.pdf"),
            ("BARC-Hardware.pdf", "Barclays-Hardware.pdf"),
        ]
        for abbreviated, expanded in pairs:
            with self.subTest(abbreviated=abbreviated):
                self.assertEqual(
                    normalized_source_name(abbreviated),
                    normalized_source_name(expanded),
                )


if __name__ == "__main__":
    unittest.main()
