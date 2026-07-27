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
China Semiconductors

# Global Memory Interface Chip: Competitive dynamics deep dive

![](images/7e10005bd7b80576f931ff4c8a2195e60360421440c02fd114413d8ea2fcab2d.jpg)

Qingyuan Lin, Ph.D.

+852 2123 2654

qingyuan.lin@bernsteinsg.com

![](images/9188f3f39ec231d16cfc6ea66d1f0f2dafd8afad2be5016d7002b86f3f28f101.jpg)

Francis Ma

+852 2123 2626

francis.ma@bernsteinsg.com

![](images/b94f488cb2f9149e324821e6ab7a5ef5938428cedbae5a925ccb16db66555425.jpg)

Kai Zhang

+852 2123 2665

kai.zhang@bernsteinsg.com

We highlighted in our memory interface chip industry deep dive that all three major sector vendors (Montage, Renesas, Rambus) will benefit from the agentic AI boom, in the report we provide a deep dive to the competitive dynamics with a focus on Rambus (RMBS, not covered). Our industry model can be downloaded here.

Rambus derives revenue from memory interface chips, DRAM-related IP royalties, and computing-chip IP licensing, exposed to three AI-driven growth engines that should support a strong revenue growth through 2030. Each segment is leveraged to a major secular AI theme: memory interface chips benefit from the server CPU Renaissance driven by agentic AI; DRAM royalties are tied to memory tech migration; and computing-chip IP licensing benefits from growing share of AI ASICs. Together, these businesses provide broad exposure to the core infrastructure layers underpinning AI development. We project the memory interface chip market alone to reach nearly USD 20Bn by 2030. ASIC will account for over two-thirds of CoWoS-based XPU shipments in 2027. Both highlight the magnitude of the opportunities available to Rambus.

However, each of Rambus's core businesses faces competitive constraints that are likely to keep growth below Montage. In memory interface chips, we believe its historical litigation-driven relationship with memory manufacturers limits its ability to gain shares from Montage and Renesas. In DRAM royalties, long-duration licensing contracts provide stable cash flow but inherently cap further growth. In IP for computing chips, Rambus competes against both vertically integrated AI ASIC designers with extensive in-house IP portfolios and ecosystem leaders such as Cadence and Synopsys, whose IP offerings are tightly bundled with EDA tools and foundry workflows. Consequently, Rambus is largely positioned to serve AI chip startups rather than first-tier hyperscaler ASIC programs.

A broader technology portfolio combined with slower revenue scaling should translate into a slower operating leverage than Montage. Rambus invests across memory interface chips, memory controllers, interconnect IP, security technologies, and applications in diverse end markets, resulting in annual R&D spending roughly 40-50% higher than Montage, whose tech portfolio is more focused. While this broad portfolio expands Rambus's addressable market, it also requires a significantly larger engineering organization. Because revenue growth is moderated by the fierce competition discussed above, Rambus generates less revenue per dollar of R&D spending than Montage. Consequently, we expect operating leverage to emerge more gradually for Rambus, leading to slower net income growth than Montage.

We expect Rambus to grow slower than Montage in both revenue and earnings as a result. Market has been trading Rambus at a discount vs. Montage, given slower expected revenue and earnings growth. Nevertheless, a business that rides on 65% TAM growth remains an attractive growth asset.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td colspan="4">23 Jul 2026</td><td>TTM</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td></td><td></td><td rowspan="2">Closing Price</td><td rowspan="2">Price Target</td><td rowspan="2">Rel. Perf.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Ticker</td><td>Rating</td><td>Cur</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>6809.HK (Montage)</td><td>O</td><td>HKD</td><td>311.80</td><td>520.00</td><td>NA</td><td>CNY</td><td>1.97</td><td>3.21</td><td>5.68</td><td>136.7</td><td>84.0</td><td>47.4</td></tr><tr><td>688008.CH (Montage)</td><td>O</td><td>CNY</td><td>225.50</td><td>400.00</td><td>142.3%</td><td>CNY</td><td>1.97</td><td>3.21</td><td>5.68</td><td>114.5</td><td>70.3</td><td>39.7</td></tr><tr><td>ASIAX</td><td></td><td></td><td>1,880.30</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate Montage Outperform, with A-Share TP at CNY 400 and H-Share TP at HKD 520.

## Table Of Contents

Company overview....3
Memory interface chips: accelerating TAM growth....5
Royalties of IP inside the DRAM module: stable but low-growth....10
Licensing IP inside the computing chips: attractive end market, but intense competition....11
Moderate operating leverage and earnings growth restricted by R&D intensity....14

## DETAILS

## COMPANY OVERVIEW

## COMPANY INTRODUCTION

