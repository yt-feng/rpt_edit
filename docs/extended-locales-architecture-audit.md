# 多语言架构与恢复核对（2026-10-10）

当前架构见[多语言生成与发布](portal-multilingual-architecture.md)。本记录替代 2026-09-25 的一次性首批说明：同源发布、跨批继承、跨日队列和英文发布器已经实现，不能继续把这些能力写成“尚未对接”。但候选存在也不能等同于全语种已发布。

本轮审阅基线为 `47066698b690a953b7163923c11dcb2ff69cdad1`。下列运行状态为 2026-10-10 的取证快照，之后的进度须以对应 run 和正式 active release 重新确认。

## 范围与入口核对

| 核对项 | 代码事实 |
| --- | --- |
| 登记总数 | 38 个语言/变体：中文 1 + 既有镜像 3 + 新增非英文阅读目标 33 + 英文评论 1 |
| `all-supported` | 33 个新增非英文目标；英文由独立开关和 source admission 进入矩阵 |
| 当前自动入口 | `Neutral edge catalog refresh` 成功 → 独立 `Extended locale source admission` → `Extended locales private R2 pipeline` |
| 来源范围 | 2026-09-25 起北京时间当天新增详情；单批 1..24 个网站页面；跨日保留已 admission 待办 |
| CPU 调度 | 全局互斥、`cancel-in-progress: false`、单矩阵 `max-parallel: 2` |
| 预算 | 每语言默认/上限 14,400 秒，job 270 分钟；有效截止时间传入模型 |
| 非英文回退 | 被拒绝模型文本不落库；精确源文保存在独立 fallback 记录，候选计数明确披露 |
| 英文 | 只翻译明确的 KC/编辑评论；禁止原文回退、全文镜像和图表；完整正文私有 |
| 自动发布 | 非英文仅对开关允许且已正式启用的语言 handoff；英文使用独立开关、ready queue、审核 |

新增语言的具体 33 个代码、产品边界和发布门禁以主架构文档及代码登记为准，不能由模型支持列表推断每个语言已经在线。

## 实际队列与失败证据

- 中文目录恢复生产 `38036944110` 后，`source admission 38043173198` 成功。新 R2 run `38043249029` 取证时为 pending。
- 旧矩阵持有者 `38030674044` 的总状态显示 queued，但 job 明细后续取证已经完成 10/34 个 locale job，其他语言仍运行/排队。它不是“CPU 完全未启动”，新 workflow 也不能绕过这个互斥组。
- 该 source 摘要中，33 个非英文目标各有 83 个 pending，选 24 个、余 59 个；英文有 81 个 pending，选 24 个。数字是各自语言队列，不应合并成不重复的源文章数量。
- `英文 job 114151900663` 完成后失败：22/24 个页面完成，62 次调用、0 次 Memo 命中；错误各为 `expansion-validation` 1、`offline-quantity-validation` 1，没有预算耗尽。
- `法语 job 114151900697` 的候选为 24/24，但 `translation_complete=false`：100 个原文回退单元、104 次使用，原因均为 `offline-quantity-validation`；315 次调用、403 次缓存命中。该候选可恢复和审核，不代表全部内容已译成法语。

## 已正式发布的语言覆盖与时效边界

生产 `38036944110` 在 2026-10-10 09:56:35 UTC 的线上审计通过，发布 ID 为 `c1c0b923210a207614c8d59ad1e12a5c`，与随后读取的 edge state 和下载服务 runtime release 一致。

- 33 个新增非英文语言：首页全部 HTTP 200，每语言两个确定性深页样本全部 HTTP 200。sitemap 页面计数为 `km` 79，其余 32 语言各 33；计数不等于成功翻译单元数量。
- 既有 `ko/ja/ar`：首页、深页和 sitemap 均 HTTP 200；候选字节、canonical、lang 与路由/资产检查通过。
- 中文加上述 36 个非中文语言具备已发布页面证据，共 37 个语言/变体；英文当次 `ENGLISH_READY=false`，assembly `ready=false,page_count=0`，不能计作英文评论已上线。
- 新增语言审计从 sitemap 深页字典序首尾取样，Blog 样本分别为 2026-09-26 与 2026-10-06。它证明已发布 Blog URL 的日期边界到 10 月 6 日，不证明中间每天齐全，也不能证明 10 月 8–9 日中文新增已同步翻译发布。

