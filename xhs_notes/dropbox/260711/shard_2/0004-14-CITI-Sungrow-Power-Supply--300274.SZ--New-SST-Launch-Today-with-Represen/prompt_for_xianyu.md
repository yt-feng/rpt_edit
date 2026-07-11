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
# Sungrow Power Supply (300274.SZ)

# New SST Launch Today with Representatives from NVIDIA, Amazon and Microsoft Joining Event

## CITI'S TAKE

Sungrow held its global launch event for its 10kV commercial Solid-State Transformer (SST) at its headquarters in Hefei, China today. This product is designed for usage at 800V high-voltage DC AI data centers with the advantages of simplified power supply architecture, high (98.5%) peak conversion efficiency, sophisticated intelligent features and good safety standards. Representatives from NVIDIA, Amazon and Microsoft have also joined the event. Sungrow has targeted to get grid safety certifications from Underwriters Laboratories ('UL') in the US by end 2026E to meet market access standards for AIDC (AI Data Center) facilities there. The company will provide samples for its potential customers to review in 2H26E when new orders are expected to receive and will be delivered in 2027E. We think this a positive share price driver for Sungrow in next 12 months. Sungrow's 13.6x 2027E PER looks inexpensive with 17% 2025-28E EPS CAGR.

New news – Sungrow held the global launch event for its 10kV commercial Solid-State Transformer (SST) themed “New Computing Infrastructure, Born for AI”—at its Hefei headquarters today. The company unveiled a comprehensive power supply solution featuring Silicon Carbide (SiC) SSTs designed for 800V high-voltage DC AI data centers. Sungrow introduced a new industry model of “immediate mass production and stock delivery” for this product, which is the first commercial medium-voltage SST in China to achieve grid-level certification and qualify for mass export to overseas computing centers.

New product development background – The project involved five years of continuous R&D with a capex over Rmb500m pa and involving 300 R&D specialists. The product development has leveraged on proprietary SiC high-frequency topology and high-frequency magnetic material technologies. Sungrow has targeted to get grid safety certifications from Underwriters Laboratories ('UL') in the US by end 2026E to meet market access standards for AIDC (AI Data Center) facilities there.

High product quality – The product quality looks high in view of (i) power supply architecture with direct conversion from 10-13.8kV AC to 800V DC, eliminating 2–3 stages of traditional transformer and rectification equipment found in conventional data centers; (ii) high peak conversion efficiency of 98.5% (around 3-5ppts above traditional transformers), with equipment volume being just one-third that of traditional oil-immersed transformers saving data center footprint by 70%; (iii) sophisticated intelligent features in term of software-programmable control, millisecond-level frequency and voltage regulation, and bidirectional energy flow; its energy storage and PV systems are supported by simultaneous integration; and (iv) high safety standards with oil-free design eliminating the risk of oil leaks and fires in

## Buy

<table><tr><td colspan="2">Catalyst Watch: Upside, expires 26-JUL-26</td></tr><tr><td>Price (09 Jul 26 15:00)</td><td>Rmb124.010</td></tr><tr><td>Target price</td><td>Rmb185.000</td></tr><tr><td>Expected share price return</td><td>49.2%</td></tr><tr><td>Expected dividend yield</td><td>1.5%</td></tr><tr><td>Expected total return</td><td>50.6%</td></tr><tr><td>Market Cap</td><td>Rmb257,099MUS$37,980M</td></tr></table>

China ESS & Solar Sector

Pierre Lau, CFA $^{AC}$ +852-2501-2716
pierre.lau@citi.com

Air Ma

air.ma@citi.com

## See Appendix A-1 for Analyst Certification, Important Disclosures and Research Analyst Affiliations

Source: Citi

data centers, making it suitable for the enclosed environments of high-density super computing centers.

Much interest from US potential buyers – According to Sungrow, representatives from NVIDIA, Amazon and Microsoft have also joined the event in Anhui, China today. We believe that these American companies are interested in the new product. This product seems likely to target AI data centers initially, and could be subsequently expand into four additional application scenarios namely wind-solar-storage power stations, offshore wind power, DC micro-grids, and hydrogen electrolysis systems which would render more demands. We also expect this product to be cost competitive and with shorter lead time compared to supplier overseas.

