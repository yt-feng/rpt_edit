#!/usr/bin/env python3
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from build_market_views_pdf import require_primary_report_dirs, source_date_dirs


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

    def test_latest_issue_date_follows_newest_available_source(self) -> None:
        self.make_dates(self.bank, "260718", "260719")
        self.make_dates(self.institutions, "260718", "260720")
        self.make_dates(self.consulting, "260717")
        report_dir = self.bank / "260719" / "shard_0" / "bank-report"
        report_dir.mkdir(parents=True)
        (report_dir / "source_mineru.md").write_text("# Parsed bank report")

        report_date, source_dirs = source_date_dirs(
            self.bank,
            [self.institutions, self.consulting],
            "latest",
        )

        self.assertEqual(report_date, "260720")
        self.assertEqual(
            source_dirs,
            [
                self.bank / "260719",
                self.institutions / "260720",
                self.consulting / "260717",
            ],
        )
        self.assertEqual(require_primary_report_dirs(source_dirs[0]), [report_dir])

    def test_explicit_date_uses_the_same_date_for_every_source_root(self) -> None:
        self.make_dates(self.bank, "260718", "260719")
        self.make_dates(self.institutions, "260717", "260719")
        self.make_dates(self.consulting, "260716", "260720")

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
                self.institutions / "260718",
                self.consulting / "260718",
            ],
        )

    def test_latest_requires_a_primary_bank_date(self) -> None:
        self.make_dates(self.institutions, "260720")

        with self.assertRaisesRegex(RuntimeError, "primary bank source root"):
            source_date_dirs(self.bank, [self.institutions], "latest")

    def test_explicit_date_rejects_non_date_paths(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "Invalid primary bank date folder"):
            source_date_dirs(self.bank, [], "../260720")

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
