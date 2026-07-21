你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
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
EU Semiconductors

# EU / Japan semis: Hybrid Bonding – Bullish logic adoption despite HBM uncertainties; Raising Besi PT to €310

![](images/8fd0e9a0c7ff675b4b4cad95e80d5d6a9ca98b2420f2b746652c3bfe289cace0.jpg)

David Dai, CFA

+852 2918 5704

david.dai@bernsteinsg.com

![](images/a3b94acc2a8cab9248330bfd39619d88368e563e6b420e8f84e4179a93af895e.jpg)

Juho Hwang

+81 3 6777 6980

juho.hwang@bernsteinsg.com

![](images/8ab8637947af563173e5f2a94585bec3f5296fe13bdae4098c27c3e177f2ec23.jpg)

Carmine Milano, CFA

+44 20 7762 1857

carmine.milano@bernsteinsg.com

Bonding technologies are essential to enable advanced packaging, and hybrid bonding (HB) is the ultimate bonding technology, as explained in our reports (The Bonder War: Part 1 — HBM, Part 2 and Bonder Primer). This report provides our latest view of the current bonding market as well as an update to our TAM forecast.

We see a clear trend for logic to adopt die-to-wafer (D2W) hybrid bonding to increase interconnection speed among logic chiplets and between logic and memory. For logic, we forecast 2028 HB TAM of \$887mn, and 2028 shipment of 237 units (103 prior), to reflect our outlook of stronger adoption at TSMC for SolC packaging. We expect TSMC's SolC capacity to grow 8x from 10kwpm in 2025 to 85kwpm in 2028, for AMD, Apple, Google, and Nvidia applications. Intel is also expected to resume HB capacity expansion from 2027, with the ramp up of Clearwater Forest and Diamond Rapids.

HBM adoption timing is less clear. Samsung may adopt HB in HBM4E (16-hi) in 2027, but if HBM4E turns out to be 12-hi only per Korean media, HB adoption is possibly postponed to 2028 with HBM5, with few (maybe 1) initial layers only while the remaining stays on TCB. For HBM, we forecast 2028 HB TAM of \$489mn, and 2028 shipment of 130 units, based on our view that some portion of HBM4E will adopt hybrid, and HBM5 will migrate to hybrid bonding.

Raising HB TAM forecast. We forecast the hybrid bonder TAM to surge to \$1.4bn in 2028, driven by the adoption in both logic and HBM. Compared to Besi's market forecast, our 2028 unit shipment estimates of 367 units is 24% above the mid case and 8% below the high case. Our HB TAM model is available for download here.

Raising Besi TP to €310, as a technology leader and structural beneficiary of hybrid bonding adoption. Assuming 2028 market share of 76% (80% logic, 70% HBM), Besi's revenue from HB would be \$1.1bn, which is based on unit sales of \~281 units and ASP assumption of \$3.75mn per unit. We raise 2027 / 2028 EPS by 3.6% / 23% respectively and our 2028 EPS is now 16.6% above consensus. Based on 40x (45x prior, cut to reflect weaker visibility on hybrid bonding) 1-year forward P/E and rolling over a quarter, we take Besi's PT up to €310.00 (€280 prior), with 39% potential upside. Reiterate Outperform rating.

For DISCO, we expect the real upside would come from hybrid bonding adoption, as dicing / grinding systems with high-cleanness specification would need to be adopted to ensure a particle-free bonding surface, enabling a high yield. Overall setup for DISCO seems favorable into 2027. Current drivers of generative AI in which DISCO partakes is mostly HBM and CoWoS. Whereas from 2027, we expect further adoption of NAND CBA bonding from more players such as Samsung, increased adoption of BSPDN, and die-to-wafer hybrid bonding. In addition, power semis such as SiC is also likely to resume investment. Reiterate Outperform rating.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td colspan="4">20 Jul 2026</td><td>TTM</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td></td><td></td><td rowspan="2">Closing Price</td><td rowspan="2">Price Target</td><td rowspan="2">Rel. Perf.</td><td rowspan="2">Cur</td><td rowspan="2">2025A</td><td rowspan="2">2026E</td><td rowspan="2">2027E</td><td rowspan="2">2025A</td><td rowspan="2">2026E</td><td rowspan="2">2027E</td></tr><tr><td>Ticker</td><td>Rating</td><td>Cur</td></tr><tr><td>BESI.NA (Besi)</td><td>O</td><td>EUR</td><td>223.50</td><td>310.00</td><td>57.2%</td><td>EUR</td><td>1.66</td><td>3.83</td><td>6.05</td><td>134.6</td><td>58.4</td><td>36.9</td></tr><tr><td>OLD</td><td></td><td></td><td></td><td>280.00</td><td></td><td></td><td></td><td>3.34</td><td>5.84</td><td></td><td></td><td></td></tr><tr><td>6146.JP (DISCO)</td><td>O</td><td>JPY</td><td>64,780</td><td>85,000</td><td>10.9%</td><td>JPY</td><td>1,246.28</td><td>1,733.62</td><td>2,127.33</td><td>52.0</td><td>37.4</td><td>30.5</td></tr><tr><td>EDME</td><td></td><td></td><td>1,587.83</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>JPL</td><td></td><td></td><td>2,545.21</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

