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
China high frequency data implies higher rates of copper & aluminium consumption in June-July; China copper premium hit \$100/t last week

We present our high-frequency inventory trends for base metals and iron ore in China for the week ended 17 Jul'26. Our data plots China weekly metals inventory trends, a proxy for consumption. Copper saw another 17kt drawdown last week with visible inventory in China now down to \~120kt, 30kt below the low level we saw in 2025. End of last week, Yangshan Copper Premium hit \$100/t mark which was last reached in May'25. Aluminium's strong destocking also continued, with total visible inventory now back to \~1Mt. JPM Commodities Research forecast a sizeable 3Q ex-China deficit that will likely pull LME pricing higher to attract metals into the global market from China (link).

JPM Commodities Research published a China demand monitor based on detailed data available to 5M'26 (link). Our colleagues note that consumption-weighted end-use for China Copper demand fell -5% YoY in 5M'26, but apparent consumption was +8% yoy in May. However in the case of both Copper and Aluminium, these weak demand datapoints represent the period 5M'26 which is consistent with our previous high frequency data assessment of weak de-stocking indictators in the month of May. Our high frequency data tracker implies strengthening in copper and aluminium consumption in June-July, as shown in the charts below.

China Q2 economic releases last week showed Q2 real GDP slowed to 4.3% YoY, from 5.0% in 1Q; manufacturing was resilient but FAI contracted significantly. Latest loan growth data for June also showed material weakness, with TSF growth slowing by 0.3% pts to a record low of 7.4% (link / link).

Within EMEA Miners, our favoured name remains Antofagasta (link) as we see the copper price support to generate FCF inflection and an inexpensive valuation on a 2028E basis driven by $>30\%$ brownfield growth. We are Neutral on BHP and RIO London listings and are UW on Anglo American taking into account of cost inflation risk at its Iron Ore division and potential weak Diamonds division result in H1'26 (link).

We provide our latest EMEA Metals & Mining valuations and commodity price scenario analysis (here).

## European Metals, Mining & Steel

Dominic O'Kane AC
(44-20) 7742-6729
dominic.j.okane@JPM.com
JPM Securities plc

Patrick Jones
(44-20) 7742-5964
patrick.jones@JPM.com
JPM Securities plc

Asia Pacific Basic Materials

Lyndon Fagan
(61-2) 9003-8648
lyndon.fagan@JPM.com
JPM Securities Australia Limited

North America Metals, Mining & Clean Tech

Bill Peterson
(1-415) 315-6766
bill.peterson@jpmchase.com
JPM Securities LLC

Global Commodities Research

Gregory C. Shearer
(44-20) 7134-8161
gregory.c.shearer@JPM.com
JPM Securities plc

Figure 1: Weekly change in China visible copper inventory (SHFE + Bonded). Red box shows May period covered by JPM Commodities Research, Jun-July appear to show a pick up in consumption

x-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY), y-axis = kt of copper increase / (decrease)  
![](images/456c7e317dddb2886605838035f73bf35fd9d17014bc56011f4c11866bddf65a.jpg)  
\*Build over first and second weeks post-CNY averaged due to lagged inventory reporting.  
Source: SHFE, CRU, SMM, JPM Commodities, \*First and second weeks grouped together due to lagged inventory reporting

Figure 2: Aluminum inventories movements in 2026 – weekly change in China visible aluminium inventory (SHFE + Bonded). 52kt of Aluminium destocking in the past week, strongest since 2026 CNY

x-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY), y-axis = kt of aluminium increase / (decrease)  
![](images/52a2fb800deb26f316ce94d6516488a3437d86db02d727a75e8f9a6235812b80.jpg)  
\*Build over first and second weeks post-CNY averaged due to lagged inventory reporting.  
Source: SHFE, CRU, SMM, JPM Commodities, \*First and second weeks grouped together due to lagged inventory reporting

## China metals inventory channel check – week ended 17 July 2026

