# MS：中国AI基础模型K3，MS观点

7月17日，月之暗面发布K3——一个2.8万亿参数的开源大模型，在Artificial Analysis全球排名中位列第三，仅次于两家美国头部模型。在Arena.ai编程排行榜上，K3直接拿下全球第一。API定价也创下中国大模型新高：输出每百万token 100元，是DeepSeek V4-Pro的16倍以上。

这份MS研报的核心判断是：K3不是一夜之间的技术突破，而是中国大模型行业在模型规模、性能和定价三个维度上全面追赶美国领先者的累积拐点。报告特别强调，K3的全球正面反馈信号意义大于技术本身——它意味着缩放定律（Scaling Law）在中国依然有效，且中国模型厂商开始有能力在高端市场定价。

![研报原图 1](assets/source_image_01.jpg)

## 1. 2.8万亿参数背后的算法创新，而非简单堆算力

K3的规模是此前中国最大开源模型GLM-5.2（7540亿参数）的近4倍，是DeepSeek V4-Pro（1.6万亿参数）的1.75倍。但MS分析师指出，真正值得关注的是K3使用的原创算法——Kimi Delta Attention和Attention Residual，这两项创新提升了计算效率，使得模型在长任务、知识工作和推理场景中表现突出。

报告将K3定位为“中国大模型在模型架构层面的追赶”，而非简单的参数竞赛。这一点从K3的上下文窗口（100万token）与同行基本持平可以看出——真正的差异化来自注意力机制的效率改进。

> **KC评论：** 参数规模大不等于模型好，但K3在编程和综合智力两个独立榜单上的排名（全球第一和第三），说明它的效率改进是真实的。对于关注AI基础设施的读者，需要留意的是K3的开源策略——完整权重将在7月27日前发布，这意味着全球开发者社区可以验证和复现其能力。

![研报原图 2](assets/source_image_02.jpg)

## 2. 定价策略的转变：从价格战转向价值定价

K3的API定价是中国大模型中最高的，输出价格是DeepSeek V4-Pro的16倍，是MiniMax M3的8倍。MS认为，这一高定价策略对整体大模型市场格局是积极信号——它打破了此前中国大模型行业“免费或低价”的竞争惯性。

报告对比了6家中国前沿大模型的定价：阿里Qwen3.7-Max输出36元/百万token，智谱GLM-5.2输出28元，而K3直接定到100元。这种定价差异反映了模型定位的分化——K3明确瞄准高价值的知识工作和复杂推理场景，而非通用对话。

对于行业而言，这意味着中国大模型市场正在从“谁便宜谁赢”转向“谁好用谁有定价权”。K3的高定价能否被市场接受，将成为检验中国大模型商业化能力的关键测试。

![研报原图 3](assets/source_image_03.jpg)

## 3. 累积进步的产物，而非孤立的技术突破

MS特别强调，K3不应被视为“一夜奇迹”。报告指出，智谱GLM-5.2在今年6月发布时已经表现出色，K3是在此基础上的进一步跃升。从时间线看：DeepSeek V4-Pro（4月）、小米MiMoV2.5Pro（4月）、阿里Qwen3.7-Max（5月）、MiniMax M3和GLM-5.2（6月）、K3（7月）——中国大模型在过去4个月里密集发布，性能持续提升。

报告预期，接下来会有更多规模更大、定价更高、性能更好的中国大模型出现，且具备全球竞争力。这一判断基于两个观察：一是缩放定律在中国依然成立，二是中国模型厂商在算法创新上开始形成自己的路径。

对于产业决策者，这意味着中国AI基础设施的竞争格局正在快速收敛——头部模型厂商的差距在拉大，而K3的出现可能加速这一分化。那些无法在模型性能或定价上建立差异化的厂商，将面临更大的市场不确定性。

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>

![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>
