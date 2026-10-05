"""Re-audit one retained complete native source without repeating extraction.

The original receipt and producer identity are immutable. A separate small R2
attestation binds the successful main-branch audit to those exact source bytes.
No OCR engine, MinerU submission, model generation or source upload is invoked.
"""
from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

SOURCE_WORKFLOW = ".github/workflows/market-views-native-recovery.yml"
WORKFLOW = ".github/workflows/market-views-native-reaudit.yml"
AUDIT_STEP = "Re-audit retained native sources without extraction"
SOURCE_STEPS = ("Extract and verify the complete original source batch",
                "Archive verified native sources in private R2",
                "Audit complete cloud OCR numeric evidence")
PREFIX = "_private-workflow-handoff/native-source-reaudits"
KIND = "native-source-reaudit"
RUN = re.compile(r"[1-9][0-9]{0,19}")
SHA = re.compile(r"[a-f0-9]{40}")
HASH = re.compile(r"[a-f0-9]{64}")
MAX_ATTESTATION = 16_384


class ReauditError(ValueError):
    pass


def require(value, category):
    if not value:
        raise ReauditError(category)


def inputs(source_run_id, date_folder, expected_reports, original_source_run_id=""):
    require(isinstance(source_run_id, str) and RUN.fullmatch(source_run_id), "invalid_source_run")
    require(isinstance(date_folder, str) and re.fullmatch(r"[0-9]{6}", date_folder), "invalid_source_date")
    try:
        datetime.strptime(date_folder, "%y%m%d")
    except ValueError:
        raise ReauditError("invalid_source_date") from None
    require(type(expected_reports) is int and 1 <= expected_reports <= 1000, "invalid_source_count")
    require(isinstance(original_source_run_id, str)
            and (not original_source_run_id or RUN.fullmatch(original_source_run_id)), "invalid_original_run")


def verify_run(run, run_id, repository, workflow):
    require(isinstance(run, dict) and type(run.get("id")) is int and str(run["id"]) == run_id
            and run.get("path") == workflow and run.get("head_branch") == "main"
            and run.get("event") == "workflow_dispatch"
            and isinstance(run.get("head_sha"), str) and SHA.fullmatch(run["head_sha"])
            and type(run.get("run_attempt")) is int and run["run_attempt"] > 0
            and isinstance(run.get("repository"), dict)
            and run["repository"].get("full_name") == repository
            and isinstance(run.get("head_repository"), dict)
            and run["head_repository"].get("full_name") == repository, "invalid_main_producer")


def verify_job_steps(run, jobs_page, job_name, expected):
    require(isinstance(jobs_page, dict), "invalid_jobs_response")
    jobs, count = jobs_page.get("jobs"), jobs_page.get("total_count")
    require(type(count) is int and 0 <= count <= 100 and isinstance(jobs, list)
            and len(jobs) == count, "incomplete_jobs_response")
    require(all(isinstance(job, dict) and type(job.get("id")) is int and job["id"] > 0 for job in jobs),
            "invalid_job_metadata")
    require(len({job["id"] for job in jobs}) == len(jobs), "ambiguous_jobs_response")
    matches = [job for job in jobs if job.get("name") == job_name]
    require(len(matches) == 1, "missing_source_job")
    job = matches[0]
    require(job.get("status") == "completed" and type(job.get("run_id")) is int
            and job["run_id"] == run["id"] and job.get("head_sha") == run["head_sha"]
            and type(job.get("run_attempt")) is int and job["run_attempt"] == run["run_attempt"], "job_context_mismatch")
    steps = job.get("steps")
    require(isinstance(steps, list) and all(isinstance(step, dict) for step in steps), "invalid_source_steps")
    numbers = [step.get("number") for step in steps]
    require(all(type(number) is int and number > 0 for number in numbers)
            and len(numbers) == len(set(numbers)), "ambiguous_source_steps")
    selected = []
    for name, conclusion in expected:
        rows = [step for step in steps if step.get("name") == name]
        require(len(rows) == 1, "missing_source_gate")
        row = rows[0]
        require(row.get("status") == "completed" and row.get("conclusion") == conclusion,
                "source_gate_not_expected")
        selected.append(row["number"])
    require(selected == sorted(selected), "source_gate_order_mismatch")


