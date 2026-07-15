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
© 2026 Citi Inc. No redistribution without Citi's written permission.
Source: Citi, Company Reports

13 Jul 2026 20:49:25 ET | 11 pages

# Shengyi Technology (600183.SS)

## Preliminary 1H26 Profit Alert Beats Citi Expectation

## CITI'S TAKE

Shengyi Technology (600183.SS, Buy): 1H26 NP guided to Rmb3.1-3.3bn, up 117-131% yoy, leaving a record \~Rmb2.0bn for 2Q26 at midpoint, up \~135% yoy against a 2Q25 comp that itself rose 61%. Stripping out \~Rmb380mn of non-operating gains (vs Rmb48mn in 1H25), recurring NP still doubled, which beat our expectation. This is primarily driven by mix upgrade towards AI-CCL carrying much higher GM than non-CCL. Recall we raised 2026-28E earnings by 28-34% in June on AI-CCL mix upgrade for rising from \~10% of total volume in the last year, 15% in mid-2026 and toward \~20% by end-2026 for Vera Rubin, with higher blended GM thru the mix. Interim report is due 15 Aug. Amongst AI-CCL/PCB chain, we prefer Shengyi to Shennan. Shennan also announced a preliminary 1H26 profit alert today with implied 2Q recurring growth of \~71% vs Shengyi's \~112%. Reiterate Buy on Shengyi Tech given recent share-price correction.

Figure 1. Quarterly P&L

