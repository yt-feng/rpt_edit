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
# ASML Holding NV (ASML.AS)

# AI Demand Extends Visibility into 2028; Raising TP to €2,200

## CITI'S TAKE

ASML's Q2 reinforces our view that the AI-driven semi investment cycle remains in its early stages, with demand strength across both advanced logic and memory, and meaningful 2027 and 2028 orders already in hand. The combination of rising lithography intensity, accelerating memory capex, improving pricing power, and increasing customer visibility supports a multi-year growth outlook, prompting us to materially raise estimates and increase TP to €2,200 while retaining Buy rating and Focus List inclusion.

Momentum continues into 2027 and 2028 — ASML continues to benefit from strong AI-driven semiconductor demand and improving customer visibility, driving a significant increase to 2026 guidance. Leading-edge foundry expansion and strong HBM/DRAM-driven memory capex are supporting EUV demand. ASML expects logic sales growth of over 25% and memory growth of over 75% this year.

Order visibility has improved dramatically — ASML indicated 2027 Low-NA EUV capacity is nearly fully booked and is already receiving meaningful 2028 orders, supporting plans to expand Low-NA EUV and DUV capacity by 30% in 2027 with a further 30% increases possible in 2028. We now forecast 67 Low-NA EUV and 130 DUV immersion units in 2026, rising to 86 / 170 in 2027, with a further increase in 2028. Our system sales forecasts move up 16–45% in 2026–28 driven by the higher unit forecasts, particularly from memory players, coupled with higher ASPs.

Margins and pricing are improving — Tight capacity and strong demand are supportive of long-term pricing power. Management highlighted ongoing value-based pricing discussions, with further upside expected as higher-productivity EUV systems and High-NA EUV become a larger share of the mix. Combined with upgrade demand and operating leverage, this supports a positive margin outlook. High-NA progress continues as Intel confirms volume production on 18A.

Material upgrade to estimates; TP to €2,200 — We adjust our 2026–26 sales up 14–36% and EPS up 25–52% driven by our higher forecasts of Low-NA EUV and DUV units and ASP. Accordingly, our TP moves to €2,200 (from €1,675) driven by 28x PE or 1x PEG based on 2028 earnings (from 39x 2027 PE). Retain Buy and Focus List.

ASML Holding NV (EUR)

<table><tr><td>Year to 31 Dec</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Sales (€M)</td><td>28,262.9</td><td>32,667.3</td><td>44,741.9</td><td>58,849.1</td><td>73,374.6</td></tr><tr><td>Net Income (€M)</td><td>7,571.6</td><td>9,609.4</td><td>15,617.4</td><td>22,737.6</td><td>29,814.5</td></tr><tr><td>Diluted EPS (€)</td><td>19.24</td><td>24.72</td><td>40.42</td><td>59.10</td><td>78.05</td></tr><tr><td>Diluted EPS (Old) (€)</td><td>19.24</td><td>24.72</td><td>32.29</td><td>42.67</td><td>51.25</td></tr><tr><td>PE (x)</td><td>83.1</td><td>64.7</td><td>39.5</td><td>27.0</td><td>20.5</td></tr><tr><td>EV/EBITDA (x)</td><td>61.8</td><td>49.5</td><td>31.5</td><td>21.5</td><td>16.0</td></tr><tr><td>DPS (€)</td><td>6.40</td><td>7.50</td><td>8.63</td><td>9.92</td><td>11.41</td></tr><tr><td>Net Div Yield (%)</td><td>0.4</td><td>0.5</td><td>0.5</td><td>0.6</td><td>0.7</td></tr></table>

## Buy

Price (16 Jul 26 16:30) €1,598.40

Target price €2,200.00↑

Expected share price return 37.6%

Expected dividend yield 0.4%

Expected total return 38.1%

Market Cap €620,415M

## Price Performance

## (RIC: ASML.AS, BB: ASML NA)

![](images/ee17334ece2a0f7889ec347612d6c95984bfe157bb8fbef783f3a02f69cb63f9.jpg)

Andrew M. Gardiner, CFA $^{AC}$ +44-20-7986-4206
andrew.gardiner@citi.com

Pavan Daswani, CFA
+44-20-7986-6889
pavan.daswani@citi.com € 1,300.00
▼19% Downside

Figure 1. Key changes in our estimates

