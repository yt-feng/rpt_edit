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
24 Jul 2026 06:00:00 ET | 11 pages

# US Semiconductors and Semiconductor Equipment

Summer Sell-off; Fundamentals Intact; Prefer Semi Caps to Semis

## CITI'S TAKE

We view the SOX pullback on surging oil prices, rising bond yields, and AI spending concerns as a buying opportunity. Fundamentally, data center remains the strongest end market (34% of semi TAM) and is on track to exceed the entire semiconductor TAM by 2030E. Recovery is underway in Auto and Industrial (21%), while demand from PCs, handsets, and consumer electronics (42%) continues to weaken due to memory cost inflation and supply constraints (see Figure 2). We recap key highlights from earnings so far and note that consensus 2026E/2027E revenue estimates for companies that reported increased 4%/7% on average, while EPS estimates rose 7%/8%. We prefer semi caps to semis on higher estimate revisions driven by capex increases.

INTC/TSMC/TSLA Capex Outlook All Very Positive for SCE - Intel highlighted meaningful foundry progress and raised 2026 capex guidance to over \$20Bn from \~\$18Bn previously, driven primarily by tools with 40% YoY growth. Intel is aggressively locking in equipment orders, accelerating clean-room buildouts, and securing key substrate and memory supply. With increased confidence in customer demand across multiple end markets and a strong advanced packaging backlog, Intel expects 2027 capex to be significantly higher than 2026, with most investments directed toward U.S. manufacturing. TSMC, during its Q2 earnings call, raised 2026 capex again to \$60-64Bn from nearly \$56Bn, driven by stronger-than-expected AI demand and higher equipment costs. Given the large supply/demand gap, management commented that capex over the next three years will be significantly higher than the prior three years and announced an additional \$100Bn investment in Arizona (now \$265Bn total), including roughly four additional fabs. Tesla reiterated that 2026 capex will exceed \$25Bn and continue growing over the next 2-3 years, including semiconductor manufacturing investments. On Terafab, management disclosed that equipment orders have already been placed for its Austin development fab, and Elon Musk indicated the company expects to announce a location and provide more detailed plans soon. On the backend, Amkor announced a \$1.5Bn multi-year partnership with NVIDIA to support U.S. advanced packaging capacity, with NVIDIA providing a prepayment to support the expansion. Amkor previously outlined a \$7Bn Arizona investment plan, with Phase 1 construction underway, HVM beginning in 2028, and full buildout by 2030.

AMD Lifts CPU TAM - At AMD AI Day, the company raised its Data Center AI Accelerator TAM forecast from \~\$200B in 2025 to \~\$1.4T by 2030E (>45% CAGR) and its Data Center CPU TAM from \~\$26B to \~\$220B (>50% CAGR). AMD's CPU TAM lift is positive for INTC.

Atif Malik $^{AC}$ +1-415-951-1892
atif.malik@citi.com

Kelsey Chia, CFA
+1-415-951-1791
kelsey.chia@citi.com

Elizabeth Sun, CFA
+1-212-816-3308
elizabeth.sun@citi.com

Adrienne Colby
+1-212-816-8975
adrienne.colby@citi.com

See Appendix A-1 for Analyst Certification, Important Disclosures and Research Analyst Affiliations

Figure 1. AMD's Updated CPU TAM  
![](images/52a1bb5a102de1c31ccf60a15a057dd7edd4e116c8ce428207f24f6c187ffe6b.jpg)

Google Capex Positive for Networking & Compute- With its Jun-Q results, GOOGL raised its outlook for FY26 capex by \$15Bn at the midpoint, as demand for capacity continues to accelerate and higher component pricing pushes up the company's technical infrastructure spend. Projected FY26 capex in the range of \$195-205Bn is more than 2x FY25 spend of \$91Bn and ahead of Citi's prior \$190Bn outlook. Importantly, GOOGL reiterated prior expectations for FY27 capex to "increase significantly." We note Jun-Q capex of \~\$45Bn, up 100% Y/Y was split 60%/ 40% between compute/ data centers and networking. We view GOOGL's capex outlook positively with regards to the broader hyperscale spending environment and specifically for CLS, AVGO, and NVDA in our coverage.