<table><tr><td>Quarterly P&amp;L (Rmb mn)</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E Low</td><td>2Q26E Mid</td><td>2Q26E High</td></tr><tr><td>Revenue</td><td>5,611</td><td>7,069</td><td>7,934</td><td>7,818</td><td>8,141</td><td></td><td></td><td></td></tr><tr><td>COGS</td><td>4,231</td><td>5,170</td><td>5,701</td><td>5,802</td><td>5,854</td><td></td><td></td><td></td></tr><tr><td>Gross profit</td><td>1,380</td><td>1,898</td><td>2,233</td><td>2,015</td><td>2,288</td><td></td><td></td><td></td></tr><tr><td>Business tax</td><td>27</td><td>38</td><td>33</td><td>53</td><td>41</td><td></td><td></td><td></td></tr><tr><td>Selling expense</td><td>117</td><td>145</td><td>140</td><td>135</td><td>135</td><td></td><td></td><td></td></tr><tr><td>Administrative expens</td><td>538</td><td>636</td><td>644</td><td>720</td><td>671</td><td></td><td></td><td></td></tr><tr><td>Operating profit</td><td>699</td><td>1,079</td><td>1,416</td><td>1,107</td><td>1,441</td><td></td><td></td><td></td></tr><tr><td>Finance expense</td><td>14</td><td>19</td><td>33</td><td>31</td><td>38</td><td></td><td></td><td></td></tr><tr><td>Other gain</td><td>49</td><td>71</td><td>40</td><td>82</td><td>54</td><td></td><td></td><td></td></tr><tr><td>Investment income</td><td>14</td><td>20</td><td>20</td><td>89</td><td>9</td><td></td><td></td><td></td></tr><tr><td>Fair value change gain</td><td>(6)</td><td>6</td><td>6</td><td>10</td><td>79</td><td></td><td></td><td></td></tr><tr><td>Asset impairment loss</td><td>(23)</td><td>(32)</td><td>(51)</td><td>(55)</td><td>(14)</td><td></td><td></td><td></td></tr><tr><td>Asset disposal gain</td><td>(0)</td><td>(3)</td><td>(5)</td><td>(2)</td><td>(0)</td><td></td><td></td><td></td></tr><tr><td colspan="3">Others (plug: adjusted OP items vs reported OP)</td><td>(65)</td><td>(62)</td><td>(77)</td><td></td><td></td><td></td></tr><tr><td>Reported operating profit</td><td>719</td><td>1,123</td><td>1,393</td><td>1,199</td><td>1,531</td><td></td><td></td><td></td></tr><tr><td>non-operating income</td><td>0</td><td>2</td><td>1</td><td>2</td><td>3</td><td></td><td></td><td></td></tr><tr><td>non-operating expense</td><td>(0)</td><td>3</td><td>3</td><td>16</td><td>3</td><td></td><td></td><td></td></tr><tr><td>Profit before tax</td><td>719</td><td>1,127</td><td>1,391</td><td>1,184</td><td>1,530</td><td></td><td></td><td></td></tr><tr><td>Tax expense</td><td>84</td><td>134</td><td>150</td><td>156</td><td>198</td><td></td><td></td><td></td></tr><tr><td>MI</td><td>71</td><td>125</td><td>224</td><td>138</td><td>174</td><td></td><td></td><td></td></tr><tr><td>Net profit</td><td>564</td><td>868</td><td>1,017</td><td>891</td><td>1,158</td><td>1,941</td><td>2,040</td><td>2,140</td></tr><tr><td>YoY change</td><td>43.8%</td><td>60.6%</td><td>131.2%</td><td>143.1%</td><td>105.5%</td><td>123.7%</td><td>135.2%</td><td>146.6%</td></tr><tr><td>Recurring net profit</td><td>560</td><td>819</td><td>1,001</td><td>795</td><td>1,083</td><td>1,636</td><td>1,736</td><td>1,835</td></tr><tr><td>YoY change</td><td>45.0%</td><td>56.6%</td><td>147.7%</td><td>119.6%</td><td>93.5%</td><td>99.9%</td><td>112.0%</td><td>124.2%</td></tr><tr><td colspan="9">YoY growth</td></tr><tr><td>Revenue</td><td>26.9%</td><td>35.8%</td><td>55.1%</td><td>38.5%</td><td>45.1%</td><td></td><td></td><td></td></tr><tr><td>Gross profit</td><td>46.5%</td><td>67.4%</td><td>90.9%</td><td>61.6%</td><td>65.7%</td><td></td><td></td><td></td></tr><tr><td>Operating profit</td><td>57.6%</td><td>86.4%</td><td>189.3%</td><td>127.4%</td><td>106.3%</td><td></td><td></td><td></td></tr><tr><td>Reported operating profit</td><td>58.0%</td><td>76.4%</td><td>146.0%</td><td>189.1%</td><td>113.0%</td><td></td><td></td><td></td></tr><tr><td>PBT</td><td>58.2%</td><td>77.3%</td><td>145.9%</td><td>187.4%</td><td>113.0%</td><td></td><td></td><td></td></tr><tr><td>NP</td><td>43.8%</td><td>60.6%</td><td>131.2%</td><td>143.1%</td><td>105.5%</td><td></td><td></td><td></td></tr><tr><td>Recurring NP</td><td>45.0%</td><td>56.6%</td><td>147.7%</td><td>119.6%</td><td>93.5%</td><td></td><td></td><td></td></tr><tr><td>Margins and ratios</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td></td><td></td><td></td></tr><tr><td>Gross margin</td><td>24.6%</td><td>26.9%</td><td>28.1%</td><td>25.8%</td><td>28.1%</td><td></td><td></td><td></td></tr><tr><td>Adjusted operating margin</td><td>12.4%</td><td>15.3%</td><td>17.8%</td><td>14.2%</td><td>17.7%</td><td></td><td></td><td></td></tr><tr><td>Net margin</td><td>10.0%</td><td>12.3%</td><td>12.8%</td><td>11.4%</td><td>14.2%</td><td></td><td></td><td></td></tr></table>

<table><tr><td colspan="2">Buy</td></tr><tr><td>Price (13 Jul 26 15:00)</td><td>Rmb134.450</td></tr><tr><td>Target price</td><td>Rmb195.000</td></tr><tr><td>Expected share price return</td><td>45.0%</td></tr><tr><td>Expected dividend yield</td><td>1.4%</td></tr><tr><td>Expected total return</td><td>46.4%</td></tr><tr><td>Market Cap</td><td>Rmb326,580MUS$48,244M</td></tr></table>

Eric Lau $^{AC}$ +852-2501-2726
eric.h.lau@citi.com

Alice Cai
+852-2501-2704
alice.cai@citi.com

Andy Li
+852-2501-2597
andy.li@citi.com

## Shengyi Technology

## Valuation

