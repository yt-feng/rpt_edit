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
This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

# China Insurance

## Profit alerts lift EPS hopes, but dividends decide the trade; prefer Ping An-H

New China Life's positive profit alert, with 1H26E NP guided at Rmb20.7B to Rmb23.7B (link), up $40\%$ to $60\%$ oya versus FY26E consensus NP of Rmb30.7B, should support sentiment and EPS revisions for China insurers ahead of the interim reporting season in mid to late August. The market backdrop has also improved, with China's CSI300 index up $7.6\%$ in the 1H26 and the 10-year government bond yield moderating to $1.73\%$ at end-Jun-26 from $1.81\%$ at end-Mar-26. Stronger investment income could therefore drive 1H earnings upside across the sector, particularly for China Life and CPIC, given their larger equity exposure classified as FVTPL. However, we believe the stock market response to profit alerts has become increasingly selective under IFRS-17/9, as a larger portion of earnings volatility is driven by unrealised valuation gains on the balance sheet. As such, investors are likely to focus less on headline NP beats but more on whether stronger earnings translate into higher interim DPS, improving CSM quality and sustained life sales momentum. We prefer Ping An-H.

\- Positive profit alerts are helpful, but DPS is the real test. Based on our estimates, a $10\%$ move in the SHCOMP Index would imply around $46\%$ sensitivity on average to FY26E consensus NP (Figure 4), suggesting the scope for EPS upgrades if equity markets remain resilient. However, unrealised gains both assets and liabilities are not typically a direct source of dividend distribution. We therefore expect the scale of interim dividend increases to be the key earnings-related catalyst, particularly for insurers with strong capital positions and progressive dividend policies.

\- Fundamentals still matter beyond the earnings beat. H-listed insurers appear inexpensive, trading at 5-7x FY26E P/E with a dividend yield of $4 - 6\%$ . Into 1H26 results, we expect investors to focus on three issues: whether double-digit life sales momentum can be sustained into 2H26, whether sales quality and margins remain healthy, and whether CSM growth is accelerating as a leading indicator of future core earnings. For non-life insurers, we expect limited surprise, with combined ratios likely around $96\%$ in 1H26. Any upside from non-auto underwriting would be the main area to watch. We are quite optimistic on fundamental upside case especially for Ping An Group and China Life.

\- Prefer Ping An-H. China's H-listed insurers have underperformed YTD, and Ping An-H's consensus FY26E dividend yield has risen to $6.4\%$ , while we forecast at $6.3\%$ . Given its steady DPS growth outlook, solid life franchise, $36\%$ oya FY26E NBV growth forecast and $11\%$ oya FY26E OPAT growth outlook, we view the current profit alert window as an opportunity to accumulate Ping An-H. China Life-H could also benefit from potential profit alert momentum, especially if accompanied by a DPS hike, while CPIC-H offers a comparable $5.5\%$ yield. Overall, we continue to prefer life insurers over non-life names, with PICC P&C and PICC Group-H remaining our least preferred stocks in the sector.

Insurance  
MW Kim AC  
(852) 2800-8517  
mw.kim@JPM.com  
JPM Securities (Asia Pacific) Limited/  
JPM Broking (Hong Kong) Limited

Dan Wang  
(86-21) 6106-6349  
dan.wang@JPM.com  
SAC Registration Number: S1730524080001  
JPM Securities (China) Company Limited

Julia Kim  
(852) 2800-8540  
julia.c.kim@JPM.com  
JPM Securities (Asia Pacific) Limited/  
JPM Broking (Hong Kong) Limited

Table 1: China Insurance: Comps table  
Rmb per share, HKD per share, x, %

<table><tr><td>Company</td><td>B&#x27;berg Code</td><td>Rating</td><td>Price (13-Jul-2026)</td><td>PT (Dec-26)</td><td>Upside/ downside</td><td>P/E 26e</td><td>P/E 27e</td><td>P/BV 26e</td><td>P/BV 27e</td></tr><tr><td>China Life-H</td><td>2628 HK Equity</td><td>OW</td><td>27.5</td><td>40.0</td><td>45%</td><td>5</td><td>4</td><td>1.0</td><td>1.0</td></tr><tr><td>China Life-A</td><td>601628 CH Equity</td><td>N</td><td>37.7</td><td>39.0</td><td>3%</td><td>18</td><td>16</td><td>1.6</td><td>1.5</td></tr><tr><td>Ping An-H</td><td>2318 HK Equity</td><td>OW</td><td>53.3</td><td>90.0</td><td>69%</td><td>6</td><td>6</td><td>0.7</td><td>0.7</td></tr><tr><td>Ping An-A</td><td>601318 CH Equity</td><td>OW</td><td>49.5</td><td>83.0</td><td>68%</td><td>6</td><td>6</td><td>0.8</td><td>0.7</td></tr><tr><td>CPIC-H</td><td>2601 HK Equity</td><td>OW</td><td>27.4</td><td>43.0</td><td>57%</td><td>5</td><td>5</td><td>0.6</td><td>0.6</td></tr><tr><td>CPIC-A</td><td>601601 CH Equity</td><td>OW</td><td>29.6</td><td>50.0</td><td>69%</td><td>7</td><td>7</td><td>0.8</td><td>0.7</td></tr><tr><td>New China Life-H</td><td>1336 HK Equity</td><td>N</td><td>43.4</td><td>45.0</td><td>4%</td><td>5</td><td>5</td><td>1.0</td><td>0.9</td></tr><tr><td>New China Life-A</td><td>601336 CH Equity</td><td>N</td><td>62.0</td><td>59.0</td><td>-5%</td><td>8</td><td>8</td><td>1.6</td><td>1.5</td></tr><tr><td>PICC Group-H</td><td>1339 HK Equity</td><td>N</td><td>4.9</td><td>5.8</td><td>18%</td><td>5</td><td>5</td><td>0.4</td><td>0.4</td></tr><tr><td>PICC Group-A</td><td>601319 CH Equity</td><td>N</td><td>7.1</td><td>6.9</td><td>-2%</td><td>11</td><td>9</td><td>1.0</td><td>1.0</td></tr><tr><td>PICC P&amp;C</td><td>2328 HK Equity</td><td>N</td><td>14.0</td><td>14.0</td><td>0%</td><td>7</td><td>7</td><td>1.0</td><td>1.0</td></tr></table>

