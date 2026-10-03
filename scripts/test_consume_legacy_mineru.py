import base64
from contextlib import redirect_stdout
from copy import deepcopy
import hashlib
import io
import json
from pathlib import Path
import stat
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

import consume_legacy_mineru as c
from inspect_legacy_mineru import canonical, classify_response


def zip_bytes(rows):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w', compression=zipfile.ZIP_STORED) as archive:
        for name, raw in rows:
            archive.writestr(name, raw)
    return buffer.getvalue()


def fixture(states=None):
    names = ['consulting-report-a.pdf', 'consulting-report-b.pdf', 'consulting-report-c.pdf',
             'consulting-report-d.pdf', 'consulting-report-e.pdf']
    copied = [{'source': '/work/_consulting_latest_pdfs/' + name,
               'batch_file': '/tmp/frozen/pdfs/' + c.copied_name(name, index),
               'stable_index': str(index)} for index, name in enumerate(names, 1)]
    members = [c.data_id(Path(row['batch_file']).name) for row in copied]
    slots = ['MINER_U', 'MINER_U_2', 'MINER_U_3', 'MINER_U_4'] * 2
    batches = [{'run_id': '37085542495', 'job_id': '111094944115',
        'batch_id': f'00000000-0000-4000-8000-{index:012d}', 'credential_slot': slots[index - 1],
        'expected_data_ids': members} for index in range(1, 9)]
    request = {'schema_version': 1, 'batches': batches}
    producer = {'run_id': '37156787082', 'attempt': '1', 'sha': 'a' * 40}
    objects = {}; descs = []
    for index, batch in enumerate(batches):
        state = states[index] if states else 'done'
        response = {'code': 0, 'data': {'batch_id': batch['batch_id'], 'extract_result': [
            {'data_id': identity, 'state': state, 'full_zip_url': f'https://private.example/{identity}?signed=private-secret'}
            for identity in members]}}
        raw = canonical(response)
        _, private = classify_response(200, raw, batch)
        payload = canonical(private); checksum = c.digest(payload)
        name = f"{producer['run_id']}-{producer['attempt']}/{c.digest(canonical(request))}/{batch['batch_id']}-{checksum}.json"
        objects[name] = payload
        descs.append({'batch_id': batch['batch_id'], 'object': name, 'sha256': checksum, 'bytes': len(payload)})
    receipt = {'schema_version': 1, 'policy': 'legacy-provider-inspection-only-v1', 'producer': producer,
        'input': request, 'input_canonical_sha256': c.digest(canonical(request)), 'objects': descs,
        'original_source_bytes_proven': False, 'historical_token_fingerprint_proven': False,
        'canonical_task_admission': False}
    original_log = ['2026-10-03T00:00:00.000Z Running batch 1: 5 PDFs']
    original_log += [f"2026-10-03T00:00:00.000Z MinerU attempt {index} using {b['credential_slot']} batch_id={b['batch_id']}"
                     for index, b in enumerate(batches, 1)]
    original_log.append('2026-10-03T00:00:00.000Z Batch 1 failed: ' + repr(
        {'batch_index': 1, 'pdf_count': 5, 'files': copied, 'returncode': 2, 'status': 'failed'}))
    log = '\n'.join(original_log).encode()
    manifest = canonical({'date': '261003', 'downloaded_count': 5,
                          'downloaded': [{'local_filename': name, 'bytes': 12345} for name in names]})
    receipt_raw = canonical(receipt)
    context = {'schema_version': 1, 'repository': 'yt-feng/rpt_edit', 'workflow_path': c.WORKFLOW,
        'run_id': '37085542495', 'job_id': '111094944115', 'execution_source_sha': 'b' * 40,
        'job_log_sha256': c.digest(log), 'manifest_sha256': c.digest(manifest),
        'inspection_receipt_sha256': c.digest(receipt_raw)}
    return receipt_raw, objects, log, manifest, context


def prepare_fixture(f=None):
    receipt, objects, log, manifest, context = f or fixture()
    return c.prepare(receipt, objects.__getitem__, log, manifest, context)


