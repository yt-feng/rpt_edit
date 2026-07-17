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
# Asia Insights

Economics - Asia ex-Japan

## China: Sectoral breakdown of Q2 GDP

The sectoral breakdown of GDP reinforces our view of a K-shaped economy, especially in nominal terms. Nominal GDP growth of both manufacturing and financial services sectors reached nearly 9.0% y-o-y in Q2, while property and construction sectors remained in an acute contraction. The higher nominal growth rate was entirely driven by price effects, while real GDP growth slowed broadly across sectors, even the manufacturing sector. Moreover, despite surging stock trading, we are skeptical of the high growth in the financial services sector, given the significant decline in brokerage commission rates, the sharp credit growth slowdown, and worsening bank profit margins. On the demand side, despite the steep FAI contraction, the growth contribution of capital formation only edged down to 1.5pp y-o-y in Q2 from 1.9pp in Q1, rekindling concerns over the quality of investment data quality. The Q2 growth slowdown reinforces our view that both markets and policymakers in Beijing cannot assume the new AI economy will cure China's economic woes. We expect a new round of supportive measures to be announced at the mid-year Politburo meeting, although at a moderate scale.

## A significant divide between nominal and real GDP growth in manufacturing

Real GDP growth in the manufacturing sector slowed sharply to 4.8% y-o-y in Q2, its lowest since Q4 2023 and down notably from 6.3% in Q1. In sharp contrast, nominal GDP growth in the manufacturing sector increased to 8.8% y-o-y in Q2, the highest reading since Q1 2022 and up from 6.2% in Q1, due mainly to a jump in its deflator to 1.4% y-o-y from -0.1%. This striking divergence was a result of supply disruptions to oil-related sectors and surging prices of oil and chips. The sharp slowdown in real manufacturing growth took place when nominal export growth in USD terms increased to 20.2% y-o-y in Q2 from 14.7% in Q1, suggesting the strength of exports was largely driven by price effects.

## Buoyant stock trading continues to boost the financial services sector

Real growth in the financial services sector advanced further to 6.9% y-o-y in Q2, reaching another new high since Q1 2016 and up from 6.5% in Q1. Thanks to a positive deflator, nominal growth in the financial sector increased markedly to 8.9% y-o-y in Q2 from 7.5% in Q1. The financial services sector accounts for 8% of GDP, with its contribution to Q2's nominal GDP growth at 0.66pp y-o-y, making it the second largest growth contributor.

Although the surge in stock trading seems to have been a major factor behind the strong growth in the financial services sector, we see two reasons why the actual boost could be much smaller. First, the average brokerage commission rate for the stock trading has dropped notably from around $0.08\%$ in 2014 to around $0.02\%$ today, amid the broadening price war. Second, the rising share of high-frequency trading could lead to more discounts on commissions. Moreover, China's financial system is still dominated by the banking sector. The higher GDP growth in the financial services sector appears inconsistent with the notable slowdown in credit growth and worsening bank profit margins.

\- On stock trading, the daily average stock trading volume surged to a new high of RMB2.9trn in Q2 from RMB2.6trn in Q1, with its year-on-year growth surging to 132.3% y-o-y from 67.9%. The ratio of stock trading volumes over GDP advanced to 4.8X in Q2 from 4.3X in Q1, marking the second highest ratio on record and approaching the peak of 5.7% in Q2 2015.

\- On credit growth, growth of aggregate financing and RMB loans dropped to 7.4% y-o-y and 5.2%, respectively, at end-Q2 from 7.9% and 5.7% at end-Q1.

\- On bank profitability, according to the latest data from the National Financial Regulatory Administration (NFRA), the weighted average NIM of commercial banks dipped to a new low of 1.40% in Q1 2026 from 1.42% in Q4 2025. We expect bank profitability to remain under pressure in Q2 2026.

## Research Analysts

Jing Wang - NIHK
jing.wang@NOM.com
+852 2252 1011

hannah.liu@NOM.com +852 2252 1082

Ting Lu - NIHK
ting.lu@NOM.com
+852 2252 1306

## The contraction in property and construction sectors deepened again

