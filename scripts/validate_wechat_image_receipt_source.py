#!/usr/bin/env python3
"""Validate a successful receipt artifact without a runner-local GitHub CLI."""
from __future__ import annotations
import json
import os
import re
from urllib.error import HTTPError, URLError
from urllib.request import Request, HTTPRedirectHandler, build_opener


class ReceiptSourceError(ValueError):
    pass


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


urlopen = build_opener(NoRedirect()).open


def require(condition, category):
    if not condition:
        raise ReceiptSourceError(category)


def github_json(repository, path, token):
    request = Request('https://api.github.com/repos/' + repository + '/' + path,
                      headers={'Authorization': 'Bearer ' + token,
                               'Accept': 'application/vnd.github+json',
                               'X-GitHub-Api-Version': '2022-11-28',
                               'User-Agent': 'WorkflowReceiptValidation/1.0'})
    try:
        with urlopen(request, timeout=30) as response:
            data = response.read(1024 * 1024 + 1)
    except HTTPError as exc:
        status = exc.code
        exc.close()
        raise ReceiptSourceError('github_http_' + str(status)) from None
    except (URLError, TimeoutError, OSError):
        raise ReceiptSourceError('github_network_stop') from None
    require(0 < len(data) <= 1024 * 1024, 'github_response_size')
    try:
        return json.loads(data)
    except (ValueError, UnicodeError):
        raise ReceiptSourceError('github_response_invalid') from None


def validate(repository, run_id, name, api):
    require(re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository), 'repository_invalid')
    require(re.fullmatch(r'[1-9][0-9]{0,19}', run_id), 'source_run_invalid')
    require(re.fullmatch(r'[A-Za-z0-9_-]{1,200}', name)
            and 'wechat' in name and 'draft' in name, 'artifact_name_invalid')
    run = api(f'actions/runs/{run_id}')
    require(run.get('id') == int(run_id) and run.get('status') == 'completed'
            and run.get('conclusion') == 'success'
            and run.get('head_repository', {}).get('full_name') == repository,
            'source_run_not_accepted')
    artifacts = []
    total = None
    for page in range(1, 11):
        data = api(f'actions/runs/{run_id}/artifacts?per_page=100&page={page}')
        count, rows = data.get('total_count'), data.get('artifacts')
        require(type(count) is int and 0 <= count <= 1000 and isinstance(rows, list)
                and len(rows) <= 100 and (total is None or count == total), 'artifact_inventory_invalid')
        total = count
        artifacts.extend(rows)
        require(len(artifacts) <= total and all(isinstance(row, dict) for row in rows), 'artifact_inventory_invalid')
        if len(artifacts) == total:
            break
        require(len(rows) == 100, 'artifact_inventory_incomplete')
    require(len(artifacts) == total and len({row.get('id') for row in artifacts}) == len(artifacts),
            'artifact_inventory_incomplete')
    matches = [row for row in artifacts if row.get('name') == name]
    require(len(matches) == 1 and matches[0].get('expired') is False, 'artifact_not_unique_and_live')
    require(type(matches[0].get('id')) is int and matches[0]['id'] > 0, 'artifact_id_invalid')
    return {'source_run_verified': True, 'artifact_verified': True, 'artifact_id': matches[0]['id']}


def main():
    try:
        token = os.environ.get('GH_TOKEN', '')
        require(bool(token), 'github_token_missing')
        repo = os.environ.get('GITHUB_REPOSITORY', '')
        result = validate(repo, os.environ.get('SOURCE_RUN_ID', ''), os.environ.get('ARTIFACT_NAME', ''),
                          lambda path: github_json(repo, path, token))
    except (ReceiptSourceError, TypeError, KeyError, AttributeError) as exc:
        category = str(exc) if isinstance(exc, ReceiptSourceError) else 'receipt_source_contract_invalid'
        print('::error::' + category)
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
