# 杰富瑞：中国AI模型成本仅为美国几分之一，架构优势而非补贴

要点 (1) 腾讯发布Hy3，进一步增强（例如成功率、成本效率、长周期任务）。API价格具有竞争力（图表4），以支持更多用户和场景；(2) Token支出指数：6月28日当周依然疲软，低于5月水平；(3) OpenRouter：Token使用量与上周相比保持稳定；(4) 智谱/MiniMax本周锁定期到期；(5) 新措施旨在保护用户免受AI虚拟亲密关系影响。

在本报告中，我们为读者提供超过50个关于OpenRouter中Token消耗、不同模型定价、Artificial Analysis中的模型智能、按子行业划分的用户趋势以及其他行业数据的数据点，以供分析。

Hy3正式版根据用户反馈进行了多项增强。Hy3与预览版相比的亮点包括 (1) 收到超过50个业务部门的反馈，并升级了用户体验。在输入/输出价格方面，Hy3以更低的价格收费，每百万Token收费人民币1元/人民币4元，而预览版为人民币2元/人民币8元。旨在支持更多用户和场景；(2) 在后期训练方面进一步增强，例如强化学习（RL）图表5。在长上下文方面表现优于参数规模大2-5倍的大模型；(3) 在生产力场景中创造价值，例如软件开发、办公、资金、设计和游戏开发；(4) 在270位专家真实工作场景中的盲测显示，Hy3得分优于GLM-5.1（例如前端、数据、存储、CI/CD）；(4) 进一步改进 (a) 任务成功率高于预览版（90%对比之前的72%），(b) Token效率：与GLM-5.2相比，在文字处理（47.4%）和PPT（49%）方面实现了Token消耗节省，(c) 幻觉减少15个百分点。请参考不同第三方评估的图表6。

硅数据LLM Token支出指数：6月28日当周持续疲软。该指数（图表2）根据使用集中度进行加权（例如，当需求转向高端模型时，支出增加）。另一方面，媒体报道（例如The Information、宏观环境观察报）强调科技和互联网公司为员工设定了Token消耗上限。根据我们的核查，该指数在6月28日至7月4日期间介于1.62至1.71之间（对比6月21日至27日期间的1.68至1.74），而5月31日为2.04。根据Artificial Analysis，中国模型DeepSeek、Qwen、Kimi、MiniMax和智谱与美国模型相比具有高成本效益，API成本仅为美国模型的一小部分（图表3），这得益于前者精炼的架构，如MoE（混合专家模型）、注意力机制（分组查询注意力GQA、稀疏注意力）和MLU（模型算力利用率）。

OpenRouter：Token消耗与上周相比保持稳定。根据对6月29日当周（对比6月22日当周）的分析（图表1），每周消耗的Token数量稳定在46.7万亿。在排名方面，DeepSeek V4 Flash排名第一，其次是小米MiMo-V2.5和MiniMax M3。

DS-V4和Seedance 2.5将于7月发布。根据我们最近的更新（链接）和（链接），DS-V4将从7月15日起实施新的定价策略，在高峰时段（9:00至12:00，14:00至18:00）输入/输出价格翻倍（图表7-9）。我们认为，在AI需求上升和供应受限的情况下，高成本效益模型是关键。另一方面，视频生成模型Seedance 2.5预计即将发布，升级包括 (a) 30秒视频生成；(b) 最多50个多模态输入资产；(c) 视频编辑和生成的升级提高了效率和质量。

图表1 - 截至7月6日的过去12个月每周Token消耗量（万亿）

[[KC_IMAGE_001]]

来源：OpenRouter，JEF

图表2 - 硅数据LLM Token支出指数

[[KC_IMAGE_002]]

来源：factset，JEF

图表3 - 中国模型与美国模型的混合价格（2026年第二季度）

[[KC_IMAGE_003]]

来源：Artificial Analysis，JEF

图表4 - 各公司旗舰模型的输入和输出价格

[[KC_IMAGE_004]]

来源：公司，JEF
注：Qwen定价基于促销结束后的官方价格

下页继续...

更多来自阿里云和腾讯云的产品将从8月1日起不再免费提供。阿里云：Databridge Agent (DTS) 将从8月1日开始商业化。它连接各种主流数据库，执行数据分析、安全以及与AI生态系统的集成；腾讯云：将从8月1日起停止为AI原生GPU开发和部署等服务提供免费配额。

