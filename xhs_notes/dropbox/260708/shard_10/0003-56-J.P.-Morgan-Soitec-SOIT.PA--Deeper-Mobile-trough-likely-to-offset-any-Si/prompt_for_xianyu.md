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
## Soitec

## Deeper Mobile trough likely to offset any SiPho upside: Stay Neutral

Soitec is \~40% off its year-to-date peak, with some investors questioning whether this represents an attractive entry point for a medium-term position. We think there is upside to consensus expectations on the SiPho opportunity, but offsetting this we see a continued contraction and a much shallower recovery in the Mobile business than is currently anticipated by consensus. AI and the associated infrastructure build-out has been a mixed blessing for Soitec, with the SiPho business booming but the Mobile business likely to suffer as high DRAM prices (due to AI demand) leads to demand destruction. We remain Neutral, on the view that the downside risk to the core Mobile Communications business is not yet fully reflected in the shares, but equally, we do not think being underweight is sensible while we see upgrade risk to the Edge & Cloud AI division.

\- SiPho remains the significant driver: We expect SiPho will be the material growth engine for Soitec (helped by rising adoption in transceivers and CPO ramping from \~2028). We model rapid growth (50% revenue CAGR FY25-30e; €535m in FY30) supported by pre-existing capacity with an assumption that Soitec's market share normalises (\~80% in FY30) as competition ramps (notably Global Wafers) plus some downward pressure on pricing as long-term supply agreements take effect. We recognise a high degree of execution risk in SiPho, both for Soitec and also at its customers (in particular ramping CPO).

\- Mobile decline to continue in FY27 with shallower recovery: Mobile remains the largest division (\~52% of FY26 revenue) but with a step-down in handset volumes expected in 2026-2027 (we estimate -16% and -3%, respectively). As DRAM pricing flows through the supply chain, we see a further contraction in Mobile revenues. Management's more disciplined approach to RF-SOI pricing from FY27 onwards could support margins, but also increase market-share-loss risk and prolong the destocking cycle (we now assume destocking into FY28). Our revenue forecast for the Mobile Communications division is 14-17% below consensus in FY27-29.

\- Auto & Industrial still working through inventory: Inventories across Auto & Industrial customers remain elevated, which will represent a headwind to Soitec volume and possibly pricing through FY27 (although pricing discipline appears to be a company priority). There are some recent indications of restocking in the Auto supply chain, but we expect IDMs to see most of the benefit (rather than wafer makers). On top of this, SmartSiC is likely to contract further based on competitive pressures (which prompted the impairment in FY26). We expect revenue to be broadly flat in FY27, with a gradual improvement in FY28 largely in line with consensus.

\- Gross margin trajectory shallower than consensus expects: We see a more gradual margin rebuild than the latest consensus, with group-level gross margin only reaching 30.2% in FY29 (vs. 32.2% consensus) despite SiPho mix benefits and improving loading. Headwinds include a higher fixed-cost/depreciation base, pricing pressure (especially RF-SOI) and currency. In the near term, elevated inventory write-downs in FY26 should support FY27 gross margins.

Sources for: Style Exposure – JPM Global Markets Strategy; all other tables are company data and JPM estimates.

## Neutral

SOIT.PA, SOI FP

60H.PA, 60H
Price (07 Jul 26):€98.16

▼Price Target (Dec-27):€92.00
Prior (Dec-27):€130.00

European Tech Hardware & Payments

Craig A McDowell AC
(44-20) 7742-4576
craig.mcdowell@JPM.com

Sandeep Deshpande
(44-20) 7134-5276
sandeep.s.deshpande@JPM.com

Anthony Girard
(44-20) 3493-6469
anthony.girard@JPM.com
JPM Securities plc

Specialist Sales contact details:

## Scott Silver - Specialist Sales - European TMT

(44-20) 7134-0412
scott.silver@JPM.com

Key Changes (FYE Mar)

<table><tr><td></td><td>Prev</td><td>Cur</td><td> $\Delta$ </td></tr><tr><td>Revenue - 27E (€ mn)</td><td>631</td><td>603</td><td>-4.4%</td></tr><tr><td>Revenue - 28E (€ mn)</td><td>824</td><td>748</td><td>-9.2%</td></tr><tr><td>Adj. EPS - 27E (€)</td><td>(0.48)</td><td>(0.59)</td><td>-21.8%</td></tr><tr><td>Adj. EPS - 28E (€)</td><td>1.79</td><td>0.91</td><td>-49.3%</td></tr><tr><td>Adj. EBIT - 27E (€ mn)</td><td>2</td><td colspan="2">(3)-246.5%</td></tr><tr><td>Adj. EBIT - 28E (€ mn)</td><td>96</td><td>58</td><td>-40.0%</td></tr></table>

