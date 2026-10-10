# 历史已发布文章的多语种准入

## 自动入口与队列锁

`portal-extended-locales-source.yml` 监听 Neutral edge、独立 Recover report article delivery，以及 Daily report articles and translations 的完成事件。普通 Neutral 成功事件继续冻结当前最新发布日；Daily 或独立恢复事件只处理该运行的精确发布回执。Daily 的 chart 等兄弟 job 失败不会掩盖已完成的文章发布链。

workflow 不持全局锁。`capture` job 先把自包含候选记录写入私有 R2，再认证并冻结小型 publication request/state、caller/run/attempt/head、实际 job 身份与 artifact 摘要。只有后续 `source_snapshot` job 持 `extended-locales-source-admission` 锁，串行写入普通日队列和历史 cohort 队列。GitHub 替换等待中的 writer 时，已捕获的记录仍可由下一个 writer 枚举，不能只处理本次事件。

候选记录不授予准入。完整捕获必须满足：

- public 同仓库、main、固定 workflow path；独立恢复仅接受 workflow_dispatch + success，Daily 接受 schedule/workflow_dispatch + completed success/failure/timed_out。
- 最多 10 个确切 attempt，完整分页 job 清单；`deliver-recovered-report-articles / generate`、`/ deliver`、`/ publish` 三个完整名称各自最近实际执行都成功，run/head 一致。不能使用后缀匹配。
- request 来自实际 deliver job 的上传时间窗，state 来自实际 publish job 的上传时间窗；两份 artifact 的身份、大小、解析后 canonical JSON 摘要与内容对应。读取前后 run/attempt 必须保持一致。
- publication request/state 仍沿用既有严格 schema；state 为 complete，记录数与 request 匹配；Neutral release 已成功且包含 archive commit。Daily caller 的扩展信息只存在新 ingress envelope，不能混入旧 publication/proof/queue schema。

Daily 真实运行 `37996300746` 已观察到父 job `deliver-recovered-report-articles` 明确 skipped。实际执行的三个嵌套全名目前按 caller key 与 callee job ID 严格约束，**首个真实 Daily 嵌套交付事件仍需验收**；未知名称不能当作无工作清除。

## 私有持久记录与中断恢复

事件身份只由 repository、caller path、run ID 和 attempt 确定；head/event/conclusion 是该身份下不可变的被验证内容。同一身份出现不同内容，保留阻断。

第一笔写入即为可枚举的自包含 `publication-ingress/pending/<event hash>/<envelope hash>.json`。认证成功后，第二份完整 envelope 仍写同一 pending namespace，因此 hint 写后中断、完整回执写后回读未知都不会形成不可发现的窗口。重复捕获同一事件使用相同 canonical 字节，不写当前捕获者的 run ID 或时间戳。原 Actions artifact 后来被新 attempt 覆盖或删除时，完整冻结的 request/state 和身份仍可用于接续；仅有旧 hint 时不得偷用新 attempt 的 artifact。

全局 writer 每次完整枚举最多 1,024 个 pending 对象，分页必须闭合；超界或不完整返回明确阻断，保留原对象，不宣告已处理干净。每轮最多处理 8 个事件、20 分钟；同一单调时钟预算从首次 listing 前开始，覆盖所有 R2 list/head/get/body-read/put/delete 前后、turn 读取及 live 收集，超时后不启动下一步事务，已写对象保留接续。底层单次请求继续受既有有限 transport 超时/重试上限约束。已有 turn 记录只用于轮换暂时失败的事件，不能作为 ACK 或永久跳过游标。历史队列仍最多 32 个未完成 cohort，满额时保留 pending。

串行准入只获取 request 中的精确 URL，并在同次 HTTP 响应上核对正文摘要、标题允许摘要、canonical、发布日期与 corpus；收集前后 public release 必须稳定。原始来源与 proof 存私有 R2，日志只输出固定计数、类别和摘要。

新 admission 写入期间，当前 producer workflow 尚未整体成功，因此**不生成最终 ACK，不删除 pending**。后续一次事件触发会读取原 producer 的精确 `/attempts/<attempt>` 运行记录，验证该 attempt 的整体 success 与唯一 `source_snapshot` job 的身份、success 和日期，再完成以下顺序：

