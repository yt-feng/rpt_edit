#!/usr/bin/env python3
"""Offline regression contracts for source-grounded discovery improvements."""
from __future__ import annotations

from argparse import Namespace
from copy import deepcopy
from datetime import date
import json
from pathlib import Path
import re
import sys
import tempfile
import unittest
from unittest import mock
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import portal_discovery_quality as quality
import build_portal_suite_site as builder
import translate_portal_titles as titles
import audit_portal_seo_live as audit

BASE = builder.SITE_BASE_URL


def report(report_id='report-a', **extra):
    return {'id': report_id, 'title': 'BofA-Micron (MU.US)-Memory outlook-260922',
            'filename': 'BofA-Micron (MU.US)-Memory outlook-260922.pdf',
            'title_zh': '美银：美光存储器研究', 'bank_code': 'BofA', 'bank_name': 'Bank of America',
            'industry': 'Tech / AI / Semis', 'date_folder': '260922',
            'server_modified': '2026-09-22T08:00:00Z', 'page_count': 12,
            'available': True, 'pdf_archived': False, **extra}


def article(**extra):
    return {'slug': '20260923-0123456789abcdef', 'title': '美银：美光存储器研究解读',
            'digest': '本文梳理存储器需求的研究口径。',
            'content': '<p>本文梳理存储器需求的研究口径。</p><p>Original report: '
                       'BofA-Micron (MU.US)-Memory outlook-260922</p>',
            'date': '2026-09-23', 'last_date': '2026-09-23', 'author': 'KC桌面',
            'source': 'root', 'origins': [{'source': 'root', 'date': '2026-09-23'}], **extra}


def nodes(html):
    found = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
    schema = json.loads(found[1])
    return {node['@type']: node for node in schema.get('@graph', [schema])}