Real GDP growth in the construction sector worsened to -4.1% y-o-y in Q2 from -3.8% in Q1, while growth in the property sector edged down to -0.2% from -0.1%. As property-related construction activity comprises part of the construction sector, we combine construction and property sectors to assess the impact of the property fallout. Specifically, their combined real GDP growth rate was -2.3% y-o-y in Q2, worsening from -1.6% in Q1. Nevertheless, we believe the actual deterioration might be much more acute than the GDP numbers suggest. According to monthly data from the NBS, new home sales (by floor space), new home starts and new home completions remained in deep contractionary territory, at -12.7% y-o-y, -25.7% and -21.9%, respectively, in Q2, compared with their Q1 growth rates of -10.4%, -20.3% and -25.0%.

In the meantime, the combined nominal GDP growth of construction and property sectors was -2.3% y-o-y in Q2, up from -4.2% in Q1. By contrast, FAI growth of infrastructure and property investment slumped to -8.6% y-o-y and -23.0%, respectively, in Q2 from 9.2% and -11.2% in Q1. This stark difference calls into question the quality of the investment data.

Fig. 1: Financial sector grew at fastest pace in a decade  
![](images/9864c0bbee59b5ae2b36e7348ad441d6fda53b9c7686be28837c3185f069cf0f.jpg)  
Source: NBS, Wind, NOM Global Economics.

Fig. 2: GDP deflator broadly turned positive  
![](images/872723d9aa773b5e741f3b8ebff4f06822e9b5544d3383f97adb1cf258eafb08.jpg)  
Source: NBS, Wind, NOM Global Economics

## Goods consumption fared worse than services consumption

Real growth in the wholesale & retail sales sector dropped to 3.3% y-o-y in Q2 from 4.1% in Q1, dragged down by payback effects from the scaled-back trade-in program, as well as weak consumer sentiment amid the perennial property crisis, despite the decent stock market performance alongside the AI boom.

Nominal growth in the wholesale & retail sales sector moderated to 4.9% y-o-y in Q2 from 5.0% in Q1. The monthly data from the NBS pointed to even weaker growth, as average monthly merchandise retail sales growth only slowed to 0.0% y-o-y in Q2 from 2.2% in Q1. In view of limited policy space for short-term stimulus, we revised down our H2 retail sales growth forecast to 3.0% y-o-y from 3.6%, with our full-year forecast lowered to 2.2% from 3.2%. As such, we expect the wholesale and retail sales sectors to remain a drag on overall economic growth.

Real growth in the hospitality and catering sector improved to 5.1% y-o-y in Q2 from 4.3% in Q1, and its nominal growth increased to 6.7% from 5.7%. This appears to contradict the retail sales value growth of catering services reported by the NBS, which showed nominal growth of catering services dropped markedly to 1.3% y-o-y in Q2 from 4.2% in Q1. Moreover, retail sales value growth of overall services fell to 5.3% y-o-y ytd in June from 5.5% in March. Despite the discrepancy between supply-side sector growth and monthly retail sales data, we believe services consumption has fared better than goods consumption this year (see China: Retail sales revisited, 2 July 2026).

Overall, consumption-related sectors should remain a drag on overall GDP growth, as the share of the hospitality and catering sector in overall GDP (4.6%) is much smaller than the wholesale and retail sales sector (10.3%).

## Logistics sector growth rose on booming exports

Real growth in the transport, storage and postal sector increased to 5.1% y-o-y in Q2 from 4.3% in Q1, and its nominal growth also rose to 7.3% from 5.7%. This was likely driven by both surging exports and rising transport fuel prices. Export growth jumped to 20.2% y-o-y in USD terms in Q2 from 17.3% in Q1. With crude oil price inflation jumping to 55.3% y-o-y in Q2 from 7.5% in Q1, transport fees likely also surged notably. On the other hand, real activity in domestic e-commerce and postal services likely remained subdued amid weak domestic demand conditions.

## Growth rates across IT- and leasing-related services remain high

Among all sub-sectors, real growth in IT and related services registered the second-highest reading at 10.8% y-o-y in Q2, largely unchanged from 10.6% in Q1. This elevated growth rate was likely underpinned by strong AI-related computing and software demand. Nominal growth in IT and related services rose to 10.5% y-o-y in Q2 from 10.3% in Q1, with the improvement likely driven by surging prices of tech-related products amid rising chip prices. The strongest sectoral growth was posted by leasing and business services, which encompasses leasing of machinery equipment, advertising, consulting and legal services. Real and nominal growth in this sector moderated only slightly to 11.6% y-o-y and 12.6%, respectively, in Q2 from 12.2% and 13.1% in Q1.

