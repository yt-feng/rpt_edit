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

- 中文目录恢复生产 [38036944110](https://github.com/yt-feng/rpt_edit/actions/runs/38036944110) 后，[source admission 38043173198](https://github.com/yt-feng/rpt_edit/actions/runs/38043173198) 成功。新 R2 run [38043249029](https://github.com/yt-feng/rpt_edit/actions/runs/38043249029) 取证时为 pending。
- 旧矩阵持有者 [38030674044](https://github.com/yt-feng/rpt_edit/actions/runs/38030674044) 的总状态显示 queued，但 job 明细已经完成 6/34 个 locale job，其他语言仍运行/排队。它不是“CPU 完全未启动”，新 workflow 也不能绕过这个互斥组。
- 该 source 摘要中，33 个非英文目标各有 83 个 pending，选 24 个、余 59 个；英文有 81 个 pending，选 24 个。数字是各自语言队列，不应合并成不重复的源文章数量。
- [英文 job 114151900663](https://github.com/yt-feng/rpt_edit/actions/runs/38030674044/job/114151900663) 完成后失败：22/24 个页面完成，62 次调用、0 次 Memo 命中；错误各为 `expansion-validation` 1、`offline-quantity-validation` 1，没有预算耗尽。
- [法语 job 114151900697](https://github.com/yt-feng/rpt_edit/actions/runs/38030674044/job/114151900697) 的候选为 24/24，但 `translation_complete=false`：100 个原文回退单元、104 次使用，原因均为 `offline-quantity-validation`；315 次调用、403 次缓存命中。该候选可恢复和审核，不代表全部内容已译成法语。

## 已正式发布的语言覆盖与时效边界

生产 [38036944110](https://github.com/yt-feng/rpt_edit/actions/runs/38036944110) 在 2026-10-10 09:56:35 UTC 的线上审计通过，发布 ID 为 `c1c0b923210a207614c8d59ad1e12a5c`，与随后读取的 edge state 和下载服务 runtime release 一致。

- 33 个新增非英文语言：首页全部 HTTP 200，每语言两个确定性深页样本全部 HTTP 200。sitemap 页面计数为 `km` 79，其余 32 语言各 33；计数不等于成功翻译单元数量。
- 既有 `ko/ja/ar`：首页、深页和 sitemap 均 HTTP 200；候选字节、canonical、lang 与路由/资产检查通过。
- 中文加上述 36 个非中文语言具备已发布页面证据，共 37 个语言/变体；英文当次 `ENGLISH_READY=false`，assembly `ready=false,page_count=0`，不能计作英文评论已上线。
- 新增语言审计从 sitemap 深页字典序首尾取样，Blog 样本分别为 2026-09-26 与 2026-10-06。它证明已发布 Blog URL 的日期边界到 10 月 6 日，不证明中间每天齐全，也不能证明 10 月 8–9 日中文新增已同步翻译发布。

这次线上证据未给出 active release 每语种的源文回退统计，不能声称全部页面均已完整翻译。后续恢复还须证明新日期进入正式发布、英文评论可读、回退数与旧已发布集合正确；不能把 38 个登记代码、34 个矩阵 job 或单语 24/24 候选写成“38 语种正常且最新”。

## 本轮修复的确定性失败类别

### 1. 英文审核取错资源版本

此前 [生产 run 37785895519](https://github.com/yt-feng/rpt_edit/actions/runs/37785895519) 的 `english_daily_review` 在精确预览投影门禁失败。prepare job 已物化部署配置，fresh review checkout 的 `app.js` 尚未物化；两者生成的 `?v=` 资产 token 不同，导致合法预览 HTML 也被判成 `Prepared English public HTML is not a preview-only projection`。

修复后，英文 compose 从**最终未激活目录的资产字节**计算版本，review 从固定上传 manifest 取同一 SHA 重建 HTML，并有界读回全部 7 项实际资产核对长度与内容 SHA。仍然精确核对预览投影，不忽略脚本 URL、HTML 差异或私有正文。回归覆盖不同部署配置、fresh reviewer 不存在本地资产、渲染后资产被篡改、固定 manifest 后任一资产被改写或删除、缺失资产及隐藏私有正文。

### 2. 英文严格校验发生在 checkpoint 写入之后

共享 Memo 的普通阅读页校验允许少量机构名汉字，而英文评论要求完全不含中日韩残留、原文链接或过长标题。旧实现先保存 Memo，之后才由英文外层拒绝；下次恢复重复命中同一个坏单元，即使有可用的新译文也不重新调用模型。

离线复现表现为首次失败、第二次仍失败，第二次 0 次模型调用、2 次缓存命中。修复把英文内容门禁移入 Memo 写入/复用之前；旧坏 checkpoint 或 seed 只剔除对应精确单元，并清理该单元的模型缓存。合格单元继续复用，坏响应不写候选、正文或成功缓存。

新增固定错误码区分 `english-language-validation`、`english-asset-validation`、`english-size-validation`，不输出原始异常正文。旧 `expansion-validation` 候选仍可只读检查和恢复。该缺陷是已复现的恢复阻塞类别，不能仅凭当前云端一个通用错误码就断定它解释了所有英文失败。

### 3. 数量门禁保留严格等价

当前英文数量诊断显示源有 `27`，响应有 `27` 与 `11`。对源文本 SHA 及最终模型输入 SHA 的精确绑定确认，其中额外记号来自“双十一”的英文活动名称表达。此类修复必须识别同一购物活动的等价值，不能删除未知数字或跳过数量校验；其它新增、遗漏、改写金额、日期和比例仍应被拒绝。

数量修复由共用 financial quantity validator 及其合成回归覆盖。该英文诊断不能推断法语全部 100 个回退都属于同一原因；各语种还需按固定源、校验错误及恢复后的结果分别核对。恢复使用当前合法 checkpoint，不清空所有合格译文，不重新抓取或改写来源 generation。

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

- 当时 main 为 `681eae64969bfe2c39aa802dc7d4f4e7eadb5424`，保留 PR #182 的 `e3992f1d335939633ee30b12b2c8020d0239e1c6` 改动。既有生产 [36064006057](https://github.com/yt-feng/rpt_edit/actions/runs/36064006057) 成功。
- 旧严格候选：Hindi [36063797431](https://github.com/yt-feng/rpt_edit/actions/runs/36063797431) 为 0/24；繁体中文 [36068010264](https://github.com/yt-feng/rpt_edit/actions/runs/36068010264) 为 0/24；法语 [36069389027](https://github.com/yt-feng/rpt_edit/actions/runs/36069389027) 为 1/24、预算到期。它们均不是成功发布。
- 该法语固定 generation 为 `f334aac3023978818d18a4d28ed16cb2541a7b9b6ea803021f1fcd0502c812aa`；恢复 checkpoint `8f7adda70f3265a9a417a995747a4fa297150368c8c9ba42ca9c8736e297f351`（50,868 字节），保存为 `cba1d08b0c9ef8dd1ec2396874b0ef94e17d86b31c4ff3f68094c34819a3036c`（81,992 字节）。
- 当轮去掉重复外层重试，以精确源文回退使剩余单元继续；后来范围明确收敛为当天新增，预算从当时 2,400 秒调整为当前 14,400 秒。此前固定历史 generation 不作为新的日常 admission 继续扩展。
- 当时英文被排除在阅读页矩阵外，且没有本轮所述的独立评论发布器；该旧限制仍适用于“英文全文镜像”，不能误读为今天完全没有英文评论链条。
