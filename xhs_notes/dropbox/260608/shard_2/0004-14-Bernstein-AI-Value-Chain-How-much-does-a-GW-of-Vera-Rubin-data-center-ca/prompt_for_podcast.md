你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
# U.S. Semiconductors

# AI Value Chain: How much does a GW of Vera Rubin data center capacity actually cost?

![](images/6a007864d27000374e8dbf648bfdbf3602dab1941e7919a2cd8519fec60b135d.jpg)

Stacy A. Rasgon, Ph.D.

+1 213 559 5917

stacy.rasgon@bernsteinsg.com

![](images/a2a4ba8d1793f4ab2c0b0e55d9bf01809a61e227a6bd76003e1ad31d62d82b8d.jpg)

Daniel Zhu

+1 917 344 8309

daniel.zhu@bernsteinsg.com

![](images/f78547a0289e94264f8fc4ec20b097b80387da5b02cd0d41c9ed0829fd23f40b.jpg)

Alex Wang, CFA

+852 2123 2613

alex.wang@bernsteinsg.com

![](images/6c54cc123025bb0a9b1bf368db0cc9aefbb1b4744d26052cec187ddccc18eeb4.jpg)

Mark Li

+852 2123 2645

mark.li@bernsteinsg.com

![](images/e61b6cfafe57b7a210e4be77abdd5a06b8b00f11f8027cc30d1c866c346b6345.jpg)

David Dai, CFA

+852 2918 5704

david.dai@bernsteinsg.com

![](images/f72fa8b2dea528e94aa00b7db831daa23ce07dedb28ff996921b227735d42552.jpg)

Madison Rezaei

+1 917 344 8622

madison.rezaei@bernsteinsg.com

![](images/c5d0e9e3e8cfad813edc7be3e3b5f0ef361435a75577c873e8efc30b6b9089dd.jpg)

Chad Dillard

+1 917 344 8469

chad.dillard@bernsteinsg.com

![](images/9653dd6a6da8a1f73565d03843f9c27e782d9ed4c4c63883c93ef7c1d305c76f.jpg)

Mark C. Newman

+1 212 845 7822

mark.newman@bernsteinsg.com

![](images/826f68a9ce74d009c966b15d39715534de57c8739d2d4cc47dc795abc57ed4ef.jpg)

Arpad von Nemes

+1 917 344 8461

arpad.vonnemes@bernsteinsg.com

![](images/5bd4937eb06b9912e52dec20941c58cbf529827b63be9774f5abfbc79079c2cc.jpg)

Alrick Shaw

+1 917 344 8454

alrick.shaw@bernsteinsg.com

![](images/1f76fa6854846b8b4d8ecdd14a782cb6d32f39e731fb973079d0c871baa9af97.jpg)

Shirley Yang, CFA

+852 2123 2660

shirley.yang@bernsteinsg.com

![](images/3457a8dd4f91b14cf68fb247ceb56af0791ec84c5a31b2a8f1ba44e84b311b2a.jpg)

Ethan Xu

+852 2123 2634

ethan.xu@bernsteinsg.com

![](images/ba29f684eacdaffef0a464d9025b60d8e80660633a3159f7b389cd376b5132ad.jpg)

Yipin Cai, CFA

+852 2123 2669

yipin.cai@bernsteinsg.com

Based on a series of conversations with industry experts as well as third-party data on physical infrastructure, we update our estimates of rack-level AI data center economics for the Vera Rubin NVL 72 architecture. This note includes our analysis and key takeaways. Excel backup is available on request.

We estimate that a typical VR / NVL72 rack costs \~\$9.1M per rack. This estimate is notably higher than the \~\$8M figure reported in the media, which appears to be based on stale memory prices. We believe the disconnect is largely coming from HBM - we land at a similar figure if we use HBM 4 price of \~\$16.6 / GB, but we expect the price to increase to \$53 / GB in 2027, when Vera Rubin will be shipping in volume, and we further believe Nvidia will pass these costs on to end customers. Overall, we believe memory / storage costs will be close to \~\$3.2M, higher than the \$2M implied by historical prices. Investors should also modify estimates as memory prices change.