<table><tr><td>Dec FY, € m</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td></td><td>New</td><td>Old</td><td>Δ%</td><td>Citi</td><td>Old</td><td>Δ%</td><td>New</td><td>Old</td><td>Δ%</td></tr><tr><td>Group revenue</td><td>44,742</td><td>39,262</td><td>14%</td><td>58,849</td><td>47,633</td><td>24%</td><td>73,375</td><td>53,942</td><td>36%</td></tr><tr><td>Operating Income</td><td>18304</td><td>14401</td><td>27%</td><td>26782</td><td>19029</td><td>41%</td><td>35182</td><td>22753</td><td>55%</td></tr><tr><td>Diluted EPS (€)</td><td>40.42</td><td>32.29</td><td>25%</td><td>59.10</td><td>42.67</td><td>38%</td><td>78.05</td><td>51.25</td><td>52%</td></tr><tr><td>Other KPIs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Net System Sales</td><td>34,280</td><td>29,564</td><td>16%</td><td>46,521</td><td>36,188</td><td>29%</td><td>59,506</td><td>41,066</td><td>45%</td></tr><tr><td>Installed Base Management</td><td>10,462</td><td>9,698</td><td>8%</td><td>12,328</td><td>11,445</td><td>8%</td><td>13,869</td><td>12,876</td><td>8%</td></tr><tr><td>Gross margin (%)</td><td>55.0%</td><td>52.1%</td><td>291 bps</td><td>56.6%</td><td>52.9%</td><td>370 bps</td><td>57.6%</td><td>54.6%</td><td>303 bps</td></tr></table>

## Bull/Bear: ASML Holding NV (ASML.AS)

![](images/144588c0862b5372f1c80e40510378576cc1a5278512e30d1bced4dccd491435.jpg)  
Spread 81pp Current Price and expected returns (upside/downside) as of 16 Jul 2026

## BULL Assumptions

![](images/c976edc1516be1c678264f2fbee49b44b1713143b4b153d12a9c1055b564be40.jpg)

\- Macro backdrop: Inflation proves less entrenched and moderation of banking stresses

• CY26E revenue: >30% growth in logic system sales and >100% growth in memory system sales

\- \~1.3x PEG based on FY28 earnings

![](images/1945ed56a8d56c935ca67fe490bee4e28ac81d88d92f8c0669b37b7515946216.jpg)

## BASE Assumptions

\- Macro backdrop: A series of rolling country-level recessions and moderation of banking stresses

\- Base case revenue and EPS aligned with our underlying financial model

## BEAR Assumptions

![](images/ff6384cb63e76b05ac74725a310a1ec4198af5317a8acafef3510572525ddb24.jpg)

\- Macro backdrop: Elevated concerns associated with banking stresses resulting in meaningful moderation of global GDP growth

• CY26 revenue: limited growth in logic system sales and memory system sales

\- \~0.6x PEG based on FY28 earnings

## ASML Holding NV

## Company description

ASML develops, manufactures, and markets photolithography projection systems used in integrated circuit semiconductor manufacturing. Since its founding in 1984, ASML has grown rapidly to become the world's top 3 semiconductor equipment company and the largest manufacturer of photolithography scanner systems.

## Investment strategy

Our Buy recommendation on ASML is based on three premises: 1) faster digital transformation, and in particular the rise of Artificial Intelligence of Things (AIoT), driving increased demand; 2) higher operational profitability, primarily as EUV matures and its share becomes significant across both systems and installed base management; and 3) stronger computational platform of semiconductor fabrication leveraging Big Data.

## Valuation

We value ASML using a 28x 2028 or 1x PEG based on FY28 earnings, in line with other strong growth stocks in our coverage, which leads to our target price of EUR 2,200. We continue to have conviction in ASML's long-term growth outlook, as evident in our forecast of a $30\%$ CAGR in EPS through 2030E. Given our strong multi-year growth forecast for ASML, we look further out than 2026 to capture the growth potential. We think this approach better captures its long-term exposure to artificial intelligence, semiconductor capex, and other structural growth areas.

## Risks

We highlight the following risk factors for ASML. If the impact of these risk factors is more or less negative than we anticipate, the share price could deviate significantly from our target price:

Technological: Challenges in development of EUV technology could result in delays and lower margins.

Competition: A gain/loss in lithography and/or process control market share would result in upside/downside risk to our estimates.

Customer Risk: ASML derives a significant share of its revenues from a few large customers, and an increase/cut in their capex could result in risk to our estimates.

Macroeconomic: A weak macroeconomic environment and/or escalation in geopolitical tensions resulting in subdued semiconductor growth/increase in cadence could cause downside to our estimates.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

## ASML Holding NV (ASML.AS)

Analyst: Andrew M. Gardiner, CFA

