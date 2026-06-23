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
# Global Robot Vacuum

# Near-term EU robot mower tariff risk deferred and strong 618 performance favor Ecovacs

## CITI'S TAKE

Two developments this week skew positive for Ecovacs, in Citi's view. First, the EU declined to impose provisional anti-dumping duties on China robot lawn mowers and continued the case towards a definitive ruling on June 19, which lifts a near-term overhang on the segment where Ecovacs (with one of Europe's best-selling robotic mowers) is the most exposed in our robot vacuum coverage. Second, Ecovacs Group reported Rmb4.02bn of 618 all-channel GMV (up $23\%$ YoY) per its own press release, which we believe is better than market's expectations, led by premium robot vacuums, window-cleaning robots and Tineco floor washers. We continue to prefer Ecovacs (603486.SS, Buy) over Roborock (688169.SS, Neutral).

EU robot lawn mower anti-dumping investigation results deferral — The European Commission on 19 June published its initial-stage conclusion and declined to levy provisional anti-dumping duties on China-made robot lawn mowers with the investigation continuing, citing the difficulty of comparing cost and pricing across smart mowers. While the definitive ruling is expected by early-2027, we see such action defers near-term tariff risk for Ecovacs, which has one of Europe's best-selling robot mowers.

Ecovacs' 618 performance — Per Ecovacs' 618 press release (1 May to 18 June), it posted Rmb4.02bn of all-channel GMV (up 23% YoY) in China. Specifically, the T90 robot vacuum series sold 290k units and Tineco Floor one series sold 230k units during 618 in China. Per its press release, Ecovacs held the top share in Rmb4,000+ premium tier and 65%+ market share in window-cleaning robots in China. Roborock separately noted it was the No.1 robot vacuum across Tmall, JD and Douyin in category share in the 618 opening period in China, without full 618 period performance reported yet.

Vincent Young $^{\mathrm{AC}}$ +852-2501-2738 vincent.young@citi.com

Xiaopo Wei, CFA +852-2501-2472 xiaopo.wei@citi.com

## Beijing Roborock

(688169.SS; Rmb97.27; 2; 18 Jun 26; 15:00)

## Valuation

Our 12-month target price of Rmb120.80 is benchmarked to 17x 26E PE, which is the average forward PE over the past 3 years.

## Risks

Upside risks that could sustain the shares above our target price include: (1) stronger than expected global macroeconomic growth and strengthened consumer spending; (2) highly successful product launches; (3) easing industry competition; (4) reduction in tariffs between China and destination countries; (5) material weakening in Rmb; (6) lower-than-expected raw material costs.

Downside risks that could impede the shares from reaching our target price include: (1) global macroeconomic slowdown and weakened consumer spending; (2) unsuccessful product launches; (3) intensified industry competition (e.g. price competition); (4) increased tariffs between China and destination countries; (5) material strengthening in Rmb; (6) higher-than-expected raw material costs.

Any of these risk factors could cause the shares to deviate from our target price.

## Ecovacs Robotics

(603486.SS; Rmb53.08; 1; 18 Jun 26; 15:00)

## Valuation

Our target price of Rmb89.3 is benchmarked to 25x 2026E PE, a 15% premium to our target PE for Roborock, to reflect Ecovacs' better focus on capital return and profitability.

## Risks

Downside risks that could impede the shares from reaching our target price include: (1) global macroeconomic slowdown and weakened consumer spending; (2) unsuccessful product launches; (3) intensified industry competition (e.g. price competition); (4) increased tariff between China and destination countries; (5) material strengthening in Rmb; and (6) higher-than-expected raw material costs.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

## Ecovacs Robotics (603486.SS)

Analyst: Vincent Young

