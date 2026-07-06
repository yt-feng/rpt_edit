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
| `GH_DISPATCH_TOKEN` | 可选（Reportify 模块），Worker 用来触发 reportify-grab 的 fine-grained PAT（Actions 读写） |
| `GH_REPO` | 可选（Reportify 模块），repository_dispatch 目标，如 `yt-feng/rpt_edit` |

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
xhs_notes/dropbox/<最新日期>/          # Dropbox 投行报告
xhs_notes/institutions/<最新日期>/     # IMF/BIS/世界银行/兰德/布鲁金斯（经 --extra-roots 合并）
```

通过 `--extra-roots "xhs_notes/institutions"` 把 §3.8 抓取的 5 家机构报告也并入市场观点 PDF。market views 不做敏感过滤，5 家全部纳入（含 RAND / Brookings）。

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
kc_desk_notes/data/catalog.json      # 长期 catalog，受 KC Desk Notes 8GiB PDF 总量上限约束
kc_desk_notes/data/search_index.json # 长期全文/标题检索索引，跟随 catalog 生成并提交
kc_desk_notes/data/archive_catalog.json # Dropbox PDF 已不在但仍保留标题/正文线索的文字归档条目
kc_desk_notes/password_rules.json    # 全局密码组 hash 对照表和分配规则，作为备用
kc_desk_notes/site_src/              # GitHub Pages 静态站点源码
workers/kc-desk-notes-worker/        # Cloudflare Worker 代码
```

Pages artifact 会从这些长期数据生成前端可访问文件：

```text
_kc_desk_notes_pages/data/catalog.json
_kc_desk_notes_pages/data/search_index.json
```

这个索引按 `report_id` 绑定搜索文本，来源包括 `bank_report_catalogs/<日期>/<投行>.txt` 里的报告条目，以及仓库中能按标题匹配到 catalog 的 `xhs_notes/dropbox/<日期>/shard_*/<报告>/source_mineru.md`。前端只用它过滤搜索结果，不在列表页展示正文片段；由于 GitHub Pages 是公开站点，进入索引的文本本身也会成为公开可下载数据。

如果 Dropbox 已经清理掉某个 PDF，但仓库里还出现过对应投行目录标题，构建会生成 `archive_catalog.json` 里的文字归档条目：该条目 `available=false`、`pdf_archived=true`，仍可在首页按标题/正文搜索到；进入详情页时只展示文字记录和联系 MacroGate 获取原文的提示，不提供直接 PDF 下载。

流程：

1. 扫描 Dropbox `/zip_backup/<日期>/` 下当前仍存在的 PDF。
2. 用既有投行脱敏规则生成页面标题。
3. 合并到长期 `catalog.json`，并统计页面可见 PDF 总容量。
4. 如果 catalog PDF 总容量超过 `storage_limit_gb`（默认 8GiB），按 `date_folder` 从旧到新删除整日旧报告，并删除对应 R2 object。
5. 将仍保留且当前扫描到的 PDF 上传到私有 R2，object key 为 `reports/<report_id>.pdf`。
6. 生成并提交 `search_index.json`、`archive_catalog.json`，再生成 Pages artifact；其中 `catalog.json` 供列表和详情页使用，`search_index.json` 供全文搜索使用。
7. 部署 GitHub Pages。
8. Cloudflare 配置齐全时，自动部署 Worker。

下载密码优先使用按 report id 推导出的 HMAC 伪密码：

```text
KC-<base32(hmac_sha256(PASSWORD_SECRET, "kc-desk-notes:" + report_id)) 前 12 位，按 4-4-4 分组>
```

不要把 `PASSWORD_SECRET` 放前端。需要计算时访问隐藏 Worker 计算器：

```text
https://<worker>/calc?id=<report_id>&key=<CALC_KEY>
```

如果需要，也可以继续使用 `KC_DESK_DOWNLOAD_PASSWORD` 作为全局备用密码。

#### 3.5.1 Reportify 模块（其他报告）