def fake_asset_writer(raw_dir, assets_dir, maximum):
    # Zero charts is valid; all original ZIP images are still retained.
    (assets_dir.parent / 'source_image_map.json').write_bytes(canonical({
        'version': 1, 'source_sha256': c.digest((assets_dir.parent / 'source_mineru.md').read_bytes()), 'images': {}}))
    return []


class OriginalProofTests(unittest.TestCase):
    def test_eight_repeated_submissions_restore_five_original_sources(self):
        plan = prepare_fixture()
        self.assertEqual(plan['verified_original_batches'], 8)
        self.assertEqual(len(plan['members']), 5)
        self.assertEqual(len({m['data_id'] for m in plan['members']}), 5)
        self.assertEqual(plan['selected_batch_id'], '00000000-0000-4000-8000-000000000001')
        self.assertEqual(plan['selected_credential_slot'], 'MINER_U')

    def test_chooses_one_whole_successful_batch_without_combining_members(self):
        plan = prepare_fixture(fixture(['failed'] + ['done'] * 7))
        self.assertTrue(plan['selected_batch_id'].endswith('000000000002'))
        self.assertEqual(plan['selected_credential_slot'], 'MINER_U_2')
        self.assertEqual(len(plan['members']), 5)

    def test_pending_original_group_blocks_even_if_another_batch_is_complete(self):
        with self.assertRaisesRegex(c.ConsumerError, 'terminal'):
            prepare_fixture(fixture(['pending'] + ['done'] * 7))

    def test_no_all_succeeded_batch_blocks_before_download(self):
        with self.assertRaisesRegex(c.ConsumerError, 'no_complete'):
            prepare_fixture(fixture(['failed'] * 8))

    def test_original_raw_log_or_manifest_hash_mismatch_blocks(self):
        f = list(fixture()); f[2] += b' altered'
        with self.assertRaisesRegex(c.ConsumerError, 'original_context'):
            prepare_fixture(f)
        f = list(fixture()); f[3] += b' '
        with self.assertRaisesRegex(c.ConsumerError, 'original_context'):
            prepare_fixture(f)

    def test_institution_workflow_and_unknown_membership_cannot_be_consumed(self):
        f = list(fixture()); f[4]['workflow_path'] = '.github/workflows/institution-latest-pdf-to-wechat.yml'
        with self.assertRaisesRegex(c.ConsumerError, 'original_context'):
            prepare_fixture(f)
        f = list(fixture()); receipt = json.loads(f[0]); receipt['input']['batches'][0]['expected_data_ids'] = []
        receipt['input_canonical_sha256'] = c.digest(canonical(receipt['input']))
        f[0] = canonical(receipt); f[4]['inspection_receipt_sha256'] = c.digest(f[0])
        with self.assertRaises(c.ConsumerError):
            prepare_fixture(f)

    def test_additional_original_manifest_source_cannot_be_silently_dropped(self):
        f = list(fixture()); manifest = json.loads(f[3]); manifest['downloaded'].append({'local_filename': 'extra.pdf'})
        manifest['downloaded_count'] = 6
        f[3] = canonical(manifest); f[4]['manifest_sha256'] = c.digest(f[3])
        with self.assertRaisesRegex(c.ConsumerError, 'original_group_incomplete'):
            prepare_fixture(f)

    def test_unreturned_second_wrapper_group_is_not_partial_job_completion(self):
        f = list(fixture()); f[2] += b'\nRunning batch 2: 5 PDFs'
        f[4]['job_log_sha256'] = c.digest(f[2])
        with self.assertRaisesRegex(c.ConsumerError, 'original_group_incomplete'):
            prepare_fixture(f)

    def test_copy_alias_or_original_filename_cannot_be_forged(self):
        f = list(fixture()); f[2] = f[2].replace(b'0001-consulting-report-a.pdf', b'0002-consulting-report-a.pdf')
        f[4]['job_log_sha256'] = c.digest(f[2])
        with self.assertRaisesRegex(c.ConsumerError, 'original_file_map'):
            prepare_fixture(f)

    def test_duplicate_json_and_identity_claims_are_rejected(self):
        with self.assertRaisesRegex(c.ConsumerError, 'duplicate_json'):
            c.decode(b'{"schema":1,"schema":2}')
        f = list(fixture()); receipt = json.loads(f[0]); receipt['canonical_task_admission'] = True
        f[0] = canonical(receipt); f[4]['inspection_receipt_sha256'] = c.digest(f[0])
        with self.assertRaisesRegex(c.ConsumerError, 'receipt_contract'):
            prepare_fixture(f)

    def test_mutated_private_object_and_batch_coverage_cannot_be_reused(self):
        f = list(fixture()); key = next(iter(f[1])); f[1][key] += b' '
        with self.assertRaisesRegex(c.ConsumerError, 'inspection_object_hash'):
            prepare_fixture(f)
        f = list(fixture()); receipt = json.loads(f[0]); receipt['input']['batches'].pop()
        receipt['input_canonical_sha256'] = c.digest(canonical(receipt['input']))
        f[0] = canonical(receipt); f[4]['inspection_receipt_sha256'] = c.digest(f[0])
        with self.assertRaisesRegex(c.ConsumerError, 'original_batch_coverage'):
            prepare_fixture(f)


