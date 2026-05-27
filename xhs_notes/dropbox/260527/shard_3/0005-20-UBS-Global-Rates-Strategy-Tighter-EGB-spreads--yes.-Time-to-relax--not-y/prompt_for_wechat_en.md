You are a senior financial newsletter editor with a consulting-style strategy lens. You turn research-report material into a long-form English article that is structured, insightful, and suitable for a serious business audience.

Objective:
- Write an English Markdown article based on the report parsing below.
- Target length: around 2200 words, plus or minus 15%.
- Tone: serious, analytical, strategic, and readable.
- The article should not feel like a summary. It should make an argument.
- You may extend the report's logic into reasonable second-order implications, but do not invent data, company actions, or quotes.
- Do not disclose every detail. Leave several meaningful open questions that make readers want the full report.

McKinsey-style writing principles:
1. Answer first: open with the controlling idea, not background.
2. Governing thought: every section must support the main answer.
3. Mutually exclusive, collectively exhaustive logic: avoid overlapping sections.
4. So what: every section must explain why the point matters.
5. Synthesis over summary: do not list facts; interpret what the pattern means.
6. Action titles: section headings must be complete, insight-bearing sentences. Do not use generic headings such as "Key Takeaways", "Market Background", "Core View", or "Reader Implications".
7. Natural hooks: if you want readers to join the community or read the full report, the hook should emerge from unresolved analytical questions, not from promotional language.

