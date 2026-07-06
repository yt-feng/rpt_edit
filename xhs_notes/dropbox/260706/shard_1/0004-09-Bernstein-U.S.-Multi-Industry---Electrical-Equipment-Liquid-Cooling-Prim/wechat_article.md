# Bernstein：从铜块到精密设计，冷板护城河为何比CDU更浅？Bernstein给出行业判断

数据中心机架热密度持续攀升，单靠风冷已无法应对AI工作负载带来的散热挑战。Bernstein最新发布的冷板行业入门报告，在肯定液冷渗透率加速增长的同时，提出了一个值得产业决策者深思的判断：冷板这一核心组件，短期量价齐升的确定性很高，但远期面临商品化甚至被替代的双重不确定性。这份报告的价值不在于罗列市场规模数字，而在于拆解了冷板业务模式中“量增”与“利缩”的结构性矛盾。

![研报原图 1](assets/source_image_01.jpg)

## 1. 冷板是液冷架构中不可或缺的“热接触点”，但业务护城河天然较浅

在直接到芯片（DTC）液冷系统中，冷板是相对少见物理接触芯片的组件。它通过内部微通道中的冷却液，将GPU/CPU产生的热量传导至CDU（冷却液分配单元）进行循环散热。以NVIDIA GB200 NVL72机架为例，单机架就需要超过100块冷板——每块GPU和CPU各配一块。

然而，冷板本质上是一个精密加工的金属块（铜或铝），核心价值集中于设计而非系统级集成。与CDU相比，冷板的服务附加率明显偏低，制造商主要获取的是硬件毛利，而非更具防御性的服务收入。这意味着，随着设计标准化和制造规模化，创新溢价和稀缺溢价将逐步消失。

> **KC评论：** 冷板的技术门槛并不低——微通道加工精度、热界面材料匹配、两相流设计等都有工程壁垒。但Bernstein想强调的是，这些壁垒更多是“know-how”而非“IP”，一旦工艺成熟，代工厂可以快速复制。这与CDU涉及的系统集成和软件控制能力有本质区别。

![研报原图 2](assets/source_image_02.jpg)

## 2. 市场规模从当前20-30亿美元增长至2030年60-70亿美元，但单价假设已隐含商品化预期

Bernstein的底稿测算显示，冷板市场规模将从当前的20-30亿美元增长至2030年的60-70亿美元。这个数字背后包含了几个关键假设：液冷在新建设施中的渗透率从30-40%提升至2030年的多数采用；GPU功耗从当前水平上升至2000-3000kW（以Rubin架构估算）；以及冷板单价从2026年的0.30美元/kW下降至2030年的0.20美元/kW（基准情形）。

值得注意的是，单价下降的假设本身就是一个判断信号：Bernstein认为冷板将不可避免地被商品化。这与CDU市场形成鲜明对比——后者因系统复杂性更高、服务收入占比更大，单价压缩空间更小。

![研报原图 3](assets/source_image_03.jpg)

## 3. 两相冷板是中期竞争焦点，但远期存在被“直接硅蚀刻”颠覆的可能

报告将冷板技术演进分为三个阶段。短期（2026-2028）以单相冷板为主，技术相对成熟，商品化不确定性较低。中期（2028-2030）两相冷板有望成为主流，冷却能力进一步提升，但届时供应链成熟度将使创新溢价消失。长期（2030年以后），如果机架密度继续攀升，冷板面临中等程度的被淘汰不确定性——直接硅蚀刻微通道冷却技术（如微软与Corintis的合作探索）有可能彻底移除冷板这一组件。

当前竞争格局中，大型工业集团正在加速整合：伊顿收购Boyd，艺康收购CoolIT，施耐德收购Motivair，维谛收购Strategic Thermal Labs。这些交易反映出行业共识——冷板是液冷基础设施的必选项，但收购方也清楚，这个业务需要与CDU、热交换器、系统服务等形成组合拳，才能构建更完整的护城河。

## 报告尚未完全回答的关键问题

Bernstein的报告提供了清晰的框架，但几个核心变量仍存在不确定性。首先是单价下降的速度和幅度——如果GPU功耗增速快于预期，冷却需求可能推动高端冷板维持溢价。其次是两相冷板的商业化节奏——目前只有Accelsius等初创公司专注于此，从工程样品到规模交付还有多远？第三是直接硅蚀刻技术的可行性——微软的投入是一个信号，但从实验室到机架部署的路径仍不清晰。

这些未解问题恰恰是跟踪这个行业最有价值的部分。冷板市场的短期确定性（量增）与长期不确定性（商品化/替代）之间的张力，将决定哪些公司能真正从液冷浪潮中持续获益。

完整报告的70页内容涵盖了冷板工作原理、性能驱动因素、设计权衡、竞争格局拆解以及市场规模的详细底稿模型。更多中文摘要、图表解读和Bernstein的完整分析框架，会放进每日国际信源汇编，适合快速对照主流叙事，也方便后续追问和横向比较。

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>

![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>
