#!/usr/bin/env python3
"""Read actual matrix outcomes before selecting the normal or degraded edition."""
import argparse
import json
import math
import re
import subprocess
import sys
import time


class JobsPending(RuntimeError):
    """GitHub has not exposed a complete job snapshot yet."""


def github_json(endpoint, timeout):
    """Use the existing gh credentials without placing diagnostics in outputs."""
    try:
        result = subprocess.run(
            ["gh", "api", endpoint], capture_output=True, text=True,
            check=False, timeout=timeout,
        )
    except subprocess.TimeoutExpired as exc:
        raise JobsPending("GitHub jobs request timed out") from exc
    if result.returncode:
        # Re-reading cannot fix an authentication, permission or endpoint error.
        # Do not echo gh's response body into workflow outputs or logs.
        if (re.search(r"HTTP 403\b", result.stderr)
                and re.search(r"rate.?limit|secondary.?limit|abuse detection", result.stderr, re.I)):
            raise JobsPending("GitHub jobs request was rate limited")
        if re.search(r"HTTP (401|403|404)\b", result.stderr):
            raise ValueError("GitHub jobs request was denied or not found")
        raise JobsPending("GitHub jobs request failed temporarily")
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise JobsPending("GitHub jobs response was incomplete") from exc


def _live_snapshot(repository, expected_shards, run_id, sha, no_work, request):
    page = request(f"repos/{repository}/actions/runs/{run_id}/jobs?filter=latest&per_page=100")
    if not isinstance(page, dict) or not isinstance(page.get("jobs"), list):
        raise JobsPending("Daily jobs inventory is not available")
    jobs = page["jobs"]
    total = page.get("total_count")
    if type(total) is not int or total < 0 or total > 100 or len(jobs) > 100:
        raise ValueError("Invalid daily jobs inventory size")
    if total != len(jobs) or not jobs:
        raise JobsPending("Daily jobs inventory is incomplete")

    shards = {}
    for position, job in enumerate(jobs):
        if not isinstance(job, dict):
            raise ValueError("Invalid daily job entry")
        match = re.fullmatch(r"process-shard \(([0-9]+)\)", job.get("name", ""))
        if not match:
            continue
        index = int(match[1])
        if (index in shards or index >= expected_shards
                or type(job.get("id")) is not int or job["id"] <= 0
                or job.get("run_id") != int(run_id) or job.get("head_sha") != sha):
            raise ValueError("Daily shard identity differs")
        shards[index] = position
    if set(shards) != set(range(expected_shards)):
        raise JobsPending("Daily shard inventory is not complete yet")

    required_gate = "Gate shard" if no_work else "Upload shard to private R2 handoff"

    def incomplete(job):
        steps = job.get("steps")
        return (job.get("status") != "completed" or not isinstance(steps, list) or not steps
                or any(not isinstance(step, dict) or step.get("status") != "completed" for step in steps)
                or (job.get("conclusion") == "success"
                    and not any(step.get("name") == required_gate for step in steps)))

    for position in shards.values():
        job = jobs[position]
        if incomplete(job):
            # A completed matrix job can briefly have no steps in list-jobs.
            # Hydrate only that exact job; never substitute another run/attempt.
            detail = request(f"repos/{repository}/actions/jobs/{job['id']}")
            if (not isinstance(detail, dict)
                    or any(detail.get(key) != job.get(key) for key in ("id", "name", "run_id", "head_sha"))):
                raise ValueError("Daily shard detail identity differs")
            jobs[position] = detail
            if incomplete(detail):
                raise JobsPending("Daily shard steps are not complete yet")
    return page


