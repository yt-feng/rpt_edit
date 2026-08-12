#!/usr/bin/env python3
"""Turn MinerU chart images into a resumable, text-searchable index.

The model endpoint and credential are read only from environment variables.  The
generated public index contains descriptions and opaque image identifiers, never
local paths, upstream URLs, credentials, or provider metadata.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import io
import json
import os
import re
import shutil
import sys
import time
import unicodedata
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Callable, Iterable
from urllib.parse import urlsplit

import requests
from PIL import Image, UnidentifiedImageError


SCHEMA_VERSION = 1
ANALYSIS_VERSION = "chart-search-v2"
IMAGE_NAME_RE = re.compile(r"^source_image_(\d+)\.(?:png|jpe?g|webp)$", re.IGNORECASE)
DATE_FOLDER_RE = re.compile(r"^\d{6,8}$")
JSON_FENCE_RE = re.compile(r"^```(?:json)?\s*|\s*```$", re.IGNORECASE)
MAX_LIST_ITEMS = 20
MAX_FIELD_CHARS = 900
BEIJING = timezone(timedelta(hours=8))
BANK_ALIASES = (
    "goldman sachs", "j p morgan", "jp morgan", "jpmorgan", "morgan stanley",
    "deutsche bank", "bank of america", "bofa", "barclays", "bernstein",
    "jefferies", "nomura", "citi", "citigroup", "ubs", "hsbc", "gs", "jpm",
    "ms", "db", "barc", "jef", "nom",
)

PUBLISHABLE_CONTENT_KINDS = frozenset({
    "chart", "table", "data_map", "flow_diagram", "data_visual",
})
INVALID_REASON_CODES = frozenset({
    "author", "cover", "decorative", "disclaimer", "end_page", "photo",
    "pure_text", "references", "toc", "unreadable",
})
STRONG_INVALID_PAGE_RE = re.compile(
    r"(?:"
    r"\b(?:about\s+the\s+author|analyst\s+certification|biograph(?:y|ies)|"
    r"contents|copyright|disclaimer|important\s+disclosures?|legal\s+notice|"
    r"table\s+of\s+contents)\b|"
    r"作者(?:介绍|简介)|分析师(?:介绍|简介|声明)|版权声明|免责声明|法律声明|"
    r"目录页?|重要声明|风险提示"
    r")",
    re.IGNORECASE,
)

VISION_PROMPT = """你是金融研报图表索引器。只根据图片中可见的信息工作，不补写图片里没有的事实。
只有包含可核验数值、坐标、图例、表格数据，或明确节点关系的图表、数据表、数据地图、流程图，才是有效图表。
以下内容必须标记为非图表：封面/标题页、目录/索引页、作者或分析师简介、头像与联系方式、免责声明/法律声明/
风险提示/版权页、参考文献、纯文字段落或截图、章节分隔页、Logo/二维码/装饰图/照片、空白或严重裁切且无法理解的图片。
若是图表，做中英双语关键词友好的结构化提取：准确识别标题、坐标、图例、单位、时间区间、地区、公司、指标、
关键数字和走势。description 用简洁中文写 2 至 4 句，并保留图中重要英文专名。trend_summary 只陈述可见变化。
严格返回一个 JSON 对象，不要 Markdown，不要解释，字段如下：
{
  "is_chart": true,
  "content_kind": "chart/table/data_map/flow_diagram/data_visual/invalid",
  "quality_score": 0,
  "has_data_evidence": true,
  "invalid_reason": "none/cover/toc/author/disclaimer/pure_text/references/end_page/decorative/photo/unreadable",
  "title": "图表标题",
  "chart_type": "line/bar/table/map/flow/other",
  "description": "可搜索的事实描述",
  "trend_summary": "可见趋势",
  "metrics": ["指标"],
  "entities": ["公司或主体"],
  "periods": ["时间"],
  "geographies": ["地区"],
  "units": ["单位"],
  "keywords": ["中文关键词", "English keyword"]
}
quality_score 用 0 到 100 表示该图片作为独立、可搜索图表的有效程度；低于 60 时 is_chart 必须为 false。
无法辨认的字段用空字符串或空数组；is_chart=false 时仍返回全部字段，并准确填写 invalid_reason。"""


class VisionConfigurationError(RuntimeError):
    """The endpoint, credential, model, or request contract is misconfigured."""


class RetryableVisionError(RuntimeError):
    """A service-wide or transport failure that must never quarantine an image."""


class StableImageError(RuntimeError):
    """A deterministic image/input failure that may be quarantined across runs."""


class VisionCircuitOpen(RuntimeError):
    """Too many consecutive transient failures; stop before spending more calls."""


TRANSIENT_HTTP_STATUSES = {408, 409, 425, 429}
CONFIGURATION_HTTP_STATUSES = {401, 403, 404, 405}
IMAGE_ERROR_MARKERS = (
    "image", "media", "base64", "decode", "dimension", "pixel", "resolution",
    "too large", "file size", "unsupported format", "input content",
)
DEFAULT_CIRCUIT_BREAKER_THRESHOLD = 3


@dataclass(frozen=True)
class ChartCandidate:
    image_path: Path
    image_sha256: str
    report_ref: str
    report_id: str
    report_title: str
    date_folder: str
    ordinal: int


def now_iso() -> str:
    return datetime.now(BEIJING).isoformat(timespec="seconds")


def clean_text(value: Any, limit: int = MAX_FIELD_CHARS) -> str:
    text = " ".join(str(value or "").replace("\x00", " ").split())
    return text[:limit]


def clean_list(value: Any, *, item_limit: int = 160) -> list[str]:
    raw = value if isinstance(value, list) else []
    result: list[str] = []
    seen: set[str] = set()
    for item in raw:
        text = clean_text(item, item_limit)
        folded = text.casefold()
        if text and folded not in seen:
            seen.add(folded)
            result.append(text)
        if len(result) >= MAX_LIST_ITEMS:
            break
    return result


def load_json(path: Path, default: dict[str, Any]) -> dict[str, Any]:
    if not path.exists():
        return default
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Invalid JSON checkpoint: {path.name}") from exc
    return value if isinstance(value, dict) else default


def atomic_write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_title(value: Any) -> str:
    text = unicodedata.normalize("NFKC", clean_text(value, 500)).casefold()
    text = re.sub(r"\.pdf$", "", text, flags=re.IGNORECASE)
    return "".join(character for character in text if character.isalnum())


def normalize_title_words(value: Any) -> str:
    text = unicodedata.normalize("NFKC", clean_text(value, 500)).casefold()
    words: list[str] = []
    current: list[str] = []
    for character in text:
        if character.isalnum():
            current.append(character)
        elif current:
            words.append("".join(current))
            current = []
    if current:
        words.append("".join(current))
    return " ".join(words)


def title_keys(value: Any) -> set[str]:
    base = re.sub(r"\.pdf$", "", Path(str(value or "")).name, flags=re.IGNORECASE)
    stripped = re.sub(r"^(?:\d{1,4}[-_]){1,3}", "", base).strip()
    variants = {base, stripped}
    variants |= {re.sub(r"[-_\s~]+(?:20)?\d{6,8}$", "", item).strip() for item in list(variants)}
    keys: set[str] = set()
    aliases = sorted((normalize_title_words(alias) for alias in BANK_ALIASES), key=len, reverse=True)
    for variant in variants:
        normalized_words = normalize_title_words(variant)
        compact = normalize_title(normalized_words)
        if compact:
            keys.add(compact)
        for alias in aliases:
            if normalized_words.startswith(alias + " "):
                without_bank = normalize_title(normalized_words[len(alias) + 1 :])
                if without_bank:
                    keys.add(without_bank)
                break
    return keys


def title_from_source_filename(value: Any) -> str:
    name = Path(str(value or "")).name
    name = re.sub(r"\.pdf$", "", name, flags=re.IGNORECASE)
    return clean_text(name, 300)


def markdown_title(report_dir: Path) -> str:
    source = report_dir / "source_mineru.md"
    if not source.exists():
        return ""
    try:
        for line in source.read_text(encoding="utf-8", errors="ignore").splitlines()[:120]:
            stripped = line.strip()
            if stripped.startswith("#"):
                return clean_text(stripped.lstrip("#"), 300)
    except OSError:
        return ""
    return ""


def load_catalog_lookup(path: Path | None) -> dict[str, list[tuple[str, str]]]:
    if path is None or not path.exists():
        return {}
    catalog = load_json(path, {"items": []})
    lookup: dict[str, list[tuple[str, str]]] = {}
    for item in catalog.get("items", []):
        if not isinstance(item, dict):
            continue
        report_id = clean_text(item.get("id"), 64)
        if not report_id:
            continue
        display_title = clean_text(item.get("title") or item.get("filename"), 300)
        for candidate in (item.get("title"), item.get("filename"), item.get("title_zh")):
            for normalized in title_keys(candidate):
                lookup.setdefault(normalized, []).append((report_id, display_title))
    return lookup


def match_catalog_report(
    report_title: str,
    lookup: dict[str, list[tuple[str, str]]],
) -> tuple[str, str]:
    matches = {
        match
        for key in title_keys(report_title)
        for match in lookup.get(key, [])
    }
    if len(matches) == 1:
        return next(iter(matches))
    return "", report_title


def report_date_folder(report_dir: Path, root: Path, explicit: str) -> str:
    if explicit:
        return explicit
    for part in reversed(report_dir.relative_to(root).parts[:-1]):
        if DATE_FOLDER_RE.fullmatch(part):
            return part
    return root.name if DATE_FOLDER_RE.fullmatch(root.name) else ""


def iter_report_dirs(root: Path) -> Iterable[Path]:
    seen: set[Path] = set()
    for image in sorted(root.rglob("assets/source_image_*")):
        if not image.is_file() or not IMAGE_NAME_RE.fullmatch(image.name):
            continue
        report_dir = image.parent.parent
        if report_dir not in seen:
            seen.add(report_dir)
            yield report_dir


def discover_candidates(
    root: Path,
    catalog_lookup: dict[str, list[tuple[str, str]]],
    *,
    date_folder: str = "",
    max_per_report: int = 0,
) -> list[ChartCandidate]:
    candidates: list[ChartCandidate] = []
    for report_dir in iter_report_dirs(root):
        status = load_json(report_dir / "status.json", {}) if (report_dir / "status.json").exists() else {}
        source_title = title_from_source_filename(status.get("source_pdf"))
        report_title = source_title or markdown_title(report_dir) or clean_text(report_dir.name, 300)
        report_id, catalog_title = match_catalog_report(report_title, catalog_lookup)
        if catalog_title:
            report_title = catalog_title
        report_date = report_date_folder(report_dir, root, date_folder)
        report_ref_seed = report_id or f"{report_date}:{normalize_title(report_title)}"
        report_ref = hashlib.sha256(report_ref_seed.encode("utf-8")).hexdigest()[:24]
        images: list[tuple[int, Path]] = []
        for image in report_dir.glob("assets/source_image_*"):
            match = IMAGE_NAME_RE.fullmatch(image.name)
            if match and image.is_file():
                images.append((int(match.group(1)), image))
        for ordinal, image in sorted(images)[: max(0, max_per_report) or None]:
            candidates.append(
                ChartCandidate(
                    image_path=image,
                    image_sha256=sha256_file(image),
                    report_ref=report_ref,
                    report_id=report_id,
                    report_title=report_title,
                    date_folder=report_date,
                    ordinal=ordinal,
                )
            )
    return candidates


def validate_api_base(value: str) -> str:
    base = value.strip().rstrip("/")
    parsed = urlsplit(base)
    if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
        raise RuntimeError("Vision API base must be a credential-free HTTPS URL")
    if parsed.query or parsed.fragment:
        raise RuntimeError("Vision API base must not contain a query or fragment")
    return base if base.endswith("/chat/completions") else base + "/chat/completions"


def parse_model_json(value: Any) -> dict[str, Any]:
    if isinstance(value, list):
        value = "".join(
            clean_text(part.get("text"), 20_000)
            for part in value
            if isinstance(part, dict) and part.get("type") == "text"
        )
    text = str(value or "").strip()
    text = JSON_FENCE_RE.sub("", text).strip()
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start < 0 or end <= start:
            raise RuntimeError("Vision response did not contain JSON")
        payload = json.loads(text[start : end + 1])
    if not isinstance(payload, dict):
        raise RuntimeError("Vision response JSON must be an object")
    return payload


def model_boolean(value: Any, *, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    text = clean_text(value, 20).casefold()
    if text in {"true", "1", "yes", "y"}:
        return True
    if text in {"false", "0", "no", "n"}:
        return False
    return default


def bounded_score(value: Any, *, default: int = 0) -> int:
    try:
        score = int(round(float(value)))
    except (TypeError, ValueError):
        score = default
    return min(100, max(0, score))


def normalize_analysis(payload: dict[str, Any]) -> dict[str, Any]:
    is_chart = model_boolean(payload.get("is_chart"))
    chart_type = clean_text(payload.get("chart_type"), 60).casefold().replace("-", "_").replace(" ", "_")
    content_kind = clean_text(payload.get("content_kind"), 60).casefold().replace("-", "_").replace(" ", "_")
    if not content_kind and is_chart:
        if chart_type == "table":
            content_kind = "table"
        elif chart_type == "map":
            content_kind = "data_map"
        elif chart_type in {"flow", "flowchart", "flow_diagram"}:
            content_kind = "flow_diagram"
        else:
            content_kind = "chart"
    normalized = {
        "is_chart": is_chart,
        "content_kind": content_kind or "invalid",
        "quality_score": bounded_score(payload.get("quality_score"), default=100 if is_chart else 0),
        "has_data_evidence": model_boolean(payload.get("has_data_evidence"), default=is_chart),
        "invalid_reason": clean_text(payload.get("invalid_reason"), 60).casefold().replace("-", "_").replace(" ", "_"),
        "title": clean_text(payload.get("title"), 300),
        "chart_type": chart_type,
        "description": clean_text(payload.get("description")),
        "trend_summary": clean_text(payload.get("trend_summary"), 500),
        "metrics": clean_list(payload.get("metrics")),
        "entities": clean_list(payload.get("entities")),
        "periods": clean_list(payload.get("periods")),
        "geographies": clean_list(payload.get("geographies")),
        "units": clean_list(payload.get("units")),
        "keywords": clean_list(payload.get("keywords")),
    }
    return normalized


def is_publishable_chart(analysis: dict[str, Any]) -> bool:
    """Apply deterministic publication rules after the model classification."""
    if not analysis.get("is_chart"):
        return False
    if clean_text(analysis.get("content_kind"), 60) not in PUBLISHABLE_CONTENT_KINDS:
        return False
    if clean_text(analysis.get("invalid_reason"), 60) in INVALID_REASON_CODES:
        return False
    if bounded_score(analysis.get("quality_score")) < 60:
        return False
    if not model_boolean(analysis.get("has_data_evidence")):
        return False
    title = clean_text(analysis.get("title"), 300)
    description = clean_text(analysis.get("description"))
    if not title or not description:
        return False
    structured = sum(
        len(analysis.get(field) or [])
        for field in ("metrics", "entities", "periods", "geographies", "units")
        if isinstance(analysis.get(field), list)
    )
    if structured < 1:
        return False
    if STRONG_INVALID_PAGE_RE.search(f"{title} {description}"):
        return False
    return True


def encode_image(path: Path, max_edge: int = 1600) -> tuple[str, bytes]:
    with Image.open(path) as source:
        image = source.convert("RGB")
        if max(image.size) > max_edge:
            image.thumbnail((max_edge, max_edge), Image.Resampling.LANCZOS)
        output = io.BytesIO()
        image.save(output, format="JPEG", quality=86, optimize=True)
    return "image/jpeg", output.getvalue()


def response_error_text(response: requests.Response) -> str:
    """Return bounded error text only for classification; callers never persist it."""
    try:
        payload = response.json()
    except (ValueError, json.JSONDecodeError):
        payload = response.text
    if isinstance(payload, dict):
        error = payload.get("error")
        if isinstance(error, dict):
            payload = error.get("message") or error.get("code") or ""
        else:
            payload = error or payload.get("message") or ""
    return clean_text(payload, 2_000).casefold()


def classify_http_error(response: requests.Response) -> RuntimeError:
    status = int(response.status_code or 0)
    if status in TRANSIENT_HTTP_STATUSES or status >= 500:
        return RetryableVisionError(f"Vision service is temporarily unavailable (status={status})")
    if status in CONFIGURATION_HTTP_STATUSES:
        return VisionConfigurationError(f"Vision service configuration was rejected (status={status})")
    if 400 <= status < 500:
        detail = response_error_text(response)
        if status in {413, 415} or any(marker in detail for marker in IMAGE_ERROR_MARKERS):
            return StableImageError(f"Vision service rejected this image (status={status})")
        return VisionConfigurationError(f"Vision request contract was rejected (status={status})")
    return RetryableVisionError(f"Vision service returned an unexpected status ({status})")


class VisionClient:
    def __init__(
        self,
        *,
        api_base: str,
        api_key: str,
        model: str,
        timeout: float,
        retries: int,
        retry_backoff: float,
        min_interval: float,
    ) -> None:
        self.endpoint = validate_api_base(api_base)
        self.model = clean_text(model, 160)
        if not api_key.strip() or not self.model:
            raise VisionConfigurationError("Vision API key and model are required")
        self.timeout = timeout
        self.retries = max(1, retries)
        self.retry_backoff = max(0.1, retry_backoff)
        self.min_interval = max(0.0, min_interval)
        self.last_request_at = 0.0
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key.strip()}",
            "Content-Type": "application/json",
        })

    def analyze(self, path: Path) -> dict[str, Any]:
        try:
            mime, image_bytes = encode_image(path)
        except (UnidentifiedImageError, OSError, ValueError) as exc:
            raise StableImageError("Source image could not be decoded") from exc
        image_url = f"data:{mime};base64,{base64.b64encode(image_bytes).decode('ascii')}"
        payload = {
            "model": self.model,
            "messages": [{
                "role": "user",
                "content": [
                    {"type": "text", "text": VISION_PROMPT},
                    {"type": "image_url", "image_url": {"url": image_url}},
                ],
            }],
            "temperature": 0,
            "max_tokens": 1200,
            "response_format": {"type": "json_object"},
        }
        last_error: RetryableVisionError | None = None
        for attempt in range(1, self.retries + 1):
            response: requests.Response | None = None
            elapsed = time.monotonic() - self.last_request_at
            if elapsed < self.min_interval:
                time.sleep(self.min_interval - elapsed)
            try:
                self.last_request_at = time.monotonic()
                response = self.session.post(self.endpoint, json=payload, timeout=self.timeout)
            except (requests.Timeout, requests.ConnectionError, requests.RequestException) as exc:
                last_error = RetryableVisionError("Vision request failed at the transport layer")
                last_error.__cause__ = exc
            else:
                if not 200 <= response.status_code < 300:
                    classified = classify_http_error(response)
                    if isinstance(classified, (VisionConfigurationError, StableImageError)):
                        raise classified
                    last_error = classified
                else:
                    try:
                        body = response.json()
                    except (ValueError, json.JSONDecodeError) as exc:
                        last_error = RetryableVisionError("Vision service returned invalid JSON")
                        last_error.__cause__ = exc
                        body = None
                    if body is not None:
                        choices = body.get("choices") if isinstance(body, dict) else None
                        if not isinstance(choices, list) or not choices:
                            last_error = RetryableVisionError("Vision response had no choices")
                        else:
                            content = ((choices[0] or {}).get("message") or {}).get("content")
                            try:
                                return normalize_analysis(parse_model_json(content))
                            except (ValueError, RuntimeError, json.JSONDecodeError) as exc:
                                last_error = RetryableVisionError("Vision model content was not valid JSON")
                                last_error.__cause__ = exc

            if attempt < self.retries:
                retry_after = response.headers.get("Retry-After", "") if response is not None else ""
                try:
                    delay = float(retry_after)
                except ValueError:
                    delay = self.retry_backoff * (2 ** (attempt - 1))
                time.sleep(min(max(delay, 0.1), 30.0))
        raise last_error or RetryableVisionError("Vision request failed")


def state_is_reusable(record: Any) -> bool:
    return (
        isinstance(record, dict)
        and record.get("status") == "ok"
        and record.get("analysis_version") == ANALYSIS_VERSION
        and isinstance(record.get("analysis"), dict)
    )


def retry_due(record: Any) -> bool:
    if isinstance(record, dict) and record.get("status") == "quarantined":
        return False
    if not isinstance(record, dict) or record.get("status") != "error":
        return True
    retry_at = clean_text(record.get("next_retry_at"), 64)
    if not retry_at:
        return True
    try:
        return datetime.fromisoformat(retry_at) <= datetime.now(BEIJING)
    except ValueError:
        return True


def attempted_in_run(record: Any, attempt_run_id: str) -> bool:
    return (
        isinstance(record, dict)
        and bool(attempt_run_id)
        and clean_text(record.get("last_attempt_run_id"), 160) == attempt_run_id
    )


def save_search_asset(source: Path, destination_dir: Path, image_id: str) -> None:
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination = destination_dir / f"{image_id}.jpg"
    if destination.exists():
        return
    _mime, image_bytes = encode_image(source)
    temporary = destination.with_suffix(".jpg.tmp")
    temporary.write_bytes(image_bytes)
    os.replace(temporary, destination)


def chart_record(candidate: ChartCandidate, analysis: dict[str, Any]) -> dict[str, Any]:
    chart_id = hashlib.sha256(
        f"{candidate.report_ref}:{candidate.image_sha256}".encode("utf-8")
    ).hexdigest()[:32]
    return {
        "id": chart_id,
        "analysis_version": ANALYSIS_VERSION,
        "image_id": candidate.image_sha256,
        "ordinal": candidate.ordinal,
        "title": analysis["title"],
        "content_kind": analysis["content_kind"],
        "quality_score": analysis["quality_score"],
        "chart_type": analysis["chart_type"],
        "description": analysis["description"],
        "trend_summary": analysis["trend_summary"],
        "metrics": analysis["metrics"],
        "entities": analysis["entities"],
        "periods": analysis["periods"],
        "geographies": analysis["geographies"],
        "units": analysis["units"],
        "keywords": analysis["keywords"],
    }


def chart_search_text(report: dict[str, Any]) -> str:
    chunks: list[str] = [clean_text(report.get("title"), 300)]
    for chart in report.get("charts", []):
        if not isinstance(chart, dict):
            continue
        for key in (
            "analysis_version", "title", "content_kind", "chart_type", "description", "trend_summary", "metrics", "entities",
            "periods", "geographies", "units", "keywords",
        ):
            value = chart.get(key)
            if isinstance(value, list):
                chunks.extend(clean_text(item, 160) for item in value)
            else:
                chunks.append(clean_text(value))
    text = " ".join(chunk for chunk in chunks if chunk)
    return text[:12_000]


def previous_reports(index: dict[str, Any]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for report in index.get("reports", []):
        if not isinstance(report, dict):
            continue
        report_ref = clean_text(report.get("report_ref"), 64)
        if report_ref:
            result[report_ref] = report
    return result


def build_index(
    candidates: list[ChartCandidate],
    *,
    state: dict[str, Any],
    previous_index: dict[str, Any],
    state_path: Path,
    asset_output_dir: Path,
    analyze: Callable[[Path], dict[str, Any]],
    max_model_calls: int,
    retry_errors_now: bool = False,
    attempt_run_id: str = "",
    circuit_breaker_threshold: int = DEFAULT_CIRCUIT_BREAKER_THRESHOLD,
) -> tuple[dict[str, Any], dict[str, Any]]:
    state_items = state.setdefault("items", {})
    if not isinstance(state_items, dict):
        state_items = {}
        state["items"] = state_items
    reports = previous_reports(previous_index)
    model_calls = 0
    cache_hits = 0
    failures = 0
    deferred = 0
    charts_added = 0
    consecutive_transient_failures = 0
    attempt_run_id = clean_text(attempt_run_id, 160) or "local"
    circuit_breaker_threshold = max(2, int(circuit_breaker_threshold))
    state.pop("circuit_breaker", None)

    for candidate in candidates:
        deterministic_chart_id = hashlib.sha256(
            f"{candidate.report_ref}:{candidate.image_sha256}".encode("utf-8")
        ).hexdigest()[:32]
        previous_report = reports.get(candidate.report_ref)
        if isinstance(previous_report, dict):
            previous_report["charts"] = [
                row
                for row in previous_report.get("charts", [])
                if isinstance(row, dict) and clean_text(row.get("id"), 64) != deterministic_chart_id
            ]
        cached = state_items.get(candidate.image_sha256)
        analysis: dict[str, Any] | None = None
        if state_is_reusable(cached):
            analysis = normalize_analysis(cached["analysis"])
            cache_hits += 1
        elif isinstance(cached, dict) and cached.get("status") == "quarantined":
            deferred += 1
            continue
        elif attempted_in_run(cached, attempt_run_id):
            deferred += 1
            continue
        elif not retry_errors_now and not retry_due(cached):
            deferred += 1
            continue
        elif max_model_calls > 0 and model_calls >= max_model_calls:
            deferred += 1
            continue
        else:
            attempts = int(cached.get("attempts") or 0) + 1 if isinstance(cached, dict) else 1
            try:
                analysis = normalize_analysis(analyze(candidate.image_path))
                model_calls += 1
                consecutive_transient_failures = 0
                state_items[candidate.image_sha256] = {
                    "status": "ok",
                    "analysis_version": ANALYSIS_VERSION,
                    "attempts": attempts,
                    "last_attempt_run_id": attempt_run_id,
                    "updated_at_bjt": now_iso(),
                    "analysis": analysis,
                }
            except VisionConfigurationError:
                atomic_write_json(state_path, state)
                raise
            except Exception as exc:  # keep successful checkpoints and classify conservatively
                model_calls += 1
                failures += 1
                delay_hours = min(2 ** min(attempts, 6), 24)
                is_stable_image_error = isinstance(exc, StableImageError)
                previous_stable_runs = int(cached.get("stable_attempt_runs") or 0) if isinstance(cached, dict) else 0
                stable_attempt_runs = previous_stable_runs + 1 if is_stable_image_error else previous_stable_runs
                status = "quarantined" if is_stable_image_error and stable_attempt_runs >= 3 else "error"
                state_items[candidate.image_sha256] = {
                    "status": status,
                    "analysis_version": ANALYSIS_VERSION,
                    "attempts": attempts,
                    "stable_attempt_runs": stable_attempt_runs,
                    "failure_class": "stable_image" if is_stable_image_error else "transient",
                    "error_type": type(exc).__name__,
                    "last_attempt_run_id": attempt_run_id,
                    "next_retry_at": (datetime.now(BEIJING) + timedelta(hours=delay_hours)).isoformat(timespec="seconds"),
                    "updated_at_bjt": now_iso(),
                }
                atomic_write_json(state_path, state)
                if is_stable_image_error:
                    consecutive_transient_failures = 0
                else:
                    consecutive_transient_failures += 1
                    if consecutive_transient_failures >= circuit_breaker_threshold:
                        state["circuit_breaker"] = {
                            "opened_at_bjt": now_iso(),
                            "run_id": attempt_run_id,
                            "consecutive_transient_failures": consecutive_transient_failures,
                        }
                        atomic_write_json(state_path, state)
                        raise VisionCircuitOpen(
                            f"Vision circuit opened after {consecutive_transient_failures} consecutive transient failures"
                        ) from exc
                continue
            atomic_write_json(state_path, state)

        if not analysis or not is_publishable_chart(analysis):
            continue
        save_search_asset(candidate.image_path, asset_output_dir, candidate.image_sha256)
        report = reports.setdefault(candidate.report_ref, {
            "report_ref": candidate.report_ref,
            "report_id": candidate.report_id,
            "title": candidate.report_title,
            "date_folder": candidate.date_folder,
            "charts": [],
        })
        if candidate.report_id:
            report["report_id"] = candidate.report_id
        if candidate.report_title:
            report["title"] = candidate.report_title
        if candidate.date_folder:
            report["date_folder"] = candidate.date_folder
        charts = [chart for chart in report.get("charts", []) if isinstance(chart, dict)]
        record = chart_record(candidate, analysis)
        charts_by_id = {clean_text(chart.get("id"), 64): chart for chart in charts if chart.get("id")}
        if record["id"] not in charts_by_id:
            charts_added += 1
        charts_by_id[record["id"]] = record
        report["charts"] = sorted(
            charts_by_id.values(),
            key=lambda item: (int(item.get("ordinal") or 0), str(item.get("id") or "")),
        )

    normalized_reports: list[dict[str, Any]] = []
    for report in reports.values():
        charts = [chart for chart in report.get("charts", []) if isinstance(chart, dict)]
        if not charts:
            continue
        normalized = {
            "report_ref": clean_text(report.get("report_ref"), 64),
            "report_id": clean_text(report.get("report_id"), 64),
            "title": clean_text(report.get("title"), 300),
            "date_folder": clean_text(report.get("date_folder"), 16),
            "chart_count": len(charts),
            "charts": charts,
        }
        normalized["search_text"] = chart_search_text(normalized)
        normalized_reports.append(normalized)
    normalized_reports.sort(key=lambda item: (str(item.get("date_folder") or ""), str(item.get("title") or "")), reverse=True)
    index = {
        "schema_version": SCHEMA_VERSION,
        "updated_at_bjt": now_iso(),
        "report_count": len(normalized_reports),
        "item_count": sum(int(report.get("chart_count") or 0) for report in normalized_reports),
        "reports": normalized_reports,
    }
    state["schema_version"] = SCHEMA_VERSION
    state["analysis_version"] = ANALYSIS_VERSION
    state["updated_at_bjt"] = now_iso()
    candidate_hashes = {candidate.image_sha256 for candidate in candidates}
    retryable_count = 0
    stable_error_count = 0
    quarantined_count = 0
    unprocessed_count = 0
    for image_hash in candidate_hashes:
        record = state_items.get(image_hash)
        status = str(record.get("status") or "") if isinstance(record, dict) else ""
        if status == "error":
            if record.get("failure_class") == "stable_image":
                stable_error_count += 1
            else:
                retryable_count += 1
        elif status == "quarantined":
            quarantined_count += 1
        elif status != "ok":
            unprocessed_count += 1
    summary = {
        "schema_version": SCHEMA_VERSION,
        "candidate_count": len(candidates),
        "model_calls": model_calls,
        "cache_hits": cache_hits,
        "failures": failures,
        "deferred": deferred,
        "retryable_count": retryable_count,
        "stable_error_count": stable_error_count,
        "quarantined_count": quarantined_count,
        "unprocessed_count": unprocessed_count,
        "charts_added": charts_added,
        "report_count": index["report_count"],
        "item_count": index["item_count"],
    }
    return index, summary


def reconcile_report_ids(
    index: dict[str, Any],
    lookup: dict[str, list[tuple[str, str]]],
) -> None:
    for report in index.get("reports", []):
        if not isinstance(report, dict) or report.get("report_id"):
            continue
        report_id, catalog_title = match_catalog_report(clean_text(report.get("title"), 300), lookup)
        if report_id:
            report["report_id"] = report_id
            report["title"] = catalog_title
            report["search_text"] = chart_search_text(report)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, help="Materialized MinerU report root")
    parser.add_argument("--catalog", default="", help="Optional portal catalog for report-id matching")
    parser.add_argument("--date-folder", default="")
    parser.add_argument("--state", required=True)
    parser.add_argument("--previous-index", required=True)
    parser.add_argument("--output-index", required=True)
    parser.add_argument("--output-summary", required=True)
    parser.add_argument("--asset-output-dir", required=True)
    parser.add_argument("--max-images", type=int, default=0, help="Maximum new model calls per pass; 0 is unlimited")
    parser.add_argument("--retry-errors-now", action="store_true", help="Retry prior error checkpoints without waiting for next_retry_at")
    parser.add_argument("--max-per-report", type=int, default=0, help="Maximum images per report; 0 is unlimited")
    parser.add_argument("--timeout", type=float, default=90.0)
    parser.add_argument("--retries", type=int, default=4)
    parser.add_argument("--retry-backoff", type=float, default=1.5)
    parser.add_argument("--min-interval", type=float, default=0.4)
    parser.add_argument(
        "--attempt-run-id",
        default="",
        help="Stable execution id used to count image failures once per workflow run",
    )
    parser.add_argument(
        "--circuit-breaker-threshold",
        type=int,
        default=DEFAULT_CIRCUIT_BREAKER_THRESHOLD,
        help="Stop after this many consecutive transient image-call failures",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root)
    if not root.is_dir():
        raise RuntimeError("MinerU report root does not exist")
    state_path = Path(args.state)
    previous_index_path = Path(args.previous_index)
    catalog_path = Path(args.catalog) if args.catalog else None
    state = load_json(state_path, {"schema_version": SCHEMA_VERSION, "items": {}})
    previous_index = load_json(previous_index_path, {"schema_version": SCHEMA_VERSION, "reports": []})
    catalog_lookup = load_catalog_lookup(catalog_path)
    candidates = discover_candidates(
        root,
        catalog_lookup,
        date_folder=clean_text(args.date_folder, 16),
        max_per_report=max(0, args.max_per_report),
    )
    if not candidates:
        print("chart_candidates=0")
        atomic_write_json(Path(args.output_index), previous_index)
        atomic_write_json(Path(args.output_summary), {
            "schema_version": SCHEMA_VERSION,
            "candidate_count": 0,
            "model_calls": 0,
            "cache_hits": 0,
            "failures": 0,
            "deferred": 0,
            "retryable_count": 0,
            "stable_error_count": 0,
            "quarantined_count": 0,
            "unprocessed_count": 0,
            "charts_added": 0,
            "report_count": int(previous_index.get("report_count") or 0),
            "item_count": int(previous_index.get("item_count") or 0),
        })
        return 0

    client = VisionClient(
        api_base=os.environ.get("VISION_INDEX_API_BASE_URL", ""),
        api_key=os.environ.get("VISION_INDEX_API_KEY", ""),
        model=os.environ.get("VISION_INDEX_MODEL", ""),
        timeout=max(5.0, args.timeout),
        retries=max(1, args.retries),
        retry_backoff=max(0.1, args.retry_backoff),
        min_interval=max(0.0, args.min_interval),
    )
    index, summary = build_index(
        candidates,
        state=state,
        previous_index=previous_index,
        state_path=state_path,
        asset_output_dir=Path(args.asset_output_dir),
        analyze=client.analyze,
        max_model_calls=max(0, args.max_images),
        retry_errors_now=bool(args.retry_errors_now),
        attempt_run_id=(
            clean_text(args.attempt_run_id, 160)
            or clean_text(
                f"{os.environ.get('GITHUB_RUN_ID', '')}:{os.environ.get('GITHUB_RUN_ATTEMPT', '')}",
                160,
            ).strip(":")
            or "local"
        ),
        circuit_breaker_threshold=max(2, args.circuit_breaker_threshold),
    )
    reconcile_report_ids(index, catalog_lookup)
    atomic_write_json(state_path, state)
    atomic_write_json(Path(args.output_index), index)
    atomic_write_json(Path(args.output_summary), summary)
    print(
        "chart_index "
        f"candidates={summary['candidate_count']} model_calls={summary['model_calls']} "
        f"cache_hits={summary['cache_hits']} failures={summary['failures']} "
        f"deferred={summary['deferred']} retryable={summary['retryable_count']} "
        f"stable_errors={summary['stable_error_count']} "
        f"quarantined={summary['quarantined_count']} unprocessed={summary['unprocessed_count']} "
        f"reports={summary['report_count']} "
        f"charts={summary['item_count']}"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
