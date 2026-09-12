# 免费离线翻译与 GitHub Actions 实施方案

核验日期：2026-09-12。目标是让项目的纯翻译流程改用开源模型在 GitHub Actions runner 内执行，取消 DeepSeek 翻译 API 调用，同时复用已经通过检查的译文。

## 选择：M2M100 在 runner 内离线运行

| 方案 | 当前官方说明 | 本项目选择 |
| --- | --- | --- |
| Argos Translate | 离线 Python 库，支持语言包及中间语言转译；库为 MIT/CC0 双许可 | 保留为回滚和单元测试路线，不作为生产默认 |
| LibreTranslate 自托管 | 使用 Argos 引擎，HTTP 服务为 AGPLv3 | 批处理无需再启动 API 服务 |
| Marian / OPUS-MT | 双语模型，许可逐模型核对；官方 `opus-mt-zh-en` 为 CC-BY-4.0 | 保留为具体语言质量对照方案 |
| M2M100 418M | 官方模型卡为 MIT，可直接处理 100 种语言间翻译；CTranslate2 提供转换示例 | 生产候选：单个多语模型、CPU INT8、整句处理 |
| NLLB 600M | CC-BY-NC-4.0；模型卡称其为研究模型，不面向生产部署或文档翻译 | 本次不采用 |

