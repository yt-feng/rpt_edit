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

    def test_both_real_builders_accept_free_fallback_and_include_credits(self):
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
                self.assertEqual(3,built['article']['content'].count('data-editorial-credit="1"'))
                self.assertNotIn('pollinations.ai',built['article']['content'])
                self.assertEqual('good-cover',built['article']['thumb_media_id'])

    def test_real_commons_credit_is_adjacent_to_its_only_image_and_html_escaped(self):
        metadata={'source':'wikimedia_commons','author':'A <script>x</script>','license':'CC BY 4.0','license_url':'https://creativecommons.org/licenses/by/4.0/','source_url':'https://commons.wikimedia.org/wiki/File:Photo.jpg','caption':'配图'}
        credit=attribution_html(metadata)
        content,*_=portal.render_fitted_wechat_html('正文完整句子。\n\n第二段完整句子。','高盛：行业观察',portal.BRAND,{},[{'url':'https://mmbiz.qpic.cn/mmbiz_jpg/example/0','token':'generic','attribution':credit}],'',portal.BOTTOM_DISCLAIMER,'','source.pdf',1200,19500,18000)
        self.assertIn(credit,content)
        self.assertNotIn('<script>',content)
        self.assertIn('licenses/by/4.0',content)
        self.assertEqual(1,content.count('data-editorial-credit="1"'))

if __name__=='__main__':unittest.main()
