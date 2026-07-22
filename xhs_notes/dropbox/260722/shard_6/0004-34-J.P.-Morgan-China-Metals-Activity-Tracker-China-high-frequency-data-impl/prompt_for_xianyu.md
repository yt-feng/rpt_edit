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
China high frequency data implies higher rates of copper & aluminium consumption in June-July; China copper premium hit \$100/t last week

We present our high-frequency inventory trends for base metals and iron ore in China for the week ended 17 Jul'26. Our data plots China weekly metals inventory trends, a proxy for consumption. Copper saw another 17kt drawdown last week with visible inventory in China now down to \~120kt, 30kt below the low level we saw in 2025. End of last week, Yangshan Copper Premium hit \$100/t mark which was last reached in May'25. Aluminium's strong destocking also continued, with total visible inventory now back to \~1Mt. JPM Commodities Research forecast a sizeable 3Q ex-China deficit that will likely pull LME pricing higher to attract metals into the global market from China (link).

JPM Commodities Research published a China demand monitor based on detailed data available to 5M'26 (link). Our colleagues note that consumption-weighted end-use for China Copper demand fell -5% YoY in 5M'26, but apparent consumption was +8% yoy in May. However in the case of both Copper and Aluminium, these weak demand datapoints represent the period 5M'26 which is consistent with our previous high frequency data assessment of weak de-stocking indictators in the month of May. Our high frequency data tracker implies strengthening in copper and aluminium consumption in June-July, as shown in the charts below.

China Q2 economic releases last week showed Q2 real GDP slowed to 4.3% YoY, from 5.0% in 1Q; manufacturing was resilient but FAI contracted significantly. Latest loan growth data for June also showed material weakness, with TSF growth slowing by 0.3% pts to a record low of 7.4% (link / link).

Within EMEA Miners, our favoured name remains Antofagasta (link) as we see the copper price support to generate FCF inflection and an inexpensive valuation on a 2028E basis driven by $>30\%$ brownfield growth. We are Neutral on BHP and RIO London listings and are UW on Anglo American taking into account of cost inflation risk at its Iron Ore division and potential weak Diamonds division result in H1'26 (link).

We provide our latest EMEA Metals & Mining valuations and commodity price scenario analysis (here).

## European Metals, Mining & Steel

Dominic O'Kane AC
(44-20) 7742-6729
dominic.j.okane@JPM.com
JPM Securities plc

Patrick Jones
(44-20) 7742-5964
patrick.jones@JPM.com
JPM Securities plc

Asia Pacific Basic Materials

Lyndon Fagan
(61-2) 9003-8648
lyndon.fagan@JPM.com
JPM Securities Australia Limited

North America Metals, Mining & Clean Tech

Bill Peterson
(1-415) 315-6766
bill.peterson@jpmchase.com
JPM Securities LLC

Global Commodities Research

Gregory C. Shearer
(44-20) 7134-8161
gregory.c.shearer@JPM.com
JPM Securities plc

Figure 1: Weekly change in China visible copper inventory (SHFE + Bonded). Red box shows May period covered by JPM Commodities Research, Jun-July appear to show a pick up in consumption

x-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY), y-axis = kt of copper increase / (decrease)  
![](images/456c7e317dddb2886605838035f73bf35fd9d17014bc56011f4c11866bddf65a.jpg)  
\*Build over first and second weeks post-CNY averaged due to lagged inventory reporting.  
Source: SHFE, CRU, SMM, JPM Commodities, \*First and second weeks grouped together due to lagged inventory reporting

Figure 2: Aluminum inventories movements in 2026 – weekly change in China visible aluminium inventory (SHFE + Bonded). 52kt of Aluminium destocking in the past week, strongest since 2026 CNY

x-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY), y-axis = kt of aluminium increase / (decrease)  
![](images/52a2fb800deb26f316ce94d6516488a3437d86db02d727a75e8f9a6235812b80.jpg)  
\*Build over first and second weeks post-CNY averaged due to lagged inventory reporting.  
Source: SHFE, CRU, SMM, JPM Commodities, \*First and second weeks grouped together due to lagged inventory reporting

## China metals inventory channel check – week ended 17 July 2026

JPM is tracking China's metal inventories for potential insights regarding end-consumer demand activity. These high-frequency datapoints provide signals to gauge China metals consumption trends. Rapid pivots in inventory de-stocking volumes (or re-stocking) can potentially provide signals that downstream consumption is improving (or weakening).

We are into the fifth week of seeing strong de-stocking in both Copper and Aluminium. Copper inventory saw another 17kt drawdown in the past week, bringing total visible copper inventory in China down to \~120kt. Aluminium also continued the strong de-stocking momentum with another drawdown of 54kt last week. Inventory level is now back to \~1Mt. Zinc however, saw re-stocking. Total onshore Zinc inventory is at 268kt, which is >130kt higher vs 5-year historical average at this time of the year.

