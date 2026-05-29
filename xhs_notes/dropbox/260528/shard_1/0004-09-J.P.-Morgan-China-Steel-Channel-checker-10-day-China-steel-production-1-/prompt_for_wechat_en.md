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
# China Steel - Channel checker

10-day China steel production -1% vs previous (+1% YoY). FOB iron ore prices flat since start of conflict as shipping costs rise

10-day China steel output 1,026Mt annualised, -1% vs previous: latest China daily crude steel output (10 days to 20 May) is tracking at a run rate of 1,026Mt annualised, -1% vs previous 10-day period (to 10 May), +1% YoY. Trailing 30-day steel production is +3% vs the previous 30 days and flat YoY, tracking at the bottom end of the 5-year range.

Spot CFR iron ore prices have eased back to \$105/t, but freight rates have increased to a post-Iran high of \$15.65/t Australia-China, Brazil-China is \$36.25/t. Net of freight, Australian FOB prices are \$2/t higher vs before the conflict (+3%), Brazil FOB prices are \$5/t lower (-7%). Our latest JPM Global iron ore market analysis raised prices \~\$5/t (link) to \$105/\$99/t in 2026/27 and JPM raised our long-term real price to \$90/t (\$80/t previous). These CFR price increases reflect higher marginal costs in the industry cost curve, rather than a demand driven increase.

Following a major accident at the Liushenyu coal mine in Shanxi, China, JPM APAC Mining estimates $\sim 122\mathrm{Mt}$ , or $\sim 3\%$ of China's total coking coal capacity is suspended (link). Shanxi represents $\sim 30\%$ of China's coking coal capacity and a prolonged shut down could meaningfully impact prices. China coking coal futures prices increased $>10\%$ since the accident. Separately, Mysteel reports production inspections in China's key energy intensive sectors, which could lead to restrictions in aluminium (link).

We published our EMEA Metals & Mining sector update today (link) and note that EMEA Miners trade at $< 10\%$ vs Fair Value under our base case, taking into account $5 - 10\%$ cost inflation and a cautious outlook for global macroeconomic environment. With rich valuations and global macro uncertainties, we remain UW Anglo American & Kumba Iron Ore, Neutral on BHP, Rio Tinto & Glencore. Norsk Hydro continues to be our only OW in the Industrials Metals space for its exposure to aluminium.

![](images/c13ac7b68739375ad7afb5fbf1ae05e91b5c87a0624f2e6462276263493e331a.jpg)

# European Metals, Mining & Steel

Dominic O'Kane AC

(44-20) 7742-6729

dominic.j.okane@JPM.com

JPM Securities plc

Patrick Jones

(44-20) 7742-5964

patrick.jones@JPM.com

JPM Securities plc

Varun Bhattad

(91-22) 6157-5027

varun.bhattad@jpmchase.com

JPM India Private Limited

Rosie Jia

(44-20) 3493-7448

rosie.jia@JPM.com

JPM Securities plc

Figure 1: Total China steel output 1,026Mt annualised run rate: daily CISA steel output for 10-days ended 20 May: -1% vs previous (+1% YoY), in line with seasonal trend   
![](images/da1521554be3e325b676fcad7451a8913715e444e03202429aa6c2cd5617f1f3.jpg)

<details>
<summary>line</summary>

| Month | 2025 | 2026 |
|-------|------|------|
| Jan   | 950  | 900  |
| Feb   | 980  | 870  |
| Mar   | 1000 | 910  |
| Apr   | 1020 | 980  |
| May   | 1030 | 1040 |
| Jun   | 1010 | 1020 |
| Jul   | 1000 | 1010 |
| Aug   | 980  | 950  |
| Sep   | 960  | 930  |
| Oct   | 940  | 880  |
| Nov   | 920  | 850  |
| Dec   | 830  | 730  |
</details>

Source: JPM estimates, CISA, Bloomberg Finance L.P.   
LHS: Iron ore price \$/mt; RHS: Shipping cost \$/mt

Figure 2: FOB iron ore price from Australia to China at \~\$89/t, flat vs end of Feb

![](images/e1073694ba5c1b0dea0f997071ca4576a598e47c01c21dbd1d21158d0a0f3ed4.jpg)

<details>
<summary>line</summary>

