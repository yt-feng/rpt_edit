# rpt_edit 工作流总览

本文档用于记录当前 repo 内已经整理好的 GitHub Actions、脚本、prompt、输出目录和日常使用方式。后续如果流程继续迭代，优先同步更新本文件。

## 1. 总体目标

`rpt_edit` 的核心目标是把每日 PDF 研报自动加工成多平台可发布内容：

1. 从 repo 的 `pdfs/` 或 Dropbox `/zip_backup/<日期>/` 获取 PDF。
2. 使用 MinerU 解析 PDF 文本和图表。
3. 使用 DeepSeek 生成小红书、微信、知乎、闲鱼等文案。
4. 对所有公开文案做投行名称脱敏、敏感词检测和合规改写。
5. 输出小红书卡片图、微信/知乎/闲鱼文案、市场观点 PDF、KC 中文精译 PDF、待发布 ZIP 包。
6. 默认把当天所有成功完成 MinerU 解析的 KC 中文精译稿转成微信公众号草稿箱图文，一组草稿默认 9 篇文章；发布接口权限开通后可打开自动提交发布。
7. 需要视频测试时，生成中文双男声 podcast 和竖屏讲解视频。

当前默认只使用 DeepSeek：`DEEPSEEK_API_KEY`。不使用 `OPENAI_API_KEY` 或 `OPENAI_SB_API_KEY`。

## 2. 必要 Secrets

| Secret | 用途 |
| --- | --- |
| `DEEPSEEK_API_KEY` | 所有文案生成、改写、宏观报告筛选、CTA 重写、敏感词命中后的改写 |
| `MINER_U` | MinerU PDF 解析和抽图 |
| `DROPBOX_APP_KEY` | Dropbox API |
| `DROPBOX_APP_SECRET` | Dropbox API |
| `DROPBOX_REFRESH_TOKEN` | Dropbox refresh token，用于读取 `/zip_backup` |
| `WECHAT_MP_APPID` | 可选，微信公众号草稿上传和发布用 AppID |
| `WECHAT_MP_APPSECRET` | 可选，微信公众号草稿上传和发布用 AppSecret |

微信公众号草稿上传和发布还依赖公众号后台 IP 白名单。正式上传走带 `wechat-draft` label 的 self-hosted fixed-IP runner；如果上传失败，优先检查 runner 是否在线、公众号白名单是否包含该固定 IP，以及微信返回的 `40164 invalid ip not in whitelist`。`dry_run` 模式不需要这两个 secret，也不会调用微信接口。

KC Desk Notes / Cloudflare R2 额外需要：

| Secret / Variable | 用途 |
| --- | --- |
| `R2_ACCOUNT_ID` | R2 S3 API account id，KC Desk Notes workflow 已默认使用 `8182ec40eab8c484e11ebf5d6a516fbd` |
| `R2_ACCESS_KEY_ID` | R2 S3 API access key |
| `R2_SECRET_ACCESS_KEY` | R2 S3 API secret key |
| `R2_BUCKET` | R2 bucket 名，KC Desk Notes workflow 已默认使用 `kc-desk-notes-pdfs` |
| `PASSWORD_SECRET` | Worker 端密码 hash pepper |
| `CALC_KEY` | Worker 隐藏计算器 key，用于计算每篇报告的伪密码 |
| `KC_DESK_DOWNLOAD_PASSWORD` | PDF 下载密码，Action 会用它和 `PASSWORD_SECRET` 生成公开 hash |
| `CLOUDFLARE_API_TOKEN` | 可选，用于 Action 自动部署 Worker |
| `CLOUDFLARE_ACCOUNT_ID` | 可选，用于 Action 自动部署 Worker |
| `KC_DESK_WORKER_URL` | Pages 前端调用的 Worker URL |
| `KC_DESK_PAGES_URL` | 可选，Worker 读取 catalog/password rules 的 Pages URL |
| `R2_OBJECT_PREFIX` | 可选，R2 内 PDF 前缀，默认 `reports` |

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
2. `select-macro-reports`：下载 Dropbox 最新日期 PDF，并用 DeepSeek 判断个股 / 宏观趋势；本地规则会额外排除股票代码、评级、目标价、业绩点评等个股信号，只保留宏观趋势相关报告。
3. `process-shard`：最多 40 个 shard 并行，每个 shard 默认处理 5 篇报告；每个 shard 内再按 batch 调 MinerU 和 DeepSeek。
4. `Finalize shard outputs`：生成闲鱼、知乎补充文案，并执行敏感词检测和脱敏。
5. `package-publish-ready`：把待发布内容打成分卷 ZIP，排除 raw、prompt、log、json、status 等调试文件。

