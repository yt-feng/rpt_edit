#!/usr/bin/env python3
"""Wait for a release containing an exact recovered archive, then verify its pages.

Publication requests and watcher state are workflow artifacts. A superseded
pending release can be replaced only by a same-repository main release containing
the archive commit. A successful sibling alone never proves article delivery.
"""
from __future__ import annotations

import argparse
import hashlib
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import time
import unicodedata
from urllib.parse import urlsplit

WORKFLOW = '.github/workflows/neutral-edge-cutover.yml'
SHA = re.compile(r'[a-f0-9]{40}')
HASH = re.compile(r'[a-f0-9]{64}')
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}


class PublicationError(ValueError):
    pass


def require(condition, category):
    if not condition:
        raise PublicationError(category)


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix('.pending')
    temporary.write_text(json.dumps(value, ensure_ascii=True, sort_keys=True), encoding='utf-8')
    temporary.replace(path)


def normalized(value):
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFKC', value)).strip()


def title_hash(value):
    value = normalized(re.sub(r'\s*\|\s*KC桌面\s*$', '', value))
    return hashlib.sha256(value.encode()).hexdigest()


class ArticleHTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.canonicals, self.body, self.heading, self.references = [], [], [], []
        self.depth = self.heading_depth = self.content_count = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'link' and 'canonical' in attrs.get('rel', '').split():
            self.canonicals.append(attrs.get('href', ''))
        if tag == 'h1':
            self.heading_depth += 1
        if self.depth:
            if tag == 'img':
                self.references.append(['img', attrs.get('src', ''), attrs.get('alt', '')])
            elif tag == 'a':
                self.references.append(['a', attrs.get('href', '')])
            if tag not in VOID:
                self.depth += 1
        elif tag == 'div' and 'blog-article-content' in attrs.get('class', '').split():
            self.depth = 1
            self.content_count += 1

    def handle_endtag(self, tag):
        if tag == 'h1':
            self.heading_depth = max(0, self.heading_depth - 1)
        if self.depth and tag not in VOID:
            self.depth -= 1

    def handle_data(self, value):
        if self.depth:
            self.body.append(value)
        if self.heading_depth:
            self.heading.append(value)


def body_identity(document, title_hashes=()):
    parsed = ArticleHTML()
    parsed.feed(document)
    parsed.close()
    require(parsed.content_count == 1 and parsed.depth == 0, 'publication_body_missing')
    text = normalized(''.join(parsed.body))
    # The renderer may repair only the leading editorial title. Keep the entire
    # remaining article, including its final source footer, in the digest.
    candidates = {*title_hashes, title_hash(''.join(parsed.heading))}
    for length in range(min(300, len(text)), 0, -1):
        if hashlib.sha256(text[:length].encode()).hexdigest() in candidates:
            text = text[length:].lstrip()
            break
    require(len(text) >= 200, 'publication_body_too_short')
    identity = json.dumps({'text': text, 'references': parsed.references}, ensure_ascii=True, sort_keys=True)
    return hashlib.sha256(identity.encode()).hexdigest(), parsed.canonicals


def committed_record(path, archive_commit):
    relative = path.resolve().relative_to(Path.cwd().resolve()).as_posix()
    require(re.fullmatch(r'portal_suite/data/blog_archive/\d{8}/[a-f0-9]{64}\.json', relative),
            'publication_archive_path_invalid')
    result = subprocess.run(['git', 'show', f'{archive_commit}:{relative}'], capture_output=True, timeout=30)
    require(result.returncode == 0 and result.stdout == path.read_bytes(), 'publication_archive_not_committed')


def record_expectation(record, origin='https://kcdesk.com'):
    """Derive only public hashes/slug from an already authenticated archive record."""
    from build_portal_suite_site import prepare_blog_discovery, render_blog_article
    prepared = prepare_blog_discovery([record], [])[0]
    title_hashes = sorted({title_hash(record['title']), title_hash(prepared['title'])})
    body_hash, _ = body_identity(render_blog_article(prepared, origin), title_hashes)
    return {'fingerprint': record['fingerprint'], 'slug': record['slug'],
            'body_sha256': body_hash, 'title_sha256': title_hashes}


