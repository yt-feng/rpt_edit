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
# China inflation

# PPI up, CPI steady

# Economics

# China

- CPI y-o-y remained relatively stable in April as the impact of the energy shock was primarily on energy components only; food items turned into a drag   
◆ PPI surged to 2.8% y-o-y and surprised on the upside (Bbg: 1.8%), driven by the fast oil price pass-through; AI-demand and anti-involution also helped   
- Early signs of cost pass-through to midstream sectors suggest downstream sector responses and transmission to core CPI will be key to monitor

# Taylor Wang

Economist, China  
The Hongkong and Shanghai Banking Corporation Limited  
taylor.t.l.wang@HSBC.com.hk  
+852 2288 8650

# Facts

Table 1. China CPI breakdown 

<table><tr><td></td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td></tr><tr><td>Headline CPI, % y-o-y, nsa</td><td>1.3</td><td>1.0</td><td>1.2</td></tr><tr><td>Core CPI (ex.food, energy), % y-o-y, nsa</td><td>1.8</td><td>1.1</td><td>1.2</td></tr><tr><td>Food prices, % y-o-y, nsa</td><td>1.7</td><td>0.3</td><td>-1.6</td></tr><tr><td>Fresh Vegetable</td><td>10.9</td><td>4.9</td><td>-0.5</td></tr><tr><td>Meat</td><td>-2.7</td><td>-4.2</td><td>-6.7</td></tr><tr><td>Pork</td><td>-8.6</td><td>-11.5</td><td>-15.2</td></tr><tr><td>Transportation and Comm, % y-o-y, nsa</td><td>-0.7</td><td>0.9</td><td>4.6</td></tr><tr><td>Transportation fuel</td><td>-9.0</td><td>3.4</td><td>17.4</td></tr><tr><td>Entertainment and culture, % y-o-y, nsa</td><td>2.0</td><td>1.1</td><td>1.3</td></tr><tr><td>Tourism</td><td>11.7</td><td>3.2</td><td>4.0</td></tr><tr><td>Services, % y-o-y, nsa</td><td>1.6</td><td>0.8</td><td>0.9</td></tr><tr><td>Headline CPI, % m-o-m, nsa</td><td>1.0</td><td>-0.7</td><td>0.3</td></tr><tr><td>Core CPI (ex.food, energy), % m-o-m, nsa</td><td>0.7</td><td>-0.7</td><td>0.2</td></tr><tr><td>Food prices, % m-o-m, nsa</td><td>1.9</td><td>-2.7</td><td>-1.6</td></tr><tr><td>Fresh Vegetable</td><td>-0.1</td><td>-10.1</td><td>-6.4</td></tr><tr><td>Meat</td><td>2.6</td><td>-3.9</td><td>-2.7</td></tr><tr><td>Pork</td><td>4.0</td><td>-7.3</td><td>-5.7</td></tr><tr><td>Transportation and Comm, % m-o-m, nsa</td><td>2.2</td><td>0.4</td><td>3.5</td></tr><tr><td>Transportation fuel</td><td>2.8</td><td>10.0</td><td>11.5</td></tr><tr><td>Entertainment and culture, % m-o-m, nsa</td><td>1.6</td><td>-1.6</td><td>0.5</td></tr><tr><td>Tourism</td><td>14.1</td><td>-12.9</td><td>4.1</td></tr><tr><td>Services, % m-o-m, nsa</td><td>1.1</td><td>-1.1</td><td>0.5</td></tr></table>

Source: CEIC, HSBC

Table 2. China PPI breakdown 

