#!/usr/bin/env python3
"""Publication queue and user-visible Blog acceptance, without network calls."""
import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

import watch_recovered_article_publication as publication

BASE = 'a' * 40
HEAD = 'b' * 40
FINGERPRINT = 'c' * 64
SLUG = '20261009-' + FINGERPRINT[:16]
ORIGIN = 'https://kcdesk.com'
BODY = 'This is the exact original analysis, with all figures and source context. ' * 8


def html(body=BODY, title='Original article', canonical=None):
    canonical = canonical or ORIGIN + '/blog/' + SLUG + '.html'
    return ('<html><head><link rel="canonical" href="' + canonical + '"></head>'
            '<body><h1>' + title + ' | KC桌面</h1><div class="blog-article-content">'
            '<p>' + title + '</p><p>' + body + '</p><p>Original report: evidence</p></div></body></html>')


def request():
    return {'schema_version': 1, 'archive_commit': BASE, 'origin': ORIGIN, 'records': [
        {'fingerprint': FINGERPRINT, 'slug': SLUG, 'body_sha256': publication.body_identity(html())[0],
         'title_sha256': [publication.title_hash('Original article')]}]}


def run(run_id=1, *, status='completed', conclusion='success', sha=BASE, **changes):
    value = {'id': run_id, 'path': publication.WORKFLOW, 'head_branch': 'main', 'head_sha': sha,
             'repository': {'full_name': 'owner/repo'}, 'head_repository': {'full_name': 'owner/repo'},
             'event': 'workflow_dispatch', 'status': status, 'conclusion': conclusion}
    value.update(changes)
    return value