def build_request(drafts_root, archive_root, archive_commit, origin, verify_record=committed_record):
    from build_portal_suite_site import (BLOG_START_DATE, load_blog_archive, load_blog_draft_articles,
                                        parse_blog_start_date)
    from update_blog_archive_from_wechat_drafts import split_hard_blocked_blog_articles
    require(SHA.fullmatch(archive_commit), 'publication_commit_invalid')
    validate_origin(origin)
    start = parse_blog_start_date(BLOG_START_DATE)
    drafts, _ = split_hard_blocked_blog_articles(load_blog_draft_articles(Path(drafts_root), start))
    archive = {row['fingerprint']: row for row in load_blog_archive(Path(archive_root), start)}
    rows = []
    for draft in drafts:
        record = archive.get(draft['fingerprint'])
        require(record is not None, 'publication_archive_record_missing')
        path = Path(archive_root) / record['date'].replace('-', '') / (record['fingerprint'] + '.json')
        verify_record(path, archive_commit)
        # Discovery may alter the displayed institution/title when a source is
        # matched to a newer catalog. The body digest normalizes that title only.
        rows.append(record_expectation(record, origin))
    return {'schema_version': 1, 'archive_commit': archive_commit, 'origin': origin,
            'records': sorted(rows, key=lambda row: row['fingerprint'])}


def validate_origin(origin):
    value = urlsplit(origin)
    require(value.scheme == 'https' and value.hostname and not value.username and not value.password
            and not value.port and value.path in {'', '/'} and not value.query and not value.fragment
            and origin == origin.rstrip('/'), 'publication_origin_invalid')


def validate_request(request):
    require(isinstance(request, dict) and request.get('schema_version') == 1
            and SHA.fullmatch(str(request.get('archive_commit', ''))), 'publication_request_invalid')
    validate_origin(request.get('origin', ''))
    rows = request.get('records')
    require(isinstance(rows, list) and len(rows) <= 1000, 'publication_request_invalid')
    seen = set()
    for row in rows:
        require(isinstance(row, dict) and HASH.fullmatch(str(row.get('fingerprint', '')))
                and HASH.fullmatch(str(row.get('body_sha256', '')))
                and re.fullmatch(r'\d{8}-[a-f0-9]{16}', str(row.get('slug', '')))
                and row['slug'].endswith(row['fingerprint'][:16])
                and isinstance(row.get('title_sha256'), list) and len(row['title_sha256']) <= 2
                and all(isinstance(value, str) and HASH.fullmatch(value) for value in row['title_sha256'])
                and row['fingerprint'] not in seen, 'publication_record_invalid')
        seen.add(row['fingerprint'])


class GitHub:
    def __init__(self, repository):
        require(re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository), 'publication_repository_invalid')
        self.repository = repository

    def command(self, args):
        try:
            result = subprocess.run(['gh', *args], capture_output=True, text=True, timeout=60, check=False)
        except (OSError, subprocess.TimeoutExpired):
            raise PublicationError('publication_github_transport_failed') from None
        require(result.returncode == 0, 'publication_github_request_failed')
        require(len(result.stdout) <= 16 * 1024 * 1024, 'publication_github_response_oversized')
        return result.stdout

    def api(self, suffix):
        try:
            return json.loads(self.command(['api', f'repos/{self.repository}/{suffix}']))
        except json.JSONDecodeError:
            raise PublicationError('publication_github_response_invalid') from None

    def run(self, run_id):
        return self.api(f'actions/runs/{int(run_id)}')

    def recent(self):
        return self.api('actions/workflows/neutral-edge-cutover.yml/runs?branch=main&per_page=100')['workflow_runs']

    def contains(self, base, head):
        require(SHA.fullmatch(base) and SHA.fullmatch(head), 'publication_commit_invalid')
        if base == head:
            return True
        comparison = self.api(f'compare/{base}...{head}')
        return comparison.get('status') in {'identical', 'ahead'} and comparison.get('merge_base_commit', {}).get('sha') == base

    def dispatch(self):
        value = self.command(['workflow', 'run', 'neutral-edge-cutover.yml', '--repo', self.repository,
                              '--ref', 'main', '-f', 'operation=migrate', '-f', 'translation_scope=incremental']).strip()
        match = re.fullmatch(r'https://github\.com/' + re.escape(self.repository) + r'/actions/runs/([1-9][0-9]*)', value)
        require(match is not None, 'publication_dispatch_identity_missing')
        return int(match[1])


def eligible(run, repository, archive_commit, contains):
    return (isinstance(run, dict) and run.get('path') == WORKFLOW and run.get('head_branch') == 'main'
            and run.get('event') in {'workflow_dispatch', 'workflow_run', 'schedule'}
            and run.get('repository', {}).get('full_name') == repository
            and run.get('head_repository', {}).get('full_name') == repository
            and SHA.fullmatch(str(run.get('head_sha', ''))) is not None
            and contains(archive_commit, run['head_sha']))


def verify_live(request, fetch=None, *, deadline=None, clock=time.monotonic):
    from fetch_release_asset import fetch_release_asset, FetchError
    fetch = fetch or fetch_release_asset
    with tempfile.TemporaryDirectory(prefix='recovered-publication-') as directory:
        path = Path(directory) / 'page.html'
        for row in request['records']:
            if deadline is not None and clock() >= deadline:
                return False
            url = request['origin'] + '/blog/' + row['slug'] + '.html'
            try:
                fetch(url, path, label='recovered Blog page', attempts=1, max_time=30,
                      max_total_time=30, max_bytes=4 * 1024 * 1024, logger=lambda _: None)
                body_hash, canonicals = body_identity(path.read_text(encoding='utf-8'), row['title_sha256'])
                if canonicals != [url] or body_hash != row['body_sha256']:
                    return False
            except (FetchError, UnicodeError, PublicationError):
                return False
    return True


