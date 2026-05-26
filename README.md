# rpt_edit

把 Dropbox 或 repo 里的 PDF 批量转成小红书笔记、统一视觉风格配图、微信公众号文章草稿、市场观点 PDF、双语讲解视频，并维护一个脱敏 PDF 搜索页。

## 快速开始

1. 在 repo secrets 里确认已经有：
   - `MINER_U`
   - `DEEPSEEK_API_KEY`
2. 日常自动流程从 Dropbox `/zip_backup/<日期>/` 读取 PDF；临时手动处理 repo 内 PDF 时参考 `docs/pdf-to-xhs-workflow.md`。
3. 打开 **Actions**，按需要运行对应 workflow。
4. 生成结果默认写到 `xhs_notes/dropbox/`、`publish_ready_zips/`、`market_view_summaries/`、`bilingual_podcast_videos/` 或 GitHub Pages。

## 输出内容

每个 PDF 默认会生成：

- `note.md`：小红书笔记。
- `wechat_article.md`：微信公众号文章 Markdown，严肃克制、无 emoji、保留社群阅读钩子。
- `assets/cover.png`：小红书封面。
- `assets/mineru_image_*.png`：MinerU 抽取图片，统一垫到深蓝色 1080×1440 小红书卡片画布。
- `assets/mineru_original_*`：原始抽取图片备份。

## 主要文件

- `.github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml`：每日 Dropbox PDF → 小红书/微信/知乎/闲鱼内容主流程。
- `.github/workflows/daily-bilingual-podcast-videos.yml`：每日生成 5 条双语 podcast 讲解视频。
- `.github/workflows/kc-desk-notes-pages.yml`：生成 KC Desk Notes 搜索页，并把 PDF 镜像到私有 Cloudflare R2。
- `scripts/pdf_to_xhs_batch.py`：批处理脚本。
- `scripts/kc_desk_notes_catalog.py`：KC Desk Notes catalog 和 R2 同步脚本。
- `prompts/xhs_report_note_prompt.md`：小红书文案 prompt。
- `prompts/wechat_report_article_prompt.md`：微信公众号文章 prompt。
- `docs/pipeline-overview.md`：当前项目架构 master doc。
- `docs/pdf-to-xhs-workflow.md`：旧版 repo 内 PDF 流程说明。

当前工作流只使用 DeepSeek：`DEEPSEEK_API_KEY`，不会读取 `OPENAI_API_KEY` 或 `OPENAI_SB_API_KEY`。