Even with increased memory costs, the GPU remains the largest contributor to cost.

We believe \~\$4M in cost is coming from the GPU (ex. HBM). Costs are less transparent outside of compute and memory / storage, but we believe that networking comprises \$1.2M of the remaining \~\$2M, led by NVLink and SpectrumX switches. Cooling and power delivery costs were also significant at \~\$150k each.

We estimate all-in AI data center capex of \~\$47B per GW. Given that the Vera Rubin NVL 72 rack is rated for 220 kW, our estimate that the rack consumes \~80% of data center power, and coupled with \$15B in physical infrastructure costs per GW, this points to all-in AI data center capex of \~\$47B per GW.

Notably, this appears to represent a continued acceleration in FP8 performance per dollar. The Vera Rubin NVL72 rack performs at 2,520 PLOPS, up from 720 for Blackwell, implying meaningful acceleration in compute capacity, both on a per GW and a per \$ basis

Given the shorter depreciation lifespan of IT Hardware such as servers and networking compared to mechanical & electrical equipment or land & buildings, and given that operating costs are relatively low, the true economic costs are likely even more heavily weighted towards servers and networking compared to what cash capex would imply. Even at an elevated cost of \$0.15/kWH, it costs \~\$1.3B in electricity to run a GW of data center capacity for a year. Personnel costs are also negligible, leaving \~\$7.2B in annual depreciation as the dominant operating cost.

Looking forward, we expect cost per GW to continue to increase, pointing to increases in power demand that lag the growth in hyperscalar capex. We also see major increases in DRAM and power content and believe substrate content is also increasing.

Available compute continues to accelerate, which could help to unlock further AI adoption.

BERNSTEIN TICKER TABLE 

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">5 Jun 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>NVDA (NVIDIA)</td><td>O</td><td>USD</td><td>205.10</td><td>315.00</td><td>22.2%</td><td>USD</td><td>4.77</td><td>9.19</td><td>12.52</td><td>43.0</td><td>22.3</td><td>16.4</td></tr><tr><td>3037.TT (Unimicron)</td><td>O</td><td>TWD</td><td>933.00</td><td>990.00</td><td>770.8%</td><td>TWD</td><td>4.36</td><td>14.06</td><td>25.10</td><td>213.9</td><td>66.4</td><td>37.2</td></tr><tr><td>2308.TT (Delta)</td><td>O</td><td>TWD</td><td>2,300.00</td><td>2,620.00</td><td>438.7%</td><td>TWD</td><td>23.09</td><td>37.09</td><td>58.40</td><td>99.6</td><td>62.0</td><td>39.4</td></tr><tr><td>2382.TT (Quanta)</td><td>U</td><td>TWD</td><td>390.50</td><td>250.00</td><td>(0.6)%</td><td>TWD</td><td>18.91</td><td>21.07</td><td>23.08</td><td>20.6</td><td>18.5</td><td>16.9</td></tr><tr><td>2360.TT (Chroma ATE)</td><td>O</td><td>TWD</td><td>2,565.00</td><td>1,660.00</td><td>597.1%</td><td>TWD</td><td>27.50</td><td>33.22</td><td>43.66</td><td>93.3</td><td>77.2</td><td>58.8</td></tr><tr><td>DLR (Digital Realty)</td><td>O</td><td>USD</td><td>186.79</td><td>232.00</td><td>(18.1)%</td><td>USD</td><td>3.87</td><td>2.74</td><td>2.37</td><td>48.3</td><td>68.3</td><td>78.7</td></tr><tr><td>EQIX (Equinix)</td><td>O</td><td>USD</td><td>1,080.95</td><td>1,222.00</td><td>(5.5)%</td><td>USD</td><td>14.96</td><td>17.88</td><td>21.36</td><td>72.3</td><td>60.4</td><td>50.6</td></tr><tr><td>CRWV (CoreWeave)</td><td>U</td><td>USD</td><td>100.39</td><td>67.00</td><td>(50.0)%</td><td>USD</td><td>(1.20)</td><td>(4.20)</td><td>(2.41)</td><td>36.0</td><td>14.1</td><td>7.5</td></tr><tr><td>SPX</td><td></td><td></td><td>7,383.74</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ASIAX</td><td></td><td></td><td>1,975.13</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended   
3037.TT, 2308.TT, 2382.TT, 2360.TT estimate is Reported EPS; NVDA, DLR, EQIX valuation is Adjusted P/E (x); CRWV valuation is EV/EBITDA (x); NVDA base year is 2026;   
Source: Bloomberg, Bernstein estimates and analysis.

