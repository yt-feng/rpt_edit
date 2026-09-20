# GitHub Actions 离线翻译

实施更新：2026-09-20。本次将纯翻译入口切到固定版本 `facebook/m2m100_418M`，在 GitHub Actions 标准 CPU runner 上使用 CTranslate2 INT8 推理。模型缺失、数字变更或译文校验失败时保留已完成结果并报错，不调用 DeepSeek / DeepL 补译。

## 覆盖范围

- 报告全文英文 → 中文、中文报告目录标题、完整报告的文件名标题。
- 网站韩文、日文、阿拉伯文，直接从中文或英文译出，不先生成重复的英文中转版本。
- 兼容脚本中的字幕及中文 → 英文视频标题；日常 podcast / 视频生成流程另行关闭。
- 公共机构和咨询报告的微信文章是基于原报告的编辑改写，保留 DeepSeek。成功通过编辑检查的正文按完整提示词、系统提示词、模型及版本缓存。

CLI 只提供离线生产入口。旧付费 locale 诊断命令拒绝执行；历史低层函数保留用于兼容回归，不接入工作流。`requirements-translation.txt` 和模型 manifest 固定依赖、模型 revision、量化方式及许可证据。模型准备步骤可下载；后续 `HF_HUB_OFFLINE=1`、`TRANSFORMERS_OFFLINE=1`，推理本身没有 HTTP 请求。

## 去重与恢复

| 内容 | 复用规则 | 保存位置 |
| --- | --- | --- |
| 模型权重 | 固定 revision + 依赖/installer/manifest 哈希，校验文件 SHA-256 | Actions model cache，仅模型公开文件 |
| 中文目录标题 | 原标题精确匹配 + 模型/翻译版本；已发布种子另要求唯一报告 ID 与匹配原题 | 既有 public title cache，每成功一条即写入 |
| 多语言网站内容 | 规范化原文 + 目标语言 +版本；旧 DeepSeek 缓存通过源文/质量校验后复用并保留来源 | 既有 locale cache，逐批保存，失败不清空 |
| 报告段落 | 精确文本 SHA-256 + 源/目标语言 + 模型 revision/转换文件身份；同批相同文本只推理一次 | 私有 R2 `_workflow-cache/report-translation/v1/<pipeline>/<YYMMDD>.tar.gz` |
| 微信编辑正文 | 源文形成的完整 prompt + system prompt + 模型 + 编辑版本 | 同上私有缓存 |

四条生产报告链（Dropbox、公共机构、咨询、ARK）会先恢复私有缓存，无论本轮成功或失败都保存已完成内容。当前跨运行覆盖同一 pipeline、同一天的重跑；内容键可去重当天多个报告中的同文。不同日期、不同 pipeline 的独立存储尚未做全局合并。报告全文不写入公开 Actions cache。

所有语言共用一个模型实例，避免为每个语言对重复占用内存。单引擎批处理，长输入按完整覆盖切片；数字/百分比/链接/占位符/代码块和表格结构检查继续执行。Locale 单轮最多运行一小时并保存 checkpoint，未完成的候选不能切换上线。旧付费译文不因切换 provider 而被整批丢弃。

## 验证边界

2026-09-12 的旧分支曾完成 Actions 小样本推理（run `34677068121`），但 PR #138 未合并，因此那次结果不代表生产已经改为免费翻译。本次必须以新提交的 `Portal offline translation preflight` 实测及生产运行记录为准。

该 preflight 无付费 API secret，只执行固定公开样本：英译中、中译英、韩/日/阿 locale 以及包含数字、图表 URL、表格的 Markdown。JSON 产物保留源文与译文供语义审查。现金流例句有已审定术语修正，同时保留没有硬编码答案的同比下降、百分点、币种金额和日期例句；结构检查通过不能替代金融含义审查。

标准 GitHub-hosted runner 对公开仓库的适用计算时长按 GitHub 官方规则；离线翻译不产生按 token 收费的 API 请求。模型 cache 和产物保留三天审计证据，R2 使用项目现有私有桶。

参考：[M2M100 官方模型](https://huggingface.co/facebook/m2m100_418M)、[CTranslate2 转换](https://opennmt.net/CTranslate2/guides/transformers.html)、[GitHub Actions 计费](https://docs.github.com/en/billing/concepts/product-billing/github-actions)。