## Most sectors recorded positive GDP deflators

The overall GDP deflator turned positive for the first time since Q1 2023, rising markedly to 1.6% y-o-y in Q2 from -0.1% in Q1. The sectoral breakdown data suggest positive deflators were reported for the sectors of manufacturing (4.0%), transport, storage & post (2.2%), financial services (2.0%), leasing services (1.0%), hospitality & catering (0.9%), wholesale & retail sales (0.6%), and property (0.6%), while negative deflators were recorded for sectors of IT services (-0.3%), construction (-0.5%) and agriculture (-3.0%). We believe the positive GDP deflator was mainly driven by external forces, especially higher prices of oil and chips, rather than domestic demand. The negative deflator for the construction sector reflects still-weakening construction demand, as the property downturn drags on.

Fig. 3: Sectoral growth breakdown: real GDP  
![](images/da04b44d5855fdb7a71677bf13f0743024476cc65496d1477740f4b6c1f3b978.jpg)  
Note: The “other services” sector includes seven industries: scientific research & technical services; water, environment & public facility services; household services, repairs & other services; education; medical care & social work; culture, sports & recreation; and public management, social security & social organization.
Source: Wind, NOM Global Economics.

Fig. 4: Sectoral growth breakdown: nominal GDP  
![](images/ca88cab7065592e63fd2ea4f76fe088f109fec0e2d2470f74d6f0c5c5d72c9b0.jpg)  
Source: Wind, NOM Global Economics.

## Appendix A-1

This report has been produced by NOM International (Hong Kong) Ltd. (NIHK), Hong Kong. See Disclaimers for NOM Group entity details.

## Analyst Certification

We, Jing Wang, Hannah Liu and Ting Lu, hereby certify (1) that the views expressed in this Research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of our compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

## Important Disclosures

## Online availability of research and conflict-of-interest disclosures

NOM Group research is available on www.NOMnow.com/research, Bloomberg, Capital IQ, Factset, LSEG.

Important disclosures may be read at http://go.NOMnow.com/research/m/Disclosures or requested from NOM Securities International, Inc. If you have any difficulties with the website, please email grpsupport@NOM.com for help.

The analysts responsible for preparing this report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by Investment Banking activities. Unless otherwise noted, the non-US analysts listed at the front of this report are not registered/qualified as research analysts under FINRA rules, may not be associated persons of NSI, and may not be subject to FINRA Rule 2241 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

NOM Global Financial Products Inc. (NGFP) NOM Derivative Products Inc. (NDP) and NOM International plc. (NIplc) are registered with the Commodities Futures Trading Commission and the National Futures Association (NFA) as swap dealers. NGFP, NDPI, and NIplc are generally engaged in the trading of swaps and other derivative products, any of which may be the subject of this report.

## Disclaimers