美团发布开源LongCat 2.0模型。亮点 (1) 总参数1.6T。动态激活在33B至56B Token之间；(2) 1M上下文；(3) 通过LSA（LongCat稀疏注意力LSA）实现高成本效益。通过零计算专家 + ScMoE实现高度Token级动态计算；(4) 在智能体、推理和交互中使用国产算力；(5) 这是首个在50K卡国产算力集群上完成完整训练和推理的该规模模型；(6) 在SWE-bench Pro（软件工程）和Terminal-Bench（智能体）中排名领先于同行。

WorkBuddy在WorkSpace Agents市场领先。根据第三方易观分析，它强调了WorkBuddy在该细分市场（2026年3月）的运营指标。这些包括 (1) 桌面端月访问量达到885万次；(2) WorkBuddy领先于Trae（字节跳动）、QClaw（腾讯）和Qoder Work（阿里巴巴）。

当局实施措施规范拟人化服务。这些措施由国家互联网信息办公室、国家发展和改革委员会、工业和信息化部、公安部和国家市场监督管理总局于2026年4月发布。这些措施将于7月15日实施，旨在 (1) 保护用户免受虚拟亲密关系服务（例如虚拟亲戚或虚拟伴侣）产生的问题影响；(2) 避免过度依赖AI并影响真实人际关系。我们看到豆包和Qwen将分别于7月15日和7月10日停止提供这些功能。

BAT、KC、AI实验室和可灵是受益者。我们预计，由于对AI模型和智能体的需求上升导致的Token消耗激增，将使百度、阿里巴巴、腾讯（BAT）、金山云（KC）、AI实验室和可灵等云服务提供商受益。根据Artificial Analysis的分析：(1) 美国和中国模型之间的智能差距正在缩小；(2) API成本仅为美国模型的一小部分，受益于MoE、线性注意力和MFU；(3) 编码、WorkSpace场景和中长篇幅内容未来应看到重大机遇（图表85-89）。

图表5 - 第三方评估：Hy3与其他模型对比

[[KC_IMAGE_005]]

[[KC_IMAGE_006]]

[[KC_IMAGE_007]]

[[KC_IMAGE_008]]

[[KC_IMAGE_009]]

[[KC_IMAGE_010]]

[[KC_IMAGE_011]]

[[KC_IMAGE_012]]

[[KC_IMAGE_013]]

[[KC_IMAGE_014]]

[[KC_IMAGE_015]]

[[KC_IMAGE_016]]

图表6 - 第三方评估：Hy3与其他模型对比

注释
所有模型的推理努力均设为最高等级，标有 * 的结果来自我们自己的测试。
对于 SWE-Bench 系列（包括 Multilingual 和 Pro），我们使用 SWE-agent 脚手架。
对于 Hy Backend 2.0、Hy-SWE Max 和 Hy-CompanyBench，除 GPT 5.5 外，所有模型均使用 Claude Code 脚手架。对于 GPT 5.5，我们使用 CodeX 脚手架。
Terminal-Bench 2.1 评估配置：脚手架：Terminus-2，解析器：xml，智能体超时：4小时，CPU：16核，内存：32 GB，最大回合数：500。
ProgramBench：所有模型均使用 mini-swe-agent 脚手架进行评估，每个任务预算为 1000 轮，超时时间为 6 小时。每个任务在沙盒环境中运行，配备 8 个 CPU 核心和 16 GB 内存，并处于严格的网络隔离下。
DeepSWE：所有模型均使用 mini-swe-agent 脚手架进行评估，每个任务超时时间为 2 小时。每个任务在沙盒环境中运行，配备 2 个 CPU 核心和 8 GB 内存，并处于严格的网络隔离下。
NL2Repo：所有模型均通过 Claude Code 进行评估，每个任务预算为 250 轮，超时时间为 12,000 秒。每个任务使用 4 个 CPU 核心和 32 GB 内存运行。应用了额外的反黑客提示约束和工具调用监控以防止奖励黑客行为。
SkillsBench：所有模型均通过 Claude Code 在 79 个任务（自包含子集，排除多模态任务）上进行评估；结果取 3 次运行的平均值。
MCP-Atlas 评分遵循 Scale 2026 年 4 月的方法论（每个任务 100 次工具调用预算，取代旧的 20 轮限制），在 500 个任务的公开集上进行评估，并使用 Gemini 2.5 Pro 作为评判模型。
ProdBench：所有模型均使用 OpenClaw Harness 进行评估。
WildClaw：所有模型均使用 OpenClaw Harness 在纯文本子集（共 35 个查询）上进行评估。
Claw Eval：所有模型均使用我们的内部 Harness 在 20260325 版本（共 105 个查询）上进行评估。我们使用 Gemini-3.5-flash 作为评判模型。
Agentic Search：所有模型均使用我们的内部 Harness 进行评估，BrowserComp 采用自我总结方法进行上下文管理。