Analog Commentary: TXN and STM both reported a broad-based recovery with Industrial revenue up roughly 30% YoY, Automotive up mid-teens YoY, and Personal Electronics up high-single digits YoY. AI data center buildouts and new power architectures are emerging as incremental drivers of analog demand, with TXN's Data Center business expected to double YoY to \$3.1Bn in 2026 and STM raising its targets to \$1Bn in 2026 and \$2Bn in 2027, roughly double prior expectations. STM reported tightening supply conditions and lengthening lead times, while TXN leverages its manufacturing capacity to maintain industry-leading lead times. Both companies are implementing price increases, with TXN expecting stronger pricing through 2026. We see the read as positive for ADI, MCHP, NXPI, and ON.

Figure 2. Semiconductor End-Market Demand

<table><tr><td>End Market</td><td>% of Semi TAM</td><td>3Q23</td><td>4Q23</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25E</td><td>4Q25</td><td>1Q26</td><td>2Q26</td><td>3Q26E</td></tr><tr><td>PC</td><td>19%</td><td>stable</td><td>stable</td><td>stable</td><td>stable</td><td>stable</td><td>stable</td><td>stable</td><td>mixed</td><td>stable</td><td>stable</td><td>falling</td><td>falling</td><td>falling</td></tr><tr><td>Wireless</td><td>16%</td><td>weak</td><td>stable</td><td>stable</td><td>stable</td><td>stable</td><td>stable</td><td>stable</td><td>stable</td><td>stable</td><td>stable</td><td>falling</td><td>falling</td><td>falling</td></tr><tr><td>Industrial</td><td>10%</td><td>mixed</td><td>falling</td><td>falling</td><td>falling</td><td>mixed</td><td>weak</td><td>mixed</td><td>stable</td><td>improving</td><td>improving</td><td>improving</td><td>improving</td><td>improving</td></tr><tr><td>Consumer</td><td>7%</td><td>weak</td><td>weak</td><td>weak</td><td>stable</td><td>stable</td><td>mixed</td><td>stable</td><td>stable</td><td>improving</td><td>improving</td><td>falling</td><td>falling</td><td>falling</td></tr><tr><td>Comm Infra</td><td>3%</td><td>weak</td><td>weak</td><td>weak</td><td>weak</td><td>improving</td><td>improving</td><td>mixed</td><td>mixed</td><td>improving</td><td>improving</td><td>improving</td><td>improving</td><td>improving</td></tr><tr><td>Automotive</td><td>11%</td><td>mixed</td><td>falling</td><td>falling</td><td>falling</td><td>mixed</td><td>mixed</td><td>weak</td><td>weak</td><td>weak</td><td>mixed</td><td>mixed</td><td>improving</td><td>improving</td></tr><tr><td>Data Center</td><td>34%</td><td>mixed</td><td>mixed</td><td>improving</td><td>improving</td><td>improving</td><td>good</td><td>good</td><td>good</td><td>strong</td><td>strong</td><td>strong</td><td>strong</td><td>strong</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.

Figure 3. C26 and C27 EPS Changes Post Earnings (Local Currency)

<table><tr><td rowspan="2"></td><td colspan="3">2026 Consensus EPS</td><td colspan="3">2027 Consensus EPS</td></tr><tr><td>Pre-earnings</td><td>Post-earnings</td><td>De ta</td><td>Pre-earnings</td><td>Post-earnings</td><td>De ta</td></tr><tr><td>STLIFA-PAR</td><td>$1.13</td><td>$1.15</td><td>1%</td><td>$2.22</td><td>$2.18</td><td>1%</td></tr><tr><td>BES-AL</td><td>$4.14</td><td>$4.18</td><td>1%</td><td>$5.43</td><td>$5.42</td><td>0%</td></tr><tr><td>VTC</td><td>$1.09</td><td>$1.19</td><td>9%</td><td>$1.82</td><td>$1.72</td><td>6%</td></tr><tr><td>ASY-AL</td><td>$37.24</td><td>$37.35</td><td>18%</td><td>$51.43</td><td>$51.37</td><td>18%</td></tr><tr><td>TXN</td><td>$7.76</td><td>$8.54</td><td>10%</td><td>$9.10</td><td>$9.10</td><td>13%</td></tr><tr><td>VACN-SWX</td><td>$10.35</td><td>$10.35</td><td>3%</td><td>$15.15</td><td>$15.15</td><td>10%</td></tr><tr><td>Average</td><td></td><td></td><td>7%</td><td></td><td></td><td>8%</td></tr><tr><td>Median</td><td></td><td></td><td>6%</td><td></td><td></td><td>8%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, FactSet

