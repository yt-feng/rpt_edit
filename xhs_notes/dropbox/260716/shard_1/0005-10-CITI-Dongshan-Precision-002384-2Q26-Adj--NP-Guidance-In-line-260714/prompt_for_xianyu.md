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
# Dongshan Precision (002384.SZ)

2Q26 Adj+ NP Guidance In-line

## CITI'S TAKE

DSBJ released 2Q26 NP/Adj+ NP mid-pt guidance of Rmb1.8/1.4bn (66%/31% QoQ growth), largely in-line with CitiE/VAe of Rmb1.5/1.4bn, as well as buyside expectation of Rmb1.4-1.5bn based on our conversations with investors. We estimate that DSBJ will realize \~Rmb3.5bn (or US\$500mn) transceiver revenue and \~Rmb1bn net profit in 2Q26, with 700k 400G and 1mn 800G shipment. Along with laser capacity ramp-up, yield improvement and client expansion, we expect DSBJ could realize Rmb5.4/25.6/52.7bn AI optics net profits in 2026-2028, with total NP of Rmb8.0/29.3/59.8bn. DSBJ is currently trading at 16x 2027 CitiE EPS.

Figure 1. DSBJ 2Q26 NP Guidance

<table><tr><td colspan="2">Buy</td></tr><tr><td>Price (14 Jul 26 15:00)</td><td>Rmb260.370</td></tr><tr><td>Target price</td><td>Rmb350.000</td></tr><tr><td>Expected share price return</td><td>34.4%</td></tr><tr><td>Expected dividend yield</td><td>0.0%</td></tr><tr><td>Expected total return</td><td>34.4%</td></tr><tr><td>Market Cap</td><td>Rmb476,896MUS$70,450M</td></tr></table>

<table><tr><td colspan="2"></td><td colspan="3">2Q26</td><td colspan="2">1Q26</td><td colspan="2">2Q25</td><td colspan="2">VA Consensus</td></tr><tr><td colspan="2">Rmb m</td><td>Reported</td><td>Citi est.</td><td>Diff%</td><td>Actual</td><td>QoQ</td><td>Actual</td><td>YoY</td><td>2Q26</td><td>Diff%</td></tr><tr><td rowspan="4">NP</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>High-end</td><td>1,890</td><td>1,491</td><td>27%</td><td>1,110</td><td>70%</td><td>302</td><td>526%</td><td>1,431</td><td>32%</td></tr><tr><td>Low-end</td><td>1,790</td><td>1,491</td><td>20%</td><td>1,110</td><td>61%</td><td>302</td><td>492%</td><td>1,431</td><td>25%</td></tr><tr><td>Mid-point</td><td>1,840</td><td>1,491</td><td>23%</td><td>1,110</td><td>66%</td><td>302</td><td>509%</td><td>1,431</td><td>29%</td></tr><tr><td rowspan="4">NP, adj</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>High-end</td><td>1,441</td><td>1,491</td><td>-3%</td><td>1,059</td><td>36%</td><td>260</td><td>454%</td><td>1,431</td><td>1%</td></tr><tr><td>Low-end</td><td>1,341</td><td>1,491</td><td>-10%</td><td>1,059</td><td>27%</td><td>260</td><td>416%</td><td>1,431</td><td>-6%</td></tr><tr><td>Mid-point</td><td>1,391</td><td>1,491</td><td>-7%</td><td>1,059</td><td>31%</td><td>260</td><td>435%</td><td>1,431</td><td>-3%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.

Karen Huang $^{AC}$ +852-2501-2755
karen.xw.huang@citi.com

Source: Citi, Company Reports, Visible Alpha

Figure 2. CitiE Optics Shipment/rev/NP

<table><tr><td>Assumption</td><td>2026</td><td>2027</td><td>2028</td></tr><tr><td colspan="4">Chips</td></tr><tr><td>Delta chip capacity (w/der month units)</td><td>23</td><td>33</td><td>-43</td></tr><tr><td>Annual Production (mm)</td><td>57</td><td>3--</td><td>6.5</td></tr><tr><td colspan="4">External Sales</td></tr><tr><td>Unit</td><td></td><td>-3</td><td>4</td></tr><tr><td>ASP (US$)</td><td></td><td>3</td><td>3</td></tr><tr><td colspan="4">Note we do not move in external grid sales - 2018</td></tr><tr><td colspan="4">Transceivers</td></tr><tr><td colspan="4">Shipment (k)</td></tr><tr><td>400G</td><td>1,601</td><td>1,601</td><td>-</td></tr><tr><td>800G</td><td>5,000</td><td>21,000</td><td>22,000</td></tr><tr><td>16&quot;</td><td>201</td><td>5,000</td><td>23,000</td></tr><tr><td colspan="4">ASP (US$)</td></tr><tr><td>400G</td><td>-73</td><td>-1</td><td>-</td></tr><tr><td>800G</td><td>-401</td><td>320</td><td>258</td></tr><tr><td>16&quot;</td><td>801</td><td>-20</td><td>578</td></tr><tr><td colspan="4">Tx Yield</td></tr><tr><td>400G</td><td>801</td><td>801</td><td>801</td></tr><tr><td>800G</td><td>851+801</td><td>801</td><td>801</td></tr><tr><td>16&quot;</td><td>801</td><td>801+801</td><td>801</td></tr><tr><td colspan="4">Implied 100G EML consumption</td></tr><tr><td>400G</td><td>12</td><td>3</td><td>-</td></tr><tr><td>800G</td><td>-3</td><td>-33</td><td>-43</td></tr><tr><td>16&quot;</td><td>1</td><td>33</td><td>258</td></tr><tr><td>Total</td><td>59</td><td>199</td><td>404</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.

