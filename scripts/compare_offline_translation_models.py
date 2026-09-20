#!/usr/bin/env python3
"""Compare pinned open translation models on Actions; never approve semantic quality automatically."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import time
from unittest import mock

HERE = Path(__file__).resolve().parent
MANIFEST = json.loads((HERE / "offline_translation_comparison_models.json").read_text())
SAMPLES = HERE / "translation_quality_samples.json"


def require_actions() -> None:
    if os.environ.get("GITHUB_ACTIONS") != "true":
        raise RuntimeError("Actual model download and inference are restricted to GitHub Actions")


def selected_samples(model: dict, path: Path = SAMPLES) -> list[dict]:
    return [row for row in json.loads(path.read_text()) if
            (model["source"] == "*" or row["source_language"] == model["source"]) and
            (model["target"] == "*" or row["target_language"] == model["target"])]


def split_clauses(text: str, source: str) -> list[str]:
    # This is an experimental context boundary, not a reviewed translation.
    # Keep numerical separators and English dates intact. The raw baseline is
    # always retained so clause splitting can be rejected when it loses context.
    if source != "zh":
        return [text]
    return [part for part in re.split(r"(?<=[，。；！？])", text) if part.strip()]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while block := stream.read(1024 * 1024):
            digest.update(block)
    return digest.hexdigest()


def provision(model: dict, root: Path) -> tuple[Path, dict]:
    require_actions()
    from huggingface_hub import snapshot_download
    from ctranslate2.converters import TransformersConverter

    root.mkdir(parents=True, exist_ok=True)
    receipt_path = root / "provenance.json"
    identity = {key: model[key] for key in ("model_id", "revision", "license", "family")}
    if receipt_path.is_file():
        receipt = json.loads(receipt_path.read_text())
        if (all(receipt.get(key) == value for key, value in identity.items())
                and all((root / relative).is_file() and sha256(root / relative) == expected
                        for relative, expected in receipt.get("files", {}).items())
                and (root / "ct2/model.bin").is_file()):
            return root, receipt
    patterns = ["README.md", "config.json", "generation_config.json", "pytorch_model.bin",
                "source.spm", "target.spm", "sentencepiece.bpe.model", "vocab.json",
                "tokenizer_config.json", "special_tokens_map.json"]
    source = Path(snapshot_download(model["model_id"], revision=model["revision"],
                                   allow_patterns=patterns, cache_dir=root / "download", max_workers=2))
    card = (source / "README.md").read_text()
    if not re.search(r"(?mi)^license:\s*" + re.escape(model["license"]) + r"\s*$", card):
        raise RuntimeError("Pinned model card license differs from the reviewed manifest")
    source_digest = sha256(source / "pytorch_model.bin")
    runtime = root / "ct2"
    TransformersConverter(str(source)).convert(str(runtime), quantization="int8", force=True)
    tokenizer = root / "tokenizer"
    tokenizer.mkdir(exist_ok=True)
    for path in source.iterdir():
        if path.name != "pytorch_model.bin" and path.is_file():
            shutil.copy2(path, tokenizer / path.name)
    files = {str(path.relative_to(root)): sha256(path) for folder in (runtime, tokenizer)
             for path in folder.rglob("*") if path.is_file()}
    receipt = {**identity, "quantization": "int8", "source_weights_sha256": source_digest,
               "attribution": "Helsinki-NLP / University of Helsinki, OPUS-MT (Tiedemann and Thottingal, 2020)" if model["family"] == "marian" else "Meta AI / M2M100",
               "model_card": f"https://huggingface.co/{model['model_id']}/blob/{model['revision']}/README.md",
               "files": files}
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n")
    shutil.rmtree(root / "download", ignore_errors=True)
    return root, receipt


class ComparisonEngine:
    def __init__(self, model: dict, root: Path):
        require_actions()
        import ctranslate2
        from transformers import AutoTokenizer
        self.config = model
        self.counters = {"requests": 0, "input_tokens": 0, "output_tokens": 0, "inference_seconds": 0.0}
        self.tokenizer = AutoTokenizer.from_pretrained(str(root / "tokenizer"), local_files_only=True)
        self.engine = ctranslate2.Translator(str(root / "ct2"), device="cpu", compute_type="int8",
                                            inter_threads=1, intra_threads=4)

    def translate_batch(self, texts: list[str], source: str, target: str) -> list[str]:
        family = self.config["family"]
        if family == "m2m100":
            self.tokenizer.src_lang = source
        encoded = [self.tokenizer.convert_ids_to_tokens(self.tokenizer.encode(self.config["source_prefix"] + text))
                   for text in texts]
        if any(len(tokens) > 512 for tokens in encoded):
            raise RuntimeError("Comparison sample exceeds input limit; no truncation allowed")
        kwargs = {"target_prefix": [[f"__{target}__"] for _ in texts]} if family == "m2m100" else {}
        started = time.monotonic()
        results = self.engine.translate_batch(encoded, beam_size=6, max_input_length=0,
                                             max_decoding_length=512, **kwargs)
        self.counters["requests"] += 1
        self.counters["input_tokens"] += sum(map(len, encoded))
        self.counters["output_tokens"] += sum(len(result.hypotheses[0]) for result in results)
        self.counters["inference_seconds"] += time.monotonic() - started
        outputs = []
        for result in results:
            tokens = result.hypotheses[0]
            if len(tokens) >= 512:
                raise RuntimeError("Decoder limit reached; sample could be incomplete")
            outputs.append(self.tokenizer.decode(self.tokenizer.convert_tokens_to_ids(tokens), skip_special_tokens=True))
        return outputs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", choices=MANIFEST, required=True)
    parser.add_argument("--model-root", type=Path, required=True)
    parser.add_argument("--diagnostics-out", type=Path, required=True)
    args = parser.parse_args()
    model = MANIFEST[args.model]
    report = {"model": model, "provider_requests": 0, "api_cost_cny": 0,
              "semantic_review": "pending-human-review", "status": "running", "samples": []}
    args.diagnostics_out.parent.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    try:
        root, receipt = provision(model, args.model_root)
        report["provenance"] = receipt
        engine = ComparisonEngine(model, root)
        from m2m100_offline_translation import M2M100OfflineTranslator
        structured = M2M100OfflineTranslator(cache_dir=args.model_root / "comparison-memo",
                                            engine_factory=lambda *_: engine)
        os.environ["HF_HUB_OFFLINE"] = "1"
        os.environ["TRANSFORMERS_OFFLINE"] = "1"
        with mock.patch("requests.sessions.Session.request", side_effect=AssertionError("Inference attempted HTTP")), \
             mock.patch("urllib.request.urlopen", side_effect=AssertionError("Inference attempted network")):
            for sample in selected_samples(model):
                source, target = sample["source_language"], sample["target_language"]
                row = {**sample, "variants": {}}
                for variant in ("whole_sentence", "independent_clauses", "production_structure_adapter"):
                    try:
                        before = dict(engine.counters)
                        variant_started = time.monotonic()
                        if variant == "production_structure_adapter":
                            output = structured.translate(sample["text"], target, source)
                        else:
                            chunks = split_clauses(sample["text"], source) if variant == "independent_clauses" else [sample["text"]]
                            output = " ".join(engine.translate_batch(chunks, source, target))
                        stats = {key: engine.counters[key] - before[key] for key in before}
                        stats["wall_seconds"] = time.monotonic() - variant_started
                        stats["output_tokens_per_second"] = round(stats["output_tokens"] / max(stats["inference_seconds"], 0.000001), 2)
                        row["variants"][variant] = {"translation": output, "semantic_review": "pending-human-review", "performance": stats}
                    except Exception as error:
                        row["variants"][variant] = {"error": str(error)}
                report["samples"].append(row)
                args.diagnostics_out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
        report["performance"] = engine.counters
        report["status"] = "inference-completed-semantic-review-pending"
        if any("error" in row["variants"]["whole_sentence"] for row in report["samples"]):
            raise RuntimeError("A raw model sample failed to execute; see per-sample diagnostics")
    except Exception as error:
        report["status"] = "failed"
        report["error"] = str(error)
        raise
    finally:
        report["seconds"] = round(time.monotonic() - started, 2)
        args.diagnostics_out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
        print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
