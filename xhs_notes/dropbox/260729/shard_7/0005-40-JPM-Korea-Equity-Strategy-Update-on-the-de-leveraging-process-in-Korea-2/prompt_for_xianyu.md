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
# JPM

## Korea Equity Strategy

Update on the de-leveraging process in Korea (2)

The Korea market has undergone an intense period of de-leveraging since mid-June. The KOSPI index is now down almost -40% from the peak on 22 June in a highly volatile move. What was triggered by routine fundamental concerns and rotational flow was amplified by leveraged ETFs, and in recent days increasingly has the hallmarks of hedge fund positioning unwind. Following our update last week (where we estimated that leveraged ETF unwind was 75% through and equity H/F de-leveraging >50% through), we now believe that leveraged ETF unwind is complete and hedge funds are done with \~90% of de-leveraging (both to acceptable levels). While it is likely that the price damage we have seen this week has residual spillovers into further de-leveraging over the coming days, and that many investors continue to exercise caution into the FOMC this week (high risk of a rate hike) and hyperscaler earnings (high expectations), the positioning setup in Korea now appears attractive on balance – and complements the cheap valuations and earnings momentum.

\- De-leveraging update: (1) Leveraged ETFs AUM has normalized: Leveraged ETFs with Korea underlyings grew to \$50bn in AUM by late June. Relative to its market size, this was 4x larger than the US and led to very pronounced volatility (and forced de-leveraging on down-days – which then caused positioning unwinds from other investors). With the reversal of the market, this cohort is now down to \$17bn. In addition, the previously rapid inflows into these products have stalled in recent days (not much dip buying). As a result, the VKOSPI to VIX ratio has started to decline and will likely fall further. (2) HF leverage has almost normalized: Swap capacity constraints kept a lid on HF leverage buildup in Korea. Still, L/S ratios in the JPM Prime book rose up to 5.7x. The process of normalization from there is now well advanced. This ratio dropped to 3.2x by 27 Jul, and given the unwind in the Price Momentum factor over 28 and 29 Jul, HF leverage has likely declined further, and not very far from the top end of 2025's range. (3) Retail leverage through margins less of a risk: Margin balances were never particularly high or witnessing rapid growth. Balances have moderated somewhat to \~\$20bn now. And, unlike leveraged ETFs that undergo a process of forced de-leveraging on any spot price declines, margin lending comes with buffers and discretion. Korean retail investors still have ample equity gains, cash balances, higher incomes and overseas assets to tap into to absorb any margin calls should they want to keep the position. (4) Record foreign outflows are slowing: LO selling pressure has substantially eased as Korea (and particularly the memory names) has underperformed, meaning that the two heavyweights are now only 6.5% and 4.5% weights in MSCI EM (vs 9.5% and 8.3% in late June).

\- Diversification trades remain in play: We continue to like: (1) “wealth effect” exposures (department stores, cosmetics, travel, brokers, construction) have a compelling tailwind; (2) Bio-pharma is a substantial laggard that potentially benefits from globally improving sentiment around the healthcare sector; (3) Pref share discounts are near record wides – with the resultant elevated yields offering good carry; (4) Banks look particularly attractive with a triple tailwind from improving asset quality with income growth, BOK rate hiking cycle a tailwind for NIMs, and heightened market volumes contributing to brokerage revenues.

## Equity Macro Research

Mixo Das AC
(852) 2800-0511
mixo.das@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Stanley Yang  
(82-2) 758-5712  
stanley.yang@JPM.com  
JPM Securities (Far East) Limited, Seoul Branch

Rajiv Batra
(65) 6882-8151
rajiv.j.batra@JPM.com
JPM Securities Singapore Private Limited

Joy Wang
(852) 2800-2322
joy.y.wang@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

See page 8 for analyst certification and important disclosures, including non-US analyst disclosures.