<table><tr><td></td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td></tr><tr><td>Headline PPI, % y-o-y, nsa</td><td>-0.9</td><td>0.5</td><td>2.8</td></tr><tr><td>Consumer goods</td><td>-1.6</td><td>-1.3</td><td>-1.0</td></tr><tr><td>Producer goods</td><td>-0.7</td><td>1.0</td><td>3.8</td></tr><tr><td>Coal Mining</td><td>-7.0</td><td>-2.2</td><td>3.1</td></tr><tr><td>Petroleum and Natural Gas Mining</td><td>-12.9</td><td>5.2</td><td>28.6</td></tr><tr><td>Ferrous Metals Manufacturing</td><td>-3.4</td><td>-2.5</td><td>-1.1</td></tr><tr><td>Non-Ferrous Metals Manufacturing</td><td>22.1</td><td>22.4</td><td>22.5</td></tr><tr><td>Petroleum and Coal Manufacturing</td><td>-12.0</td><td>-4.5</td><td>14.2</td></tr><tr><td>Computer and Communication</td><td>-0.9</td><td>0.4</td><td>1.5</td></tr><tr><td>Headline PPI, % m-o-m, nsa</td><td>0.4</td><td>1.0</td><td>1.7</td></tr><tr><td>Consumer goods</td><td>0.0</td><td>-0.1</td><td>-0.1</td></tr><tr><td>Producer goods</td><td>0.5</td><td>1.3</td><td>2.1</td></tr><tr><td>Coal Mining</td><td>-0.5</td><td>0.1</td><td>1.9</td></tr><tr><td>Petroleum and Natural Gas Mining</td><td>5.1</td><td>15.8</td><td>18.5</td></tr><tr><td>Ferrous Metals Manufacturing</td><td>0.1</td><td>0.3</td><td>0.6</td></tr><tr><td>Non-Ferrous Metals Manufacturing</td><td>4.6</td><td>1.0</td><td>0.2</td></tr><tr><td>Petroleum and Coal Manufacturing</td><td>0.4</td><td>5.8</td><td>16.4</td></tr><tr><td>Computer and Communication</td><td>0.6</td><td>0.7</td><td>0.6</td></tr></table>

Source: CEIC, HSBC

# Implications

April's inflation data indicated that energy cost pass-through became more pronounced in industrial sectors, as evidenced by the stronger-than-expected rise in PPI (2.8% y-o-y; HSBC: 1.8%, Bbg: 1.8%). The breakdown revealed that price pass-through to domestic oil-related upstream and midstream sectors was a key driver. Looking ahead, if energy prices remain elevated, we think midstream firms will likely need to pass on more costs to buyers, even if this risks market share losses. On the consumer side, the impact appeared largely confined to energy components so far (CPI up 1.2% y-o-y; HSBC: 1.0%, Bbg: 0.9%), though more time is needed to gauge the full impact of the oil shock. In other words, it will be important to monitor for signs of PPI feeding into core CPI in coming months and quarters, which may prompt additional policy support for hard-hit groups.

Headline CPI y-o-y showed a very mixed story in April, as energy components were primarily boosted by surging global oil prices while food items turned into a drag. In particular, vehicle fuel prices recorded the highest y-o-y increase since Oct 2022 (up $17.4\%$ y-o-y). However, the NDRC's pricing regulations have already provided a much-needed buffer, as increases in domestic vehicle fuel prices largely lagged global oil price movements over the month (chart 1). With global crude oil prices still elevated (Brent trading at above USD100 per barrel at the time of writing), and domestic price adjustments lagging alongside a low base from last year (Brent only averaged USD 64 per barrel in May 2025), energy is likely to remain a key contributor to CPI growth this month.

For food items, while vegetables and fruit prices m-o-m appeared weaker than the seasonal trend due to warmer weather this year, the key drag still came from pork, whose y-o-y prices have been declining for eleven consecutive months in this cycle. The imbalance between supply and demand has also drawn the attention of policymakers, particularly as the April Politburo meeting explicitly called for stabilising prices of live hogs (Xinhua, 28 April). The Ministry of Agriculture and Rural Affairs and the NDRC have recently signalled tighter production-capacity management, and the rollout of specific follow-up measures should help pork prices improve.

