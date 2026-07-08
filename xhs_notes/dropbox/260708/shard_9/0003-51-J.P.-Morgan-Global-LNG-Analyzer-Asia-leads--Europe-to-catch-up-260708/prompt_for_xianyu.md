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
Source: Bloomberg Finance L.P., JPM Commodities Research

# JPM

# Global LNG Analyzer

Asia leads, Europe to catch up

\- Global LNG imports held up better than expected in June, supported by a recovery in Asian demand. Global LNG imports averaged 1,507 Mcm/day in June, down only 27 Mcm/day (1.8%) YoY. After months of decline and broadly flat YoY trend in May, China's LNG imports rose 5 Mcm/day (2%) YoY in June. Demand recovery was broad-based across Asia (ex-China/JKM), as imports increased 32 Mcm/day, or 9%, YoY, led by India (+21 Mcm/day, +22% YoY) and Thailand (+12 Mcm/day, +38% YoY), likely driven by the upcoming El Niño and increased cooling needs. JKM demand, meanwhile, has remained broadly stable at around 340–350 Mcm/day over the past three months, suggesting that domestic energy systems have partly adjusted through greater coal use, particularly in the power sector. Egypt also retained strong import momentum, with LNG imports reaching a new high of 60 Mcm/day (+10 Mcm/day MoM, +37 Mcm/day YoY).

\- With Asia absorbing more spot LNG, European imports lag significantly. European LNG imports declined by 80 Mcm/day (-20%) YoY in June. As we have been highlighting through our supply and shipping trackers, this reflects the pull from higher JKM/TTF premiums, which peaked near \$4/MMBtu at the onset of the conflict and remained elevated around \$2/MMBtu before the ceasefire announcement, and still trades at around \$1.3/MMBtu since the ceasefire. Ongoing robust premiums have redirected marginal US spot cargoes towards Asia rather than Europe, as the European share in US spot LNG imports dropped to nearly 50% in June, compared to 65% in June-2025.

\- Our spot LNG model underscores the same rebalancing pattern. Overall, estimated Asian spot LNG imports reached a new high of 290 Mcm/day in June, at the expense of European destinations, where spot volumes fell to 192 Mcm/day. This compares with 215 Mcm/day in June 2025, when NWE storage stood at 43%, versus 30% in 2026 (both as of June 1). Despite the post-ceasefire decline in spot prices, the core market fundamentals remain broadly unchanged as the JKM premium is proving resilient and continuing to pull spot cargoes toward Asia, while Europe’s storage trajectory continues to lag.

\- The recovery in demand was made possible by stronger-than-expected global LNG supply. The upside was led by the US, and particularly Sabine Pass, where feedgas and loading profiles showed little evidence of the usual June seasonal maintenance. We estimate Sabine Pass exports were 31 Mcm/day higher in June, essentially skipping the seasonal maintenance, while total US LNG exports averaged 505 Mcm/day (+31% YoY). As a result, global LNG exports declined by only 15 Mcm/day YoY in June, a much smaller contraction than the roughly 100 Mcm/day decline seen in April–May and the 150 Mcm/day decline in March.

\- Robust June supply also shifts the overall disrupted balance. At the onset of the conflict, we estimated that alternative supply could offset up to half of the lost Qatar/UAE LNG volumes, an estimate which largely held true through the first three months of the conflict (Mar-May). However, incorporating the much more modest decline in global LNG supply in June, the March to June average offset is now closer to two thirds. More specifically, against a 300 Mcm/day decline in Qatar/UAE supply, alternative sources offset 200 Mcm/day, led by the US (+87 Mcm/day) and Canada/ Mexico (+45 Mcm/day).

## Global Commodities Research

Otar Dgebuadze, CFA
(44-20) 3493-8246
otar.dgebuadze@JPM.com
JPM Securities plc

Aradhaya Makkar
aradhaya.makkar@jpmchase.com
JPM India Private Limited

Figure 1: USGC LNG exports by destination
Mcm/day, 14d ma  
![](images/50d01e4573da1aa030e37a147cc5bd6c861bb1ae429df7b7622f70989a7cb12a.jpg)

