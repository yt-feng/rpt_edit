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
# China Renewable Energy

## Solar Product Prices Further Dipped; Companies Loss-Making except Inverter and PV Film Players

## CITI'S TAKE

PRC solar supply chain continues to face downward pressure from oversupply-led ASP cuts, including down 0.6-1.1% wow for polysilicon, wafter, solar cell and module prices. Most PRC solar equipment suppliers were loss-making in 1H26E dragged by low product prices and weak demand, except inverter and PV film makers. Deye expects its net profit to be Rmb1,480-1,540m (up 81-89% yoy and 25-30% qoq) in 2Q26E riding on strong energy storage demand and that of Hangzhou First is Rmb558m (+489.3% yoy and +78.8% qoq) thanks to increased PV film prices. For module makers, LONGi's net loss reduced slightly qoq in 2Q26E while that for JA Solar exacerbated yoy and qoq. Polysilicon maker Tongwei's quarterly net loss was largely stable yoy and qoq. In PRC solar and ESS sector, we prefer ESS makers like Sungrow and Deye with high shipment volume growth.

Polysilicon prices further declined — The average market price of n-type grade rod-type polysilicon declined 0.8% wow to Rmb31.6/kg, and that for granular polysilicon was unchanged at Rmb31.5/kg in the week ended 15 Jul 2026. PRC monthly polysilicon is expected to rise 7.6% mom to over 100k tons in July in flood season, which is more than the expected monthly demand of 91k tons, according to China Silicon Industry Association. According to SMM, total polysilicon inventory at producer plants was 310k tons as of 15 July, up 3.0% wow.

Wafer and solar cell prices mildly dropped wow — Market prices of n-type wafer declined 1.1% wow to Rmb0.86/W for 182mm products and -0.9% wow at Rmb1.16/W for 210mm products, due to weak demand. SMM estimates China wafer production volume could drop by 3.7% mom to 52.3GW in July, and its inventory level increased 2.3% wow to 27.9k GW as of July 9. Capacity consolidation has begun at wafer segment, with tier 2 and 3 companies leasing out their capacity, according to SMM. Average solar cell price further was dropped 0.9% wow to Rmb0.27/W for TOPCon products this week.

Solar module price continued to drop — Average solar module price was down 0.6% wow to Rmb0.71/W for 182mm products this week. The price further declined despite of a moderate increase of downstream demand from utility-scale projects. PRC monthly solar module output is expected to be +11.0% mom to 42.0GW in July, according to SMM.

China Solar Sector

Pierre Lau, CFA $^{AC}$

+852-2501-2716

pierre.lau@citi.com

Air Ma

air.ma@citi.com

See Appendix A-1 for Analyst Certification, Important Disclosures and Research Analyst Affiliations

Solar glass prices flat — Average solar glass market prices continued to be both flat wow at Rmb9.0/m2 for 2.0mm products and at Rmb15.5/m2 for 3.2mm ones. The industry-wide average inventory period was 47.8 days as of July 9, -0.4% wow. China operational daily solar glass melting capacity reduced 2.0% wow to 79,750 tonnes (-15.2% yoy) as of July 9 with two production lines being suspended, according to SCI99.

Solar companies reporting losses in 1H26 — Based on profit alerts issued so far, most PRC solar companies stayed loss making in 1H26 due to low product prices, except inverter and PV film maker:

\- Deye estimated its net profit to jump 75-79% yoy to Rmb2,668-2,728m in 1H26E, including up 81-89% yoy and 25-30% qoq to Rmb1,480-1,540m in 2Q26E with explosive demand growth of residential energy storage system;

\- Hangzhou First reported preliminary net profit +75.4% yoy to Rmb869m in 1H26E, including +489.3% yoy and +78.8% qoq to Rmb558m in 2Q26E mainly boosted by higher sales price of PV films;

\- Flat Glass estimated its net loss to be Rmb300-400m in 1H26E, including Rmb338-438m in 2Q26E (vs. net profits of Rmb155m in 2Q25 and Rmb38m in 1Q26) dragged by sharp decline of solar glass prices;

\- Tongwei estimated its net loss to be Rmb4.8-5.4bn in 1H26E, including Rmb2.4-3.0bn in 2Q26E (vs. losses of Rmb2,363m in 2Q25 and Rmb2,444m in 1Q26);