| Month   | CFR - 62% Iron Ore Price | FOB - 62% Iron Ore - Australia |
|---------|--------------------------|--------------------------------|
| Jan-25  | ~91                      | ~85                            |
| Feb-25  | ~97                      | ~90                            |
| Mar-25  | ~98                      | ~88                            |
| Apr-25  | ~93                      | ~82                            |
| May-25  | ~89                      | ~81                            |
| Jun-25  | ~90                      | ~80                            |
| Jul-25  | ~91                      | ~79                            |
| Aug-25  | ~97                      | ~87                            |
| Sep-25  | ~99                      | ~88                            |
| Oct-25  | ~100                     | ~89                            |
| Nov-25  | ~98                      | ~86                            |
| Dec-25  | ~100                     | ~87                            |
| Jan-26  | ~107                     | ~98                            |
| Feb-26  | ~104                     | ~95                            |
| Mar-26  | ~95                      | ~85                            |
| Apr-26  | ~106                     | ~93                            |
| May-26  | ~110                     | ~95                            |
</details>

FOB $62\%$ Iron Ore price calculated as CFR $62\%$ Iron Ore price less West Australia to Qingdao bulk shipping costs.   
Source: JPM estimates, Bloomberg Finance L.P.

Figure 3: China steel mill margins remain loss making but China HRC margins have shown improvements in the past few weeks on improving onshore HRC prices   
![](images/b2172205497af82ca39b4055d6b3e3ab126ce7473d3cee7efa930aa65409098b.jpg)

<details>
<summary>line</summary>

| Date    | China HRC Margin | China Rebar Margin |
|---------|------------------|--------------------|
| Jun-19  | ~200             | ~400               |
| Dec-19  | ~400             | ~750               |
| Jun-20  | ~300             | ~500               |
| Dec-20  | ~600             | ~200               |
| Jun-21  | ~1,300           | ~1,000             |
| Dec-21  | ~700             | ~500               |
| Jun-22  | ~100             | ~-400              |
| Dec-22  | ~150             | ~-250              |
| Jun-23  | ~100             | ~-300              |
| Dec-23  | ~-200            | ~-500              |
| Jun-24  | ~-500            | ~-400              |
| Dec-24  | ~-100            | ~-300              |
| Jun-25  | ~150             | ~-100              |
| Dec-25  | ~-100            | ~-400              |
</details>

Source: Bloomberg Finance L.P, JPM estimates.

Figure 4: Iron ore bulk shipping costs from Australia, Brazil and South Africa to China are all $+45\%$ since start of the Iran conflict   
LHS: Iron ore price \$/mt; RHS: Shipping cost \$/mt   
![](images/4a1074f0d64329cade396b9c97c29de46a19c91432e3dd1a352288234879bb16.jpg)

<details>
<summary>line</summary>

| Month   | West Australia to Qingdao | Tubarao to Qingdao | Saldanha to Beilun |
|---------|----------------------------|---------------------|---------------------|
| Jan-25  | 7                          | 18                  | 13                  |
| Feb-25  | 6                          | 17                  | 12                  |
| Mar-25  | 9                          | 24                  | 15                  |
| Apr-25  | 8                          | 20                  | 18                  |
| May-25  | 7                          | 19                  | 15                  |
| Jun-25  | 8                          | 27                  | 19                  |
| Jul-25  | 6                          | 19                  | 14                  |
| Aug-25  | 9                          | 24                  | 18                  |
| Sep-25  | 10                         | 24                  | 18                  |
| Oct-25  | 10                         | 25                  | 19                  |
| Nov-25  | 9                          | 23                  | 18                  |
| Dec-25  | 11                         | 24                  | 20                  |
| Jan-26  | 8                          | 23                  | 17                  |
| Feb-26  | 9                          | 26                  | 18                  |
| Mar-26  | 10                         | 30                  | 21                  |
| Apr-26  | 13                         | 32                  | 23                  |
| May-26  | 15                         | 37                  | 27                  |
</details>

FOB 62% Iron Ore price calculated as CFR 62% Iron Ore price less West Australia to Qingdao bulk shipping costs.   
Source: JPM estimates, Bloomberg Finance L.P.

Figure 5: Total China Steel exports (seasonality): Apr'26 export run-rate of 116Mtpa at top end of historical average   
Mtpa exports (annualised)   
![](images/11d671d4143a5fe74021138ee396444704ca16265d6f270c4dc7d69fc498f43c.jpg)