![](images/bbaa8de744715466944dcdc2ddc4fe49c457543a01cf3f6c5b61882d2cb9c386.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>20-Aug-24 06:16:15</td><td>*2</td><td>*37.80</td><td>36.92</td></tr><tr><td>2</td><td>03-Oct-24 05:58:59</td><td>2</td><td>*56.10</td><td>51.21</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>3</td><td>15-Jul-25 00:34:13</td><td>*1</td><td>*87.10</td><td>70.43</td></tr><tr><td>4</td><td>14-Aug-25 21:49:41</td><td>1</td><td>*127.70</td><td>89.00</td></tr></table>

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>5</td><td>12-Dec-25 04:29:29</td><td>1</td><td>*102.20</td><td>79.60</td></tr><tr><td>6</td><td>14-Apr-26 02:46:32</td><td>1</td><td>*89.30</td><td>63.11</td></tr></table>

Rating/target price changes above reflect Eastern Time

## Beijing Roborock (688169.SS)

Ratings and Target Price History
Fundamental Research

Analyst: Vincent Young

![](images/6ff7e72a4ba952133be222aa071bb3f45d01e5634758ae542237829f96d94d4d.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>20-Aug-24 06:16:15</td><td>*1</td><td>*212.64</td><td>142.77</td></tr><tr><td>2</td><td>03-Oct-24 05:58:59</td><td>1</td><td>*320.64</td><td>198.51</td></tr><tr><td>3</td><td>03-Nov-24 19:07:22</td><td>1</td><td>*239.79</td><td>160.31</td></tr><tr><td>4</td><td>13-Feb-25 04:02:21</td><td>1</td><td>*224.00</td><td>174.96</td></tr></table>

\*Indicates Change

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>5</td><td>19-Jun-25 10:02:24</td><td>1</td><td>*181.71</td><td>148.93</td></tr><tr><td>6</td><td>24-Jun-25 12:05:12</td><td>1</td><td>*181.70</td><td>143.75</td></tr><tr><td>7</td><td>14-Aug-25 21:49:41</td><td>1</td><td>*212.10</td><td>175.86</td></tr><tr><td>8</td><td>23-Oct-25 06:47:03</td><td>1</td><td>*241.50</td><td>183.80</td></tr></table>

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>9</td><td>20-Nov-25 05:44:11</td><td>1</td><td>*193.20</td><td>160.73</td></tr><tr><td>10</td><td>13-Jan-26 02:56:31</td><td>1</td><td>*183.10</td><td>158.53</td></tr><tr><td>11</td><td>15-Apr-26 08:01:26</td><td>*2</td><td>*120.80</td><td>113.62</td></tr></table>

Rating/target price changes above reflect Eastern Time

<table><tr><td colspan="2">Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>1</td><td>03-Nov-24 14:07:22</td><td>Add STV</td><td>Downside</td><td>30 Days</td><td>160.31</td></tr><tr><td>2</td><td>03-Dec-24 21:28:13</td><td>Remove STV</td><td>Downside</td><td>30 Days</td><td>158.96</td></tr><tr><td>3</td><td>27-Feb-25 10:55:18</td><td>Add STV</td><td>Downside</td><td>30 Days</td><td>181.63</td></tr><tr><td>4</td><td>28-Mar-25 14:14:17</td><td>Remove STV</td><td>Downside</td><td>30 Days</td><td>175.90</td></tr></table>

Beijing Roborock (688169.SS)

Short-Term View/Catalyst Watch Research

![](images/a458cd93fe400a7d7a4ae7a599e593b2a7eca99982f39be5ee2d388e389733a9.jpg)  
CW - Catalyst Watch, STV - Short-Term View  
Rating/target price changes above reflect Eastern Time

![](images/2ec82f02a57a54ba2339e0d59ac334677d9e85c215ea7a6d89cb793702772442.jpg)

<table><tr><td rowspan="2" colspan="2">Date</td><td rowspan="2">Action</td><td rowspan="2">ExpectedDirection</td><td colspan="2">ClosingPrice</td><td rowspan="2" colspan="2">Date</td><td rowspan="2">ExpectedDirection</td><td rowspan="2" colspan="2">ClosingPrice</td><td rowspan="2" colspan="2">Date</td><td rowspan="2">ExpectedDirection</td><td rowspan="2" colspan="2">ClosingPrice</td></tr><tr><td>Duration</td><td>30 Days</td></tr><tr><td>1</td><td>21-Oct-24 00:10:21</td><td>Add CW</td><td>Upside</td><td>53.05</td><td></td><td>14-Jul-25 20:34:13</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>64.03</td><td>13-Apr-26 22:46:32</td><td>Add STV</td><td>Upside</td><td>30 Days</td><td>62.68</td></tr><tr><td>2</td><td>20-Nov-24 21:28:28</td><td>Remove CW</td><td>Upside</td><td>48.38</td><td></td><td>05-Aug-25 18:46:32</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>87.70</td><td>14-May-26 23:28:49</td><td>Remove STV</td><td>Upside</td><td>30 Days</td><td>61.90</td></tr></table>

CW - Catalyst Watch, STV - Short-Term View  
Rating/target price changes above reflect Eastern Time

Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from Beijing Roborock in the past 12 months.

Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: Beijing Roborock.

Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, non-securities-related: Beijing Roborock.

Analysts' compensation is determined by Citi management and Citi's senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the "Firm"). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.

For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.

Unless stated otherwise neither the Research Analyst nor any member of their team has viewed the material operations of the Companies for which an investment view has been provided within the past 12 months.

For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product ("the Product"), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013, Attention: Legal/Compliance [E6WYB6412478]. In addition, the same important disclosures, with the exception of the Valuation and Risk assessments and historical disclosures, are contained on the Firm's disclosure website at https://www.citivelocity.com/cvr/eppublic/citi\_research\_disclosures. Valuation and Risk assessments can be found in the text of the most recent research note/report regarding the subject company. Pursuant to the Market Abuse Regulation a history of all Citi recommendations published during the preceding 12-month period can be accessed via Citi Velocity (https://www.citivelocity.com/cv2) or your standard distribution portal. Historical disclosures (for up to the past three years) will be provided upon request.

<table><tr><td>Citi Global Markets Asia Limited</td><td>Xiaopo Wei, CFA; Vincent Young</td></tr></table>

Citi Equity Ratings Distribution

<table><tr><td></td><td colspan="3">12 Month Rating</td><td colspan="3">Catalyst Watch</td></tr><tr><td>Data current as of 01 Apr 2026</td><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Citi Global Fundamental Coverage (Neutral=Hold)</td><td>61%</td><td>32%</td><td>8%</td><td>37%</td><td>47%</td><td>16%</td></tr><tr><td>% of companies in each rating category that are investment banking clients</td><td>38%</td><td>41%</td><td>28%</td><td>42%</td><td>37%</td><td>36%</td></tr></table>

Guide to Citi Fundamental Research Investment Ratings:

Citi stock recommendations include an investment rating and an optional risk rating to highlight high risk stocks. Risk rating takes into account both price volatility and fundamental criteria. Stocks will either have no risk rating or a High risk rating assigned.

Investment Ratings: Citi investment ratings are Buy, Neutral and Sell. Our ratings are a function of analyst expectations of expected total return ("ETR") and risk. ETR is the sum of the forecast price appreciation (or depreciation) plus the dividend yield for a stock within the next 12 months. The target price is based on a 12 month time horizon. The Investment rating definitions are: Buy (1) ETR of 15% or more or 25% or more for High risk stocks; and Sell (3) for negative ETR. Any covered stock not assigned a Buy or a Sell is a Neutral (2). For stocks rated Neutral (2), if an analyst believes that there are insufficient valuation drivers and/or investment catalysts to derive a positive or negative investment view, they may elect with the approval of Citi management not to assign a target price and, thus, not derive an ETR. Citi may suspend its rating and target price and assign "Rating Suspended" status for regulatory and/or internal policy reasons. Citi may also suspend its rating and target price and assign "Under Review" status for other exceptional circumstances (e.g. lack of information critical to the analyst's thesis, trading suspension) affecting the company and/or trading in the company's securities. In both such situations, the rating and target price will show as “—” and “-” respectively in the rating history price chart. Prior to 11 April 2022 Citi assigned "Under Review" status to both situations and prior to 11 Nov 2020 only in exceptional circumstances. As soon as practically possible, the analyst will publish a note re-establishing a rating and investment thesis. Investment ratings are determined by the ranges described above at the time of initiation of coverage, a 

[中间内容因长度限制已省略]

eipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality,

accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
