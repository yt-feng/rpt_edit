#!/usr/bin/env python3
"""Generate Zhihu-style articles for completed report output folders."""
from __future__ import annotations

import argparse
import os
import re
from pathlib import Path
from typing import Any

import requests

try:
    from finalize_outputs import sanitize_text, trim_source_text
except Exception:
    def sanitize_text(text: str) -> str:
        return text

    def trim_source_text(source_text: str, max_chars: int) -> str:
        source_text = re.sub(r"\n{3,}", "\n\n", source_text).strip()
        if len(source_text) <= max_chars:
            return source_text
        head_len = int(max_chars * 0.72)
        tail_len = int(max_chars * 0.22)
        return source_text[:head_len] + "\n\n[中间内容因长度限制已省略]\n\n" + source_text[-tail_len:]


def log(message: str) -> None:
    print(message, flush=True)


def parse_json_response(response: requests.Response, label: str) -> dict[str, Any]:
    try:
        data = response.json()
    except Exception as exc:
        raise RuntimeError(f"{label}: HTTP {response.status_code}, non-json response: {response.text[:500]}") from exc
    if response.status_code >= 400:
        raise RuntimeError(f"{label}: HTTP {response.status_code}, response={response.text[:1000]}")
    return data


def call_deepseek(prompt: str, args: argparse.Namespace, label: str) -> str:
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        return f"未检测到 DEEPSEEK_API_KEY。请复制 prompt_for_zhihu.md 手动生成：{label}\n"
    response = requests.post(
        args.deepseek_base_url.rstrip("/") + "/chat/completions",
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
        json={
            "model": args.model,
            "thinking": {"type": "disabled"},
            "temperature": 0.55,
            "messages": [
                {"role": "system", "content": "你是知乎行业研究长文作者，写作克制、有逻辑、有洞察，避免收益承诺和操作建议。"},
                {"role": "user", "content": prompt},
            ],
        },
        timeout=240,
    )
    data = parse_json_response(response, f"DeepSeek generate {label}")
    return sanitize_text(data["choices"][0]["message"]["content"].strip() + "\n")


def generate_zhihu_for_item(item_dir: Path, args: argparse.Namespace) -> dict[str, str]:
    source_path = item_dir / "source_mineru.md"
    template_path = Path(args.zhihu_prompt_template)
    status: dict[str, str] = {}
    if not source_path.exists():
        status["zhihu_error"] = "source_mineru.md not found"
        return status
    if not template_path.exists():
        status["zhihu_error"] = f"prompt template not found: {template_path}"
        return status
    source_text = trim_source_text(source_path.read_text(encoding="utf-8", errors="ignore"), args.zhihu_prompt_chars)
    prompt = sanitize_text(template_path.read_text(encoding="utf-8").format(target_length=args.zhihu_length, source_text=source_text))
    (item_dir / "prompt_for_zhihu.md").write_text(prompt, encoding="utf-8")
    try:
        article = call_deepseek(prompt, args, "Zhihu article")
    except Exception as exc:
        article = f"DeepSeek 生成知乎文章失败：{exc}\n\n请复制 prompt_for_zhihu.md 手动生成。\n"
        status["zhihu_error"] = str(exc)
    (item_dir / "zhihu_article.md").write_text(sanitize_text(article), encoding="utf-8")
    status["zhihu_article"] = "zhihu_article.md"
    status["prompt_for_zhihu"] = "prompt_for_zhihu.md"
    return status


def update_item_status(item_dir: Path, update: dict[str, str]) -> None:
    # Keep this lightweight; finalize_outputs.py will sanitize and update metadata later.
    try:
        import json
        status_path = item_dir / "status.json"
        status = {}
        if status_path.exists():
            try:
                status = json.loads(status_path.read_text(encoding="utf-8", errors="ignore"))
            except Exception:
                status = {}
        status.update(update)
        status_path.write_text(sanitize_text(json.dumps(status, ensure_ascii=False, indent=2)), encoding="utf-8")
    except Exception as exc:
        log(f"Could not update status for {item_dir}: {exc}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--model", default=os.getenv("DEEPSEEK_MODEL", "deepseek-v4-flash"))
    parser.add_argument("--deepseek-base-url", default=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    parser.add_argument("--zhihu-prompt-template", default="prompts/zhihu_report_article_prompt.md")
    parser.add_argument("--zhihu-prompt-chars", type=int, default=26000)
    parser.add_argument("--zhihu-length", type=int, default=2200)
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    count = 0
    for item_dir in sorted(p for p in output_dir.iterdir() if p.is_dir()):
        if not (item_dir / "source_mineru.md").exists():
            continue
        log(f"Generating Zhihu article for {item_dir.name}")
        update = generate_zhihu_for_item(item_dir, args)
        update_item_status(item_dir, update)
        if update.get("zhihu_article"):
            count += 1
    log(f"Generated Zhihu articles for {count} report folders.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
