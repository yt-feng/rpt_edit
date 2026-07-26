# MS：AMDAI活动回顾与要点

AMD在2026年7月的AI活动上，将2030年服务器CPU市场总规模预测从1200亿美元上调至约2200亿美元，年复合增长率达到50%。这一数字在2025年10月的分析师日上仅为600亿美元，18个月内预测值翻了近4倍。MS在活动后发布的报告中指出，CPU需求增长的幅度是整场活动最乐观的数据点，也是AMD当前具有明确领先优势的领域。

与此同时，AMD正式推出Helios产品，将72颗Instinct MI455X GPU与18颗第六代EPYC“Venice”CPU及Pensando智能网卡整合。报告测算，Helios每美元可产出的推理token数比Nvidia高出30%，其计算性能领先15%，HBM容量和带宽高出50%，扩展带宽高出50%。Helios已进入全面生产阶段，预计三季度末开始出货，四季度放量。

![研报原图 1](assets/source_image_01.jpg)

## 1. 服务器CPU市场预测在18个月内从600亿升至2200亿美元

MS在报告中梳理了AMD对服务器CPU市场总规模的预测变化：2025年10月分析师日时为600亿美元（年复合增长率18%），2026年4月财报电话会上调至1200亿美元（35%），本次AI活动进一步上调至2200亿美元（50%）。报告认为，这一上调速度“前所未有”，也暗示AMD即将公布的数据中心业务数据可能非常强劲。

> **KC评论：** 预测值在8个月内弹性较高、18个月内翻近4倍，本身并不代表市场真实规模，但反映了AMD内部对CPU需求判断的急剧转向。报告也坦承，如果8个月前的预测偏差如此之大，当前数字的置信度同样需要审慎看待。

![研报原图 2](assets/source_image_02.jpg)

## 2. Helios性能指标明确，但生态系统成熟仍需时间

报告详细列出了Helios的技术参数：相比上一代MI355X，MI455X在FP8和FP16算力上分别提升约2倍和1.5倍，HBM3e容量从192GB增至288GB，内存带宽从5.2TB/s提升至8TB/s。AMD还发布了面向HPC和主权AI工作负载的MI430X，配备原生FP64硬件，算力达288 TFLOPS，已进入美国橡树岭国家实验室和欧洲CSN/Genci的百亿亿次系统。

在软件生态方面，AMD推出rocm.ai代理层，让Claude、Codex、Cursor等现有编码代理原生理解AMD硬件和ROCm，实现内核自动选择、调优和优化。AMD演示了在MI355上优化MiniMax M3后每秒token数提升38%，并宣称DeepSeek模型在ROCm上的平均训练加速2.4倍、推理加速3.3倍。ROCm的发布周期也从每4个月缩短至每6周。

![研报原图 3](assets/source_image_03.jpg)

## 3. 与Cerebras合作提供推理替代方案，CPU路线图延伸至2030年

Cerebras CEO Andrew Feldman在活动上宣布，将Helios机架与Cerebras晶圆级引擎整合，推出联合分离式推理方案，目标实现5倍吞吐量提升，今年晚些时候通过Cerebras云提供服务。MS认为，这一合作可能成为对抗Nvidia（通过收购Groq整合标准GPU与SRAM方案）的重要力量。

在CPU路线图上，AMD披露了后续产品规划：2028年推出Zen 7架构的“Florence”“Ferrara”和“Fidenza”CPU，2030年推出Zen 8架构的“Ravenna”。GPU方面，2027年推出MI500系列，宣称四年内推理性能提升超过2000倍；2028年推出MI600系列。Helios 500和Helios 600机架平台将随这些GPU代际同步更新。

## 4. 企业端与客户端同步推进，物理AI领域推出Kria平台

在企业市场，AMD发布了风冷版MI350P，目标对标Nvidia RTX 6000。AT&T CTO登台介绍了基于AMD硬件训练的开源电信模型Otel 2.0。客户端方面，AMD推出Ryzen AI Halo（120GB统一内存，支持200B参数模型），并预览了“Gorgon Halo”（192GB统一内存，支持300B参数模型），均捆绑一年Hugging Face Pro订阅。

在物理AI领域，AMD推出基于Ryzen AI Embedded X100的Kria AI系统模组和机器人开发平台，声称实时性能比Nvidia Jetson Thor好3.4倍，并发代理数量多2.3倍。

> **KC评论：** 从CPU到GPU再到机器人，AMD试图在每个计算节点都建立产品覆盖。但报告也指出，客户证言虽然显示Helios在2027年将强劲上量，但长期竞争力仍需时间验证。AMD通过收购ZT的机架工程业务和客户认股权证结构（虽然成本高昂）来加速生态采用，这些举措的方向正确，但本代产品仍不处于领先位置。

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>

![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>