数据边界：

```text
Dropbox /zip_backup/<日期>/
  -> _dropbox_latest_pdfs
  -> _selected_macro_pdfs
  -> xhs_notes/dropbox/<日期>/shard_<编号>/<报告文件夹>/
  -> publish_ready_zips/<日期>/
```

容错规则：

- `select-macro-reports` 只负责选 PDF，不生成发布内容。
- `process-shard` 使用 `scripts/run_pdf_to_xhs_in_batches.py` 做分片和分批。
- MinerU 单 batch 默认最多 5 个 PDF，poll timeout 为 3600 秒。
- 如果 MinerU batch 超时，但已有部分 PDF 返回 `done + full_zip_url`，`scripts/pdf_to_xhs_batch.py` 会继续处理这些已完成 PDF，并跳过仍在 `running/pending` 的 PDF。
- 如果某个本应处理 PDF 的 shard 最终没有生成任何包含 `note.md` 和 `wechat_article.md` 的报告文件夹，该 shard 会失败，避免“绿色成功但没有 publish-ready 内容”。
- `package-publish-ready` 使用 `set -o pipefail`，打包脚本报错时 workflow 会失败，不再上传只有日志的空 artifact。

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
- 没有报告文件夹的空 shard 会被打包脚本跳过；如果所有 shard 都没有 publish-ready 文件，打包会失败。

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

用途：基于每日已经生成的宏观报告内容，整理一份市场观点汇总 PDF。它覆盖的是 `xhs_notes/dropbox/<日期>` 下已经成功产出 `source_mineru.md` 的报告文件夹；如果当天主流程只有部分 shard 成功产出报告文件夹，本 PDF 也只会覆盖这些已完成报告。

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
- PDF 开头包含带页码目录，正文先按主题分门别类综合观点，再附“报告覆盖清单”和“逐篇报告摘录”，用于确认当天哪些报告被纳入。
- 结尾使用灰色小字号长版 Disclaimer。

### 3.4 Daily bilingual podcast videos

文件：`.github/workflows/daily-bilingual-podcast-videos.yml`

用途：每天从 Dropbox 最新日期文件夹中默认挑选 3 篇偏宏观 / 策略 / 行业趋势的报告，生成 mixed bilingual podcast 讲解视频。当前默认模式只产出 mixed bilingual 版本，避免同时生成中文、英文 standalone 视频造成 ElevenLabs 额度浪费；手动运行时可以把 `output_mode` 切到 `all` 恢复三版输出。

触发方式：

- 手动运行：Actions → **Daily bilingual podcast videos**
- 定时运行：北京时间 07:00，cron 为 `0 23 * * *`

主要参数：

- `video_count`：默认 `3`。
- `output_mode`：默认 `bilingual_only`，只生成 mixed bilingual 视频和从最终视频抽出的音频；可选 `all`，生成中文、英文、mixed 三版。
- `podcast_minutes`：控制生成脚本和 TTS 的目标时长。

流程：

1. 从 Dropbox 最新日期文件夹下载 PDF。
2. 先用 `scripts/select_macro_trend_pdfs.py` 做宏观优先筛选，尽量排除个股、评级、目标价、财报点评类报告。
3. 再从宏观候选中选择默认 3 份至少 5 页的报告。
4. 用 MinerU 解析文本和图表。
5. 用 DeepSeek 生成 podcast 脚本。
6. `bilingual_only` 模式只跑一次 ElevenLabs TTS，生成英文音频/timeline。
7. 用这一次音频渲染 mixed bilingual 视频，并从最终 mp4 抽出音频文件。
8. `all` 模式保留旧逻辑：生成中文、英文、mixed 三版讲解视频。