def verify_retained_source(producer, jobs, source_run_id, repository):
    verify_run(producer, source_run_id, repository, SOURCE_WORKFLOW)
    require(producer.get("status") == "completed" and producer.get("conclusion") == "failure",
            "failed_audit_producer_required")
    verify_job_steps(producer, jobs, "recover", tuple(zip(SOURCE_STEPS, ("success", "success", "failure"))))


def verify_reaudit_producer(producer, jobs, run_id, repository):
    verify_run(producer, run_id, repository, WORKFLOW)
    require(producer.get("status") == "completed" and producer.get("conclusion") == "success",
            "successful_reaudit_required")
    verify_job_steps(producer, jobs, "reaudit", ((AUDIT_STEP, "success"),))


def gh_json(repository, suffix):
    require(re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository), "invalid_repository")
    try:
        result = subprocess.run(["gh", "api", f"repos/{repository}/actions/runs/{suffix}"],
                                capture_output=True, timeout=60, check=False)
        require(result.returncode == 0 and len(result.stdout) <= 2_000_000, "producer_metadata_unavailable")
        return json.loads(result.stdout)
    except (OSError, subprocess.TimeoutExpired, UnicodeError, json.JSONDecodeError):
        raise ReauditError("producer_metadata_unavailable") from None


def attestation_key(run_id, run_attempt, date_folder):
    inputs(run_id, date_folder, 1)
    require(type(run_attempt) is int and run_attempt > 0, "invalid_reaudit_attempt")
    return f"{PREFIX}/{run_id}/{run_attempt}/{date_folder}.json"


def _unique_object(pairs):
    value = {}
    for key, item in pairs:
        require(key not in value, "duplicate_attestation_field")
        value[key] = item
    return value


def read_attestation(client, bucket, key):
    try:
        response = client.get_object(Bucket=bucket, Key=key)
        body = response["Body"]
        try:
            require(type(response.get("ContentLength")) is int
                    and 0 < response["ContentLength"] <= MAX_ATTESTATION, "invalid_attestation_size")
            raw = body.read(MAX_ATTESTATION + 1)
        finally:
            body.close()
        metadata = response.get("Metadata", {})
        require(isinstance(raw, bytes) and len(raw) == response["ContentLength"]
                and metadata.get("kind") == KIND and metadata.get("sha256") == hashlib.sha256(raw).hexdigest(),
                "invalid_attestation_integrity")
        return json.loads(raw, object_pairs_hook=_unique_object)
    except ReauditError:
        raise
    except Exception:
        raise ReauditError("attestation_unavailable") from None


FIELDS = {"schema", "kind", "repository", "source_context", "source_run_attempt", "report_count",
          "receipt_sha256", "receipt_bytes", "manifest_sha256", "page_count", "fixture_sha256",
          "fixture_count", "reaudit_run_id", "reaudit_execution_sha", "reaudit_run_attempt",
          "ocr_call_count", "provider_post_count", "model_call_count"}


