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
# China Auto Manufacturers

## Jun NEV Database Update; CR5 at 57.1% (+0.1ppt MoM)

## CITI'S TAKE

CPCA announced Jun-26 NEV PV wholesales volume at 1.48mn units, +19% YoY/+10% MoM. Jun NEV penetration rate reached 62.8% (+13.0ppt YoY/+1.7ppt MoM). During the month, BEV PV wholesale volume was +27% YoY/+11% MoM to 980.9k units, and PHEV PV +6% YoY/+7% MoM to 500.5k units. 6M26 NEV PV wholesale volume +5% YoY to 6.79mn units, with BEV +8% YoY to 4.29mn units and PHEV +0% YoY to 2.50mn units. CR5 at 57.1% in Jun-26, +0.1ppt MoM/-1.4ppt YoY.

BYD logged wholesale volume of 397.3k units of sales, +5% YoY/+5% MoM, and Jun market share -3.6ppt YoY/-1.1ppt MoM to 26.8%. Song DM/Tai 7 PHEV +9%/+13% MoM to 67.5k/19.2k units, and Dolphin +15% MoM to 25.5k. BYD's BEV export sales mix was 43.6% in Jun-26 (-10.9ppt MoM/-19.9ppt YoY on PHEV ramp-up), with blended global export MSRP at Rmb345k (+3% MoM/+1% YoY).

Geely Jun NEV wholesale volume +30% YoY/+21% MoM to 158.8k units, with market share of 10.7% (+0.9ppt YoY/+1.0ppt MoM). Zeekr 7X -5% MoM to 7.3k units during Jun, Zeekr 9X/8X -24%/-18% MoM to 6.4k/4.7k units. Galaxy Starship 7/Starshine 8 PHEV +37%/+26% MoM to 19.4k/2.6k units.

Chery Jun NEV sales +61% YoY/+13% MoM to 106.9k units, with market share of 7.2% (+1.9ppt YoY/+0.2ppt MoM).

GWM Jun NEV sales -5% YoY/+14% MoM to 34.6k units. Ora 5 sales +157% MoM to 5.0k units, High Mountain logged 5.3k units in Jun (-12% MoM), Tank 400/500 PHEV logged 1.7/2.3k units (-17%/-20% MoM).

Tesla China Jun sales logged 89.1k units, +24% YoY and +4% MoM. Model 3/Y logged 32.6k/56.5k units of sales, +5%/+3% MoM.

NIO wholesales volume +63% YoY/+8% MoM to 40.6k units, and Jun market share reached 2.7% (+0.7ppt YoY/+0.0ppt MoM). ES8 -22% MoM to 9.0k units. ES6/EC6 -30%/-4% MoM to 1.2k/0.5k units. ET5/ET5T -12%/-19% MoM to 0.6k/1.8k units. Onvo L90 booked 3.5k units and L80 4.1k units in Jun.

XPeng wholesales unit +16% YoY/+25% MoM to 40.1k units with Jun mkt shr -0.1ppt YoY/+0.3ppt MoM to 2.7%. P7/G6 sales logged +10%/+1% MoM to 6.5k/6.6k units. MONA M03 booked 14.2k units (+0% MoM).

Li Auto Jun sales -15% YoY/-7% MoM to 30.9k units with Jun mkt shr -0.8ppt YoY/-0.4ppt MoM to 2.1%. L9/L8/L7/L6 logged +138%/+33%/-69%/-82% MoM to 6.1k/0.6k/0.8k/0.9k units in Jun. i6/i8 booked 21.5k/0.8k units in Jun (+3%/-50% MoM).

Huawei AITO Jun sales -30% YoY/+0% MoM to 30.3k units with mkt share -1.4ppt YoY/-0.2ppt MoM to 2.0%. Leapmotor Jun wholesale unit +95% YoY/+14% MoM to 93.4k units, with market share of 6.3% (+2.4ppt YoY/+0.3ppt MoM).

Jeff Chung $^{AC}$ +852-2501-2787 jeff.m.chung@citi.com

+852-2501-8483

kyle.wu@citi.com

Figure 1. NEV Wholesale Volumes (Units) of Major OEMs

