"""Read Dropbox source metadata in Actions; never download report bodies."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from download_dropbox_latest_pdfs import (dropbox_access_token, list_folder,
    parse_date_folder, recent_date_folder_names, select_date_folder, validate_expected_date_folder)


def inspect(token, root, expected, *, reader=list_folder):
    entries = reader(token, root, recursive=False)
    names = recent_date_folder_names(entries)
    result = {'schema_version': 1, 'read_only': True, 'source_root': root,
              'expected_date_folder': expected, 'available_date_folders': names,
              'report_body_downloads': 0, 'source_writes': 0, 'latest_folders': []}
    for name in names[:3]:
        folder = select_date_folder(entries, name)
        path = folder.get('path_lower') or folder.get('path_display') or root.rstrip('/')+'/'+name
        rows = reader(token, path, recursive=True)
        files = [r for r in rows if r.get('.tag') == 'file']
        pdfs = [r for r in files if r.get('name', '').lower().endswith('.pdf')]
        modified = [r.get('server_modified', '') for r in files if r.get('server_modified')]
        result['latest_folders'].append({'date_folder': name, 'source_date': parse_date_folder(name).isoformat(),
             'files': len(files), 'pdfs': len(pdfs), 'total_bytes': sum(r.get('size', 0) for r in files),
             'newest_server_modified': max(modified) if modified else None})
    latest = select_date_folder(entries, '')
    result['selected_date_folder'] = latest['name']
    try:
        validate_expected_date_folder(latest, expected, 1)
        result['freshness'] = 'passed'
    except RuntimeError:
        result['freshness'] = 'blocked_source_date'
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', default='/zip_backup')
    parser.add_argument('--expected-date', required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    parse_date_folder(args.expected_date)
    try:
        result = inspect(dropbox_access_token(), args.root, args.expected_date)
    except Exception:
        # Provider error bodies, filenames and credentials remain private.
        result = {'schema_version': 1, 'read_only': True, 'source_root': args.root,
                  'report_body_downloads': 0, 'source_writes': 0, 'status': 'metadata_read_failed'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2)+'\n')
    print(json.dumps(result, sort_keys=True))
    return 1 if result.get('status') == 'metadata_read_failed' else 0


if __name__ == '__main__':
    raise SystemExit(main())