Based on loading dates, in transit volumes based on current location of the vessels.

## Contents

<table><tr><td>3Q balance remains structurally tight</td><td>3</td></tr><tr><td>Price Forecasts</td><td>10</td></tr><tr><td>NWE + UK S&amp;D Balance</td><td>10</td></tr><tr><td>LNG supply and shipping tracker</td><td>12</td></tr><tr><td>Global LNG balances</td><td>15</td></tr><tr><td>LNG trade matrix</td><td>18</td></tr><tr><td>Export/import capacity utilization rates</td><td>20</td></tr><tr><td>Import trends by country – Asia</td><td>35</td></tr><tr><td>Import trends by country – Europe</td><td>44</td></tr><tr><td>Import trends by country – Other</td><td>54</td></tr><tr><td>Export trends by country</td><td>58</td></tr><tr><td>Appendix 1 – LNG export projects (2025-35)</td><td>76</td></tr><tr><td>Appendix 2 – Export/import regions</td><td>77</td></tr></table>

\- However, we still expect LNG supply growth to moderate from here. Much of the forecasted 2026 supply growth (ex. Qatar/UAE) have already been delivered by the projects that started up in 2025, meaning their YoY contribution naturally fades as we move through the second half. Plaquemines is the clearest example: it remains the largest single contributor to 2026 growth, but 75% of its expected annual increase has already materialized YTD. Similar base effects will emerge for LNG Canada and Arctic LNG 2 as they approach their 2025 start-up anniversaries, while Golden Pass continues to miss expectations.

\- Our view on the Qatar ramp-up pace is unchanged. Assuming no re-closure or further incidents around the Strait of Hormuz, we model Qatari LNG utilization to reach 83% (the new normal, given the two damaged trains) in August and current events in the region potentially indicate further delay risks. Based on loading data, we estimate Qatar utilization averaged close to 16% in June. However, given limited traffic through Hormuz toward month-end, export-based utilization was closer to 10%. We model an average utilization rate of 50% in July, 62% in August, and 83% from September onward. Under these assumptions, Qatar's 2026 annual utilization would average near 58%, equivalent to 50 Bcm decline in annual exports versus 2025.

\- Paced Qatari restarts, slowing ex-Middle East supply growth, low Golden Pass utilization and resilient Asian demand leave Europe in a difficult position ahead of winter. Supply risks to Europe are further complicated by potential upside to Asian LNG demand from El Niño related cooling needs. At the same time, on-the-ground fundamentals on the continent show record low storage levels with a trajectory that deteriorates day after day compared to last year's path (which was the lowest since 2022). Additionally, the hottest summer on record (since at least 1973) also raises power system risks and increases the call on gas-fired generation, not only to meet rising cooling demand but also to offset weaker output from heat-sensitive alternative sources such as wind, hydro, nuclear and potentially even coal/lignite.

\- Taken together, these factors point to either structurally tight 3Q balances... In our view, the market will require higher prices and TTF/JKM spreads for Europe to outbid Asia for spot LNG cargoes, incentivize the maximum feasible coal use in the power sector and ultimately correct the storage trajectory. We think the market is already moving in that direction. Like other fossil fuels, spot natural gas prices fell sharply after the ceasefire (gas -20%, oil -13%, coal -11% Jun 10-19). However, unlike other fossil fuels, gas prices have since recovered by 12%, while oil and coal have continued to weaken (oil -10%, coal -2%, Jun 19 to date).

\- ...or significant risks into 4Q and winter. Last winter, Europe relied on winter LNG availability rather than building storage ahead of the heating season, contributing to a nearly 50% price spike in January during a short-lived transatlantic cold spell. This winter, with storage potentially at the lowest level on record, prices already elevated, Hormuz risks higher, normal weather risks still present and El Niño uncertainty on top, price moves could be much bigger. In that context, betting on El Niño to deliver a mild winter on the continent may prove too optimistic and could come at a high cost.

## 3Q balance remains structurally tight

