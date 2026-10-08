import hashlib
import io
import json
import subprocess
import sys
import time
import unittest
from unittest.mock import patch
import zipfile

import institution_hold_provenance as p
from institution_original_cache import OPTIONS
from mineru_task_ledger import digest, encoded


class API:
    def __init__(self, responses):
        self.responses, self.calls = responses, []

    def get(self, suffix, binary=False):
        self.calls.append((suffix, binary))
        return self.responses[suffix]


def binding(name='example.pdf', size=12, checksum='b'*64):
    value = {'source': name, 'size': size, 'sha256': checksum, 'scope': 'institution',
             'endpoint': 'https://mineru.net', 'options': OPTIONS}
    return dict(value, id=digest(encoded(value)))


def source(**changes):
    return dict({'local_filename': 'example.pdf', 'bytes': 12,
                 'source_page_url': 'https://www.imf.org/en/publications/example',
                 'published': '2026-10-07T04:00:00+00:00',
                 'pdf_url': 'https://www.imf.org/files/2026/example.pdf'}, **changes)


def fixtures(rows=None, *, run_id=123, entries=None):
    manifest = json.dumps({'date': '261008', 'downloaded_count': len(rows or [source()]),
                           'downloaded': rows or [source()]}).encode()
    output = io.BytesIO()
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as zipped:
        zipped.writestr(p.MANIFEST, manifest)
        for name, payload in (entries or []):
            zipped.writestr(name, payload)
    archive = output.getvalue()
    run = {'id': run_id, 'run_attempt': 1, 'path': p.PRODUCER, 'head_branch': 'main',
           'head_sha': 'a'*40, 'event': 'schedule', 'status': 'completed', 'conclusion': 'failure',
           'repository': {'id': p.REPOSITORY_ID, 'full_name': p.REPOSITORY},
           'head_repository': {'id': p.REPOSITORY_ID, 'full_name': p.REPOSITORY}}
    artifact = {'id': run_id+1000, 'name': f'institution-pdf-run-261008-{run_id}',
                'size_in_bytes': len(archive), 'expired': False,
                'digest': 'sha256:'+hashlib.sha256(archive).hexdigest(),
                'workflow_run': {'id': run_id, 'repository_id': p.REPOSITORY_ID,
                                 'head_repository_id': p.REPOSITORY_ID, 'head_branch': 'main',
                                 'head_sha': 'a'*40}}
    return run, artifact, archive


def responses(run, artifact, archive):
    return {f"actions/runs/{run['id']}": run,
            f"actions/runs/{run['id']}/artifacts?per_page=100": {'total_count': 1, 'artifacts': [artifact]},
            f"actions/artifacts/{artifact['id']}/zip": archive}