Rambus is a Silicon Valley veteran that has reinvented itself twice - from a memory technology inventor into a patent-licensing house, and over the past decade into a fabless as memory interface chip supplier. Founded in 1990 by Stanford engineers Mike Farmwald and Mark Horowitz and listed on Nasdaq in 1997, the company first rose to prominence with RDRAM, a proprietary high-speed memory interface adopted by Intel around the Pentium 4 era. When the industry standardized on DDR SDRAM instead, Rambus spent the following decade monetizing its patent estate through litigation and licensing against the major DRAM manufacturers, a history we detail in the Royalties business section below. The pivot back to silicon began in 2016 with the acquisition of Inphi's memory interconnect business, which brought DDR4 buffer chips, and accelerated under current CEO Luc Seraphin, who was appointed in 2018 and refocused on memory interface chips.

Today, Rambus operates three revenue pillars: memory interface chips, where it ranks third globally with \~21% share of the core market in 2024; patent royalties from DRAM manufacturers; and silicon IP licensed to computing chip designers. The company generated USD 708Mn of revenue in 2025, up 27% YoY.

## PRODUCT OFFERINGS

Rambus runs two broad business segments, Products and Royalties/ IP Licensing, which are reported in three lines in its financial statements: Product revenue, Royalty revenue, and Contract & other revenue.

The Product line consists of memory interface chips integrated in DDR modules to connect with server CPU, improving bandwidth and signal integrity for servers. This spans the core memory interface chips (RCD, DB, MRCD, MDB, and CKD) and the complementary supporting chips (SPD Hub, PMIC, temperature sensors, and voltage regulators). Product revenue contributed 49% of total revenue in 2025 and grew 40.9% YoY, making it the company's largest and fastest-growing line.

The Royalties/ IP Licensing segment monetizes two distinct groups of IP for two distinct customer bases, memory manufacturers and computing chip designers. IP inside the DRAM module contributed \~33% of 2025 revenue and grew in LSD YoY. These patents are mainly related to the module's device physics and architecture, licensed to memory manufacturers under 10-20 year contracts structured as fixed upfront payments or per-module royalties with caps. Silicon IP contributed the remaining \~18% of 2025 revenue and is guided to grow at 10-15% YoY. Silicon IP licenses IP inside computing chips to ASIC/ SoC designers, including memory controllers IP for DDR/ HBM/ LPDDR/ GDDR and interconnect IP for PCIe/ CXL, as well as security IP spanning root of trust, secure networking, quantum-safe cryptography, and anti-counterfeit. These engagements combine license fees with engineering contracts carrying milestone payments.

EXHIBIT 1: Rambus has two primary business segments but reports financial statements in three lines. Two business segments ride on the wave of CPU Renaissance and AI ASIC respectively  
![](images/4de59ecd7c4f048d76da2e6efb8e0ad520a42f2753be57d183607d72bd39f412.jpg)  
The revenue mix and growth rate numbers are operational approximations per management commentary, not formal reporting segments  
Source: company reports, Bernstein analysis

## BUSINESS MODEL

The two segments run on fundamentally different business models - one sells chips, the other licenses IP rights.

The memory interface chip Product business is a classic fabless model: Rambus designs the chipsets, outsources fabrication to foundry partners, and sells physical chips to Samsung, SK hynix, and Micron. Revenue scales directly with module volumes and content per chipset, giving the business full exposure to the server memory upgrade cycle.

The Royalties and Silicon IP businesses are licensing models: Rambus monetizes intangible assets through long-duration patent contracts and design-win-based IP licenses with engineering milestones. Licensing revenue is extremely high-margin and recurring, but its growth is bounded by contract structures.

Overall, the Product business carries the growth story, while licensing provides the stable cash flow that funds R&D.

## MEMORY INTERFACE CHIPS: ACCELERATING TAM GROWTH

As we have elaborated in our memory interface chip primer, these chips are a core beneficiary of the Agentic AI era, and Rambus enjoys the full strength of this industry beta. Agentic AI is structurally reshaping demand for server CPUs, DDR memory, and the interface chips connecting them. As workloads shift from GPU-centric training toward inference-heavy agentic deployments, the CPU reclaims its role as orchestrator of multistep, sequential tasks.

EXHIBIT 2: Providing memory interface chips for RDIMM & MRDIMM alongside Montage, Rambus is the only supplier of SOCAMM2 interface chips today  
![](images/32bdef3274fa8b7ffe2e4e16a14a2360a4b83f2542596cdfedb090cff1db07de.jpg)  
Source: company reports, Bernstein analysis

We project the global memory interface chip TAM to grow at \~65% CAGR'25-'30 to reach USD 20Bn in 2030. The strong momentum will be driven by three compounding tailwinds: rising server CPU volumes, more DRAM package per CPU, and higher chipset value per module through the MRDIMM upgrade. MRDIMM is the single largest contributor: we project MRCD and MDB to account for 73% of 2030 TAM, as interface silicon content per MRDIMM module runs roughly 10x that of RDIMM. Importantly, the downside is well protected: even in a bear-case scenario on CPU shipments and MRDIMM penetration, the 2030 TAM still reaches our prior-version projection in \$ 8Bn.

EXHIBIT 3: We raise our global memory interface TAM projection to USD 20Bn in 2030, with MRDIMM's MRCD and MDB contributing 73%, driven by significantly higher chipset value per module

