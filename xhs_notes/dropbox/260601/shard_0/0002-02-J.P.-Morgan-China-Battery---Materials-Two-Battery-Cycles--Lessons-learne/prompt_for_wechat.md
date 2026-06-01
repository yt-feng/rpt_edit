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
This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

# China Battery & Materials

Two Battery Cycles: Lessons learned and investment strategy for 2H26-2027

We published a comprehensive 100-page deep-dive on 30 May, analyzing the China battery sector's two major upcycles. The China battery sector is transitioning from the 2021-22 supercycle – driven by price hikes and aggressive expansion – to a more selective recovery phase. In this cycle, we recommend investors shift focus from ‘price hike expectations’ to ‘volume-led cashflow and earnings delivery’. We advocate a range-bound trading approach for material and tier-2 battery makers: buy on weakness, take profit when expectations become crowded. In our 30-May report, we tactically upgraded CALB and Putailai to Overweight on attractive valuations (12-14x) and >40% volume-driven earnings growth for 2027E, without relying on price or unit profit increases. CATL remains our top pick and core holding, given its unmatched record of stable, through-cycle earnings growth – the sector’s only true compounder.

- 2021-22 supercycle vs 2025-current recovery cycle: The 2021-22 battery cycle was a true supercycle, driven by near-zero interest rates, rapid China EV penetration, aggressive capacity expansion, strong fund flows, and extreme raw-material price inflation. By contrast, the current cycle is more of a recovery cycle: demand is more diversified across EV and ESS, industry participants are more disciplined on capacity, ASP recovery is meaningful but far smaller than the last cycle, and valuations remain much lower. As a result, we believe the current cycle is less likely to deliver a broad one-way sector rerating and more likely to reward companies with sustainable earnings growth, strong utilization, and cash-flow resilience.   
- Lessons learned from the last cycle: Stock prices peaked well ahead of ASP or earnings highs, as the market rapidly prices in expectations of future price increases. For example, Yunnan Energy's share price reached its peak in Sep-Oct 2021, preceding or coinciding with the initial rebound in industry separator selling prices from their trough.   
- Investment focus likely to shift from ASP recovery to profit delivery. In the current battery cycle, we see the investment focus shifting from ASP recovery to volume-led earnings durability. The first phase of the rally from 2H25 to early 2026 was driven largely by a selling-price recovery across batteries and materials. However, with price recovery now increasingly embedded in market expectations and industry players starting to accelerate capacity expansion again, the next phase of equity performance is likely to be more selective, in our view. We expect investors to focus less on further ASP upside and more on whether companies can deliver stable cashflow and profit growth through volume.

# Asia Autos & EV Battery

Rebecca Wen AC

(852) 2800-8505

rebecca.y.wen@JPM.com

JPM Securities (Asia Pacific) Limited/

JPM Broking (Hong Kong) Limited

Cathy Liu

(852) 2800-8629

cathy.xiao.liu@JPM.com

JPM Securities (Asia Pacific) Limited/

JPM Broking (Hong Kong) Limited

Shirley Feng

(86-21) 6106-6149

shirley.x.feng@JPM.com

SAC Registration Number: S1730524040001

JPM Securities (China) Company

Limited

\- Range-bound trading in 2H26-1H27. This argues for a more range-bound trading approach for material names and tier-2 battery makers. In 2025, LFP cathode names such as Hunan Yuneng worked well as price-recovery trades, followed by separator names such as Yunnan Energy in 1H26 as ASP recovery and utilization improvement became more visible. Going forward, however, we would be more disciplined in buying these names on weakness and taking profit when expectations become crowded, especially where earnings recovery depends on further price increases or processing-fee expansion. For lower-valuation laggards, such as Putailai or selected tier-2 battery makers such as CALB, the opportunity may come from volume growth and operating leverage rather than ASP beta, but these should still be treated as cyclical trades rather than long-duration compounders, in our view.