PRICE TARGET CHANGE / ESTIMATE CHANGE IN BOLD

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate Besi (TP=€310.00) and Disco (TP=¥85,000) Outperform.

## DETAILS

Bonding technologies are essential to enable advanced packaging — we have written extensively on the different bonding technologies such as Thermocompression bonding (TCB) as well as hybrid bonding (HB) for both High Bandwidth Memory (HBM) and logic applications, in our previous reports (The Bonder War: Part 1 — HBM bonding technology shifts, The Bonder War: Part 2 — Path to advanced packaging for logic chips and The Bonder Primer: Essential enablers of advanced packaging).

This report provides our latest view of the current bonding market as well as an update to our TAM forecast (Exhibit 1). In short,

\- We see a clear trend for logic to adopt die-to-wafer (D2W) hybrid bonding to increase interconnection speed between logic chiplets and between logic and memory. For logic, we forecast 2028 HB TAM of \$887mn, and 2028 shipment of 237 units (103 prior), to reflect our outlook of stronger adoption at TSMC for SolC packaging.

\- HBM adoption is less clear. While Samsung may adopt HB in HBM4E in 2027, it's possible to be postponed to 2028 with HBM5, with few (maybe 1) initial layer only. We forecast 2028 HB TAM of \$489mn, and 2028 shipment of 130 units, based on our view that some portion of HBM4E will adopt hybrid, and HBM5 will migrate to hybrid bonding.

\- We forecast the hybrid bonder TAM to surge to c. \$1.4bn in 2028, driven by the adoption in both logic and HBM. Compared to Besi's hybrid bonding market forecast, we are more optimistic in logic adoption despite being more conservative with HBM adoption of HB, and our 2028 unit shipment estimates of 367 units is 24% above the mid case and 8% below the high case (Exhibit 2).

\- For Besi, assuming 2028 market share of 76% (80% logic, 70% HBM), Besi's revenue from HB would be c. \$1.1bn, which is based on unit sales of \~281 units and ASP assumption of \$3.75mn per unit.

The following sections will discuss logic and HBM adoption in detail.

EXHIBIT 1: Summary of our TCB / HB market forecast.

<table><tr><td>Total Market</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>TC Bonding TAM</td><td>654.0</td><td>847.2</td><td>1,169.7</td><td>1,601.4</td><td>2,048.9</td></tr><tr><td>HBM</td><td>399.6</td><td>478.1</td><td>782.3</td><td>1,002.5</td><td>1,316.0</td></tr><tr><td>Logic</td><td>254.4</td><td>369.1</td><td>387.5</td><td>598.9</td><td>733.0</td></tr><tr><td>% YoY</td><td></td><td>29.5%</td><td>38.1%</td><td>36.9%</td><td>27.9%</td></tr><tr><td>Hybrid Bonding TAM</td><td>101.3</td><td>99.8</td><td>206.3</td><td>524.1</td><td>1,376.0</td></tr><tr><td>HBM</td><td>--</td><td>--</td><td>--</td><td>91.8</td><td>488.8</td></tr><tr><td>Logic</td><td>101.3</td><td>99.8</td><td>206.3</td><td>432.4</td><td>887.2</td></tr><tr><td>% YoY</td><td></td><td>(1.5%)</td><td>106.8%</td><td>154.1%</td><td>162.5%</td></tr><tr><td>Total TCB + HB TAM</td><td>755.2</td><td>946.9</td><td>1,376.0</td><td>2,125.5</td><td>3,425.0</td></tr><tr><td>HBM</td><td>399.6</td><td>478.1</td><td>782.3</td><td>1,094.3</td><td>1,804.8</td></tr><tr><td>Logic</td><td>355.6</td><td>468.9</td><td>593.7</td><td>1,031.3</td><td>1,620.2</td></tr><tr><td>% YoY</td><td></td><td>25.4%</td><td>45.3%</td><td>54.5%</td><td>61.1%</td></tr><tr><td>Besi HB Revenue</td><td>101.3</td><td>99.8</td><td>206.3</td><td>488.8</td><td>1,052.0</td></tr><tr><td>HBM</td><td>--</td><td>--</td><td>--</td><td>78.0</td><td>342.2</td></tr><tr><td>Logic</td><td>101.3</td><td>99.8</td><td>206.3</td><td>410.8</td><td>709.8</td></tr><tr><td>Implied Besi Market Share (HB)</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>93.2%</td><td>76.4%</td></tr><tr><td>HBM</td><td></td><td></td><td></td><td>85.0%</td><td>70.0%</td></tr><tr><td>Logic</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>95.0%</td><td>80.0%</td></tr></table>

