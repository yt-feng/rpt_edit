#!/usr/bin/env python3
"""Run pdf_to_xhs_batch.py in smaller chunks.

This wrapper is useful when an input folder contains many PDFs. MinerU batch upload
can return non-standard responses or hit service limits when too many files are
submitted at once. The wrapper copies a small group of PDFs into a temporary
folder and invokes the existing pipeline per group.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


def log(message: str) -> None:
    print(message, flush=True)


def find_pdfs(input_dir: Path, output_dir: Path) -> list[Path]:
    output_resolved = output_dir.resolve()
    return sorted(
        p for p in input_dir.rglob("*.pdf")
        if p.is_file() and output_resolved not in p.resolve().parents
    )


def unique_batch_name(pdf: Path, index: int) -> str:
    safe = "".join(ch if ch.isalnum() or ch in "._-()[] " else "-" for ch in pdf.name).strip()
    return f"{index:04d}-{safe or 'report.pdf'}"


def copy_batch_to_temp(batch: list[Path], tmp_input: Path, offset: int) -> list[dict[str, str]]:
    copied = []
    tmp_input.mkdir(parents=True, exist_ok=True)
    for i, pdf in enumerate(batch, offset + 1):
        target = tmp_input / unique_batch_name(pdf, i)
        shutil.copy2(pdf, target)
        copied.append({"source": str(pdf), "batch_file": str(target)})
    return copied


def build_child_command(args: argparse.Namespace, tmp_input: Path) -> list[str]:
    cmd = [
        sys.executable,
        "scripts/pdf_to_xhs_batch.py",
        "--input-dir", str(tmp_input),
        "--output-dir", args.output_dir,
        "--prompt-template", args.prompt_template,
        "--wechat-prompt-template", args.wechat_prompt_template,
        "--model", args.model,
        "--deepseek-base-url", args.deepseek_base_url,
        "--mineru-model", args.mineru_model,
        "--language", args.language,
        "--ocr", args.ocr,
        "--wechat-length", str(args.wechat_length),
        "--community-cta", args.community_cta,
        "--max-images", str(args.max_images),
        "--poll-timeout", str(args.poll_timeout),
        "--poll-interval", str(args.poll_interval),
        "--watermark", args.watermark,
    ]
    return cmd


def run_batch(batch_index: int, batch: list[Path], args: argparse.Namespace, offset: int) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix=f"pdf_batch_{batch_index:03d}_") as tmp:
        tmp_input = Path(tmp) / "pdfs"
        copied = copy_batch_to_temp(batch, tmp_input, offset)
        log(f"Running batch {batch_index}: {len(batch)} PDFs")
        cmd = build_child_command(args, tmp_input)
        result = subprocess.run(cmd, text=True)
        return {
            "batch_index": batch_index,
            "pdf_count": len(batch),
            "files": copied,
            "returncode": result.returncode,
            "status": "ok" if result.returncode == 0 else "failed",
        }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run PDF-to-XHS workflow in smaller PDF batches.")
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--batch-size", type=int, default=5)
    parser.add_argument("--continue-on-batch-error", default="true")

    parser.add_argument("--prompt-template", default="prompts/xhs_report_note_prompt.md")
    parser.add_argument("--wechat-prompt-template", default="prompts/wechat_report_article_prompt.md")
    parser.add_argument("--model", default=os.getenv("DEEPSEEK_MODEL", "deepseek-chat"))
    parser.add_argument("--deepseek-base-url", default=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    parser.add_argument("--mineru-model", default="vlm")
    parser.add_argument("--language", default="en")
    parser.add_argument("--ocr", default="true")
    parser.add_argument("--wechat-length", type=int, default=3000)
    parser.add_argument("--community-cta", default="加入社群，领取完整研报解读与原始图表。")
    parser.add_argument("--max-images", type=int, default=8)
    parser.add_argument("--poll-timeout", type=int, default=1800)
    parser.add_argument("--poll-interval", type=int, default=15)
    parser.add_argument("--watermark", default="KC桌面")
    args = parser.parse_args()

    input_dir = Path(args.input_dir).resolve()
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    pdfs = find_pdfs(input_dir, output_dir)
    if not pdfs:
        print(f"ERROR: No PDFs found under {input_dir}", file=sys.stderr)
        return 2

    batch_size = max(1, int(args.batch_size))
    continue_on_error = str(args.continue_on_batch_error).lower() in {"1", "true", "yes", "y", "on"}
    log(f"Found {len(pdfs)} PDFs. Running with batch_size={batch_size}.")

    summary: list[dict[str, Any]] = []
    failures = 0
    for start in range(0, len(pdfs), batch_size):
        batch = pdfs[start : start + batch_size]
        batch_index = start // batch_size + 1
        try:
            result = run_batch(batch_index, batch, args, offset=start)
        except Exception as exc:
            result = {
                "batch_index": batch_index,
                "pdf_count": len(batch),
                "files": [str(p) for p in batch],
                "returncode": 99,
                "status": "failed",
                "error": str(exc),
            }
        summary.append(result)
        if result.get("returncode") != 0:
            failures += 1
            log(f"Batch {batch_index} failed: {result}")
            if not continue_on_error:
                break

    summary_path = output_dir / "batch_run_summary.json"
    summary_path.write_text(json.dumps({"input_dir": str(input_dir), "pdf_count": len(pdfs), "batch_size": batch_size, "failures": failures, "batches": summary}, ensure_ascii=False, indent=2), encoding="utf-8")
    if failures:
        log(f"Completed with {failures} failed batch(es). See {summary_path}")
        return 0 if continue_on_error else 2
    log("All batches completed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