Excluding volatile components, core CPI was broadly in line with expectations: the m-o-m increase roughly matched its seasonal pattern, and the y-o-y increase remained relatively stable. The impact of the energy shock appeared muted at this juncture. Instead, despite slower y-o-y price growth, gold products (up 47%) still added 0.2ppts to headline CPI y-o-y inflation (NBS, 11 May). Excluding that, some growth momentum is likely shifting from goods consumption towards services now. For one, the waning impact of trade-ins was still reflected by household appliance prices, which only rose 2.6% y-o-y in April versus 4.8% in Q1. A modest uplift was recorded in culture and entertainment, with prices rising 1.3% y-o-y in April versus 1.0% in Q1, supported by ongoing policy measures (including spring breaks for primary and secondary students) and fiscal support announced at the Two Sessions. Going forward, policymakers have pledged to further unlock services consumption potential, while the NDRC's refined oil pricing regulations should continue to partially mitigate cost pressures across transport-related sectors.

Chart 1. The most direct impact was still on vehicle fuels and upstream sectors...   
![](images/2b09ed5775a743b726b66234a724118d530c34b45e150aef01d31630e246a76b.jpg)

<details>
<summary>line</summary>

| Month   | Brent | CPI: vehicle fuel | PPI: petroleum and natural gas mining | PPI: petroleum and coal processing |
|---------|-------|-------------------|--------------------------------------|------------------------------------|
| Jan-22  | 70    | 20                | 40                                   | 30                                 |
| Oct-22  | 60    | 30                | 50                                   | 40                                 |
| Jul-23  | -30   | -10               | -20                                  | -15                                |
| Apr-24  | 10    | 5                 | 0                                    | 0                                  |
| Jan-25  | -10   | -5                | -10                                  | -5                                 |
| Oct-25  | 60    | 15                | 30                                   | 20                                 |
</details>

Source: Bloomberg, CEIC, HSBC

Chart 2. ...but some midstream sectors using oil as inputs also raised prices   
![](images/c8e55d8a01ee43dcea0af6bfbae1e670b26f9cc8dd331950d058c2f8cd282604.jpg)

<details>
<summary>line</summary>

| Month   | PPI: chemical product and materials | PPI: chemical fibre | Brent (RHS) |
|---------|-------------------------------------|---------------------|-------------|
| Jan-22  | 20                                  | 15                  | 10          |
| Dec-22  | 10                                  | 5                   | 0           |
| Nov-23  | -10                                 | -5                  | -10         |
| Oct-24  | -5                                  | -10                 | -5          |
| Sep-25  | 0                                   | 0                   | 0           |
</details>

Source: Bloomberg, CEIC, HSBC

Chart 3. Headline CPI was boosted by energy components in April   
![](images/4f04d9c746e8677c7b4d17bd2f68675955ad0285181ddca7e122e1ff0c2bc16f.jpg)

<details>
<summary>line</summary>

| Date    | Energy | Food | Core/Other | Headline CPI % y-o-y |
|---------|--------|------|------------|----------------------|
| Jan-19  | 0.0    | 0.0  | 0.0        | 1.5                  |
| Jul-19  | 0.0    | 1.0  | 0.0        | 2.5                  |
| Jan-20  | 0.0    | 4.0  | 0.0        | 5.5                  |
| Jul-20  | 0.0    | 2.0  | 0.0        | 2.5                  |
| Jan-21  | 0.0    | -1.0 | 0.0        | -1.0                 |
| Jul-21  | 0.0    | -1.0 | 1.5        | 1.5                  |
| Jan-22  | 0.0    | -1.0 | 1.5        | 2.5                  |
| Jul-22  | 0.0    | 1.5  | 1.5        | 2.5                  |
| Jan-23  | 0.0    | 1.5  | 1.5        | 2.5                  |
| Jul-23  | 0.0    | -1.0 | 1.5        | -1.0                 |
| Jan-24  | 0.0    | -1.0 | 1.5        | -1.0                 |
| Jul-24  | 0.0    | -1.0 | 1.5        | -1.0                 |
| Jan-25  | 0.0    | -1.0 | 1.5        | -1.0                 |
| Jul-25  | 0.0    | -1.0 | 1.5        | -1.0                 |
| Jan-26  | 0.0    | -1.0 | 1.5        | -1.0                 |
</details>

