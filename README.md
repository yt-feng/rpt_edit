# rpt_edit

把 Dropbox 或 repo 里的 PDF 批量转成小红书笔记、统一视觉风格配图、微信公众号文章草稿、市场观点 PDF、双语讲解视频，并维护一个脱敏 PDF 搜索页。

## 快速开始

1. 在 repo secrets 里确认已经有：
   - `MINER_U`
   - `DEEPSEEK_API_KEY`
2. 日常自动流程从 Dropbox `/zip_backup/<日期>/` 读取 PDF；临时手动处理 repo 内 PDF 时参考 `docs/pdf-to-xhs-workflow.md`。
3. 打开 **Actions**，按需要运行对应 workflow。
4. 生成结果默认写到 `xhs_notes/dropbox/`、`publish_ready_zips/`、`bilingual_podcast_videos/` 或 GitHub Pages。Market Views 只在 Actions 临时工作区生成，最终 PDF 仅存入私有 Cloudflare R2。

## 输出内容

每个 PDF 默认会生成：

- `note.md`：小红书笔记。
- `wechat_article.md`：微信公众号文章 Markdown，严肃克制、无 emoji、无中间 CTA，只保留 编辑评论和统一结尾。
- `assets/cover.png`：小红书封面。
- `assets/mineru_image_*.png`：MinerU 抽取图片，统一垫到深蓝色 1080×1440 小红书卡片画布。
- `assets/mineru_original_*`：原始抽取图片备份。

## 主要文件

- `.github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml`：每日 Dropbox PDF → 小红书/微信/知乎/闲鱼内容主流程。
- `.github/workflows/daily-bilingual-podcast-videos.yml`：每日生成 5 条双语 podcast 讲解视频。
- `.github/workflows/portal-suite-pages.yml`：生成 Portal Suite 搜索页，并把 PDF 镜像到私有 Cloudflare R2。
- `.github/workflows/reportify-grab.yml`：按需抓取单篇 reportify.cn 报告 PDF 并上传到 R2（Portal Suite「其他报告 · Reportify」模块用）。
- `scripts/pdf_to_xhs_batch.py`：批处理脚本。
- `scripts/portal_suite_catalog.py`：Portal Suite catalog 和 R2 同步脚本。
- `prompts/xhs_report_note_prompt.md`：小红书文案 prompt。
- `prompts/wechat_report_article_prompt.md`：微信公众号文章 prompt。
- `docs/pipeline-overview-v2.md`：当前项目工作流总览。
- `docs/report-to-wechat-architecture.md`：报告到微信公众号的 runner 边界、幂等、重试、标题审核和恢复手册。
- `docs/pdf-to-xhs-workflow.md`：旧版 repo 内 PDF 流程说明。

当前工作流只使用 DeepSeek：`DEEPSEEK_API_KEY`，不会读取 `OPENAI_API_KEY` 或 `OPENAI_SB_API_KEY`。

## 公开源码与部署配置

仓库中的站点名称、域名、账号、外部仓库和存储标识均为公开别名。生产映射、验证文件和品牌资产只保存在 GitHub 加密 Secret 或加密资产包中，并由 Runner 在临时工作区物化；不得写回 Git、日志或 artifact。

自动化默认由 `PORTAL_AUTOMATION_ENABLED=false` 冻结。重新启用前必须先配置私密部署 profile 与资产密钥，并通过 workflow 内的占位符检查。生成的发布包、草稿、视频和 Blog 缓存只进入私有存储或临时工作区，不再提交到公开仓库。
