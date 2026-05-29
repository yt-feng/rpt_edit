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
# Strategy Trade update

Rates - Asia ex-Japan

# Maintain long CHF/JPY trade with a high conviction

SNB's interventions are likely to be measured rather than aggressive; MOF remains vigilant on FX, but no further escalation from last week

# The trade

Long CHF/JPY with a high conviction level of 4/5, with a target of 206.50 by end-June (entry at 200.20 on 30 April 2026).

# Rationale

SNB Chairman Schlegel's speech reaffirmed to the market that the central bank is willing to intervene in the FX market, particularly in view of increased CHF appreciation pressures stemming from the escalation of the Middle East conflict. There has also been little change in tone on FX intervention over the last few months ("greater" or "higher" willingness to intervene since March). It is difficult to predict the timing and size of intervention on a daily basis from publicly available SNB data. Monthly FX reserves data, adjusted for FX and portfolio valuation effects, do not suggest a meaningful pick up in FX intervention activity in March or April, although sporadic action is likely to have occurred, in our view. We believe EUR/CHF below 0.91 represents a level of caution for the market, as the pair recently rebounded after entering the 0.91–0.90 range.

However, Schlegel also noted in his presentation that CHF appreciation in real effective terms has been significantly less pronounced than in nominal effective terms (Fig. 1). From this perspective, we expect any SNB intervention to be measured rather than aggressive — aimed at easing appreciation pressures to limit disinflationary effects from the currency, rather than attempting to reverse the broader trend.

Notably, the SNB revised its inflation forecast higher at its March meeting relative to its December projection, yet the CPI outlook for 2026 remains at just 0.5% y-o-y, meaning significant disinflationary pressures are unwelcome (Fig. 2). Despite this, President Schlegel remains reluctant to return the policy rate to negative territory, emphasizing that inflation is stabilizing.

Given our views above, this reinforces our view that CHF depreciation driven by SNB FX intervention may occur on an occasional basis, but the policy rate will not serve as an influential factor to weaken the currency. Therefore, we believe capital flows such as the strong current account surplus, seasonal capital flows and safe-haven flows will continue to strongly support CHF into the end of the quarter.