class ProvenanceTests(unittest.TestCase):
    def test_failed_main_producer_legacy_manifest_matches_without_invented_sha(self):
        run, artifact, archive = fixtures(entries=[('institution_fetch_progress.log', b'log')])
        api = API(responses(run, artifact, archive))
        rows, receipts = p.get_original_versions(['123'], [binding()], api=api)
        self.assertEqual(rows, [dict(source(), binding_id=binding()['id'])])
        self.assertNotIn('sha256', rows[0])
        self.assertEqual(receipts[0]['artifact_sha256'], artifact['digest'][7:])
        self.assertEqual(set(receipts[0]), {'run_id', 'artifact_id', 'artifact_sha256', 'manifest_sha256'})
        self.assertEqual(len(api.calls), 3)

    def test_complete_binding_checked_before_api(self):
        api = API({})
        wrong = dict(binding(), size=11)
        with self.assertRaises(ValueError):
            p.get_original_versions(['123'], [wrong], api=api)
        self.assertEqual(api.calls, [])

    def test_run_rejects_pr_fork_wrong_workflow_and_incomplete(self):
        for changes in ({'event': 'pull_request'}, {'head_branch': 'feature'}, {'path': 'other.yml'},
                        {'status': 'in_progress'}, {'id': True}, {'run_attempt': True},
                        {'head_repository': {'id': 7, 'full_name': p.REPOSITORY}},
                        {'repository': {'id': p.REPOSITORY_ID, 'full_name': 'other/repo'}}):
            with self.subTest(changes=changes):
                run, artifact, archive = fixtures()
                run.update(changes)
                api = API({'actions/runs/123': run})
                with self.assertRaises(ValueError):
                    p.get_original_versions(['123'], [binding()], api=api)
                self.assertEqual(len(api.calls), 1)

    def test_artifact_identity_and_digest_rejected(self):
        for change in ({'id': True}, {'size_in_bytes': True}, {'size_in_bytes': p.MAX_ARCHIVE+1},
                       {'name': 'institution-pdf-run-261008-999'}, {'digest': 'sha256:'+'0'*64},
                       {'workflow_run': {'id': 999}}):
            with self.subTest(change=change):
                run, artifact, archive = fixtures()
                artifact.update(change)
                with self.assertRaises(ValueError):
                    p.read_manifest(artifact, run, archive)

    def test_wrong_size_and_changed_archive_fail(self):
        run, artifact, archive = fixtures()
        for bad in (archive+b'x', archive[:-1], b'x'*len(archive)):
            with self.subTest(length=len(bad)), self.assertRaises(ValueError):
                p.read_manifest(artifact, run, bad)

    def test_missing_expired_manifest_does_not_supply_versions(self):
        for artifacts in ([], [dict(fixtures()[1], expired=True)]):
            run, _, _ = fixtures()
            api = API({'actions/runs/123': run,
                       'actions/runs/123/artifacts?per_page=100': {'total_count': len(artifacts), 'artifacts': artifacts}})
            self.assertEqual(p.get_original_versions(['123'], [binding()], api=api), ([], []))
            self.assertEqual(len(api.calls), 2)

    def test_duplicate_artifact_and_truncated_listing_rejected(self):
        run, artifact, archive = fixtures()
        for listing in ({'total_count': 2, 'artifacts': [artifact, artifact]},
                        {'total_count': 101, 'artifacts': [artifact]}):
            data = responses(run, artifact, archive)
            data['actions/runs/123/artifacts?per_page=100'] = listing
            with self.assertRaises(ValueError):
                p.get_original_versions(['123'], [binding()], api=API(data))

    def test_unsafe_zip_members_rejected_without_extraction(self):
        symlink = zipfile.ZipInfo('link'); symlink.external_attr = 0o120777 << 16
        for name in ('../outside', '/absolute', 'folder\\file', symlink):
            with self.subTest(name=str(name)):
                run, artifact, archive = fixtures(entries=[(name, b'x')])
                with self.assertRaises(ValueError):
                    p.read_manifest(artifact, run, archive)

    def test_zip_manifest_expansion_bounded(self):
        run, artifact, archive = fixtures(entries=[('large.log', b'x'*(p.MAX_ARCHIVE+1))])
        with self.assertRaises(ValueError):
            p.read_manifest(artifact, run, archive)
        run, artifact, archive = fixtures([source(title='x'*p.MAX_MANIFEST)])
        with self.assertRaises(ValueError):
            p.read_manifest(artifact, run, archive)

    def test_exact_actual_hash_kept_and_mismatch_not_matched(self):
        self.assertEqual(p.match_versions([source(sha256='b'*64)], [binding()])[0]['sha256'], 'b'*64)
        self.assertEqual(p.match_versions([source(sha256='c'*64)], [binding()]), [])

    def test_filename_size_and_binding_collision_remain_unmatched(self):
        self.assertEqual(p.match_versions([source(bytes=13)], [binding()]), [])
        self.assertEqual(p.match_versions([source(local_filename='different.pdf')], [binding()]), [])
        self.assertEqual(p.match_versions([source()], [binding(), binding(checksum='c'*64)]), [])
        self.assertEqual(len(p.match_versions([source()], [binding(), binding()])), 1)

    def test_same_name_size_different_year_or_url_is_ambiguous(self):
        for change in ({'published': '2025-10-07T04:00:00+00:00'},
                       {'pdf_url': 'https://www.imf.org/files/2025/example.pdf'},
                       {'source_page_url': 'https://www.imf.org/en/publications/different'}):
            with self.subTest(change=change):
                self.assertEqual(p.match_versions([source(), source(**change)], [binding()]), [])
        self.assertEqual(len(p.match_versions([source(), source()], [binding()])), 1)

    def test_ambiguity_combined_across_requested_runs(self):
        first = fixtures()
        second = fixtures([source(pdf_url='https://www.imf.org/other.pdf')], run_id=124)
        api = API(dict(responses(*first), **responses(*second)))
        rows, receipts = p.get_original_versions(['123', '124'], [binding()], api=api)
        self.assertEqual(rows, [])
        self.assertEqual(len(receipts), 2)

    def test_only_bounded_official_publication_metadata_is_admitted(self):
        for change in ({'pdf_url': 'https://imf.org.evil.test/file.pdf'},
                       {'source_page_url': 'https://person:password@imf.org/a'},
                       {'pdf_url': 'http://imf.org/file.pdf'}, {'published': '2026-10-07'},
                       {'feed_pdf_candidates': ['https://other.test/file.pdf']},
                       {'feed_pdf_candidates': ['https://imf.org/a.pdf']*21},
                       {'pdf_url': 'https://imf.org/'+'a'*4096}):
            with self.subTest(change=change):
                self.assertEqual(p.match_versions([source(**change)], [binding()]), [])
        good = source(feed_pdf_candidates=['https://imf.org/a.pdf'])
        self.assertEqual(p.match_versions([good], [binding()])[0]['feed_pdf_candidates'], good['feed_pdf_candidates'])

    def test_official_http_page_and_rfc_feed_date_preserved_without_fetch(self):
        row = source(source_page_url='http://documents.worldbank.org/curated/en/example',
                     published='Fri, 02 Oct 2026 00:00:00 GMT',
                     pdf_url='https://documents.worldbank.org/example.pdf')
        self.assertEqual(p.match_versions([row], [binding()]), [dict(row, binding_id=binding()['id'])])

    def test_canonical_api_endpoint_and_shared_deadline(self):
        with patch.object(p, 'bounded_command', return_value=b'{}') as command:
            api = p.GitHubAPI()
            api.get('actions/runs/123')
            api.get('actions/artifacts/1123/zip', binary=True)
            one, two = command.call_args_list
            self.assertEqual(one.args[0], ['gh', 'api', '--hostname', 'github.com',
                                         'repos/yt-feng/rpt_edit/actions/runs/123'])
            self.assertEqual(one.args[2], two.args[2])
            self.assertEqual(two.args[1], p.MAX_ARCHIVE)

    def test_api_failure_is_not_hidden_or_retried(self):
        class Broken:
            calls = 0
            def get(self, *args, **kwargs):
                self.calls += 1
                raise RuntimeError('transport stopped')
        api = Broken()
        with self.assertRaises(RuntimeError):
            p.get_original_versions(['123'], [binding()], api=api)
        self.assertEqual(api.calls, 1)

    def test_actual_subprocess_oversize_and_timeout_are_reaped(self):
        original = subprocess.Popen
        for script, limit, seconds in (("import os,time; os.write(1,b'x'*10000); time.sleep(30)", 100, 2),
                                       ('import time; time.sleep(30)', 100, 0.15)):
            processes = []
            def launch(*args, **kwargs):
                process = original(*args, **kwargs); processes.append(process); return process
            with patch.object(p.subprocess, 'Popen', side_effect=launch):
                started = time.monotonic()
                with self.assertRaises(ValueError):
                    p.bounded_command([sys.executable, '-c', script], limit, started+seconds)
                self.assertLess(time.monotonic()-started, seconds+1)
            self.assertIsNotNone(processes[0].poll())
            self.assertTrue(processes[0].stdout.closed)


if __name__ == '__main__':
    unittest.main()