这次线上证据未给出 active release 每语种的源文回退统计，不能声称全部页面均已完整翻译。后续恢复还须证明新日期进入正式发布、英文评论可读、回退数与旧已发布集合正确；不能把 38 个登记代码、34 个矩阵 job 或单语 24/24 候选写成“38 语种正常且最新”。

## 本轮修复的确定性失败类别

### 1. 英文审核取错资源版本

此前 `生产 run 37785895519` 的 `english_daily_review` 在精确预览投影门禁失败。prepare job 已物化部署配置，fresh review checkout 的 `app.js` 尚未物化；两者生成的 `?v=` 资产 token 不同，导致合法预览 HTML 也被判成 `Prepared English public HTML is not a preview-only projection`。

修复后，英文 compose 从**最终未激活目录的资产字节**计算版本，review 从固定上传 manifest 取同一 SHA 重建 HTML，并有界读回全部 7 项实际资产核对长度与内容 SHA。仍然精确核对预览投影，不忽略脚本 URL、HTML 差异或私有正文。回归覆盖不同部署配置、fresh reviewer 不存在本地资产、渲染后资产被篡改、固定 manifest 后任一资产被改写或删除、缺失资产及隐藏私有正文。

### 2. 英文严格校验发生在 checkpoint 写入之后

共享 Memo 的普通阅读页校验允许少量机构名汉字，而英文评论要求完全不含中日韩残留、原文链接或过长标题。旧实现先保存 Memo，之后才由英文外层拒绝；下次恢复重复命中同一个坏单元，即使有可用的新译文也不重新调用模型。

离线复现表现为首次失败、第二次仍失败，第二次 0 次模型调用、2 次缓存命中。修复把英文内容门禁移入 Memo 写入/复用之前；旧坏 checkpoint 或 seed 只剔除对应精确单元，并清理该单元的模型缓存。合格单元继续复用，坏响应不写候选、正文或成功缓存。

新增固定错误码区分 `english-language-validation`、`english-asset-validation`、`english-size-validation`，不输出原始异常正文。旧 `expansion-validation` 候选仍可只读检查和恢复。该缺陷是已复现的恢复阻塞类别，不能仅凭当前云端一个通用错误码就断定它解释了所有英文失败。

### 3. 数量门禁保留严格等价

当前英文数量诊断显示源有 `27`，响应有 `27` 与 `11`。对源文本 SHA 及最终模型输入 SHA 的精确绑定确认，其中额外记号来自“双十一”的英文活动名称表达。此类修复必须识别同一购物活动的等价值，不能删除未知数字或跳过数量校验；其它新增、遗漏、改写金额、日期和比例仍应被拒绝。

数量修复由共用 financial quantity validator 及其合成回归覆盖。该英文诊断不能推断法语全部 100 个回退都属于同一原因；各语种还需按固定源、校验错误及恢复后的结果分别核对。恢复使用当前合法 checkpoint，不清空所有合格译文，不重新抓取或改写来源 generation。

法语另有两类已离线复现的格式误判：合法千分组 `1 234,5` 被拆成两个数字，以及 `troisième trimestre de 2026` 未识别为带年份的第三季度。早期法语修订仅在显式 `fr` 一侧、Unicode 空格折叠之前识别完整合法分组（普通空格、不换行空格或窄不换行空格；首组 1–3 位、后组严格三位、可选逗号小数），并识别四个固定法语季度序数及四位年份或无年份表达。坏分组、额外数字、金额/币种/比例、季度或年份变化继续拒绝；当时默认及其它语言语法、既有“双十一”契约保持不变。后续已按 CLDR/ICU 证据补齐所有 33 个扩展语言的相关数字语法，详见[共用数字翻译契约](financial-quantity-translation.md)；以下法语段落保留原策略的历史与兼容入口说明。合成正反向与变异回归已经通过，但这不证明真实法语 100 项回退都由这两类造成，也不代表对应生产译文已经恢复或上线。