## 中国 vs 美国对比

## AI 模型：公司情况更新

根据 OpenRouter 的数据，2026 年 2 月的 Token 消耗量显著增加，原因是 (a) 编码/智能体的采用激增，这使得人们使用 AI 从“聊天”转向“工作”。它连接了可以本地或服务器部署的大模型，允许你通过自然语言聊天自动化工作流程；(b) 发布了一系列高性能且高性价比的模型，包括 Kimi K2.5（2026 年 1 月）、M2.5（2026 年 2 月）和 GLM-5（2026 年 2 月）。

根据 OpenRouter 的数据，编码/智能体采用率的上升以及高性能、高性价比中国模型的发布正在推动 Token 消耗

图表 7 - DeepSeek-V4-Pro 定价


来源：公司，JEF
注：高峰时段指北京时间上午 9 点至 12 点和下午 2 点至 6 点

图表 8 - DeepSeek-V4-Flash 定价


来源：公司，JEF
注：高峰时段指北京时间上午 9 点至 12 点和下午 2 点至 6 点

图表 9 - 最近一周按模型划分的 Token 消耗量前十排名


来源：OpenRouter，JEF

图表 10 - 截至 7 月 6 日的过去 12 个月每周 Token 消耗量（万亿）

[[KC_IMAGE_016]]

来源：OpenRouter，JEF

根据 OpenRouter（6 月 29 日至 7 月 5 日），中国模型的 Token 消耗量较前一周增长 14.9%，达到 23.4 万亿。相比之下，美国模型的 Token 消耗量为 4.3 万亿。DeepSeek V4 Flash 每周 Token 消耗量快速增长

在 OpenRouter 中，中国模型在 6 月 29 日当周的 Token 消耗量超过了美国模型

图表 11 - 市场份额：截至 7 月 6 日按公司划分的每周 Token 消耗量

[[KC_IMAGE_017]]

来源：OpenRouter，JEF

图表 12 - 自 2026 年 1 月以来的每周 Token 消耗量（十亿）

[[KC_IMAGE_018]]

来源：OpenRouter，JEF

DeepSeek V4 Flash 在 6 月 29 日当周的 Token 消耗量排名第一

图表 13 - 最近一周按模型划分的 Token 消耗量前十排名


来源：OpenRouter，JEF

图表 14 - 最近一周按模型划分的 Token 消耗量第 11-20 名排名


来源：OpenRouter，JEF

根据 Artificial Analysis 的数据，中国模型 DeepSeek、Qwen、Kimi、MiniMax 和智谱在智能水平上正在缩小与美国模型的差距。中国模型在混合专家（MoE）架构、线性注意力和 MLU（模型算力利用率）上具有很高的性价比。

中国模型在智能水平上正在缩小与美国模型的差距。在输入/输出 API 价格上，中国大模型相对于美国模型具有很高的效率。

图表 16 - 人工智能指数 vs 混合价格

根据 2026 年斯坦福 AI 指数报告（2026 年 4 月），美国顶尖模型领先中国模型 2.7%。另外，截至 2026 年 3 月，Anthropic（1503）、xAI（1495）、Google（1494）、OpenAI（1481）、阿里巴巴（1449）和 DeepSeek（1424）占据了 Arena Elo 评分的第一梯队。

图表 15 - 截至 7 月 6 日领先模型的缓存命中/输入/输出 API 价格
- 缓存命中
- 输入
- 输出

[[KC_IMAGE_019]]


[[KC_IMAGE_020]]

来源：Artificial Analysis，JEF