<table><tr><td>Rev</td><td>2026</td><td>2027</td><td>2028</td></tr><tr><td colspan="4">Chips</td></tr><tr><td>Rev mn Rmb:</td><td></td><td></td><td></td></tr><tr><td>Chips</td><td></td><td>5,945</td><td>15,156</td></tr></table>

<table><tr><td colspan="4">Transceivers</td></tr><tr><td colspan="4">Rev. mln Rmb:</td></tr><tr><td>-1,000</td><td>3,200</td><td>-77</td><td>-</td></tr><tr><td>5,000</td><td>-9,000</td><td>-8,000</td><td>55,762</td></tr><tr><td>1,877</td><td>1,800</td><td>25,200</td><td>62,768</td></tr><tr><td>Transceivers</td><td>18,400</td><td>71,774</td><td>132,518</td></tr><tr><td>Total</td><td>18,400</td><td>77,719</td><td>147,676</td></tr></table>

<table><tr><td>NP</td><td>2026</td><td>2027</td><td>2028</td></tr><tr><td colspan="4">Chips</td></tr><tr><td>NP (mm Rmb)</td><td></td><td></td><td></td></tr><tr><td>Chips</td><td></td><td>2,378</td><td>6,063</td></tr><tr><td>P*</td><td></td><td>-1</td><td>-1</td></tr></table>

<table><tr><td colspan="4">Transceivers</td></tr><tr><td colspan="4">NPmn Rmba</td></tr><tr><td>-2013</td><td></td><td></td><td></td></tr><tr><td>-2015</td><td></td><td></td><td></td></tr><tr><td>37</td><td></td><td></td><td></td></tr><tr><td>Transceivers</td><td>5,376</td><td>23,278</td><td>48,602</td></tr><tr><td>*P*</td><td>23</td><td>32</td><td>35</td></tr><tr><td>Tsa</td><td>5,376</td><td>25,656</td><td>52,668</td></tr><tr><td>*P*</td><td>23</td><td>33</td><td>33</td></tr></table>

## Source: Citi

## Bull/Bear: Dongshan Precision

![](images/3edef5476868e714ce5d4220c64203a13ad3808b2bdfd7f5b834f0e8d90b7d5a.jpg)  
Current Price and expected returns (upside/downside) as of 14 Jul 2026

## BULL Assumptions

![](images/893a9039f4002f3c63a07ce47ccad741b2e878ba8a22514da2c321031c3b6278.jpg)

\- 15x P/E to DSBJ's original biz 2026 net profit;

• 20x 2027 P/E optical transceiver biz with NPM of 35%; 60x 2027 P/E optical chip biz with NPM of 50%;

• 25x 2027 P/E AI-PCB biz with NPM of 25%.

## BASE Assumptions

![](images/c29e8c73815ac1ab47b8e2dd6faedf5a29abe0a5ff4f4ee663e576361e8a22f8.jpg)

\- 15x P/E to DSBJ's original biz 2026 net profit;

• 20x 2027 P/E optical transceiver biz with NPM of 30%; 50x 2027 P/E optical chip biz with NPM of 40%;

• 25x 2027 P/E AI-PCB biz with NPM of 20%.

## BEAR Assumptions

![](images/01f497022dec082bca39a8b74dde89d2b6afa854b6c1562fa22b916d39d80eb1.jpg)

\- 15x P/E to DSBJ's original biz 2026 net profit;

• 15x 2027 P/E optical transceiver biz with NPM of 25%; 40x 2027 P/E optical chip biz with NPM of 30%;

• 15x 2027 P/E AI-PCB biz with NPM of 15%.

## Dongshan Precision

## Valuation

We use SOTP methodology to derive our TP of Rmb350. We apply (1) 15x 26E P/E to DSBJ's original biz (past 5-year average); (2) 20x 27E P/E to the optical transceiver biz, in-line with the optical transceiver names average fwd P/E; (3) 50x 27E P/E to the optical chip biz, in-line with the optical chip names' average fwd P/E; (4) 25x to the 27E AI-PCB biz, in-line with PCB names' average fwd P/E.

