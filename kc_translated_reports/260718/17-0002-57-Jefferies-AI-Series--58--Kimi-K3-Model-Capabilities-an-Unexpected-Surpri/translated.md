# 杰富瑞：杰富瑞AI系列第58期，KimiK3模型能力给市场带来意外惊喜

Moonshot AI发布了首个开源2.8T模型K3，在Artificial Analysis中排名第三，仅次于Fable5和GPT-5.6 Sol (Max)。它在Frontend Code Arena中排名第一。我们认为这一突破出乎意料，并在快速模型迭代中推动行业创新。根据Token Expenditure Index，这反映出对高性价比模型的持续吸引力（图表3），这对具有强大性价比的中国模型是利好（图表2）。

在本报告中，我们为读者提供各公司模型定价、中美定价对比、Artificial Analysis的模型智能、OpenRouter中的Token消耗、Token Expenditure Index趋势以及其他行业数据以供分析。

Moonshot AI发布了首个开源2.8T模型，并在不同指标上排名靠前（图表5-6）。K3专为长周期编程、知识工作和推理而构建。亮点：(1) 1M上下文和原生多模态；(2) 在Artificial Analysis Index中排名第三，仅次于Fable5和GPT-5.6 Sol (Max)；(3) 在Frontend Code Arena中排名第一；与全球同行相比，在编程、通用Agent和视觉Agent方面处于领先地位。完整模型权重将于7月27日发布。

与全球同行的性价比对比。我们将K3的输入/输出价格与全球同行进行性价比比较（图表1）。K3基于Delta Attention和Attention Residuals构建。亮点：(1) Delta Attention在百万Token上下文中实现高达6.3倍的解码加速；(2) Attention Residuals以不到2%的额外成本实现25%的训练效率提升。架构更新带来：(1) 与Stable LatentMoE框架配合时，有效激活896个专家中的16个；(2) 与K2相比，整体扩展效率提升2.5倍。

Silicon Data LLM Token Expenditure Index：7月12日当周持续疲软。该指数（图表3）按使用集中度加权（例如，当需求转向高端模型时，支出增加）。另一方面，媒体报道（例如The Information、宏观环境观察报）强调科技和互联网公司为员工设定了Token消耗上限。根据我们的核查，7月12日当周该指数在1.57至1.61之间（7月5日当周为1.63至1.65），而5月31日为2.04。根据Artificial Analysis，中国模型DeepSeek、Qwen、Kimi、MiniMax和智谱相比美国模型具有极高的性价比，API成本仅为美国模型的一小部分（图表2），这得益于前者精炼的架构，如MoE（混合专家）、注意力机制（分组查询注意力GQA、稀疏注意力）和MLU（模型算力利用率）。

OpenRouter：Token消耗较前一周上升。根据对7月6日当周（对比6月29日当周）的分析（图表4），每周消耗的Token数量增长12.6%，达到52.6万亿。排名方面，DeepSeek V4 Flash排名第一，其次是Xiaomi MiMo-V2.5和MiniMax M3。

BAT、KC、AI实验室和Kling是AI需求上升的受益者。我们预计，AI模型和Agent需求上升带来的Token消耗激增将使CSP（如百度、阿里巴巴、腾讯（BAT）、金山云（KC）、AI实验室和Kling）受益。根据Artificial Analysis的分析：(1) 中美模型之间的智能差距正在缩小；(2) 得益于MoE、线性注意力和MFU，API成本仅为美国模型的一小部分；(3) 编程、工作空间场景和中长篇幅内容未来将迎来重大机遇。

下页继续...

图表1 - 各公司旗舰模型的输入和输出价格

来源：公司，JEF
注：Qwen定价基于促销结束后的官方价格，DeepSeek-V4-Pro定价为高峰时段价格

图表2 - 中国模型与美国模型的混合价格对比（2026年第二季度）

[[KC_IMAGE_001]]

来源：Artificial Analysis，JEF

图表3 - Silicon Data LLM Token Expenditure Index

[[KC_IMAGE_002]]

来源：彭博，JEF

图表4 - 截至7月13日的过去12个月每周Token消耗量（万亿）

[[KC_IMAGE_003]]

来源：OpenRouter，JEF

视觉Agent均在思考努力上达到最大值：max或xhigh。