def evaluate_live(repository, expected_shards, run_id, sha, selected_count=None, *,
                  timeout=180, poll_interval=5, api=github_json,
                  monotonic=time.monotonic, sleep=time.sleep):
    """Wait briefly for complete API evidence, then use the unchanged strict gate."""
    if (not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository)
            or not re.fullmatch(r"[1-9][0-9]*", str(run_id))
            or not re.fullmatch(r"[a-f0-9]{40}", sha)
            or type(expected_shards) is not int or not 0 <= expected_shards <= 100
            or (selected_count is not None and (type(selected_count) is not int or selected_count < 0))
            or not math.isfinite(timeout) or not math.isfinite(poll_interval)
            or timeout <= 0 or poll_interval <= 0):
        raise ValueError("Invalid live daily source status request")
    if expected_shards == 0 and selected_count != 0:
        raise ValueError("No shards for nonempty selection")
    deadline = monotonic() + timeout

    def request(endpoint):
        remaining = deadline - monotonic()
        if remaining <= 0:
            raise JobsPending("Daily jobs evidence deadline reached")
        return api(endpoint, timeout=min(20, remaining))

    attempt = 0
    while True:
        attempt += 1
        try:
            page = _live_snapshot(repository, expected_shards, run_id, sha, selected_count == 0, request)
            return evaluate(page, expected_shards, run_id, sha, selected_count)
        except JobsPending as exc:
            remaining = deadline - monotonic()
            if remaining <= 0:
                raise TimeoutError(f"Complete daily shard evidence unavailable after {timeout:g}s: {exc}") from exc
            delay = min(poll_interval * 2 ** min(attempt - 1, 2), remaining)
            print(f"Daily source status attempt {attempt}: {exc}; retrying in {delay:g}s.", file=sys.stderr)
            sleep(delay)


def evaluate(jobs_page, expected_shards, run_id, sha, selected_count=None):
    jobs = jobs_page.get("jobs")
    if (not isinstance(jobs, list) or jobs_page.get("total_count") != len(jobs)
            or not 0 < len(jobs) <= 100 or type(expected_shards) is not int or expected_shards < 0
            or (selected_count is not None and (type(selected_count) is not int or selected_count < 0))):
        raise ValueError("Incomplete daily jobs inventory")
    no_work = selected_count == 0
    if expected_shards == 0 and not no_work:
        raise ValueError("No shards for nonempty selection")
    shards, provider_only = {}, []
    for job in jobs:
        match = re.fullmatch(r"process-shard \(([0-9]+)\)", job.get("name", ""))
        if not match:
            continue
        index = int(match[1])
        if (index in shards or job.get("run_id") != int(run_id) or job.get("head_sha") != sha
                or job.get("status") != "completed"):
            raise ValueError("Daily shard identity or completion differs")
        steps = job.get("steps", [])
        if not steps:
            raise ValueError("Daily shard steps are missing")
        if no_work:
            gates = [step for step in steps if step.get("name") == "Gate shard"]
            if (job.get("conclusion") != "success" or len(gates) != 1
                    or gates[0].get("conclusion") != "success"
                    or any(step.get("conclusion") in {"failure", "cancelled", "timed_out"} for step in steps)
                    or any(step.get("name") == "Generate shard outputs" and step.get("conclusion") != "skipped" for step in steps)):
                raise ValueError("Empty selection did not finish as a clean no-op")
            shards[index] = False
            continue
        # Job-level continue-on-error never grants access to partial generated
        # notes: inspect the real steps, and require the completed handoff gate.
        handoff = [step for step in steps if step.get("name") == "Upload shard to private R2 handoff"]
        shards[index] = (job.get("conclusion") == "success"
            and not any(step.get("conclusion") in {"failure", "cancelled", "timed_out"} for step in steps)
            and len(handoff) == 1 and handoff[0].get("conclusion") == "success")
        if not shards[index]:
            failed_names = {step.get("name") for step in steps if step.get("conclusion") in {"failure", "cancelled", "timed_out"}}
            proof = [step for step in steps if step.get("name") == "Confirm provider-only source degradation"]
            provider_only.append(failed_names == {"Generate shard outputs"}
                                 and len(proof) == 1 and proof[0].get("conclusion") == "success")
    if set(shards) != set(range(expected_shards)):
        raise ValueError("Daily shard inventory differs from the selected manifest")
    if no_work:
        return {"primary_ready": False, "degraded_shards": 0, "provider_only": False, "no_work": True}
    return {"primary_ready": all(shards.values()), "degraded_shards": sum(not ready for ready in shards.values()),
            "provider_only": bool(provider_only) and all(provider_only), "no_work": False}


def require_provider_only_failure(summary):
    batches = summary.get("batches")
    if not isinstance(batches, list) or not batches:
        raise ValueError("Missing generation failure evidence")
    failed = []
    for batch in batches:
        code = batch.get("returncode")
        if type(code) is not int or batch.get("status") != ("ok" if code == 0 else "failed"):
            raise ValueError("Invalid generation failure evidence")
        if code:
            failed.append(batch)
    if not failed or summary.get("failures") != len(failed):
        raise ValueError("Generation failure inventory differs")
    if any(batch.get("provider_failure_category") != "mineru_unavailable" for batch in failed):
        raise ValueError("Non-provider generation failure remains unresolved")
    return len(failed)


