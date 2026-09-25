# 多语言架构核对与本轮修正（2026-09-25）

## 结论

新增语种卡住的主要原因不是 R2 权限、Actions 没有 CPU，或模型只支持
日/韩/阿语，而是两条管线的处理和发布口径不一致。日/韩/阿语允许
翻译失败单元保留原文；新增管线先前遇到一个失败字段就放弃整页，并要求
24 页全部完成才能产生可审批候选。不断换语言、重跑同一失败批次不能解决这个差异。

用户本轮明确接受以 SEO/GEO 发布为目的的翻译质量，现将新增管线也接入
`--allow-source-fallback`：失败单元精确保留原文，后续单元继续处理。
仍然使用固定 Hy-MT2、公共 Linux CPU runner；没有付费兜底。

## 两条现有路径

| 环节 | 中文与日/韩/阿语 | 34 个新增目标 |
| --- | --- | --- |
| 中文源 | 构建当次 `_neutral_site`，目录、Blog、公开数据与应用页面 | 从公开 canonical 页面采集一批 24 页，固定 corpus generation |
| 取词 | `build_portal_locales.py` 的 DOM 文本节点、元数据、JSON-LD、目录字段等 | `PublicParser` 抽取标题、摘要、HTML 文本块、相关链接标签 |
| 页面形态 | 保留原应用布局与功能，通过 locale assets/data overlays 本地化 | 独立静态阅读页，原报告、会员、图表访问回到中文源页面 |
| 翻译 | 去重文本单元 → Hy-MT2 → 持久缓存 | 去重文本字段 → 同一 Hy-MT2 → R2 checkpoint |
| 单元失败 | 生产参数已经启用 `--allow-source-fallback` | 本轮改为相同原文回退；默认 CLI 严格模式仍可用于诊断 |
| 预算 | 当次增量、历史 cohort、已发布历史状态分开管理 | 每 locale 1..2400 秒，24 页，matrix 最大并发 2 |
| 发布 | 未激活目录 → 校验 → 审批 → 原子切换 → 线上验收/回滚 | 私有完整候选 → 恢复/组装 → 同一生产流程；还有下述集成缺口 |

新增目标由 `compare_hymt_translation.LANGUAGES` / `portal_extended_locales.ADDITIONAL`
登记。38 个语言/变体减去中文、日语、韩语、阿语得到 34 个目标；登记可用不等于已上线。
新增阅读页没有将会员应用复制成 34 套；这与“为公开内容提供 SEO/GEO 阅读入口”的范围相符。

## 具体失败原因

1. **页面与文本单元耦合。** 原 `translate_document()` 的第一处异常会退出本页。
   多页共用的一个标题/链接失败，会挡住多页后续文本。现在内容校验失败只回退该单元。
2. **重试叠加。** 模型有三次尝试，外层还有一次重试，多个页面又会反复触发同一源文本。
   本轮新增回退模式每单元只做一次模型尝试；精确源文本、语言和 policy 绑定的
   回退记录单独持久化，重复页面和续跑直接复用。严格模式也去掉了外层重复重试。
3. **颗粒度不同。** 原管线处理 DOM 文本节点；新增抽取会将列表内的报告标题和机构文字
   拼成一块。例如当前公开页中可见 `...-260923Goldman Sachs · 高盛`。
   新增构建器还曾按所有逗号/分号再拆句，破坏上下文。本轮移除该拆句；结构性 `|`
   仍在模型外保留，长文继续使用共用模型适配器的句末分段。DOM 抽取层尚未改成原应用的
   完整字段清单；当前固定 corpus 不会在续跑时重新抓取。
4. **校验与语种不完全匹配。** `zh-Hant` 的汉字与简体可能相同，通用“原文未翻译”规则会
   拒绝部分合法同文；数量识别也不覆盖全部语言写法。允许回退后这类内容不再整页失败。
   本轮没有以关闭金额/日期校验来接受错误模型输出。
5. **结构错误进入外层才被发现。** 模型会在纯文本标题中添加 `|`；原适配器只在 Markdown
   模式校验结构，外层才发现并失败。本轮将 pipe 检查移到适配器缓存之前。
