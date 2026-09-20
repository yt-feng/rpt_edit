#!/usr/bin/env python3
"""Compare official Hy-MT2 GGUF on public samples, only on an Actions CPU runner.

No phrase overrides, placeholders or paid fallback are applied. Each result is
saved immediately, with human semantic review still required even after a green
workflow. The localhost server exists only on the remote Actions runner.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import http.client
import json
import os
from pathlib import Path
import platform
import re
import resource
import subprocess
import time


LANGUAGES = {"zh": "Chinese", "en": "English", "ko": "Korean", "ja": "Japanese", "ar": "Arabic"}
SCRIPT_PATTERNS = {
    "zh": r"[\u3400-\u9fff]", "en": r"[A-Za-z]", "ko": r"[\uac00-\ud7af]",
    "ja": r"[\u3040-\u30ff\u3400-\u9fff]", "ar": r"[\u0600-\u06ff]",
}


def require_actions() -> None:
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("RUNNER_OS") != "Linux":
        raise RuntimeError("Model inference is restricted to Linux GitHub Actions runners")


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_model(path: Path, manifest: dict) -> str:
    actual = file_sha256(path)
    if actual != manifest["model"]["sha256"]:
        raise ValueError("Model SHA256 does not match the pinned official Q8_0 artifact")
    return actual


def load_samples(path: Path) -> list[dict]:
    samples = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(samples, list) or not samples:
        raise ValueError("Expected a nonempty public sample list")
    ids = set()
    for sample in samples:
        if not re.fullmatch(r"[a-z0-9-]+", sample["id"]) or sample["id"] in ids:
            raise ValueError("Sample ids must be unique, simple identifiers")
        ids.add(sample["id"])
        if sample["source_language"] not in LANGUAGES or sample["target_language"] not in LANGUAGES:
            raise ValueError("Unsupported sample language")
        if not isinstance(sample["text"], str) or not sample["text"].strip():
            raise ValueError("Empty source sample")
    return samples


def translation_request(sample: dict, manifest: dict) -> dict:
    # Full official language names; keep figures and complete propositions in
    # context instead of replacing numbers/dates with disconnected fragments.
    prompt = (
        f"Translate the following text into {LANGUAGES[sample['target_language']]}. "
        "Note that you should only output the translated result without any additional explanation:\n"
        + sample["text"]
    )
    return {
        "model": "hymt-comparison", "messages": [{"role": "user", "content": prompt}],
        "stream": False, "cache_prompt": False, **manifest["sampling"],
    }


def request_json(port: int, route: str, payload: dict | None = None, timeout: float = 30) -> dict:
    # http.client connects directly to this runner's own server; no API account
    # or environment-derived provider URL participates in inference.
    connection = http.client.HTTPConnection("127.0.0.1", port, timeout=timeout)
    try:
        body = json.dumps(payload).encode("utf-8") if payload is not None else None
        connection.request("POST" if payload is not None else "GET", route,
                           body=body, headers={"Content-Type": "application/json"})
        response = connection.getresponse()
        data = response.read()
        if response.status != 200:
            raise RuntimeError(f"llama-server returned HTTP {response.status}: {data[:1000].decode(errors='replace')}")
        return json.loads(data)
    finally:
        connection.close()


def structural_issues(sample: dict, response: dict) -> list[str]:
    choice = response["choices"][0]
    text = choice["message"].get("content") or ""
    issues = []
    if not text.strip():
        issues.append("empty_translation")
    elif not re.search(SCRIPT_PATTERNS[sample["target_language"]], text):
        issues.append("target_script_missing")
    if sample["target_language"] == "en" and re.search(SCRIPT_PATTERNS["zh"], text):
        issues.append("untranslated_chinese_in_english_output")
    if choice.get("finish_reason") != "stop":
        issues.append(f"incomplete_finish_reason:{choice.get('finish_reason')}")
    return issues


def write_report(output: Path, report: dict) -> None:
    output.mkdir(parents=True, exist_ok=True)
    temporary = output / "diagnostics.json.tmp"
    temporary.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(output / "diagnostics.json")
    model = report["manifest"]["model"]
    runtime = report["manifest"]["runtime"]
    lines = [
        "# Hy-MT2 public translation comparison", "",
        f"Execution: **{report['status']}**. Semantic review: **pending human review**.", "",
        "Passing structural checks does not verify financial meaning. No approved phrase overrides are used.", "",
        f"Model: [{model['repository']} {model['quantization']}]({model['source_url']}); "
        f"[license: {model['license']}]({model['license_url']}).",
        f"Runtime: [{runtime['repository']} {runtime['version']}]({runtime['source_url']}), CPU only.", "",
        f"Model SHA256: `{model['sha256']}`.",
        f"Total elapsed seconds: {report.get('elapsed_seconds', 0)}; "
        f"samples completed: {len(report['samples'])}/{report['sample_count']}; paid provider requests: 0.", "",
    ]
    for sample in report["samples"]:
        lines += [
            f"## {sample['id']} ({sample['source_language']} → {sample['target_language']})", "",
            f"Status: {sample['status']}; seconds: {sample.get('elapsed_seconds', 0)}.", "",
            "Source:", "", sample["text"], "", "Translation:", "",
            sample.get("translation") or "(No translation produced)", "",
            f"Review criteria: {sample.get('review_notes', '')}", "",
        ]
        if sample.get("error"):
            lines += [f"Error: {sample['error']}", ""]
        if sample.get("structural_issues"):
            lines += [f"Structural issues: {', '.join(sample['structural_issues'])}", ""]
    if report["errors"]:
        lines += ["## Execution errors", ""] + [f"- {error}" for error in report["errors"]] + [""]
    (output / "review.md").write_text("\n".join(lines), encoding="utf-8")


def run_comparison(args: argparse.Namespace) -> int:
    require_actions()
    started = time.monotonic()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    samples = load_samples(args.samples)
    report = {
        "status": "running", "semantic_review": "pending-human-review", "manifest": manifest,
        "sample_count": len(samples), "samples_sha256": file_sha256(args.samples),
        "samples": [], "errors": [], "provider_requests": 0, "api_cost_cny": 0,
        "started_at": datetime.now(timezone.utc).isoformat(),
        "runner": {"platform": platform.platform(), "cpu_count": os.cpu_count(), "threads": args.threads},
        "github_run_id": os.environ.get("GITHUB_RUN_ID", ""),
        "github_run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT", ""),
        "github_sha": os.environ.get("GITHUB_SHA", ""),
    }
    write_report(args.output_dir, report)
    process = None
    log_handle = None
    try:
        report["verified_model_sha256"] = verify_model(args.model, manifest)
        actual_revision = subprocess.check_output(
            ["git", "-C", str(args.runtime_source), "rev-parse", "HEAD"], text=True, timeout=30,
        ).strip()
        if actual_revision != manifest["runtime"]["revision"]:
            raise ValueError("llama.cpp checkout does not match pinned official runtime revision")
        report["verified_runtime_revision"] = actual_revision
        report["runtime_version_output"] = subprocess.check_output(
            [str(args.server_bin), "--version"], text=True, stderr=subprocess.STDOUT, timeout=30,
        ).strip()
        command = [
            str(args.server_bin), "--model", str(args.model), "--alias", "hymt-comparison",
            "--host", "127.0.0.1", "--port", str(args.port), "--gpu-layers", "0", "--device", "none",
            "--threads", str(args.threads), "--threads-batch", str(args.threads),
            "--ctx-size", "8192", "--parallel", "1", "--cache-ram", "0", "--jinja", "--offline",
        ]
        report["server_command"] = command
        log_handle = (args.output_dir / "llama-server.log").open("w", encoding="utf-8")
        loading_started = time.monotonic()
        process = subprocess.Popen(command, stdout=log_handle, stderr=subprocess.STDOUT)
        while True:
            if process.poll() is not None:
                raise RuntimeError(f"llama-server exited during startup: {process.returncode}; see llama-server.log")
            if time.monotonic() - loading_started > args.startup_timeout:
                raise TimeoutError("llama-server startup exceeded its time budget")
            try:
                request_json(args.port, "/health", timeout=2)
                break
            except (OSError, RuntimeError, json.JSONDecodeError):
                time.sleep(1)
        report["model_load_seconds"] = round(time.monotonic() - loading_started, 3)
        for sample in samples:
            remaining = args.max_seconds - (time.monotonic() - started)
            if remaining <= 0:
                raise TimeoutError("Comparison exceeded total time budget; completed samples were retained")
            row = {**sample, "semantic_review": "pending-human-review", "reviewed_override": False}
            sample_started = time.monotonic()
            stop_after_sample = False
            try:
                response = request_json(
                    args.port, "/v1/chat/completions", translation_request(sample, manifest),
                    timeout=min(args.sample_timeout, remaining),
                )
                row["translation"] = response["choices"][0]["message"].get("content") or ""
                row["raw_response"] = response
                row["timings"] = response.get("timings", {})
                row["usage"] = response.get("usage", {})
                row["structural_issues"] = structural_issues(sample, response)
                row["status"] = "structural-check-failed" if row["structural_issues"] else "generated-review-required"
                if row["structural_issues"]:
                    report["errors"].append(f"{sample['id']}: {', '.join(row['structural_issues'])}")
            except Exception as error:
                row["status"] = "failed"
                row["error"] = f"{type(error).__name__}: {error}"
                report["errors"].append(f"{sample['id']}: {row['error']}")
                # A disconnected request may still be computing. Terminate the
                # server instead of queuing further samples behind that work.
                stop_after_sample = isinstance(error, (OSError, http.client.HTTPException))
            row["elapsed_seconds"] = round(time.monotonic() - sample_started, 3)
            report["samples"].append(row)
            report["elapsed_seconds"] = round(time.monotonic() - started, 3)
            write_report(args.output_dir, report)
            print(f"{sample['id']}: {row['status']} ({row['elapsed_seconds']}s)", flush=True)
            if stop_after_sample:
                raise RuntimeError("Stopped after a server transport failure; completed samples were retained")
    except Exception as error:
        report["errors"].append(f"{type(error).__name__}: {error}")
    finally:
        if process is not None:
            if process.poll() is None:
                process.terminate()
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait(timeout=10)
            report["server_exit_code"] = process.returncode
        if log_handle is not None:
            log_handle.close()
        report["child_peak_rss_kib"] = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
        report["elapsed_seconds"] = round(time.monotonic() - started, 3)
        report["status"] = "failed" if report["errors"] or len(report["samples"]) != len(samples) else "completed-review-required"
        write_report(args.output_dir, report)
    return int(report["status"] == "failed")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=Path(__file__).with_name("hymt_translation_model_manifest.json"))
    parser.add_argument("--samples", type=Path, default=Path(__file__).with_name("translation_quality_samples.json"))
    parser.add_argument("--model", type=Path, required=True)
    parser.add_argument("--runtime-source", type=Path, required=True)
    parser.add_argument("--server-bin", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--threads", type=int, default=4)
    parser.add_argument("--port", type=int, default=18088)
    parser.add_argument("--startup-timeout", type=int, default=180)
    parser.add_argument("--sample-timeout", type=int, default=180)
    parser.add_argument("--max-seconds", type=int, default=1800)
    return run_comparison(parser.parse_args())


if __name__ == "__main__":
    raise SystemExit(main())
