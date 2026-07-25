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
# Hengli Hydraulic (601100.SS)

Ball Screw and Linear Guide Likely a Beat; Positive Humanoid Read-Through from Seenpin

## CITI'S TAKE

Our Japan machinery analyst Graeme McDonald expects THK (6481.HK) to report strong FY12/26 Q2 results on August 5, with FY12/26 OP guidance raised to around ¥40.0bn. This again echoes our takeaway of previous trip to Hengli which benefits from “spill-over” effect on ball screw and linear guide since both THK and NSK (6471.T) see tight supply in China, prolonging their delivery time to nine months. Hengli recently also indicated that their ball screw and linear guide orders have reached Rmb500mn YTD. We therefore believe that Hengli could beat its current 2026 revenue guidance of Rmb300mn. Separately, Seenpin (新剑传动) – a planetary roller screw/linear actuator supplier in Tesla Optimus supply chain – disclosed on its A-share IPO prospectus that its physical AI linear actuator GPM was 62.4%/70.3%/59.5% in 2023/24/25, leading us to believe that Hengli's humanoid robot component business will also be GPM accretive.

Ample upside to ball screw and linear guide - Differing from Japanese companies that see strong ball screw and linear guide demand from China's semiconductor and high precision manufacturing industries, Hengli benefits more from import replacement trend in China's PIMM (Plastic Injection Molding Machine) and machine tool sectors, and recently, AI and humanoid robot sectors create more machine tool demand and hence derive incremental demand for ball screw and linear guide. In addition, Hengli may also benefit from CATL's (300750.SZ/3750.HK) battery swap station buildout in China as mgmt. estimates the ball screw and linear guide dollar content per battery swap station to be \~Rmb50k. Lastly, mgmt. guided that Hengli will launch non-magnetic and extremely corrosion-resistant or high-speed ball screw and linear guide products for the semiconductor industry in 2027 to capture the 25% of the ball screw and linear guide TAM in China (see Hengli Hydraulic (601100.SS) - What's New From China Industrial & Automation Tour | Ball Screw a S-T Pain, L-T Gain).

Read-through from Seenpin - Per our industry check, Seenpin is one of the linear actuator suppliers to Tesla Optimus. According to its A-share IPO document, its physical AI linear actuator ASP stayed \~60% or above from 2023 to 2025 despite certain degree of fluctuation. We thus believe that that Hengli's planetary roller screw products for humanoid robot clients could be GPM accretive (i.e., higher than blended average GPM) business for Hengli.

Recent note - Hengli Hydraulic (601100.SS) - 2Q26E Preview: Strong Core Business but Sizable FX Loss Again; Humanoid Robot in Progress

## Buy

<table><tr><td>Price (23 Jul 26 15:00)</td><td>Rmb107.420</td></tr><tr><td>Target price</td><td>Rmb160.000</td></tr><tr><td>Expected share price return</td><td>48.9%</td></tr><tr><td>Expected dividend yield</td><td>0.6%</td></tr><tr><td>Expected total return</td><td>49.6%</td></tr><tr><td>Market Cap</td><td>Rmb144,031MUS$21,266M</td></tr></table>

Jamie Wang $^{AC}$ +852-2501-2772 jamie.ck.wang@citi.com

Eric Lau

+852-2501-2726

eric.h.lau@citi.com

See Appendix A-1 for Analyst Certification, Important Disclosures and Research Analyst Affiliations

