"""Additional negative contracts; fixtures are synthetic, not translated pages."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock
import test_portal_extended_locales as fixtures
from test_portal_extended_locales import FakeTranslator, HOME, BLOG, corpus, html
from portal_extended_locales import (ExpansionError, digest, document_from_html, make_corpus, stable_bytes)
from build_portal_extended_locales import build, Memo, validate_text
from collect_portal_extended_sources import collect_local, select_urls
from assemble_portal_extended_locales import assemble

class HardeningTests(unittest.TestCase):
    def test_english_target_cannot_accept_chinese_output(self):
        with self.assertRaises(ExpansionError):
            validate_text('Public research document.', '这是一段中文译文。', 'en', 'en')

    def test_english_brand_literal_is_not_misclassified(self):
        validate_text('KC桌面 research library', 'KC桌面 research library', 'en', 'en')

    def test_nested_cell_paragraphs_preserve_full_table_rows(self):
        doc = document_from_html(HOME, html(body='<h1>Library</h1><table><tr><td><p>Revenue</p></td><td><p>USD10m</p></td></tr></table>'))
        self.assertIn({'tag': 'tr', 'text': 'Revenue | USD10m'}, doc['blocks'])

    def test_alias_source_paths_cannot_overwrite_the_same_file(self):
        first = document_from_html(HOME, html())
        second = copy.deepcopy(first)
        second['url'] = HOME + 'reports/index.html'
        second['content_sha256'] = digest(stable_bytes({k:v for k,v in second.items() if k != 'content_sha256'}))
        third = copy.deepcopy(second); third['url'] = HOME + 'reports/'
        third['content_sha256'] = digest(stable_bytes({k:v for k,v in third.items() if k != 'content_sha256'}))
        with self.assertRaises(ExpansionError): make_corpus([first, second, third])

    def test_missing_homepage_is_not_an_activatable_candidate(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with self.assertRaises(ExpansionError):
                build(make_corpus([corpus()['documents'][1]]), 'fr', root/'out', root/'memo.json', FakeTranslator())
            self.assertFalse((root/'out').exists())

    def test_symlink_checkpoint_is_rejected_without_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); target = root/'protected.json'; target.write_text('unchanged')
            link = root/'memo.json'; link.symlink_to(target)
            with self.assertRaises(ExpansionError):
                build(corpus(), 'fr', root/'out', link, FakeTranslator())
            self.assertEqual(target.read_text(), 'unchanged')

    def test_symlink_candidate_directory_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); (root/'protected').mkdir(); (root/'out').symlink_to(root/'protected', target_is_directory=True)
            with self.assertRaises(ExpansionError):
                build(corpus(), 'fr', root/'out', root/'memo.json', FakeTranslator())
            self.assertFalse(list((root/'protected').iterdir()))

    def test_homepage_has_priority_even_in_unsorted_inventory(self):
        self.assertEqual(select_urls([BLOG, HOME+'/reports/', HOME], 1), [HOME])

    def test_local_collection_rejects_oversize_before_reading(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); (root/'index.html').write_bytes(html())
            with mock.patch('collect_portal_extended_sources.MAX_DOCUMENT_BYTES', 1):
                with self.assertRaises(ExpansionError): collect_local(root, 1)

    def test_prior_assembly_cannot_silently_drop_previous_languages(self):
        fixture = fixtures.AssemblyTests('test_dry_run_writes_nothing'); fixture.setUp()
        try:
            fixture.runbuild(); root, _ = fixture.staging()
            p=root/'data/extended-locales/assembly.json';p.parent.mkdir(parents=True);p.write_text('{}')
            with self.assertRaisesRegex(ExpansionError,'fresh inactive tree'):
                assemble(root,fixture.c,[fixture.base/'candidate'],('fr',),apply=True)
            self.assertFalse((root/'fr').exists())
        finally: fixture.tearDown()

if __name__ == '__main__':
    unittest.main()