默认输出目录：

```text
bilingual_podcast_videos/<日期>/<run_id>/<报告文件夹>/
  podcast_mixed_bilingual_explainer.mp4
  podcast_mixed_bilingual_audio.m4a
```

`output_mode=all` 时额外输出：

```text
  podcast_zh_explainer.mp4
  podcast_en_explainer.mp4
```

说明：

- 视频脚本和标题会复用 `finalize_outputs.py` 的脱敏规则。
- mixed bilingual 版本有安全区、中文字体和英文单词高亮断行修复。
- 默认模式会删除中间的 `podcast_en.wav`，最终音频以 `podcast_mixed_bilingual_audio.m4a` 为准。

### 3.5 KC Desk Notes Pages

文件：`.github/workflows/kc-desk-notes-pages.yml`

用途：生成 GitHub Pages 搜索站点 **KC Desk Notes**。站点展示脱敏后的 Dropbox PDF 标题，并提供标题、投行目录 txt、已存在 MinerU 正文的全文搜索；PDF 不进入 repo，也不在前端暴露 Dropbox token 或 R2 key。点击报告进入详情页后，必须输入密码，由 Cloudflare Worker 校验后从私有 R2 以 attachment 方式返回 PDF。

触发方式：

- 手动运行：Actions → **KC Desk Notes Pages**
- 定时运行：北京时间 09:30，cron 为 `30 1 * * *`

核心数据：

```text
kc_desk_notes/data/catalog.json      # 长期保留历史文件名和 report id，不随 Dropbox 清理删除
kc_desk_notes/password_rules.json    # 全局密码组 hash 对照表和分配规则，作为备用
kc_desk_notes/site_src/              # GitHub Pages 静态站点源码
workers/kc-desk-notes-worker/        # Cloudflare Worker 代码
```

Pages artifact 会额外生成但不提交到 repo：

```text
_kc_desk_notes_pages/data/search_index.json
```

这个索引按 `report_id` 绑定搜索文本，来源包括 `bank_report_catalogs/<日期>/<投行>.txt` 里的报告条目，以及仓库中能按标题匹配到 catalog 的 `xhs_notes/dropbox/<日期>/shard_*/<报告>/source_mineru.md`。前端只用它过滤搜索结果，不在列表页展示正文片段；由于 GitHub Pages 是公开站点，进入索引的文本本身也会成为公开可下载数据。

流程：

1. 扫描 Dropbox `/zip_backup/<日期>/` 下当前仍存在的 PDF。
2. 用既有投行脱敏规则生成页面标题。
3. 合并到长期 `catalog.json`，历史条目保留。
4. 将当前扫描到的 PDF 上传到私有 R2，object key 为 `reports/<report_id>.pdf`。
5. 生成 Pages artifact，其中 `catalog.json` 供列表和详情页使用，`search_index.json` 供全文搜索使用。
6. 部署 GitHub Pages。
7. Cloudflare 配置齐全时，自动部署 Worker。

下载密码优先使用按 report id 推导出的 HMAC 伪密码：

```text
KC-<base32(hmac_sha256(PASSWORD_SECRET, "kc-desk-notes:" + report_id)) 前 12 位，按 4-4-4 分组>
```

不要把 `PASSWORD_SECRET` 放前端。需要计算时访问隐藏 Worker 计算器：

```text
https://<worker>/calc?id=<report_id>&key=<CALC_KEY>
```

如果需要，也可以继续使用 `KC_DESK_DOWNLOAD_PASSWORD` 作为全局备用密码。

### 3.6 KC translated reports and WeChat publishing

相关文件：

