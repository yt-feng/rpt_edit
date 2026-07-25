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
# China Auto Manufacturers

Weichai-Sinotruk Momentum Tracker

## CITI'S TAKE

We recognize Weichai share price has been driven by AI momentum and we try to quantify the correlations in this note. We develop an AIDC/SOFC/AI-Hardware weighted index (Figure 1), by assigning 50%/50% weight on daily share price of Generac/Bloom Energy. The R-square of this index and Weichai share price in YTD-2026 comes at 0.84, indicating Weichai share price's strong correlation with AIDC/SOFC/AI-Hardware weighted index, while Sinotruk (R-square with the index only at 0.22) correlates more on export YoY fundamental (Figure 2). Notably, in the previous cycle, Sinotruk's share price exhibited a 15-day lag relative to export growth momentum — Figure 2: the green line at day n corresponds to the blue line at day n–15. Therefore, if the lag relationship holds, a strong export YoY in Jul could support Sinotruk share price rally from now until mid-Aug, given high-margin export growth should bring earnings upside to Sinotruk.

Meanwhile, the AI hardware, Generac and Bloom Energy earnings visibility and share price performance should also define whether Weichai share price to outperform Sinotruk in 3Q (similar to mid-March to mid-May cycle), in our view.

## Further readings:

(1) Sinotruk (Hong Kong) (3808.HK) - 1H Earnings Preview & 2H outlook; Raise TP to HK\$55.0

(2) Weichai Power (2338.HK) - Powering up more AIDCs; Lift up 26-28E NP by 4/13/56% and TP to HK\$50

Jeff Chung $^{AC}$ +852-2501-2787
jeff.m.chung@citi.com

Kyle Wu

+852-2501-8483

kyle.wu@citi.com