Figure 3: Total China visible copper inventory (SHFE + Bonded) week ended 17 Jul'26. Copper inventory (119kt) tightest in the past decade during this time of the year; Inventory level sits 30kt below 2025 low  
x-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY), y-axis = kt of copper  
![](images/dce52117b6cfb7cfc30a94b152420b22831447274e9edb91dbba67f461065a28.jpg)  
Source: SHFE, CRU, SMM, JPM Commodities

Figure 4: Total China visible aluminum inventory (SHFE + Regional Warehouses) week ended 17 Jul'26. China aluminum inventory (1.0Mt) begins to fall due to stronger drawdowns in the past few weeks  
x-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY), y-axis = kt of aluminium  
![](images/bbd5392b71bd3e2f4ec114d6707d156306a7cb2d4b3540ee798047c23ec1dcb8.jpg)  
Source: SHFE, CRU, SMM, JPM Commodities

Figure 5: Zinc inventories movements in 2026 – weekly change in China visible zinc inventory (SHFE + Bonded). Zinc restocking of 3kt in the past week x-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY), y-axis = kt of aluminium increase / (decrease)  
![](images/01afd10d578eda08ce2a8cc6e7cffa82115aea6258149ce8851e4edbef20ba28.jpg)  
\*Build over first and second weeks post-CNY averaged due to lagged inventory reporting.
Source: SHFE, CRU, SMM, JPM Commodities, \*First and second weeks grouped together due to lagged inventory reporting

Figure 6: Total China visible zinc inventory for week ended 17 Jul'26. Total inventory (268kt) remains at the highest level since 2022 x-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY), y-axis = kt of zinc  
![](images/cb68ff1b139a379939be85a45ffa841625642574a94b47122155a5df566c6281.jpg)  
Source: SHFE, CRU, SMM, JPM Commodities Research

Figure 7: China Yangshan Copper Premium vs LME Copper Spot: Strong physical market demand brings premium to \$100/t
LHS: Yangshan Premium; RHS: LME Copper Spot; Unit: \$/t  
![](images/739c504a6b66880a160f288441db544e8cbfddd2e0478429a4f28d9c55efebf7.jpg)  
Source: Bloomberg Finance L.P.

Figure 8: China steel mill margins extend losses driven by higher coking coal prices  
![](images/cfb2e63653a950b17c238b4791ce95398ade0b3541ef987c99bf1ba5da53070f.jpg)  
Source: Bloomberg Finance L.P, JPM estimates.

Figure 9: China steel inventory week ending 17 Jul, flat WoW and +12% YoY; Inventory has picked up since June  
![](images/21f5a2bd0b6602cc88de2fc696ba11e0f25d0a07b3233b02757007e1478cf8fd.jpg)  
Source: JPM estimates, Bloomberg Finance L.P.

Figure 10: Iron Ore inventory saw \~3Mt drawdown in the past week after flat inventory for \~9 weeks  
![](images/609c07b93252b252daea69bb42eee84cc6f8fd46777cab13f7cb6a95d33c3ee4.jpg)  
Source: JPM estimates, Bloomberg Finance L.P.

Figure 11: Global iron ore shipments - Global shipments +2% MoM in May & -2% YoY  
Mt iron ore exports, red bar = February, typical seasonal trough for shipments is Jan/Feb  
![](images/1eb20227cdb13fd2310683a2706cb31e1e0db93077dfd2b4fcbb3c72b24d2d2b.jpg)  
Source: JPM estimates, Bloomberg Finance L.P.

Figure 12: Australia iron ore shipments - Latest data suggests Australian iron ore shipments +5% MoM in May& -2% YoY
Mt iron ore exports, red bar = February, typical seasonal trough for shipments is Jan/Feb  
![](images/80cb7b04b96a4b5c116cb23c5d5afab3c4242e5a33489515c41360883ba09be3.jpg)  
Source: JPM estimates, Bloomberg Finance L.P.

Figure 13: Brazil iron ore shipments -3% MoM in May, -8% YoY  
Mt iron ore exports, red bar = February, typical seasonal trough for shipments is Jan/Feb  
![](images/a8655d2436fd3d25e89d7dfeeeee0b60af54e773e8398a0493d3bda283976d5b.jpg)  
Source: JPM estimates, Bloomberg Finance L.P.

Figure 14: Chinese visible copper inventory (SHFE + Bonded) for week ended 17 Jul. Copper inventories lower in the past week due to significant inventory draw  
![](images/9c98b8cf8edf60b3ea0117b831586ef83f17a8bdc0e710c8606eff8a31dde56e.jpg)  
Source: SHFE, CRU, SMM, JPM Commodities