```text
.github/workflows/kc-translated-reports-test.yml
.github/workflows/kc-translated-wechat-draft-test.yml
scripts/build_kc_translated_reports.py
scripts/push_kc_translated_to_wechat_drafts.py
```

用途：

- 从 `xhs_notes/dropbox/<日期>/.../source_mineru.md` 选取报告，清理原报告 logo、作者、页脚免责声明和披露段落。
- 用 DeepSeek 翻译成中文正文，保留正文图表，渲染为带 **KC桌面——外资精译** 品牌的 PDF。
- 中文精译 PDF 每页带 45 度灰色底层水印 `公众号：KC桌面`，底部居中有蓝色公众号标识。
- 默认把 `kc_translated_reports/<日期>/<报告>/translated.md` 转成微信公众号短版图文 HTML，可见正文约 2000 字；正文图片先走微信 `uploadimg`，封面走永久图片素材，并调用 `draft/add` 创建草稿；当 `wechat_freepublish=true` 时再调用 `freepublish/submit` 提交发布。
- 微信短版正文图默认最多 3 张、至少 3 张。优先使用 MinerU 抽出的报告图表；如果报告图不足，会参考 `gen_rpt` 的方式用 Pollinations 生成主题相关 AI 配图，下载压缩后再上传微信。
- 每篇公众号草稿正文末尾固定追加 `prompts/zsxq_img.jpg`，上传时会先通过微信 `uploadimg` 转成公众号可用图片 URL。
- 每篇公众号草稿正文末尾、星球图之前固定加钩子：`更多完整报告和后续精译，扫文末图片进群交流。`
- 图文分组默认 `articles_per_draft=8`。如果微信 `draft/add` 返回 `45008 article size out of limit`，脚本会自动把该组拆小重试，优先保证草稿能保存成功；`wechat_freepublish=true` 时会按实际成功草稿组提交发布。

主流程入口：

- `.github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml` 的 `translated_report_count` 默认 `all`，表示当天所有成功完成 MinerU 解析并产出 `source_mineru.md` 的报告都会生成 KC 中文精译版。手动运行时设为正整数可限制数量，设为 `0` 可关闭翻译和草稿上传。
- `wechat_draft_upload` 默认 `true`，在翻译 PDF job 成功后上传公众号草稿；手动运行时可改成 `false` 只生成翻译 PDF。
- `wechat_freepublish` 默认 `false`，因为当前公众号测试 `freepublish/submit` 返回 `48001 api unauthorized`；等公众号后台开通发布接口权限后，手动运行时改成 `true` 或把 workflow 默认值改回 `true`。
- `wechat_draft_articles_per_draft` 默认 `8`。
- `wechat_draft_max_body_chars` 默认 `2000`。
- `wechat_draft_min_inline_images` 默认 `3`。
- `wechat_draft_max_inline_images` 默认 `3`。

测试方式：

- 只测翻译 PDF：Actions → **KC translated reports PDF test**。
- 只测公众号 payload：Actions → **KC translated WeChat draft test**，默认 `dry_run=true`，只生成 `wechat_drafts/<日期>/draft_payload_*.json` 和 summary，不调用微信 API。
- 确认 secret 和 IP 白名单可用后，把 `dry_run=false` 才会真正写入公众号草稿箱；同时把 `publish=true` 才会提交发布。

输出目录：

```text
kc_translated_reports/<日期>/<报告>/translated.md
kc_translated_reports/<日期>/<报告>/kc_translated_report_XX.pdf
wechat_drafts/<日期>/draft_payload_01.json
wechat_drafts/<日期>/wechat_draft_summary.json
```

### 3.7 Legacy repo-local PDF flow

说明文档：`docs/pdf-to-xhs-workflow.md`

