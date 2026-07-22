# BofA：美国半导体存储芯片需求与开源模型扩展TAM

中国AI公司推出的开源大模型定价远低于西方竞品，但BofA半导体团队在最新报告中指出，这更多是商业模式选择，而非硬件成本的真实反映。Kimi K3等模型虽然API价格只有Claude Opus的几分之一，但每个服务实例仍需要约1.4TB的HBM容量。报告的核心判断是：开源模型的扩散反而扩大了存储芯片的终端市场，因为每个下载权重的企业都需要自建硬件部署环境。

![研报原图 1](assets/source_image_01.jpg)

## 1. 开源模型权重规模持续增长，直接拉动HBM需求

BofA统计显示，前沿开源模型的参数规模从DeepSeek-V3的671B（2024年12月）增长到Kimi K3的2.8T（2026年7月），两年内增长超过4倍。即便采用MXFP4原生低比特量化将存储需求压缩一半，K3所需的权重内存仍达到1.4TB，是DeepSeek-V3在FP8精度下的两倍。

关键机制在于：MoE架构虽然通过稀疏激活大幅降低计算量（K3每次只激活50B参数），但全部专家权重必须常驻HBM。HBM容量与总参数规模直接相关，而非活跃参数。这意味着模型规模每翻一倍，每个服务实例所需的HBM也翻一倍。

> **KC评论：** 市场容易将“效率提升”等同于“存储需求下降”。但BofA的数据表明，参数规模的增长速度远快于量化压缩带来的节省。K3的2.8T参数在4-bit精度下仍需要1.4TB HBM，这个数字比DeepSeek-V3在FP8下的671GB还要高出一倍。

![研报原图 2](assets/source_image_02.jpg)

## 2. 开源模型复制内存终端，而非共享

报告区分了两种部署模式对存储需求的不同影响。闭源模型（如GPT-5.6）的权重只存放在少数Azure数据中心，全球用户共享同一份HBM池。而开源模型每被下载一次，就产生一个新的硬件部署节点。

以Kimi K3为例，Moonshot官方建议每个服务实例需要64个以上加速器。每个下载该模型的企业、机构或云服务商，都需要独立配置这一规模的HBM集群。报告估算，如果10,000家企业自托管同一个开源模型，就需要10,000份独立的HBM池。这些存储需求在闭源API模式下根本不会存在。

![研报原图 3](assets/source_image_03.jpg)

## 3. 中国模型的低价策略源于非硬件因素

BofA拆解了中国模型定价优势的来源。架构效率方面，极端的MoE稀疏性（K3激活率仅1.8%）、MLA混合注意力机制（KV缓存压缩10-90倍）以及原生低比特量化，合计带来每token 2-3倍的计算效率提升。基础设施成本方面，中国电价、工程师薪酬和土地成本比美国低1.5-2倍。

但报告特别指出，Moonshot在K3发布后48小时内暂停了新订阅，小米在2026年5月将MiMo模型价格削减99%。这些信号暗示，低价策略可能伴随亏损运营，而非真实的硬件成本优势。如果K3的低价真正反映了硬件节省，Moonshot应该有能力预置足够的GPU容量。

## 4. 中国存储厂商在AI存储领域竞争有限

报告提及长鑫存储（CXMT）正在积极扩产，目前已占全球晶圆产能的10%左右。但BofA认为，CXMT主要面向消费级和通用DRAM市场，而非HBM3E/HBM4。美国OEM厂商短期内也不太可能获得批准采购CXMT产品。

> **KC评论：** 中国存储厂商的产能扩张对AI存储芯片的竞争格局影响有限。真正值得关注的是，美光在2026年12月将解除CHIPS法案相关的回购限制，届时可能启动每年500-600亿美元的公司回购计划，约占其1万亿美元市值的5-6%。

报告的核心逻辑链条清晰：开源模型参数规模增长快于效率提升，每个部署节点独立消耗HBM，中国模型的低价策略扩大整体推理需求而非压缩硬件需求。这些因素共同指向存储芯片需求的持续扩张，而非市场担忧的见顶。

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>

![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>
