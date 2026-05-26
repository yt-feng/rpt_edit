你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  ✅ 三大情景框架：DCF、P/ARR、EV/Sales
  ✅ 关键变量分析
  ✅ 估值逻辑、假设、终值占比等核心内容覆盖
  ✅ 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

【研报解析内容】
"""
# China Semiconductors

# China Semis: Huawei's Tau (T) Law, another DeepSeek moment

![](images/33ff6051c58c49f74843544f6b2729c6b9c9c52b9c7072cb8150a4db9683a01a.jpg)

Qingyuan Lin, Ph.D.

+852 2123 2654

qingyuan.lin@bernsteinsg.com

![](images/a3f5fb937a43263aca5b590742dc59028671a9a92c83c225f03b9654afb0bf3c.jpg)

Francis Ma

+852 2123 2626

francis.ma@bernsteinsg.com

![](images/7c989706638a5b4da57ea13fde5754017b677b91b01eae7dd9704b17fd3c556c.jpg)

Zheng Cui

+852 2123 2694

zheng.cui@bernsteinsg.com

Huawei unveiled the "Tau ( $\tau$ ) Scaling Law" at ISCAS 2026 on May 25, 2025, proposing a shift from geometric scaling (making transistors smaller) to temporal scaling (reducing signal latency) as a successor to Moore's Law. A-share semis names rallied yesterday (STAR 50 +5.9%). We believe the Tau law demonstrates that China is making impressive tech breakthrough despite export controls, and sets a clear roadmap for continuous improvement in chip performance without EUV, making it another DeepSeek moment for China Semis. Reiterate Outperform for the sector.

Tau Law demonstrates breakthrough beyond what's achieved. The core idea of the Tau law is systematically reducing the time constant $\tau$ by cutting signal latency across entire semis stacks. One of Huawei's tech innovation called 'LogicFolding' looks similar to TSMC's SolC at first glance, as they both stack two dies on top of each other. But Huawei is able to achieve impressive sub-2um bonding pitch (Exhibit 2), which allow them to stack logic on top of logic to reduce latency (cell to cell) rather than just stack up at chip level (die to die, usually SRAM on logic). This is why they are able to improve not only on density but also on frequency (Exhibit 1). On top of that, Huawei emphasizes the importance of end-to-end co-optimization for AI, where the improvement across the transistor-circuit-chip-system levels are all leveraged. They target to achieve 125X compute power improvement at superPoD level in the next five years through near-packaged optical I/O ('Hi-ONE') and Unified Bus networking (Exhibit 3). With these improvements across different tech stacks, they are able to deliver massive performance improvement at the cluster level, which is what the customers actually needs. Therefore, we think of Tau law as a predictable and scalable roadmap metric to guide the China Semis to go beyond the EUV constrain and continuously improve for the next decade.

However, Tau Law comes with constraints and won't allow China to close the gap with global leaders yet. First, Tau Law assumes sustained progress in 3DIC advanced packaging, areas where global leaders like TSMC still hold a meaningful technology and ecosystem lead. Second, stacking multiple dies boosts transistor density but also increases power density, thermal constraints will be a key issue that require power-delivery innovations. Thirdly, the yield and cost will also be another barrier for adoption if not engineered properly. Arguably the innovations from Huawei are the ones that global players can copy, but Huawei won't have EUV anytime soon yet, so China will be still behind global leaders in semis, although we do see that these innovations could allow Huawei to continuously improve and gradually narrow the gap. The differentiation for Huawei will likely come down to how fast they can solve these challenges, integrate the stacks more tightly, and scale manufacturing reliably and economically.

The upside for China semis is massive if the Tau Law is executed successfully. Just like DeepSeek innovation on algorithm encouraged China to invest in AI and build a whole AI-stack locally, Huawei's Tau Law now will give the industry a lot more confidence to invest in China semis and build a whole Semis-stack locally, further enhancing our localization thesis for the sector. We like SMIC, NAURA, Piotech the most under this theme, as SMIC executes the advanced logic and packaging manufacturing, NAURA delivers the tools for advanced logic fabrication, and Piotech could potentially support the bonding tools for the LogicFolding design.

BERNSTEIN TICKER TABLE 

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td rowspan="2">Cur</td><td rowspan="2">25 May 2026 Closing Price</td><td rowspan="2">Price Target</td><td rowspan="2">TTM Rel. Perf.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>688981.CH (SMIC-A)</td><td>O</td><td>CNY</td><td>156.00</td><td>120.00</td><td>45.0%</td><td>USD</td><td>0.09</td><td>0.10</td><td>0.13</td><td>267.6</td><td>229.1</td><td>182.0</td></tr><tr><td>981.HK (SMIC-H)</td><td>O</td><td>HKD</td><td>79.85</td><td>70.00</td><td>48.8%</td><td>USD</td><td>0.09</td><td>0.10</td><td>0.13</td><td>118.8</td><td>101.7</td><td>80.8</td></tr><tr><td>688347.CH (Hua Hong-A)</td><td>O</td><td>CNY</td><td>214.80</td><td>140.00</td><td>305.3%</td><td>USD</td><td>0.03</td><td>0.11</td><td>0.16</td><td>995.5</td><td>297.0</td><td>203.4</td></tr><tr><td>1347.HK (Hua Hong-H)</td><td>O</td><td>HKD</td><td>130.10</td><td>100.00</td><td>271.1%</td><td>USD</td><td>0.03</td><td>0.11</td><td>0.16</td><td>523.1</td><td>156.0</td><td>106.9</td></tr><tr><td>002371.CH (NAURA)</td><td>O</td><td>CNY</td><td>698.19</td><td>680.00</td><td>77.8%</td><td>CNY</td><td>5.66</td><td>10.22</td><td>16.41</td><td>123.3</td><td>68.3</td><td>42.6</td></tr><tr><td>688012.CH (AMEC)</td><td>O</td><td>CNY</td><td>485.30</td><td>500.00</td><td>137.5%</td><td>CNY</td><td>3.40</td><td>4.95</td><td>7.18</td><td>142.7</td><td>98.1</td><td>67.6</td></tr><tr><td>688072.CH (Piotech)</td><td>O</td><td>CNY</td><td>721.00</td><td>580.00</td><td>341.6%</td><td>CNY</td><td>3.32</td><td>8.12</td><td>12.40</td><td>217.2</td><td>88.8</td><td>58.2</td></tr><tr><td>688256.CH (Cambricon)</td><td>O</td><td>CNY</td><td>1,406.50</td><td>2,000.00</td><td>181.3%</td><td>CNY</td><td>(1.09)</td><td>5.38</td><td>11.26</td><td>N/M</td><td>261.2</td><td>124.9</td></tr><tr><td>688041.CH (Hygon)</td><td>O</td><td>CNY</td><td>329.68</td><td>280.00</td><td>101.5%</td><td>CNY</td><td>0.83</td><td>1.35</td><td>2.42</td><td>397.2</td><td>244.3</td><td>136.3</td></tr><tr><td>ASIAX</td><td></td><td></td><td>1,939.99</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended   
688256.CH, 688041.CH base year is 2024;   
Source: Bloomberg, Bernstein estimates and analysis.

# INVESTMENT IMPLICATIONS

We rate SMIC, Hua Hong, NAURA, AMEC, Piotech, Cambricon, Hygon Outperform benefiting from this new roadmap for China Semis.

On beneficiaries, we see the Tau Law roadmap as structurally positive for China's leading foundry, advanced-packaging supply chain, and AI chip ecosystem. On foundry, SMIC is a clear strategic partner and likely a critical enabler if Huawei is to deliver the roadmap and eventually reach TSMC A14-equivalent logic density via multi-die integration without EUV, implying sustained demand for SMIC's most advanced DUV based multi-patterning advanced logic nodes. Hua Hong likely will also benefit as the expected acquisition of Huali who is potentially also working on advanced logic packaging. In semicap, we see upside skewed to domestic tool vendors who has higher exposure for advanced logic and packaging: NAURA should benefit more than AMEC as it has much higher exposure in advanced logic, while Piotech has been working on bonding tools for advanced packaging and thus market will perceive it as one of the core beneficiaries. For AI fabless, Huawei's framework provides a clearer path to sustain performance scaling under EUV constraints, which should be supportive for domestic accelerator and CPU vendors such as Cambricon and Hygon as they co-optimize architectures to exploit higher effective density and lower latency interconnect within China's manufacturing envelope. On the other hand they also face more intense competition from Huawei so the upside will be smaller for the AI fabless names compared to foundry and semicap.

# DETAILS

# HUAWEI'S ROADMAP ON CIRCUITS AND SYSTEMS

In the event, Huawei released its roadmap for chip improvement under the guidance of Tau Scaling Law.

# Three key highlights:

1. Fast transistor density improvement. Trough advanced packaging (or so-called 'LogicFolding' by Huawei), they are able to improve the transistor density from 155 MTr/mm^2 in 2025 (HiSilicon Kirin 9030, based on SMIC N+3 node, between TSMC N5 and N7) to 238 MTr/mm^2 in 2026 (equivalent to TSMC N3 node density. Likely that's based on two chips stack on top of each other, for example one SMIC N+3 node chip with another SMIC N+2 node chip, so no longer apple to apple comparison). By 2031, they target to achieve 400+ MTr/mm^2 (equivalent to TSMC 14A density, but again not apple to apple comparison);   
2. Steadily increasing max frequency. The speed of a transistor is generally measured by how fast it can switch, or the frequency, further improvement on the max frequency is achieved through the tau optimization that reduced the latency, which is the critical-path delay between adjacent transistors, which in turn is dominated by interconnect RC;   
3. Exponentially growing AI cluster scaling. On top of improvement on chip performance, the Tau Scaling Law also emphasizes on the improvement of networking between chips to build exponentially larger AI superPoDs, we have illustrated that in the Huawei AI chip roadmap analysis, and now Huawei targets to achieve 125X improvement in superPoD total compute power by 2030, which indicates an aggressive 3.3X improvement every year.

EXHIBIT 1: Huawei's tau scaling roadmap   
τ-Scaling Roadmap: Sustainable PPDC Evolution   
![](images/b3e51189752f6a33c298a5ed617161069cccce7b09ac4f33be789dba1fc0ca8f.jpg)

<details>
<summary>line</summary>

| Year | Density (MTr/mm²) | P-Core Freq. (GHz) |
|------|-------------------|--------------------|
| 2023 | 126               | 2.6                |
| 2024 | 126               | 2.65               |
| 2025 | 155               | 2.75               |
| 2026 | 238               | 3.1                |
| 2027 | 252               | 3.39               |
| 2028 | 266               | 3.71               |
| 2029 | 277               | 4.0                |
| 2030 | 292               | 4.3                |
| 2031 | 5.0               | 5.0                |
</details>

Note:
Density = $\frac{2}{CPP \times cell height}$ · Position = Density · Design Utilization(60\~75%)

![](images/68d5da09b15f9ef587ed3538841a8ee1f3dfc8d3dafbc96bbf3cb5909b233539.jpg)

<details>
<summary>bar</summary>

Systems Roadmap
SuperPOD Performance Scaling
| System | Performance (EFLOPS) |
| :--- | :--- |
| Atlas950 (2026) | 8 |
| Atlas960 (2027) | 60 |
| AtlasNEXT (2030) | Z FLOPS |
125x
</details>

Source: Company reports, Bernstein analysis

# THE TIME SCALING THEORY

Link to the full technical paper: A Time Scaling Theory for Multi-Layer Electronic Systems

Copying the abstract here:

For six decades, Moore's geometric scaling drove progress in semiconductors. That industry compact no longer holds: returns from pure dimensional shrinking have flattened, leading-edge design budgets exceed one billion dollars per chip, and cost-per-transistor at the most advanced nodes is no longer falling. This perspective argues for a successor scaling principle — T scaling — that adopts time itself, rather than transistor area, as the primary metric of progress, applying a single characteristic time constant T as the unifying optimization target across twelve orders of magnitude, from a switching transistor to a data-center workload. Two production-scale demonstrations are presented. On a mobile SoC, LogicFolding — a methodology that partitions digital, analog, and memory circuits across vertically stacked active tiers — delivers a 55% step-wise increase in transistor density and a 41% power-efficiency gain at a fixed device node. On AI systems, a co-designed stack comprising the memory-semantic Unified Bus fabric, near-packaged Hi-ONE optical I/O, and edge-to-surface 3D Folding projects more than 100× growth in hardware integration by 2035. The deeper claim is methodological: T scaling is the first scaling principle since Dennard to establish a shared optimization target across the entire computing stack.

The theory dictates optimizing and compressing delay ( $\tau$ ) across four collaborative layers of the compute stack:

- Transistor Level: Reducing intrinsic transistor switching and interconnect delays. This part is where the Moore's law has been making the direct impact, where shrinking the feature size of a transistor help to improve the speed of calculation. Beyond shrinking the size of the feature, changing the structure could also improve transistor performance (e.g. from planner to FinFET to GAA structure). We believe local foundry are also making progress at this level, such as using DUV to manufacture GAA structure;   
- Circuit Level: Implementing LogicFolding (breaking down and vertically stacking logic, memory, and analog blocks using 3D heterogeneous integration and fine-pitch hybrid bonding) to drastically shorten critical wiring and reduce RC loads. Beyond the traditional 3DIC roadmap, Huawei further bring the design from 'Chip to Chip' stacking to 'Cell to Cell' stacking, allow different part of the circuit function (the Combinational logic and Sequential logic, which performs the calculation and memory parts within a transistor) to be stacked on to of each other.   
- Chip Level: Optimizing silicon and software holistically to reduce total execution time. This is commonly cited as 'Design-Technology Co-Optimization' by the industry. As Huawei is forced to build its own know-how on process, and even build its own fabs, it's also possible that Huawei can move faster in the co-optimization to deliver better results at the chip level.   
- System Level: Utilizing memory-semantic unified bus structures (e.g., UnifiedBus) and high-speed optical I/O (e.g., Hi-ONE) to bypass physical distance bottlenecks and compress cluster communication latency from tens of microseconds to \~100 nanoseconds. This is the networking architecture optimization illustrated in Huawei's paper on UB-Mesh (UB-Mesh: a Hierarchically Localized nD-FullMesh Datacenter Network Architecture)

Specifically, in the paper Huawei illustrates the advanced packaging technology that they rely on to get to the impressive 238 MTr/mm^2 transistor density in 2026 that likely will be deployed on its next generation mobile phone Huawei Mate90, and the networking innovations that allow Huawei to deliver more scaling capabilities for AI clusters for the next decade.

# EXHIBIT 2: Technology used for LogicFold

# Sidebar A — LogicFolding at a Glance

• Hybrid-bonding pitch: sub-2 $\mu$ m (1.5 $\mu$ m in Kirin 2026; target gear ratio $\approx$ 1)   
• Overlay accuracy: under 0.5 μm   
• TSV CD/KOZ: sub-1.5 $\mu$ m; pitch sub-6 $\mu$ m; failure rate <100 ppm; repair rate 99.9%   
• Yield: \~100% with smart redundancy   
• Transistor density: $155 \rightarrow 238$ MTr/mm $^{2}$ in a single step   
• Power-efficiency / frequency gain (SoC P-core): +41% / +13%   
• SRAM operating frequency: +40%+   
- Clock-buffer count / clock skew / wire length on a representative core: $-50\% / -25\% / -30\%$

Source: Company reports, Bernstein Analysis

# EXHIBIT 3: Key technology Huawei used to improve system level tao

# Sidebar B — $\tau$ at AI System Scale

- UB remote-access latency: $\sim 10\mathrm{s}$ of $\mu \mathrm{s} \rightarrow \sim 100\mathrm{ns}$ ( $\approx 500\times \tau$ reduction)   
• HiONE per-module bandwidth:

[中间内容因长度限制已省略]

erein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engage in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek for independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
