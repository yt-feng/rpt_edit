#!/usr/bin/env python3
"""Read actual matrix outcomes before selecting the normal or degraded edition."""
import argparse
import json
import re


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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--jobs", required=True)
    parser.add_argument("--selected-count", type=int)
    parser.add_argument("--expected-shards", type=int, required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--execution-sha", required=True)
    args = parser.parse_args()
    result = evaluate(json.load(open(args.jobs)), args.expected_shards, args.run_id, args.execution_sha, args.selected_count)
    print(f"primary_ready={str(result['primary_ready']).lower()}")
    print(f"degraded_shards={result['degraded_shards']}")
    print(f"provider_only={str(result['provider_only']).lower()}")

    print(f"no_work={str(result['no_work']).lower()}")