## 法语已完成候选的精确回退恢复

`fr-quantity-fallback-v1` 是独立于原有 legacy basis-point `checkpoint-repair` 的窄策略，校验修订固定为 `fr-space-grouping-quarter-v1`。该兼容入口不会自动重试全部 fallback；新入口也不清空全局 Memo、不更改其它 locale、不重开历史 admission。原 producer 必须已经结束，原 source 与 `locale (fr)` job 成功；同一全局串行队列及 `max-parallel: 2` 保持不变。

1. 在现有 `portal-extended-locales-r2.yml` 的主线人工入口选择 `source-fallback-inspect`，`locales=fr`，固定 `source_generation`；`continuation_evidence` 提供策略、修订、原 producer 的 `run_id/attempt/sha`、原 checkpoint SHA、candidate ID、manifest SHA 和 `units: []`。只读步骤可从校验过的 immutable origin 补齐 `source_sha256/origin_sha256`。它重新验证原页、完整缓存覆盖和原候选字节，仅输出 eligible unit hashes、完整 request、计数；模型调用与 R2 写入均为零，locale 与 publication job 不运行。
2. 将只读结果中的完整 request 固定下来，把 `units` 换成 1..20 个排序且不重复的明确 eligible hashes，使用同 workflow 的 `checkpoint-repair`。所有选中项必须是当前精确旧 checkpoint 内的 `offline-quantity-validation` 源文回退。未选中的译文/回退逐项保留；模型只处理选中单元，仍使用完整质量门，每个单元只允许一个模型尝试。
3. 私有 durable ledger 的身份包含模型、checkpoint 版本、`fr`、单元 hash 和固定修订，独立于 run、generation 和请求包装。原子 started claim 必须写入并读回后才允许模型调用；accepted 或 terminal outcome 不可改写。已启动但结果未知时阻止重开，换 run 或重包装 request 不能重复付出模型工作。
4. 已接受的 exact rows 合入原固定 checkpoint，使用零模型缓存重放证明原完整页面集合不变、其它单元保持原字节。页面没有改变时保留原 candidate/manifest/checkpoint，不覆盖相同 candidate ID。页面改变时生成新不可变候选，将 registered outcome 从 complete 精确替换到 complete；原 source/origin/continuation 计数与其它语言、其它完成页保持。最新增量 Memo 即使已前进到另一 generation，也只合并被接受的精确 keys，不倒退指针、不覆盖较新冲突单元。
5. immutable proof 和候选先持久化，再写原 generation checkpoint、最新 Memo、completed receipts 和 queue。manifest 已写而 ready 未写的中断可以按相同字节补齐；prepared tail 中断则从原 proof 重新完整验证后恢复。若新 run 仅完成这个尾部，会生成绑定原 prepared proof 的独立 completion receipt；审核必须验证该新主线人工 run 的 source 成功、locale 明确 skipped。普通路径仍要求原 repair source 与法语 locale 成功，不把失败 locale 冒充成功。
6. handoff 绑定修复 proof、原 origin、新 candidate 和精确 checkpoint；如有 completion，也绑定其独立身份。活动批准 ledger 原序保留，再追加新全页候选。正常 Environment 审核、未激活目录校验、整站切换和真实 URL 验收均保留。

本地回归覆盖 restore→build→persist、manifest/ready 中断、prepared tail 跨 run 恢复、连续两批修复、较新 Memo/页面冲突、无页面变化、handoff 精确身份及保留原批准 ledger 的零模型 compose。这些是恢复机制验收，真实旧法语 100 项的重新翻译、回退下降和生产发布仍待验收；只读旧响应诊断不可用，也不能声称这 100 项都由空格或季度格式引起。