图表 17 - 中国模型季度输入/输出价格

[[KC_IMAGE_021]]

来源：Artificial Analysis，JEF

图表 18 - 美国模型季度输入/输出价格

[[KC_IMAGE_022]]

来源：Artificial Analysis，JEF

在输入/输出 API 价格方面，中国模型仅为美国模型的一小部分。
图表 19 - 截至 7 月 6 日的前 20 名模型智能指数

[[KC_IMAGE_023]]


图表 20 - 截至 7 月 6 日前沿语言模型智能随时间变化

[[KC_IMAGE_024]]

来源：Artificial Analysis，JEF
■ 专有 □ 开放权重 ■ 开放权重（商业使用受限）
来源：Artificial Analysis，JEF

截至 7 月 6 日，在前 20 名大模型中，有 8 个是中国模型且为开放权重。

图表 21 - 截至 7 月 6 日的前 20 名模型智能体指数

[[KC_IMAGE_025]]

来源：Artificial Analysis，JEF
■ 专有 □ 开放权重 ■ 开放权重（商业使用受限）

图表 22 - 截至 7 月 6 日的前 20 名模型编码指数

[[KC_IMAGE_026]]

■ 专有 □ 开放权重 ■ 开放权重（商业使用受限）
来源：Artificial Analysis，JEF

图表 23 - 截至 7 月 6 日运行人工智能指数的成本
最具吸引力的象限

[[KC_IMAGE_027]]

来源：Artificial Analysis，JEF

图表 24 - 截至 7 月 6 日运行人工智能指数的输出速度

[[KC_IMAGE_028]]

来源：Artificial Analysis，JEF

## 各公司模型输入/输出价格

图表 25 - DeepSeek：输入价格
来源：Artificial Analysis，JEF

图表 26 - DeepSeek：输出价格
图表 27 - 智谱：输入价格
来源：Artificial Analysis，JEF

来源：Artificial Analysis，JEF
注：GLM-5.2 在所有上下文长度上的 API 价格相同，而 GLM-5.1 采用分层定价

图表 28 - 智谱：输出价格
来源：Artificial Analysis，JEF

图表 29 - Qwen：输入价格

注：GLM-5.2 在所有上下文长度上的 API 价格相同，而 GLM-5.1 采用分层定价

来源：Artificial Analysis，JEF

图表 30 - Qwen：输出价格
来源：Artificial Analysis，JEF

图表 31 - MiniMax：输入价格
来源：Artificial Analysis，JEF
注：MiniMax-M3 的输入 Token 数 > 512k

图表 32 - MiniMax：输出价格
来源：Artificial Analysis，JEF
注：MiniMax-M3 的输入 Token 数 > 512k

图表 33 - 小米：输入价格
来源：Artificial Analysis,JEF

图表 34 - 小米：输出价格
来源：Artificial Analysis,JEF

图表 35 - 腾讯：输入价格
来源：Artificial Analysis,JEF

图表 36 - 腾讯：输出价格
图表 37 - Kimi：输入价格
来源：Artificial Analysis,JEF

来源：Artificial Analysis,JEF

图表 38 - Kimi：输出价格
来源：Artificial Analysis,JEF

图表 39 - 百度：输入价格
来源：Artificial Analysis,JEF
注：32k < 输入 tokens <= 128k

图表 40 - 百度：输出价格
来源：Artificial Analysis,JEF
注：32k < 输入 tokens <= 128k

图表 41 - 阶跃星辰：输入价格
来源：Artificial Analysis,JEF

图表 42 - 阶跃星辰：输出价格
来源：Artificial Analysis,JEF

图表 43 - OpenAI：输入价格
来源：Artificial Analysis,JEF

图表 44 - OpenAI：输出价格
来源：Artificial Analysis,JEF

图表 46 - Anthropic：输出价格

来源：Artificial Analysis,JEF

来源：Artificial Analysis,JEF

图表 47 - 模型定价趋势

来源：公司,JEF

图表 48 - 模型定价趋势（续）

## 视频生成模型产品

红色表示当月价格上涨/新价格

不同视频生成模型的定价方案

图表 49 - 视频生成模型定价（人民币）

来源：各公司,JEF

图表 50 - 视频生成模型定价（美元）

来源：各公司,JEF