<table><tr><td rowspan="2"></td><td colspan="6">Jun-26</td><td colspan="4">6M26</td></tr><tr><td>Sales</td><td>YoY</td><td>MoM</td><td>Mkt Shr</td><td>YoY</td><td>MoM</td><td>Sales</td><td>YoY</td><td>Mkt Shr</td><td>YoY</td></tr><tr><td>BYD</td><td>397,292</td><td>5%</td><td>5%</td><td>26.8%</td><td>-3.6ppt</td><td>-1.1ppt</td><td>1,777,375</td><td>-16%</td><td>26.2%</td><td>-6.4ppt</td></tr><tr><td>Geely</td><td>158,849</td><td>30%</td><td>21%</td><td>10.7%</td><td>0.9ppt</td><td>1.0ppt</td><td>794,536</td><td>10%</td><td>11.7%</td><td>0.5ppt</td></tr><tr><td>Chery</td><td>106,922</td><td>61%</td><td>13%</td><td>7.2%</td><td>1.9ppt</td><td>0.2ppt</td><td>441,678</td><td>29%</td><td>6.5%</td><td>1.2ppt</td></tr><tr><td>Leapmotor</td><td>93,376</td><td>95%</td><td>14%</td><td>6.3%</td><td>2.4ppt</td><td>0.3ppt</td><td>356,487</td><td>61%</td><td>5.3%</td><td>1.8ppt</td></tr><tr><td>Tesla China</td><td>89,091</td><td>24%</td><td>4%</td><td>6.0%</td><td>0.2ppt</td><td>-0.3ppt</td><td>467,949</td><td>28%</td><td>6.9%</td><td>1.3ppt</td></tr><tr><td>Chang&#x27;an</td><td>72,194</td><td>-17%</td><td>14%</td><td>4.9%</td><td>-2.2ppt</td><td>0.2ppt</td><td>325,829</td><td>-17%</td><td>4.8%</td><td>-1.3ppt</td></tr><tr><td>SAIC GM Wuling</td><td>69,419</td><td>12%</td><td>7%</td><td>4.7%</td><td>-0.3ppt</td><td>-0.1ppt</td><td>267,875</td><td>-26%</td><td>3.9%</td><td>-1.7ppt</td></tr><tr><td>SAIC Motor</td><td>64,931</td><td>307%</td><td>40%</td><td>4.4%</td><td>3.1ppt</td><td>1.0ppt</td><td>238,439</td><td>221%</td><td>3.5%</td><td>2.4ppt</td></tr><tr><td>Nio</td><td>40,597</td><td>63%</td><td>8%</td><td>2.7%</td><td>0.7ppt</td><td>0.0ppt</td><td>191,123</td><td>68%</td><td>2.8%</td><td>1.1ppt</td></tr><tr><td>XPeng Motor</td><td>40,126</td><td>16%</td><td>25%</td><td>2.7%</td><td>-0.1ppt</td><td>0.3ppt</td><td>165,977</td><td>-16%</td><td>2.4%</td><td>-0.6ppt</td></tr><tr><td>Xiaomi Auto</td><td>34,738</td><td>36%</td><td>6%</td><td>2.3%</td><td>0.3ppt</td><td>-0.1ppt</td><td>185,055</td><td>17%</td><td>2.7%</td><td>0.3ppt</td></tr><tr><td>GWM</td><td>34,610</td><td>-5%</td><td>14%</td><td>2.3%</td><td>-0.6ppt</td><td>0.1ppt</td><td>144,430</td><td>-10%</td><td>2.1%</td><td>-0.3ppt</td></tr><tr><td>BJEV</td><td>31,900</td><td>99%</td><td>33%</td><td>2.2%</td><td>0.9ppt</td><td>0.4ppt</td><td>120,240</td><td>55%</td><td>1.8%</td><td>0.6ppt</td></tr><tr><td>GAC NEV</td><td>31,431</td><td>29%</td><td>-9%</td><td>2.1%</td><td>0.2ppt</td><td>-0.4ppt</td><td>190,524</td><td>44%</td><td>2.8%</td><td>0.8ppt</td></tr><tr><td>Li Auto</td><td>30,895</td><td>-15%</td><td>-7%</td><td>2.1%</td><td>-0.8ppt</td><td>-0.4ppt</td><td>193,472</td><td>-5%</td><td>2.9%</td><td>-0.3ppt</td></tr><tr><td>AITO</td><td>30,345</td><td>-30%</td><td>0%</td><td>2.0%</td><td>-1.4ppt</td><td>-0.2ppt</td><td>160,609</td><td>-5%</td><td>2.4%</td><td>-0.2ppt</td></tr><tr><td>Brilliance BMW</td><td>2,103</td><td>-14%</td><td>-21%</td><td>0.1%</td><td>-0.1ppt</td><td>-0.1ppt</td><td>14,455</td><td>-50%</td><td>0.2%</td><td>-0.2ppt</td></tr><tr><td>Others</td><td>152,633</td><td>5%</td><td>2%</td><td>10.3%</td><td>-1.5ppt</td><td>-0.7ppt</td><td>751,765</td><td>17%</td><td>11.1%</td><td>1.2ppt</td></tr><tr><td>Total NEV PV</td><td>1,481,452</td><td>19%</td><td>10%</td><td></td><td></td><td></td><td>6,787,818</td><td>5%</td><td></td><td></td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, CPCA