Source: Company disclosures, TechInsights, Bernstein estimates and analysis.

EXHIBIT 2: Our hybrid bonder estimates are between Besi's mid and high case guidance.  
![](images/77b7c9eab917d52609cd2e1c0b905d4e279091eaa30621f7c54a0b867db66318.jpg)  
Source: Company disclosures, Bernstein estimates and analysis.

## LOGIC: CLEAR TRAJECTORY OF HYBRID ADOPTION

Hybrid bonding is expanding in adoption among the various interconnect technologies, especially for leading-edge chiplet architectures. The key driver remains to be the fact that it enables higher interconnect density while lowering power consumption than with conventional micro-bump based approaches.

We see three primary use cases for hybrid bonding:

\- XPU-to-XPU chiplet integration (bonding logic on logic): to improve logic transistor count and boost computing power. Examples of XPU-to-XPU chiplet integrations include AMD's Instinct GPUs (Exhibit 3) utilizing advanced chiplet architectures, as well as future Nvidia multi-die GPU architectures such as Feynman GPUs. Apple's M5 Pro uses unique CPU +GPU chiplet integration named Fusion Architecture.

\- XPU+Memory (bonding memory on logic): to break the memory wall, and there are a few variations:

\- The most prominent is bonding XPU with SRAM, and AMD's 3D V-Cache architecture (Exhibit 4) is a good example of this, and already with a sizeable production volume. EPYC (Milan-X / Genoa-X) and Ryzen X3D (7800X3D / 9800X3D) series have logic die bonded to cache memory die, to realize improved cache capacity as well as lower latency. The Nvidia Groq LPU is also anticipated to use XPU+SRAM integration in the next generation. Intel is also working on their own architecture of HB named Foveros Direct 3D.

\- There is also XPU bonding with DRAM, as shown in China's LongShine CPU which integrates HBM and DRAM on chip. In the LongShine setup, hybrid bonding helps make DRAM behave more like a first-class extension of the processor package rather than a distant off-package resource.

\- CPO (optical communication): most prominently TSMC's COUPE which integrates optical chip (PIC) and electrical chip (EIC) together with hybrid bonding (Exhibit 5).

For these applications, we expect hybrid bonding capacity to increase rapidly, leading to strong growth of hybrid bonding equipment revenue. In terms of capacity, TSMC and Intel are the leaders.

\- For TSMC (covered by Mark Li), current use cases are mainly for AMD CPUs and GPUs mentioned above, and some for Apple (M5 Pro / M5 Max). Going forward, we expect TSMC's HB capacity to nearly double for both this year and next year driven by increased adoption, for Broadcom's 3.5D packaging as well as for Nvidia's Feynman GPUs.

Source: AMD

\- Intel (covered by Stacy Rasgon) has already deployed hybrid-bonding based architectures through their Foveros Direct 3D platform and remains strategically committed to advanced 3D packaging. Intel's Clearwater Forest is an instance of their HB adoption, and we expect higher adoption going forward as Diamond Rapids and subsequent CPUs start ramping. As for Intel, we don't anticipate much ramp in HB capacity quite yet in 2026 as they already have 30 units of hybrid bonders, and Diamond Rapids seems to be delayed to 2027, but capacity expansion should happen again from 2027 (Exhibit 6-Exhibit 8).