class ArchiveTests(unittest.TestCase):
    def extract(self, rows):
        temporary = tempfile.TemporaryDirectory(); self.addCleanup(temporary.cleanup)
        root = Path(temporary.name) / 'raw'
        return c.safe_unzip(zip_bytes(rows), root), root

    def test_unambiguous_exact_utf8_markdown_is_retained(self):
        source = '# Exact original source\n\nMeaningful report body.\n'.encode()
        markdown, root = self.extract([('nested/full.md', source), ('nested/images/one.png', b'image')])
        self.assertEqual(markdown, source)
        self.assertEqual((root / 'nested/full.md').read_bytes(), source)

    def test_paths_duplicates_symlinks_and_ambiguous_markdown_are_rejected(self):
        for bad in ('../escape.md', '/absolute.md', 'C:/bad.md', 'a\\bad.md', 'a/./bad.md'):
            with self.subTest(path=bad), self.assertRaisesRegex(c.ConsumerError, 'zip_path'):
                self.extract([(bad, b'source')])
        with self.assertRaisesRegex(c.ConsumerError, 'zip_path'):
            self.extract([('a.md', b'one'), ('A.md', b'two')])
        link = zipfile.ZipInfo('link'); link.create_system = 3
        link.external_attr = (stat.S_IFLNK | 0o777) << 16
        with self.assertRaisesRegex(c.ConsumerError, 'zip_path'):
            self.extract([(link, b'../escape')])
        for rows in ([('a/full.md', b'one'), ('b/full.md', b'two')], [('a.md', b'one'), ('b.md', b'two')]):
            with self.assertRaisesRegex(c.ConsumerError, 'markdown_ambiguous'):
                self.extract(rows)

    def test_archive_crc_truncation_and_size_limits_are_checked(self):
        raw = zip_bytes([('full.md', b'original source unique sentinel')])
        changed = raw.replace(b'original source unique sentinel', b'changed! source unique sentinel')
        with tempfile.TemporaryDirectory() as temp:
            for content in (changed, raw[:-20]):
                with self.assertRaisesRegex(c.ConsumerError, 'zip_integrity'):
                    c.safe_unzip(content, Path(temp) / c.digest(content))
            with patch.object(c, 'MAX_EXPANDED', 4), self.assertRaisesRegex(c.ConsumerError, 'zip_expansion'):
                c.safe_unzip(raw, Path(temp) / 'large')
            with patch.object(c, 'MAX_FILES', 0), self.assertRaisesRegex(c.ConsumerError, 'zip_member_count'):
                c.safe_unzip(raw, Path(temp) / 'many')

    def test_empty_and_invalid_utf8_markdown_never_publish(self):
        for content, category in ((b' ', 'markdown_empty'), (b'\xff', 'markdown_encoding'), (b'', 'markdown_size')):
            with self.subTest(category=category), self.assertRaisesRegex(c.ConsumerError, category):
                self.extract([('full.md', content)])