# INVESTMENT IMPLICATIONS

NVDA (OP, US\$315.00): We rate Nvidia Outperform, PT=US\$315.00.

Unimicron (OP, NT\$990.00): We rate Unimicron Outperform, PT=NT\$990.00.

Delta (OP, NT\$2,620.00): We rate Delta Outperform, PT=NT\$2,620.00.

Quanta (UP, NT\$250.00): We rate Quanta Underperform, PT=NT\$250.00.

Chroma (OP, NT\$1,660.00): We rate Chroma Outperform, PT=NT\$1,660.00.

Digital Realty (OP, \$232): We rate DLR Outperform, PT=\$232.

Equinix (OP, \$1,222): We rate Equinix Outperform, PT=\$1,222.

Coreweave (UP, \$67): We rate Coreweave Underperform, PT=\$67.

# DETAILS

Based on a series of conversations with industry experts, supply chain checks, and third party data on out-of-rack costs of land and physical infrastructure, we update our estimates of GB200/NVL72 AI data center rack-level economics for the Vera Rubin NVL72 architecture. This note includes our analysis and key takeaways. See AI Value Chain: How much does a GW of data center capacity actually cost, and what goes into it? for our original view on the Blackwell cycle, and our Black Book for our updated perspective: Artificial Intelligence: The AI Infrastructure Value Chain

# We believe the Vera Rubin NVL 72 to be an \~\$9.1M rack. This estimate is notably higher than the \~\$8M figure reported in the media, which we believe to be based on stale memory prices. For our breakdown of rack costs, see:

Exhibit 1. We construct a bottom-up estimate of Vera Rubin NVL 72 rack costs, and land at \$9.1M. Notably, this is notably higher than the \$8M figure which has been widely reported in the media. We believe the disconnect is largely coming from memory prices: if we use the historical HBM 4 price of \~\$16.6 / GB, we land at a similar figure. However, we expect HBM 4 prices to increase to \$53/GB by 2027, when Vera Rubin will be shipping in volume. Moreover, we believe that Nvidia likely has some form of dynamic pricing mechanism, and will pass on this increase to customers instead of absorbing it as a hit to margin. As a result, we believe memory / storage costs will be close to \~\$3.2M, significantly higher than the \$2M implied by historical prices. This also serves as a reminder that our own cost breakdown will rapidly become stale, and investors using these estimates will need to frequently reflect volatility in memory prices in order for numbers to be accurate. That said, even with the increase in memory price, the GPU (ex. HBM) remains the largest part of cost, accounting for \~\$4M. Costs are less transparent outside of compute and memory / storage, but we believe that networking comprises \$1.2M of the remaining \~\$2M, while cooling and power delivery costs are also significant.

\- GPU / CPU. Our views are consistent with widespread reporting that the Rubin GPUs are selling for \$55k per GPU $^{1}$ . At 72 GPUs per rack, this implies \$3.96M in GPU cost alone, nearly half of the rack cost. Similarly, the Vera CPU is reportedly selling for \$5k per CPU, pointing to \$180k in total cost for 36 CPUs per rack.