\- LONGi estimated its net loss to be Rmb3.4-3.8bn in 1H26E, including Rmb1.5-1.9bn in 2Q26E (vs. losses of Rmb1,133m in 2Q25 and Rmb1,920m in 1Q26);

\- JA Solar estimates its net loss to be Rmb 2.4-2.9 bn in 1H26E, including Rmb1.3-1.8bn in 2Q26E (vs. losses of Rmb942m in 2Q25 and Rmb1,067m in 1Q26).

Figure 1. ePRC weekly polysilicon prices in the week ended Jul 15

<table><tr><td></td><td colspan="4">Mono-S</td></tr><tr><td>182mm TOPCon</td><td>This week</td><td>WoW</td><td>MoM</td><td>YoY</td></tr><tr><td>Polysilicon (Rmb/kg)</td><td>31.6</td><td>-0.8%</td><td>-3.6%</td><td>-28.3%</td></tr><tr><td>Wafer (Rmb/pc)</td><td>0.86</td><td>-1.1%</td><td>-2.3%</td><td>-21.8%</td></tr><tr><td>Cell (Rmb/W)</td><td>0.27</td><td>-0.9%</td><td>-10.9%</td><td>0.0%</td></tr><tr><td>Module (Rmb/W)</td><td>0.71</td><td>-0.6%</td><td>-1.3%</td><td>7.9%</td></tr><tr><td>Glass -2.0mm (Rmb/m2)</td><td>9.0</td><td>0.0%</td><td>0.0%</td><td>-12.2%</td></tr></table>