Source: Bloomberg Finance L,P. JPM estimates. Data as of 13 July 2026.

Figure 1: China H-share insurers: FY26E/27E dividend yield %  
![](images/11debf717bb44d253497f8f4d9fef77cea52663b43ed572bf5ee0bf44c7cce22.jpg)  
Source: Bloomberg Finance L,P. JPM estimates. Data as of 13 July 2026.

Figure 2: China A-share insurers: FY26E/27E dividend yield %  
![](images/059c4ef4315224a1e30ed0e450a444594907381d9aba5e7e9c34a10bc5c9f64d.jpg)  
Source: Bloomberg Finance L,P. JPM estimates. Data as of 13 July 2026.

Figure 3: China Insurance: Equity investment breakdown by accounting classification %  
![](images/f6a0e998cc5159cdf68289b0a540fa65c4f6c1f5b084080841b853e8254bf385.jpg)  
Source: Each company's FY24-25 annual reports, JPM calculations.

Figure 4: China Insurance: FY26E consensus NP sensitivity to 10% movement of SHCOMP Index  
![](images/e88ba0bb5e90c1b3806e7448269089270bcafd6600cf115f05403c9f980df285.jpg)  
Source: Each company's FY25 annual report, Bloomberg Finance L.P., JPM estimates. Note: Consensus data is as of 13 July 2026.

Figure 5: China H-share Insurance: YTD stock performance %  
![](images/5cf658dbbd93c1ad0c1b687552d9dcb857969b01d430e6daccbb3ca712edebec.jpg)  
Source: Bloomberg Finance L.P. Price as of 13 July 2026. Note: Past performance is not an indicator of future results

Figure 6: China A-share Insurance: YTD stock performance %  
![](images/3befee64aa57d77c23ced6bbe533d637b4433f377d10456555a6a7dfc6e8828b.jpg)  
Source: Bloomberg Finance L.P. Price as of 13 July 2026. Note: Past performance is not an indicator of future results

Table 2: China Insurance: Shareholder return policy summary

<table><tr><td>Company</td><td>Mid-to-long-term capital management guidance</td></tr><tr><td>China Life</td><td rowspan="2">China Life has proposed an interim dividend of Rmb0.238 and final total dividend of Rmb0.86, implying 16%/18% payout ratio in 2025. In 2024-2026, the company&#x27;s annual distributable profit in each profitable year will be positive. In compliance with the solvency adequacy ratio requirements of the national laws and regulations, the company&#x27;s annual dividend amount will be 20-50% of the audited net profit attributable to the parent. Ping An Group has also historically paid out interim dividend. The company has grown cash dividends for 14 consecutive years.</td></tr><tr><td>Ping An Group</td></tr><tr><td></td><td rowspan="2">CPIC affirmed its intention to introduce interim dividend commencing in 2026. Company determines interim and final dividend based on OPAT and investment performance. The initial payout ratio is expected to be set prudently, reflecting management&#x27; focus on sustaining both the flexibility and long-term credibility of the dividend policy.</td></tr><tr><td>CPIC</td></tr><tr><td>PICC Group</td><td>PICC Group has proposed an interim dividend of Rmb0.075 and final total dividend of Rmb0.22, implying 13%/21% payout ratio in 2025.</td></tr><tr><td>New China Life</td><td>NCI has proposed an interim dividend of Rmb0.67 and final total dividend of Rmb2.73, implying 14%/23% payout ratio in 2025.</td></tr><tr><td>PICC P&amp;C</td><td>PICC P&amp;C has proposed an interim dividend of Rmb0.24 and final total dividend of Rmb0.68, implying 22%/37% payout ratio in 2025.</td></tr></table>