截至上述 10/34 矩阵快照，另外已完成的非英文候选也均为 24/24 页面且 `translation_complete=false`：`pt` 109、`es` 100、`tr` 127、`ru` 113、`th` 124、`it` 118、`de` 116、`vi` 114 个源文回退单元。除 `th` 同时有数量与目标文字校验外，其余已列候选仅报告数量校验；未保存的拒绝响应不能由错误码推断具体原因。原法语窄策略不直接用于这些语言；后续通用质量欠账策略在固定各自 locale/source/unit 身份下复用同一恢复引擎，见文末。已发布 37 个语言/变体的路由证据仍不等于新日期内容全部翻译完成。

## 跨语种渲染进度与翻译质量欠账

`complete-candidate`、R2 ready 和 `completed` 日游标只证明页面已完整渲染、上传和可复用，不再被自动发布入口解释为“全部翻译完成”。这两个状态必须独立：保留 render receipts 的去重，避免普通定时任务重复调用已拒绝的模型单元；`translation_complete=true`、零源文回退、完整页面集合、零 budget/failure 才能进入新的自动 handoff。

`portal_extended_quality.py` 在候选持久化后、完成日游标之前保存 immutable quality proof，绑定 locale、source generation、实际 source bytes SHA、candidate ID 和实际 manifest bytes SHA。新 build manifest 仅附加本次实际使用的 fallback unit hashes，不能把跨代 seed 中未使用的旧 fallback 计入本批。旧 manifest 缺少明确质量字段时记为 `unproven`，不会从页面成功状态推断为就绪。没有 hash 清单的旧 fallback 仍保留其精确 manifest 身份和欠账计数，不伪造单元级证据。

每个 locale 的 `incremental/quality-debt/<locale>/latest/state.json` 独立记录最多 500 个 generation；每份 quality proof 的 fallback hashes 最多 10,000 个、字节不超过 1 MiB。完整证据先写入并读回，再更新欠账。相同结果重复保存不产生新模型调用；翻译完全就绪只清理相同 generation 的欠账。原注册结果、日完成页、有效 Memo、continuation 计数、其它语言和较新源不被重置。正常 prepare 即使 `has_work=false/pending_page_count=0`，摘要仍显示各语言的 quality debt 与 fallback 数；源任务也会从旧 registered complete outcomes 补齐质量欠账。既有 active fallback 候选被 publication ACK 移除队列前，先保留其质量欠账。

自动 handoff 对每种语言分别验证候选字节与 quality proof，只选择已证明 translation-ready 的新候选；一个语言欠账不会阻断同批其它已就绪语言。handoff receipt 包含每种候选的 quality proof SHA，读回及自动 reviewer 重新验证 source/manifest 的精确身份。旧无质量证明的 handoff 不可直接取得新的自动批准。现有 active approval ledger、已发布 fallback 页面和 source-content binding 保持原契约：只在已批准的同一源内容上零模型重放。`current_document` 遇到正文变化仍拒绝把旧译文重新绑定到新源，也不借此覆盖中文正文。

法语窄修复的 accepted 单元可以继续逐批持久化，但若仍有其它 fallback，新候选只记为质量欠账；直到全部单元符合原质量门，才允许正常自动 handoff。已准备尾部的跨 run 恢复仍复用原 proof，不重新调用模型。此变化不自动把同一修订的 terminal/unknown 单元重新排队，也不推断其它语言的具体数量误差原因。

原 continuation 的 64-generation 上限和双 CPU worker 限制保持不变。未发布且仍欠账的 registered complete rows 保留，便于精确人工恢复；达到该既有上限时仍显式停止，不静默删除历史结果。今后若要退休这些队列行，必须同时提供绑定 immutable quality proof 的恢复入口，不能靠删除行或清缓存消除欠账。