![](images/ba493239f0719cf6dbb9e294f03de522a044d51f128684ab522ceb2c0ec00462.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>15-Dec-23 00:00:00</td><td>1</td><td>*900.00</td><td>694.70</td></tr><tr><td>2</td><td>12-Apr-24 00:00:00</td><td>1</td><td>*1,250.00</td><td>907.50</td></tr><tr><td>3</td><td>18-Sep-24 00:00:00</td><td>1</td><td>*1,150.00</td><td>715.00</td></tr><tr><td>4</td><td>17-Oct-24 01:07:32</td><td>1</td><td>*930.00</td><td>634.20</td></tr></table>

\*Indicates Change

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td></td><td>5 17-Apr-25 11:23:20</td><td>1</td><td>*860.00</td><td>564.20</td></tr><tr><td></td><td>6 16-Jul-25 18:41:06</td><td>1</td><td>*825.00</td><td>625.80</td></tr><tr><td></td><td>7 07-Oct-25 00:06:11</td><td>1</td><td>*1,050.00</td><td>874.80</td></tr><tr><td></td><td>8 10-Dec-25 00:00:00</td><td>1</td><td>*1,200.00</td><td>946.00</td></tr></table>

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>9</td><td>20-Jan-26 00:00:00</td><td>1</td><td>*1,400.00</td><td>1,140.00</td></tr><tr><td>10</td><td>29-Jan-26 00:00:00</td><td>1</td><td>*1,600.00</td><td>1,192.00</td></tr><tr><td>11</td><td>16-Apr-26 00:00:00</td><td>1</td><td>*1,675.00</td><td>1,222.60</td></tr></table>

Rating/target price changes above reflect Eastern Time

![](images/71542513cd071a6e127ecd94b5af4ef77dd9c215c95a0f3c8f5c7b3f4baeffd4.jpg)

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>1</td><td>15-Oct-23 21:48:46</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>573.60</td></tr><tr><td>2</td><td>15-Nov-23 05:34:57</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>627.80</td></tr><tr><td>3</td><td>21-Jan-24 19:00:00</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>686.30</td></tr><tr><td>4</td><td>21-Feb-24 05:35:09</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>834.00</td></tr><tr><td>5</td><td>11-Apr-24 20:00:00</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>909.10</td></tr><tr><td>6</td><td>10-May-24 12:08:52</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>864.50</td></tr><tr><td>7</td><td>05-Jul-24 14:09:25</td><td>Add CW</td><td>Upside</td><td>90 Days</td><td>993.00</td></tr></table>

CW - Catalyst Watch, STV - Short-Term View

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>8</td><td>30-Sep-24 23:33:40</td><td>Remove CW</td><td>Upside</td><td>90 Days</td><td>745.60</td></tr><tr><td>9</td><td>01-Oct-24 20:00:00</td><td>Add CW</td><td>Upside</td><td>90 Days</td><td>741.80</td></tr><tr><td>10</td><td>15-Oct-24 07:27:39</td><td>Remove CW</td><td>Upside</td><td>90 Days</td><td>668.10</td></tr><tr><td>11</td><td>14-Nov-24 20:44:40</td><td>Add STV</td><td>Upside</td><td>90 Days</td><td>671.60</td></tr><tr><td>12</td><td>29-Jan-25 20:23:53</td><td>Remove STV</td><td>Upside</td><td>90 Days</td><td>682.50</td></tr><tr><td>13</td><td>30-Mar-25 21:17:09</td><td>Add CW</td><td>Upside</td><td>90 Days</td><td>625.60</td></tr><tr><td>14</td><td>17-Apr-25 07:23:20</td><td>Remove CW</td><td>Upside</td><td>90 Days</td><td>564.20</td></tr></table>

<table><tr><td rowspan="2" colspan="2">Date</td><td>Action</td><td>ExpectedDirection</td><td>Duration</td><td>ClosingPrice</td></tr><tr><td>Add STV</td><td>Upside</td><td>90 Days</td><td>677.60</td></tr><tr><td>15</td><td>02-Jul-25 20:00:00</td><td></td><td></td><td></td><td></td></tr><tr><td>16</td><td>16-Jul-25 14:41:06</td><td>Remove STV</td><td>Upside</td><td>90 Days</td><td>625.80</td></tr><tr><td>17</td><td>06-Oct-25 20:06:11</td><td>Add STV</td><td>Upside</td><td>30 Days</td><td>897.30</td></tr><tr><td>18</td><td>06-Nov-25 05:35:31</td><td>Remove STV</td><td>Upside</td><td>30 Days</td><td>895.30</td></tr><tr><td>19</td><td>28-Jan-26 19:00:00</td><td>Add STV</td><td>Upside</td><td>90 Days</td><td>1,194.40</td></tr><tr><td>20</td><td>06-Apr-26 20:00:00</td><td>Remove STV</td><td>Upside</td><td>90 Days</td><td>1,161.00</td></tr></table>

Rating/target price changes above reflect Eastern Time

Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from ASML Holding NV in the past 12 months.

Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: ASML Holding NV.

Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, non-securities-related: ASML Holding NV.

Citi Global Markets Inc. and/or its affiliates has a significant financial interest in relation to ASML Holding NV. (For an explanation of the determination of significant financial interest, please refer to the policy for managing conflicts of interest which can be found at www.citiVelocity.com.)

Analysts' compensation is determined by Citi management and Citi's senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the "Firm"). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of cove

[中间内容因长度限制已省略]

eipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality,

accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the "Product"), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