Figure 4. C26 and C27 Sales Changes Post Earnings (Local Currency)

<table><tr><td rowspan="2"></td><td colspan="3">2026 Consensus Sales</td><td colspan="3">2027 Consensus Sales</td></tr><tr><td>Pre-earnings</td><td>Post-earnings</td><td>De ta</td><td>Pre-earnings</td><td>Post-earnings</td><td>De ta</td></tr><tr><td>STJIFA-PAR</td><td>$12,528</td><td>$12.5-3</td><td>0%</td><td>$1-889</td><td>$1-300</td><td>1%</td></tr><tr><td>BES-XL</td><td>$655</td><td>$58</td><td>1%</td><td>$1,028</td><td>$1,128</td><td>0%</td></tr><tr><td>VTO</td><td>$64-87</td><td>$55-44</td><td>9%</td><td>$53,857</td><td>$57-88</td><td>15%</td></tr><tr><td>ASML</td><td>$45,778</td><td>$4-878</td><td>9%</td><td>$57,188</td><td>$53-43</td><td>11%</td></tr><tr><td>TXN</td><td>$21,128</td><td>$21,855</td><td>4%</td><td>$23,687</td><td>$24-83</td><td>6%</td></tr><tr><td>VACN-SWX</td><td>$1,300</td><td>$1,328</td><td>2%</td><td>$1,858</td><td>$1,828</td><td>8%</td></tr><tr><td>Average</td><td></td><td></td><td>4%</td><td></td><td></td><td>7%</td></tr><tr><td>Voclar</td><td></td><td></td><td>3%</td><td></td><td></td><td>7%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, FactSet

## Companies Mentioned:

Analog Devices (ADI.O; US\$380.2; 1; 23 Jul 26; 16:00) | Broadcom Inc (AVGO.O; US\$392.47; 1; 23 Jul 26; 16:00) | Celestica (CLS.N; US\$334.75; 1; 23 Jul 26; 16:00) | Intel Corp (INTC.O; US\$100.23; 1; 23 Jul 26; 16:00) | Microchip Technology (MCHP.O; US\$81.35; 1; 23 Jul 26; 16:00) | NVIDIA Corp (NVDA.O; US\$208.76; 1; 23 Jul 26; 16:00) | NXP Semiconductors NV (NXPI.O; US\$277.29; 1; 23 Jul 26; 16:00) | ON Semiconductor (ON.O; US\$90.13; 2; 23 Jul 26; 16:00)

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

<table><tr><td>A member of Citi&#x27;s Board of Directors is also on the Board of Directors of Analog Devices.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates beneficially owns 1% or more of any class of common equity securities of ON Semiconductor. This position reflects information available as of the prior business day.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates has a net long position of 0.5% or more of any class of common equity securities of Microchip Technology,NXP Semiconductors NV,ON Semiconductor.</td></tr><tr><td>Within the past 12 months, Citi Global Markets Inc. or its affiliates has acted as manager or co-manager of an offering of securities of Broadcom Inc,Intel Corp,NVIDIA Corp,ON Semiconductor.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates has received compensation for investment banking services provided within the past 12 months from Analog Devices,Broadcom Inc,Celestica,Intel Corp,NVIDIA Corp,NXP Semiconductors NV,ON Semiconductor.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates expects to receive or intends to seek, within the next three months, compensation for investment banking services from Celestica,Intel Corp.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates received compensation for products and services other than investment banking services from Analog Devices,Broadcom Inc,Celestica,Intel Corp,NVIDIA Corp,NXP Semiconductors NV,ON Semiconductor in the past 12 months.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as investment banking client(s): Analog Devices,Broadcom Inc,Celestica,Intel Corp,NVIDIA Corp,NXP Semiconductors NV,ON Semiconductor.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, securities-related: Analog Devices,Broadcom Inc,Celestica,Intel Corp,NVIDIA Corp,NXP Semiconductors NV,ON Semiconductor.</td></tr><tr><td>Citi Global Markets Inc. or its affiliates currently has, or had within the past 12 months, the following as clients, and the services provided were non-investment-banking, non-securities-related: Analog Devices,Broadcom Inc,Celestica,Intel Corp,NVIDIA Corp,NXP Semiconductors NV,ON Semiconductor.</td></tr><tr><td>Citi Global Markets Inc. and/or its affiliates has a significant financial interest in relation to Broadcom Inc,Intel Corp,NVIDIA Corp. (For an explanation of the determination of significant financial interest, please refer to the policy for managing conflicts of interest which can be found at www.citiVelocity.com.)</td></tr><tr><td>Analysts&#x27; compensation is determined by Citi management and Citi&#x27;s senior management and is based upon activities and services intended to benefit the investor clients of Citi Global Markets Inc. and its affiliates (the &quot;Firm&quot;). Compensation is not linked to specific transactions or recommendations. Like all Firm employees, analysts receive compensation that is impacted by overall Firm profitability which includes investment banking, sales and trading, and principal trading revenues. One factor in equity research analyst compensation is arranging corporate access events between institutional clients and the management teams of covered companies. Typically, company management is more likely to participate when the analyst has a positive view of the company.</td></tr><tr><td>For financial instruments recommended in the Product in which the Firm is not a market maker, the Firm is a liquidity provider in such financial instruments (and any underlying instruments) and may act as principal in connection with transactions in such instruments. The Firm is a regular issuer of traded financial instruments linked to securities that may have been recommended in the Product. The Firm regularly trades in the securities of the issuer(s) discussed in the Product. The Firm may engage in securities transactions in a manner inconsistent with the Product and, with respect to securities covered by the Product, will buy or sell from customers on a principal basis.</td></tr></table>