JPM is tracking China's metal inventories for potential insights regarding end-consumer demand activity. These high-frequency datapoints provide signals to gauge China metals consumption trends. Rapid pivots in inventory de-stocking volumes (or re-stocking) can potentially provide signals that downstream consumption is improving (or weakening).

We are into the fifth week of seeing strong de-stocking in both Copper and Aluminium. Copper inventory saw another 17kt drawdown in the past week, bringing total visible copper inventory in China down to \~120kt. Aluminium also continued the strong de-stocking momentum with another drawdown of 54kt last week. Inventory level is now back to \~1Mt. Zinc however, saw re-stocking. Total onshore Zinc inventory is at 268kt, which is >130kt higher vs 5-year historical average at this time of the year.

Figure 3: Total China visible copper inventory (SHFE + Bonded) week ended 17 Jul'26. Copper inventory (119kt) tightest in the past decade during this time of the year; Inventory level sits 30kt below 2025 low  
x-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY), y-axis = kt of copper  
![](images/dce52117b6cfb7cfc30a94b152420b22831447274e9edb91dbba67f461065a28.jpg)  
Source: SHFE, CRU, SMM, JPM Commodities

Figure 4: Total China visible aluminum inventory (SHFE + Regional Warehouses) week ended 17 Jul'26. China aluminum inventory (1.0Mt) begins to fall due to stronger drawdowns in the past few weeks  
x-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY), y-axis = kt of aluminium  
![](images/bbd5392b71bd3e2f4ec114d6707d156306a7cb2d4b3540ee798047c23ec1dcb8.jpg)  
Source: SHFE, CRU, SMM, JPM Commodities

Figure 5: Zinc inventories movements in 2026 – weekly change in China visible zinc inventory (SHFE + Bonded). Zinc restocking of 3kt in the past week x-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY), y-axis = kt of aluminium increase / (decrease)  
![](images/01afd10d578eda08ce2a8cc6e7cffa82115aea6258149ce8851e4edbef20ba28.jpg)  
\*Build over first and second weeks post-CNY averaged due to lagged inventory reporting.
Source: SHFE, CRU, SMM, JPM Commodities, \*First and second weeks grouped together due to lagged inventory reporting

Figure 6: Total China visible zinc inventory for week ended 17 Jul'26. Total inventory (268kt) remains at the highest level since 2022 x-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY), y-axis = kt of zinc  
![](images/cb68ff1b139a379939be85a45ffa841625642574a94b47122155a5df566c6281.jpg)  
Source: SHFE, CRU, SMM, JPM Commodities Research

Figure 7: China Yangshan Copper Premium vs LME Copper Spot: Strong physical market demand brings premium to \$100/t
LHS: Yangshan Premium; RHS: LME Copper Spot; Unit: \$/t  
![](images/739c504a6b66880a160f288441db544e8cbfddd2e0478429a4f28d9c55efebf7.jpg)  
Source: Bloomberg Finance L.P.

Figure 8: China steel mill margins extend losses driven by higher coking coal prices  
![](images/cfb2e63653a950b17c238b4791ce95398ade0b3541ef987c99bf1ba5da53070f.jpg)  
Source: Bloomberg Finance L.P, JPM estimates.

Figure 9: China steel inventory week ending 17 Jul, flat WoW and +12% YoY; Inventory has picked up since June  
![](images/21f5a2bd0b6602cc88de2fc696ba11e0f25d0a07b3233b02757007e1478cf8fd.jpg)  
Source: JPM estimates, Bloomberg Finance L.P.

Figure 10: Iron Ore inventory saw \~3Mt drawdown in the past week after flat inventory for \~9 weeks  
![](images/609c07b93252b252daea69bb42eee84cc6f8fd46777cab13f7cb6a95d33c3ee4.jpg)  
Source: JPM estimates, Bloomberg Finance L.P.

Figure 11: Global iron ore shipments - Global shipments +2% MoM in May & -2% YoY  
Mt iron ore exports, red bar = February, typical seasonal trough for shipments is Jan/Feb  
![](images/1eb20227cdb13fd2310683a2706cb31e1e0db93077dfd2b4fcbb3c72b24d2d2b.jpg)  
Source: JPM estimates, Bloomberg Finance L.P.

