你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
# NVIDIA Corp (NVDA.O)

What Are Investors Asking?

## CITI'S TAKE

We recently spoke with NVIDIA's investor relations team to synthesize the answers to key investor topics. We maintain NVDA as our top buy-rated mega-cap data center semis pick on strong access to DRAM memory amidst constrained industry supply (see note).

Kyber Rubin Ultra Delay: Nvidia continues to state that its roadmap is fully intact. Additionally, management mentioned that the NVLink domains they showed at Computex this year have not changed either.

CPO: Management reiterated that currently CPO for scale-out is in production with Spectrum-X and the company will have more details on customer adoption later this year, but NVIDIA nevertheless points to the customer adoption being high for CPO for scale-out. Beginning in CY2028 with Feynman, customers will have an option to use NVLink with CPO or Copper.

Meta's Cloud Ambitions: NVIDIA does not comment on customer plans but continues to see very strong demand and will focus on addressing demand.

Neocloud vs. Hyperscalers: NVIDIA will continue to serve hyperscalers, neocloud, sovereigns, enterprises, etc. The company nevertheless points out that initially hyperscalers drove most of the deployments, but the AI market is seeing more AI labs also ramping capacity, with also sovereign and enterprise on-prem demand gaining momentum over the past two years. Management believes that as the promise of AI continues to turn to reality, the non-hyperscaler portion of the market will have to ultimately be bigger, specially as physical AI starts to ramp.

Open vs. Closed Models: NVIDIA believes both are important. While frontier models are important in terms of driving performance, open source models are important for enterprise and sovereign to adopt, ramp, and scale AI. NVIDIA identified a market need which is why the company developed its own free models (Nemotron, Cosmos, and Alpha Mayo). NVIDIA is nevertheless clear that the objective is not to compete with frontier models but to help sovereigns and enterprises along in their AI journey.

Cost/GW: Management was helpful in clarifying that the \$100B per 1GW long term should be viewed as an energy efficiency comment by Jensen, meaning that in the future \$100B of compute will require only 1GW vs now with \$30B-\$40B for 1GW today. This is because gen to gen GPUs become more energy-efficient, with notably Blackwell being 25x more power-efficient than Hopper. NVIDIA believes it can continue on that cadence moving forward. On the other side, as the ROI continues to increase, NVIDIA expects to see more revenue intensity per GW.

Data Centers in Space: NVIDIA mentioned that they have announced at GTC having

<table><tr><td colspan="2">Buy</td></tr><tr><td>Price (08 Jul 26 16:00)</td><td>US$204.12</td></tr><tr><td>Target price</td><td>US$300.00</td></tr><tr><td>Expected share price return</td><td>47.0%</td></tr><tr><td>Expected dividend yield</td><td>0.0%</td></tr><tr><td>Expected total return</td><td>47.0%</td></tr><tr><td>Market Cap</td><td>US$4,939,704M</td></tr></table>

## Atif Malik $^{AC}$

+1-415-951-1892

atif.malik@citi.com

Papa Sylla

+1-212-816-9476

papa.sylla@citi.com

See Appendix A-1 for Analyst Certification, Important Disclosures and Research Analyst Affiliations a variant of Vera Rubin for space in the form of an accelerated satellite. In terms of realizing the vision Space X has discussed, though it has engineering challenges, the company does not believe it is impossible.

Memory Maker's LTA Impact: NVIDIA continues to stick to its mid-70s GM guide provided last quarter.

Capital Allocation: NVIDIA reiterated its target of 50% of cash flow to be returned to shareholders this year. As it moves to outer years, management mentioned that given where the stock is, they can expect the company to increase buybacks. On the recent \$25B debt offering, NVIDIA mentioned it was mostly to offer itself more flexibility.

d-Matrix Announcement: NVIDIA has not officially announced a collaboration with d-Matrix. Management mentioned that the company in the past has been more than willing to look at outside technologies to incorporate in their platform, and Groq is the latest example.

## NVIDIA Corp

## Valuation

Our price target for NVDA of \$300 is based on \~28x P/E on C27E earnings power of \~\$11.9 (incl. SBC) discounted back. Our 28x P/E multiple is in-line with 3 year average.

## Risks

Downside risks to the attainment of our target price include: 1) competition on gaming could drive the stock lower if Nvidia loses market share; 2) slower-than-expected adoption of new platforms can drive lower data center and gaming sales; 3) lumpiness in auto and data center markets can add volatility to the stock/multiple; and 4) cryptomining impact on gaming sales.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

NVIDIA Corp (NVDA)
Ratings and Target Price History
Fundamental Research

Analyst: Atif Malik

