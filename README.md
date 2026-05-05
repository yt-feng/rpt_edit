# rpt_edit

把 repo 里的 PDF 批量转成小红书笔记。

## 快速开始

1. 在 repo secrets 里确认已经有：
   - `MINER_U`
   - `DEEPSEEK_API_KEY`
2. 上传 PDF 到 `pdfs/` 文件夹。
3. 打开 **Actions** → **PDF to Xiaohongshu notes** → **Run workflow**。
4. 生成结果默认写到 `xhs_notes/`，并会作为 workflow artifact 上传。

## 主要文件

- `.github/workflows/pdf-to-xhs.yml`：GitHub Action 入口。
- `scripts/pdf_to_xhs_batch.py`：批处理脚本。
- `prompts/xhs_report_note_prompt.md`：小红书文案 prompt。
- `docs/pdf-to-xhs-workflow.md`：详细使用说明。

当前工作流只使用 DeepSeek：`DEEPSEEK_API_KEY`，不会读取 `OPENAI_API_KEY` 或 `OPENAI_SB_API_KEY`。