Our target price for SYTECH of Rmb195 is based on a 56x 2027E PE, +4SD. We employ a PE target multiple at +4SD reflecting Shengyi demonstrating persistent increase of wallet share at NVDA from GB200 to GB300 and further in Vera Rubin. We still see continued earnings upgrade opportunity for 2026E-28E backed by rising % of revenue from AI-CCL in coming years. The premium PE target over mean is justified, in our view, based on our 3-year EPS CAGR of 45% over 2025-28E, following a \~24% decline in 2023. Our target PE implies 1.2x PEG which looks comparable with major regional peers. We believe its high PE target over mean is appropriate given: 1) SYTECH's strong track record of winning market share in the global CCL market (from 8% in 2007 to 13% in 2024); 2) SYTECH's technology edge as the first to enter Nvidia AI supply chain among China CCL players; and 3) increasing premium for domestic component sourcing, underpinned by bans preventing dealing with US companies to source components.

## Risks

Key downside risks to achieving our target price include: 1) lower-than-expected demand for AI-CCL order, 2) subdued China consumption, and 3) worse-than-expected capex on 5G/IoT products. Key upside risks to achieving our target price include: 1) secure of ASIC-based customers for CCL orders, 2) better-than-expected macro-economic conditions in China, 3) better-than-expected operating margin on higher rev growth due to high operating leverage, and 4) stronger-than-expected AI demand and consumption subsidy.

## Shennan Circuit

(002916.SZ; Rmb393.59; 1; 13 Jul 26; 15:00)

## Valuation

Our target price for Shennan shares of RMB360 is based on forward 2027E PE target of 38x at +2sd over mean as we roll over from prior 43x PE to 38x PE (at +2SD) following the release of 1Q26 results beat. We employ +2SD over mean for Shennan earnings upcycle under AI-PCB demand. This is backed by 3-yr EPS CAGR of 32% thru 2028E. The company's status is one of the key proxies on AI server and BT substrate – both contributed \~75% of total sales. The PE target reflects the sustained PCB industry upcycle with datacenter server, AI server, EV, etc. during 2026-28E, though the 5G base station installations maintain modest growth in China this year. The start-up loss for new plant for Guangzhou FC-BGA Ph1 took place in 2025 but this would start operate breakeven from 2026 which is about 1yr earlier than prior guidance of 2027. Our target PE of 38x forward equates to a \~20-30% premium to the sector average, which we see as warranted given: 1) Shennan's leading position in the communication PCB sector, enhanced by its SOE background; and 2) the company's technology leadership position on AI-server, communication, datacenters, autos (on ADAS) among peers with the potential to deliver a higher margin on a more advanced technology curve.

## Risks

Downside risks that could hinder the shares from reaching to our target price include: 1) Foreign AI server boom and other leading players is slower than expected; 2) weaker-than-expected demand on auto and ADAS system; 3) lower-than-expected profit of BT substrate new plant in Wuxi; and 4) higher-than-expected laminate cost inflation.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

Analyst: Eric Lau