## Risks

Key downside risks that could impede the stock from reaching our TP include: (1) slower-than-expected progress in modules FPC and share gain from overseas peers; (2) slower-than-expected Tesla business growth due to fierce competition in the China NEV market; (3) continued optoelectronic business loss due to weak demand and intensified competition; (4) increasing materials costs; and (5) US-China geopolitical risk.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

![](images/a85b713f3c44b0e8594fc839a341fa5f5b1d300045b8ced3bfd06d14ebe2601c.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>29-Nov-24 14:04:53</td><td>*1</td><td>*37.00</td><td>25.64</td></tr><tr><td>2</td><td>16-Sep-25 11:45:47</td><td>1</td><td>*99.00</td><td>79.71</td></tr><tr><td>3</td><td>26-Oct-25 22:42:41</td><td>1</td><td>*95.00</td><td>69.15</td></tr></table>

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>4</td><td>15-Mar-26 21:31:51</td><td>1</td><td>*148.00</td><td>110.93</td></tr><tr><td>5</td><td>21-Apr-26 21:40:41</td><td>1</td><td>*205.00</td><td>169.40</td></tr><tr><td>6</td><td>28-Apr-26 05:56:26</td><td>1</td><td>*225.00</td><td>183.90</td></tr></table>

\*Indicates Change  
Rating/target price changes above reflect Eastern Time

![](images/598b4a6a449751fd7b9d025d10d5fe04c098b1c308adc013da15a938ef889866.jpg)  
CW - Catalyst Watch, STV - Short-Term View  
Rating/target price changes above reflect Eastern Time

Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from Dongshan Precision in the past 12 months.

Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: Dongshan Precision.

Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, non-securities-related: Dongshan Precision.

Analysts' compensation is determined by Citi management and Citi's senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the "Firm"). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.

For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.

Unless stated otherwise neither the Research Analyst nor any member of their team has viewed the material operations of the Companies for which an investment view has been provided within the past 12 months.

For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product ("the Product"), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013, Attention: Legal/Compliance [E6WYB6412478]. In addition, the same important disclosures, with the exception of the Valuation and Risk assessments and historical disclosures, are contained on the Firm's disclosure website at https://www.citivelocity.com/cvr/eppublic/citi\_research\_disclosures. Valuation and Risk assessments can be found in the text of the most recent research note/report regarding the subject company. Pursuant to the Market Abuse Regulation a history of all Citi recommendations published during the preceding 12-month period can be accessed via Citi Velocity (https://www.citivelocity.com/cv2) or your standard distribution portal. Historical disclosures (for up to the past three years) will be provided upon request.

Citi Equity Ratings Distribution

<table><tr><td></td><td colspan="3">12 Month Rating</td><td colspan="3">Catalyst Watch</td></tr><tr><td>Data current as of 01 Jul 2026</td><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Citi Global Fundamental Coverage (Neutral=Hold)</td><td>61%</td><td>32%</td><td>7%</td><td>36%</td><td>48%</td><td>16%</td></tr><tr><td>% of companies in each rating category that are investment banking clients</td><td>38%</td><td>42%</td><td>27%</td><td>42%</td><td>37%</td><td>36%</td></tr></table>

Guide to Citi Fundamental Research Investment Ratings:

Citi stock recommendations include an investment rating and an optional risk rating to highlight high risk stocks. Risk rating takes into account both price volatility and fundamental criteria. Stocks will either have no risk rating or a High risk rating assigned.

Investment Ratings: Citi investment ratings are Buy, Neutral and Sell. Our ratings are a function of analyst expectations of expected total return ("ETR") and risk. ETR is the sum of the forecast price appreciation (or depreciation) plus the dividend yield for a stock within the next 12 months. The target price is based on a 12 month time horizon. The Investment rating definitions are: Buy (1) ETR of 15% or more or 25% or more for High risk stocks; and Sell (3) for negative ETR. Any covered stock not assigned a Buy or a Sell is a Neutral (2). For stocks rated Neutral (2), if an analyst believes that there are insufficient valuation drivers and/or investment catalysts to derive a positive or negative investment view, they may elect with the approval of Citi management not to assign a target price and, thus, not derive an ETR. Citi may suspend its rating and target price and assign "Rating Suspended" status for regulatory and/or internal policy reasons. Citi may also suspend its rating and target price and assign "Under Review" status for other exceptional circumstances (e.g. lack of information critical to the analyst's thesis, trading suspension) affecting the company and/or trading in the company's securities. In both such situations, the rating and target price will show as “—” and “-” respectively in the rating history price chart. Prior to 11

[中间内容因长度限制已省略]

ceipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
