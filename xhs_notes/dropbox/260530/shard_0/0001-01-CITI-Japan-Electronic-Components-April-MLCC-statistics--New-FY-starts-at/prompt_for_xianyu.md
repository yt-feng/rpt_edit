你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  ✅ 三大情景框架：DCF、P/ARR、EV/Sales
  ✅ 关键变量分析
  ✅ 估值逻辑、假设、终值占比等核心内容覆盖
  ✅ 适合准备 AI 相关面试、研究 AI 估值的同学
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
28 May 2026 00:55:09 ET | 10 pages

# Japan Electronic Components

April MLCC statistics: New FY starts at high levels

# CITI'S TAKE

The Ministry of Finance released trade statistics at 9:30 on May 28. April MLCC shipment volume rose 10.4% YoY and 6.5% MoM, shipment value rose 28.0% YoY and 9.3% MoM (in USD: +16.6% YoY and +8.9% MoM), and ASP grew 15.9% YoY and 2.6% MoM. April benefited from YoY yen depreciation ( $¥144/$$ → $¥158/$$ ), but ongoing strong demand for AI servers drove ASPs to high levels. Our forecast for Murata's Q1 capacitor revenue suggests approximately 15% YoY growth, and we see numbers well above this as positive. MLCC company shares have risen significantly post-earnings, and we believe expectations of favorable Q1 progress versus guidance will continue to act as support.

Takayuki Naito $^{AC}$

+81-3-6776-4644

takayuki.naito@citi.com

Figure 1. Summary of MLCC trade statistics   
![](images/2fa2a86c3c8899a638402a3099a9cd4c022125b90b40cdf441a139b2bbf0ac77.jpg)

![](images/04b4ebe8065a8e6787c2afe93260d8c1f927a8e49bf50d2c3544c48158667e15.jpg)

![](images/a6103f92872c01bb37f5118d561d244d6f952e722e17c164b6e97e47fbd51ebe.jpg)

<details>
<summary>line</summary>

| Date   | g(000pieces)(LHS) | g(000pieces) YoY(RHS) |
|--------|-------------------|------------------------|
| 07/01  | 10                | 60%                    |
| 08/01  | 9                 | 40%                    |
| 09/01  | 8                 | 20%                    |
| 10/01  | 7                 | 0%                     |
| 11/01  | 6                 | -20%                   |
| 12/01  | 5                 | -40%                   |
| 13/01  | 4                 | -20%                   |
| 14/01  | 3                 | 0%                     |
| 15/01  | 2                 | 20%                    |
| 16/01  | 1                 | 40%                    |
| 17/01  | 2                 | 20%                    |
| 18/01  | 3                 | 0%                     |
| 19/01  | 4                 | -20%                   |
| 20/01  | 5                 | -40%                   |
| 21/01  | 6                 | -20%                   |
| 22/01  | 7                 | 0%                     |
| 23/01  | 8                 | 20%                    |
| 24/01  | 9                 | 40%                    |
| 25/01  | 10                | 60%                    |
| 26/01  | 11                | 40%                    |
</details>

![](images/b3e17162104c4b793544863b01cdf3ed00b28fea4ced6e517238039b69cd6e71.jpg)

<details>
<summary>line</summary>

| Date   | USD price per gram (YoY) |
|--------|--------------------------|
| 16/07  | -30%                     |
| 17/07  | -20%                     |
| 18/07  | 40%                      |
| 19/07  | 30%                      |
| 20/07  | 10%                      |
| 21/07  | -10%                     |
| 22/07  | -20%                     |
| 23/07  | -10%                     |
| 24/07  | 10%                      |
| 25/07  | 0%                       |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.   
Source: MoF, Citi

# Murata

(6981.T; ¥7820.0; 2; 27 May 26; 15:30)

# Valuation

In setting our target prices for the electronic component industry, we employ a RoIC-WACC approach, taking net cash into consideration. We set a base year of FY3/28, assume an expected growth rate of 0% and a risk-free rate of 1.5%, and calculate an equity-risk premium of 4.0% from the recent TOPIX earnings yield.

