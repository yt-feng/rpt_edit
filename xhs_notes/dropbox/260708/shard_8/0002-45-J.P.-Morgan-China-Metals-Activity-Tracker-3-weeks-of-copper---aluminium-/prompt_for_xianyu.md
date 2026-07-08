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
## 3 weeks of copper & aluminium inventory declines signal strengthening China metals consumption

We present our high-frequency inventory trends for base metals, steel and iron ore in China for the week ended 3 Jul'26. Our data plots China weekly metals inventory trends, a proxy for consumption. After six weeks of weak copper inventory movement, Copper has recorded three consecutive weeks of larger inventory drawdowns (-13kt last week). These significant reductions reduce China's total copper inventory to the multi-year low for this time of year at 163kt. We interpret this as a signal of improved China copper consumption, synchronous with the US continuing to pull metal to COMEX, ahead of the US Department of Commerce decision on whether to impose US copper import tariffs. China's copper purchase premium climbed back to >\$70/t in the last week, which is a signal of improving regional demand.

This de-stocking trend also continues in Aluminium & Zinc. In Aluminium, last week saw the largest de-stocking since Chinese New Year (-75kt) and China's aluminium inventories have dropped $>300\mathrm{kt}$ in the past 8 weeks. Zinc inventories saw a significant drawdown for the first time since CNY at -11kt.

JPM China Economists note improving stockpile signals, even as China FAI softens, potentially providing muted evidence of improved domestic consumption (link). Our colleagues see demand recovery as narrow, and policy-tilted towards high-end manufacturing supply chains, rather than consumption driven sectors which calls for the need of policy support to broaden demand. The high-end manufacturing supply chains in focus however, does provide relatively stronger demand support for base metals especially copper & aluminium. (Link to JPM China Economists' Mid-Year Outlook)

We provide our latest EMEA Metals & Mining valuations and commodity price scenario analysis (here).

## European Metals, Mining & Steel

Dominic O'Kane AC (44-20) 7742-6729 dominic.j.okane@JPM.com JPM Securities plc

Patrick Jones (44-20) 7742-5964  
patrick.jones@JPM.com  
JPM Securities plc

Asia Pacific Basic Materials

Lyndon Fagan  
(61-2) 9003-8648  
lyndon.fagan@JPM.com  
JPM Securities Australia Limited

North America Metals, Mining & Clean Tech

Bill Peterson (1-415) 315-6766 bill.peterson@jpmchase.com JPM Securities LLC

Global Commodities Research

Gregory C. Shearer  
(44-20) 7134-8161  
gregory.c.shearer@JPM.com  
JPM Securities plc

Figure 1: China Yangshan Copper Premium vs LME Copper Spot: Physical market premium recovered back above \$70/t whilst copper price trending sideways since late June

LHS: Yangshan Premium; RHS: LME Copper Spot; Unit: \$/t

![](images/70b261f98008e0b060dbfffeb7d5f1fdc1c270b9e042c9838febc393162554d7.jpg)  
Source: Bloomberg Finance L.P.

See page 9 for analyst certification and important disclosures, including non-US analyst disclosures.

Figure 2: Aluminum inventories movements in 2026 – weekly change in China visible aluminium inventory (SHFE + Bonded). 75kt of Aluminium destocking in the past week, strongest since 2026 CNY  
x-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY), y-axis = kt of aluminium increase / (decrease)  
![](images/f950ce32a1cb50f539602d34e6cc71f151ab5439771e4e251ade4446047f910c.jpg)  
\*Build over first and second weeks post-CNY averaged due to lagged inventory reporting.  
Source: SHFE, CRU, SMM, JPM Commodities, \*First and second weeks grouped together due to lagged inventory reporting

## China metals inventory channel check – week ended 3 July 2026

JPM is tracking China's metal inventories for potential insights regarding end-consumer demand activity. These high-frequency datapoints provide signals to gauge China metals consumption trends. Rapid pivots in inventory de-stocking volumes (or re-stocking) can potentially provide signals that downstream consumption is improving (or weakening).

