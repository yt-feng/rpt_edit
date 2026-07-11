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
09 Jul 2026 11:45:50 ET | 12 pages

# China Battery Materials

## Lithium into 2nd week of July – Our read to the sell off this week

## CITI'S TAKE

Lithium price and equity names meltdown in the last two days, on (1) JXW resumption, and (2) potential proposal on LFP cathode capacity control ahead. Our read follows – (1) We expect CATL to give investors more colour on the JXW mine resumption, new battery capacity timeline, and full year battery output/shipment target in the upcoming results call of which the impact to lithium fundamental we estimate to skew to the positive, (2) we see immaterial impact from the potential capacity control proposal on LFP cathode ahead, as this echoes to our previous anti-involution call (see note) and the timeline remains uncertain, and (3) we await more details on JXW resumption (i.e. scale, cost, and etc), but we believe market has priced in most of the negative in the last few weeks.

Weekly wrap-up: Lithium ASP was in the downtrend WoW during last week. Among that, Li2CO3 and LiOH ASP is quoted at Rmb158.5k/t and Rmb142.5k/t as of 9th July respectively, vs Rmb162.5k/t and Rmb158.5k/t as of 2nd July. Production wise, China Li2CO3 production was -3% WoW at 24,855 tons last week. Among that, output from brine, lepidolite, spodumene, and recycle was +2%/-20%/-3%/+1% WoW respectively. Inventory wise, total inventory of Li2CO3 came in at 92,236 tons this week (-2% WoW / -2,338 tons WoW). Within that, inventory of downstream players (mainly cathode makers), smelters, and others (mainly battery makers and traders) were -2%, -9%, -8% WoW to 50,339 tons, 12,415 tons, and 29,482 tons respectively.

Jack Shang, CFA $^{AC}$ +852-2501-2441
jack.shang@citi.com

Anna Wang
+852-2501-2739
anna.d.wang@citi.com

Jimmy Feng
+852-2501-7588
jimmy.feng@citi.com

Cynthia Wu
+852-2868-7813
cynthia.d.wu@citi.com

## Shreyas Madabushi

+91-22-4277-5048
shreyas.madabushi@citi.com

Figure 1. Lithium carbonate monthly inventory  
![](images/82fe21562474c5b3c99b874dba5e3e4721c456bfcf7d2ede878a183c5d0a30b8.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, SMM

Figure 2. Lithium carbonate weekly inventory  
![](images/58468feb2c9fff78605a8b77d2602ebfce3f441ba7afb99ec2a6e49584b73b7d.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, SMM

Figure 3. Spread of battery-grade LC (assume 1M inventory)  
![](images/9d03a88b3f22ab8b82d3f3fd633c100b94e614b83757729fc7c0c5a24f3f642d.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, SMM

Figure 4. Spread of battery-grade LC (assume 1M inventory)  
![](images/39bacdc1e17a72afddd32a1ef9eff16b465c34633f8e0dfeb741e96dd91ff275.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, SMM

Figure 5. Lithium carbonate monthly production  
![](images/6fad36d44434319368ed1ae53d76da319657ed45b4a932a6ef7b74e067585aed.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, SMM

Figure 6. Lithium carbonate weekly production  
![](images/cb75ef5dc8729d107f3a67d373d7055900ba5a36f90596dcea9b2327ede7fc5c.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, SMM

## CATL

(3750.HK; HK\$637.5; 1; 09 Jul 26; 16:10)

## Valuation

We value CATL-H at HK\$888/share, based on 28% premium, the historical H/A premium for CATL, on our A-share TP of Rmb603/sh. Our TP for the A-share is based on 17.5x 2026E EV/EBITDA, 0.25x SD above the stock's historical average since the listing of the A-share. We opt for an EV/EBITDA approach as it eliminates changes in capital structure. Our target price for H share implies 34.3x 26E P/E and 8.7x 26E P/B.

## Risks

Our Quant model rates the CATL-H stock High Risk for its short trading history, which we believe is unwarranted given the company's established history as an operating company and given the A-share's long history. Downside risks that could mean the CATL-H shares fail to achieve our target price include: 1) lower-than-expected EV demand; 2) competition in the EV battery market turns fierce, resulting in a market share for CATL that is lower than our expectations; and 3) higher-than-expected raw material costs.

## CATL

(300750.SZ; Rmb375.5; 1; 09 Jul 26; 15:00)

## Valuation

We value CATL-A at Rmb603/share based on 17.5x 2026E EV/EBITDA, 0.25xSD above the stock's historical average since listing. We opt for an EV/EBITDA approach as it eliminates changes in capital structure. Our target price implies 26.8x 26E P/E and 6.8x 26E P/B.

## Risks

Downside risks that could mean the CATL-A shares fail to achieve our target price include: 1) lower-than-expected EV demand; 2) competition in the EV battery market turns fierce, resulting in a market share for CATL that is lower than our expectations; and 3) higher-than-expected raw material costs.