1. 回读并核验 immutable admission、source corpus、publication proof 和 request claim。
2. 归档完整 envelope，写入绑定 event/envelope/request/admission 的最终 ACK，并回读验证。
3. 删除已确认的 pending 指针。

若原 producer 已 completed 非 success，只有精确 live source 重验且 corpus generation 不变后，才串行创建新 immutable admission，原位置替换历史队列 pointer，最后更新 request claim；旧 source/proof/receipt 保持不变，新 pending 等待新 producer 成功。queue 写入后 claim 未写的中断按实际队列恢复，不会永远复用失败 producer。若旧失败 producer 的 queue 条目已被正常 completed 去重清理，只有该 corpus 对全部 33 语种均无待处理 content-key 时，才允许重建 producer receipt/claim 而不重新入队；依旧等待新 producer 的实际 success 才最终 ACK。任一语种仍待办而 queue 缺失时保持阻断。已成功的原 attempt 不因后续 attempt 失败而失效。ACK 后清理失败只复核已成功的原 producer attempt 与持久证明并清理，不再生成文章、上传微信或重新绑定到 cleanup job。

没有发布文章仅在已成功的空 publication receipt，或完整 exact-attempt 证据明确父 job skipped / 全部嵌套 job skipped 且无任何 publication artifact 时才终结。先前 attempt 有实际嵌套执行、缺失 job 身份、任何 publication artifact 存在但验证失败、分页/API/附件读取未知、run attempt 改变，均保留待处理。

## 无新事件时的有界唤醒

独立 `portal-extended-source-wakeup.yml` 每小时 UTC 第 17 分运行；它不在 source 或 locale consumer 的 workflow_run 监听名单中，避免空任务替换有用的待运行消费者。它只执行一次最多一个对象的 pending 列表读取；空队列零写入、零 dispatch、零模型调用。

有 pending 时，在独立 wake 锁下先持久化并回读当个 UTC 小时的 reservation，再最多一次 dispatch 既有 source workflow 的 main，输入 `reconcile_only=true`。因此真实 admission producer 仍是旧 reader 支持的 workflow_dispatch；该输入跳过 latest-day 抓取，仅执行串行 pending 接续。写入或 POST 结果未知时同小时不立即重发；下个小时先重新检查 pending 再允许一次唤醒。若 reservation 写后、POST 前中断，只延迟到下一小时，不丢候选。wake 不发送文章、不触发付费模型、不递归监听自身。

source 尚在运行时保留的 pending、最终 ACK 后清理失败，或最后一个 writer 被取消，都不再依赖以后恰好出现新的外部发布事件才能继续。分页、存储或身份超界仍保留明确阻断，而不是宣告成功。

## 消费者兼容与边界

沿用 schema v3 admission、原 recovered publication/proof 和 request-hash claim；正常最新日队列不被历史 cohort 覆盖，同日不同 cohort 可并存。兼容测试实际执行 main #335 原 `checked_publication`、`validate_proof`、`read_proof` 和 `read_admission` 函数，验证新 Daily 准入与失败 producer 重绑定的产物。

33 个扩展阅读语种继续使用既有不可变 corpus、每批最多 24 页、全局最多 2 个离线 CPU 翻译任务，以及原质量/发布门禁。这里不增加模型调用，不重新发送微信，不改变标题或正文生成预算。English 历史 commentary 与 ko/ja/ar 的既有发布合同未扩展；不能把本入口成功等同于全部语言已翻译或上线。

手动 `recovered_publication_run_id` 可以指定一个已完成 Daily 或独立恢复运行；留空沿正常最新日收集并接续所有耐久 pending。capture/reconcile 均在既有 source workflow 中执行，不需要新模型权限。仅旧 hint 而原 attempt 附件已不可恢复时，继续报告 pending，不能伪造出版证明。

## 验证与验收

离线回归覆盖 capture 每个写入窗口、相同事件幂等/冲突、跨 attempt artifact 时间窗、捕获后附件消失、A writer 被 B 替换、同日多 cohort、普通队列继承、32 cohort 上界、分页与预算轮换、旧 producer 取消、重绑定每笔写入中断、最终 ACK/清理未知，以及旧 reader 兼容。

本修复的云端检查、首个真实 Daily 嵌套事件冻结、既有历史 cohort 进入 locale queue、对应翻译与公开阅读页验收分别记录；本地回归通过不能替代这些生产回执。