Figure 1: KOSPI index has now declined \~40% from the peak of 22 Jun  
![](images/0caab12a23e8f1c3b85f1423d995c5ae946dee02ea77e8a6cc9fc734506a6a5f.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 2: This week's move has brought index RSI to oversold levels  
![](images/7387910d940ef34e3c93b8842c8c8f0ddb820f74ea1b8895bd3f202e38b9c9d8.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 3: KOSPI fwd P/E at 5x is cheap – even after adjusting for cyclicality  
![](images/d3e7fc891e77082230497bc01276e7b3412c914ce7bc1819db892ddb0748f1ec.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 4: 5x estimated FCF is, similarly, “crisis-level” valuation  
![](images/e169de189b6b14b09a02fe249f8b2d6afd2dd694cc1c00b4a820cf6fccf92fbe.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 5: Our simplistic modeling of memory price longevity suggests current market pricing implies memory prices start normalizing to pre-AI levels in early 2027; each extra year adds \~\$150bn  
Key memory maker's valuation based on how long prices sustain at 2026-average levels. Please ask for details.  
![](images/8554e14aae64bafc456e9fe37397ba878a5247ff8b8a4d66468b6f7eb8a2b0bc.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 6: Relative to this, spot memory prices on aggregate are still moving higher; contract prices up in 3Q too – albeit at slower pace q-q  
![](images/748a541da3008f74226b999851ff00e1900b08b35d52096e723d97f472b97c93.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 7: Korea market concentration has been another problem – which led to very narrow breadth until recently
% of stocks outperforming KOSPI on a rolling 6m basis  
![](images/c8ffa557edb9cbfd2427c4fefa2cbe65efaa945f31b4e567844577ee3cc865b4.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 8: Notably, in the correction in July, market breadth (advance-declines) has actually held up relatively well – indicating losses were also concentrated in few names  
![](images/d5cd73e678f82b0bed3d9d3d238e99c74366992013836c69d3d2946c33d9aadb.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 9: Indeed, KOSPI decline has matched with underperformance of memory names – but this appears to be stabilizing  
![](images/f4919c9c7256a72bcca4c317397860c8d9bf7f3c64d558be3c704a60a3c28599.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 10: Similarly, in the US, the unwind of concentration has been violent, but likely healthy  
![](images/b7fc1816b005d2c0da71dc98c7b39ba1aa5fb18623427836dd76d7d8ba4128d1.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 11: Relative performance of market segments in Korea – big catchup from laggards in Value and Defensive spaces relative to KOSPI  
![](images/56ac47a9c314968cdc4cb0246996f22935043752bb792c917f909c1e0463124e.jpg)

![](images/07dc5b41c6549d0e67e8454035751821097be42c6c844582bb68cc5805d21c1b.jpg)

![](images/0abf6070047a0d80d45d95ce19a0a9be6539158b3d82375de373bf9504f6469a.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

![](images/70c7b8297abd836b4436ccb2c85f66e17c1b5dbcb49da3e9d47943d55edd87c4.jpg)

X  
Figure 12: In terms of leveraged ETFs, their AUM has now declined to levels we believe are no longer problematic
AUM - USD mn  
![](images/d40f073e2bd7bf31cb8ba832fec30db8e786c2ab5b685d8d6dc39801ae592d03.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 13: Inflows into leveraged products has also stalled in recent days – with recent regulatory tightening potentially keeping inflows in check  
Cumulative inflows, USD mn  
![](images/1058e4d81c3a70b0b54cccb6902b909b268976e7520adae4eed60dcfdbece13a.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 14: As a result, KOSPI volatility has started to normalize and will likely continue to  
![](images/51fa6f475497860ce38c78625d41882f7f96e8860a3934d152e0c3ea1c3ff9e9.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 15: The open interest of single stock futures (implementation channel of the leveraged ETFs) continues to moderate as well  
![](images/80951ac50372b1f41af3b086a3e25b0a766d9176a854315e26de9f9978d9f694.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 16: L/S ratio for hedge funds in the JPM Prime book has declined from highs...  
Latest data as of 27 July  
![](images/3295d8e29abf9ee252cc14665ec93bb8452fd13f501381d1a8c58093aab73c3f.jpg)  
Source: JPM Positioning Intelligence.

Figure 17: ... and has likely further normalized looking at the sharp underperformance of the Price Momentum factor over 28 and 29 July Indicative performance of L/S quintiles  
![](images/534f50b5f7e2575614c11cb668d70a52d2c730ce95d1b84b8fc98c8d89f41de2.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 18: For retail investors, margin leverage is not too high and has not climbed very aggressively this year  
![](images/a3ec5ef7232a292408aff8d9d0d455f09ffcfc2f0f3d9e6a2482a43c007ced68.jpg)  
Source: Bloomberg Finance L.P., KSD, JPM Equity Macro Research.

Figure 19: As a share of market cap, margin balances have actually been declining this year  
![](images/b67433703457a99f1e94f84b6ef92e210e7828c39588b70de2156e4a4868e533.jpg)  
Source: Bloomberg Finance L.P., KSD, JPM Equity Macro Research.

Figure 20: For foreign investors overall, they have sold >\$110bn of Korean equities YTD, but most of this was due to mandate constraints for LOs on owning large-caps

Cumulative flow, \$mn, KRX data

![](images/ca562cefbee3b8321eab6cb2d0e2368d88b8687d4efe1aff9052b3bd100eb06f.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Figure 21: Indeed, 90% of the outflow is from the two memory names; the decline in EM index weights of these stocks has substantially slowed outflows  
Cumulative flow, \$mn  
![](images/e622ed361d608656dd29d3bd70bd096709565125ac04ff710ccaebd394a501f1.jpg)  
Source: Bloomberg Finance L.P., JPM Equity Macro Research.  
USD mn, KRX data only

Figure 22: Foreign flows by market segments and key market regimes YTD – a lot of sectors seeing buying even during the latest KOSPI correction since 22 Jun

<table><tr><td rowspan="2">USD mn</td><td colspan="4">Tech / AI exposure</td><td colspan="4">Value exposure</td><td colspan="6">Industrials and commodities</td><td colspan="5">Others</td></tr><tr><td>Samsung</td><td>Hynix</td><td>Grid/Power</td><td>Tech supply chain</td><td>Autos</td><td>Banks</td><td>Non Bank Fin</td><td>Holdco</td><td>Battery</td><td>Oils/Che micals</td><td>Metals</td><td>Shipping /building</td><td>Defense</td><td>E&amp;C</td><td>Bio-Pharma</td><td>Internet/ Media</td><td>Consumer exports</td><td>Telco</td><td>Services</td></tr><tr><td>1 Jan - 27 Feb</td><td>-12987</td><td>-6419</td><td>459</td><td>988</td><td>-3854</td><td>-87</td><td>-485</td><td>92</td><td>1291</td><td>780</td><td>52</td><td>1642</td><td>-16</td><td>1296</td><td>967</td><td>324</td><td>456</td><td>146</td><td>45</td></tr><tr><td>27 Feb - 31 Mar</td><td>-12138</td><td>-5412</td><td>-170</td><td>-482</td><td>-2587</td><td>-451</td><td>-418</td><td>-136</td><td>-181</td><td>-205</td><td>-286</td><td>62</td><td>-616</td><td>-13</td><td>269</td><td>-342</td><td>-111</td><td>48</td><td>-29</td></tr><tr><td>31 Mar - 22 Jun</td><td>-17913</td><td>-17105</td><td>-1947</td><td>-1611</td><td>-4180</td><td>-97</td><td>50</td><td>-2073</td><td>1027</td><td>963</td><td>-79</td><td>-1190</td><td>833</td><td>-220</td><td>10</td><td>-892</td><td>81</td><td>-255</td><td>-330</td></tr><tr><td>22 Jun - now</td><td>-10362</td><td>-15536</td><td>-307</td><td>1023</td><td>85</td><td>-354</td><td>116</td><td>-2472</td><td>-47</td><td>-25</td><td>56</td><td>-244</td><td>-69</td><td>175</td><td>86</td><td>15</td><td>91</td><td>-177</td><td>-28</td></tr></table>

Source: Bloomberg Finance L.P., JPM Equity Macro Research.

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe of the relevant duration of the region. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap Equity Research, each stock's expected total return is compared to the expected total retur

[中间内容因长度限制已省略]

mance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 29 Jul 2026 03:27 PM HKT

Disseminated 29 Jul 2026 03:27 PM HKT
"""