Figure 1. AIDC Related Value Chain  
Data Center Roadmap
Architecting AI Infrastructure for Next-Gen AI Factories  
![](images/6cac85a3c0e8cb28e60088e127647ac0c4cdf87c21fb559ff996b3ae885fe417.jpg)

![](images/6d0ae9301608b49f735ba00ffb56ef87e84084d303c5e8cfdbbc5fa6d3f5adee.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.

## Bull/Bear: Sungrow Power Supply

![](images/cb06584eadf4ae35654d5eabc72505d3069d046161ea465523b502411f3ce7de.jpg)  
Spread 69pp
Current Price and expected returns (upside/downside) as of 09 Jul 2026

![](images/5087f2daa751dff0b9da74b3847e5da1092dea14a791a73f2dfe0f24263fc040.jpg)

![](images/bb6d4959ef9ad7b32d542340af8ee785e3735fd1333fedf781953f6015764242.jpg)

![](images/1197dfbbb8fdaed87559b1d59ddc834ace59c16201f6264b790c44aa6bcd68eb.jpg)

## Sungrow Power Supply

## Valuation

Our target price for Sungrow shares of Rmb185.0 is based on a DCF valuation, which we believe is appropriate because it captures the long-term potential returns of the company. We factor in earnings forecasts up to 2035E and terminal growth of 4%. Our WACC for Sungrow is 10.2%, which assumes: 1) a risk-free rate of 5.2%; 2) a market risk premium of 6.8%; 3) an equity beta of 1.1x; 4) a cost-of-debt of 3.9%; 5) a target debt-to-capital ratio of 30%; and 6) a 25.0% corporate tax rate. At our DCF-based target price, Sungrow would trade at 20.2x 2027E PE and 5.3x PB.

## Risks

Key downside risks that could prevent Sungrow shares from reaching our target price include: (i) slower-than-expected solar installation that could accelerate Sungrow's PV inverter and EPC business growth; (ii) less-than-expected energy storage system demand from China and the overseas market; and (iii) intensification of overseas trade tensions that could lessen the exports of Sungrow's products.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

Sungrow Power Supply (300274.SZ)
Ratings and Target Price History
Fundamental Research

Analyst: Pierre Lau, CFA