图表5 - 编程评估：K3与全球同行对比

编程均在思考努力上达到最大值：max或xhigh。

[[KC_IMAGE_004]]

[[KC_IMAGE_005]]

[[KC_IMAGE_006]]

[[KC_IMAGE_007]]

[[KC_IMAGE_008]]

注：所有Fable 5结果均包含潜在回退。所有GPT-5.6 Sol结果均包含潜在网络防护。

[[KC_IMAGE_009]]

来源：Moonshot AI，JEF

图表6 - 通用评估：K3与全球同行对比
通用Agent均在思考努力上达到最大值：max或xhigh。

[[KC_IMAGE_010]]

[[KC_IMAGE_011]]

[[KC_IMAGE_012]]

[[KC_IMAGE_013]]

[[KC_IMAGE_014]]

[[KC_IMAGE_015]]

[[KC_IMAGE_016]]

来源：Moonshot AI，JEF

[[KC_IMAGE_017]]

注：所有Fable 5结果均包含潜在回退。所有GPT-5.6 Sol结果均包含潜在网络防护。

图表7 - 每任务编程成本评估：K3与全球同行对比

[[KC_IMAGE_018]]

来源：Moonshot AI，JEF

图表8 - 每任务浏览成本评估：K3与全球同行对比
BrowseComp · 得分与每任务成本

[[KC_IMAGE_019]]

来源：Moonshot AI，JEF

图表9 - 完整基准测试表

来源：Moonshot AI，JEF

图表10 - 完整基准测试表（续）

来源：Moonshot AI，JEF

图表11 - 完整基准测试表（续）

来源：Moonshot AI，JEF

图表12 - Artificial Analysis智能指数
Artificial Analysis智能指数v4.1包含9项评估：GDPval-AA v2、$\tau^3$ -Banking、Terminal-Bench v2.1、SciCode、Humanity's Last Exam、GPQA Diamond、CritPt、AA-Omniscience、AA-LCR

Artificial Analysis智能指数

[[KC_IMAGE_020]]

推理模型以灯泡图标标示
来源：Artificial Analysis，JEF

## 中美对比：公司情况更新

## AI模型：公司情况更新

根据OpenRouter，Token消耗在2026年2月显著上升，原因是：(a) 编程/Agent采用率激增，使人们使用AI从"聊天"转向"工作"。它连接了可在本地或服务器上部署的大模型，允许您通过自然语言聊天实现工作流自动化；(b) 发布了一系列高性能、高性价比的中国模型，包括Kimi K2.5（2026年1月）、M2.5（2026年2月）和GLM-5（2026年2月）。

图表13 - 最近一周按模型划分的Token消耗量前十排名

来源：OpenRouter，JEF

图表14 - 截至7月13日的过去12个月每周Token消耗量（万亿）

[[KC_IMAGE_021]]

来源：OpenRouter，JEF

根据OpenRouter（7月6日至7月12日），中国模型的Token消耗量较前一周增长17.7%，达到27.6万亿。相比之下，美国模型Token消耗量为6.3万亿。DeepSeek V4 Flash每周Token消耗量快速增长。

图表15 - 截至7月13日按公司划分的每周Token消耗量市场份额

[[KC_IMAGE_022]]

来源：OpenRouter，JEF

在OpenRouter中，中国模型在7月6日当周的Token消耗量超过了美国模型。

图16 - 自1月26日以来的每周Token消耗量（十亿）

[[KC_IMAGE_023]]

资料来源：OpenRouter,JEF

图17 - 最近一周各模型Token消耗量前十排名

资料来源：OpenRouter,JEF

Hy3（免费版）在7月6日当周的Token消耗量排名第一

图18 - 最近一周各模型Token消耗量第11至20名排名

资料来源：OpenRouter,JEF

根据Artificial Analysis，中国模型DeepSeek、Qwen、Kimi、MiniMax和智谱在智能水平上正缩小与美国模型的差距。中国模型在混合专家（MoE）架构、线性注意力机制和模型算力利用率（MLU）方面具有很高的成本效益。根据2026年斯坦福AI指数报告（2026年4月），美国顶尖模型领先中国模型2.7%。此外，截至2026年3月，Anthropic（1503）、xAI（1495）、Google（1494）、OpenAI（1481）、阿里巴巴（1449）和DeepSeek（1424）占据了Arena Elo评分的第一梯队。