Meanwhile, the Japanese currency authorities also remain vigilant on currency moves. On 19 May, Finance Minister Katayama conducted verbal intervention using the strongly worded phrase “bold action” that Japan could take when needed to counter disorderly market moves (source: Bloomberg). However, for the market to take the risk of actual intervention more seriously, what likely matters is whether verbal intervention escalates further through more frequent jawboning — not just from the Finance Minister, but also from Mimura, the Vice Minister of Finance for International Affairs at the MOF (i.e., the key person in charge of the MOF's intervention decisions). However, we have not seen jawboning from him recently.

In our recent survey, a majority of respondents (67.2%) expect the MOF to conduct intervention again by the time USD/JPY reaches 162 (Fig. 3). In this environment, where the market remains cautious but not alarmed about decisive MOF action, and with both 1m and 3m implied volatility significantly subdued, we believe intervention risk has not materially risen (Fig. 4). However, should USD/JPY continue to grind higher and approach the market's key 162 level, we would revisit our trade as the probability of the MOF acting to strengthen the currency would have increased.

# Research Analysts

# Global FX Strategy

Yusuke Miyairi, CFA - NIplc

yusuke.miyairi@NOM.com

+44 (0) 20 7102 4145

Dominic Bunning - Nlplc

dominic.bunning@NOM.com

+44 (0) 20 7102 4063

Fig. 1: CHF's effective exchange rate and SNB's intervention history   
![](images/7a1ab28cf1cc80cb5a1a89c63bdeeb212f642d52287ca6ec81d501b564cd7c54.jpg)

<details>
<summary>line</summary>

| Year | CHF real effective exchange rate, rhs | CHF nominal effective exchange rate, rhs | SNB's FX sales and CHF buying flows, lhs |
|------|----------------------------------------|------------------------------------------|------------------------------------------|
| 16   | -30                                    | -10                                      | -                                        |
| 17   | -35                                    | -15                                      | -                                        |
| 18   | -40                                    | -20                                      | -                                        |
| 19   | -35                                    | -10                                      | -                                        |
| 20   | -30                                    | 0                                        | 50                                       |
| 21   | -35                                    | 5                                        | 10                                       |
| 22   | -30                                    | 10                                       | 15                                       |
| 23   | -25                                    | 20                                       | -                                        |
| 24   | -30                                    | 30                                       | -                                        |
| 25   | -25                                    | 40                                       | 5                                        |
| 26   | -20                                    | 50                                       | -                                        |
</details>

Note: SNB's intervention results are quarterly data, which we converted to monthly data. Source: Macrobond, Bloomberg, NOM

Fig. 2: Actual CPI and SNB's CPI projection as of March 2026   
![](images/624d2f6062e2aad90400adffb90ec645681a02daa64f322eb758e4f169ca01c3.jpg)

<details>
<summary>line</summary>

| Year | SNB's CPI projection as of March 2026 |
| ---- | ------------------------------------- |
| 22   | 2.1                                   |
| 23   | 1.6                                   |
| 24   | 1.4                                   |
| 25   | 0.0                                   |
| 26   | 0.6                                   |
| 27   | 0.5                                   |
| 28   | 0.7                                   |
</details>

Source: Macrobond, NOM

Fig. 3: At what level do you think BOJ/MOF would intervene again to support JPY?   
![](images/535d65e875024c20fe3bfa55e3d55ffa7e230a6da4f25c267e942b4a82362866.jpg)

<details>
<summary>bar</summary>

| Category | Share of respondents (%) |
| :--- | :--- |
| ~160 | 30.2 |
| ~162 | 37.2 |
| ~165 | 12.4 |
| ~170 | 10.1 |
| Unlikely to intervene | 10.1 |
</details>

Note: Results are from NOM Pulse Check (issued on 26 May 2026), as of 28 May 2026.
Source: NOM

Fig. 4: Spot rate and implied volatilities of USD/JPY   
![](images/36d8f1348324a731719a041dcddbec08a395dc51b00a2d4cfe8a6eb72ea62ff5.jpg)  
Source: Bloomberg, NOM

Fig. 5: Long CHF/JPY - target 206.50 by end-June (conviction level 4/5)   
![](images/c36432d5c00989f762768a0046cd7ec8ed4dbb7b4fadddb605b5e95da96cac78.jpg)

<details>
<summary>line</summary>

| Date       | Conviction (0-5) | Latest Target (rhs) |
| ---------- | ---------------- | ------------------- |
| 1 May 2026 | 3                | 320                 |
</details>

Source: Bloomberg, NOM

Fig. 6: List of current strategy trades 

<table><tr><td>Trade</td><td>Target</td><td>Timeline</td><td>Conviction(0-5)</td><td>Entry Date</td></tr><tr><td>Short AUD/NZD</td><td>1.1750</td><td>end-Aug</td><td>3</td><td>27-May-26</td></tr><tr><td>Short USD/TWD</td><td>30.5</td><td>end-Sep</td><td>3</td><td>25-May-26</td></tr><tr><td>Long EUR/PHP</td><td>-</td><td>-</td><td>2</td><td>25-May-26</td></tr><tr><td>Long USD/CAD</td><td>1.425</td><td>end-Jul</td><td>3</td><td>22-May-26</td></tr><tr><td>Receive 2y2y Korea NDIRS</td><td>3.75%</td><td>end-Jun</td><td>3</td><td>22-May-26</td></tr><tr><td>Receive Jun-IMM 1y SORA</td><td>1.20%</td><td>end-Jun</td><td>3</td><td>15-May-26</td></tr><tr><td>Short USD/CNH</td><td>6.6</td><td>end-Aug</td><td>4</td><td>8-May-26</td></tr><tr><td>Long 12m USD/HKD</td><td>7.8</td><td>12-May-27</td><td>3</td><td>08-May-26</td></tr><tr><td>Long CNH vs 6FX abridged basket</td><td>-</td><td>-</td><td>2</td><td>8-May-26</td></tr><tr><td>Long CHF/JPY</td><td>206.5</td><td>end-Jun</td><td>4</td><td>30-Apr-26</td></tr><tr><td>Long EUR/SEK</td><td>-</td><td>-</td><td>2</td><td>17-Apr-26</td></tr><tr><td>Pay Jun-3y China NDIRS</td><td>15bp gain</td><td>end-Jun</td><td>3</td><td>14-Apr-26</td></tr><tr><td>Receive Jun-IMM 5y THOR (50% vs. US)</td><td>20bp gain</td><td>end-Jun</td><td>3</td><td>08-Apr-26</td></tr><tr><td>Long EUR/INR</td><td>113</td><td>end-Aug</td><td>3</td><td>01-Apr-26</td></tr><tr><td>Pay Jun-IMM 10y HK IRS</td><td>50bp gain</td><td>end-Jun</td><td>3</td><td>6-Mar-26</td></tr><tr><td>Long USD/THB</td><td>-</td><td>-</td><td>1</td><td>02-Feb-26</td></tr><tr><td>Long 9m USD/HKD</td><td>7.8</td><td>27-Oct-26</td><td>3</td><td>23-Jan-26</td></tr><tr><td>Long 12m USD/HKD</td><td>7.8</td><td>27-Jan-27</td><td>3</td><td>23-Jan-26</td></tr><tr><td>Long SGD/IDR</td><td>14,200</td><td>end-Aug</td><td>4</td><td>9-Jan-26</td></tr><tr><td>Long EUR/GBP</td><td>0.8950</td><td>end-Jun</td><td>3</td><td>9-Jan-26</td></tr></table>

Source: NOM

Please see FX Insights - Strategy portfolio update (7 May 2026) for our full portfolio.

# Appendix A-1

This report has been produced by NOM International plc (NIplc), UK.

See Disclaimers for NOM Group entity details.

# Analyst Certification

We, Yusuke Miyairi and Dominic Bunning, hereby certify (1) that the views expressed in this Research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of our compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

# Important Disclosures

# Online availability of research and conflict-of-interest disclosures

NOM Group research is available on www.NOMnow.com/research, Bloomberg, Capital IQ, Factset, LSEG.

Important disclosures may be read at http://go.NOMnow.com/research/m/Disclosures or requested from NOM Securities International, Inc. If you have any difficulties with the website, please email grpsupport@NOM.com for help.

The analysts responsible for preparing this report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by Investment Banking activities. Unless otherwise noted, the non-US analysts listed at the front of this report are not registered/qualified as research analysts under FINRA rules, may not be associated persons of NSI, and may not be subject to FINRA Rule 2241 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

NOM Global Financial Products Inc. (NGFP) NOM Derivative Products Inc. (NDP) and NOM International plc. (NIplc) are registered with the Commodities Futures Trading Commission and the National Futures Association (NFA) as swap dealers. NGFP, NDPI, and NIplc are generally engaged in the trading of swaps and other derivative products, any of which may be the subject of this report.

# ADDITIONAL DISCLOSURES REQUIRED IN THE U.S.

Principal Trading: NOM Securities International, Inc and its affiliates will usually trade as principal in the fixed income securities (or in related derivatives) that are the subject of this research report. Analyst Interactions with other NOM Securities International, Inc. Personnel: The fixed income research analysts of NOM Securities International, Inc and its affiliates regularly interact with sales and trading desk personnel in connection with obtaining liquidity and pricing information for their respective coverage universe.

# Valuation methodology - Fixed Income

NOM's Fixed Income Strategists express views on the price of securities and financial markets by providing trade recommendations. These can be relative value recommendations, directional trade recommendations, asset allocation recommendations, or a mixture of all three.

The analysis which is embedded in a trade recommendation would include, but not be limited to:

\- Fundamental analysis regarding whether a security's price deviates from its underlying macro- or micro-economic fundamentals.

• Quantitative analysis of price variations.

\- Technical factors such as regulatory changes, changes to risk appetite in the market, unexpected rating actions, primary market activity and supply/ demand considerations.

The timeframe for a trade recommendation is variable. Tactical ideas have a short timeframe, typically less than three months. Strategic trade ideas have a longer timeframe of typically more than three months.

For the purposes of the EU Market Abuse Regulation, the distribution of ratings published by NOM Global Fixed Income Research is as follows:

52% have been assigned a Buy (or equivalent) rating; 50% of issuers with this rating were supplied material services\* by the NOM Group\*\*.
0% have been assigned a Neutral (or equivalent) rating.

48% have been assigned a Sell (or equivalent) rating; 50% of issuers with this rating were supplied material services by the NOM Group. As at 31 Mar 2026.

\*As defined by the EU Market Abuse Regulation

\*\*The NOM Group as defined in the Disclaimer section at the end of this report

# Disclaimers

This publication contains material that has been prepared by the NOM Group entity identified on page 1 and, if applicable, with the contributions of one or more NOM Group entities whose employees and their respective affiliations are specified on page 1 or identified elsewhere in this publication. The term "NOM Group" used herein refers to NOM Holdings, Inc. and its affiliates and subsidiaries including: (a) NOM Securities Co., Ltd. ('NSC') Tokyo, Japan, (b) NOM Financial Products Europe GmbH ('NFPE'), Germany, (c) NOM International plc ('NIplc'), UK, (d) NOM Securities International, Inc. ('NSI'), New York, US, (e) NOM International (Hong Kong) Ltd.

('NIHK'), Hong Kong, (f) NOM Financial Investment (Korea) Co., Ltd. ('NFIK'), Korea (Information on NOM analysts registered with the Korea Financial Investment Association ('KOFIA') can be found on the KOFIA Intranet at http://dis.kofia.or.kr, (g) NOM Singapore Ltd. ('NSL'), Singapore (Registration number 197201440E, regulated by the Monetary Authority of Singapore) (h) NOM Australia Ltd. ('NAL'), Australia (ABN 48 003 032 513), regulated by the Australian Securities and Investment Commission ('ASIC') and holder of an Australian financial services licence number 246412, (i) NOM Securities Malaysia Sdn. Bhd. ('NSM'), Malaysia, (j) NIHK, Taipei Branch ('NITB'), Taiwan, (k) NOM Financial Advisory and Securities (India) Private Limited ('NFASL'), Mumbai, India (Registered Address: Ceejay House, Level 11, Plot F, Shivsagar Estate, Dr. Annie Besant Road, Worli, Mumbai- 400 018, India; Tel: 91 22 4037 4037, Fax: 91 22 4037 4111; CIN No: U74140MH2007PTC169116, SEBI Registration No. for Stock Broking activities : INZ000255633; SEBI Registration No. for Merchant Banking : INM000011419; SEBI Registration No. for Research: INH000001014 - Compliance Officer: Ms. Pratiksha Tondwalkar, 91 22 40374904, grievance email: investorgrievancesra@NOM.com Webpage: LINK

For reports with respect to Indian public companies or authored by India-based NFASL research analysts: (i) Investment in securities markets is subject to market risks. Read all the related documents carefully before investing. (ii) Registration granted by SEBI, and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. (iii) NFASL terms and conditions for availing research services is disclosed on NFASL webpage.

(I) NOM Fiduciary Research & Consulting Co., Ltd. ('NFRC') Tokyo, Japan. (m) NOM Orient International Securities Co., Ltd ("NOI"), is a majority owned joint venture amongst NOM Group, Orient International (Holding) Co., Ltd, and Shanghai Huangpu Investment Holding (Group) Co., Ltd. In accordance with the laws of the People's Republic of China ("PRC", excluding Hong Kong, Macau and Taiwan, for the purpose of this document), NOI is licensed in the PRC to provide securities research and investment recommendations and it operates independently from the other members of the NOM Group; in particular, NOI's interests in PRC securities are not disclosed to, or aggregated with the holdings of, any other NOM Group entities and the interests in PRC securities of other NOM Group entities are not disclosed to, or aggregated with the holdings of, NOI. An individual name printed next to NOI on the front page of a research report indicates that individual is employed by NOI to provide research assistance to NIHK under a research partnership agreement. 'NSFSPL' next to an employee's name on the front page of a research report indicates that the individual is employed by NOM Structured Finance Services Private Limited to provide assistance to certain NOM entities under inter-company agreements. 'Verdhana' next to an individual's name on the front page of a research report indicates that the individual is employed by PT Verdhana Sekuritas Indonesia ('Verdhana') to provide research assistance to NIHK under a research partnership agreement and neither Verdhana nor such individual is licensed outside of Indonesia.

THIS MATERIAL IS: (I) FOR YOUR PRIVATE INFORMATION, AND WE ARE NOT SOLICITING ANY ACTION BASED UPON IT; (II) NOT TO BE CONSTRUED AS AN OFFER TO SELL OR A SOLICITATION OF AN OFFER TO BUY ANY SECURITIES IN ANY JURISDICTION WHERE SUCH OFFER OR SOLICITATION WOULD BE ILLEGAL; AND (III) OTHER THAN DISCLOSURES RELATING TO THE NOM GROUP, BASED UPON INFORMATION FROM SOURCES THAT WE CONSIDER REL

[中间内容因长度限制已省略]

DVISER REGARDING THE SUITABILITY OF THE INVESTMENT, UNDER A SEPARATE ENGAGEMENT, AS THE RECIPIENT DEEMS FIT. Unless prohibited by the provisions of Regulation S of the 1933 Act, this material is distributed in the US, by NSI, a US-registered broker-dealer, which accepts responsibility for its contents in accordance with the provisions of Rule 15a-6, under the US Securities Exchange Act of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia (‘Saudi Arabia’) or a ‘Market Counterparty’ or a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International plc, UK. All rights reserved.
"""