Source: CEIC, HSBC estimates

For PPI, several key observations are worth highlighting. First, the most direct impact still came from oil-related upstream sectors (chart 1). Our estimates showed that the combined contribution of petroleum & natural gas extractions, coal mining, and petroleum & coal processing to PPI y-o-y growth increased by c1.1ppts compared with the previous month. Given these sectors' stronger linkage to global oil prices, a prolonged Middle East conflict is likely to keep their prices elevated. Second, some midstream sectors that use petroleum as raw inputs also raised their output prices. In particular, chemical products & materials and chemical fibres saw positive y-o-y price growth for the first time since August and September 2024 (chart 2). We estimated that their combined contribution to PPI y-o-y also increased by c0.7ppt compared with March. However, as their price increases have largely lagged those in upstream sectors, this may still suggest a risk of profit margin compression. Third, downstream consumer-facing sectors have not yet seen a material impact, as price responses remained muted (Chart 4). As a result, pass-through to core CPI appeared contained at this stage. Looking ahead, we continue to expect midstream and downstream players will need to pass more costs on to customers if energy prices stay elevated for an extended period, given the significant hit to their profit margins. Lastly, excluding the oil impact, strong AI-driven demand, rising global copper prices, domestic electrification and anti-involution measures were also key drivers. The most impacted sectors were electrical machinery, computers and communications, and non-ferrous metals (mining and manufacturing), whose y-o-y prices all climbed up higher in April.

Chart 4. Consumer-facing downstream sectors have not seen material price shocks   
![](images/7f01c99fd9f9aadca9a9b09c482d5d0d85d1ae7a4a7acf682f9c20a80b0de4f4.jpg)

<details>
<summary>line</summary>

| Date    | PPI: producer goods | PPI: consumer goods |
|---------|---------------------|---------------------|
| Jan-22  | -0.8                | 0.1                 |
| May-22  | 1.4                 | 0.2                 |
| Sep-22  | -1.4                | 0.3                 |
| Jan-23  | -0.6                | 0.1                 |
| May-23  | -1.0                | 0.0                 |
| Sep-23  | 0.5                 | 0.2                 |
| Jan-24  | -0.2                | 0.1                 |
| May-24  | -0.1                | 0.0                 |
| Sep-24  | -1.0                | -0.1                |
| Jan-25  | -0.2                | -0.1                |
| May-25  | -0.6                | -0.1                |
| Sep-25  | -0.1                | -0.1                |
| Jan-26  | 0.6                 | 0.1                 |
| May-26  | 2.2                 | -0.1                |
</details>

Source: CEIC, HSBC

# Disclosure appendix

# Analyst certification

The following analyst(s), who is(are) primarily responsible for this document, certifies(y) that the opinion(s), views or forecasts expressed herein accurately reflect their personal view(s) and that no part of their compensation was, is or will be directly or indirectly related to the specific recommendation(s) or views contained in this research report: Taylor Wang

This document has been prepared and is being distributed by the Research Department of HSBC and is intended solely for the clients of HSBC and is not for publication to other persons, whether through the press or by other means.

This document does not provide individually tailored investment advice and should not be construed as an offer or the solicitation of an offer to buy or sell any securities or to participate in any trading strategy. The information contained within this document is believed to be reliable but we do not guarantee its completeness or accuracy. Any opinions expressed herein are subject to change without notice. HSBC may hold a position in, buy or sell on a principal basis or act as a market maker in any financial instrument discussed herein.

HSBC and its affiliates will from time to time sell to and buy from customers the securities/instruments (including derivatives) of companies covered in HSBC on a principal or agency basis.