![](images/3d74979d8e62caad82e4aadcd18d03577ce2cdf57097bb5589a712e1357b207f.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>24-Aug-23 14:05:57</td><td>1</td><td>*104.29</td><td>70.93</td></tr><tr><td>2</td><td>27-Oct-23 14:13:49</td><td>1</td><td>*85.71</td><td>59.19</td></tr><tr><td>3</td><td>22-Apr-24 12:53:27</td><td>1</td><td>*87.86</td><td>67.14</td></tr><tr><td>4</td><td>30-Jun-24 14:26:02</td><td>1</td><td>*76.00</td><td>62.03</td></tr><tr><td>5</td><td>25-Aug-24 11:11:18</td><td>1</td><td>*78.00</td><td>68.12</td></tr><tr><td>6</td><td>31-Oct-24 12:55:52</td><td>1</td><td>*105.00</td><td>90.62</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>7</td><td>10-Feb-25 09:07:21</td><td>1</td><td>*85.00</td><td>72.13</td></tr><tr><td>8</td><td>23-Feb-25 08:42:35</td><td>*3</td><td>*63.00</td><td>67.47</td></tr><tr><td>9</td><td>15-Apr-25 08:13:28</td><td>3</td><td>*48.00</td><td>57.29</td></tr><tr><td>10</td><td>27-Apr-25 20:08:42</td><td>3</td><td>*53.00</td><td>58.82</td></tr><tr><td>11</td><td>27-Jul-25 17:35:10</td><td>*1</td><td>*90.00</td><td>75.78</td></tr><tr><td>12</td><td>25-Aug-25 13:35:38</td><td>1</td><td>*120.00</td><td>102.60</td></tr></table>

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>13</td><td>22-Sep-25 03:45:06</td><td>1</td><td>*160.00</td><td>137.23</td></tr><tr><td>14</td><td>28-Oct-25 12:58:24</td><td>1</td><td>*200.00</td><td>165.88</td></tr><tr><td>15</td><td>09-Nov-25 16:02:51</td><td>1</td><td>*240.00</td><td>201.00</td></tr><tr><td>16</td><td>31-Mar-26 13:36:12</td><td>1</td><td>*200.10</td><td>150.76</td></tr><tr><td>17</td><td>27-Apr-26 12:08:02</td><td>1</td><td>*168.00</td><td>131.39</td></tr><tr><td>18</td><td>25-Jun-26 10:15:49</td><td>1</td><td>*185.00</td><td>152.66</td></tr></table>

Rating/target price changes above reflect Eastern Time

## Sungrow Power Supply (300274.SZ) Short-Term View/Catalyst Watch Research

Analyst: Pierre Lau, CFA

![](images/a0788ceccc6c13f16d4e9ea7c4b9f7d5c7eefda98c6ecbe35a7f8dc5832efd88.jpg)

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>1</td><td>15-Apr-24 01:38:47</td><td>Add CW</td><td>Downside</td><td>30 Days</td><td>71.24</td></tr><tr><td>2</td><td>15-May-24 13:01:03</td><td>Remove CW</td><td>Downside</td><td>30 Days</td><td>75.11</td></tr><tr><td>3</td><td>01-Jul-24 00:27:42</td><td>Add CW</td><td>Downside</td><td>90 Days</td><td>63.15</td></tr><tr><td>4</td><td>27-Sep-24 14:27:48</td><td>Remove CW</td><td>Downside</td><td>90 Days</td><td>85.20</td></tr></table>

CW - Catalyst Watch, STV - Short-Term View

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>5</td><td>10-Feb-25 04:07:21</td><td>Add CW</td><td>Downside</td><td>90 Days</td><td>72.13</td></tr><tr><td>6</td><td>11-May-25 23:13:57</td><td>Remove CW</td><td>Downside</td><td>90 Days</td><td>62.52</td></tr><tr><td>7</td><td>27-Jul-25 13:35:10</td><td>Add STV</td><td>Upside</td><td>90 Days</td><td>75.78</td></tr><tr><td>8</td><td>24-Oct-25 14:21:43</td><td>Remove STV</td><td>Upside</td><td>90 Days</td><td>165.00</td></tr></table>

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>9</td><td>27-Jan-26 22:15:05</td><td>Add CW</td><td>Downside</td><td>90 Days</td><td>158.19</td></tr><tr><td>10</td><td>28-Apr-26 23:16:25</td><td>Remove CW</td><td>Downside</td><td>90 Days</td><td>129.89</td></tr><tr><td>11</td><td>25-Jun-26 06:15:49</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>152.66</td></tr></table>

Rating/target price changes above reflect Eastern Time

<table><tr><td>Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from Sungrow Power Supply in the past 12 months.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: Sungrow Power Supply.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, non-securities-related: Sungrow Power Supply.</td></tr><tr><td>Analysts’ compensation is determined by Citi management and Citi’s senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the “Firm”). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.</td></tr><tr><td>For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.</td></tr><tr><td>Unless stated otherwise neither the Research Analyst nor any member of their team has viewed the material operations of the Companies for which an investment view has been provided within the past 12 months.</td></tr><tr><td>For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product (“the Product”), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013, Attention: Legal/Compliance [E6WYB6412478]. In addition, the same important disclosures, with the exception of the Valuation and Risk assessments and historical disclosures, are contained on the Firm&#x27;s disclosure website at https://www.citivelocity.com/cvr/eppublic/citi_research_disclosures. Valuation and Risk assessments can be found in the text of the most recent research note/report regarding the subject company. Pursuant to the Market Abuse Regulation a history of all Citi recommendations published during the preceding 12-month period can be accessed via Citi Velocity (https://www.citivelocity.com/cv2) or your standard distribution portal. Historical disclosures (for up to the past three years) will be provided upon request.</td></tr></table>

Citi Equity Ratings Distribution

<table><tr><td></td><td colspan="3">12 Month Rating</td><td colspan="3">Catalyst Watch</td></tr><tr><td>Data current as of 01 Jul 2026</td><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Citi Global Fundamental Coverage (Neutral=Hold)</td><td>61%</td><td>32%</td><td>7%</td><td>36%</td><td>48%</td><td>16%</td></tr><tr><td>% of companies in each rating category that are investment banking clients</td><td>38%</td><td>42%</td><td>27%</td><td>42%</td><td>37%</td><td>36%</td></tr></table>

Guide to Citi Fundamental Research Investment Ratings:

Citi stock recommendations include an investment rating and an optional risk rating to highlight high risk sto

[中间内容因长度限制已省略]

ternal parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
