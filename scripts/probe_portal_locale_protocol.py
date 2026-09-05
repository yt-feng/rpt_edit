#!/usr/bin/env python3
"""Compare four bounded translation protocol controls without site or cache writes."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
import os
from pathlib import Path
import re
import sys
from typing import Any, Callable

import build_portal_locales as builder


SOURCE_TEXT = "上半年业绩低于预期。"
MAX_PROVIDER_REQUESTS = 4
MAX_OUTPUT_TOKENS = 1000


@dataclass(frozen=True)
class Control:
    name: str
    model: str
    locale: str
    structured: bool = False


def controls() -> tuple[Control, ...]:
    return (
        Control("flash-plain-ko", "deepseek-v4-flash", "ko"),
        Control("flash-plain-ar", "deepseek-v4-flash", "ar"),
        Control("flash-json-ko", "deepseek-v4-flash", "ko", True),
        Control("pro-plain-ko", "deepseek-v4-pro", "ko"),
    )


def request_payload(control: Control) -> dict[str, Any]:
    language = "韩语（한국어）" if control.locale == "ko" else "阿拉伯语（العربية）"
    system = f"请把用户提供的中文句子完整翻译成{language}。必须使用目标语言，不要复制原中文，不要解释。"
    if control.structured:
        system += '仅返回JSON对象 {"translations":[{"id":"0","text":"目标语言译文"}]}。保留字符串ID。'
        user = json.dumps({"task": f"把每项source_text翻译成{language}", "target_language": control.locale,
                           "items": [{"id": "0", "source_text": SOURCE_TEXT}]}, ensure_ascii=False)
    else:
        system += "仅返回译文，不要JSON或Markdown。"
        user = SOURCE_TEXT
    payload: dict[str, Any] = {
        "model": control.model, "thinking": {"type": "disabled"},
        "temperature": 0, "max_tokens": MAX_OUTPUT_TOKENS,
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
    }
    if control.structured:
        payload["response_format"] = {"type": "json_object"}
    return payload


def first_api_key() -> str:
    for name in builder.DEEPSEEK_KEY_ENV_NAMES:
        for part in re.split(r"[\n,;]+", os.getenv(name, "")):
            if part.strip():
                return part.strip()
    raise builder.TranslationError("A DeepSeek API key is required for the protocol probe")


def safe_text(value: Any, credential: str, limit: int = 1200) -> str:
    text = value if isinstance(value, str) else "unknown"
    if credential:
        text = text.replace(credential, "[redacted]")
    text = re.sub(r"(?i)\b(?:authorization|api[_ -]?key|bearer)\s*[:=]?\s*\S+", "[redacted]", text)
    text = "".join(character for character in text if character in "\n\t" or ord(character) >= 32)
    return text[:limit]


def run_probe(
    *, diagnostics_out: Path, base_url: str = "https://api.deepseek.com",
    transport: Callable[..., Any] | None = None,
) -> dict[str, Any]:
    state = builder.TranslationRun(max_requests=MAX_PROVIDER_REQUESTS)
    rows: list[dict[str, Any]] = []
    report: dict[str, Any] = {"schema_version": 1, "mode": "protocol", "source": SOURCE_TEXT, "cases": rows}
    credential = ""
    diagnostics_out.parent.mkdir(parents=True, exist_ok=True)

    def write_report() -> None:
        report.update({
            "status": "passed" if len(rows) == 4 and all(row["status"] == "passed" for row in rows) and not state.stop_reason else "failed",
            "provider_requests": state.data["provider_requests"],
            "max_provider_requests": MAX_PROVIDER_REQUESTS,
            "max_output_tokens_per_request": MAX_OUTPUT_TOKENS,
            "usage_totals": state.data["usage_totals"],
            "usage_unknown_responses": state.data["usage_unknown_responses"],
            "usage_partial_responses": state.data["usage_partial_responses"],
            "unobserved_provider_requests": state.data["unobserved_provider_requests"],
        })
        if state.stop_reason:
            report["stop_reason"] = safe_text(state.stop_reason, credential, 240)
        diagnostics_out.write_text(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")

    try:
        base_url = builder.validate_deepseek_base_url(base_url)
        credential = first_api_key()
        if transport is None:
            from deepseek_http import request_with_key_fallback
            transport = request_with_key_fallback
        _protected, unit = builder.unit_for_text(SOURCE_TEXT, "html:text:p")
        if unit is None:
            raise builder.TranslationError("Protocol control source has no translation unit")
        compact_unit = builder.TranslationUnit("0", unit.context, unit.source)
        for control in controls():
            if state.stop_reason:
                break
            payload = request_payload(control)
            try:
                request_id = state.reserve(payload)
            except builder.TranslationStopped:
                break
            row: dict[str, Any] = {
                "control_case": control.name, "requested_model": control.model,
                "locale": control.locale, "status": "failed", "http_status": None,
                "returned_model": "unknown", "finish_reason": "unknown", "usage": "unknown",
                "translation": "",
            }
            rows.append(row)
            try:
                response = transport(
                    base_url.rstrip("/") + "/chat/completions",
                    headers={"Content-Type": "application/json"}, payload=payload,
                    label=control.name, api_keys=[("configured", credential)],
                    timeout=120, max_attempts=1, allow_model_fallback=False,
                    logger=lambda _message: None,
                )
            except Exception as error:
                row["error"] = f"Provider transport failed ({type(error).__name__})"
                state.stop("Provider transport failed; stopped remaining controls")
                write_report()
                break
            state.response(request_id, control.locale, response)
            observation = state.data["responses"][-1]
            row.update({"http_status": observation["http_status"],
                        "finish_reason": safe_text(observation["finish_reason"], credential, 96),
                        "usage": observation["usage"], "usage_completeness": observation["usage_completeness"]})
            try:
                body = response.json()
                if isinstance(body, dict):
                    row["returned_model"] = safe_text(body.get("model"), credential, 96)
            except Exception:
                pass
            if row["http_status"] != 200:
                row["error"] = f"Provider HTTP {row['http_status']}"
                write_report()
                continue
            try:
                content = builder._response_content(response, control.name)
                row["translation"] = safe_text(content, credential)
                if control.structured:
                    translated = builder.parse_translation_batch(content, [compact_unit], control.locale)["0"]
                else:
                    translated = content.strip()
                    builder.validate_translation_quality(control.locale, unit, translated)
                row["translation"] = safe_text(translated, credential)
                row["status"] = "passed"
            except builder.TranslationError as error:
                row["error"] = safe_text(str(error), credential, 300)
            write_report()
    except builder.TranslationError as error:
        state.stop(safe_text(str(error), credential, 240))
    except Exception as error:
        state.stop(f"Protocol probe failed ({type(error).__name__})")
    finally:
        write_report()
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--diagnostics-out", type=Path, required=True)
    parser.add_argument("--deepseek-base-url", default=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    args = parser.parse_args()
    report = run_probe(diagnostics_out=args.diagnostics_out, base_url=args.deepseek_base_url)
    print(json.dumps({key: report[key] for key in ("status", "provider_requests", "max_provider_requests", "usage_totals")}))
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