Unless stated otherwise neither the Research Analyst nor any member of their team has viewed the material operations of the Companies for which an investment view has been provided within the past 12 months. For important disclosures (including copies of historical disclosures) regarding the companies that are the subject of this Citi product ("the Product"), please contact Citi, 388 Greenwich Street, 6th Floor, New York, NY, 10013, Attention: Legal/Compliance [E6WYB6412478]. In addition, the same important disclosures, with the exception of the Valuation and Risk assessments and historical disclosures, are contained on the Firm's disclosure website at https://www.citivelocity.com/cvr/eppublic/citi\_research\_disclosures. Valuation and Risk assessments can be found in the text of the most recent research note/report regarding the subject company. Pursuant to the Market Abuse Regulation a history of all Citi recommendations published during the preceding 12-month period can be accessed via Citi Velocity (https://www.citivelocity.com/cv2) or your standard distribution portal. Historical disclosures (for up to the past three years) will be provided upon request.

Citi Equity Ratings Distribution

<table><tr><td rowspan="2">Data current as of 01 Jul 2026</td><td colspan="3">12 Month Rating</td><td colspan="3">Catalyst Watch</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Citi Global Fundamental Coverage (Neutral=Hold)</td><td>61%</td><td>32%</td><td>7%</td><td>36%</td><td>48%</td><td>16%</td></tr><tr><td>% of companies in each rating category that are investment banking clients</td><td>38%</td><td>42%</td><td>27%</td><td>42%</td><td>37%</td><td>36%</td></tr></table>

## Guide to Citi Fundamental Research Investment Ratings:

Citi stock recommendations include an investment rating and an optional risk rating to highlight high risk stocks. Risk rating takes into account both price volatility and fundamental criteria. Stocks will either have no risk rating or a High risk rating assigned.

Investment Ratings: Citi investment ratings are Buy, Neutral and Sell. Our ratings are a function of analyst expectations of expected total return ("ETR") and risk. ETR is the sum of the forecast price appreciation (or depreciation) plus the dividend yield for a stock within the next 12 months. The target price is based on a 12 month time horizon. The Investment rating definitions are: Buy (1) ETR of 15% or more or 25% or more for High risk stocks; and Sell (3) for negative ETR. Any covered stock not assigned a Buy or a Sell is a Neutral (2). For stocks rated Neutral (2), if an analyst believes that there are insufficient valuation drivers and/or investment catalysts to derive a positive or negative investment view, they may elect with the approval of Citi management not to assign a target price and, thus, not derive an ETR. Citi may suspend its rating and target price and assign "Rating Suspended"

[中间内容因长度限制已省略]

r investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality,

accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any

unauthorized use, duplication, redistribution or disclosure of this report (the "Product"), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
