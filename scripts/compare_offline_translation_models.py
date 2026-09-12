#!/usr/bin/env python3
"""Actions-only full-sentence M2M100 comparison; produces evidence, never publishes.

Suggested isolated Actions environment: Ubuntu 24.04, Python 3.11.
  python -m pip install torch==2.8.0 --index-url https://download.pytorch.org/whl/cpu
  python -m pip install transformers==4.57.6 sentencepiece==0.2.1
  python /tmp/rpt_m2m100_cpu_experiment.py --diagnostics-out "$RUNNER_TEMP/m2m100.json"

The pinned official model card declares MIT. Model loading is refused outside
GitHub Actions to avoid consuming the user's concurrently used local computer.
"""
from __future__ import annotations

import argparse
from collections import Counter
import importlib.metadata
import json
import os
from pathlib import Path
import re
import time
import unicodedata
from unittest import mock

MODEL = "facebook/m2m100_418M"
REVISION = "55c2e61bbf05dfb8d7abccdc3fae6fc8512fd636"
CASES = [
    ("zh", "今年公司收入增长12.5%，营业利润率为8%。", ("ko", "ja", "ar")),
    ("en", "Operating cash flow rose by 15% in 2026.", ("ko", "ja", "ar", "zh")),
    ("zh", "2026年，经营活动产生的现金流增长了15%。", ("ko", "ja", "ar", "en")),
    ("en", "Revenue increased by 12.5% in 2026, while the operating profit margin was 8%.", ("ko", "ja", "ar", "zh")),
    ("zh", "阅读完整报告并查看图表数据。", ("ko", "ja", "ar")),
    ("en", "Revenue was USD 120 million and net profit declined by 3%.", ("zh",)),
]
SCRIPTS = {"ko": r"[\uac00-\ud7af]", "ja": r"[\u3040-\u30ff\u3400-\u9fff]",
           "ar": r"[\u0600-\u06ff]", "zh": r"[\u3400-\u9fff]", "en": r"[A-Za-z]"}


def numbers(text: str) -> Counter:
    text = "".join(str(unicodedata.decimal(c)) if c.isdecimal() else c for c in text)
    text = text.replace("٫", ".").replace("٬", ",")
    return Counter(re.findall(r"\d+(?:\.\d+)?", text))


def save(path: Path, report: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--diagnostics-out", required=True, type=Path)
    parser.add_argument("--cache-dir", type=Path, default=Path(os.getenv("RUNNER_TEMP", "/tmp")) / "m2m100-model")
    args = parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS") != "true":
        parser.error("This comparison is restricted to GitHub Actions; do not load the model on the local Mac")
    report = {"model": MODEL, "revision": REVISION, "model_card_license": "mit",
              "device": "cpu", "api_translation_requests": 0, "semantic_review": "pending",
              "status": "preparing", "samples": [], "errors": []}
    save(args.diagnostics_out, report)
    try:
        import torch
        from huggingface_hub import snapshot_download
        from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

        report["runtime"] = {name: importlib.metadata.version(name)
                             for name in ("torch", "transformers", "sentencepiece", "huggingface-hub")}
        torch.set_num_threads(4)
        torch.set_num_interop_threads(1)
        torch.manual_seed(0)
        started = time.monotonic()
        # Download only the one PyTorch weight file and its tokenizer/configs.
        # The repository's separate Rust weights are not needed.
        directory = snapshot_download(MODEL, revision=REVISION, cache_dir=args.cache_dir,
            allow_patterns=["README.md", "config.json", "generation_config.json", "pytorch_model.bin",
                            "sentencepiece.bpe.model", "special_tokens_map.json", "tokenizer_config.json", "vocab.json"],
            max_workers=2)
        report["model_download_seconds"] = round(time.monotonic() - started, 3)
        card = (Path(directory) / "README.md").read_text(encoding="utf-8")
        if not re.search(r"^license:\s*mit\s*$", card, re.MULTILINE | re.I):
            raise ValueError("Pinned model card no longer declares the expected MIT license")
        report["license_evidence"] = "license: mit in pinned official README.md"
        tokenizer = M2M100Tokenizer.from_pretrained(directory, local_files_only=True)
        model = M2M100ForConditionalGeneration.from_pretrained(directory, local_files_only=True,
                                                              torch_dtype=torch.float32).to("cpu").eval()
        report["status"] = "generating_samples"
        save(args.diagnostics_out, report)
        started = time.monotonic()
        # Inference keeps numbers and complete sentence context together.
        # Checks detect mechanical issues; they cannot certify semantic quality.
        with mock.patch("urllib.request.urlopen", side_effect=AssertionError("Network during inference")), \
             mock.patch("requests.sessions.Session.request", side_effect=AssertionError("HTTP during inference")), \
             torch.inference_mode():
            for source_language, source, targets in CASES:
                tokenizer.src_lang = source_language
                inputs = tokenizer(source, return_tensors="pt", truncation=False)
                if inputs.input_ids.shape[1] > 256:
                    raise ValueError("Comparison sentence exceeds the fixed token bound")
                for target in targets:
                    row = {"source_language": source_language, "target_language": target, "source": source,
                           "semantic_review": "pending"}
                    begin = time.monotonic()
                    outputs = model.generate(**inputs, forced_bos_token_id=tokenizer.get_lang_id(target),
                                             do_sample=False, num_beams=4, max_new_tokens=192)
                    text = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0].strip()
                    issues = []
                    if not text or text == source:
                        issues.append("empty_or_unchanged")
                    if not re.search(SCRIPTS[target], text):
                        issues.append("missing_target_script")
                    if numbers(source) != numbers(text):
                        issues.append("number_values_changed")
                    if outputs.shape[1] >= 193:
                        issues.append("output_limit_reached")
                    row.update(translation=text, structural_status="failed" if issues else "passed",
                               structural_issues=issues, seconds=round(time.monotonic() - begin, 3))
                    report["samples"].append(row)
                    save(args.diagnostics_out, report)
                    print(json.dumps(row, ensure_ascii=False), flush=True)
        report["inference_seconds"] = round(time.monotonic() - started, 3)
        report["status"] = "samples_ready_for_review"
        report["structural_failed_count"] = sum(row["structural_status"] == "failed" for row in report["samples"])
        return 0
    except Exception as error:
        report["status"] = "failed"
        report["errors"].append(f"{type(error).__name__}: {error}")
        return 1
    finally:
        save(args.diagnostics_out, report)


if __name__ == "__main__":
    raise SystemExit(main())