def require_preview_producer(producer, jobs_page, run_id, repository):
    if (producer.get("id") != int(run_id) or producer.get("head_branch") != "main"
            or producer.get("path") != ".github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml"
            or producer.get("event") not in {"schedule", "workflow_dispatch"}
            or producer.get("repository", {}).get("full_name") != repository
            or producer.get("head_repository", {}).get("full_name") != repository
            or not re.fullmatch(r"[a-f0-9]{40}", producer.get("head_sha", ""))):
        raise ValueError("Source edition producer is not the exact main Daily run")
    jobs = jobs_page.get("jobs", [])
    if jobs_page.get("total_count") != len(jobs) or len(jobs) > 100:
        raise ValueError("Source edition jobs inventory is incomplete")
    matches = [job for job in jobs if job.get("name") == "recover-market-sources"]
    if len(matches) != 1:
        raise ValueError("Source edition recovery job is ambiguous")
    job = matches[0]
    if job.get("run_id") != int(run_id) or job.get("head_sha") != producer["head_sha"]:
        raise ValueError("Source edition recovery job identity differs")
    for name in ("Prepare bounded original-page edition", "Save bounded original-page edition to private R2"):
        steps = [step for step in job.get("steps", []) if step.get("name") == name]
        if len(steps) != 1 or steps[0].get("status") != "completed" or steps[0].get("conclusion") != "success":
            raise ValueError("Source edition recovery gate did not succeed")
    return producer["head_sha"]


def verify_frozen_daily(run, jobs_page, run_id, repository):
    if (run.get('id') != int(run_id) or run.get('head_branch') != 'main'
            or run.get('path') != '.github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml'
            or run.get('event') not in {'schedule', 'workflow_dispatch'}
            or run.get('status') != 'completed'
            or run.get('repository', {}).get('full_name') != repository
            or run.get('head_repository', {}).get('full_name') != repository
            or not re.fullmatch('[a-f0-9]{40}', run.get('head_sha', ''))):
        raise ValueError('Frozen original producer is not an exact completed main Daily')
    jobs = jobs_page.get('jobs', [])
    if jobs_page.get('total_count') != len(jobs) or len(jobs) > 100:
        raise ValueError('Frozen producer job inventory is incomplete')
    matches = [job for job in jobs if job.get('name') == 'select-macro-reports']
    if len(matches) != 1:
        raise ValueError('Frozen source selection is ambiguous')
    job = matches[0]
    if (job.get('run_id') != int(run_id) or job.get('head_sha') != run['head_sha']
            or job.get('status') != 'completed' or job.get('conclusion') != 'success'):
        raise ValueError('Frozen source selection did not succeed')
    matches = [step for step in job.get('steps', []) if step.get('name') == 'Upload selected macro PDFs artifact']
    if len(matches) != 1 or matches[0].get('conclusion') != 'success':
        raise ValueError('Frozen originals were not uploaded completely')
    return run['head_sha']


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--jobs", help="Evaluate a saved jobs response without network access")
    source.add_argument("--repository", help="Read and hydrate live GitHub jobs for owner/repository")
    parser.add_argument("--timeout", type=float, default=180)
    parser.add_argument("--poll-interval", type=float, default=5)
    parser.add_argument("--selected-count", type=int)
    parser.add_argument("--expected-shards", type=int, required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--execution-sha", required=True)
    args = parser.parse_args()
    if args.jobs:
        with open(args.jobs, encoding="utf-8") as handle:
            result = evaluate(json.load(handle), args.expected_shards, args.run_id, args.execution_sha, args.selected_count)
    else:
        result = evaluate_live(args.repository, args.expected_shards, args.run_id, args.execution_sha,
                               args.selected_count, timeout=args.timeout, poll_interval=args.poll_interval)
    print(f"primary_ready={str(result['primary_ready']).lower()}")
    print(f"degraded_shards={result['degraded_shards']}")
    print(f"provider_only={str(result['provider_only']).lower()}")

    print(f"no_work={str(result['no_work']).lower()}")