在 KC Desk Notes 搜索页，本地 catalog 结果下方新增「其他报告 · Reportify」一栏，实时检索
[reportify.cn](https://reportify.cn/reports) 的公开研报，点击即可下载 PDF。reportify 的搜索和
报告详情都无需登录。

数据通路（全部走现有 Cloudflare Worker，避免浏览器跨域并隐藏第三方调用）：

```text
Pages 前端 → {worker}/reportify/search?q=关键词 → api.reportify.cn/reports?query=关键词
Pages 前端 → {worker}/reportify/pdf?id=<report_id>
   1) 可直接预览（readable）→ Worker 转发其 presigned url_pdf，秒级返回 PDF
   2) 已抓取过 → Worker 从 R2 `reportify/<report_id>.pdf` 直接返回
   3) 需后台抓取（gated）→ Worker 用 repository_dispatch 触发 reportify-grab workflow，
      返回 202 pending；前端提示「约 2 分钟后回本页刷新重新点击下载」并轮询 /reportify/status
```

相关文件：

```text
.github/workflows/reportify-grab.yml          # repository_dispatch / 手动触发的单篇抓取
scripts/reportify_pdf_grabber.py              # Playwright 抓取器（与 assets/rptify 一致）
scripts/upload_reportify_pdf_to_r2.py         # 把抓到的 PDF 传到 R2 reportify/<id>.pdf
workers/kc-desk-notes-worker/src/index.js     # /reportify/search、/reportify/pdf、/reportify/status
```

额外配置：Worker 需要 `GH_REPO`（如 `yt-feng/rpt_edit`）和 secret `GH_DISPATCH_TOKEN`
（fine-grained PAT，Actions 读写权限），只用于触发 gated 报告的后台抓取；不配置时 readable 报告
仍可下载，gated 报告会回退为提示去 reportify.cn 查看。grab workflow 复用现有 `R2_*` secrets。

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
- 中文精译 PDF 每页在页眉和页脚居中放置蓝色 `公众号：KC桌面` 标识，不再使用页面中央大水印。
- 默认把 `kc_translated_reports/<日期>/<报告>/translated.md` 转成微信公众号短版图文 HTML，可见正文约 2000 字；正文图片先走微信 `uploadimg`，封面走永久图片素材，并调用 `draft/add` 创建草稿；当 `wechat_freepublish=true` 时再调用 `freepublish/submit` 提交发布。
- 微信短版正文图默认最多 3 张、至少 3 张。优先使用 MinerU 抽出的报告图表；如果报告图不足，会参考 `gen_rpt` 的方式用 Pollinations 生成主题相关 AI 配图，下载压缩后再上传微信。
- 每篇公众号草稿正文末尾固定追加 `prompts/zsxq_img.jpg`，上传时会先通过微信 `uploadimg` 转成公众号可用图片 URL。
- 星球图之前的钩子（`DEFAULT_BODY_HOOK`）：`更多国际信源汇编&评论，扫码交流，每日更新~40页…`（星球介绍 CTA）。
- 星球图之后、文章最结尾再追加关注/星标提醒（`DEFAULT_AFTER_IMAGE_NOTE`）：`微信推荐机制调整，期望收到更多此类信息，关注后可以加微信从朋友圈查看更新&免费领取原文报告。或将「KC桌面」设为星标`。两段文案都在 `scripts/push_kc_translated_to_wechat_drafts.py` 顶部常量里改。
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

### 3.8 Institution latest PDF to WeChat（IMF / 世界银行 / BIS / OECD / 亚开行 / 世界经济论坛 / 联合国贸发会议 / WTO / Bruegel）

相关文件：

```text
.github/workflows/institution-latest-pdf-to-wechat.yml
scripts/fetch_institution_latest_pdfs.py
```

用途：在 Dropbox 主流程之外，每天额外抓取以下机构最新公开 PDF 报告，复用现有
MinerU → KC 中文精译 → 微信公众号草稿 链路，把它们也加工成公众号图文。原始 PDF
只是中转输入，不留存；只把原始 PDF 链接长期归档。

抓取来源：

| 机构 | 来源 | PDF 定位方式 |
| --- | --- | --- |
| IMF 国际货币基金组织 | Coveo 搜索 API（`imfproduction561s308u.org.coveo.com`，按 `@imfdate` 倒序、筛 English PUBS）。IMF 官网是 JS+Akamai，RSS 已废，但搜索后端 Coveo 不在 WAF 后 | 用 `curl_cffi`（Chrome 指纹）打开 imf.org 落地页，提取 `.pdf` / `.ashx`（含 JSON 内嵌链接） |
| World Bank 世界银行 | `search.worldbank.org/api/v2/wds` JSON API，默认只取 Policy Research Working Paper | API 直接返回 `pdfurl` |
| BIS 国际清算银行 | 4 条 RSS：`bis_fsi_publs`（研究报告，含年报/Bulletin/FSI）、`wppubls`（工作论文）、`bcbspubls`（巴塞尔委员会）、`cgfs_publs`（CGFS） | 把 `.htm` 落地页直接换成 `.pdf` |
| OECD 经合组织 | `oecd.org/en/publications.html` 列表页（服务端渲染）。Akamai 会拦 Chrome 指纹，但放行 Firefox 指纹（`impersonate_profile: firefox135`） | 打开报告页，提取 `/content/dam/` 下的 PDF |
| ADB 亚洲开发银行 | `adb.org/rss/publications`（含 ADBI 研究所论文）。WAF 拦 Chrome 系指纹，需 Firefox 指纹 | 打开落地页，提取 PDF |
| WEF 世界经济论坛 | `weforum.org/publications/` 列表页（服务端渲染，需 Chrome 指纹） | 打开报告页，提取 `reports.weforum.org/docs/` 的 PDF |
| UNCTAD 联合国贸发会议 | `unctad.org/publications` 列表页（服务端渲染） | 打开报告页，提取 PDF；已排除每页都挂的 "UNCTAD at a glance" 宣传册 |
| WTO 世界贸易组织 | `library/rss/latest_news_e.xml` 新闻 feed（出版物 feed 已死链） | 报告发布类新闻页带 PDF，纯公告自动跳过 |
| Bruegel 布鲁盖尔研究所 | `bruegel.org/feed/publications-feed.xml`，只保留 working-paper / policy-brief 等报告类。**Cloudflare 目前按 IP 整体拦 GitHub 云端 runner（各指纹均 403），该源暂只在本地/自托管环境可抓**，失败隔离不影响其它源 | 打开文章页，提取 PDF |

9 个来源均已实测可抓到真实 PDF（OECD 对 GitHub runner IP 偶发 403，靠单源隔离 + seen 去重次日自动补上；Bruegel 见上）。每个来源相互隔离，单个失败不影响其它。RAND 兰德、Brookings 布鲁金斯的配置仍保留，但已移出默认名单（话题偏敏感、涉华负面内容多），只有手动指定 `--institutions rand,brookings` 时才会抓。

触发方式：

- 手动运行：Actions → **Institution latest PDF to WeChat**
- 定时运行：北京时间 06:00，cron 为 `0 22 * * *`，排在 Dropbox 主流程（05:00）之后

主要参数（手动运行）：

- `institutions`：默认 `all` = `imf,worldbank,bis,oecd,adb,wef,unctad,wto,bruegel`（按优先级排序；总量达到上限时靠前的机构优先保额度）。`rand` / `brookings` 不在 `all` 里，必须显式指定才会抓。
- `since_days`：默认 `7`，只抓最近 N 天内发布的报告。**去重靠 seen 状态文件，不靠日期**，所以调大也不会重复处理旧报告，反而能兜住不是每天都发的来源。
- `max_per_institution`：默认 `25`，单机构限量，防止某一家刷屏。
- `max_total`：默认 `100`，单次运行全部机构合计的新 PDF 上限，对应"每天 100 篇公众号文章以内"的要求。
- `max_translated`：默认 `all`，翻译并生成公众号草稿的报告数量。
- `dry_run`：默认 `false`，真正写公众号草稿箱；测试时设 `true` 只产出 payload。
- `publish`：默认 `false`，公众号发布接口开通前保持 false。

数据流（与 Dropbox 主流程并行、互不干扰）：

```text
IMF/WB/BIS/OECD/ADB/WEF/UNCTAD/WTO/Bruegel feeds
  -> _institution_latest_pdfs/            # 中转 PDF，已 gitignore，不入库
  -> xhs_notes/institutions/<日期>/<报告>/source_mineru.md ...
  -> kc_translated_reports/institutions/<日期>/<报告>/kc_translated_report_XX.pdf
  -> wechat_drafts/institutions/<日期>/draft_payload_*.json
```

链接归档与去重：

```text
institution_feeds/institution_pdf_archive.jsonl   # 每条记录：机构 / 标题 / 发布日期 / 原始 PDF 链接 / 来源页 / 本地文件名
institution_feeds/seen_state.json                 # 去重状态，标记 downloaded / no_pdf / too_old，默认保留 120 天
```

说明：

- 原始下载的 PDF 落在 `_institution_latest_pdfs/`，已加入 `.gitignore`，处理完即可丢弃；仓库里只保留 `institution_pdf_archive.jsonl` 中的原始链接和精译后产物。
- 每个来源相互隔离：某个机构 feed 失败不会影响其它机构。
- 网络错误（feed / 落地页拉取失败）不会写入 seen，下次运行会重试；只有“已下载”和“确认无 PDF”才会标记 seen。
- 复用的 secret 和主流程一致：`MINER_U`、`DEEPSEEK_API_KEY`、`WECHAT_MP_APPID`、`WECHAT_MP_APPSECRET`。微信上传仍走带 `wechat-draft` label 的固定 IP self-hosted runner。
- 机构中文名通过 `scripts/institution_names.py` 推断（含 IMF / 世界银行 / BIS / 经合组织 / 亚洲开发银行 / 世界经济论坛 / 联合国贸发会议 / 世界贸易组织 / 布鲁盖尔研究所 / 兰德 / 布鲁金斯），公众号标题会自动带上机构名。
- 调整抓取来源 / feed / 文档类型：编辑 `scripts/fetch_institution_latest_pdfs.py` 顶部的 `INSTITUTIONS` 配置。
- IMF 走 Coveo 搜索 API，用的是公网浏览器可见的 search key（写在 `INSTITUTIONS["imf"]["coveo_token"]`）。如 IMF 轮换该 key，可用 `IMF_COVEO_TOKEN` 环境变量覆盖，无需改代码。`--imf-rows` 控制每次扫描的 Coveo 结果数（默认 60）。IMF PUBS 每天发很多（工作论文、国别报告、Selected Issues、FSAP、Article IV 等）；如只想要部分，收紧 `coveo_aq` 的 `@imfcontenttype` 过滤即可。
- World Bank 的 WDS `docdt` 比实际发布滞后数月，因此该来源不按日期过滤（`recency_filter=False`），只按 `docdt` 倒序取最新若干篇并靠 seen 去重；其余来源按 `since_days` 过滤。
- 依赖 `curl_cffi`（已加入 `requirements.txt`）：IMF / WEF 用 Chrome TLS 指纹，OECD 用 Firefox 指纹（Akamai 对 Chrome 指纹更严）。未安装时对无指纹要求的来源无影响。整条链路不需要无头浏览器。
- **微信公众号合规：RAND / Brookings 已从默认抓取名单移除；精译步骤仍保留 `--exclude-institutions "rand,brookings"` 双保险，即使手动抓了也不翻译、不上公众号。**
- **标题敏感性审核：精译步骤加了 `--title-guard`，对进入精译的每篇用 DeepSeek 审核标题（是否唱衰中国 / 攻击中国制度 / 涉敏感政治议题）。判为 SENSITIVE 的不翻译、不进草稿箱；DeepSeek 报错或结论不明时按"宁可漏发"处理（跳过）。被跳过的记录在 `kc_translated_reports/institutions/<日期>/translation_summary.json` 的 `sensitive_skipped` 里。**
- market views 汇总 PDF 不做敏感过滤，当天抓到的机构全部纳入，见 §3.3。

### 3.9 Consulting latest PDF to WeChat（MBB：麦肯锡 / BCG，贝恩暂缓）

文件：`.github/workflows/consulting-latest-pdf-to-wechat.yml`，复用 `scripts/fetch_institution_latest_pdfs.py`。

用途：和 §3.8 并行，每天额外抓取 MBB 战略咨询的最新报告 PDF，复用 MinerU → KC 精译 → 公众号草稿 链路。MBB 官网都是 JS + 反爬（Bain 直接 Cloudflare 挑战），所以不直接爬官网：

| 机构 | 发现方式 | 时效控制 |
| --- | --- | --- |
| McKinsey 麦肯锡 | DuckDuckGo 搜 `site:mckinsey.com filetype:pdf`（curl_cffi），PDF 在 mckinsey.com/~/media 直链下载 | DDG 按相关性排序、非按日期，故用 `recent_years=2` 只保留 URL/标题含 **当年或去年** 的报告，过滤掉旧的常青报告 |
| BCG 波士顿咨询 | 站点 sitemap 列出全部 publications，页面链向 web-assets/media-publications 的 PDF | 按 `<lastmod>` 倒序，并用 `sitemap_max_age_days=120` 只取最近修改的，过滤旧报告 |
| Bain 贝恩 | 暂缓 | 报告 PDF 在 `www.bain.com/contentassets` 的 Cloudflare 后面，下载直接 403，curl_cffi 过不去；以后有稳定绕过方法再加 |

触发：手动 Actions → **Consulting latest PDF to WeChat**；定时北京时间 06:30（cron `30 22 * * *`，排在机构流程 06:00 之后）。

输出（与 §3.8 同构、相互独立）：

```text
_consulting_latest_pdfs/                          # 中转 PDF，gitignore
institution_feeds/consulting_pdf_archive.jsonl    # 原始链接长期归档
institution_feeds/consulting_seen_state.json      # 去重状态
xhs_notes/consulting/<日期>/...
kc_translated_reports/consulting/<日期>/...
wechat_drafts/consulting/<日期>/...               # 独立的一批公众号草稿
```

说明：

- **时效性：不是"只抓当天发布"，而是"最新优先 + 旧报告过滤 + seen 去重"。** McKinsey 限定当年/去年，BCG 限定最近 120 天修改；首跑会抓当前这批近期报告，之后每天只增量抓新出现的（seen 去重保证不重复）。想更严格可调小 `recent_years`（改 1）或 `sitemap_max_age_days`（改 30/60）。这些常青站点没有可靠的"今天发布"信号，做不到严格的"仅当天"。
- 同样过 `--title-guard` 标题敏感性审核；`--max-per-institution` 默认 5，控制每家每天量。
- MBB 也并入 market views 汇总 PDF（§3.3 的 `--extra-roots` 已含 `xhs_notes/consulting`）。
- 加 / 调来源、时效阈值：编辑 `scripts/fetch_institution_latest_pdfs.py` 顶部 `INSTITUTIONS` 里 `mckinsey` / `bcg` / `bain` 的配置。

## 4. 主要脚本

| 脚本 | 用途 |
| --- | --- |
| `scripts/download_dropbox_latest_pdfs.py` | 读取 Dropbox `/zip_backup` 最新日期文件夹，并下载 PDF |
| `scripts/fetch_institution_latest_pdfs.py` | 抓取 IMF/BIS/世界银行/兰德/布鲁金斯 最新 PDF 报告到中转目录，归档原始链接并按 seen 状态去重 |
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
| `scripts/kc_desk_notes_catalog.py` | 扫描 Dropbox PDF、合并长期 catalog、按 8GiB 总量上限清理旧日期、同步当前 PDF 到 R2 |
| `scripts/build_kc_desk_notes_site.py` | 生成 KC Desk Notes GitHub Pages 静态站点 artifact，并把投行目录 txt 与可匹配的 MinerU 正文并入前端全文搜索索引 |
| `scripts/hash_kc_desk_notes_password.py` | 生成 `password_rules.json` 里的密码 hash |
| `scripts/reportify_pdf_grabber.py` | Playwright 抓取 reportify.cn 单篇报告 PDF（Reportify 模块后台抓取用） |
| `scripts/upload_reportify_pdf_to_r2.py` | 把抓到的 reportify PDF 上传到 R2 `reportify/<id>.pdf` |
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
xhs_notes/institutions/
publish_ready_zips/
bank_report_catalogs/
market_view_summaries/
bilingual_podcast_videos/
kc_translated_reports/
kc_translated_reports/institutions/
wechat_drafts/
wechat_drafts/institutions/
```

`institution_feeds/`（原始 PDF 链接长期归档 + seen 去重状态）也由 Actions 维护并提交，但它不是按日期分目录、不参与按最近 3 天的清理，应长期保留。机构来源的原始下载 PDF 落在 `_institution_latest_pdfs/`，已 gitignore，不入库。

本地修代码时不要用旧的本地生成目录覆盖远端。合并或 rebase 时的默认策略：

- 代码、workflow、prompt、文档：以本地明确修改为准。
- 上面列出的日期型生成目录：以远端 Actions 产物为准。
- KC Desk Notes 的 `kc_desk_notes/data/catalog.json` 不按最近 3 天清理；它按页面可见 PDF 总容量控制，默认超过 8GiB 后从最旧 `date_folder` 开始删除整日旧报告，并同步删除对应 R2 object。
- KC Desk Notes 的 `kc_desk_notes/data/search_index.json` 和 `kc_desk_notes/data/archive_catalog.json` 也不按最近 3 天清理；它们用于保留历史文本检索能力。`search_index.json` 受构建参数 `--search-index-limit-gb` 控制，默认最多 2GiB，超出后按旧日期从文本索引中移除。

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
6. 如果要额外把 IMF/BIS/世界银行/兰德/布鲁金斯 当天报告转成公众号草稿，跑：**Institution latest PDF to WeChat**（默认每天 06:00 自动跑）。
7. 如果只是手动上传 repo 内 PDF，参考旧版 `docs/pdf-to-xhs-workflow.md`。

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