![](images/5b44fe88450399504a978a6152aa9e01b2c8618e523ef7d275d5358a3f2c4bb7.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>18-Aug-23 11:43:29</td><td>*3</td><td>*12.00</td><td>14.45</td></tr><tr><td>2</td><td>26-Oct-23 16:01:40</td><td>*1</td><td>*19.00</td><td>16.27</td></tr><tr><td>3</td><td>28-Mar-24 17:00:11</td><td>1</td><td>*20.00</td><td>17.54</td></tr><tr><td>4</td><td>26-Apr-24 12:34:42</td><td>1</td><td>*22.50</td><td>16.83</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>5</td><td>22-May-24 19:52:26</td><td>1</td><td>*27.00</td><td>20.33</td></tr><tr><td>6</td><td>20-Jan-25 04:55:26</td><td>1</td><td>*35.00</td><td>29.06</td></tr><tr><td>7</td><td>20-Feb-25 09:48:03</td><td>1</td><td>*41.00</td><td>33.72</td></tr><tr><td>8</td><td>14-Jul-25 11:40:03</td><td>1</td><td>*43.80</td><td>32.91</td></tr></table>

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>9</td><td>17-Aug-25 18:25:36</td><td>1</td><td>*60.00</td><td>44.83</td></tr><tr><td>10</td><td>28-Oct-25 11:39:58</td><td>1</td><td>*83.00</td><td>67.39</td></tr><tr><td>11</td><td>26-Apr-26 19:07:57</td><td>1</td><td>*96.00</td><td>72.63</td></tr><tr><td>12</td><td>11-Jun-26 09:01:12</td><td>1</td><td>*195.00</td><td>149.73</td></tr></table>

Rating/target price changes above reflect Eastern Time

## Shennan Circuit (002916.SZ)

Ratings and Target Price History
Fundamental Research

Analyst: Eric Lau

![](images/2ef5c540aaad2697648d357184d9b38d91423e09f3a773c54a16f661ad839aa7.jpg)

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>23-Aug-23 12:40:58</td><td>3</td><td>*36.92</td><td>47.80</td></tr><tr><td>2</td><td>14-Mar-24 12:44:06</td><td>3</td><td>*44.62</td><td>64.29</td></tr><tr><td>3</td><td>15-Apr-24 18:02:05</td><td>3</td><td>*57.69</td><td>75.37</td></tr><tr><td>4</td><td>12-Sep-24 19:07:57</td><td>3</td><td>*61.54</td><td>70.62</td></tr></table>

\*Indicates Change

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>5</td><td>12-Mar-25 12:31:10</td><td>3</td><td>*73.08</td><td>97.75</td></tr><tr><td>6</td><td>23-Apr-25 13:51:13</td><td>*1</td><td>*103.85</td><td>85.15</td></tr><tr><td>7</td><td>05-Jun-25 06:00:50</td><td>1</td><td>*103.85</td><td>92.42</td></tr><tr><td>8</td><td>27-Aug-25 18:20:49</td><td>1</td><td>*201.00</td><td>169.50</td></tr></table>

<table><tr><td></td><td>Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>9</td><td>18-Sep-25 12:35:26</td><td>1</td><td>*230.00</td><td>197.47</td></tr><tr><td>10</td><td>29-Oct-25 12:55:41</td><td>1</td><td>*281.00</td><td>227.80</td></tr><tr><td>11</td><td>12-Mar-26 16:42:37</td><td>1</td><td>*320.00</td><td>252.61</td></tr><tr><td>12</td><td>24-Apr-26 13:03:49</td><td>1</td><td>*360.00</td><td>301.36</td></tr></table>

Rating/target price changes above reflect Eastern Time

![](images/001279074be8704e043ff7adf27eb44292b1850fc92f128966e12e9964e83867.jpg)

![](images/12da2f607f382e71993ff59c8912e61000c27c6f6ecd2cd610853a93902d4a3f.jpg)  
CW - Catalyst Watch, STV - Short-Term View  
Rating/target price changes above reflect Eastern Time

Citi Global Markets Inc. or its affiliates has received compensation for investment banking services provided within the past 12 months from Shennan Circuit.

Citi Global Markets Inc. or its affiliates expects to receive or intends to seek, within the next three months, compensation for investment banking services from Shennan Circuit.

Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from Shennan Circuit in the past 12 months.

Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as investment banking client(s): Shennan Circuit.

Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: Shennan Circuit.

Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, non-securities-related: Shennan Circuit.

Citi Global Markets Inc. and/or its affiliates has a significant financial interest in relation to Shennan Circuit. (For an explanation of the determination of significant financial interest, please refer to the policy for managing conflicts of interest which can be found at www.citiVelocity.com.)

Analysts' compensation is determined by Citi management and Citi's senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the “Firm”). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive

compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.

For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.

Unless stated otherwise neither the Research Analyst nor any member of their team has viewed the material operations of the Companies for which an investment view has been provided within the past 12 months.

For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product ("the Product"), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013,

Citi Equity Ratings Distribution

Attention: Legal/Compliance [E6WYB6412478]. In addition, the same important disclosures, with the exception of the Valuation and Risk assessments and historical disclosures, are contained on the Firm's disclosure website at https://www.citivelocity.com/cvr/eppublic/citi\_research\_disclosures. Valuation and Risk assessments can be found in the text of the most recent research note/report regarding the subject company. Pursuant to the Market Abuse Regulation a history of all Citi recommendations published during the preceding 12-month period can be accessed via Citi Velocity (https://www.citivelocity.com/cv2) or your standard distribution portal. Historical disclosures (for up to the past three years) will be provided upon request.

<table><tr><td></td><td colspan="3">12 M

[中间内容因长度限制已省略]

lar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
