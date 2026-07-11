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
EQUITY: TECHNOLOGY

# Net catch: China's original route to rocket reuse

First-stage recovery success is a cost inflection; watch for refly cadence, per-kg cost, and constellation orders

LM-10B first stage recovered at sea; first net-system catch

On 10 July 2026, China Aerospace Science and Technology Corporation (CASC) (unlisted) announced that the Long March 10B (LM-10B) rocket lifted off from the Hainan commercial launch site, and around six minutes after first- and second-stage separation, the first stage executed a vertical return and was successfully recovered at sea. This is China's first controlled recovery of an orbital launcher's first stage and the first net-system rocket recovery. The catch was performed by "Navigator", a purpose-built 25,000-tonne recovery vessel. We view the mission as a critical inflection point for the industry. Technologically, China's recoverable rockets now move from trial validation to engineering application, making China the second country after the US to master the technology. On cost, we expect total per-launch cost to fall substantially, potentially converging toward SpaceX's (SPCX US, Not rated) Falcon 9 unit economics — at USD2,500-3,500/kg based on our industry survey — as reuse scales. On the industry side, the recovery success should accelerate the two constellation projects (Guowang and Qianfan) roll-out, ease the launch-capacity bottleneck, and drive order growth across rockets, satellites and ground equipment.

## From landing legs to nets: mapping rocket recovery technology routes

