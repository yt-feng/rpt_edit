# rpt_edit 工作流总览

本文档用于记录当前 repo 内已经整理好的 GitHub Actions、脚本、prompt、输出目录和日常使用方式。后续如果流程继续迭代，优先同步更新本文件。

## 1. 总体目标

`rpt_edit` 的核心目标是把每日 PDF 研报自动加工成多平台可发布内容：

1. 从 repo 的 `pdfs/` 或 Dropbox `/zip_backup/<日期>/` 获取 PDF。
2. 使用 MinerU 解析 PDF 文本和图表。
3. 使用 DeepSeek 生成小红书、微信、知乎、闲鱼等文案。
4. 对所有公开文案做投行名称脱敏、敏感词检测和合规改写。
5. 输出小红书卡片图、微信/知乎/闲鱼文案、市场观点 PDF、待发布 ZIP 包。
6. 需要视频测试时，生成中文双男声 podcast 和竖屏讲解视频。

当前默认只使用 DeepSeek：`DEEPSEEK_API_KEY`。不使用 `OPENAI_API_KEY` 或 `OPENAI_SB_API_KEY`。

## 2. 必要 Secrets

| Secret | 用途 |
| --- | --- |
| `DEEPSEEK_API_KEY` | 所有文案生成、改写、宏观报告筛选、CTA 重写、敏感词命中后的改写 |
| `MINER_U` | MinerU PDF 解析和抽图 |
| `DROPBOX_APP_KEY` | Dropbox API |
| `DROPBOX_APP_SECRET` | Dropbox API |
| `DROPBOX_REFRESH_TOKEN` | Dropbox refresh token，用于读取 `/zip_backup` |

可选环境变量：

| 变量 | 默认值 | 用途 |
| --- | --- | --- |
| `DEEPSEEK_BASE_URL` | `https://api.deepseek.com` | DeepSeek API base URL |
| `DEEPSEEK_MODEL` | `deepseek-chat` | DeepSeek 模型名 |
| `SENSITIVE_API_URL` | `https://v.api.aa1.cn/api/api-mgc/index.php` | free-api 敏感词检测接口 |

## 3. 主要 GitHub Actions

### 3.1 Final PDF to XHS notes

文件：`.github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml`

用途：每日主流程。会从 Dropbox 最新日期文件夹中取 PDF，筛选宏观/趋势类报告，分 shard 跑内容生成，最后打待发布 ZIP。

触发方式：

- 手动运行：Actions → **Final PDF to XHS notes** → Run workflow
- 定时运行：北京时间 05:00，cron 为 `0 21 * * *`

主要步骤：

1. `resolve-inputs`：解析 workflow 参数。
2. `select-macro-reports`：下载 Dropbox 最新日期 PDF，并用 DeepSeek 判断个股 / 宏观趋势，只保留宏观趋势相关报告。
3. `process-shard`：最多 40 个 shard 并行，每个 shard 默认处理 5 篇报告。
4. `Finalize shard outputs`：生成闲鱼、知乎补充文案，并执行敏感词检测和脱敏。
5. `package-publish-ready`：把待发布内容打成分卷 ZIP，排除 raw、prompt、log、json、status 等调试文件。

主输出目录：

```text
xhs_notes/dropbox/<日期>/shard_<编号>/<报告文件夹>/
```

待发布 ZIP 目录：

```text
publish_ready_zips/<日期>/publish_ready_<日期>_part001.zip
publish_ready_zips/<日期>/publish_ready_<日期>_part002.zip
publish_ready_zips/<日期>/publish_ready_<日期>_summary.json
```

说明：

- ZIP 默认按 90MB 分卷，避免 GitHub 单文件 100MB 限制。
- ZIP 内所有 `.md` 会改成 `.txt`，方便手机打开。
- ZIP 只保留待发布内容和图片。

### 3.2 Debug package publish-ready ZIP

文件：`.github/workflows/debug-package-publish-ready.yml`

用途：只重新打包已经生成好的内容，不重跑 MinerU / DeepSeek / 小红书生成。

适用场景：

- Final 主流程内容已经生成，但 ZIP 打包或 push 出错。
- 想对某个日期重新生成 publish-ready ZIP。

推荐参数：

```text
date_folder: latest 或具体日期，例如 260515
max_zip_mb: 90
commit_results: true
```

输出同样在：

```text
publish_ready_zips/<日期>/
```

### 3.3 Market views daily PDF

文件：`.github/workflows/market-views-latex-pdf.yml`

用途：基于每日已经生成的宏观报告内容，整理一份市场观点汇总 PDF。

触发方式：

- 手动运行：Actions → **Market views daily PDF**
- 定时运行：北京时间 08:00，cron 为 `0 0 * * *`

输入来源：

```text
xhs_notes/dropbox/<最新日期>/
```