<details>
<summary>line</summary>

| Month | Avg (6yr) | 2026 YTD |
|-------|-----------|----------|
| Jan   | 75        | 90       |
| Feb   | 70        | 95       |
| Mar   | 90        | 100      |
| Apr   | 95        | 110      |
| May   | 90        | 115      |
| Jun   | 85        | 110      |
| Jul   | 80        | 105      |
| Aug   | 80        | 100      |
| Sep   | 85        | 95       |
| Oct   | 80        | 90       |
| Nov   | 80        | 85       |
| Dec   | 85        | 80       |
</details>

Source: JPM estimates, Bloomberg Finance L.P.

Figure 6: 4M'2026 China steel exports at 34Mt, tracking at \~ 10% of total output   
![](images/d73ac6a7505eb19ad590309ec929f44c47d83cb1421c129ce723631b7d37d134.jpg)

<details>
<summary>bar_line</summary>

| Year | Total exports (Mt) | YTD run-rate (%) | % of total crude steel production (RHS) |
|---|---|---|---|
| 2017 | 76 | 10 | 9.5 |
| 2018 | 70 | 8 | 8.5 |
| 2019 | 64 | 7 | 7.5 |
| 2020 | 54 | 5 | 6.5 |
| 2021 | 67 | 7 | 7.5 |
| 2022 | 67 | 7 | 8.0 |
| 2023 | 91 | 9 | 10.0 |
| 2024 | 111 | 12 | 12.5 |
| 2025 | 119 | 12 | 13.0 |
| 2026 | 34 | 10 | 11.0 |
</details>

Source: JPM estimates, Bloomberg Finance L.P.

Figure 7: Official NBS China steel output (annualised) – we estimate 2026 China steel production at \~1,000Mt   
![](images/a568e762db192bb86242b3f5c5e44d62dbb56dde7283d062e475e7218ee6d7f4.jpg)

<details>
<summary>bar</summary>

| Year | Production (Mt) |
| :--- | :--- |
| 2016 | 808 |
| 2017 | 832 |
| 2018 | 928 |
| 2019 | 996 |
| 2020 | 1,065 |
| 2021 | 1,033 |
| 2022 | 1,013 |
| 2023 | 1,019 |
| 2024 | 1,005 |
| 2025 | 961 |
| 2026 | 669 |
| 2026 | 331 |
</details>

Source: JPM estimates, NBS, Bloomberg Finance L.P.

Figure 8: China steel inventory week ending 21 May, -1% WoW and +9% YoY; total steel inventory tracking in line with seasonal level   
![](images/d1ae95c16ce8eb3700f2fbb073872a96c0a77db5ca99fff9a077274a41824620.jpg)

<details>
<summary>line</summary>

| Month | 5 year range | 2025 | 2026 |
|-------|--------------|------|------|
| Jan   | ~24.0        | ~21.0 | 26.0 |
| Feb   | ~30.0        | ~23.0 | 27.0 |
| Mar   | ~40.0        | ~31.0 | 31.0 |
| Apr   | ~35.0        | ~29.0 | 31.0 |
| May   | ~36.0        | ~27.0 | 30.0 |
| Jun   | ~34.0        | ~27.0 | -    |
| Jul   | ~33.0        | ~27.0 | -    |
| Aug   | ~32.0        | ~27.0 | -    |
| Sep   | ~31.0        | ~28.0 | -    |
| Oct   | ~30.0        | ~29.0 | -    |
| Nov   | ~29.0        | ~28.0 | -    |
| Dec   | ~28.0        | ~27.0 | -    |
</details>

Source: JPM estimates, Bloomberg Finance L.P.

Figure 9: Iron Ore inventory held at ports in China at \~160Mt, tracking at historical high but 7Mt down since peak inventory in March   
![](images/64086b44dbf012671bbf35c4775e20542713f5f5f61b64d195432943f1299085.jpg)

<details>
<summary>line</summary>

| Month | 2025 | 2026 |
|-------|------|------|
| Jan   | 145  | 150  |
| Feb   | 147  | 158  |
| Mar   | 140  | 168  |
| Apr   | 138  | 167  |
| May   | 135  | 162  |
| Jun   | 132  | -    |
| Jul   | 130  | -    |
| Aug   | 130  | -    |
| Sep   | 132  | -    |
| Oct   | 132  | -    |
| Nov   | 135  | -    |
| Dec   | 148  | -    |
</details>

