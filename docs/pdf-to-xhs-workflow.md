# PDF 批量生成小红书笔记与微信公众号文章工作流

这个 repo 已经添加了一个可以在 GitHub Actions 里直接运行的工作流：`PDF to Xiaohongshu notes`。

## 你需要准备什么

### 1. Repo Secrets

需要这两个 secrets：

- `MINER_U`：MinerU API Key。
- `DEEPSEEK_API_KEY`：DeepSeek API Key。

当前工作流不会读取 `OPENAI_API_KEY` 或 `OPENAI_SB_API_KEY`。

### 2. PDF 文件夹

在 repo 里的 `pdfs/` 文件夹上传 PDF：

```text
pdfs/
  report-a.pdf
  report-b.pdf
```

工作流会递归扫描这个文件夹下面所有 `.pdf` 文件。

## 怎么运行

1. 打开 GitHub repo。
2. 点击 **Actions**。
3. 选择 **PDF to Xiaohongshu notes**。
4. 点击 **Run workflow**。
5. 参数可以先用默认值：

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `input_dir` | `pdfs` | PDF 所在文件夹 |
| `output_dir` | `xhs_notes` | 输出文件夹 |
| `model` | `deepseek-v4-flash` | DeepSeek 文案生成模型 |
| `deepseek_base_url` | `https://api.deepseek.com` | DeepSeek API 地址 |
| `mineru_model` | `vlm` | MinerU 模型版本 |
| `language` | `en` | PDF 语言。英文研报用 `en`，中文用 `ch` |
| `ocr` | `true` | 扫描件/图片 PDF 建议开启 |
| `wechat_length` | `1200` | 微信公众号文章目标字数 |
| `community_cta` | `更新信息参见portal.example.invalid` | 兼容参数；正文中间 CTA 会被清理，最终文字由微信渲染脚本统一追加 |
| `deepseek_max_attempts` | `4` | DeepSeek 连接重置、超时、`429` 和部分 `5xx` 的最大尝试次数 |
| `commit_results` | `true` | 是否把生成结果自动提交回 repo |

## 生成结果在哪里

默认输出到：

```text
xhs_notes/
  report-a/
    note.md
    wechat_article.md
    prompt_for_xhs.md
    prompt_for_wechat.md
    source_mineru.md
    status.json
    mineru_result.zip
    mineru_raw/
    assets/
      cover.png
      mineru_image_01.png
      mineru_image_02.png
      mineru_original_01.png
  summary.json
```

含义：

- `note.md`：可直接复制/微调的小红书笔记。
- `wechat_article.md`：微信公众号文章 Markdown，风格更严肃克制，无 emoji，并保留社群阅读钩子。
- `prompt_for_xhs.md`：真正发送给 DeepSeek 的小红书 prompt。
- `prompt_for_wechat.md`：真正发送给 DeepSeek 的微信公众号 prompt。
- `source_mineru.md`：MinerU 从 PDF 里解析出来的 Markdown。
- `assets/cover.png`：自动生成的小红书封面。
- `assets/mineru_image_*.png`：MinerU 从 PDF 中抽取出来的图片/图表，会统一垫到深蓝色 1080×1440 小红书卡片画布上。
- `assets/mineru_original_*`：原始抽取图片备份。
- `summary.json`：本次批处理汇总。

## 文案结构在哪里改

小红书 Prompt 文件在：

```text
prompts/xhs_report_note_prompt.md
```

微信公众号 Prompt 文件在：

```text
prompts/wechat_report_article_prompt.md
```

小红书 prompt 已经按“分段结构”做了：

- 爆款标题
- 封面短标题
- 封面副标题
- 一句话结论
- 3 个关键逻辑
- 我最想提醒的一点
- 评论区提问
- 配图建议

微信公众号 prompt 是更严肃的公众号文章风格：

- 无 emoji
- 不讲完整报告所有细节
- 埋下关键伏笔和后续阅读钩子
- 不生成中间 CTA，只保留 编辑评论；最终统一文字由微信渲染脚本追加

## 本地运行

也可以在本地跑：

```bash
pip install -r requirements.txt
export MINER_U="你的 MinerU token"
export DEEPSEEK_API_KEY="你的 DeepSeek key"
export DEEPSEEK_BASE_URL="https://api.deepseek.com"

python scripts/pdf_to_xhs_batch.py \
  --input-dir pdfs \
  --output-dir xhs_notes \
  --model deepseek-v4-flash \
  --language en \
  --ocr true \
  --wechat-length 1200 \
  --community-cta "更新信息参见portal.example.invalid"
```

完整的运行边界、标题审核、失败语义和恢复方式见
[`docs/report-to-wechat-architecture.md`](report-to-wechat-architecture.md)。