Required Markdown structure:
- `# Title`: make it a direct argument, not a topic label.
- Opening: 4-6 short paragraphs that state the main thesis and why now matters.
- 4-6 `##` sections. Each `##` heading must be an action title: a sentence that tells the reader the insight.
- One section should identify what the report does not fully answer yet.
- One section should translate the report into a decision framework for readers.
- Final section: naturally invite readers to join the community or read the full report using this CTA: Join the community to read the full report and review the original charts.
- End with: `*This article is for learning and discussion only and does not constitute investment advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
# Global Rates Strategy

# Tighter EGB spreads, yes. Time to relax, not yet.

# Positive risk sentiment - No pandemic or '22 playbook on fiscal policy

We have been advising clients to not fight any tightening in 10y spreads of Italy, France and Spain against Germany. We have been long 10y bunds since end March so have been constructive on European core duration. The reasons why we think spreads could also tighten further are relatively straightforward, if maybe not entirely comfortable. First, we do not see a repeat of the fiscal support granted in the pandemic or in '22 as the European Commission is reviewing the escape clauses for fiscal rules. Second, risk sentiment is doing the heavy lifting now. When European equities perform, spreads go along (Figure 5). Third, the political calendar with 2027 budget and 2028 elections could lead to some volatility and spread widening but is relatively distant. Mark your calendar for end August '26 when we expect conversations on 2027 budgets to start in earnest.

# Italy versus France - Carry dominates for now

We think that Italy may eventually underperform France, but we have been telling clients not to mistake a future concern for a present trade as a moderate search for carry in EGBs has resumed. The market tested and rejected Italian underperformance when 10y Italy vs France rose to 22 bps in March '26, after trading around zero in the final quarter of '25. In recent years, Italy has benefited from political stability, the NGEU program, and a reduction in budget deficits to \~3%GDP. But NGEU support could be fading together with the boost from nominal growth (Figure 2).

# But do not mistake calm for comfortable

German 30y are now sitting at our end-2026 forecast of 3.50%. That level is 35 bps above 30y EUR swap rates, with the spread 12 bps wider on the year. When sovereigns consistently fund above swap rates, it is an indication that the market is pricing in more lasting fiscal risks, even if it is just basis point by basis point. German growth and fiscal developments in the year ahead will be key.

# Funding market dog has not barked

We did not pick up material concerns on EUR or US funding markets in recent client meetings. That being said, EGB issuance is running slightly below its 3y average. We thought that near-term EGB issuance could lead to some modest widening of sovereign rates versus swap rates but the recent duration rally is likely to alleviate some of these concerns.

Figure 1: Trends in r-g across countries   
![](images/12fa1cc79c32db73e1b7c1f85db2aa1c690a5ac0b1d5e1a5b4f0803fea9207e7.jpg)

<details>
<summary>line</summary>

| Year | US Pre-war | UK Pre-war | US Post-war | UK Post-war | Germany Pre-war | Germany Post-war | France Pre-war | France Post-war | Spain Pre-war | Italy Pre-war | Italy Post-war | Japan Pre-war | Japan Post-war |
|------|------------|------------|-------------|-------------|-----------------|------------------|----------------|-----------------|---------------|---------------|----------------|---------------|----------------|
| 1997 | ~0         | ~0         | ~0          | ~0          | ~0              | ~0               | ~0             | ~0              | ~0            | ~0            | ~0             | ~0            | ~0             |
| 2000 | ~0         | ~0         | ~0          | ~0          | ~0              | ~0               | ~0             | ~0              | ~0            | ~0            | ~0             | ~0            | ~0             |
| 2003 | ~0         | ~0         | ~0          | ~0          | ~0              | ~0               | ~0             | ~0              | ~0            | ~0            | ~0             | ~0            | ~0             |
| 2006 | ~0         | ~0         | ~0          | ~0          | ~0              | ~0               | ~0             | ~0              | ~0            | ~0            | ~0             | ~0            | ~0             |
| 2009 | ~5         | ~5         | ~5          | ~5          | ~5              | ~5               | ~5             | ~5              | ~5            | ~5            | ~5             | ~5            | ~5             |
| 2012 | ~5         | ~5         | ~5          | ~5          | ~5              | ~5               | ~5             | ~5              | ~5            | ~5            | ~5             | ~5            | ~5             |
| 2015 | ~0         | ~0         | ~0          | ~0          | ~0              | ~0               | ~0             | ~0              | ~0            | ~0            | ~0             | ~0            | ~0             |
| 2018 | ~-5        | ~-5        | ~-5         | ~-5         | ~-5             | ~-5              | ~-5            | ~-5             | ~-5           | ~-5           | ~-5            | ~-5           | ~-5            |
| 2021 | -10        | -10        | -10         | -10         | -10             | -10              | -10            | -10             | -10           | -10           | -10            | -10           | -10            |
| 2024E| -5         | -5         | -5          | -5          | -5              | -5               | -5             | -5              | -5            | -5            | -5             | -5            | -5             |
| 2027E| 0          | 0          | 0           | 0           | 0               | 0                | 0              | 0               | 0            | 0            | 0              | 0             | 0              |
The data is already in CSV format for future years. The values are estimated based on the date range from 1997 to 2027E. There is no additional data series present in this code. The values represent the absolute magnitude of the data points. The labels for the data series are 'US Pre-war' or 'Italy Post-war'.
</details>

Source: UBS (incl estimates)

Figure 2: Italy - nominal interest rate vs nominal growth rate   
![](images/b0897c925664f3ccd47a89c133c24a9a46b0daad59eca48d565e408dd5b192a4.jpg)

<details>
<summary>line</summary>

| Year | r    | g    | r-g  |
|------|------|------|------|
| 1996 | 0.0  | 4.0  | 0.0  |
| 1999 | 6.0  | 5.0  | 3.0  |
| 2002 | 5.0  | 3.0  | 1.0  |
| 2005 | 4.0  | 4.0  | 2.0  |
| 2008 | 5.0  | -4.0 | 7.0  |
| 2011 | 3.0  | 2.0  | 5.0  |
| 2014 | 3.0  | -2.0 | 4.0  |
| 2017 | 3.0  | 2.0  | 1.0  |
| 2020 | 2.0  | -8.0 | -10.0|
| 2023 | 3.0  | 10.0 | -5.0 |
| 2026E| 3.0  | 3.0  | -1.0 |
</details>

Source: UBS (incl estimates)

# Interest Rates

Global

Reinout De Bock

Strategist

reinout.de-bock@ubs.com

+44-20-7567 0152

Mustafa Oguz Caylan

Strategist

mustafa.caylan@ubs.com

+44-20-7901 5203

Figure 3: BTP 2y real   
![](images/16119c14ef9161264e80e3b45df682dcc8d95bf210c7ebbdfb2dd48ec6490f2d.jpg)

<details>
<summary>line</summary>

| Year | Real 2y |
| ---- | ------- |
| 12   | 0.0     |
| 13   | 3.0     |
| 14   | 3.5     |
| 15   | 0.5     |
| 16   | 0.0     |
| 17   | -0.5    |
| 18   | -1.0    |
| 19   | -2.0    |
| 20   | -0.5    |
| 21   | 0.5     |
| 22   | -1.5    |
| 23   | -6.0    |
| 24   | 2.0     |
| 25   | 0.5     |
</details>

Source: Bloomberg

Figure 4: BTP 10y real   
![](images/444fca142ce8aba60ca28b2f0a07ba0e064904c12dd817daf378a0299e257c2c.jpg)

<details>
<summary>line</summary>

| Year | Real 10y |
| ---- | -------- |
| 12   | 5.0      |
| 13   | 3.0      |
| 14   | 1.0      |
| 15   | 0.0      |
| 16   | 0.5      |
| 17   | 1.0      |
| 18   | 2.0      |
| 19   | 1.5      |
| 20   | 0.5      |
| 21   | -0.5     |
| 22   | 1.0      |
| 23   | 2.5      |
| 24   | 2.0      |
| 25   | 1.5      |
</details>

Source: Bloomberg

Figure 5: EURO STOXX 600 and 30y BTP-bund spreads   
![](images/19cf9908278c16bc60789d6f1a304bc68d9a9860912edcb163ec39b663cdf112.jpg)

<details>
<summary>line</summary>

| Date    | 30y BTP-Bund spread | STOXX 600 [RHS, inverse] |
|---------|---------------------|--------------------------|
| Jan. 22 | ~185                | ~190                     |
| May. 23 | ~230                | ~225                     |
| Sep. 24 | ~160                | ~155                     |
| Jan. 26 | ~80                 | ~75                      |
</details>

Source: Bloomberg, UBS.

Figure 6: 10y term premium estimates for Germany, France and Italy   
![](images/3e4ad5c883a987884e08a9be862787f9cb3cd14b71e4d551025b7877246a6e51.jpg)

<details>
<summary>line</summary>

| Year | Euro Area Crisis | 2018 Italian General Elections | Lagarde: "Not here to close spreads" | 2022 Italian General Elections | Germany | France | Italy | 2022 Italian General Elections |
|------|------------------|-------------------------------|------------------------------------|--------------------------------|---------|--------|-------|--------------------------------|
| 1994 | ~4.5             | ~4.5                          | ~4.5                               | ~4.5                           | ~4.5    | ~4.5   | ~4.5  | ~4.5                           |
| 1997 | ~3.0             | ~3.0                          | ~3.0                               | ~3.0                           | ~3.0    | ~3.0   | ~3.0  | ~3.0                           |
| 2000 | ~2.5             | ~2.5                          | ~2.5                               | ~2.5                           | ~2.5    | ~2.5   | ~2.5  | ~2.5                           |
| 2003 | ~2.0             | ~2.0                          | ~2.0                               | ~2.0                           | ~2.0    | ~2.0   | ~2.0  | ~2.0                           |
| 2006 | ~1.5             | ~1.5                          | ~1.5                               | ~1.5                           | ~1.5    | ~1.5   | ~1.5  | ~1.5                           |
| 2009 | ~1.0             | ~1.0                          | ~1.0                               | ~1.0                           | ~1.0    | ~1.0   | ~1.0  | ~1.0                           |
| 2012 | ~0.5             | ~0.5                          | ~0.5                               | ~0.5                           | ~0.5    | ~0.5   | ~0.5  | ~0.5                           |
| 2015 | ~-0.5            | ~-0.5                         | ~-0.5                              | ~-0.5                          | ~-0.5   | ~-0.5  | ~-0.5 | ~-0.5                          |
| 2018 | ~-1.0            | ~-1.0                         | ~-1.0                              | ~-1.0                          | ~-1.0   | ~-1.0  | ~-1.0 | ~-1.0                          |
| 2021 | ~-1.5            | ~-1.5                         | ~-1.5                              | ~-1.5                          | ~-1.5   | ~-1.5  | ~-1.5 | ~-1.5                          |
| 2024 | ~-1.0            | ~-1.0                         | ~-1.0                              | ~-1.0                          | ~-1.0   | ~-1.0  | ~-1.0 | ~-1.0                          |
| 2027 | ~-0.5            | ~-0.5                         | ~-0.5                              | ~-0.5                          | ~-0.5   | ~-0.5  | ~-0.5 | ~-0.5                          |
| 2030 | ~1.0             | ~1.0                          | ~1.0                               | ~1.0                           | ~1.0    | ~1.0   | ~1.0  | ~1.0                           |
| 2033 | ~1.5             | ~1.5                          | ~1.5                               | ~1.5                           | ~1.5    | ~1.5   | ~1.5  | ~1.5                           |
| 2036 | ~2.0             | ~2.0                          | ~2.0                               | ~2.0                           | ~2.0    | ~2.0   | ~2.0  | ~2.0                           |
| 2039 | ~2.5             | ~2.5                          | ~2.5                               | ~2.5                           | ~2.5    | ~2.5   | ~2.5  | ~2.5                           |
| 2042 | ~3.0             | ~3.0                          | ~3.0                               | ~3.0                           | ~3.0    | ~3.0   | ~3.0  | ~3.0                           |
| 2045 | ~3.5             | ~3.5                          | ~3.5                               | ~3.5                           | ~3.5    | ~3.5   | ~3.5  | ~3.5                           |
| 2048 | ~4.0             | ~4.0                          | ~4.0                               | ~4.0                           | ~4.0    | ~4.0   | ~4.0  | ~4.0                           |
| 2051 | ~4.5             | ~4.5                          | ~4.5                               | ~4.5                           | ~4.5    | ~4.5   | ~4.5  | ~4.5                           |
| 2054 | ~5.0             | ~5.0                          | ~5.0                               | ~5.0                           | ~5.0    | ~5.0   | ~5.0  | ~5.0                           |
| 2057 | ~4.5             | ~4.5                          | ~4.5                               | ~4.5                           | ~4.5    | ~4.5   | ~4.5  | ~4.5                           |
| 2060 | ~4.0             | ~4.0                          | ~4.0                               | ~4.0                           | ~4.0    | ~4.0   | ~4.0  | ~4.0                           |
| 2063 | ~3.5             | ~3.5                          | ~3.5                               | ~3.5                           | ~3.5    | ~3.5   | ~3.5  | ~3.5                           |
| 2066 | ~3.0             | ~3.0                          | ~3.0                               | ~3.0                           | ~3.0    | ~3.0   | ~3.0  | ~3.0                           |
| 2069 | ~2.5             | ~2.5                          | ~2.5                               | ~2.5                           | ~2.5    | ~2.5   | ~2.5  | ~2.5                           |
| 2072 | ~2.0             | ~2.0                          | ~2.0                               | ~2.0                           | ~2.0    | ~2.0   | ~2.0  | ~2.0                           |
| 2075 | ~1.5             | ~1.5                          | ~1.5                               | ~1.5                           | ~1.5    | ~1.5   | ~1.5  | ~1.5                           |
| 2078 | ~1.0             | ~1.0                          | ~1.0                               | ~1.0                           | ~1.0    | ~1.0   | ~1.0  | ~1.0                           |
| 2081 | -          | -                             | -                                  | -                              | -       | -      | -     | -                              |
| 2084 | -          | -                             | -                                  | -                              | -       | -      | -     | -                              |
| 2087       | -          | -                             | -                                  | -                              | -       | -      | -     | -                              |
| 2090       | -          | -                             | -                                  | -                              | -       | -      | -     | -                              |
| 2193       (post-SRD) 1997 vs 1998 (post-SRD)        |
| Note: The data provided in the code is estimated based on the given code and the original data source used in the plot (e.g., bar, line, color) and the original data source used in the plot (e.g., legend). The values for the last three data points are estimated based on the given code and the original data source used in the plot (e.g., bar, line, color). Since the original data source is not explicitly labeled in the code, I have indicated that this is estimated based on the original data source used in the plot (e.g., bar, line, color). The actual data source used in the plot is not explicitly labeled in the code but referenced from the original data source using it as shown in the original chart.
</details>

Source: Bloomberg, UBS estimates based on Adrian, Crump and Moench (2013).

We would like to thank Deepak Joy and Mehak Bhalla, our research support service professionals in our Hyderabad Research BSC, for assisting in preparing this research report.

A record of our current and 12 month historical, Rates trade recommendations is available on UBS Neo or via your UBS sales representative.

# Valuation Method and Risk Statement

Risks of multi-asset investing include but are not limited to market risk, credit risk, interest rate risk, and foreign exchange risk. Correlations of returns among different asset classes may deviate from historical patterns. Geopolitical events and policy shocks pose risks that can reduce asset returns. Valuations may be adversely affected during times of high market volatility, thin liquidity, and economic dislocation. All option recommendations are ‘over-the-counter’.

# Required Disclosures

This document has been prepared by UBS AG London Branch, an affiliate of UBS AG. UBS AG, its subsidiaries, branches and affiliates, including former CS AG and its subsidiaries, branches and affiliates are referred to herein as "UBS".

For information on the ways in which UBS manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures. Unless otherwise indicated, information and data in this report are based on company disclosures including but not limited to annual, interim, quarterly reports and other company announcements. The figures contained in performance charts refer to the past; past performance is not a reliable indicator of future results. Additional information will be made available upon request. UBS Co. Limited is licensed to conduct securities investment consultancy businesses by the China Securities Regulatory Commission. UBS acts or may act as principal in the debt securities (or in related derivatives) that may be the subject of this report. This recommendation was finalized on: 26 May 2026 07:18 AM GMT. UBS has designated certain UBS Global Research department members as Derivatives Research Analysts where those department members publish research principally on the analysis of the price or market for a derivative, and provide information reasonably sufficient upon which to base a decision to enter into a derivatives transaction. Where Derivatives Research Analysts co-author research reports with Equity Research Analysts or Economists, the Derivatives Research Analyst is responsible for the derivatives investment views, forecasts, and/or recommendations. Quantitative Research Review: UBS Global Research publishes a quantitative assessment of its analysts' responses to certain questions about the likelihood of

[中间内容因长度限制已省略]

ns or opinions in such this publication or material are not made or provided to you, and (ii) to the maximum extent permitted by law (a) indemnify UBS and its associates or related entities (and their respective Directors, officers, agents and Advisors) (each a 'Relevant Person') for any loss, damage, liability or claim any of them may incur or suffer as a result of, or in connection with, your unauthorised reliance on this publication or material and (b) waive any rights or remedies you may have against any Relevant Person for (or in respect of) any loss, damage, liability or claim you may incur or suffer as a result of, or in connection with, your unauthorised reliance on this publication or material. Korea: Distributed in Korea by UBS Pte. Ltd., Seoul Branch. This report may have been edited or contributed to from time to time by affiliates of UBS Pte. Ltd., Seoul Branch. This material is intended for professional/institutional clients only and not for distribution to any retail clients. Malaysia: This material is authorized to be distributed in Malaysia by UBS Malaysia Sdn. Bhd (Capital Markets Services License No.: CMSL/A0063/2007). This material is intended for professional/institutional clients only and not for distribution to any retail clients. India: Distributed by UBS India Private Ltd. (Corporate Identity Number U67120MH1996PTC097299) 2/F, 3 North Avenue, Maker Maxity, Bandra Kurla Complex, Bandra (East), Mumbai (India) 400051. Phone: +912261556000. It provides brokerage services bearing SEBI Registration Number: INZ000259830; Merchant Banking services bearing SEBI Registration Number: INM000013101; and Research Analyst services bearing SEBI Registration Number: INH000001204. Name of Compliance Officer Mr. Parameshwaran Shivaramakrishnan, Phone: +912261556151, Email: +912261556151, Email: ol-ubs-sec-compliance@ubs.com Registration granted by SEBI, and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. UBS may have debt holdings or positions in the subject Indian company/companies. UBS may have financial interests (e.g. loan/derivative products, rights to or interests in investments, etc.) in the subject Indian company/companies from time to time. Within the past 12 months, UBS may have received compensation for non-investment banking securities-related services and/or non-securities services from the subject Indian company/companies. The subject company/companies may have been a client/clients of UBS during the 12 months preceding the date of distribution of the research report with respect to investment banking and/or non-investment banking securities-related services and/or non-securities services. With regard to information on associates, please refer to the Annual Report at: https://www.ubs.com/global/en/about\_ubs/investor\_relations/annualreporting.html The Research Annual Compliance Report for UBS India Private Limited is available on www.ubs.com/ubssi under Research tab. Taiwan: Except as otherwise specified herein, this material may not be distributed in Taiwan. Information and material on securities/instruments that are traded in a Taiwan organized exchange is deemed to be issued and distributed by UBS Pte. LTD., Taipei Branch, which is licensed and regulated by Taiwan Financial Supervisory Commission. Save for securities/instruments that are traded in a Taiwan organized exchange, this material should not constitute "recommendation" to clients or recipients in Taiwan for the covered companies or any companies mentioned in this document. No portion of the document may be reproduced or quoted by the press or any other person without authorisation from UBS. Indonesia: This report is being distributed by PT UBS Sekuritas Indonesia and is delivered by its licensed employee(s), including marketing/sales person, to its client. PT UBS Sekuritas Indonesia, having its registered office at Sequis Tower Level 22 unit 22-1,Jl.Jend. Sudirman, kav.71, SCBD lot 11B, Jakarta 12190. Indonesia, is a subsidiary company of UBS AG and licensed under Capital Market Law no. 8 year 1995, a holder of broker-dealer and underwriter licenses issued by the Capital Market and Financial Institution Supervisory Agency (now Otoritas Jasa Keuangan/OJK). PT UBS Sekuritas Indonesia is also a member of Indonesia Stock Exchange and supervised by Otoritas Jasa Keuangan (OJK). Neither this report nor any copy hereof may be distributed in Indonesia or to any Indonesian citizens except in compliance with applicable Indonesian capital market laws and regulations. This report is not an offer of securities in Indonesia and may not be distributed within the territory of the Republic of Indonesia or to Indonesian citizens in circumstance which constitutes an offering within the meaning of Indonesian capital market laws and regulations.

The disclosures contained in research documents produced by UBS AG, London Branch or UBS Europe SE shall be governed by and construed in accordance with English law.

UBS specifically prohibits the redistribution of this document in whole or in part without the written permission of UBS and in any event UBS accepts no liability whatsoever for any redistribution of this document or its contents or the actions of third parties in this respect. Images may depict objects or elements that are protected by third party copyright, trademarks and other intellectual property rights. © UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/cf4c06914ba5f1b6ed904826c8bbb6aa9fc62651720d416ae859105d665990df.jpg)
"""