回归使用两页、两个真实渲染 fallback 单元证明：页面去重后模型工作为零但欠账仍为二；正常重放不重试；ready sibling 可独立 handoff；active ACK 不删除欠账；完全恢复只清同 generation；hash/源/manifest/候选变化、伪造就绪、旧无证明 handoff 均拒绝。另验证已有 active fallback 的原字节继承以及正文变化仍阻断。该机制不代表旧批所有语言已经恢复，需以实际逐语种回退下降、handoff、正式切换和公共 URL 继续验收。

## 已验收历史 Blog 批次的精确准入

正常 `latest-published-source-refresh-v1` 仍只采集网站最新内容日期。补发的较早 Blog 不会通过修改日期、倒退 latest-day 指针或重抓全部历史混入该路径。`portal-extended-locales-source.yml` 另接收成功的 **Recover report article delivery** 完成事件；也可在 `main` 手动填写 `recovered_publication_run_id`，指定已经完成的独立恢复运行。空输入仍走原有最新日准入。

`portal_extended_recovered_admission.py` 先认证同仓库、公开仓库、main、精确 run/attempt/SHA，以及 `generate`、`deliver`、`publish` 三个成功任务。仅下载该运行的 `recovered-publication-request-{run}` 和 `recovered-publication-state-{run}` 两份非正文制品；要求 state 为 `complete`、request 哈希和篇数一致、成功 Neutral release 包含已提交 Blog archive commit。未完成生成、仅提交 archive、仅 dispatch 发布或未验证线上正文，均不能得到来源准入。

采集集合严格等于 request 中的 canonical Blog URL（1–500 页，同一内容日），逐篇从同一 HTTP 响应验证完整正文与引用摘要，再抽取翻译 corpus。URL 日期与页面自身 JSON-LD 发布日期必须一致；前后 edge release 身份必须稳定。publication request/state、来源正文哈希、原始 HTML 哈希、corpus generation 和真实 capture day 组成不可变私有证明。准入输出只有日期、计数、hash、状态和 release identity，不上传正文或模型响应到 Actions artifacts。

该证明使用 `accepted-recovered-blog-cohort-v1` / admission schema 3。历史批次存放在独立、最多32项的 `incremental/recovered-source-cohorts/queue.json`，普通最新日队列不被修改；同一天的两个恢复批次均保留。请求哈希对应的不可变 claim 使重复事件成为无写入复用；即使最终 claim 写入中断，也从已验证队列恢复原 admission。完整 immutable corpus 和证明读回成功后才写队列指针。队列满时显式停止，不清除未完成来源。

消费者合并读取两种已准入队列，仍使用现有 URL＋`content_key` 完成账本、每语言独立游标、每批最多24页、原 continuation 和 quality-debt 门禁。恢复来源没有新模型入口，也不重置任何完成/欠账记录。来源准入沿用 `extended-locales-source-admission` 锁；所有翻译继续进入 `extended-locales-r2-pipeline` 全局锁和 `max-parallel: 2`。本轮已持久化的页数确实推进后，只要任一已准入批次仍有待办，便继续下一批；没有进展不会自行反复 dispatch。

这一路径覆盖现有33种非英语扩展阅读页。ko/ja/ar 继续由 Neutral 自身流程处理；English 仍是独立 KC commentary 契约，其历史 cohort 是否已精确入队需要单独证明，此修复不会把源文章全文塞进英文评论队列。各语言仍须逐项通过 translation-ready、既有发布允许列表、handoff、review 和实际公共页面验收，不能从中文发布成功推断所有语种完成。

261007 的 `xhs_notes` 按既有日期规则形成2026-10-08 Blog。实际待恢复的文章数量应取其已验收 publication request，而非硬编码44；如存在既定内容排除，生成44篇、微信接受数＋排除数、公开 Blog 数必须分别记录。此入口的本地合成回归不代表该真实批次已发布或已进入33语种队列；真实准入必须等恢复运行产生成功的 publication state 后再验收。

## 已完成的回归与待完成的云端验收

