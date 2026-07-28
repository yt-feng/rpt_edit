You are a senior financial newsletter editor with a consulting-style strategy lens. You turn research-report material into a long-form English article that is structured, insightful, and suitable for a serious business audience.

Objective:
- Write an English Markdown article based on the report parsing below.
- Target length: around 2200 words, plus or minus 15%.
- Tone: serious, analytical, strategic, and readable.
- The article should not feel like a summary. It should make an argument.
- You may extend the report's logic into reasonable second-order implications, but do not invent data, company actions, or quotes.
- Do not disclose every detail. Keep the article concise and end after the last substantive point.

McKinsey-style writing principles:
1. Answer first: open with the controlling idea, not background.
2. Governing thought: every section must support the main answer.
3. Mutually exclusive, collectively exhaustive logic: avoid overlapping sections.
4. So what: every section must explain why the point matters.
5. Synthesis over summary: do not list facts; interpret what the pattern means.
6. Action titles: section headings must be complete, insight-bearing sentences. Do not use generic headings such as "Key Takeaways", "Market Background", "Core View", or "Reader Implications".
7. Source specificity: ground every interpretation in a concrete number, named mechanism, comparison, or causal relationship from the report.

Required Markdown structure:
- `# Title`: make it a direct argument, not a topic label.
- Opening: 4-6 short paragraphs that state the main thesis and why now matters.
- 4-6 `##` sections. Each `##` heading must be an action title: a sentence that tells the reader the insight.
- One section should translate the report into a decision framework for readers.
- Never create a section about unresolved questions, what the report failed to answer, research gaps, limitations, further reading, or community access. If the source explicitly states a limitation, mention it once inside the relevant analytical paragraph.
- End with the final substantive paragraph. Do not add a CTA, promotional invitation, website, community reference, summary, or rhetorical question.
- End with: `*For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Open with the most specific fact, contrast, or tension in the source. Avoid generic openings such as "Against this backdrop", "In recent years", or "As the market evolves".
- Vary sentence and paragraph length naturally. Do not repeat stock transitions such as "This means", "In other words", or "What matters most".
- Do not invent a personal voice, interview, or first-hand experience. Editorial character must come from evidence selection and precise phrasing.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
# Lens Tech (300433.SZ / 6613.HK)

Collaboration with Intel on Glass Substrate

## CITI'S TAKE

Intel and Lens Tech on 25 July announced a strategic collaboration focused on accelerating the development of glass substrate-based packaging solutions to enable higher performance, increased interconnect density, and improved power efficiency for future computing platforms. Intel unveiled its first glass substrate in 2023 and introduced EMIB-T in May 2025. We believe Intel has ambitions to commercialize the glass substrate and EMIB-T, with production ramp in 2027-28 likely. Establishing strategic supply-chain cooperation is needed. Lens Tech started R&D on glass substrate solutions three years ago. The company believes it could help commercialize glass substrate technology given its proven mass-production capabilities for glass grinding and polishing process that facilitate improving the yield for TGV (through-glass-via) and reducing micro-crack and warpage for large packaging size and high-power chips. We expect certain qualification processes this year and potential product launch from its customers next year.

Kyna Wong $^{AC}$ +852-2868-7820
kyna.wong@citi.com

Karen Huang +852-2501-2755 karen.xw.huang@citi.com

Kevin Chen +852-2501-2125 kevin.y.chen@citi.com

Yiming Li, CFA +852-2501-2857 yiming.li@citi.com

<table><tr><td rowspan="2" colspan="14"></td><td colspan="2">Current Fiscal Year</td><td colspan="2">Next Fiscal Year</td></tr><tr><td rowspan="2" colspan="2">EPS</td><td rowspan="2" colspan="2">EPS</td></tr><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Ccy</td><td rowspan="2">Price</td><td rowspan="2">Mkt Cap (M)</td><td rowspan="2">Date &amp; Time</td><td colspan="2">Rating</td><td rowspan="2">Short-Term View</td><td colspan="2">Target Price</td><td></td><td></td><td></td></tr><tr><td>Old</td><td>New</td><td>Old</td><td>New</td><td>ESPR (%)</td><td>Div Yld (%)</td><td>ETR (%)</td><td>Last Rpt Yr</td><td>Old</td><td>New</td><td>Old</td></tr><tr><td>Lens Technology</td><td>300433.SZ</td><td>Rmb</td><td>37.320</td><td>197,003</td><td>24 Jul 15:00</td><td>2</td><td>nc</td><td>-</td><td>30.000</td><td>nc</td><td>-19.6</td><td>2.0</td><td>-17.6</td><td>Dec-25</td><td>0.825</td><td>nc</td><td>1.346</td></tr><tr><td>Lens</td><td>6613.HK</td><td>HK$</td><td>21.86</td><td>228,138</td><td>24 Jul 16:10</td><td>1</td><td>nc</td><td>-</td><td>25.00</td><td>nc</td><td>14.4</td><td>3.9</td><td>18.3</td><td>Dec-25</td><td>0.825</td><td>nc</td><td>1.346</td></tr></table>

$1 =$ Buy, $2 =$ Neutral, $3 =$ Sell, $\mathrm{H} =$ High Risk  
ESPR = Expected Share Price Return, ETR = Expected Total Return, nc = no change ^Catalyst Watch

Earnings Estimates

<table><tr><td colspan="4"></td><td colspan="5">Last Reported Year</td><td colspan="5">Current Fiscal Year</td><td colspan="5">Next Fiscal Year</td></tr><tr><td>Company Name</td><td>Ticker</td><td>Last Rpt Year</td><td>Currency</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>FY0</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>FY1</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>FY2</td></tr><tr><td>Lens Technology</td><td>300433.SZ</td><td>Dec-25</td><td>Rmb</td><td>0.086</td><td>0.143</td><td>0.336</td><td>0.229</td><td>0.783</td><td>-0.029</td><td>0.101</td><td>0.390</td><td>0.363</td><td>0.825</td><td>0.087</td><td>0.147</td><td>0.538</td><td>0.574</td><td>1.346</td></tr><tr><td>Lens</td><td>6613.HK</td><td>Dec-25</td><td>Rmb</td><td>0.086</td><td>0.143</td><td>0.336</td><td>0.229</td><td>0.783</td><td>-0.029</td><td>0.101</td><td>0.390</td><td>0.363</td><td>0.825</td><td>0.087</td><td>0.147</td><td>0.538</td><td>0.574</td><td>1.346.</td></tr><tr><td colspan="19">Source: Citi</td></tr></table>

## Lens Technology

## Company description

Lens Technology, which was founded in 2006, produces covers for smartphones, tablets, wearables, etc. Apple and Xiaomi are the company's two largest clients. Chinese OEM clients include Xiaomi and Huawei.

## Investment strategy

We rate Lens Technology A share as Neutral on its fair valuation despite we remain positive on its dual growth engines of automotive and iPhone cover glass upgrade and metal casing share gain and assembly businesses.

## Valuation

Our target price of Rmb30.0 is based on 30.0x 2H26-1H27E EPS, justified by our estimated 31% 3-year earnings CAGR. We believe Lens Tech is in an upcycle driven by share gains in metal casing and NEV businesses, and margin improvement.

## Risks

Key risks that could impede the stock from reaching our target price include: 1) potential delay/acceleration in foldable iOS smartphone launch; 2) lower/higher-than-expected growth in global smartphone/tablet/automotive/XR and AI smart glasses; 3) reverse of electronic device tariff exemptions; 4) lower/higher-than-expected cover glass ASP; 5) lower/higher-than-expected automotive demand; and 6) FX volatility due to macro uncertainties.

## Lens Technology

## Company description

Lens Technology, which was founded in 2006, produces covers for smartphones, tablets, wearables, etc. Apple and Xiaomi are the company's two largest clients. Chinese OEM clients include Xiaomi and Huawei.

## Investment strategy

We rate Lens Technology as Buy on its dual growth engines of automotive and iPhone cover glass upgrade and metal casing share gain and assembly businesses.

## Valuation

Our target price of HK\$25.0 is based on 23.0x 2H26-1H27E EPS, a 25% discount to our A-share P/E target multiple. The H-share traded at a 25-26% discount to the A-share on 11 July 2025, its listing day. We believe the H-share will likely re-rate to components valuations of EMS due to the upcoming key upgrade cycle, driven by cover glass content upgrade in iOS foldable devices.

## Risks

Key risks that could impede the stock from reaching our target price include: 1) potential delay in foldable iOS smartphone launch, 2) lower-than-expected growth in global smartphone/tablet/automotive/XR and AI smart glasses, 3) reverse of electronic device tariff exemptions, 4) lower-than-expected cover glass ASP, 5) lower-than-expected automotive demand, and 5) FX volatility due to macro uncertainties.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

![](images/b5f0c42f51bdb2f2f5f2974d60c0a8c7736a3135a823ac7983e1b5828b0b5e06.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>14-Jul-25 21:09:04</td><td>*1</td><td>*26.00</td><td>19.00</td></tr><tr><td>2</td><td>27-Aug-25 01:20:36</td><td>1</td><td>*31.00</td><td>27.98</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>3</td><td>28-Oct-25 13:43:01</td><td>1</td><td>*32.00</td><td>27.36</td></tr><tr><td>4</td><td>12-Apr-26 21:17:15</td><td>1</td><td>*27.00</td><td>20.56</td></tr></table>

Rating/target price changes above reflect Eastern Time

## Lens Technology (300433.SZ)

Ratings and Target Price History
Fundamental Research

Analyst: Kyna Wong

![](images/af47d409205013c3ac70d1b68a8886155ce37ee0d352310507c28464d494545f.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>01-Aug-23 11:30:42</td><td>1</td><td>*15.00</td><td>12.33</td></tr><tr><td>2</td><td>23-Apr-24 15:50:13</td><td>1</td><td>*16.00</td><td>13.60</td></tr><tr><td>3</td><td>09-Jul-24 07:36:11</td><td>1</td><td>*21.00</td><td>19.46</td></tr><tr><td>4</td><td>26-Aug-24 13:30:16</td><td>1</td><td>*22.00</td><td>17.00</td></tr></table>

\*Indicates Change

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>5</td><td>20-Oct-24 21:22:40</td><td>1</td><td>*27.00</td><td>22.52</td></tr><tr><td>6</td><td>30-Mar-25 21:41:38</td><td>1</td><td>*30.00</td><td>25.61</td></tr><tr><td>7</td><td>21-Apr-25 00:59:24</td><td>1</td><td>*25.00</td><td>20.27</td></tr><tr><td>8</td><td>14-Jul-25 21:09:04</td><td>1</td><td>*32.00</td><td>23.26</td></tr></table>

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td></td><td>9 27-Aug-25 01:20:36</td><td>1</td><td>*37.00</td><td>31.40</td></tr><tr><td></td><td>10 28-Oct-25 13:43:01</td><td>1</td><td>*38.00</td><td>29.68</td></tr><tr><td></td><td>11 12-Apr-26 21:17:15</td><td>*2</td><td>*32.00</td><td>30.13</td></tr><tr><td></td><td>12 15-Apr-26 13:16:30</td><td>2</td><td>*30.00</td><td>29.59</td></tr></table>

Rating/target price changes above reflect Eastern Time

![](images/dcd81bc25929d235809d78c65dc36193418f6c05694ec0e526e1b1830450f4e2.jpg)

<table><tr><td colspan="2">Date14-Jul-25 17:09:04</td><td>ActionAdd STV</td><td>ExpectedDirectionUpside</td><td>ClosingPrice90 Days</td><td>23.26</td><td>Date212-Oct-25 23:06:26</td><td>ActionRemove STV</td><td>ExpectedDirectionUpside</td><td>ClosingPrice90 Days</td><td>31.90</td></tr></table>

CW - Catalyst Watch, STV - Short-Term View

![](images/11c4740e265fc791d13e8d0845ee9716ed8df21a8157bda4cbbad65a0039cdf1.jpg)  
CW - Catalyst Watch, STV - Short-Term View  
Rating/target price changes above reflect Eastern Time

Analysts' compensation is determined by Citi management and Citi's senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the "Firm"). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.

For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.

Unless stated otherwise neither the Research Analyst nor any member of their team has viewed the material operations of the Companies for which an investment view has been provided within the past 12 months.

For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product ("the Product"), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013, Attention: Legal/Compliance [E6WYB6412478]. In addition, the same important disclosures, with the exception of the Valuation and Risk assessments and historical disclosures, are contained on the Firm's disclosure website at https://www.citivelocity.com/cvr/eppublic/citi\_research\_disclosures. Valuation and Risk assessments can be found in the text of the most recent research note/report regarding the subject company. Pursuant to the Market Abuse Regulation a history of all Citi recommendations published during the preceding 12-month period can be accessed via Citi Velocity (https://www.citivelocity.com/cv2) or your standard distribution portal. Historical disclosures (for up to the past three years) will be provided upon request.

<table><tr><td colspan="7">Citi Equity Ratings Distribution</td></tr><tr><td></td><td colspan="3">12 Month Rating</td><td colspan="3">Catalyst Watch</td></tr><tr><td>Data current as of 01 Jul 2026</td><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Citi Global Fundamental Coverage (Neutral=Hold)</td><td>61%</td><td>32%</td><td>7%</td><td>36%</td><td>48%</td><td>16%</td></tr><tr><td>% of companies in each rating category that are investment banking clients</td><td>38%</td><td>42%</td><td>27%</td><td>42%</td><td>37%</td><td>36%</td></tr></table>

<table><tr><td>Any price(s) of instruments mentioned in recommendations are as of the prior day&#x27;s market close on the primary market for the instrument, unless otherwise stated.</td></tr><tr><td>The completion and first dissemination of any recommendations made within this research report are as of the Eastern date-time displayed at the top of the Product. If the Product references views of other analysts then please refer to the price chart or rating history table for the date/time of completion and first dissemination with respect to that view.</td></tr><tr><td>Regulations in various jurisdictions require that where a recommendation differs from any of the author&#x27;s previous recommendations concerning the same financial instrument or issuer that has been published during the preceding 12-month period that the change(s) and the date of that previous recommendation are indicated. For fundamental coverage please refer to the price chart or rating change history within this disclosure appendix or the issuer disclosure summary at https://www.citivelocity.com/cvr/eppublic/citi_research_disclosures.</td></tr><tr><td>Citi has implemented policies for identifying, considering and managing potential conflicts of interest arising as a result of publication or distribution of investment research. A description of these policies can be found at https://www.citivelocity.com/cvr/eppublic/citi_research_disclosures.</td></tr></table>

## Guide to Citi Fundamental Research Investment Ratings:

Citi stock recommendations include an investment rating and an optional risk rating to highlight high risk stocks. Risk rating takes into account both price volatility and fundamental criteria. Stocks will either have no risk rating or a High risk rating assigned.

Investment Ratings: Citi investment ratings are Buy, Neutral and Sell. Our ratings are a function of analyst expectations of expected total return ("ETR") and risk. ETR is the sum of the forecast price appreciation (or depreciation) plus the dividend yield for a stock within the next 12 months. The target price is based on a 12 month time horizon. The Investment rating definitions are: Buy (1) ETR of 15% or more or 25% or more for High risk stocks; and Sell (3) for negative ETR. Any covered stock not assigned a Buy or a Sell is a Neutral (2). For stocks rated Neutral (2), if an analyst believes that there are insufficient valuation drivers and/or investment catalysts to derive a positive or negative investment view, they may elect with the approval of Citi management not to assign a target price and, thus, not derive an ETR. Citi may suspend its rating and target price and assign "Rating Suspended" status for regulatory and/or internal policy reasons. Citi may also suspend its rating and target price and assign "Under Review" status for other exceptional circumstances (e.g. lack of information critical to the analyst's thesis, trading suspension) affecting the company and/or trading in the company's securities. In both such situations, the rating and target price will show as “—” and “-” respectively in the rating history price chart. Prior to 11 April 2022 Citi assigned "Under Review" status to both situations and prior to 11 Nov 2020 only in exceptional circumstances. As soon as practically possible, the analyst will publish a note re-establishing a rating and investment thesis. Investment ratings are determined by the ranges described above at the time of initiation of coverage, a change in investment and/or risk rating, or a change in target price (subject to limited management discretion). At times, the expected total returns may fall outside of these ranges because of market price movements and/or other short-term volatility or trading patterns. Such interim deviations will be permitted but will become subject to review by Research Management. Your decision to buy or sell a security should be based upon your personal investment objectives and should be made only after evaluating the stock's expected performance and risk.

## Catalyst Watch/Short Term Views ("STV") Ratings Disclosure:

Catalyst Watch and STV Upside/Downside calls: Citi may also include a Catalyst Watch or STV Upside or Downside call to indicate the analyst expects the share price to rise (fall) in absolute terms over a specified period of 30 or 90 days in reaction to one or more specific near-term catalysts or events impacting the company or the market. A Catalyst Watch will be published when Analyst confidence is high that an impact to share price will occur; it will be a STV when confidence level is moderate. A Catalyst Watch or STV Upside/Downside call will automatically expire at the end of the specified 30/90 day p

[中间内容因长度限制已省略]

ves, financial situation or needs of any particular

investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality,

accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.
"""
