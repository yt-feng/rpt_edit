你是知乎商业/行业研究作者，擅长把英文/中文研报改写成适合知乎发布的长文。

【目标】
- 基于下面研报解析内容，生成一篇中文知乎文章。
- 风格接近微信公众号文章，但更适合知乎：论证更完整、语气更克制、有问题意识、有推理链条。
- 文章不需要把研报所有内容讲完，要留下继续阅读完整报告或加入社群讨论的空间。
- 目标长度：约 2200 字，允许上下浮动 20%。

【结构要求】
1. 第一行：知乎标题，直接讲观点，不要标题党，不要夸张极限词。
2. 开头 2-3 段：用一个真实问题或市场分歧切入，说明为什么这份报告值得看。
3. 正文按金字塔原则组织：先给核心判断，再展开 3-5 个支撑逻辑。
4. 每个小标题都要像观点句，不要写“核心判断”“支撑逻辑一”“对读者的启发”这种模板名。
5. 内容要比小红书更理性，比微信更像问答式分析，可以适度提出反问。
6. 结尾自然留下讨论空间，可使用这类表达：`完整报告里还有不少细节，适合放在社群里继续拆。`

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- 不要写“非投资建议”“仅做学习交流”这种免责声明，也不要出现包含“投资”的免责声明。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要使用“爆款”“震惊”“必看”“必读”“最强”“最全”“唯一”“全网首发”等极限词。

【内容要求】
- 只能基于研报原文和解析内容推导，不要编造数据、页数、作者、结论或引用。
- 可以基于报告内容做适度发散，但必须明确哪些是报告内容，哪些是你的延展观察。
- 默认避免具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或使用 GS/JPM/MS 等缩写。
- 不要输出解释说明，只输出知乎文章正文。

