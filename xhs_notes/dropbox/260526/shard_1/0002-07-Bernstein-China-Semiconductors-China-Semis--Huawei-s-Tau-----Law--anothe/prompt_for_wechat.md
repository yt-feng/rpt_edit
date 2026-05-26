你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：一句主判断，不超过 32 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

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
• HiONE per-module bandwidth: 8 Tb/s (matches per-chip UB bandwidth)   
- HiONE SerDes reach: $\sim 100\mathrm{cm}\rightarrow \sim 5\mathrm{cm}$ ; panel-to-panel reach: $< 1\mathrm{m}\rightarrow 100\mathrm{m}$   
- Fan-out dilemma: compute $\propto$ N $^{2}$ , perimeter-bound BW/I/O/power $\propto$ N   
- 3D Folding: relocates BW, optical I/O, and power delivery from edges onto surfaces, restoring $\mathbf{N}^2$ parity   
• 2026 → 2035 projected hardware-integration growth: >100×

Source: Company reports, Bernstein Analysis

# I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted otherwise, for purposes of these disclosures, references to Bernstein's “affiliates” relate to both SG and AB and their respective affiliates.

# VALUATION METHODOLOGY

This research publication covers six or more companies. For valuation methodology and other company disclosures:

Please visit: https://bernstein-autonomous.bluematrix.com/sellside/Disclosures.action.

Or, you can also write to the Director of Compliance, Bernstein Institutional Services LLC, 245 Park Avenue, New York, NY 10167.

# RISKS

This research publication covers six or more companies. For risks and other company disclosures:

Please visit: https://bernstein-autonomous.bluematrix.com/sellside/Disclosures.action.

Or, you can also write to the Director of Compliance, Bernstein Institutional Services LLC, 245 Park Avenue, New York, NY 10167.

# RATINGS DEFINITIONS, BENCHMARKS AND DISTRIBUTION

# EQUITY RATINGS DEFINITIONS

# Bernstein brand

The Bernstein brand rates stocks based on forecasts of relative performance for the next 12 months versus the S&P 500 for stocks listed on the U.S. and Canadian exchanges, versus the Bloomberg Europe Developed Markets Large and Mid Cap Price Return Index EUR (EDME) for stocks listed on the European exchanges and emerging markets exchanges outside of the Asia Pacific region, versus the Bloomberg Japan Large and Mid Cap Price Return Index USD (JPL) for stocks listed on the Japanese exchanges, and versus the Bloomberg Asia ex-Japan Large and Mid Cap Pric

[中间内容因长度限制已省略]

 learning or artificial intelligence system, or as a prompt or input into any such system. You also may not, without Bernstein's express written consent, do any of the foregoing in connection with your own internal machine learning or artificial intelligence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engage in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek for independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