Figure 2. BEV/PHEV Sector Wholesales  
![](images/f52f0b8de5ae0a9b5ea7bb77819ab42323750e9dfff6691655b731aa52babbdf.jpg)  
© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, CPCA

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

Analysts' compensation is determined by Citi management and Citi's senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the "Firm"). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.

For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.

Unless stated otherwise neither the Research Analyst nor any member of their team has viewed the material operations of the Companies for which an investment view has been provided within the past 12 months.

For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product ("the Product"), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013, Attention: Legal/Compliance [E6WYB6412478]. In addition, the same important disclosures, with the exception of the Valuation and Risk assessments and historical disclosures, are contained on the Firm's disclosure website at

https://www.citivelocity.com/cvr/eppublic/citi\_research\_disclosures. Valuation and Risk assessments can be found in the text of the most recent research note/report regarding the subject company. Pursuant to the Market Abuse Regulation a history of all Citi recommendations published during the preceding 12-month period can be accessed via Citi Velocity (https://www.citivelocity.com/cv2) or your standard distribution portal. Historical disclosures (for up to the past three years) will be provided upon request.

## Citi Equity Ratings Distribution

<table><tr><td></td><td colspan="3">12 Month Rating</td><td colspan="3">Catalyst Watch</td></tr><tr><td>Data current as of 01 Jul 2026</td><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Citi Global Fundamental Coverage (Neutral=Hold)</td><td>61%</td><td>32%</td><td>7%</td><td>36%</td><td>48%</td><td>16%</td></tr><tr><td>% of companies in each rating category that are investment banking clients</td><td>38%</td><td>42%</td><td>27%</td><td>42%</td><td>37%</td><td>36%</td></tr></table>

## Guide to Citi Fundamental Research Investment Ratings:

Citi stock recommendations include an investment rating and an optional risk rating to highlight high risk stocks. Risk rating takes into account both price volatility and fundamental criteria. Stocks will either have no risk rating or a High risk rating assigned.

