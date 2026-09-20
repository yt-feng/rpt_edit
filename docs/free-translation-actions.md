# GitHub Actions 离线翻译

更新：2026-09-20。生产候选已切至腾讯官方 `Hy-MT2-1.8B-GGUF` 的 Q8_0 权重，使用固定版本 `llama.cpp` 在 GitHub Actions CPU runner 推理。是否上线以生产适配器 preflight 的原文/译文人工复核及实际生产运行记录为准，不能把结构检查通过当作金融语义合格。

## 模型和运行机制

`hymt_translation_model_manifest.json` 固定 Hugging Face revision、GGUF SHA-256、上游 llama.cpp commit 和采样参数。模型为 Apache-2.0，运行时为 MIT；安装时保留许可证和来源审计记录。公共 Actions cache 只存模型及编译后的 CPU runtime；构建关闭 NATIVE，避免缓存要求另一台 runner 的特定指令集。

`setup-offline-translation` 安装并校验模型。推理进程只允许 Linux GitHub Actions；在 runner 内启动绑定 `127.0.0.1` 的 llama-server，Python 通过本机 HTTP 调用该进程。没有外部翻译 API 请求或自动付费补译。本机开发测试使用注入的假引擎，不下载或运行模型。

报告全文英译中、报告标题、网站静态韩/日/阿译文、兼容脚本中的英译字幕与视频标题走同一模型。中文或英文直接译出目标语言。生产入口 `offline_translation.py` 只导出 HyMT；保留的 M2M100/OPUS 比较代码不作为生产后备。

机构、咨询、ARK 以及混合 Dropbox 批次中的文章式中文导读属于编辑写作，仍保留 DeepSeek，并归入 `REPORT_NOTES` key / `report-article` 阶段。选报、普通报告微信正文、保留的知乎生成、必要内容改写和 Market Views 综合写作也仍可能付费。成功结果按各自缓存条件复用。已关闭的 podcast、视频、XHS/闲鱼自动流程不会因离线翻译而重新开启。

网站 Worker 的报告详情按需翻译是单独路径：缓存未命中的 POST 在配置 runtime key 时仍会调用 DeepSeek，默认每天最多 100 请求、10 万源字符；GET 轮询不触发模型。它没有迁入本次 Actions 批处理，也不在 Python token 账本内。因而“离线翻译无付费 API”只描述这些批处理步骤，不能解读为整个项目或账号零费用。完整 key/覆盖范围见 [DeepSeek usage accounting](deepseek-usage-accounting.md)。

## 文本与缓存

金额、单位、日期、同比关系和百分比留在完整自然句中。长段落仅在完整句末拆分；超长单句明确拒绝，保留原文。Markdown 链接目标、图片、代码及 HTML 作为不可修改内容保留；locale 使用原有 `__KC_PH_...__` 数据占位协议。输出校验占位符数量和结构，并对金额尺度、币种、日期、百分比与百分点做类型归一检查；它们不证明所有词义、比较对象或因果关系都正确。

韩文另使用小范围金融术语表保护毛利、营业利润、净利润及其利润率等概念。模型输入中的对应名词用占位符承载，译后恢复为固定术语；金额、谓语和句子关系仍由完整上下文翻译。这不是整句答案替换。按 GEO/SEO 用途，韩日措辞差异不阻挡发布，只保留数字、格式和占位符完整性检查。仅公开固定样本预检显式开启模型输入、原始输出及术语映射诊断，正常生产默认不记录正文。

| 内容 | 复用条件 | 保存位置 |
| --- | --- | --- |
| 目录标题 | 原标题精确匹配、目标/模型版本；发布种子另需唯一报告 ID | 既有公开 title cache，每条落盘 |
| 网站 locale | 源文、目标、提示及模型版本 | 既有 locale cache，逐批落盘 |
| 报告段落 | 精确源文 SHA-256、源/目标语言、固定模型和适配器版本 | 私有 R2 report-translation checkpoint |
| 微信编辑正文/文件名 | 完整提示、模型及编辑/标题优化版本 | 同上私有 R2 checkpoint |

旧 DeepSeek 已通过质量检查的译文保留来源并继续复用；不因换模型全量重翻。淘汰的离线模型结果不被冒充为新模型结果。报告正文不放进公开 Actions cache。Dropbox、机构、咨询和 ARK 四条生产报告链均恢复私有 checkpoint；恢复成功后的保存步骤使用 `always()`，错误后仍尝试保存已完成片段。Dropbox 翻译分片另有软超时，为上传留出时间；runner 硬中断仍可能阻止保存。

私有报告缓存当前覆盖同一 pipeline、同一天的跨运行恢复；不同日期/不同 pipeline 尚未全局合并。Dropbox 翻译再按分片独立保存，收齐后校验索引并合并。较早的正文生成阶段也有独立私有 checkpoint，以 PDF 内容哈希、分片成员、代码/提示和参数验证能否复用，并在复用后重新发布当次 handoff。详见 [generation checkpoint](private-generation-checkpoint.md)；[私有存储 smoke](private-checkpoint-smoke.md) 只测试合成内容的存取，不证明真实报告或翻译质量。

## 验证记录与限制

2026-09-12 的 PR #138 从未合并，因此旧免费翻译测试不能证明此前生产已切换。2026-09-20 的实模型对照 run `35497801759` 显示：M2M100 曾改变美元金额数量级、丢失句子和同比关系；OPUS 速度更快，但会把“营业利润率”译成 turnover rate、“毛利率”译成 Māori rate。两者均被排除出生产候选。

Hy-MT2 独立对照与 production adapter preflight 分开执行。后者直接覆盖自然英中/中英金融句、长段落、真实 locale 数字占位输入、Markdown 表格和链接，保存完整源文、模型实际输入及译文供人工检查。没有逐句硬编码答案或例句自动替换。候选不合格时保留已完成结果、报错并停止，不回退到付费服务。

免费 CPU 计算不等于无限吞吐；locale 采用增量缓存和一小时软窗口，报告任务分片并留 checkpoint 上传时间。实际吞吐须以新模型在 Actions 的每条样本时长及生产报告完成时间衡量。

参考：[腾讯官方模型](https://huggingface.co/tencent/Hy-MT2-1.8B-GGUF)、[llama.cpp](https://github.com/ggml-org/llama.cpp)、[GitHub Actions 计费规则](https://docs.github.com/en/billing/concepts/product-billing/github-actions)。