Rocket recovery targets reuse of the first stage — which is roughly 60-65% of the total vehicle cost — to cut launch costs and lift cadence. Mainstream rocket recovery technology routes are: legged vertical landing on land or droneships (SpaceX's Falcon 9), parachute-and-splashdown (Rocket Lab [RKLB US, Not rated]), tower "chopstick" capture (Starship booster), and net-system capture, now pioneered by China. Net capture replaces landing legs — typically several tons of dead weight — with hooks on the airframe, reducing payload loss, while the vessel's mobility relaxes landing-precision requirements versus fixed towers. A downrange recovery along the flight path is preferred to return-to-launch-site given far smaller payload penalties. Siting is dictated by geography: inland sites force land recovery, coastal sites favor sea. A sea recovery is safer but a rolling deck challenges legged landings — a weakness net capture avoids, hence, we believe it is a more creative route. In China, vertical takeoff and landing (VTVL) trials began in 2019, and by 2025 CASC, LandSpace (unlisted), i-Space (unlisted), and peers had completed tests, moving the sector into engineering flight validation. In 2025, Long March 12A and LandSpace's Zhuque-3 made China's first engineering-level recovery attempts, and Long March 10A completed a controlled sea splashdown in February 2026.

## China closes recovery gap; high-cadence reliable reuse is next milestone

In our Global satellites – accelerated launch plans and broadened applications published in June 2026, we did a comparison of China's satellite development with US players. For rocket reuse, SpaceX remains the benchmark: its S-1 filing discloses \~620 Falcon 9 launches with >99% mission success and boosters reflown up to 34 times (qualification now extended to 40 flights). According to SpaceX and NSF, Falcon 9's \~4.2% payload fraction compares with 1.8-3.0% for global peers, and the new Raptor-3 delivers \~250t thrust per engine at \~1.5t weight (thrust-to-weight \~164) with 30MPa-plus chamber pressure versus \~10MPa typical of domestic engines. Our industry checks put China roughly 10 years behind — SpaceX landed boosters in 2015 (land) and 2016 (sea) — though views split: some see validated technical routes compressing the catch-up, others see the gap slightly widening given SpaceX's costlier, faster iteration. In addition, Starship's 12th flight achieved most of its primary test objectives (industry survey shows >95%), though booster recovery failed on re-ignition. SpaceX targets an orbital land

## Research Analysts

China Technology
Frank Fan - NIHK
frank.fan@NOM.com
+852 2252 2195

## Donnie Teng - NIHK

donnie.teng@NOM.com +852 2252 1439

Asia Technology

Anne Lee, CFA - NITB
anne.lee@NOM.com
+886(2) 21769966

Production Complete: 2026-07-10 14:24 UTC

recovery in 2027E, while the domestic second-stage recovery remains at the feasibility stage (i-Space trials \~2030E). Further, LM-10B's net-system route is an original Chinese path, shifting buffer structures from rocket to vessel. The remaining gap, in our view, is not single-mission recovery but high-cadence reliable reuse — a capability SpaceX only industrialised after 2020.

## Launch cost economics: booster reuse drives steepest cost curve

Reuse economics are best read at mission level. According to SpaceX, its Falcon 9 launch cost of \~USD2,700/kg compares with \~USD18,500/kg historically (based on the company's \~620 launches with boosters reflown up to 34 times). Our industry survey indicates that long-term cost economics could be even lower: all-in internal cost below USD10mn per Starlink mission — c.USD1,000/kg — split between an expendable second stage closer to USD5mn (the effective cost floor), \~USD1mn of landing and refurbishment, and a few hundred thousand dollars of propellant. Booster qualification has been extended from 10 to 40 flights, with 50-60 deemed feasible; which suggests an expendable Falcon 9 mission at \~USD67mn versus USD34-37mn on a high-reflight booster. By comparison, according to STCN, China's current pricing of \~CNY60,000/kg (\~USD8,400/kg) is roughly 3x Falcon 9's disclosed cost; LM-10B targets CNY20,000/kg (\~USD2,800/kg), with net recovery eliminating landing legs to lift payload by 10-15% and targeting \~72-hour turnaround over 10-plus reuses. Putting together, for the domestic cost curve: a 20t expendable rocket at CNY200mn (CNY10mn/t) falls to \~CNY120mn (CNY7.5mn/t) with first-stage reuse — the first stage being \~60% of the hardware cost — and to CNY70-80mn (\~CNY5.8mn/t) with full reuse. With expendable rockets priced within 10-20% of one another, we believe reusables' 30%-plus cost advantage should decide the 2027-29F shakeout in the industry; hence, per-kg economics, not recovery headlines, would be the arbiter, in our view.

In the China aerospace sector, we have a Buy rating on Sunway Communication (300136 CH) with a target price of CNY138, supported by likely acceleration in China's satellite deployment. We also maintain a Neutral rating on China Spacesat (600118 CH) with a target price of CNY80, as its business is likely to shift from satellite manufacturing, margin-compressed revenue based, to a high-value mix anchored by application, but offset by a high-valuation cap.

## Appendix A-1

This report has been produced by NOM International (Hong Kong) Ltd. (NIHK), Hong Kong. See Disclaimers for NOM Group entity details.

## Analyst Certification

We, Frank Fan, Donnie Teng and Anne Lee, hereby certify (1) that the views expressed in this Research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of our compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

## Issuer Specific Regulatory Disclosures

The terms "NOM" and "NOM Group" used herein refer to NOM Holdings, Inc. and its affiliates and subsidiaries, including NOM Securities International, Inc. ('NSI') and Instinet, LLC ('ILLC'), U. S. registered broker dealers and members of SIPC.

Materially mentioned issuers

<table><tr><td>Issuer</td><td>Ticker</td><td>Price</td><td>Price date</td><td>Stock rating</td><td>Sector rating</td><td>Disclosures</td></tr><tr><td>Shenzhen Sunway Communication</td><td>300136 CH</td><td>CNY 99.38</td><td>10-Jul-2026</td><td>Buy</td><td>N/A</td><td></td></tr><tr><td>China Spacesat Co.</td><td>600118 CH</td><td>CNY 90.02</td><td>10-Jul-2026</td><td>Neutral</td><td>N/A</td><td></td></tr></table>

Shenzhen Sunway Communication (300136 CH)  
CNY 99.38 (10-Jul-2026) Buy (Sector rating: N/A)  
![](images/6ca1402db3bd0194cf993d2407254023b3ba7a1510479b6d9885ae58c4063a97.jpg)  
Source: LSEG, NOM  
For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology Our TP of CNY138 is based on 86x 2028F P/E, +3.0x SD of its 9-years historical average P/E at 39x, which is supported by 1) its 2025-28F earnings CAGR at $29\%$ based on growth in satellite sector and product mix improvement, and 2) likely re-rating by shifting from a consumer electronics, margin-compressed revenue based toward a higher-value, more diversified mix anchored by satellite communication.