<table><tr><td>Date122-May-25 05:00:03</td><td>Rating*1</td><td>Target Price*425.00</td><td>Closing Price326.98</td></tr></table>

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

![](images/3d0fe1ebc5bd0aeb3340dc44ef4c7ec121a8c8a8cb3c0d2177f07ac3df376854.jpg)  
\*Indicates Change  
Rating/target price changes above reflect Eastern Time

## CATL (300750.SZ)

Ratings and Target Price History
Fundamental Research

Analyst: Jack Shang, CFA

![](images/88fc697785dd01449bebc3231edc4fe089af288b9df6153450f5e19e5a4495e6.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>28-Jul-23 03:11:29</td><td>1</td><td>*329.00</td><td>230.05</td></tr><tr><td>2</td><td>19-Oct-23 13:49:14</td><td>1</td><td>*313.00</td><td>182.70</td></tr><tr><td>3</td><td>22-Feb-24 05:35:55</td><td>1</td><td>*287.00</td><td>160.35</td></tr><tr><td>4</td><td>15-Mar-24 13:30:59</td><td>1</td><td>*292.00</td><td>181.00</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>5</td><td>07-Oct-24 09:38:25</td><td>1</td><td>*328.00</td><td>251.89</td></tr><tr><td>6</td><td>18-Oct-24 13:40:59</td><td>1</td><td>*362.00</td><td>249.89</td></tr><tr><td>7</td><td>22-May-25 05:00:03</td><td>1</td><td>*391.00</td><td>270.37</td></tr><tr><td>8</td><td>30-Jul-25 13:54:08</td><td>1</td><td>*404.00</td><td>277.09</td></tr></table>

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>9</td><td>29-Sep-25 13:29:31</td><td>1</td><td>*571.00</td><td>397.37</td></tr><tr><td>10</td><td>09-Mar-26 12:56:26</td><td>1</td><td>*576.00</td><td>357.50</td></tr><tr><td>11</td><td>04-Jun-26 09:26:43</td><td>1</td><td>*603.00</td><td>408.20</td></tr></table>

Rating/target price changes above reflect Eastern Time

<table><tr><td>Date</td><td>Action</td><td>ExpectedDirection</td><td>Duration</td><td>ClosingPrice</td><td></td><td>Date</td><td>Action</td><td>ExpectedDirection</td><td>Duration</td><td>ClosingPrice</td></tr><tr><td>27-Jan-26 07:40:16</td><td>Add CW</td><td>Downside</td><td>30 Days</td><td>463.00</td><td>2</td><td>24-Feb-26 02:14:39</td><td>Remove CW</td><td>Downside</td><td>30 Days</td><td>521.00</td></tr></table>

![](images/b8b2745dff1b5146762a743e8ba9e910d576a4778750f814a1bb85fa6ca08488.jpg)  
CW - Catalyst Watch, STV - Short-Term View  
Rating/target price changes above reflect Eastern Time

![](images/6ecb756ba955428b5abec32703e6e9da0c89bf685924ab23559d456680da08da.jpg)

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>1</td><td>26-Oct-23 22:51:21</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>178.07</td></tr><tr><td>2</td><td>26-Nov-23 11:05:17</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>175.00</td></tr><tr><td>3</td><td>22-Feb-24 01:07:19</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>160.35</td></tr><tr><td>4</td><td>22-Mar-24 12:04:11</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>186.51</td></tr></table>

CW - Catalyst Watch, STV - Short-Term View

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>5</td><td>25-Jul-24 02:11:04</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>187.73</td></tr><tr><td>6</td><td>23-Aug-24 14:22:15</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>181.80</td></tr><tr><td>7</td><td>07-Oct-24 05:38:25</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>251.89</td></tr><tr><td>8</td><td>06-Nov-24 21:29:06</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>256.50</td></tr></table>

<table><tr><td colspan="2">Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>9</td><td>13-Nov-24 05:12:17</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>282.00</td></tr><tr><td>10</td><td>13-Dec-24 12:29:12</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>267.03</td></tr><tr><td>11</td><td>27-Jan-26 07:40:16</td><td>Add CW</td><td>Downside</td><td>30 Days</td><td>339.40</td></tr><tr><td>12</td><td>26-Feb-26 21:27:37</td><td>Remove CW</td><td>Downside</td><td>30 Days</td><td>346.00</td></tr></table>

Rating/target price changes above reflect Eastern Time

The Firm has made a market in the publicly traded equity securities of Contemporary Amperex Technology Co Ltd on at least one occasion since 1 Jan 2025.

<table><tr><td>Citi Global Markets Inc. or its affiliates expects to receive or intends to seek, within the next three months, compensation for investment banking services from CATL.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from CATL in the past 12 months.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as investment banking client(s): CATL.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: CATL.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, non-securities-related: CATL.</td></tr><tr><td>Citi Global Markets Inc. and/or its affiliates has a significant financial interest in relation to CATL. (For an explanation of the determination of significant financial interest, please refer to the policy for managing conflicts of interest which can be found at www.citiVelocity.com.)</td></tr><tr><td>Analysts’ compensation is determined by Citi management and Citi’s senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the “Firm”). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.</td></tr><tr><td>For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may</td></tr></table>

engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.

The Firm is a market maker in the publicly traded equity securities of CATL.

Citi Equity Ratings Distribution

<table><tr><td></td><td colspan="3">12 Month Rating</td><td colspan="3">Catalyst Watch</td></tr><tr><td>Data current as of 01 Jul 2026</td><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Citi Global Fundamental Coverage (Neutral=Hold)</td><td>61%</td><td>32%</td><td>7%</td><td>36%</td><td>48%</td><td>16%</td></tr><tr><td>% of companies in each rating category that are investment banking clients</td><td>38%</td><td>42%</td><td>27%</td><td>42%</td><td>37%</td><td>36%</td></tr></table>

Guide to Citi Fundamental Research Investment Ratings:

Citi stock recommendations include an investment rating and an optional risk rating to highlight high risk stocks. Risk rating takes into account both price volatility and fundamental criteria. Stocks will either have no risk rating or a High risk rating assigned.

Investment Ratings: Citi investment ratings are Buy, Neutral and Sell. Our ratings are a function of analyst expectations of expected total return ("ETR") and risk. ETR is the sum of the forecast price appreciation (or depreciation) plus the dividend yield for a stock within the next 12 months. The target price is based on a 12 month time horizon. The Investment rating definitions are: Buy (1) ETR of 15% or more or 25% or more for High risk stocks; and Sell (3) for negative ETR. Any covered stock not assigned a Buy or a Sell is a Neutral (2). For stocks rated Neutral (2), if an analyst believes that there are insufficient valuation drivers and/or investment catalysts to derive a positive or negative investment view, they may elect with the approval of Citi management not to assign a target price and, thus, not derive an ETR. Citi may suspend its rating and target price and assign "Rating Suspended" status for regulatory and/or internal policy reasons. Citi may also suspend its rating and target price and assign "Under Review" status for other exceptional circumstances (e.g. lack of information critical to the analyst's thesis, trading suspension) affecting the company and/or trading in the company's sec

[中间内容因长度限制已省略]

eipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality,

accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
