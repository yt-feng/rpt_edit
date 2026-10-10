#!/usr/bin/env python3
"""Probe the configured vision contract once, using a generated public test chart."""
from __future__ import annotations

import argparse
import json
import os
import tempfile
from pathlib import Path
from urllib.parse import urlsplit

from PIL import Image, ImageDraw

import build_chart_search_index as chart


def inspect_configuration() -> dict:
    report = {
        "schema_version": 1, "probe_status": "configuration_invalid",
        "source": "generated_synthetic_chart", "provider_posts": 0,
        "storage_reads": 0, "storage_writes": 0, "endpoint_changed": False,
        "endpoint_path_kind": "unavailable", "reason": "configuration", "http_status": None,
    }
    try:
        client = chart.VisionClient(
            api_base=os.environ.get("VISION_INDEX_API_BASE_URL", ""),
            api_key=os.environ.get("VISION_INDEX_API_KEY", ""),
            model=os.environ.get("VISION_INDEX_MODEL", ""),
            timeout=90, retries=1, retry_backoff=1, min_interval=0,
            allow_redirects=False,
        )
    except Exception:
        return report
    path = urlsplit(client.endpoint).path
    report["endpoint_path_kind"] = (
        "root_chat_completions" if path == "/chat/completions" else
        "versioned_chat_completions" if path.endswith("/v1/chat/completions") else
        "other_chat_completions"
    )
    with tempfile.TemporaryDirectory(prefix="chart-config-probe-") as folder:
        image_path = Path(folder) / "synthetic-chart.png"
        image = Image.new("RGB", (640, 360), "white")
        draw = ImageDraw.Draw(image)
        draw.text((40, 20), "Synthetic test: units by year", fill="black")
        draw.line((50, 60, 50, 310, 600, 310), fill="black", width=3)
        for x, height, year in ((150, 70, "2024"), (300, 130, "2025"), (450, 210, "2026")):
            draw.rectangle((x, 310-height, x+60, 310), fill="blue")
            draw.text((x, 320), year, fill="black")
            draw.text((x, 290-height), str(height), fill="black")
        image.save(image_path)
        try:
            report["provider_posts"] = 1
            client.analyze(image_path)
        except chart.VisionConfigurationError as exc:
            report.update(probe_status="configuration_rejected", reason=exc.reason, http_status=exc.status)
        except chart.RetryableVisionError as exc:
            report.update(probe_status="service_or_response_failure", reason=chart.retryable_reason_code(exc))
        except chart.StableImageError:
            report.update(probe_status="synthetic_image_rejected", reason="image_contract")
        except Exception:
            report.update(probe_status="probe_failed", reason="internal")
        else:
            report.update(probe_status="accepted", reason="none", http_status=200)
        finally:
            client.session.close()
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    report = inspect_configuration()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, sort_keys=True))
    # A completed diagnostic is successful even when its result identifies a
    # rejected configuration. probe_status, not this exit code, is acceptance.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