This publication contains material that has been prepared by the NOM Group entity identified on page 1 and, if applicable, with the contributions of one or more NOM Group entities whose employees and their respective affiliations are specified on page 1 or identified elsewhere in this publication. The term "NOM Group" used herein refers to NOM Holdings, Inc. and its affiliates and subsidiaries including: (a) NOM Securities Co., Ltd. ('NSC') Tokyo, Japan, (b) NOM Financial Products Europe GmbH ('NFPE'), Germany, (c) NOM International plc ('NIplc'), UK, (d) NOM Securities International, Inc. ('NSI'), New York, US, (e) NOM International (Hong Kong) Ltd. ('NIHK'), Hong Kong, (f) NOM Financial Investment (Korea) Co., Ltd. ('NFIK'), Korea (Information on NOM analysts registered with the Korea Financial Investment Association ('KOFIA') can be found on the KOFIA Intranet at http://dis.kofia.or.kr, (g) NOM Singapore Ltd. ('NSL'), Singapore (Registration number 197201440E, regulated by the Monetary Authority of Singapore) (h) NOM Australia Ltd. ('NAL'), Australia (ABN 48 003 032 513), regulated by the Australian Securities and Investment Commission ('ASIC') and holder of an Australian financial services licence number 246412, (i) NOM Securities Malaysia Sdn. Bhd. ('NSM'), Malaysia, (j) NIHK, Taipei Branch ('NITB'), Taiwan, (k) NOM Financial Advisory and Securities (India) Private Limited ('NFASL'), Mumbai, India (Registered Address: Ceejay House, Level 11, Plot F, Shivsagar Estate, Dr. Annie Besant Road, Worli, Mumbai- 400 018, India; Tel: 91 22 4037 4037, Fax: 91 22 4037 4111; CIN No: U74140MH2007PTC169116, SEBI Registration No. for Stock Broking activities : INZ000255633; SEBI Registration No. for Merchant Banking : INM000011419; SEBI Registration No. for Research: INH000001014 - Compliance Officer: Ms. Pratiksha Tondwalkar, 91 22 40374904, grievance email: investorgrievancesra@NOM.com Webpage: LINK

For reports with respect to Indian public companies or authored by India-based NFASL research analysts: (i) Investment in securities markets is subject to market risks. Read all the related documents carefully before investing. (ii) Registration granted by SEBI, and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. (iii) NFASL terms and conditions for availing research services is disclosed on NFASL webpage.

(I) NOM Fiduciary Research & Consulting Co., Ltd. ('NFRC') Tokyo, Japan. (m) NOM Orient International Securities Co., Ltd ("NOI"), is a majority owned joint venture amongst NOM Group, Orient International (Holding) Co., Ltd, and Shanghai Huangpu Investment Holding (Group) Co., Ltd. In accordance with the laws of the People's Republic of China ("PRC", excluding Hong Kong, Macau and Taiwan, for the purpose of this document), NOI is licensed in the PRC to provide securities research and investment recommendations and it operates independently from the other members of the NOM Group; in particular, NOI's interests in PRC securities are not disclosed to, or aggregated with the holdings of, any other NOM Group entities and the interests in PRC securities of other NOM Group entities are not disclosed to, or aggregated with the holdings of, NOI. An individual name printed next to NOI on the front page of a research report indicates that individual is employed by NOI to provide research assistance to NIHK under a research partnership agreement. 'NSFSPL' next to an employee's name on the front page of a research report indicates that the individual is employed by NOM Structured Finance Services Private Limited to provide assistance to certain NOM entities under inter-company agreements. 'Verdhana' next to an individual's name on the front page of a research report indicates that the individual is employed by PT Verdhana Sekuritas Indonesia ('Verdhana') to provide research assistance to NIHK under a research partnership agreement and neither Verdhana nor such individual is licensed outside of Indonesia.

THIS MATERIAL IS: (I) FOR YOUR PRIVATE INFORMATION, AND WE ARE NOT SOLICITING ANY ACTION BASED UPON IT; (II) NOT TO BE CONSTRUED AS AN OFFER TO SELL OR A SOLICITATION OF AN OFFER TO BUY ANY SECURITIES IN ANY JURISDICTION WHERE SUCH OFFER OR SOLICITATION WOULD BE ILLEGAL; AND (III) OTHER THAN DISCLOSURES RELATING TO THE NOM GROUP, BASED UPON INFORMATION FROM SOURCES THAT WE CONSIDER RELIABLE, BUT HAS NOT BEEN INDEPENDENTLY VERIFIED BY NOM GROUP.

Other than disclosures relating to the NOM Group, the NOM Group does not warrant, represent or undertake, express or implied, that the document is fair, accurate, complete, correct, reliable or fit for any particular purpose or merchantable, and to the maximum extent permissible by law and/or regulation, does not accept liability (in negligence or otherwise, and in whole or in part) for any act (or decision not to act) resulting from use of this document and related data. To the maximum extent permissible by law and/or regulation, all warranties and other assurances by the NOM Group are hereby excluded and the NOM Group shall have no liability (in negligence or otherwise, and in whole or in part) for any loss howsoever arising from the use, misuse, or distribution of this material or the information contained in this material or otherwise arising in connection therewith.

Opinions or estimates expressed are current opinions as of the original publication date appearing on this material and the information, including the opinions and estimates contained herein, are subject to change without notice. The NOM Group, however, expressly disclaims any obligation, and therefore is under no duty, to update or revise this document. Any comments or statements made herein are those of the author(s) and may di

[中间内容因长度限制已省略]

34. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia (‘Saudi Arabia’) or a ‘Market Counterparty’ or a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, "Offshore Issuers") that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

## NOM Securities Co., Ltd.

Financial instruments firm registered with the Kanto Local Finance Bureau (registration No. 142)

Member associations: Japan Securities Dealers Association; Investment Management Association of Japan; The Financial Futures Association of Japan; Type II Financial Instruments Firms Association; and Japan Security Token Offering Association.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