class InstitutionQualityTests(unittest.TestCase):
    def test_known_mistranslations_are_repaired_without_changing_other_banks_in_body(self):
        for wrong in ('花旗', '摩根大通'):
            fixed = quality.repair_institution_prefix('BofA-Global FX Weekly', wrong + '：外汇与花旗观点比较', builder.INSTITUTION_HUBS)
            self.assertEqual(fixed, '美银：外汇与花旗观点比较')
        self.assertEqual(quality.repair_institution_prefix('Comparison with BofA', '花旗：对比', builder.INSTITUTION_HUBS), '花旗：对比')

    def test_source_prefix_boundaries_and_multiword_aliases(self):
        for source in ('Microsystems', 'MSCI outlook', 'DBS outlook', 'GoldmanSachsville outlook'):
            self.assertEqual(quality.institution_prefix(source, builder.INSTITUTION_HUBS), (None, 0))
        definition, _ = quality.institution_prefix('Goldman Sachs: Micron', builder.INSTITUTION_HUBS)
        self.assertEqual(definition['slug'], 'goldman-sachs')

    def test_new_translation_protects_institution_and_numeric_identifiers(self):
        translator = mock.Mock()
        translator.translate.return_value = '__KC_PH_0002__-美光__KC_PH_0000__增长12.5%__KC_PH_0001__'
        actual = titles.translate_title('BofA-Micron(MU.US) growth 12.5%-260922', Namespace(_offline_translator=translator))
        self.assertEqual(actual, '美银-美光(MU.US)增长12.5%-260922')
        self.assertIn('12.5%', translator.translate.call_args.args[0])
        self.assertNotIn('BofA', translator.translate.call_args.args[0])

    def test_mutated_institution_placeholder_is_rejected(self):
        translator = mock.Mock()
        translator.translate.return_value = '花旗-错误译名'
        with self.assertRaisesRegex(RuntimeError, 'protected title identifier'):
            titles.translate_title('BofA-Outlook', Namespace(_offline_translator=translator))

    def test_placeholder_failure_retries_once_with_visible_boundaries(self):
        translator = mock.Mock()
        translator.translate.side_effect = [
            RuntimeError("Hy-MT2 changed, omitted, or duplicated a protected placeholder"),
            "__KC_PH_0001__-香港股票策略专家访谈要点 __KC_PH_0000__",
        ]
        result = titles.translate_title(
            'JPM-Hong Kong Equity Strategy Expert Call takeaways-260918',
            Namespace(_offline_translator=translator),
        )
        self.assertEqual(result, '摩根大通-香港股票策略专家访谈要点 -260918')
        self.assertEqual(translator.translate.call_count, 2)
        self.assertIn('takeaways __KC_PH_0000__', translator.translate.call_args.args[0])

    def test_retry_never_accepts_damaged_output_or_loops(self):
        translator = mock.Mock()
        translator.translate.return_value = '没有保留标识符'
        with self.assertRaisesRegex(RuntimeError, 'protected title identifier'):
            titles.translate_title('JPM-Outlook-260918', Namespace(_offline_translator=translator))
        self.assertEqual(translator.translate.call_count, 2)

    def test_quantity_failure_is_not_retried_as_a_placeholder_error(self):
        translator = mock.Mock()
        translator.translate.side_effect = RuntimeError('financial quantity mismatch')
        with self.assertRaisesRegex(RuntimeError, 'financial quantity mismatch'):
            titles.translate_title('JPM-Growth 12.5%-260918', Namespace(_offline_translator=translator))
        self.assertEqual(translator.translate.call_count, 1)

    def test_existing_catalog_repairs_without_model_request(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'catalog.json'
            path.write_text(json.dumps({'items': [report(title_zh='花旗：美光存储器研究')]}))
            with mock.patch.object(sys, 'argv', ['titles', '--catalog-path', str(path)]), mock.patch.object(titles, 'OfflineTranslator') as engine:
                self.assertEqual(titles.main(), 0)
            engine.assert_not_called()
            self.assertEqual(json.loads(path.read_text())['items'][0]['title_zh'], '美银：美光存储器研究')

    def test_dry_run_preserves_existing_catalog_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'catalog.json'
            path.write_text(json.dumps({'items': [report(title_zh='花旗：美光存储器研究')]}))
            before = path.read_bytes()
            with mock.patch.object(sys, 'argv', ['titles', '--catalog-path', str(path), '--dry-run']):
                titles.main()
            self.assertEqual(path.read_bytes(), before)

    def test_cache_and_public_rendering_cannot_restore_wrong_prefix(self):
        source = 'BofA-Global FX Weekly'
        entry = {'source': source, 'model': titles.MODEL_ID, 'prompt_version': titles.TITLE_PROMPT_VERSION, 'title_zh': '摩根大通：全球外汇周报'}
        key = titles.title_cache_key(source, titles.MODEL_ID)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'cache.json'
            path.write_text(json.dumps({'schema_version': 1, 'provider': titles.PROVIDER, 'entries': {key: entry}}))
            self.assertEqual(titles.load_title_cache(path)['entries'][key]['title_zh'], '美银：全球外汇周报')
        item = report(title=source, title_zh='花旗：全球外汇周报')
        self.assertEqual(builder.item_display_title(item), '美银：全球外汇周报')
        self.assertEqual(builder.public_catalog_item(item)['title_zh'], '美银:全球外汇周报')
        self.assertTrue(builder.report_browser_title(item).startswith('美银'))


class SourceMatchingTests(unittest.TestCase):
    def test_exact_name_links_punctuation_but_retains_report_date(self):
        idx = quality.ReportSourceIndex([report()])
        self.assertEqual(idx.resolve(article())[0], 'matched')
        self.assertEqual(idx.resolve(article(content='<p>Original report: BofA Micron MU.US Memory outlook 260921</p>'))[0], 'unmatched')

    def test_pipeline_counter_is_removed_only_before_known_bank(self):
        self.assertEqual(quality.document_name_key('09-BofA-Micron(MU.US)-260922.pdf'), quality.document_name_key('BofA Micron MU.US 260922'))
        self.assertNotEqual(quality.document_name_key('2026 forecast'), quality.document_name_key('forecast'))

    def test_duplicates_ambiguous_and_explicit_conflict_are_not_linked(self):
        idx = quality.ReportSourceIndex([report(), report('report-b')])
        self.assertEqual(idx.resolve(article())[0], 'ambiguous')
        other = report('other', title='UBS-Nvidia-260922', filename='UBS-Nvidia-260922.pdf')
        idx = quality.ReportSourceIndex([report(), other])
        self.assertEqual(idx.resolve(article(source_report_id='other'))[0], 'conflict')
        self.assertEqual(idx.resolve(article(source_report_id='report-a'))[0], 'matched')

    def test_multiple_sources_remain_ambiguous_and_fake_footer_script_ignored(self):
        idx = quality.ReportSourceIndex([report()])
        content = article()['content'] + '<p>Original report: UBS-Nvidia-260922</p>'
        self.assertEqual(idx.resolve(article(content=content))[0], 'ambiguous')
        content = '<script>Original report: BofA-Micron(MU.US)-Memory outlook-260922</script>'
        self.assertEqual(idx.resolve(article(content=content))[0], 'not_provided')

    def test_original_sidecar_wins_over_sanitized_footer_not_over_conflicting_id(self):
        row = article(source_report_name=report()['filename'], content='<p>Original report: BofA-经清洗的展示标题</p>')
        self.assertEqual(quality.ReportSourceIndex([report()]).resolve(row)[0], 'matched')
        row['source_report_id'] = 'unknown'
        self.assertEqual(quality.ReportSourceIndex([report()]).resolve(row)[0], 'unmatched')

    def test_source_metadata_never_exposes_directories_or_urls(self):
        self.assertEqual(quality.report_source_metadata({'source_pdf': '/private/batches/BofA-Micron.pdf'}), {'source_report_name': 'BofA-Micron.pdf'})
        for value in ('s3://private/token.pdf', 'https://example.com/a.pdf?token=secret', '../', '<script>.pdf'):
            self.assertEqual(quality.report_source_metadata({'source_pdf': value}), {})

    def test_schema_source_card_and_report_backlinks_share_canonical(self):
        row = builder.prepare_blog_discovery([article()], [report()])[0]
        rendered = builder.render_blog_article(row, BASE)
        schema = nodes(rendered)['BlogPosting']
        self.assertEqual(schema['citation']['url'], BASE + '/reports/report-a.html')
        self.assertNotIn('datePublished', schema['citation'])
        self.assertIn('目录收录日期：2026-09-22', rendered)
        self.assertIn('本篇依据的报告', rendered)
        back = builder.render_report_seo_page(report(), BASE, '2026-09-23', source_articles=[row])
        self.assertIn('/blog/' + row['slug'] + '.html', back)
        self.assertEqual(nodes(back)['Report']['abstract'], builder.report_citable_summary(report()))
        published = builder.prepare_blog_discovery([article()], [report(published_at='2026-09-21')])[0]
        card, schema = builder.render_blog_source_card(published, BASE)
        self.assertIn('原报告发布日期：2026-09-21', card)
        self.assertEqual(schema['datePublished'], '2026-09-21')

    def test_draft_sidecar_roundtrip_preserves_fingerprint_and_slug(self):
        with tempfile.TemporaryDirectory() as directory:
            drafts = Path(directory) / 'drafts'
            path = drafts / 'root' / '260922' / 'draft_payload_01.json'
            path.parent.mkdir(parents=True)
            raw = article()
            api_article = {key: raw[key] for key in ('title', 'content', 'digest', 'author')}
            payload = {'articles': [api_article], 'source_reports': [{'source_report_name': report()['filename']}]}
            path.write_text(json.dumps(payload))
            rows = builder.load_blog_draft_articles(drafts, date(2026, 7, 27))
            self.assertEqual(rows[0]['source_report_name'], report()['filename'])
            self.assertEqual(rows[0]['fingerprint'], builder.blog_article_fingerprint(api_article['title'], api_article['content']))
            archive = Path(directory) / 'archive'
            builder.persist_blog_archive(archive, rows, date(2026, 7, 27))
            loaded = builder.load_blog_archive(archive, date(2026, 7, 27))
            self.assertEqual(loaded[0]['slug'], rows[0]['slug'])
            self.assertEqual(loaded[0]['source_report_name'], report()['filename'])
            payload['source_reports'] = []
            path.write_text(json.dumps(payload))
            with self.assertRaisesRegex(ValueError, 'align'):
                builder.load_blog_draft_articles(drafts, date(2026, 7, 27))


class DisplayQualityTests(unittest.TestCase):
    def test_sentence_excerpt_keeps_decimals_and_never_manufactures_a_period(self):
        value = 'Earnings were 4.10 dollars. The next sentence is much too long for this budget.'
        self.assertEqual(quality.sentence_excerpt(value, 30), 'Earnings were 4.10 dollars.')
        self.assertEqual(quality.sentence_excerpt('未结束的长句' * 30, 50), '')
        self.assertEqual(quality.sentence_excerpt('短摘要', 50), '短摘要')

    def test_known_fedex_repair_is_guarded_and_archive_is_unchanged(self):
        override = builder.discovery_editorial_overrides()['20260922-3526286512146198']
        raw = article(slug='20260922-3526286512146198', title=override['expected_title'],
                      content='<p>' + override['expected_title'] + '</p><p>FedEx Freight（FDXF）盈利预测按日历年整理。</p>')
        before = deepcopy(raw)
        fixed = builder.prepare_blog_discovery([raw], [])[0]
        self.assertEqual(raw, before)
        self.assertEqual(fixed['title'], builder.public_brand_text(override['title']))
        self.assertNotIn(override['expected_title'], fixed['content'])
        self.assertEqual(fixed['slug'], raw['slug'])
        no_match = article(slug=raw['slug'], title=raw['title'], content='<p>无对应来源内容。</p>')
        self.assertEqual(builder.prepare_blog_discovery([no_match], [])[0]['title'], raw['title'])

    def test_historic_digest_drops_duplicate_banner_and_partial_final_sentence(self):
        title = '美光行业观察'
        digest = '外资精译 ' + title + ' ' + '这是有完整口径的研究句子。' * 12 + '这是被截断的下一句'
        fixed = builder.prepare_blog_discovery([article(title=title, digest=digest)], [])[0]['digest']
        self.assertNotIn(title, fixed)
        self.assertNotIn('被截断', fixed)
        self.assertTrue(fixed.endswith('。'))

    def test_ticker_and_fine_topic_relevance_reaches_beyond_latest_40(self):
        seed = report('seed', date_folder='260601', server_modified='2026-06-01T00:00:00Z')
        older = report('older', title='UBS-Micron(MU.US)-DRAM research', bank_code='UBS', bank_name='UBS', date_folder='260602', server_modified='2026-06-02T00:00:00Z')
        unrelated = [report(f'other-{i}', title=f'BofA-Microsoft cloud {i}', filename=f'BofA-Microsoft cloud {i}.pdf', title_zh=f'微软云研究{i}') for i in range(70)]
        result = builder.build_related_reports([seed, older, *unrelated])
        self.assertEqual(result['seed'][0]['id'], 'older')
        self.assertNotIn('seed', [row['id'] for row in result['seed']])
        self.assertEqual(result, builder.build_related_reports([seed, older, *unrelated]))

    def test_short_ticker_does_not_match_unrelated_word(self):
        self.assertNotIn('micron', quality.research_entities('museum music MU volume')[0])
        self.assertIn('micron', quality.research_entities('Company (MU.US)')[0])

    def test_topic_hub_does_not_use_incidental_full_body(self):
        definition = next(row for row in builder.TOPIC_HUBS if row['slug'] == 'tech-ai-semis')
        incidental = article(title='欧洲通胀走势', digest='消费者价格口径变化。', content='<p>Artificial intelligence data centers semiconductors.</p>')
        focused = article(title='HBM存储器与半导体行业', digest='AI需求口径。')
        rows = builder.topic_hub_related_articles(definition, [incidental, focused])
        self.assertEqual(rows, [focused])

    def test_home_has_crawlable_reports_and_articles_without_javascript(self):
        html = builder.render_home_discovery([report(f'r-{i}') for i in range(30)], [article(slug=f'article-{i}') for i in range(10)], BASE)
        self.assertEqual(len(re.findall(r'href="[^" ]*/reports/r-\d+\.html"', html)), 24)
        self.assertEqual(len(re.findall(r'href="[^" ]*/blog/article-\d+\.html"', html)), 6)
        self.assertNotIn('<script', html)
        source = (ROOT / 'portal_suite/site_src/index.html').read_text()
        self.assertIn('PUBLIC_DISCOVERY_START', source)
        self.assertIn('id="searchInput"', source)

    def test_hub_pagination_canonical_sitemap_and_stable_entities(self):
        items = [report(f'r-{i}') for i in range(205)]
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory)
            builder.build_seo_outputs(out, {'items': items, 'updated_at_bjt': '2026-09-23 12:00:00'}, blog_articles=[])
            urls = {row.text for row in ET.parse(out / 'sitemap-pages.xml').getroot().findall('.//{*}loc')}
            for root, entity in [('reports/institutions/bank-of-america/', 'organization'), ('reports/topics/tech-ai-semis/', 'topic')]:
                for page, count in [(1, 100), (2, 100), (3, 5)]:
                    filename = 'index.html' if page == 1 else f'page-{page}.html'
                    canonical = BASE + '/' + root + ('' if page == 1 else filename)
                    self.assertIn(canonical, urls)
                    html = (out / root / filename).read_text()
                    schema = nodes(html)
                    self.assertEqual(schema['CollectionPage']['url'], canonical)
                    self.assertEqual(schema['ItemList']['numberOfItems'], count)
                    self.assertEqual(schema['CollectionPage']['about']['@id'], BASE + '/' + root + '#' + entity)
                    self.assertIn(f'rel="canonical" href="{canonical}"', html)
                    if page == 2:
                        self.assertIn('href="./"', html)
                        self.assertIn('href="page-3.html"', html)
                        self.assertIn('第 2 页', html)
            self.assertFalse((out / 'reports/institutions/ubs').exists())


