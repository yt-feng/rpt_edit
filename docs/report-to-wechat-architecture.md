# 报告到微信公众号流水线架构

本文档是 Dropbox、国际机构、咨询公司和 ARK 报告进入微信公众号草稿箱的架构基线。
工作流、脚本边界、持久化状态、失败语义或恢复方式发生变化时，必须同步更新本文档和
`docs/pipeline-overview-v2.md` 的对应入口说明。

最后更新：2026-07-20。

## 1. 目标与范围

这条流水线负责：

1. 从 Dropbox 或公开信源发现 PDF。
2. 用 MinerU 提取正文和原始图表。
3. 用 DeepSeek 生成短版中文文章、标题和 KC 评论。
4. 用确定性规则与模型审核过滤不适合公众号的标题。
5. 生成 KC 中文汇编 PDF 和公众号 HTML。
6. 通过固定 IP self-hosted runner 慢速上传微信公众号草稿，并用 `draft/get` 校验。

市场观点 PDF 与公众号存在不同的内容边界：市场观点 PDF 可以保留原始国际信源；
公众号必须通过更严格的标题、措辞和荐股语言审核。

## 2. 运行边界

```mermaid
flowchart LR
  A["Dropbox / IMF / WB / BIS / MBB / ARK"] --> B["GitHub-hosted runner: discover + download"]
  B --> C["Transient PDFs"]
  C --> D["MinerU: Markdown + charts"]
  D --> E["DeepSeek: note + WeChat article"]
  E --> F["Deterministic title guard + model guard"]
  F --> G["KC translated artifacts"]
  G --> H["Commit required handoff to origin/main"]
  H --> I["Fixed-IP self-hosted runner"]
  I --> J["Build HTML + upload images + pacing"]
  J --> K["WeChat draft/add"]
  K --> L["WeChat draft/get verification"]
  L --> M["Draft summary committed to origin/main"]
  D --> N["Market views PDF"]
```

### GitHub-hosted runner

负责公开信源抓取、MinerU、DeepSeek、图表筛选、标题审核、中文汇编 PDF 和产物提交。
该 runner 不需要微信公众号固定 IP。

### 固定 IP self-hosted runner

label 为 `wechat-draft`。负责微信 token、图片上传、`draft/add`、`draft/get` 校验和草稿摘要。
输入必须来自已经推送到远端 `main` 的产物，不以某台开发电脑的工作区为准。

## 3. 核心组件

| 组件 | 职责 |
| --- | --- |
| `scripts/fetch_institution_latest_pdfs.py` | 国际机构和咨询来源发现、PDF 下载、seen 状态和链接归档 |
| `scripts/run_pdf_to_xhs_in_batches.py` | 分片、稳定编号、已有产物跳过和 batch 汇总 |
| `scripts/pdf_to_xhs_batch.py` | MinerU、短版文章、标题候选、图表和逐篇状态 |
| `scripts/deepseek_http.py` | DeepSeek 瞬时网络错误和可重试 HTTP 状态的有界退避 |
| `scripts/sensitive_content_guard.py` | 荐股措辞、严格词语和公众号敏感标题的确定性规则 |
| `scripts/build_kc_translated_reports.py` | 精译、文章化、标题双层审核和 KC PDF |
| `scripts/commit_output_dir.sh` | 并发环境中的 fetch/reset/add/commit/push 重试和关键交接校验 |
| `scripts/push_kc_translated_to_wechat_drafts.py` | HTML、三张正文图、慢速图片上传、草稿创建与回读校验 |

主要入口：

| Workflow | 来源 | 默认时间（北京时间） |
| --- | --- | --- |
| `dropbox-latest-pdf-to-xhs-sharded.yml` | Dropbox 投行报告 | 05:00 |
| `institution-latest-pdf-to-wechat.yml` | IMF / WB / BIS 等 | 06:00 |
| `consulting-latest-pdf-to-wechat.yml` | McKinsey / BCG | 06:30 |
| `ark-invest-feed-to-wechat.yml` | ARK feed | 以 workflow 配置为准 |

## 4. 持久化与幂等

远端 GitHub `main` 是唯一可信版本。原始 PDF 是中转输入，不要求永久保留。

长期状态包括：

- `institution_feeds/*archive.jsonl`：原始链接归档。
- `institution_feeds/*seen_state.json`：跨日去重。
- `xhs_notes/<source>/<date>/`：MinerU、文章和逐篇状态。
- `kc_translated_reports/<source>/<date>/`：公众号上游和每日汇编输入。
- `wechat_drafts/<source>/<date>/`：payload、成功 `media_id` 和校验结果。

幂等规则：

- 只有确认下载或确认无 PDF 的条目才进入 seen；网络错误不写 seen，次日继续尝试。
- 报告目录同时存在 `source_mineru.md`、`note.md`、`wechat_article.md` 才算可复用成功产物。
- `force_reprocess=false` 时跳过完整产物；`true` 时清理当天目标目录后重做。
- 微信成功不是只看 `draft/add` 返回值，必须再用 `draft/get` 确认文章数一致。

## 5. 内容与标题不变量

