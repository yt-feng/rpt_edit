"""Cloud-only evidence for the 17 IMF sources frozen on 2026-10-12.

This diagnostic never calls a downloader itself or changes production state.
PDF identity is presented for human review, not inferred from fuzzy title scores.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
from urllib.parse import urlsplit
from zoneinfo import ZoneInfo

from institution_pending_intake import PendingIntake

FIXTURE = Path("scripts/fixtures/institution_sources/imf_pending_acceptance_20261012.json")
FIXTURE_SHA256 = "e0674b735b429c35515319cd6b959f8da1923dc076038ac897e020459d965a5f"
OUT = Path("_fetch_test")
PROTECTED = (
    "institution_feeds/pending_intake/imf.json",
    "institution_feeds/seen_state.json",
    "institution_feeds/institution_pdf_archive.jsonl",
)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def file_hash(path):
    if not path.is_file() or path.is_symlink():
        raise ValueError("required_regular_file_missing")
    return sha(path.read_bytes())


def frozen(root):
    path = root / FIXTURE
    if file_hash(path) != FIXTURE_SHA256:
        raise ValueError("frozen_seed_hash_mismatch")
    PendingIntake(path, {}, now=datetime.now(timezone.utc), retry_limit=17)
    data = read_json(path)
    if len(data["items"]) != 17:
        raise ValueError("frozen_seed_count_mismatch")
    return data


def prepare(root):
    frozen(root)
    output = root / OUT
    if output.exists():
        raise ValueError("test_output_must_be_fresh")
    protected = {path: file_hash(root / path) for path in PROTECTED}
    output.mkdir()
    shutil.copyfile(root / FIXTURE, output / "frozen_seed.json")
    shutil.copyfile(root / FIXTURE, output / "imf-pending-intake.json")
    (output / "acceptance_prepare.json").write_text(json.dumps({
        "schema": 1, "target_count": 17, "frozen_seed_sha256": FIXTURE_SHA256,
        "protected_sha256": protected,
    }, indent=2) + "\n")


def fetch(root, producer=None):
    """Run the ordinary resolver with only the frozen intake eligible to download."""
    if producer is None:
        import fetch_institution_latest_pdfs as producer
    seed = frozen(root)
    expected = seed["items"]
    output = root / OUT
    original_intake, original_argv = producer.PendingIntake, sys.argv

    class FrozenIntake(original_intake):
        def merge(self, discovered):
            if (set(self.items) != set(expected)
                    or any(self.items[key]["item"] != expected[key]["item"] for key in expected)):
                raise ValueError("isolated_intake_identity_changed")
            # Preserve the ordinary discovery call and its error/empty status.
            # Only restrict download work after the genuine discovery result.
            merged = super().merge(discovered)
            scoped = [item for item in merged if "imf:" + item["guid"] in expected]
            if len(scoped) != 17 or len({item["guid"] for item in scoped}) != 17:
                raise ValueError("isolated_intake_scope_invalid")
            (output / "acceptance_scope.json").write_text(json.dumps({
                "target_count": 17, "guids": sorted(item["guid"] for item in scoped),
                "discovered_count": len(discovered),
                "excluded_fresh_count": len(merged) - len(scoped),
            }, indent=2) + "\n")
            return scoped

    producer.PendingIntake = FrozenIntake
    sys.argv = ["fetch_institution_latest_pdfs.py",
                "--output-dir", str(output),
                "--pending-intake-path", str(output / "imf-pending-intake.json"),
                "--imf-pending-retries", "17",
                "--date", datetime.now(ZoneInfo("Asia/Shanghai")).strftime("%y%m%d"),
                "--institutions", "imf", "--since-days", "7",
                "--max-per-institution", "17", "--max-total", "17",
                "--force-reprocess", "false", "--archive-path", str(output / "test_archive.jsonl"),
                "--seen-state-path", str(output / "test_seen.json")]
    try:
        return producer.main()
    finally:
        producer.PendingIntake, sys.argv = original_intake, original_argv


def pdf_evidence(path, preview_path):
    import pymupdf as fitz
    from pypdf import PdfReader

    data = path.read_bytes()
    if not data.startswith(b"%PDF-") or not 0 < len(data) <= 60 * 1024 * 1024:
        raise ValueError("pdf_bytes_invalid")
    reader = PdfReader(path)
    if reader.is_encrypted:
        raise ValueError("pdf_encrypted")
    pages = len(reader.pages)
    if not 1 <= pages <= 5000:
        raise ValueError("pdf_page_count_invalid")
    # Read every page object, then independently render the first page for review.
    for page in reader.pages:
        tuple(page.mediabox)
    with fitz.open(path) as doc:
        if doc.page_count != pages:
            raise ValueError("pdf_parser_page_count_disagrees")
        page = doc.load_page(0)
        if page.rect.width <= 0 or page.rect.height <= 0:
            raise ValueError("pdf_page_geometry_invalid")
        scale = min(1.5, 1400 / max(page.rect.width, page.rect.height))
        page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False).save(preview_path)
        text = page.get_text("text").strip()
    return {"bytes": len(data), "sha256": sha(data), "pages": pages,
            "first_page_text": text[:2400], "first_page_text_sha256": sha(text.encode()),
            "first_page_preview": preview_path.name}


def verify(root, producer_exit_code, inspect_pdf=pdf_evidence):
    output = root / OUT
    result = {"schema": 1, "target_count": 17, "producer_exit_code": producer_exit_code,
              "status": "failed", "errors": [], "reports": [],
              "identity_review": "pending human review of source-bound first pages",
              "frozen_seed_sha256": FIXTURE_SHA256}
    errors = result["errors"]
    try:
        seed = frozen(root)
        checkpoint = read_json(output / "acceptance_prepare.json")
        if file_hash(output / "frozen_seed.json") != FIXTURE_SHA256:
            errors.append("frozen_working_copy_changed")
        result["production_state_unchanged"] = all(
            file_hash(root / path) == checkpoint["protected_sha256"].get(path)
            for path in PROTECTED)
        if not result["production_state_unchanged"]:
            errors.append("production_state_changed")
        pending = read_json(output / "imf-pending-intake.json")
        if set(pending.get("items", {})) != set(seed["items"]):
            errors.append("pending_scope_changed")
        for key, original in seed["items"].items():
            current = pending.get("items", {}).get(key, {})
            if any(current.get(field) != original[field] for field in ("item", "admitted_at", "since_days")):
                errors.append("pending_identity_or_admission_changed:" + key)
        if producer_exit_code != 0:
            errors.append("producer_failed")
        manifest = read_json(output / "institution_run_manifest.json")
        targets = {row["item"]["source_url"]: row["item"] for row in seed["items"].values()}
        scope = read_json(output / "acceptance_scope.json")
        if (scope.get("target_count") != 17
                or scope.get("guids") != sorted(item["guid"] for item in targets.values())):
            errors.append("fetch_attempt_scope_mismatch")
        rows = manifest.get("downloaded", [])
        if not isinstance(rows, list):
            raise ValueError("downloaded_records_invalid")
        actual = [row.get("source_page_url") for row in rows]
        if len(rows) != 17 or len(set(actual)) != 17 or set(actual) != set(targets):
            errors.append("exact_17_source_coverage_mismatch")
        if manifest.get("downloaded_count") != 17 or manifest.get("institutions") != ["imf"]:
            errors.append("download_manifest_count_or_scope_mismatch")
        if manifest.get("skipped_count") != 0 or manifest.get("skipped") != []:
            errors.append("source_skipped")
        checks = manifest.get("source_checks", [])
        if (len(checks) != 1 or checks[0].get("institution") != "imf"
                or checks[0].get("status") != "ok"
                or checks[0].get("resolution_failure_count") != 0
                or checks[0].get("eligible_item_count") != 17
                or checks[0].get("new_pdf_count") != 17
                or checks[0].get("deferred_retry_count") != 0
                or checks[0].get("error") != ""
                or checks[0].get("discovery_error") is not False):
            errors.append("source_health_not_clean")
        previews = output / "first_pages"
        previews.mkdir(exist_ok=True)
        recorded_files = set()
        for row in rows:
            source = row.get("source_page_url")
            if source not in targets:
                continue
            item = targets[source]
            proof = {"guid": item["guid"], "source_url": source,
                     "expected_title": item["title"], "expected_published": item["date"],
                     "identity_review": "pending", "errors": []}
            result["reports"].append(proof)
            try:
                filename = row.get("local_filename", "")
                suffix = hashlib.sha1(("imf:" + item["guid"]).encode()).hexdigest()[:8]
                if (not isinstance(filename, str) or Path(filename).name != filename
                        or not filename.endswith("_" + suffix + ".pdf") or filename in recorded_files):
                    raise ValueError("source_filename_binding_invalid")
                recorded_files.add(filename)
                path = output / filename
                if not path.is_file() or path.is_symlink():
                    raise ValueError("pdf_file_missing")
                if row.get("institution") != "imf" or row.get("published") != item["date"]:
                    raise ValueError("source_publication_binding_invalid")
                url = urlsplit(row.get("pdf_url", ""))
                if (url.scheme != "https" or url.hostname != "www.imf.org"
                        or url.username or url.password
                        or url.port not in (None, 443)
                        or not url.path.lower().endswith((".pdf", ".ashx"))):
                    raise ValueError("official_pdf_url_invalid")
                proof["pdf_url_without_query"] = url._replace(query="", fragment="").geturl()
                proof["pdf_url_sha256"] = sha(row["pdf_url"].encode())
                evidence = inspect_pdf(path, previews / (item["guid"] + ".png"))
                proof.update(evidence)
                if evidence["bytes"] != row.get("bytes") or evidence["sha256"] != row.get("sha256"):
                    raise ValueError("pdf_bytes_or_hash_mismatch")
                proof["machine_checks"] = "passed"
            except Exception as error:
                # Error types and reviewed fixed codes only; no request/secret text.
                code = str(error) if type(error) is ValueError else type(error).__name__
                proof["errors"].append(code if code in {
                    "source_filename_binding_invalid", "pdf_file_missing", "source_publication_binding_invalid",
                    "official_pdf_url_invalid", "pdf_bytes_invalid", "pdf_encrypted", "pdf_page_count_invalid",
                    "pdf_parser_page_count_disagrees", "pdf_page_geometry_invalid", "pdf_bytes_or_hash_mismatch",
                } else type(error).__name__)
                errors.append("source_pdf_validation_failed:" + item["guid"])
        actual_files = {path.name for path in output.glob("*.pdf")}
        if recorded_files != actual_files:
            errors.append("pdf_files_do_not_match_manifest")
        result["verified_report_count"] = sum(row.get("machine_checks") == "passed" for row in result["reports"])
        result["duplicate_content_groups"] = [guids for guids in (
            [row["guid"] for row in result["reports"] if row.get("sha256") == checksum]
            for checksum in sorted({row["sha256"] for row in result["reports"] if "sha256" in row})) if len(guids) > 1]
        if not errors and result["verified_report_count"] == 17:
            result["status"] = "machine_checks_passed_pending_identity_review"
    except Exception as error:
        errors.append("acceptance_validation_failed:" + type(error).__name__)
    output.mkdir(exist_ok=True)
    (output / "exact17_acceptance.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    review = ["# IMF exact-source PDF identity review", "", "Automated checks: " + result["status"], "",
              "Review each first page against its original source/title/date. No fuzzy-title threshold is used.",
              "Shared hashes, image-only cover pages, and uncertain identities require examination before production resumes.", ""]
    for row in result["reports"]:
        review.extend(["## " + row["expected_title"], "", "Source: " + row["source_url"],
                       "", "GUID: " + row["guid"], "", "Expected publication: " + row["expected_published"], ""])
        if row.get("first_page_preview"):
            review.extend(["![First page](first_pages/" + row["first_page_preview"] + ")", ""])
    (output / "identity_review.md").write_text("\n".join(review) + "\n")
    return result


def main():
    if os.getenv("GITHUB_ACTIONS") != "true":
        raise SystemExit("Cloud Actions execution only; offline unit tests may call injected helpers")
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("prepare", "fetch", "verify"))
    parser.add_argument("--producer-exit-code", type=int, default=0)
    args = parser.parse_args()
    if args.command == "prepare":
        prepare(Path.cwd())
        print("Prepared isolated 17-source IMF acceptance; production state unchanged.")
        return 0
    if args.command == "fetch":
        return fetch(Path.cwd())
    result = verify(Path.cwd(), args.producer_exit_code)
    print(json.dumps({"status": result["status"], "verified_report_count": result.get("verified_report_count", 0),
                      "error_count": len(result["errors"])}))
    return 0 if not result["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