图表 51 - 视频生成会员比较（原价）

来源：公司,JEF

图表 52 - 视频生成会员比较（促销后）

来源：公司,JEF

## OpenClaw

根据 OpenRouter，OpenClaw 基于 token 消耗量的前三名模型均来自中国，分别是 MiniMax M3、DeepSeek V4 Flash 和 DeepSeek V4 Pro。其他模型包括 MiniMax M2.7、MiMo V2.5 Pro 和 Kimi K2.6。

根据 OpenRouter，MiniMax M3、DeepSeek V4 Flash 和 Owl Alpha 在 OpenClaw 上的 token 消耗量排名前三。

图表 53 - OpenClaw 的 Token 消耗量（十亿）
来源：OpenRouter,JEF

图表 54 - Hermes Agent 的 Token 消耗量（十亿）
来源：OpenRouter,JEF

图表 55 - 过去 30 天 OpenClaw 使用的前 15 个模型（截至 7 月 6 日）

来源：OpenRouter,JEF

图表 56 - 过去 30 天 Hermes Agent 使用的前 15 个模型（截至 7 月 6 日）

来源：OpenRouter,JEF

图表 57 - 全球：截至 7 月 6 日成功率排名前 10 的模型
来源：PinchBench,JEF

图表 58 - 中国：截至 7 月 6 日成功率排名前 10 的模型
来源：PinchBench,JEF

## AI 助手：公司情况更新

\- 环比趋势：5 月通义千问 DAU 达到 2790 万（4 月：2920 万），元宝达到 880 万（4 月：900 万）。豆包环比增长 5% 至 1.58 亿（4 月：1.51 亿）。DeepSeek DAU 环比增长约 6% 至约 3050 万。

5 月多家领先玩家的 DAU 环比增长

图表 59 - 中国主要 AI 助手周 DAU（百万）
来源：QuestMobile,JEF

图表 60 - 中国主要 AI 助手月 DAU（百万）
来源：QuestMobile,JEF

图表 61 - 中国主要 AI 助手每周 DAU 人均使用时长（分钟）

图表 62 - 中国主要 AI 助手每月 DAU 人均日使用时长（分钟）

## 视频生成模型

根据 Artificial Analysis（截至 6 月 29 日），HappyHorse-1.1 和 HappyHorse-1.0 在文生视频和图生视频方面排名前五。其他模型包括 Seedance 2.0 720p、Wan 2.7、SkyReels V4、Kling 3.0 1080p (Pro) 和 grok-imagine-video。

图表 63 - 图生视频排行榜前 15（含音频）

来源：Artificial Analysis,JEF

图表 64 - 文生视频排行榜前 15（含音频）

来源：Artificial Analysis,JEF

## 全球及中国 AI 手机应用 MAU 排名

图表 65 - 全球 AI 手机应用 MAU 排名（6 月 26 日）

来源：AICPB,JEF

根据 aicpb.com，由于 2 月春节因素，包括豆包、通义千问、夸克和元宝在内的中国 AI 应用 MAU 相比 ChatGPT 实现了强劲的环比增长。

图表 66 - 中国 AI 手机应用 MAU 排名（6 月 26 日）

来源：AICPB,JEF

在国内市场，通义千问的 MAU 在 6 月实现了快速的环比增长。

## 5 月 26 日：来自 QuestMobile 分析的月度应用追踪

## 在线购物：公司情况更新

\- 环比趋势：5 月淘宝/唯品会 DAU 分别增长 5%/1%，拼多多下降 0.5%。京东 DAU 5 月环比增长 13%。

\- 同比趋势：京东 DAU 同比下降 3%，淘宝/拼多多同比分别增长 1%/8%。

5 月拼多多 DAU 同比保持快速增长

来源：QuestMobile,JEF

## 外卖：公司情况更新

5 月美团 MAU 环比基本稳定

• 环比趋势：美团 MAU 当月环比增长 1%。

• 同比趋势：5 月美团 MAU 同比增长 3%（4 月同比 4%）。

图表 69 - 过去 12 个月美团应用 MAU
来源：QuestMobile,JEF

## 在线音乐：公司情况更新