\- Memory and storage. We expect memory and storage costs to land at \$3.2M per rack (about 35% of rack costs), significantly above the \~\$2M implied by using historical prices. We believe this is the main driver of the differentiation between our estimate of \$9.1M in rack costs, vs. media reports that this is a \~\$8M rack. This also serves as reminder that, given continued volatility in DRAM and NAND prices, our own estimates will likely become stale relatively quickly, and that investors following the space should frequently reflect fluctuations in DRAM and NAND prices in order to maintain accurate forecasts.

\- High-Bandwidth Memory (HBM). Nvidia's published spec (link) lists 20.7 TB of HBM 4 (Exhibit 2). We currently model HBM 4 is priced at \$16.63 / GB $^{2}$ (for more details on HBM, see: Global Memory: Price increase more than expected in 2QCY26). However, we expect HBM 4 prices to increase to \$48 / GB in 2027, when Vera Rubin will be shipping in volume. Moreover, Nvidia may have a dynamic pricing mechanism. As a result, instead of absorbing the cost increase as a hit to margin, Nvidia should be able to pass on the increase to end customers, and likely even collect a \~10% markup, pointing to \~\$53/GB for HBM in the BOM paid by customers. Reflecting this price increase increases the HBM contribution from \$344k to \$1.1M, which we believe to be the biggest driver in our differentiation from the widely reported \~\$8M rack cost figure.

\- CPU DRAM. The VR spec includes 54 TB in LPDDR5X CPU memory. While the 2Q26 contract price for mobile LP5X is \$11.43 / GB, our channel checks suggest that Nvidia's SOCAMM architecture includes a 30% premium over mobile DRAM prices. As a result, we price DRAM at \$14.85 / GB, and land at \$802k per rack in CPU DRAM content. We also expect LPDDR price to rise further in 2H26, but likely peak and the fall some time in 2027 or 2028. This presents a cost uncertainty to Nvidia. The possible shortage of LPDDR may also limit the shipment of VR, & standalone Vera CPU. Accordingly, Nvidia may choose to install a lower default DRAM capacity but allow customers install more after VR or standalone Vera CPU is shipped so that customers can balance their need against the latest memory price to determine the optimal DRAM capacity for them. Alternately, Nvidia may choose to price VR & standalone Vera dynamically based on the latest DRAM price reflect uncertainties.

\- Direct-attached storage. Direct-attached storage is somewhat less transparent, given that storage is excluded from Nvidia's specs and there is likely room for configuration variance. However, for GB200 NVL72, we anchor to Super Micro's data sheet (link), which lists 8 E1.S drives for each of the 18 compute trays, or a total of 144 slots. Assuming each of those slots are 15.36 TB (in line with the Solidigm D7-PS1010), and each tray has another 2 TB M.2 boot drive, that points to 2.2 PB of total NAND content for Blackwell. For Vera Rubin, we assume constant E1.S content and add 16.9 GB / GPU in ICMS content, for 3.5 PB in total NAND. Assuming TLC NAND prices of \$0.37 / GB (which assumes a 30% premium over current client prices, consistent with the premium paid for DRAM), we land at \$1.3M per rack in storage content.

