#!/usr/bin/env python3
"""Download only redacted usage events for a dated Actions daily summary."""
from __future__ import annotations

import argparse
from datetime import date, datetime, time, timedelta, timezone
import io
import json
from pathlib import Path
import subprocess
import zipfile
from zoneinfo import ZoneInfo


def artifact_overlaps_day(artifact: dict, day: date, zone: ZoneInfo) -> bool:
    """A job may start on the requested day and upload after midnight."""
    created = datetime.fromisoformat(artifact['created_at'].replace('Z', '+00:00'))
    start = datetime.combine(day, time.min, zone).astimezone(timezone.utc)
    return start <= created < start + timedelta(days=2)


def extract_events(payload: bytes, destination: Path) -> int:
    """Flatten validated event JSON only; never extract paths or other artifacts."""
    count = 0
    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        for info in archive.infolist():
            if info.is_dir() or not info.filename.endswith('.json'):
                continue
            if info.file_size > 64_000:
                continue
            data = archive.read(info)
            try:
                event = json.loads(data)
            except (ValueError, UnicodeDecodeError):
                continue
            if not isinstance(event, dict) or not event.get('event_id'):
                continue
            # No ZIP path or event identifier is used as a local path.
            (destination / f'event-{count:08d}.json').write_bytes(data)
            count += 1
    return count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', required=True)
    parser.add_argument('--date', required=True)
    parser.add_argument('--timezone', default='Asia/Shanghai')
    parser.add_argument('--output-dir', required=True)
    args = parser.parse_args()
    day = date.fromisoformat(args.date)
    zone = ZoneInfo(args.timezone)
    root = Path(args.output_dir)
    root.mkdir(parents=True, exist_ok=True)
    start = datetime.combine(day, time.min, zone).astimezone(timezone.utc)
    artifacts = []
    for page in range(1, 101):
        result = subprocess.run(['gh', 'api', f'repos/{args.repo}/actions/artifacts?per_page=100&page={page}'], check=True, capture_output=True)
        batch = json.loads(result.stdout)['artifacts']
        for item in batch:
            if item['name'].startswith('deepseek-usage-') and not item['expired'] and artifact_overlaps_day(item, day, zone):
                artifacts.append(item)
        if len(batch) < 100 or all(datetime.fromisoformat(item['created_at'].replace('Z', '+00:00')) < start for item in batch):
            break
    else:
        raise RuntimeError('Artifact listing exceeded 100 pages; refusing an incomplete daily summary')
    count = 0
    for item in artifacts:
        result = subprocess.run(['gh', 'api', f'repos/{args.repo}/actions/artifacts/{int(item["id"])}/zip'], check=True, capture_output=True)
        destination = root / str(int(item['id']))
        destination.mkdir(exist_ok=True)
        count += extract_events(result.stdout, destination)
    manifest = {'date': day.isoformat(), 'timezone': args.timezone, 'artifacts_downloaded': len(artifacts), 'events_downloaded': count, 'coverage': 'Instrumented GitHub Actions calls only; not a provider invoice. In-flight jobs appear after artifact upload; rerun this summary to include late arrivals.'}
    (root / 'collection.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(manifest, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