EXHIBIT 3: AMD Instinct GPUs employing XPU-XPU chiplet integration  
EXHIBIT 4: AMD 3D V-cache employing XPU-Memory bonding  
![](images/335581c48d4913eed2f99a4920f8fdff857ad3a403c96657199e9923c79a4889.jpg)

EXHIBIT 5: Optical interconnects employing hybrid bonding.  
![](images/f513d6047fa2eed397d38d3f2681a013cda3d71acdc22014ab781581b548c0a9.jpg)  
Source: Bernstein analysis.

EXHIBIT 6: Intel product roadmap with Foveros Direct 3D  
![](images/905740c4ff575a29166d3e427a8db58986dea13b7350e7c397c313836d36a9cb.jpg)  
Source: Intel

EXHIBIT 7: Intel Clearwater Forest is Intel's first major CPU that employs hybrid bonding to connect CPU chiplet to base chiplet, before bonding to EMIB substrate.  
![](images/ed6445e7545c7090440cb69b243aad790fae4d2dafeff446c9b7d0bae2435394.jpg)  
Source: Intel

EXHIBIT 8: Hybrid bonding (Foveros Direct 3D) is a key technology to enable Intel's product roadmap.  
![](images/9d925b5f927f41cac4e6e5423b8f1ed0ae2202bd16f7c912bd03d14245964db0.jpg)  
Source: Intel

In terms of TAM, we expect a strong ramp and model the logic hybrid bonding capacity (installed base) to grow 4.5x to 582 units in 2028 from 137 units in 2025 (Exhibit 10).

\- We believe the install base at TSMC could reach \~440 units as AP7 followed by AP8 ramps up — from the current \~65 unit fleet mostly in AP6. AP7 capacity expansion occurring in three phases: 1. Initial SolC applications 2. HPC chiplet deployment 3. More broad-based adoption such as wafer-level multi-chip module (WMCM) adoption.

\- We expect TSMC's capacity grow \~8x from 10kwpm in end 2025 to 80kwpm in 2028 (Exhibit 9), driven by the adoption of AMD, Apple, followed by Google TPU, Groq LPU, and Nvidia GPU (Feynman).

\- At a higher level, we estimate that each kwpm SolC capacity addition requires around 5-6 hybrid bonders, and that the intensity will go down over time as hybrid bonding throughput improves.

\- For Intel, we expect them to resume HB capacity addition from 2027 and model the install base to reach \~65 units in 2028 from the current install base of \~30 units, and others (including Samsung) doubling to \~68 units from \~33 units. As a result, we expect the logic HB TAM to reach \$887mn in 2028, effectively growing eightfold from 2025 (Exhibit 11).

EXHIBIT 9: We expect TSMC's capacity to grow rapidly to 80kwpm in 2028.

2024-2028E: TSMC SolC capacity

![](images/cd5627bfed73699d6c92dd696e74768c62cd1794d9292193bc1335c788cc0174.jpg)  
Source: Company disclosures, Bernstein estimates and analysis.  
EXHIBIT 10: We expect the install base to grow 4.5x in 3 years.  
2025-2028E: Hybrid bonder (Logic) Install base

![](images/0fde53cad0949add9650f7ee047627bad014944ce048e95c8380e39caad5c3d8.jpg)  
Source: Company disclosures, Bernstein estimates and analysis.  
EXHIBIT 11: As a result, we expect logic hybrid bonder TAM to reach \$887mn in 2028.  
2025-2028E: Hybrid bonder (Logic) Market size

![](images/affdd4bf81391045406a094427e8f0f9ef11c9aedb1603cdf17a6cf8f8650719.jpg)  
Source: Company disclosures, TechInsights, Bernstein estimates and analysis.

## HBM: UNCERTAINTIES STILL PRESENT IN HB PENETRATION

While hybrid bonding has become increasingly established in logic applications, adoption within HBM is likely to proceed more gradually. The primary reason is that the current TCB solutions remain highly effective and sufficient for many HBM requirements, especially given that 1. JEDEC seems increasingly likely to relax HBM height standards to \~900 $\mu$ m from the current 775 $\mu$ m, 2. HBM4E seems likely to stay mostly at 12-hi 3. Both Samsung 

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
