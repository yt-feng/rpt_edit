# 观察：AMD与Anthropic和微软合作推进AI部署

AMD 在旧金山举办的 Advancing AI 大会上释放了一系列信号。观察团队现场参加后认为，读者原本就对这次活动抱有建设性预期，而本周公布的几项合作与产品发布，基本满足了这些期待。

最引人关注的是 AMD 与 Anthropic 的战略合作。根据协议，Anthropic 将从 2027 年上半年开始部署 2GW 的 Instinct MI450 GPU Helios 机架系统，首批 1GW 预计在 1H27 启动。AMD 还计划对 Anthropic 进行最高 50 亿美元的战略股权研究。双方的合作不止于硬件采购，还包括在 AMD GPU 上优化 Claude 工作负载、加速 ROCm 软件平台开发，以及在 AMD 工程和产品团队中推广 Claude 的使用。

另一个重要合作方是微软。微软计划从 2026 年下半年开始部署 Helios 机架，并在 Azure 上使用 AMD 的 CPU、网络设备和软件。Azure 将把 Helios 用于前沿模型的推理工作负载，以及微软自身的 AI 服务和 Azure 客户应用。Azure 还将推出基于 AMD 下一代 2nm Venice CPU 的新虚拟机，并扩大 AMD Pensando DPU 在 Azure 网络服务中的应用。

> **观察评论：** 这两项合作的关键不在于采购规模，而在于客户类型。Anthropic 代表前沿 AI 模型公司，微软代表云服务商，AMD 同时拿到了两类客户，这比单一订单更有结构意义。50 亿美元股权研究也值得注意——这不是单纯的客户关系，而是更深层的绑定。


![研报原图 1](assets/source_image_01.jpg)

## 1. 数据中心与 CPU 市场规模预期上调

AMD 在大会上更新了市场预期。公司认为，代理式 AI 正在推动计算需求的变化，加速器和 CPU 都需要处理越来越复杂的工作流。具体数字是：数据中心 AI 加速器 TAM 从 2000 亿美元增长到 2030 年的 1.4 万亿美元（年复合增长率 40%）；数据中心 CPU TAM 从 260 亿美元增长到 2200 亿美元（年复合增长率 50%）；AMD 的总计算 TAM 从 3650 亿美元增长到 2 万亿美元。AMD 还预计到 2030 年将占据数据中心 CPU 市场 50% 的份额。

这些数字本身很大，但报告没有展开的是：TAM 上调背后的假设是什么。代理式 AI 对计算需求的影响，目前仍处于早期阶段，实际落地节奏存在不确定性。


![研报原图 2](assets/source_image_02.jpg)

## 2. Helios 平台已进入量产阶段

AMD 发布了下一代 Helios AI 机架平台，基于 CDNA 5 架构，GPU 最高可达 40 PFLOPS（FP4）、20 PFLOPS（FP8），配备 432 GB HBM4 内存和 23.3 TB/s 内存带宽。系统由 75 个 GPU 通过以太网 UALink 连接，搭配 EPYC CPU、Salina DPU、Volcano 800G AI NIC 和六个网络托盘。AMD 表示 Helios 已进入全面生产，出货从三季度末开始，四季度放量。

此外，AMD 与 Cerebras 合作，将 Helios 系统与 Cerebras 的晶圆级引擎结合，目标是在 2026 年下半年通过 Cerebras Cloud 提供推理解决方案，宣称每瓦 token 数提升 5 倍。


## 3. ROCm.ai 与 Hyperloom 优化层提升软件生态

AMD 推出了 ROCm.ai 平台，集成 Cursor、Claude、Codex、Gemini 等工具，为开发者提供 AI 驱动的软件开发体验。同时发布的 Hyperloom 优化层，可以自动调整系统配置并优化端到端 AI 工作负载。AMD 称已有超过 14,000 个模型通过 Hyperloom 优化，相比 ROCm 7 平均性能提升 3.3 倍。

软件生态一直是 AMD 在 AI 领域的关注点。这次发布的 ROCm.ai 和 Hyperloom，至少在工具链和优化层上给出了具体方案。14,000 个模型和 3.3 倍性能提升是可验证的指标，但实际部署效果还需要看开发者社区的反馈。

报告也列出了几个需要关注的不确定性：代理式 AI 采用速度、AMD GPU 部署节奏、不同架构在企业 AI 中的应用变化，以及运营层面的效率。


<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>

![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>
