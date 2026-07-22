# JEF：中国AI策略转向务实-数据半导体成核心

中国AI策略在2026年世界人工智能大会上展现出清晰转向：从追求模型性能领先，转向以开源模式向新兴市场输出算力与绿色能源，并以此支撑其“一带一路”框架。JEF在最新发布的WAIC观察报告中指出，这一策略的核心支撑并非模型本身，而是半导体制造能力与数据基础设施。报告认为，中国AI玩家将维持开源路线，这对商业化变现并不友好，但有助于扩大生态影响力。同时，美国最可能的回应是进一步收紧芯片出口管制，并要求美国AI企业在其先进模型中嵌入反蒸馏功能。

> **KC评论：** 中国AI策略的底层逻辑正在从“追赶性能”转向“输出生态”。开源模式虽然牺牲了短期变现，但降低了新兴市场的使用门槛，这反过来可能对闭源模型的定价权形成结构性不确定性。报告没有直接讨论这种策略对全球AI定价体系的影响，但读者可以留意这一趋势。

![研报原图 1](assets/source_image_01.jpg)

## 1. 华为超级节点采用光学互联与堆叠DRAM，功耗是英伟达方案的7.4倍

华为在WAIC上发布了Atlas 950 SuperPoD，这是一个连接1024颗Ascend 950 GPU的超级节点设计，采用LPO光学模块互联，下一代将扩展至8192颗。该方案提供107.52 TB/s的内存带宽和2 EFLOPs算力，对比英伟达Vera Rubin NVL72的20.7 TB/s带宽和1.4 EFLOPs算力，性能指标领先。但代价是功耗高达1.7 MW，是Rubin NVL72的7.4倍。JEF认为，这一对比意味着中国IDC玩家将受益于更高的电力需求。此外，报告观察到两家中国GPU厂商采用3D DRAM技术，将4层DDR5通过混合键合堆叠在GPU上方，目标实现20+ TB/s带宽，接近HBM4水平。堆叠由中国OSAT厂商完成，DDR5由长鑫存储提供。但这些GPU仍基于14nm制程，因此这类完全本土化的方案更侧重内存带宽而非算力，报告认为这很可能由智能体AI推理需求驱动。

![研报原图 2](assets/source_image_02.jpg)

## 2. 中国在数据生成与智能体工具链上加速追赶

报告指出，美国在AI数据收集上长期领先，但文本数据已被基本耗尽，剩余数据多掌握在企业层面。中国自2022年提出“数据作为生产要素”政策后，2023年10月成立国家数据局，2026年计划设立一家中央国有企业，专门负责跨行业高质量数据集的收集、标注与交易。JEF认为，中国在数据标注上的成本优势依然明显，雇佣本地专业人士验证和贡献数据集的费用远低于美国。同时，中国AI厂商在智能体产品中已展现出较强的工具链能力，包括上下文管理、子智能体编排、工具调用、护栏机制和反馈循环管理。报告强调，对于智能体性能而言，工具链能力与模型智能同等重要。

![研报原图 3](assets/source_image_03.jpg)

## 3. 机器人仍是重要主题，但人形机器人展示明显减少

机器人展区占据WAIC约25%的展览空间，比例高于去年。但报告观察到，人形机器人的演示和展示数量显著下降，焦点转向轮式机器人。JEF认为，这意味着机器人厂商变得更加务实，降低了行业不确定性。报告重申其判断：人形机器人距离商业化仍有约5年距离，主要挑战包括算力（尤其对中国厂商）、昂贵的内存、散热、灵巧手所需的功率半导体与电机小型化，以及减速器等。轮式机器人在生产难度、成本和商业化前景上均更具优势。

## 4. AI智能手机仍面临生态与供应链挑战

一家中国AI厂商在WAIC上展示了自研AI智能手机，其操作系统由手机版大语言模型（10亿至100亿参数）驱动，内核仍基于Android，由ODM代工。JEF认为，OpenAI可能也有类似计划，但这类产品的体验与云端服务相比缺乏差异化。主要互联网平台可能出于安全或生态保护目的，阻止其API接入，导致应用生态受限。此外，硬件供应链议价能力不足和高企的内存价格也是现实障碍。

> **KC评论：** 报告对AI智能手机的判断相对谨慎，核心问题不在于技术可行性，而在于生态壁垒和成本结构。这与云端AI服务的竞争逻辑不同——手机端的AI需要同时解决硬件集成、应用生态和用户习惯三个层面的问题，任何一个环节的短板都可能限制渗透率。

## 5. 半导体制造能力被视为中国AI策略的最大研究方向

报告总结认为，中国AI策略的成功高度依赖半导体制造能力，包括逻辑芯片和存储芯片。杰富研报将中微公司和华虹半导体列为关键受益标的，认为大晶圆厂资本开支仍将维持高位。同时，报告提及中国AI模型Kimi 3在智能水平上已接近Anthropic的Fable 5，差距约为5%，这一进展使得中国开源模型有能力向新兴市场提供低成本选择。

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>

![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>