def verify_attestation(value, source, reaudit, repository, date_folder, expected_reports, identity):
    require(isinstance(value, dict) and set(value) == FIELDS, "invalid_attestation_schema")
    require(type(value["schema"]) is int and value["schema"] == 1 and value["kind"] == KIND
            and value["repository"] == repository, "invalid_attestation_schema")
    context = value["source_context"]
    require(isinstance(context, dict) and set(context) == {"date_folder", "producer_run_id", "execution_sha", "original_source_run_id"},
            "invalid_attestation_context")
    inputs(str(source["id"]), date_folder, expected_reports, context["original_source_run_id"])
    require(context["date_folder"] == date_folder and context["producer_run_id"] == str(source["id"])
            and context["execution_sha"] == source["head_sha"]
            and type(value["source_run_attempt"]) is int and value["source_run_attempt"] == source["run_attempt"],
            "attestation_source_mismatch")
    require(value["reaudit_run_id"] == str(reaudit["id"])
            and value["reaudit_execution_sha"] == reaudit["head_sha"]
            and type(value["reaudit_run_attempt"]) is int and value["reaudit_run_attempt"] == reaudit["run_attempt"],
            "attestation_reaudit_mismatch")
    require(type(value["report_count"]) is int and value["report_count"] == expected_reports
            and type(value["receipt_bytes"]) is int and value["receipt_bytes"] == identity["bytes"]
            and value["receipt_sha256"] == identity["sha256"] and HASH.fullmatch(str(value["receipt_sha256"]))
            and HASH.fullmatch(str(value["manifest_sha256"])), "attestation_receipt_mismatch")
    require(type(value["page_count"]) is int and value["page_count"] > 0
            and type(value["fixture_count"]) is int and value["fixture_count"] >= 0
            and ((value["fixture_count"] == 0 and value["fixture_sha256"] is None)
                 or (value["fixture_count"] > 0 and HASH.fullmatch(str(value["fixture_sha256"])))), "invalid_attestation_counts")
    require(all(type(value[key]) is int and value[key] == 0
                for key in ("ocr_call_count", "provider_post_count", "model_call_count")), "invalid_reaudit_operations")
    return context


def consume_attestation(source_dir, source, source_jobs, reaudit_run_id, repository, date_folder,
                        expected_reports, *, client, bucket, get_metadata=gh_json):
    """Alternative audit gate only; caller must still run full source validation."""
    from audit_market_views_ocr_receipt import receipt_identity
    from extract_native_market_sources import RECEIPT_NAME
    inputs(str(source["id"]), date_folder, expected_reports)
    require(isinstance(reaudit_run_id, str) and RUN.fullmatch(reaudit_run_id), "invalid_reaudit_run")
    verify_retained_source(source, source_jobs, str(source["id"]), repository)
    reviewer = get_metadata(repository, reaudit_run_id)
    reviewer_jobs = get_metadata(repository, f"{reaudit_run_id}/jobs?filter=latest&per_page=100")
    verify_reaudit_producer(reviewer, reviewer_jobs, reaudit_run_id, repository)
    attestation = read_attestation(client, bucket, attestation_key(reaudit_run_id, reviewer["run_attempt"], date_folder))
    return verify_attestation(attestation, source, reviewer, repository, date_folder, expected_reports,
                              receipt_identity(Path(source_dir) / RECEIPT_NAME))