class FakeGitHub:
    repository = 'owner/repo'

    def __init__(self, runs, candidates=()):
        self.runs = runs
        self.candidates = list(candidates)
        self.dispatched = 0
        self.reads = []

    def run(self, run_id):
        self.reads.append(run_id)
        return copy.deepcopy(self.runs[run_id])

    def recent(self):
        return copy.deepcopy(self.candidates)

    def contains(self, base, head):
        return base == BASE and head in {BASE, HEAD}

    def dispatch(self):
        self.dispatched += 1
        return 1


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.state = Path(self.directory.name) / 'state.json'
        self.now = 0

    def sleep(self, duration):
        self.now += duration

    def watch(self, github, **kwargs):
        return publication.watch(request(), github, self.state, budget=180, interval=60,
                                 clock=lambda: self.now, sleep=self.sleep, **kwargs)

    def fetch(self, document):
        def fetch(url, output, **kwargs):
            Path(output).write_text(document, encoding='utf-8')
        return fetch

    def test_superseded_pending_follows_exact_containing_successor_then_checks_pages(self):
        github = FakeGitHub({1: run(conclusion='cancelled'), 2: run(2, sha=HEAD)}, [run(2, sha=HEAD)])
        verify = Mock(return_value=True)
        result = self.watch(github, verify=verify)
        self.assertEqual(result['run_ids'], [1, 2])
        self.assertEqual(result['release_run_id'], 2)
        self.assertEqual(result['article_count'], 1)
        self.assertEqual(github.dispatched, 1)
        verify.assert_called_once_with(request())

    def test_older_unrelated_fork_and_wrong_workflow_green_cannot_replace_cancelled_run(self):
        candidates = [run(0), run(2, sha='d' * 40), run(3, path='other.yml'),
                      run(4, head_repository={'full_name': 'outsider/repo'}), run(5, head_branch='other')]
        github = FakeGitHub({1: run(conclusion='cancelled')}, candidates)
        verify = Mock(return_value=True)
        with self.assertRaisesRegex(publication.PublicationError, 'pending_resume_required'):
            self.watch(github, verify=verify)
        verify.assert_not_called()
        self.assertEqual(json.loads(self.state.read_text())['run_ids'], [1])

    def test_actual_failure_cannot_be_hidden_by_sibling_success(self):
        github = FakeGitHub({1: run(conclusion='failure')}, [run(2)])
        verify = Mock(return_value=True)
        with self.assertRaisesRegex(publication.PublicationError, 'release_failed'):
            self.watch(github, verify=verify)
        verify.assert_not_called()
        self.assertEqual(json.loads(self.state.read_text())['status'], 'release_failed')

    def test_successful_workflow_with_missing_or_changed_live_body_does_not_pass(self):
        github = FakeGitHub({1: run()})
        for document in [html().replace('blog-article-content', 'unrelated'), html(BODY + 'CHANGED'),
                         html(canonical=ORIGIN + '/blog/unrelated.html')]:
            self.assertFalse(publication.verify_live(request(), self.fetch(document)))
        with self.assertRaisesRegex(publication.PublicationError, 'pending_resume_required'):
            self.watch(github, verify=lambda value: publication.verify_live(value, self.fetch(html(BODY + 'CHANGED'))))
        self.assertEqual(json.loads(self.state.read_text())['status'], 'pending_timeout')

    def test_live_canonical_and_full_body_match_and_title_only_repair_is_allowed(self):
        self.assertTrue(publication.verify_live(request(), self.fetch(html())))
        self.assertTrue(publication.verify_live(request(), self.fetch(html(title='Repaired institution title'))))
        self.assertFalse(publication.verify_live(request(), self.fetch(html().replace('source context', 'different facts', 1))))
        self.assertFalse(publication.verify_live(request(), self.fetch(html().replace('Original report: evidence', ''))))

    def test_body_images_and_source_links_are_part_of_exact_live_identity(self):
        document = html().replace('</p><p>Original report:', '</p><img src="https://example.com/chart.png" alt="evidence"><a href="https://example.com/report">Source</a><p>Original report:')
        value = request()
        value['records'][0]['body_sha256'] = publication.body_identity(document)[0]
        self.assertTrue(publication.verify_live(value, self.fetch(document)))
        self.assertFalse(publication.verify_live(value, self.fetch(document.replace('<img src="https://example.com/chart.png" alt="evidence">', ''))))
        self.assertFalse(publication.verify_live(value, self.fetch(document.replace('https://example.com/report', 'https://example.com/wrong'))))

    def test_resume_reuses_prior_child_and_never_dispatches_again(self):
        github = FakeGitHub({1: run(status='pending', conclusion=None)})
        with self.assertRaisesRegex(publication.PublicationError, 'pending_resume_required'):
            self.watch(github, verify=lambda _: True)
        github.runs[1] = run()
        self.now = 0
        self.assertEqual(self.watch(github, verify=lambda _: True)['status'], 'complete')
        self.assertEqual(github.dispatched, 1)

    def test_uncertain_dispatch_ack_never_automatically_posts_again(self):
        github = FakeGitHub({1: run()})
        github.dispatch = Mock(side_effect=publication.PublicationError('publication_github_request_failed'))
        with self.assertRaises(publication.PublicationError):
            self.watch(github, verify=lambda _: True)
        self.assertEqual(json.loads(self.state.read_text())['status'], 'dispatch_pending')
        with self.assertRaisesRegex(publication.PublicationError, 'dispatch_confirmation_required'):
            self.watch(github, verify=lambda _: True)
        github.dispatch.assert_called_once()
        self.assertEqual(self.watch(github, initial_run_id=1, verify=lambda _: True)['status'], 'complete')

    def test_archive_identity_changed_on_resume_is_rejected(self):
        github = FakeGitHub({1: run()})
        self.watch(github, verify=lambda _: True)
        changed = request()
        changed['archive_commit'] = HEAD
        with self.assertRaisesRegex(publication.PublicationError, 'resume_identity_changed'):
            publication.watch(changed, github, self.state)

    def test_compare_requires_exact_archive_merge_base(self):
        github = publication.GitHub('owner/repo')
        with patch.object(github, 'api', return_value={'status': 'ahead', 'merge_base_commit': {'sha': 'd' * 40}}):
            self.assertFalse(github.contains(BASE, HEAD))
        with patch.object(github, 'api', return_value={'status': 'ahead', 'merge_base_commit': {'sha': BASE}}):
            self.assertTrue(github.contains(BASE, HEAD))

    def test_request_rejects_url_path_injection_and_unsafe_origin(self):
        for change in ({'origin': 'http://kcdesk.com'}, {'origin': 'https://kcdesk.com/private'},
                       {'archive_commit': '../main'}):
            value = request()
            value.update(change)
            with self.assertRaises(publication.PublicationError):
                publication.validate_request(value)
        value = request()
        value['records'][0]['slug'] = '../private'
        with self.assertRaises(publication.PublicationError):
            publication.validate_request(value)

    def test_no_public_articles_needs_no_release_dispatch(self):
        value = request()
        value['records'] = []
        github = FakeGitHub({})
        self.assertEqual(publication.watch(value, github, self.state)['article_count'], 0)
        self.assertEqual(github.dispatched, 0)

    def test_real_archive_renderer_and_policy_request(self):
        from build_portal_suite_site import blog_article_fingerprint
        root = Path(self.directory.name)
        payload = root / 'drafts/xhs_notes/261008'
        payload.mkdir(parents=True)
        content = '<p>Original article</p><p>' + BODY + '</p>'
        (payload / 'draft_payload_01.json').write_text(json.dumps({'articles': [{'title': 'Original article', 'content': content}]}))
        from build_portal_suite_site import load_blog_draft_articles, persist_blog_archive, parse_blog_start_date, BLOG_START_DATE
        start = parse_blog_start_date(BLOG_START_DATE)
        articles = load_blog_draft_articles(root / 'drafts', start)
        persist_blog_archive(root / 'archive', articles, start)
        verify_record = Mock()
        actual = publication.build_request(root / 'drafts', root / 'archive', BASE, ORIGIN, verify_record)
        publication.validate_request(actual)
        self.assertEqual(actual['records'][0]['fingerprint'], blog_article_fingerprint('Original article', content))
        self.assertTrue(actual['records'][0]['slug'].startswith('20261009-'))
        self.assertEqual(len(actual['records']), 1)
        verify_record.assert_called_once()
        self.assertNotIn('Original article', json.dumps(actual))

    def test_uncommitted_archive_record_cannot_enter_request(self):
        path = Path.cwd() / 'portal_suite/data/blog_archive/20261009' / (FINGERPRINT + '.json')
        with patch.object(publication.subprocess, 'run') as command, patch.object(Path, 'read_bytes', return_value=b'changed'):
            command.return_value.returncode = 0
            command.return_value.stdout = b'committed'
            with self.assertRaisesRegex(publication.PublicationError, 'archive_not_committed'):
                publication.committed_record(path, BASE)

    def test_accepted_current_page_cannot_hide_changed_archive_body(self):
        # Hash-only manifests still bind the entire body after title repair.
        value = request()
        value['records'][0]['title_sha256'] = [publication.title_hash('Previously saved title')]
        self.assertTrue(publication.verify_live(value, self.fetch(html(title='Latest catalog heading'))))
        self.assertFalse(publication.verify_live(value, self.fetch(html(BODY + 'extra analysis', title='Latest catalog heading'))))


if __name__ == '__main__':
    unittest.main()