![](images/b095b52e31a28a80261d0e8c9f6ff7d978d9c7414123cec4f25d60b020bd3233.jpg)  
For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology Our TP of CNY80 is based on 10x 2028F P/S, +2.5x SD of its 10-years historical average P/S at 5x, which is supported by its 2025-28F sales CAGR at 16% and a growing total addressable market for satellite. Driven by the solid growth in LEO (Low Earth Orbit) satellite market, we expect the company is a direct beneficiary of accelerated deployment of constellation and overseas business expansion, and will likely lead to a valuation re-rating backed by growing demand and mix change anchored by constellation projects. The benchmark index is CSI300.

Risks that may impede the achievement of the target price Downside risks include: 1) downstream demand falling short of expectations; 2) slower-than-expected aerospace development due to technology progress, macroeconomic environment, and policy riskst; and 3) intensified competition in aerospace sector. Upside risks include: 1) accelerated mega-constellation roll-out; and 2) better-than-expected contributions from satellite applications.

## Important Disclosures

## Online availability of research and conflict-of-interest disclosures

NOM Group research is available on www.NOMnow.com/research, Bloomberg, Capital IQ, Factset, LSEG.

Important disclosures may be read at http://go.NOMnow.com/research/m/Disclosures or requested from NOM Securities International, Inc. If you have any difficulties with the website, please email grpsupport@NOM.com for help.

The analysts responsible for preparing this report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by Investment Banking activities. Unless otherwise noted, the non-US analysts listed at the front of this report are not registered/qualified as research analysts under FINRA rules, may not be associated persons of NSI, and may not be subject to FINRA Rule 2241 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

NOM Global Financial Products Inc. (NGFP) NOM Derivative Products Inc. (NDP) and NOM International plc. (NIplc) are registered with the Commodities Futures Trading Commission and the National Futures Association (NFA) as swap dealers. NGFP, NDPI, and NIplc are generally engaged in the trading of swaps and other derivative products, any of which may be the subject of this report.

## Distribution of ratings (NOM Group)

The distribution of all ratings published by NOM Group Global Equity Research is as follows:

58% have been assigned a Buy rating which, for purposes of mandatory disclosures, are classified as a Buy rating; 33% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services\*\* by the NOM Group.

39% have been assigned a Neutral rating which, for purposes of mandatory disclosures, is classified as a Hold rating; 57% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services by the NOM Group

3% have been assigned a Reduce rating which, for purposes of mandatory disclosures, are classified as a Sell rating; 15% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services by the NOM Group.

\*The NOM Group as defined in the Disclaimer section at the end of this report.

\*\* As defined by the EU Market Abuse Regulation

## Definition of NOM Group's equity research rating system and sectors

The rating system is a relative system, indicating expected performance against a specific benchmark identified for each individual stock, subject to limited management discretion. An analyst's target price is an assessment of the current intrinsic fair value of the stock based on an appropriate valuation methodology determined by the analyst. Valuation methodologies include, but are not limited to, discounted cash flow analysis, expected return on equity and multiple analysis. Analysts may also indicate expected absolute upside/downside relative to the stated target price, defined as (target price - current price)/current price.

## STOCKS

A rating of 'Buy', indicates that the analyst expects the stock to outperform the Benchmark over the next 12 months. A rating of 'Neutral', indicates that the analyst expects the stock to perform in line with the Benchmark over the next 12 months. A rating of 'Reduce', indicates that the analyst expects the stock to underperform the Benchmark over the next 12 months. A rating of 'Suspended', indicates that the rating, target price and estimates have been suspended temporarily to comply with applicable regulations and/or firm policies. Securities and/or companies that are labelled as 'Not rated' or shown as 'No rating' are not in regular research coverage. Investors should not expect continuing or additional information from NOM relating to such securities and/or companies. Benchmarks are as follows: United States/Europe/Asia ex-Japan: please see valuation methodologies for explanations of relevant benchmarks for stocks, which can be accessed at: http://go.NOMnow.com/research/m/Disclosures; Global Emerging Markets (ex-Asia): MSCI Emerging Markets ex-Asia, unless otherwise stated in the valuation methodology; Japan: Russell/NOM Large Cap.

## SECTORS