Investment Ratings: Citi investment ratings are Buy, Neutral and Sell. Our ratings are a function of analyst expectations of expected total return ("ETR") and risk. ETR is the sum of the forecast price appreciation (or depreciation) plus the dividend yield for a stock within the next 12 months. The target price is based on a 12 month time horizon. The Investment rating definitions are: Buy (1) ETR of $15\%$ or more or $25\%$ or more for High risk stocks; and Sell (3) for negative ETR. Any covered stock not assigned a Buy or a Sell is a Neutral (2). For stocks rated Neutral (2), if an analyst believes that there are insufficient valuation drivers and/or investment catalysts to derive a positive or negative investment view, they may elect with the approval of Citi management not to assign a target price and, thus, not derive an ETR. Citi may suspend its rating and target price and assign “Rating Suspended” status for regulatory and/or internal policy reasons. Citi may also suspend its rating and target price and assign "Under Review" status for other exceptional circumstances (e.g. lack of information critical to the analyst's thesis, trading suspension) affecting the company and/or trading in the company's securities. In both such situations, the rating and target price will show as “—” and “-” respectively in the rating history price chart. Prior to 11 April 2022 Citi assigned “Under Review” status to both situations and prior to 11 Nov 2020 only in exceptional circumstances. As soon as practically possible, the analyst will publish a note re-establishing a rating and investment thesis. Investment ratings are determined by the ranges described above at the time of initiation of coverage, a change in investment and/or risk rating, or a change in target price (subject to limited management discretion). At times, the expected total returns may fall outside of these ranges because of market price movements and/or other short-term volatility or trading patterns. Such interim deviations will be permitted but will become subject to review by Research Management. Your decision to buy or sell a security should be based upon your personal investment objectives and should be made only after evaluating the stock's expected performance and risk.

## Catalyst Watch/Short Term Views ("STV") Ratings Disclosure:

Catalyst Watch and STV Upside/Downside calls: Citi may also include a Catalyst Watch or STV Upside or Downside call to indicate the analyst expects the share price to rise (fall) in absolute terms over a specified period of 30 or 90 days in reaction to one or more specific near-term catalysts or events impacting the company or the market. A Catalyst Watch will be published when Analyst confidence is high that an impact to share price will occur; it will be a STV when confidence level is moderate. A Catalyst Watch or STV Upside/Downside call will automatically expire at the end of the specified 30/90 day period. The Catalyst Watch will also be automatically removed if share price performance (calculated at market close) exceeds $15\%$ against the direction of the call (unless over-ridden by the analyst). The analyst may also remove a Catalyst Watch or STV call prior to the end of the specified period in a published research note. A Catalyst Watch/STV Upside or Downside call may be different from and does not affect a stock's fundamental equity rating, which reflects a longer-term total absolute return expectation. For purposes of FINRA ratings-distribution-disclosure rules, a Catalyst Watch/STV Upside call corresponds to a buy recommendation and a Catalyst Watch/STV Downside call corresponds to a sell recommendation. Any stock not assigned to a Catalyst Watch Upside, Catalyst Watch Downside, STV Upside, or STV Downside call is considered Catalyst Watch/STV No View. For purposes of FINRA ratings distribution-disclosure rules, we correspond Catalyst Watch/STV No View to Hold in our ratings distribution table for our Catalyst Watch/STV Upside/Downside rating system. However, we reiterate that we do not consider No View to be a recommendation. For all Catalyst Watch/STV Upside/Downside calls, risk exists that the catalyst(s) and associated share-price movement will not materialize as expected.

## RESEARCH ANALYST AFFILIATIONS / NON-US RESEARCH ANALYST DISCLOSURES

The legal entities employing the authors of this report are listed below (and their regulators are listed further herein). Non-US research analysts who have prepared this report (i.e., all research analysts listed below other than those identified as employed by Citi Global Markets Inc.) are not registered/qualified as research analysts with FINRA. Such research analysts may not be associated persons of the member organization (but are employed by an affiliate of the member organization) and therefore may not be subject to the FINRA Rule 2241 restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Citi Global Markets Asia Limited

Jeff Chung; Kyle Wu

## OTHER DISCLOSURES

<table><tr><td>Any price(s) of instruments mentioned in recommendations are as of the prior day&#x27;s market close on the primary market for the instrument, unless otherwise stated.</td></tr><tr><td>The completion and first dissemination of any recommendations made within this research report are as of the Eastern date-time displayed at the top of the Product. If the Product references views of other analysts then please refer to the price chart or rating history table for the date/time of completion and first dissemination with respect to that view.</td></tr><tr><td>Regulations in various jurisdictions require that where a recommendation differs from any of the author&#x27;s previous recommendations concerning the same financial instrument or issuer that has been published during the preceding 12-month period that the change(s) and the date of that previous recommendation are indicated. For fundamental coverage please refer to the price chart or rating change history within this disclosure appendix or the issuer disclosure summary at https://www.citivelocity.com/cvr/eppublic/citi_research_disclosures.</td></tr><tr><td>Citi has implemented policies for identifying, considering and managing potential conflicts of interest arising as a result of publication or distribution of investment research. A description of these policies can be found at https://www.citivelocity.com/cvr/eppublic/citi_research_disclosures.</td></tr><tr><td>The proportion of all Citi recommendations that were the equivalent to &quot;Buy&quot;, &quot;Hold&quot;, &quot;Sell&quot; at the end of each quarter over the prior 12 months (with the % of these that had received investment firm services from Citi in the prior 12 months shown in brackets) is as follows; Q1 2026 Buy 33%(63%), Hold 44% (52%), Sell 23% (46%), RV 0.5% (89%): Q4 2025 Buy 33% (63%), Hold 44% (50%), Sell 23% (46%), RV 0.4% (91%); Q3 2025 Buy 33% (61%), Hold 44% (52%), Sell 23% (50%), RV 0.4% (80%); Q2 2025 Buy 33%(63%), Hold 44% (51%),

[中间内容因长度限制已省略]

ar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a

subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
