# MS：GPU短缺的真正信号是云巨头开始“转租算力”

上周市场因Meta计划推出云服务而出现一轮调整，许多读者将其解读为超大规模厂商自身算力过剩的信号。MS半导体团队在最新周报中提出了一个完全相反的判断：这恰恰证明了GPU计算资源处于整体性短缺，而非某一家巨头的供给过剩。

报告的核心观点清晰而直接：当前GPU的最高效用途，就是租给其他人。

![研报原图 1](assets/source_image_01.jpg)

## 1. 云巨头转租算力，反映的不是过剩而是需求外溢

Meta计划推出面向外部客户的云服务，被部分市场参与者理解为该公司拥有“多余的GPU”。MS团队指出，这种解读忽略了关键事实——这已经不是他们第一次听到类似消息。多家原本以内部需求为主的超大规模厂商，正在定期向外部提供GPU算力。

报告认为，更合理的解释是：市场上存在大量无法被满足的GPU计算需求，以至于对于拥有GPU的厂商而言，出租算力比自用更能创造价值。这不是供给过剩的信号，而是需求外溢的证据。

> **KC评论：** 这个视角切换了对“云服务扩张”的理解。不是巨头闲得慌才做云，而是外部客户的需求太强，逼着它们把算力变成商品出租。完整报告里对Meta、微软、AWS等多家厂商的算力分配细节值得细看。

![研报原图 2](assets/source_image_02.jpg)

## 2. 英伟达是这一趋势的最大受益者，而非受害者

如果算力转租成为常态，谁最受益？MS的答案很明确：英伟达。

逻辑在于，当算力出现供需错配时，市场会倾向于选择行业事实标准——CUDA生态下的英伟达GPU。ASIC芯片几乎无法转租，尤其是小批量定制的ASIC。AMD的GPU虽然比ASIC更通用，但市场占有率远低于英伟达，意味着其可转租的二级市场体量有限。

报告还引用了英伟达在Computex上的论述：其GPU不仅提供最高的每千兆瓦token产出，还通过更快的部署速度、更长的平均无故障时间和更长的资产寿命，在总拥有成本上优于竞品。现在可以加上“算力通用性”作为另一个关键优势。

![研报原图 3](assets/source_image_03.jpg)

## 3. 5月SIA数据虽低于预期，但结构性改善逻辑未变

报告同时分析了5月半导体行业协会（SIA）数据。整体销售额环比增长16.1%，低于MS预测的22.0%，但显著高于10年均值6.9%。分项来看，模拟芯片和分立器件环比下滑，MPU和逻辑芯片则超出预期。

存储芯片方面，DRAM环比增长27.7%，低于预期但仍是历史高位；NAND环比增长40.7%，略低于预期但高于5年均值。报告指出，月度数据的波动并不改变核心判断——这是一个由AI驱动的结构性紧缺周期，而非传统的库存复苏。

> **KC评论：** 月度数据有噪音，但季度趋势已经非常清晰。报告中的季度SIA数据表（Exhibit 5）显示，2026年第二季度半导体销售额预计环比增长29.2%，同比增速将突破114%。这个增速本身已经说明问题。

## 4. 报告尚未完全回答的关键问题：算力转租的市场规模有多大

MS提出了“算力转租”这一趋势，但并未量化其市场体量。这是一个值得继续追问的方向：如果云巨头将GPU出租给外部客户，这一部分收入占其总云收入的比例会达到多少？是否会改变市场对英伟达GPU总需求的测算框架？

另一个未解问题是，AMD通过权证结构向Meta提供的GPU折扣（报告提到初始1 GW的算力实际折扣约75%）是否会在其他客户中复制，从而改变竞争格局。报告认为这对Meta而言是重大激励，但未展开对AMD市场份额的长期影响。

这两个问题，在完整报告中对各家公司的细分拆解和财务模型中可能有更深入的讨论。

---

以上是这篇MS周报的核心导读。完整的5月SIA数据图表、季度预测表、以及英伟达与AMD在算力转租场景下的竞争分析，会放进每日国际信源汇编中继续跟踪。适合快速把握本周半导体板块的核心叙事，也方便后续对单个公司做进一步追问和横向比较。

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>

![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>