Global memory interface chips TAM (Bn USD)  
![](images/9296b08f5815eb8fc8835008b2b6197cd428bd3dbc7800c06f41de82e312ec51.jpg)

Our TAM forecast does not include memory interface chips used in NVIDIA proprietary CPUs, such as voltage regulators and PMICs. We expect the impact to be only LSD, as NVIDIA CPUs account for a small portion of server CPU shipments and the related components are of relatively low value.
Source: Mercury, TrendForce, Gartner, Bernstein analysis and estimates

EXHIBIT 4: The expansion of the TAM is driven by three core factors, each of which is expected to accelerate in the second half of this decade relative to the past 5 years

Driver 1: Global server CPU shipment vol (Mn units)

![](images/fd24dbe81ea37b21989623c6f60f1e4f8dbdc6fdb3b6a417f615dc83fa9bbb55.jpg)  
Driver 2: Avg. # of DIMM package per CPU (Units)

Source: Gartner, Mercury, Bernstein analysis and estimates

![](images/38b7067d820992315994fdc5990aea9cd4fbc28aa62bd1aa2d83e9e3205a40b6.jpg)  
Driver 3: Avg. \$ content of interface chips per DIMM module (USD)

![](images/f4e4631f7ff50335928fbb120cfacadbdeb00bb50ea841c77122d99f8be2eb42.jpg)

EXHIBIT 5: 2030 TAM Sensitivity Analysis: Even in a bear-case scenario, the global memory interface chip TAM reaches our prior-version projection, reinforcing a well-protected downside for all memory interface chip suppliers

<table><tr><td rowspan="2" colspan="2">2030 TAM sensitivity analysis (Bn USD)</td><td colspan="7">Server CPU shipment in 2030 (excl. NV, Mn units)</td></tr><tr><td>60</td><td>70</td><td>80</td><td>89</td><td>100</td><td>110</td><td>120</td></tr><tr><td rowspan="7">MRDIMM penetration in 2030</td><td>10%</td><td>8</td><td>9</td><td>10</td><td>12</td><td>13</td><td>14</td><td>16</td></tr><tr><td>15%</td><td>10</td><td>11</td><td>13</td><td>14</td><td>16</td><td>18</td><td>19</td></tr><tr><td>20%</td><td>12</td><td>13</td><td>15</td><td>17</td><td>19</td><td>21</td><td>23</td></tr><tr><td>25%</td><td>13</td><td>16</td><td>18</td><td>20</td><td>22</td><td>24</td><td>27</td></tr><tr><td>30%</td><td>15</td><td>18</td><td>20</td><td>23</td><td>25</td><td>28</td><td>30</td></tr><tr><td>35%</td><td>17</td><td>20</td><td>23</td><td>25</td><td>28</td><td>31</td><td>34</td></tr><tr><td>40%</td><td>19</td><td>22</td><td>25</td><td>28</td><td>32</td><td>35</td><td>38</td></tr></table>

Source: Bernstein analysis and estimates

Within this expanding market, Rambus competes from the third position in a textbook oligopoly and holds a differentiated footprint across module form factors. The top three players consolidated 90% of the core memory interface chip market in 2024, with Rambus as \~21% behind Montage and Renesas. For DDR5 RDIMM RCD, Rambus management claims that the company is expanding its market share continuously. The company has also closed its historical gap in complementary supporting chips through sequential in-house development since 2022 to pursue a “full chipset” strategy, as management noted that customers increasingly want the whole chipset from one supplier for interoperability reasons at high speed. Now Rambus offers a fully in-house chipset for both RDIMM and MRDIMM, and the management has guided the complementary supporting chips to contribute mid-double-digit percentage of revenue by year end 2026. Notably, Rambus is today the only supplier of SOCAMM2 interface chips, giving it a first-mover position in emerging socket.

As a late entrant to MRDIMM, Rambus has material room to expand share in the segment where the TAM growth is concentrated. Skipping the MRDIMM Gen 1, Rambus directly resources to Gen 2. Starting from a currently almost negligible share base, every Gen 2 design win is incremental: we model Rambus's MRDIMM interface chipset share rising from 2% in 2026 to 18% by 2030, conservatively assuming its long-term market share in MRDIMM chipset lower than that in RDIMM chipset. Meanwhile, management has also guided for continued share gains in complementary supporting chips, where its portfolio build-out is now complete. In short, the company's share trajectory in the highest-growth product category points upward from a low base, a favorable setup relative to competitors defending high shares.

EXHIBIT 6: The core memory interface chips market is a textbook oligopoly, with top 3 players consolidating 90+% of market share. Rambus is ranked in the 3rd place.

Market landscape of the core memory interface chips in 2024

![](images/a00a085ba91c18306c314f38ef436b7de02e24b5f8f8fc4e6b403c6fa496e3f4.jpg)  
Source: company reports, Bernstein analysis and estimates

EXHIBIT 7: Three industry leaders remain closely matched in DDR5 RDIMM and MRDIMM offerings. However, Rambus is the late entrant in MRDIMM memory interface chips  
![](images/acae60270c64ee3c1573fe

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