class PublishedCrawlerPolicyTests(unittest.TestCase):
    def test_specific_search_groups_longest_rule_and_training_separation(self):
        text = 'User-agent: *\nDisallow: /\nUser-agent: OAI-SearchBot\nAllow: /\nDisallow: /api/\nUser-agent: GPTBot\nDisallow: /\n'
        self.assertTrue(audit.robots_path_allowed(text, 'OAI-SearchBot', '/reports/a.html'))
        self.assertFalse(audit.robots_path_allowed(text, 'OAI-SearchBot', '/api/private'))
        self.assertFalse(audit.robots_path_allowed(text, 'GPTBot', '/'))
        self.assertTrue(audit.robots_path_allowed('User-agent: *\nDisallow: /reports/*\nAllow: /reports/public$\n', 'Bingbot', '/reports/public'))
        self.assertFalse(audit.robots_path_allowed('User-agent: *\nDisallow: /reports/*\nAllow: /reports/public$\n', 'Bingbot', '/reports/public-other'))

    def test_grouped_agents_and_duplicate_group_merge(self):
        text = 'User-agent: OAI-SearchBot\nUser-agent: PerplexityBot\nDisallow: /reports/\nUser-agent: OAI-SearchBot\nAllow: /reports/open\n'
        self.assertFalse(audit.robots_path_allowed(text, 'PerplexityBot', '/reports/a'))
        self.assertTrue(audit.robots_path_allowed(text, 'OAI-SearchBot', '/reports/open'))

    def test_challenge_detection_and_readonly_audit_failure(self):
        import test_audit_portal_seo_live as fixtures
        routes = fixtures.healthy_routes()
        routes[BASE + '/robots.txt'] = fixtures.result(200, BASE + '/robots.txt', 'User-agent: *\nAllow: /\nSitemap: '+BASE+'/sitemap.xml\nUser-agent: OAI-SearchBot\nDisallow: /\n')
        response = fixtures.result(200, BASE + '/reports/report-a.html', '<title>Just a moment...</title>')
        self.assertTrue(audit.is_challenge_response(response))
        routes[response.final_url] = response
        result = audit.audit_site(BASE, indexnow_key=fixtures.KEY, sample_size=18, fetcher=fixtures.FakeFetcher(routes))
        serialized = json.dumps(result)
        self.assertIn('search_agent_blocked', serialized)
        self.assertIn('challenge_response', serialized)

    def test_new_contract_runs_in_production_validation_and_pr_checks(self):
        for filename in ('public-identity-guard.yml', 'neutral-edge-cutover.yml'):
            text = (ROOT / '.github/workflows' / filename).read_text()
            self.assertIn('scripts/test_portal_discovery_quality.py', text)
            if filename == 'neutral-edge-cutover.yml':
                self.assertIn('--build-contract scripts/portal_discovery_quality.py', text)
                self.assertIn('--build-contract portal_suite/discovery_editorial.json', text)


class PaginatedTopicIdentityTests(unittest.TestCase):
    def test_topic_page_titles_and_entity_urls_are_stable(self):
        definition = builder.TOPIC_HUBS[2]
        items = [report(f"topic-{index}") for index in range(201)]
        pages = [builder.render_topic_hub(definition, items, [], BASE, "2026-09-23", page_number=n)
                 for n in (1, 2, 3)]
        titles = [re.search(r"<title>(.*?)</title>", page).group(1) for page in pages]
        self.assertEqual(len(set(titles)), 3)
        self.assertIn("第 2 页", titles[1])
        root = BASE + "/" + builder.topic_hub_path(definition)
        for page in pages:
            entity = nodes(page)["CollectionPage"]["about"]
            self.assertEqual(entity["@id"], root + "#topic")
            self.assertEqual(entity["url"], root)


if __name__ == '__main__':
    unittest.main()