\- CATL the only core holding that can exhibit outperformance through cycles. By contrast, we believe CATL remains the core long-term holding in the sector. It is the only major battery supply-chain company that has demonstrated stable and solid earnings growth through the cycle, supported by scale, technology leadership, stronger bargaining power, stable unit profitability and superior cash-flow generation. While materials and tier-2 battery names may offer better tactical upside at certain points in the cycle, their earnings are more sensitive to pricing, utilization and capacity expectations. CATL, in our view, deserves to be held through the cycle as the sector's quality anchor, while the rest of the supply chain should be traded more actively around valuation, ASP expectations and EPS revision momentum.

# Battery & materials ASP index in the two cycles vs stock price peak time (ASP bottom prices index to 100)

Figure 1: NCM Battery: Price Index vs. No. of months of price increase in the two upcycles (2022-2023 vs. 2025-now)   
![](images/ac39d1c25caba47811bafa220c3417cf73eef37e5481213e4673f9f3b32e9f03.jpg)

<details>
<summary>line</summary>

| Month | NCM (2022-2023 upcycle) | NCM (2025-2026 upcycle) |
|-------|--------------------------|--------------------------|
| Bottom | 100 | 100 |
| 1M | 110 | 105 |
| 2M | 115 | 108 |
| 3M | 125 | 110 |
| 4M | 130 | 115 |
| 5M | 132 | 115 |
| 6M | 133 | 115 |
| 7M | 135 | 115 |
| 8M | 138 | 115 |
| 9M | 138 | 115 |
| 10M | 138 | 115 |
| 11M | 138 | 115 |
| 12M | 138 | 115 |
| 13M | 140 | 115 |
| 14M | 140 | 115 |
| 15M | 140 | 115 |
| 16M | 140 | 115 |
| 17M | 135 | 110 |
| 18M | 120 | 100 |
</details>

Source: ICCSino, JPM.

Figure 2: LFP Battery: Price Index vs. No. of months of price increase in the two upcycles (2022-2023 vs. 2025-now)   
![](images/90344158364e0acf48aa5d8bcebe17f7e03bbca653cc1525d234a96e1baabdf0.jpg)

<details>
<summary>line</summary>

| Date | LFP (2022-2023 upcycle) | ESS battery (2025-2026 upcycle) |
|------|--------------------------|----------------------------------|
| 1M   | ~100                     | ~100                             |
| 2M   | ~105                     | ~105                             |
| 3M   | ~115                     | ~105                             |
| 4M   | ~130                     | ~105                             |
| 5M   | ~140                     | ~105                             |
| 6M   | ~145                     | ~105                             |
| 7M   | ~150                     | ~110                             |
| 8M   | ~150                     | ~115                             |
| 9M   | ~150                     | ~115                             |
| 10M  | ~150                     | ~120                             |
| 11M  | ~150                     | ~120                             |
| 12M  | ~150                     | ~120                             |
| 13M  | ~155                     | ~120                             |
| 14M  | ~155                     | ~120                             |
| 15M  | ~155                     | ~120                             |
| 16M  | ~155                     | ~120                             |
| 17M  | ~150                     | ~120                             |
| 18M  | ~130                     | ~120                             |
</details>

Source: ICCSino, JPM.

Figure 3: LFP Cathode: Price Index vs. No. of months of price increase in the two upcycles (2020-2022 vs. 2025-now)   
![](images/836caf0d8122e4bfc923cd8b5f43e6744ddb5943d8b1d9d8982d5dcd7b60d35f.jpg)

<details>
<summary>line</summary>

| Date       | LFP Cathode (2020-2022) | Premium LFP Cathode - EV (2025-2026) |
| ---------- | ------------------------ | ------------------------------------ |
| 2026.5.7   | 81                       | 180                                  |
| 2022.7.5   | 462                      | -                                    |
</details>

Source: ICCSino, JPM.

Figure 4: Artificial graphite anode: Price Index vs. No. of months of price increase in the last upcycle (2021-2022), no price hikes yet in 2025-26   
![](images/d06a7a288b7e930a226e7b4568043dc890c3ae698195fdf69c3e46294cf721a9.jpg)

<details>
<summary>line</summary>

| Date       | Stock Price |
| ---------- | ----------- |
| 2021.11.29 | 67          |
</details>