After the initial shock, when Asia lost almost 30% of its LNG supply and the adjustment had to come largely through demand, the region is now absorbing more spot cargoes despite still elevated spot prices. Somewhat contrary to expectations, the largest demand decline has been in Japan and South Korea, where Apr to Jun imports averaged around 40 Mcm/day lower YoY, as domestic energy systems, particularly power generation, adjusted toward alternative fuels such as coal. In China, LNG demand weakened again in 1Q26 after signs of recovery in late 4Q last year, but appears to have troughed in March. Since then, demand has increased by almost 100 Mcm/day into June and recorded its first YoY increase (Figure 2). Demand is also picking up across the rest of Asia (ex. China/JKM). Beyond established buyers such as India and Thailand, imports have also strengthened in Indonesia and Vietnam, which we largely attribute to hotter weather and rising El Niño related cooling risks. It is difficult to disentangle how much of the imported LNG has already been consumed and how much is being held back for rainy (or very hot days) in July and August, but we think Asian summer demand remains skewed to the upside (Figure 3).

Figure 2: China LNG imports

![](images/9aa76a1a869232df306c9d077d9389a8262c0c78f569010b20d4e33596ebd7b6.jpg)  
Source: Bloomberg Finance L.P., JPM Commodities Research

Figure 3: Other Asia LNG imports  
![](images/06acb0ebfa7c5e5a25b15ca169e6f4328ebd72af74e1c42a79fc5006e2376e3a.jpg)  
Other Asia : Asia ex-China, Japan, S. Korea  
Source: Bloomberg Finance L.P., JPM Commodities Research

The strength in Asian imports is a direct consequence of persistent JKM premiums over TTF. The spread peaked near \$4/MMBtu at the onset of the conflict and averaged around \$2/MMBtu in 2Q. Despite the announced ceasefire and the decline in flat prices, the premium has not dissipated materially and continues to trade around \$1.1-1.3/MMBtu. Based on our estimates of shipping and other costs for the next couple of months, Asia and Europe imply broadly similar netbacks, with a more visible European premium emerging only from October (Figure 4).

Figure 4: JKM/TTF differentials history

![](images/420019cb45bb56c171bac560ba476163d9bc451ec0403f4a0a712b2855e277e7.jpg)  
Netbacks based on USGC origin cargoes, assuming current West of Suez shipping spot rates and estimated other costs (insurance, port fees, etc.). Latest market data as of COB 6 Jul 2026
Source: Bloomberg Finance L.P., JPM Commodities Research

Figure 5: JKM and TTF Netbacks  
![](images/e3bb683b1c621683867989302c5831c699d67a43629cb7557b28398915ab137e.jpg)  
Netbacks based on USGC origin cargoes, assuming current West of Suez shipping spot rates and estimated other costs (insurance, port fees, etc.). Latest market data as of COB 6 Jul 2026
Source: Bloomberg Finance L.P., JPM Commodities Research

As a result, Asian spot imports reached a new historical high in June at nearly 300 Mcm/day, while European spot imports fell below 200 Mcm/day (Figure 6 and Figure 7). We still expect Europe to correct this imbalance by eventually outbidding Asia and re-emerging as the preferred destination for marginal spot cargoes. So far, however, the gap between actual and required European imports continues to widen. In our view, Europe can still correct the storage path, but this requires higher TTF prices and a narrower JKM premium.

Figure 6: Asia spot LNG imports  
![](images/8fc9141cc391229dda24261ca54a14038b242caade19a7ed8dd162ef61525c5e.jpg)  
Total Asia. \*JPMe  
Source: Bloomberg Finance L.P., JPM Commodities Research

Figure 7: Europe spot LNG imports  
![](images/5f90298ca08ff44b9ab1ce3ab4a9134349895e83c469eb8cfb690ad3c53762d6.jpg)  
Total Europe (ex. Turkey). \*JPMe  
Source: Bloomberg Finance L.P., JPM Commodities Research

The robust Asian imports were largely enabled by stronger-than-forecast US supply (Figure 8). US LNG exports averaged 505 Mcm/day in June (+31% YoY). The upside was largely driven by Sabine Pass (+35 Mcm/day YoY), as the facility effectively skipped its usual seasonal maintenance. In our view, and consistent with historical patterns, this maintenance is unlikely to be avoided and more likely to be deferred, implying that supply growth should moderate in July and August (Figure 9).