Analyst(s) are paid in part by reference to the profitability of HSBC which includes investment banking revenues.

# Additional disclosures

1 This report is dated as at 11 May 2026.   
2 All market data included in this report are dated as at close 11 May 2026, unless a different date and/or a specific time of day is indicated in the report.   
3 HSBC has procedures in place to identify and manage any potential conflicts of interest that arise in connection with its Research business. HSBC's analysts and its other staff who are involved in the preparation and dissemination of Research operate and have a management reporting line independent of HSBC's Investment Banking business. Information Barrier procedures are in place between the Investment Banking, Principal Trading, and Research businesses to ensure that any confidential and/or price sensitive information is handled in an appropriate manner.   
4 You are not permitted to use, for reference, any data in this document for the purpose of (i) determining the interest payable, or other sums due, under loan agreements or under other financial contracts or instruments, (ii) determining the price at which a financial instrument may be bought or sold or traded or redeemed, or the value of a financial instrument, and/or (iii) measuring the performance of a financial instrument or of an investment fund.

# Disclaimer

Legal entities as at 7 December 2024:

HSBC Bank plc; HSBC Continental Europe; HSBC Continental Europe SA, Germany; HSBC Bank Middle East Limited, DIFC; HSBC Bank Middle East Limited, UAE branch; HSBC Yatirim Menkul Degerler AS, Istanbul; The Hongkong and Shanghai Banking Corporation Limited, Hong Kong; The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch; The Hongkong and Shanghai Banking Corporation Limited, Seoul Securities Branch; The Hongkong and Shanghai Banking Corporation Limited, Seoul Branch; HSBC Qianhai Securities Limited; HSBC Securities (Taiwan) Corporation Limited; HSBC Securities and Capital Markets (India) Private Limited, Mumbai; HSBC Bank Australia Limited; HSBC Securities (USA) Inc., New York; HSBC México, SA, Institución de Banca Múltiple, Grupo Financiero HSBC; Banco HSBC SA

Issuer of report

The Hongkong and Shanghai Banking Corporation Limited

Level 16, 1 Queen's Road Central

Hong Kong SAR

Telephone: +852 2843 9111

Fax: +852 2801 4138

Website: www.research.HSBC.com

This document has been issued by The Hongkong and Shanghai Banking Corporation Limited ("HSBC") in the conduct of its Hong Kong regulated business for the information of its institutional and professional investor (as defined by Securities and Future Ordinance (Chapter 571)) customers; it is not intended for and should not be distributed to retail customers in Hong Kong, unless permitted otherwise. The Hongkong and Shanghai Banking Corporation Limited is regulated by the Hong Kong Monetary Authority. All enquires by recipients in Hong Kong must be directed to your HSBC contact in Hong Kong. If it is received by a customer of an affiliate of HSBC, its provision to the recipient is subject to the terms of business in place between the recipient and such affiliate. Any recommendations contained in it are intended for the professional investors to whom it is distributed. This material is not and should not be construed as an offer to sell or the solicitation of an offer to purchase or sUBScribe for any investment. HSBC has based this document on information obtained from sources it believes to be reliable but which it has not independently verified; HSBC makes no guarante

[中间内容因长度限制已省略]

ion has been distributed by HSBC Continental Europe or by such other HSBC affiliate from which the recipient receives relevant services.