中国模型在智能水平上正缩小与美国模型的差距。在输入/输出API方面，中国大模型相对于美国模型具有高效率。

图19 - 人工智能能力 vs 混合价格

[[KC_IMAGE_024]]

资料来源：Artificial Analysis,JEF

图20 - 中国模型季度输入/输出价格

[[KC_IMAGE_025]]

资料来源：Artificial Analysis,JEF

图21 - 美国模型季度输入/输出价格

[[KC_IMAGE_026]]

资料来源：Artificial Analysis,JEF
在输入/输出API价格方面，中国模型仅为美国模型的一个零头。

图22 - 截至7月13日前沿语言模型智能水平随时间变化

[[KC_IMAGE_027]]

资料来源：Artificial Analysis,JEF

## 各公司模型输入/输出价格

图23 - DeepSeek：输入价格

[[KC_IMAGE_028]]

图24 - DeepSeek：输出价格
资料来源：Artificial Analysis,JEF

资料来源：Artificial Analysis,JEF

图25 - Kimi：输入价格
资料来源：Artificial Analysis,JEF

图26 - Kimi：输出价格
资料来源：Artificial Analysis,JEF

图27 - 智谱：输入价格
资料来源：Artificial Analysis,JEF
注：GLM-5.2在所有上下文长度下API价格相同，而GLM-5.1采用分级定价。
图28 - 智谱：输出价格
资料来源：Artificial Analysis,JEF
注：GLM-5.2在所有上下文长度下API价格相同，而GLM-5.1采用分级定价。

图29 - Qwen：输入价格
资料来源：Artificial Analysis,JEF

图30 - Qwen：输出价格
图31 - MiniMax：输入价格
资料来源：Artificial Analysis,JEF

资料来源：Artificial Analysis,JEF
注：MiniMax-M3的输入Token数 > 512k

图32 - MiniMax：输出价格
图33 - 豆包Seed：输入价格
资料来源：Artificial Analysis,JEF
注：MiniMax-M3的输入Token数 > 512k

资料来源：公司,JEF
注：doubao-seed-2.0-pro、doubao-seed-1.8的输入Token数在128k < 输入Token数 <= 256k范围内

图34 - 豆包Seed：输出价格
资料来源：公司,JEF
注：doubao-seed-2.0-pro、doubao-seed-1.8的输入Token数在128k < 输入Token数 <= 256k范围内

图35 - 小米：输入价格
资料来源：Artificial Analysis,JEF

图36 - 小米：输出价格

图37 - 腾讯：输入价格
资料来源：Artificial Analysis,JEF
资料来源：公司,JEF

图38 - 腾讯：输出价格
图39 - 百度：输入价格
资料来源：公司,JEF

资料来源：Artificial Analysis,JEF
注：32k < 输入Token数 <= 128k

图40 - 百度：输出价格

图41 - StepFun：输入价格
资料来源：Artificial Analysis,JEF
资料来源：Artificial Analysis,JEF
注：32k < 输入Token数 <= 128k

图42 - StepFun：输出价格
资料来源：Artificial Analysis,JEF

图43 - OpenAI：输入价格
资料来源：Artificial Analysis,JEF

图44 - OpenAI：输出价格
资料来源：Artificial Analysis,JEF

图45 - Anthropic Claude Opus：输入价格
资料来源：Artificial Analysis,JEF

图46 - Anthropic Claude Opus：输出价格
资料来源：Artificial Analysis,JEF

图47 - Anthropic Claude Sonnet：输入价格
资料来源：Artificial Analysis,JEF

图48 - Anthropic Claude Sonnet：输出价格
资料来源：Artificial Analysis,JEF

图49 - 模型定价趋势

资料来源：公司,JEF

图50 - 模型定价趋势（续）

## 视频生成模型产品

红色表示当月价格上涨/新价格

不同视频生成模型的定价方案

图51 - 视频生成模型定价（人民币）

资料来源：各公司,JEF

图52 - 视频生成模型定价（美元）

资料来源：各公司,JEF

图53 - 视频生成会员比较（原价）

资料来源：公司,JEF

图54 - 视频生成会员比较（促销后）

资料来源：公司,JEF

## 公司估值/不确定性