Source: ICCSino, JPM.

Figure 5: Separator: Price Index vs. No. of months of price increase in the two upcycles (2021-2022 vs. 2025-now)   
![](images/266f8991fc3f1878291c410710924a845ae8dc00449ad98cb937c8c44c3ddb31.jpg)

<details>
<summary>line</summary>

| Date       | Wet 9μm: mid-end (2021-2022) | Wet 9μm: mid-end (2025-2026) |
| ---------- | ---------------------------- | ---------------------------- |
| 1M         | 100                          | 100                          |
| 2M         | 100                          | 100                          |
| 3M         | 100                          | 100                          |
| 4M         | 100                          | 100                          |
| 5M         | 100                          | 100                          |
| 6M         | 100                          | 100                          |
| 7M         | 100                          | 100                          |
| 8M         | 100                          | 100                          |
| 9M         | 100                          | 100                          |
| 10M        | 108                          | 108                          |
| 11M        | 115                          | 128                          |
| 12M        | 120                          | 130                          |
| 13M        | 125                          | 130                          |
| 14M        | 125                          | 130                          |
| 15M        | 125                          | 130                          |
| 16M        | 125                          | 130                          |
| 17M        | 125                          | 130                          |
| 18M        | 125                          | 130                          |
| 19M        | 125                          | 130                          |
| 20M        | 125                          | 130                          |
| 21M        | 125                          | 130                          |
| 22M        | 125                          | 130                          |
| 23M        | 125                          | 130                          |
| 24M        | 125                          | 130                          |
</details>

Source: ICCSino, JPM.

Figure 6: LiPF6: Price Index vs. No. of months of price increase in the two upcycles (2020-2022 vs. 2025-now)   
![](images/a8a911c45b500a9c2f08b5c651c832cf50fd1a3746fb07cb3ad128413ae2baee.jpg)

<details>
<summary>line</summary>

| Date       | LiPF6 (2020-2022) | LiPF6 (2025-2026) |
| ---------- | ----------------- | ----------------- |
| 2026.5.6   | 64                | -                 |
| 8/21.10.29 | -                 | -                 |
</details>

Source: ICCSino, JPM.

# The two battery cycles: Similarities, differences, and valuation implications

# 2021-22 supercycle vs. 2025-current recovery cycle

Table 3 compares the 2021-22 battery supercycle with the 2025-current recovery cycle, and we believe the current cycle should not be valued as a simple repeat of the last one. The 2021-22 cycle was driven by a powerful combination of near-zero global interest rates, rapid rise in EV penetration, aggressive capacity expansion, large capital inflows, and extreme raw-material price inflation. By contrast, the 2025-current cycle is supported by recovering utilization, more diversified demand drivers, and renewed pricing momentum, but it is occurring in a relatively more disciplined capital-market and industry environment. In the last cycle, battery stocks peaked in 2H21 at roughly 40-80x 2022E P/E; in the current cycle, only CATL amongst the top players have exceeded prior share-price peaks, while most remain 30-80% below their 2021 highs and trade mostly at 15-25x 2027E P/E.

# Demand drivers: Single factor in 2022 vs multiple drivers in 2026

Demand is also structurally different. The 2021-22 cycle was mainly driven by China passenger-vehicle EV demand which contributed to \~45% of the demand mix in 2022. In 2026, demand is more diversified, with China passenger EV now only contributing to 24% of total mix and ESS overall is expected to make up >40% of demand (up from <20% in 2022). The importance of EU/EV exports and China commercial EV also increased. This diversification is positive for earnings resilience because the sector is no longer dependent on a single China PV EV adoption curve. However, it also means the investment narrative is less simple and less powerful than the last cycle's “EV penetration explosion” story. The current cycle is more about multiple demand engines – EV, commercial vehicles, China ESS, and overseas ESS – rather than one dominant driver.

# Policy changes: multiple policy to watch out for