![](images/c30e5c043610df43f52699f25c0c9b41ce601ac5d8e1670a2afad05b79c428a4.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>17-Jul-23 01:50:06</td><td>1</td><td>*52.00</td><td>46.46</td></tr><tr><td>2</td><td>24-Aug-23 02:36:33</td><td>1</td><td>*63.00</td><td>47.16</td></tr><tr><td>3</td><td>18-Oct-23 00:32:40</td><td>1</td><td>*57.50</td><td>42.20</td></tr><tr><td>4</td><td>22-Feb-24 02:01:24</td><td>1</td><td>*82.00</td><td>78.54</td></tr><tr><td>5</td><td>20-Mar-24 06:26:15</td><td>1</td><td>*103.00</td><td>90.37</td></tr><tr><td>6</td><td>23-May-24 02:55:03</td><td>1</td><td>*126.00</td><td>103.80</td></tr><tr><td>7</td><td>26-Jun-24 05:00:00</td><td>1</td><td>*150.00</td><td>126.40</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>8</td><td>12-Nov-24 08:00:00</td><td>1</td><td>*170.00</td><td>148.29</td></tr><tr><td>9</td><td>21-Nov-24 05:00:00</td><td>1</td><td>*175.00</td><td>146.67</td></tr><tr><td>10</td><td>05-Feb-25 08:00:00</td><td>1</td><td>*163.00</td><td>124.83</td></tr><tr><td>11</td><td>10-Apr-25 22:30:00</td><td>1</td><td>*150.00</td><td>107.57</td></tr><tr><td>12</td><td>29-May-25 01:37:50</td><td>1</td><td>*180.00</td><td>139.19</td></tr><tr><td>13</td><td>07-Jul-25 02:00:00</td><td>1</td><td>*190.00</td><td>158.24</td></tr><tr><td>14</td><td>28-Aug-25 01:41:01</td><td>1</td><td>*210.00</td><td>180.17</td></tr></table>

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>15</td><td>08-Sep-25 02:00:00</td><td>1</td><td>*200.00</td><td>168.31</td></tr><tr><td>16</td><td>30-Sep-25 04:04:43</td><td>1</td><td>*210.00</td><td>186.58</td></tr><tr><td>17</td><td>10-Nov-25 06:11:57</td><td>1</td><td>*220.00</td><td>199.05</td></tr><tr><td>18</td><td>20-Nov-25 02:46:50</td><td>1</td><td>*270.00</td><td>180.64</td></tr><tr><td>19</td><td>26-Feb-26 02:41:17</td><td>1</td><td>*300.00</td><td>184.89</td></tr></table>

Rating/target price changes above reflect Eastern Time

## NVIDIA Corp (NVDA)

Short-Term View/Catalyst Watch Research

Analyst: Atif Malik

![](images/772ea16e3ec8894a68aef4513eb0baabd15794364bf4c24f1e48c74dc228fa23.jpg)

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>1</td><td>11-Dec-23 08:11:55</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>46.63</td></tr><tr><td>2</td><td>10-Jan-24 11:06:14</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>54.35</td></tr><tr><td>3</td><td>15-Apr-24 01:00:00</td><td>Add CW</td><td>Upside</td><td>90 Days</td><td>86.00</td></tr><tr><td>4</td><td>16-Jun-24 21:00:00</td><td>Remove CW</td><td>Upside</td><td>90 Days</td><td>131.88</td></tr></table>

CW - Catalyst Watch, STV - Short-Term View

<table><tr><td></td><td>Date</td><td>Action</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td>5</td><td>22-Jul-24 01:00:00</td><td>Add CW</td><td>Upside</td><td>30 Days</td><td>123.54</td></tr><tr><td>6</td><td>04-Aug-24 14:08:32</td><td>Remove CW</td><td>Upside</td><td>30 Days</td><td>107.27</td></tr><tr><td>7</td><td>21-Nov-24 00:00:00</td><td>Add CW</td><td>Upside</td><td>90 Days</td><td>146.67</td></tr><tr><td>8</td><td>14-Jan-25 02:06:50</td><td>Remove CW</td><td>Upside</td><td>90 Days</td><td>131.76</td></tr></table>

<table><tr><td>Date</td><td>Action</td><td>ExpectedDirection</td><td>Duration</td><td>ClosingPrice</td></tr><tr><td>10-Nov-25 01:11:57</td><td>Add STV</td><td>Upside</td><td>30 Days</td><td>199.05</td></tr><tr><td>10-Dec-25 11:07:18</td><td>Remove STV</td><td>Upside</td><td>30 Days</td><td>183.78</td></tr></table>

Rating/target price changes above reflect Eastern Time

<table><tr><td>Within the past 12 months, Citi Global Markets Inc. or its affiliates has acted as manager or co-manager of an offering of securities of NVIDIA Corp.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates has received compensation for investment banking services provided within the past 12 months from NVIDIA Corp.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from NVIDIA Corp in the past 12 months.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as investment banking client(s): NVIDIA Corp.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: NVIDIA Corp.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, non-securities-related: NVIDIA Corp.</td></tr><tr><td>Citi Global Markets Inc. and/or its affiliates has a significant financial interest in relation to NVIDIA Corp. (For an explanation of the determination of significant financial interest, please refer to the policy for managing conflicts of interest which can be found at www.citiVelocity.com.)</td></tr><tr><td>Analysts&#x27; compensation is determined by Citi management and Citi&#x27;s senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the &quot;Firm&quot;). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.</td></tr><tr><td>For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.</td></tr><tr><td>Unless stated otherwise neither the Research Analyst nor any member of their team has viewed the material operations of the Companies for which an investment view has been provided within the past 12 months.</td></tr><tr><td>For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product (&quot;the Product&quot;), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013, Attention: Legal/Compliance [E6WYB6412478]. In addition, the same important disclosures, with the exception of the Valuation and Risk assessments and historical disclosures, are contained on the Firm&#x27;s disclosure website at https://www.citivelocity.com/cvr/eppublic/citi_research_disclosures. Valuation and Risk assessments can be found in the text of the most recent research note/report regarding the subject company. Pursuant to the Market Abuse Regulation a history of all Citi recommendations published during the preceding 12-month period can be accessed via Citi Velocity (https://www.citivelocity.com/cv2) or your standard distribution portal. Historical disclosures (for up to the past three years) will be provided upon request.</td></tr></table>

<table><tr><td colspan="7">Citi Equity Ratings Distribution</td></tr><tr><td></td><td colspan="3">12 Month Rating</td><td colspan="3">Catalyst Watch</td></tr><tr><td>Data current as of 01 Jul 2026</td><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Citi Global Fundamental Coverage (Neutral=Hold)</td><td>61%</td><td>32%</td><td>7%</td><td>36%</td><td>48%</td><td>16%</td></tr><tr><td>% of companies in each rating category that are investment banking clients</td><td>38%</td><td>42%</td><td>27%</td><td>42%</td><td>37%</td><td>36%</td></tr></table>

## Guide to Citi Fundamental Research Investment Ratings:

Citi stock recommendations include an investment rating and an optional risk rating to highlight high risk stocks. Risk rating takes into account both price volatility and fundamental criteria. Stocks will either have no risk rating or a High risk rating assigned.

Investment Ratings: Citi investment ratings are Buy, Neutral and Sell. Our ratings are a function of analyst expectations of expected total return ("ETR") and risk. ETR is the sum of the forecast price appreciation (or depreciation) plus the dividend yield for a stock within the next 12 months. The target price is based on a 12 month time horizon. The Investment rating definitions are: Buy (1) ETR of 15% or more or 25% or more for High risk stocks; and Sell (3) for negative ETR. Any covered stock not assigned a Buy or a Sell is a Neutral (2). For stocks rated Neutral (2), if an analyst believes that there are insufficient valuation drivers and/or investment catalysts to derive a positive or negative investment view, they may elect with the approval of Citi management not to assign a target price and, thus, not derive an ETR. Citi may suspend its rating and target price and assign "Rating Suspended" status for regulatory and/or internal policy reasons. Citi may also suspend its rating and target price and assign "Under Review" status for other exceptional circumstances (e.g. lack of information critical to the analyst's thesis, trading suspension) affecting the company and/or trading in the company's securities. In both such situations, the rating and target price will show as “—” and “-” respectively in the rating history price chart. Prior to 11 April 2022 Citi assigned “Under Review” status to both situations and prior to 11 Nov 2020 only in exceptional circumstances. As soon as practically possible, the analyst will publish a note re-establishing a rating and

investment thesis. Investment ratings are determined by the ranges described above at the time of initiation of coverage, a change in investment and/or risk rating, or a change in target price (subject to limited management discretion). At times, the expected total returns may fall outside of these ranges because of market price movements and/or other short-term volatility or trading patterns. Such interim deviations will be permitted but will become subject to review by Research Management. Your decision to buy or sell a security should be based upon your personal investment objectives and should be made only after evaluating the stock's expected performance and risk.

## Catalyst Watch/Short Term Views ("STV") Ratings Disclosure:

Catalyst Watch and STV Upside/Downside calls: Citi may also include a Catalyst Watch or STV Upside or Downside call to indicate the analyst expects the share price to rise (fall) in absolute terms over a specified period of 30 or 90 days in reaction to one or more specific near-term catalysts or events impacting the company or the market. A Catalyst Watch will be published when Analyst confidence is high that an impact to share price will occur; it will be a STV when confidence level is moderate. A Catalyst Watch or STV Upside/Downside call will automatically expire at the end of the specified 30/90 day period. The Catalyst Watch will also be automatically removed if share price performance (calculated at market close) exceeds 15% against the direction of the call (unless over-ridden by the analyst). The analyst may also remove a Catalys

[中间内容因长度限制已省略]

lar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
