# MS：AI芯片的“库存担忧”被高估了，2027年才是真正的放量年

市场对AI芯片库存的讨论，最近有些过度。MS最新发布的AI供应链追踪报告，给出了一个直接且有力的判断：Blackwell芯片所谓的“库存”，本质是供应链缓冲，到2026年将被完全消化，无需担忧。更关键的是，这份报告首次系统性地拆解了2027年的CoWoS产能分配与芯片出货量，揭示出一个被当前讨论忽视的结构性趋势——AI芯片的竞争格局，正在从“GPU单极”走向“GPU+ASIC双轮驱动”。

这份报告最值得关注的，不是某个季度的出货预期修正，而是它提供的2027年全局视图。当市场还在为季度波动争论时，MS已经用数据证明：AI基础设施的研究周期远未结束，只是驱动力正在发生变化。

> **KC评论：** 报告的真正价值不在于预测数字本身，而在于它给出了一个可验证的框架——用CoWoS产能反推芯片出货，再折算成HBM消耗和整机需求。这比单纯跟踪季度出货更接近真实需求。


![研报原图 1](assets/source_image_01.jpg)

## 1. AMD的CoWoS分配不变，但执行不确定性是2027年的关键变量

市场对AMD的CoWoS分配有过疑虑。MS维持了AMD 2027年24万片CoWoS的预期，MI455和MI450合计出货150万颗。但报告也明确提醒：AMD过去有削减CoWoS订单的记录，2027年的执行不确定性不能忽视。

值得注意的结构性变化是AMD产品线的分化。MI455是标准版，面向微软、AWS和Oracle；MI450则是为Meta定制的半尺寸芯片。这种定制化策略，一方面降低了单一客户的依赖，另一方面也意味着AMD正在从“通用GPU供应商”向“半定制化方案商”转型。这对供应链的弹性提出了更高要求。

另一个被忽视的信号是AMD的Venice CPU。作为AMD首款采用CoWoS的CPU，2027年出货量预计达到570-600万颗，是2026年的5-6倍。这意味着CoWoS的需求不再仅仅来自GPU，CPU的先进封装需求正在成为新的增长极。


![研报原图 2](assets/source_image_02.jpg)

## 2. Google TPU的节奏变化，暴露了ASIC赛道的两个关键转折点

Google TPU的进展是这份报告中最值得细读的部分。Sunfish（TPU v8i）的出货节奏从3季度推迟到4季度，导致KYEC 3季度营收增速低于预期。但报告判断，这不是订单削减，而是集中出货的时间后移。

更重要的信息来自两个维度。一是Zebrafish（TPU v8t）的量产时间没有变化，仍按原计划在4季度启动。二是TPU v9（Humufish）已经进入规划，采用2nm制程和HBM4e。这说明Google的ASIC路线图正在加速迭代，从一代到下一代的周期在缩短。

> **KC评论：** 报告没有直接说，但可以推导出一个判断：ASIC的迭代速度正在追赶GPU。如果Google能在两年内完成从TPU v8到v9的跨越，那么定制化芯片对通用GPU的替代效应，将在2028-2029年显著加速。


![研报原图 3](assets/source_image_03.jpg)

## 3. 2027年CoWoS总产能将超过260万片，但分布结构正在改变

MS给出的2027年全球CoWoS产能预测是266.4万片。这个数字本身已经很大，但更值得关注的是结构变化。

NVIDIA的占比将从2025年的62%下降到2027年的45%，而AMD从9%上升到20%，MediaTek则从0%跃升到7%。MediaTek的崛起主要来自Google TPU v8t和v9的订单。这是一个重要的信号：AI芯片的封装需求正在从单一供应商向多元化演变。

另一个结构性变化是OSAT（外包封测）的参与度提升。ASE/SPIL、Amkor和Powertech都在增加CoWoS产能。2027年，非台积电的CoWoS产能将达到约50万片，占总量近20%。这意味着台积电在先进封装领域的垄断地位正在松动，虽然它仍是最重要的供应商，但供应链的弹性正在增强。

## 4. 报告尚未完全回答的关键问题：CoWoS产能扩张的瓶颈在哪里

这份报告给出了详细的产能分配，但有几个关键问题没有完全展开。

第一，CoWoS-L和CoWoS-R的技术成熟度是否足以支撑2027年的量产目标？NVIDIA在2027年有13万片CoWoS-R的规划，而AMD的CoWoS-L达到了23万片。这些新技术路线的良率和产能爬坡速度，将是影响出货量的最大变量。

第二，HBM4的供应能否匹配？报告预测2027年HBM总需求将达到60亿Gb，其中HBM4和HBM4e占比超过70%。如果三星或美光在HBM4的量产上遇到问题，整个供应链都会受到影响。

第三，Meta取消的2nm ASIC项目（Olympus）被Apollo取代，但量产时间要到2028年。这意味着Meta在2027年的ASIC贡献可能低于预期。这对Broadcom和GUC的影响，报告没有深入分析。

这些未解问题，恰恰是跟踪AI供应链时需要持续关注的变量。

## 5. 对读者的观察框架：从“芯片出货量”转向“CoWoS产能利用率”

这份报告提供了一个更可靠的观察框架。过去市场习惯跟踪GPU出货量，但出货量会受到库存、客户提货节奏等因素干扰。更稳定的指标是CoWoS产能利用率和分配比例。

建议关注三个维度。第一，台积电CoWoS产能的季度环比增速。如果连续两个季度低于预期，可能意味着需求端出现了变化。第二，非台积电OSAT的CoWoS产能爬坡速度。这是判断供应链瓶颈是否缓解的关键。第三，HBM4的良率和供应商切换节奏。HBM是AI芯片性能的瓶颈，也是2027年最大的供应链不确定性点。

当市场讨论从“芯片出货”转向“封装产能”时，意味着AI基础设施的研究逻辑正在从“量”的扩张转向“质”的效率提升。而这，才是这份报告最值得反复阅读的地方。


<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>

![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>
