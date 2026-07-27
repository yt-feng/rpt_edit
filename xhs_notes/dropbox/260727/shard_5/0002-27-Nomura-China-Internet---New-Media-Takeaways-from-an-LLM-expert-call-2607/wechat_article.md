# 学习笔记：中国互联网-新媒体-LLM专家交流，3万亿参数与效率竞争

中国大模型开发商的下一阶段竞争，不再只看参数规模。相关研究团队在与一家头部大模型厂商专家交流后认为，模型持续扩展、模型与智能体框架深度整合、以及系统级token宏观环境学，正在成为三个相互关联的竞争主轴。其中，DeepSeek试图同时在这三个方向上缩小与海外前沿模型的差距，同时保持结构性更低的成本基础和更低的token定价。

![研报原图 1](assets/xhs_card_01.png)

## 1. 参数规模仍在增长，但效率成为新的区分维度

中国大模型正在向万亿参数架构演进。专家认为，约3万亿参数是中国大模型的下一个实际里程碑。更大规模的算力集群、超节点、高速互联和光网络是支撑这一趋势的基础设施前提。

但单纯参数扩展的边际回报正在递减。模型竞争力将越来越多地取决于架构效率和训练后优化、内存管理、工具调用的可靠性以及长周期任务表现。这意味着，参数规模本身不再是竞争壁垒，工程效率正在成为新的区分维度。

> **学习笔记：** 3万亿参数这个数字本身不是重点，重点是专家明确说“纯参数扩展接近收益递减”。这提示读者，评估中国大模型公司时，不能只看参数规模排名，更要看单位参数的实际产出效率。

## 2. 模型与智能体框架的深度整合正在创造数据飞轮

DeepSeek推迟V4正式发布，部分原因是在智能体框架层面进行调试和优化。其目标是构建一个与Claude Code或Codex类似的一体化产品，覆盖专业软件开发和更广泛的知识工作场景。

这种深度整合可能创造专有数据飞轮。任务轨迹、工具调用、用户修正、执行失败和真实工作流，都可以转化为模型和产品改进的反馈。竞争优势正在从独立模型转向模型-智能体集成系统。这意味着，单纯发布一个更强的基座模型，已经不足以建立长期壁垒。

## 3. DeepSeek的结构性成本优势支撑其价格领导地位

DeepSeek将自己定位为性价比领导者。专家估计，假设60%的缓存命中率，其综合推理成本低于每百万token 0.8元人民币，而综合售价约为每百万token 1.3元人民币。这意味着推理贡献毛利率约40%，尽管V4代产品价格下降了约75%。

专家将DeepSeek的成本优势归因于更高效的注意力机制和内存管理，包括将KV缓存卸载到NVMe SSD，以及更高的基础设施利用率和在国内加速器上的大规模部署。DeepSeek正在通过架构和基础设施优化降低成本曲线，并将部分节省通过更低的token价格传递给客户。

> **学习笔记：** 40%的推理毛利率在降价75%后仍然成立，这个数字本身值得注意。它说明DeepSeek的成本优化不是一次性工程，而是架构层面的结构性优势。对于关注大模型商业化的读者，这是评估价格战可持续性的关键锚点。

## 4. AI-in-the-loop正在缩短模型领先周期，开源成为分发杠杆

专家估计，单代模型的竞争领先时间已从约六个月缩短到三到四个月。AI-in-the-loop是主要驱动因素。自动评估、LLM-as-a-Judge、多模型评分和教师模型反馈，正在变得比传统人工标注更重要。可持续的差异化将来自计算规模、专有用户交互以及从真实工作流中自动提取高质量训练信号的能力。

DeepSeek的海外增长由开发者驱动。专家估计其截至2026年6月的ARR约为5.2亿美元，海外市场贡献约47-48%。海外用户集中在欧洲和美国，其次是日本、韩国和澳大利亚。一个值得注意的模式是模型分层：开发者可能使用Claude Code或Codex进行初始规划、架构设计和复杂推理，然后切换到DeepSeek进行持续的代码生成和执行。DeepSeek不需要取代整个工作流中的前沿模型，它可以先捕获token密集的执行层，这一层使用量更高、价格敏感度更强。

开源策略虽然对直接商业化有不确定性，但可以降低采用门槛、扩大海外覆盖范围、促进跨云和硬件平台部署，并让海外客户保留对数据、基础设施和定制化的更大控制权。在行业层面，有能力的开源替代方案使闭源模型提供商更难维持高API溢价。

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>

![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>