## Style Exposure

<table><tr><td rowspan="2">Quant Factors</td><td rowspan="2">Current %Rank</td><td colspan="4">Hist %Rank (1=Top)</td></tr><tr><td>6M</td><td>1Y</td><td>3Y</td><td>5Y</td></tr><tr><td>Value</td><td>91</td><td>23</td><td>28</td><td>47</td><td>53</td></tr><tr><td>Growth</td><td>13</td><td>54</td><td>58</td><td>12</td><td></td></tr><tr><td>Momentum</td><td>96</td><td>91</td><td>86</td><td>36</td><td>56</td></tr><tr><td>Quality</td><td>70</td><td>88</td><td>78</td><td>65</td><td>37</td></tr><tr><td>Low Vol</td><td>1</td><td>94</td><td>93</td><td>61</td><td>34</td></tr><tr><td>ESGQ</td><td>51</td><td>47</td><td>35</td><td>83</td><td>97</td></tr></table>

See page 14 for analyst certification and important disclosures, including non-US analyst disclosures.

Price Performance  
![](images/2c68f21429f7ff6db89c17a58014b4932136404157e73056bee6c36a1bc02c19.jpg)

— SOIT.PA Price (€) — SBF120 (rebased)

<table><tr><td></td><td>YTD</td><td>1m</td><td>3m</td><td>12m</td></tr><tr><td>Abs</td><td>323.3%</td><td>-33.1%</td><td>100.3%</td><td>109.9%</td></tr><tr><td>Rel</td><td>319.8%</td><td>-35.4%</td><td>93.9%</td><td>101.2%</td></tr></table>

Company Data

<table><tr><td>Shares O/S (mn)</td><td>36</td></tr><tr><td>52-week range (€)</td><td>200.50-22.62</td></tr><tr><td>Market cap ($ mn)</td><td>4,004.53</td></tr><tr><td>Exchange rate</td><td>0.87</td></tr><tr><td>Free float (%)</td><td>69.5%</td></tr><tr><td>3M ADV (mn)</td><td>0.58</td></tr><tr><td>3M ADV ($ mn)</td><td>84.4</td></tr><tr><td>Volatility (90 Day)</td><td>128</td></tr><tr><td>Index</td><td>SBF 120 INDEX (CAC 120)</td></tr><tr><td>BBG ANR (Buy | Hold | Sell)</td><td>6|10|3</td></tr></table>

Key Metrics (FYE Mar)

<table><tr><td>€ in millions</td><td>FY26A</td><td>FY27E</td><td>FY28E</td></tr><tr><td colspan="4">Financial Estimates</td></tr><tr><td>Revenue</td><td>592</td><td>603</td><td>748</td></tr><tr><td>Adj. EBIT</td><td>(131)</td><td>(3)</td><td>58</td></tr><tr><td>Adj. EBITDA</td><td>143</td><td>131</td><td>189</td></tr><tr><td>Adj. net income</td><td>(220)</td><td>(21)</td><td>33</td></tr><tr><td>Adj. EPS</td><td>(6.17)</td><td>(0.59)</td><td>0.91</td></tr><tr><td>BBG EPS</td><td>(1.94)</td><td>(0.14)</td><td>2.00</td></tr><tr><td>Cashflow from operations</td><td>205</td><td>176</td><td>160</td></tr><tr><td>FCFF</td><td>68</td><td>80</td><td>44</td></tr><tr><td colspan="4">Margins and Growth</td></tr><tr><td>Revenue Growth Y/Y (%)</td><td>(33.6%)</td><td>1.8%</td><td>24.1%</td></tr><tr><td>EBIT margin</td><td>(22.1%)</td><td>(0.4%)</td><td>7.7%</td></tr><tr><td>EBIT Growth Y/Y (%)</td><td>(210.1%)</td><td>(98.0%)</td><td>(2248.4%)</td></tr><tr><td>EBITDA margin</td><td>24.2%</td><td>21.7%</td><td>25.3%</td></tr><tr><td>EBITDA Growth Y/Y (%)</td><td>(52.0%)</td><td>(8.4%)</td><td>44.5%</td></tr><tr><td>Net margin</td><td>(37.2%)</td><td>(3.6%)</td><td>4.4%</td></tr><tr><td>Adj. EPS growth</td><td>(340.4%)</td><td>(90.5%)</td><td>(254.9%)</td></tr><tr><td colspan="4">Ratios</td></tr><tr><td>Adj. tax rate</td><td>(37.9%)</td><td>(9.0%)</td><td>16.0%</td></tr><tr><td>Interest cover</td><td>4.8</td><td>7.7</td><td>10.5</td></tr><tr><td>Net debt/Equity</td><td>0.0</td><td>NM</td><td>NM</td></tr><tr><td>Net debt/EBITDA</td><td>0.4</td><td>NM</td><td>NM</td></tr><tr><td>ROE</td><td>(15.1%)</td><td>(1.6%)</td><td>2.5%</td></tr><tr><td colspan="4">Valuation</td></tr><tr><td>FCFF yield</td><td>1.9%</td><td>2.2%</td><td>1.2%</td></tr><tr><td>Dividend yield</td><td>0.0%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>EV/Revenue</td><td>7.2</td><td>7.0</td><td>5.6</td></tr><tr><td>EV/EBITDA</td><td>29.9</td><td>32.2</td><td>22.1</td></tr><tr><td>Adj. P/E</td><td>NM</td><td>NM</td><td>108.3</td></tr></table>