依据：[Argos Translate](https://github.com/argosopentech/argos-translate)、[LibreTranslate](https://github.com/LibreTranslate/LibreTranslate)、[OPUS 中文到英文模型](https://huggingface.co/Helsinki-NLP/opus-mt-zh-en)、[M2M100 模型](https://huggingface.co/facebook/m2m100_418M)、[CTranslate2 转换示例](https://opennmt.net/CTranslate2/guides/transformers.html)、[NLLB 模型](https://huggingface.co/facebook/nllb-200-distilled-600M)。

## 语言与模型

生产 Actions 使用固定 revision 的 `facebook/m2m100_418M`，只在模型准备步骤下载一次并转换为 CTranslate2 INT8；推理步骤只读 `M2M100_MODEL_DIR`，网络和 DeepSeek 凭据均不参与。模型卡声明 MIT，模型 revision、模型卡许可证据、源文件和转换后文件 SHA-256 会写入 `m2m100-model-provenance.json`。Argos 包路由仍保留在清单中，供回滚和无模型结构单元测试使用。

以下文件来自 [Argos 官方模型索引](https://raw.githubusercontent.com/argosopentech/argospm-index/main/index.json)。只安装所需语言包，推理期间不临时下载模型。

| 直接翻译方向 | 固定模型包 |
| --- | --- |
| 中文 → 英文 | `translate-zh_en-1_9.argosmodel` |
| 英文 → 中文 | `translate-en_zh-1_9.argosmodel` |
| 英文 → 日文 | `translate-en_ja-1_1.argosmodel` |
| 英文 → 韩文 | `translate-en_ko-1_1.argosmodel` |
| 英文 → 阿拉伯文 | `translate-en_ar-1_0.argosmodel` |

M2M100 直接覆盖中文、英文、日文、韩文和阿拉伯文之间的当前项目路由，不再用中文到英文的中转。金额短语（例如 `USD 120 million`）在进入模型前保持为源文片段，百分比、日期、负数和其他数字在输出后做数量与原始格式校验。中文已经存在的内容直接复用。

Argos 官方明确说明，中间语言转译可能降低质量。因此，验收应使用本项目真实金融文本，覆盖标题、长段落、表格、指标名称、百分比、负数、日期、币种、机构名称、专有名词及引用。继续检查段落覆盖、数字、占位符、链接和目标语言；通顺或出现目标语言文字本身不能证明译意正确。固定界面词与审定术语优先使用已有译文。依据：[Argos 中转说明](https://argos-translate.readthedocs.io/en/latest/)。

**许可核验状态：** 已在 [Actions 样测](https://github.com/yt-feng/rpt_edit/actions/runs/34674689210) 下载并检查五个模型包，固定包的 SHA-256。五包均无独立 LICENSE 文件；英文到中文、中文到英文两包的 README 声明其原始 OPUS 模型为 CC-BY 4.0。日、韩、阿包 README 记录数据/作者来源，没有完整模型许可条款。不能将 Argos 库的 MIT/CC0 许可等同于全部模型许可。包内 README、元数据及校验值保留在 Actions 模型审计产物中。

## 费用与执行边界

离线推理本身不调用翻译 API，因此没有按字符或 token 计费的翻译 API 支出。GitHub 当前对公开仓库的标准 GitHub-hosted runner 计算时长免费；较大 runner 始终收费，缓存和构建产物有独立额度，应控制在包含额度内。不能把这理解为所有 GitHub 产品及无限存储永久免费。依据：[GitHub Actions 计费](https://docs.github.com/en/billing/concepts/product-billing/github-actions)。

推荐 `ubuntu-24.04`，公开仓库标准配置当前为 4 CPU、16 GB RAM，单个 job 最长 6 小时。模型与译文缓存减少重复工作；按缺失内容分批运行，完成后保存检查通过的译文，失败部分保留待续状态。依据：[runner 配置](https://docs.github.com/en/actions/reference/runners/github-hosted-runners)、[Actions 限制](https://docs.github.com/en/enterprise-cloud%40latest/actions/reference/limits)。

本方案用于本仓库软件项目自身的静态多语种网站、内容构建和发布。GitHub 条款要求 hosted runner 工作与关联项目的生产、测试、部署或发布有关，并限制把 Actions 当作通用托管服务。前述用途是对条款与本项目实现方式的工程判断，并非 GitHub 对本项目的单独确认。依据：[GitHub Actions 条款](https://docs.github.com/en/site-policy/github-terms/github-terms-for-additional-products-and-features#actions)。

运行依赖为 Python 3.11、`ctranslate2==4.8.2`、`transformers==4.57.6`、`sentencepiece==0.2.1` 和 Actions CPU 版 `torch==2.8.0`。采用 CPU INT8，明确限制线程数；本地适配器测试不会下载模型，实际模型任务只在 GitHub Actions runner 执行。依据：[M2M100 模型](https://huggingface.co/facebook/m2m100_418M)、[CTranslate2 转换示例](https://opennmt.net/CTranslate2/guides/transformers.html)、[CTranslate2 版本](https://pypi.org/project/ctranslate2/)、[INT8 支持](https://opennmt.net/CTranslate2/quantization.html)。

## 当前诊断与迁移范围

本次审计的 Actions run `34672413981` 显示：41,639 个翻译单元、2,792,650 个字符；待补译分别为韩文 1,246、日文 1,317、阿拉伯文 1,614 个单元。该 run 的预检发生 4 次 HTTP 调用，记录 20,269 tokens，其中输入 10,859、输出 9,410；91 条有效译文已保存，全量补译未开始。

这是一轮预检的局部调用记录，不能据此推算整个账户的实际消费。内容量与重复构建的关系说明应保留增量译文缓存：仅处理新增或源文变更的单元，缓存键包含源文、目标语言及翻译版本，持续复用有效旧译文。

迁移覆盖网站多语种文案、报告纯翻译、标题和字幕纯翻译。模型安装、翻译、格式还原及质量检查分开执行；翻译失败不得自动转回 DeepSeek。文章创作、摘要、编辑改写等非翻译能力保持原有配置。本文件记录方案与核验状态，不代表全部迁移、GitHub Actions 实测或上线已完成。


## 实测与验收记录

2026-09-12，独立分支 Actions 已完成 M2M100 PyTorch CPU 对照：19 个完整句子在约 55 秒内完成，翻译 API 请求为零。相对 Argos 的按数字切分版本，`Operating cash flow rose by 15% in 2026.` 的日韩译文已保持为整句语义；首次对照仍发现日文小数标点和 `USD 120 million` 单位边界问题，因此加入源文金额保护和数字格式恢复。本分支需要重新跑模型准备、结构样本和人工金融语义复核，复核通过前不宣称可直接发布。

运行时只安装锁定的 CPU M2M100 推理依赖；模型准备步骤临时安装 Torch 用于读取官方权重和 CTranslate2 转换，最终翻译步骤只使用 CTranslate2、SentencePiece 和 tokenizer 文件。不会调用翻译 API，也不把模型文件或译文缓存放进公共仓库缓存以外的发布物。

网站与中文标题沿用公开内容的 Actions 译文缓存。完整报告段落缓存放在各自报告输出目录 `.translation_cache`，不会进入公共模型缓存；只有该私有输出目录仍在或被恢复时，才能跨运行复用。当前新 runner 未自动恢复历史报告输出，不能宣称它已支持所有报告的跨工作流续译。