输出目录：

```text
market_view_summaries/<日期>/market_views_<日期>.pdf
market_view_summaries/<日期>/market_views_<日期>.tex
market_view_summaries/<日期>/market_views_structured.json
market_view_summaries/<日期>/figures/
```

说明：

- 默认用 ReportLab 快速渲染 PDF，不依赖完整 LaTeX 安装。
- 可选 `compile_latex=true` 时才尝试安装 XeLaTeX 并编译 `.tex`。
- 图表会优先选择带 Exhibit / Figure / 图表编号的候选。
- 已对邮箱、电话、HTML、表格残片等异常 caption 做过滤。

### 3.4 Test Chinese podcast video

文件：`.github/workflows/test-zh-podcast-video.yml`

用途：测试中文 podcast + 竖屏讲解视频链路。不会影响每日主流程。

流程：

1. 从 Dropbox 最新日期文件夹里选择一份至少 5 页的 PDF。
2. 用 MinerU 解析文本和图表。
3. 生成中文双男声对话脚本。
4. 使用本地 Piper TTS 生成中文 wav。
5. 用 Pillow + ffmpeg 生成 Remotion-like 竖屏讲解视频。
6. 视频底部水印为 `KC桌面`。

输出目录：

```text
podcast_video_tests/<run_id>/<报告文件夹>/
  podcast_zh_script.txt
  podcast_zh.wav
  podcast_zh_timeline.json
  podcast_zh_explainer.mp4
```

说明：

- 当前为测试流程，只生成中文。
- 两个角色都是男声：`ZH_A` 主持人，`ZH_B` 研究员。
- 用同一个 Piper 中文模型，通过音频后处理做两种男声音色区分。

### 3.5 PDF to Xiaohongshu notes

文件：`.github/workflows/pdf-to-xhs.yml`

用途：手动处理 repo 内 `pdfs/` 文件夹里的 PDF。适合临时丢 PDF 进去跑一批。

输入目录：

```text
pdfs/
```

输出目录：

```text
xhs_notes/<报告文件夹>/
```

## 4. 主要脚本

| 脚本 | 用途 |
| --- | --- |
| `scripts/download_dropbox_latest_pdfs.py` | 读取 Dropbox `/zip_backup` 最新日期文件夹，并下载 PDF |
| `scripts/select_macro_trend_pdfs.py` | 使用 DeepSeek 判断报告是否为宏观/趋势类，过滤个股报告 |
| `scripts/run_pdf_to_xhs_in_batches.py` | 分批、分 shard 调用 PDF 生成链路 |
| `scripts/pdf_to_xhs_batch.py` | 核心 PDF → MinerU → 小红书/微信/图表卡片生成脚本 |
| `scripts/finalize_outputs.py` | 生成闲鱼、知乎文案，统一结尾，脱敏，敏感词 guard |
| `scripts/sensitive_content_guard.py` | 文案敏感词检测、本地替换、DeepSeek 改写 |
| `scripts/package_publish_ready_outputs.py` | 打待发布 ZIP，过滤 raw/prompt/log/json/status，md 改 txt，分卷压缩 |
| `scripts/build_market_views_pdf.py` | 生成市场观点汇总结构化 JSON 和 LaTeX 源文件 |
| `scripts/render_market_views_reportlab_pdf.py` | 用 ReportLab 快速渲染市场观点 PDF |
| `scripts/select_test_pdf.py` | 测试 podcast/video 时选择 5 页以上 PDF |
| `scripts/generate_test_podcast_video.py` | 生成中文双男声 podcast 和讲解视频 |
| `scripts/commit_output_dir.sh` | GitHub Action 里提交输出目录，带重试和强制 add PDF |

## 5. Prompt 文件

| Prompt | 用途 |
| --- | --- |
| `prompts/xhs_report_note_prompt.md` | 小红书笔记 |
| `prompts/wechat_report_article_prompt.md` | 微信中文文章 |
| `prompts/wechat_report_article_en_prompt.md` | 微信英文文章 |
| `prompts/xianyu_report_listing_prompt.md` | 闲鱼商品说明 |
| `prompts/zhihu_report_article_prompt.md` | 知乎长文 |
| `prompts/podcast_zh_only_prompt.md` | 中文双男声 podcast 脚本 |
| `prompts/podcast_zh_en_prompt.md` | 中英文 podcast 旧版/备用 prompt |
| `prompts/zsxq_img.jpg` | 微信中文文章末尾插入的社群图 |

## 6. 每篇报告的常见输出

生成完成后，每篇报告文件夹通常包含：

