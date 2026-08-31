#!/usr/bin/env python3
"""Run pdf_to_xhs_batch.py in smaller chunks.

This wrapper is useful when an input folder contains many PDFs. MinerU batch upload
can return non-standard responses or hit service limits when too many files are
submitted at once. The wrapper can also process a deterministic shard so GitHub
Actions can run many shards in parallel.

It also skips already-converted PDFs by default. If an expected output folder
already has source_mineru.md, note.md, and wechat_article.md, the PDF is not sent
to MinerU again.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

PDFRecord = tuple[int, Path]
REPORT_MARKERS = {"note.md", "wechat_article.md"}
CHART_SOURCE_MARKERS = {"source_mineru.md", "status.json"}


def log(message: str) -> None:
    print(message, flush=True)


def as_bool(value: str | bool) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def slug(value: str) -> str:
    value = Path(value).name
    value = re.sub(r"\.pdf$", "", value, flags=re.IGNORECASE)
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-._")
    return value[:80] or "report"


def find_pdfs(input_dir: Path, output_dir: Path) -> list[Path]:
    output_resolved = output_dir.resolve()
    return sorted(
        p for p in input_dir.rglob("*.pdf")
        if p.is_file() and output_resolved not in p.resolve().parents
    )


def apply_shard_filter(pdfs: list[Path], args: argparse.Namespace) -> list[Path]:
    max_total = int(args.max_total_reports)
    if max_total > 0:
        pdfs = pdfs[:max_total]

    shard_index = int(args.shard_index)
    shard_count = int(args.shard_count)
    max_per_shard = int(args.max_reports_per_shard)
    if shard_count <= 1:
        return pdfs[:max_per_shard] if max_per_shard > 0 else pdfs
    if shard_index < 0 or shard_index >= shard_count:
        raise RuntimeError(f"Invalid shard_index={shard_index}; shard_count={shard_count}")

    if max_per_shard > 0:
        start = shard_index * max_per_shard
        end = start + max_per_shard
        return pdfs[start:end]

    return [pdf for idx, pdf in enumerate(pdfs) if idx % shard_count == shard_index]


def unique_batch_name(pdf: Path, index: int) -> str:
    safe = "".join(ch if ch.isalnum() or ch in "._-()[] " else "-" for ch in pdf.name).strip()
    return f"{index:04d}-{safe or 'report.pdf'}"


def expected_item_dir(output_dir: Path, pdf: Path, index: int) -> Path:
    return output_dir / slug(unique_batch_name(pdf, index))


def is_already_converted(item_dir: Path, *, chart_source_only: bool = False) -> bool:
    required = CHART_SOURCE_MARKERS if chart_source_only else {"source_mineru.md", *REPORT_MARKERS}
    return item_dir.is_dir() and all((item_dir / name).exists() for name in required)


def count_generated_report_dirs(output_dir: Path, *, chart_source_only: bool = False) -> int:
    if not output_dir.exists():
        return 0
    markers = CHART_SOURCE_MARKERS if chart_source_only else REPORT_MARKERS
    return sum(
        1 for path in output_dir.iterdir()
        if path.is_dir() and all((path / marker).exists() for marker in markers)
    )


def split_existing(
    records: list[PDFRecord],
    output_dir: Path,
    skip_existing: bool,
    *,
    chart_source_only: bool = False,
) -> tuple[list[PDFRecord], list[dict[str, str]]]:
    if not skip_existing:
        return records, []
    todo: list[PDFRecord] = []
    skipped: list[dict[str, str]] = []
    for index, pdf in records:
        item_dir = expected_item_dir(output_dir, pdf, index)
        if is_already_converted(item_dir, chart_source_only=chart_source_only):
            log(f"Skipping already converted PDF: {pdf.name} -> {item_dir}")
            skipped.append({"source": str(pdf), "expected_item_dir": str(item_dir), "reason": "already_converted"})
        else:
            todo.append((index, pdf))
    return todo, skipped


def copy_batch_to_temp(batch: list[PDFRecord], tmp_input: Path) -> list[dict[str, str]]:
    copied = []
    tmp_input.mkdir(parents=True, exist_ok=True)
    for stable_index, pdf in batch:
        target = tmp_input / unique_batch_name(pdf, stable_index)
        shutil.copy2(pdf, target)
        copied.append({"source": str(pdf), "batch_file": str(target), "stable_index": str(stable_index)})
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
        "--deepseek-max-attempts", str(args.deepseek_max_attempts),
        "--deepseek-retry-base-seconds", str(args.deepseek_retry_base_seconds),
        "--deepseek-retry-max-seconds", str(args.deepseek_retry_max_seconds),
        "--mineru-model", args.mineru_model,
        "--language", args.language,
        "--ocr", args.ocr,
        "--length", str(args.length),
        "--wechat-length", str(args.wechat_length),
        "--community-cta", args.community_cta,
        "--max-images", str(args.max_images),
        "--poll-timeout", str(args.poll_timeout),
        "--poll-interval", str(args.poll_interval),
        "--mineru-retries", str(args.mineru_retries),
        "--mineru-no-progress-timeout", str(args.mineru_no_progress_timeout),
        "--watermark", args.watermark,
    ]
    if not args.wechat_title_refine:
        cmd.append("--no-wechat-title-refine")
    if args.chart_source_only:
        cmd.append("--chart-source-only")
    return cmd


def run_batch(batch_index: int, batch: list[PDFRecord], args: argparse.Namespace) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix=f"pdf_batch_{batch_index:03d}_") as tmp:
        tmp_input = Path(tmp) / "pdfs"
        copied = copy_batch_to_temp(batch, tmp_input)
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


def write_summary(output_dir: Path, payload: dict[str, Any]) -> None:
    summary_path = output_dir / "batch_run_summary.json"
    summary_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def write_empty_summary(output_dir: Path, input_dir: Path, args: argparse.Namespace, total_pdf_count: int, skipped: list[dict[str, str]] | None = None) -> None:
    write_summary(output_dir, {
        "input_dir": str(input_dir),
        "total_pdf_count_before_shard": total_pdf_count,
        "pdf_count": 0,
        "generated_report_count": 0,
        "batch_size": int(args.batch_size),
        "shard_index": int(args.shard_index),
        "shard_count": int(args.shard_count),
        "max_reports_per_shard": int(args.max_reports_per_shard),
        "max_total_reports": int(args.max_total_reports),
        "skip_existing": as_bool(args.skip_existing),
        "chart_source_only": bool(args.chart_source_only),
        "skipped_existing_count": len(skipped or []),
        "skipped_existing": skipped or [],
        "failures": 0,
        "batches": [],
        "status": "empty_or_all_skipped",
    })


def main() -> int:
    parser = argparse.ArgumentParser(description="Run PDF-to-XHS workflow in smaller PDF batches.")
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--batch-size", type=int, default=5)
    parser.add_argument("--continue-on-batch-error", default="true")
    parser.add_argument("--shard-index", type=int, default=0)
    parser.add_argument("--shard-count", type=int, default=1)
    parser.add_argument("--max-reports-per-shard", type=int, default=0)
    parser.add_argument("--max-total-reports", type=int, default=0)
    parser.add_argument("--skip-existing", default="true")
    parser.add_argument(
        "--chart-source-only",
        action="store_true",
        help="Retain only MinerU source markdown and source chart images.",
    )

    parser.add_argument("--prompt-template", default="prompts/xhs_report_note_prompt.md")
    parser.add_argument("--wechat-prompt-template", default="prompts/wechat_report_article_prompt.md")
    parser.add_argument("--model", default=os.getenv("DEEPSEEK_MODEL", "deepseek-v4-flash"))
    parser.add_argument("--deepseek-base-url", default=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    parser.add_argument("--deepseek-max-attempts", type=int, default=int(os.getenv("DEEPSEEK_MAX_ATTEMPTS", "4")))
    parser.add_argument("--deepseek-retry-base-seconds", type=float, default=float(os.getenv("DEEPSEEK_RETRY_BASE_SECONDS", "4")))
    parser.add_argument("--deepseek-retry-max-seconds", type=float, default=float(os.getenv("DEEPSEEK_RETRY_MAX_SECONDS", "45")))
    parser.add_argument("--mineru-model", default="vlm")
    parser.add_argument("--language", default="en")
    parser.add_argument("--ocr", default="true")
    parser.add_argument("--length", type=int, default=1000)
    parser.add_argument("--wechat-length", type=int, default=1200)
    parser.add_argument(
        "--community-cta",
        default=(
            "更新信息参见portal.example.invalid"
        ),
    )
    parser.add_argument("--no-wechat-title-refine", dest="wechat_title_refine", action="store_false",
                        help="Skip the extra DeepSeek title-candidate pass in child batches.")
    parser.set_defaults(wechat_title_refine=True)
    parser.add_argument("--max-images", type=int, default=8)
    parser.add_argument("--poll-timeout", type=int, default=3600)
    parser.add_argument("--poll-interval", type=int, default=15)
    parser.add_argument("--mineru-retries", type=int, default=1)
    parser.add_argument("--mineru-no-progress-timeout", type=int, default=600)
    parser.add_argument("--watermark", default="KC桌面")
    args = parser.parse_args()

    input_dir = Path(args.input_dir).resolve()
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    all_pdfs = find_pdfs(input_dir, output_dir)
    if not all_pdfs:
        print(f"ERROR: No PDFs found under {input_dir}", file=sys.stderr)
        return 2

    sharded_pdfs = apply_shard_filter(all_pdfs, args)
    if not sharded_pdfs:
        log(f"Shard {args.shard_index}/{args.shard_count} has no PDFs. Nothing to do.")
        write_empty_summary(output_dir, input_dir, args, total_pdf_count=len(all_pdfs))
        return 0

    records: list[PDFRecord] = [(idx + 1, pdf) for idx, pdf in enumerate(sharded_pdfs)]
    records, skipped_existing = split_existing(
        records,
        output_dir,
        skip_existing=as_bool(args.skip_existing),
        chart_source_only=args.chart_source_only,
    )
    if not records:
        log(f"Shard {args.shard_index}/{args.shard_count}: all {len(sharded_pdfs)} PDFs are already converted. Skipping MinerU.")
        write_empty_summary(output_dir, input_dir, args, total_pdf_count=len(all_pdfs), skipped=skipped_existing)
        return 0

    batch_size = max(1, int(args.batch_size))
    continue_on_error = str(args.continue_on_batch_error).lower() in {"1", "true", "yes", "y", "on"}
    log(
        f"Found {len(all_pdfs)} total PDFs; shard {args.shard_index}/{args.shard_count} "
        f"has {len(sharded_pdfs)} PDFs, skips {len(skipped_existing)} already converted, "
        f"will process {len(records)} PDFs with batch_size={batch_size}."
    )

    summary: list[dict[str, Any]] = []
    failures = 0
    for start in range(0, len(records), batch_size):
        batch = records[start : start + batch_size]
        batch_index = start // batch_size + 1
        try:
            result = run_batch(batch_index, batch, args)
        except Exception as exc:
            result = {
                "batch_index": batch_index,
                "pdf_count": len(batch),
                "files": [str(p) for _idx, p in batch],
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

    generated_report_count = count_generated_report_dirs(
        output_dir,
        chart_source_only=args.chart_source_only,
    )

    write_summary(output_dir, {
        "input_dir": str(input_dir),
        "total_pdf_count_before_shard": len(all_pdfs),
        "pdf_count_before_skip": len(sharded_pdfs),
        "pdf_count": len(records),
        "generated_report_count": generated_report_count,
        "batch_size": batch_size,
        "shard_index": int(args.shard_index),
        "shard_count": int(args.shard_count),
        "max_reports_per_shard": int(args.max_reports_per_shard),
        "max_total_reports": int(args.max_total_reports),
        "skip_existing": as_bool(args.skip_existing),
        "chart_source_only": bool(args.chart_source_only),
        "skipped_existing_count": len(skipped_existing),
        "skipped_existing": skipped_existing,
        "failures": failures,
        "batches": summary,
    })
    if failures:
        log(f"Completed with {failures} failed batch(es). See {output_dir / 'batch_run_summary.json'}")
        if generated_report_count == 0:
            log("No publish-ready report directories were generated; treating this shard as failed.")
            return 2
        return 0 if continue_on_error else 2
    log(f"All batches completed successfully. Generated {generated_report_count} report directories.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
