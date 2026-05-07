# rpt_edit

把 repo 里的 PDF 批量转成小红书笔记、统一视觉风格配图，以及微信公众号文章草稿。

## 快速开始

1. 在 repo secrets 里确认已经有：
   - `MINER_U`
   - `DEEPSEEK_API_KEY`
2. 上传 PDF 到 `pdfs/` 文件夹。
3. 打开 **Actions** → **PDF to Xiaohongshu notes** → **Run workflow**。
4. 生成结果默认写到 `xhs_notes/`，并会作为 workflow artifact 上传。

## 输出内容

每个 PDF 默认会生成：

- `note.md`：小红书笔记。
- `wechat_article.md`：微信公众号文章 Markdown，严肃克制、无 emoji、保留社群阅读钩子。
- `assets/cover.png`：小红书封面。
- `assets/mineru_image_*.png`：MinerU 抽取图片，统一垫到深蓝色 1080×1440 小红书卡片画布。
- `assets/mineru_original_*`：原始抽取图片备份。

## 主要文件

- `.github/workflows/pdf-to-xhs.yml`：GitHub Action 入口。
- `scripts/pdf_to_xhs_batch.py`：批处理脚本。
- `prompts/xhs_report_note_prompt.md`：小红书文案 prompt。
- `prompts/wechat_report_article_prompt.md`：微信公众号文章 prompt。
- `docs/pdf-to-xhs-workflow.md`：详细使用说明。

当前工作流只使用 DeepSeek：`DEEPSEEK_API_KEY`，不会读取 `OPENAI_API_KEY` 或 `OPENAI_SB_API_KEY`。