In Japan, this publication has been distributed by HSBC Securities (Japan) Co., Ltd.. It may not be further distributed in whole or in part for any purpose. In Korea, this publication is distributed by either The Hongkong and Shanghai Banking Corporation Limited, Seoul Securities Branch ("HBAP SLS") or The Hongkong and Shanghai Banking Corporation Limited, Seoul Branch ("HBAP SEL") for the general information of professional investors specified in Article 9 of the Financial Investment Services and Capital Markets Act ("FSCMA"). This publication is not a prospectus as defined in the FSCMA. It may not be further distributed in whole or in part for any purpose. Both HBAP SLS and HBAP SEL are regulated by the Financial Services Commission and the Financial Supervisory Service of Korea. In Singapore, this publication is distributed by The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch for the general information of institutional investors or other persons specified in Sections 274 and 304 of the Securities and Futures Act 2001 of Singapore ("SFA") and accredited investors and other persons in accordance with the conditions specified in Sections 275 and 305 of the SFA. Only Economics or Currencies reports are intended for distribution to a person who is not an Accredited Investor, Expert Investor or Institutional Investor as defined in SFA. The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch accepts legal responsibility for the contents of reports. This publication is not a prospectus as defined in the SFA. It may not be further distributed in whole or in part for any purpose. The Hongkong and Shanghai Banking Corporation Limited Singapore Branch is regulated by the Monetary Authority of Singapore. Recipients in Singapore should contact a "Hongkong and Shanghai Banking Corporation Limited, Singapore Branch" representative in respect of any matters arising from, or in connection with this report. Please refer to The Hongkong and Shanghai Banking Corporation Limited Singapore Branch's website at www.business.HSBC.com.sg for contact details. In Australia, this publication has been distributed by The Hongkong and Shanghai Banking Corporation Limited (ABN 65 117 925 970, AFSL 301737) for the general information of its "wholesale" customers (as defined in the Corporations Act 2001). Where distributed to retail customers, this research is distributed by HSBC Bank Australia Limited (ABN 48 006 434 162, AFSL No. 232595). These respective entities make no representations that the products or services mentioned in this document are available to persons in Australia or are necessarily suitable for any particular person or appropriate in accordance with local law. No consideration has been given to the particular investment objectives, financial situation or particular needs of any recipient.

HSBC Securities (USA) Inc. accepts responsibility for the content of this research report prepared by its non-US foreign affiliate. The information contained herein is under no circumstances to be construed as investment advice and is not tailored to the needs of the recipient. All US persons receiving and/or accessing this report and intending to effect transactions in any security discussed herein should do so with HSBC Securities (USA) Inc. in the United States and not with its non-US foreign affiliate, the issuer of this report. HSBC México, SA, Institución de Banca Múltiple, Grupo Financiero HSBC is authorized and regulated by Secretaría de Hacienda y Crédito Público and Comisión Nacional Bancaria y de Valores (CNBV). In Brazil, this document has been distributed by Banco HSBC SA ("HSBC Brazil"), and/or its affiliates. As required by Resolution No. 20/2021 of the Securities and Exchange Commission of Brazil (Comissão de Valores Mobiliários), potential conflicts of interest concerning (i) HSBC Brazil and/or its affiliates; and (ii) the analyst(s) responsible for authoring this report are stated on the chart above labelled "HSBC & Analyst Disclosures". If you are a customer of HSBC International Wealth & Premier Banking ("IWPB"), including HSBC Private Bank, you are eligible to receive this publication only if: (i) you have been approved to receive relevant research publications by an applicable HSBC legal entity; (ii) you have agreed to the applicable HSBC entity's terms and conditions and/or customer declaration for accessing research; and (iii) you have agreed to the terms and conditions of any other internet banking, online banking, mobile banking and/or investment services offered by that HSBC entity, through which you will access research publications (collectively with (ii), the "Terms"). If you do not meet the above eligibility requirements, please disregard this publication and, if you are a IWPB customer, please notify your Relationship Manager or call the relevant customer hotline. Distribution of this publication is the sole responsibility of the HSBC entity with whom you have agreed the Terms. Receipt of research publications is strictly subject to the Terms and any other conditions or disclaimers applicable to the provision of the publications that may be advised by IWPB.

© Copyright 2026, The Hongkong and Shanghai Banking Corporation Limited, ALL RIGHTS RESERVED. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, on any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of The Hongkong and Shanghai Banking Corporation Limited.

[1279101]
"""