Source: JPM estimates, Bloomberg Finance L.P.

Companies Discussed in This Report (all prices in this report as of market close on 25 May 2026, unless otherwise indicated) Anglo American(AAL.L/3,835p[22 May 2026]/UW), Anglo American (AGLJ.J)(AGLJ.J/86,328c/UW), Antofagasta(ANTO.L/3,931p[22 May 2026]/N), BHP Group Ltd (BHG SJ)(BHGJ.J/70,670c/N), BHP Group Ltd (BHP LN) (BHPB.L/3,137p[22 May 2026]/N), First Quantum Minerals Ltd(FM.TO/C\$39.74/N), Glencore PLC(GLEN.L/569p[22 May 2026]/N), Glencore plc (GLN SJ)(GLNJ.J/12,703c/N), Kumba Iron Ore Limited(KIOJ.J/30,704c/UW), Lundin Mining(LUMIN.ST/Skr268.30/UW), Lundin Mining Corp(LUN.TO/C\$39.89/UW), Norsk Hydro(NHY.OL/Nkr110.90[22 May 2026]/OW), Rio Tinto plc(RIO.L/7,777p[22 May 2026]/N)

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

# Important Disclosures

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

# Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe of the relevant duration of the region. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap Equity Research, each stock's expected total return is compared to the expected total return of a benchmark country market index, not to those Research Analysts' coverage universe. If it does not appear in the Important Disclosures section of this report, the certifying Research Analyst's coverage universe can be found on JPM's Research website, https://www.JPMmarkets.com.

Coverage Universe: O'Kane, Dominic J: Acerinox (ACX.MC), Anglo American (AAL.L), Anglo American (AGLJ.J) (AGLJ.J), Aperam (APAM.AS), ArcelorMittal (MT.AS), BHP Group Ltd (BHG SJ) (BHGJ.J), BHP Group Ltd (BHP LN) (BHPB.L), Glencore PLC (GLEN.L), Glencore plc (GLN SJ) (GLNJ.J), Harmony Gold Mining Co Ltd (HARJ.J), Harmony Gold Mining-ADR (HMY), Impala Platinum Holdings Ltd (IMPJ.J), Kumba Iron Ore Limited (KIOJ.J), Northam Platinum Ltd (NPHJ.J), Outokumpu (OUT1V.HE), Rio Tinto plc (RIO.L), SSAB-A (SSABa.ST), SSAB-B (SSABb.ST), Salzgitter (SZGG.DE), Sibanye-Stillwater (SSWJ.J), Sibanye-Stillwater-ADR (SBSW), ThyssenKrupp (TKAG.DE), Valterra Platinum - ADR (AGPPF), Valterra Platinum Limited (VALJ.J), voestalpine (VOES.VI)

JPM Equity Research Ratings Distribution, as of April 04, 2026 

<table><tr><td></td><td>Overweight (buy)</td><td>Neutral (hold)</td><td>Underweight (sell)</td></tr><tr><td>JPM Global Equity Research Coverage*</td><td>51%</td><td>37%</td><td>12%</td></tr><tr><td>IB clients**</td><td>83%</td><td>79%</td><td>74%</td></tr><tr><td>JPMS Equity Research Coverage*</td><td>49%</td><td>39%</td><td>13%</td></tr><tr><td>IB clients**</td><td>94%</td><td>93%</td><td>85%</td></tr></table>

\*Please note that the percentages may not add to $100\%$ because of rounding.  
\*\*Percentage of subject companies within each of the "buy," "hold" and "sell" categories for which JPM has provided investment banking services within the previous 12 months.

For purposes of FINRA ratings distribution rules only, our Overweight rating falls into a buy rating category; our Neutral rating falls into a hold rating category; and our Underweight rating falls into a sell rating category. Please note that stocks with an NR designation are not included in the table above. This information is current as of the end of the most recent calendar quarter.

Equity Valuation and Risks: For valuation methodology and risks associated with covered companies or price targets for covered companies, please see the most recent company-specific research report at http://ww

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 26 May 2026 10:42 AM BST

Disseminated 26 May 2026 10:42 AM BST
"""