Policy support has also changed in character. In the last cycle, China EV subsidies were only phased out from January 2023. In the current cycle, there may be several policy changes: China EV trade-in subsidies were lowered from January 2026, purchase-tax subsidies were halved for passenger and commercial vehicles, battery export rebates are being reduced, and there is a potential battery consumption-tax increase under discussion. At the same time, nationwide ESS subsidies were clarified in early 2026, but China's ESS target is set for 2027, raising the risk of a potential decline in ESS installations in 2028, which could translate into battery-shipment pressure in 2027. This suggests that investors should watch not only near-term demand strength but also the durability of 2027-28 growth.

# Government attitude on capacity expansion: from encouragement to disciplined

On the supply side, the contrast is equally important. During 2021-22, local governments actively encouraged NEV and battery capacity expansion with subsidies and support. In the current cycle, central-government scrutiny has increased under broader “anti-involution” and fair-competition policies aimed at curbing irrational price competition, overcapacity, and preferential local support. Local governments also have less fiscal bandwidth to provide direct subsidies, although they may still support strategic players indirectly through equity investments, industrial funds, or government-backed consolidation vehicles. This creates a more disciplined supply environment, but it does not eliminate overcapacity risk. Current capacity expansion is more concentrated among tier-1 and tier-2 players, with fewer new entrants, improved capex efficiency, and shorter capacity lead times.

# Capital raising: more concentrated at battery makers, particularly CATL

Capital raising also shows a different pattern. In 2021-22, A/H placements, IPOs, and GDR issuance totaled around Rmb150bn from top industry players, with roughly half raised by battery makers and around 20% by upstream raw-material companies. In the current cycle, H-share IPOs and A/H-share placements have already raised more than Rmb105bn, but around 80% of the capital has come from battery makers, with very little from upstream raw-material suppliers. This reinforces the idea that bargaining power and investment focus have shifted toward battery cell makers, especially those with scale, utilization, technology, and cash-flow advantages. For example, CATL has raised Rmb77bn in this cycle, representing around 70% of total capital raised across the supply chain so far. This compares with Rmb45bn in the previous cycle, or roughly 30% of the total.

# ASP gains are milder, with prices still 40–80% below the prior peak

Pricing behavior is another major difference. The last cycle saw extreme inflation in upstream and midstream materials: lithium carbonate rose by more than 1,300%, LiPF6 by more than 670%, LFP cathode by more than 390%, and LFP cathode processing fees by more than 70%. In the current cycle, price increases are meaningful but much smaller: lithium carbonate is up more than 130% from the 2H25 bottom, LiPF6 is up 97%, LFP cathode is up more than 80%, but cathode processing fees are up only 16%; wet separator is up 28%, while graphite anode has seen no price upcycle. Importantly, the latest prices are still 40-80% below the last-cycle peak, which limits the case for simply extrapolating 2022 peak earnings into the current cycle.

# Profit distribution shifts from resources to downstream; CATL stands out as the only through-cycle winner

Profit distribution has shifted from upstream/resource-led earnings in the last cycle to battery-cell-led earnings in the current cycle. In the 2021-22 supercycle, the most dramatic profit pool expansion was concentrated in upstream raw materials, especially lithium, as shown by Ganfeng-A's peak quarterly net profit of Rmb6.1bn in 4Q22, far above most midstream material and battery makers. By contrast, in the current cycle, most supply-chain companies are still meaningfully below their last-cycle profit peaks by $20 - 80\%$ . Only select names have recovered to or surpassed prior peak profitability. More importantly, CATL stands out as the only major name that delivered stable and growing earnings through the cycle, highlighting that industry profit distribution has shifted toward leading battery cell makers with scale, utilization, bargaining power, and stronger cash-flow resilience.

# Market concentration ratio declined

Battery and materials industry concentration has generally declined versus the last cycle, suggesting that pricing power is more fragmented despite improving utilization. The most notably declined are in wet separator (CR3 and CR5 ratio reduced by 10ppt/15ppt), and to a lesser extent in EV/ESS batteries. Overall, although the current cycle has fewer new entrants and more disciplined capacity expansion, lower concentration in several segments means investors should be selective and focus on companies with real cost, technology, customer, and

[中间内容因长度限制已省略]

aterial only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