本轮英文发布、UI、评论与 pipeline 共 92 个测试通过；新增语言相关 260 个测试通过，其中 1 个既有 opt-in 测试未启用。测试覆盖实际资产物化差异、旧坏缓存/跨代 seed、原文嵌入、字段长度、精确数量、私有正文隔离以及跨日队列。它们证明本地修复契约，不代替云端模型输出与正式发布验收。

后续验收须依次记录：

1. 修复合入的默认分支 SHA、真实 Actions 检查；
2. 原英文 generation 的恢复结果，确认剩余失败页面通过原有严格门禁，已完成单元复用；
3. 33 个新增目标的完整矩阵、逐语种页数、fallback 和实际剩余队列；
4. handoff、未激活目录、英文/非英文 review、正式切换的同一发布身份；
5. 公共语言集合、各语种最新源日期、实际页面/评论接口与旧已发布内容继承。

仓库仅保留公开运行链接、计数、错误类别和合成测试。source、checkpoint、候选原文、完整评论、模型响应及其私有读取证据不进入本文件或公开 artifact。

## 历史取证：2026-09-25 首批修复

以下是旧轮次的证据，保留用于追溯，不能代表 2026-10-10 的现状或待办：

- 当时 main 为 `681eae64969bfe2c39aa802dc7d4f4e7eadb5424`，保留 PR #182 的 `e3992f1d335939633ee30b12b2c8020d0239e1c6` 改动。既有生产 `36064006057` 成功。
- 旧严格候选：Hindi `36063797431` 为 0/24；繁体中文 `36068010264` 为 0/24；法语 `36069389027` 为 1/24、预算到期。它们均不是成功发布。
- 该法语固定 generation 为 `f334aac3023978818d18a4d28ed16cb2541a7b9b6ea803021f1fcd0502c812aa`；恢复 checkpoint `8f7adda70f3265a9a417a995747a4fa297150368c8c9ba42ca9c8736e297f351`（50,868 字节），保存为 `cba1d08b0c9ef8dd1ec2396874b0ef94e17d86b31c4ff3f68094c34819a3036c`（81,992 字节）。
- 当轮去掉重复外层重试，以精确源文回退使剩余单元继续；后来范围明确收敛为当天新增，预算从当时 2,400 秒调整为当前 14,400 秒。此前固定历史 generation 不作为新的日常 admission 继续扩展。
- 当时英文被排除在阅读页矩阵外，且没有本轮所述的独立评论发布器；该旧限制仍适用于“英文全文镜像”，不能误读为今天完全没有英文评论链条。


## 33 语言旧质量欠账的自动有界准入

原质量欠账版本只保存 rendered-complete 与 translation-ready 的区别，普通 pending=0 时不会自动启动模型；旧法语人工修复是当时唯一精确重译入口。后续 `extended-quality-debt-v1` 将相同引擎推广至 33 个明确登记的非英文目标，保留旧策略、旧 ledger 和原 source，增加可验证、每次 1..20 单元的自动准入。所有数字规则继续使用[共用数量契约](financial-quantity-translation.md)，完整机制见[质量欠账恢复](extended-locale-quality-recovery.md)。

已明确的拒绝输出多数未保存，不能假装对旧失败文本做零模型复验；只有实际存在、当前校验通过的 adapter cache 或完整 accepted ledger 可零推理恢复。未知 started、terminal、坏缓存、缺少原 immutable snapshot 均有明确阻断。质量债与普通文章按语言交替，完整历史结果的 ACK 不再丢失修复 proof 定位，原双 worker 和完整页/原文绑定保持。

现有真实旧批的 fallback 计数仅为待恢复证据。新机制需先在 GitHub CI、真实原 source 的逐语言有界恢复、fallback下降/translation-ready、handoff 和线上发布逐步验收；不能以这里的实现或离线测试代替生产结果。旧已修复且已 ACK、又没有完整 reverse anchor 的记录不能从裸 snapshot 猜回，保留 typed blocker 等待精确证据。被新版数量校验判为无效的旧 accepted 行仍 fail closed，不通过清空缓存或篡改 metadata 宣称完成。