Figure 2. PRC weekly polysilicon price  
![](images/6663dbc53e5a0b9e6227f95702fb1b12ecbf4b18ed296644012f398e65c2b936.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: SMM, Citi

Figure 3. PRC weekly wafer price  
![](images/475dd4da0cd8496831b44a57899673eec236455af7ea6950989fa511f8837737.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: SMM, Citi

Figure 4. PRC weekly cell price  
![](images/b9e25689069a01e002c866134395257eb499cef33604d3e3cfc65f756bf40d1e.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: SMM, Citi

Figure 5. PRC weekly module price  
![](images/1702581f01230e4a048e774f498b0534565e543284b63ffc1971d73d7a92ba04.jpg)  
Source: SMM, Citi  
© 2026 Citi Inc. No redistribution without Citi's written permission.

Figure 6. PRC weekly solar glass price  
![](images/f8d8428adf101ee49e7a51f21bd30f363a7b5779586baf8b707aa7bc0f04e9f9.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, SMM

## Companies Mentioned:

Flat Glass (6865.HK; HK\$6.26; 2; 15 Jul 26; 16:10) | Hangzhou First Applied Material (603806.SS; Rmb14.75; 1; 15 Jul 26; 15:00) | JA Solar (002459.SZ; Rmb7.18; 3; 15 Jul 26; 15:00) | LONGi Green Energy Technology (601012.SS; Rmb12.0; 1; 15 Jul 26; 15:00) | Ningbo Deye Technology (605117.SS; Rmb85.4; 1; 15 Jul 26; 15:00) | Sungrow Power Supply (300274.SZ; Rmb108.95; 1; 15 Jul 26; 15:00) | Tongwei (600438.SS; Rmb10.8; 1; 15 Jul 26; 15:00)

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from Flat Glass, JA Solar, LONGi Green Energy Technology, Sungrow Power Supply in the past 12 months.

Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: Flat Glass, JA Solar, Sungrow Power Supply.

Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, non-securities-related: Flat Glass, JA Solar, LONGi Green Energy Technology, Sungrow Power Supply.

Analysts' compensation is determined by Citi management and Citi's senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the "Firm"). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.

For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.

Unless stated otherwise neither the Research Analyst nor any member of their team has viewed the material operations of the Companies for which an investment view has been provided within the past 12 months.

For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product ("the Product"), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013, Attention: Legal/Compliance [E6WYB6412478]. In addition, the same important disclosures, with the exception of the Valuation and Risk assessments and historical disclosures, are contained on the Firm's disclosure website at https://www.citivelocity.com/cvr/eppublic/citi\_research\_disclosures. Valuation and Risk assessments can be found in the text of the most recent research note/report regarding the subject company. Pursuant to the Market Abuse Regulation a history of all Citi recommendations published during the preceding 12-month period can be accessed via Citi Velocity (https://www.citivelocity.com/cv2) or your standard distribution portal. Historical disclosures (for up to the past three years) will be provided upon request.

Citi Equity Ratings Distribution

<table><tr><td></td><td colspan="3">12 Month Rating</td><td colspan="3">Catalyst Watch</td></tr><tr><td>Data current as of 01 Jul 2026</td><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Citi Global Fundamental Coverage (Neutral=Hold)</td><td>61%</td><td>32%</td><td>7%</td><td>36%</td><td>48%</td><td>16%</td></tr><tr><td>% of companies in each rating category that are investment banking clients</td><td>38%</td><td>42%</td><td>27%</td><td>42%</td><td>37%</td><td>36%</td></tr></table>

Guide to Citi Fundamental Research Investment Ratings:

Citi stock recommendations include an investment rating and an optional risk rating to highlight high risk stocks. Risk rating takes into account both price volatility and fundamental criteria. Stocks will either have no risk rating or a High risk

## rating assigned.

Investment Ratings: Citi investment ratings are Buy, Neutral and Sell. Our ratings are a function of analyst expectations of expected total return ("ETR") and risk. ETR is the sum of the forecast price appreciation (or depreciation) plus the dividend yield for a stock within the next 12 months. The target price is based on a 12 month time horizon. The Investment rating definitions are: Buy (1) ETR of 15% or more or 25% or more for High risk stocks; and Sell (3) for negative ETR. Any covered stock not assigned a Buy or a Sell is a Neutral (2). For stocks rated Neutral (2), if an analyst believes that there are insufficient valuation drivers and/or investment catalysts to derive a positive or negative investment view, they may elect with the approval of Citi management not to assign a target price and, thus, not derive an ETR. Citi may suspend its rating and target price and assign "Rating Suspended" status for regulatory and/or internal policy reasons. Citi may also suspend its rating and target price and assign "Under Review" status for other exceptional circumstances (e.g. lack of information critical to the analyst's thesis, trading suspension) affecting the company and/or trading in the company's securities. In both such situations, the rating and target price will show as “—” and “-” respectively in the rating history price chart. Prior to 11 April 2022 Citi assigned "Under Review" status to both situations and prior to 11 Nov 2020 only in exceptional circumstances. As soon as practically possible, the analyst will publish a note re-establishing a rating and investment thesis. Investment ratings are determined by the ranges described above at the time of initiation of coverage, a change in investment and/or risk rating, or a change in target price (subject to limited management discretion). At times, the expected total returns may fall outside of these ranges because of market price movements and/or other short-term volatility or trading patterns. Such interim deviations will be permitted but will become subject to review by Research Management. Your decision to buy or sell a security should be based upon your personal investment objectives and should be made only after evaluating the stock's expected performance and risk.

## Catalyst Watch/Short Term Views ("STV") Ratings Disclosure:

Catalyst Watch and STV Upside/Downside calls: Citi may also include a Catalyst Watch or STV Upside or Downside call to indicate the analyst expects the share price to rise (fall) in absolute terms over a specified period of 30 or 90 days in reaction to one or more specific near-term catalysts or events impacting the company or the market. A Catalyst Watch will be published when Analyst confidence is high that an impact to share price will occur; it will be a STV when confidence level is moderate. A Catalyst Watch or STV Upside/Downside call will automatically expire at the end of the specified 30/90 day period. The Catalyst Watch will also be automatically removed if share price performance (calculated at market close) exceeds $15\%$ against the direction of the call (unless over-ridden by the analyst). The analyst may also remove a Catalyst Watch or STV call prior to the end of the specified period in a published research note. A Catalyst Watch/STV Upside or Downside call may be different from and does not affect a stock's fundamental equity rating, which reflects a longer-term total absolute return expectation. For purposes of FINRA ratings-distribution-disclosure rules, a Catalyst Watch/STV Upside call corresponds

[中间内容因长度限制已省略]

eipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality,

accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