Figure 15: China visible aluminium inventory (SHFE + Regional Warehouses) for week ended 17 Jul. Destocking in the past few weeks has significantly reduced aluminium inventory  
![](images/c72c8ec5c7fd841598e056cd21ac0da4593b20817ee787da9ac77e48a46da3f8.jpg)  
Source: SHFE, CRU, SMM, JPM Commodities Research

Figure 16: China visible zinc inventory (SHFE + Regional Warehouses) for week ended 17 Jul. Zinc inventories are still at the highest level vs 5-year range kt of zinc  
![](images/37525409374fe27321da12bd50762ae739b39c7d37ca0505897f53c2d18672b5.jpg)  
Source: SHFE, CRU, SMM, JPM Commodities

Companies Discussed in This Report (all prices in this report as of market close on 17 July 2026, unless otherwise indicated)
Anglo American (AGLJ.J)(AGLJ.J/75,537c/UW), Antofagasta(ANTO.L/3,491p/OW), BHP Group Ltd (BHG SJ) (BHGJ.J/66,222c/N), Lundin Mining(LUMIN.ST/Skr225.80/UW), Norsk Hydro(NHY.OL/Nkr84.96/OW), Rio Tinto plc(RIO.L/6,726p/N)

## Disclosures

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe of the relevant duration of the region. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap Equity Research, each stock's expected total return is compared to the expected total return of a benchmark country market index, not to those Research Analysts' coverage universe. If it does not appear in the Important Disclosures section of this report, the certifying Research Analyst's coverage universe can be found on JPM's Research website, https://www.JPMmarkets.com.

Coverage Universe: O'Kane, Dominic J: Acerinox (ACX.MC), Anglo American (AAL.L), Anglo American (AGLJ.J) (AGLJ.J), Aperam (APAM.AS), ArcelorMittal (MT.AS), BHP Group Ltd (BHG SJ) (BHGJ.J), BHP Group Ltd (BHP LN) (BHPB.L), Glencore PLC (GLEN.L), Glencore plc (GLN SJ) (GLNJ.J), Harmony Gold Mining Co Ltd (HARJ.J), Harmony Gold Mining-ADR (HMY), Impala Platinum Holdings Ltd (IMPJ.J), Kumba Iron Ore Limited (KIOJ.J), Northam Platinum Ltd (NPHJ.J), Outokumpu (OUT1V.HE), Rio Tinto plc (RIO.L), SSAB-A (SSABa.ST), SSAB-B (SSABb.ST), Salzgitter (SZGG.DE), Sibanye-Stillwater (SSWJ.J), Sibanye-Stillwater-ADR (SBSW), ThyssenKrupp (TKAG.DE), Valterra Platinum - ADR (AGPPF), Valterra Platinum Limited (VALJ.J), voestalpine (VOES.VI)

## JPM Equity Research Ratings Distribution, as of July 04, 2026

<table><tr><td></td><td>Overweight (buy)</td><td>Neutral (hold)</td><td>Underweight (sell)</td></tr><tr><td>JPM Global Equity Research Coverage*</td><td>53%</td><td>36%</td><td>12%</td></tr><tr><td>IB clients**</td><td>83%</td><td>80%</td><td>73%</td></tr><tr><td>JPMS Equity Research Coverage*</td><td>51%</td><td>37%</td><td>12%</td></tr><tr><td>IB clients**</td><td>95%</td><td>92%</td><td>87%</td></tr></table>

\*Please note that the percentages may not add to 100% because of rounding.

\*\*Percentage of subject companies within each of the "buy," "hold" and "sell" categories for which JPM has provided investment banking services within the previous 12 months.

For purposes of FINRA ratings distribution rules only, our Overweight rating falls into a buy rating category; our Neutral rating falls into a hold rating category; and our Underweight rating falls into a sell rating category. Please note that stocks with an NR designation are not included in the table above. This information is current as of the end of the most recent calendar quarter.

Equity Valuation and Risks: For valuation methodology and risks associated with covered companies or price targets 

[中间内容因长度限制已省略]

gence tools may have been used in the preparation of this material, including assisting in data analysis, pattern recognition, and content drafting for research material. JPM accepts no liability whatsoever for any loss arising from any use of this material or its contents, and neither JPM nor any of its respective directors, officers or employees, shall be in any way responsible for the contents hereof, apart from the liabilities and responsibilities that may be imposed on them by the relevant regulatory authority in the jurisdiction in question, or the regulatory regime thereunder. Opinions, forecasts or projections contained in this material represent JPM's current opinions or judgment as of the date of the material only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR
"""