Figure 1. Hengli: Ball screw and linear guide 2026 revenue guidance vs. order YTD  
![](images/67bb172b9a1f85b97ed8bc483bcfaf06093278dbc7cf5f97c5687034aec873c5.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, Company Reports

Figure 2. Seenpin: Physical AI linear actuator revenue and GPM, 2023-25  
![](images/27d65e89cf9d0c171848c20c2d0396b8c23934c139c4789b162b8b5067fd2756.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, Company Reports

## Bull/Bear: Hengli Hydraulic

![](images/7b526180e572deafbecfd1da473afed1edd62bcb58fbad9a815f721b45ee174e.jpg)  
Spread 93pp  
Current Price and expected returns (upside/downside) as of 23 Jul 2026

## BULL Assumptions

![](images/8bbb03da8c82f3893f38ffb0ffec6e55a324665f6d394a3a2cd2a00f44eb877f.jpg)

\- Valuation rerate on 62x 2027E P/E on strong product demand.

![](images/2771971c1f29595aebfa65bd252dea775ef3d8d6868161740d42e86a878ca4ea.jpg)

## BASE Assumptions

\- Valuation based on 50x 2027E P/E.

![](images/a601b981f2fe8a9454e9b8a8a344dfe4be5547f7d26c992554e8bdaa628f2a2a.jpg)

## BEAR Assumptions

\- Valuation derate on 38x 2027E P/E due to weaker demand.

## Hengli Hydraulic

## Valuation

Our target price for Hengli of Rmb160.0 is based on 50x 2027E P/E, which is equal to its average P/E + 0.5x SD, to reflect its strong core business and potential re-rating due to rising humanoid robot exposure.

## Risks

Key fundamental downside risks include: 1) weaker demand for excavator and non-excavator components; 2) weaker profitability of ball screw and Mexico plants due to weaker economies of production scale; and 3) lower-than-expected GPM on favorable product mix change. Any of these risk factors could cause the stock to deviate from our target price.

![](images/291e65556d43b5ba2956866846086cb786cd46604163e64a0302d259fa02edc2.jpg)

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

