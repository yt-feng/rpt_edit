# Bernstein：AMD在AI活动上发布Helios架构与路线图

AMD 在 7 月 22-23 日举办的 Advancing AI 活动上，发布了多项关键更新。Bernstein分析师 Stacy Rasgon 在活动后的报告中认为，整体信号相当积极。核心看点包括：Helios（MI450）架构正式发布，并公布了从 MI500 到 MI600 系列的年度机架级系统更新路线图；Anthropic 成为继 OpenAI 和 Meta 之后的第三家主要客户；公司大幅上调了 CPU 与加速器的 2030 年 TAM 预期。

这些更新共同指向一个判断：AMD 正在试图从一家以 GPU 追赶者身份被市场认知的公司，转向一个同时拥有 CPU 和 GPU 两条增长曲线的计算平台供应商。报告特别指出，公司同时受益于 CPU 和 GPU 两条业务线的基本面上升。

![研报原图 1](assets/source_image_01.jpg)

## 1. Anthropic 成为第三家 Helios 大客户，AMD 承诺研究 50 亿美元

Anthropic 与 AMD 达成的战略合作是本次活动中最具体的商业信号。根据协议，AMD 将向 Anthropic 研究至多 50 亿美元，双方还将围绕 ROCm 软件栈展开协作。Anthropic 计划部署高达 2GW 的计算能力，其中第一个 1GW 将于 2027 年上半年开始部署，目标是在 2027 年内完成大部分部署。

这一合作使 AMD 在 AI 客户名单上补上了重要一块。此前其 Helios 架构已获得 OpenAI 和 Meta 的采用。报告同时提到，AMD 还与微软达成了在 Azure 上大规模部署 Helios 的合作，但未提供具体目标。

> **KC评论：** 50 亿美元的研究规模值得注意。它既不是纯股权认购（报告明确提到“no warrants”），也不是简单的采购承诺。这笔资金更接近一种战略绑定——AMD 用资本换取了一个大客户在架构和软件层面的长期合作，尤其是在 ROCm 生态的共建上。

![研报原图 2](assets/source_image_02.jpg)

## 2. CPU 与加速器 TAM 预期大幅上调，代理型 AI 是主要驱动力

AMD 在活动中将 2030 年 CPU TAM 从三个月前给出的 1200 亿美元上调至 2200 亿美元。这意味着从 2025 年 260 亿美元的基数出发，年复合增长率超过 50%。报告指出，增长的主要驱动力来自代理型 AI（agentic AI）。

加速器 TAM 的预期同样被大幅上调。AMD 预计到 2030 年，加速器 TAM 将达到 1.4 万亿美元，对应约 45% 的年复合增长率，主要受推理支出推动。整体计算 TAM 预计在 2030 年达到约 2 万亿美元。

这些数字本身带有公司自我叙事色彩，但上调幅度之大——尤其是 CPU TAM 在三个月内几乎弹性较高——反映了 AMD 对 AI 推理需求向 CPU 侧扩散的判断。代理型 AI 需要更多 CPU 节点来承载推理前的调度、编排和数据处理，这可能是 AMD 认为其 CPU 业务能获得额外增长空间的核心逻辑。

![研报原图 3](assets/source_image_03.jpg)

## 3. 产品路线图覆盖从机架级到企业级的多层市场

AMD 在活动上展示了从高端到入门级的完整产品矩阵。在高端市场，Helios 架构的 MI455X 预计在 2025 年第三季度开始出货，第四季度放量。MI500 和 MI600 系列分别计划在 2027 年和 2028 年推出，保持年度更新的节奏。

在企业级市场，AMD 推出了 Instinct 350P GPU，定位为非前沿工作负载的本地数据中心提供高性价比方案。在个人 AI 计算领域，Ryzen AI 400 和 Ryzen AI Max 可运行 24B 到 200B 参数的模型。此外，AMD 还发布了面向机器人开发的 KRIA AI Robotics 平台。

CPU 方面，下一代 Venice 系列将提供多个变体，分别针对 GPU 服务器主机节点、代理型 CPU 服务器（高核心数、高 ASP 的 Venice 256c）以及通用 CPU 服务器。管理层认为，其 CPU 组合在与 x86 和 Arm 架构的竞争中具有优势，有望继续获得市场份额。

## 4. ROCm.AI 与 Cerebras 合作：软件生态与低延迟推理的双线布局

AMD 在软件层面推出了 ROCm.AI，一个利用 AI 来加速 GPU 性能优化和编程的开发平台。报告将其描述为 AMD 对 NVIDIA CUDA 护城河的回应。该平台基于核心 ROCm 软件栈，集成了 AI 编码代理，能够帮助生成代码以优化 GPU 性能。

在推理架构层面，AMD 与 Cerebras 宣布合作，目标是结合 AMD Instinct GPU 的高吞吐量与 Cerebras 的超低延迟 token 生成能力。报告指出，这一合作与 NVIDIA 对 Groq 采取的策略类似，但 NVIDIA 的做法可能更加集成。Cerebras 计划在 2026 年下半年通过其云服务提供首个联合解决方案。

> **KC评论：** 与 Cerebras 的合作值得关注，但技术细节仍然有限。推理工作负载正在变得高度异质化——客户对延迟、吞吐量、token 容量和成本的要求各不相同。AMD 选择与 Cerebras 合作而非自研低延迟方案，说明其当前策略更倾向于通过生态组合来覆盖不同场景，而不是在每个环节都与 NVIDIA 正面竞争。这种策略能否在客户部署中形成差异化，取决于联合方案的落地速度和实际性能表现。

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>

![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>
