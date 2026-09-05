from __future__ import annotations

from html.parser import HTMLParser
import json
import unittest
from unittest import mock

import portal_locale_scope as scope
from portal_locale_scope import deferred_locale_source, restrict_html_to_cohort


BASE = "https://portal.example.invalid"
CURRENT = BASE + "/blog/current/"
OLD = BASE + "/blog/old/"
NEW = BASE + "/blog/new/"
REPORT = BASE + "/reports/old-report/"
KNOWN = frozenset({CURRENT, OLD, NEW, REPORT})
ELIGIBLE = frozenset({CURRENT, NEW})


class _Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []

    def handle_data(self, data):
        self.text.append(data)


class LocaleScopeTests(unittest.TestCase):
    def restrict(self, source, *, canonical=CURRENT, eligible=ELIGIBLE):
        return restrict_html_to_cohort(source, canonical, eligible, KNOWN)

    def test_normalization_is_cached_across_pages_without_rewalking_inventory(self):
        scope._normalized_canonical_set.cache_clear()
        self.addCleanup(scope._normalized_canonical_set.cache_clear)
        with mock.patch.object(scope, "_canonical_identity", wraps=scope._canonical_identity) as normalize:
            self.assertEqual(self.restrict('<p>当前正文</p>'), '<p>当前正文</p>')
            first_count = normalize.call_count
            self.assertEqual(first_count, len(KNOWN) + len(ELIGIBLE) + 1)
            self.assertEqual(self.restrict('<p>另一篇正文</p>', canonical=NEW), '<p>另一篇正文</p>')
            self.assertEqual(normalize.call_count, first_count + 1)  # Only the new primary URL.
        self.assertEqual(scope._normalized_canonical_set.cache_info().hits, 2)

    def test_cached_scope_normalizes_mixed_urls_by_origin_and_keeps_primary_protected(self):
        known = frozenset({'/blog/old/', 'blog/new/index.html', CURRENT,
                           'https://external.example/blog/old/', '/?report=old'})
        eligible = frozenset({'/blog/new/'})
        source = '<a href="../old/">旧标题</a><a href="../new/">新文章</a><a href="./">当前文章</a><a href="https://external.example/blog/old/">外链</a>'
        result = restrict_html_to_cohort(source, CURRENT, eligible, known)
        self.assertEqual(result, source.split('</a>', 1)[1])
        # The same relative inventory is valid for another origin, without cache contamination.
        other = 'https://second.example.invalid/blog/current/'
        self.assertEqual(restrict_html_to_cohort('<a href="../old/">旧标题</a>', other, eligible, known), '')

    def test_normalized_inventory_cache_is_bounded(self):
        scope._normalized_canonical_set.cache_clear()
        self.addCleanup(scope._normalized_canonical_set.cache_clear)
        for index in range(12):
            scope._normalized_canonical_set(BASE + '/', frozenset({f'/blog/item-{index}/'}))
        self.assertEqual(scope._normalized_canonical_set.cache_info().maxsize, 8)
        self.assertEqual(scope._normalized_canonical_set.cache_info().currsize, 8)

    def test_nested_cards_remove_whole_old_card_but_keep_new_card_exactly(self):
        new = '<article class="blog-card"><h2><a href="../new/">新文章</a></h2><p>新摘要 &amp; 说明</p></article>'
        old = '<article class="featured blog-card"><div><h2><a href="../old/#intro"><em>旧标题</em></a></h2></div><p>旧摘要</p></article>'
        source = f'<main><div class="blog-card-grid">{old}{new}</div></main>'
        self.assertEqual(self.restrict(source), f'<main><div class="blog-card-grid">{new}</div></main>')

    def test_nested_lists_drop_nearest_list_item_not_outer_structure(self):
        source = '<ul><li>分类<ul><li><span><a href="/reports/old-report/?from=related">旧报告</a></span>旧说明</li><li><a href="../new/">新文章</a></li></ul></li></ul>'
        expected = '<ul><li>分类<ul><li><a href="../new/">新文章</a></li></ul></li></ul>'
        self.assertEqual(self.restrict(source), expected)

    def test_optional_li_end_tags_do_not_remove_next_sibling(self):
        self.assertEqual(self.restrict('<ul><li><a href="../old/">旧标题</a><li>保留</ul>'), '<ul><li>保留</ul>')

    def test_primary_article_and_legal_panel_keep_body_only_excluded_anchor_removed(self):
        source = '<main><article><h1>当前文章</h1><p>当前正文 <a href="../old/">旧标题</a> 继续正文。</p></article><li class="legal-panel">法律说明 <a href="../old/">旧标题</a> 保留法律条款。</li></main>'
        expected = '<main><article><h1>当前文章</h1><p>当前正文  继续正文。</p></article><li class="legal-panel">法律说明  保留法律条款。</li></main>'
        self.assertEqual(self.restrict(source), expected)

    def test_standalone_anchor_removed_including_nested_text(self):
        source = '前文 <a HREF="../old/index.html"><strong>旧标题</strong>旧摘要</a> 后文'
        self.assertEqual(self.restrict(source), '前文  后文')

    def test_external_assets_query_home_and_unknown_links_are_unchanged(self):
        source = "\n".join([
            '<a href="https://other.example/blog/old/">外链</a>',
            '<a href="//other.example/blog/old/">外链二</a>',
            '<a href="/assets/old.pdf">共享附件</a>',
            '<a href="/?report=/blog/old/">首页查询</a>',
            '<a href="/index.html?topic=old">首页主题</a>',
            '<a href="/blog/unknown/">未知详情</a>',
            '<a href="mailto:editor@example.com">联系</a>',
            '<a href="#section">当前锚点</a>',
        ])
        self.assertEqual(self.restrict(source), source)

    def test_jsonld_removes_old_titles_references_and_reindexes_itemlist(self):
        payload = {"@context": "https://schema.org", "@graph": [
            {"@type": "Article", "url": CURRENT, "headline": "当前标题", "articleBody": "当前完整正文",
             "citation": OLD, "isRelatedTo": {"@type": "Report", "url": REPORT, "name": "旧报告标题"}},
            {"@type": "ItemList", "numberOfItems": 3, "itemListElement": [
                {"@type": "ListItem", "position": 1, "url": OLD, "name": "旧文章标题"},
                {"@type": "ListItem", "position": 2, "item": {"@type": "Article", "@id": NEW, "headline": "新标题"}},
                {"@type": "ListItem", "position": 3, "item": {"@type": "Report", "mainEntityOfPage": {"@id": REPORT}, "headline": "旧报告标题"}},
            ]},
            {"@type": "Report", "mainEntityOfPage": REPORT, "headline": "旧报告标题"},
        ]}
        source = '<script type="application/ld+json">\n' + json.dumps(payload, ensure_ascii=False) + '\n</script>'
        result = self.restrict(source)
        self.assertNotIn("旧文章标题", result)
        self.assertNotIn("旧报告标题", result)
        self.assertNotIn(OLD, result)
        self.assertNotIn(REPORT, result)
        filtered = json.loads(result.split('>', 1)[1].rsplit('</script>', 1)[0])
        graph = filtered["@graph"]
        self.assertEqual(len(graph), 2)
        self.assertEqual(graph[0]["articleBody"], "当前完整正文")
        self.assertEqual(graph[1]["numberOfItems"], 1)
        self.assertEqual(graph[1]["itemListElement"][0]["position"], 1)

    def test_breadcrumb_core_and_primary_identity_survive_even_when_not_eligible(self):
        payload = {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "item": BASE + "/", "name": "首页"},
            {"@type": "ListItem", "position": 2, "item": BASE + "/blog/", "name": "文章"},
            {"@type": "ListItem", "position": 3, "item": OLD, "name": "旧标题"},
            {"@type": "ListItem", "position": 4, "item": CURRENT, "name": "当前标题"},
        ]}
        source = '<script type="application/ld+json">' + json.dumps(payload) + '</script><a href="./">当前标题</a>'
        result = self.restrict(source, eligible=frozenset({NEW}))
        filtered = json.loads(result.split('>', 1)[1].split('</script>', 1)[0])
        self.assertEqual([row["name"] for row in filtered["itemListElement"]], ["首页", "文章", "当前标题"])
        self.assertEqual([row["position"] for row in filtered["itemListElement"]], [1, 2, 3])
        self.assertTrue(result.endswith('<a href="./">当前标题</a>'))

    def test_jsonld_array_and_scripts_inside_removed_card_have_no_overlapping_edits(self):
        document = json.dumps([{"@type": "Article", "url": OLD, "headline": "旧标题"}, {"@type": "Article", "url": NEW, "headline": "新标题"}])
        card = f'<article class="blog-card"><a href="../old/">旧标题</a><script type="application/ld+json">{document}</script></article>'
        self.assertEqual(self.restrict(card + "<p>保留</p>"), "<p>保留</p>")

    def test_no_removal_preserves_source_byte_for_byte_and_result_is_deterministic(self):
        source = '<!DOCTYPE html>\n<!-- 保留 --> <A href="../new/"> 新 &amp; 文 </A>\n<script type="application/ld+json"> { "url": "' + CURRENT + '" } </script>'
        self.assertEqual(self.restrict(source), source)
        restricted = self.restrict(source + '<a href="../old/">旧标题</a>')
        self.assertEqual(restricted, source)
        self.assertEqual(self.restrict(restricted), restricted)

    def test_deferred_source_is_generic_noindex_complete_and_escaped(self):
        canonical = CURRENT + '?x="quoted"&y=1'
        result = deferred_locale_source(canonical)
        self.assertTrue(result.startswith('<!doctype html>'))
        self.assertTrue(result.endswith('</body></html>'))
        self.assertIn('lang="zh-CN"', result)
        self.assertIn('content="noindex,follow"', result)
        self.assertIn('此内容暂未开放多语言版本，请浏览最新文章。', result)
        self.assertIn('x=&quot;quoted&quot;&amp;y=1', result)
        for path in ('/', '/blog/', '/reports/'):
            self.assertIn(f'href="{path}"', result)
        text = _Text()
        text.feed(result)
        self.assertNotIn("current", ''.join(text.text))
        self.assertEqual(result, deferred_locale_source(canonical))


if __name__ == "__main__":
    unittest.main()