\- 环比趋势：5 月汽水音乐 MAU 环比增长 4% 至 1.668 亿。腾讯音乐方面，QQ 音乐/酷狗音乐 MAU 环比分别增长 2%/1%，酷我音乐环比下降 2%。网易云音乐 MAU 当月环比增长 1%。

5 月汽水音乐 MAU 同比保持快速增长，环比基本稳定

\- 同比趋势：5 月汽水音乐 MAU 同比增长 75%，网易云音乐 MAU 同比增长 1%。腾讯音乐方面，QQ 音乐 MAU 同比增长 1%，酷狗音乐/酷我音乐 MAU 同比分别下降 9%/17%。

图表 70 - 5 月 26 日腾讯音乐、汽水音乐和网易云音乐 MAU
250
来源：QuestMobile,JEF

图表 71 - 过去 12 个月汽水音乐 MAU
来源：QuestMobile,JEF
在线视频
5 月主要长视频平台 MAU 同比下降

\- 环比趋势：腾讯视频/爱奇艺/芒果 TV MAU 环比增长 1%/3%/3%，优酷环比下降 3%。

• 同比趋势：当月主要长视频玩家 MAU 同比下降。

图表 72 - 5 月 26 日爱奇艺、腾讯视频和优酷 MAU
来源：QuestMobile,JEF

## 直播与短视频

5 月抖音 DAU 保持稳健同比增长

\- 环比趋势：5 月抖音主应用 DAU 环比增长 2%。游戏直播方面，虎牙 MAU 环比下降 1%，斗鱼环比增长 3%。哔哩哔哩 MAU 当月环比增长 2%。

\- 同比趋势：抖音主应用 DAU 保持 21% 的稳健同比增长。游戏直播方面，虎牙和斗鱼 MAU 同比分别下降 7% 和 11%。哔哩哔哩 MAU 当月同比增长约 4%。

图表 73 - 过去 12 个月抖音 DAU
来源：QuestMobile,JEF
在线旅游

图表 74 - 过去 12 个月哔哩哔哩 MAU
来源：QuestMobile,JEF
2 月春节过后，携程国内 MAU 5 月环比下降

• 环比趋势：5 月携程/去哪儿 MAU 环比分别下降 7%/8%。

• 同比趋势：5 月携程/去哪儿 MAU 同比分别下降 9%/13%。

图表 75 - 过去 12 个月携程 MAU
来源：QuestMobile,JEF

## 新闻应用：公司情况更新

• 环比：5 月微博 MAU 增长 4%，今日头条 MAU 增长 1%。

5 月微博 MAU 实现正同比增长

• 同比：5 月微博 MAU 同比增长 1%，今日头条同比下降 2%。

图表 76 - 过去 12 个月微博 MAU
来源：QuestMobile,JEF

## 百度应用：公司情况更新

• 环比：5 月 MAU 保持稳定，DAU 下降 2%。

• 同比：5月MAU同比下降8%，DAU同比下降21%。

百度APP MAU 5月环比稳定，同比下降

图表77 - 百度过去12个月MAU
来源：QuestMobile，JEF

## IDC对公有云Token消耗的估算及展望

图表78 - 2025年中国MaaS市场月均日均Token消耗量

来源：IDC，JEF

图表79 - 2025年中国MaaS市场按Token消耗量计算的份额
来源：IDC，JEF
图表80 - 2025年中国MaaS市场主要厂商份额（按收入计）

来源：IDC，JEF
图表81 - 2025年中国私有大模型平台市场主要厂商份额（按收入计）

图表82 - 推动人们决定广泛部署模型的最重要因素

来源：IDC，JEF
来源：IDC，JEF

来源：IDC，JEF

## 附录：公司情况更新

## Omdia亚太及大洋洲智能体AI开发平台热力图

据Omdia，智能体AI软件市场预计将以105%的复合年增长率增长，从2025年的2.71亿美元增至2030年的97亿美元。阿里云在5个领域获得最高排名：（1）上下文工程，（2）模型支持，（3）多智能体框架，（4）运维与生命周期管理，（5）开源与社区。

据Omdia，阿里云被列为构建和部署AI智能体的领导者及首选之一。其在7项指标中的5项获得最高排名。

## 图表84 - Omdia亚太及大洋洲智能体AI开发平台热力图

## 市场规模：编码、工作空间与内容创作