\- What about HDDs? Our analysis is focused on server racks and thus server direct-attached storage. Given the dramatic increase in NAND prices, direct-attached storage is now a far more material portion of costs than during our analysis last year, when NAND was 75% cheaper and NAND content was also lower. Furthermore, NAND availability has also been a growing concern (albeit somewhat insulated by AI buyers' willingness to pay a premium and outbid the smartphone and PC industries for limited supply). However, data center operators appear hesitate to substitute NAND for HDDs for direct-attached storage, as the drop-off in performance remains a concern, especially since using lower-performance storage can increase the burden on memory, when DRAM and HBM are also scarce. Moreover, because HDDs are physically larger and consume more power compared to NAND, incorporating HDDs within-rack (as opposed to on external storage arrays) could require significant redesign, which may not be possible for some of the tier 2 CSPs. With that said, less latency-sensitive cold storage use cases (such as the later stages of SSN attention networks) are often stored on external storage arrays, which actually account for the majority of storage capacity. In external storage, we have seen greater adoption of HDDs, consistent with the industry average of 20% NAND and 80% HDDs in terms of GB storage capacity. For a primer on the HDD industry, see: Global Hard Disk Drives: It's HAMR time! A primer on the HDD industry and why STX is poised to reap outsized rewards.

\- Memory and storage prices remain volatile; investors (and industry participants!) will need to track prices closely. At the risk of stating the obvious, despite a MoM stabilization of NAND prices in May, overall memory prices remaining more volatile than history, with NAND prices increasing 11.3x from the trough in April 2023 to May 2026 (115% CAGR), which contrasts sharply with the January 2019 to April 2023 trend of -20% CAGR (Exhibit 3). Moreover, we believe that Nvidia likely has dynamic pricing mechanisms to protect its own margins, and price fluctuations are being passed on to end customers. As a result, investors (and industry participants!) that are leveraging this analysis will need to frequently reflect memory / storage price fluctuations in order for estimates to remain accurate. Our latest estimates for DRAM and NAND prices can be found in our monthly memory price tracker: MEMORY TRACKER (May): Price hike c. 60% QoQ in 2QCY26, but likely at a slower pace in 2HCY26

- Networking. There is likely more variance in networking architectures (and thus costs), especially given replacing the SpectrumX top of rack switch with a third party scale-out switch appears to be one of the more common deviations from Nvidia's reference architecture among hyperscale customers. However, based on our conversations with industry participants, we see \~13% of rack costs in networking costs as typical, including 8% for scale-up and 5% in scale-out. Within that, we estimate \~\$250k for NVlink switches across 18 chips (9 switch trays and 2 NVSwitch chips each), \~\$240k in cabling, and \~\$380k in backplanes and other scale-up content. Similarly, we estimate the SpectrumX Switch at \~\$200k, and believe it to be about half of the total cost of the scale-out fabric.   
- Cooling, power delivery. We estimate power content as ramping from \~\$50k per rack for GB200 to \~\$150k for VR (Exhibit 4 - for more details, see: Delta Electronics 1Q26: adding capacity for long-term AI demand. PT raise to NT\$2,620). Based on conversations with industry contacts, we estimate cooling at \~\$160k (2% of total rack cost).   
- Others. Our conviction levels are lower for some of the components which are a smaller part of the BOM, as they are more likely to be excluded from the specs and harder to size top-down. Notably, while multilayer ceramic capacitors (MLCCs) have become a hotly debated topic, we were unable to form a high conviction view. However, based on industry conversations, our best guess is that the rack chassis costs \~\$100k, and there is perhaps another \$100k in other rack content, landing at a \$9.1M BOM.

Given that the Vera Rubin NVL 72 rack is rated for 220 kW, and that we believe the rack consumes \~80% of data center power, that points to 3.6k racks per GW, or \$32B in rack cost per GW. Coupled with \$15B in physical infrastructure costs per GW, this points to all-in AI data center capex of \~\$47B per GW - Exhibit 5.

\- \~\$9.1M in cost per rack translates to \$32B in rack cost per GW. We observe that, without redundancy, the VR rack is designed for 220 kW per rack, up from 130 kW for GB200. We maintain our estimate from GB200 that the rack is 78% of the data center power load $^{3}$ , implying 281 kW in total data center power consumption per rack, or that a GW of power can support 3,557 racks. This in turn implies 32.3B in rack cost per GW.

\- \$47B per GW in total capex. Based on our conversations with data

[中间内容因长度限制已省略]

ence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engage in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek for independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