def reaudit_retained(source_dir, producer, source_jobs, reviewer, repository, date_folder, expected_reports,
                     original_source_run_id, *, fixtures=None, client, bucket):
    from audit_market_views_ocr_receipt import audit_sources, receipt_identity
    from extract_native_market_sources import RECEIPT_NAME
    from private_workflow_handoff import download_directory
    source_run_id = str(producer["id"])
    inputs(source_run_id, date_folder, expected_reports, original_source_run_id)
    verify_retained_source(producer, source_jobs, source_run_id, repository)
    verify_run(reviewer, str(reviewer["id"]), repository, WORKFLOW)
    context = {"date_folder": date_folder, "producer_run_id": source_run_id,
               "execution_sha": producer["head_sha"], "original_source_run_id": original_source_run_id}
    download_directory(f"_private-workflow-handoff/market-sources/{source_run_id}/{date_folder}/shard_0.tar.gz",
                       Path(source_dir), client=client, bucket=bucket)
    identity = receipt_identity(Path(source_dir) / RECEIPT_NAME)
    print(json.dumps({"receipt_bytes": identity["bytes"],
                      "exceeds_legacy_audit_limit": identity["bytes"] > 256_000_000}), flush=True)
    summary = audit_sources(Path(source_dir), expected_reports, fixtures=fixtures, expected_source_context=context)
    require(summary["success"] is True and summary["source_contract_verified"] is True,
            "reaudit_fixture_rejected")
    require(summary["receipt_sha256"] == identity["sha256"] and receipt_identity(Path(source_dir) / RECEIPT_NAME) == identity,
            "receipt_changed_during_reaudit")
    value = {"schema": 1, "kind": KIND, "repository": repository, "source_context": context,
             "source_run_attempt": producer["run_attempt"], "report_count": summary["report_count"],
             "receipt_sha256": identity["sha256"], "receipt_bytes": identity["bytes"],
             "manifest_sha256": summary["manifest_sha256"], "page_count": summary["page_count"],
             "fixture_sha256": hashlib.sha256(Path(fixtures).read_bytes()).hexdigest() if fixtures else None,
             "fixture_count": summary["fixture_count"], "reaudit_run_id": str(reviewer["id"]),
             "reaudit_execution_sha": reviewer["head_sha"], "reaudit_run_attempt": reviewer["run_attempt"],
             "ocr_call_count": 0, "provider_post_count": 0, "model_call_count": 0}
    verify_attestation(value, producer, reviewer, repository, date_folder, expected_reports, identity)
    raw = (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()
    require(len(raw) <= MAX_ATTESTATION, "invalid_attestation_size")
    key = attestation_key(str(reviewer["id"]), reviewer["run_attempt"], date_folder)
    client.put_object(Bucket=bucket, Key=key, Body=raw, IfNoneMatch="*", ContentType="application/json",
                      Metadata={"kind": KIND, "sha256": hashlib.sha256(raw).hexdigest()})
    require(read_attestation(client, bucket, key) == value, "attestation_readback_mismatch")
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-run-id", required=True)
    parser.add_argument("--date-folder", required=True)
    parser.add_argument("--expected-reports", required=True, type=int)
    parser.add_argument("--original-source-run-id", default="")
    parser.add_argument("--source-dir", required=True, type=Path)
    parser.add_argument("--fixtures", type=Path)
    args = parser.parse_args()
    try:
        repository = os.environ.get("GITHUB_REPOSITORY", "")
        require(os.environ.get("GITHUB_ACTIONS") == "true" and os.environ.get("GITHUB_EVENT_NAME") == "workflow_dispatch"
                and os.environ.get("GITHUB_REF") == "refs/heads/main"
                and os.environ.get("GITHUB_WORKFLOW_REF") == f"{repository}/{WORKFLOW}@refs/heads/main", "manual_main_required")
        run_id = os.environ.get("GITHUB_RUN_ID", "")
        inputs(run_id, args.date_folder, args.expected_reports)
        inputs(args.source_run_id, args.date_folder, args.expected_reports, args.original_source_run_id)
        producer = gh_json(repository, args.source_run_id)
        jobs = gh_json(repository, f"{args.source_run_id}/jobs?filter=latest&per_page=100")
        reviewer = gh_json(repository, run_id)
        require(reviewer.get("head_sha") == os.environ.get("GITHUB_SHA")
                and str(reviewer.get("run_attempt")) == os.environ.get("GITHUB_RUN_ATTEMPT"), "reaudit_execution_mismatch")
        from private_workflow_handoff import build_r2_client, r2_bucket
        result = reaudit_retained(args.source_dir, producer, jobs, reviewer, repository, args.date_folder,
                                 args.expected_reports, args.original_source_run_id, fixtures=args.fixtures,
                                 client=build_r2_client(), bucket=r2_bucket())
        print(json.dumps({key: result[key] for key in ("report_count", "page_count", "receipt_bytes", "receipt_sha256",
                                                       "fixture_count", "ocr_call_count", "provider_post_count", "model_call_count")}))
        return 0
    except Exception:
        # Upstream validation and SDK errors can contain private source paths.
        print("Native source re-audit stopped: source_or_attestation_invalid", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
