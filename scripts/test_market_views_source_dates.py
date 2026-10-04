#!/usr/bin/env python3
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from build_market_views_pdf import require_primary_report_dirs, source_date_dirs, report_digest, report_extract


class SourceDateDirsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = TemporaryDirectory()
        base = Path(self.temp_dir.name)
        self.bank = base / "dropbox"
        self.institutions = base / "institutions"
        self.consulting = base / "consulting"

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    @staticmethod
    def make_dates(root: Path, *dates: str) -> None:
        for date in dates:
            (root / date).mkdir(parents=True)

    @staticmethod
    def make_report(root: Path, date: str) -> Path:
        report = root / date / "report"
        report.mkdir(parents=True, exist_ok=True)
        (report / "source_mineru.md").write_text("# Parsed report")
        return report

    def test_latest_issue_date_follows_bank_batch_and_excludes_future_auxiliary(self) -> None:
        self.make_dates(self.bank, "260718", "260719")
        self.make_dates(self.institutions, "260718", "260720")
        self.make_dates(self.consulting, "260717")
        for date in ("260718", "260720"):
            self.make_report(self.institutions, date)
        self.make_report(self.consulting, "260717")
        report_dir = self.bank / "260719" / "shard_0" / "bank-report"
        report_dir.mkdir(parents=True)
        (report_dir / "source_mineru.md").write_text("# Parsed bank report")

        report_date, source_dirs = source_date_dirs(
            self.bank,
            [self.institutions, self.consulting],
            "latest",
        )

        self.assertEqual(report_date, "260719")
        self.assertEqual(
            source_dirs,
            [
                self.bank / "260719",
                self.institutions / "260718",
                self.consulting / "260717",
            ],
        )
        self.assertEqual(require_primary_report_dirs(source_dirs[0]), [report_dir])

    def test_explicit_bank_date_includes_latest_usable_auxiliary_on_or_before_issue(self) -> None:
        self.make_dates(self.bank, "260718", "260719")
        self.make_dates(self.institutions, "260717", "260719")
        self.make_dates(self.consulting, "260716", "260720")
        self.make_report(self.institutions, "260717")
        self.make_report(self.consulting, "260716")

        report_date, source_dirs = source_date_dirs(
            self.bank,
            [self.institutions, self.consulting],
            "260718",
        )

        self.assertEqual(report_date, "260718")
        self.assertEqual(
            source_dirs,
            [
                self.bank / "260718",
                self.institutions / "260717",
                self.consulting / "260716",
            ],
        )

    def test_latest_requires_a_primary_bank_date(self) -> None:
        self.make_dates(self.institutions, "260720")

        with self.assertRaisesRegex(RuntimeError, "primary bank source root"):
            source_date_dirs(self.bank, [self.institutions], "latest")

    def test_explicit_date_rejects_non_date_paths(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "Invalid primary bank date folder"):
            source_date_dirs(self.bank, [], "../260720")

    def test_explicit_date_rejects_invalid_calendar_dates(self) -> None:
        for invalid in ("261099", "2610030", "20261301"):
            with self.subTest(invalid=invalid), self.assertRaisesRegex(RuntimeError, "Invalid primary bank date"):
                source_date_dirs(self.bank, [], invalid)

    def test_empty_auxiliary_date_falls_back_to_usable_older_source(self) -> None:
        self.make_dates(self.bank, "261003")
        self.make_dates(self.institutions, "261002")
        self.make_report(self.institutions, "261001")
        self.assertEqual(source_date_dirs(self.bank, [self.institutions, self.consulting], "latest"),
                         ("261003", [self.bank / "261003", self.institutions / "261001"]))

    def test_mixed_six_and_eight_digit_source_dates_follow_calendar_order(self) -> None:
        self.make_dates(self.bank, "261003", "20261001")
        self.make_report(self.institutions, "20261002")
        self.make_report(self.institutions, "261004")
        self.assertEqual(source_date_dirs(self.bank, [self.institutions], "latest"),
                         ("261003", [self.bank / "261003", self.institutions / "20261002"]))

    def test_native_pdf_source_reaches_report_discovery_and_summary_inputs(self) -> None:
        report = self.bank / "261003" / "shard_0" / "report-a"
        report.mkdir(parents=True)
        text = "# Original report title\n\n" + "Native original report evidence covering growth and inflation. " * 20
        (report / "source_native_pdf.md").write_text(text)
        self.assertEqual(require_primary_report_dirs(self.bank / "261003"), [report])
        self.assertIn("growth and inflation", report_digest(report, 2200)["digest"])
        self.assertIn("growth and inflation", report_extract(report, 2200))

    def test_primary_bank_date_must_contain_parsed_report_outputs(self) -> None:
        (self.bank / "260720").mkdir(parents=True)
        self.make_dates(self.institutions, "260720")
        (self.institutions / "260720" / "note.md").write_text("# Auxiliary only")

        with self.assertRaisesRegex(RuntimeError, "auxiliary sources alone"):
            require_primary_report_dirs(self.bank / "260720")

    def test_primary_bank_report_markers_are_accepted(self) -> None:
        report_dir = self.bank / "260720" / "shard_0" / "report-a"
        report_dir.mkdir(parents=True)
        (report_dir / "source_mineru.md").write_text("# Parsed bank report")

        self.assertEqual(require_primary_report_dirs(self.bank / "260720"), [report_dir])


if __name__ == "__main__":
    unittest.main()
