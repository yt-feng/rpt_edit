import json
from pathlib import Path
from types import SimpleNamespace
import tempfile
import unittest
from unittest.mock import patch
import push_portal_translated_to_wechat_drafts as portal
import push_xhs_notes_to_wechat_drafts as xhs
from free_editorial_images import bundled_fallback_image, attribution_html

class EditorialIntegrationTests(unittest.TestCase):
    def args(self):
        return SimpleNamespace(author=portal.AUTHOR,body_hook='',brand=portal.BRAND,content_source_url='',disclaimer=portal.BOTTOM_DISCLAIMER,dry_run=False,image_upload_delay_seconds=0,max_body_chars=1200,max_content_bytes=18000,max_content_chars=19500,max_inline_images=3,min_inline_images=3,timeout=30)

    def test_both_real_builders_accept_free_fallback_without_annotations(self):
        for module, filename in ((portal,'translated.md'),(xhs,'wechat_article.md')):
            with self.subTest(builder=module.__name__), tempfile.TemporaryDirectory() as temp:
                root=Path(temp);report=root/'GS-semiconductor';report.mkdir()
                markdown='# 高盛：半导体订单与交付周期更新\n\n## 订单交付观察\n\n报告记录了订单变化。企业表示产能建设仍在推进。\n'
                (report/filename).write_text(markdown)
                (report/'status.json').write_text(json.dumps({'source_pdf':'GS-semiconductor.pdf'}))
                (report/'translation_status.json').write_text(json.dumps({'source_pdf':'GS-semiconductor.pdf'}))
                def download(_session, title, target, timeout, index=1, cache_dir=None):
                    return bundled_fallback_image(target,title,index)
                urls=iter(f'https://mmbiz.qpic.cn/mmbiz_jpg/image{i}/0' for i in range(3))
                with patch.object(portal,'download_editorial_image',side_effect=download) as provider, patch.object(module,'upload_article_image',side_effect=lambda *a:next(urls)), patch.object(module,'upload_cover_material',return_value='good-cover'):
                    built=module.build_article(report,1,self.args(),object(),'token',root/'out','')
                self.assertEqual(3,provider.call_count)
                self.assertEqual(3,built['body_image_count'])
                self.assertNotIn('data-editorial-credit',built['article']['content'])
                self.assertNotIn('主题示意图',built['article']['content'])
                self.assertNotIn('pollinations.ai',built['article']['content'])
                self.assertEqual('good-cover',built['article']['thumb_media_id'])

    def test_render_discards_cached_annotation_and_markdown_variants_preserves_data_sources(self):
        variants=['主题示意图：Portal Suite 原创插画，非实拍或数据图。',
                  '主題示意圖：Ｐｏｒｔａｌ Ｓｕｉｔｅ 原創插畫，非實拍或數據圖。',
                  '<p><span>主题示意图：Portal Suite 原创插画，非实拍或数据图。</span></p>']
        credit='<p class="image-credit" data-editorial-credit="1">'+variants[0]+'</p>'
        for note in variants:
            for reference in ('', '![报告图表](source.png)'):
                with self.subTest(note=note, reference=bool(reference)):
                    markdown='正文完整句子。\n\n'+reference+'\n\n'+note+'\n\n图表1：年度收入增长。\n\n数据来源：公司年报。'
                    content,*_=portal.render_fitted_wechat_html(markdown,'高盛：行业观察',portal.BRAND,
                        {'source.png':'https://mmbiz.qpic.cn/example/0'},
                        [{'url':'https://mmbiz.qpic.cn/example/0','alt':'source.png','attribution':credit}],
                        '',portal.BOTTOM_DISCLAIMER,'','source.pdf',1200,19500,18000)
                    self.assertNotIn('原创插画',content);self.assertNotIn('原創插畫',content)
                    self.assertNotIn('data-editorial-credit',content)
                    self.assertIn('图表1：年度收入增长',content);self.assertIn('数据来源：公司年报',content)
                    self.assertIn('Original report: source.pdf',content)

    def test_cover_only_production_uses_photo_provider_in_both_builders(self):
        for module, filename in ((portal,'translated.md'),(xhs,'wechat_article.md')):
            with self.subTest(builder=module.__name__), tempfile.TemporaryDirectory() as temp:
                root=Path(temp);report=root/'GS-semiconductor';report.mkdir()
                (report/filename).write_text('# 高盛：半导体行业数据更新\n\n行业数据出现新的变化。')
                (report/'status.json').write_text(json.dumps({'source_pdf':'GS-semiconductor.pdf'}))
                (report/'translation_status.json').write_text(json.dumps({'source_pdf':'GS-semiconductor.pdf'}))
                args=self.args();args.min_inline_images=0;args.max_inline_images=0
                def download(_session,title,target,timeout,index=1,cache_dir=None):
                    return bundled_fallback_image(target,title,index)
                with patch.object(portal,'download_editorial_image',side_effect=download) as provider, \
                     patch.object(module,'upload_cover_material',return_value='stock-cover'):
                    built=module.build_article(report,1,args,object(),'token',root/'out','')
                provider.assert_called_once();self.assertEqual(0,provider.call_args.kwargs['index'])
                self.assertEqual(0,built['body_image_count']);self.assertEqual('stock-cover',built['article']['thumb_media_id'])

if __name__=='__main__':unittest.main()
