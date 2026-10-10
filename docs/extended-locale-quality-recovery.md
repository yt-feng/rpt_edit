# 扩展语言质量欠账的有界恢复

本契约覆盖登记的全部 33 个 `all-supported` 非英文静态阅读目标；`en`、中文源站和 `ko/ja/ar` 使用各自既有流程。总范围和发布阶段见[主架构](portal-multilingual-architecture.md)，数量规则见[数字翻译契约](financial-quantity-translation.md)。代码以 `portal_extended_quality_recovery.py`、`portal_extended_repair_contract.py`、既有法语 `RepairEngine/RepairPipeline` 为入口。

## 固定身份与界限

`extended-quality-debt-v1` 的当前 validator 修订为 `cldr48-complete-number-v1`。每个 source job、每种语言最多扫描 4 个既有 debt generation、每 generation 最多 60 个 fallback 单元，从中选 1..20 个；generation 和 unit 均有有界持久轮转，前面的 terminal/blocked 项不能永远遮住后面的债。每个候选仍为原固定 1..24 页，不重新抓取来源。source 阶段的 tail 与债扫描共享 5 分钟 monotonic 准入期限、1200 次 R2 HEAD/GET 和 16 次 GitHub GET 上限；缓存 API 响应仅限同一 source job。小型 scheduler cursor 的控制读写，以及至多 33 语言、每语言 3 个小型 active/plan/prepared-pointer 控制对象的尾部预留清单单独有界；不读取 source、页或 unit ledger，用于确保预算耗尽也能写回位置并阻止同语言普通 Memo 越过未完 tail。期限在请求之间检查，已进入的 SDK 调用仍受既有超时/重试配置约束；整个 source job 保留原 20 分钟硬上限。耗尽后保留已选计划和 locale/generation 游标，普通当前日路径继续，预算停止本身不算进展也不触发自续。原全局 `extended-locales-r2-pipeline` 串行组、`cancel-in-progress=false` 和最多 2 个 CPU job 保持。

债 proof 必须逐字节绑定 locale、source、candidate、manifest；原 immutable origin、原 source 和 locale job 必须有精确 producer/run/attempt/SHA 且实际完成成功。已注册 complete row 必须仍匹配原快照。已 ACK 的行优先通过绑定 quality proof SHA 的 reverse anchor 找回完整 immutable outcome（包括 repair/completion）；没有 anchor 的普通旧行仅枚举合法 continuation 计数 0..3，必须存在唯一、逐字节相等的 immutable result。零个或多个匹配、旧已修复行缺 anchor、较新页面 receipt、坏源/缓存等保留 typed blocker；不能重新 fetch 或自行扩大历史准入。

## 缓存、调用与未知结果

源文回退只保存原文和错误类别，已拒绝响应通常被丢弃。可零推理恢复的证据仅为实际存在且通过当前质量门的 adapter cache，或完整 accepted unit ledger。源计划显式记录每个单元是 accepted-ledger 复用还是 fresh-authorized；全部属于前者时 `requires_engine=false`，restore 将该字段传至 workflow，模型 setup 跳过，build 使用禁止推理的实现且不构造 adapter。

需要处理新单元时，先用独立 adapter 的禁止 engine factory 读取真实 cache；现存 JSON/身份/结构/数量错误不会被当作缺文件。只有明确 cache miss 才使用计划已经授权的离线推理，每个单元一个质量尝试。模型的单元可由多个片段构成，所以 unit attempts 与实际片段数不是同一个计数。没有任何付费 provider fallback。

原子 started 写入并精确读回后才可处理单元；accepted/terminal outcome 不覆盖。自动 ledger 的 namespace 不随 validator revision 改变，旧 revision claim 不兼容时 fail closed；法语还显式读取旧 `fr-space-grouping-quarter-v1` ledger。旧 unknown started/terminal 不因新策略重新尝试，旧 accepted 必须通过当前质量校验才迁移。批次对全部选中单元预检，再启动任何新工作。缓存损坏或未知结果保留 started，待明确诊断，不自动重放。

## 完整候选、写入尾部与发布

新 accepted rows 仅替换选中的原 fallback。完整候选用 ForbiddenTranslator 从固定 checkpoint 重建，模型调用为零；未选中的译文、fallback、页面覆盖、原 source/origin/continuation 计数不变。合并最新 Memo 只触及确切已接受 keys，拒绝覆盖较新冲突值。新 immutable checkpoint/candidate/proof 先写，随后更新 generation pointer、Memo、完成页面和完整 queue row、quality proof/debt。

prepared tail 中断可从同一 proof 只完成原精确 before/after 写入。source-only completion 绑定完成尾部的新 producer；active marker 保留到实际已完成的 source/locale job 被精确验真，不能因 source 脚本中途成功就提前清除。普通 source 后续失败时，下个串行 run 可再次零推理补齐并绑定成功 source。无法验证的 tail 留下 typed blocker，不覆盖较新内容。预算在 queue-after、completion 前后任一写边界中断时，该语言继续保留 lane，完成尾部前本轮普通页和质量修复均不会改它的 Memo；没有 prepared proof 的 unknown unit 不占这个预留位置，其他语言照常推进。

自动 handoff 支持每种 locale 的精确 repair/completion proof，但仍只接受 translation-ready、零 fallback、完整且无 budget/failure 的新候选。已有活动 fallback 页及批准 ledger 保留原契约。源正文变化继续阻止旧译文改绑；修复数字识别不会以 metadata 让历史 accepted 行自动合格。

## 公平推进与摘要

已有 incomplete 普通页继续原 claim/续跑流程。对没有进行中页任务的语言，quality 与确实存在的 ordinary 待办交替，每个语言每轮只有一个 matrix row。空 ordinary 轮次不占位置。quality 只有已经提交、完整验证的新 accepted-unit delta 才可续发；当前 generation 完成后可推进同语言其它债或新文章。普通页最后一轮取得实际 durable 进展后，也可交给一次有界 debt scan。若扫描只遇 terminal/unknown/blocked，零 accepted 进展就停止自续。

摘要分开记录 selected、新 accepted、仍 fallback 的 terminal、unknown/blocked、accepted-ledger/cache-only 复用和 fresh inference unit attempts。source-only tail 本轮 fresh count 为 0，不借用旧 producer 的调用数。无阶段表示 paid provider 调用，均为 0。

## 验收边界

本地回归使用真实两页/两 fallback 的 render/checkpoint/R2 契约、原子 fake R2 及合成 translator，覆盖整批/部分恢复、缓存零推理、单元终止与未知、旧 revision 桥接、ACK 前 anchor 和唯一旧结果恢复、producer/locale/源/完整 row 篡改、断点尾部、当前日公平及进展续跑。workflow 测试实际执行 shell 路由，并检查空 needs-model 不触发 setup。

这些是机制验收。真实运行仍需依次核对原 source 的 fallback 减少、各语言 translation-ready、保护审核、正式发布和公共 URL；旧运行仍使用自己的旧提交，不能仅因新代码合并就算已恢复。