Last week, we saw de-stocking across all three base metals. Following close to 2 months of muted copper inventory movement, Copper inventory draws re-emerged and saw sharper declines vs historical trends. Visible inventories (SHFE + Bonded) dropped by roughly $\sim 13\mathrm{kt}$ in the past week. Aluminium also continued to fall, with last week's destocking the strongest post CNY this year, declining by approximately $75\mathrm{kt}$ , vs only modest draw typically observed in this seasonal period. Zinc also reverted to a strong de-stocking of -11kt in the past week.

Figure 3: Weekly change in China visible copper inventory (SHFE + Bonded). Significant restocking of 13kt against seasonality in week ended 3 Jul'26 x-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY), y-axis = kt of copper increase / (decrease)  
![](images/ffe07374f0e4be1f51af7972a179947d1659413d4fe5aa87fe282d1ead779401.jpg)  
\*Build over first and second weeks post-CNY averaged due to lagged inventory reporting.  
Source: SHFE, CRU, SMM, JPM Commodities, \*First and second weeks grouped together due to lagged inventory reporting

Figure 4: Total China visible copper inventory (SHFE + Bonded) week ended 3 Jul'26. Copper inventory (163kt) in line vs 2025 low x-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY), y-axis = kt of copper  
![](images/dbc3e3a2903f0939dc2b96db72ab7cfec34cfaec79ee4acd8425ead8d07afe8f.jpg)  
Source: SHFE, CRU, SMM, JPM Commodities

Figure 5: Aluminum inventories movements in 2026 – weekly change in China visible aluminium inventory (SHFE + Bonded). 75kt of Aluminium destocking in the past week, strongest since 2026 CNY  
x-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY), y-axis = kt of aluminium increase / (decrease)  
![](images/21e74d946f5548bbe44c537333489f7dd7f70f87f6862cd942db6b7f6e45d57a.jpg)  
\*Build over first and second weeks post-CNY averaged due to lagged inventory reporting.  
Source: SHFE, CRU, SMM, JPM Commodities, \*First and second weeks grouped together due to lagged inventory reporting

Figure 6: Total China visible aluminum inventory (SHFE + Regional Warehouses) week ended 3 Jul'26. China aluminum inventory (1.1Mt) begins to fall due to stronger drawdowns in the past few weeks  
x-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY), y-axis = kt of aluminium  
![](images/5727c1e906bd0b6ad11ec2208d0dfdab8fbeb643cf31f4f2fa1e62ba4df75a8f.jpg)  
Source: SHFE, CRU, SMM, JPM Commodities

Figure 7: Zinc inventories movements in 2026 – weekly change in China visible zinc inventory (SHFE + Bonded). Destocking of 11kt of Zinc in the past week  
x-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY), y-axis = kt of aluminium increase / (decrease)  
![](images/947e94868a5e13868fe49d609123fa992c341bd6cfac4509c6149be0a573e465.jpg)  
\*Build over first and second weeks post-CNY averaged due to lagged inventory reporting.  
Source: SHFE, CRU, SMM, JPM Commodities, \*First and second weeks grouped together due to lagged inventory reporting

Figure 8: Total China visible zinc inventory for week ended 3 Jul'26. Total inventory (265kt) remains at the highest level since 2022 x-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY), y-axis = kt of zinc  
![](images/d56db1d06ed1c30344259168eeec84bcbe147ea1ef71eb9c458ee0b25395d040.jpg)  
Source: SHFE, CRU, SMM, JPM Commodities Research

Figure 9: China Yangshan Copper Premium vs LME Copper Spot: Physical market premium recovered back above \$70/t whilst copper price trending sideways since late June  
LHS: Yangshan Premium; RHS: LME Copper Spot; Unit: \$/t  
![](images/c38b607cb9f03048779da8b5041a57ab83bf1513b2bf0fb61b4625b9264ec025.jpg)  
Source: Bloomberg Finance L.P.

Figure 10: China steel mill margins extend losses driven by higher coking coal prices  
![](images/c465e78bd82c59d385e8c7ac0dd76a5a8bcb946391334a056a2e6b2952d1cbb2.jpg)  
Source: Bloomberg Finance L.P, JPM estimates.