class MaterializerTests(unittest.TestCase):
    def test_no_pdf_or_token_needed_and_public_summary_never_exposes_private_content(self):
        plan = prepare_fixture(); calls = []
        raw = zip_bytes([('full.md', b'# private source body\n\nOriginal full report.')])
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / 'original_source'
            def download(url): calls.append(url); return raw
            result = c.materialize(plan, destination, downloader=download, asset_writer=fake_asset_writer)
            self.assertEqual(len(calls), 5)
            self.assertEqual(result['source_count'], 5)
            self.assertEqual(result['result_downloads'], 5)
            for key in ('provider_posts', 'provider_gets', 'paid_requests', 'new_submissions'):
                self.assertEqual(result[key], 0)
            self.assertFalse(result['original_source_bytes_proven'])
            self.assertFalse(result['canonical_task_admission'])
            self.assertIsNone(result['original_pdf_sha256'])
            public = json.dumps(result)
            for private in ('private-secret', 'private.example', 'private source body', 'consulting-report'):
                self.assertNotIn(private, public)
            reports = list(destination.glob('*/status.json'))
            self.assertEqual(len(reports), 5)
            self.assertEqual(list(destination.rglob('*.pdf')), [])
            receipt = json.loads((destination / '_legacy_output_receipt.json').read_bytes())
            self.assertEqual(c.digest((destination / '_legacy_output_receipt.json').read_bytes()), result['legacy_output_receipt_sha256'])
            self.assertEqual(stat.S_IMODE((destination / '_legacy_output_receipt.json').stat().st_mode), 0o600)
            for row in receipt['files']:
                payload = (destination / row['path']).read_bytes()
                self.assertEqual((len(payload), c.digest(payload)), (row['bytes'], row['sha256']))
            for path in reports:
                status = json.loads(path.read_bytes())
                self.assertIsNone(status['original_pdf_sha256'])
                self.assertEqual(status['legacy_result']['zip_sha256'], c.digest(raw))

    def test_transport_failure_stops_later_downloads_and_atomic_publish(self):
        calls = []
        def download(url):
            calls.append(url)
            raise c.NetworkStop('network_stop')
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / 'source'
            with self.assertRaises(c.NetworkStop):
                c.materialize(prepare_fixture(), destination, downloader=download, asset_writer=fake_asset_writer)
            self.assertEqual(len(calls), 1)
            self.assertFalse(destination.exists())
            self.assertEqual(list(Path(temp).iterdir()), [])

    def test_late_invalid_result_preserves_no_partial_destination(self):
        calls = []
        valid = zip_bytes([('full.md', b'original source')])
        def download(url): calls.append(url); return valid if len(calls) == 1 else b'invalid private-url-body'
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / 'source'
            with self.assertRaisesRegex(c.ConsumerError, 'zip_integrity'):
                c.materialize(prepare_fixture(), destination, downloader=download, asset_writer=fake_asset_writer)
            self.assertEqual(len(calls), 2)
            self.assertFalse(destination.exists())

    def test_existing_destination_and_invalid_image_mapping_cannot_be_reused(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / 'source'; destination.mkdir()
            (destination / 'source_mineru.md').write_text('wrong prior source')
            with self.assertRaisesRegex(c.ConsumerError, 'destination_exists'):
                c.materialize(prepare_fixture(), destination, downloader=lambda _: b'bad')
            self.assertEqual((destination / 'source_mineru.md').read_text(), 'wrong prior source')
            bad = Path(temp) / 'bad'
            def writer(raw, assets, maximum):
                (assets.parent / 'source_image_map.json').write_bytes(canonical({'version': 1, 'source_sha256': '0' * 64, 'images': {}}))
                return []
            with self.assertRaisesRegex(c.ConsumerError, 'image_map_contract'):
                c.materialize(prepare_fixture(), bad, downloader=lambda _: zip_bytes([('full.md', b'original')]), asset_writer=writer)
            self.assertFalse(bad.exists())

    def test_url_validation_does_not_accept_redirect_targets_local_addresses_or_credentials(self):
        for value in ('http://private.example/x', 'https://127.0.0.1/x', 'https://[::1]/x',
                      'https://localhost/x', 'https://user:private@private.example/x', 'https://private.example:80/x',
                      'https://private.example/x#fragment', 'https://private.example/x\nheader'):
            with self.subTest(value=value), self.assertRaises(c.ConsumerError):
                c.valid_url(value)
        c.valid_url('https://private.example/x?signature=private-secret')

    def test_download_is_one_get_without_authorization_redirect_or_retry(self):
        class Response:
            status = 200; headers = {'Content-Length': '3'}
            def __enter__(self): return self
            def __exit__(self, *args): pass
            def read(self, size):
                value = getattr(self, 'remaining', b'zip'); self.remaining = b''; return value
        calls = []
        class Opener:
            def open(self, request, timeout):
                calls.append((request, timeout)); return Response()
        with patch('consume_legacy_mineru.urllib.request.build_opener', return_value=Opener()) as build:
            self.assertEqual(c.download_once('https://private.example/x?signature=secret'), b'zip')
        self.assertEqual(len(calls), 1)
        request, timeout = calls[0]
        self.assertEqual(request.get_method(), 'GET')
        self.assertEqual(request.headers, {})
        self.assertEqual(timeout, 20)
        self.assertIs(build.call_args.args[0], c.NoRedirect)
        with patch('consume_legacy_mineru.urllib.request.build_opener') as build:
            build.return_value.open.side_effect = OSError('https://private-url secret-token')
            with self.assertRaisesRegex(c.NetworkStop, '^network_stop$'):
                c.download_once('https://private.example/x')
            self.assertEqual(build.return_value.open.call_count, 1)

    def test_prepared_member_url_tampering_blocks_before_download(self):
        plan = prepare_fixture()
        plan['members'][0]['result']['full_zip_url'] = 'https://different.example/other-source'
        with tempfile.TemporaryDirectory() as temp, self.assertRaisesRegex(c.ConsumerError, 'prepared_contract'):
            c.materialize(plan, Path(temp) / 'source', downloader=lambda _: self.fail('download must not run'))

    def test_real_source_only_producer_and_portal_input_contract_without_pdf(self):
        from PIL import Image, ImageDraw
        import build_portal_translated_reports as portal
        image = Image.new('RGB', (640, 400), 'white')
        draw = ImageDraw.Draw(image)
        for index in range(8):
            draw.rectangle((40 + index * 65, 300 - index * 24, 70 + index * 65, 350), fill='blue')
        buffer = io.BytesIO(); image.save(buffer, format='PNG')
        markdown = b'# Original report\n\nThe source explains technology policy mechanisms.\n\n![Chart](images/chart.png)\n'
        raw = zip_bytes([('nested/full.md', markdown), ('nested/images/chart.png', buffer.getvalue())])
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / 'original_source'
            result = c.materialize(prepare_fixture(), destination, downloader=lambda _: raw)
            self.assertEqual(result['source_count'], 5)
            directories = portal.find_report_dirs(destination)
            self.assertEqual(len(directories), 5)
            for index, directory in enumerate(directories, 1):
                self.assertTrue(portal.report_title(directory).startswith(f'{index:04d}-consulting-report-'))
                clean, figures = portal.prepare_clean_markdown(directory, Path(temp) / f'portal-{index}', 28)
                self.assertIn('technology policy mechanisms', clean)
                self.assertEqual(len(figures), 1)
                self.assertTrue(Path(figures[0]['path']).is_file())
            self.assertEqual(list(destination.rglob('*.pdf')), [])

    def test_cli_failure_never_prints_exception_body_or_signed_url(self):
        f = fixture()
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); files = []
            for name, raw in (('receipt', f[0]), ('original-log', f[2]), ('original-manifest', f[3]), ('context', canonical(f[4]))):
                path = root / name; path.write_bytes(raw); files += ['--' + name, str(path)]
            objects = root / 'objects'
            for name, raw in f[1].items():
                path = objects / name; path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(raw)
            files += ['--objects-root', str(objects), '--output', str(root / 'source')]
            output = io.StringIO()
            environment = {'GITHUB_ACTIONS': 'true', 'GITHUB_REF': 'refs/heads/main',
                           'GITHUB_REPOSITORY': 'yt-feng/rpt_edit', 'GITHUB_EVENT_NAME': 'workflow_dispatch', 'GITHUB_WORKFLOW_REF':'yt-feng/rpt_edit/.github/workflows/mineru-legacy-consume.yml@refs/heads/main'}
            with patch.dict('os.environ', environment), patch('sys.argv', ['consumer', *files]), patch.object(c, 'materialize', side_effect=OSError('private-token https://private.example/?signed=secret')) as materialize, redirect_stdout(output):
                self.assertEqual(c.main(), 2)
            materialize.assert_called_once()
            text = output.getvalue()
            self.assertNotIn('private-token', text)
            self.assertNotIn('private.example', text)
            self.assertIn('legacy-consumption-rejected', text)

    def test_cli_denies_local_download_before_reading_input(self):
        output = io.StringIO()
        values = []
        for name in ('receipt', 'objects-root', 'original-log', 'original-manifest', 'context', 'output'):
            values.extend(['--' + name, '/nonexistent/' + name])
        with patch.dict('os.environ', {'GITHUB_ACTIONS': 'false'}), patch('sys.argv', ['consumer', *values]), patch.object(c, 'prepare') as prepare, redirect_stdout(output):
            self.assertEqual(c.main(), 2)
        prepare.assert_not_called()
        self.assertIn('legacy-consumption-rejected', output.getvalue())


class MaterializedVerificationTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(); self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)/'original_source'
        raw = zip_bytes([('nested/full.md', b'# Private original source\n\nBody grounded in original source.')])
        c.materialize(prepare_fixture(), self.root, downloader=lambda _: raw, asset_writer=fake_asset_writer)
        self.receipt = json.loads((self.root/'_legacy_output_receipt.json').read_bytes())

    def verify(self):
        return c.verify_materialized_output(self.root, canonical(self.receipt))

    def freeze(self):
        (self.root/'_legacy_output_receipt.json').write_bytes(canonical(self.receipt))

    def report_dir(self):
        return self.root/c.output_name(self.receipt['reports'][0]['source_pdf'])

    def rehash(self, path):
        relative = path.relative_to(self.root).as_posix()
        row = next(row for row in self.receipt['files'] if row['path'] == relative)
        payload = path.read_bytes(); row.update(sha256=c.digest(payload), bytes=len(payload))

    def change_status(self, change):
        status = self.receipt['reports'][0]; change(status)
        path = self.report_dir()/'status.json'; path.write_bytes(canonical(status)); self.rehash(path)
        self.freeze()

    def test_frozen_source_only_output_verifies_without_private_summary(self):
        result = self.verify()
        self.assertEqual(result['source_count'], 5)
        self.assertEqual(result['legacy_output_receipt_sha256'], c.digest(canonical(self.receipt)))
        self.assertIsNone(result['original_pdf_sha256'])
        self.assertFalse(result['canonical_task_admission'])
        for private in ('Private original', 'consulting-report', 'private.example'):
            self.assertNotIn(private, json.dumps(result))

    def test_modified_missing_and_extra_file_cannot_pass(self):
        path = self.report_dir()/'source_mineru.md'
        original = path.read_bytes(); path.write_bytes(original+b' forged')
        with self.assertRaisesRegex(c.ConsumerError, 'materialized_files|materialized_file_hash'): self.verify()
        path.write_bytes(original); path.unlink()
        with self.assertRaisesRegex(c.ConsumerError, 'materialized_files'): self.verify()
        path.write_bytes(original)
        extra = self.root/'unapproved.pdf'; extra.write_bytes(b'new source')
        with self.assertRaisesRegex(c.ConsumerError, 'materialized_files'): self.verify()

    def test_symlink_is_rejected_even_when_pointing_to_valid_declared_bytes(self):
        path = self.report_dir()/'source_mineru.md'; other = self.root/'alias'
        other.symlink_to(path)
        with self.assertRaisesRegex(c.ConsumerError, 'materialized_files'): self.verify()

    def test_canonical_and_pdf_proof_claims_cannot_be_added(self):
        for key, bad in (('canonical_task_admission', True), ('original_source_bytes_proven', True),
                         ('original_pdf_sha256', 'a'*64), ('historical_token_fingerprint_proven', True), ('provider_posts', 1)):
            old = self.receipt[key]; self.receipt[key] = bad; self.freeze()
            with self.subTest(key=key), self.assertRaisesRegex(c.ConsumerError, 'materialized_receipt_contract'): self.verify()
            self.receipt[key] = old
        self.freeze()

    def test_exact_receipt_bytes_and_source_identity_are_required(self):
        path = self.root/'_legacy_output_receipt.json'; path.write_bytes(path.read_bytes()+b' ')
        with self.assertRaisesRegex(c.ConsumerError, 'materialized_receipt_hash'): self.verify()
        self.freeze(); self.receipt['context']['workflow_path'] = '.github/workflows/institution-pdf-to-wechat.yml'; self.freeze()
        with self.assertRaisesRegex(c.ConsumerError, 'materialized_context'): self.verify()

    def test_rehashed_status_cannot_change_batch_member_or_credential_slot(self):
        for key, value in (('batch_id', '00000000-0000-4000-8000-000000000009'),
                           ('data_id', 'different-original.pdf'), ('credential_slot', 'MINER_U_4'),
                           ('provider_response_sha256', 'f'*64)):
            original = self.receipt['reports'][0]['legacy_result'][key]
            self.change_status(lambda status: status['legacy_result'].update({key: value}))
            with self.subTest(key=key), self.assertRaisesRegex(c.ConsumerError, 'materialized_provenance'): self.verify()
            self.change_status(lambda status: status['legacy_result'].update({key: original}))

    def test_rehashed_markdown_and_map_cannot_depart_from_retained_original(self):
        path = self.report_dir()/'source_mineru.md'; path.write_bytes(b'Forged source content.')
        self.rehash(path)
        mapping_path = self.report_dir()/'source_image_map.json'
        mapping = json.loads(mapping_path.read_bytes()); mapping['source_sha256'] = c.digest(path.read_bytes())
        mapping_path.write_bytes(canonical(mapping)); self.rehash(mapping_path)
        self.change_status(lambda status: status['legacy_result'].update(source_markdown_sha256=c.digest(path.read_bytes())))
        with self.assertRaisesRegex(c.ConsumerError, 'materialized_markdown'): self.verify()

    def test_rehashed_image_map_must_still_match_markdown(self):
        path = self.report_dir()/'source_image_map.json'
        value = json.loads(path.read_bytes()); value['source_sha256'] = 'f'*64
        path.write_bytes(canonical(value)); self.rehash(path); self.freeze()
        with self.assertRaisesRegex(c.ConsumerError, 'materialized_image_map'): self.verify()

    def test_receipt_cannot_declare_duplicate_or_escaping_paths(self):
        original = deepcopy(self.receipt['files'])
        self.receipt['files'].append(deepcopy(self.receipt['files'][0])); self.freeze()
        with self.assertRaisesRegex(c.ConsumerError, 'materialized_files'): self.verify()
        self.receipt['files'] = original; self.receipt['files'][0]['path'] = '../escape'; self.freeze()
        with self.assertRaisesRegex(c.ConsumerError, 'materialized_files'): self.verify()

    def test_http_error_preserves_status_without_body_or_url(self):
        import urllib.error
        opener = unittest.mock.MagicMock()
        opener.open.side_effect = urllib.error.HTTPError('https://private.example/?signed=secret', 403,
                                                         'private error body', {}, io.BytesIO(b'private body'))
        with patch('consume_legacy_mineru.urllib.request.build_opener', return_value=opener):
            with self.assertRaises(c.ResultHTTPError) as caught: c.download_once('https://private.example/result')
        self.assertEqual(caught.exception.category, 'result_http')
        self.assertEqual(caught.exception.http_status, 403)
        self.assertEqual(str(caught.exception), 'result_http')
        self.assertEqual(opener.open.call_count, 1)


if __name__ == '__main__':
    unittest.main()