Figure 1. YTD Share Price Movements of Weichai/Sinotruk/Generac/BE  
![](images/9278a77ef45b19999fdb72ddf4ce796d1f6caeccf8742e2b9a01ef4bfb9179fb.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Note: We develop a AIDC/SOFC/AI-Hardware weighted index, by assigning 50%/50% weight on daily share price of Generac/Bloom Energy.

Source: Citi Estimates, Bloomberg

Figure 2. Sinotruk Shar Price vs. China HDT Export/Domestic Retail YoY  
![](images/0c21e7a812a1bae6f386638b9ac38da8cd4e3701ebe8534f4d8dd6dd5e404bd7.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, CAAM, Thinkercar

## Note in the index :

Generac, Bloom Energy, and Weichai Power are distinct major players in the global power and energy ecosystem. Weichai and Bloom Energy are direct competitors in SOFC field. Weichai supplies parts and collaboration to Generac.

## Sinotruk (Hong Kong)

(3808.HK; HK\$42.82; 1; 23 Jul 26; 16:10)

## Valuation

Our target price for Sinotruk of HK\$55.0/share is based on 15x 2026E P/E (2 standard deviation above historical average) to factor in our expectation for the company to continue outperforming in the medium term.

## Risks

Key downside risks to our target price include any economic slowdown and the absence of FAI improvement; weaker-than-expected fleet replacement trends; and competition.

Key upside risks to our target price include stronger-than-expected economic growth; stronger-than-expected truck sales; and FAI improvements.

Any of these factors could cause the shares to deviate from our target price.

## Weichai Power

(2338.HK; HK\$33.46; 1; 23 Jul 26; 16:10)

## Valuation

By applying 23x 2026E PER (2SD above the historical average to factor in upside potential on data center engines earnings), we set our target price at HK\$50.0.

## Risks

Key downside risks to our target price and investment view on Weichai include: worse highway freight traffic and/or property FAI; decline in major customers outsourcing engine supply; and weaker US/EU logistics markets.

Key upside risks to our target price are: stronger-than-expected FAI growth; and faster-than-expected market share gain.

Any of these factors could cause the shares to deviate from our target price.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

Sinotruk (Hong Kong) (3808.HK)
Ratings and Target Price History
Fundamental Research

Analyst: Jeff Chung

![](images/db52cc96e83812058d3a891f6016b8eab603f3bef5d5e27c9843ce920d43560a.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>30-Aug-23 15:40:37</td><td>1</td><td>*19.10</td><td>15.40</td></tr><tr><td>2</td><td>23-Jan-24 11:48:16</td><td>1</td><td>*18.00</td><td>14.42</td></tr><tr><td>3</td><td>25-Mar-24 19:17:29</td><td>1</td><td>*24.80</td><td>20.00</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>4</td><td>04-Jul-24 20:48:25</td><td>1</td><td>*23.40</td><td>18.02</td></tr><tr><td>5</td><td>14-Jul-24 22:23:11</td><td>1</td><td>*25.60</td><td>17.94</td></tr><tr><td>6</td><td>22-Aug-24 17:37:01</td><td>1</td><td>*26.40</td><td>20.45</td></tr></table>

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>7</td><td>21-Jan-26 12:09:02</td><td>1</td><td>*39.40</td><td>32.24</td></tr><tr><td>8</td><td>02-Apr-26 06:45:58</td><td>1</td><td>*51.00</td><td>42.54</td></tr><tr><td>9</td><td>22-Jul-26 09:34:41</td><td>1</td><td>*55.00</td><td>38.64</td></tr></table>

Rating/target price changes above reflect Eastern Time

## Weichai Power (2338.HK)

Ratings and Target Price History
Fundamental Research

Analyst: Jeff Chung

![](images/7530da25b555d78069e416f6371700f9c1e32d0ec6c5b4e21771118f84ccf4e8.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>30-Aug-23 18:19:33</td><td>2</td><td>*11.00</td><td>9.95</td></tr><tr><td>2</td><td>15-Oct-23 17:53:04</td><td>2</td><td>*11.40</td><td>11.12</td></tr><tr><td>3</td><td>30-Oct-23 16:20:50</td><td>2</td><td>*13.20</td><td>11.94</td></tr><tr><td>4</td><td>25-Mar-24 16:19:24</td><td>2</td><td>*15.40</td><td>15.28</td></tr><tr><td>5</td><td>29-Apr-24 16:38:39</td><td>2</td><td>*17.20</td><td>16.50</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>6</td><td>04-Jul-24 20:48:25</td><td>2</td><td>*14.00</td><td>12.88</td></tr><tr><td>7</td><td>22-Aug-24 17:28:07</td><td>2</td><td>*12.90</td><td>12.22</td></tr><tr><td>8</td><td>30-Oct-24 19:20:42</td><td>2</td><td>*12.60</td><td>11.88</td></tr><tr><td>9</td><td>30-Mar-25 23:42:48</td><td>2</td><td>*18.40</td><td>16.76</td></tr><tr><td>10</td><td>01-May-25 22:05:29</td><td>2</td><td>*16.30</td><td>15.20</td></tr></table>

Rating/target price changes above reflect Eastern Time

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>11</td><td>10-Nov-25 04:01:02</td><td>2</td><td>*21.30</td><td>20.04</td></tr><tr><td>12</td><td>22-Jan-26 22:37:43</td><td>*1</td><td>*34.00</td><td>24.40</td></tr><tr><td>13</td><td>29-Apr-26 12:00:03</td><td>1</td><td>*42.00</td><td>36.12</td></tr><tr><td>14</td><td>21-Jun-26 19:22:38</td><td>1</td><td>*50.00</td><td>39.72</td></tr></table>

![](images/c8429c0cb0905eb6ffd6ec94450c614c97fd77595211b419c57e7160dca81a97.jpg)

<table><tr><td rowspan="2" colspan="2">Date</td><td rowspan="2">Action</td><td rowspan="2">Expected Direction</td><td rowspan="2">Duration</td><td rowspan="2">Closing Price</td><td rowspan="3"></td><td colspan="2">Date</td><td>Expected Direction</td><td>Duration</td><td>Closing Price</td></tr><tr><td rowspan="2">25-Jul-24 20:00:57</td><td rowspan="2">Remove CW</td><td rowspan="2">Downside</td><td rowspan="2">90 Days</td><td rowspan="2">17.66</td></tr><tr><td>1</td><td>04-Jul-24 16:48:25</td><td>Add CW</td><td>Downside</td><td>90 Days</td><td>18.02</td></tr></table>

CW - Catalyst Watch, STV - Short-Term View  
Rating/target price changes above reflect Eastern Time

![](images/24178f2143defaa5a3d0992708523ba6c4ab8ef152b8ac8912c6a6200d86e266.jpg)

<table><tr><td colspan="2">Date104-Jul-24 16:48:25</td><td>ActionAdd CW</td><td>ExpectedDirectionDownside</td><td>Duration90 Days</td><td>ClosingPrice12.88</td><td>Date225-Jul-24 21:06:40</td><td>ActionRemove CW</td><td>ExpectedDirectionDownside</td><td>Duration90 Days</td><td>ClosingPrice11.66</td></tr></table>

CW - Catalyst Watch, STV - Short-Term View  
Rating/target price changes above reflect Eastern Time

The Firm has made a market in the publicly traded equity securities of Weichai Power Co Ltd on at least one occasion since 1 Jan 2025.

<table><tr><td>Jan 2023.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates has received compensation for investment banking services provided within the past 12 months from Sinotruk (Hong Kong).</td></tr><tr><td>Citi Global Markets Inc. or its affiliates expects to receive or intends to seek, within the next three months, compensation for investment banking services from Sinotruk (Hong Kong).</td></tr><tr><td>Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from Sinotruk (Hong Kong),Weichai Power in the past 12 months.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as investment banking client(s): Sinotruk (Hong Kong).</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: Sinotruk (Hong Kong).</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, non-securities-related: Sinotruk (Hong Kong),Weichai Power.</td></tr><tr><td>Citi Global Markets Inc. and/or its affiliates has a significant financial interest in relation to Sinotruk (Hong Kong). (For an explanation of the determination of significant financial interest, please refer to the policy for managing conflicts of interest which can be found at www.citiVelocity.com.)</td></tr><tr><td>Analysts’ compensation is determined by Citi management and Citi’s senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the “Firm”). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.</td></tr><tr><td>For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may</td></tr></table>

engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.

The Firm is a market maker in the publicly traded equity securities of Weichai Power.

Citi Equity Ratings Distribution

<table><tr><td></td><td colspan="3">12 Month Rating</td><td colspan="3">Catalyst Watch</td></tr><tr><td>Data current as of 01 Jul 2026</td><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Citi Global Fundamental Coverage (Neutral=Hold)</td><td>61%</td><td>32%</td><td>7%</td><td>36%</td><td>48%</td><td>16%</td></tr><tr><td>% of companies in each rating category that are investment banking clients</td><td>38%</td><td>42%</td><td>27%</td><td>42%</td><td>37%</td><td>36%</td></tr></table>

Guide to Citi Fundamental Research Investment Ratings:

Citi stock recommendations include an investment rating and an optional risk rating to highlight high risk stocks. Risk rating takes into account both price volatility and fundamental criteria. Stocks will either have no risk rating or a High risk rating assigned.

Investment Ratings: Citi investment ratings are Buy, Neutral and Sell. Our ratings are a function of analyst expectations of expected total return ("ETR") and risk. ETR is the sum of the forecast price appreciation (or depreciation) plus the dividend yield for a stock within the next 12 months. The target price is based on a 12 month time horizon. The Investment rating definitions are: Buy (1) ETR of 15% or more or 25% or more for High risk stocks; and Sell (3) for negative ETR. Any covered stock not assigned a Buy or a Sell is a Neutral (2). For stocks rated Neutral (2), if an analyst believes that there are insufficient valuation drivers and/or investment catalysts to derive a positive or negative investment view, they may elect with the approval of Citi management not to assign a target price and, thus, not derive an ETR. Citi may suspend its rating and target price and assign "Rating Suspended" status for regulatory and/or internal policy reasons. Citi may also suspend its rating and target price and assign "Under Review" status for other exceptional circumstances (e.g. lack of information critical to the analyst's thesis, trading suspension) affecting the company and/or trading in the company's securities. In both such situations, the rating and target price will show as “—” and “-” respectively in the rating history price chart. Prior to 11 April 2022 Citi assigned "Under Review" status to both situations and prior to 11 Nov 2020 only in exceptional circumstances. As soon as practically possible, the analyst will publish a note re-establishing a rating and investment thesis. Investment ratings are determined by the ranges described above at the time of initiation of coverage, a change in investment and/or risk rating, or a change in target price (subject to limited management discretion). At times, the expected total returns may fall outside of these ranges because of market price movements and/or other short-term volatility or trading patterns. Such interim deviations will be permitted but will become subject to review by Research Management. Your decision to buy or sell a security should be based upon your personal investment objectives and should be made only after evaluating the stock's expected performance and risk.

## Catalyst Watch/Short Term Views (“STV”) Ratings Disclosure:

Catalyst Watch and STV Upside/Downside calls: Citi may also include a Catalyst Watch or STV Upside or Downside call to indicate the analyst expects the share price to rise (fall) in absolute terms over a specified period of 30 or 90 days in reaction to one or more specific near-term catalysts or events impacting the company or the market. A Catalyst Watch will be published when Analyst confidence is high that an impact to share price will occur; it will be a STV when confidence level is moderate. A Catalyst Watch or STV Upside/Downside call will automatically expire at the end of the specified 30/90 day period. The Catalyst Watch will also be automatically removed if share price performance (calculated at market close) exceeds $15\%$ against the direction of the call (unless over-ridden by the analyst). The analyst may also remove a Catalyst Watch or STV call prior to the end of the specified period in a published research note. A Catalyst Watch/STV Upside or Downside call may be different from and does not affect a stock's fundamental equity rating, which reflects a longer-term total absolute return expectation. For purposes of FINRA ratings-distribution-disclosure rules, a Catalyst Watch/STV Upside call corresponds to a buy recommendation and a Catalyst Watch/STV Downside call corresponds to a sell recommendation. Any stock not assigned to a Catalyst Watch Upside, Catalyst Watch Downside, STV Upside, or STV Downside call is considered Catalyst Watch/STV No View. For purposes of FINRA ratings distribution-disclosure rules, we correspond Catalyst Watch/STV No View to Hold in our ratings distribution table for our Catalyst Watch/STV Upside/Downside rating system. However, we reiterate that we do not consider No View to be a recommendation. For all Catalyst Watch/STV Upside/Downside calls, risk exists that the catalyst(s) and associated share-price movement will not materialize as expected.

RESEARCH ANALYST AFFILIATIONS / NON-US RESEARCH ANALYST DISCLOSURES

The legal entities employing the authors of this report are listed below (and their regulators are listed further herein). Non-US research analysts who have prepared this report (i.e., all research analysts listed below other than those identified as employed by Citi Global Markets I

[中间内容因长度限制已省略]

ar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective

investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
