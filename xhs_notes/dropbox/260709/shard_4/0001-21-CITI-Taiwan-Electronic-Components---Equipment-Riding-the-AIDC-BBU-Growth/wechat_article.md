# Citi：不是库存回补而是架构演进，Citi详解BBU渗透率跃升路径

AI基础设施正在经历一场不易察觉但影响深远的电源架构变革。Citi最新发布的研究指出，随着机架功率密度持续攀升，数据中心备用电源正在从传统的集中式UPS向机架级分布式备份电源迁移。这一转变的核心组件——电池备份单元（BBU），正从可选配置变为高密度AI机架的标准配置。

报告的核心判断是：BBU的单机架价值量和行业渗透率将在未来几年同步提升，形成一条被市场低估的多年度增长曲线。Citi测算，BBU在AI机架中的渗透率将从2025年的40-45%跃升至2026年的60-65%，到2027年超过85%。与此同时，单机架BBU价值量将从当前GB300 NVL72的约1.5-1.6万美元，攀升至Rubin架构的1.7-1.8万美元，在Rubin Ultra架构下可能超过3.3万美元。

这一判断的关键驱动力来自两个方向：一是机架功率密度提升使得集中式UPS在响应速度、转换损耗和可扩展性方面的劣势被放大；二是高压直流配电架构的普及为分布式BBU创造了更好的集成条件。Citi认为，这不是一个周期性的库存回补，而是电源架构本身的结构性演进。

> **KC评论：** 将BBU渗透率从40%拉到85%以上，意味着这个市场在未来三年内会从“少数先行者的选择”变成“行业标配”。对于关注AI硬件供应链的读者，报告第6页的BBU供应链估值对比表值得细看——它清晰展示了不同环节公司的当前定价是否已反映这一增长预期。

![研报原图 1](assets/source_image_01.jpg)

## 1. 这轮变化真正考验的是企业能否把规模转化为议价权

Citi在报告中明确表达了对两家BBU供应商的不同偏好。AES-KY作为当前BBU市场的龙头，在规模、客户关系和技术积累上占据明显优势。但Citi认为，Dynapack在当前阶段的回报特征更具吸引力。

核心逻辑在于盈利增长的斜率差异。Citi测算，Dynapack在2025-2028年间的每股盈利年复合增长率约为60%，而AES-KY约为27%。差距主要来自产品结构改善和运营杠杆——随着BBU在Dynapack收入中的占比提升，其整体毛利率预计从2025年的16.6%升至2028年的28.4%。

这不是一个“谁更好”的问题，而是“谁的增长曲线更陡峭”的判断。在AI基础设施研究周期的早期阶段，市场通常愿意为盈利加速增长的公司支付溢价。Dynapack的非IT业务收入复合增长率高达74%，而IT业务仅增长12%左右，说明其增长引擎几乎完全由BBU驱动。

![研报原图 2](assets/source_image_02.jpg)

## 2. 报告没有完全回答的关键问题：竞争格局何时开始出现变化

Citi的研究对BBU市场的增长空间做了充分拆解，但有一个问题着墨不多：当渗透率从85%走向100%甚至更高时，竞争格局会如何演变。

当前BBU供应链仍处于供不应求阶段，主要供应商享有较高的议价权。但随着更多电池模组厂商和电源系统集成商进入这一领域，单位价值量是否会面临不确定性？报告给出的Rubin Ultra单机架BBU价值量超过3.3万美元的预测，是基于当前技术路线的模块化估算，但并未讨论竞争加剧可能带来的价格节奏变化不确定性。

另一个值得追问的问题是：如果AI芯片架构再次发生重大变化，比如从机架级向晶圆级集成演进，BBU的形态和需求是否会受到冲击？这超出了当前报告的分析范围，但对于长期持有者而言，这是不可回避的变量。

> **KC评论：** Citi对BBU渗透率的预测路径——2025年40-45%、2026年60-65%、2027年85%以上——背后的隐含假设是AI机架出货量持续增长且功率密度只升不降。如果其中任何一个环节出现节奏变化，这条曲线的斜率就需要重新评估。报告第20页的BBU价值量拆解表提供了关键参考数据。

![研报原图 3](assets/source_image_03.jpg)

## 3. 一个观察框架：用三个指标追踪BBU主题的兑现进度

对于希望独立跟踪这一主题的读者，可以从报告中提炼三个核心观测指标。

第一个是机架功率密度的实际爬升速度。Citi的分析建立在功率密度持续上升的前提上，但不同云服务商的部署节奏存在差异。如果GB300到Rubin的过渡时间拉长，BBU的渗透率提升也可能滞后于当前预测。

第二个是BBU模块的单价走势。当前BBU仍处于早期量产阶段，随着规模效应显现，单位成本有望下降。但如果价格下降速度超过价值量提升速度，单机架BBU收入可能不如预期乐观。

第三个是Dynapack毛利率的实际兑现节奏。报告预测其毛利率从16.6%升至28.4%，这一改善幅度在电子制造服务行业中属于较高水平。需要持续跟踪其季度毛利率是否沿着预期路径行进，以及BBU产品在客户端的验证进度是否顺利。

这三个指标没有一个是孤立的——它们共同构成了BBU增长故事能否兑现的验证链条。对于产业决策者和读者而言，不如把注意力放在这些可观测的先行信号上。

---

*本文基于Citi研究内容撰写，仅用于信息分享，不构成任何研究交流。*

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>

![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)

<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated,translated,summarized,or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment,legal,tax,accounting,or other professional advice.</p>