Figure 11: China steel inventory week ending 2 Jul, +1% WoW and +11% YoY; Inventory has picked up since June Mt  
![](images/de3fbb62159fd6228c48ac01720be8a3f6f1529cc4003a480f45f595ccdf243e.jpg)  
Source: JPM estimates, Bloomberg Finance L.P.

Figure 12: Iron Ore inventory held at ports in China \~160Mt is high vs history and destocking has slowed after two months' of drawdown from March peak  
![](images/03f9582905419d24fdb3219a60a2776d6973f9951714209d911291bfc1dd2825.jpg)  
Source: JPM estimates, Bloomberg Finance L.P.

Figure 13: Global iron ore shipments - we are entering the seasonal period during which global iron ore shipments ramp up. Global shipments +8% MoM in April & +6% YoY  
Mt iron ore exports, red bar = February, typical seasonal trough for shipments is Jan/Feb  
![](images/5533ef209e5e68a1e5e03739d1a3a836f88caebc9820c6065532fd3ef76b357e.jpg)  
Source: JPM estimates, Bloomberg Finance L.P.

Figure 14: Australia iron ore shipments - Latest data suggests Australian iron ore shipments +8% MoM in April & +3% YoY Mt iron ore exports, red bar = February, typical seasonal trough for shipments is Jan/Feb  
![](images/e05288177f2ba50b7fdc9aa8c7be0266e353bdae6d53cebc9d353b4d27126d8d.jpg)  
Source: JPM estimates, Bloomberg Finance L.P.

Figure 15: Brazil iron ore shipments +10% MoM in April, +10% YoY  
Mt iron ore exports, red bar = February, typical seasonal trough for shipments is Jan/Feb  
![](images/f1f5465d7057b1eb8ba2c721fb5098058cf30f39cb87df359efe4984f2def4a5.jpg)  
Source: JPM estimates, Bloomberg Finance L.P.

Figure 16: Chinese visible copper inventory (SHFE + Bonded) for week ended 3 Jul. Copper inventories lower in the past week due to significant inventory draw  
![](images/40db8a2b32c425e8781c24e61e4fe3d9671bc83131ce4457242ecaba399d65d7.jpg)  
Source: SHFE, CRU, SMM, JPM Commodities

Figure 17: China visible aluminium inventory (SHFE + Regional Warehouses) for week ended 3 Jul. Aluminum inventories are still at the highest level vs 5-year range but de-stocking has gained momentum in China  
![](images/54965fd203b598a4a649f2a2b660bf690168cb5654838601eace6a58978d8bde.jpg)  
Source: SHFE, CRU, SMM, JPM Commodities Research

Figure 18: China visible zinc inventory (SHFE + Regional Warehouses) for week ended 3 Jul. Zinc inventories are still at the highest level vs 5-year range kt of zinc  
![](images/570fc26a19943b04ee6d1d7f1b026392b5b048956d9a6ae63c032bd83cc75d7c.jpg)  
Source: SHFE, CRU, SMM, JPM Commodities

Companies Discussed in This Report (all prices in this report as of market close on 03 July 2026, unless otherwise indicated) Anglo American (AGLJ.J)(AGLJ.J/81,651c/UW), BHP Group Ltd (BHG SJ)(BHGJ.J/68,093c/N), Lundin Mining(LUMIN.ST/Skr239.00/UW), Norsk Hydro(NHY.OL/Nkr86.20/OW), Rio Tinto plc(RIO.L/7,070p/N)

## Disclosures

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

\- Market Maker/ Liquidity Provider: JPM is a market maker and/or liquidity provider in the financial instruments of/related to Anglo American (AGLJ.J), BHP Group Ltd (BHG SJ), Lundin Mining, Norsk Hydro, Rio Tinto plc or related entities.

\- Client: JPM currently has, or had within the past 12 months, the following entity(ies) as clients: Anglo American (AGLJ.J), BHP Group Ltd (BHG SJ), Lundin Mining, Norsk Hydro, Rio Tinto plc or related entities.

