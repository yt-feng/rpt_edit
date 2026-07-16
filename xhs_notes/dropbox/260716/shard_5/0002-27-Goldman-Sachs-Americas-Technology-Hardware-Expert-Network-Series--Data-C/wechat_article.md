# 研究笔记：数据中心网络设备2026年7月展望

一份来自行业专家研讨会的判断正在改变数据中心研究的传统认知：以太网交换市场将在2035年突破2000亿美元，而驱动这一增长的并非传统的服务器升级，而是AI网络架构对带宽和互联密度的根本性重构。650 Group创始人Alan Weckel在7月14日的分享中给出了一个关键信号——网络设备在数据中心基础设施资本开支中的占比将持续扩大，这一趋势才刚刚开始。

当前市场普遍关注GPU算力的直接采购，但网络层的研究滞后性意味着，真正的网络设备需求高峰可能要到2027-2028年才会充分显现。数据中心运营方仍在摸索计算互联的具体需求规模，这为网络设备厂商提供了超出当前市场预期的增长空间。

![研报原图 1](assets/xhs_card_01.png)

## 1. 以太网正在从“机架互联”走向“GPU互联”，与NVLink正面竞争

传统上，以太网在AI数据中心主要负责scale-out网络，即机架与机架之间的数据交换。但650 Group认为，以太网将在scale-up网络（GPU到GPU的直接互联）中占据越来越大的份额。这意味着以太网将直接与NVIDIA的NVLink技术竞争，成为多厂商加速器生态下的标准化互联方案。

这一转变的关键在于，随着AI训练和推理对带宽需求的指数级增长，单一厂商的封闭互联方案可能无法满足多样化硬件组合的灵活性要求。以太网的开放性和成熟生态，使其成为数据中心运营方在构建异构算力集群时的自然选择。

> **KC评论：** 这里容易被忽略的是，以太网在scale-up领域的渗透不是替代NVLink，而是填补NVLink覆盖不到的场景——特别是当数据中心采用多家厂商的GPU时，以太网成为相对少见的通用互联语言。

## 2. 园区网络正在经历“AI就绪”驱动的超周期，增速从2倍GDP跃升至4倍

企业园区网络市场正在经历一轮超出历史规律的扩张。传统上，园区网络增长约为GDP增速的2倍，但650 Group预计当前周期将增长至约4倍。两个因素在推动这一变化：一是企业对Project Glasswing（一项涉及网络安全的监管或技术担忧）的应对，导致IT预算向网络设备倾斜；二是设备更新周期进入关键窗口——Cisco的pre-Cat9K系列产品将在未来一年内陆续停止支持，同时Wi-Fi 7的升级需求正在释放。

这意味着，企业网络设备采购不再只是例行更新，而是与AI就绪和网络安全合规深度绑定的战略性支出。对于网络设备厂商而言，这一轮需求的结构性更强，持续性也更长。

## 3. 传统服务器市场预期被大幅上调，网络升级将紧随其后

650 Group将2026-2030年传统服务器市场的年度预测平均上调了约31%，预计到2030年市场规模将达到约1640亿美元。这一增长并非来自AI服务器的直接拉动，而是源于现有CPU服务器基数的更新换代——新一代服务器拥有显著更高的核心密度，能够在提升数据中心整体能效的同时，支撑AI Agent与数据库、应用层之间日益密集的数据交互。

但更值得关注的判断是：传统服务器的算力升级之后，网络升级将紧随其后。为了匹配更高核心密度带来的带宽需求，数据中心需要将网络系统升级至400G甚至800G。这意味着，服务器采购的加速将直接转化为网络设备需求的增量，且这一传导链条在时间上存在明确的先后顺序。

> **KC评论：** 报告没有完全展开的是，这种“先算力后网络”的节奏意味着，网络设备厂商的订单可见性可能比服务器厂商滞后6-12个月，但需求的确定性反而更高——因为算力已经部署，网络必须跟上。

## 4. DCI市场五年复合增速29%，AI跨数据中心互联是最大变量

数据中心互联（DCI）市场预计将从2025年的约90亿美元增长至2030年的约330亿美元，五年复合增长率约29%。其中，AI驱动的scale-across网络（数据中心之间的互联）增速高达96%，是非AI DCI增速（约18%）的5倍以上。

这一数据揭示了一个被低估的趋势：AI工作负载不仅需要单数据中心内的算力集群，还需要跨数据中心的协同训练和推理。随着模型规模持续扩大，单一数据中心无法容纳全部算力，跨数据中心互联将成为AI基础设施的刚性需求。而这一领域的网络设备供应商，将受益于比数据中心内部网络更长的增长周期。

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>

![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>