Source: Each company's FY25 annual report and earnings PPT.

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe of the relevant duration of the region. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap Equity Research, each stock's expected total return is compared to the expected total return of a benchmark country market index, not to those Research Analysts' coverage universe. If it does not appear in the Important Disclosures section of this report, the certifying Research Analyst's coverage universe can be found on JPM's Research website, https://www.JPMmarkets.com.

Coverage Universe: Kim, MW : AIA Group Ltd (1299) (1299.HK), Bangkok Life (BLA.BK), China Life Insurance - A (601628.SS), China Life Insurance - H (2628.HK), China Pacific Insurance Group - A (601601.SS), China Pacific Insurance Group - H (2601.HK), DB Insurance Co Ltd (005830.KS), FWD Group Holdings (1828.HK), Hanwha Life Insurance (088350.KS), Hyundai Marine & Fire Insurance (001450.KS), Korean Reinsurance Company (003690.KS), LPI Capital (LOND.KL), New China Life Insurance - A (601336.SS), New China Life Insurance - H (1336.HK), PICC Group - A (601319.SS), PICC Group - H (1339.HK), PICC Property and Casualty (2328) (2328.HK), Ping An Insurance Group - A (601318.SS), Ping An Insurance Group - H (2318.HK), Samsung Fire & Marine Insurance (000810.KS), Samsung Life Insurance (032830.KS), Seoul Guarantee Insurance (031210.KS), Thai Life Insurance (TLI.BK)

JPM Equity Research Ratings Distribution, as of July 04, 2026

<table><tr><td></td><td>Overweight (buy)</td><td>Neutral (hold)</td><td>Underweight (sell)</td></tr><tr><td>JPM Global Equity Research Coverage*</td><td>53%</td><td>36%</td><td>12%</td></tr><tr><td>IB clients**</td><td>83%</td><td>80%</td><td>73%</td></tr><tr><td>JPMS Equity Research Coverage*</td><td>51%</td><td>37%</td><td>12%</td></tr><tr><td>IB clients**</td><td>95%</td><td>92%</td><td>87%</td></tr></table>

\*Please note that the percentages may not add to 100% because of rounding.  
\*\*Percentage of subject companies within each of the "buy," "hold" and "sell" categories for which JPM has provided investment banking services within the previous 12 months.  
For purposes of FINRA ratings distribution rules only, our Overweight rating falls into a buy rating category; our Neutral rating falls into a hold rating category; and our Underweight rating falls into a sell rating category. Please note that stocks with an NR designation are not included in the table above. This information is current as of the end of the most recent calendar quarter.

Equity Valuation and Risks: For valuation methodology and risks associated with covered companies or price targets for covered companies, please see the most recent company-specific research report at http://www.JPMmarkets.com, contact the primary analyst or your JPM representative, or email research.disclosure.inquiries@JPM.com. For material information about the proprietary models used, please see the Summary of Financials in company-specific research reports and the Company Tearsheets, which are available to download on the company pages of our client website, http://www.JPMmarkets.com. This report also sets out within it the material underlying assumptions used.

## History of Investment Recommendations:

A history of JPM investment recommendations disseminated during the preceding 12 months can be accessed on the Research & Commentary page of http://www.JPMmarkets.com where you can also search by analyst name, sector or financial instrument.

Analysts' Compensation: The research analysts responsible for the preparation of this report receive compensation based upon various factors, including the quality and accuracy of research, client feedback, competitive factors, and overall firm revenues.

Registration of non-US Analysts: Unless otherwise noted, the non-US analysts listed on the front of this report are employees of non-US affiliates of JPM Securities LLC, may not be registered as research analysts under FINRA rules, may not be associated persons of JPM Securities LLC, and may not be subject to FINRA Rule 2241 or 2242 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

## Other Disclosures

JPM is a marketing name for investment banking businesses of JPM Chase & Co. and its subsidiaries and affiliates worldwide.

UK MIFID FICC research unbundling exemption: UK clients should refer to UK MIFID Research Unbundling exemption for details of JPM's implementation of the FICC research exemption and guidance on relevant FICC research categorisation.

All research material made available to clients are simultaneously available on our client website, JPM Markets, unless specifically permitted by relevant laws. Not all research content is redistributed, e-mailed or made available to third-party aggregators. For all research material available on a particular stock, please contact your sales representative.

Any long form nomenclature for references to China; Hong Kong; Taiwan; and Macau within this research material are Mainland China; Hong Kong SAR (China); Taiwan (China); and Macau SAR (China).

JPM may, from time to time, write on issuers or securities targeted by economic or financial sanctions imposed or administered by the governmental authorities of the U.S., EU, UK or other relevant jurisdictions (Sanctioned Securities). Nothing in this report is intended to be read or construed as encouraging, facilitating, promoting or otherwise approving investment or dealing in such Sanctioned Securities. Clients should be aware of their own legal and compliance obligations when making investment decisions.

Any digital or crypto assets discussed in this research report are subject to a rapidly changing regulatory landscape. For relevant regulatory advisories on crypto assets, including bitcoin and ether, please see https://w

[中间内容因长度限制已省略]

erial only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own

independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
