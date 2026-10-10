#!/usr/bin/env python3
"""Inspect allowlisted models or probe one synthetic chart at the existing origin."""
from __future__ import annotations

import argparse
import json
import os
import re
import tempfile
from pathlib import Path
from urllib.parse import urlsplit

from PIL import Image, ImageDraw

import build_chart_search_index as chart

MODEL_ALLOWLIST = ('qwen3-vl-flash', 'qwen3-vl-plus', 'qwen-vl-plus', 'qwen-vl-max',
                   'qwen2.5-vl-72b-instruct')
MAX_RESPONSE_BYTES = 1024 * 1024
MAX_MODEL_ROWS = 10000


class DiagnosticError(ValueError):
    """Only fixed error categories are included in public reports."""


def strict_json(raw):
    def object_pairs(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise DiagnosticError('response_json')
            result[key] = value
        return result
    def invalid_constant(_):
        raise DiagnosticError('response_json')
    try:
        return json.loads(raw.decode('utf-8'), object_pairs_hook=object_pairs, parse_constant=invalid_constant)
    except (UnicodeDecodeError, ValueError, RecursionError):
        raise DiagnosticError('response_json') from None


def bounded_response_bytes(response):
    length = response.headers.get('Content-Length')
    if length is not None:
        if not isinstance(length, str) or not re.fullmatch(r'[0-9]{1,10}', length):
            raise DiagnosticError('response_length_invalid')
        if int(length) > MAX_RESPONSE_BYTES:
            raise DiagnosticError('response_too_large')
    raw = bytearray()
    for chunk in response.iter_content(chunk_size=16384):
        if not isinstance(chunk, bytes):
            raise DiagnosticError('response_body_invalid')
        if len(raw) + len(chunk) > MAX_RESPONSE_BYTES:
            raise DiagnosticError('response_too_large')
        raw.extend(chunk)
    # iter_content may decode compressed HTTP bodies; the decoded byte limit is
    # always enforced, while Content-Length describes their encoded wire bytes.
    if length is not None and not response.headers.get('Content-Encoding') and len(raw) != int(length):
        raise DiagnosticError('response_length_mismatch')
    return bytes(raw)


class BoundedResponse:
    def __init__(self, response):
        self.status_code = response.status_code
        self.headers = response.headers
        try:
            if type(self.status_code) is not int or not 100 <= self.status_code <= 599:
                raise DiagnosticError('http_status_invalid')
            if 200 <= self.status_code < 300 and self.status_code != 200:
                raise DiagnosticError('http_unexpected')
            self.raw = bounded_response_bytes(response)
        finally:
            response.close()

    def json(self):
        return strict_json(self.raw)

    @property
    def text(self):
        return self.raw.decode('utf-8', errors='replace')


class BoundedProbeSession:
    """Keep the normal request contract while bounding its diagnostic response."""
    def __init__(self, session):
        self.session = session

    def post(self, *args, **kwargs):
        return BoundedResponse(self.session.post(*args, **kwargs, stream=True))

    def close(self):
        self.session.close()


def base_report(operation):
    return {
        'schema_version': 1, 'operation': operation, 'probe_status': 'configuration_invalid',
        'source': 'generated_synthetic_chart' if operation == 'vision-config' else 'provider_model_metadata',
        'provider_posts': 0, 'provider_gets': 0, 'storage_reads': 0, 'storage_writes': 0,
        'endpoint_changed': False, 'endpoint_path_kind': 'unavailable', 'reason': 'configuration', 'http_status': None,
    }


def configured_client(model_override='', *, models=False):
    if model_override and model_override not in MODEL_ALLOWLIST:
        raise DiagnosticError('model_override_invalid')
    if models and model_override:
        raise DiagnosticError('model_override_not_applicable')
    return chart.VisionClient(
        api_base=os.environ.get('VISION_INDEX_API_BASE_URL', ''),
        api_key=os.environ.get('VISION_INDEX_API_KEY', ''),
        # /models does not select a model or send a model parameter.
        model='models-read-only' if models else model_override or os.environ.get('VISION_INDEX_MODEL', ''),
        timeout=90, retries=1, retry_backoff=1, min_interval=0, allow_redirects=False)


def path_kind(endpoint):
    path = urlsplit(endpoint).path
    return ('root_chat_completions' if path == '/chat/completions' else
            'versioned_chat_completions' if path.endswith('/v1/chat/completions') else 'other_chat_completions')


def inspect_models(model_override='') -> dict:
    report = {**base_report('vision-models'), 'available_models': []}
    try:
        client = configured_client(model_override, models=True)
    except DiagnosticError as exc:
        report['reason'] = str(exc)
        return report
    except Exception:
        return report
    response = None
    try:
        report['endpoint_path_kind'] = path_kind(client.endpoint)
        suffix = '/chat/completions'
        if not client.endpoint.endswith(suffix):
            raise DiagnosticError('models_path_invalid')
        endpoint = client.endpoint[:-len(suffix)] + '/models'
        # Slice only the normalized terminal path; origin, port and base prefix
        # remain exactly those already validated by the configured client.
        if urlsplit(endpoint).netloc != urlsplit(client.endpoint).netloc:
            raise DiagnosticError('models_path_invalid')
        report['provider_gets'] = 1
        response = client.session.get(endpoint, timeout=(15, 60), allow_redirects=False, stream=True)
        status = response.status_code
        if type(status) is not int or not 100 <= status <= 599:
            raise DiagnosticError('http_status_invalid')
        report['http_status'] = status
        if status != 200:
            report.update(probe_status='configuration_rejected' if status in {400, 401, 403, 404, 405} else
                          'service_or_response_failure', reason='authentication' if status in {401, 403} else
                          'models_route_unavailable' if status in {404, 405} else
                          'redirect_rejected' if 300 <= status < 400 else 'http_unexpected')
            return report
        payload = strict_json(bounded_response_bytes(response))
        if (not isinstance(payload, dict) or 'error' in payload or type(payload.get('data')) is not list
                or len(payload['data']) > MAX_MODEL_ROWS):
            raise DiagnosticError('models_response_shape')
        if (payload.get('has_more') is not None and payload.get('has_more') is not False) or payload.get('next') is not None:
            raise DiagnosticError('models_response_incomplete')
        ids = set()
        for row in payload['data']:
            if (not isinstance(row, dict) or not isinstance(row.get('id'), str)
                    or not 1 <= len(row['id']) <= 512 or row['id'].strip() != row['id']):
                raise DiagnosticError('models_response_shape')
            ids.add(row['id'])
        # Only fixed allowlisted identifiers can leave this function; never
        # publish unknown IDs, their count, provider fields or response contents.
        report.update(probe_status='accepted', reason='none',
                      available_models=[model for model in MODEL_ALLOWLIST if model in ids])
    except DiagnosticError as exc:
        report.update(probe_status='service_or_response_failure', reason=str(exc))
    except chart.requests.RequestException as exc:
        report.update(probe_status='service_or_response_failure', reason=chart.transport_reason_code(exc))
    except Exception:
        report.update(probe_status='probe_failed', reason='internal')
    finally:
        if response is not None:
            response.close()
        client.session.close()
    return report


def inspect_configuration(model_override='') -> dict:
    report = base_report('vision-config')
    try:
        client = configured_client(model_override)
    except DiagnosticError as exc:
        report['reason'] = str(exc)
        return report
    except Exception:
        return report
    report['endpoint_path_kind'] = path_kind(client.endpoint)
    report['model_selection'] = 'allowlisted_override' if model_override else 'configured'
    if model_override:
        report['model_override'] = model_override
    client.session = BoundedProbeSession(client.session)
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
        except DiagnosticError as exc:
            report.update(probe_status='service_or_response_failure', reason=str(exc))
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
    parser.add_argument('--operation', choices=('vision-config', 'vision-models'), default='vision-config')
    parser.add_argument('--model-override', default='')
    args = parser.parse_args()
    report = inspect_models(args.model_override) if args.operation == 'vision-models' else inspect_configuration(args.model_override)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, sort_keys=True))
    # A completed diagnostic is successful even when its result identifies a
    # rejected configuration. probe_status, not this exit code, is acceptance.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