【研报解析内容】
"""
# China and Japan Semiconductors

# Global Semis: SOCAMM2 - Innovative but niche, limited impact on memory interface chip TAM

![](images/4a0c8f97d494d4598a75de9e645ca2555c4a9c92095984bec5b5d4c3fb4901d6.jpg)

Qingyuan Lin, Ph.D.

+852 2123 2654

qingyuan.lin@bernsteinsg.com

![](images/61d73a22c42e2edc97eaf9b1fa7f02ff5058179deb82113a4fa758afbf5fbad7.jpg)

David Dai, CFA

+852 2918 5704

david.dai@bernsteinsg.com

![](images/524ecd47d421a5ebb096de5bcf97319e0497300c248d80a326df4adf6c150925.jpg)

Francis Ma

+852 2123 2626

francis.ma@bernsteinsg.com

![](images/cb105ca795174ceb43929b1965ec9578e29766463803f75c6cc9eb15f348047f.jpg)

Kai Zhang

+852 2123 2665

kai.zhang@bernsteinsg.com

Nvidia recently released their latest ARM-based server CPU called Vera, in which they used a new memory package format called SOCAMM2. As this new package uses much less memory interface chip content, some investors are concerned that this will reduce the TAM for Montage/Renesas. We believe the SOCAMM2 format will likely remain niche to Nvidia and thus only bring HSD to LT% impact to the memory interface chip TAM, reiterate Outperform on Montage and Renesas.

SOCAMM is a DRAM package customized for NVIDIA rather than a disruptive new standard. In Nvidia's Grace CPU design, they use LPDDR5x instead of DDR5 to reduce the power consumption. From Grace to Vera, the shift from soldered LPDDR5x to modular SOCAMM2 provides modularity flexibility and expands the total capacity/bandwidth. However, SOCAMM2 advantages are tightly aligned with NVIDIA's rack-level optimization, where maximizing performance-per-watt is paramount. Critically, these benefits come with trade-offs in capacity, bandwidth, and ecosystem maturity compared with MRDIMM, therefore we expect this solution will remain niche mainly to Nvidia, which we estimated to only have HSD to LT% in volume in the next few years.

Other high-end ARM-based CPU and x86 server CPU likely will remain using MRDIMM if they want to enjoy better capacity and bandwidth. NVIDIA's adoption reflects its full-stack control and greenfield design, enabling re-design at rack level for their specific target. In contrast, x86 and other ARM CPU vendors are already fully integrated with the DDR ecosystem, they will face prohibitive switching costs across memory controllers, platform design, and ecosystem requalification, alongside loss of backward compatibility. Meanwhile, MRDIMM continues to offer superior bandwidth (up to 1.6TB/s vs 1.2TB/s per CPU) and capacity (up to 16TB vs 1.5TB per CPU) over SOCAMM2, making it difficult for the high end x86 server CPU design to shift module selection.

Economic impact on interface chip suppliers is modest. SOCAMM2 introduces incremental chipset content versus soldered LPDDR, but value per module is only a few dollars, far below DDR5 MRDIMM's interface silicon content at 50-70 USD, thus indeed if SOCAMM2 became mainstream the memory interface chip TAM will reduce. Yet if the package design will remain niche to Nvidia, then the impact to TAM will be limited to the Nvidia CPU vol share (HSD to LT%). Small incremental MRDIMM adoption could easily offset that impact. Additionally, SOCAMM2 also use some memory interface chip so the shift from LPDDR5 to SOCAMM2 within Nvidia actually brings some upside to the memory interface TAM. Rambus holds first-mover advantage at this stage, but we expect Renesas and Montage to catch up quickly given the relatively low technical barriers in SOCAMM2 interface chips.

We maintain Outperform on Montage and Renesas, with conviction reinforced by limited substitution risk. SOCAMM2 does not alter the structural dominance of DDR in the broader server market. For Montage, concerns around displacement are overstated, and the durability of MRDIMM-led growth remains the core investment thesis underpinning our positive view.

BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">17 Jun 2026</td><td colspan="2">TTMRel.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Target Perf.</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td><td></td></tr><tr><td>6809.HK (Montage)</td><td>O</td><td>HKD</td><td>420.60</td><td>320.00</td><td>NA</td><td>CNY</td><td>1.97</td><td>3.00</td><td>4.77</td><td>184.2</td><td>121.0</td><td>76.1</td><td></td></tr><tr><td>688008.CH (Montage)</td><td>O</td><td>CNY</td><td>262.50</td><td>220.00</td><td>181.0%</td><td>CNY</td><td>1.97</td><td>3.00</td><td>4.77</td><td>133.2</td><td>87.5</td><td>55.1</td><td></td></tr><tr><td>6723.JP (Renesas)</td><td>O</td><td>JPY</td><td>4,477.00</td><td>4,200.00</td><td>92.8%</td><td>JPY</td><td>181.61</td><td>242.22</td><td>270.50</td><td>24.7</td><td>18.5</td><td>16.6</td><td></td></tr><tr><td>ASIAX</td><td></td><td></td><td>2,032.93</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>JPL</td><td></td><td></td><td>2,631.42</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
6723.JP estimate is Adjusted EPS; 6723.JP valuation is Adjusted P/E (x);  
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate Montage Technology as Outperform and set a target price of CNY 220 for A shares, based on a 44x P/E multiple applied to 2BF (2027Q2–2028Q1) earnings. Given the company's high-growth profile and the anticipated new product launch cycle in 2027, we believe a 2BF P/E multiple provides a proper valuation anchor that captures the inflection in the company's earnings trajectory.

For H shares, we set a target price of HKD 320. The H share premium reflects that global investors favor Montage as a scarce China AI-exposed name without direct geopolitical risks, unlike many other Chinese semiconductor companies that face entity list restrictions or export control headwinds. At our target price, the implied P/E multiple on 2BF EPS for H shares is 56.4x.

Renesas: We rate Renesas Outperform, with PT = ¥4,200. With a market cap slightly above Montage's, Renesas appears significantly undervalued: its memory interface revenue, comparable in scale to Montage's, accounts for only single-digit % of total company revenue—the high-growth business is obscured by its broad product lines. We see re-rating opportunity for Renesas.

## DETAILS

## NVIDIA CPU DRAM TECH ROADMAP: FROM SOLDERED LPDDR TO MODULAR SOCAMM2

NVIDIA's server CPU platform is undergoing a key memory architecture transition. The current Grace CPU uses soldered LPDDR5X — high-bandwidth, power-efficient mobile DRAM physically bonded to the motherboard. While this delivers excellent performance-per-watt, it sacrifices field upgradeability: if memory fails or capacity needs change, the entire board must be replaced.

SOCAMM2 (Small Outline Compression Attached Memory Module 2) solves this by packaging LPDDR5X into a detachable, standardized module with a compression connector. Originally a proprietary NVIDIA design (SOCAMM1), the standard has been adopted by JEDEC under specification JESD328, with Samsung, Micron, and SK Hynix all developing compliant modules.

The transition from soldered LPDDR to SOCAMM2 enables multi-vendor memory sourcing and field serviceability for NVIDIA's server platforms for the first time, a critical requirement for hyperscaler adoption.

Micron has already demonstrated SOCAMM2 modules scaling from 128 GB to 256 GB per module using 32Gb LPDDR5X dies on 1 $\gamma$ process technology.

EXHIBIT 1: In the Grace generation, LPDDR5 is soldered directly onto the board, making it non-replaceable and preventing any changes to the memory configuration  
![](images/49a18eb150de3524bb61ed78ce2f0d07517003bd180d0436f8573b1ab1e2a939.jpg)

<details>
<summary>text_image</summary>

Blackwell Ultra GPU
Blackwell Ultra GPU
Grace CPU
LPDDR5
ConnectX-8 SuperNICs
</details>

Source: NVIDIA reports, Bernstein analysis

EXHIBIT 2: In the Vera generation, SOCAMM2 uses modular LPDDR5x connected to the board via a compression/ pressure connector, enabling a replaceable memory format  
![](images/3eb4224babf8c7f77347f2f113e42f4a201919dff510fb2cb3042c0e832335ef.jpg)

<details>
<summary>natural_image</summary>

Exploded view of a microchip module with visible internal components and external circuitry (no text or symbols)
</details>

Source: NVIDIA reports, Bernstein analysis

EXHIBIT 3: Diagram of NVIDIA Vera CPU and SOCAMM2 layout  
NVIDIA Vera CPU  
![](images/d0c22843ef0736ca030f84da74040495a374313ca2adc8ed6a4083aeedd6ba95.jpg)

<details>
<summary>text_image</summary>

Monolithic Compute Die
88 NVIDIA Custom Olympus Cores with 176 threads
162MB L3 Cache
2nd Gen NVIDIA Scalable Coherency Fabric (SCF)
Confidential Computing TEE-I/O Capable
Vera CPU
NVLINK-C2C
LPDDR CTRL
LPDDR CTRL
LPDDR CTRL
LPDDR CTRL
NVIDIA OLYMPUS CORE
LPDDR CTRL
LPDDR CTRL
LPDDR CTRL
NVLink-C2C
1,800GB/s Coherent
CPU-GPU Interface
1.5TB SOCAMM LPDDR5X
1.2TB/s Memory BW
x16 PCIe Gen 6
CXL 3.1
SYSTEM IO
</details>

Source: NVIDIA website, Bernstein analysis

## NVIDIA HALVES INITIAL VERA RUBIN SOCAMM2 CAPACITY

During the recent ComputeX, NVIDIA and SK Hynix unveiled that Vera Rubin NVL72 will ship with 96GB SOCAMM2 modules instead of originally specified 192GB, reducing rack-level CPU aggregated memory from \~55TB to \~28TB.

This spec adjustment reflects supply-side constraints in a nascent SOCAMM2 ecosystem, not weakening demand. LPDDR5x supply remains extremely tight. As an emerging niche product, SOCAMM2 has limited capacity in both memory manufacturers and interface chips vendor. By shipping lower-density modules, NVIDIA can deploy more racks under the same DRAM supply, accelerating the time-to-market.

Shipping 96GB modules delivers meaningful rack-level cost savings, lowering the system price from \$7.6Mn to \$6.8Mn per rack (estimated by SemiAnalysis). Clients requiring the full 1.5TB spec can upgrade to larger-capacity modules, when supply matures and pricing normalizes.

The move validates SOCAMM2's modularity advantage over Grace's soldered LPDDR. Had Vera used soldered memory, NVIDIA would have been forced to either delay shipments or permanently lock in a lower spec. SOCAMM2's detachable design explicitly enables the “install now, upgrade later” flexibility.

EXHIBIT 4: Leading memory manufacturers all begin to provide SOCAMM2 modules starting in 2026

<table><tr><td></td><td>Samsung</td><td>SK Hynix</td><td>Micron</td></tr><tr><td>Capacity variants for servers</td><td>192GB</td><td>96GB192GB</td><td>192GB256GB (industry first)</td></tr><tr><td>Total capacity per Vera CPU</td><td>1.5TB</td><td>0.75TB (96GB)1.5TB (192GB)</td><td>1.5TB (192GB)2TB (256GB)</td></tr><tr><td>DRAM tech generation</td><td>1b LPDDR5x</td><td>1c LPDDR5x</td><td>1y 32GB monolithicLPDDR5x</td></tr><tr><td>Data rate</td><td>Up to 9,600 MT/s</td><td>Up to 9,600 MT/s</td><td>Up to 9,600 MT/s</td></tr><tr><td>Mass production timeline</td><td>Early 2026 (first to mass produce)</td><td>2Q26 ramp up</td><td>Sampling(192GB in Oct &#x27;25;256GB in Mar &#x27;26)</td></tr></table>

Source: companies reports, Bernstein analysis

## TECHNOLOGY COMPARISON: DDR5 RDIMM/MRDIMM VS. LPDDR5X SOCAMM2

The three server memory architectures diverge meaningfully across the bandwidth, capacity, power, cost and ecosystem maturity. In summary, SOCAMM2 excels in power efficiency and compact design, closely aligning with NVIDIA's overarching strategy of rack-level vertical integration and maximizing tokens per second per watt. By comparison, DDR DIMMs maintain advantage in bandwidth and capacity, backed by a more established and mature ecosystem.

EXHIBIT 5: Spec comparison across DDR5 RDIMM, MRDIMM, and SOCAMM2

<table><tr><td></td><td>DDR5RDIMM (Gen 3)</td><td>DDR5MRDIMM (Gen 2)</td><td>LPDDR5xSOCAMM2 for NV Vera(original design)</td><td>LPDDR5xSOCAMM2 for NV Vera(adjusted design)</td></tr><tr><td>Data rate</td><td>6,400 MT/s (Gen 3)</td><td>12,800 MT/s (Gen 2)</td><td colspan="2">9,600 MT/s</td></tr><tr><td>Aggregated bandwidth for CPU</td><td>819.2 GB/s for 16-channel CPU(6400*64 bit*16-ch/8)</td><td>1,638.4 GB/s for 16-channel CPU(12800*64bit*16-ch/8)</td><td colspan="2">1,228.8 GB/s for NV Vera(9600*128bit*8 modules/8)</td></tr><tr><td>Memory capacity per module</td><td>16/32/64/96/128/256 GB</td><td>128/256/512 GB</td><td>192 GB</td><td>96 GB</td></tr><tr><td>Total capacity per CPU</td><td>Up to 8TB+(16-ch * 2 DIMM/Ch * 258GB)</td><td>Up to 16TB+(16-CH * 2 DIMM/Ch * 512GB)</td><td>1.5TB(8 SOCAMM2 * 192GB)</td><td>0.75TB(8 SOCAMM2 * 96GB)</td></tr><tr><td>Power efficiency</td><td>Moderate ~1.1v</td><td>Higher than RDIMM – due toadditional interface chips</td><td colspan="2">Best-in-class – 1.05V(total energy consumption 30% lower than RDIMM)</td></tr><tr><td>Compactness</td><td>288 pins, requiring vertical slotspace</td><td>Similar to RDIMM</td><td colspan="2">Highly compactlow-profile compression module, smaller footprint</td></tr><tr><td>Price per GB</td><td>$24.3</td><td>$50-75 (small sampling price)</td><td colspan="2">$29 (small sampling price)</td></tr><tr><td>Per module price</td><td>$3,200+ (128GB)</td><td>$6,000-9,000 (128GB)</td><td>$5,600 (196GB)</td><td>$2,800 (96GB)</td></tr><tr><td colspan="5"></td></tr><tr><td>Interface chip content</td><td>1 RCD + SPD + PMIC + TS (~$7)</td><td>1 MRCD + 10 MDB + SPD +PMIC + 2TS(~$50-70)</td><td colspan="2">Minimal – 1 SPD + 3 voltage regulators;direct-attach without RCD/DB chips(a few dollars)</td></tr></table>

The pricing reflects the contract rates for 2Q26 as updated by TrendForce in May 2026. As MRDIMM and SOCAMM2 are still in the early sampling stage, their ASPs represent sample pricing, which is expected to decline to normalized levels as production volume increases.

Source: companies reports, Bernstein analysis

EXHIBIT 6: Architecture comparison between SOCAMM2 and DDR5 RDIMM  
![](images/b3d518423c41e57daa297403f38d9bdc327974bc953d277a7d76b269c6dc4ef2.jpg)

<details>
<summary>natural_image</summary>

Close-up of a microcontroller DDR5 RDIMM 96GB, showing internal memory chips and RAM slots (no readable text beyond branding)
</details>

- \~133mm x \~31mm x \~2.5mm  
• 288 pins on edge connector  
• Vertical, insertion socket

![](images/9c323ded6e512fd514c1cc8a52a4170cf9f9de2cc8f7747d2477756c893febe5.jpg)

<details>
<summary>natural_image</summary>

Product image of SOCAMM2 chip with circuit board background (no readable text or symbols)
</details>

Source: AMD website, Bernstein analysis

- \~86mm x \~14mm x \~1mm  
- 694 pins on back  
• Horizontal, screw mounted

EXHIBIT 7: On x86 CPUs, DDR channels accommodate vertically inserted DIMM modules  
![](images/e28e2b85bdb76abb4a54c0f5f1e4d954e52c7b222964cbdeca5c4b858ea880f4.jpg)

<details>
<summary>natural_image</summary>

Close-up of an AMD7 EPYC processor on a computer motherboard with visible circuitry and components (no readable text beyond branding)
</details>

![](images/18e65468d881b8bf9756ee8a193f759ebd73d79ea687fc8df2d9414372d2851e.jpg)

<details>
<summary>natural_image</summary>

Close-up of a computer motherboard with green and black plastic components, no visible text or symbols
</details>

Source: AMD website, Bernstein analysis

EXHIBIT 8: In contrast, SOCAMM2 employs a horizontally compressed design, enabling a more space-efficient layout. Even the last generation LPCAMM2 saves 64% of space vs. DIMM module  
![](images/4d6a7dcaf70435e824b4218032818479c05dd1fba54062d6705fce017c8fd770.jpg)

<details>
<summary>text_image</summary>

LPCAMM2
64% space savings
2xSODIMM
78.0mm
4.5mm
9.3mm
3NC47 D8DHC
2X100000000000000000000000000000000000000000000000000000000000000000000000000000000000
Micron
LPCAMM2
47.1mm
34.0mm
2XSODIMM
74.9mm
</details>

Source: Micron, Bernstein analysis

On aggregate bandwidth, SOCAMM2 on NVIDIA Vera (\~1,229 GB/s) narrows the gap significantly versus 16-channel DDR5 RDIMM (\~819 GB/s), though it trails MRDIMM (\~1,638 GB/s). However, SOCAMM2's power advantage is substantial: at 1.05V with \~30% lower total energy consumption versus RDIMM, SOCAMM2 delivers superior bandwidth-per-watt — the metric that matters most in GPU-centric AI servers where CPU memory power competes with GPU compute for the system power budget.

The capacity trade-off is notable. SOCAMM2's total capacity of 1.5 TB (8 × 192 GB) is adequate for NVIDIA's AI server use case where HBM on the GPU handles the primary data set. However, it falls well short of x86 platforms that can deploy 8–16 TB+ via high-density RDIMM/MRDIMM configurations — a critical requirement for memory-intensive enterprise and HPC workloads.

On interface chip content, SOCAMM2 carries significantly lower value per module (\~\$3–5 for SPD and voltage regulators) compared to MRDIMM's \~\$70+ chipset. This differential is the core economic consideration for memory interface chip suppliers.

## PLATFORM ADOPTION: WHY WE BELIEVE THAT SOCAMM2 WILL REMAIN NVIDIA-SPECIFIC

We anticipate SOCAMM2 to remain largely NVIDIA-specific within the foreseeable future, rather than evolving into a broader industry standard across ARM-based and x86 server CPU ecosystems. The adoption of SOCAMM2 by NVIDIA should be understood less as a DRAM technology inflection point, but more a system-level architectural optimization tightly coupled to NVIDIA's AI platform strategy. This divergence fundamental differences in switching costs, architectural priorities, and ecosystem dependencies between NVIDIA's greenfield ARM platform and the deeply entrenched server ecosystem of mainstream suppliers.

NVIDIA's full-stack co-optimization justifies the architectural bet. NVIDIA is unique among server CPU vendors in its ability and willingness to redesign the entire compute stack from silicon on rack. The Vera CPU is not a standalone processor competing for socket share in the open server market; it is a purpose-built component within an integrated system spanning GPU, CPU, NVLink interconnect, thermal management, and rack-level power delivery. In this context, SOCAMM2 is not merely a memory module choice, but an architectural enabler within the entire NVIDIA AI rack. By adopting SOCAMM2, NVIDIA can optimize memory power consumption at the rack level, freeing thermal and electrical headroom for GPU compute. This system-level co-optimization is viable only when a single vendor controls the full stack, and it is precisely what differentiates NVIDIA's approach from the rest of server ecosystem.

Switching c

[中间内容因长度限制已省略]

egoing in connection with your own internal machine learning or artificial intelligence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