Figure 12: Australia iron ore shipments - Latest data suggests Australian iron ore shipments +5% MoM in May& -2% YoY
Mt iron ore exports, red bar = February, typical seasonal trough for shipments is Jan/Feb  
![](images/80cb7b04b96a4b5c116cb23c5d5afab3c4242e5a33489515c41360883ba09be3.jpg)  
Source: JPM estimates, Bloomberg Finance L.P.

Figure 13: Brazil iron ore shipments -3% MoM in May, -8% YoY  
Mt iron ore exports, red bar = February, typical seasonal trough for shipments is Jan/Feb  
![](images/a8655d2436fd3d25e89d7dfeeeee0b60af54e773e8398a0493d3bda283976d5b.jpg)  
Source: JPM estimates, Bloomberg Finance L.P.

Figure 14: Chinese visible copper inventory (SHFE + Bonded) for week ended 17 Jul. Copper inventories lower in the past week due to significant inventory draw  
![](images/9c98b8cf8edf60b3ea0117b831586ef83f17a8bdc0e710c8606eff8a31dde56e.jpg)  
Source: SHFE, CRU, SMM, JPM Commodities

Figure 15: China visible aluminium inventory (SHFE + Regional Warehouses) for week ended 17 Jul. Destocking in the past few weeks has significantly reduced aluminium inventory  
![](images/c72c8ec5c7fd841598e056cd21ac0da4593b20817ee787da9ac77e48a46da3f8.jpg)  
Source: SHFE, CRU, SMM, JPM Commodities Research

Figure 16: China visible zinc inventory (SHFE + Regional Warehouses) for week ended 17 Jul. Zinc inventories are still at the highest level vs 5-year range kt of zinc  
![](images/37525409374fe27321da12bd50762ae739b39c7d37ca0505897f53c2d18672b5.jpg)  
Source: SHFE, CRU, SMM, JPM Commodities

Companies Discussed in This Report (all prices in this report as of market close on 17 July 2026, unless otherwise indicated)
Anglo American (AGLJ.J)(AGLJ.J/75,537c/UW), Antofagasta(ANTO.L/3,491p/OW), BHP Group Ltd (BHG SJ) (BHGJ.J/66,222c/N), Lundin Mining(LUMIN.ST/Skr225.80/UW), Norsk Hydro(NHY.OL/Nkr84.96/OW), Rio Tinto plc(RIO.L/6,726p/N)

## Disclosures

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe of the relevant duration of the region. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap Equity Research, each stock's expected total return is compared to the expected total return of a benchmark country market index, not to those Research Analysts' coverage universe. If it does not appear in the Important Disclosures section of this report, the certifying Research Analyst's coverage universe can be found on JPM's Research website, https://www.JPMmarkets.com.

Coverage Universe: O'Kane, Dominic J: Acerinox (ACX.MC), Anglo American (AAL.L), Anglo American (AGLJ.J) (AGLJ.J), Aperam (APAM.AS), ArcelorMittal (MT.AS), BHP Group Ltd (BHG SJ) (BHGJ.J), BHP Group Ltd (BHP LN) (BHPB.L), Glencore PLC (GLEN.L), Glencore plc (GLN SJ) (GLNJ.J), Harmony Gold Mining Co Ltd (HARJ.J), Harmony Gold Mining-ADR (HMY), Impala Platinum Holdings Ltd (IMPJ.J), Kumba Iron Ore Limited (KIOJ.J), Northam Platinum Ltd (NPHJ.J), Outokumpu (OUT1V.HE), Rio Tinto plc (RIO.L), SSAB-A (SSABa.ST), SSAB-B (SSABb.ST), Salzgitter (SZGG.DE), Sibanye-Stillwater (SSWJ.J), Sibanye-Stillwater-ADR (SBSW), ThyssenKrupp (TKAG.DE), Valterra Platinum - ADR (AGPPF), Valterra Platinum Limited (VALJ.J), voestalpine (VOES.VI)