## Summary Investment Thesis and Valuation

## Investment Thesis

Soitec is going through a period of extreme inventory correction at customers, which is having a significant negative impact on revenue. At the same time, concerns over the competition for Soitec's largest product (RF-SOI) are heightened. Other products are beginning to compensate, notably POI and Photonics-SOI, which we expect to become the dominant revenue stream in the next 2-3 years. Market enthusiasm for Silicon Photonics has resulted in a significant run-up in the shares; however, we now see the valuation as full to fair, reflecting the future opportunity.

## Valuation

Our Dec-27 price target of €92 is based on 11.0x FY29e EBITDA (y/e March 2029) (previously €130 valued on 15.0x FY29). The chosen multiple is at the high end of the wafer maker range, justified by higher growth; the multiple is a \~10% premium to the last five-year average, justified by improving growth, returns and cash flow. We value on FY29 earnings, which we expect to be more normalised following a period of depressed financial performance (in FY26 and expected/guided in FY27).

Performance Drivers  
![](images/becec39b3ec02678520036fd0bb0f1987e87cb72b7cd0cd05ceb42d5696b4530.jpg)

<table><tr><td>Factors</td><td>6M Corr</td><td>1Y Corr</td></tr><tr><td>Market: MSCI Europe ex UK</td><td>0.37</td><td>0.38</td></tr><tr><td>Sect: Technology</td><td>0.46</td><td>0.45</td></tr><tr><td>Ind: Semicond &amp; S Equip</td><td>0.27</td><td>0.30</td></tr><tr><td>Macro:</td><td></td><td></td></tr><tr><td>Euro</td><td>-0.23</td><td>-0.23</td></tr><tr><td>Citi Eco Surprise Eurozone</td><td>-0.17</td><td>-0.19</td></tr><tr><td>Eurozone Exports</td><td>0.10</td><td>0.11</td></tr><tr><td>Quant Styles:</td><td></td><td></td></tr><tr><td>Quality</td><td>0.20</td><td>0.25</td></tr><tr><td>DivYld</td><td>-0.13</td><td>-0.21</td></tr><tr><td>Value</td><td>-0.15</td><td>-0.18</td></tr></table>