6. **生产组装的确定性错误。** `existing_locales=('ko','ja','ar')` 曾调用仅接受新增语种的
   `locale_url()`，必然抛错。本轮修复为只纳入实际存在、自 canonical 正确且可索引的旧语言页；
   缺失或 noindex 的旧语言页不会被虚构成 hreflang。
7. **此前“第二条任务排队”不是 CPU 卡住。** workflow 有全局互斥组；`max-parallel: 2` 只对
   同一 workflow 的 locale matrix 生效。另发一个 workflow 会等待前一条结束。

## 本轮实现后的数据口径

```text
固定 R2 corpus
  → 每个标题/摘要/正文块/链接标签
      → 已验收译文：复用 checkpoint.rows
      → 已记录回退：复用 checkpoint.source_fallbacks 中绑定的原文
      → 尚未处理：Hy-MT2 一次 → 合格译文或精确原文回退
  → 完整 24 页候选（仍 noindex）
  → R2 manifest / ready receipt
  → 源版本匹配 + 正常审批后才进入生产切换
```

`complete-candidate` 表示页面集合完整、可进入审批，不表示所有单元都翻译成功。
清单新增 `translation_complete`、`translation_policy`、`source_fallback_unit_count`、
`source_fallback_occurrences` 与固定枚举原因。被拒绝的模型响应不会写进 checkpoint 或页面。
原文回退与合格译文分开保存；严格模式不会把回退记录当成译文。
预算到期仍为未完成并持久化检查点；模型缺失、权限/存储错误、损坏的 source/candidate 仍是异常。
预算也传到模型请求，避免临近预算结束时启动额外的长重试。

## 发布集成仍待完成的事项

- **固定源必须与发布树同源。** 当前候选从线上抓取，而 `neutral-edge-cutover.yml` 会重建
  新的中文目录。组装器比较每页原始 HTML SHA；更新日期、目录内容或 head 改动都会导致不匹配。
  应在同一未激活树上冻结 source，再恢复候选组装；不能去掉 SHA 校验接受旧版本。
- **旧镜像构建与新增组装的顺序。** 目前 extended assembly 在 ko/ja/ar locale build 之前，
  后者会改写根页 alternate。应在最终旧镜像树上统一合并 alternate，并验证互相引用。
- **后续批次保留。** 当前 assembler 只接受新目录与同一 generation 的完整批准集合；
  普通生产刷新也未从 active release 继承已批准新增语言。还需要持久化批准集合、继承旧页面、
  对新变化生成候选，并合并 sitemap/hreflang。
- **历史游标。** 当前 collector 有 500 页硬上限与稳定排序，但尚无跨批次持久游标。
  现有“24 页首批”不能被描述成已覆盖全档案。

这些事项与翻译容错是不同层次的问题；本轮 Action 只生成候选，不声称完成上线。

## 已核对证据与停止点

- 核对时 main：`681eae64969bfe2c39aa802dc7d4f4e7eadb5424`；已合入隔离开发分支，保留
  PR #182 的 `e3992f1d335939633ee30b12b2c8020d0239e1c6` 修改。
- 现有生产 `36064006057`：成功；源码 `681eae64969bfe2c39aa802dc7d4f4e7eadb5424`。
- 旧严格候选：`hi 36063797431` 为 `0/24`；`zh-Hant 36068010264` 为 `0/24`；
  `fr 36069389027` 为 `1/24`、预算到期。均非成功发布。
- 法语 run 恢复 R2 checkpoint SHA `8f7adda70f3265a9a417a995747a4fa297150368c8c9ba42ca9c8736e297f351`
  （50,868 字节），保存为 `cba1d08b0c9ef8dd1ec2396874b0ef94e17d86b31c4ff3f68094c34819a3036c`
  （81,992 字节）。源 generation 不变：
  `f334aac3023978818d18a4d28ed16cb2541a7b9b6ea803021f1fcd0502c812aa`。
- 本轮使用已有固定 source / checkpoint，英文首批 24 页、2400 秒，显式开启原文回退。
  提交、触发 Actions 后停止。用户已要求不持续监控；不设置后台轮询或自动监控。

相关源码：`build_portal_locales.py`、`portal_extended_locales.py`、
`build_portal_extended_locales.py`、`hymt_offline_translation.py`、
`assemble_portal_extended_locales.py` 与两个 release/candidate workflows。