def watch(request, github, state_path, *, initial_run_id=None, budget=350 * 60,
          interval=60, clock=time.monotonic, sleep=time.sleep, verify=None):
    validate_request(request)
    require(0 < budget <= 350 * 60 and 0 < interval <= 60, 'publication_wait_budget_invalid')
    state_path = Path(state_path)
    request_hash = hashlib.sha256(json.dumps(request, sort_keys=True).encode()).hexdigest()
    state = {'schema_version': 1, 'request_sha256': request_hash, 'status': 'pending', 'run_ids': []}
    if state_path.is_file():
        saved = json.loads(state_path.read_text())
        require(saved.get('request_sha256') == request_hash, 'publication_resume_identity_changed')
        state = saved
    if not request['records']:
        state.update(status='complete', article_count=0)
        write_json(state_path, state)
        return state
    current = initial_run_id or (state['run_ids'][-1] if state['run_ids'] else None)
    if current is None:
        require(state.get('status') != 'dispatch_pending', 'publication_dispatch_confirmation_required')
        state['status'] = 'dispatch_pending'
        write_json(state_path, state)
        current = github.dispatch()
    if current not in state['run_ids']:
        state['run_ids'].append(current)
    write_json(state_path, state)
    deadline = clock() + budget
    ancestry = {}

    def contains(base, head):
        require(clock() < deadline, 'publication_pending_resume_required')
        if head not in ancestry:
            ancestry[head] = github.contains(base, head)
        return ancestry[head]

    while clock() < deadline:
        run = github.run(current)
        require(eligible(run, github.repository, request['archive_commit'], contains), 'publication_run_identity_changed')
        conclusion = run.get('conclusion') if run.get('status') == 'completed' else None
        if conclusion == 'success':
            accepted = verify(request) if verify is not None else verify_live(request, deadline=deadline, clock=clock)
            if accepted:
                state.update(status='complete', release_run_id=current, article_count=len(request['records']))
                write_json(state_path, state)
                return state
            state['status'] = 'awaiting_live_content'
        elif conclusion in {'failure', 'timed_out', 'action_required', 'startup_failure'}:
            state.update(status='release_failed', release_run_id=current, conclusion=conclusion)
            write_json(state_path, state)
            raise PublicationError('publication_release_failed')
        elif conclusion == 'cancelled':
            # GitHub replaces the single pending concurrency slot. Follow only a
            # later release containing this exact archive, never an older green.
            candidates = [row for row in github.recent()
                          if int(row.get('id', 0)) > current
                          and row.get('conclusion') not in {'cancelled', 'skipped'}
                          and eligible(row, github.repository, request['archive_commit'], contains)]
            if candidates:
                current = min(int(row['id']) for row in candidates)
                state['run_ids'].append(current)
                state['status'] = 'following_successor'
            else:
                state['status'] = 'awaiting_successor'
        elif conclusion is not None:
            raise PublicationError('publication_release_not_executed')
        write_json(state_path, state)
        sleep(min(interval, max(0, deadline - clock())))
    state['status'] = 'pending_timeout'
    write_json(state_path, state)
    raise PublicationError('publication_pending_resume_required')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    build = sub.add_parser('request')
    build.add_argument('--drafts-root', required=True)
    build.add_argument('--archive-root', required=True)
    build.add_argument('--archive-commit', required=True)
    build.add_argument('--origin', default='https://kcdesk.com')
    build.add_argument('--output', required=True)
    wait = sub.add_parser('watch')
    wait.add_argument('--request', required=True)
    wait.add_argument('--state', required=True)
    wait.add_argument('--repository', default=os.environ.get('GITHUB_REPOSITORY', ''))
    wait.add_argument('--initial-run-id', type=int)
    args = parser.parse_args(argv)
    try:
        if args.command == 'request':
            value = build_request(args.drafts_root, args.archive_root, args.archive_commit, args.origin)
            validate_request(value)
            write_json(args.output, value)
        else:
            value = watch(json.loads(Path(args.request).read_text()), GitHub(args.repository),
                          args.state, initial_run_id=args.initial_run_id)
        print(json.dumps({'status': 'complete', 'stage': args.command,
                          'article_count': len(value['records']) if args.command == 'request' else value['article_count']}))
        return 0
    except PublicationError as error:
        print(json.dumps({'status': 'failed', 'category': str(error)}), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