![](images/5af1be9abdfd72f952b5f58c10c584fc4565eacbfd6a690bb20882e974a9652a.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>03-Sep-23 11:12:07</td><td>1</td><td>*80.00</td><td>64.08</td></tr><tr><td>2</td><td>16-Oct-23 11:50:01</td><td>1</td><td>*74.00</td><td>59.56</td></tr><tr><td>3</td><td>07-Nov-23 17:22:26</td><td>1</td><td>*68.00</td><td>57.30</td></tr><tr><td>4</td><td>23-Apr-24 06:18:54</td><td>1</td><td>*59.00</td><td>51.24</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>5</td><td>27-Aug-24 09:15:53</td><td>1</td><td>*62.00</td><td>48.12</td></tr><tr><td>6</td><td>29-Apr-25 11:21:40</td><td>1</td><td>*85.00</td><td>73.71</td></tr><tr><td>7</td><td>26-Aug-25 10:25:10</td><td>1</td><td>*105.00</td><td>86.90</td></tr><tr><td>8</td><td>18-Dec-25 11:38:03</td><td>1</td><td>*135.00</td><td>105.00</td></tr></table>

![](images/6de72180d91008f0f6f476de0dac47e1b330d607ebaff57dfef83fe973e38b97.jpg)  
Rating/target price changes above reflect Eastern Time

![](images/e95841bd0922aa09239d0a44d1e3043430b41e460468cbf289c840b60babb1f6.jpg)

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>1</td><td>08-Nov-23 02:23:35</td><td>Add CW</td><td>Downside</td><td>30 Days</td><td>58.22</td></tr><tr><td>2</td><td>08-Dec-23 11:00:30</td><td>Remove CW</td><td>Downside</td><td>30 Days</td><td>52.77</td></tr><tr><td>3</td><td>25-Jul-24 02:08:49</td><td>Add STV</td><td>Upside</td><td>90 Days</td><td>45.28</td></tr><tr><td>4</td><td>23-Oct-24 23:28:11</td><td>Remove STV</td><td>Upside</td><td>90 Days</td><td>57.35</td></tr></table>

CW - Catalyst Watch, STV - Short-Term View

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>5</td><td>29-Oct-24 20:50:50</td><td>Add CW</td><td>Downside</td><td>90 Days</td><td>53.00</td></tr><tr><td>6</td><td>20-Jan-25 01:12:43</td><td>Remove CW</td><td>Downside</td><td>90 Days</td><td>61.91</td></tr><tr><td>7</td><td>10-Jul-25 04:48:00</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>70.20</td></tr><tr><td>8</td><td>08-Aug-25 14:18:06</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>78.13</td></tr></table>

Rating/target price changes above reflect Eastern Time

Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from Hengli Hydraulic in the past 12 months.

<table><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: Hengli Hydraulic.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, non-securities-related: Hengli Hydraulic.</td></tr><tr><td>Analysts&#x27; compensation is determined by Citi management and Citi&#x27;s senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the &quot;Firm&quot;). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.</td></tr><tr><td>For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.</td></tr><tr><td>Unless stated otherwise neither the Research Analyst nor any member of their team has viewed the material operations of the Companies for which an investment view has been provided within the past 12 months.</td></tr><tr><td>For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product (&quot;the Product&quot;), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013, Attention: Legal/Compliance [E6WYB6412478]. In addition, the same important disclosures, with the exception of the Valuation and Risk assessments and historical disclosures, are contained on the Firm&#x27;s disclosure website at https://www.citivelocity.com/cvr/eppublic/citi_research_disclosures. Valuation and Risk assessments can be found in the text of the most recent research note/report regarding the subject company. Pursuant to the Market Abuse Regulation a history of all Citi recommendations published during the preceding 12-month period can be accessed via Citi Velocity (https://www.citivelocity.com/cv2) or your standard distribution portal. Historical disclosures (for up to the past three years) will be provided upon request.</td></tr></table>

<table><tr><td></td><td colspan="3">12 Month Rating</td><td colspan="3">Catalyst Watch</td></tr><tr><td>Data current as of 01 Jul 2026</td><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Citi Global Fundamental Coverage (Neutral=Hold)</td><td>61%</td><td>32%</td><td>7%</td><td>36%</td><td>48%</td><td>16%</td></tr><tr><td>% of companies in each rating category that are investment banking clients</td><td>38%</td><td>42%</td><td>27%</td><td>42%</td><td>37%</td><td>36%</td></tr></table>

## Guide to Citi Fundamental Research Investment Ratings:

Citi stock recommendations include an investment rating and an optional risk rating to highlight high risk stocks. Risk rating takes into account both price volatility and fundamental criteria. Stocks will either have no risk rating or a High risk rating assigned.

Investment Ratings: Citi investment ratings are Buy, Neutral and Sell. Our ratings are a function of analyst expectations of expected total return ("ETR") and risk. ETR is the sum of the forecast price appreciation (or depreciation) plus the dividend yield for a stock within the next 12 months. The target price is based on a 12 month time horizon. The Investment rating definitions are: Buy (1) ETR of $15\%$ or more or $25\%$ or more for High risk stocks; and Sell (3) for negative ETR. Any covered stock not assigned a Buy or a Sell is a Neutral (2). For stocks rated Neutral (2), if an analyst believes that there are insufficient valuation drivers and/or investment catalysts to derive a positive or negative investment view, they may elect with the approval of Citi management not to assign a target price and, thus, not derive an ETR. Citi may suspend its rating and target price and assign "Rating Suspended" status for regulatory and/or internal policy reasons. Citi may also suspend its rating and target price and assign "Under Review" status for other exceptional circumstances (e.g. lack of information critical to the analyst's thesis, trading suspension) affecting the company and/or trading in the company's securities. In both such situations, the rating and target price will show as “—” and “-” respectively in the rating history price chart. Prior to 11 April 2022 Citi assigned "Under Review" status to both situations and prior to 11 Nov 2020 only in exceptional circumstances. As soon as practically possible, the analyst will publish a note re-establishing a rating and investment thesis. Investment ratings are determined by the ranges described above at the time of initiation of coverage, a change in investment and/or risk rating, or a change in target price (subject to limited management discretion). At times, the expected total returns may fall outside of these ranges because of market price movements and/or other short-term volatility or trading patterns. Such interim deviations will be permitted but will become subject to review by Research Management. Your decision to buy or sell a security should be based upon your personal investment objectives and should be made only after evaluating the stock's expected performance and risk.

Catalyst Watch/Short Term Views ("STV") Ratings Disclosure:

Catalyst Watch and STV Upside/Downside calls: Citi may also include a Catalyst Watch or STV Upside or Downside call to indicate the analyst expects the share p

[中间内容因长度限制已省略]

ceipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the "Product"), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
