"""Read one current IMF search response and prove pre-download hold selection."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import time
from types import SimpleNamespace

import requests
import fetch_institution_latest_pdfs as producer

MAX_FEED_BYTES = 1024 * 1024


class FeedStopped(ValueError):
    def __init__(self, message, *, status=None):
        super().__init__(message)
        self.status = status


class SingleFeedRequest:
    """Expose only the existing producer's one exact Coveo search POST."""
    def __init__(self, session):
        self.session, self.calls = session, 0

    def post(self, url, *, headers, json, timeout):
        if self.calls or url != producer.INSTITUTIONS['imf']['coveo_url']:
            raise FeedStopped('Feed request not permitted')
        self.calls += 1
        deadline = time.monotonic()+45
        try:
            with self.session.post(url, headers=headers, json=json, timeout=(10, min(timeout, 30)),
                                   allow_redirects=False, stream=True) as response:
                if response.status_code != 200:
                    raise FeedStopped('Feed response rejected', status=response.status_code)
                chunks, size = [], 0
                for part in response.iter_content(65536):
                    size += len(part)
                    if size > MAX_FEED_BYTES or time.monotonic() > deadline:
                        raise FeedStopped('Feed response exceeds bound')
                    chunks.append(part)
            import json as codec
            data = codec.loads(b''.join(chunks))
            if not isinstance(data, dict) or not isinstance(data.get('results'), list) or len(data['results']) > 60:
                raise FeedStopped('Feed response shape rejected')
            return SimpleNamespace(status_code=200, raise_for_status=lambda: None, json=lambda: data)
        except FeedStopped:
            raise
        except Exception:
            # Producer retry classification must never turn this diagnostic into
            # another request. Omit transport text and private response content.
            raise FeedStopped('Feed request stopped') from None


def source_hash(name):
    return hashlib.sha256(name.encode()).hexdigest()


def inspect(holds, archive, expected, *, session):
    if (not re.fullmatch(r'[a-f0-9]{64}', expected) or not isinstance(holds, dict)
            or type(holds.get('schema')) is not int or holds['schema'] != 1
            or not isinstance(holds.get('sources'), list) or len(holds['sources']) > 1000
            or not isinstance(holds.get('versions'), list)):
        raise FeedStopped('Hold export invalid')
    target = [row for row in holds['sources'] if isinstance(row, dict)
              and isinstance(row.get('source'), str) and source_hash(row['source']) == expected]
    if len(target) != 1:
        raise FeedStopped('Expected held source is absent or ambiguous')
    versions = producer.dependency_hold_versions(archive, holds['sources'], holds['versions'])
    reader = SingleFeedRequest(session)
    items = producer.collect_coveo_items(producer.INSTITUTIONS['imf'], reader, 30, 60)
    held, unresolved, others = set(), set(), set()
    for item in items:
        dedup = 'imf:'+(item['guid'] or item['source_url'])
        title = item['title'] or item['guid'] or item['source_url']
        name = f"IMF_{producer.slug(title)}_{producer.short_hash(dedup)}.pdf"
        key = source_hash(name)
        if producer.matches_dependency_hold(versions, name, item):
            held.add(key)
        elif any(row['source'] == name for row in holds['sources']):
            unresolved.add(key)
        else:
            others.add(key)
    return {'schema': 1, 'status': 'expected_source_held' if expected in held else 'expected_source_not_held',
            'expected_source_name_sha256': expected, 'expected_source_held': expected in held,
            'feed_queries': reader.calls, 'feed_items': len(items), 'held_source_names_sha256': sorted(held),
            'held_source_count': len(held), 'unmatched_held_source_names_sha256': sorted(unresolved),
            'other_source_count': len(others), 'pdf_gets': 0, 'landing_gets': 0,
            'provider_gets': 0, 'provider_posts': 0, 'production_writes': 0,
            'acceptance_scope': 'Current feed pre-download selection only; no publication or original-byte recovery'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--holds', type=Path, required=True)
    parser.add_argument('--archive', type=Path, default=Path('institution_feeds/institution_pdf_archive.jsonl'))
    parser.add_argument('--expected-source-name-sha256', required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.holds.stat().st_size > 256*1024 or args.output.exists():
        raise FeedStopped('Diagnostic input or output bound invalid')
    with requests.Session() as session:
        session.headers.update(producer.source_request_headers(producer.DEFAULT_USER_AGENT))
        result = inspect(json.loads(args.holds.read_bytes()), args.archive,
                         args.expected_source_name_sha256, session=session)
    args.output.write_text(json.dumps(result, sort_keys=True)+'\n')
    print(json.dumps(result, sort_keys=True))
    return 0 if result['expected_source_held'] else 1


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except Exception as error:
        report = {'status': 'feed_diagnostic_stopped', 'exception_class': type(error).__name__}
        if isinstance(error, FeedStopped) and type(error.status) is int:
            report['feed_http_status'] = error.status
        print(json.dumps(report))
        raise SystemExit(1) from None