Our ¥3,900 target price is derived as follows.

Theoretical shareholder value (= FY3/28E adjusted NOPAT x future business value multiplier + end-FY3/28E net cash [after deducting an amount equivalent to 5% of annual sales, including book value of investment securities] – end-FY3/28E minority interest) / (1 + WACC)^(number of months to end of valuation base FY/12).

# Risks

Risks to our target price include 1) overall technology product demand trends, 2) automotive supply chain inventory adjustments, 3) rapid forex changes, 4) intensified competition on the emergence of new rivals in Asia, 5) renewed growth acceleration and market share trends in high-end smartphones, and 6) a change in MLCC supply-demand or price hikes.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

# Appendix A-1

# ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

# IMPORTANT DISCLOSURES

# Murata (6981)

Ratings and Target Price History
Fundamental Research

Analyst: Takayuki Naito

![](images/bb352644e5de122acad6d9a1b8084453eee792bff98366c89d686cd534408a2f.jpg)

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>15-Jun-23 02:05:13</td><td>2</td><td>*2,833</td><td>2,840</td></tr><tr><td>2</td><td>12-Sep-23 02:05:15</td><td>2</td><td>*2,767</td><td>2,731</td></tr><tr><td>3</td><td>29-Sep-23 02:05:36</td><td>2</td><td>*2,800</td><td>2,734</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>4</td><td>06-Dec-23 01:05:00</td><td>2</td><td>*3,000</td><td>2,892</td></tr><tr><td>5</td><td>13-Dec-24 01:35:00</td><td>2</td><td>*2,700</td><td>2,493</td></tr><tr><td>6</td><td>27-May-25 02:35:00</td><td>2</td><td>*2,200</td><td>2,081</td></tr></table>

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>7</td><td>18-Aug-25 02:35:00</td><td>2</td><td>*2,400</td><td>2,444</td></tr><tr><td>8</td><td>15-Dec-25 02:24:12</td><td>2</td><td>*3,300</td><td>3,271</td></tr><tr><td>9</td><td>17-Mar-26 02:35:59</td><td>2</td><td>*3,900</td><td>3,802</td></tr></table>

Rating/target price changes above reflect Eastern Time

# Murata (6981)

Short-Term View/Catalyst Watch Research

Analyst: Takayuki Naito

![](images/ef08e4cd8650562591199dfa91abdf9bbbf09825b4d6be1ed5b794f5e99d49ab.jpg)

<details>
<summary>line</summary>

| Date       | Short-Term View/Catalyst Watch | No View |
| ---------- | ------------------------------ | ------- |
| J 2024     | ~2,500                         | ~2,500  |
| J 2025     | ~2,500                         | ~3,000  |
| A 2026     | ~2,500                         | ~3,500  |
| D 2026     | ~3,000                         | ~4,000  |
| M 2026     | ~4,000                         | ~6,500  |
</details>

<table><tr><td></td><td>Date</td><td>Action</td><td>ExpectedDirection</td><td>Duration</td><td>ClosingPrice</td></tr><tr><td>1</td><td>29-May-24 22:05:00</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>2,945</td></tr><tr><td>2</td><td>28-Jun-24 12:05:20</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>3,322</td></tr></table>

CW - Catalyst Watch, STV - Short-Term View

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>3</td><td>17-Aug-25 22:35:00</td><td>Add STV</td><td>Upside</td><td>90 Days</td><td>2,400</td></tr><tr><td>4</td><td>16-Nov-25 20:59:32</td><td>Remove STV</td><td>Upside</td><td>90 Days</td><td>3,109</td></tr></table>

Rating/target price changes above reflect Eastern Time

Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from Murata in the past 12 months.

Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: Murata.

Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, non-securities-related: Murata.

Analysts' compensation is determined by Citi management and Citi's senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the “Firm”). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.

For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.

Unless stated otherwise neither the Research Analyst nor any member of their team has viewed the material operations of the Companies for which an investment view has been provided within the past 12 months.