用途：旧版手动处理 repo 内 `pdfs/` 文件夹里的 PDF。当前日常默认走 Dropbox 主流程；如果后续恢复 repo-local Action，优先同步更新这里。

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
| `scripts/prune_generated_date_dirs.py` | 清理重型生成目录，只保留最新日期文件夹 |
| `scripts/build_bank_report_catalog.py` | 生成 `bank_report_catalogs/<日期>/<投行>.txt`，每个投行目录开头会带单篇/周合集商品说明，并用实际投行显示名替换 |
| `scripts/build_kc_translated_reports.py` | 从 MinerU 结果生成 KC 中文精译 Markdown 和 PDF |
| `scripts/push_kc_translated_to_wechat_drafts.py` | 把 KC 中文精译 Markdown 转成 2000 字左右的公众号草稿图文，可选 Pollinations 补图和提交发布，支持 dry-run |
| `scripts/build_market_views_pdf.py` | 生成市场观点汇总结构化 JSON 和 LaTeX 源文件 |
| `scripts/render_market_views_reportlab_pdf.py` | 用 ReportLab 快速渲染市场观点 PDF |
| `scripts/select_test_pdf.py` | 测试 podcast/video 时选择 5 页以上 PDF |
| `scripts/generate_test_podcast_video_eleven_batch_v5.py` | 批量生成中英文和 mixed bilingual podcast 讲解视频 |
| `scripts/kc_desk_notes_catalog.py` | 扫描 Dropbox PDF、合并长期 catalog、同步当前 PDF 到 R2 |
| `scripts/build_kc_desk_notes_site.py` | 生成 KC Desk Notes GitHub Pages 静态站点 artifact，并把投行目录 txt 与可匹配的 MinerU 正文并入前端全文搜索索引 |
| `scripts/hash_kc_desk_notes_password.py` | 生成 `password_rules.json` 里的密码 hash |
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

### 7.1 生成产物保留与归属

重型生成目录由 GitHub Actions 写入 repo，远端 `main` 是这些目录的事实来源：

```text
xhs_notes/dropbox/
publish_ready_zips/
bank_report_catalogs/
market_view_summaries/
bilingual_podcast_videos/
kc_translated_reports/
wechat_drafts/
```

本地修代码时不要用旧的本地生成目录覆盖远端。合并或 rebase 时的默认策略：

- 代码、workflow、prompt、文档：以本地明确修改为准。
- 上面列出的日期型生成目录：以远端 Actions 产物为准。
- KC Desk Notes 的 `kc_desk_notes/data/catalog.json` 是长期 catalog，不按最近 3 天清理。

清理逻辑：

```text
.github/workflows/prune-generated-date-folders.yml
scripts/prune_generated_date_dirs.py --keep 3
```

默认每个重型输出 root 只保留最新 3 个日期文件夹。这样 repo 保持可 clone，历史发布包和中间产物应以 GitHub Actions artifact、Dropbox/R2 或本地备份为准，不依赖 repo 长期保存所有旧日期目录。

## 8. 小红书内容规则

`note.md` 当前规则：

- 正文最终限制为不超过 1000 个可见字符。
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
4. 如果要生成每日中英双语视频，跑：**Daily bilingual podcast videos**。
5. 如果要更新 PDF 搜索站点，跑：**KC Desk Notes Pages**。
6. 如果只是手动上传 repo 内 PDF，参考旧版 `docs/pdf-to-xhs-workflow.md`。

## 13. 常见问题

### ZIP push 失败，提示超过 100MB

使用 **Debug package publish-ready ZIP** 重新打包。脚本会按 90MB 分卷。

### 某个 shard 没有产出

如果 shard 的索引超过本次选出的 PDF 数量范围，`Shard <n>/40 has no PDFs` 是正常现象，最终 ZIP 会自动跳过。

如果 shard 明明分到了 PDF，但没有生成任何报告文件夹，通常是 MinerU 或 DeepSeek 阶段失败。当前流程会让该 shard 失败，并在 `batch_run_summary.json`、`generate_progress.log` 和 workflow log 中保留原因。

### publish-ready artifact 很小或为空

现在打包步骤已经启用 `pipefail`。如果没有任何 publish-ready 文件，`package-publish-ready` 会失败，不应再出现 workflow 绿色但 artifact 只有几百字节日志的情况。

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