## JPM Equity Research Ratings Distribution, as of July 04, 2026

<table><tr><td></td><td>Overweight (buy)</td><td>Neutral (hold)</td><td>Underweight (sell)</td></tr><tr><td>JPM Global Equity Research Coverage*</td><td>53%</td><td>36%</td><td>12%</td></tr><tr><td>IB clients**</td><td>83%</td><td>80%</td><td>73%</td></tr><tr><td>JPMS Equity Research Coverage*</td><td>51%</td><td>37%</td><td>12%</td></tr><tr><td>IB clients**</td><td>95%</td><td>92%</td><td>87%</td></tr></table>

\*Please note that the percentages may not add to 100% because of rounding.

\*\*Percentage of subject companies within each of the "buy," "hold" and "sell" categories for which JPM has provided investment banking services within the previous 12 months.

For purposes of FINRA ratings distribution rules only, our Overweight rating falls into a buy rating category; our Neutral rating falls into a hold rating category; and our Underweight rating falls into a sell rating category. Please note that stocks with an NR designation are not included in the table above. This information is current as of the end of the most recent calendar quarter.

Equity Valuation and Risks: For valuation methodology and risks associated with covered companies or price targets for covered companies, please see the most recent company-specific research report at http://www.JPMmarkets.com, contact the primary analyst or your JPM representative, or email research.disclosure.inquiries@JPM.com. For material information about the proprietary models used, please see the Summary of Financials in company-specific research reports and the Company Tearsheets, which are available to download on the company pages of our client website, http://www.JPMmarkets.com. This report also sets out within it the material underlying assumptions used.

## History of Investment Recommendations:

A history of JPM investment recommendations disseminated during the preceding 12 months can be accessed on the Research & Commentary page of http://www.JPMmarkets.com where you can also search by analyst name, sector or financial instrument.

Analysts' Compensation: The research analysts responsible for the preparation of this report receive compensation based upon various factors, including the quality and accuracy of research, client feedback, competitive factors, and overall firm revenues.

Registration of non-US Analysts: Unless otherwise noted, the non-US analysts listed on the front of this report are employees of non-US affiliates of JPM Securities LLC, may not be registered as research analysts under FINRA rules, may not be associated persons of JPM Securities LLC, and may not be subject to FINRA Rule 2241 or 2242 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

Company-Specific Disclosures: Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

## Other Disclosures

JPM is a marketing name for investment banking businesses of JPM Chase & Co. and its subsidiaries and affiliates worldwide.

UK MIFID FICC research unbundling exemption: UK clients should refer to UK MIFID Research Unbundling exemption for details of JPM's implementation of the FICC research exemption and guidance on relevant FICC research categorisation.

All research material made available to clients are simultaneously available on our client website, JPM Markets, unless specifically permitted by relevant laws. Not all research content is r

[中间内容因长度限制已省略]

ively JPM) make no representations or warranties whatsoever to the completeness or accuracy of the material provided, except with respect to any disclosures relative to JPM and the Research Analyst's involvement with the issuer that is the subject of the material. Accordingly, no reliance should be placed on the accuracy, fairness or completeness of the information contained in this material. There may be certain discrepancies with data and/or limited content in this material as a result of calculations, adjustments, translations to different languages, and/or local regulatory restrictions, as applicable. These discrepancies should not impact the overall investment analysis, views and/or recommendations of the subject company(ies) that may be discussed in the material. Artificial intelligence tools may have been used in the preparation of this material, including assisting in data analysis, pattern recognition, and content drafting for research material. JPM accepts no liability whatsoever for any loss arising from any use of this material or its contents, and neither JPM nor any of its respective directors, officers or employees, shall be in any way responsible for the contents hereof, apart from the liabilities and responsibilities that may be imposed on them by the relevant regulatory authority in the jurisdiction in question, or the regulatory regime thereunder. Opinions, forecasts or projections contained in this material represent JPM's current opinions or judgment as of the date of the material only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR
"""