\- What else could drive upside for the shares from here? The current share price appears to assume SiPho delivering €500m+ revenue by FY30, other divisions returning to growth in FY28, and an improving margin/FCF profile. Beyond any changes to forecasts, we do not think the portfolio review (possibly at H1'27 results) will significantly change the market's perception, while investors will be reluctant to fully underwrite ‘incubator projects’ at an early stage.

\- Q1'27 and Q2'27 reflecting our medium term view: For Q1 (June-end quarter), we are in line with company guidance (+15% y/y organic) which is in line with consensus. Similarly, for Q2 we are broadly in line with consensus. However, we are below on Mobile Communications, but ahead on Edge & Cloud AI (see Table 4).

Conclusion for the shares: Soitec is running at two speeds with SiPho revenue surging, while Mobile Communications (as well as Automotive & Industrial) is seeing slow growth in the forecast period. We think that revenue forecast upgrades could come through on SiPho/Edge & Cloud AI, but there is downside risk to other division estimates; net, at the group level, our forecasts are 4%/6%/3% below the latest consensus. We remain Neutral, on the view that the downside risk to the core Mobile Communications business is not yet fully reflected in the shares, but equally, we do not think being underweight is sensible while we see upgrade risk to the Edge & Cloud AI division.

\- Forecast and PT update: We revise our revenue forecasts with group level changes of -4%/-9%/-3% in FY27/28/29, respectively, with revisions to Mobile as well as Auto & Industrial. The lower revenue assumptions flow through the P&L with limited changes to our opex and D&A assumptions (see Table 2 for summary of forecast changes). Our new PT is €92 (previously €130), which reflects our lowered estimates as well as a lowered multiple (11.0x from 15.0x, reflecting multiple contraction across the peer group).

## SiPho remains the significant driver

On volume, we expect Silicon Photonics (SiPho)-based modules to represent a growing share of optical transceivers in the forecast period, given energy and data-efficiency benefits, while leveraging mature silicon foundries for high-volume production (e.g. STMicroelectronics moving into the SiPho foundry). Industry consultancy Lightcounting estimates that in 2026, SiPho will represent \~52% of the optical transceiver market (up from \~33% in 2024). CPO will be the next leg of growth later in the decade as it ramps from 2028 onwards – we expect this will be completely based on SiPho (with much larger SiPho content). The result is very significant growth in the SiPho wafer market through to 2030 (JPMe \~66% CAGR 2025-2030).

On pricing, while pricing in FY27 is likely to remain positive, we think LTSAs will lead to small (LSD%) blended ASP erosion for Soitec's SiPho business. This will be based on both the initial contract price but also an assumption of pricing descalators (i.e. higher volumes at lower prices). From our discussions with the company, we understand that the aim of the long-term supply agreements (LTSAs) is to gain greater confidence on future volume and pricing, as well as to improve the working capital profile - not necessarily to optimise price. A parallel may be drawn to the memory makers which have managed to secure material LTSA's with customers stretching for 3-5 years and in some cases structured as take or pay - we think this will be the ambition for Soitec.

On market share, we forecast an erosion of Soitec's market share to \~80% in FY30 (from an effective \~100% currently). Soitec is in the process of qualifying with a number of customers for CPO, which should support market share in the face of competition. In terms of competitors, we highlight Global Wafers (covered by Jimmy Huang) as the main competitive threat. As a reminder, Global Wafers has developed silicon on insulator technology (independent of Soitec patents) and developed a facility in Missouri dedicated to SOI at 300mm. The latest commentary from Global Wafers is that the Missouri facility is already covered by long-term agreements, although the split between RF-SOI and Photonics is uncertain (“Capacity is nearly full with output largely sold through and selected RF-SOI and photonics already ramping.”, 5 May 2026 Q1 earnings call). Global Wafers management has indicated that it is exploring the expansion of its SOI production capacity, although no firm commitment has been made. Shin Etsu is also a competitor in SiPho, however, it is reliant on a SmartCut licence and as such may be less cost competitive.

We recognise a high degree of execution risk to SiPho estimates, both internally for Soitec in terms of converting capacity, securing contracts, etc, but also with customers as it launches CPO products (which will be a significant driver of SiPho content).

Taken together, we see faster growth for Soitec's Edge & Cloud AI business, with our revenue forecasts for this division $+6\% / +10\% / +14\%$ below the latest Vara consensus (Table 2).

Figure 1: Optical market, units by form factor  
![](images/e139a72b6dc737db455bb95a2a2e4879f9bd7b74d1fe3651c5431366dc5487de.jpg)  
Source: JPM estimates.

Figure 2: SiPho wafer demand by form factor
Millions of wafers (calendarised)  
![](images/478b20c704ebbc6f7e75e8837b667ef19ec52475135caed7178251c6863e4565.jpg)  
Source: JPM estimates.

Figure 3: SiPho wafer market and Soitec market share
Millions of wafers (March year-end)  
![](images/b09bbe806b57c295ba16002c4f742bff7dacb90b3ea8139423a6543171df1c01.jpg)  
Source: JPM estimates.

Figure 4: Soitec, SiPho revenue  
![](images/81f6e82d9644f11

[中间内容因长度限制已省略]

 market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and

should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