据Grand View Research，全球AI代码工具市场预计将从2025年到2030年增长3倍，达到260亿美元。另一方面，F&S预测中国AI代码生成市场将在2028年达到约47亿美元。KA定制化解决方案预计将成为关键收入贡献者。

全球AI代码工具市场预计2030年规模将是2025年的3倍

图表85 - 全球AI代码工具市场规模（十亿美元）
来源：Grand View Research，JEF

图表86 - 中国AI代码生成市场规模按服务类型划分（十亿元人民币）
来源：Frost & Sullivan，JEF

图表87 - 中国AI代码在不同行业的渗透率
在AI代码渗透率方面，互联网、游戏、AI、资金和能源是前五大关键行业
来源：Frost & Sullivan，JEF
据Gonyn Industry Research（2024），AI+工作空间软件市场规模预计在2028年达到1910亿元人民币，是2024年规模的6倍。

图表88 - 中国AI+工作空间市场规模
来源：Gonyn，JEF

图表89 - 内容创作中的生成式AI市场规模2025至2035年（十亿美元）
来源：Precedence Research，JEF
据Precedence Research，全球生成式AI内容创作市场预计将增长7倍，在2035年超过1400亿美元，对比2025年。

图表90 - 2025年下半年与上半年中国企业日均Token消耗量（万亿）
来源：Frost & Sullivan，JEF

据F&S，企业日均Token消耗量环比增长263%至37万亿，其中阿里云市场份额增幅最大，在2025年下半年以32%的份额占据第一（2025年上半年为17.7%），其次是豆包的21.3%（2025年上半年为14.1%）和DeepSeek的18.4%（2025年上半年为10.3%）。

阿里通义千问在2025年下半年企业Token消耗量中排名第一

图表91 - 2025年上半年企业Token消耗量市场份额
来源：Frost & Sullivan，JEF

图表92 - 2025年下半年企业Token消耗量市场份额
来源：Frost & Sullivan，JEF

## 中国大语言模型

据F&S/中国信通院，中国LLM市场预计在2024年至2030年间以约64%的复合年增长率增长，并在2030年超过1000亿元人民币。按细分市场看，由于付费意愿仍然较低，消费者收入的增长速度预计将慢于企业。

图表93 - 中国LLM市场规模（十亿元人民币）
来源：Frost & Sullivan，中国信通院，JEF

中国大语言模型预计在2024年至2030年间以64%的复合年增长率增长。按细分市场看，本地部署是主要收入贡献者

图表94 - 中国企业LLM市场规模（十亿元人民币）
来源：Frost & Sullivan，中国信通院，JEF

## Anthropic与OpenAI

- 2026年5月，Anthropic于5月28日宣布投后估值9650亿美元。其在H轮融资中筹集了650亿美元。ARR在5月初超过470亿美元。

- 据The Information，OpenAI收入预计在2030年达到2000亿美元，是2026年规模的6倍以上。未来几年智能体收入贡献预计将上升。

图表95 - Anthropic的ARR

图表96 - OpenAI的ARR
来源：The Information，公司报告，JEF
来源：The Information，公司报告，JEF

图表97 - OpenAI 2023年至2030年预测收入（截至2025年第三季度）
来源：The Information，JEF

图表98 - OpenAI 2024年至2030年预测收入结构（截至2025年第三季度）
来源：The Information，JEF

图表99 - MiniMax：未来几年占OpenAI收入的百分比
来源：CIC，JEF估算

## 中国主要参与者的模型

图表100 - 阿里模型列表

来源：公司，JEF

图表101 - 腾讯模型列表

来源：公司，JEF

图表102 - 百度模型列表

来源：公司，JEF

图表103 - MiniMax模型列表

来源：公司，JEF

图表104 - Moonshot AI模型列表

来源：公司，JEF

图表105 - Z.ai模型列表

来源：公司，JEF

图表106 - 基准测试术语表

来源：JEF

不同的第三方分析显示，中国正在为全球Token消耗做出重要贡献。据Hugging Face，在截至2026年2月的12个月中，中国模型占全球下载量的41%。

来源：国家数据局，JEF

图表108 - 豆包日均Token消耗量
■ 日均Token消耗量（万亿）
来源：火山引擎，JEF

图表109 - 按地区划分的Token份额
来源：OpenRouter，JEF

## 公司估值/不确定性