\- Client/Investment Banking: JPM currently has, or had within the past 12 months, the following entity(ies) as investment banking clients: BHP Group Ltd (BHG SJ), Rio Tinto plc or related entities.

\- Client/Non-Investment Banking, Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-investment-banking, securities-related: Anglo American (AGLJ.J), BHP Group Ltd (BHG SJ), Lundin Mining, Norsk Hydro, Rio Tinto plc or related entities.

\- Client/Non-Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-securities-related: Anglo American (AGLJ.J), BHP Group Ltd (BHG SJ), Lundin Mining, Norsk Hydro, Rio Tinto plc or related entities.

\- Investment Banking Compensation Received: JPM has received in the past 12 months compensation for investment banking services from BHP Group Ltd (BHG SJ), Rio Tinto plc or related entities.

\- Potential Investment Banking Compensation: JPM expects to receive, or intends to seek, compensation for investment banking services in the next three months from Anglo American (AGLJ.J), BHP Group Ltd (BHG SJ), Lundin Mining, Norsk Hydro, Rio Tinto plc or related entities.

• Non-Investment Banking Compensation Received: JPM has received compensation in the past 12 months for products or services other than investment banking from Anglo American (AGLJ.J), BHP Group Ltd (BHG SJ), Lundin Mining, Norsk Hydro, Rio Tinto plc or related entities.

• Broker: JPM acts as Corporate Broker to Rio Tinto plc or related entities.

• JSE Sponsor: JPM acts as Johannesburg Stock Exchange Sponsor to BHP Group Ltd (BHG SJ) or related entities.

\- Debt Position: JPM may hold a position in the debt securities of Anglo American (AGLJ.J), BHP Group Ltd (BHG SJ), Lundin Mining, Norsk Hydro, Rio Tinto plc or related entities, if any.

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

Anglo American (AGLJ.J) (AGLJ.J, AGL SJ) Price Chart  
![](images/1843b070341dd2b1bfefe14484f8d0adcc0f6e26c260b4dbd421d097258ec900.jpg)  
Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Jan 01, 1999. All share prices are as of market close on the previous business day.

<table><tr><td>Date</td><td>Rating</td><td>Price (c)</td><td>Price Target (c)</td></tr><tr><td>14-Jul-23</td><td>OW</td><td>55980</td><td>64,000</td></tr><tr><td>20-Jul-23</td><td>OW</td><td>53115</td><td>63,500</td></tr><tr><td>28-Jul-23</td><td>OW</td><td>55700</td><td>60,500</td></tr><tr><td>14-Sep-23</

[中间内容因长度限制已省略]

. Material published by non-U.S. affiliates is distributed in the U.S. by JPMS who accepts responsibility for its content.

General: Additional information is available upon request. The information in this material has been obtained from sources believed to be reliable. While all reasonable care has been taken to ensure that the facts stated in this material are accurate and that the forecasts, opinions and expectations contained herein are fair and reasonable, JPM Chase & Co. or its affiliates and/or subsidiaries (collectively JPM) make no representations or warranties whatsoever to the completeness or accuracy of the material provided, except with respect to any disclosures relative to JPM and the Research Analyst's involvement with the issuer that is the subject of the material. Accordingly, no reliance should be placed on the accuracy, fairness or completeness of the information contained in this material. There may be certain discrepancies with data and/or limited content in this material as a result of calculations, adjustments, translations to different languages, and/or local regulatory restrictions, as applicable. These discrepancies should not impact the overall investment analysis, views and/or recommendations of the subject company(ies) that may be discussed in the material. Artificial intelligence tools may have been used in the preparation of this material, including assisting in data analysis, pattern recognition, and content drafting for research material. JPM accepts no liability whatsoever for any loss arising from any use of this material or its contents, and neither JPM nor any of its respective directors, officers or employees, shall be in any way responsible for the contents hereof, apart from the liabilities and responsibilities that may be imposed on them by the relevant regulatory authority in the jurisdiction in question, or the regulatory regime thereunder. Opinions, forecasts or projections contained in this material represent JPM's current opinions or judgment as of the date of the material only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.
"""