For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product ("the Product"), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013, Attention: Legal/Compliance [E6WYB6412478]. In addition, the same important disclosures, with the exception of the Valuation and Risk assessments and historical disclosures, are contained on the Firm's disclosure website at https://www.citivelocity.com/cvr/eppublic/citi\_research\_disclosures. Valuation and Risk assessments can be found in the text of the most recent research note/report regarding the subject company. Pursuant to the Market Abuse Regulation a history of all Citi recommendations published during the preceding 12-month period can be accessed via Citi Velocity (https://www.citivelocity.com/cv2) or your standard distribution portal. Historical disclosures (for up to the past three years) will be provided upon request.

Citi Equity Ratings Distribution 

<table><tr><td></td><td colspan="3">12 Month Rating</td><td colspan="3">Catalyst Watch</td></tr><tr><td>Data current as of 01 Apr 2026</td><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Citi Global Fundamental Coverage (Neutral=Hold)</td><td>61%</td><td>32%</td><td>8%</td><td>37%</td><td>47%</td><td>16%</td></tr><tr><td>% of companies in each rating category that are investment banking clients</td><td>38%</td><td>41%</td><td>28%</td><td>42%</td><td>37%</td><td>36%</td></tr></table>

# Guide to Citi Fundamental Research Investment Ratings:

Citi stock recommendations include an investment rating and an optional risk rating to highlight high risk stocks.

Risk rating takes into account both price volatility and fundamental criteria. Stocks will either have no risk rating or a High risk rating assigned.

Investment Ratings: Citi investment ratings are Buy, Neutral and Sell. Our ratings are a function of analyst expectations of expected total return ("ETR") and risk. ETR is the sum of the forecast price appreciation (or depreciation) plus the dividend yield for a stock within the next 12 months. The target price is based on a 12 month time horizon. The Investment rating definitions are: Buy (1) ETR of 15% or more or 25% or more for High risk stocks; and Sell (3) for negative ETR. Any covered stock not assigned a Buy or a Sell is a Neutral (2). For stocks rated Neutral (2), if an analyst believes that there are insufficient valuation drivers and/or investment catalysts to derive a positive or negative investment view, they may elect with the approval of Citi management not to assign a target price and, thus, not derive an ETR. Citi may suspend its rating and target price and assign "Rating Suspended" status for regulatory and/or internal policy reasons. Citi may also suspend its rating and target price and assign "Under Review" status for other exceptional circumstances (e.g. lack of information critical to the analyst's thesis, trading suspension) affecting the company and/or trading in the company's securities. In both such situations, the rating and target price will show as “—” and “-” respectively in the rating history price chart. Prior to 11 April 2022 Citi assigned "Under Review" status to both situations and prior to 11 Nov 2020 only in exceptional circumstances. As soon as practically possible, the analyst will publish a note re-establishing a rating and investment thesis. Investment ratings are determined by the ranges described above at the time of initiation of coverage, a change in investment and/or risk rating, or a change in target price (subject to limited management discretion). At times, the expected total returns may fall outside of these ranges because of market price movements and/or other short-term volatility or trading patterns. Such interim deviations will be permitted but will become subject to review by Research Management. Your decision to buy or sell a security should be based upon your personal investment objectives and should be made only after evaluating the stock's expected performance and risk.

# Catalyst Watch/Short Term Views ("STV") Ratings Disclosure:

Catalyst Watch and STV Upside/Downside calls: Citi may also include a Catalyst Watch or STV Upside or Downside call to indicate the analyst expects the share price to rise (fall) in absolute terms over a specified period of 30 or 90 days in reaction to one or more specific near-term catalysts or events impacting the company or the market. A Catalyst Watch will be published when Analyst confidence is high that an impact to share price will occur; it will be a STV when confidence level is moderate. A Catalyst Watch or STV Upside/Downside call will automatically expire at the end of the specified 30/90 day period. The Catalyst Watch will also be automatically removed if share price performance (calculated at market close) exceeds

15% against the direction of the call (unless over-ridden by the analyst). The analyst may also remove a Catalyst Watch or STV call prior to the end of the specified period in a published resear

[中间内容因长度限制已省略]

ceipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