Outside Sabine Pass, output was also stronger at Corpus Christi (+27 Mcm/day YoY), and Plaquemines (+39 Mcm/day YoY), as both facilities continued to ramp up and came in slightly above our expectations. Cameron provided additional support, up around 10 Mcm/day YoY. This helped limit the YoY decline in global LNG exports to only around 15 Mcm/day in June, compared with roughly 100 Mcm/day in April and May and around 150 Mcm/day in March.

Figure 8: US LNG exports

![](images/5a9b103e0c8f5c7a0ebe2cb51ae407540fd610cd92eaea266a3493909cba50ee.jpg)

![](images/f52b9302f7c50acca66da27db9f942c3ab98a3bbcc4f5e2705a9fe5e62f63cd3.jpg)  
Source: Bloomberg Finance L.P., JPM Commodities Research  
Source: Bloomberg Finance L.P., JPM Commodities Research

The significant recovery in global LNG supply (ex. Qatar/UAE) materially reshaped the post-conflict balance. Our expectation at the onset of the conflict was that rising alternative supply could offset around half of lost Qatar/UAE volumes, which largely materialized through May. However, the stronger June supply response brings the March to June average offset closer to two-thirds. Against a 300 Mcm/day decline in Qatar/UAE supply, alternative sources offset close to 200 Mcm/day, led by the US and Canada/Mexico (Figure 10).

On the demand side, the primary balancing factor remains Europe. European LNG imports declined by 80 Mcm/day YoY in June, an acceleration from the 51 Mcm/day YoY decline in May, as the continent emerges almost like residual balancing market (Figure 11).

Figure 10: Global LNG market rebalancing
Mcm/day YoY, Mar-Jun 2026

Bcm  
![](images/962aac9b29a1768dfcbffdff8262fecf2f34927ca1ed9597b643aedb197ace77.jpg)  
balance = higher supply / lower demand

Red bars refer to tighter balance = lower supply / higher demand; Green bars refer to looser  
Figure 11: Global LNG supply/demand changes  
![](images/1ee07772c311bd01a8076a71860bd2cbf886e683b3ecb2a630f48e537c62c6dc.jpg)  
Source: Bloomberg Finance L.P., JPM Commodities Research  
Source: Bloomberg Finance L.P., JPM Commodities Research

We still expect supply growth to moderate through the balance of the summer and into the injection season. US maintenance should eventually arrive, while the YoY contribution from new projects naturally fades as facilities that started in 2025 approach their first anniversary. Golden Pass also continues to disappoint, with the facility running at around 30% of capacity compared to our prior expectation of roughly 80% in the summer and above 90% in the winter (Figure 12).

Figure 12: LNG supply decomposition (2025-27)

<table><tr><td>Country</td><td>Project</td><td>JPMe start date</td><td>Capacity (Bcm/Year)</td><td>2025 Output</td><td>2026 Output</td><td>2027 Output</td><td>2025 y/y</td><td>2026 y/y</td><td>2027 y/y</td></tr><tr><td colspan="10">Projects started in 2025</td></tr><tr><td>US</td><td>Plaquemines LNG Phase 1 + 2</td><td>Jan-25</td><td>38.4</td><td>22.8</td><td>37.7</td><td>37.7</td><td>22.8</td><td>14.8</td><td>-</td></tr><tr><td>Canada</td><td>LNG Canada</td><td>Jul-25</td><td>19.2</td><td>2.7</td><td>15.3</td><td>16.2</td><td>2.7</td><td>12.5</td><td>0.9</td></tr><tr><td>US</td><td>Corpus Christi LNG Stage 3</td><td>Jan-25</td><td>16.4</td><td>2.9</td><td>11.0</td><td>15.6</td><td>2.9</td><td>8.1</td><td>4.6</td></tr><tr><td>Russia</td><td>Arctic LNG 2 - 

[中间内容因长度限制已省略]

mance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 08 Jul 2026 12:34 AM BST

Disseminated 08 Jul 2026 12:34 AM BST
"""