A 'Bullish' stance, indicates that the analyst expects the sector to outperform the Benchmark during the next 12 months. A 'Neutral' stance, indicates that the analyst expects the sector to perform in line with the Benchmark during the next 12 months. A 'Bearish' stance, indicates that the analyst expects the sector to underperform the Benchmark during the next 12 months. Sectors that are labelled as 'Not rated' or shown as 'N/A' are not assigned ratings. Benchmarks are as follows: United States: S&P 500; Europe: Dow Jones STOXX 600; Global Emerging Markets (ex-Asia): MSCI Emerging Markets ex-Asia. Japan/Asia ex-Japan: Sector ratings are not assigned.

## Target Price

A Target Price, if discussed, indicates the analyst's forecast for the share price with a 12-month time horizon, reflecting in part the analyst's estimates for the company's earnings. The achievement of any target price may be impeded by general market and macroeconomic trends, and by other risks related to the company or the market, and may not occur if the company's earnings differ from estimates.

## Disclaimers

This publication contains material that has been prepared by the NOM Group entity identified on page 1 and, if applicable, with the contributions of one or more NOM Group entities whose employees and their respective affiliations are specified on page 1 or identified elsewhere in this publication. The term "NOM Group" used herein refers to NOM Holdings, Inc. and its affiliates and subsidiaries including: (a) NOM Securities Co., Ltd. ('NSC') Tokyo, Japan, (b) NOM Financial Products Europe GmbH ('NFPE'), Germany, (c) NOM International plc ('NIplc'), UK, (d) NOM Securities International, Inc. ('NSI'), New York, US, (e) NOM International (Hong Kong) Ltd. ('NIHK'), Hong Kong, (f) NOM Financial Investment (Korea) Co., Ltd. ('NFIK'), Korea (Information on NOM analysts registered with the Korea Financial Investment Association ('KOFIA') can be found on the KOFIA Intranet at http://dis.kofia.or.kr, (g) NOM Singapore Ltd. ('NSL'), Singapore (Registration number 197201440E, regulated by the Monetary Authority of Singapore) (h) NOM Australia Ltd. ('NAL'), Australia (ABN 48 003 032 513), regulated by the Australian Securities and Investment Commission ('ASIC') and holder of an Australian financial services licence number 246412, (i) NOM Securities Malaysia Sdn. Bhd. ('NSM'), Malaysia, (j) NIHK, Taipei Branch ('NITB'), Taiwan, (k) NOM Financial Advisory and Securities (India) Private Limited ('NFASL'), Mumbai, India (Registered Address: Ceejay House, Level 11, Plot F, Shivsagar Estate, Dr. Annie Besant Road, Worli, Mumbai- 400 018, India; Tel: 91 22 4037 4037, Fax: 91 22 4037 4111; CIN No: U74140MH2007PTC169116, SEBI Registration No. for Stock Broking activities : INZ000255633; SEBI Registration No. for Merchant Banking : INM000011419; SEBI Registration No. for Research: INH000001014 - Compliance Officer: Ms. Pratiksha Tondwalkar, 91 22 40374904, grievance email: investorgrievancesra@NOM.com Webpage: LINK

For reports with respect to Indian public companies or authored by India-based NFASL research analysts: (i) Investment in securities markets is subject to market risks. Read all the related documents carefully before investing. (ii) Registration granted by SEBI, and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. (iii) NFASL terms and conditions for availing research services is disclosed on NFASL webpage.

(I) NOM Fiduciary Research & Consulting Co., Ltd. ('NFRC') Tokyo, Japan. (m) NOM Orient International Securities Co., Ltd ("NOI"), is a majority owned joint venture amongst NOM Group, Orient Internatio

[中间内容因长度限制已省略]

OM AN INDEPENDENT FINANCIAL ADVISER REGARDING THE SUITABILITY OF THE INVESTMENT, UNDER A SEPARATE ENGAGEMENT, AS THE RECIPIENT DEEMS FIT. Unless prohibited by the provisions of Regulation S of the 1933 Act, this material is distributed in the US, by NSI, a US-registered broker-dealer, which accepts responsibility for its contents in accordance with the provisions of Rule 15a-6, under the US Securities Exchange Act of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia ('Saudi Arabia') or a 'Market Counterparty' or a 'Professional Client' (as defined by the Dubai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than 'Authorised Persons', 'Exempt Persons' or 'Institutions' located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS. This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