- 标题以原始 PDF 文件名为最高权重，DeepSeek 只负责翻译、压缩和补充有证据的数字或反常识钩子。
- 标题必须完整、自然、可独立理解，目标长度 20-35 个中文字。
- 先执行不依赖模型的敏感标题规则，再执行 DeepSeek 审核。
- 军事、国防、军用装备、武器、战争、战备，以及明确政治敏感议题的标题直接阻断进入微信。
- 标题审核在原始标题和最终精修标题各执行一次，防止翻译或精修阶段重新引入敏感词。
- 微信上传脚本还会执行第三次最终标题策略过滤；KC 精译和 XHS 直传两条路径共用该规则。
- 个股报告不得出现目标价、评级、买入、卖出或推荐措辞。
- 正文不放中间 CTA；只保留 KC 评论和最结尾统一文字 `更新信息参见ΚСⅾеѕk․сοｍ`。
- 正文默认三张图，优先原报告图表；缺图时生成与相邻段落相关的图，并分散插入正文。

## 6. 失败与重试语义

| 边界 | 行为 |
| --- | --- |
| 信源 GET / API POST / PDF 下载 | 最多 3 次；只重试连接错误、`408/425/429/5xx`；尊重 `Retry-After`；`401/403/404` 直接返回 |
| IMF PDF 定位 | Coveo 的系列编号优先推导官方 `/media/files/publications/` PDF；Akamai 落地页只作后备，避免落地页 `403` 造成假空结果 |
| 单一信源 | 与其他信源隔离；发现未处理的新条目但全部解析或下载失败时记为 `error`，部分失败记为 `degraded`，不能解释为确认零更新 |
| MinerU | 支持多个 token、分轮重试和无进展超时；已完成 PDF 可继续处理 |
| DeepSeek 短版文章 | 最多 4 次有界指数退避；连接重置不能直接终止 batch |
| DeepSeek 精译 | 每个片段最多 3 次完整调用；标题与文章化调用也有 HTTP 重试 |
| 单篇报告 | 捕获异常并写 `status.json`；继续同批其他报告 |
| 空产物 | 一个 shard 有输入但最终没有 publish-ready 报告时返回失败，禁止假绿 |
| Git 交接 | 最多 8 次同步并推送；微信下游依赖的目录启用 strict handoff，推送失败则 job 失败 |
| 微信 API | 网络、`-1 system busy` 和可重试状态最多 5 次；图片和草稿提交有固定 pacing |
| 微信草稿 | `draft/add` 后等待并执行 `draft/get`；文章数不一致视为失败 |

永久性认证、余额或参数错误不会被无限重试。所有重试必须有次数上限和最长等待时间。

## 7. 批处理成功标准

- 某一篇失败不应抹掉同批已经完成的报告。
- 多篇输入时，只要存在成功报告，可以继续后续步骤，同时在 summary 中保留失败明细。
- 所有报告都失败时必须返回非零退出码。
- 全程零下载时，IMF、World Bank、BIS、McKinsey、BCG 任一核心发现源为 `empty/error/degraded`，抓取步骤必须失败；只有核心来源均健康且候选已 seen/确认为无 PDF，才可把 0 篇解释为正常无更新。
- 所有报告都被标题审核主动过滤时，可以成功结束但不得创建微信草稿。
- 微信 job 只有在 `translation_summary.json` 明确显示全部因标题审核跳过时才接受空输入；真实生成失败造成的空目录仍必须失败。
- 关键 Git 交接未进入远端 `main` 时，微信上传 job 不得继续。

## 8. 恢复手册

### DeepSeek 瞬时失败

查看 `Generate MinerU source text and notes` 日志。如果 MinerU 已 `done`，但 DeepSeek 在重试耗尽后失败，
修复或充值后从最新 `main` 重新触发 workflow。失败运行未提交 seen 状态时，不需要 `force_reprocess`。

### 已提交 seen，但需要重做当天文章

手动运行 workflow，并设置 `force_reprocess=true`。这会重建当天输出；上传前仍会经过标题审核。

### 微信 job queued

检查 `wechat-draft` self-hosted runner 是否在线、磁盘是否充足，以及同一 runner 是否已有 job。
不要改用本地电脑绕过固定 IP。

### 微信上传失败

先看微信 errcode：固定 IP 白名单、token、图片大小和草稿文章总大小分别处理。
只在没有成功 `draft/get` 校验时补跑；已有成功 `media_id` 时不要盲目重复创建。

### 关键产物推送失败

strict handoff 会让 build job 失败并阻止微信 job。先解决并发 push 或 GitHub 状态，再从最新 `main` 补跑。

## 9. 可观测性

每次运行至少保留：

- source manifest 和 source health。
- `mineru_attempts_summary.json`。
- `summary.json` / `batch_run_summary.json`。
- `translation_summary.json`，含成功、失败和敏感标题跳过明细。
- `wechat_draft_summary.json`，含 payload、`media_id` 和 `draft/get` 文章数。
- 微信标题日志，便于连续观察 DeepSeek 标题质量。

不要仅依据 workflow 绿色图标判断业务成功；要核对报告数量、草稿文章数量和 `media_id`。

## 10. 变更检查清单

修改这条流水线时至少确认：

1. 新外部请求是否定义了超时、可重试条件、最大次数和永久错误行为。
2. 单篇失败是否会影响同批其他文章。
3. 失败是否会错误写 seen 或造成重复草稿。
4. 标题是否同时经过原题和最终题两次审核。
5. 关键产物是否已经进入远端 `main` 才启动 self-hosted runner。
6. 微信是否执行慢速上传和 `draft/get` 校验。
7. 是否补充了定向测试。
8. 是否同步更新本文档和 `docs/pipeline-overview-v2.md`。