```text
note.md                         # 小红书笔记
wechat_article.md               # 微信中文文章
wechat_article_en.md            # 微信英文文章
zhihu_article.md                # 知乎文章
xianyu_note.md                  # 闲鱼文案
assets/                         # 小红书卡片、封面、原图等
mineru_raw/                     # MinerU 原始解析结果，不进入 publish_ready ZIP
source_mineru.md                # MinerU 文本源，不进入 publish_ready ZIP
status.json                     # 调试元数据，不进入 publish_ready ZIP
prompt_for_*.md                 # 调试 prompt，不进入 publish_ready ZIP
```

## 7. publish_ready_zips 的保留与排除规则

最终 ZIP 只保留待发布内容。

会保留：

```text
note.txt
wechat_article.txt
wechat_article_en.txt
zhihu_article.txt
xianyu_note.txt
*.png / *.jpg / *.jpeg / *.webp
```

会排除：

```text
mineru_raw/
source_mineru.md
shard_run_summary.md
*.json
*.log
status.json
prompt_for_xhs.md
prompt_for_wechat.md
prompt_for_wechat_en.md
prompt_for_xianyu.md
prompt_for_zhihu.md
prompt_for_podcast.md
podcast_script_zh.md
podcast_script_en.md
podcast_zh.md
podcast_en.md
podcast_zh_script.txt
podcast_en_script.txt
```

说明：

- ZIP 内 `.md` 自动改成 `.txt`，不改变 repo 原文件名。
- ZIP 分卷默认 90MB，避免 GitHub 100MB 单文件限制。

## 8. 小红书内容规则

`note.md` 当前规则：

- 不展示写作框架词，比如 `一句话结论`、`我最想提醒的一点`、`配图建议`。
- 不输出包含 `投资` 的免责声明，例如 `非投资建议`。
- 不输出 `#财经`、`#金融`、`#股票`、`#基金`、`#理财`、`#投资学习`。
- 允许标签：

```text
#学习笔记 #研究笔记 #学习研究 #研报解读
```

## 9. 闲鱼内容规则

`xianyu_note.md` 当前规则：

- 不输出 `建议价格`。
- 不输出 `搜索关键词`。
- 如有关键词，统一改为 `Hashtag`。
- 避免敏感标签，如 `#财经`、`#投资`、`#股票`、`#基金`、`#理财`。

常用安全标签：

```text
#学习资料 #研究笔记 #学习笔记 #行业研究 #研报资料 #资料整理 #报告学习 #案例研究
```

## 10. 微信与知乎内容规则

微信：

- 中文文章结构偏严肃，使用金字塔原则。
- 结尾在英文灰色免责声明前插入 `prompts/zsxq_img.jpg`。
- 英文免责声明为：

```html
<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>
```

知乎：

- 类似微信风格，但更偏问题驱动和长文论证。
- 不输出硬性的关注点赞 CTA。
- 避免财经操作建议和极限词。

## 11. 敏感词和脱敏规则

所有公开物料会经过：

1. 投行品牌替换：如高盛 → GS，摩根大通 → JPM，摩根士丹利 → MS 等。
2. 本地高风险词替换：如买入、卖出、稳赚、保本、抄底、上车等。
3. free-api 敏感词检测。
4. 命中后调用 DeepSeek 改写。

敏感词处理脚本：

```text
scripts/sensitive_content_guard.py
```

检测结果保存为：

```text
sensitive_content_guard_summary.json
```

但该 JSON 不进入 publish-ready ZIP。

## 12. 日常运行建议

最常用：

1. 每天自动跑：**Final PDF to XHS notes**。
2. 如果最终 ZIP 出问题，只跑：**Debug package publish-ready ZIP**。
3. 如果要看市场观点总览，跑：**Market views daily PDF**。
4. 如果要测试音频/视频，跑：**Test Chinese podcast video**。
5. 如果只是手动上传 repo 内 PDF，跑：**PDF to Xiaohongshu notes**。

## 13. 常见问题

### ZIP push 失败，提示超过 100MB

使用 **Debug package publish-ready ZIP** 重新打包。脚本会按 90MB 分卷。

### 某个 shard 没有产出

最终 ZIP 会自动跳过没有生成报告文件夹的 shard。

### Market views 没看到 PDF

检查 `market_view_summaries/<日期>/market_views_pdf_render_progress.log` 或 workflow artifact。现在 workflow 有 PDF 存在校验，找不到会直接失败。

### 小红书 note 里仍有不想要的词

优先修改：

```text
prompts/xhs_report_note_prompt.md
scripts/sensitive_content_guard.py
```

### 闲鱼文案出现价格或搜索关键词

优先修改：

```text
prompts/xianyu_report_listing_prompt.md
scripts/sensitive_content_guard.py
```

## 14. 当前文档维护约定

- 高层总览：`docs/pipeline-overview.md`
- 旧版 repo 内 PDF 流程：`docs/pdf-to-xhs-workflow.md`
- 如果修改 workflow、输出目录、ZIP 规则、prompt 规则，记得同步更新本文档。
